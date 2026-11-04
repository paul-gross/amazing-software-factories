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
_361 repos, last measured 2026-11-04. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A F B | 83,763 | 86,178 | 51.5 | 34% | 12% | 71% | 408 KB | 85 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | A E D | 53,886 | 73,818 | 0.1 | 59% | 62% | 41% | 2,623 KB | 2 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 53,036 | 67,228 | 44.1 | 73% | 59% | 83% | 739 KB | 11 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A E A | 47,735 | 63,444 | 155 | 44% | 70% | 97% | 212 KB | 19 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 43,741 | 48,261 | 67.0 | 36% | 56% | 99% | 3,390 KB | 2,090 (+8) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 42,291 | 218,124 | 121 | 40% | 6% | 53% | 309 KB | 4 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 40,133 | 43,434 | 69.3 | 74% | 37% | 97% | 1,036 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 37,787 | 198,076 | 163 | 14% | 4% | 89% | 2,294 KB | 4 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B E B | 35,750 | 51,321 | 98.5 | 54% | 28% | 91% | 4,731 KB | 79 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B D B | 34,048 | 83,096 | 57.4 | 68% | 12% | 78% | 592 KB | 1 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B C B | 33,179 | 44,630 | 0.0 | 86% | 50% | 82% | 221 KB | 117 (+2) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 30,874 | 53,924 | 0.0 | 59% | 28% | – | 458 KB | 2 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 29,599 | 38,629 | 29.5 | 23% | 41% | 100% | 1,619 KB | 96 (+1) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 29,316 | 41,492 | 35.9 | 78% | 22% | 89% | 805 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B D B | 27,646 | 206,313 | 1.3 | 66% | 4% | 100% | 3,340 KB | 7 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,047 | 27,495 | 21.8 | 74% | 49% | 92% | 803 KB | 6 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 26,403 | 35,715 | 44.8 | 88% | 31% | 85% | 845 KB | 0 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 26,027 | 29,712 | 28.0 | 77% | 40% | 100% | 363 KB | 11 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | B F A | 24,116 | 73,785 | 7.3 | 17% | 18% | 92% | 462 KB | 139 (-1) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B D A | 23,542 | 37,933 | 47.7 | 64% | 18% | 90% | 332 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B C D | 21,938 | 40,259 | 55.9 | 71% | 55% | 25% | 822 KB | 16 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | B F B | 20,911 | 75,898 | 18.8 | 49% | 37% | 84% | 126 KB | 5 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | B D C | 20,879 | 23,304 | 25.7 | 69% | 52% | 100% | 184 KB | 33 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C D C | 19,570 | 38,624 | 24.1 | 61% | 11% | 100% | 314 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 19,505 | 26,864 | 18.3 | 9% | 16% | 89% | 8,727 KB | 132 (+1) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 19,123 | 29,902 | 0.0 | 85% | 30% | 38% | 1,376 KB | 35 (+1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C D A | 18,702 | 48,261 | 44.8 | 66% | 28% | 100% | 302 KB | 3 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C E C | 17,711 | 27,656 | 2.9 | 42% | 22% | 98% | 2,284 KB | 0 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F C | 16,214 | 59,625 | 10.3 | 30% | 11% | 69% | 533 KB | 19 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 15,809 | 28,124 | 0.0 | 82% | 56% | – | 1,123 KB | 3 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C E C | 15,006 | 24,108 | 14.9 | 67% | 29% | 92% | 527 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 14,614 | 23,094 | 28.6 | 79% | 0% | 100% | 450 KB | 9 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C F D | 14,416 | 19,016 | 14.3 | 47% | 0% | 16% | 144 KB | 15 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 14,225 | 46,851 | 26.5 | 31% | 45% | 99% | 493 KB | 21 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C C B | 13,990 | 14,313 | 13.7 | 75% | 24% | 93% | 1,229 KB | 13 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 13,861 | 17,854 | 20.6 | 55% | 18% | 88% | 735 KB | 0 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | C F B | 13,822 | 23,781 | 25.8 | 34% | 0% | 73% | 312 KB | 1 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E C | 13,669 | 20,082 | 99.9 | 53% | 17% | 76% | 375 KB | 74 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B C | 13,439 | 20,227 | 0.0 | 84% | 43% | 51% | 357 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | C E B | 13,415 | 22,221 | 15.3 | 46% | 38% | 99% | 258 KB | 13 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 13,367 | 25,979 | 90.2 | 54% | 71% | 100% | 4,357 KB | 15 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F C | 12,885 | 17,545 | 0.0 | 60% | 30% | 69% | 311 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | C C D | 12,784 | 19,687 | 0.0 | 70% | 38% | – | 373 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C A B | 12,706 | 16,033 | 68.2 | 90% | 19% | 96% | 530 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 12,619 | 20,570 | 39.8 | 4% | 56% | 100% | 225 KB | 7 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 12,421 | 22,532 | 0.0 | 47% | 1% | 96% | 590 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 12,410 | 60,445 | 27.0 | 45% | 14% | 63% | 255 KB | 1 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 12,268 | 43,984 | 0.0 | 68% | 2% | – | 983 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 12,254 | 15,756 | 67.3 | 43% | 10% | 78% | 275 KB | 6,548 (+5) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F C | 12,229 | 18,586 | 31.1 | 67% | 10% | 98% | 599 KB | 22 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | C E C | 12,163 | 19,031 | 4.8 | 52% | 19% | 51% | 326 KB | 2 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | C F D | 11,978 | 15,420 | 0.0 | 30% | 0% | 0% | 601 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C C D | 11,934 | 68,651 | 0.0 | 72% | 3% | 32% | 158 KB | 116 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | C F B | 11,681 | 14,632 | 25.0 | 83% | 10% | 80% | 179 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 11,539 | 29,258 | 32.6 | 80% | 31% | 98% | 200 KB | 6 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C E B | 11,225 | 16,791 | 17.2 | 58% | 2% | 85% | 781 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 11,173 | 12,652 | 47.2 | 23% | 66% | 88% | 335 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C E B | 11,172 | 18,297 | 171 | 69% | 2% | 98% | 2,404 KB | 1 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C E C | 11,162 | 31,440 | 32.2 | 56% | 34% | 61% | 1,425 KB | 70,670 (+39) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C C C | 10,887 | 143,566 | 0.0 | 71% | 27% | 50% | 560 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | C F C | 10,581 | 785,535 | 46.4 | 5% | 0% | 100% | 703 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C F B | 10,464 | 21,815 | 24.4 | 27% | 17% | 100% | 562 KB | 1 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C E A | 10,218 | 30,441 | 91.2 | 70% | 1% | 100% | 62 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 10,187 | 22,223 | 54.0 | 29% | 23% | 100% | 154 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | D C B | 9,737 | 51,082 | 29.3 | 73% | 16% | 98% | 1,094 KB | 36 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D F B | 9,632 | 12,605 | 23.5 | 65% | 13% | 99% | 1,149 KB | 8 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D E C | 9,629 | 13,919 | 5.8 | 41% | 61% | 79% | 3,991 KB | 552 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 9,481 | 11,295 | 0.0 | 10% | 4% | 89% | 674 KB | 2 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C A | 9,393 | 18,837 | 17.6 | 80% | 40% | 89% | 141 KB | 5 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D E B | 9,291 | 9,934 | 49.6 | 60% | 33% | 98% | 937 KB | 2 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | D F D | 9,249 | 30,551 | 0.1 | 22% | 6% | 40% | 1,271 KB | 445 (+4) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F E | 9,128 | 43,072 | 50.4 | 5% | 0% | 83% | 3,975 KB | 1 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 9,102 | 10,591 | 14.4 | 57% | 27% | 97% | 446 KB | 12 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D E A | 8,167 | 9,929 | 39.9 | 75% | 31% | 100% | 131 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D D A | 8,138 | 13,477 | 29.2 | 61% | 27% | 85% | 102 KB | 233 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D F B | 7,966 | 12,437 | 25.5 | 65% | 46% | 100% | 1,666 KB | 3 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | D F C | 7,960 | 146,449 | 74.8 | 46% | 23% | 87% | 378 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | D E B | 7,916 | 9,939 | 5.4 | 70% | 8% | 100% | 211 KB | 7 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | D F D | 7,633 | 13,080 | 56.6 | 24% | 2% | 95% | 20,146 KB | 1 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D E C | 7,620 | 10,350 | 13.6 | 78% | 7% | 99% | 163 KB | 1 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | D D A | 7,463 | 66,583 | 18.4 | 64% | 0% | 99% | 353 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 7,220 | 11,092 | 9.9 | 59% | 41% | 24% | 219 KB | 9 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D E B | 7,186 | 202,937 | 35.8 | 51% | 55% | 99% | 214 KB | 9 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | D F D | 7,122 | 10,148 | 12.9 | 45% | 0% | 0% | 333 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D F B | 7,113 | 8,095 | 12.0 | 28% | 0% | 100% | 89 KB | 0 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D E B | 6,777 | 23,332 | 11.7 | 52% | 41% | 76% | 29 KB | 0 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 6,761 | 7,555 | 32.5 | 59% | 26% | 99% | 766 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 6,486 | 97,295 | 13.6 | 39% | 33% | – | 95 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | D F C | 6,302 | 7,490 | 41.2 | 5% | 0% | 96% | 249 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | D F B | 6,236 | 14,273 | 18.9 | 2% | 0% | 83% | 2,626 KB | 41 (+1) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | D F C | 6,229 | 12,505 | 32.0 | 55% | 16% | 99% | 636 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | D F D | 6,173 | 15,514 | 0.1 | 20% | 0% | 91% | 1,468 KB | 1,117 (+1) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | D F D | 6,105 | 9,141 | 0.8 | 31% | 6% | – | 452 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | D F B | 5,930 | 12,376 | 26.6 | 30% | 5% | 95% | 628 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 5,739 | 11,154 | 19.9 | 19% | 0% | 98% | 223 KB | 5 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 5,733 | 7,223 | 17.6 | 0% | 17% | 100% | 544 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D D B | 5,638 | 9,310 | 15.2 | 66% | 44% | 93% | 395 KB | 2 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 5,586 | 13,198 | 50.1 | 4% | 40% | 100% | 59 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D F B | 5,505 | 9,051 | 0.0 | 76% | 0% | 95% | 455 KB | 3 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | D F C | 5,375 | 32,974 | 12.5 | 58% | 22% | 94% | 356 KB | 23 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D E D | 5,290 | 13,793 | 12.8 | 43% | 34% | – | 569 KB | 2 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 5,232 | 24,433 | 0.0 | 37% | 0% | – | 202 KB | 29 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D E B | 5,220 | 6,611 | 16.0 | 58% | 55% | 99% | 590 KB | 1 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 5,193 | 9,383 | 20.0 | 22% | 0% | 100% | 537 KB | 86 (+1) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | D F B | 5,082 | 17,355 | 29.6 | 32% | 0% | 100% | 158 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,983 | 5,873 | 17.0 | 49% | 0% | 100% | 254 KB | 2 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 4,951 | 17,080 | 0.0 | 23% | 0% | 98% | 948 KB | 48 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | E E B | 4,703 | 122,751 | 44.8 | 58% | 4% | 86% | 1,435 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E D D | 4,666 | 11,191 | 54.4 | 62% | 15% | – | 432 KB | 3 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,639 | 9,601 | 7.3 | 24% | 32% | 93% | 359 KB | 0 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E F B | 4,597 | 21,653 | 36.1 | 60% | 11% | 100% | 2,256 KB | 5 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | E F D | 4,571 | 102,265 | 0.0 | 82% | 0% | 0% | 3,286 KB | 1 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E F B | 4,353 | 7,227 | 11.1 | 49% | 0% | 97% | 88 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E E B | 4,352 | 11,991 | 42.7 | 72% | 2% | 98% | 99 KB | 3 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E C B | 4,347 | 7,907 | 6.5 | 71% | 38% | 97% | 547 KB | 11 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 4,325 | 5,990 | 0.1 | 51% | 15% | 86% | 1,037 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E E C | 4,323 | 6,483 | 42.7 | 45% | 38% | 100% | 589 KB | 5 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 4,192 | 4,432 | 16.6 | 31% | 32% | – | 51 KB | 3 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,183 | 11,242 | 22.9 | 2% | 4% | 97% | 889 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 4,141 | 4,643 | 15.5 | 22% | 15% | 97% | 386 KB | 2 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | E F B | 4,076 | 9,334 | 26.6 | 29% | 25% | 100% | 571 KB | 37 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E F D | 4,044 | 6,607 | 42.1 | 52% | 16% | – | 213 KB | 3 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | E C A | 4,030 | 171,561 | 48.4 | 70% | 26% | 95% | 158 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E D C | 3,985 | 3,834 | 13.9 | 69% | 40% | 100% | 245 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,935 | 6,412 | 25.8 | 38% | 36% | 100% | 391 KB | 17 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,923 | 13,363 | 12.8 | 55% | 0% | 95% | 150 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F B | 3,837 | 16,358 | 27.7 | 47% | 0% | 82% | 59 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F C | 3,637 | 13,067 | 26.2 | 19% | 0% | 50% | 184 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 3,631 | 7,588 | 0.0 | 19% | 0% | 33% | 402 KB | 464 (-1) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 3,588 | 12,117 | 0.1 | 38% | 0% | 100% | 472 KB | 0 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 3,584 | 4,280 | 24.0 | 28% | 33% | 97% | 269 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 3,580 | 17,851 | 15.8 | 19% | 0% | 78% | 294 KB | 2 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 3,388 | 4,427 | 17.5 | 30% | 0% | 90% | 458 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 3,374 | 4,627 | 0.9 | 58% | 30% | 0% | 194 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E D B | 3,357 | 5,283 | 34.9 | 66% | 20% | 99% | 354 KB | 2 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,264 | 4,101 | 17.1 | 16% | 0% | 95% | 143 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | E F A | 3,204 | 4,541 | 21.9 | 60% | 12% | 99% | 96 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 3,153 | 72,695 | 80.0 | 16% | 0% | 99% | 614 KB | 2 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F C | 3,123 | 8,814 | 9.8 | 32% | 0% | 85% | 105 KB | 3 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 3,038 | 9,449 | 40.6 | 37% | 19% | 100% | 1,357 KB | 8 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 3,016 | 6,049 | 35.4 | 53% | 13% | 96% | 512 KB | 0 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 2,961 | 4,132 | 0.1 | 30% | 0% | 46% | 376 KB | 1 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 2,896 | 15,108 | 25.7 | 5% | 27% | 95% | 363 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E C B | 2,883 | 9,570 | 33.2 | 79% | 66% | 99% | 36 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 2,882 | 5,905 | 7.5 | 10% | 33% | 88% | 739 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F A | 2,835 | 6,569 | 15.7 | 68% | 0% | 85% | 382 KB | 7 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 2,821 | 10,920 | 10.8 | 55% | 0% | 96% | 721 KB | 10 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E E C | 2,753 | 8,210 | 0.0 | 42% | 6% | 72% | 288 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E E F | 2,702 | 111,838 | 0.0 | 63% | 17% | – | 8,190 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 2,620 | 13,228 | 30.1 | 19% | 18% | 87% | 986 KB | 114 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F A | 2,599 | 35,227 | 59.4 | 80% | 0% | 94% | 241 KB | 124 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 2,586 | 2,636 | 17.5 | 31% | 0% | 100% | 160 KB | 2 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E E B | 2,542 | 4,307 | 13.9 | 46% | 34% | 95% | 338 KB | 170 (+2) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 2,515 | 3,718 | 18.7 | 10% | 0% | 73% | 169 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 2,493 | 3,072 | 12.5 | 6% | 0% | 96% | 42 KB | 2 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,429 | 13,103 | 12.8 | 19% | 16% | 100% | 1,076 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,391 | 19,301 | 43.8 | 46% | 20% | – | 440 KB | 1 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,373 | 14,331 | 14.7 | 36% | 0% | 95% | 383 KB | 2 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 2,369 | 5,201 | 0.0 | 23% | 22% | 0% | 305 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 2,363 | 5,558 | 0.0 | 74% | 0% | 42% | 267 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E E A | 2,304 | 3,117 | 13.2 | 79% | 12% | 100% | 260 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 2,288 | 2,703 | 8.0 | 33% | 12% | 95% | 355 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 2,282 | 5,160 | 16.1 | 62% | 0% | 100% | 190 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,265 | 9,651 | 0.0 | 10% | 0% | 97% | 534 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E E C | 2,167 | 21,456 | 6.6 | 56% | 12% | 95% | 697 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F B | 2,147 | 7,855 | 24.5 | 19% | 0% | 82% | 326 KB | 160 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 2,145 | 5,718 | 0.0 | 62% | 0% | 96% | 224 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,136 | 9,032 | 0.0 | 26% | 3% | 0% | 1,230 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 2,125 | 13,466 | 17.5 | 48% | 0% | 99% | 399 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 2,123 | 7,609 | 21.9 | 22% | 0% | 89% | 608 KB | 1 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 2,115 | 10,022 | 20.1 | 40% | 24% | 76% | 1,648 KB | 6 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F D | 2,062 | 9,167 | 15.0 | 33% | 3% | 37% | 7,014 KB | 20 (+1) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,054 | 3,881 | 7.1 | 84% | 0% | 100% | 132 KB | 242 (+1) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 2,045 | 3,444 | 18.4 | 24% | 0% | 99% | 504 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 1,960 | 6,143 | 8.7 | 21% | 0% | 72% | 297 KB | 340 (+1) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,958 | 6,168 | 19.6 | 11% | 19% | 99% | 286 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,951 | 10,826 | 3.6 | 13% | 0% | 100% | 1,146 KB | 5 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,933 | 4,183 | 12.6 | 19% | 33% | 73% | 271 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 1,923 | 3,738 | 15.5 | 60% | 0% | 99% | 165 KB | 1 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 1,871 | 6,221 | 1.3 | 24% | 21% | 76% | 66 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 1,868 | 4,525 | 37.8 | 0% | 0% | 86% | 67 KB | 63 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,849 | 3,179 | 12.2 | 49% | 9% | 100% | 4,314 KB | 28 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,830 | 4,147 | 71.1 | 15% | 26% | 97% | 560 KB | 2 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | E F B | 1,821 | 4,671 | 7.5 | 44% | 0% | 87% | 27 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 1,819 | 6,345 | 28.8 | 55% | 0% | 95% | 49 KB | 23,825 (+5) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,790 | 3,707 | 27.7 | 63% | 0% | 100% | 158 KB | 6 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 1,775 | 9,281 | 23.8 | 49% | 11% | 98% | 42 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E F B | 1,765 | 4,257 | 30.4 | 65% | 0% | 98% | 1,060 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 1,755 | 4,518 | 11.8 | 26% | 0% | 96% | 663 KB | 2 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 1,651 | 13,308 | 20.4 | 41% | 44% | 84% | 540 KB | 10 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 1,599 | 2,285 | 32.2 | 15% | 0% | 97% | 270 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,541 | 3,737 | 13.9 | 26% | 0% | 99% | 61 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,422 | 2,185 | 21.9 | 41% | 0% | 87% | 998 KB | 2 (+1) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 1,412 | 1,268 | 15.4 | 42% | 0% | 99% | 456 KB | 12 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | E F C | 1,366 | 7,239 | 23.3 | 39% | 0% | 100% | 25 KB | 18 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,346 | 3,453 | 22.2 | 33% | 29% | 97% | 101 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 1,318 | 3,339 | 13.5 | 44% | 0% | 99% | 127 KB | 23 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F B | 1,307 | 5,599 | 25.4 | 50% | 0% | 100% | 126 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,252 | 2,095 | 57.1 | 32% | 0% | 97% | 695 KB | 14 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 1,246 | 3,664 | 22.4 | 23% | 0% | 98% | 1,116 KB | 1 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 1,237 | 6,342 | 20.2 | 49% | 0% | 98% | 93 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 1,140 | 2,815 | 38.2 | 33% | 0% | 99% | 211 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 1,136 | 6,262 | 23.1 | 15% | 13% | 94% | 160 KB | 11 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,123 | 3,860 | 0.0 | 59% | 21% | – | 883 KB | 2 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,078 | 1,179 | 30.1 | 35% | 0% | 100% | 403 KB | 2 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 980 | 52,486 | 23.3 | 17% | 0% | 88% | 1,414 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F A | 935 | 12,512 | 50.9 | 22% | 0% | 96% | 169 KB | 2 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 915 | 1,429 | 9.8 | 0% | 0% | – | 631 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 903 | 3,721 | 28.5 | 15% | 9% | 100% | 553 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 860 | 1,038,353 | 38.1 | 60% | 0% | 82% | 416 KB | 9 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 839 | 1,703 | 5.9 | 0% | 0% | 96% | 807 KB | 2 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F D C | 782 | 5,834 | 0.0 | 68% | 79% | 100% | 1,478 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 776 | 24,271 | 0.0 | 31% | 0% | 94% | 554 KB | 29 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 730 | 10,247 | 8.7 | 11% | 0% | 98% | 45 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 728 | 1,806 | 11.1 | 27% | 16% | 68% | 635 KB | 4 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 716 | 2,516 | 5.2 | 10% | 0% | 90% | 3,845 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | F F B | 691 | 1,441 | 30.8 | 39% | 0% | 94% | 107 KB | 4 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 607 | 3,344 | 14.7 | 45% | 0% | 94% | 5,248 KB | 40,568 (+36) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 567 | 1,179 | 0.0 | 59% | 13% | 0% | 665 KB | 3 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F D D | 487 | 1,693 | 0.0 | 61% | 23% | 0% | 342 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F E C | 440 | 1,281 | 14.2 | 49% | 0% | 98% | 445 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 427 | 7,308 | 18.0 | 62% | 0% | 99% | 632 KB | 11 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 370 | 3,609 | 0.1 | 46% | 0% | 82% | 152 KB | 104 (+74) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F B | 330 | 3,818 | 5.4 | 33% | 0% | 86% | 262 KB | 1,250 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 311 | 1,076 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | F F B | 278 | 3,747 | 19.7 | 71% | 0% | 96% | 518 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 270 | 8,072 | 12.9 | 49% | 0% | 61% | 6,579 KB | 8 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 243 | 1,173 | 6.6 | 0% | 0% | 99% | 571 KB | 1 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 240 | 1,616 | 3.8 | 9% | 0% | 13% | 115 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | F F A | 231 | 4,875 | 24.4 | 13% | 0% | 99% | 380 KB | 49 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 225 | 2,308 | 21.9 | 7% | 0% | 96% | 122 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 214 | 13,019 | 13.8 | 36% | 0% | 100% | 617 KB | 1 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 178 | 477 | 0.0 | 0% | 0% | 99% | 444 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 164 | 12,975 | 20.5 | 65% | 0% | 97% | 383 KB | 1,605 (+3) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | F F C | 142 | 7,357 | 24.3 | 0% | 0% | 53% | 4,722 KB | 105 (+2) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 117 | 992,817 | 5.0 | 2% | 0% | 85% | 23 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 106 | 229 | 1.8 | 0% | 0% | 88% | 151 KB | 347 (+2) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 92 | 2,039 | 7.1 | 0% | 0% | 99% | 100 KB | 4 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 77 | 5,521 | 12.9 | 48% | 0% | 96% | 99 KB | 1 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 62 | 1,136 | 10.0 | 22% | 0% | 100% | 71 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 50 | 119 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 45 | 2,795 | 9.5 | 34% | 0% | 0% | 285 KB | 25 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 35 | 154 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 32 | 3,924 | 14.4 | 44% | 0% | 96% | 66 KB | 3 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 4 | 71 | 6.4 | 0% | 0% | – | 56 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 4 | 658 | 4.8 | 0% | 0% | 96% | 163 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 3 | 42,264 | 5.0 | 0% | 0% | 97% | 149 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 3 | 2,571 | 3.4 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 2,704 | 57.3 | 0% | 0% | 96% | 136 KB | 1 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F F B | 0 | 2,891 | 54.4 | 0% | 0% | 100% | 3,196 KB | 30 (+10) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 0 | 41.9 | 0% | 0% | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F F B | – | – | 38.5 | 30% | 27% | 88% | 2,258 KB | 1,483 (+3) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 491 | 26.2 | 0% | 0% | 98% | 240 KB | 10 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | 0 | 2,099 | 24.8 | 0% | 0% | 99% | 884 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 23.5 | 10% | 0% | 100% | 342 KB | 4 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 20.1 | 44% | 32% | 100% | 1,016 KB | 4 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | 0 | 1,507 | 19.7 | 0% | 0% | 100% | 41 KB | 3 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 19.5 | – | – | 98% | 363 KB | 1 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,610 | 18.0 | 27% | 0% | 84% | 1,170 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F F B | – | – | 16.5 | 71% | 0% | 86% | 86 KB | 6 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 875 | 16.0 | 0% | 0% | 77% | 332 KB | 1 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 11 | 15.8 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 71 | 14.1 | 0% | 0% | 98% | 88 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | – | – | 13.7 | – | – | 96% | 32 KB | 1 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 0 | 13.6 | 26% | 4% | 94% | 484 KB | 3 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 2,810 | 12.6 | 40% | 0% | 96% | 53 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 91 | 12.6 | 0% | 0% | 83% | 15 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 12.4 | – | – | 97% | 94 KB | 17 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 77 | 12.2 | 0% | 0% | 95% | 8,119 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 12.1 | – | – | 93% | 576 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | F F A | 0 | 7,361 | 12.0 | 61% | 0% | 95% | 236 KB | 5 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 12.0 | – | – | 98% | 231 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F E D | – | – | 11.3 | 50% | 5% | 0% | 206 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 10.8 | – | – | 98% | 43 KB | 1 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | 0 | 0 | 10.6 | – | – | 99% | 80 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | – | – | 10.5 | – | – | 88% | 700 KB | 4 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 639 | 9.9 | 0% | 0% | 94% | 41 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 534 | 9.2 | 0% | 0% | 97% | 57 KB | 1 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 2,140 | 8.3 | 0% | 0% | – | 100 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 1,020 | 8.2 | 0% | 0% | 88% | 489 KB | 57 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 0 | 1,399 | 7.5 | 0% | 0% | – | 415 KB | 0 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 0 | 589 | 7.3 | 15% | 0% | 80% | 83 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 0 | 2,954 | 6.9 | 27% | 0% | 98% | 363 KB | 1 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 371 | 6.8 | 0% | 0% | 100% | 153 KB | 2 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 0 | 3,196 | 6.6 | 0% | 0% | 89% | 682 KB | 6 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 6.4 | – | – | 96% | 122 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | 0 | 0 | 5.9 | – | – | – | 311 KB | 4 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | – | – | 5.8 | – | – | 80% | 552 KB | 2 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 594 | 5.8 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 13 | 4.9 | 0% | 0% | 75% | 161 KB | 2 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 4.5 | – | – | 98% | 723 KB | 6 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 82,767 | 4.4 | 41% | 0% | 91% | 163 KB | 14 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 2,175 | 4.3 | 10% | 0% | 97% | 43 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 4.3 | – | – | – | 115 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 4.3 | – | – | 90% | 195 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 4.2 | – | – | 99% | 298 KB | 5 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F B D | – | – | 4.1 | 86% | 96% | 0% | 2,040 KB | 462 (+1) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 982 | 3.1 | 0% | 0% | 82% | 1,423 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 0 | 2.9 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 20,019 | 2.7 | 0% | 0% | 98% | 579 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 2.6 | – | – | 98% | 42 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 2.2 | – | – | 98% | 149 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 2.2 | 0% | 0% | 99% | 73 KB | 4 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 0 | 1,124 | 1.5 | 80% | 0% | 11% | 52 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | F F C | 0 | 4,169 | 1.5 | 37% | 0% | 69% | 5,602 KB | 1 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 176 | 0.9 | 0% | 0% | 20% | 154 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 0 | 520 | 0.9 | 44% | 0% | – | 53 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.6 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.5 | – | – | 69% | 290 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | 0 | 485 | 0.4 | 0% | 0% | 0% | 518 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 66% | 0% | 89% | 842 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.2 | 81% | 0% | 96% | 34,213 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 0 | 0.1 | 0% | 0% | 16% | 904 KB | 1,313 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D B | – | – | 0.1 | 62% | 32% | 76% | 87 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 0 | 281 | 0.0 | 0% | 0% | 100% | 478 KB | 6 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,371 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 239 | 0.0 | 0% | 0% | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 0 | 183 | 0.0 | 0% | 0% | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 99 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 198 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | 0 | 3,652 | 0.0 | 27% | 0% | 30% | 308 KB | 554 (+67) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+1) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 36,865 | 0.0 | 0% | 0% | – | 110 KB | 0 (+0) |
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
