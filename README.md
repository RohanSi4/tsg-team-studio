# Common Hour | 30-minute TSG team challenge

**3–5 developers · 30 minutes including setup · one shared change**

Common Hour is a fictional Charlottesville startup that handles reservations for fitness studios. A studio manager opens the schedule before the doors open. It shows class times, seat counts, and booking requests. The founder asks: **“What could we change today that would make this schedule more useful to someone at the studio?”**

Choose who you want to help and what they should be able to tell or do. By minute 30, demo one working change using one class from the sample data.

## 0–5 min · Get it running

One teammate shares their screen and runs the commands below with Git and Python 3.8+. If your team already has a fork, clone its URL instead. Everyone can work together in one checkout.

```sh
git clone https://github.com/RohanSi4/tsg-team-studio.git
cd tsg-team-studio
python3 explore.py
python3 schedule.py
```

Find the 08:00 yoga class. It has 20 seats and 21 requests. What would a staff member still need to know? A request can end in attendance, cancellation, a no-show, a waitlist place, or an unrecorded outcome.

## 5–8 min · Pick one change

Give everyone a chance to pitch an idea. Pick one you can show in a single terminal run. In [TEAM.md](TEAM.md), finish the sentence “A ___ needs to ___” and write one example of the output you expect. If you're stuck, try flagging classes where requests exceed seats. Your own idea is welcome.

## 8–22 min · Build together

Start in [schedule.py](schedule.py). The SQL in `daily_schedule` selects the records. The loop in `main` controls what a person sees. The [data notes](data/README.md) explain the fields if you need another one.

One person drives, one traces a real class through the data, and one checks the result against your example. With four or five, have a teammate sketch the output and another find a case where it should behave differently. Switch drivers halfway through so a second person works on the change.

## 22–27 min · Hand it to a teammate

Have someone other than the last driver run the feature. Check your original example and one contrasting case. For instance, studio 1 on January 15 has classes both above and below capacity by request count. Fix the most important mismatch and record what your teammate observed in TEAM.md.

## 27–30 min · Demo

Give a one-minute demo. Name your user, run the change, and point to one result that helps them. Save your code and the three lines in TEAM.md. A local commit is enough for this exercise. Teams using GitHub can share a single pull request from their fork.
