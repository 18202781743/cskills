import importlib.util
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
SPEC = importlib.util.spec_from_file_location("workhours", SCRIPTS / "workhours.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def task_row(work_content="", day=None):
    empty = {"workHourDay": "", "hours": "", "status": "", "id": ""}
    row = {
        "projectId": 2454,
        "projectCode": "PROJECT",
        "projectName": "DDE",
        "taskId": 4176,
        "taskCode": "TASK",
        "taskName": "DDE",
        "taskStatus": 1,
        "projectStageType": 1,
        "projectStageName": "项目执行阶段",
        "approveIdOne": "internal-approver",
        "approveNameOne": "审批人",
        "taskType": None,
        "workContent": work_content,
    }
    for field in MODULE.DAY_FIELDS:
        row[field] = dict(empty)
    if day:
        row["one"] = day
    return row


class FakeClient:
    def __init__(self, rows=None, attendance=None, calendar=None):
        self.rows = rows or {}
        self.attendance = attendance or {}
        self.calendar_rows = calendar or []
        self.saved = []

    def week(self, monday, sunday):
        return self.rows.get(monday.isoformat(), [])

    def attendance_month(self, month):
        return self.attendance

    def calendar(self, start, end):
        return self.calendar_rows

    def save(self, payload):
        self.saved.append(payload)


class WorkhoursHelpersTest(unittest.TestCase):
    def test_merge_keeps_current_week_and_drops_cross_week_lines(self):
        content = (
            "2026-09-14 原有事项，\n"
            "2026-09-15 已有内容，\n"
            "2026-09-07 上周内容，"
        )
        merged = MODULE.merge_week_content(
            content,
            date(2026, 9, 14),
            date(2026, 9, 20),
            {date(2026, 9, 16): "新增事项"},
        )
        self.assertEqual(
            merged,
            "2026-09-14 原有事项，\n2026-09-15 已有内容，\n2026-09-16 新增事项，",
        )

    def test_merge_same_content_is_idempotent(self):
        content = "2026-09-14 原有事项；完成回归测试，"
        merged = MODULE.merge_week_content(
            content,
            date(2026, 9, 14),
            date(2026, 9, 20),
            {date(2026, 9, 14): "原有事项；完成回归测试"},
        )
        self.assertEqual(merged, content)

    def test_load_plan_rejects_duplicate_dates(self):
        with tempfile.TemporaryDirectory() as temporary:
            plan = Path(temporary) / "plan.json"
            plan.write_text(
                '{"project_id": 1, "task_id": 2, "entries": ['
                '{"date": "2026-09-21", "hours": 8, "content": "A"},'
                '{"date": "2026-09-21", "hours": 8, "content": "B"}]}',
                encoding="utf-8",
            )
            with self.assertRaisesRegex(ValueError, "重复日期"):
                MODULE.load_plan(plan)

    def test_prepare_reuses_existing_draft_id(self):
        monday = date(2026, 9, 21)
        row = task_row(
            "2026-09-21 原内容，",
            {"workHourDay": "2026-09-21", "hours": "", "status": "0", "id": "42", "submitNew": "new"},
        )
        client = FakeClient({monday.isoformat(): [row]})
        plan = {
            "project_id": 2454,
            "task_id": 4176,
            "entries": [{"date": monday, "hours": MODULE.decimal_hours(8), "content": "新增内容，"}],
        }
        groups = MODULE.prepare_groups(client, plan)
        self.assertEqual(groups[0]["payload"][0]["id"], "42")
        self.assertIn("原内容；新增内容，", groups[0]["content"])

    def test_prepare_refuses_submitted_record(self):
        monday = date(2026, 9, 21)
        row = task_row(
            "2026-09-21 原内容，",
            {"workHourDay": "2026-09-21", "hours": "8.00", "status": "1", "id": "42"},
        )
        client = FakeClient({monday.isoformat(): [row]})
        plan = {
            "project_id": 2454,
            "task_id": 4176,
            "entries": [{"date": monday, "hours": MODULE.decimal_hours(8), "content": "新增内容，"}],
        }
        with self.assertRaisesRegex(RuntimeError, "已非可编辑草稿"):
            MODULE.prepare_groups(client, plan)

    def test_automatic_hours_uses_attendance_rules(self):
        monday = date(2026, 9, 21)
        row = task_row()
        attendance = {
            "21": {
                "date": "2026-09-21",
                "isWorkDay": True,
                "signInfo": [
                    {"title": "上班打卡", "signTime": "09:00:00"},
                    {"title": "下班打卡", "signTime": "18:00:00"},
                ],
                "workflow": [],
            }
        }
        client = FakeClient({monday.isoformat(): [row]}, attendance)
        plan = {
            "project_id": 2454,
            "task_id": 4176,
            "entries": [{"date": monday, "hours": None, "content": "新增内容，"}],
        }
        groups = MODULE.prepare_groups(client, plan)
        self.assertEqual(groups[0]["entries"][0]["hours"], MODULE.decimal_hours("8.0"))

    def test_submit_uses_two_decimal_string_and_requires_draft(self):
        monday = date(2026, 9, 21)
        row = task_row(
            "2026-09-21 原内容，",
            {"workHourDay": "2026-09-21", "hours": "8.00", "status": "0", "id": "42"},
        )
        client = FakeClient({monday.isoformat(): [row]})
        plan = {
            "project_id": 2454,
            "task_id": 4176,
            "entries": [{"date": monday, "hours": MODULE.decimal_hours(8), "content": "原内容，"}],
        }
        payload = MODULE.prepare_groups(client, plan, submit=True)[0]["payload"]
        self.assertEqual(len(payload), 7)
        self.assertEqual(payload[0]["hours"], "8.00")
        self.assertEqual((payload[0]["status"], payload[0]["startLog"], payload[0]["saveUpdateFlag"]), (1, 1, 1))
        self.assertEqual(payload[0]["sourceType"], "0")
        for empty in payload[1:]:
            self.assertIsNone(empty["hours"])
            self.assertEqual((empty["status"], empty["startLog"], empty["saveUpdateFlag"]), (0, 1, 1))

    def test_submit_refuses_unplanned_draft_hours(self):
        monday = date(2026, 9, 21)
        row = task_row(
            "2026-09-21 计划内容，\n2026-09-22 其他草稿，",
            {"workHourDay": "2026-09-21", "hours": "8.00", "status": "0", "id": "42"},
        )
        row["two"] = {"workHourDay": "2026-09-22", "hours": "8.00", "status": "0", "id": "43"}
        client = FakeClient({monday.isoformat(): [row]})
        plan = {
            "project_id": 2454,
            "task_id": 4176,
            "entries": [{"date": monday, "hours": MODULE.decimal_hours(8), "content": "计划内容，"}],
        }
        with self.assertRaisesRegex(RuntimeError, "未包含在计划中"):
            MODULE.prepare_groups(client, plan, submit=True)

    def test_inspect_excludes_completed_rounding_difference(self):
        monday = date(2026, 9, 21)
        row = task_row()
        calendar = [
            {
                "workHourDay": "2026-09-21",
                "notRequestedFill": None,
                "notFillHours": 0.1,
                "shouldHours": 10.9,
                "havedHours": 10.8,
                "finishPercent": "100%",
            }
        ]
        client = FakeClient({monday.isoformat(): [row]}, calendar=calendar)
        result = MODULE.inspect_range(client, monday, monday)
        self.assertEqual(result["incomplete"], [])


if __name__ == "__main__":
    unittest.main()
