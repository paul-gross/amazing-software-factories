# Amazing software factories

An open analysis of software factory repos on GitHub: projects built by fleets of AI coding agents rather than a
person at a keyboard, tracked over time to see which concepts are emerging and where they're heading.

**[Browse the list on the site →](https://paul-gross.github.io/amazing-software-factories/)** It has every repo on a
map of night against day activity, a table you can sort by any column and search, and a page per repo with its grades,
what it's missing for the next one up, its commit clock and how it has changed over time. It's updated every hour from
the same data as [the table below](#the-list).

The list is measured from public GitHub data by the code in this repo, and every repo goes through the same checks.
The main one is simple: work has to keep landing while its owner is asleep, night after night. Commit volume alone
doesn't count, since anyone with a few agent terminals open can make hundreds of commits in a day.

## How a repo gets on the list

Candidates come from three places: a week of public push activity from [GH Archive](https://www.gharchive.org/), the
repos linked from a few curated lists ([data/source-lists.txt](data/source-lists.txt)), and a hand-kept list of known
factories ([data/manual.txt](data/manual.txt)). Being nominated doesn't count for anything; everyone goes through the
same checks.

1. **Is it busy?** At least 10 commits a day to the default branch over four weeks, kept up for most of them, with a
   real amount of code. Forks and archived repos stop here.
2. **Is it one person?** A team working in shifts would look like a factory, so one human has to write most of the
   human commits. Bots don't count against anyone.
3. **Is there a night shift?** Over the week, the repo's quietest six hours of the day have to be at least 40% as
   busy as an even spread would make them, and code has to land on at least 5 of the 7 nights. This is the step that
   matters. It only looks at commit counts, so it's cheap enough to recheck every waiting repo every day.
4. **Is it real work?** A cron job that commits the same file every hour passes step 3 too, so the newest commit
   messages have to actually vary.

Most repos that make it past step 2 fail step 3. They're people coding, often with an assistant, and that's fine;
they're just not what this list is about. They never show up here.

A repo that passes is watched for good. Before anything else happens, a model reads it to decide what it is: a
factory building itself, a project being built by one, a project a person builds with agents, or not software at all
(docs, data, proofs). Working through the night is necessary for a factory but not proof of one, since anyone can leave
agents running overnight; what the model looks for is a system that picks up work and lands it on its own. This list
is only about software factories, software that can be pointed at other software to build it, so only the first is
listed and measured. A factory also has to be built by its own pipeline, or another factory's: one that isn't
dogfooding isn't ready for the public. A project built by a factory is the factory's product, not a factory. Until a
repo has been read, it isn't shown.

From then on it's measured once a day, even through a slow week, and its grades will say so if it slows down. Each
repo has its own hour of the day, so the work is spread out instead of landing all at once.

A repo that goes quiet, with no commits at all across its four measured weeks, goes dormant: it drops off the list and
stops being measured, but its history stays. A cheap daily check brings it back once work lands on 3 of 7 days again.

## The grades

Every listed repo gets three letters, A to F. Each letter is a set of requirements in [config.toml](config.toml), and
the page shows what a repo is missing for the next one up.

- **Output** is lines of code added on the median day of the week: A at 40,000, B at 20,000, C at 10,000, D at 5,000,
  E at 1,000. Using the median means one huge import can't carry a week.
- **Autonomy** is how close the repo gets to running around the clock. An A needs its quietest hours at least 90% as
  busy as the rest of the day and code landing every night. B, C and D step down to 80%, 70% and 60%, allowing a
  missed night from C down. E is 40% with up to two nights missed, the same bar a repo clears to get on the list:
  it works most nights, just not around the clock. Below that the work stops for part of each day.
- **Discipline** is whether the codebase holds up: how often CI on the main branch passes, whether pull requests run
  tests, lint and type checks, how much test code there is next to the source, and how big the biggest file has
  gotten.

## What counts as a line of code

Code lines come from a shallow clone of the measured week, read with `git log` and deleted right away. Nothing is
checked out, built or run.

Only source and test files count, including CSS, HTML and shell scripts. JSON, YAML, lock files, Markdown and other
data don't. A few kinds of produced code are left out by looking at the files themselves:

- files that start with a code generator's marker, like `Code generated ... DO NOT EDIT`;
- exact copies of a file already counted somewhere else;
- batches where one commit stamps out the same file many times;
- files rewritten over and over in a day, which only count by how much they actually grew.

Everything else on the page (pull requests, commits, CI, the commit clock) comes from GitHub's API. The measured week
ends two days before each run, so work that hasn't been pushed yet doesn't make a busy repo look idle.

## Things to know

- Commit times are whatever git recorded. They can be faked, and a fleet that only pushes once a day will look
  less autonomous than it is.
- Time zones don't matter. "Night" is each repo's own quietest stretch of the day, wherever that falls.
- Only public repos with activity on their default branch can be seen. Work that lives on other branches doesn't show
  until it lands.
- The thresholds are judgment calls. They're all in one file so you can disagree with them precisely.

## Disclosure

I build [paul-gross/blizzard](https://github.com/paul-gross/blizzard), a tool for running agent fleets, and it's on
this list under the same rules as everyone else. The code and every raw number are here to check.

## Getting off the list

Open an issue asking for your repo to be removed and it will be, no questions asked. It won't be added back.

## The list

The same list is easier to explore on [the site](https://paul-gross.github.io/amazing-software-factories/), with each
repo's grade breakdown and history.

<!-- BEGIN GENERATED -->
_284 repos, last measured 2026-10-21. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (284)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 84,937 | 65,799 | 67.9 | 28% | 0% | 79% | 3,045 KB | 1,990 (+10) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 77,143 | 414,597 | 62.5 | 18% | 5% | 96% | 3,975 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A D B | 66,037 | 77,446 | 33.6 | 67% | 25% | 97% | 514 KB | 11 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | A D B | 54,212 | 187,450 | 10.7 | 67% | 25% | 71% | 727 KB | 4 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A E C | 51,030 | 82,890 | 58.0 | 58% | 8% | 99% | 184 KB | 117 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | A F B | 50,134 | 186,934 | 15.5 | 37% | 11% | 94% | 213 KB | 0 |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 43,508 | 45,005 | 41.5 | 70% | 25% | 93% | 802 KB | 1 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 41,401 | 58,695 | 19.9 | 63% | 8% | 99% | 158 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | B C B | 39,714 | 38,938 | 29.3 | 84% | 0% | 98% | 231 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B F B | 37,183 | 41,176 | 37.7 | 12% | 7% | 95% | 534 KB | 37 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B F B | 36,869 | 55,297 | 7.5 | 46% | 6% | 80% | 265 KB | 326 (+1) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 35,571 | 79,969 | 65.7 | 72% | 30% | 97% | 166 KB | 2 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 35,511 | 40,941 | 30.4 | 80% | 81% | 92% | 363 KB | 9 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | B C C | 35,193 | 36,836 | 66.7 | 78% | 34% | 100% | 691 KB | 14 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 34,906 | 64,014 | 23.7 | 83% | 47% | 90% | 646 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 33,990 | 84,287 | 23.5 | 38% | 33% | 34% | 4,722 KB | 96 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 30,886 | 97,977 | 98.5 | 0% | 0% | 46% | 306 KB | 3 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B E B | 30,710 | 40,529 | 27.7 | 52% | 45% | 99% | 1,060 KB | 0 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B D C | 30,180 | 96,639 | 63.2 | 70% | 49% | 51% | 1,737 KB | 4 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B B A | 29,514 | 71,888 | 61.6 | 80% | 42% | 95% | 60 KB | 0 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B E B | 29,478 | 40,486 | 178 | 48% | 67% | 100% | 3,024 KB | 1 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B F D | 28,844 | 29,189 | 0.0 | 36% | 29% | – | 288 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B D C | 27,520 | 52,068 | 0.2 | 64% | 5% | 56% | 1,271 KB | 439 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | B E B | 27,379 | 27,619 | 20.2 | 45% | 20% | 88% | 883 KB | 4 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | B F A | 27,242 | 31,092 | 22.8 | 43% | 0% | 95% | 218 KB | 5 |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B D B | 26,972 | 644,387 | 89.6 | 68% | 40% | 94% | 581 KB | 2 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B D A | 26,942 | 47,012 | 102 | 63% | 15% | 100% | 219 KB | 14 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B E C | 26,731 | 30,914 | 35.3 | 44% | 26% | 100% | 437 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 25,962 | 122,612 | 26.8 | 50% | 42% | 100% | 887 KB | 33 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 25,838 | 94,516 | 39.7 | 33% | 45% | 100% | 55 KB | 0 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 25,628 | 40,682 | 160 | 32% | 4% | 89% | 2,294 KB | 3 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 25,309 | 29,087 | 31.8 | 39% | 21% | 98% | 1,356 KB | 92 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 25,198 | 36,551 | 46.7 | 73% | 67% | 100% | 354 KB | 2 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B C C | 24,293 | 46,102 | 61.9 | 73% | 25% | 99% | 553 KB | 2 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 23,636 | 29,120 | 101 | 36% | 20% | 92% | 3,537 KB | 71 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | B F A | 22,840 | 108,055 | 23.2 | 66% | 0% | 99% | 377 KB | 48 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | B F B | 22,779 | 32,968 | 33.9 | 26% | 0% | 91% | 2,600 KB | 35 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 21,971 | 19,972 | 0.0 | 84% | 25% | – | 226 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 21,255 | 24,344 | 34.1 | 78% | 4% | 99% | 599 KB | 22 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 20,838 | 37,770 | 0.0 | 46% | 41% | – | 296 KB | 2 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 19,562 | 29,969 | 61.5 | 40% | 60% | 95% | 768 KB | 6,384 (+11) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C C A | 19,413 | 120,079 | 25.0 | 77% | 23% | 98% | 158 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C B B | 18,773 | 25,787 | 20.4 | 84% | 18% | 100% | 962 KB | 1 |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 18,501 | 22,513 | 16.7 | 35% | 30% | 96% | 6,732 KB | 120 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C E B | 18,160 | 40,647 | 8.5 | 44% | 35% | 93% | 781 KB | 0 |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 17,742 | 34,396 | 33.8 | 28% | 24% | 100% | 874 KB | 4 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 17,439 | 29,261 | 21.8 | 87% | 63% | 97% | 200 KB | 6 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 16,889 | 22,997 | 33.9 | 71% | 51% | 91% | 1,519 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 16,858 | 21,632 | 13.2 | 56% | 0% | 98% | 714 KB | 9 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 16,690 | 21,784 | 0.0 | 51% | 0% | 96% | 589 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C E D | 16,350 | 20,944 | 0.7 | 56% | 16% | 0% | 164 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C C B | 16,059 | 19,917 | 8.0 | 71% | 20% | 77% | 594 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | C E C | 15,918 | 21,980 | 16.8 | 86% | 0% | 100% | 41 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | C E C | 15,603 | 36,090 | 39.8 | 53% | 28% | 57% | 3,052 KB | 2 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C E A | 15,308 | 27,190 | 2.7 | 55% | 0% | 100% | 258 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 15,111 | 25,669 | 0.0 | 70% | 49% | – | 1,206 KB | 3 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C E C | 14,836 | 53,876 | 32.0 | 64% | 1% | 100% | 78 KB | 2 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 14,718 | 20,121 | 22.9 | 79% | 8% | 100% | 137 KB | 32 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 14,604 | 31,145 | 28.9 | 2% | 30% | 96% | 225 KB | 7 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,604 | 24,639 | 5.0 | 14% | 16% | 97% | 409 KB | 132 (+1) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C B C | 14,590 | 18,271 | 20.0 | 88% | 29% | 96% | 668 KB | 9 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | C E A | 14,568 | 32,422 | 17.6 | 60% | 0% | 97% | 90 KB | 1 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C B D | 14,385 | 380,203 | 0.0 | 82% | 47% | 0% | 3,283 KB | 1 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C D C | 14,354 | 24,453 | 24.0 | 63% | 4% | 93% | 750 KB | 5 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | C E B | 13,819 | 29,323 | 14.9 | 78% | 2% | 97% | 140 KB | 2 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C E B | 13,808 | 25,601 | 11.6 | 74% | 0% | 98% | 86 KB | 6 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 13,335 | 20,212 | 99.1 | 23% | 49% | 76% | 351 KB | 51 (+2) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 13,220 | 19,480 | 0.0 | 74% | 10% | 11% | 274 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 13,188 | 21,913 | 32.9 | 36% | 38% | 82% | 330 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C E B | 12,994 | 27,633 | 30.5 | 50% | 29% | 100% | 587 KB | 2 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 12,906 | 20,569 | 26.7 | 74% | 30% | 96% | 153 KB | 4 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 12,679 | 22,860 | 69.7 | 54% | 40% | 25% | 837 KB | 16 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C D D | 12,586 | 16,522 | 0.0 | 70% | 53% | 43% | 984 KB | 32 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | C E B | 12,476 | 17,637 | 10.8 | 59% | 52% | 96% | 489 KB | 0 |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C F A | 12,115 | 16,675 | 33.4 | 36% | 20% | 100% | 118 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 11,889 | 53,097 | 0.0 | 68% | 12% | 50% | 478 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | C F C | 11,827 | 17,525 | 11.6 | 60% | 0% | 100% | 17 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C C D | 11,623 | 14,880 | 8.5 | 77% | 16% | 26% | 194 KB | 2 (+0) |
| [integry/propr](https://github.com/integry/propr) | C E B | 11,145 | 16,025 | 14.6 | 55% | 48% | 100% | 4,314 KB | 20 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 11,119 | 15,917 | 39.0 | 56% | 13% | 100% | 251 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C E A | 11,114 | 20,335 | 14.9 | 59% | 0% | 97% | 128 KB | 5 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C E B | 10,925 | 439,059 | 30.0 | 47% | 9% | 97% | 1,414 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C C B | 10,917 | 14,668 | 29.5 | 79% | 27% | 74% | 1,371 KB | 70,229 (+26) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 10,783 | 47,583 | 26.0 | 80% | 0% | 100% | 1,942 KB | 5 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | C E C | 10,729 | 34,768 | 0.0 | 59% | 12% | 100% | 487 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 10,639 | 12,746 | 20.8 | 65% | 67% | 100% | 555 KB | 1 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 10,633 | 28,743 | 26.4 | 45% | 0% | 90% | 458 KB | 19 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 10,506 | 19,035 | 32.4 | 58% | 0% | 99% | 399 KB | 9 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 10,175 | 20,044 | 30.6 | 28% | 49% | 100% | 1,195 KB | 8 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C E B | 10,161 | 19,900 | 12.3 | 55% | 15% | 97% | 575 KB | 1 (+1) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F D | 9,873 | 19,769 | 0.0 | 10% | 33% | 30% | 220 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D F C | 9,839 | 7,531 | 11.5 | 45% | 0% | 89% | 6,579 KB | 8 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 9,664 | 17,578 | 20.2 | 29% | 8% | 88% | 700 KB | 4 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 9,583 | 13,878 | 0.0 | 48% | 26% | 100% | 414 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 9,464 | 14,681 | 30.2 | 13% | 11% | 100% | 134 KB | 7 (+6) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 9,391 | 11,283 | 14.1 | 24% | 36% | 94% | 320 KB | 158 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 9,278 | 27,202 | 0.0 | 35% | 0% | 0% | 601 KB | 1 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | D E D | 9,267 | 11,948 | 0.0 | 49% | 31% | 38% | 308 KB | 244 (+1) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | D D C | 9,145 | 30,837 | 6.9 | 69% | 38% | 100% | 100 KB | 0 |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | D E D | 9,064 | 39,001 | 13.0 | 79% | 5% | 43% | 431 KB | 0 |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | D E B | 8,925 | 9,352 | 10.9 | 72% | 0% | 97% | 56 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | D E C | 8,793 | 17,456 | 38.6 | 56% | 8% | 73% | 319 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,731 | 13,154 | 0.2 | 52% | 18% | 100% | 344 KB | 2 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | D D A | 8,555 | 37,411 | 24.8 | 66% | 17% | 99% | 393 KB | 0 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D D | 8,486 | 11,104 | 13.6 | 62% | 14% | 30% | 129 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | D F D | 8,455 | 19,994 | 10.5 | 44% | 5% | 0% | 285 KB | 24 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | D D B | 8,232 | 10,829 | 9.5 | 65% | 7% | 94% | 79 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 8,122 | 12,709 | 47.5 | 0% | 43% | 89% | 67 KB | 61 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | D D C | 8,040 | 13,447 | 36.8 | 67% | 11% | 100% | 220 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D F B | 8,015 | 13,485 | 14.2 | 32% | 0% | 83% | 1,188 KB | 13 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D D A | 8,001 | 14,363 | 13.2 | 66% | 42% | 94% | 137 KB | 0 |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 7,872 | 8,373 | 76.4 | 74% | 11% | 100% | 752 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | D F D | 7,839 | 50,392 | 18.2 | 14% | 2% | 37% | 140 KB | 0 |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D E A | 7,823 | 18,962 | 13.0 | 44% | 24% | 90% | 236 KB | 5 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D D B | 7,656 | 25,699 | 32.8 | 67% | 8% | 91% | 1,430 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 7,512 | 23,259 | 0.0 | 59% | 0% | – | 813 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 7,425 | 14,049 | 29.6 | 44% | 36% | 100% | 316 KB | 159 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,340 | 18,160 | 4.5 | 39% | 38% | 79% | 3,440 KB | 545 (+1) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 7,305 | 23,704 | 15.0 | 65% | 11% | 97% | 330 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 7,102 | 12,380 | 28.8 | 40% | 34% | 100% | 557 KB | 5 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D E C | 6,813 | 24,779 | 17.3 | 59% | 25% | 100% | 43 KB | 15 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D F C | 6,775 | 46,862 | 1.2 | 24% | 28% | 97% | 3,340 KB | 7 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 6,752 | 10,927 | 0.1 | 31% | 3% | 71% | 152 KB | 29 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | D F A | 6,631 | 15,029 | 1.3 | 52% | 0% | 100% | 163 KB | 11 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | D E D | 6,540 | 9,411 | 0.0 | 75% | 0% | 42% | 266 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | D C C | 6,458 | 28,445 | 10.2 | 72% | 38% | 98% | 140 KB | 1 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D D D | 6,342 | 13,806 | 34.7 | 62% | 55% | – | 421 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 6,232 | 12,918 | 0.0 | 13% | 35% | 96% | 401 KB | 1 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | D E E | 6,159 | 15,562 | 14.6 | 53% | 59% | 76% | 1,538 KB | 5 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D D D | 6,119 | 10,125 | 34.8 | 67% | 6% | – | 188 KB | 2 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 6,026 | 11,101 | 1.6 | 30% | 8% | 77% | 42 KB | 1 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 6,009 | 14,194 | 14.1 | 68% | 0% | 100% | 696 KB | 11 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 5,865 | 7,845 | 0.0 | 38% | 19% | 86% | 869 KB | 1 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,808 | 6,926 | 23.4 | 32% | 0% | 92% | 941 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D F B | 5,699 | 9,995 | 24.3 | 47% | 11% | 90% | 800 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 5,620 | 6,869 | 21.7 | 79% | 64% | 100% | 103 KB | 0 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | D E B | 5,616 | 11,096 | 4.9 | 60% | 14% | 80% | 65 KB | 0 |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | D F B | 5,540 | 7,338 | 19.9 | 15% | 26% | 90% | 436 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,527 | 11,330 | 3.4 | 32% | 22% | 90% | 319 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 5,336 | 16,043 | 8.0 | 38% | 33% | 100% | 530 KB | 11 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D C A | 5,320 | 8,642 | 28.3 | 78% | 40% | 90% | 102 KB | 231 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 5,310 | 14,199 | 17.8 | 20% | 9% | 98% | 361 KB | 7 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 5,112 | 6,786 | 21.1 | 35% | 35% | 99% | 388 KB | 20 (+1) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,059 | 14,397 | 21.6 | 12% | 0% | 98% | 489 KB | 28 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | D E B | 5,023 | 6,249 | 45.5 | 53% | 23% | 99% | 303 KB | 2 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E D B | 4,989 | 11,607 | 19.2 | 60% | 18% | 96% | 499 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 4,918 | 6,941 | 38.3 | 53% | 7% | – | 365 KB | 3 (+1) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | E E D | 4,860 | 5,618 | 0.0 | 59% | 15% | – | 3,234 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 4,826 | 10,236 | 5.6 | 50% | 32% | 98% | 70 KB | 15 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E E D | 4,783 | 5,375 | 0.0 | 47% | 33% | 33% | 397 KB | 460 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 4,777 | 10,597 | 8.5 | 46% | 27% | – | 136 KB | 14 |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 4,631 | 13,101 | 29.1 | 37% | 18% | 99% | 468 KB | 17 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E B A | 4,559 | 4,205 | 16.5 | 80% | 52% | 100% | 399 KB | 11 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 4,518 | 6,922 | 10.8 | 48% | 0% | – | 82 KB | 2 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F A | 4,405 | 7,529 | 28.6 | 22% | 0% | 86% | 203 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 4,316 | 5,536 | 15.6 | 53% | 15% | 100% | 193 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | E F C | 4,178 | 7,033 | 10.9 | 23% | 30% | 99% | 99 KB | 4 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,159 | 11,083 | 21.2 | 18% | 18% | 93% | 269 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 4,147 | 13,103 | 6.7 | 40% | 35% | 93% | 261 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 4,144 | 9,849 | 0.0 | 13% | 8% | 0% | 435 KB | 4 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 4,141 | 18,719 | 0.0 | 33% | 6% | 45% | 149 KB | 110 (+2) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 3,726 | 9,503 | 34.8 | 41% | 0% | 95% | 106 KB | 5 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,628 | 11,370 | 10.2 | 53% | 43% | 97% | 111 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 3,570 | 4,613 | 9.4 | 24% | 6% | 100% | 66 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E E B | 3,566 | 6,863 | 0.9 | 58% | 20% | 100% | 182 KB | 7 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E E B | 3,519 | 8,639 | 22.6 | 65% | 0% | 100% | 1,172 KB | 0 |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E B E | 3,380 | 22,518 | 22.2 | 83% | 11% | 99% | 625 KB | 11 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 3,341 | 85,137 | 14.5 | 35% | 0% | 99% | 244 KB | 2 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E E E | 3,321 | 9,532 | 22.0 | 43% | 36% | 98% | 1,109 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E E C | 3,273 | 7,485 | 32.5 | 57% | 0% | 90% | 403 KB | 2 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 3,203 | 3,761 | 14.0 | 48% | 0% | 100% | 161 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F A | 3,164 | 4,056 | 13.5 | 14% | 31% | 98% | 467 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 3,108 | 3,720 | 23.3 | 22% | 12% | 97% | 544 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 3,080 | 12,716 | 35.4 | 39% | 0% | 89% | 240 KB | 9 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 3,021 | 10,058 | 23.3 | 50% | 22% | 95% | 69 KB | 10 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,927 | 25,407 | 0.0 | 54% | 0% | – | 200 KB | 28 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E E B | 2,893 | 4,521 | 9.0 | 77% | 15% | 100% | 716 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E D C | 2,861 | 4,244 | 12.8 | 60% | 0% | 96% | 118 KB | 1 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | E F C | 2,857 | 3,510 | 23.2 | 77% | 0% | 98% | 363 KB | 1 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 2,725 | 6,121 | 28.6 | 49% | 0% | 89% | 980 KB | 99 (+1) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,693 | 4,488 | 0.1 | 43% | 0% | 86% | 309 KB | 3 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,656 | 7,687 | 19.4 | 16% | 14% | 100% | 386 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,599 | 5,074 | 23.8 | 37% | 0% | 99% | 127 KB | 23 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 2,598 | 12,994 | 24.4 | 34% | 0% | 89% | 118 KB | 3 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E E A | 2,503 | 5,403 | 9.6 | 52% | 28% | 92% | 244 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,355 | 7,340 | 29.5 | 33% | 0% | 100% | 617 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 2,273 | 107,649 | 0.0 | 36% | 0% | – | 8,190 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 2,216 | 9,921 | 11.3 | 17% | 20% | 71% | 527 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 2,179 | 3,904 | 15.8 | 36% | 0% | – | 48 KB | 3 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,100 | 3,416 | 20.2 | 5% | 41% | 97% | 624 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,054 | 10,439 | 13.9 | 56% | 0% | 100% | 1,007 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E F C | 1,971 | 5,284 | 9.9 | 23% | 0% | 88% | 8,119 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,945 | 8,009 | 20.8 | 26% | 0% | 88% | 277 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E E D | 1,932 | 5,460 | 0.3 | 75% | 11% | 0% | 453 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F C | 1,914 | 28,653 | 0.8 | 68% | 5% | 53% | 5,520 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E E B | 1,821 | 3,801 | 42.0 | 74% | 7% | 93% | 142 KB | 8 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,757 | 7,792 | 0.0 | 39% | 0% | – | 592 KB | 2 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,601 | 5,045 | 9.5 | 38% | 14% | 98% | 787 KB | 2 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | E F D | 1,451 | 8,068 | 0.0 | 49% | 0% | 0% | 315 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E D C | 1,425 | 8,369 | 17.2 | 64% | 6% | 98% | 407 KB | 1 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,348 | 1,517 | 0.1 | 60% | 28% | 0% | 634 KB | 3 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | E E E | 1,319 | 3,525 | 20.6 | 55% | 0% | 94% | 555 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 1,318 | 5,823 | 27.4 | 42% | 0% | 47% | 97 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,308 | 3,710 | 4.9 | 43% | 25% | 94% | 7,014 KB | 18 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,303 | 2,817 | 14.9 | 0% | 0% | 99% | 132 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F C | 1,251 | 4,658 | 0.0 | 29% | 0% | 63% | 554 KB | 27 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,160 | 10,598 | 26.4 | 15% | 0% | 100% | 122 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,149 | 4,704 | 26.3 | 60% | 0% | 100% | 148 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 1,130 | 3,972 | 0.0 | 46% | 0% | 0% | 1,120 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 1,074 | 29,332 | 0.3 | 78% | 0% | 90% | 1,468 KB | 1,100 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,068 | 6,374 | 27.1 | 0% | 16% | 100% | 526 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F D C | 954 | 2,539 | 6.2 | 63% | 5% | 100% | 140 KB | 2 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F B | 921 | 5,816 | 13.7 | 10% | 17% | 73% | 229 KB | 1 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 909 | 1,916 | 1.9 | 50% | 0% | 33% | 61 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 890 | 7,976 | 9.9 | 16% | 0% | 90% | 38 KB | 0 |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 796 | 17,338 | 14.3 | 11% | 0% | – | 408 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 769 | 5,115 | 19.4 | 34% | 12% | 99% | 215 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 755 | 3,670 | 13.1 | 62% | 0% | 99% | 49 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 693 | 829 | 5.1 | 0% | 0% | 97% | 72 KB | 4 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 585 | 8,656 | 1.5 | 56% | 0% | – | 295 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | F F B | 511 | 1,123 | 9.5 | 57% | 0% | 94% | 330 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 481 | 6,478 | 7.5 | 77% | 0% | 100% | 175 KB | 225 (+3) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 424 | 33,156 | 6.0 | 26% | 0% | 100% | 24 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 392 | 4,243 | 13.2 | 52% | 0% | 99% | 298 KB | 5 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 389 | 12,344 | 0.0 | 58% | 0% | 97% | 478 KB | 6 |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 350 | 6,957 | 0.0 | 66% | 0% | – | 108 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 293 | 34,404 | 3.5 | 37% | 0% | 100% | 1,116 KB | 5 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 283 | 1,133 | 0.0 | 13% | 0% | 98% | 384 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 170 | 3,132 | 18.8 | 42% | 0% | 88% | 303 KB | 23 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 150 | 1,659 | 0.0 | 19% | 0% | 93% | 211 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 134 | 884 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 106 | 10,103 | 2.3 | 59% | 12% | 86% | 149 KB | 0 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 102 | 4,511 | 0.0 | 18% | 0% | – | 112 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 82 | 4,813 | 0.0 | 36% | 0% | 0% | 473 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 58 | 516 | 26.3 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 36 | 3,028 | 15.2 | 4% | 0% | 96% | 66 KB | 3 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 30 | 7,839 | 12.8 | 32% | 0% | 98% | 43 KB | 1 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 28 | 224,348 | 9.9 | 21% | 0% | 99% | 378 KB | 1 |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 2,666 | 0.0 | 42% | 0% | 96% | 70 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 2,339,981 | 50.5 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F B B | – | – | 38.4 | 86% | 30% | 89% | 2,162 KB | 1,416 (+4) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | – | – | 29.8 | – | – | 52% | 92 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 18,303 | 26.1 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 1,491 | 22.8 | 0% | 0% | 99% | 87 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F C | 0 | 2,912 | 22.6 | 0% | 0% | 99% | 311 KB | 4 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F B B | – | – | 22.0 | 83% | 36% | 94% | 965 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | 0 | 0 | 18.9 | – | – | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 14.8 | 2% | 0% | 98% | 723 KB | 5 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 827 | 14.1 | 0% | 0% | – | 131 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 1,048 | 14.0 | 0% | 0% | – | 55 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 3 | 13.8 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 13.6 | 33% | 0% | 98% | 342 KB | 4 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | 0 | 3,912 | 13.6 | 38% | 0% | 90% | 195 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 0 | 12.2 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 0 | 1 | 10.9 | 0% | 0% | – | 115 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 5,837 | 7.8 | 40% | 0% | 98% | 122 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F B | – | – | 6.3 | 53% | 0% | 82% | 206 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 43 | 5.6 | 0% | 0% | 63% | 464 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 5.4 | 61% | 56% | 0% | 1,772 KB | 457 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F E B | 0 | 0 | 4.8 | 40% | 33% | 80% | 149 KB | 2 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,279 | 3.8 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 0 | 837 | 1.9 | 32% | 0% | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 871 | 1.3 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 1.0 | 0% | 0% | – | 92 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 65% | 5% | 80% | 816 KB | 5 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 75% | 84% | 96% | 25,276 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 770 | 0.1 | 14% | 0% | 9% | 904 KB | 1,281 (+1) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 1,761 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | 32% | 0% | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 412 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 46% | 16% | 50% | 84 KB | 5 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 7 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
<!-- END GENERATED -->

## Running it

The list is kept up to date by two scripts, each of which pulls, runs, commits and pushes:

```sh
scripts/daily.sh      # find new candidates and screen them (steps 1 and 2)
scripts/hourly.sh     # recheck waiting repos (steps 3 and 4) and measure the listed ones
```

Classifying newly watched repos is run by hand with `python -m asf classify`, which needs the `claude` CLI signed in;
[context/classify-workflow.md](context/classify-workflow.md) has the steps.

You need Python 3.11 or newer, git, and a GitHub token (`GH_TOKEN`, or a signed-in `gh`). There are no other
dependencies. [context/](context/index.md) has the details for running and maintaining it, written for people and
coding agents alike.

## License

The code is [MIT](LICENSE). The data and reports are [CC BY 4.0](LICENSE-DATA).
