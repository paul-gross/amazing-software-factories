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
_349 repos, last measured 2026-11-21. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (349)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 90,586 | 100,914 | 79.6 | 53% | 45% | 89% | 432 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A E B | 65,713 | 71,678 | 63.7 | 76% | 0% | 100% | 328 KB | 3 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | A F B | 41,796 | 54,245 | 109 | 26% | 33% | 92% | 6,076 KB | 87 (-1) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 39,609 | 2,148,065 | 0.0 | 84% | 48% | 0% | 3,286 KB | 1 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B C C | 39,209 | 52,874 | 16.9 | 76% | 31% | 91% | 8,727 KB | 146 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 38,304 | 62,432 | 219 | 22% | 0% | 100% | 2,294 KB | 5 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B E A | 37,194 | 62,669 | 72.0 | 50% | 0% | 94% | 429 KB | 87 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B E B | 36,140 | 57,709 | 95.8 | 56% | 5% | 95% | 505 KB | 1 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 32,902 | 116,227 | 160 | 54% | 67% | 55% | 311 KB | 4 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B E B | 30,255 | 46,501 | 35.6 | 47% | 22% | 98% | 4,176 KB | 2,133 (+3) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 29,484 | 48,696 | 44.1 | 81% | 44% | 99% | 891 KB | 5 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 27,063 | 47,352 | 0.0 | 74% | 43% | – | 1,000 KB | 2 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B E D | 25,155 | 35,016 | 0.0 | 52% | 29% | 0% | 4,193 KB | 3 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | B F C | 22,887 | 34,360 | 0.0 | 31% | 62% | 92% | 20,387 KB | 2 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,905 | 49,365 | 0.0 | 48% | 60% | – | 575 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 21,546 | 34,656 | 23.2 | 59% | 47% | 100% | 1,992 KB | 158 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | B D C | 21,213 | 43,075 | 33.1 | 70% | 52% | 99% | 3,196 KB | 6 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | B B A | 20,871 | 33,116 | 15.0 | 87% | 27% | 94% | 255 KB | 5 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B E B | 20,844 | 26,942 | 51.9 | 43% | 49% | 87% | 158 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | B D B | 20,730 | 46,545 | 0.0 | 70% | 34% | 82% | 397 KB | 0 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B B B | 20,324 | 88,964 | 91.6 | 81% | 29% | 85% | 1,567 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C C C | 19,907 | 26,843 | 139 | 77% | 41% | 100% | 5,251 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 19,269 | 27,915 | 27.5 | 30% | 21% | 80% | 1,026 KB | 1 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 19,073 | 25,439 | 24.1 | 51% | 30% | 100% | 606 KB | 22 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C E B | 18,192 | 37,062 | 0.1 | 57% | 27% | 89% | 4,060 KB | 7 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C D | 17,674 | 29,593 | 26.2 | 73% | 27% | 42% | 107 KB | 234 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C C B | 17,509 | 20,951 | 25.0 | 77% | 51% | 79% | 597 KB | 7 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 17,362 | 25,045 | 23.0 | 43% | 11% | – | 122 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 16,970 | 48,416 | 22.4 | 60% | 16% | 100% | 1,195 KB | 40 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 16,894 | 46,541 | 0.0 | 49% | 27% | – | 1,119 KB | 0 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 16,443 | 23,865 | 154 | 60% | 30% | 100% | 272 KB | 22 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | C F D | 15,539 | 33,814 | 0.0 | 5% | 0% | 33% | 1,692 KB | 465 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 15,400 | 27,073 | 7.8 | 0% | 0% | 100% | 543 KB | 150 (+2) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 15,212 | 26,828 | 20.6 | 79% | 26% | 99% | 199 KB | 36 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 15,153 | 40,230 | 6.6 | 16% | 47% | 100% | 618 KB | 19 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 62,016 | 30.6 | 45% | 12% | 62% | 65 KB | 3 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 14,534 | 35,418 | 88.9 | 24% | 35% | 100% | 173 KB | 74 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C F C | 14,407 | 47,265 | 0.0 | 62% | 0% | 53% | 5,368 KB | 450 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 13,823 | 38,809 | 20.5 | 89% | 17% | 83% | 363 KB | 11 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C D B | 13,585 | 19,843 | 43.2 | 61% | 47% | 98% | 996 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | C D B | 12,755 | 24,330 | 41.2 | 63% | 16% | 100% | 75 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C B C | 12,127 | 21,069 | 34.1 | 83% | 19% | 100% | 473 KB | 10 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 11,621 | 14,753 | 0.0 | 76% | 8% | 5% | 471 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C E C | 11,285 | 15,884 | 19.5 | 80% | 6% | 100% | 437 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C E D | 11,156 | 37,498 | 0.1 | 47% | 0% | 0% | 255 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | C E F | 11,128 | 68,874 | 0.0 | 75% | 0% | – | 8,190 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E D | 10,888 | 42,485 | 61.8 | 45% | 41% | 44% | 510 KB | 6,731 (+6) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C E D | 10,582 | 13,834 | 0.0 | 54% | 64% | 10% | 1,653 KB | 38 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C E A | 10,564 | 15,559 | 65.5 | 83% | 4% | 99% | 29 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C F C | 10,550 | 18,057 | 0.1 | 56% | 5% | 86% | 417 KB | 2 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 10,376 | 21,681 | 32.8 | 12% | 4% | 99% | 308 KB | 1 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | C F B | 10,187 | 17,277 | 28.7 | 22% | 0% | 97% | 497 KB | 1,689 (+2) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C C D | 10,075 | 14,322 | 85.3 | 79% | 33% | – | 480 KB | 3 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D F B | 9,940 | 24,938 | 42.9 | 32% | 31% | 75% | 1,523 KB | 71,031 (+23) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C A | 9,898 | 33,623 | 19.6 | 76% | 18% | 89% | 155 KB | 4 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D F A | 9,289 | 10,373 | 28.7 | 81% | 0% | 100% | 135 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 14,385 | 6.4 | 24% | 14% | 86% | 743 KB | 9 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 9,131 | 27,927 | 17.4 | 63% | 6% | 84% | 340 KB | 0 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | D E A | 9,108 | 7,741 | 10.5 | 52% | 0% | 100% | 370 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 8,883 | 11,384 | 39.4 | 78% | 45% | 100% | 2,491 KB | 5 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D E A | 8,876 | 12,563 | 23.5 | 72% | 16% | 93% | 233 KB | 1 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | D C B | 8,556 | 14,243 | 0.0 | 74% | 44% | 89% | 250 KB | 133 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 8,446 | 58,938 | 34.0 | 57% | 24% | 100% | 617 KB | 1 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D E C | 8,382 | 9,637 | 8.5 | 83% | 0% | 100% | 4,357 KB | 15 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 8,269 | 8,962 | 11.5 | 0% | 0% | 97% | 544 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D E B | 7,693 | 14,827 | 18.6 | 58% | 40% | 90% | 102 KB | 4 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D D B | 7,622 | 10,258 | 19.6 | 64% | 0% | 98% | 634 KB | 1 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D F B | 7,564 | 13,314 | 21.1 | 83% | 0% | 96% | 158 KB | 5 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D B B | 7,541 | 13,774 | 14.1 | 82% | 14% | 98% | 1,159 KB | 8 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 7,509 | 10,839 | 5.0 | 35% | 0% | 100% | 2,284 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D E D | 7,457 | 28,693 | 7.4 | 47% | 4% | 25% | 267 KB | 16 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 7,361 | 7,833 | 14.2 | 5% | 0% | 97% | 631 KB | 13 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D E A | 6,960 | 53,364 | 19.0 | 55% | 13% | 94% | 41 KB | 0 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D D A | 6,899 | 10,185 | 47.4 | 64% | 27% | 100% | 59 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 6,830 | 19,279 | 37.5 | 35% | 0% | 100% | 605 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D E C | 6,785 | 8,942 | 22.6 | 40% | 20% | 100% | 358 KB | 18 (+0) |
| [integry/propr](https://github.com/integry/propr) | D F B | 6,751 | 15,733 | 7.6 | 75% | 2% | 100% | 4,314 KB | 34 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 6,637 | 18,574 | 11.3 | 15% | 5% | 97% | 577 KB | 95 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 6,531 | 34,455 | 0.0 | 70% | 3% | 97% | 690 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,312 | 22,274 | 43.0 | 11% | 3% | 97% | 236 KB | 7 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 6,099 | 11,878 | 17.5 | 44% | 0% | 97% | 49 KB | 23,970 (+7) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 6,086 | 19,273 | 0.0 | 69% | 25% | 50% | 570 KB | 1 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D C B | 5,976 | 7,639 | 0.0 | 78% | 59% | 100% | 401 KB | 3 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F D | 5,911 | 8,731 | 0.4 | 10% | 25% | 1% | 284 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 5,618 | 8,169 | 12.2 | 23% | 35% | 85% | 391 KB | 186 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 5,461 | 11,116 | 19.2 | 68% | 0% | 93% | 315 KB | 159 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | E C D | 4,838 | 11,941 | 10.4 | 73% | 3% | 0% | 233 KB | 11 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E E B | 4,794 | 77,277 | 7.0 | 66% | 0% | 99% | 332 KB | 6 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,489 | 7,325 | 0.0 | 52% | 8% | 73% | 137 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,396 | 9,773 | 6.5 | 8% | 20% | 93% | 378 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F A | 4,174 | 9,962 | 18.3 | 26% | 0% | 93% | 262 KB | 9 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 3,867 | 31,838 | 0.0 | 52% | 0% | – | 221 KB | 31 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E E C | 3,838 | 10,505 | 0.0 | 55% | 30% | 75% | 1,175 KB | 51 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E B B | 3,706 | 7,021 | 57.9 | 87% | 70% | 97% | 246 KB | 9 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 3,686 | 6,365 | 33.0 | 26% | 0% | 100% | 63 KB | 3 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E F B | 3,657 | 16,764 | 24.3 | 54% | 0% | 99% | 1,925 KB | 3 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E D C | 3,614 | 9,729 | 17.1 | 60% | 0% | 88% | 515 KB | 26 (+1) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 3,545 | 17,049 | 10.8 | 20% | 9% | 100% | 920 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 3,509 | 13,162 | 3.6 | 27% | 0% | 100% | 1,523 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 3,414 | 6,393 | 18.5 | 0% | 5% | 100% | 68 KB | 64 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E D B | 3,364 | 10,081 | 23.3 | 64% | 6% | 95% | 644 KB | 3 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 3,269 | 5,742 | 15.8 | 49% | 32% | 100% | 628 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E E B | 3,261 | 6,786 | 17.2 | 48% | 23% | 94% | 425 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 3,204 | 8,347 | 1.8 | 58% | 33% | 92% | 4,273 KB | 566 (+2) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | E F C | 3,054 | 12,327 | 23.1 | 0% | 0% | 78% | 523 KB | 21 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E E B | 2,976 | 26,647 | 0.0 | 44% | 27% | 97% | 590 KB | 1 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 2,900 | 3,331 | 16.2 | 23% | 0% | 100% | 322 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | E E A | 2,721 | 7,039 | 43.5 | 73% | 0% | 99% | 340 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E D C | 2,694 | 5,078 | 10.8 | 63% | 52% | 92% | 177 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 2,666 | 5,044 | 19.1 | 44% | 23% | 97% | 258 KB | 3 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,648 | 4,839 | 4.2 | 41% | 0% | – | 201 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,547 | 4,568 | 3.4 | 8% | 0% | 95% | 728 KB | 3 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,479 | 5,464 | 13.7 | 24% | 21% | 79% | 312 KB | 1 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,445 | 30,711 | 4.3 | 45% | 0% | 89% | 24 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 2,424 | 23,271 | 16.3 | 54% | 0% | 100% | 1,129 KB | 49 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 2,376 | 3,187 | 14.5 | 15% | 0% | 96% | 163 KB | 1 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,360 | 4,202 | 31.0 | 46% | 2% | 100% | 512 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E D A | 2,330 | 4,041 | 6.5 | 68% | 0% | 100% | 236 KB | 6 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E D D | 2,303 | 2,769 | 0.1 | 64% | 0% | 0% | 606 KB | 1 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,255 | 2,545 | 6.2 | 36% | 0% | 98% | 101 KB | 260 (+2) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 2,216 | 2,453 | 14.0 | 58% | 0% | 95% | 431 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | E F D | 2,013 | 28,270 | 0.0 | 71% | 0% | 28% | 308 KB | 845 (-1) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F B | 1,967 | 11,731 | 25.5 | 19% | 0% | 82% | 242 KB | 138 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 1,911 | 5,213 | 3.3 | 0% | 0% | 71% | 302 KB | 351 (-2) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,776 | 3,786 | 8.2 | 19% | 23% | 91% | 518 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F C | 1,748 | 14,847 | 0.1 | 0% | 0% | 56% | 1,295 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 1,735 | 14,977 | 0.0 | 56% | 30% | 42% | 268 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,728 | 4,634 | 13.8 | 29% | 51% | 99% | 386 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F C | 1,688 | 6,294 | 11.5 | 38% | 0% | 54% | 1,263 KB | 13 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F A | 1,683 | 7,641 | 4.1 | 21% | 0% | 88% | 167 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 1,649 | 5,943 | 2.2 | 55% | 0% | 82% | 685 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E E C | 1,640 | 2,658 | 2.2 | 58% | 38% | 91% | 1,468 KB | 1,119 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,614 | 4,628 | 0.0 | 58% | 6% | 69% | 297 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,595 | 2,886 | 16.5 | 14% | 0% | 97% | 106 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E C B | 1,595 | 1,961 | 10.3 | 85% | 0% | 100% | 361 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,582 | 7,415 | 22.0 | 7% | 21% | 95% | 324 KB | 1 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,577 | 5,512 | 0.9 | 52% | 30% | 92% | 5,651 KB | 1 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E D C | 1,575 | 4,272 | 17.2 | 64% | 16% | 88% | 677 KB | 2 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | E F C | 1,565 | 1,684 | 12.1 | 42% | 0% | 99% | 885 KB | 3 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E F C | 1,513 | 2,400 | 22.5 | 58% | 0% | 91% | 947 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E F D | 1,475 | 9,658 | 2.6 | 32% | 0% | 0% | 6,837 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 1,409 | 224,118 | 105 | 25% | 7% | 94% | 378 KB | 4 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E F E | 1,401 | 10,977 | 11.2 | 23% | 0% | 99% | 634 KB | 11 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,367 | 1,652 | 8.9 | 36% | 0% | 87% | 1,054 KB | 2 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,315 | 9,924 | 22.2 | 36% | 0% | 94% | 363 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,214 | 4,370 | 21.6 | 12% | 0% | 98% | 595 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | E F B | 1,143 | 11,135 | 4.0 | 0% | 0% | 90% | 2,640 KB | 47 (+1) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 1,138 | 4,786 | 13.0 | 50% | 0% | 78% | 1,116 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 1,132 | 4,767 | 17.5 | 16% | 36% | 87% | 540 KB | 12 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 1,119 | 2,607 | 3.2 | 0% | 0% | 87% | 739 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,101 | 2,287 | 0.0 | 0% | 0% | – | 1,033 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 1,004 | 44,003 | 11.1 | 25% | 0% | 97% | 1,414 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,004 | 2,994 | 9.1 | 20% | 0% | 74% | 274 KB | 1 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | F F A | 987 | 3,978 | 14.2 | 54% | 0% | 99% | 162 KB | 7 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 934 | 1,388 | 0.0 | 42% | 36% | 100% | 515 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 923 | 3,009 | 12.6 | 0% | 0% | 98% | 74 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 914 | 3,218 | 5.8 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 903 | 1,682 | 7.4 | 18% | 0% | 100% | 98 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 833 | 2,414 | 12.3 | 41% | 0% | 100% | 393 KB | 2 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | F F B | 813 | 11,652 | 49.8 | 39% | 14% | 100% | 1,445 KB | 8 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | F F D | 810 | 2,044 | 0.8 | 12% | 0% | 30% | 259 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 743 | 3,188 | 7.3 | 18% | 0% | 98% | 6,579 KB | 9 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 709 | 2,623 | 5.9 | 34% | 0% | 100% | 45 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F E A | 598 | 2,610 | 9.7 | 46% | 0% | 100% | 468 KB | 14 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 566 | 1,564 | 21.3 | 14% | 0% | – | 454 KB | 1 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 539 | 7,425 | 6.9 | 46% | 16% | 98% | 485 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 458 | 1,168 | 25.9 | 78% | 0% | 90% | 1,000 KB | 121 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | F F B | 444 | 6,637 | 19.4 | 0% | 0% | 93% | 705 KB | 50 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 435 | 1,639 | 14.5 | 16% | 0% | 100% | 126 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | F E D | 427 | 2,024 | 18.8 | 45% | 0% | – | 63 KB | 4 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 421 | 1,856 | 3.5 | 27% | 0% | 99% | 173 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 386 | 12,929 | 5.7 | 29% | 0% | 100% | 100 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 380 | 12,905 | 17.0 | 25% | 0% | 92% | 149 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 346 | 941 | 5.2 | 0% | 17% | 92% | 763 KB | 7 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 252 | 1,396 | 0.0 | 29% | 0% | 42% | 198 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 249 | 1,602 | 11.1 | 43% | 0% | 100% | 269 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 224 | 26,793 | 32.3 | 19% | 0% | 11% | 3,975 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 214 | 1,520 | 18.3 | 0% | 0% | 100% | 190 KB | 2 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 179 | 765 | 7.0 | 33% | 0% | 99% | 271 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 169 | 10,694 | 11.5 | 46% | 0% | 100% | 221 KB | 7 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 135 | 420 | 0.0 | 0% | 0% | 93% | 269 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 91 | 1,237 | 0.6 | 0% | 0% | 0% | 52 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 83 | 735 | 14.2 | 0% | 0% | 96% | 93 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,317 | 11.0 | 0% | 88% | 21% | 7,014 KB | 21 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 75 | 3,620 | 3.0 | 18% | 0% | 94% | 697 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 69 | 1,681 | 3.5 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 68 | 162 | 0.0 | 0% | 0% | 0% | 673 KB | 3 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 51 | 2,953 | 13.8 | 32% | 0% | 99% | 178 KB | 15 (+1) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F D | 50 | 2,042 | 0.0 | 10% | 0% | 43% | 554 KB | 29 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 46 | 3,358 | 9.5 | 9% | 0% | 97% | 249 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 42 | 33,153 | 5.5 | 0% | 0% | 97% | 952 KB | 2 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | F F B | 35 | 47,113 | 15.1 | 3% | 0% | 100% | 266 KB | 2 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 24 | 5,162 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | 4 | 10,201 | 0.0 | 30% | 0% | – | 320 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F C C | 4 | 5,456 | 0.0 | 78% | 27% | 100% | 2,138 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 1 | 25,059 | 24.3 | 0% | 0% | 99% | 635 KB | 2 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 1 | 1,719 | 1.3 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F C B | – | – | 64.4 | 74% | 16% | 100% | 3,196 KB | 162 (+2) |
| [purlis/purlis](https://github.com/purlis/purlis) | F E B | – | – | 54.6 | 55% | 19% | 93% | 966 KB | 12 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F B | 0 | 0 | 48.3 | 0% | 0% | 97% | 1,125 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 0 | 1,300 | 39.2 | 12% | 0% | 100% | 598 KB | 5 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 15,398 | 33.6 | 56% | 0% | 100% | 178 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 34 | 31.0 | 0% | 0% | 85% | 263 KB | 1,258 (-1) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 23.6 | 62% | 7% | 90% | 2,290 KB | 1,557 (+6) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 294 | 23.4 | 0% | 0% | 99% | 703 KB | 2 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 0 | 691 | 22.8 | 42% | 0% | 99% | 981 KB | 2 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | 0 | 2,801 | 20.3 | 10% | 0% | 100% | 192 KB | 0 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 1,719 | 17.9 | 33% | 0% | 99% | 295 KB | 2 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 17.6 | – | – | 91% | 306 KB | 7 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 0 | 17.5 | 12% | 0% | 76% | 1,770 KB | 6 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 0 | 707 | 16.3 | 38% | 0% | 99% | 578 KB | 2 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 16.2 | – | – | 100% | 703 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | – | – | 16.2 | – | – | 100% | 42 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | 0 | 1 | 15.9 | 0% | 0% | 66% | 324 KB | 40,973 (+18) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 15.5 | 49% | 21% | 95% | 1,044 KB | 4 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 15.1 | – | – | 79% | 416 KB | 9 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 426 | 14.1 | 0% | 0% | 79% | 22 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 2,118 | 12.6 | 24% | 0% | 92% | 576 KB | 2 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 12.5 | 0% | 0% | 100% | 154 KB | 4 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 6 | 11.9 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 559 | 11.9 | 0% | 0% | 87% | 137 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,263 | 11.5 | 0% | 0% | 94% | 943 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 848 | 11.2 | 29% | 0% | 100% | 1,060 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 366 | 10.4 | 23% | 0% | 0% | 348 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 0 | 1,401 | 9.7 | 0% | 0% | 95% | 105 KB | 3 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 0 | 1,220 | 9.3 | 0% | 0% | 98% | 215 KB | 1 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 9.3 | 24% | 0% | 88% | 710 KB | 4 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 99 | 8.4 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F E D | – | – | 8.4 | 49% | 0% | 0% | 206 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 8.2 | – | – | 98% | 165 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 1,201 | 8.2 | 0% | 0% | 96% | 127 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 0 | 1,712 | 7.6 | 33% | 0% | 97% | 53 KB | 2 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 1,822 | 7.2 | 0% | 0% | 100% | 168 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 7.1 | 59% | 29% | 75% | 86 KB | 7 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,777 | 6.1 | 0% | 0% | 92% | 1,170 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | – | – | 5.5 | – | – | 100% | 25 KB | 19 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 5.4 | – | – | 100% | 160 KB | 2 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 573 | 4.5 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 4.4 | – | – | 96% | 99 KB | 1 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 4.4 | – | – | 95% | 385 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | F F B | 0 | 485 | 4.4 | 0% | 0% | 97% | 552 KB | 12 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 4.0 | – | – | 100% | 403 KB | 2 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | – | – | 3.8 | – | – | 72% | 396 KB | 2 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 48 | 3.8 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 777 | 3.7 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 3.6 | – | – | 100% | 41 KB | 2 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 3.6 | – | – | 99% | 87 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 2,969 | 3.5 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 242 | 3.3 | 0% | 0% | 87% | 489 KB | 89 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 7 | 3.1 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 0 | 877 | 3.0 | 0% | 0% | 99% | 608 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 3.0 | – | – | 99% | 98 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 18 | 2.9 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 2.9 | – | – | – | 710 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 36 | 2.7 | 0% | 0% | 97% | 504 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 5 | 2.6 | 0% | 0% | 91% | 43 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 2.6 | – | – | 99% | 80 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 6 | 2.6 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 21 | 2.4 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 2.4 | 0% | 0% | 89% | 163 KB | 15 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 158 | 2.2 | 0% | 0% | 98% | 104 KB | 4 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 330 | 2.0 | 0% | 0% | 88% | 617 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 1.9 | – | – | 95% | 8,119 KB | 1 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 1,704 | 1.8 | 0% | 0% | 91% | 3,845 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 1.4 | – | – | 93% | 576 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 6,283 | 1.4 | 0% | 0% | 60% | 46 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 267 | 1.2 | 0% | 0% | 88% | 156 KB | 2 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 1.1 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 1.0 | – | – | 80% | 83 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 476 | 0.5 | 0% | 0% | – | 14 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.4 | 46% | 32% | 0% | 13,975 KB | 463 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.2 | – | – | 20% | 154 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.2 | 79% | 80% | 80% | 900 KB | 7 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 0.1 | – | – | 53% | 3,052 KB | 2 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.1 | – | – | – | 311 KB | 4 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.1 | – | – | 96% | 122 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,341 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 71% | 8% | 50% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 0 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F C | 0 | 3,043 | 0.0 | 0% | 0% | 89% | 177 KB | 105 (-4) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | – | – | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 479 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 0 | 5,373 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.0 | – | – | 98% | 42 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.0 | 72% | 37% | 94% | 43,113 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 107 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 20 | 0.0 | 0% | 0% | 6% | 158 KB | 122 (+0) |
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
