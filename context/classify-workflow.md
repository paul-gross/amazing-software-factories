# Running classification

Classification names what each watched repository is: an **assembly line** (factory software built by its own
pipeline or another assembly line's; one a person steers session by session is agent-assisted), a project
**built by an assembly line**, an **agent-assisted** project (a person building with agents, session by session), or
**not software**. The gate only shows that work lands through the night, which a person leaving agents running can
also do, so the classifier decides whether a system or a person drives the work. Until it does, a watched repository is neither
measured nor listed, and afterwards only assembly lines are: software that builds other software. Run it after the gate has admitted new repositories;
an unmeasured one is described to the classifier by the numbers it passed the gate with.

It runs on a local machine, not in GitHub Actions: each repository is one call to the `claude` command, signed in to a
Claude subscription, at roughly the cost of a short conversation.

## Run it

From the repository root, with a clean working tree:

1. `git pull --rebase`
2. `nice -n 15 python3 -m asf classify`: classifies every watched repository whose stored answer is missing or from
   an older classifier version, twenty at a time: it fetches their evidence, classifies them four at once and saves,
   while the next twenty's evidence is fetched, so a stopped run loses at most one chunk and picks up what is left.
   `classify 50` does a fixed random sample of 50 instead, to review a new prompt before running it on everything,
   drawn from repositories no version has read while enough remain, so each review sees new ones. A
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

[asf/kind.py](../asf/kind.py) holds the prompt and the evidence: description, topics, the layout two levels deep, the
agent instruction files at their usual paths (AGENTS.md, CLAUDE.md and the like: size and opening), the CI workflows,
the first 8,000 characters of the README, the newest 20 commits with bodies and authors, and the measured numbers.

The line between a factory and agent-assisted work: exhaustive agent-facing context (a library of the codebase's
conventions, architecture, rules and verification, written for agents, or a companion repository holding them) and
work flowing through a loop without a person picking each item point to a factory. Agent roles do not: a factory may
use named roles or none. Automation guardrails (CI that gates changes,
agent review or verification, enforced rules) add weight, but a factory can run without them; the discipline grade
measures them. A single CLAUDE.md or AGENTS.md with no supporting library or repository points to agent-assisted,
and so do customizations of a person's own assistant: .claude/agents, .claude/skills, slash commands, MCP
configuration. Both halves must show, the context and the loop; with only one, it is agent-assisted, or built by an
assembly line at low confidence. The loop must have agents writing code: dependency and package bump bots and
scheduled data refreshes land work around the clock but are not a factory. Repository
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
