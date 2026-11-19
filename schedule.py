"""Browse one studio's day. Run python3 explore.py to load the sample data."""
import argparse
import sqlite3
from datetime import date
from pathlib import Path


def daily_schedule(db, studio_id, day):
    return db.execute(
        """
        SELECT s.starts_at, st.specialty, st.seats, COUNT(r.request_id) AS requests
        FROM sessions AS s
        JOIN studios AS st ON st.studio_id = s.studio_id
        LEFT JOIN requests AS r ON r.session_id = s.session_id
        WHERE s.studio_id = ? AND date(s.starts_at) = ?
        GROUP BY s.session_id
        ORDER BY s.starts_at
        """,
        (studio_id, day.isoformat()),
    ).fetchall()


def main():
    parser = argparse.ArgumentParser(description="Show the classes at one studio on one day.")
    parser.add_argument("--studio", type=int, default=1, help="studio ID (default 1)")
    parser.add_argument("--date", type=date.fromisoformat, default=date(2026, 1, 15),
                        help="local date, YYYY-MM-DD (default 2026-01-15)")
    args = parser.parse_args()
    database = Path(__file__).resolve().with_name("studio.sqlite")
    if not database.exists():
        parser.exit(1, "Run python3 explore.py first to load the sample data.\n")
    with sqlite3.connect(database.as_uri() + "?mode=ro", uri=True) as db:
        studio = db.execute("SELECT city FROM studios WHERE studio_id = ?", (args.studio,)).fetchone()
        if studio is None:
            parser.error(f"Studio {args.studio} does not exist in this dataset.")
        rows = daily_schedule(db, args.studio, args.date)
    print(f"Studio {args.studio} · {studio[0]} · {args.date}")
    if not rows:
        print("No classes scheduled for this date.")
        return
    print(f"{'Time':<8}{'Class':<12}{'Seats':>5}{'Requests':>10}")
    for start, activity, seats, requests in rows:
        print(f"{start[11:16]:<8}{activity:<12}{seats:>5}{requests:>10}")


if __name__ == "__main__":
    main()
