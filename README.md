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
_360 repos, last measured 2026-11-10. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (360)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A B C | 66,952 | 203,471 | 144 | 82% | 50% | 54% | 311 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 53,178 | 211,917 | 201 | 20% | 35% | 67% | 2,305 KB | 5 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A D A | 52,830 | 85,167 | 60.8 | 64% | 21% | 92% | 241 KB | 128 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A E C | 52,742 | 160,504 | 73.4 | 57% | 43% | 68% | 565 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A C A | 47,058 | 72,462 | 47.8 | 75% | 20% | 100% | 310 KB | 3 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B C B | 38,932 | 39,658 | 70.1 | 72% | 45% | 80% | 1,080 KB | 1 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B D D | 37,071 | 43,618 | 0.1 | 69% | 55% | 0% | 2,975 KB | 3 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B B B | 34,860 | 44,351 | 54.4 | 81% | 32% | 85% | 381 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B B B | 33,726 | 42,774 | 1.2 | 84% | 4% | 94% | 3,340 KB | 7 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B B D | 29,799 | 57,836 | 0.0 | 82% | 31% | – | 451 KB | 2 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | B E C | 29,372 | 32,971 | 33.4 | 57% | 18% | 99% | 195 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B D B | 28,935 | 52,359 | 12.9 | 65% | 16% | 72% | 396 KB | 2 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B D B | 27,424 | 35,160 | 23.5 | 66% | 27% | 97% | 405 KB | 1,629 (+7) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,086 | 32,380 | 25.6 | 76% | 44% | 99% | 669 KB | 6 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 26,467 | 36,313 | 26.9 | 26% | 55% | 100% | 1,723 KB | 138 (+14) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B E C | 25,926 | 28,746 | 17.4 | 40% | 14% | 97% | 8,727 KB | 139 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B F B | 25,502 | 47,325 | 55.7 | 48% | 6% | 75% | 410 KB | 87 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B F D | 24,168 | 97,710 | 0.0 | 38% | 4% | 43% | 5,368 KB | 446 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 24,138 | 41,964 | 41.3 | 72% | 52% | 100% | 841 KB | 4 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C B | 23,475 | 222,671 | 42.8 | 73% | 34% | 97% | 1,436 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | B C D | 23,426 | 55,306 | 0.0 | 75% | 31% | – | 1,019 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B F B | 23,080 | 29,539 | 20.5 | 28% | 16% | 85% | 781 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B E D | 21,938 | 45,582 | 35.8 | 50% | 5% | 25% | 822 KB | 16 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B C B | 21,274 | 32,682 | 0.0 | 73% | 59% | 87% | 223 KB | 120 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B F B | 21,107 | 33,582 | 50.4 | 57% | 35% | 97% | 3,391 KB | 2,106 (+1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C D C | 19,176 | 181,162 | 35.3 | 62% | 20% | 62% | 277 KB | 1 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C E D | 19,080 | 58,492 | 71.2 | 74% | 0% | – | 448 KB | 3 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F B | 17,761 | 18,216 | 0.0 | 70% | 36% | 84% | 329 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C C C | 17,163 | 27,213 | 28.0 | 77% | 61% | 86% | 363 KB | 11 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D C | 16,661 | 29,034 | 30.4 | 62% | 55% | 60% | 102 KB | 233 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C F D | 16,515 | 26,379 | 14.8 | 47% | 44% | 42% | 142 KB | 16 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 16,367 | 32,782 | 28.4 | 70% | 28% | 96% | 1,884 KB | 3 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B D | 15,556 | 22,260 | 0.0 | 87% | 31% | 16% | 359 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 15,545 | 29,594 | 8.5 | 4% | 8% | 96% | 552 KB | 19 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C C A | 14,924 | 49,944 | 50.4 | 80% | 38% | 100% | 403 KB | 0 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C D C | 14,835 | 21,999 | 0.0 | 70% | 50% | 100% | 4,357 KB | 15 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 14,758 | 20,031 | 95.6 | 45% | 35% | 76% | 390 KB | 73 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 14,584 | 30,355 | 66.4 | 43% | 51% | 88% | 275 KB | 6,568 (+4) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,566 | 26,788 | 8.8 | 4% | 23% | 98% | 483 KB | 142 (+2) |
| [alexec/Agents](https://github.com/alexec/Agents) | C E D | 14,563 | 29,205 | 61.4 | 44% | 46% | 90% | 20,146 KB | 1 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 14,473 | 22,526 | 34.7 | 85% | 50% | 97% | 200 KB | 6 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C D B | 14,136 | 34,152 | 17.5 | 68% | 37% | 72% | 144 KB | 4 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,689 | 15,772 | 24.0 | 76% | 54% | 100% | 197 KB | 34 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C D D | 13,679 | 30,396 | 0.0 | 60% | 49% | – | 1,127 KB | 2 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C D C | 13,271 | 79,831 | 26.8 | 63% | 57% | 99% | 510 KB | 21 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | C F C | 13,223 | 21,095 | 0.1 | 6% | 0% | 84% | 173 KB | 54 (-6) |
| [goat-si/goat](https://github.com/goat-si/goat) | C F B | 13,147 | 38,223 | 60.1 | 24% | 4% | 98% | 3,196 KB | 71 (+27) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 13,031 | 36,802 | 149 | 32% | 20% | 98% | 233 KB | 19 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 12,836 | 21,541 | 42.2 | 12% | 11% | 100% | 225 KB | 7 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | C F B | 12,814 | 35,697 | 10.4 | 5% | 26% | 88% | 2,636 KB | 42 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 12,813 | 26,402 | 12.3 | 25% | 13% | – | 108 KB | 2 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 12,727 | 30,821 | 30.4 | 49% | 0% | 100% | 470 KB | 9 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C D B | 11,983 | 54,451 | 29.9 | 63% | 25% | 97% | 1,142 KB | 37 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C F B | 11,624 | 14,651 | 16.1 | 55% | 0% | 98% | 461 KB | 13 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C F A | 11,024 | 28,734 | 0.0 | 50% | 0% | 92% | 254 KB | 0 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 10,887 | 103,227 | 0.0 | 70% | 48% | 50% | 563 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 10,678 | 18,270 | 5.2 | 10% | 35% | 100% | 2,284 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 10,670 | 11,649 | 13.0 | 71% | 27% | 85% | 1,243 KB | 13 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 10,453 | 17,482 | 0.0 | 81% | 43% | 49% | 1,587 KB | 36 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C C B | 10,265 | 16,040 | 52.3 | 70% | 53% | 100% | 871 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | D F D | 9,682 | 206,434 | 0.0 | 29% | 0% | 0% | 3,286 KB | 1 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D B B | 9,552 | 16,650 | 97.6 | 82% | 30% | 85% | 4,886 KB | 80 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 9,177 | 13,162 | 15.7 | 34% | 0% | 92% | 383 KB | 9 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 8,894 | 35,713 | 0.0 | 0% | 0% | – | 203 KB | 30 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 8,829 | 9,568 | 13.8 | 83% | 0% | 98% | 165 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 8,766 | 13,080 | 38.7 | 67% | 60% | 97% | 216 KB | 9 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D E B | 8,750 | 18,836 | 16.0 | 65% | 29% | 99% | 258 KB | 4 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D D B | 8,609 | 14,661 | 33.5 | 67% | 49% | 82% | 1,438 KB | 70,803 (+16) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | D E B | 8,477 | 13,557 | 3.3 | 55% | 15% | 86% | 263 KB | 1,254 (+1) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D E F | 8,161 | 244,324 | 0.0 | 46% | 13% | – | 8,190 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D E B | 7,813 | 8,708 | 14.8 | 81% | 35% | 100% | 518 KB | 0 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D C B | 7,654 | 40,630 | 16.4 | 75% | 34% | 84% | 32 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 7,047 | 25,452 | 18.1 | 41% | 42% | 99% | 617 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 7,012 | 12,754 | 10.5 | 76% | 9% | 0% | 227 KB | 9 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 6,919 | 11,535 | 19.6 | 13% | 0% | 98% | 225 KB | 5 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | D D A | 6,774 | 203,376 | 56.4 | 65% | 50% | 98% | 158 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | D F C | 6,666 | 130,902 | 106 | 50% | 1% | 81% | 378 KB | 3 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 6,660 | 21,659 | 23.3 | 25% | 7% | 98% | 634 KB | 48 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 6,652 | 22,699 | 37.0 | 88% | 38% | 100% | 2,291 KB | 5 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D D D | 6,642 | 9,604 | 0.9 | 69% | 14% | 0% | 242 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | D E C | 6,626 | 16,769 | 25.7 | 42% | 23% | 100% | 322 KB | 0 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D D B | 6,615 | 11,492 | 22.6 | 70% | 18% | 95% | 158 KB | 5 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 6,409 | 97,578 | 18.6 | 42% | 0% | 100% | 259 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D F B | 6,290 | 16,758 | 158 | 47% | 3% | 100% | 2,419 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | D E D | 6,096 | 46,232 | 1.3 | 44% | 5% | 0% | 3,638 KB | 1 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D F B | 6,092 | 7,281 | 31.3 | 62% | 0% | 99% | 1,060 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D E B | 6,074 | 8,225 | 44.6 | 60% | 36% | 73% | 335 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D F A | 6,071 | 9,323 | 34.0 | 41% | 7% | 97% | 131 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D E B | 6,018 | 18,345 | 20.6 | 46% | 6% | 98% | 911 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F A | 5,999 | 42,710 | 25.9 | 0% | 30% | 100% | 380 KB | 49 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D F B | 5,920 | 108,230 | 0.0 | 50% | 0% | 88% | 590 KB | 1 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | D C C | 5,748 | 51,806 | 32.0 | 73% | 12% | 95% | 538 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | D F D | 5,713 | 42,179 | 0.1 | 39% | 0% | 90% | 1,468 KB | 1,120 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D D B | 5,621 | 8,808 | 42.6 | 62% | 18% | 100% | 1,401 KB | 8 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 5,523 | 10,711 | 18.3 | 33% | 41% | 97% | 303 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | D F B | 5,421 | 17,776 | 20.5 | 12% | 43% | 80% | 312 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 5,370 | 8,095 | 49.8 | 52% | 0% | – | 233 KB | 3 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,352 | 18,325 | 7.1 | 0% | 0% | 87% | 489 KB | 79 (+20) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D F D | 5,290 | 7,552 | 15.2 | 23% | 0% | – | 633 KB | 2 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D F B | 5,227 | 7,734 | 14.1 | 20% | 26% | 92% | 135 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 5,227 | 15,841 | 0.0 | 53% | 0% | 97% | 562 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | D F B | 5,188 | 11,912 | 26.2 | 20% | 23% | 99% | 600 KB | 2 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D E C | 5,156 | 9,251 | 0.0 | 58% | 34% | 63% | 390 KB | 3 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D C B | 5,121 | 6,163 | 14.5 | 82% | 54% | 100% | 596 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 4,993 | 11,822 | 29.2 | 53% | 46% | 100% | 628 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | E F B | 4,925 | 6,126 | 6.6 | 40% | 0% | 96% | 385 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,758 | 8,986 | 9.3 | 13% | 29% | 93% | 376 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E B | 4,676 | 8,394 | 27.7 | 78% | 0% | 78% | 59 KB | 1 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 4,670 | 9,444 | 18.9 | 11% | 0% | 100% | 541 KB | 89 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 4,622 | 5,449 | 12.8 | 14% | 5% | 98% | 544 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 4,582 | 7,183 | 0.0 | 31% | 0% | – | 403 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,556 | 6,243 | 12.9 | 26% | 9% | 95% | 151 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | E E A | 4,520 | 6,656 | 78.7 | 71% | 13% | 100% | 40 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 4,505 | 7,285 | 1.3 | 19% | 0% | 76% | 66 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 4,467 | 5,353 | 16.9 | 34% | 43% | – | 65 KB | 3 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F C | 4,419 | 56,102 | 28.4 | 11% | 0% | 50% | 191 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 4,389 | 15,110 | 16.6 | 77% | 19% | 74% | 527 KB | 0 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E E B | 4,352 | 6,418 | 34.9 | 55% | 0% | 98% | 100 KB | 3 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | E F C | 4,338 | 6,520 | 22.2 | 4% | 32% | 89% | 737 KB | 1 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 4,306 | 7,390 | 21.1 | 30% | 3% | 88% | 608 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 4,156 | 23,514 | 49.4 | 7% | 14% | 100% | 605 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 4,101 | 11,094 | 6.2 | 64% | 0% | 99% | 550 KB | 12 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | E F B | 4,096 | 6,098 | 53.5 | 28% | 0% | 98% | 974 KB | 2 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 4,096 | 6,359 | 15.7 | 41% | 0% | 99% | 42 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 4,058 | 4,710 | 0.1 | 5% | 16% | 86% | 1,101 KB | 2 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 3,751 | 48,288 | 21.6 | 45% | 0% | 95% | 1,414 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 3,743 | 4,037 | 13.4 | 38% | 18% | 100% | 260 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 3,740 | 38,823 | 40.7 | 51% | 0% | 96% | 219 KB | 1 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E D C | 3,713 | 6,463 | 37.9 | 64% | 37% | 99% | 837 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E E B | 3,655 | 7,475 | 12.9 | 40% | 13% | 90% | 345 KB | 172 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 3,604 | 4,859 | 26.1 | 62% | 0% | 100% | 313 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 3,560 | 7,205 | 9.9 | 59% | 0% | 83% | 6,579 KB | 8 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,536 | 125,891 | 8.4 | 35% | 3% | 73% | 131 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 3,458 | 11,024 | 8.0 | 50% | 0% | 74% | 299 KB | 344 (+2) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,396 | 6,150 | 25.1 | 30% | 44% | 100% | 386 KB | 18 (+1) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 3,382 | 38,290 | 4.4 | 38% | 0% | 84% | 23 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 3,380 | 29,815 | 13.2 | 43% | 37% | 95% | 399 KB | 25 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 3,323 | 4,082 | 6.0 | 36% | 0% | 98% | 569 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F A | 3,240 | 5,187 | 38.2 | 34% | 0% | 91% | 169 KB | 2 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E D E | 3,228 | 12,086 | 24.1 | 66% | 44% | 76% | 1,719 KB | 6 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E B B | 3,136 | 10,832 | 31.9 | 84% | 52% | 98% | 33 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E E B | 3,125 | 8,341 | 7.6 | 65% | 23% | 100% | 212 KB | 7 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 3,105 | 5,085 | 25.7 | 27% | 12% | 96% | 163 KB | 6 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E E B | 3,092 | 4,697 | 19.2 | 70% | 0% | 97% | 93 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E F B | 3,053 | 7,243 | 8.0 | 38% | 0% | 98% | 54 KB | 0 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E F B | 3,017 | 5,727 | 22.9 | 60% | 0% | 100% | 623 KB | 2 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | E F C | 2,834 | 15,596 | 21.5 | 11% | 0% | 100% | 599 KB | 22 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 2,833 | 5,419 | 25.6 | 15% | 29% | 100% | 42 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 2,821 | 9,288 | 16.2 | 60% | 0% | 99% | 215 KB | 1 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 2,742 | 14,273 | 0.0 | 14% | 8% | 87% | 674 KB | 2 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 2,720 | 3,468 | 4.9 | 39% | 0% | 100% | 166 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E E D | 2,695 | 3,910 | 38.9 | 61% | 15% | – | 440 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,655 | 4,171 | 0.0 | 10% | 0% | 33% | 402 KB | 463 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 2,558 | 6,155 | 21.3 | 0% | 0% | 99% | 240 KB | 9 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E F B | 2,556 | 5,163 | 16.1 | 60% | 0% | 91% | 408 KB | 2 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E B C | 2,553 | 7,109 | 0.0 | 85% | 80% | 100% | 2,016 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,477 | 5,803 | 15.6 | 25% | 7% | 99% | 386 KB | 2 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 2,457 | 14,207 | 20.8 | 66% | 46% | 84% | 540 KB | 10 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,428 | 6,215 | 0.0 | 9% | 5% | 0% | 1,273 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 2,409 | 14,527 | 6.2 | 29% | 0% | 93% | 941 KB | 2 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 2,363 | 10,194 | 0.0 | 58% | 13% | 42% | 267 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 2,280 | 8,082 | 0.0 | 2% | 0% | 67% | 948 KB | 50 (+2) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E E C | 2,192 | 6,157 | 5.1 | 42% | 10% | 83% | 4,075 KB | 556 (+1) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,142 | 2,751 | 19.1 | 0% | 28% | 97% | 104 KB | 1 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 2,130 | 3,313 | 0.0 | 14% | 25% | 76% | 292 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E E C | 2,052 | 5,085 | 45.6 | 43% | 30% | 99% | 593 KB | 5 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 1,982 | 51,390 | 0.0 | 27% | 8% | 21% | 158 KB | 117 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | E F C | 1,964 | 15,563 | 15.2 | 67% | 0% | 67% | 5,040 KB | 40,712 (+26) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E F E | 1,887 | 28,530 | 0.0 | 29% | 0% | 88% | 153 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E E E | 1,885 | 8,016 | 11.4 | 65% | 0% | 100% | 1,072 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 1,853 | 3,436 | 26.6 | 0% | 0% | 92% | 49 KB | 23,868 (+6) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 1,851 | 8,719 | 11.6 | 32% | 0% | 99% | 399 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 1,849 | 5,544 | 12.3 | 19% | 0% | 90% | 458 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 1,843 | 7,951 | 11.6 | 56% | 0% | 93% | 151 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 1,825 | 33,499 | 55.9 | 34% | 0% | 92% | 627 KB | 2 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,810 | 8,754 | 0.0 | 65% | 19% | – | 1,001 KB | 1 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,786 | 12,923 | 24.0 | 6% | 32% | 99% | 363 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 1,775 | 4,068 | 26.4 | 8% | 0% | 96% | 99 KB | 4 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,770 | 6,183 | 8.6 | 40% | 6% | 100% | 355 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,751 | 3,642 | 53.1 | 16% | 19% | 95% | 564 KB | 2 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E F B | 1,751 | 3,665 | 30.2 | 61% | 9% | 98% | 578 KB | 2 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 1,654 | 36,218 | 0.0 | 0% | 4% | 0% | 290 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F C | 1,637 | 3,493 | 11.7 | 10% | 0% | 64% | 274 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 1,630 | 2,489 | 17.7 | 62% | 0% | 100% | 168 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,605 | 11,921 | 2.6 | 37% | 0% | 99% | 1,176 KB | 5 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,586 | 6,042 | 8.1 | 0% | 0% | 78% | 105 KB | 3 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,571 | 2,480 | 46.7 | 12% | 5% | 98% | 704 KB | 13 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E E C | 1,567 | 24,596 | 24.1 | 46% | 0% | 55% | 4,722 KB | 110 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 1,549 | 3,253 | 6.7 | 29% | 0% | – | 415 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F B | 1,534 | 1,987 | 28.4 | 0% | 0% | 80% | 67 KB | 63 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 1,471 | 2,465 | 30.8 | 46% | 30% | 96% | 512 KB | 0 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 1,471 | 5,033 | 0.1 | 6% | 0% | 35% | 376 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | E F D | 1,279 | 2,902 | 0.0 | 50% | 0% | – | 80 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F B | 1,224 | 5,353 | 21.8 | 25% | 29% | 100% | 126 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F C | 1,209 | 6,190 | 25.3 | 6% | 0% | 70% | 327 KB | 160 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 1,148 | 13,054 | 49.8 | 6% | 0% | 100% | 179 KB | 2 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 1,142 | 3,716 | 8.6 | 0% | 0% | 94% | 729 KB | 9 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | E F B | 1,120 | 9,777 | 19.7 | 48% | 0% | 99% | 1,126 KB | 8 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F C | 1,057 | 3,135 | 1.2 | 31% | 0% | 97% | 5,623 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 1,051 | 3,288 | 0.0 | 25% | 0% | – | 202 KB | 5 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 941 | 1,975 | 12.0 | 21% | 0% | 100% | 85 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 933 | 14,205 | 14.9 | 52% | 0% | 89% | 381 KB | 2 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 782 | 1,542 | 5.0 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 758 | 7,896 | 0.1 | 19% | 0% | 100% | 472 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | F F C | 733 | 2,123 | 14.4 | 67% | 0% | 79% | 998 KB | 2 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F C | 673 | 3,660 | 27.3 | 37% | 0% | 55% | 991 KB | 117 (+1) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 631 | 1,522 | 0.0 | 19% | 0% | 0% | 670 KB | 3 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 611 | 8,577 | 17.3 | 58% | 15% | 99% | 634 KB | 11 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 606 | 2,071 | 9.5 | 25% | 0% | 99% | 87 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 583 | 621 | 12.5 | 42% | 0% | 98% | 457 KB | 13 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | F F D | 579 | 5,049 | 0.1 | 4% | 0% | 0% | 601 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F D C | 570 | 6,641 | 5.9 | 67% | 0% | 95% | 697 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 473 | 6,133 | 20.5 | 0% | 12% | 97% | 166 KB | 12 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 460 | 14,491 | 6.1 | 15% | 0% | 99% | 883 KB | 3 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 401 | 1,074 | 13.9 | 18% | 0% | 99% | 65 KB | 1 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 301 | 2,092 | 18.9 | 0% | 0% | 97% | 1,116 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 283 | 2,259 | 7.7 | 45% | 0% | 100% | 132 KB | 247 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 240 | 480 | 6.0 | 0% | 0% | – | 710 KB | 1 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 210 | 7,493 | 0.0 | 27% | 0% | 79% | 554 KB | 29 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 173 | 2,542 | 6.0 | 0% | 0% | 99% | 100 KB | 4 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 169 | 1,525 | 20.5 | 0% | 0% | 100% | 25 KB | 18 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 169 | 391 | 16.4 | 67% | 0% | 76% | 15 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 167 | 3,893 | 24.7 | 0% | 0% | 92% | 556 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 124 | 187 | 28.0 | 62% | 0% | 96% | 270 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 96 | 730 | 11.5 | 80% | 0% | 98% | 451 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,288 | 12.8 | 0% | 0% | 31% | 7,014 KB | 20 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 65 | 6,594 | 0.0 | 50% | 0% | 0% | 254 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 54 | 293 | 7.2 | 0% | 0% | 57% | 642 KB | 4 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 45 | 2,259 | 9.1 | 0% | 0% | 0% | 285 KB | 25 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 33 | 598 | 7.2 | 44% | 0% | 100% | 156 KB | 2 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 31 | 371 | 13.1 | 32% | 0% | 0% | 348 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 28 | 527 | 6.0 | 0% | 0% | 90% | 46 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 14 | 78,946 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 13 | 4,248 | 9.0 | 9% | 0% | 99% | 59 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 10 | 253 | 7.9 | 0% | 0% | 80% | 27 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 2 | 11,589 | 5.2 | 0% | 0% | 86% | 149 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 2 | 20,084 | 2.2 | 67% | 0% | 99% | 579 KB | 0 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F C B | – | – | 54.4 | 70% | 68% | 95% | 839 KB | 11 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 531 | 48.6 | 0% | 0% | 96% | 136 KB | 1 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F E | 0 | 132,473 | 39.6 | 0% | 0% | – | 3,975 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 156,031 | 37.1 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 34.0 | – | – | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 33.5 | 44% | 46% | 87% | 2,272 KB | 1,504 (+4) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 28,444 | 28.5 | 0% | 0% | 79% | 416 KB | 9 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 178 | 26.6 | 0% | 0% | 95% | 249 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | 0 | 5,987 | 24.6 | 0% | 0% | 99% | 167 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 0 | 1,091 | 22.1 | 55% | 0% | 99% | 98 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 19.4 | 38% | 18% | 95% | 1,034 KB | 4 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 584 | 18.8 | 0% | 0% | 95% | 122 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 18.2 | 0% | 0% | 98% | 154 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 466 | 17.4 | 0% | 0% | 99% | 504 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 17.0 | – | – | 100% | 403 KB | 2 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 233 | 16.4 | 0% | 0% | 76% | 335 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 15.9 | – | – | 100% | 41 KB | 2 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 0 | 15.9 | – | – | 91% | 306 KB | 7 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 864 | 15.2 | 0% | 0% | 98% | 1,170 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 15.1 | 44% | 0% | 87% | 86 KB | 7 (+1) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 0 | 2,931 | 14.9 | 0% | 0% | 99% | 355 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 11.9 | 0% | 0% | 0% | 206 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 370 | 11.7 | 0% | 0% | 96% | 66 KB | 3 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 0 | 2 | 11.1 | 0% | 0% | 100% | 160 KB | 2 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 11.0 | – | – | 98% | 363 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 0 | 10.8 | 0% | 0% | 95% | 8,119 KB | 1 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 10.6 | – | – | 99% | 80 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 4,242 | 10.2 | 17% | 0% | 100% | 95 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 0 | 10.1 | – | – | 99% | 35 KB | 1 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 8 | 10.0 | 0% | 0% | 96% | 99 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 9.5 | – | – | 93% | 576 KB | 1 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 645 | 8.5 | 0% | 0% | 97% | 663 KB | 2 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 0 | 1,474 | 8.5 | 0% | 0% | 98% | 45 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 1,059 | 8.3 | 0% | 0% | – | 100 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | F F B | 0 | 707 | 8.0 | 22% | 0% | 100% | 4,314 KB | 32 (+1) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 0 | 66 | 7.4 | 0% | 0% | 80% | 83 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 332 | 7.4 | 0% | 0% | 99% | 127 KB | 24 (+1) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 7.1 | 7% | 12% | 88% | 700 KB | 4 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | F F A | 0 | 1,457 | 7.1 | 0% | 0% | 93% | 236 KB | 5 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 0 | 0 | 6.8 | 0% | 0% | 89% | 682 KB | 6 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 2,404 | 6.2 | 5% | 0% | 88% | 739 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 2 | 4.5 | 0% | 0% | 90% | 163 KB | 14 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 0 | 4.4 | 0% | 0% | 86% | 162 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 0 | 4.3 | – | – | 79% | 590 KB | 2 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | – | – | 4.3 | – | – | 97% | 43 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 3.9 | – | – | 96% | 122 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 3.5 | – | – | 90% | 195 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F B | 0 | 452 | 3.0 | 0% | 0% | 100% | 1,403 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | – | – | 2.9 | – | – | 90% | 319 KB | 1 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 2.7 | 54% | 41% | 0% | 2,040 KB | 461 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 2.7 | – | – | 99% | 298 KB | 5 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 80 | 2.4 | 0% | 0% | – | 56 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 2.1 | – | – | 98% | 723 KB | 5 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 2.0 | – | – | 97% | 94 KB | 16 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 0 | 597 | 1.5 | 0% | 0% | 100% | 52 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 1.5 | – | – | 98% | 231 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 1.4 | – | – | – | 311 KB | 4 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 14 | 1.3 | 0% | 0% | 99% | 73 KB | 3 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,425 | 0.9 | 0% | 0% | – | 201 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 0 | 0 | 0.8 | 0% | 0% | – | 53 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 115 | 0.5 | 0% | 0% | 20% | 154 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.5 | – | – | 98% | 42 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.4 | – | – | 100% | 59 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.3 | – | – | 0% | 518 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F D B | – | – | 0.2 | 68% | 13% | 75% | 846 KB | 7 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.2 | – | – | 69% | 290 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 0.1 | – | – | – | 115 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,320 (+3) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F C | – | – | 0.1 | 22% | 43% | 67% | 87 KB | 5 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 164 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 0 | 196 | 0.0 | 0% | 0% | 100% | 444 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 622 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | 0 | 1,052 | 0.0 | 12% | 0% | 0% | 342 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 36 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 114 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | – | – | 0.0 | – | – | 30% | 308 KB | 783 (+20) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F F E | – | – | 0.0 | 62% | 6% | 94% | 34,213 KB | 0 (+0) |
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
