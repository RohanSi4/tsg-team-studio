# Common Hour data notes

Each gzip file contains a UTF-8 CSV with column headers. Session dates cover January 1 through April 30, 2026. All timestamps are local Virginia wall time. Reservations may precede January 1.

| File | One row per | Fields |
| --- | --- | --- |
| studios.csv.gz | Studio | `studio_id` identifies a location. `city` is its market, `specialty` is its class type, and `seats` is the capacity for each of its sessions. |
| members.csv.gz | Member account in the export | `member_id` identifies an account across sessions. `city` is its home market and `acquisition_channel` is how it was acquired. |
| sessions.csv.gz | Scheduled class | `session_id` identifies the class. `studio_id` links it to a location. `starts_at` is the scheduled start and `checkin_method` records paper or app attendance collection. |
| requests.csv.gz | Member requesting a particular session | `request_id` identifies the request. `session_id` and `member_id` link to the other exports. `requested_at` is when the request arrived. `outcome` is its final recorded state. |

**Outcome definitions.** The original reservation system confirms requests in arrival order up to capacity. It keeps later requests on a waitlist and does not promote them after cancellations. A confirmed place can end as attended, cancelled, no_show, or unrecorded. Unrecorded means the desk did not report whether the member came. Waitlisted means the person never received a confirmed place.

**What the snapshot can tell you.** A session can have more requests than seats. Count distinct members when reporting people and specify your denominator for rates. Booking demand, confirmed places, and observed attendance answer different questions. Cancellation times, calls to the desk, prices, costs, member opinions, and reasons for absence were never collected. Describe how you would validate any conclusion that depends on them.

**Rebuilding.** The distributed exports are synthetic and contain structured variation across studios, times, and recording methods. To regenerate them, run `python3 data/generate.py` from the project root. The script uses a fixed seed. Reload with `python3 explore.py` after regenerating.
