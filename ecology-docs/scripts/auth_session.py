#!/usr/bin/env python3
"""Authentication, encrypted credentials, and reusable ecology sessions."""
import argparse
import getpass
import base64
import http.cookiejar
import json
import os
from io import BytesIO
from pathlib import Path
import re
import sys
import subprocess
import shutil
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlencode, urlsplit, urljoin, unquote
from urllib.request import build_opener, HTTPCookieProcessor, HTTPRedirectHandler, Request

ORIGIN = "https://ecology.chinauos.com"
PROVIDER = "https://login-platform.uniontech.com"
ADMIN = ORIGIN + "/identification/doc_admin/"
CALLBACK_PATH = "/adaptidentification/uos/develop/callbackdoc"
# 内置兜底注册参数；正常情况下从后台页面的登录链接解析（见 login_endpoint），失败才用它。
FALLBACK_PARAMS = {"access_type": "offline", "client_id": "f92a36f237733b6c2aef5423efbf2a045a5131b7",
                   "redirect_uri": ORIGIN + CALLBACK_PATH,
                   "response_type": "code", "scope": "base,user:read,certify:edit"}
FALLBACK_LOGIN = PROVIDER + "/login?" + urlencode({**FALLBACK_PARAMS, "state": ADMIN})
DEFAULT_STATE = Path(os.environ.get("XDG_STATE_HOME", str(Path.home() / ".local/state"))) / "ecology-docs"


class AuthError(RuntimeError):
    pass


class CaptchaError(AuthError):
    """验证码被拒绝；换一张新验证码即可重试。"""


def trusted(url):
    parsed = urlsplit(url)
    if parsed.scheme != "https" or parsed.netloc not in ("login-platform.uniontech.com", "ecology.chinauos.com"):
        raise AuthError("登录流程返回了非预期地址，已停止")
    return url


def build_login_url(params):
    """拼接登录入口；state 固定为后台地址，与页面 JS 用当前地址拼 state 的行为一致。"""
    return PROVIDER + "/login?" + urlencode({**params, "state": ADMIN})


def parse_login_params(page):
    """从后台页面解析本应用（回调必须是 CALLBACK_PATH）的 SSO 注册参数，找不到返回 None。"""
    for raw in re.findall(r"https://login-platform\.uniontech\.com/login\?[^\"'\s<>\\]+", page or ""):
        query = parse_qs(urlsplit(raw.replace("&amp;", "&")).query)
        client_id = (query.get("client_id") or [""])[0]
        redirect_uri = (query.get("redirect_uri") or [""])[0]
        if client_id and redirect_uri == ORIGIN + CALLBACK_PATH:
            return {"access_type": (query.get("access_type") or ["offline"])[0], "client_id": client_id,
                    "redirect_uri": redirect_uri, "response_type": (query.get("response_type") or ["code"])[0],
                    "scope": (query.get("scope") or ["base,user:read,certify:edit"])[0]}
    return None


DEFAULT_CONFIG = Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config"))) / "ecology-docs"


class CredentialError(AuthError):
    pass


def _cipher():
    try:
        from cryptography.fernet import Fernet
        return Fernet
    except ImportError:
        raise CredentialError("缺少系统 cryptography；不能加密保存凭据，不会回退到明文") from None


def _secret():
    try:
        import gi
        gi.require_version("Secret", "1")
        from gi.repository import Secret
        return Secret
    except Exception:
        raise CredentialError(f"当前 Python（{sys.executable}）缺少 PyGObject/Secret，无法访问系统密钥环；"
                              "请改用带 gi 的解释器，或在虚拟环境 pyvenv.cfg 中启用 include-system-site-packages") from None


def _key(config_dir, create=False):
    Secret = _secret()
    try:
        schema = Secret.Schema.new("com.uniontech.ecology-docs", Secret.SchemaFlags.NONE,
                                   {"config_path": Secret.SchemaAttributeType.STRING})
        attrs = {"config_path": str(Path(config_dir).expanduser().resolve())}
        key = Secret.password_lookup_sync(schema, attrs, None)
        if key is None and create:
            key = _cipher().generate_key().decode("ascii")
            if not Secret.password_store_sync(schema, attrs, Secret.COLLECTION_DEFAULT,
                                              "Ecology Docs credential encryption key", key, None):
                raise CredentialError("系统密钥环未保存解密密钥")
        if key is None:
            raise CredentialError("系统密钥环中没有解密密钥，请重新配置登录凭据")
        return key.encode("ascii")
    except CredentialError:
        raise
    except Exception:
        raise CredentialError("系统密钥环不可用或未解锁；不会把解密密钥或密码写入明文文件") from None


