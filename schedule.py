import json
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path


def load_schedule():
    schedule_path = Path(__file__).with_name("schedule.json")
    with schedule_path.open(encoding="utf-8") as schedule_file:
        return json.load(schedule_file)


def filter_by_date(events, target_date):
    return sorted(
        (event for event in events if date.fromisoformat(event["start"][:10]) == target_date),
        key=lambda event: event["start"],
    )


def format_event(event):
    start = datetime.fromisoformat(event["start"]).strftime("%H:%M")
    end = datetime.fromisoformat(event["end"]).strftime("%H:%M")
    location = event.get("location") or "（場所なし）"
    location = f"  @{location}"
    return f"{start}-{end}  {event['title']}{location}"


def main():
    if len(sys.argv) > 2:
        print("日付は1つだけ指定してください。")
        return 1

    try:
        target_date = (
            date.fromisoformat(sys.argv[1])
            if len(sys.argv) == 2
            else datetime.now(timezone(timedelta(hours=9))).date()
        )
    except ValueError:
        print("日付は YYYY-MM-DD の形式で指定してください。")
        return 1

    try:
        events = load_schedule()
    except FileNotFoundError:
        print("schedule.json が見つかりません。同じフォルダに配置してください。")
        return 1

    matching_events = filter_by_date(events, target_date)
    print(f"{target_date.isoformat()} の予定 {len(matching_events)} 件")
    for event in matching_events:
        print(format_event(event))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
