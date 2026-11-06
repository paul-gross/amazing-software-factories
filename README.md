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
_361 repos, last measured 2026-11-06. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A F A | 85,158 | 76,130 | 53.6 | 38% | 15% | 87% | 410 KB | 86 (+1) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | A C C | 50,791 | 72,904 | 0.1 | 77% | 56% | 50% | 2,688 KB | 3 (+1) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 46,312 | 189,458 | 170 | 18% | 4% | 89% | 2,294 KB | 5 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A D B | 43,818 | 98,870 | 63.8 | 64% | 22% | 95% | 597 KB | 1 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 43,453 | 48,729 | 60.3 | 50% | 56% | 99% | 3,391 KB | 2,098 (+2) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 42,291 | 218,124 | 121 | 40% | 6% | 53% | 309 KB | 4 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A F A | 41,700 | 62,935 | 61.8 | 76% | 0% | 95% | 241 KB | 127 (+1) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A E A | 41,433 | 55,262 | 156 | 42% | 44% | 100% | 212 KB | 19 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B D A | 39,032 | 49,969 | 47.4 | 66% | 22% | 100% | 303 KB | 3 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B C B | 38,932 | 44,546 | 69.1 | 78% | 39% | 75% | 1,069 KB | 1 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B C B | 38,797 | 213,182 | 1.2 | 84% | 4% | 92% | 3,340 KB | 7 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B D B | 37,798 | 51,471 | 96.7 | 64% | 27% | 91% | 4,783 KB | 80 (-1) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B D D | 36,436 | 69,224 | 0.0 | 64% | 36% | – | 453 KB | 2 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B C B | 34,860 | 47,858 | 52.0 | 74% | 56% | 76% | 332 KB | 0 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 29,599 | 37,784 | 29.0 | 15% | 57% | 100% | 1,655 KB | 96 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,589 | 27,867 | 22.9 | 77% | 44% | 92% | 830 KB | 6 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 27,184 | 38,098 | 37.8 | 75% | 23% | 98% | 809 KB | 4 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | B E B | 26,519 | 21,842 | 27.6 | 75% | 5% | 97% | 187 KB | 0 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 25,140 | 28,663 | 28.2 | 71% | 51% | 90% | 363 KB | 11 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B C B | 24,841 | 40,504 | 0.0 | 75% | 62% | 81% | 221 KB | 118 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B D B | 23,475 | 241,563 | 45.2 | 68% | 24% | 91% | 1,435 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B D D | 21,938 | 43,394 | 46.6 | 63% | 32% | 25% | 822 KB | 16 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 21,801 | 30,362 | 48.1 | 87% | 36% | 87% | 856 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 18,758 | 34,602 | 32.4 | 47% | 0% | 100% | 455 KB | 9 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C C C | 18,732 | 126,089 | 29.9 | 74% | 16% | 62% | 259 KB | 1 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 16,214 | 62,596 | 9.1 | 23% | 7% | 96% | 544 KB | 19 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C D C | 15,889 | 22,769 | 25.1 | 65% | 54% | 100% | 187 KB | 34 (+1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | C E C | 15,743 | 69,507 | 18.0 | 46% | 9% | 68% | 318 KB | 1 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C F B | 15,532 | 25,744 | 18.9 | 45% | 1% | 86% | 781 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F C | 15,106 | 21,897 | 98.4 | 39% | 22% | 76% | 376 KB | 74 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C F D | 14,776 | 34,491 | 0.0 | 24% | 8% | 42% | 5,368 KB | 446 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 14,753 | 150,849 | 0.0 | 68% | 43% | 50% | 561 KB | 1 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C C D | 14,681 | 50,287 | 0.0 | 72% | 40% | – | 1,007 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,566 | 49,857 | 7.4 | 21% | 24% | 90% | 466 KB | 140 (+1) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 14,473 | 35,031 | 34.3 | 89% | 36% | 93% | 200 KB | 6 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C F D | 14,416 | 22,323 | 14.9 | 42% | 0% | 27% | 144 KB | 14 (-1) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B D | 14,105 | 20,692 | 0.0 | 89% | 48% | 20% | 359 KB | 0 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 13,958 | 23,382 | 3.1 | 42% | 25% | 99% | 2,284 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 13,849 | 87,367 | 26.9 | 44% | 43% | 99% | 496 KB | 21 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C B A | 13,463 | 20,745 | 54.6 | 89% | 31% | 100% | 468 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C D C | 13,367 | 24,864 | 89.3 | 62% | 49% | 100% | 4,357 KB | 15 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | C F B | 13,341 | 20,257 | 20.1 | 46% | 17% | 80% | 126 KB | 5 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 13,274 | 26,194 | 41.5 | 6% | 45% | 99% | 225 KB | 7 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F B | 12,885 | 16,000 | 0.0 | 31% | 38% | 74% | 322 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | C F B | 12,814 | 38,850 | 16.5 | 2% | 3% | 84% | 2,627 KB | 42 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C E B | 12,369 | 20,939 | 16.8 | 78% | 39% | 84% | 141 KB | 4 (-1) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 12,229 | 18,001 | 28.5 | 68% | 10% | 98% | 599 KB | 22 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 12,177 | 25,697 | 0.0 | 82% | 40% | – | 1,118 KB | 2 (-1) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C E D | 11,934 | 56,293 | 0.0 | 46% | 4% | 32% | 158 KB | 117 (+1) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | C E C | 11,930 | 152,047 | 103 | 68% | 23% | 90% | 378 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | C F D | 11,634 | 15,633 | 56.6 | 25% | 5% | 93% | 20,146 KB | 1 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C D B | 11,624 | 15,238 | 16.3 | 61% | 22% | 96% | 446 KB | 12 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 11,483 | 21,740 | 17.8 | 22% | 13% | 90% | 8,727 KB | 135 (+2) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 11,315 | 17,260 | 26.7 | 67% | 38% | 100% | 1,763 KB | 3 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 11,265 | 18,972 | 65.0 | 46% | 12% | 84% | 275 KB | 6,555 (+3) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 11,169 | 20,852 | 54.2 | 29% | 9% | 100% | 154 KB | 2 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 10,762 | 15,496 | 21.1 | 29% | 22% | 100% | 737 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C E D | 10,669 | 15,387 | 10.9 | 52% | 35% | 12% | 224 KB | 9 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 10,453 | 18,969 | 0.0 | 72% | 43% | 30% | 1,561 KB | 36 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | C D B | 10,240 | 30,982 | 13.2 | 63% | 38% | 77% | 30 KB | 0 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 9,940 | 12,672 | 0.0 | 17% | 0% | 0% | 601 KB | 1 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | D B B | 9,737 | 55,714 | 29.8 | 82% | 23% | 100% | 1,140 KB | 36 (+1) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | D F B | 9,703 | 21,578 | 22.8 | 18% | 0% | 72% | 312 KB | 1 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D F B | 9,632 | 10,014 | 23.4 | 57% | 0% | 99% | 1,150 KB | 8 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D E B | 9,568 | 17,197 | 168 | 68% | 2% | 100% | 2,407 KB | 0 (-1) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D E B | 9,548 | 10,562 | 46.0 | 45% | 40% | 84% | 335 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | D C C | 9,521 | 12,243 | 14.9 | 88% | 18% | 76% | 527 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 9,519 | 12,203 | 14.1 | 77% | 29% | 98% | 165 KB | 0 (-1) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | D F B | 9,322 | 19,240 | 25.7 | 20% | 18% | 100% | 597 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 9,064 | 13,340 | 13.6 | 36% | 14% | – | 95 KB | 2 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D E B | 9,045 | 18,833 | 30.7 | 57% | 24% | 78% | 102 KB | 232 (-1) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F E | 8,905 | 33,195 | 34.9 | 11% | 0% | 20% | 3,975 KB | 1 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D E B | 8,750 | 19,235 | 15.8 | 48% | 35% | 99% | 258 KB | 4 (-9) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 8,654 | 25,978 | 56.7 | 67% | 0% | – | 440 KB | 3 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | D D A | 8,434 | 29,557 | 88.8 | 70% | 27% | 100% | 62 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D E B | 8,299 | 14,140 | 35.5 | 57% | 61% | 91% | 216 KB | 9 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | D F D | 8,210 | 92,517 | 0.0 | 72% | 0% | 0% | 3,286 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D F A | 8,167 | 9,559 | 39.0 | 66% | 5% | 97% | 131 KB | 1 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D C B | 8,166 | 11,495 | 13.6 | 75% | 22% | 87% | 1,230 KB | 13 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D F B | 7,591 | 8,098 | 32.6 | 58% | 0% | 99% | 1,060 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | D F D | 7,282 | 12,140 | 0.0 | 37% | 0% | – | 388 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 7,240 | 28,764 | 24.0 | 29% | 10% | 97% | 634 KB | 46 (+10) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 7,135 | 12,374 | 7.3 | 16% | 41% | 93% | 362 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D F B | 7,113 | 8,204 | 11.9 | 36% | 0% | 100% | 95 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | D F C | 6,990 | 427,080 | 44.4 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D F B | 6,935 | 16,630 | 0.0 | 51% | 2% | 96% | 590 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | D F D | 6,924 | 38,297 | 0.1 | 25% | 0% | 89% | 1,468 KB | 1,119 (+1) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D F D | 6,854 | 10,320 | 14.6 | 14% | 41% | – | 614 KB | 2 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | D E B | 6,797 | 10,373 | 6.6 | 65% | 32% | 100% | 211 KB | 7 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 6,775 | 11,476 | 0.1 | 13% | 0% | 84% | 153 KB | 72 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D E C | 6,410 | 9,434 | 5.7 | 54% | 35% | 86% | 4,013 KB | 554 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D E B | 6,409 | 32,588 | 17.9 | 65% | 0% | 100% | 257 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | D F C | 6,266 | 25,585 | 27.6 | 33% | 9% | 99% | 321 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | D D C | 6,252 | 14,694 | 34.8 | 65% | 47% | 97% | 676 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | D F D | 6,096 | 8,500 | 1.2 | 34% | 7% | 0% | 452 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 5,995 | 7,282 | 15.6 | 13% | 32% | 98% | 544 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D E B | 5,950 | 12,401 | 0.0 | 68% | 15% | 93% | 373 KB | 3 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D F B | 5,904 | 20,888 | 13.9 | 26% | 0% | 100% | 617 KB | 1 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 5,895 | 6,568 | 34.4 | 80% | 29% | 98% | 797 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D E B | 5,867 | 9,845 | 53.1 | 58% | 0% | 98% | 970 KB | 2 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D E F | 5,833 | 204,246 | 0.0 | 59% | 13% | – | 8,190 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 5,739 | 11,393 | 19.9 | 20% | 0% | 98% | 223 KB | 5 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 5,586 | 10,908 | 48.4 | 7% | 21% | 100% | 605 KB | 0 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D E D | 5,370 | 8,445 | 46.8 | 78% | 13% | – | 225 KB | 3 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | D F B | 5,272 | 23,369 | 58.5 | 23% | 0% | 99% | 3,196 KB | 33 (+2) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D B B | 5,260 | 7,764 | 16.0 | 82% | 19% | 93% | 395 KB | 2 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D C B | 5,226 | 25,600 | 32.1 | 74% | 44% | 75% | 1,395 KB | 70,736 (+28) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D D B | 5,121 | 6,402 | 15.2 | 64% | 46% | 99% | 592 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F B | 4,993 | 9,218 | 26.4 | 18% | 5% | 97% | 628 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,823 | 17,980 | 24.2 | 38% | 9% | 98% | 911 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E E A | 4,767 | 23,988 | 0.0 | 45% | 0% | 98% | 254 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 4,759 | 8,890 | 11.4 | 51% | 0% | 72% | 6,579 KB | 8 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E D B | 4,679 | 16,770 | 28.4 | 68% | 0% | 81% | 59 KB | 1 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 4,509 | 12,930 | 0.1 | 40% | 0% | 100% | 472 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 4,449 | 7,347 | 1.3 | 11% | 19% | 76% | 66 KB | 1 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E F B | 4,353 | 7,560 | 11.5 | 57% | 23% | 97% | 107 KB | 1 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 4,323 | 7,035 | 45.4 | 42% | 36% | 100% | 590 KB | 5 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 4,323 | 6,632 | 21.3 | 14% | 12% | 93% | 160 KB | 12 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 4,209 | 4,929 | 13.4 | 59% | 0% | 97% | 42 KB | 2 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E F B | 4,069 | 5,956 | 36.6 | 56% | 13% | 100% | 2,287 KB | 5 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,059 | 6,513 | 35.4 | 49% | 3% | 99% | 99 KB | 3 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 4,050 | 6,293 | 6.9 | 12% | 0% | 88% | 739 KB | 0 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | E C A | 4,030 | 142,976 | 52.4 | 71% | 21% | 100% | 158 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,980 | 6,372 | 16.4 | 3% | 35% | 98% | 386 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,840 | 5,280 | 0.1 | 35% | 14% | 86% | 1,040 KB | 2 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 3,796 | 9,109 | 17.4 | 60% | 22% | 99% | 201 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F A | 3,686 | 14,809 | 46.8 | 40% | 0% | 92% | 169 KB | 2 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 3,481 | 8,373 | 19.6 | 14% | 0% | 100% | 541 KB | 88 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 3,388 | 7,177 | 16.2 | 44% | 0% | 90% | 458 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 3,380 | 29,317 | 12.6 | 49% | 26% | 95% | 356 KB | 25 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 3,374 | 5,812 | 0.9 | 51% | 30% | 0% | 237 KB | 0 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F B | 3,359 | 49,263 | 27.1 | 8% | 0% | 75% | 188 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E C B | 3,357 | 5,085 | 32.5 | 71% | 4% | 99% | 354 KB | 2 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 3,302 | 4,692 | 65.5 | 17% | 15% | 97% | 561 KB | 2 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,264 | 3,469 | 14.5 | 24% | 0% | 96% | 146 KB | 1 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E E E | 3,228 | 11,198 | 23.0 | 46% | 39% | 76% | 1,648 KB | 6 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,226 | 4,667 | 13.8 | 8% | 6% | 73% | 131 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 3,207 | 4,079 | 13.7 | 64% | 17% | 97% | 260 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E E B | 3,188 | 4,180 | 13.7 | 57% | 28% | 95% | 339 KB | 171 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 3,113 | 33,313 | 0.0 | 42% | 0% | – | 203 KB | 28 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 3,059 | 7,202 | 6.1 | 70% | 31% | 99% | 548 KB | 12 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 2,956 | 4,688 | 25.6 | 47% | 22% | 100% | 310 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E E B | 2,903 | 5,737 | 41.0 | 47% | 30% | 100% | 1,390 KB | 8 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 2,896 | 17,294 | 25.7 | 9% | 47% | 98% | 363 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E C B | 2,890 | 10,071 | 32.1 | 76% | 62% | 100% | 32 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 2,882 | 6,541 | 26.2 | 22% | 0% | 94% | 49 KB | 23,841 (+10) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F B | 2,835 | 10,614 | 16.0 | 78% | 0% | 85% | 382 KB | 9 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 2,821 | 10,507 | 9.9 | 60% | 0% | 94% | 721 KB | 9 (-1) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 2,742 | 7,518 | 0.0 | 16% | 7% | 90% | 674 KB | 2 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E F C | 2,640 | 3,961 | 33.7 | 38% | 16% | 96% | 512 KB | 0 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 2,609 | 4,548 | 0.0 | 3% | 12% | 73% | 288 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F B | 2,608 | 4,668 | 34.9 | 0% | 0% | 82% | 67 KB | 63 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 2,553 | 12,114 | 28.2 | 16% | 0% | 91% | 987 KB | 115 (+1) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 2,486 | 12,341 | 13.1 | 43% | 0% | 95% | 150 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 2,470 | 3,257 | 19.6 | 32% | 0% | 99% | 93 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 2,369 | 34,199 | 0.0 | 23% | 4% | 0% | 303 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 2,363 | 6,158 | 0.0 | 52% | 0% | 42% | 267 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,344 | 12,600 | 12.4 | 32% | 18% | 100% | 1,080 KB | 0 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F C | 2,320 | 7,674 | 10.5 | 11% | 0% | 65% | 105 KB | 3 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 2,288 | 3,003 | 8.3 | 39% | 10% | 95% | 350 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 2,167 | 5,759 | 25.0 | 25% | 40% | 98% | 393 KB | 17 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 2,135 | 8,194 | 0.0 | 7% | 0% | 93% | 948 KB | 48 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 2,111 | 6,425 | 16.7 | 20% | 0% | 99% | 399 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,100 | 8,823 | 0.0 | 50% | 0% | 97% | 543 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 2,039 | 15,953 | 14.5 | 26% | 0% | 78% | 294 KB | 2 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 1,997 | 7,073 | 0.0 | 4% | 4% | 0% | 1,259 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 1,989 | 26,243 | 72.5 | 18% | 0% | 97% | 614 KB | 2 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 1,985 | 5,148 | 20.8 | 31% | 0% | 89% | 608 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,958 | 7,837 | 19.5 | 27% | 23% | 100% | 289 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 1,957 | 9,934 | 43.4 | 64% | 30% | – | 440 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F B | 1,799 | 6,843 | 24.4 | 9% | 0% | 75% | 326 KB | 160 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,790 | 3,097 | 24.5 | 44% | 0% | 99% | 163 KB | 6 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 1,754 | 5,243 | 23.2 | 54% | 20% | 100% | 42 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E D C | 1,656 | 13,234 | 6.4 | 64% | 14% | 95% | 697 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,622 | 3,511 | 22.2 | 32% | 28% | 97% | 104 KB | 1 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 1,622 | 5,080 | 0.1 | 36% | 0% | 39% | 376 KB | 1 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 1,596 | 38,893 | 40.5 | 26% | 0% | 98% | 212 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 1,567 | 12,799 | 20.5 | 55% | 48% | 84% | 540 KB | 10 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 1,532 | 3,049 | 10.0 | 18% | 0% | 97% | 663 KB | 2 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,472 | 1,869 | 4.7 | 0% | 0% | 100% | 166 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | E F C | 1,366 | 1,932 | 21.8 | 0% | 0% | 100% | 25 KB | 18 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,351 | 3,666 | 16.3 | 44% | 42% | – | 57 KB | 3 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,328 | 2,432 | 10.0 | 52% | 0% | 100% | 4,314 KB | 30 (+2) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F B | 1,307 | 6,064 | 24.1 | 40% | 0% | 100% | 126 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,296 | 4,360 | 17.6 | 62% | 0% | 100% | 518 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 1,262 | 2,714 | 16.4 | 41% | 0% | 100% | 165 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F B | 1,235 | 10,998 | 27.1 | 44% | 0% | 99% | 167 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 1,220 | 6,835 | 8.1 | 0% | 0% | 72% | 299 KB | 341 (+1) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,163 | 2,253 | 52.3 | 33% | 39% | 95% | 704 KB | 13 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 1,159 | 2,103 | 13.6 | 72% | 0% | 94% | 381 KB | 2 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,123 | 8,390 | 0.0 | 80% | 23% | – | 931 KB | 1 (-1) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E F B | 1,094 | 6,401 | 12.0 | 44% | 0% | 98% | 54 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | E F A | 1,015 | 2,037 | 22.1 | 41% | 0% | 99% | 96 KB | 0 (-1) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 998 | 1,055 | 14.3 | 37% | 0% | 100% | 456 KB | 13 (+1) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | F F A | 964 | 39,078 | 25.5 | 8% | 0% | 98% | 380 KB | 49 (-1) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 913 | 2,385 | 21.6 | 50% | 0% | 97% | 1,116 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F C | 871 | 3,339 | 11.9 | 22% | 0% | 63% | 274 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 871 | 5,286 | 0.0 | 27% | 0% | 33% | 402 KB | 462 (-2) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | F F C | 863 | 2,173 | 17.9 | 57% | 0% | 86% | 998 KB | 2 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F B C | 782 | 4,165 | 0.0 | 83% | 83% | 99% | 1,920 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 776 | 24,049 | 0.0 | 34% | 0% | 85% | 554 KB | 29 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 739 | 56,206 | 21.9 | 36% | 0% | 88% | 1,414 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 716 | 1,954 | 4.9 | 0% | 16% | 90% | 3,845 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | F F B | 691 | 1,937 | 27.3 | 39% | 0% | 93% | 107 KB | 4 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 609 | 1,728 | 5.6 | 7% | 0% | 99% | 843 KB | 2 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 576 | 1,876 | 10.6 | 28% | 0% | 99% | 127 KB | 23 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 567 | 660 | 0.0 | 60% | 30% | 0% | 670 KB | 3 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 556 | 10,196 | 14.8 | 36% | 0% | 94% | 5,248 KB | 40,646 (+33) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 548 | 2,675 | 7.9 | 53% | 0% | 100% | 132 KB | 243 (+1) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 530 | 3,960 | 36.5 | 15% | 0% | 96% | 249 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 525 | 1,676 | 30.6 | 10% | 0% | 96% | 270 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 512 | 2,642 | 26.0 | 0% | 0% | 99% | 553 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F E D | 465 | 1,459 | 0.0 | 62% | 0% | 0% | 342 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F C E | 442 | 8,983 | 18.6 | 84% | 20% | 99% | 632 KB | 11 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F E C | 418 | 939 | 13.5 | 72% | 0% | 98% | 446 KB | 0 (-1) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 401 | 1,555 | 13.6 | 26% | 0% | 99% | 61 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | F F C | 352 | 636 | 23.0 | 0% | 0% | 55% | 4,722 KB | 110 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 312 | 998,652 | 4.7 | 2% | 0% | 85% | 23 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 311 | 935 | 0.0 | 0% | 0% | – | 202 KB | 5 (+1) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 243 | 2,628 | 7.0 | 45% | 0% | 99% | 571 KB | 1 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 213 | 2,540 | 6.6 | 0% | 0% | 99% | 100 KB | 4 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 178 | 234 | 0.0 | 0% | 0% | 99% | 444 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F B | 108 | 9,313 | 3.7 | 35% | 0% | 100% | 1,149 KB | 5 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 100 | 2,404 | 6.6 | 10% | 0% | 96% | 363 KB | 1 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 2,706 | 14.9 | 37% | 0% | 35% | 7,014 KB | 20 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 70 | 3,184 | 9.5 | 35% | 0% | 0% | 285 KB | 25 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 54 | 329 | 9.3 | 0% | 54% | 64% | 635 KB | 4 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 50 | 115 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 24 | 142 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 19 | 798 | 21.1 | 0% | 0% | 95% | 122 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 13 | 2,721 | 7.6 | 50% | 0% | 78% | 27 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 9 | 591 | 13.3 | 42% | 0% | 96% | 66 KB | 3 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 7 | 35,518 | 4.8 | 0% | 0% | 75% | 149 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 4 | 125 | 3.5 | 0% | 0% | – | 56 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 2 | 6,030 | 12.8 | 26% | 0% | 0% | 346 KB | 1 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 346 | 53.1 | 0% | 0% | 96% | 136 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F C B | – | – | 50.4 | 78% | 50% | 90% | 775 KB | 11 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 0 | 41.9 | – | – | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 35.9 | 44% | 27% | 79% | 2,264 KB | 1,494 (+4) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 450,618 | 32.1 | 46% | 0% | 79% | 416 KB | 9 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | 0 | 530 | 26.3 | 37% | 0% | 100% | 403 KB | 2 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 805 | 25.6 | 0% | 0% | 100% | 240 KB | 10 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 2,757 | 22.8 | 32% | 0% | 97% | 383 KB | 1,610 (+4) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | 0 | 0 | 22.7 | – | – | 99% | 884 KB | 5 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 22.3 | 39% | 26% | 100% | 1,032 KB | 4 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 19.4 | 0% | 0% | 98% | 342 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 783 | 18.0 | 0% | 0% | 99% | 504 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | 0 | 46 | 17.9 | 0% | 0% | 100% | 41 KB | 2 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 0 | 20,586 | 17.4 | 53% | 0% | 99% | 353 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 309 | 16.2 | 0% | 0% | 76% | 335 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,499 | 16.2 | 0% | 0% | 86% | 1,170 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 11 | 16.2 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F F B | – | – | 15.8 | 55% | 0% | 89% | 86 KB | 6 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 561 | 15.6 | 0% | 0% | 100% | 519 KB | 2 (-1) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 0 | 1,123 | 15.1 | 52% | 0% | 100% | 160 KB | 2 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 15.1 | – | – | 98% | 363 KB | 0 (-1) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | – | – | 13.7 | – | – | 96% | 32 KB | 1 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 190 | 13.7 | 0% | 0% | 83% | 15 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 4,981 | 12.2 | 16% | 0% | 96% | 99 KB | 1 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 0 | 12.1 | 0% | 0% | 95% | 8,119 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 11.5 | 46% | 0% | 0% | 206 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 10.8 | – | – | 93% | 576 KB | 1 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 10.6 | – | – | 99% | 80 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 0 | 1,246 | 10.3 | 27% | 0% | 100% | 79 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 684 | 9.9 | 0% | 0% | 97% | 45 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | F F A | 0 | 74 | 9.8 | 0% | 0% | 97% | 236 KB | 5 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 26 | 9.3 | 0% | 0% | 95% | 88 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 339 | 8.9 | 0% | 0% | 97% | 57 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 15,201 | 8.7 | 0% | 0% | 87% | 489 KB | 57 (-1) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 0 | 4,469 | 8.5 | 0% | 0% | 98% | 45 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | – | – | 8.4 | – | – | 88% | 700 KB | 4 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 1,059 | 8.3 | 0% | 0% | – | 100 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 7.9 | – | – | 97% | 94 KB | 16 (-1) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 7.7 | – | – | – | 311 KB | 4 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 822 | 7.5 | 0% | 0% | – | 678 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 0 | 243 | 7.4 | 0% | 0% | 80% | 83 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 0 | 4,842 | 7.2 | 0% | 0% | 89% | 682 KB | 6 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 0 | 1,125 | 7.1 | 0% | 0% | – | 415 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 335 | 6.8 | 0% | 0% | 100% | 156 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | – | – | 5.4 | – | – | 80% | 552 KB | 2 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 5.1 | – | – | 96% | 122 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 0 | 4.9 | – | – | 75% | 161 KB | 2 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F B | 0 | 2,020 | 4.8 | 0% | 0% | 86% | 262 KB | 1,252 (+2) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 4.4 | 0% | 0% | 90% | 163 KB | 14 (+1) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 1,182 | 4.3 | 19% | 0% | 97% | 43 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 4.3 | – | – | 90% | 195 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F C D | – | – | 3.5 | 76% | 87% | 0% | 2,040 KB | 460 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 1,324 | 3.4 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 3.2 | – | – | 98% | 723 KB | 5 (-1) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 563 | 3.2 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 3.2 | – | – | 98% | 231 KB | 0 (-1) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 3.1 | – | – | 99% | 298 KB | 5 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | – | – | 2.9 | – | – | 100% | 258 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 20,065 | 2.6 | 0% | 0% | 99% | 579 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 2.2 | – | – | – | 115 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 14 | 2.2 | 0% | 0% | 99% | 73 KB | 3 (-1) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 120 | 2.1 | 0% | 0% | 88% | 151 KB | 351 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 0 | 1,229 | 1.5 | 0% | 0% | 11% | 52 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | F F C | 0 | 451 | 1.4 | 0% | 0% | 76% | 5,602 KB | 1 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 1.2 | – | – | 98% | 42 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 0 | 0 | 0.9 | 0% | 0% | – | 53 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 242 | 0.7 | 0% | 0% | 20% | 154 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.5 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.5 | – | – | 69% | 290 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | 0 | 0 | 0.4 | – | – | 0% | 518 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 79% | 0% | 98% | 846 KB | 7 (+1) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,315 (+3) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 65% | 31% | 63% | 87 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F C | 0 | 2,627 | 0.0 | 21% | 0% | 93% | 134 KB | 0 (-6) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,371 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 1,535 | 0.0 | 42% | 0% | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 0 | 0 | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 0 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 3,583 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | 0 | 0 | 0.0 | 0% | 0% | 30% | 308 KB | 720 (+29) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.0 | 63% | 0% | 94% | 34,213 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 22,577 | 0.0 | 0% | 0% | – | 110 KB | 1 (+1) |
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
