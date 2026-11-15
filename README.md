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
_355 repos, last measured 2026-11-15. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (355)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 88,807 | 86,978 | 69.4 | 61% | 28% | 87% | 416 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A B B | 80,926 | 111,797 | 61.2 | 84% | 32% | 100% | 322 KB | 3 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A B C | 68,376 | 189,742 | 155 | 84% | 85% | 55% | 311 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A E C | 63,755 | 122,763 | 228 | 45% | 35% | 91% | 2,350 KB | 5 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A C D | 53,667 | 148,178 | 89.9 | 78% | 42% | 3% | 490 KB | 1 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | A D D | 40,585 | 51,318 | 0.1 | 69% | 67% | 0% | 3,565 KB | 3 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B C B | 32,414 | 43,406 | 0.1 | 74% | 37% | 88% | 3,842 KB | 7 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,086 | 34,745 | 22.7 | 74% | 33% | 100% | 613 KB | 6 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E D | 26,024 | 129,438 | 0.0 | 60% | 2% | 44% | 5,368 KB | 449 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 24,608 | 28,357 | 22.8 | 30% | 53% | 93% | 1,863 KB | 159 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B E B | 22,251 | 32,492 | 64.8 | 57% | 16% | 93% | 1,106 KB | 1 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C B | 20,405 | 163,846 | 52.3 | 72% | 26% | 81% | 1,504 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C F D | 19,784 | 27,492 | 18.5 | 35% | 0% | 25% | 822 KB | 16 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C D D | 19,666 | 39,740 | 0.0 | 70% | 34% | – | 534 KB | 2 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C E C | 19,506 | 41,652 | 17.7 | 51% | 42% | 90% | 8,727 KB | 144 (+1) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C C A | 18,811 | 57,499 | 42.6 | 70% | 5% | 86% | 241 KB | 136 (+2) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | C D B | 18,751 | 44,424 | 47.1 | 63% | 17% | 100% | 878 KB | 4 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 18,144 | 41,355 | 0.0 | 90% | 35% | – | 1,153 KB | 2 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | C F B | 17,697 | 29,269 | 34.5 | 34% | 30% | 98% | 3,556 KB | 2,117 (+2) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B D | 17,544 | 23,247 | 0.0 | 90% | 59% | 4% | 441 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C B D | 17,255 | 442,360 | 0.0 | 81% | 44% | 0% | 3,286 KB | 1 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F C | 16,331 | 26,019 | 21.9 | 26% | 0% | 100% | 607 KB | 22 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 16,293 | 72,576 | 0.0 | 67% | 47% | – | 1,058 KB | 0 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 15,738 | 43,039 | 0.0 | 57% | 25% | 50% | 565 KB | 1 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | C F B | 15,167 | 20,615 | 23.2 | 64% | 6% | 97% | 158 KB | 5 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C A B | 15,125 | 19,253 | 0.0 | 92% | 30% | 99% | 223 KB | 127 (+2) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C C D | 15,117 | 101,962 | 2.0 | 79% | 3% | 0% | 6,837 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D B | 14,512 | 31,350 | 30.9 | 69% | 36% | 76% | 103 KB | 233 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,427 | 49,006 | 35.5 | 50% | 0% | 62% | 355 KB | 2 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C D C | 14,415 | 21,097 | 21.6 | 67% | 23% | 99% | 198 KB | 34 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C B C | 14,325 | 18,508 | 0.0 | 82% | 18% | 100% | 4,357 KB | 15 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C C | 14,293 | 21,064 | 31.5 | 76% | 47% | 94% | 201 KB | 6 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 14,140 | 27,838 | 150 | 33% | 28% | 94% | 237 KB | 21 (+1) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 14,064 | 31,249 | 95.4 | 51% | 59% | 76% | 393 KB | 74 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | C E B | 13,910 | 14,980 | 19.9 | 50% | 24% | 95% | 162 KB | 1 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 13,878 | 22,174 | 16.0 | 13% | 35% | – | 125 KB | 2 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C B A | 13,811 | 19,386 | 45.6 | 89% | 31% | 96% | 338 KB | 1 (+1) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 13,569 | 21,960 | 33.4 | 74% | 12% | 100% | 464 KB | 9 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | C F B | 13,548 | 12,228 | 24.9 | 29% | 0% | 100% | 192 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C F B | 13,246 | 53,652 | 2.9 | 39% | 0% | 99% | 1,488 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 12,936 | 28,846 | 8.2 | 0% | 9% | 98% | 516 KB | 142 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C E B | 12,719 | 26,155 | 27.8 | 78% | 4% | 100% | 1,965 KB | 3 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C F B | 12,068 | 11,536 | 15.4 | 23% | 0% | 97% | 612 KB | 13 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C D B | 11,951 | 24,896 | 49.5 | 62% | 5% | 98% | 252 KB | 1 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | C F A | 11,793 | 35,151 | 61.2 | 11% | 5% | 90% | 413 KB | 87 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | C F A | 11,608 | 17,203 | 17.9 | 26% | 35% | 94% | 262 KB | 9 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 11,360 | 32,006 | 24.8 | 32% | 25% | 98% | 515 KB | 21 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C E A | 11,288 | 25,307 | 20.1 | 42% | 0% | 89% | 300 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | C D B | 11,188 | 26,931 | 37.6 | 70% | 32% | 100% | 178 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 11,129 | 17,931 | 7.0 | 41% | 9% | 97% | 595 KB | 19 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C B B | 11,059 | 17,296 | 48.1 | 80% | 64% | 97% | 939 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 11,016 | 22,390 | 65.5 | 52% | 41% | 100% | 275 KB | 6,583 (+4) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 11,004 | 14,781 | 0.0 | 74% | 21% | 15% | 1,648 KB | 37 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C A | 10,792 | 32,990 | 20.7 | 76% | 36% | 87% | 154 KB | 4 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C E B | 10,769 | 15,417 | 24.7 | 55% | 2% | 96% | 608 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C C C | 10,526 | 23,202 | 25.6 | 70% | 53% | 89% | 363 KB | 11 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 10,452 | 17,240 | 29.9 | 54% | 2% | 100% | 135 KB | 1 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 10,053 | 31,995 | 26.6 | 52% | 18% | 100% | 1,158 KB | 39 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 9,968 | 15,066 | 49.3 | 19% | 34% | 96% | 158 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 9,909 | 14,605 | 0.0 | 79% | 34% | 84% | 344 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 9,654 | 13,516 | 44.4 | 70% | 43% | 99% | 223 KB | 9 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 9,618 | 18,726 | 5.2 | 26% | 23% | 100% | 2,284 KB | 0 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D F B | 8,926 | 24,426 | 105 | 38% | 33% | 93% | 5,422 KB | 85 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | D E C | 8,741 | 15,195 | 0.0 | 59% | 33% | 95% | 1,175 KB | 51 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 8,490 | 11,996 | 7.5 | 63% | 9% | 88% | 710 KB | 4 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | D E B | 8,386 | 18,757 | 6.6 | 60% | 0% | 91% | 941 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E B | 8,231 | 20,715 | 13.0 | 49% | 0% | 76% | 1,258 KB | 13 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 8,227 | 13,325 | 38.2 | 76% | 27% | 100% | 2,365 KB | 5 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D F A | 8,199 | 45,920 | 18.6 | 32% | 39% | 88% | 38 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D F A | 7,924 | 8,277 | 0.0 | 25% | 0% | 92% | 254 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 7,848 | 35,983 | 21.0 | 55% | 6% | 96% | 705 KB | 48 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 7,776 | 12,086 | 11.4 | 30% | 13% | 97% | 232 KB | 5 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 7,589 | 8,321 | 54.2 | 52% | 0% | – | 250 KB | 3 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 7,536 | 24,865 | 23.4 | 51% | 55% | 99% | 617 KB | 1 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | D F C | 7,236 | 13,342 | 0.0 | 21% | 0% | 64% | 255 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D D D | 7,213 | 17,705 | 75.0 | 69% | 3% | – | 470 KB | 3 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | D E C | 7,167 | 23,775 | 14.4 | 67% | 39% | 93% | 464 KB | 25 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | D F C | 7,090 | 23,469 | 10.8 | 39% | 6% | 99% | 884 KB | 3 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | D E B | 7,026 | 12,640 | 29.6 | 66% | 13% | 99% | 703 KB | 2 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D D B | 6,736 | 71,470 | 33.9 | 64% | 45% | 86% | 1,434 KB | 70,914 (+22) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D F B | 6,735 | 6,268 | 14.5 | 60% | 16% | 99% | 605 KB | 1 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D E B | 6,722 | 10,952 | 13.0 | 54% | 9% | 95% | 360 KB | 184 (+2) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 6,555 | 11,554 | 6.2 | 68% | 0% | 88% | 739 KB | 9 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D F B | 6,408 | 10,374 | 23.4 | 39% | 0% | 72% | 104 KB | 4 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F B | 6,352 | 36,140 | 18.9 | 21% | 0% | 98% | 1,129 KB | 49 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 6,334 | 12,088 | 19.1 | 27% | 0% | 91% | 315 KB | 159 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 6,177 | 68,979 | 15.8 | 74% | 29% | 97% | 393 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D C B | 6,128 | 15,042 | 136 | 79% | 35% | 100% | 2,499 KB | 0 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 25,396 | 29.0 | 32% | 5% | 77% | 270 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D E B | 5,618 | 8,444 | 17.6 | 62% | 0% | 88% | 423 KB | 2 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 5,571 | 17,190 | 0.0 | 56% | 0% | 97% | 640 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | D F B | 5,390 | 53,004 | 42.1 | 27% | 0% | 100% | 634 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 5,364 | 9,247 | 44.8 | 8% | 18% | 90% | 230 KB | 7 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D B B | 5,166 | 19,830 | 37.8 | 81% | 60% | 100% | 37 KB | 0 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 4,951 | 7,868 | 0.1 | 4% | 14% | 12% | 283 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | E C A | 4,916 | 7,592 | 69.4 | 77% | 12% | 100% | 28 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,860 | 12,636 | 20.0 | 7% | 32% | 93% | 316 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E C C | 4,857 | 20,784 | 17.9 | 75% | 19% | 82% | 431 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E E D | 4,842 | 9,630 | 19.2 | 42% | 8% | – | 65 KB | 3 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,781 | 5,176 | 14.4 | 56% | 8% | 92% | 153 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | E F B | 4,710 | 4,820 | 4.0 | 10% | 0% | 99% | 59 KB | 3 (+1) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 4,660 | 7,656 | 24.5 | 25% | 0% | 99% | 49 KB | 23,918 (+8) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E E B | 4,578 | 46,946 | 16.0 | 65% | 8% | 96% | 1,414 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 4,576 | 21,784 | 0.0 | 14% | 22% | 94% | 674 KB | 2 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 4,487 | 8,618 | 3.7 | 15% | 34% | 90% | 4,198 KB | 560 (+1) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E E C | 4,312 | 11,571 | 24.3 | 63% | 0% | 100% | 628 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 4,253 | 8,207 | 20.7 | 26% | 0% | 100% | 42 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E E B | 4,201 | 106,400 | 0.0 | 54% | 0% | 97% | 590 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | E E B | 4,170 | 11,546 | 15.2 | 69% | 0% | 99% | 1,145 KB | 9 (+1) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,143 | 91,902 | 18.1 | 17% | 0% | 100% | 261 KB | 2 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 4,092 | 5,559 | 11.8 | 4% | 0% | 97% | 557 KB | 96 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E C B | 4,058 | 6,361 | 0.0 | 77% | 66% | 82% | 394 KB | 3 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E E D | 4,005 | 5,013 | 0.8 | 70% | 19% | 22% | 257 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 3,989 | 7,998 | 0.0 | 57% | 0% | – | 202 KB | 5 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | E F D | 3,971 | 95,494 | 32.3 | 0% | 0% | 36% | 3,975 KB | 1 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,944 | 10,813 | 0.1 | 23% | 7% | 86% | 390 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E D C | 3,738 | 7,144 | 49.6 | 67% | 35% | 100% | 598 KB | 5 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 3,686 | 6,117 | 37.4 | 48% | 0% | 97% | 107 KB | 3 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 3,591 | 3,567 | 11.9 | 40% | 0% | 98% | 544 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | E F C | 3,481 | 13,910 | 22.0 | 30% | 18% | 100% | 374 KB | 0 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E D C | 3,467 | 3,460 | 33.1 | 66% | 28% | 99% | 860 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 3,392 | 10,999 | 47.6 | 35% | 12% | 100% | 1,428 KB | 8 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,309 | 5,369 | 24.0 | 34% | 18% | 100% | 387 KB | 18 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,246 | 122,918 | 4.3 | 46% | 6% | 73% | 126 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 3,232 | 4,341 | 19.9 | 9% | 30% | 83% | 312 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,076 | 6,188 | 9.3 | 8% | 4% | 93% | 378 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 3,019 | 4,701 | 12.8 | 36% | 0% | 98% | 71 KB | 1 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | E F A | 2,944 | 4,176 | 13.2 | 59% | 0% | 100% | 365 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,905 | 35,139 | 0.0 | 41% | 0% | – | 212 KB | 30 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | E F C | 2,878 | 153,741 | 17.0 | 60% | 0% | 66% | 324 KB | 40,823 (+15) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 2,748 | 4,555 | 10.8 | 57% | 0% | 72% | 1,031 KB | 2 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 2,694 | 6,587 | 10.7 | 46% | 0% | 78% | 162 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E B D | 2,685 | 11,141 | 0.0 | 82% | 48% | 42% | 268 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,640 | 4,094 | 27.3 | 40% | 27% | – | 454 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E E D | 2,521 | 5,545 | 0.1 | 58% | 19% | 0% | 601 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,498 | 7,028 | 0.0 | 4% | 0% | 0% | 1,274 KB | 0 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E F C | 2,481 | 3,163 | 33.1 | 49% | 7% | 100% | 512 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 2,428 | 8,464 | 0.0 | 16% | 0% | – | 320 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E A | 2,341 | 6,216 | 24.9 | 71% | 0% | 90% | 59 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 2,294 | 6,444 | 19.4 | 50% | 23% | 84% | 540 KB | 11 (+1) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 2,245 | 5,870 | 42.4 | 9% | 0% | 100% | 190 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 2,242 | 25,829 | 43.6 | 5% | 5% | 100% | 605 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 2,242 | 3,123 | 12.1 | 31% | 24% | 98% | 267 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 2,220 | 3,471 | 7.1 | 23% | 0% | 97% | 6,579 KB | 8 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 2,216 | 3,225 | 11.6 | 56% | 0% | 100% | 168 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,201 | 2,369 | 16.7 | 18% | 16% | 97% | 106 KB | 1 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 2,161 | 5,323 | 6.1 | 22% | 0% | 73% | 299 KB | 348 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | E F C | 2,123 | 4,387 | 26.3 | 18% | 18% | 97% | 833 KB | 1 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E B E | 2,068 | 88,556 | 0.0 | 80% | 13% | 54% | 188 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 2,049 | 3,449 | 19.1 | 19% | 0% | 93% | 322 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 2,044 | 4,594 | 9.8 | 72% | 47% | 99% | 358 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 2,029 | 4,319 | 11.5 | 34% | 0% | 99% | 43 KB | 2 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,003 | 7,768 | 20.4 | 8% | 14% | 99% | 169 KB | 13 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 1,879 | 4,432 | 6.8 | 74% | 0% | 99% | 236 KB | 5 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 1,842 | 1,957 | 18.4 | 58% | 0% | 96% | 93 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E D C | 1,751 | 6,123 | 0.9 | 62% | 8% | 95% | 5,635 KB | 1 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | E F B | 1,606 | 3,632 | 6.8 | 32% | 0% | 99% | 45 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 1,598 | 7,340 | 5.4 | 29% | 0% | 98% | 550 KB | 12 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,594 | 2,456 | 0.0 | 21% | 28% | 72% | 294 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 1,572 | 45,434 | 4.8 | 22% | 0% | 83% | 23 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E E D | 1,567 | 2,267 | 18.0 | 60% | 0% | 62% | 646 KB | 2 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,514 | 5,238 | 0.0 | 30% | 0% | 33% | 284 KB | 464 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 1,513 | 4,961 | 20.1 | 72% | 0% | 98% | 258 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,488 | 3,707 | 26.4 | 30% | 0% | 73% | 996 KB | 120 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,473 | 2,734 | 9.5 | 32% | 0% | 82% | 274 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,446 | 2,552 | 4.9 | 55% | 0% | 99% | 168 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,431 | 3,032 | 13.9 | 9% | 0% | 98% | 386 KB | 2 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,382 | 1,974 | 9.3 | 8% | 0% | 98% | 105 KB | 3 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E D C | 1,361 | 1,956 | 8.6 | 69% | 11% | 98% | 483 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,358 | 3,171 | 0.0 | 29% | 0% | – | 1,007 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,344 | 22,529 | 4.1 | 78% | 0% | 100% | 1,185 KB | 6 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,321 | 6,961 | 5.9 | 8% | 0% | 100% | 4,314 KB | 34 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 1,303 | 8,624 | 0.0 | 63% | 9% | 6% | 158 KB | 120 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F C | 1,239 | 9,015 | 0.1 | 7% | 0% | 82% | 173 KB | 54 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,158 | 6,878 | 24.2 | 19% | 50% | 100% | 363 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 1,155 | 1,792 | 10.2 | 51% | 30% | 95% | 457 KB | 14 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 1,141 | 1,701 | 22.5 | 0% | 0% | 95% | 68 KB | 63 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,119 | 2,146 | 8.5 | 29% | 0% | 97% | 518 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E F B | 1,108 | 2,682 | 22.8 | 9% | 0% | 99% | 578 KB | 2 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 1,092 | 4,145 | 10.4 | 8% | 0% | 45% | 144 KB | 16 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,066 | 1,232 | 33.6 | 35% | 0% | 94% | 573 KB | 2 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | F F A | 987 | 2,125 | 16.2 | 17% | 0% | 97% | 163 KB | 6 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F B | 967 | 4,148 | 25.8 | 32% | 9% | 99% | 603 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 934 | 2,378 | 3.8 | 20% | 0% | 87% | 602 KB | 2 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 909 | 711 | 8.6 | 41% | 0% | 100% | 94 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 885 | 108,884 | 0.0 | 61% | 0% | – | 8,190 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F C C | 853 | 4,164 | 0.0 | 78% | 78% | 100% | 2,040 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 843 | 1,419 | 0.0 | 66% | 0% | 83% | 554 KB | 29 (+1) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 834 | 8,186 | 12.1 | 80% | 7% | 99% | 634 KB | 11 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 786 | 8,436 | 12.1 | 51% | 0% | 100% | 1,089 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 782 | 1,534 | 34.9 | 10% | 0% | 100% | 704 KB | 13 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | F E D | 699 | 8,752 | 10.9 | 65% | 0% | 1% | 227 KB | 9 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | 594 | 1,338 | 12.3 | 33% | 0% | 98% | 165 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 511 | 3,869 | 14.1 | 0% | 0% | 99% | 215 KB | 1 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 414 | 5,493 | 17.2 | 0% | 0% | 99% | 243 KB | 9 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 400 | 59,121 | 108 | 20% | 0% | 94% | 378 KB | 3 (-1) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 387 | 3,920 | 22.9 | 0% | 0% | 98% | 582 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 374 | 5,495 | 5.9 | 28% | 0% | 95% | 385 KB | 1 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 346 | 665 | 6.2 | 0% | 0% | 64% | 642 KB | 6 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 343 | 1,401 | 16.9 | 11% | 0% | 100% | 126 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 343 | 655 | 0.0 | 52% | 0% | 0% | 673 KB | 3 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 333 | 9,788 | 15.6 | 29% | 0% | 80% | 149 KB | 0 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 314 | 2,417 | 16.7 | 0% | 0% | 98% | 1,116 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 313 | 3,041 | 2.0 | 51% | 0% | – | 201 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 261 | 4,167 | 5.0 | 46% | 0% | – | 424 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 230 | 1,143 | 3.4 | 29% | 0% | 98% | 104 KB | 4 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 228 | 721 | 32.0 | 0% | 0% | 99% | 974 KB | 2 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 208 | 837 | 18.7 | 41% | 0% | 76% | 16 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 167 | 726 | 7.7 | 0% | 0% | 100% | 104 KB | 253 (+5) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 156 | 1,503 | 3.8 | 0% | 0% | 99% | 569 KB | 1 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 130 | 1,002 | 4.8 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 97 | 920 | 11.1 | 44% | 0% | 94% | 1,170 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,197 | 11.7 | 0% | 78% | 22% | 7,014 KB | 20 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 75 | 2,175 | 3.8 | 9% | 0% | 96% | 697 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 42 | 1,021 | 9.6 | 18% | 0% | 99% | 87 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 35 | 5,796 | 2.5 | 0% | 0% | 66% | 46 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 31 | 879 | 13.9 | 0% | 0% | 91% | 249 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 30 | 42,566 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 18 | 4,469 | 1.1 | 29% | 0% | 100% | 52 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 4 | 1,851 | 4.2 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 3 | 725 | 0.0 | 48% | 0% | 100% | 490 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 2 | 551 | 9.7 | 0% | 0% | 97% | 270 KB | 0 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F E B | – | – | 69.0 | 51% | 2% | 100% | 3,196 KB | 90 (+3) |
| [purlis/purlis](https://github.com/purlis/purlis) | F D B | – | – | 58.6 | 68% | 27% | 99% | 946 KB | 12 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 431 | 29.9 | 0% | 0% | 91% | 137 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 26.3 | – | – | 100% | 703 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 739 | 25.9 | 0% | 0% | 97% | 405 KB | 1,663 (+11) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F B | 0 | 2,698 | 24.3 | 0% | 0% | 71% | 169 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 24.1 | 75% | 0% | 90% | 2,290 KB | 1,529 (+3) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 2,494 | 21.5 | 21% | 0% | 76% | 1,719 KB | 6 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 332 | 21.3 | 29% | 0% | 99% | 1,060 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 19.9 | 43% | 0% | 100% | 154 KB | 4 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 0 | 19.5 | – | – | 79% | 416 KB | 9 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 0 | 0 | 18.0 | 0% | 0% | 99% | 98 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 17.8 | 54% | 22% | 90% | 1,039 KB | 4 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 17.0 | – | – | 91% | 306 KB | 7 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 103 | 14.4 | 61% | 0% | 85% | 263 KB | 1,255 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F D B | – | – | 13.9 | 69% | 10% | 73% | 86 KB | 7 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,058 | 13.6 | 0% | 0% | 94% | 935 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 9 | 13.1 | 0% | 0% | 100% | 25 KB | 19 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 215 | 13.1 | 0% | 0% | 0% | 348 KB | 1 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 12.9 | – | – | 100% | 41 KB | 2 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 206 | 11.4 | 0% | 0% | 95% | 123 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 276 | 10.6 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 9.8 | – | – | 53% | 3,052 KB | 2 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 9.5 | 0% | 0% | 0% | 206 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 4,221 | 9.2 | 47% | 0% | 99% | 221 KB | 7 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 9.1 | – | – | 100% | 160 KB | 2 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 9.1 | – | – | 99% | 80 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 1,229 | 8.5 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 9 | 8.1 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 8.1 | – | – | 95% | 8,119 KB | 1 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | 0 | 23,149 | 8.0 | 39% | 0% | 72% | 396 KB | 2 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 7.6 | – | – | 100% | 403 KB | 2 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 0 | 7.4 | 0% | 0% | 96% | 99 KB | 1 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.8 | – | – | 89% | 682 KB | 6 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 0 | 27 | 6.6 | 0% | 0% | 78% | 27 KB | 0 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 0 | 5.7 | – | – | 97% | 504 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | – | – | 5.1 | – | – | 99% | 127 KB | 25 (+1) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 120 | 5.0 | 0% | 0% | 87% | 489 KB | 86 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 169 | 5.0 | 0% | 0% | 100% | 156 KB | 2 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 95 | 4.9 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 0 | 4.8 | – | – | – | 14 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 0 | 4.6 | – | – | 88% | 739 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 12,776 | 4.6 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 2,299 | 4.4 | 0% | 0% | 0% | 285 KB | 25 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 470 | 4.3 | 0% | 0% | 97% | 695 KB | 2 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 4.1 | – | – | – | 311 KB | 4 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 4.1 | – | – | 93% | 576 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 4.0 | – | – | 80% | 83 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 4.0 | – | – | 89% | 163 KB | 15 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 0 | 3.9 | – | – | 91% | 43 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 1,629 | 3.2 | 0% | 0% | 95% | 165 KB | 2 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 239 | 3.0 | 0% | 0% | – | 710 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 6,266 | 2.5 | 0% | 0% | 92% | 2,640 KB | 44 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 2.3 | – | – | 90% | 319 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 1,189 | 2.2 | 26% | 0% | 79% | 625 KB | 0 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 2.1 | – | – | 98% | 363 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 1.3 | – | – | 99% | 298 KB | 5 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 0.8 | – | – | 98% | 723 KB | 5 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | – | – | 0.7 | – | – | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.5 | – | – | 99% | 73 KB | 3 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.4 | – | – | 96% | 122 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.4 | 48% | 29% | 0% | 2,040 KB | 463 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.3 | – | – | 20% | 154 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.2 | – | – | 100% | 59 KB | 1 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.2 | – | – | 98% | 42 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 0.2 | – | – | 98% | 231 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.2 | – | – | 0% | 518 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 1,509 | 0.1 | 27% | 0% | 90% | 1,468 KB | 1,121 (+3) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F B B | – | – | 0.1 | 87% | 19% | 82% | 857 KB | 7 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,331 (+3) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 44% | 16% | 61% | 88 KB | 5 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 156 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | – | – | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 371 | 0.0 | 0% | 0% | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 164 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 169 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 1,996 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | – | – | 0.0 | – | – | 30% | 308 KB | 821 (+5) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.0 | – | – | 69% | 290 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.0 | 60% | 35% | 94% | 41,060 KB | 0 (+0) |
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
