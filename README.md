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
_359 repos, last measured 2026-11-12. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (359)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A B C | 68,376 | 189,742 | 155 | 84% | 85% | 55% | 311 KB | 4 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A C B | 59,775 | 91,216 | 55.0 | 73% | 16% | 100% | 319 KB | 3 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A E D | 51,382 | 138,371 | 82.2 | 51% | 41% | 4% | 478 KB | 1 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 44,859 | 62,425 | 64.1 | 68% | 22% | 87% | 400 KB | 0 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 43,749 | 115,330 | 219 | 35% | 32% | 77% | 2,335 KB | 5 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B B B | 38,159 | 47,481 | 0.2 | 82% | 56% | 93% | 3,350 KB | 7 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B C D | 37,071 | 41,886 | 0.1 | 73% | 52% | 0% | 3,344 KB | 3 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B B B | 27,589 | 38,797 | 24.6 | 82% | 49% | 100% | 613 KB | 6 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B F D | 25,810 | 37,157 | 29.0 | 35% | 4% | 25% | 822 KB | 16 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | B D A | 25,489 | 62,390 | 53.3 | 66% | 5% | 90% | 241 KB | 131 (+1) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 24,608 | 30,881 | 25.4 | 33% | 53% | 100% | 1,797 KB | 159 (+1) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | B E D | 23,426 | 99,103 | 0.0 | 59% | 37% | – | 1,043 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B C A | 22,811 | 51,748 | 48.2 | 70% | 18% | 100% | 334 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B C B | 22,251 | 33,790 | 66.2 | 78% | 15% | 100% | 1,098 KB | 1 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,063 | 32,529 | 62.7 | 40% | 42% | 86% | 20,146 KB | 1 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B D B | 20,920 | 38,029 | 42.2 | 61% | 20% | 100% | 861 KB | 4 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B B D | 20,778 | 52,410 | 0.0 | 82% | 62% | – | 450 KB | 2 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E D | 20,772 | 100,817 | 0.0 | 52% | 6% | 31% | 5,368 KB | 449 (+1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B F B | 20,057 | 35,149 | 12.8 | 58% | 0% | 72% | 396 KB | 2 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | C E B | 19,617 | 41,961 | 63.3 | 46% | 3% | 99% | 3,196 KB | 81 (+5) |
| [arul28/ADE](https://github.com/arul28/ADE) | C E C | 19,506 | 29,201 | 17.5 | 43% | 45% | 96% | 8,727 KB | 140 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 19,486 | 95,981 | 35.3 | 52% | 20% | 62% | 349 KB | 1 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C B B | 19,295 | 25,522 | 0.0 | 86% | 52% | 95% | 223 KB | 121 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | C F B | 18,382 | 33,722 | 40.6 | 29% | 43% | 82% | 3,552 KB | 2,114 (+4) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C B B | 17,329 | 200,579 | 51.6 | 81% | 36% | 92% | 1,460 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C F A | 16,994 | 23,677 | 19.4 | 46% | 0% | 88% | 281 KB | 0 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C E B | 16,414 | 29,376 | 27.6 | 76% | 4% | 98% | 1,925 KB | 3 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C C | 16,321 | 25,282 | 30.2 | 73% | 62% | 66% | 102 KB | 233 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | C E B | 16,200 | 24,777 | 35.1 | 56% | 23% | 99% | 200 KB | 0 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C B C | 15,811 | 43,323 | 0.0 | 81% | 55% | 50% | 563 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 15,810 | 17,605 | 0.0 | 87% | 13% | 35% | 1,592 KB | 37 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 15,733 | 20,941 | 0.0 | 76% | 29% | 5% | 404 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C C D | 15,117 | 99,597 | 1.9 | 70% | 5% | 0% | 6,837 KB | 1 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 14,415 | 17,898 | 24.2 | 53% | 24% | 100% | 198 KB | 34 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 14,293 | 19,428 | 34.5 | 75% | 55% | 95% | 201 KB | 6 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C C | 14,136 | 35,086 | 18.5 | 78% | 36% | 68% | 149 KB | 4 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | C F B | 13,910 | 13,931 | 19.1 | 50% | 16% | 94% | 158 KB | 1 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 13,902 | 29,670 | 13.7 | 19% | 10% | – | 116 KB | 2 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 13,679 | 38,277 | 0.0 | 71% | 44% | – | 1,143 KB | 2 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 13,655 | 86,739 | 26.1 | 46% | 54% | 97% | 513 KB | 21 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C C D | 13,629 | 45,247 | 72.6 | 71% | 13% | – | 452 KB | 3 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C F B | 13,567 | 13,842 | 15.0 | 62% | 0% | 98% | 574 KB | 13 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | C C B | 13,341 | 18,796 | 24.2 | 76% | 27% | 89% | 158 KB | 5 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 12,994 | 27,261 | 151 | 35% | 21% | 100% | 233 KB | 20 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | C F B | 12,965 | 34,582 | 60.2 | 5% | 5% | 85% | 413 KB | 87 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 12,944 | 21,230 | 8.6 | 0% | 49% | 97% | 493 KB | 142 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 12,628 | 24,590 | 95.6 | 22% | 40% | 76% | 391 KB | 73 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C C C | 12,422 | 19,105 | 16.6 | 74% | 59% | 100% | 4,357 KB | 15 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C E D | 11,975 | 343,436 | 0.0 | 59% | 4% | 0% | 3,286 KB | 1 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 11,129 | 28,154 | 8.1 | 14% | 4% | 95% | 585 KB | 19 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 11,018 | 23,675 | 30.0 | 51% | 13% | 100% | 451 KB | 9 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C F B | 10,670 | 21,807 | 14.4 | 34% | 16% | 80% | 1,244 KB | 13 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 10,583 | 28,029 | 66.8 | 51% | 50% | 71% | 275 KB | 6,576 (+3) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C D B | 10,503 | 70,164 | 32.5 | 65% | 56% | 92% | 1,431 KB | 70,849 (+19) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C C B | 10,278 | 15,161 | 48.1 | 72% | 62% | 97% | 889 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 10,094 | 40,109 | 26.6 | 50% | 22% | 99% | 1,118 KB | 38 (+1) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C B D | 10,092 | 14,335 | 11.5 | 81% | 8% | 0% | 227 KB | 9 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D C B | 9,654 | 15,219 | 42.5 | 76% | 62% | 99% | 217 KB | 9 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 9,612 | 14,419 | 0.0 | 84% | 33% | 84% | 344 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | D B C | 9,602 | 20,312 | 27.1 | 86% | 62% | 94% | 363 KB | 11 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D D B | 9,552 | 15,883 | 106 | 61% | 28% | 91% | 5,238 KB | 82 (+1) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D F A | 9,101 | 25,746 | 0.0 | 55% | 0% | 92% | 254 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F C | 8,859 | 18,158 | 0.1 | 5% | 0% | 82% | 173 KB | 54 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 8,408 | 15,906 | 5.5 | 22% | 26% | 100% | 2,284 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | D F B | 8,386 | 19,762 | 7.1 | 52% | 0% | 90% | 941 KB | 2 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | D C A | 8,093 | 229,373 | 59.1 | 77% | 48% | 98% | 158 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | D F B | 7,841 | 7,619 | 6.2 | 25% | 0% | 95% | 385 KB | 1 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | D F C | 7,699 | 22,978 | 10.0 | 31% | 0% | 99% | 884 KB | 3 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 7,625 | 7,410 | 53.2 | 40% | 0% | – | 249 KB | 3 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | D F D | 7,411 | 13,949 | 12.4 | 31% | 31% | 45% | 144 KB | 16 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D D B | 7,368 | 22,477 | 20.2 | 60% | 37% | 98% | 617 KB | 1 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | D F B | 7,223 | 11,983 | 22.1 | 52% | 2% | 95% | 608 KB | 0 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | D D B | 7,026 | 11,444 | 26.9 | 62% | 22% | 99% | 698 KB | 2 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D E B | 7,008 | 8,610 | 27.9 | 75% | 0% | 78% | 59 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 6,652 | 23,224 | 38.1 | 81% | 34% | 100% | 2,359 KB | 5 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 6,590 | 9,546 | 46.5 | 28% | 31% | 91% | 158 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | D C C | 6,471 | 17,908 | 17.2 | 79% | 24% | 82% | 431 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D E D | 6,334 | 8,133 | 0.9 | 71% | 18% | 0% | 243 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 6,330 | 10,026 | 16.4 | 23% | 20% | 94% | 393 KB | 9 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 6,267 | 140,281 | 17.9 | 29% | 0% | 100% | 260 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D D B | 6,128 | 17,781 | 148 | 63% | 36% | 100% | 2,433 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,119 | 17,164 | 44.3 | 17% | 13% | 100% | 227 KB | 7 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D C B | 6,105 | 30,755 | 17.4 | 76% | 48% | 84% | 34 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D E A | 6,086 | 8,829 | 33.1 | 49% | 0% | 97% | 133 KB | 1 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D F C | 5,990 | 9,764 | 24.2 | 29% | 18% | 100% | 42 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D F B | 5,920 | 106,245 | 0.0 | 39% | 0% | 88% | 590 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F C | 5,901 | 56,285 | 30.3 | 9% | 0% | 65% | 220 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | D F B | 5,807 | 6,129 | 7.9 | 7% | 0% | 99% | 59 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D D B | 5,661 | 6,622 | 15.6 | 67% | 15% | 99% | 603 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 5,546 | 12,163 | 19.9 | 14% | 28% | 100% | 310 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | D F B | 5,367 | 31,591 | 5.4 | 9% | 0% | 88% | 2,636 KB | 43 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | D E C | 5,305 | 9,424 | 0.0 | 43% | 7% | 91% | 948 KB | 51 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,969 | 6,389 | 14.3 | 56% | 8% | 97% | 152 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 4,933 | 8,428 | 18.5 | 34% | 35% | – | 65 KB | 3 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E C B | 4,734 | 8,746 | 18.7 | 77% | 32% | 99% | 258 KB | 4 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E E B | 4,601 | 46,404 | 46.0 | 58% | 0% | 100% | 251 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | E C A | 4,520 | 6,005 | 73.1 | 86% | 12% | 96% | 40 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 4,487 | 8,163 | 4.2 | 32% | 15% | 83% | 4,103 KB | 559 (+2) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 4,431 | 15,149 | 21.0 | 57% | 0% | 96% | 1,414 KB | 0 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 4,344 | 4,960 | 12.4 | 24% | 36% | 98% | 544 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 4,341 | 5,234 | 22.6 | 15% | 13% | 97% | 163 KB | 6 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 4,312 | 11,042 | 26.6 | 71% | 0% | 100% | 628 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | E F C | 4,208 | 12,235 | 22.8 | 44% | 7% | 100% | 374 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | E F A | 4,190 | 5,299 | 14.3 | 17% | 0% | 97% | 225 KB | 5 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 4,156 | 23,799 | 48.5 | 3% | 9% | 100% | 605 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 4,115 | 5,682 | 0.0 | 50% | 54% | 70% | 393 KB | 3 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E B B | 4,109 | 16,703 | 35.0 | 80% | 38% | 100% | 36 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E E C | 4,086 | 59,885 | 15.6 | 55% | 20% | 94% | 393 KB | 2 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,059 | 6,021 | 35.1 | 57% | 0% | 95% | 107 KB | 3 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,944 | 4,543 | 0.1 | 16% | 18% | 86% | 1,101 KB | 2 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 3,828 | 21,101 | 12.4 | 50% | 44% | 94% | 457 KB | 25 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 3,743 | 3,397 | 12.6 | 33% | 29% | 95% | 266 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | E F B | 3,701 | 8,617 | 26.4 | 22% | 25% | 99% | 603 KB | 2 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E F C | 3,642 | 3,766 | 37.3 | 39% | 41% | 100% | 855 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E E B | 3,641 | 8,447 | 45.3 | 56% | 31% | 100% | 1,426 KB | 8 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 3,625 | 21,635 | 19.6 | 17% | 0% | 96% | 1,129 KB | 49 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 3,591 | 9,568 | 7.1 | 48% | 0% | 73% | 299 KB | 348 (+2) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,567 | 5,789 | 23.9 | 28% | 58% | 100% | 387 KB | 18 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,536 | 125,500 | 6.0 | 38% | 4% | 73% | 125 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,501 | 7,340 | 11.0 | 59% | 0% | 82% | 151 KB | 0 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 3,444 | 5,166 | 22.9 | 45% | 0% | 98% | 321 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 3,401 | 15,475 | 0.0 | 3% | 12% | 94% | 674 KB | 2 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 3,381 | 61,878 | 4.9 | 25% | 0% | 84% | 23 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F C | 3,375 | 5,728 | 1.3 | 31% | 0% | 76% | 83 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 3,317 | 7,438 | 0.0 | 11% | 24% | 0% | 1,273 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 3,303 | 6,746 | 12.6 | 32% | 10% | 83% | 350 KB | 176 (+2) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E E B | 3,251 | 6,424 | 10.6 | 54% | 32% | 99% | 518 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | E F C | 3,219 | 4,466 | 23.8 | 5% | 45% | 94% | 737 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,185 | 4,670 | 15.8 | 41% | 10% | 99% | 386 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E E C | 3,135 | 6,317 | 48.0 | 45% | 27% | 99% | 598 KB | 5 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,116 | 6,894 | 9.4 | 12% | 27% | 93% | 378 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 3,113 | 22,102 | 0.0 | 30% | 0% | – | 209 KB | 30 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E C B | 3,092 | 4,263 | 18.9 | 72% | 0% | 96% | 93 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 3,046 | 165,158 | 0.0 | 40% | 0% | – | 8,190 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 2,997 | 8,840 | 20.1 | 0% | 0% | 99% | 243 KB | 9 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,974 | 13,911 | 0.0 | 32% | 0% | 97% | 568 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E E C | 2,871 | 4,287 | 13.0 | 70% | 0% | 98% | 165 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,860 | 5,077 | 9.2 | 49% | 0% | 99% | 221 KB | 7 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | E F C | 2,834 | 14,618 | 20.7 | 15% | 0% | 95% | 599 KB | 22 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 2,644 | 3,900 | 22.3 | 60% | 0% | 76% | 1,719 KB | 6 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,640 | 3,764 | 33.5 | 78% | 16% | – | 454 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E F B | 2,556 | 6,279 | 17.8 | 45% | 0% | 90% | 422 KB | 2 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 2,461 | 6,551 | 15.8 | 2% | 0% | 98% | 541 KB | 93 (+2) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,414 | 4,549 | 20.5 | 7% | 23% | 84% | 312 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E E C | 2,405 | 4,417 | 13.8 | 65% | 0% | 100% | 168 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,390 | 8,176 | 6.1 | 26% | 0% | 98% | 550 KB | 12 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 2,294 | 7,320 | 20.0 | 38% | 44% | 84% | 540 KB | 10 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | E E C | 2,263 | 141,156 | 16.4 | 60% | 0% | 66% | 324 KB | 40,789 (+25) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 2,220 | 3,785 | 8.3 | 55% | 0% | 84% | 6,579 KB | 8 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 2,198 | 7,528 | 0.0 | 66% | 0% | – | 202 KB | 5 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E A C | 2,096 | 6,894 | 0.0 | 95% | 90% | 99% | 2,051 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 2,044 | 6,868 | 9.0 | 37% | 18% | 99% | 356 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E D D | 2,012 | 9,602 | 0.0 | 60% | 12% | 42% | 268 KB | 0 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E F C | 2,009 | 1,907 | 30.0 | 18% | 44% | 98% | 512 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,003 | 5,193 | 20.2 | 4% | 8% | 96% | 169 KB | 13 (+1) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E E D | 1,982 | 19,371 | 0.0 | 57% | 33% | 6% | 158 KB | 119 (+1) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E E D | 1,924 | 4,795 | 0.1 | 49% | 0% | 0% | 601 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 1,860 | 6,702 | 24.8 | 35% | 18% | 97% | 100 KB | 4 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F D | 1,842 | 4,336 | 16.3 | 59% | 0% | – | 645 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,839 | 4,746 | 1.1 | 43% | 38% | 96% | 5,635 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 1,825 | 59,995 | 48.5 | 40% | 0% | 92% | 627 KB | 2 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E E E | 1,796 | 52,560 | 0.0 | 56% | 15% | 24% | 183 KB | 1 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 1,796 | 11,692 | 0.0 | 3% | 0% | 0% | 255 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,725 | 2,774 | 4.5 | 31% | 0% | 99% | 168 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,672 | 9,137 | 24.0 | 9% | 46% | 99% | 363 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 1,625 | 45,058 | 3.1 | 34% | 0% | 100% | 1,446 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 1,612 | 2,731 | 7.8 | 62% | 0% | 94% | 236 KB | 5 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,594 | 2,561 | 0.0 | 0% | 20% | 76% | 293 KB | 0 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,586 | 6,283 | 8.8 | 0% | 0% | 89% | 105 KB | 3 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 1,549 | 4,266 | 5.7 | 42% | 0% | – | 415 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 1,534 | 1,580 | 24.3 | 0% | 0% | 86% | 67 KB | 63 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,518 | 4,175 | 14.2 | 34% | 0% | 99% | 43 KB | 2 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,514 | 1,642 | 0.0 | 0% | 0% | 33% | 402 KB | 465 (+1) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,488 | 3,913 | 26.5 | 27% | 0% | 88% | 996 KB | 119 (+1) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E F B | 1,482 | 2,959 | 28.3 | 48% | 14% | 99% | 578 KB | 2 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,467 | 9,101 | 0.0 | 46% | 32% | – | 1,007 KB | 1 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,439 | 2,458 | 13.2 | 29% | 0% | 99% | 69 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,344 | 21,216 | 3.6 | 67% | 0% | 99% | 1,182 KB | 6 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 1,281 | 3,824 | 26.8 | 14% | 0% | 97% | 49 KB | 23,899 (+9) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F A | 1,209 | 8,321 | 19.5 | 8% | 0% | 92% | 315 KB | 159 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 1,142 | 6,583 | 6.6 | 0% | 0% | 93% | 730 KB | 9 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,140 | 2,179 | 40.1 | 34% | 0% | 95% | 568 KB | 2 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,128 | 1,812 | 40.9 | 8% | 0% | 100% | 704 KB | 13 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | E F B | 1,120 | 6,639 | 16.2 | 46% | 0% | 99% | 1,138 KB | 8 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 1,119 | 4,154 | 0.1 | 0% | 0% | 16% | 376 KB | 1 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 1,049 | 5,532 | 15.0 | 5% | 0% | 99% | 215 KB | 1 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 1,026 | 1,337 | 10.0 | 0% | 0% | 91% | 458 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | E F D | 1,020 | 2,686 | 0.0 | 57% | 0% | – | 80 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F E C | 909 | 1,402 | 11.4 | 64% | 9% | 100% | 86 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 834 | 9,740 | 16.2 | 38% | 16% | 99% | 634 KB | 11 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | F F B | 799 | 1,771 | 12.4 | 0% | 30% | 97% | 106 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 786 | 4,379 | 10.9 | 52% | 0% | 100% | 1,072 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 751 | 2,160 | 39.3 | 35% | 0% | 98% | 974 KB | 2 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 631 | 1,454 | 0.0 | 30% | 0% | 0% | 671 KB | 3 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F B | 610 | 1,632 | 10.2 | 0% | 0% | 82% | 274 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 606 | 2,131 | 9.6 | 23% | 0% | 99% | 87 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 583 | 882 | 10.5 | 52% | 46% | 95% | 457 KB | 14 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | 408 | 5,954 | 0.0 | 26% | 0% | – | 406 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 400 | 71,943 | 106 | 45% | 0% | 96% | 378 KB | 4 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 353 | 3,990 | 43.5 | 0% | 0% | 100% | 184 KB | 2 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 343 | 2,069 | 19.6 | 27% | 0% | 100% | 126 KB | 0 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 333 | 582 | 3.6 | 0% | 0% | – | 710 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F E B | 316 | 4,295 | 14.9 | 46% | 0% | 98% | 911 KB | 0 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 301 | 1,386 | 17.1 | 0% | 0% | 98% | 1,116 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 248 | 1,282 | 24.9 | 41% | 0% | 99% | 1,060 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 227 | 1,995 | 7.3 | 0% | 0% | 100% | 45 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 219 | 484 | 16.8 | 58% | 0% | 76% | 16 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 218 | 1,086 | 9.8 | 38% | 0% | 98% | 477 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 210 | 827 | 0.0 | 25% | 0% | 72% | 554 KB | 28 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 173 | 848 | 4.2 | 0% | 0% | 98% | 104 KB | 4 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 167 | 745 | 7.9 | 0% | 0% | 100% | 104 KB | 248 (-1) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | F F C | 163 | 3,303 | 10.6 | 36% | 0% | 71% | 1,031 KB | 2 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | 150 | 10,386 | 22.6 | 18% | 0% | 100% | 192 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 107 | 2,293 | 5.1 | 22% | 0% | 99% | 569 KB | 1 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 87 | 1,854 | 13.1 | 40% | 0% | 100% | 355 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 81 | 88,814 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 791 | 12.2 | 0% | 0% | 26% | 7,014 KB | 20 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 61 | 178,537 | 40.9 | 2% | 0% | 96% | 3,975 KB | 1 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 60 | 13,515 | 8.2 | 28% | 0% | 92% | 149 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 53 | 321 | 6.9 | 0% | 0% | 61% | 642 KB | 5 (+1) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 35 | 951 | 5.5 | 20% | 0% | 65% | 46 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 33 | 631 | 7.2 | 44% | 0% | 100% | 156 KB | 2 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 18 | 4,487 | 1.5 | 0% | 0% | 100% | 52 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 15 | 780 | 4.9 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 3 | 324 | 0.0 | 0% | 0% | 100% | 470 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 2 | 443 | 18.0 | 0% | 0% | 96% | 270 KB | 0 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F C B | – | – | 58.4 | 80% | 71% | 92% | 887 KB | 12 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 364 | 40.6 | 0% | 0% | 93% | 137 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F A | 0 | 2,807 | 32.3 | 0% | 0% | 91% | 169 KB | 2 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 31.6 | – | – | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 27.6 | 63% | 43% | 89% | 2,290 KB | 1,522 (+8) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 28,444 | 25.0 | 0% | 0% | 79% | 416 KB | 9 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F E B | 0 | 0 | 24.2 | 59% | 0% | 97% | 405 KB | 1,632 (+1) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 0 | 2,539 | 22.4 | 0% | 0% | 95% | 567 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 21.5 | – | – | 53% | 3,052 KB | 2 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | F F B | 0 | 0 | 21.3 | 16% | 5% | 96% | 634 KB | 48 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 20.0 | 59% | 0% | 100% | 154 KB | 4 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 0 | 158 | 18.7 | 0% | 0% | 99% | 98 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 169 | 18.3 | 0% | 0% | 95% | 249 KB | 0 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 18.0 | 31% | 23% | 97% | 1,038 KB | 4 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 779 | 17.3 | 0% | 0% | 100% | 25 KB | 19 (+1) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 163 | 16.7 | 0% | 0% | 95% | 123 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 390 | 16.5 | 0% | 0% | 76% | 336 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 15.5 | – | – | 91% | 306 KB | 7 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 14.0 | 63% | 8% | 81% | 86 KB | 7 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 13.7 | – | – | 100% | 41 KB | 2 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 13.5 | – | – | 100% | 403 KB | 2 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 846 | 13.2 | 0% | 0% | 92% | 1,170 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 234 | 13.1 | 50% | 0% | 0% | 348 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 12.3 | 0% | 0% | 0% | 206 KB | 0 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | – | – | 12.1 | – | – | 99% | 504 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 0 | 0 | 10.9 | – | – | 100% | 160 KB | 2 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 10.6 | – | – | 99% | 80 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 0 | 10.6 | 56% | 0% | 85% | 263 KB | 1,255 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 1 | 10.0 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 4,193 | 9.9 | 17% | 0% | 100% | 95 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 0 | 9.0 | 0% | 0% | 96% | 99 KB | 1 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 8.3 | – | – | 95% | 8,119 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 0 | 48 | 7.9 | 0% | 0% | 80% | 27 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 1,045 | 7.1 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | F F B | 0 | 638 | 6.9 | 0% | 0% | 100% | 4,314 KB | 33 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 0 | 0 | 6.8 | 0% | 0% | 89% | 682 KB | 6 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 3,052 | 6.8 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 2,797 | 6.6 | 6% | 0% | 0% | 285 KB | 25 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | – | – | 6.4 | – | – | 99% | 127 KB | 24 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | – | – | 6.2 | – | – | – | 100 KB | 0 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 0 | 66 | 6.2 | 0% | 0% | 80% | 83 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 11,728 | 6.2 | 0% | 0% | 87% | 489 KB | 86 (+1) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 6.1 | – | – | 98% | 363 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 358 | 5.7 | 0% | 0% | 97% | 663 KB | 2 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 1,043 | 5.5 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 0 | 5.2 | – | – | 88% | 739 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 5.1 | – | – | 93% | 576 KB | 1 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 5.1 | 12% | 0% | 88% | 700 KB | 4 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 0 | 2,279 | 4.4 | 20% | 0% | 96% | 697 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | – | – | 4.3 | – | – | 97% | 43 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 1,629 | 4.0 | 0% | 0% | 88% | 162 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 1,010 | 3.9 | 20% | 0% | 87% | 602 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 2 | 3.9 | 0% | 0% | 90% | 163 KB | 14 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 3.4 | – | – | 96% | 122 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 3.0 | – | – | – | 311 KB | 4 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | – | – | 2.6 | – | – | 90% | 319 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 169 | 2.1 | 0% | 0% | 88% | 591 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 2,536 | 1.6 | 56% | 0% | – | 201 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 1.5 | – | – | 98% | 231 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 1.1 | – | – | 90% | 195 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 1.0 | – | – | 99% | 73 KB | 3 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 0.9 | – | – | 98% | 723 KB | 5 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 0 | 0 | 0.8 | 0% | 0% | – | 53 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | – | – | 0.8 | – | – | – | 56 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.6 | 53% | 39% | 0% | 2,040 KB | 461 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.4 | – | – | 98% | 42 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.3 | – | – | 100% | 59 KB | 1 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 107 | 0.2 | 0% | 0% | 20% | 154 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 51% | 17% | 96% | 846 KB | 7 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.2 | – | – | 0% | 518 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F D | 0 | 14,205 | 0.1 | 63% | 0% | 90% | 1,468 KB | 1,118 (-1) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 0.1 | – | – | – | 115 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,327 (+4) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F B | – | – | 0.1 | 32% | 18% | 70% | 88 KB | 5 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.1 | – | – | 69% | 290 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 190 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | 0 | 0 | 0.0 | 0% | 0% | 0% | 342 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 27 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 94 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 6,988 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | – | – | 0.0 | – | – | 30% | 308 KB | 811 (+4) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 0.0 | – | – | 99% | 298 KB | 5 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 87% | 77% | 94% | 38,763 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
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
