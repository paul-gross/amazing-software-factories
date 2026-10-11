# Running classification

Classification names what each watched repository is: an **assembly line** (a factory building itself), a project
**built by an assembly line**, or **not software**. Whether a repository runs without people is already settled by the
gate before it is watched, so the classifier only decides what it is. Until it does, a watched repository is neither
measured nor listed: only assembly lines and what they build are. Run it after the gate has admitted new repositories;
an unmeasured one is described to the classifier by the numbers it passed the gate with.

It runs on a local machine, not in GitHub Actions: each repository is one call to the `claude` command, signed in to a
Claude subscription, at roughly the cost of a short conversation.

## Run it

From the repository root, with a clean working tree:

1. `git pull --rebase`
2. `nice -n 15 python3 -m asf classify`: classifies every watched repository whose stored answer is missing or from
   an older classifier version, four at a time. A line starting `kind ` is one repository the classifier could not
   answer for; the next run retries it. With nothing waiting it prints nothing and exits.
3. `python3 -m asf render`: the README and the site pick up the new kinds.
4. `python3 -m unittest discover -s tests -q`
5. If anything changed, commit `data/kinds.jsonl`, `docs/`, `README.md` and `reports/` with a message like
   `data: classify watched repositories <date>`, and push.

Report back how many repositories were classified, the count per kind, and any that failed.

## Before running

- `claude --version` succeeds and the subscription is signed in.
- Nothing uncommitted: the pull rebases.

## How it decides

[asf/kind.py](../asf/kind.py) holds the prompt and the evidence: description, topics, top-level entries, the first
8,000 characters of the README, the newest 20 commits with bodies and authors, and the measured numbers. Repository
text goes to the model as data, from an empty directory, with no tools. Each answer is stored with the classifier's
`VERSION`; changing the prompt means raising `VERSION`, and the next run classifies everything again.

## Correcting a classification

A hand entry in [data/annotations.toml](../data/annotations.toml) always wins over the classifier:

```toml
[repo."owner/name"]
kind = "not-software"          # or "assembly line", "built by an assembly line", "copy"
reason = "One line a reader will see"
```

Render again (`python3 -m asf render`) and commit the annotation with the rendered files.