def store_credentials(config_dir, username, password):
    if not username.strip() or not password:
        raise CredentialError("用户名和密码不能为空")
    root = Path(config_dir).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True, mode=0o700)
    root.chmod(0o700)
    content = json.dumps({"username": username.strip(), "password": password}, ensure_ascii=False).encode()
    encrypted = _cipher()(_key(root, create=True)).encrypt(content)
    target = root / "credentials.enc"
    fd, name = tempfile.mkstemp(prefix=".credentials-", dir=root)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(encrypted)
        os.replace(name, target)
    finally:
        if os.path.exists(name):
            os.unlink(name)
    return {"credentials_saved": True, "file": str(target), "encrypted": True, "key_storage": "system-secret-service"}


def load_credentials(config_dir=DEFAULT_CONFIG):
    root = Path(config_dir).expanduser().resolve()
    try:
        encrypted = (root / "credentials.enc").read_bytes()
        plain = _cipher()(_key(root)).decrypt(encrypted)
        credentials = json.loads(plain)
        if not credentials.get("username") or not credentials.get("password"):
            raise CredentialError("加密凭据内容无效，请重新配置")
        return credentials
    except CredentialError:
        raise
    except Exception:
        raise CredentialError("加密凭据不存在或无法解密，请重新配置；不会读取旧明文密码") from None


class Redirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        trusted(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def private_write(path, content):
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=".login-")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(content)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


_OCR_ENGINES = {}


def _ocr_engine(beta):
    """按需加载并缓存 ddddocr 模型；缺少依赖时抛 RuntimeError。"""
    engine = _OCR_ENGINES.get(beta)
    if engine is None:
        try:
            import ddddocr
        except ImportError as exc:
            raise RuntimeError("缺少验证码识别依赖，请运行：python3 -m pip install ddddocr") from exc
        engine = ddddocr.DdddOcr(show_ad=False, beta=beta)
        _OCR_ENGINES[beta] = engine
    return engine


def classify_captcha(image_bytes, beta=False):
    """用 ddddocr 识别图片字节流中的 4 位数字/字母验证码。"""
    engine = _ocr_engine(beta)
    _verify_image(image_bytes)
    return _clean_result(engine.classification(image_bytes))


def _verify_image(image_bytes):
    """确认字节流是有效图片；缺少 Pillow 时抛 RuntimeError。"""
    try:
        from PIL import Image, UnidentifiedImageError
    except ImportError as exc:
        raise RuntimeError("缺少验证码识别依赖，请运行：python3 -m pip install ddddocr") from exc
    try:
        with Image.open(BytesIO(image_bytes)) as image:
            image.verify()
    except (UnidentifiedImageError, OSError, SyntaxError, ValueError) as exc:
        raise ValueError("验证码内容不是有效图片") from exc


def _clean_result(text):
    """只接受 4 位数字/英文字母，其余识别结果按失败处理。"""
    result = text.strip()
    if not re.fullmatch(r"[0-9A-Za-z]{4}", result):
        raise ValueError(f"未识别出 4 位数字或英文字母验证码，识别结果：{result!r}")
    return result


