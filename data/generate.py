"""Rebuild the fictional Common Hour exports with Python's standard library."""
import csv
import gzip
import io
import random
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
rng = random.Random(6421)
first_day = date(2026, 1, 1)
regions = ["Charlottesville", "Richmond", "Roanoke"]
activities = ["yoga", "cycling", "strength", "dance"]


def export(name, columns, rows):
    with (ROOT / (name + ".csv.gz")).open("wb") as raw:
        with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0) as packed:
            with io.TextIOWrapper(packed, encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream, lineterminator="\n")
                writer.writerow(columns.split())
                writer.writerows(rows)


sites = [(i, regions[(i - 1) % 3], activities[(i - 1) % 4], rng.choice([12, 16, 20, 24]))
         for i in range(1, 25)]
export("studios", "studio_id city specialty seats", sites)
members = [(i, rng.choice(regions), rng.choice(["referral", "walk_in", "search", "partner"]))
           for i in range(1, 6001)]
export("members", "member_id city acquisition_channel", members)
locals_by_city = {city: [m[0] for m in members if m[1] == city] for city in regions}
sessions, requests = [], []
for offset in range(120):
    day = first_day + timedelta(days=offset)
    for studio, city, activity, seats in sites:
        for hour in [8, 12, 18]:
            start = datetime.combine(day, datetime.min.time()).replace(hour=hour)
            session = len(sessions) + 1
            manual = studio % 7 == 0 and offset < 60
            sessions.append((session, studio, start.isoformat(timespec="minutes"), "paper" if manual else "app"))
            demand = {8: 0.80, 12: 0.55, 18: 1.25}[hour]
            if day.weekday() >= 5:
                demand += 0.35 if hour == 8 else -0.25
            count = max(1, round(seats * demand * rng.uniform(0.55, 1.5)))
            users = rng.sample(locals_by_city[city], count)
            leads = sorted((rng.randint(1, 10080) for _ in users), reverse=True)
            for index, (member, lead) in enumerate(zip(users, leads)):
                if index >= seats:
                    outcome = "waitlisted"
                elif rng.random() < 0.07 + 0.10 * (lead > 7200):
                    outcome = "cancelled"
                elif manual and rng.random() < 0.27:
                    outcome = "unrecorded"
                else:
                    outcome = "no_show" if rng.random() < 0.06 + 0.08 * (hour == 8) else "attended"
                requested = start - timedelta(minutes=lead)
                requests.append((len(requests) + 1, session, member, requested.isoformat(timespec="minutes"), outcome))
export("sessions", "session_id studio_id starts_at checkin_method", sessions)
export("requests", "request_id session_id member_id requested_at outcome", requests)
