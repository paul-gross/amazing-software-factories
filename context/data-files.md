# The data files

Everything under `data/` is committed. `.cache/` is not: it holds a day's screen reads so a rerun need not repeat them.

| File                         | Holds                                                                                                   |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| `watchlist.jsonl`            | Repositories that passed the gate, one row each, for good: when, from which source, and status (`active`, `dormant`: no commits in its measured window, `archived`, `opted-out`) |
| `screened.jsonl`             | Repositories that passed layers 1 and 2: `waiting` for the gate (with the last gate check's numbers), `admitted`, or `out` (`out_reason: not found` after a week of misses) |
| `latest.jsonl`               | Every watched repository's newest full measurement, rewritten as each is measured                       |
| `daily/<date>.jsonl`         | A compact record per repository per day: grades, headline numbers, the week's commit tally (four-week figures sum these) |
| `snapshots/<date>.jsonl`     | Full rows, kept once a week                                                                             |
| `kinds.jsonl`                | The classifier's answers, with the classifier version that gave them                                    |
| `annotations.toml`           | Hand corrections; they win over the classifier                                                          |
| `manual.txt`                 | Repositories nominated by hand: known factories                                                         |
| `source-lists.txt`           | Curated lists whose repository links are nominated                                                      |
| `judgments/<date>/`          | LLM judges' cold reads                                                                                  |

Rows are keyed by `owner/name` as GitHub spells it; lookups ignore case. Every date is a UTC date.