class AuthSession:
    def __init__(self, root, config_dir=DEFAULT_CONFIG):
        self.root = Path(root).expanduser().resolve()
        self.config_dir = Path(config_dir).expanduser().resolve()
        self.root.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.root.chmod(0o700)
        self.jar_file = self.root / ".http-login-cookies.txt"
        self.jar = http.cookiejar.LWPCookieJar(str(self.jar_file))
        self.opener = build_opener(HTTPCookieProcessor(self.jar), Redirect())
        self.login_url = None

    def login_endpoint(self):
        """登录入口：优先用后台页面里的链接，取不到则用内置参数；成功解析后缓存。"""
        if self.login_url is None:
            try:
                with self.open(ADMIN) as response:
                    params = parse_login_params(response.read().decode("utf-8", "replace"))
            except (HTTPError, URLError, OSError, ValueError):
                params = None
            if params:
                self.login_url = build_login_url(params)
        return self.login_url or FALLBACK_LOGIN

    def open(self, url, data=None, json_body=False):
        trusted(url)
        referer = self.login_endpoint() if url.startswith(PROVIDER) else ADMIN
        headers = {"User-Agent": "ecology-docs-http/1.0", "Referer": referer}
        if data is not None:
            headers["Content-Type"] = "application/json" if json_body else "application/x-www-form-urlencoded"
            data = json.dumps(data).encode() if json_body else urlencode(data).encode()
        return self.opener.open(Request(url, data=data, headers=headers), timeout=30)

    def captcha(self, open_image=False):
        with self.open(self.login_endpoint()) as response:
            response.read()
        with self.open(PROVIDER + "/captcha") as response:
            raw = response.read().decode()
        if raw.startswith('"'):
            raw = json.loads(raw)
        if not isinstance(raw, str) or not raw.startswith("data:image/") or ";base64," not in raw:
            raise AuthError("验证码响应格式不符合登录页面契约")
        image = base64.b64decode(raw.split(";base64,", 1)[1], validate=True)
        path = self.root / ("captcha-" + str(time.time_ns()) + ".png")
        private_write(path, image)
        private_write(self.jar_file, b"")
        self.jar.save(ignore_discard=True)
        recognized, recognition_error = None, None
        # 默认模型优先；结果不是 4 位数字/字母时再用 beta 模型复核一次。
        for beta in (False, True):
            try:
                recognized = classify_captcha(image, beta=beta)
                break
            except RuntimeError as exc:
                recognition_error = str(exc)
                break
            except ValueError as exc:
                recognition_error = str(exc)
        opened = False
        if recognized is None and open_image and shutil.which("xdg-open"):
            try:
                subprocess.Popen(["xdg-open", str(path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                opened = True
            except OSError:
                pass
        if recognized is not None:
            return {"status": "captcha_recognized", "captcha_required": True, "captcha": recognized,
                    "captcha_image": str(path), "image_viewer_requested": opened,
                    "next_action": "已自动识别验证码；login 会自行获取并提交，无需手动传入"}
        return {"status": "human_input_required", "captcha_required": True, "captcha_image": str(path),
                "image_viewer_requested": opened, "captcha_recognition_error": recognition_error,
                "next_action": "自动识别失败；请在真人终端重试 login 后按提示输入验证码"}

    def load_session(self):
        path = self.root / "session.json"
        return json.loads(path.read_text()) if path.exists() else {}

    def save_session(self, state):
        private_write(self.root / "session.json", json.dumps(state, ensure_ascii=False, indent=2).encode())

    def status(self):
        result = self.reuse()
        if result is None:
            raise AuthError("无有效会话；先执行 python scripts/auth_session.py login")
        return result

    def check(self, usercode):
        """判断 usercode 当前是否仍可用；不依赖本地 cookie。"""
        if not usercode:
            return False
        try:
            with self.open(ORIGIN + "/api/auth/islogin", {"usercode": usercode}) as response:
                result = json.loads(response.read())
        except (HTTPError, URLError, OSError, ValueError):
            return False
        user = result.get("user") or result.get("data")
        return (result.get("code") == 200 and isinstance(user, dict)
                and user.get("code") == usercode and "文档管理" in user.get("range", []))

    def reuse(self):
        path = self.root / "session.json"
        if not path.exists():
            return None
        state = json.loads(path.read_text())
        if not state.get("usercode"):
            return None
        try:
            with self.open(ORIGIN + "/api/auth/islogin", {"usercode": state["usercode"]}) as response:
                result = json.loads(response.read())
        except HTTPError as exc:
            if exc.code in (401, 403):
                return None
            raise
        user = result.get("user") or result.get("data")
        if result.get("code") != 200 or not isinstance(user, dict) or not user.get("code") or "文档管理" not in user.get("range", []):
            return None
        state["usercode"] = user["code"]
        self.save_session(state)
        return {"authenticated": True, "method": "saved-session", "account": user.get("number"),
                "permissions": user.get("range", []), "state_file": str(path), "reusable_session_verified": True}

    def login_auto(self, attempts=5):
        """非交互登录：自动获取并识别验证码；识别失败或验证码被拒时换新验证码重试。

        不读取终端、不打开图片查看器；attempts 用尽后抛出带图片路径的 AuthError。
        """
        last_error, challenge = None, {}
        for _ in range(attempts):
            challenge = self.captcha()
            captcha = challenge.get("captcha")
            if not captcha:
                last_error = challenge.get("captcha_recognition_error") or "验证码自动识别失败"
                if "缺少验证码识别依赖" in last_error:
                    break  # 换图也无济于事，直接给出安装提示
                continue
            try:
                return self.login(captcha)
            except CaptchaError as exc:
                last_error = exc
        raise AuthError(f"验证码自动识别连续 {attempts} 次未通过：{last_error}；"
                        f"图片在 {challenge.get('captcha_image')}，请在真人终端重试 login")

    def login(self, captcha):
        if not captcha.strip():
            raise AuthError("需要用户填写本次图片验证码")
        if not self.jar_file.exists():
            raise AuthError("先执行 captcha 获取验证码和对应会话")
        self.jar.load(ignore_discard=True)
        credentials = load_credentials(self.config_dir)
        fields = {"username": credentials["username"], "password": credentials["password"], "captcha": captcha.strip()}
        with self.open(self.login_endpoint(), fields) as response:
            result = json.loads(response.read())
        code = result.get("code")
        if code == -10002:
            raise CaptchaError("验证码错误或过期；重新获取验证码后再提交")
        if code == -10003:
            raise AuthError("账号或密码验证失败；未保存新登录会话")
        if code != 0 or not isinstance(result.get("msg"), str):
            raise AuthError("LDAP 登录未成功；未保存新登录会话")
        target = trusted(urljoin(PROVIDER, result["msg"]))
        with self.open(target) as response:
            response.read()
        # The admin page sends decodeURIComponent(document.cookie) as JSON.
        cookies = [c for c in self.jar if c.domain.lstrip(".") == "ecology.chinauos.com"]
        cookie_header = unquote("; ".join(c.name + "=" + c.value for c in cookies if not c.has_nonstandard_attr("HttpOnly")))
        with self.open(ORIGIN + "/api/auth/islogin", {"cookie": cookie_header, "usercode": ""}, json_body=True) as response:
            auth = json.loads(response.read())
        user = auth.get("user") or auth.get("data")
        if auth.get("code") != 200 or not isinstance(user, dict) or not user.get("code") or "文档管理" not in user.get("range", []):
            raise AuthError("LDAP 登录成功，但生态文档权限校验未通过")
        state = {"usercode": user["code"], "account": user.get("number"), "name": user.get("name"),
                 "cookies": [{"name": c.name, "value": c.value, "domain": c.domain, "path": c.path, "secure": c.secure} for c in cookies]}
        # Verify the reusable usercode, without relying on the LDAP session.
        with self.open(ORIGIN + "/api/auth/islogin", {"usercode": state["usercode"]}) as response:
            verified = json.loads(response.read())
        if verified.get("code") != 200:
            raise AuthError("新会话复用校验失败，未替换原 session.json")
        self.save_session(state)
        self.jar_file.unlink(missing_ok=True)
        for image in self.root.glob("captcha-*.png"):
            image.unlink(missing_ok=True)
        (self.root / "captcha.png").unlink(missing_ok=True)
        return {"authenticated": True, "method": "username-password-http", "account": user.get("number"),
                "permissions": user.get("range", []), "state_file": str(self.root / "session.json"), "reusable_session_verified": True}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE)
    parser.add_argument("--config-dir", type=Path, default=DEFAULT_CONFIG)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("status", help="校验已保存会话")
    cfg = sub.add_parser("configure", help="加密保存账号密码")
    cfg.add_argument("--username", required=True)
    cfg.add_argument("--password-stdin", action="store_true")
    cp = sub.add_parser("captcha")
    cp.add_argument("--open", action="store_true", help="用本机图片查看器打开验证码")
    lg = sub.add_parser("login")
    lg.add_argument("--force", action="store_true", help="跳过已有会话复用，获取新验证码重新认证")
    args = parser.parse_args(argv)
    client = AuthSession(args.state_dir, args.config_dir)
    if args.command == "configure":
        password = sys.stdin.readline().rstrip("\r\n") if args.password_stdin else getpass.getpass("密码：")
        result = store_credentials(client.config_dir, args.username, password)
    elif args.command == "status":
        result = client.status()
    elif args.command == "captcha":
        result = client.captcha(args.open)
    elif args.command == "login":
        result = None if args.force else client.reuse()
        if result is None:
            try:
                # 自动获取、识别并提交验证码；识别失败或验证码被拒时自动换图重试。
                result = client.login_auto()
            except AuthError:
                if not sys.stdin.isatty():
                    raise
                # 真人终端：再取一张新验证码，展示后请用户填写。
                challenge = client.captcha(open_image=True)
                print(json.dumps(challenge, ensure_ascii=False, indent=2), flush=True)
                result = client.login(input("请读取上面的新验证码图片，输入验证码："))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except AuthError as exc:
        print(f"错误：{exc}", file=sys.stderr)
        sys.exit(1)
    except (HTTPError, URLError, OSError, ValueError, KeyError):
        # Network exception strings can include OAuth codes; keep output generic.
        print("错误：HTTP 登录请求失败或本地配置格式无效；未确认登录成功", file=sys.stderr)
        sys.exit(1)
