import importlib.util
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "calculate_hours.py"
SPEC = importlib.util.spec_from_file_location("calculate_hours", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def day(start="09:00:00", end="18:00:00", workflow=None, workday=True):
    return {
        "date": "2026-09-07",
        "isWorkDay": workday,
        "signInfo": [
            {"title": "上班打卡", "signTime": start},
            {"title": "下班打卡", "signTime": end},
        ],
        "workflow": workflow or [],
    }


class AttendanceHoursTest(unittest.TestCase):
    def test_normal_day_and_overtime_boundary(self):
        for end, expected in [
            ("18:00:00", "8.0"),
            ("20:59:00", "8.0"),
            ("21:00:00", "10.0"),
            ("21:05:00", "10.1"),
        ]:
            with self.subTest(end=end):
                result = MODULE.calculate(day(end=end), "2026-09-07")
                self.assertEqual(result["status"], "ready")
                self.assertEqual(result["hours"], expected)

    def test_short_span_requires_user_hours(self):
        result = MODULE.calculate(day(end="17:59:00"), "2026-09-07")
        self.assertEqual(result["status"], "review")
        self.assertIsNone(result["hours"])

    def test_missing_punch_and_leave_require_review(self):
        missing = MODULE.calculate(day(end="未打卡"), "2026-09-07")
        leave = MODULE.calculate(day(workflow=[{"title": "加班调休假"}]), "2026-09-07")
        self.assertEqual(missing["status"], "review")
        self.assertEqual(leave["status"], "review")

    def test_non_workday_and_cross_midnight_require_review(self):
        self.assertEqual(MODULE.calculate(day(workday=False), "2026-09-07")["status"], "review")
        self.assertEqual(MODULE.calculate(day(start="21:00:00", end="09:00:00"), "2026-09-07")["status"], "review")


if __name__ == "__main__":
    unittest.main()
