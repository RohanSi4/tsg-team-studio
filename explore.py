"""Load the shipped CSV exports into a fresh local SQLite database."""
import csv
import gzip
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCHEMAS = {
    "studios": "studio_id INTEGER PRIMARY KEY, city TEXT, specialty TEXT, seats INTEGER",
    "members": "member_id INTEGER PRIMARY KEY, city TEXT, acquisition_channel TEXT",
    "sessions": "session_id INTEGER PRIMARY KEY, studio_id INTEGER REFERENCES studios, starts_at TEXT, checkin_method TEXT",
    "requests": "request_id INTEGER PRIMARY KEY, session_id INTEGER REFERENCES sessions, member_id INTEGER REFERENCES members, requested_at TEXT, outcome TEXT, UNIQUE(session_id, member_id)",
}


def main():
    with sqlite3.connect(ROOT / "studio.sqlite") as db:
        db.execute("PRAGMA foreign_keys = ON")
        db.execute("BEGIN IMMEDIATE")
        for table in reversed(SCHEMAS):
            db.execute(f"DROP TABLE IF EXISTS {table}")
        for table, schema in SCHEMAS.items():
            db.execute(f"CREATE TABLE {table} ({schema})")
            with gzip.open(ROOT / "data" / f"{table}.csv.gz", "rt", newline="") as stream:
                rows = csv.reader(stream)
                header = next(rows)
                expected = [row[1] for row in db.execute(f"PRAGMA table_info({table})")]
                if header != expected:
                    raise ValueError(f"Unexpected columns in {table}: {header}")
                placeholders = ", ".join("?" for _ in header)
                db.executemany(f"INSERT INTO {table} VALUES ({placeholders})", rows)
            print(table, db.execute(f"SELECT count(*) FROM {table}").fetchone()[0])


if __name__ == "__main__":
    main()
