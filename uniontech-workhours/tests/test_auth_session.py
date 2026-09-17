import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

import requests


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "auth_session.py"
SPEC = importlib.util.spec_from_file_location("auth_session", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class FakeResponse:
    def __init__(self, body=None, text=""):
        self.body = body or {}
        self.text = text

    def raise_for_status(self):
        pass

    def json(self):
        return self.body


class FakeSession:
    def __init__(self):
        self.cookies = requests.cookies.RequestsCookieJar()
        self.calls = []

    def post(self, url, **kwargs):
        self.calls.append(("POST", url, kwargs))
        if url.endswith("/checkLogin"):
            self.cookies.set("loginidweaver", "test-only", domain="oa.uniontech.com")
            return FakeResponse()
        if url.endswith("/workHourUser"):
            return FakeResponse({"code": 0, "token": "test-token"})
        raise AssertionError(url)

    def get(self, url, **kwargs):
        self.calls.append(("GET", url, kwargs))
        if url.endswith("/getAccount"):
            return FakeResponse({"data": {"userid": 1}})
        if url.endswith("/getUserRedirectBi"):
            return FakeResponse(text='"encrypted-login-name"')
        raise AssertionError(url)


class SharedAuthenticationTest(unittest.TestCase):
    def test_credential_format_matches_shared_store(self):
        with tempfile.TemporaryDirectory() as temporary:
            self.assertIsNone(MODULE.load_credentials(temporary))
            MODULE.save_credentials("test-user", "test-password", temporary)
            self.assertEqual(MODULE.load_credentials(temporary), ("test-user", "test-password"))
            saved = json.loads((Path(temporary) / "default.json").read_text())
            self.assertEqual(set(saved), {"loginid", "password_encrypted", "saved_at", "metadata"})
            self.assertNotIn("test-password", (Path(temporary) / "default.json").read_text())
            self.assertEqual((Path(temporary) / "default.json").stat().st_mode & 0o777, 0o600)

    def test_oa_and_bi_login_chain(self):
        fake = FakeSession()
        session, token, user = MODULE.authenticate("test-user", "test-password", fake)
        self.assertIs(session, fake)
        self.assertEqual(token, "test-token")
        self.assertEqual(user["userid"], 1)
        self.assertEqual([call[0] for call in fake.calls], ["POST", "GET", "GET", "POST"])
        self.assertEqual(fake.calls[-1][2]["json"], {"loginName": "encrypted-login-name"})


if __name__ == "__main__":
    unittest.main()
