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
_355 repos, last measured 2026-11-14. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (355)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 88,807 | 86,978 | 69.4 | 61% | 28% | 87% | 416 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A C B | 81,753 | 101,903 | 60.4 | 79% | 24% | 99% | 322 KB | 3 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A B C | 68,376 | 189,742 | 155 | 84% | 85% | 55% | 311 KB | 4 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A C D | 54,503 | 153,551 | 84.2 | 73% | 38% | 1% | 488 KB | 1 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A E C | 43,672 | 119,132 | 217 | 43% | 34% | 91% | 2,340 KB | 5 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | A B D | 40,918 | 54,285 | 0.1 | 84% | 62% | 0% | 3,565 KB | 3 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B C B | 32,414 | 43,406 | 0.1 | 74% | 37% | 88% | 3,842 KB | 7 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B F A | 27,591 | 39,315 | 61.6 | 4% | 4% | 90% | 413 KB | 87 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,086 | 37,607 | 23.8 | 73% | 64% | 100% | 612 KB | 6 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E D | 26,024 | 129,438 | 0.0 | 60% | 2% | 44% | 5,368 KB | 449 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 24,608 | 28,357 | 22.8 | 30% | 53% | 93% | 1,863 KB | 159 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B E B | 22,251 | 32,492 | 64.8 | 57% | 16% | 93% | 1,106 KB | 1 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B D B | 20,920 | 47,342 | 46.0 | 65% | 17% | 100% | 874 KB | 4 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C B | 20,405 | 163,846 | 52.3 | 72% | 26% | 81% | 1,504 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C F D | 19,784 | 29,036 | 21.5 | 36% | 0% | 25% | 822 KB | 16 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C C D | 19,713 | 39,491 | 0.0 | 77% | 34% | – | 485 KB | 2 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 19,506 | 37,411 | 17.6 | 31% | 42% | 91% | 8,727 KB | 143 (+2) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C B A | 19,160 | 34,146 | 46.1 | 81% | 25% | 97% | 338 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C C A | 18,811 | 57,499 | 42.6 | 70% | 5% | 86% | 241 KB | 136 (+2) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 18,144 | 41,355 | 0.0 | 90% | 35% | – | 1,153 KB | 2 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | C F B | 17,697 | 29,269 | 34.5 | 34% | 30% | 98% | 3,556 KB | 2,117 (+2) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B D | 17,544 | 23,247 | 0.0 | 90% | 59% | 4% | 441 KB | 0 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C B B | 17,477 | 20,444 | 0.0 | 89% | 46% | 99% | 223 KB | 124 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 16,293 | 72,576 | 0.0 | 67% | 47% | – | 1,058 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 15,995 | 37,225 | 25.3 | 39% | 42% | 98% | 515 KB | 21 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 15,738 | 43,039 | 0.0 | 57% | 25% | 50% | 565 KB | 1 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 15,311 | 23,414 | 15.2 | 15% | 35% | – | 123 KB | 2 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | C E B | 15,167 | 20,852 | 24.4 | 67% | 36% | 91% | 158 KB | 5 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C C D | 15,117 | 101,962 | 2.0 | 79% | 3% | 0% | 6,837 KB | 1 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 14,955 | 445,294 | 0.0 | 71% | 47% | 0% | 3,286 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C B | 14,512 | 32,454 | 30.1 | 72% | 34% | 80% | 102 KB | 233 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 14,489 | 29,593 | 27.2 | 67% | 3% | 100% | 1,965 KB | 3 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,427 | 49,006 | 35.5 | 50% | 0% | 62% | 355 KB | 2 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C D C | 14,415 | 19,800 | 22.5 | 66% | 24% | 99% | 198 KB | 34 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 14,293 | 18,455 | 33.1 | 78% | 51% | 99% | 201 KB | 6 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 14,235 | 19,488 | 5.4 | 20% | 22% | 100% | 2,284 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C D B | 14,185 | 72,298 | 34.6 | 69% | 56% | 87% | 1,434 KB | 70,892 (+11) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 14,140 | 27,838 | 150 | 33% | 28% | 94% | 237 KB | 21 (+1) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | C E B | 13,910 | 14,980 | 19.9 | 50% | 24% | 95% | 162 KB | 1 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | C F B | 13,548 | 12,228 | 24.9 | 29% | 0% | 100% | 192 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C F B | 13,246 | 53,652 | 2.9 | 39% | 0% | 99% | 1,488 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 229,395 | 60.2 | 82% | 43% | 96% | 158 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 12,880 | 18,248 | 8.1 | 0% | 10% | 98% | 516 KB | 142 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 12,695 | 18,688 | 32.8 | 54% | 15% | 100% | 462 KB | 9 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 12,653 | 30,206 | 94.6 | 53% | 57% | 76% | 392 KB | 74 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C B C | 12,422 | 19,801 | 17.3 | 83% | 77% | 100% | 4,357 KB | 15 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C F B | 12,068 | 11,235 | 15.2 | 23% | 0% | 97% | 612 KB | 13 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C D B | 11,951 | 24,896 | 49.5 | 62% | 5% | 98% | 252 KB | 1 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C E A | 11,288 | 16,335 | 19.8 | 49% | 0% | 88% | 281 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | C C B | 11,188 | 19,864 | 37.1 | 72% | 29% | 100% | 178 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 11,129 | 20,692 | 7.1 | 12% | 7% | 100% | 595 KB | 19 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C B B | 11,059 | 17,296 | 48.1 | 80% | 64% | 97% | 939 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 11,016 | 22,390 | 65.5 | 52% | 41% | 100% | 275 KB | 6,583 (+4) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 11,004 | 14,781 | 0.0 | 74% | 21% | 15% | 1,648 KB | 37 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C B A | 11,002 | 35,528 | 20.6 | 80% | 34% | 88% | 153 KB | 4 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C E B | 10,769 | 15,417 | 24.7 | 55% | 2% | 96% | 608 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F C | 10,639 | 17,946 | 21.4 | 33% | 0% | 100% | 599 KB | 22 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C C C | 10,526 | 23,202 | 25.6 | 70% | 53% | 89% | 363 KB | 11 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 10,082 | 27,854 | 27.1 | 61% | 21% | 99% | 1,148 KB | 39 (+1) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 9,968 | 15,066 | 49.3 | 19% | 34% | 96% | 158 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 9,909 | 14,605 | 0.0 | 79% | 34% | 84% | 344 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 9,654 | 13,516 | 44.4 | 70% | 43% | 99% | 223 KB | 9 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D D A | 9,101 | 10,137 | 0.0 | 61% | 12% | 92% | 254 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 8,935 | 14,430 | 17.1 | 28% | 41% | 94% | 262 KB | 9 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 8,490 | 11,996 | 7.5 | 63% | 9% | 88% | 710 KB | 4 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 8,479 | 14,645 | 39.2 | 79% | 28% | 100% | 2,365 KB | 5 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | D E B | 8,386 | 18,757 | 6.6 | 60% | 0% | 91% | 941 KB | 2 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D E B | 8,284 | 24,713 | 107 | 40% | 32% | 92% | 5,372 KB | 85 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E B | 8,231 | 20,715 | 13.0 | 49% | 0% | 76% | 1,258 KB | 13 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | D D B | 8,223 | 13,834 | 30.7 | 69% | 21% | 99% | 703 KB | 2 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F D | 8,119 | 225,234 | 35.3 | 0% | 0% | 83% | 3,975 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 7,848 | 35,983 | 21.0 | 55% | 6% | 96% | 705 KB | 48 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 7,776 | 9,846 | 11.6 | 11% | 19% | 98% | 226 KB | 5 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D D B | 7,694 | 25,692 | 22.0 | 62% | 58% | 99% | 617 KB | 1 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D E A | 7,638 | 37,731 | 18.5 | 52% | 41% | 87% | 35 KB | 0 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 7,589 | 8,321 | 54.2 | 52% | 0% | – | 250 KB | 3 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | D F C | 7,236 | 13,342 | 0.0 | 21% | 0% | 64% | 255 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D D D | 7,213 | 17,705 | 75.0 | 69% | 3% | – | 470 KB | 3 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | D E C | 7,167 | 23,775 | 14.4 | 67% | 39% | 93% | 464 KB | 25 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | D F C | 7,090 | 23,469 | 10.8 | 39% | 6% | 99% | 884 KB | 3 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D F A | 7,013 | 15,580 | 31.1 | 33% | 2% | 100% | 135 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D F B | 6,708 | 6,989 | 14.6 | 77% | 14% | 99% | 605 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | D E C | 6,471 | 23,756 | 18.2 | 77% | 22% | 82% | 431 KB | 0 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | D F C | 6,417 | 11,425 | 0.0 | 49% | 6% | 95% | 1,175 KB | 51 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F B | 6,352 | 36,140 | 18.9 | 21% | 0% | 98% | 1,129 KB | 49 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 6,334 | 12,088 | 19.1 | 27% | 0% | 91% | 315 KB | 159 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D C C | 6,177 | 68,430 | 16.1 | 74% | 19% | 97% | 393 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D D B | 6,128 | 13,660 | 139 | 62% | 39% | 100% | 2,484 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D F B | 5,920 | 106,388 | 0.0 | 56% | 0% | 94% | 590 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F A | 5,901 | 20,497 | 29.4 | 35% | 0% | 87% | 253 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 5,875 | 9,731 | 6.8 | 61% | 0% | 91% | 739 KB | 9 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | D F B | 5,807 | 6,116 | 5.0 | 8% | 0% | 99% | 59 KB | 2 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D E B | 5,618 | 8,444 | 17.6 | 62% | 0% | 88% | 423 KB | 2 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 5,364 | 9,247 | 44.8 | 8% | 18% | 90% | 230 KB | 7 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D C B | 5,166 | 19,927 | 37.3 | 79% | 58% | 100% | 36 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | D F D | 5,127 | 10,128 | 20.0 | 31% | 8% | – | 65 KB | 3 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,860 | 12,636 | 20.0 | 7% | 32% | 93% | 316 KB | 1 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,781 | 5,176 | 14.4 | 56% | 8% | 92% | 153 KB | 1 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 4,660 | 7,656 | 24.5 | 25% | 0% | 99% | 49 KB | 23,918 (+8) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 4,578 | 47,350 | 21.5 | 55% | 7% | 96% | 1,414 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 4,576 | 21,784 | 0.0 | 14% | 22% | 94% | 674 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | E D A | 4,520 | 6,580 | 71.9 | 66% | 8% | 99% | 28 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 4,487 | 8,618 | 3.7 | 15% | 34% | 90% | 4,198 KB | 560 (+1) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 4,391 | 6,337 | 0.1 | 0% | 19% | 20% | 283 KB | 1 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E E C | 4,266 | 11,078 | 25.4 | 64% | 0% | 100% | 628 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E E D | 4,256 | 6,583 | 0.8 | 62% | 18% | – | 257 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 4,253 | 8,207 | 20.7 | 26% | 0% | 100% | 42 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | E E B | 4,170 | 11,546 | 15.2 | 69% | 0% | 99% | 1,145 KB | 9 (+1) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,143 | 91,902 | 18.1 | 17% | 0% | 100% | 261 KB | 2 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E C B | 4,058 | 6,361 | 0.0 | 77% | 66% | 82% | 394 KB | 3 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 3,989 | 7,998 | 0.0 | 57% | 0% | – | 202 KB | 5 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,873 | 4,323 | 0.1 | 21% | 8% | 86% | 382 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E D C | 3,738 | 7,144 | 49.6 | 67% | 35% | 100% | 598 KB | 5 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 3,686 | 6,117 | 37.4 | 48% | 0% | 97% | 107 KB | 3 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E E B | 3,641 | 12,868 | 47.2 | 58% | 32% | 100% | 1,428 KB | 8 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E D C | 3,616 | 3,880 | 34.2 | 61% | 26% | 100% | 858 KB | 0 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 3,591 | 3,567 | 11.9 | 40% | 0% | 98% | 544 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 3,588 | 16,977 | 0.0 | 63% | 0% | 97% | 635 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | E F C | 3,481 | 13,910 | 22.0 | 30% | 18% | 100% | 374 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,309 | 5,369 | 24.0 | 34% | 18% | 100% | 387 KB | 18 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E E B | 3,303 | 9,460 | 12.8 | 46% | 11% | 94% | 356 KB | 182 (+5) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,246 | 122,918 | 4.3 | 46% | 6% | 73% | 126 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F A | 3,232 | 4,798 | 20.4 | 8% | 28% | 86% | 312 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,076 | 6,705 | 10.0 | 11% | 28% | 93% | 378 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 3,019 | 4,701 | 12.8 | 36% | 0% | 98% | 71 KB | 1 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | E F A | 2,944 | 4,176 | 13.2 | 59% | 0% | 100% | 365 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,905 | 35,139 | 0.0 | 41% | 0% | – | 212 KB | 30 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | E F C | 2,878 | 153,741 | 17.0 | 60% | 0% | 66% | 324 KB | 40,823 (+15) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 2,788 | 3,991 | 7.0 | 46% | 0% | 87% | 6,579 KB | 8 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E D D | 2,764 | 10,718 | 0.0 | 69% | 56% | 42% | 268 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 2,748 | 4,555 | 10.8 | 57% | 0% | 72% | 1,031 KB | 2 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 2,694 | 6,587 | 10.7 | 46% | 0% | 78% | 162 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,640 | 3,827 | 29.3 | 41% | 22% | – | 454 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E E D | 2,521 | 5,545 | 0.1 | 58% | 19% | 0% | 601 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,498 | 7,028 | 0.0 | 4% | 0% | 0% | 1,274 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,477 | 3,289 | 14.1 | 49% | 0% | 99% | 386 KB | 2 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 2,461 | 4,847 | 14.4 | 4% | 0% | 97% | 556 KB | 96 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 2,457 | 8,375 | 19.5 | 45% | 52% | 84% | 540 KB | 10 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 2,428 | 8,464 | 0.0 | 16% | 0% | – | 320 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | E D D | 2,348 | 10,596 | 11.2 | 67% | 0% | 1% | 227 KB | 9 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 2,242 | 25,829 | 43.6 | 5% | 5% | 100% | 605 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 2,242 | 3,586 | 11.9 | 20% | 23% | 98% | 266 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 2,216 | 3,225 | 11.6 | 56% | 0% | 100% | 168 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,201 | 2,369 | 16.7 | 18% | 16% | 97% | 106 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,186 | 7,730 | 5.9 | 42% | 0% | 98% | 550 KB | 12 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 2,167 | 5,951 | 6.1 | 25% | 0% | 78% | 299 KB | 348 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,128 | 2,113 | 30.0 | 51% | 10% | 100% | 512 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | E F C | 2,123 | 3,344 | 24.6 | 3% | 21% | 98% | 791 KB | 1 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 2,123 | 3,518 | 18.0 | 11% | 0% | 97% | 163 KB | 6 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E C C | 2,091 | 5,047 | 0.0 | 76% | 78% | 100% | 2,039 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E D E | 2,068 | 88,808 | 0.0 | 63% | 12% | 52% | 188 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 2,049 | 3,449 | 19.1 | 19% | 0% | 93% | 322 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 2,030 | 8,429 | 17.2 | 0% | 0% | 99% | 243 KB | 9 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 2,029 | 4,319 | 11.5 | 34% | 0% | 99% | 43 KB | 2 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,003 | 7,768 | 20.4 | 8% | 14% | 99% | 169 KB | 13 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E E D | 1,982 | 9,650 | 0.0 | 62% | 8% | 6% | 158 KB | 120 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 1,956 | 7,653 | 11.0 | 37% | 0% | 45% | 144 KB | 16 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,925 | 4,332 | 9.2 | 57% | 55% | 99% | 358 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 1,914 | 2,581 | 18.8 | 68% | 0% | 96% | 93 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 1,879 | 4,432 | 6.8 | 74% | 0% | 99% | 236 KB | 5 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 1,872 | 5,025 | 43.5 | 10% | 0% | 100% | 190 KB | 2 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F C | 1,860 | 6,960 | 22.6 | 41% | 0% | 52% | 103 KB | 4 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 1,851 | 41,023 | 4.9 | 16% | 0% | 84% | 24 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E E B | 1,825 | 59,833 | 43.4 | 44% | 0% | 100% | 628 KB | 2 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E D C | 1,751 | 6,123 | 0.9 | 62% | 8% | 95% | 5,635 KB | 1 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,651 | 3,772 | 9.5 | 42% | 0% | 97% | 518 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,594 | 2,504 | 0.0 | 22% | 20% | 75% | 294 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F B | 1,540 | 5,195 | 24.8 | 64% | 0% | 81% | 59 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,514 | 1,845 | 0.0 | 0% | 0% | 33% | 284 KB | 464 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 1,513 | 4,250 | 19.1 | 60% | 0% | 98% | 258 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,488 | 3,707 | 26.4 | 30% | 0% | 73% | 996 KB | 120 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F D | 1,478 | 2,021 | 17.0 | 50% | 0% | 25% | 646 KB | 2 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,473 | 2,833 | 9.6 | 25% | 0% | 82% | 274 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,446 | 2,552 | 4.9 | 55% | 0% | 99% | 168 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,382 | 3,945 | 0.0 | 33% | 0% | – | 1,007 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,344 | 22,529 | 4.1 | 78% | 0% | 100% | 1,185 KB | 6 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F C | 1,239 | 9,015 | 0.1 | 7% | 0% | 82% | 173 KB | 54 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,158 | 6,800 | 23.8 | 20% | 51% | 100% | 363 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E F B | 1,152 | 3,065 | 25.6 | 13% | 0% | 99% | 578 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E F C | 1,145 | 1,603 | 12.5 | 29% | 0% | 98% | 165 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 1,141 | 1,701 | 22.5 | 0% | 0% | 95% | 68 KB | 63 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,066 | 1,232 | 33.6 | 35% | 0% | 94% | 573 KB | 2 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 1,017 | 1,658 | 9.1 | 53% | 12% | 98% | 478 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F B | 967 | 4,148 | 25.8 | 32% | 9% | 99% | 603 KB | 2 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 956 | 129,162 | 0.0 | 54% | 0% | – | 8,190 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 934 | 2,378 | 3.8 | 20% | 0% | 87% | 602 KB | 2 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 865 | 1,489 | 9.9 | 72% | 34% | 95% | 457 KB | 14 (+0) |
| [integry/propr](https://github.com/integry/propr) | F F B | 855 | 2,398 | 5.7 | 0% | 0% | 100% | 4,314 KB | 34 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 786 | 5,484 | 11.4 | 60% | 0% | 100% | 1,089 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 782 | 1,534 | 34.9 | 10% | 0% | 100% | 704 KB | 13 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 752 | 1,669 | 8.9 | 0% | 0% | 98% | 105 KB | 3 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 611 | 7,427 | 13.0 | 62% | 7% | 99% | 634 KB | 11 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 600 | 1,281 | 0.0 | 29% | 0% | 0% | 671 KB | 3 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 511 | 3,869 | 14.1 | 0% | 0% | 99% | 215 KB | 1 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 480 | 633 | 10.4 | 54% | 0% | 100% | 87 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 474 | 928 | 0.0 | 22% | 0% | – | 80 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 458 | 2,867 | 7.4 | 10% | 0% | 99% | 45 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 448 | 4,818 | 9.4 | 53% | 0% | 99% | 221 KB | 7 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 400 | 59,121 | 108 | 20% | 0% | 94% | 378 KB | 3 (-1) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 374 | 5,495 | 5.9 | 28% | 0% | 95% | 385 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 343 | 1,401 | 16.9 | 11% | 0% | 100% | 126 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 333 | 9,875 | 15.3 | 23% | 0% | 80% | 149 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 329 | 1,057 | 0.0 | 42% | 0% | 83% | 554 KB | 28 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 314 | 2,417 | 16.7 | 0% | 0% | 98% | 1,116 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 261 | 4,075 | 5.3 | 44% | 0% | – | 424 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 260 | 627 | 6.7 | 0% | 0% | 65% | 642 KB | 6 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 228 | 721 | 32.0 | 0% | 0% | 99% | 974 KB | 2 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 208 | 525 | 17.8 | 46% | 0% | 76% | 16 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 171 | 2,668 | 1.7 | 62% | 0% | – | 201 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 167 | 726 | 7.7 | 0% | 0% | 100% | 104 KB | 253 (+5) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 156 | 1,605 | 4.0 | 0% | 0% | 99% | 569 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 147 | 3,302 | 22.5 | 0% | 0% | 97% | 582 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 130 | 1,002 | 4.8 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 97 | 920 | 11.1 | 44% | 0% | 94% | 1,170 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,108 | 11.9 | 0% | 0% | 24% | 7,014 KB | 20 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 42 | 1,021 | 9.6 | 18% | 0% | 99% | 87 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 35 | 4,186 | 4.0 | 25% | 0% | 67% | 46 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 30 | 42,566 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 18 | 4,469 | 1.1 | 29% | 0% | 100% | 52 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 4 | 1,851 | 4.2 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 3 | 643 | 0.0 | 64% | 0% | 100% | 477 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 2 | 410 | 11.0 | 0% | 0% | 97% | 270 KB | 0 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F E B | – | – | 69.0 | 51% | 2% | 100% | 3,196 KB | 90 (+3) |
| [purlis/purlis](https://github.com/purlis/purlis) | F B B | – | – | 58.7 | 83% | 30% | 91% | 914 KB | 12 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 271 | 35.7 | 0% | 0% | 91% | 137 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 26.3 | – | – | 100% | 703 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F B | 0 | 168 | 26.1 | 0% | 0% | 71% | 169 KB | 2 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 0 | 25.8 | 50% | 0% | 97% | 405 KB | 1,652 (+16) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 24.1 | 75% | 0% | 90% | 2,290 KB | 1,529 (+3) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 2,494 | 21.5 | 21% | 0% | 76% | 1,719 KB | 6 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 332 | 21.3 | 29% | 0% | 99% | 1,060 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 3 | 20.7 | 0% | 0% | 79% | 416 KB | 9 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 19.9 | 43% | 0% | 100% | 154 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 0 | 0 | 18.0 | 0% | 0% | 99% | 98 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 17.8 | 54% | 22% | 90% | 1,039 KB | 4 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 16.7 | – | – | 91% | 306 KB | 7 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 260 | 16.6 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 870 | 15.8 | 0% | 0% | 94% | 249 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 10 | 14.4 | 0% | 0% | 100% | 25 KB | 19 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 103 | 14.4 | 61% | 0% | 85% | 263 KB | 1,255 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 14.0 | 59% | 9% | 76% | 86 KB | 7 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,230 | 13.6 | 13% | 0% | 93% | 927 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 215 | 13.1 | 0% | 0% | 0% | 348 KB | 1 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 12.9 | – | – | 100% | 41 KB | 2 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 12.8 | – | – | 53% | 3,052 KB | 2 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 257 | 12.7 | 0% | 0% | 95% | 123 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 9.9 | – | – | 100% | 403 KB | 2 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | 0 | 23,149 | 9.6 | 39% | 0% | 72% | 396 KB | 2 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 9.5 | 0% | 0% | 0% | 206 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 9.1 | – | – | 100% | 160 KB | 2 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 9.1 | – | – | 99% | 80 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 1,161 | 8.7 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 9 | 8.6 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 0 | 8.6 | 0% | 0% | 96% | 99 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 0 | 8.4 | – | – | 97% | 504 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 8.1 | – | – | 95% | 8,119 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 0 | 32 | 7.9 | 0% | 0% | 80% | 27 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.8 | – | – | 89% | 682 KB | 6 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 389 | 6.0 | 0% | 0% | 100% | 156 KB | 2 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | – | – | 5.5 | – | – | 99% | 127 KB | 24 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 13,112 | 5.1 | 28% | 0% | 99% | 399 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 120 | 5.0 | 0% | 0% | 87% | 489 KB | 86 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 95 | 4.9 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 0 | 4.8 | – | – | – | 14 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 4.6 | – | – | – | 311 KB | 4 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 0 | 4.6 | – | – | 88% | 739 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 6 | 4.4 | 0% | 0% | 97% | 695 KB | 2 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 2,299 | 4.4 | 0% | 0% | 0% | 285 KB | 25 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | – | – | 4.3 | – | – | 97% | 43 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 4.1 | – | – | 93% | 576 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 4.0 | – | – | 80% | 83 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 0 | 2,446 | 4.0 | 9% | 0% | 96% | 697 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 4.0 | – | – | 89% | 163 KB | 15 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 987 | 3.9 | 29% | 0% | 98% | 104 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 3.6 | – | – | 98% | 363 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 1,629 | 3.2 | 0% | 0% | 95% | 165 KB | 2 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 294 | 3.0 | 0% | 0% | – | 710 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 6,581 | 2.8 | 0% | 0% | 85% | 2,636 KB | 44 (+1) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | – | – | 2.4 | – | – | 90% | 319 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 1,189 | 2.2 | 26% | 0% | 79% | 625 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 1.3 | – | – | 99% | 298 KB | 5 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 1.1 | – | – | 98% | 231 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.8 | – | – | – | 53 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 0.8 | – | – | 98% | 723 KB | 5 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | – | – | 0.7 | – | – | – | 56 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.5 | – | – | 99% | 73 KB | 3 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.5 | 46% | 36% | 0% | 2,040 KB | 463 (+2) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.4 | – | – | 96% | 122 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.3 | – | – | 20% | 154 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.2 | – | – | 100% | 59 KB | 1 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F D B | – | – | 0.2 | 70% | 26% | 77% | 852 KB | 7 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.2 | – | – | 98% | 42 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.2 | – | – | 0% | 518 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 1,509 | 0.1 | 27% | 0% | 90% | 1,468 KB | 1,121 (+3) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,331 (+3) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 46% | 17% | 61% | 88 KB | 5 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 156 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 164 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 169 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 1,996 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | – | – | 0.0 | – | – | 30% | 308 KB | 821 (+5) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.0 | – | – | 69% | 290 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F D E | – | – | 0.0 | 63% | 35% | 94% | 40,903 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
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
