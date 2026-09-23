#!/usr/bin/env python3
"""Inspect, save, verify, and submit UnionTech OA work hours.

The CLI keeps credentials and raw API responses in memory. Machine-readable
results go to stdout; errors go to stderr through argparse/SystemExit.

Examples:
  python scripts/workhours.py inspect --start 2026-09-01 --end 2026-09-22
  python scripts/workhours.py save-drafts --input /tmp/workhours-plan.json
  python scripts/workhours.py save-drafts --input /tmp/workhours-plan.json --apply
  python scripts/workhours.py submit --input /tmp/workhours-plan.json --apply --confirm-submit
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from zoneinfo import ZoneInfo

import auth_session
import calculate_hours
import requests


BI_API = f"{auth_session.BI_BASE}/oa-bi"
WORKHOURS_WEB_URL = f"{auth_session.OA_BASE}/wui/ChanYanWorkHour.html"
DAY_FIELDS = ("one", "two", "three", "four", "five", "six", "seven")
LINE_DATE = re.compile(r"^(\d{4}-\d{2}-\d{2})\s+(.+?)\s*$")


def parse_date(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError) as error:
        raise ValueError(f"日期必须为 YYYY-MM-DD：{value!r}") from error


def week_bounds(day):
    monday = day - timedelta(days=day.weekday())
    return monday, monday + timedelta(days=6)


def iter_weeks(start, end):
    current = week_bounds(start)[0]
    while current <= end:
        yield current, current + timedelta(days=6)
        current += timedelta(days=7)


def process_code(day):
    iso = day.isocalendar()
    return f"{iso.year}{iso.week:02d}"


def decimal_hours(value):
    try:
        number = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as error:
        raise ValueError(f"工时不是有效数字：{value!r}") from error
    if number <= 0 or number > 24:
        raise ValueError(f"工时必须大于 0 且不超过 24：{value!r}")
    return number.quantize(Decimal("0.1"))


def find_day(row, target):
    for field in DAY_FIELDS:
        item = row.get(field) or {}
        if item.get("workHourDay") == target.isoformat():
            return item
    return None


def dated_content(content, monday, sunday):
    """Return target-week dated lines, silently dropping inherited cross-week lines."""
    entries = {}
    for raw_line in (content or "").splitlines():
        line = raw_line.strip()
        match = LINE_DATE.match(line)
        if not match:
            continue
        try:
            line_day = parse_date(match.group(1))
        except ValueError:
            continue
        if monday <= line_day <= sunday:
            entries[line_day] = match.group(2)
    return entries


def normalize_content(value):
    text = " ".join(str(value).split()).strip(" ，,;；")
    if not text:
        raise ValueError("工作内容不能为空")
    return text + "，"


def merge_week_content(existing, monday, sunday, additions):
    entries = dated_content(existing, monday, sunday)
    for target, content in additions.items():
        normalized = normalize_content(content)
        old = entries.get(target)
        if old:
            old_text = old.strip(" ，,;；")
            old_parts = [part.strip(" ，,;；") for part in re.split(r"[；;]", old_text) if part.strip(" ，,;；")]
            new_part = normalized.strip(" ，,;；")
            if new_part != old_text and new_part not in old_parts:
                entries[target] = "；".join(old_parts + [new_part]) + "，"
        else:
            entries[target] = normalized
    return "\n".join(f"{day.isoformat()} {entries[day]}" for day in sorted(entries))


class WorkhoursClient:
    def __init__(self, session, token):
        self.session = session
        self.headers = {"token": token}

    @classmethod
    def authenticated(cls, config_dir=None):
        session, token, _user = auth_session.authenticate_shared(config_dir)
        return cls(session, token)

    def _bi_get(self, path, **params):
        response = self.session.get(BI_API + path, headers=self.headers, params=params, timeout=30)
        response.raise_for_status()
        body = response.json()
        if body.get("code") != 0:
            raise RuntimeError(f"BI 查询失败：{body.get('msg') or body.get('code')}")
        return body.get("result")

    def calendar(self, start, end):
        return self._bi_get(
            "/sys/workHourReportForm/getCalendarWorkHourGroupByUserAndDate",
            startDate=start.isoformat(), endDate=end.isoformat(), sourceType=0,
        ) or []

    def week(self, monday, sunday):
        return self._bi_get(
            "/sys/sysworkhour/getWorkHourWeekOrLastWeek",
            sourceType=0, flag=0,
            startDate=monday.isoformat(), endDate=sunday.isoformat(),
        ) or []

    def attendance_month(self, month):
        response = self.session.post(
            f"{auth_session.OA_BASE}/api/kq/myattendance/getHrmKQMonthReportInfo",
            data={"typevalue": month, "loaddata": "1", "type": "2"}, timeout=30,
        )
        response.raise_for_status()
        body = response.json()
        if body.get("api_status") is not True or not isinstance(body.get("result"), dict):
            raise RuntimeError(f"OA 考勤月历查询失败：{month}")
        return body["result"]

    def save(self, payload):
        response = self.session.post(
            BI_API + "/sys/sysworkhour/save", headers=self.headers, json=payload, timeout=30,
        )
        response.raise_for_status()
        body = response.json()
        if body.get("code") != 0:
            raise RuntimeError(f"工时写入失败：{body.get('msg') or body.get('code')}")


def attendance_by_date(client, dates):
    months = {}
    result = {}
    for target in dates:
        month = target.strftime("%Y-%m")
        if month not in months:
            months[month] = client.attendance_month(month)
        day = months[month].get(str(target.day))
        calculated = calculate_hours.calculate(day, target.isoformat())
        result[target] = calculated
    return result


def public_task(row):
    return {
        "project_id": row.get("projectId"),
        "project_name": row.get("projectName"),
        "task_id": row.get("taskId"),
        "task_name": row.get("taskName"),
        "task_status": row.get("taskStatus"),
        "stage": row.get("projectStageName"),
    }


def inspect_range(client, start, end):
    calendar = sorted(client.calendar(start, end), key=lambda item: item.get("workHourDay") or "")
    incomplete = []
    targets = []
    for item in calendar:
        target = parse_date(item.get("workHourDay"))
        missing = Decimal(str(item.get("notFillHours") or 0))
        if (item.get("notRequestedFill") is None and missing > 0
                and item.get("finishPercent") not in ("100%", "100")):
            targets.append(target)
            incomplete.append({
                "date": target.isoformat(),
                "should_hours": item.get("shouldHours"),
                "filled_hours": item.get("havedHours"),
                "missing_hours": item.get("notFillHours"),
            })
    calculated = attendance_by_date(client, targets) if targets else {}
    for item in incomplete:
        item["attendance"] = calculated[parse_date(item["date"])]

    tasks = {}
    lookup_start = week_bounds(start)[0] - timedelta(days=56)
    for monday, sunday in iter_weeks(lookup_start, end):
        for row in client.week(monday, sunday):
            key = (row.get("projectId"), row.get("taskId"))
            if row.get("taskStatus") == 1:
                tasks[key] = public_task(row)
    return {
        "web_url": WORKHOURS_WEB_URL,
        "range": {"start": start.isoformat(), "end": end.isoformat()},
        "incomplete": incomplete,
        "active_recent_tasks": list(tasks.values()),
    }


def load_plan(path):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"无法读取计划文件 {path}：{error}") from error
    if not isinstance(data, dict) or not isinstance(data.get("entries"), list) or not data["entries"]:
        raise ValueError("计划必须包含非空 entries 数组")
    try:
        project_id = int(data["project_id"])
        task_id = int(data["task_id"])
    except (KeyError, TypeError, ValueError) as error:
        raise ValueError("计划必须包含整数 project_id 和 task_id") from error
    entries = []
    seen = set()
    for raw in data["entries"]:
        if not isinstance(raw, dict):
            raise ValueError("entries 中每项都必须是对象")
        target = parse_date(raw.get("date"))
        if target in seen:
            raise ValueError(f"计划包含重复日期：{target}")
        seen.add(target)
        entries.append({
            "date": target,
            "content": normalize_content(raw.get("content", "")),
            "hours": decimal_hours(raw["hours"]) if raw.get("hours") is not None else None,
        })
    return {"project_id": project_id, "task_id": task_id, "entries": entries}


def task_row(rows, project_id, task_id):
    matches = [row for row in rows if row.get("projectId") == project_id and row.get("taskId") == task_id]
    if len(matches) > 1:
        raise RuntimeError(f"同一周返回多个相同项目/任务记录：{project_id}/{task_id}")
    return matches[0] if matches else None


def find_task_template(client, monday, project_id, task_id):
    for offset in range(1, 9):
        old_monday = monday - timedelta(days=7 * offset)
        row = task_row(client.week(old_monday, old_monday + timedelta(days=6)), project_id, task_id)
        if row and row.get("taskStatus") == 1:
            return row
    raise RuntimeError(
        f"目标周及前 8 周均找不到可沿用的有效项目/任务：{project_id}/{task_id}；请先核对任务"
    )


def payload_item(row, target, hours, content, monday, sunday, existing, status):
    return {
        "id": existing.get("id") if existing else None,
        "submitNew": (existing.get("submitNew") or "new") if existing else "new",
        "approveIdOne": row.get("approveIdOne"),
        "approveNameOne": row.get("approveNameOne"),
        "projectId": row.get("projectId"),
        "projectCode": row.get("projectCode"),
        "projectName": row.get("projectName"),
        "taskId": row.get("taskId"),
        "taskName": row.get("taskName"),
        "taskCode": row.get("taskCode"),
        "taskType": row.get("taskType"),
        "workContent": content,
        "projectStageType": row.get("projectStageType"),
        "projectStageName": row.get("projectStageName"),
        "sourceType": 0,
        "workHourDay": target.isoformat(),
        "hours": f"{hours:.2f}" if status == 1 else float(hours),
        "firstDayWeek": monday.isoformat(),
        "lastDayDeek": sunday.isoformat(),
        "processCode": process_code(target),
        "status": status,
        "startLog": status,
        "saveUpdateFlag": status,
    }


def prepare_groups(client, plan, submit=False):
    automatic = attendance_by_date(client, [entry["date"] for entry in plan["entries"] if entry["hours"] is None])
    grouped = defaultdict(list)
    for entry in plan["entries"]:
        hours = entry["hours"]
        if hours is None:
            result = automatic[entry["date"]]
            if result.get("status") != "ready":
                raise RuntimeError(f"{entry['date']} 无法自动计算工时：{result.get('reason')}")
            hours = decimal_hours(result["hours"])
        grouped[week_bounds(entry["date"])].append({**entry, "hours": hours})

    prepared = []
    for (monday, sunday), entries in sorted(grouped.items()):
        rows = client.week(monday, sunday)
        current = task_row(rows, plan["project_id"], plan["task_id"])
        row = current or find_task_template(client, monday, plan["project_id"], plan["task_id"])
        if row.get("taskStatus") != 1:
            raise RuntimeError("所选项目任务当前不是有效状态")
        additions = {entry["date"]: entry["content"] for entry in entries}
        content = merge_week_content(current.get("workContent") if current else "", monday, sunday, additions)
        payload = []
        for entry in entries:
            existing = find_day(current, entry["date"]) if current else None
            old_status = str(existing.get("status")) if existing else None
            if submit:
                if not existing or old_status != "0" or not existing.get("id"):
                    raise RuntimeError(f"{entry['date']} 不是已回读的可提交草稿")
            elif existing and old_status != "0":
                raise RuntimeError(f"{entry['date']} 已非可编辑草稿，状态为 {old_status}")
            payload.append(payload_item(
                row, entry["date"], entry["hours"], content, monday, sunday,
                existing, 1 if submit else 0,
            ))
        prepared.append({
            "monday": monday,
            "sunday": sunday,
            "row": row,
            "content": content,
            "entries": entries,
            "payload": payload,
        })
    return prepared


def verify_groups(client, plan, groups, expected_status):
    verified = []
    for group in groups:
        row = task_row(client.week(group["monday"], group["sunday"]), plan["project_id"], plan["task_id"])
        if not row or row.get("workContent") != group["content"]:
            raise RuntimeError(f"{group['monday']} 至 {group['sunday']} 工作内容回读不一致")
        for entry in group["entries"]:
            actual = find_day(row, entry["date"])
            expected_hours = f"{entry['hours']:.2f}"
            if (not actual or not actual.get("id") or str(actual.get("status")) != str(expected_status)
                    or actual.get("hours") != expected_hours):
                raise RuntimeError(f"{entry['date']} 回读校验失败")
            verified.append({
                "date": entry["date"].isoformat(),
                "hours": actual.get("hours"),
                "status": "draft" if expected_status == 0 else "submitted",
                "record_id": actual.get("id"),
            })
    return verified


def public_preview(plan, groups, mode, applied=False, verified=None):
    row = groups[0]["row"]
    return {
        "web_url": WORKHOURS_WEB_URL,
        "mode": mode,
        "applied": applied,
        "task": public_task(row),
        "weeks": [
            {
                "start": group["monday"].isoformat(),
                "end": group["sunday"].isoformat(),
                "work_content": group["content"],
                "entries": [
                    {"date": item["date"].isoformat(), "hours": str(item["hours"])}
                    for item in group["entries"]
                ],
            }
            for group in groups
        ],
        "verified": verified or [],
    }


def run_write(client, args, submit=False):
    plan = load_plan(args.input)
    groups = prepare_groups(client, plan, submit=submit)
    if not args.apply:
        return public_preview(plan, groups, "submit-preview" if submit else "draft-preview")
    if submit and not args.confirm_submit:
        raise RuntimeError("提交需要同时提供 --apply 和 --confirm-submit")
    verified = []
    for group in groups:
        client.save(group["payload"])
        verified.extend(verify_groups(client, plan, [group], 1 if submit else 0))
    return public_preview(
        plan, groups, "submitted" if submit else "draft-saved", applied=True, verified=verified,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--config-dir", help="共享 OA 凭据目录；默认遵循 UNIONTECH_OA_CONFIG_DIR")
    sub = parser.add_subparsers(dest="command", required=True)

    inspect_parser = sub.add_parser("inspect", help="查询日期范围内未填工时、考勤计算和近期有效任务")
    inspect_parser.add_argument("--start", required=True, help="起始日期 YYYY-MM-DD")
    inspect_parser.add_argument("--end", help="结束日期 YYYY-MM-DD；默认今天之前")

    for name, help_text in (
        ("save-drafts", "预览或保存草稿并回读"),
        ("submit", "预览或提交已回读草稿并回读"),
    ):
        command = sub.add_parser(name, help=help_text)
        command.add_argument("--input", required=True, help="JSON 计划文件")
        command.add_argument("--apply", action="store_true", help="执行写入；省略时只输出预览")
        if name == "submit":
            command.add_argument(
                "--confirm-submit", action="store_true",
                help="确认用户已在草稿回读后单独授权提交；仅与 --apply 一起有效",
            )

    sub.add_parser("web-url", help="输出 OA 工时填报网页地址")
    args = parser.parse_args()
    try:
        if args.command == "web-url":
            output = {"web_url": WORKHOURS_WEB_URL}
        else:
            client = WorkhoursClient.authenticated(args.config_dir)
            if args.command == "inspect":
                start = parse_date(args.start)
                end = parse_date(args.end) if args.end else datetime.now(ZoneInfo("Asia/Shanghai")).date() - timedelta(days=1)
                if end < start:
                    raise ValueError("结束日期不能早于起始日期")
                output = inspect_range(client, start, end)
            else:
                output = run_write(client, args, submit=args.command == "submit")
        print(json.dumps(output, ensure_ascii=False, indent=2))
    except (ValueError, RuntimeError, requests.RequestException) as error:
        print(json.dumps({"error": str(error), "web_url": WORKHOURS_WEB_URL}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
