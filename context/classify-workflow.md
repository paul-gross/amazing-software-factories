# Running classification

Classification names what each watched repository is: an **assembly line** (a factory building itself), a project
**built by an assembly line**, an **agent-assisted** project (a person building with agents, session by session), or
**not software**. The gate only shows that work lands through the night, which a person leaving agents running can
also do, so the classifier decides whether a system or a person drives the work. Until it does, a watched repository is neither
measured nor listed: only assembly lines and what they build are. Run it after the gate has admitted new repositories;
an unmeasured one is described to the classifier by the numbers it passed the gate with.

It runs on a local machine, not in GitHub Actions: each repository is one call to the `claude` command, signed in to a
Claude subscription, at roughly the cost of a short conversation.

## Run it

From the repository root, with a clean working tree:

1. `git pull --rebase`
2. `nice -n 15 python3 -m asf classify`: classifies every watched repository whose stored answer is missing or from
   an older classifier version, four at a time, saving every twenty answers, so a stopped run picks up what is left.
   `classify 50` does a fixed random sample of 50 instead, to review a new prompt before running it on everything. A
   line starting `kind ` is one repository the classifier could not answer for; the next run retries it. Until the
   current version reads a repository, its answer from an older version stands.
3. `python3 -m asf render`: the README and the site pick up the new kinds.
4. `python3 -m unittest discover -s tests -q`
5. `scripts/publish.sh "data: classify watched repositories <date>"`: commits what changed and pushes. If the
   hourly workflow pushed meanwhile, it rebases onto that and renders the README and site again before pushing.

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
kind = "not-software"          # or "assembly line", "built by an assembly line", "agent-assisted", "copy"
reason = "One line a reader will see"
```

Render again (`python3 -m asf render`) and commit the annotation with the rendered files.
