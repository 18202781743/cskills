"""Offline document-client contract tests without production writes or credentials."""
import contextlib
import copy
import importlib.util
import io
import json
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/ecology_docs.py"
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location("ecology_docs", SCRIPT)
docs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docs)
ID = "a" * 24
PARENT = "b" * 24


class FakeClient(docs.Client):
    def __init__(self, state_dir):
        super().__init__(state_dir)
        self.doc = {"_id": ID, "parent": PARENT, "title": "中文标题", "info": "旧正文\n",
                    "sort": 2, "status": "publish", "type": "document", "ctime": 1, "mtime": 2}
        self.calls = []
        self.read_count = 0
        self.conflict = False
        self.bad_after = False

    def read(self, doc_id):
        self.read_count += 1
        value = copy.deepcopy(self.doc)
        if self.conflict and self.read_count == 2:
            value["info"] = "别人已修改"
        if self.bad_after and self.read_count == 3:
            value["parent"] = "c" * 24
        return value

    def _directories(self):
        return [{"_id": PARENT}]

    def request(self, method, path, fields=None, files=None, authenticated=True):
        self.calls.append((method, path, fields, files))
        self.doc.update(title=fields["title"], status=fields["status"], info=files["file"][1].decode("utf-8"))
        if "dirid" in fields:
            self.doc["parent"] = fields["dirid"]
            return ID
        return ""


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = FakeClient(self.root / "state")

    def test_update_preserves_publication_and_metadata(self):
        before = copy.deepcopy(self.client.doc)
        result = self.client.update(ID, "新正文\n", expected_sha=docs.sha(before["info"]))
        self.assertTrue(result["verified"])
        method, endpoint, fields, files = self.client.calls[0]
        self.assertEqual((method, endpoint), ("POST", "/api/doc/adddoc"))
        self.assertEqual(fields["status"], "publish")
        self.assertNotIn("dirid", fields)
        self.assertEqual(files["file"][1], "新正文\n".encode())
        self.assertEqual(json.loads(Path(result["backup"]).read_text()), before)
        self.assertEqual(Path(result["backup"]).stat().st_mode & 0o777, 0o600)
        self.assertEqual(Path(result["backup"]).parent.stat().st_mode & 0o777, 0o700)

    def test_no_write_on_conflict(self):
        self.client.conflict = True
        with self.assertRaisesRegex(docs.DocsError, "发生变化"):
            self.client.update(ID, "new")
        self.assertEqual(self.client.calls, [])
        self.assertEqual(len(list((self.root / "state/runs").glob("*/before.json"))), 1)

    def test_no_write_on_expected_hash_mismatch(self):
        with self.assertRaisesRegex(docs.DocsError, "SHA256"):
            self.client.update(ID, "new", expected_sha="0" * 64)
        self.assertEqual(self.client.calls, [])

    def test_failed_readback_is_not_success(self):
        self.client.bad_after = True
        with self.assertRaisesRegex(docs.DocsError, "回读不匹配"):
            self.client.update(ID, "new")
        journal = json.loads(next((self.root / "state/runs").glob("*/result.json")).read_text())
        self.assertEqual(journal["status"], "write_attempted")
        self.assertNotIn("verified", journal)

    def test_unchanged_document_is_not_rewritten(self):
        result = self.client.update(ID, self.client.doc["info"])
        self.assertEqual(result["action"], "unchanged")
        self.assertEqual(self.client.calls, [])

    def test_new_document_uses_directory_and_draft(self):
        result = self.client.create(PARENT, "示例", "正文")
        self.assertTrue(result["verified"])
        fields = self.client.calls[0][2]
        self.assertEqual(fields["dirid"], PARENT)
        self.assertEqual(fields["status"], "save")
        self.assertNotIn("id", fields)

    def test_dry_run_does_not_load_session_or_network(self):
        path = self.root / "article.md"
        path.write_text("# 中文\n", encoding="utf-8")
        for command, extra in [("update", ["--id", ID]), ("create", ["--parent", PARENT, "--title", "标题"]), ("upload", [])]:
            out = io.StringIO()
            with patch.object(docs, "Client", side_effect=AssertionError("会话被加载")), contextlib.redirect_stdout(out):
                docs.main([command, "--file", str(path), "--dry-run", *extra])
            result = json.loads(out.getvalue())
            self.assertEqual(result["network_requests"], 0)


    def test_business_error_does_not_echo_secret(self):
        client = docs.Client(self.root / "state")
        client.state = {"usercode": "secret"}
        response = unittest.mock.Mock(status_code=200)
        response.json.return_value = {"code": 401, "info": "secret"}
        with patch.object(client.session, "request", return_value=response) as send, \
                patch.object(client.auth, "check", return_value=True):
            with self.assertRaises(docs.DocsError) as error:
                client.request("POST", "/api/auth/islogin")
        self.assertNotIn("secret", str(error.exception))
        self.assertEqual(send.call_count, 1)

    def test_asset_upload_download_hash_and_host_validation(self):
        client = docs.Client(self.root / "state")
        path = self.root / "example.zip"
        path.write_bytes(b"synthetic zip bytes")
        response = unittest.mock.Mock(status_code=200, content=path.read_bytes())
        url = docs.ORIGIN + "/mingdaoyun/mdoc/normal/example.zip?name=example"
        with patch.object(client, "request", return_value=url), patch.object(client.session, "get", return_value=response):
            result = client.upload(path)
        self.assertTrue(result["verified"])
        self.assertNotIn("?", result["url"])
        with patch.object(client, "request", return_value="https://foreign.example/file"), patch.object(client.session, "get") as download:
            with self.assertRaisesRegex(docs.DocsError, "预期"):
                client.upload(path)
            download.assert_not_called()

    def test_export_keeps_existing_parent_permissions(self):
        parent = self.root / "shared"
        parent.mkdir(mode=0o755)
        docs.save_json(parent / "readback.json", {"info": "正文"})
        self.assertEqual(parent.stat().st_mode & 0o777, 0o755)
        self.assertEqual((parent / "readback.json").stat().st_mode & 0o777, 0o600)


