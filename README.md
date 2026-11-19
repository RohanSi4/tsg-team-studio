# Common Hour | TSG developer team project

Common Hour is a fictional Charlottesville startup that handles class reservations for independent fitness studios across Virginia. Members reserve spots before class. Studio owners set the schedule, and front-desk staff record attendance. The founder has a small engineering team and enough time to try one improvement with one partner studio.

> “At a partner check-in, one owner asked why people still call the desk after reserving. Another wanted to know whether to keep her noon class. I promised them we'd take a closer look. If I give you our first four months of records and one studio willing to try something, what should we do first?”

Those conversations are leads. You can pursue either, challenge them, or find a better question. Your team owns the problem statement, the technology, and the choice of what to ship. All people, conversations, and operating records in this exercise are fictional.

## Your first meeting

1. Each developer opens the data and brings one observation, one uncertainty, and a question they would ask a studio owner, member, or staffer. Save the query or calculation behind the observation.
2. Compare at least two possible problems. Pick one person you want to help and one decision or task you could improve. Record why the other problem can wait.
3. Fill in [the team brief](TEAM.md) together. Give the founder a way to tell whether a pilot helped. If the exports lack a needed measure, say how the pilot would collect it.

## Open the data

The four compressed CSVs in `data/` are ready to use in any stack. To work in SQL, run this from the repo root with Python 3.8+ and the SQLite CLI. The first command needs only Python and rebuilds the four starter tables in a local database.

```sh
python3 explore.py
sqlite3 studio.sqlite "SELECT city, count(*) AS studios FROM studios GROUP BY city;"
```

Expect eight studios per city. The snapshot contains 24 studios, 6,000 member accounts, 8,640 sessions and 131,799 requests. Read the [data notes](data/README.md) before interpreting a rate. Your product can use a subset if that fits the pilot.

## Working as a team of 3–5

| Checkpoint | Practice | What teammates should be able to see |
| --- | --- | --- |
| Kickoff | Agree on the user, pilot, and scope. Choose who will play the founder for the first check-in. | A shared brief, an evidence query, and questions for the client. |
| First build | Break one user workflow into small issues. Give each an owner, a reviewer, and an observable acceptance check. Agree on a sample input and expected output wherever two pieces meet. | A teammate can run the thinnest working version from a fresh checkout. |
| Feedback | Walk the founder through one realistic case. Ask what they would actually do next. Capture the answer and revise one issue. | A decision tied to feedback, plus a recorded tradeoff. |
| Handoff | Exchange roles and let someone who did not implement the last change run the demo. | Setup instructions, a repeatable check, a known limitation, and the next pilot decision. |

With three people, rotate who gathers evidence, builds the workflow, and verifies it. With four or five, pair on separate issues that meet at the agreed input/output. Rotate reviewers so everyone reads code outside their own piece. Each developer should own a change and review someone else's.

For each issue, create a branch, make a focused change, and open a pull request using the included template. Ask the reviewer to try the acceptance check and an edge case. Merge when someone else can explain what changed and reproduce the result. If working locally, exchange branches and record the review in the team brief.

## Final demo

Start with the user's original task. Show how that person would complete it with what you built, using a record from the dataset. Explain one design decision you changed after review and what the pilot still needs to establish. Leave the founder with a clear next decision and another developer with enough information to run the project.
