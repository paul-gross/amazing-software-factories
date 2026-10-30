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
_361 repos, last measured 2026-10-30. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A E A | 83,765 | 112,966 | 34.5 | 54% | 25% | 100% | 406 KB | 80 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 67,983 | 230,171 | 122 | 57% | 4% | 51% | 307 KB | 4 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | A C B | 65,774 | 117,404 | 38.9 | 77% | 30% | 100% | 3,196 KB | 17 (+11) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 49,535 | 61,431 | 73.3 | 5% | 11% | 97% | 3,207 KB | 2,057 (+3) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 43,505 | 134,685 | 0.2 | 48% | 9% | 27% | 1,271 KB | 440 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 42,429 | 48,704 | 60.9 | 75% | 58% | 95% | 1,000 KB | 1 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | A D B | 42,278 | 230,844 | 1.4 | 70% | 34% | 85% | 3,340 KB | 7 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | A D D | 40,441 | 64,686 | 0.0 | 68% | 34% | – | 209 KB | 0 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 37,787 | 116,834 | 168 | 25% | 26% | 89% | 2,294 KB | 4 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B C B | 35,553 | 52,934 | 0.0 | 73% | 49% | 82% | 211 KB | 114 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | B F B | 34,158 | 51,988 | 35.0 | 42% | 35% | 99% | 624 KB | 11 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 32,333 | 66,516 | 28.9 | 78% | 15% | 75% | 785 KB | 4 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B D A | 30,038 | 30,451 | 81.6 | 62% | 1% | 85% | 60 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B E B | 29,786 | 36,620 | 18.6 | 56% | 3% | 97% | 383 KB | 1,591 (+4) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B C C | 29,623 | 40,561 | 28.6 | 78% | 14% | 98% | 722 KB | 9 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 29,514 | 33,925 | 32.4 | 41% | 52% | 94% | 1,464 KB | 92 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 27,737 | 30,801 | 94.9 | 28% | 38% | 90% | 4,201 KB | 77 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B D B | 27,509 | 29,018 | 33.4 | 68% | 2% | 77% | 745 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,047 | 32,653 | 21.5 | 73% | 46% | 89% | 769 KB | 5 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B F A | 26,818 | 57,979 | 37.5 | 59% | 22% | 95% | 200 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 26,751 | 29,505 | 18.1 | 25% | 13% | 78% | 6,732 KB | 129 (+2) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B E C | 24,903 | 28,911 | 100 | 50% | 57% | 76% | 373 KB | 74 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B D C | 24,539 | 35,495 | 28.9 | 68% | 19% | 94% | 363 KB | 10 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 23,146 | 41,472 | 123 | 43% | 15% | 97% | 144 KB | 18 (+1) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | B F D | 22,991 | 25,067 | 0.0 | 69% | 0% | 38% | 1,211 KB | 34 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | B E A | 22,910 | 24,622 | 12.7 | 55% | 11% | 90% | 258 KB | 0 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 22,630 | 43,574 | 0.0 | 70% | 62% | 96% | 549 KB | 2 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | B E A | 22,565 | 40,365 | 40.1 | 43% | 2% | 98% | 240 KB | 9 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B C C | 22,374 | 35,138 | 27.2 | 72% | 49% | 100% | 315 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | B F A | 21,528 | 20,010 | 30.4 | 62% | 0% | 99% | 49 KB | 23,783 (+1) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B C D | 21,430 | 393,780 | 0.0 | 89% | 0% | 0% | 3,286 KB | 1 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B D B | 21,209 | 27,542 | 47.2 | 63% | 16% | 98% | 533 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | B E A | 20,780 | 24,709 | 28.5 | 60% | 52% | 90% | 312 KB | 1 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B D C | 20,188 | 32,048 | 74.8 | 61% | 13% | 89% | 549 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C C B | 19,736 | 110,632 | 31.2 | 77% | 43% | 97% | 1,008 KB | 33 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 19,155 | 25,216 | 25.1 | 75% | 28% | 100% | 179 KB | 33 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C F A | 18,747 | 62,133 | 60.1 | 26% | 0% | 94% | 210 KB | 123 (+1) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | C D A | 18,360 | 79,762 | 16.5 | 65% | 4% | 96% | 353 KB | 0 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 17,814 | 24,497 | 3.1 | 48% | 7% | 96% | 2,284 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C B B | 17,585 | 34,841 | 22.9 | 81% | 23% | 80% | 199 KB | 6 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | C F B | 17,570 | 39,953 | 9.2 | 33% | 8% | 74% | 294 KB | 337 (+1) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B C | 17,400 | 25,591 | 0.0 | 85% | 16% | 66% | 318 KB | 0 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | C B C | 17,089 | 16,773 | 9.9 | 80% | 10% | 100% | 49 KB | 3 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 17,065 | 28,735 | 0.0 | 49% | 23% | 100% | 4,357 KB | 15 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C D A | 16,644 | 28,613 | 47.8 | 63% | 48% | 100% | 303 KB | 2 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | C F D | 15,918 | 29,599 | 0.1 | 28% | 9% | 26% | 2,879 KB | 2 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C C B | 15,599 | 20,163 | 24.6 | 73% | 0% | 90% | 1,105 KB | 8 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,352 | 43,099 | 6.8 | 4% | 0% | 92% | 442 KB | 138 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 15,274 | 24,179 | 40.7 | 36% | 53% | 98% | 1,331 KB | 8 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C C B | 15,237 | 19,295 | 23.4 | 72% | 35% | 92% | 608 KB | 1 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 15,027 | 31,544 | 0.0 | 88% | 44% | – | 1,231 KB | 3 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 14,655 | 35,211 | 39.9 | 3% | 47% | 100% | 225 KB | 7 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 14,525 | 27,273 | 46.5 | 5% | 7% | 96% | 249 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 14,464 | 35,034 | 25.6 | 34% | 18% | 96% | 480 KB | 21 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 14,249 | 21,096 | 67.0 | 48% | 61% | 79% | 275 KB | 6,479 (+9) |
| [vantt/forgent](https://github.com/vantt/forgent) | C E D | 13,869 | 40,263 | 0.0 | 45% | 5% | 0% | 299 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C D B | 13,855 | 26,431 | 31.9 | 64% | 61% | 82% | 1,406 KB | 70,478 (+38) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C E B | 13,821 | 21,674 | 186 | 59% | 52% | 100% | 2,355 KB | 1 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | C F C | 13,404 | 15,860 | 6.6 | 55% | 8% | 52% | 7,014 KB | 18 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | C D D | 13,285 | 26,657 | 0.0 | 63% | 19% | 28% | 284 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C C B | 13,153 | 738,929 | 47.2 | 76% | 57% | 82% | 416 KB | 9 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | C D B | 12,794 | 16,109 | 8.8 | 66% | 42% | 99% | 363 KB | 1 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | C F B | 12,642 | 15,276 | 37.4 | 44% | 0% | 100% | 80 KB | 3 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | C F B | 12,590 | 19,224 | 22.0 | 47% | 0% | 99% | 532 KB | 82 (+1) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 12,222 | 17,320 | 0.0 | 50% | 20% | 30% | 308 KB | 439 (+26) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C F D | 12,058 | 18,151 | 71.9 | 35% | 30% | 25% | 837 KB | 16 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 12,051 | 16,286 | 38.0 | 76% | 0% | 100% | 2,202 KB | 5 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C E C | 11,968 | 23,129 | 15.8 | 51% | 44% | 73% | 518 KB | 0 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C E B | 11,801 | 211,022 | 43.5 | 51% | 34% | 95% | 1,431 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 10,828 | 10.8 | 44% | 0% | 89% | 720 KB | 9 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C E D | 11,647 | 25,102 | 0.4 | 51% | 22% | – | 448 KB | 1 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C F B | 11,464 | 20,709 | 13.4 | 43% | 0% | 92% | 781 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | C C A | 11,379 | 11,570 | 28.9 | 70% | 35% | 100% | 159 KB | 5 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C D B | 11,361 | 13,215 | 43.8 | 60% | 9% | 99% | 847 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 11,005 | 11,678 | 14.6 | 50% | 36% | 80% | 1,214 KB | 13 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | C D B | 10,961 | 13,856 | 37.2 | 68% | 21% | 79% | 196 KB | 9 (+1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 10,949 | 12,553 | 0.0 | 86% | 33% | – | 203 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D A | 10,808 | 14,293 | 33.4 | 69% | 29% | 94% | 102 KB | 232 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 10,723 | 97,751 | 19.0 | 50% | 32% | 99% | 631 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 10,712 | 12,201 | 26.8 | 82% | 40% | 99% | 200 KB | 6 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | C F B | 10,626 | 26,857 | 6.0 | 27% | 0% | 91% | 569 KB | 6 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [ijun17/centralu](https://github.com/ijun17/centralu) | C F B | 10,415 | 11,868 | 26.2 | 26% | 0% | 96% | 628 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | C F B | 10,391 | 13,289 | 29.4 | 19% | 42% | 95% | 160 KB | 10 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | C F C | 10,373 | 30,650 | 0.0 | 33% | 21% | 99% | 938 KB | 29 (+1) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | C E C | 10,364 | 16,367 | 12.4 | 53% | 31% | 66% | 42 KB | 13 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C E D | 10,074 | 36,488 | 12.4 | 45% | 48% | 0% | 144 KB | 15 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | C F B | 10,021 | 22,700 | 8.8 | 56% | 17% | 83% | 680 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D C D | 9,882 | 14,717 | 8.5 | 72% | 0% | 32% | 199 KB | 8 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 9,836 | 23,518 | 2.9 | 13% | 0% | 80% | 1,423 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | D C D | 9,832 | 46,103 | 0.0 | 71% | 30% | 29% | 155 KB | 116 (+2) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F D | 9,794 | 44,244 | 57.8 | 7% | 0% | 72% | 3,975 KB | 1 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 9,791 | 13,497 | 19.8 | 15% | 0% | 97% | 221 KB | 5 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 9,623 | 18,282 | 0.0 | 34% | 6% | 96% | 674 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D D B | 9,393 | 485,754 | 33.1 | 63% | 6% | 88% | 1,414 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 9,357 | 40,197 | 52.7 | 11% | 44% | 100% | 59 KB | 0 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | D B A | 9,272 | 230,324 | 39.9 | 86% | 26% | 99% | 158 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | D F C | 9,197 | 33,007 | 25.9 | 29% | 0% | 54% | 4,722 KB | 96 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D E C | 9,159 | 15,236 | 0.0 | 80% | 15% | 68% | 257 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D F A | 9,106 | 24,330 | 0.0 | 60% | 0% | 93% | 224 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C A | 9,063 | 18,193 | 18.4 | 73% | 65% | 86% | 138 KB | 5 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | D B B | 9,017 | 18,037 | 20.8 | 90% | 10% | 85% | 92 KB | 0 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D F B | 8,788 | 144,659 | 15.2 | 50% | 16% | 87% | 126 KB | 4 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | D E C | 8,779 | 22,649 | 0.0 | 52% | 52% | 100% | 939 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | D F B | 8,602 | 13,120 | 19.8 | 17% | 2% | 77% | 260 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 8,463 | 9,741 | 21.0 | 0% | 25% | 98% | 544 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 8,448 | 33,728 | 0.0 | 77% | 2% | 100% | 503 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D B B | 8,383 | 17,185 | 13.4 | 87% | 54% | 94% | 372 KB | 2 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | D E D | 8,185 | 15,528 | 0.0 | 57% | 7% | 34% | 535 KB | 1 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | D E D | 8,029 | 10,816 | 0.0 | 53% | 0% | – | 334 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 7,986 | 14,327 | 0.1 | 46% | 7% | 96% | 390 KB | 2 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D C C | 7,953 | 9,888 | 0.4 | 76% | 17% | 61% | 376 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | D E B | 7,929 | 137,298 | 89.6 | 54% | 10% | 99% | 614 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D B C | 7,879 | 9,732 | 15.3 | 87% | 23% | 94% | 150 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 7,842 | 10,450 | 18.4 | 38% | 44% | 78% | 382 KB | 7 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,755 | 9,747 | 5.3 | 7% | 48% | 89% | 3,869 KB | 548 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 7,740 | 8,368 | 28.2 | 48% | 0% | 99% | 678 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 7,719 | 17,294 | 3.5 | 74% | 0% | 90% | 319 KB | 1 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | D F A | 7,669 | 14,375 | 57.2 | 46% | 21% | 96% | 135 KB | 1 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 7,668 | 11,793 | 0.1 | 23% | 9% | 86% | 918 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | D F E | 7,633 | 29,613 | 47.3 | 53% | 2% | 99% | 20,146 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D E B | 7,463 | 14,083 | 10.7 | 68% | 0% | 92% | 89 KB | 0 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 7,433 | 10,146 | 6.9 | 35% | 22% | 93% | 403 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D E D | 7,309 | 18,294 | 7.2 | 48% | 33% | – | 496 KB | 2 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D C A | 7,211 | 9,511 | 37.6 | 79% | 2% | 100% | 128 KB | 1 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | D F D | 7,016 | 18,893 | 29.4 | 52% | 14% | 93% | 599 KB | 22 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 85,333 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 6,726 | 58,775 | 19.7 | 42% | 0% | 99% | 251 KB | 2 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D F B | 6,692 | 9,208 | 17.2 | 70% | 0% | 99% | 569 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 6,644 | 10,776 | 44.6 | 9% | 44% | 86% | 334 KB | 1 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D D D | 6,628 | 12,115 | 52.5 | 63% | 2% | – | 408 KB | 3 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | D E B | 6,460 | 30,018 | 23.8 | 52% | 0% | 93% | 158 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | D F B | 6,243 | 21,055 | 16.0 | 76% | 0% | 91% | 86 KB | 6 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D F C | 6,240 | 7,939 | 31.6 | 48% | 31% | 81% | 194 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | D F B | 6,169 | 9,863 | 8.0 | 10% | 0% | 99% | 83 KB | 2 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D D C | 6,051 | 10,931 | 21.8 | 67% | 23% | 100% | 42 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D C B | 6,032 | 13,828 | 0.0 | 75% | 19% | 96% | 590 KB | 1 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | D F D | 6,029 | 11,470 | 0.0 | 37% | 4% | – | 370 KB | 2 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 5,958 | 9,325 | 15.3 | 47% | 0% | 91% | 376 KB | 2 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | D F B | 5,886 | 20,668 | 14.3 | 38% | 39% | 96% | 518 KB | 19 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 5,683 | 31,921 | 0.0 | 60% | 17% | 50% | 514 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 5,552 | 10,139 | 43.1 | 32% | 53% | 100% | 581 KB | 5 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | D F B | 5,433 | 12,888 | 8.8 | 69% | 0% | 97% | 45 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D C B | 5,373 | 15,480 | 31.4 | 71% | 46% | 100% | 1,172 KB | 0 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D E C | 5,324 | 13,411 | 22.6 | 70% | 0% | 65% | 174 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | D F A | 5,278 | 29,101 | 15.9 | 25% | 44% | 100% | 386 KB | 2 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D E B | 5,244 | 7,080 | 7.8 | 60% | 0% | 91% | 685 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | D C B | 5,124 | 15,180 | 41.1 | 78% | 0% | 98% | 196 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | D F E | 5,091 | 8,502 | 22.9 | 43% | 7% | 85% | 1,170 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | D F B | 5,067 | 6,090 | 17.6 | 14% | 16% | 96% | 141 KB | 1 (+1) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | D F B | 5,066 | 4,904 | 10.6 | 46% | 0% | 99% | 80 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 5,052 | 13,335 | 44.6 | 6% | 2% | 99% | 83 KB | 2 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 5,024 | 8,783 | 44.8 | 0% | 17% | 89% | 67 KB | 62 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | E E B | 4,989 | 5,733 | 63.8 | 54% | 0% | 98% | 808 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | E C B | 4,939 | 20,640 | 33.7 | 86% | 0% | 99% | 571 KB | 37 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | E F B | 4,938 | 8,558 | 33.7 | 0% | 0% | 99% | 884 KB | 4 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 4,886 | 10,879 | 1.3 | 15% | 2% | 76% | 85 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E F D | 4,855 | 5,945 | 0.0 | 27% | 0% | 0% | 601 KB | 1 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E D B | 4,799 | 24,560 | 7.9 | 65% | 30% | 83% | 24 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 4,572 | 16,084 | 42.9 | 63% | 52% | – | 440 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 4,548 | 5,654 | 19.9 | 8% | 49% | 100% | 155 KB | 1 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E F B | 4,519 | 8,447 | 29.1 | 38% | 33% | 99% | 1,572 KB | 3 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 4,511 | 7,819 | 11.9 | 14% | 32% | 99% | 415 KB | 12 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E C D | 4,504 | 5,372 | 0.9 | 71% | 38% | 0% | 184 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 4,402 | 14,962 | 21.2 | 43% | 13% | 84% | 77 KB | 10 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 4,336 | 6,457 | 24.2 | 56% | 13% | 100% | 204 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 4,318 | 6,217 | 0.4 | 32% | 11% | 0% | 518 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | E F C | 4,202 | 8,582 | 23.0 | 73% | 0% | 90% | 25 KB | 17 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,194 | 7,261 | 24.8 | 20% | 0% | 100% | 840 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,961 | 5,704 | 12.1 | 55% | 0% | 98% | 137 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 3,897 | 91,726 | 10.8 | 17% | 0% | – | 88 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 3,894 | 11,429 | 1.8 | 61% | 0% | 91% | 5,602 KB | 1 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E B | 3,818 | 50,471 | 27.9 | 63% | 0% | 81% | 59 KB | 1 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | E F C | 3,452 | 75,059 | 5.6 | 60% | 0% | 91% | 78 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 3,397 | 5,855 | 0.0 | 21% | 0% | 33% | 399 KB | 464 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | E F B | 3,389 | 14,824 | 5.4 | 56% | 0% | 86% | 262 KB | 1,248 (+2) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,351 | 9,240 | 0.0 | 31% | 10% | 0% | 472 KB | 4 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | E F E | 3,334 | 7,058 | 15.9 | 12% | 0% | 71% | 332 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 3,323 | 6,797 | 7.1 | 40% | 0% | 91% | 543 KB | 11 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 3,296 | 75,534 | 18.1 | 30% | 6% | 97% | 378 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E F B | 3,240 | 3,827 | 23.4 | 64% | 0% | 99% | 146 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,139 | 7,571 | 26.8 | 33% | 17% | 100% | 386 KB | 17 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F B | 3,049 | 15,250 | 24.3 | 12% | 21% | 76% | 215 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F C | 3,048 | 5,775 | 0.0 | 20% | 22% | 97% | 458 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E E A | 3,005 | 13,507 | 23.6 | 46% | 0% | 99% | 399 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,943 | 3,187 | 41.9 | 56% | 22% | 90% | 331 KB | 2 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,909 | 6,124 | 28.0 | 84% | 9% | 94% | 512 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E C C | 2,874 | 5,878 | 24.4 | 71% | 62% | 96% | 976 KB | 1 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 2,856 | 21,076 | 15.0 | 40% | 18% | 100% | 216 KB | 1 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | E F A | 2,789 | 7,449 | 20.2 | 36% | 7% | 100% | 41 KB | 3 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 2,733 | 4,847 | 8.6 | 53% | 41% | 99% | 343 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E E A | 2,700 | 22,519 | 62.4 | 62% | 0% | 100% | 169 KB | 2 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 2,632 | 7,498 | 13.4 | 28% | 16% | 99% | 165 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E E D | 2,575 | 5,409 | 40.1 | 42% | 39% | – | 211 KB | 3 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 2,477 | 5,211 | 6.8 | 35% | 0% | 96% | 522 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 2,476 | 11,395 | 26.9 | 39% | 5% | 96% | 46 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 2,471 | 3,646 | 14.9 | 32% | 16% | 99% | 450 KB | 12 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,373 | 2,724 | 17.9 | 52% | 0% | 100% | 127 KB | 23 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,371 | 3,551 | 9.9 | 26% | 0% | 0% | 285 KB | 25 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 2,362 | 5,451 | 25.0 | 26% | 18% | 93% | 1,116 KB | 1 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 2,355 | 4,133 | 19.7 | 4% | 0% | 95% | 277 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 2,255 | 7,820 | 13.8 | 60% | 0% | 95% | 236 KB | 5 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F A | 2,244 | 5,216 | 27.4 | 58% | 0% | 90% | 318 KB | 159 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E E D | 2,173 | 6,524 | 0.0 | 52% | 0% | – | 803 KB | 2 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,138 | 5,201 | 20.8 | 6% | 31% | 97% | 94 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,136 | 5,903 | 0.0 | 28% | 0% | 0% | 1,186 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E D D | 2,117 | 6,739 | 6.3 | 67% | 8% | – | 311 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,080 | 5,691 | 13.0 | 15% | 0% | 96% | 644 KB | 2 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 2,040 | 7,481 | 13.8 | 0% | 0% | – | 526 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,017 | 6,698 | 13.9 | 31% | 0% | 100% | 1,069 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | E F B | 2,000 | 10,226 | 3.2 | 32% | 28% | 95% | 43 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,965 | 5,330 | 0.0 | 55% | 41% | 42% | 267 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F A | 1,940 | 6,847 | 26.4 | 42% | 0% | 100% | 377 KB | 49 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 1,939 | 15,368 | 20.4 | 43% | 0% | 98% | 184 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E E B | 1,889 | 2,852 | 9.5 | 41% | 0% | 100% | 521 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E C E | 1,871 | 10,471 | 18.1 | 71% | 0% | 99% | 632 KB | 11 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E E B | 1,856 | 3,757 | 30.8 | 57% | 0% | 100% | 1,060 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F C | 1,804 | 4,540 | 14.4 | 34% | 20% | 64% | 271 KB | 1 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 1,773 | 6,417 | 15.4 | 25% | 38% | 92% | 333 KB | 165 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,773 | 2,573 | 13.4 | 79% | 0% | 86% | 625 KB | 4 (+1) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E E B | 1,707 | 6,880 | 7.7 | 71% | 8% | 100% | 57 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 1,663 | 4,493 | 21.0 | 38% | 0% | 98% | 502 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | E F D | 1,622 | 16,422 | 0.0 | 11% | 0% | – | 861 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,594 | 2,081 | 35.8 | 52% | 7% | 100% | 403 KB | 2 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,561 | 3,434 | 14.8 | 25% | 0% | – | 49 KB | 3 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,534 | 3,985 | 62.1 | 23% | 0% | 99% | 695 KB | 14 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,461 | 2,072 | 12.9 | 29% | 0% | 100% | 4,314 KB | 26 (+3) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 1,442 | 2,181 | 2.1 | 23% | 0% | 100% | 192 KB | 7 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,415 | 3,415 | 27.4 | 23% | 0% | 99% | 527 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 1,386 | 4,150 | 0.0 | 8% | 7% | 100% | 472 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 1,374 | 3,004 | 34.0 | 63% | 37% | 88% | 980 KB | 112 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | E F C | 1,369 | 6,081 | 6.0 | 19% | 0% | 91% | 3,845 KB | 1 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 1,355 | 4,375 | 36.6 | 79% | 0% | 96% | 257 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,334 | 2,931 | 13.2 | 60% | 0% | 96% | 61 KB | 0 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E E B | 1,309 | 3,292 | 10.5 | 77% | 3% | 92% | 446 KB | 2 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,271 | 2,481 | 24.5 | 59% | 0% | 83% | 518 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 1,253 | 2,914 | 28.4 | 26% | 0% | 73% | 193 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 1,249 | 27,042 | 0.2 | 7% | 0% | 40% | 1,479 KB | 1,111 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | E F C | 1,210 | 45,899 | 45.0 | 7% | 0% | 100% | 703 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F C | 1,191 | 3,330 | 3.6 | 0% | 0% | 100% | 1,127 KB | 5 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,175 | 9,488 | 0.0 | 0% | 0% | – | 200 KB | 29 (+1) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 1,111 | 3,396 | 5.9 | 34% | 10% | 97% | 134 KB | 238 (+6) |
| [codethread/hive](https://github.com/codethread/hive) | E F D | 1,086 | 4,877 | 0.9 | 58% | 28% | – | 53 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 1,059 | 3,037 | 35.5 | 54% | 0% | 97% | 107 KB | 4 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,041 | 2,088 | 9.4 | 41% | 0% | 90% | 161 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,037 | 3,202 | 29.1 | 0% | 0% | 97% | 122 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 997 | 6,970 | 6.6 | 5% | 18% | 96% | 337 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 867 | 1,211 | 9.9 | 10% | 0% | 100% | 67 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F C D | 867 | 3,049 | 0.0 | 75% | 20% | 0% | 324 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 851 | 14,576 | 0.0 | 40% | 0% | 78% | 554 KB | 29 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 845 | 1,523 | 0.0 | 17% | 0% | 99% | 444 KB | 0 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 842 | 19,601 | 6.9 | 47% | 35% | 80% | 83 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 801 | 83,630 | 4.4 | 41% | 0% | 95% | 163 KB | 13 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 740 | 5,005 | 13.2 | 26% | 0% | 95% | 8,119 KB | 1 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 725 | 1,434 | 0.0 | 57% | 0% | 100% | 499 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | F E D | 685 | 7,318 | 24.8 | 56% | 15% | 99% | 396 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 685 | 2,787 | 11.9 | 0% | 0% | – | 414 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 607 | 7,355 | 11.9 | 41% | 31% | 94% | 5,221 KB | 40,398 (+42) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F B | 561 | 19,892 | 21.0 | 24% | 0% | 100% | 983 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 529 | 61,966 | 0.0 | 36% | 0% | – | 8,190 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 510 | 1,108 | 0.1 | 71% | 41% | 0% | 658 KB | 3 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 492 | 1,778 | 20.9 | 30% | 0% | 95% | 448 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 479 | 1,006 | 15.3 | 32% | 0% | 98% | 435 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 421 | 1,668 | 13.7 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 321 | 2,277 | 10.5 | 0% | 0% | 94% | 92 KB | 1 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 317 | 803 | 9.2 | 26% | 0% | 90% | 6,579 KB | 8 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 306 | 2,508 | 1.5 | 20% | 0% | 96% | 52 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 291 | 6,592 | 13.8 | 10% | 0% | 97% | 331 KB | 23 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 272 | 39,245 | 5.0 | 6% | 11% | 87% | 149 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F E E | 121 | 1,933 | 3.6 | 47% | 46% | 0% | 115 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 77 | 2,339 | 11.1 | 29% | 0% | 99% | 92 KB | 1 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 73 | 1,236 | 1.2 | 0% | 0% | 33% | 144 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 49 | 3,698 | 6.9 | 50% | 0% | 100% | 151 KB | 2 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 49 | 950 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 32 | 1,659 | 0.0 | 14% | 6% | 84% | 478 KB | 6 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | F F C | 27 | 7,527 | 0.0 | 22% | 0% | 61% | 405 KB | 3 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 12 | 4,650 | 20.1 | 26% | 0% | 97% | 93 KB | 1 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 11 | 2,565 | 0.0 | 14% | 0% | – | 159 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 2 | 199,091 | 0.0 | 57% | 0% | – | 110 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 1 | 211 | 8.6 | 0% | 0% | 83% | 15 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 2,935 | 41.9 | 0% | 0% | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F F B | – | – | 37.2 | 38% | 28% | 90% | 2,198 KB | 1,461 (+3) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 480 | 27.4 | 0% | 0% | 92% | 2,600 KB | 36 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 25.9 | – | – | 98% | 231 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F D | 0 | 1,369 | 23.8 | 64% | 0% | 47% | 100 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F E C | – | – | 23.3 | 43% | 0% | 100% | 342 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | 0 | 0 | 21.9 | – | – | 98% | 363 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 751 | 21.0 | 0% | 0% | 100% | 88 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F C B | – | – | 20.6 | 72% | 0% | 95% | 983 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 19.1 | – | – | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.6 | 8% | 0% | 12% | 279 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 0 | 16.5 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 3,945 | 16.2 | 0% | 0% | 96% | 66 KB | 3 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 104 | 15.9 | 0% | 0% | 76% | 1,538 KB | 6 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 3,585 | 15.5 | 57% | 0% | 88% | 700 KB | 4 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 0 | 9,293 | 15.0 | 15% | 0% | 93% | 576 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 0 | 2,360 | 14.8 | 0% | 0% | 100% | 617 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 1,963 | 13.9 | 0% | 0% | 98% | 489 KB | 55 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 1,119 | 13.9 | 0% | 0% | 98% | 49 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 12.8 | – | – | 98% | 43 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 25 | 12.1 | 0% | 0% | – | 55 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 571 | 12.0 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 49 | 9.9 | 0% | 0% | 97% | 41 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 411 | 9.5 | 0% | 0% | 99% | 99 KB | 4 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 9.0 | 48% | 0% | 0% | 206 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 372 | 8.5 | 0% | 0% | 80% | 552 KB | 2 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 0 | 8.4 | – | – | 99% | 298 KB | 5 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 2,035 | 8.2 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 514 | 8.2 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 3,881 | 8.1 | 0% | 0% | – | 100 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 7.2 | – | – | 98% | 723 KB | 6 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 6.9 | – | – | 98% | 149 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 6.7 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 25 | 6.6 | 0% | 0% | 96% | 787 KB | 2 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 5.5 | – | – | 90% | 195 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 602 | 5.0 | 0% | 0% | 75% | 161 KB | 2 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 1 | 4.8 | 0% | 0% | 94% | 24 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 4.8 | – | – | – | 115 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 4.2 | 29% | 6% | 0% | 472 KB | 458 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 3.5 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 3 | 2.9 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 0 | 2.9 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 1.4 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 0 | 1.4 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | 0 | 1,244 | 1.3 | 0% | 0% | – | 311 KB | 4 (+1) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.6 | 66% | 0% | 91% | 822 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 76% | 44% | 96% | 34,213 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 0 | 1,894 | 0.1 | 0% | 0% | 76% | 152 KB | 29 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 543 | 0.1 | 0% | 0% | 16% | 904 KB | 1,302 (+2) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F C | – | – | 0.1 | 43% | 0% | 50% | 84 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | 0 | 1,224 | 0.0 | 29% | 0% | – | 3,234 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 449 | 0.0 | 22% | 0% | 94% | 268 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 206 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 1,587 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 12 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+1) |
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
