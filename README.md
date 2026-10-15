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
_214 repos, last measured 2026-10-15. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (214)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 91,868 | 127,292 | 64.0 | 26% | 52% | 87% | 2,994 KB | 1,880 (+70) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 77,447 | 93,454 | 31.0 | 71% | 27% | 98% | 231 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 62,320 | 83,181 | 24.4 | 81% | 20% | 96% | 621 KB | 10 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A C B | 53,949 | 91,837 | 33.9 | 77% | 40% | 92% | 2,585 KB | 34 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | A D C | 50,569 | 60,933 | 49.2 | 66% | 56% | 97% | 607 KB | 2 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | A F B | 49,554 | 649,321 | 75.1 | 31% | 57% | 98% | 567 KB | 2 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A E A | 48,745 | 66,221 | 89.3 | 77% | 57% | 99% | 162 KB | 14 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 45,515 | 57,526 | 60.5 | 88% | 36% | 95% | 680 KB | 14 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 42,904 | 50,061 | 29.5 | 59% | 54% | 88% | 732 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | A E B | 42,622 | 55,747 | 36.5 | 56% | 3% | 98% | 526 KB | 37 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C B | 39,272 | 291,071 | 28.6 | 71% | 2% | 92% | 1,428 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 38,149 | 43,539 | 25.8 | 84% | 41% | 82% | 364 KB | 9 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B D C | 38,122 | 94,773 | 45.5 | 66% | 39% | 89% | 2,449 KB | 4 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B C B | 37,151 | 119,896 | 23.7 | 75% | 22% | 100% | 772 KB | 31 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 36,307 | 1,926,368 | 78.1 | 4% | 0% | 95% | 3,975 KB | 1 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 35,108 | 39,145 | 33.4 | 74% | 61% | 100% | 599 KB | 22 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B D B | 34,907 | 49,376 | 28.5 | 68% | 44% | 100% | 1,316 KB | 91 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D C | 33,244 | 108,333 | 8.6 | 64% | 33% | 65% | 691 KB | 4 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E C | 30,858 | 127,631 | 0.2 | 41% | 0% | 64% | 1,271 KB | 434 (+2) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B C B | 28,544 | 36,534 | 149 | 73% | 54% | 100% | 3,182 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 28,518 | 53,016 | 40.5 | 83% | 53% | 100% | 353 KB | 2 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B F A | 28,449 | 36,496 | 19.2 | 72% | 0% | 97% | 94 KB | 16 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B E A | 25,737 | 50,257 | 46.3 | 78% | 44% | 96% | 156 KB | 2 (+1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 25,099 | 25,040 | 0.0 | 86% | 65% | – | 225 KB | 0 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 25,050 | 77,231 | 93.4 | 38% | 37% | 46% | 310 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B E B | 24,987 | 29,785 | 13.1 | 52% | 57% | 99% | 704 KB | 9 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 22,791 | 70,359 | 32.8 | 51% | 14% | 93% | 56 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | B E C | 22,656 | 43,931 | 33.7 | 67% | 0% | 93% | 119 KB | 115 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B C A | 22,385 | 28,991 | 0.7 | 70% | 50% | 100% | 163 KB | 11 (+2) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 21,621 | 44,549 | 0.0 | 63% | 57% | – | 1,185 KB | 3 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | B E B | 21,401 | 39,818 | 26.8 | 41% | 17% | 96% | 387 KB | 9 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B F B | 21,230 | 33,609 | 16.3 | 55% | 12% | 92% | 434 KB | 0 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B C C | 21,165 | 51,141 | 151 | 73% | 9% | 89% | 2,294 KB | 3 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B F D | 20,755 | 29,857 | 0.0 | 81% | 0% | 40% | 250 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | B E C | 20,741 | 51,039 | 26.5 | 50% | 34% | 96% | 453 KB | 18 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | B E B | 20,723 | 31,317 | 8.3 | 55% | 0% | 93% | 86 KB | 5 |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B C C | 20,298 | 32,940 | 0.2 | 76% | 47% | 100% | 312 KB | 0 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | B B D | 20,008 | 17,840 | 0.0 | 81% | 17% | 0% | 601 KB | 1 |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 19,698 | 28,827 | 33.7 | 30% | 30% | 100% | 409 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C E D | 19,679 | 20,497 | 9.8 | 58% | 0% | – | 82 KB | 2 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 19,585 | 31,415 | 27.9 | 77% | 34% | 98% | 147 KB | 4 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | C E D | 19,083 | 47,192 | 23.0 | 43% | 50% | 34% | 3,082 KB | 96 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E C | 19,002 | 84,732 | 23.1 | 55% | 46% | 100% | 309 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C C B | 17,890 | 28,552 | 46.7 | 72% | 37% | 100% | 559 KB | 2 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 17,076 | 34,199 | 0.0 | 71% | 16% | 51% | 455 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 15,685 | 26,488 | 22.1 | 59% | 0% | 96% | 114 KB | 1 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 15,500 | 20,316 | 58.0 | 60% | 69% | 100% | 768 KB | 6,315 (+18) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 15,240 | 16,106 | 0.0 | 59% | 31% | 29% | 219 KB | 168 (+19) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 14,604 | 28,318 | 27.6 | 24% | 28% | 97% | 225 KB | 6 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C F B | 14,510 | 23,180 | 6.6 | 34% | 34% | 80% | 556 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C E A | 13,554 | 19,615 | 34.8 | 54% | 48% | 94% | 301 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C B C | 13,509 | 20,513 | 58.0 | 86% | 68% | 100% | 4,310 KB | 15 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C F C | 13,417 | 35,325 | 53.2 | 38% | 16% | 98% | 325 KB | 3 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 13,329 | 26,016 | 29.8 | 49% | 26% | 99% | 573 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C E B | 13,282 | 19,991 | 0.0 | 51% | 21% | 74% | 204 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 13,143 | 12,005 | 19.5 | 77% | 21% | 94% | 531 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C C B | 12,778 | 25,645 | 21.3 | 74% | 28% | 100% | 1,066 KB | 6 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C E D | 12,634 | 20,755 | 0.0 | 77% | 26% | 42% | 265 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C C C | 12,631 | 19,308 | 0.0 | 76% | 10% | 86% | 853 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C F B | 12,496 | 24,146 | 16.1 | 50% | 21% | 96% | 808 KB | 4 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C E B | 12,377 | 18,818 | 32.6 | 56% | 47% | 87% | 1,402 KB | 3 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | C E A | 12,218 | 33,905 | 11.6 | 49% | 0% | 100% | 236 KB | 5 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C D C | 12,174 | 21,285 | 8.2 | 62% | 38% | 95% | 109 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | C F D | 12,113 | 23,019 | 0.0 | 63% | 0% | – | 259 KB | 0 |
| [integry/propr](https://github.com/integry/propr) | C E B | 12,104 | 22,583 | 11.4 | 58% | 10% | 100% | 4,314 KB | 17 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 11,995 | 79,453 | 21.8 | 36% | 44% | 90% | 116 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 11,866 | 17,526 | 18.3 | 79% | 36% | 100% | 123 KB | 32 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 11,730 | 545,893 | 0.0 | 79% | 0% | 0% | 3,283 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | C E D | 11,475 | 15,320 | 20.4 | 57% | 15% | – | 378 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C E B | 11,461 | 20,463 | 12.8 | 76% | 44% | 78% | 126 KB | 5 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 11,234 | 27,750 | 15.8 | 26% | 12% | 93% | 67 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C A | 11,206 | 15,393 | 30.6 | 72% | 66% | 89% | 102 KB | 229 (+1) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | C E D | 11,068 | 17,120 | 0.0 | 74% | 0% | 30% | 17 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 11,012 | 27,147 | 11.9 | 38% | 7% | 91% | 2,869 KB | 115 (+1) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 10,779 | 14,912 | 87.4 | 22% | 55% | 76% | 340 KB | 48 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C F B | 10,492 | 18,145 | 0.0 | 50% | 14% | 93% | 588 KB | 1 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 10,486 | 22,916 | 20.3 | 54% | 27% | 100% | 1,797 KB | 5 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 10,230 | 15,025 | 0.0 | 52% | 0% | – | 776 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,870 | 13,551 | 8.1 | 34% | 16% | 100% | 490 KB | 11 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | D E B | 9,780 | 24,250 | 28.6 | 60% | 13% | 99% | 6,926 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D D C | 9,715 | 45,477 | 3.9 | 62% | 5% | 100% | 1,116 KB | 5 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 9,658 | 8,487 | 9.8 | 32% | 0% | 89% | 97 KB | 3 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 9,529 | 13,483 | 42.2 | 0% | 59% | 95% | 66 KB | 60 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D E B | 9,405 | 13,111 | 27.5 | 66% | 18% | 71% | 185 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D D B | 9,182 | 30,658 | 73.9 | 65% | 19% | 100% | 632 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D D C | 9,102 | 13,804 | 16.1 | 60% | 21% | 100% | 634 KB | 8 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | D F C | 8,969 | 11,428 | 25.7 | 59% | 0% | 99% | 293 KB | 4 |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D E B | 8,920 | 12,278 | 28.8 | 51% | 0% | 97% | 105 KB | 4 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F A | 8,658 | 19,814 | 4.8 | 0% | 0% | 98% | 395 KB | 128 (+1) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D E C | 8,486 | 13,356 | 6.7 | 87% | 34% | 59% | 111 KB | 0 |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D E C | 8,479 | 11,377 | 10.2 | 49% | 29% | 97% | 6,579 KB | 8 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | D F B | 8,227 | 17,354 | 45.9 | 15% | 51% | 100% | 793 KB | 4 (+1) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D E C | 8,179 | 11,140 | 24.4 | 51% | 0% | 100% | 403 KB | 2 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D D F | 8,154 | 274,582 | 0.0 | 66% | 35% | – | 8,190 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D F B | 8,094 | 21,132 | 19.3 | 55% | 22% | 100% | 1,058 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 8,059 | 188,882 | 19.0 | 31% | 8% | 100% | 1,414 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D C C | 7,990 | 13,291 | 7.0 | 81% | 25% | 93% | 154 KB | 8 |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 7,837 | 8,595 | 9.0 | 56% | 27% | 24% | 189 KB | 2 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 7,582 | 7,453 | 22.6 | 64% | 45% | 79% | 803 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | D D E | 7,388 | 8,116 | 20.4 | 66% | 6% | 95% | 549 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D C D | 7,204 | 11,142 | 0.0 | 71% | 50% | 48% | 1,022 KB | 32 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D F A | 6,835 | 29,153 | 0.0 | 49% | 0% | 95% | 211 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D D B | 6,806 | 7,247 | 14.9 | 61% | 51% | 100% | 93 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 6,721 | 23,570 | 0.0 | 42% | 0% | – | 189 KB | 28 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 6,715 | 15,737 | 19.9 | 52% | 0% | 90% | 700 KB | 4 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D B B | 6,616 | 11,227 | 29.2 | 87% | 54% | 94% | 1,500 KB | 70,032 (+31) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 6,374 | 13,485 | 20.1 | 40% | 5% | 100% | 240 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 6,335 | 16,125 | 2.4 | 34% | 43% | 66% | 3,212 KB | 534 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D E A | 6,298 | 21,348 | 10.9 | 56% | 16% | 99% | 126 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D D C | 6,244 | 7,391 | 10.5 | 67% | 58% | 91% | 115 KB | 1 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | D E B | 6,085 | 12,304 | 26.9 | 55% | 36% | 99% | 972 KB | 93 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 6,064 | 11,260 | 17.5 | 34% | 0% | 95% | 385 KB | 19 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D E A | 5,899 | 8,987 | 7.5 | 46% | 57% | 95% | 240 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D E D | 5,893 | 9,577 | 0.0 | 84% | 0% | – | 108 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 5,533 | 9,334 | 21.9 | 44% | 19% | 100% | 543 KB | 5 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D E C | 5,517 | 7,608 | 25.5 | 52% | 0% | 98% | 535 KB | 17 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 5,467 | 15,620 | 0.0 | 67% | 13% | 100% | 226 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D E C | 5,310 | 8,266 | 18.1 | 62% | 8% | 70% | 360 KB | 7 (+1) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 5,179 | 6,146 | 28.0 | 72% | 25% | – | 337 KB | 2 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | D B A | 5,038 | 5,510 | 19.6 | 90% | 38% | 100% | 387 KB | 9 |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | D E C | 5,029 | 9,262 | 1.3 | 50% | 0% | 68% | 290 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E E B | 4,809 | 30,364 | 0.0 | 52% | 41% | 96% | 398 KB | 1 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E E D | 4,722 | 10,258 | 0.0 | 59% | 11% | 0% | 330 KB | 4 |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E C B | 4,541 | 12,904 | 18.8 | 79% | 33% | 82% | 64 KB | 10 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E D C | 4,512 | 18,577 | 36.0 | 68% | 35% | 58% | 240 KB | 9 |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E E B | 4,496 | 11,790 | 12.2 | 60% | 6% | 96% | 49 KB | 0 |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 4,451 | 16,673 | 18.3 | 63% | 43% | 98% | 401 KB | 0 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E E C | 4,226 | 19,301 | 0.0 | 42% | 63% | 51% | 142 KB | 107 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,120 | 16,887 | 13.8 | 37% | 9% | 100% | 240 KB | 2 |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,090 | 7,031 | 14.3 | 43% | 0% | 98% | 141 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 3,987 | 5,930 | 13.6 | 37% | 0% | – | 43 KB | 3 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | E F C | 3,796 | 19,773 | 0.0 | 63% | 0% | 100% | 441 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 3,780 | 9,663 | 25.1 | 35% | 18% | 97% | 125 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E C B | 3,671 | 19,828 | 9.2 | 74% | 12% | 91% | 523 KB | 0 |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 3,624 | 7,233 | 7.6 | 77% | 3% | 92% | 68 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E E C | 3,542 | 4,879 | 23.4 | 59% | 29% | 95% | 544 KB | 0 |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E D C | 3,349 | 15,455 | 18.6 | 69% | 53% | 100% | 170 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 3,332 | 6,689 | 4.1 | 29% | 10% | 96% | 7,014 KB | 18 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 3,243 | 9,337 | 8.8 | 29% | 10% | 96% | 762 KB | 2 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,144 | 4,139 | 17.7 | 57% | 14% | 100% | 386 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,012 | 6,665 | 9.4 | 48% | 4% | 98% | 329 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,953 | 15,603 | 10.3 | 56% | 0% | 93% | 312 KB | 2 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,910 | 9,475 | 0.0 | 32% | 12% | 99% | 337 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,890 | 6,753 | 27.8 | 52% | 0% | 47% | 94 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,693 | 4,626 | 0.1 | 38% | 0% | 89% | 268 KB | 3 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 2,689 | 32,776 | 0.7 | 50% | 17% | 36% | 5,272 KB | 1 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,664 | 5,042 | 43.8 | 52% | 28% | 99% | 293 KB | 2 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E E D | 2,614 | 5,356 | 0.2 | 43% | 15% | 0% | 427 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,590 | 5,627 | 0.1 | 32% | 21% | 71% | 153 KB | 29 |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F B | 2,462 | 12,298 | 13.5 | 63% | 0% | 90% | 1,194 KB | 13 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,366 | 5,909 | 25.0 | 73% | 0% | 99% | 129 KB | 22 (+1) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,288 | 68,617 | 5.1 | 31% | 0% | 97% | 24 KB | 0 |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E E D | 2,274 | 6,316 | 13.5 | 47% | 0% | – | 96 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,244 | 9,704 | 29.2 | 10% | 13% | 100% | 617 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E C E | 2,204 | 14,746 | 19.1 | 76% | 13% | 99% | 607 KB | 11 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 2,075 | 8,558 | 23.9 | 0% | 0% | 92% | 489 KB | 27 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,871 | 4,789 | 12.4 | 39% | 28% | 82% | 225 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 1,774 | 8,405 | 46.2 | 74% | 8% | 95% | 119 KB | 8 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,751 | 3,751 | 21.4 | 21% | 0% | 98% | 119 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,738 | 7,390 | 15.2 | 64% | 0% | 100% | 176 KB | 0 |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,696 | 2,314 | 28.1 | 80% | 0% | 100% | 136 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 1,651 | 2,220 | 13.8 | 35% | 20% | – | 55 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,578 | 2,011 | 14.3 | 20% | 0% | 97% | 268 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E F D | 1,553 | 2,340 | 0.2 | 40% | 25% | 0% | 627 KB | 3 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,551 | 2,575 | 17.9 | 50% | 50% | 97% | 493 KB | 1 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,502 | 6,186 | 0.0 | 54% | 14% | – | 433 KB | 2 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,451 | 1,384 | 15.3 | 50% | 0% | 100% | 154 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,259 | 3,414 | 1.9 | 39% | 0% | 33% | 54 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 1,225 | 10,541 | 20.5 | 32% | 0% | 88% | 303 KB | 22 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E E D | 1,193 | 41,105 | 8.5 | 75% | 0% | 10% | 428 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,089 | 4,750 | 23.9 | 14% | 16% | 96% | 511 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | E F D | 1,080 | 10,347 | 11.7 | 32% | 0% | – | 115 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 810 | 10,137 | 12.8 | 58% | 0% | 100% | 960 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 739 | 3,141 | 0.0 | 71% | 0% | – | 80 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 669 | 4,192 | 0.0 | 43% | 0% | – | 202 KB | 4 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 591 | 6,367 | 0.0 | 20% | 0% | 33% | 397 KB | 456 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 428 | 2,827 | 0.1 | 63% | 0% | 100% | 133 KB | 7 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 404 | 2,894 | 5.6 | 5% | 0% | 81% | 466 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 341 | 6,969 | 15.6 | 11% | 0% | – | 408 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 341 | 966 | 6.6 | 0% | 0% | 94% | 72 KB | 4 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 323 | 44,389 | 12.8 | 31% | 28% | 97% | 66 KB | 3 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 304 | 7,540 | 10.3 | 56% | 36% | 98% | 43 KB | 1 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 218 | 9,046 | 1.5 | 60% | 16% | 55% | 149 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 177 | 1,494 | 9.3 | 62% | 0% | 100% | 173 KB | 219 (+2) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 132 | 4,169 | 0.0 | 20% | 0% | 0% | 473 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 95 | 2,146 | 7.0 | 55% | 0% | 98% | 42 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 83 | 355 | 1.1 | 40% | 0% | 100% | 102 KB | 2 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 68 | 752 | 2.9 | 52% | 0% | 100% | 59 KB | 1 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 32 | 394 | 0.0 | 34% | 0% | – | 18 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 482,864 | 41.0 | 30% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 34.1 | 67% | 43% | 88% | 1,999 KB | 1,391 (+11) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 397 | 33.3 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | 0 | 4,087 | 26.3 | 0% | 0% | 52% | 92 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 1,448 | 23.2 | 66% | 0% | 0% | 153 KB | 1 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 21.2 | 38% | 14% | 99% | 1,104 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F A | 0 | 2,299 | 20.7 | 71% | 0% | 100% | 73 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 20.2 | 52% | 34% | 92% | 916 KB | 4 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 16.2 | 34% | 0% | 97% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 1,720 | 12.6 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 6,541 | 12.2 | 26% | 0% | 98% | 149 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 7.4 | 58% | 0% | 97% | 333 KB | 4 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 4 | 6.7 | 0% | 0% | 89% | 150 KB | 347 (+1) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F C D | – | – | 5.2 | 70% | 72% | 0% | 1,061 KB | 457 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 0 | 1.0 | 59% | 0% | – | 5,619 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 76% | 3% | 75% | 812 KB | 4 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F C D | 0 | 31 | 0.3 | 70% | 0% | – | 232 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 7,558 | 0.2 | 47% | 0% | 86% | 1,451 KB | 1,096 (+2) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 779 | 0.2 | 15% | 0% | 8% | 904 KB | 1,275 (+2) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.2 | 56% | 0% | 97% | 14,566 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,168 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 0 | 2,780 | 0.0 | 0% | 0% | – | 15 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 346 | 0.0 | 0% | 0% | – | 59 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D B | – | – | 0.0 | 66% | 46% | 74% | 72 KB | 5 (+0) |
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
