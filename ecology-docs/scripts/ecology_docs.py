#!/usr/bin/env python3
"""List, read, upload, create and update ecology documents using auth_session."""
import argparse
import hashlib
import json
import mimetypes
import os
from pathlib import Path
import re
import sys
import tempfile
import time
from urllib.parse import urlencode, urlsplit

import requests
import auth_session

ORIGIN = auth_session.ORIGIN
ADMIN = auth_session.ADMIN
UPLOAD = "/adaptidentification/uos/develop/imgtobase64"
DEFAULT_STATE = auth_session.DEFAULT_STATE

class DocsError(RuntimeError):
    pass


class SessionExpired(DocsError):
    """服务端拒绝了当前会话；可以自动重新登录后重试一次。"""


def sha(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def private_dir(path):
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    if path.is_symlink():
        raise DocsError("私有目录不能是符号链接")
    path.chmod(0o700)


def save_json(path, value):
    # A read --output target may live in a shared directory such as /tmp.
    # Keep the file private without changing permissions of existing parents.
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    fd, name = tempfile.mkstemp(prefix=".tmp-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def checked_id(value):
    if not re.fullmatch(r"[0-9a-f]{24}", value or ""):
        raise DocsError("文档或目录 ID 必须是 24 位小写十六进制字符串")
    return value


def links(doc):
    query = urlencode({"dirid": doc["parent"], "id": doc["_id"]})
    return {"admin_url": ADMIN + "#edit?type=document&" + query,
            "front_url": "https://uosdn.uniontech.com/#document3?" + query}


class Client:
    def __init__(self, state_dir=DEFAULT_STATE, session=None):
        self.state_dir = Path(state_dir).expanduser().resolve()
        self.state_file = self.state_dir / "session.json"
        self.session = session or requests.Session()
        self.auth = auth_session.AuthSession(self.state_dir)
        self.state = self.auth.load_session()
        self.session.headers.update({"Referer": ADMIN, "Origin": ORIGIN})
        self._load_cookies()

    def _load_cookies(self):
        self.session.cookies.clear()
        for cookie in self.state.get("cookies", []):
            # Only ecology cookies belong in the document transport.
            if cookie.get("domain", "").lstrip(".") == "ecology.chinauos.com":
                self.session.cookies.set(cookie["name"], cookie["value"],
                                         domain=cookie["domain"], path=cookie.get("path", "/"),
                                         secure=cookie.get("secure", True))

    def refresh_session(self):
        """会话失效时非交互地重新登录（自动识别验证码）并刷新本地 cookie。

        复用已有会话失败才重新登录；自动登录失败时给出人工登录指引，不阻塞任务。
        """
        try:
            report = self.auth.reuse()
            if report is None:
                report = self.auth.login_auto()
        except auth_session.AuthError as exc:
            raise DocsError(f"会话已失效，自动重新登录失败：{exc}；请执行 python scripts/auth_session.py login") from None
        self.state = self.auth.load_session()
        self._load_cookies()
        return report

    def persist(self):
        private_dir(self.state_dir)
        self.state["cookies"] = [{"name": c.name, "value": c.value, "domain": c.domain,
                                  "path": c.path, "secure": c.secure}
                                 for c in self.session.cookies
                                 if c.domain.lstrip(".") == "ecology.chinauos.com"]
        self.auth.save_session(self.state)

    def request(self, method, path, fields=None, files=None, authenticated=True, include_metadata=False):
        arguments = (method, path, fields, files, authenticated, include_metadata)
        try:
            return self._send(*arguments)
        except SessionExpired:
            # 服务端已拒绝该请求，重新登录后重试一次，避免任务中途直接失败。
            self.refresh_session()
            try:
                return self._send(*arguments)
            except SessionExpired:
                raise DocsError("重新登录后服务端仍拒绝请求；请检查账号权限") from None

    def _session_invalid(self):
        try:
            return not self.auth.check(self.state.get("usercode"))
        except Exception:
            # 探活本身失败时不据此重试，按原业务错误返回。
            return False

    def _send(self, method, path, fields=None, files=None, authenticated=True, include_metadata=False):
        payload = dict(fields or {})
        if authenticated:
            code = self.state.get("usercode")
            if not code:
                raise SessionExpired("本地没有可用 usercode")
            payload["usercode"] = code
        kwargs = {"params" if method == "GET" else "data": payload}
        try:
            response = self.session.request(method, ORIGIN + path, files=files,
                                            timeout=60, allow_redirects=False, **kwargs)
        except requests.RequestException:
            raise DocsError("网络请求失败；写入请求可能已被服务端处理，请先 read 核对，勿自动重试") from None
        if response.status_code in (301, 302, 303, 307, 308, 401, 403):
            raise SessionExpired(f"服务端 HTTP {response.status_code}")
        if response.status_code != 200:
            raise DocsError(f"服务端 HTTP {response.status_code}；请先回读核对写入状态")
        try:
            result = response.json()
        except ValueError:
            raise DocsError("接口未返回 JSON；请检查登录状态") from None
        if not isinstance(result, dict) or result.get("code") != 200:
            if self._session_invalid():
                raise SessionExpired("接口业务状态非 200 且会话校验失败")
            # Do not print server info: it can echo credentials or request contents.
            raise DocsError("接口业务状态非 200；请检查登录、权限和目标 ID")
        user = result.get("user")
        if isinstance(user, dict) and user.get("code"):
            self.state["usercode"] = user["code"]
            self.persist()
        return result if include_metadata else result.get("data")

    def _directories(self):
        data = self.request("GET", "/api/doc", {"type": "document", "statusall": "all"})
        if not isinstance(data, list):
            raise DocsError("目录响应不是数组")
        return data

    def _documents(self, parent=None):
        fields = {"type": "document", "status": "all"}
        if parent is not None:
            fields["parent"] = checked_id(parent)
        result = self.request("GET", "/api/doc/doc", fields, include_metadata=True)
        data = result.get("data")
        if not isinstance(data, list) or result.get("count") != len(data):
            raise DocsError("文章列表不完整，不能报告已列出全部文章")
        if parent is not None and any(d.get("parent") != parent for d in data):
            raise DocsError("文章目录过滤结果不匹配")
        return data

    def list_tree(self, parent=None):
        directories = self._directories()
        by_id = {d["_id"]: d for d in directories}
        if len(by_id) != len(directories):
            raise DocsError("目录 ID 重复")
        if parent is not None and checked_id(parent) not in by_id:
            raise DocsError("指定目录不存在或不可访问")
        child_dirs, child_docs = {}, {}
        for d in directories:
            child_dirs.setdefault(d.get("parent"), []).append(d)
        if parent is None:
            documents = self._documents()
        else:
            # Select the complete subtree before requesting articles. The API
            # returns full bodies, so downloading unrelated articles is costly.
            selected, pending = set(), [parent]
            documents = []
            while pending:
                ident = pending.pop()
                if ident in selected:
                    raise DocsError("目录存在循环引用")
                selected.add(ident)
                pending.extend(d["_id"] for d in child_dirs.get(ident, []))
            for ident in sorted(selected):
                documents.extend(self._documents(ident))
        for d in documents:
            child_docs.setdefault(d.get("parent"), []).append(d)
        visited, active = set(), set()
        document_count = 0

        def order(d):
            try:
                rank = float(d.get("sort", 9999999))
            except (TypeError, ValueError):
                rank = 9999999
            return rank, str(d.get("title", "")), d["_id"]

        def article(d):
            nonlocal document_count
            document_count += 1
            return {"kind": "document", **{k: d.get(k) for k in ("_id", "title", "parent", "status", "sort", "mtime")}}

        def directory(d):
            ident = d["_id"]
            if ident in active:
                raise DocsError("目录存在循环引用")
            active.add(ident)
            node = {"kind": "directory", **{k: d.get(k) for k in ("_id", "title", "parent", "status", "sort")}}
            node["children"] = [directory(c) for c in sorted(child_dirs.get(ident, []), key=order)]
            node["children"] += [article(a) for a in sorted(child_docs.get(ident, []), key=order)]
            active.remove(ident)
            visited.add(ident)
            return node

        if parent is not None:
            items = [directory(by_id[parent])]
        else:
            roots = sorted((d for d in directories if d.get("parent") not in by_id), key=order)
            items = [directory(d) for d in roots]
            # A cycle has no natural root; inspect every remaining component too.
            for d in directories:
                if d["_id"] not in visited:
                    items.append(directory(d))
            items += [article(a) for a in sorted(documents, key=order) if a.get("parent") not in by_id]
        return {"parent": parent, "directory_count": len(visited), "document_count": document_count, "items": items}

    def read(self, doc_id):
        doc_id = checked_id(doc_id)
        data = self.request("GET", "/api/doc/doc", {"id": doc_id, "status": "all"})
        if not isinstance(data, list) or len(data) != 1 or data[0].get("_id") != doc_id:
            raise DocsError("文档回读 ID 不匹配或不可访问")
        doc = data[0]
        if doc.get("type") != "document" or not isinstance(doc.get("info"), str):
            raise DocsError("仅支持普通 document Markdown 文档")
        return doc

    def update(self, doc_id, text, title=None, status=None, expected_sha=None):
        before = self.read(doc_id)
        if expected_sha and sha(before["info"]) != expected_sha:
            raise DocsError("线上正文与预期 SHA256 不一致，停止更新")
        title = title if title is not None else before["title"]
        status = status or before["status"]
        if status not in ("save", "publish"):
            raise DocsError("仅支持 save/publish 状态")
        if before["info"] == text and before["title"] == title and before["status"] == status:
            return {"id": doc_id, "verified": True, "action": "unchanged", "document_status": status, "sha256": sha(text), **links(before)}
        run = self.state_dir / "runs" / (time.strftime("%Y%m%d-%H%M%S") + "-" + str(time.time_ns()))
        private_dir(self.state_dir)
        save_json(run / "before.json", before)
        journal = {"action": "update", "id": doc_id, "status": "prepared", "desired_sha256": sha(text)}
        save_json(run / "result.json", journal)
        current = self.read(doc_id)
        if current != before:
            raise DocsError("备份后线上文档发生变化，停止更新；备份已保留")
        fields = {"id": doc_id, "title": title, "type": "document", "status": status}
        journal["status"] = "write_attempted"
        save_json(run / "result.json", journal)
        self.request("POST", "/api/doc/adddoc", fields,
                     files={"file": ("document.md", text.encode("utf-8"), "text/markdown;charset=utf-8")})
        after = self.read(doc_id)
        save_json(run / "after.json", after)
        if (after.get("info") != text or after.get("title") != title or after.get("status") != status
                or any(after.get(k) != before.get(k) for k in ("_id", "parent", "sort", "type", "ctime"))):
            raise DocsError(f"写入后的正文或属性回读不匹配；记录保存在 {run}")
        journal.update(status="verified", document_status=after["status"], verified=True, sha256=sha(text), backup=str(run / "before.json"), **links(after))
        save_json(run / "result.json", journal)
        return journal

    def create(self, parent, title, text, status="save"):
        parent = checked_id(parent)
        if not title.strip():
            raise DocsError("新文档标题不能为空")
        dirs = self._directories()
        if not isinstance(dirs, list) or not any(d.get("_id") == parent for d in dirs):
            raise DocsError("目标目录不存在或不可访问")
        run = self.state_dir / "runs" / ("create-" + str(time.time_ns()))
        private_dir(self.state_dir)
        journal = {"action": "create", "parent": parent, "title": title,
                   "desired_sha256": sha(text), "status": "write_attempted"}
        save_json(run / "result.json", journal)
        result = self.request("POST", "/api/doc/adddoc", {"dirid": parent, "title": title, "type": "document", "status": status},
                              files={"file": ("document.md", text.encode("utf-8"), "text/markdown;charset=utf-8")})
        if not isinstance(result, str) or not re.fullmatch(r"[0-9a-f]{24}", result):
            raise DocsError(f"新建接口未返回文档 ID；先在目录中核对，勿重复新建；记录：{run}")
        journal["id"] = result
        save_json(run / "result.json", journal)
        after = self.read(result)
        save_json(run / "after.json", after)
        if any(after.get(k) != v for k, v in {"parent": parent, "title": title, "info": text, "status": status}.items()):
            raise DocsError(f"新建后回读不一致；记录：{run}")
        journal.update(status="verified", document_status=after["status"], verified=True, sha256=sha(text), **links(after))
        save_json(run / "result.json", journal)
        return journal

    def upload(self, path):
        content = path.read_bytes()
        url = self.request("POST", UPLOAD, files={"file": (path.name, content, mimetypes.guess_type(path.name)[0] or "application/octet-stream")})
        parsed = urlsplit(url) if isinstance(url, str) else None
        if not parsed or parsed.scheme != "https" or parsed.netloc != "ecology.chinauos.com" or not parsed.path.startswith("/mingdaoyun/"):
            raise DocsError("上传响应不是预期的本站资源地址，停止自动下载")
        url = ORIGIN + parsed.path  # Site URLs may have display-only query parameters.
        try:
            response = self.session.get(url, timeout=60, allow_redirects=False)
        except requests.RequestException:
            raise DocsError("上传后下载验证失败；资源可能已创建，请勿自动重复上传") from None
        if response.status_code in (401, 403):
            # 上传本身已成功，仅是回读被拒：重新登录后重试下载，不重复上传。
            self.refresh_session()
            try:
                response = self.session.get(url, timeout=60, allow_redirects=False)
            except requests.RequestException:
                raise DocsError("上传后下载验证失败；资源可能已创建，请勿自动重复上传") from None
        digest = hashlib.sha256(content).hexdigest()
        verified = response.status_code == 200 and hashlib.sha256(response.content).hexdigest() == digest
        report = {"file": str(path), "url": url, "sha256": digest, "verified": verified}
        private_dir(self.state_dir)
        save_json(self.state_dir / "uploads" / (str(time.time_ns()) + ".json"), report)
        if not verified:
            raise DocsError("上传后资源哈希不一致；上传记录已保留")
        return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--state-dir", type=Path, default=DEFAULT_STATE)
    sub = parser.add_subparsers(dest="command", required=True)
    ls = sub.add_parser("list", help="完整目录文章树；--parent 限定子树")
    ls.add_argument("--parent")
    rd = sub.add_parser("read")
    rd.add_argument("--id", required=True)
    rd.add_argument("--output", type=Path)
    for command in ("update", "create"):
        cmd = sub.add_parser(command)
        cmd.add_argument("--id" if command == "update" else "--parent", required=True)
        cmd.add_argument("--file", type=Path, required=True)
        cmd.add_argument("--title", required=command == "create")
        cmd.add_argument("--status", choices=("save", "publish"), default="save" if command == "create" else None)
        cmd.add_argument("--dry-run", action="store_true")
        if command == "update":
            cmd.add_argument("--expected-sha256")
    up = sub.add_parser("upload")
    up.add_argument("--file", type=Path, required=True)
    up.add_argument("--dry-run", action="store_true")
    opts = parser.parse_args(argv)
    if hasattr(opts, "file") and not opts.file.is_file():
        raise DocsError("输入文件不存在或不是普通文件")
    if hasattr(opts, "id"):
        checked_id(opts.id)
    if getattr(opts, "parent", None):
        checked_id(opts.parent)
    if getattr(opts, "dry_run", False):
        if opts.command in ("create", "update"):
            opts.file.read_text(encoding="utf-8")
        result = {"dry_run": True, "network_requests": 0, "action": opts.command,
                  "file": str(opts.file), "bytes": opts.file.stat().st_size,
                  "endpoint": ORIGIN + (UPLOAD if opts.command == "upload" else "/api/doc/adddoc"),
                  "id": getattr(opts, "id", None), "parent": getattr(opts, "parent", None)}
        if opts.command != "upload":
            result["status"] = getattr(opts, "status", None) or "preserve-current"
    else:
        client = Client(opts.state_dir)
        # 会话失效时自动重新登录，避免任务中途直接终止。
        client.refresh_session()
        if opts.command == "list":
            result = client.list_tree(opts.parent)
        elif opts.command == "read":
            result = client.read(opts.id)
            if opts.output:
                save_json(opts.output, result)
                result = {"id": opts.id, "output": str(opts.output), "sha256": sha(result["info"]), **links(result)}
        elif opts.command == "upload":
            result = client.upload(opts.file)
        elif opts.command == "update":
            result = client.update(opts.id, opts.file.read_text(encoding="utf-8"), opts.title, opts.status, opts.expected_sha256)
        elif opts.command == "create":
            result = client.create(opts.parent, opts.title, opts.file.read_text(encoding="utf-8"), opts.status)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    try:
        main()
    except (DocsError, auth_session.AuthError, OSError, ValueError, KeyError) as exc:
        # Parsing errors can contain secret source text; only expose our own messages.
        print(f"错误：{exc}" if isinstance(exc, (DocsError, auth_session.AuthError)) else "错误：本地文件不可读或格式无效", file=sys.stderr)
        sys.exit(1)
