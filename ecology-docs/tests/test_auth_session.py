"""Contract tests for HTTP authentication and encrypted credentials."""
import base64
import builtins
import importlib.util
import io
import json
import sys
import contextlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.parse import quote

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/auth_session.py"
sys.path.insert(0, str(SCRIPT.parent))
spec = importlib.util.spec_from_file_location("auth_session", SCRIPT)
login = importlib.util.module_from_spec(spec)
spec.loader.exec_module(login)


def response(value):
    return io.BytesIO(json.dumps(value).encode())


class AuthSessionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "state"
        self.client = login.AuthSession(self.root, self.root / "config")
        # 除登录入口发现用例外，固定使用兜底入口，避免每个用例都要多一次页面请求。
        self.client.login_url = login.FALLBACK_LOGIN
        keypatch = patch.object(login, "_key", return_value=base64.urlsafe_b64encode(b"k" * 32))
        keypatch.start()
        self.addCleanup(keypatch.stop)
        login.store_credentials(self.client.config_dir, "sample", "synthetic-secret")
        self.client.jar.save(ignore_discard=True)

    def test_complete_chain_saves_verified_session_not_password(self):
        auth = {"code": 200, "data": {"code": "synthetic-usercode", "number": "TEST", "range": ["文档管理"]}}
        replies = [response({"code": 0, "msg": "/authorize?code=synthetic"}), io.BytesIO(b"admin"), response(auth), response(auth)]
        with patch.object(self.client, "open", side_effect=replies) as request:
            report = self.client.login("user-entered-captcha")
        self.assertTrue(report["authenticated"])
        self.assertTrue(report["reusable_session_verified"])
        self.assertEqual(request.call_args_list[0].args[1]["captcha"], "user-entered-captcha")
        saved = (self.root / "session.json").read_text()
        self.assertNotIn("synthetic-secret", saved)
        self.assertNotIn("synthetic-usercode", json.dumps(report))
        self.assertEqual((self.root / "session.json").stat().st_mode & 0o777, 0o600)
        self.assertFalse(self.client.jar_file.exists())

    def test_wrong_password_does_not_replace_old_session(self):
        login.private_write(self.root / "session.json", b'{"old":"session"}')
        with patch.object(self.client, "open", return_value=response({"code": -10003})):
            with self.assertRaisesRegex(login.AuthError, "账号或密码"):
                self.client.login("user-entered-captcha")
        self.assertEqual((self.root / "session.json").read_bytes(), b'{"old":"session"}')

    def test_expired_captcha_not_reported_as_login_success(self):
        with patch.object(self.client, "open", return_value=response({"code": -10002})):
            with self.assertRaisesRegex(login.CaptchaError, "验证码"):
                self.client.login("user-entered-captcha")
        self.assertFalse((self.root / "session.json").exists())

    def test_login_auto_retries_with_new_captcha(self):
        challenges = [{"status": "captcha_recognized", "captcha": "AAAA"},
                      {"status": "captcha_recognized", "captcha": "BBBB"}]
        with patch.object(self.client, "captcha", side_effect=challenges) as fetch, \
                patch.object(self.client, "login",
                             side_effect=[login.CaptchaError("验证码错误或过期"), {"authenticated": True}]) as submit:
            report = self.client.login_auto()
        self.assertTrue(report["authenticated"])
        self.assertEqual(fetch.call_count, 2)
        self.assertEqual([call.args[0] for call in submit.call_args_list], ["AAAA", "BBBB"])

    def test_login_auto_stops_after_attempts(self):
        challenge = {"status": "captcha_recognized", "captcha": "AAAA"}
        with patch.object(self.client, "captcha", return_value=challenge) as fetch, \
                patch.object(self.client, "login", side_effect=login.CaptchaError("验证码错误或过期")):
            with self.assertRaisesRegex(login.AuthError, "连续 3 次"):
                self.client.login_auto(attempts=3)
        self.assertEqual(fetch.call_count, 3)

    def test_login_auto_retries_when_recognition_fails(self):
        challenge = {"status": "human_input_required", "captcha_image": "/private/c.png",
                     "captcha_recognition_error": "no ocr"}
        with patch.object(self.client, "captcha", return_value=challenge) as fetch, \
                patch.object(self.client, "login") as submit:
            with self.assertRaisesRegex(login.AuthError, "/private/c.png"):
                self.client.login_auto(attempts=2)
        self.assertEqual(fetch.call_count, 2)
        submit.assert_not_called()

    def test_login_auto_stops_without_ocr_dependency(self):
        challenge = {"status": "human_input_required", "captcha_image": "/private/c.png",
                     "captcha_recognition_error": "缺少验证码识别依赖，请运行：python3 -m pip install ddddocr"}
        with patch.object(self.client, "captcha", return_value=challenge) as fetch:
            with self.assertRaisesRegex(login.AuthError, "ddddocr"):
                self.client.login_auto()
        self.assertEqual(fetch.call_count, 1)

    def test_check_rejects_missing_or_unknown_usercode(self):
        self.assertFalse(self.client.check(""))
        with patch.object(self.client, "open", return_value=response({"code": 401})):
            self.assertFalse(self.client.check("synthetic-usercode"))
        auth = {"code": 200, "data": {"code": "synthetic-usercode", "number": "TEST", "range": ["文档管理"]}}
        with patch.object(self.client, "open", return_value=response(auth)):
            self.assertTrue(self.client.check("synthetic-usercode"))

    def test_untrusted_authorization_target_rejected(self):
        with patch.object(self.client, "open", return_value=response({"code": 0, "msg": "https://foreign.example/authorize"})) as request:
            with self.assertRaisesRegex(login.AuthError, "非预期"):
                self.client.login("user-entered-captcha")
        self.assertEqual(request.call_count, 1)

    def test_captcha_session_and_image_are_private(self):
        image = b"synthetic-image"
        data = "data:image/png;base64," + base64.b64encode(image).decode()
        models = []

        def classify(image_bytes, beta=False):
            models.append(beta)
            if not beta:
                raise ValueError("未识别出 4 位数字或英文字母验证码，识别结果：'47778'")
            return "AB12"

        with patch.object(self.client, "open", side_effect=[io.BytesIO(b"login"), io.BytesIO(data.encode())]), \
                patch.object(login, "classify_captcha", side_effect=classify):
            report = self.client.captcha()
        self.assertEqual(models, [False, True])
        path = Path(report["captcha_image"])
        self.assertEqual(path.read_bytes(), image)
        self.assertEqual(path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(self.client.jar_file.stat().st_mode & 0o777, 0o600)
        self.assertEqual(report["status"], "captcha_recognized")
        self.assertEqual(report["captcha"], "AB12")
        self.assertFalse(report["image_viewer_requested"])

    def test_open_captcha_falls_back_to_viewer_when_recognition_fails(self):
        data = "data:image/png;base64," + base64.b64encode(b"synthetic-image").decode()
        with patch.object(self.client, "open", side_effect=[io.BytesIO(b"login"), io.BytesIO(data.encode())]), \
                patch.object(login, "classify_captcha", side_effect=ValueError("no ocr")) as classify, \
                patch.object(login.shutil, "which", return_value="/usr/bin/xdg-open"), \
                patch.object(login.subprocess, "Popen") as viewer:
            report = self.client.captcha(open_image=True)
        self.assertEqual(classify.call_count, 2)
        self.assertEqual(report["status"], "human_input_required")
        self.assertNotIn("captcha", report)
        self.assertEqual(report["captcha_recognition_error"], "no ocr")
        self.assertTrue(report["image_viewer_requested"])
        self.assertEqual(viewer.call_args.args[0], ["xdg-open", report["captcha_image"]])

    def test_recognized_captcha_is_submitted_without_stdin(self):
        out = io.StringIO()
        with patch.object(login, "AuthSession", return_value=self.client), \
                patch.object(self.client, "login_auto", return_value={"authenticated": True}) as auto, \
                patch.object(self.client, "captcha") as fetch, \
                patch.object(login.sys.stdin, "isatty", return_value=False), \
                patch("builtins.input", side_effect=AssertionError("must not wait on stdin")), \
                contextlib.redirect_stdout(out):
            login.main(["login", "--force"])
        auto.assert_called_once_with()
        fetch.assert_not_called()
        self.assertTrue(json.loads(out.getvalue())["authenticated"])

    def test_clean_result_requires_four_characters(self):
        self.assertEqual(login._clean_result(" 5324 "), "5324")
        with self.assertRaisesRegex(ValueError, "4 位"):
            login._clean_result("47778")
        with self.assertRaisesRegex(ValueError, "4 位"):
            login._clean_result("")

    def test_login_endpoint_is_discovered_from_admin_page(self):
        page = ('<a href="https://login-platform.uniontech.com/login?access_type=offline&amp;client_id=abc123'
                "&redirect_uri=https%3A%2F%2Fecology.chinauos.com%2Fadaptidentification%2Fuos%2Fdevelop%2Fcallbackdoc"
                '&response_type=code">登录</a>')
        params = login.parse_login_params(page)
        self.assertEqual(params, {"access_type": "offline", "client_id": "abc123",
                                 "redirect_uri": login.ORIGIN + login.CALLBACK_PATH,
                                 "response_type": "code", "scope": "base,user:read,certify:edit"})
        discovered = login.build_login_url(params)
        self.assertIn("client_id=abc123", discovered)
        self.assertIn("state=" + quote(login.ADMIN, safe=""), discovered)
        self.client.login_url = None
        with patch.object(self.client, "open", return_value=io.BytesIO(page.encode())) as request:
            endpoint = self.client.login_endpoint()
        self.assertEqual(request.call_args.args[0], login.ADMIN)
        self.assertEqual(endpoint, discovered)
        # 解析结果会缓存，不再重复请求页面。
        with patch.object(self.client, "open", side_effect=AssertionError("must be cached")):
            self.assertEqual(self.client.login_endpoint(), endpoint)

    def test_login_endpoint_ignores_unrelated_login_links(self):
        page = ('<a href="https://login-platform.uniontech.com/login?client_id=x'
                "&redirect_uri=https%3A%2F%2Fother.example%2Fcallbackdoc"
                '">其他</a><a href="https://login-platform.uniontech.com/login?client_id=y">无回调</a>'
                '<a href="https://login-platform.uniontech.com/login?client_id=z'
                "&redirect_uri=https%3A%2F%2Fecology.chinauos.com%2Fadaptidentification%2Fuos%2Fdevelop%2Fothercallback"
                '">同站其他应用</a>')
        self.assertEqual(login.parse_login_params(page), None)
        self.client.login_url = None
        with patch.object(self.client, "open", return_value=io.BytesIO(page.encode())):
            self.assertEqual(self.client.login_endpoint(), login.FALLBACK_LOGIN)

    def test_login_endpoint_falls_back_without_admin_page(self):
        self.client.login_url = None
        with patch.object(self.client, "open", side_effect=login.URLError("offline")):
            self.assertEqual(self.client.login_endpoint(), login.FALLBACK_LOGIN)

    def test_captcha_uses_discovered_login_entry(self):
        page = ('<a href="https://login-platform.uniontech.com/login?client_id=abc123'
                "&redirect_uri=https%3A%2F%2Fecology.chinauos.com%2Fadaptidentification%2Fuos%2Fdevelop%2Fcallbackdoc\">登录</a>")
        data = "data:image/png;base64," + base64.b64encode(b"synthetic-image").decode()
        self.client.login_url = None
        replies = [io.BytesIO(page.encode()), io.BytesIO(b"login page"), io.BytesIO(data.encode())]
        with patch.object(self.client, "open", side_effect=replies) as request, \
                patch.object(login, "classify_captcha", return_value="AB12"):
            report = self.client.captcha()
        self.assertEqual(request.call_args_list[0].args[0], login.ADMIN)
        self.assertIn("client_id=abc123", request.call_args_list[1].args[0])
        self.assertEqual(report["captcha"], "AB12")

    def test_noninteractive_login_reports_failure_without_reading_stdin(self):
        challenge = {"status": "human_input_required", "captcha_image": "/private/new.png"}
        with patch.object(login, "AuthSession", return_value=self.client), \
                patch.object(self.client, "reuse", return_value=None), \
                patch.object(self.client, "login_auto", side_effect=login.AuthError("验证码自动识别失败")) as auto, \
                patch.object(self.client, "captcha", return_value=challenge) as fetch, \
                patch.object(login.sys.stdin, "isatty", return_value=False), \
                patch.object(self.client, "login") as submit, \
                patch("builtins.input", side_effect=AssertionError("must not wait on stdin")):
            with self.assertRaisesRegex(login.AuthError, "验证码自动识别失败"):
                login.main(["login"])
        auto.assert_called_once_with()
        submit.assert_not_called()
        fetch.assert_not_called()

    def test_interactive_path_is_output_before_waiting(self):
        challenge = {"status": "human_input_required", "captcha_image": "/private/new.png"}
        out = io.StringIO()
        def human_input(prompt):
            self.assertIn(challenge["captcha_image"], out.getvalue())
            return "user-entered-captcha"
        with patch.object(login, "AuthSession", return_value=self.client), \
                patch.object(self.client, "captcha", return_value=challenge), \
                patch.object(self.client, "reuse", side_effect=AssertionError("force must skip session")), \
                patch.object(self.client, "login_auto", side_effect=login.AuthError("识别失败")), \
                patch.object(self.client, "login", return_value={"authenticated": True}) as submit, \
                patch.object(login.sys.stdin, "isatty", return_value=True), \
                patch("builtins.input", side_effect=human_input), contextlib.redirect_stdout(out):
            login.main(["login", "--force"])
        submit.assert_called_once_with("user-entered-captcha")

    def test_valid_session_does_not_get_new_captcha(self):
        out = io.StringIO()
        with patch.object(login, "AuthSession", return_value=self.client), \
                patch.object(self.client, "reuse", return_value={"authenticated": True, "method": "saved-session"}), \
                patch.object(self.client, "captcha") as fetch, contextlib.redirect_stdout(out):
            login.main(["login"])
        fetch.assert_not_called()
        self.assertEqual(json.loads(out.getvalue())["method"], "saved-session")

    def test_login_has_no_manual_captcha_option(self):
        with patch.object(login, "AuthSession", return_value=self.client), \
                patch.object(self.client, "login_auto", return_value={"authenticated": True}) as auto, \
                contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                login.main(["login", "--captcha", "AB12"])
        auto.assert_not_called()

    def test_modified_ciphertext_is_rejected(self):
        path = self.client.config_dir / "credentials.enc"
        path.write_bytes(b"invalid-ciphertext")
        with self.assertRaises(login.CredentialError):
            login.load_credentials(self.client.config_dir)

    def test_missing_key_does_not_fall_back_to_plaintext(self):
        with patch.object(login, "_key", side_effect=login.CredentialError("key missing")):
            with self.assertRaises(login.CredentialError):
                login.load_credentials(self.client.config_dir)

    def test_missing_pygobject_reports_interpreter(self):
        real_import = builtins.__import__

        def fake_import(name, *args, **kwargs):
            if name == "gi":
                raise ImportError("gi missing")
            return real_import(name, *args, **kwargs)

        with patch("builtins.__import__", side_effect=fake_import):
            with self.assertRaisesRegex(login.CredentialError, "PyGObject"):
                login._secret()

    def test_encrypted_credentials_have_private_permissions(self):
        path = self.client.config_dir / "credentials.enc"
        self.assertEqual(path.stat().st_mode & 0o777, 0o600)
        self.assertEqual(path.parent.stat().st_mode & 0o777, 0o700)
        self.assertNotIn(b"synthetic-secret", path.read_bytes())
        self.assertEqual(login.load_credentials(self.client.config_dir)["username"], "sample")

    def test_status_validates_session_without_decrypting_credentials(self):
        self.client.save_session({"usercode": "synthetic-usercode"})
        auth = {"code": 200, "data": {"code": "synthetic-usercode", "number": "TEST", "range": ["文档管理"]}}
        with patch.object(self.client, "open", return_value=response(auth)), \
                patch.object(login, "load_credentials", side_effect=AssertionError("status must not decrypt")):
            report = self.client.status()
        self.assertEqual(report["method"], "saved-session")
        self.assertNotIn("synthetic-usercode", json.dumps(report))


if __name__ == "__main__":
    unittest.main()
