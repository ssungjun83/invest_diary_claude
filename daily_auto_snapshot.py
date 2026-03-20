import argparse
from datetime import date

import app


def _parse_date(text: str) -> date:
    value = (text or "").strip()
    if not value:
        return date.today()
    return date.fromisoformat(value)


def main() -> int:
    parser = argparse.ArgumentParser(description="투자일기 일일 자동 주가갱신/스냅샷 저장")
    parser.add_argument("--date", dest="target_date", default="", help="실행 기준일 (YYYY-MM-DD), 기본값: 오늘")
    parser.add_argument("--force", action="store_true", help="시간/실행이력 조건 무시하고 강제 실행")
    args = parser.parse_args()

    try:
        target_date = _parse_date(args.target_date)
    except Exception as exc:
        print(f"[ERROR] 날짜 형식이 올바르지 않습니다: {exc}")
        return 2

    conn = app.get_conn()
    conn.close()
    app.initialize_api_settings(force=True)

    ok, msg = app.run_daily_auto_snapshot(force=bool(args.force), target_date=target_date)
    if msg:
        print(msg)
    else:
        print("자동 실행 스킵: 아직 실행 조건이 아닙니다.")

    if ok:
        return 0
    if msg:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
