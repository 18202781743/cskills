#!/usr/bin/env python3
"""Reuse the encrypted OA credentials shared with uos-pms-bug-workflow-trigger.

The module returns live OA/BI sessions in memory. Its CLI prints status only.
"""

import argparse
import getpass
import json
import os
from datetime import datetime
from pathlib import Path

import requests
from cryptography.fernet import Fernet, InvalidToken


OA_BASE = "https://oa.uniontech.com"
BI_BASE = "https://bi.uniontech.com"
FP_COOKIE = os.getenv("OA_FP_COOKIE", "f8ab66bf80759eee1d4be524945427ae")


def credential_dir(config_dir=None):
    if config_dir:
        return Path(config_dir).expanduser()
    override = os.getenv("UNIONTECH_OA_CONFIG_DIR")
    return Path(override).expanduser() if override else Path.home() / ".config" / "uniontech-oa"


def load_credentials(config_dir=None):
    """Return shared loginid/password or None; never create files on read."""
    directory = credential_dir(config_dir)
    key_file = directory / "key.bin"
    data_file = directory / "default.json"
    if not key_file.is_file() or not data_file.is_file():
        return None
    try:
        data = json.loads(data_file.read_text(encoding="utf-8"))
        password = Fernet(key_file.read_bytes()).decrypt(data["password_encrypted"].encode()).decode()
        loginid = str(data["loginid"]).strip()
        return (loginid, password) if loginid and password else None
    except (KeyError, ValueError, OSError, InvalidToken):
        return None


def save_credentials(loginid, password, config_dir=None):
    """Store successful credentials in the PMS-compatible Fernet format."""
    directory = credential_dir(config_dir)
    directory.mkdir(mode=0o700, parents=True, exist_ok=True)
    key_file = directory / "key.bin"
    if key_file.exists():
        key = key_file.read_bytes()
    else:
        key = Fernet.generate_key()
        key_file.write_bytes(key)
        key_file.chmod(0o600)
    data = {
        "loginid": loginid,
        "password_encrypted": Fernet(key).encrypt(password.encode()).decode(),
        "saved_at": datetime.now().isoformat(),
        "metadata": {},
    }
    data_file = directory / "default.json"
    data_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    data_file.chmod(0o600)


def authenticate(loginid, password, session=None):
    """Create fresh OA cookies, then exchange OA identity for a BI token."""
    client = session or requests.Session()
    if session is None:
        client.trust_env = False  # The machine's generic HTTPS proxy breaks internal OA TLS.
        proxy = os.getenv("AI_UT_PROXY", "").strip()
        if proxy:
            client.proxies.update({"http": proxy, "https": proxy})
    client.cookies.set("fp", FP_COOKIE, domain="oa.uniontech.com")
    response = client.post(
        f"{OA_BASE}/api/hrm/login/checkLogin",
        data={"loginid": loginid, "userpassword": password},
        headers={"X-Requested-With": "XMLHttpRequest"},
        timeout=30,
    )
    response.raise_for_status()
    if "loginidweaver" not in client.cookies:
        raise RuntimeError("OA 登录未建立会话")

    account = client.get(f"{OA_BASE}/api/portal/account/getAccount", timeout=30)
    account.raise_for_status()
    user = account.json().get("data")
    if not isinstance(user, dict) or not user.get("userid"):
        raise RuntimeError("OA 会话验证失败")

    redirect = client.get(
        f"{OA_BASE}/api/uniontech/marketbudget/getUserRedirectBi",
        params={"flags": "1"}, timeout=30,
    )
    redirect.raise_for_status()
    encrypted_name = redirect.text.strip().strip('"')
    if len(encrypted_name) < 10:
        raise RuntimeError("无法从 OA 获取 BI 登录参数")
    bi = client.post(
        f"{BI_BASE}/oa-bi/sys/workHourUser",
        json={"loginName": encrypted_name},
        headers={"Origin": OA_BASE, "Referer": f"{OA_BASE}/"},
        timeout=30,
    )
    bi.raise_for_status()
    body = bi.json()
    token = body.get("token") if body.get("code") == 0 else None
    if not token:
        raise RuntimeError("BI 登录未返回有效 token")
    return client, token, user


def authenticate_shared(config_dir=None):
    credentials = load_credentials(config_dir)
    if not credentials:
        raise RuntimeError("共享 OA 凭据不存在或无法解密")
    return authenticate(*credentials)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("check", "setup"))
    parser.add_argument("--config-dir", help="共享 OA 凭据目录；默认遵循 UNIONTECH_OA_CONFIG_DIR")
    args = parser.parse_args()
    try:
        if args.action == "setup":
            old = load_credentials(args.config_dir)
            loginid = input("OA/LDAP loginid: ").strip() or (old[0] if old else "")
            password = getpass.getpass("OA/LDAP password: ")
            if not loginid or not password:
                raise RuntimeError("未提供账号或密码")
            authenticate(loginid, password)
            save_credentials(loginid, password, args.config_dir)
        else:
            authenticate_shared(args.config_dir)
        print(json.dumps({"oa": "ok", "bi": "ok", "credential_source": "shared_store"}, ensure_ascii=False))
    except (RuntimeError, requests.RequestException) as error:
        print(json.dumps({"oa": "unavailable", "bi": "unavailable", "reason": type(error).__name__}, ensure_ascii=False))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
