#!/usr/bin/env python3
"""Calculate proposed OA work hours from a monthly attendance API response.

Read JSON from stdin; never persist the response or print workflow details.
"""

import argparse
import json
import re
import sys
from datetime import date
from decimal import Decimal, ROUND_HALF_UP
from html import unescape


def _time_to_seconds(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{2}:\d{2}(?::\d{2})?", value):
        return None
    parts = [int(part) for part in value.split(":")]
    if len(parts) == 2:
        parts.append(0)
    hour, minute, second = parts
    if hour > 23 or minute > 59 or second > 59:
        return None
    return hour * 3600 + minute * 60 + second


def _one_decimal(value):
    return str(value.quantize(Decimal("0.1"), rounding=ROUND_HALF_UP))


def calculate(day, target_date):
    """Return a proposed hour value or a review reason for one calendar day."""
    result = {"date": target_date, "status": "review", "hours": None}
    if not isinstance(day, dict) or day.get("date") != target_date:
        return {**result, "reason": "考勤日历未返回目标日期"}
    if day.get("isWorkDay") is not True:
        return {**result, "reason": "非工作日或工作日状态不明，需要确认"}

    signs = day.get("signInfo")
    if not isinstance(signs, list) or len(signs) != 2:
        return {**result, "reason": "上下班打卡记录缺失或数量异常，需要确认请假或漏卡"}
    by_title = {entry.get("title"): entry.get("signTime") for entry in signs if isinstance(entry, dict)}
    if len(by_title) != 2 or set(by_title) != {"上班打卡", "下班打卡"}:
        return {**result, "reason": "无法唯一识别上下班打卡，需要确认"}
    start = _time_to_seconds(by_title["上班打卡"])
    end = _time_to_seconds(by_title["下班打卡"])
    if start is None or end is None:
        return {**result, "reason": "存在未打卡或无效时间，需要确认请假或漏卡"}
    if end <= start:
        return {**result, "reason": "打卡跨日或顺序异常，需要确认"}

    span = Decimal(end - start) / Decimal(3600)
    workflows = day.get("workflow") or []
    has_leave = any(
        "请假" in unescape(str(item.get("title", ""))) or "调休假" in unescape(str(item.get("title", "")))
        for item in workflows if isinstance(item, dict)
    )
    if span < 9:
        reason = "打卡跨度不足 9 小时；考勤日历显示请假记录，需要用户明确实际工作时长" if has_leave else "打卡跨度不足 9 小时，可能漏卡或请假，需要用户明确实际工作时长"
        return {**result, "reason": reason, "check_in": by_title["上班打卡"], "check_out": by_title["下班打卡"], "punch_span_hours": _one_decimal(span), "leave_hint": has_leave}
    if has_leave:
        return {**result, "reason": "考勤日历显示请假记录，需要核对实际工作时长", "check_in": by_title["上班打卡"], "check_out": by_title["下班打卡"], "leave_hint": True}

    extra = span - Decimal(9)  # Eight normal work hours plus one-hour break.
    overtime = extra - Decimal(1) if extra >= 3 else Decimal(0)
    hours = Decimal(8) + overtime
    return {
        "date": target_date,
        "status": "ready",
        "check_in": by_title["上班打卡"],
        "check_out": by_title["下班打卡"],
        "hours": _one_decimal(hours),
        "overtime_hours": _one_decimal(overtime),
        "punch_span_hours": _one_decimal(span),
        "rule": "正常下班=上班打卡+9小时；距正常下班满3小时才计加班，再扣1小时吃饭",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="YYYY-MM-DD")
    args = parser.parse_args()
    target = date.fromisoformat(args.date)
    payload = json.load(sys.stdin)
    if not isinstance(payload, dict) or payload.get("api_status") is not True:
        raise SystemExit("考勤月历 API 未返回成功状态")
    days = payload.get("result") if isinstance(payload, dict) else None
    if not isinstance(days, dict):
        raise SystemExit("考勤月历响应缺少 result 对象")
    day = days.get(str(target.day))
    print(json.dumps(calculate(day, args.date), ensure_ascii=False))


if __name__ == "__main__":
    main()