class FakeAuth:
    """AuthSession 替身：只暴露会话失效处理需要的接口。"""

    def __init__(self, reuse=None, session=None, error=None):
        self.reuse_result = reuse
        self.session = session or {}
        self.error = error
        self.auto_login_calls = 0

    def reuse(self):
        return self.reuse_result

    def login_auto(self):
        self.auto_login_calls += 1
        if self.error is not None:
            raise self.error
        return {"authenticated": True}

    def load_session(self):
        return dict(self.session)


class SessionRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.client = docs.Client(self.root / "state")
        self.client.state = {"usercode": "u1", "cookies": []}

    @staticmethod
    def response(status_code, payload=None):
        value = unittest.mock.Mock(status_code=status_code)
        if payload is None:
            value.json.side_effect = ValueError("no json")
        else:
            value.json.return_value = payload
        return value

    def test_expired_session_is_renewed_and_request_retried(self):
        replies = [self.response(401), self.response(200, {"code": 200, "data": ["ok"]})]
        with patch.object(self.client.session, "request", side_effect=replies) as send, \
                patch.object(self.client, "refresh_session") as renew:
            self.assertEqual(self.client.request("GET", "/api/doc"), ["ok"])
        self.assertEqual(send.call_count, 2)
        renew.assert_called_once_with()

    def test_repeated_rejection_stops_after_one_renewal(self):
        with patch.object(self.client.session, "request", return_value=self.response(403)) as send, \
                patch.object(self.client, "refresh_session"):
            with self.assertRaisesRegex(docs.DocsError, "仍拒绝"):
                self.client.request("GET", "/api/doc")
        self.assertEqual(send.call_count, 2)

    def test_missing_usercode_is_recovered_by_relogin(self):
        self.client.state = {}

        def renew():
            self.client.state["usercode"] = "u2"
            return {"authenticated": True}

        with patch.object(self.client.session, "request", side_effect=[self.response(200, {"code": 200, "data": "ok"})]), \
                patch.object(self.client, "refresh_session", side_effect=renew) as renew_request:
            self.assertEqual(self.client.request("GET", "/api/doc"), "ok")
        renew_request.assert_called_once_with()

    def test_business_error_with_live_session_is_not_retried(self):
        with patch.object(self.client.session, "request", return_value=self.response(200, {"code": 500})) as send, \
                patch.object(self.client.auth, "check", return_value=True) as probe, \
                patch.object(self.client, "refresh_session") as renew:
            with self.assertRaisesRegex(docs.DocsError, "业务状态非 200"):
                self.client.request("POST", "/api/doc/adddoc")
        self.assertEqual(send.call_count, 1)
        self.assertEqual(probe.call_count, 1)
        renew.assert_not_called()

    def test_business_error_on_expired_session_triggers_relogin(self):
        replies = [self.response(200, {"code": 401}), self.response(200, {"code": 200, "data": "done"})]
        with patch.object(self.client.session, "request", side_effect=replies) as send, \
                patch.object(self.client.auth, "check", return_value=False), \
                patch.object(self.client, "refresh_session") as renew:
            self.assertEqual(self.client.request("POST", "/api/doc/adddoc"), "done")
        self.assertEqual(send.call_count, 2)
        renew.assert_called_once_with()

    def test_probe_failure_is_not_treated_as_expiry(self):
        with patch.object(self.client.auth, "check", side_effect=OSError("keyring unavailable")):
            self.assertFalse(self.client._session_invalid())

    def test_refresh_session_relogins_and_reloads_cookies(self):
        self.client.auth = FakeAuth(session={"usercode": "u2", "cookies": [
            {"name": "c", "value": "v", "domain": "ecology.chinauos.com", "path": "/", "secure": True}]})
        report = self.client.refresh_session()
        self.assertEqual(report, {"authenticated": True})
        self.assertEqual(self.client.auth.auto_login_calls, 1)
        self.assertEqual(self.client.state["usercode"], "u2")
        self.assertEqual(self.client.session.cookies.get("c"), "v")

    def test_refresh_session_reports_manual_login_instructions(self):
        self.client.auth = FakeAuth(error=docs.auth_session.AuthError("验证码自动识别失败"))
        with self.assertRaisesRegex(docs.DocsError, "auth_session.py login"):
            self.client.refresh_session()


class TreeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.client = docs.Client(Path(temp.name))
        self.root_id, self.child_id, self.other_id = "c" * 24, "d" * 24, "e" * 24
        self.directories = [
            {"_id": self.child_id, "parent": self.root_id, "title": "子目录", "sort": 1},
            {"_id": self.other_id, "parent": "", "title": "其他目录", "sort": 2},
            {"_id": self.root_id, "parent": "", "title": "根目录", "sort": 1},
        ]
        self.articles = [
            {"_id": ID, "parent": self.child_id, "title": "文章", "sort": 1, "info": "正文不应出现在树里"},
            {"_id": "f" * 24, "parent": self.other_id, "title": "另一篇", "sort": 1},
        ]

    def listing(self, parent=None):
        def request(method, path, fields, **kwargs):
            if path == "/api/doc":
                return self.directories
            articles = self.articles
            if "parent" in fields:
                articles = [a for a in articles if a["parent"] == fields["parent"]]
            return {"count": len(articles), "data": articles}
        with patch.object(self.client, "request", side_effect=request) as req:
            result = self.client.list_tree(parent)
        return result, req

    def test_full_tree_contains_all_sorted_directories_and_articles(self):
        tree, req = self.listing()
        self.assertEqual(tree["directory_count"], 3)
        self.assertEqual(tree["document_count"], 2)
        self.assertEqual([n["_id"] for n in tree["items"]], [self.root_id, self.other_id])
        article = tree["items"][0]["children"][0]["children"][0]
        self.assertEqual(article["_id"], ID)
        self.assertNotIn("info", article)
        self.assertEqual(req.call_count, 2)

    def test_parent_returns_only_selected_subtree(self):
        tree, request = self.listing(self.root_id)
        self.assertEqual(tree["directory_count"], 2)
        self.assertEqual(tree["document_count"], 1)
        self.assertEqual(tree["items"][0]["_id"], self.root_id)
        self.assertNotIn(self.other_id, json.dumps(tree))
        article_calls = [call for call in request.call_args_list if call.args[1] == "/api/doc/doc"]
        self.assertEqual({call.args[2]["parent"] for call in article_calls}, {self.root_id, self.child_id})

    def test_leaf_fetches_articles_only_for_that_parent(self):
        tree, request = self.listing(self.child_id)
        self.assertEqual(tree["document_count"], 1)
        article_calls = [call for call in request.call_args_list if call.args[1] == "/api/doc/doc"]
        self.assertEqual(len(article_calls), 1)
        self.assertEqual(article_calls[0].args[2]["parent"], self.child_id)

    def test_ignored_parent_filter_is_reported(self):
        with patch.object(self.client, "request", return_value={"count": 2, "data": self.articles}):
            with self.assertRaisesRegex(docs.DocsError, "过滤"):
                self.client._documents(self.child_id)

    def test_selected_cycle_stops_before_article_fetch(self):
        self.directories[2]["parent"] = self.child_id
        with patch.object(self.client, "_directories", return_value=self.directories), patch.object(self.client, "_documents") as articles:
            with self.assertRaisesRegex(docs.DocsError, "循环"):
                self.client.list_tree(self.root_id)
            articles.assert_not_called()

    def test_unknown_parent_stops_before_article_query(self):
        with patch.object(self.client, "_directories", return_value=self.directories), patch.object(self.client, "_documents") as articles:
            with self.assertRaisesRegex(docs.DocsError, "不存在"):
                self.client.list_tree("0" * 24)
            articles.assert_not_called()

    def test_unavailable_parent_does_not_hide_nodes(self):
        self.directories[2]["parent"] = "0" * 24
        self.articles.append({"_id": "1" * 24, "parent": "2" * 24, "title": "无可见目录的文章"})
        tree, _ = self.listing()
        self.assertEqual(tree["directory_count"], 3)
        self.assertEqual(tree["document_count"], 3)
        self.assertEqual(tree["items"][-1]["kind"], "document")

    def test_directory_cycle_is_reported(self):
        self.directories[2]["parent"] = self.child_id
        with self.assertRaisesRegex(docs.DocsError, "循环"):
            self.listing()

    def test_truncated_response_is_not_reported_as_complete(self):
        with patch.object(self.client, "request", return_value={"count": 10, "data": self.articles}):
            with self.assertRaisesRegex(docs.DocsError, "不完整"):
                self.client._documents()




if __name__ == "__main__":
    unittest.main()
