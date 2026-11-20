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
_349 repos, last measured 2026-11-20. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (349)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 90,586 | 103,317 | 78.8 | 60% | 46% | 89% | 432 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A E B | 65,713 | 76,090 | 62.6 | 77% | 0% | 97% | 326 KB | 3 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [arul28/ADE](https://github.com/arul28/ADE) | A F C | 42,778 | 60,160 | 15.1 | 48% | 40% | 92% | 8,727 KB | 146 (+2) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | A F B | 41,796 | 56,182 | 106 | 28% | 35% | 91% | 6,073 KB | 88 (+1) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 39,609 | 2,252,993 | 0.0 | 89% | 49% | 0% | 3,286 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B F A | 37,194 | 45,914 | 67.1 | 16% | 0% | 94% | 429 KB | 87 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 36,811 | 63,903 | 224 | 32% | 0% | 100% | 2,454 KB | 5 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B D B | 36,140 | 66,770 | 90.4 | 66% | 5% | 99% | 504 KB | 1 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 32,902 | 116,227 | 160 | 54% | 67% | 55% | 311 KB | 4 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B E B | 32,512 | 47,975 | 36.1 | 48% | 22% | 99% | 4,158 KB | 2,130 (+2) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B B B | 29,484 | 55,535 | 44.5 | 82% | 36% | 99% | 887 KB | 5 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B B D | 29,028 | 50,430 | 0.0 | 80% | 42% | – | 1,001 KB | 2 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B E D | 25,155 | 41,988 | 0.0 | 56% | 28% | 0% | 4,028 KB | 3 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | B F C | 22,887 | 34,360 | 0.0 | 31% | 62% | 92% | 20,387 KB | 2 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,716 | 41,193 | 0.0 | 45% | 67% | – | 575 KB | 2 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | B C C | 21,213 | 42,307 | 32.0 | 75% | 56% | 100% | 3,196 KB | 6 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | B B A | 20,871 | 34,908 | 14.7 | 84% | 52% | 94% | 254 KB | 5 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B E B | 20,844 | 29,300 | 52.1 | 43% | 47% | 90% | 158 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | B C B | 20,730 | 46,262 | 0.0 | 74% | 35% | 85% | 396 KB | 0 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B D B | 20,324 | 101,907 | 90.0 | 67% | 9% | 83% | 1,559 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | B E C | 20,051 | 74,923 | 32.0 | 50% | 10% | 62% | 65 KB | 3 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | C D B | 19,339 | 28,872 | 23.7 | 62% | 49% | 98% | 1,949 KB | 158 (-1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 18,687 | 55,628 | 23.1 | 62% | 32% | 97% | 1,195 KB | 40 (+1) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C E B | 18,192 | 37,062 | 0.1 | 57% | 27% | 89% | 4,060 KB | 7 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 17,663 | 40,097 | 21.0 | 85% | 20% | 84% | 363 KB | 11 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C F B | 17,246 | 31,879 | 39.5 | 32% | 32% | 77% | 1,514 KB | 71,008 (+14) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C C C | 16,902 | 25,632 | 136 | 78% | 46% | 100% | 5,251 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 16,894 | 28,948 | 0.0 | 58% | 39% | – | 1,119 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C C | 16,861 | 35,992 | 27.0 | 73% | 28% | 50% | 107 KB | 234 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 16,654 | 24,050 | 27.2 | 26% | 25% | 94% | 1,026 KB | 1 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 16,443 | 23,865 | 154 | 60% | 30% | 100% | 272 KB | 22 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 16,167 | 36,478 | 89.4 | 37% | 34% | 96% | 172 KB | 74 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 15,664 | 35,219 | 0.0 | 72% | 0% | 28% | 308 KB | 846 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | C F D | 15,539 | 30,894 | 0.0 | 5% | 0% | 33% | 284 KB | 465 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 15,212 | 27,106 | 21.2 | 73% | 25% | 100% | 198 KB | 36 (+1) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 15,153 | 40,819 | 7.1 | 16% | 48% | 97% | 617 KB | 19 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B D | 15,080 | 16,905 | 0.0 | 81% | 7% | 4% | 471 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C F D | 14,407 | 49,962 | 0.0 | 50% | 0% | 36% | 5,368 KB | 450 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C E B | 13,589 | 20,352 | 42.4 | 52% | 47% | 98% | 981 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C C B | 12,694 | 18,291 | 24.7 | 78% | 45% | 79% | 597 KB | 7 (+1) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 12,547 | 22,008 | 24.4 | 49% | 37% | 98% | 606 KB | 22 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 12,127 | 21,774 | 33.3 | 81% | 18% | 100% | 470 KB | 10 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 12,101 | 16,912 | 35.9 | 29% | 0% | 100% | 605 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | C F B | 11,925 | 26,455 | 29.4 | 34% | 1% | 97% | 497 KB | 1,687 (+2) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C E C | 11,285 | 23,399 | 20.0 | 56% | 8% | 100% | 429 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | C E F | 11,145 | 91,993 | 0.0 | 60% | 0% | – | 8,190 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C E D | 11,033 | 26,328 | 0.1 | 59% | 0% | 0% | 255 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C D D | 11,004 | 15,563 | 0.0 | 61% | 58% | 13% | 1,652 KB | 38 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E D | 10,888 | 42,485 | 61.8 | 45% | 41% | 44% | 510 KB | 6,731 (+6) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 10,600 | 26,090 | 7.8 | 0% | 0% | 100% | 537 KB | 148 (+6) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C E A | 10,564 | 16,251 | 69.2 | 89% | 3% | 93% | 28 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 10,376 | 22,419 | 37.8 | 16% | 3% | 96% | 283 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | C F A | 10,295 | 13,111 | 18.5 | 37% | 0% | 94% | 262 KB | 9 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 10,108 | 16,797 | 22.4 | 42% | 49% | – | 122 KB | 2 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C C D | 10,075 | 14,155 | 83.4 | 78% | 36% | – | 476 KB | 3 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 9,712 | 13,403 | 40.9 | 78% | 42% | 100% | 2,491 KB | 5 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 9,475 | 12,204 | 0.1 | 66% | 7% | 86% | 416 KB | 2 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C B | 9,321 | 29,754 | 19.2 | 81% | 19% | 74% | 155 KB | 4 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D B B | 9,308 | 16,023 | 14.5 | 80% | 16% | 98% | 1,159 KB | 8 (-1) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D F A | 9,289 | 11,516 | 28.1 | 73% | 0% | 100% | 135 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 16,079 | 6.6 | 44% | 11% | 87% | 742 KB | 9 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | D E A | 9,108 | 8,076 | 11.7 | 50% | 11% | 100% | 370 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [integry/propr](https://github.com/integry/propr) | D F B | 9,005 | 15,999 | 7.1 | 75% | 2% | 100% | 4,314 KB | 34 (-1) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D E A | 8,876 | 12,563 | 23.5 | 72% | 16% | 93% | 233 KB | 1 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 8,631 | 27,846 | 17.6 | 63% | 27% | 84% | 340 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 8,451 | 59,021 | 33.4 | 59% | 15% | 100% | 617 KB | 1 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D F C | 8,253 | 8,517 | 9.7 | 70% | 0% | 100% | 4,357 KB | 15 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D E A | 8,203 | 57,400 | 20.0 | 57% | 28% | 94% | 41 KB | 0 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 8,049 | 9,198 | 14.4 | 4% | 0% | 97% | 631 KB | 13 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D F B | 7,693 | 15,015 | 19.0 | 37% | 34% | 74% | 105 KB | 4 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 7,509 | 12,166 | 5.0 | 25% | 0% | 100% | 2,284 KB | 0 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | D C B | 7,495 | 14,113 | 0.0 | 79% | 36% | 88% | 246 KB | 133 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 7,256 | 10,937 | 12.7 | 30% | 32% | 88% | 391 KB | 186 (+2) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D F B | 7,235 | 18,573 | 24.5 | 35% | 0% | 99% | 1,902 KB | 3 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 7,113 | 24,700 | 0.0 | 61% | 23% | 50% | 570 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 7,022 | 7,659 | 11.4 | 13% | 0% | 98% | 544 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D F D | 7,003 | 48,536 | 7.6 | 47% | 0% | 25% | 252 KB | 16 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D E C | 6,785 | 8,942 | 22.6 | 40% | 20% | 100% | 358 KB | 18 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D C B | 6,735 | 7,165 | 16.6 | 71% | 0% | 99% | 625 KB | 1 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 6,637 | 17,716 | 12.0 | 13% | 5% | 99% | 574 KB | 95 (-1) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D C A | 6,604 | 7,909 | 44.7 | 77% | 0% | 92% | 59 KB | 1 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,312 | 22,274 | 43.0 | 11% | 3% | 97% | 236 KB | 7 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 6,204 | 31,880 | 0.0 | 62% | 3% | 97% | 690 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 6,099 | 12,896 | 18.7 | 43% | 0% | 96% | 49 KB | 23,963 (+10) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | D E B | 6,006 | 11,864 | 23.9 | 52% | 8% | 95% | 644 KB | 3 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D B B | 5,976 | 7,989 | 0.0 | 86% | 61% | 100% | 400 KB | 3 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F D | 5,911 | 9,722 | 0.4 | 9% | 23% | 0% | 284 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 5,729 | 14,774 | 19.2 | 61% | 0% | 93% | 315 KB | 159 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | D F C | 5,503 | 6,409 | 2.2 | 52% | 0% | 81% | 685 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D E B | 5,160 | 24,200 | 40.6 | 59% | 18% | 100% | 75 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F B | 4,673 | 14,703 | 26.9 | 7% | 0% | 84% | 242 KB | 138 (+1) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | E C D | 4,514 | 11,011 | 10.1 | 72% | 0% | 2% | 232 KB | 11 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,489 | 7,325 | 0.0 | 52% | 8% | 73% | 137 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 4,336 | 6,589 | 18.0 | 0% | 5% | 99% | 68 KB | 64 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E C C | 4,124 | 11,748 | 0.0 | 72% | 33% | 74% | 1,175 KB | 51 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 3,829 | 8,509 | 16.2 | 58% | 41% | 100% | 628 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 3,688 | 17,238 | 11.3 | 34% | 8% | 100% | 918 KB | 0 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 3,686 | 5,783 | 36.9 | 13% | 0% | 100% | 66 KB | 3 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E C C | 3,614 | 10,042 | 16.5 | 74% | 0% | 88% | 504 KB | 25 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 3,509 | 13,162 | 3.6 | 27% | 0% | 100% | 1,523 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | E E A | 3,504 | 8,442 | 44.5 | 70% | 10% | 99% | 340 KB | 1 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | E F B | 3,367 | 10,819 | 20.8 | 59% | 0% | 96% | 158 KB | 5 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 3,349 | 4,562 | 12.8 | 28% | 0% | 98% | 74 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,294 | 10,435 | 6.7 | 7% | 17% | 93% | 378 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 3,293 | 56,149 | 7.1 | 75% | 0% | 100% | 332 KB | 6 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E E B | 3,261 | 6,786 | 17.2 | 48% | 23% | 94% | 425 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E B B | 3,078 | 6,225 | 55.5 | 88% | 68% | 99% | 244 KB | 9 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | E F C | 3,054 | 7,765 | 23.0 | 0% | 0% | 75% | 521 KB | 21 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,905 | 39,392 | 0.0 | 50% | 0% | – | 221 KB | 31 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 2,900 | 3,331 | 17.0 | 23% | 0% | 100% | 322 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 2,773 | 8,410 | 1.8 | 62% | 35% | 94% | 4,263 KB | 564 (+2) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E F B | 2,723 | 25,954 | 0.0 | 40% | 0% | 97% | 590 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E D C | 2,694 | 5,078 | 10.8 | 63% | 52% | 92% | 177 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,648 | 4,843 | 4.2 | 41% | 0% | – | 201 KB | 0 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,479 | 6,051 | 14.3 | 23% | 20% | 79% | 312 KB | 1 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E D C | 2,455 | 4,503 | 31.0 | 68% | 2% | 100% | 512 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 2,424 | 28,230 | 16.4 | 67% | 0% | 100% | 1,129 KB | 49 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 2,420 | 4,998 | 19.6 | 27% | 20% | 97% | 258 KB | 3 (-1) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 2,376 | 3,009 | 14.5 | 13% | 0% | 94% | 160 KB | 1 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E E C | 2,350 | 15,720 | 14.1 | 55% | 0% | 95% | 431 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E D A | 2,330 | 4,041 | 6.5 | 68% | 0% | 100% | 236 KB | 6 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,255 | 2,545 | 6.2 | 36% | 0% | 98% | 101 KB | 260 (+2) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,201 | 3,328 | 16.9 | 17% | 0% | 97% | 106 KB | 1 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 2,148 | 4,249 | 4.0 | 0% | 0% | 71% | 302 KB | 353 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,107 | 2,825 | 3.0 | 12% | 0% | 95% | 728 KB | 3 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | E F C | 2,064 | 2,086 | 12.1 | 61% | 0% | 99% | 885 KB | 3 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E D D | 2,050 | 2,975 | 0.1 | 62% | 0% | 0% | 606 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 1,961 | 2,862 | 11.4 | 30% | 0% | 100% | 269 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,925 | 2,011 | 10.1 | 78% | 0% | 100% | 361 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 1,873 | 10,704 | 0.0 | 71% | 34% | 42% | 268 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,728 | 4,412 | 14.1 | 33% | 12% | 97% | 386 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F C | 1,688 | 6,294 | 11.5 | 38% | 0% | 54% | 1,263 KB | 13 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E D C | 1,667 | 2,376 | 2.2 | 62% | 0% | 91% | 1,468 KB | 1,119 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 1,640 | 190,254 | 106 | 18% | 10% | 93% | 378 KB | 4 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,614 | 4,598 | 0.0 | 56% | 6% | 69% | 297 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,607 | 2,751 | 9.0 | 59% | 0% | 80% | 1,042 KB | 2 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,582 | 7,415 | 22.0 | 7% | 21% | 95% | 324 KB | 1 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,577 | 5,512 | 0.9 | 52% | 30% | 92% | 5,651 KB | 1 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F C | 1,575 | 3,462 | 17.2 | 31% | 18% | 88% | 677 KB | 2 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E F C | 1,513 | 2,289 | 25.0 | 57% | 0% | 91% | 936 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 1,487 | 76,532 | 11.6 | 44% | 0% | 97% | 1,414 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 1,476 | 10,475 | 0.0 | 29% | 0% | – | 320 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E F D | 1,475 | 12,115 | 2.1 | 32% | 0% | 0% | 6,837 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E F E | 1,401 | 10,759 | 11.5 | 23% | 0% | 99% | 634 KB | 11 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F A | 1,361 | 7,462 | 4.0 | 21% | 0% | 86% | 167 KB | 2 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,315 | 10,491 | 23.2 | 32% | 19% | 96% | 363 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,307 | 3,602 | 7.9 | 0% | 26% | 92% | 518 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,271 | 3,258 | 9.0 | 36% | 0% | 77% | 274 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,214 | 4,778 | 22.3 | 6% | 39% | 98% | 595 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | E F B | 1,143 | 11,135 | 4.0 | 0% | 0% | 90% | 2,640 KB | 46 (+1) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 1,138 | 2,816 | 13.7 | 65% | 0% | 81% | 1,116 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 1,132 | 4,870 | 17.0 | 15% | 35% | 86% | 540 KB | 12 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E E D | 1,031 | 4,023 | 19.0 | 45% | 0% | – | 63 KB | 4 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 973 | 7,651 | 7.1 | 51% | 15% | 98% | 485 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 934 | 1,544 | 0.0 | 52% | 30% | 100% | 515 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 914 | 3,219 | 6.3 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | F F B | 906 | 14,126 | 20.6 | 32% | 0% | 90% | 705 KB | 50 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F E B | 874 | 1,614 | 26.6 | 49% | 22% | 99% | 998 KB | 121 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 861 | 915 | 7.5 | 0% | 0% | 100% | 98 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 852 | 2,157 | 22.0 | 22% | 0% | – | 454 KB | 1 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 848 | 2,044 | 0.0 | 31% | 0% | – | 1,027 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | F F D | 842 | 3,005 | 0.8 | 77% | 0% | 30% | 259 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 833 | 8,092 | 11.8 | 64% | 0% | 100% | 393 KB | 2 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | F F B | 813 | 12,872 | 49.8 | 23% | 14% | 100% | 1,441 KB | 8 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 752 | 1,574 | 10.0 | 0% | 0% | 95% | 105 KB | 3 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 743 | 3,038 | 7.8 | 12% | 0% | 98% | 6,579 KB | 9 (+1) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 709 | 2,801 | 5.5 | 37% | 0% | 100% | 45 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 706 | 5,064 | 5.6 | 29% | 0% | 100% | 100 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F E E | 646 | 61,235 | 0.0 | 60% | 0% | 49% | 194 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 633 | 9,927 | 0.0 | 0% | 0% | 26% | 1,295 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 598 | 1,854 | 9.2 | 65% | 0% | 100% | 453 KB | 14 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 591 | 3,021 | 14.4 | 31% | 0% | 100% | 169 KB | 14 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 511 | 1,733 | 10.1 | 0% | 0% | 99% | 215 KB | 1 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | F F A | 468 | 3,517 | 15.1 | 56% | 0% | 99% | 162 KB | 7 (+1) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 421 | 1,856 | 3.5 | 27% | 0% | 99% | 173 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 420 | 2,059 | 18.7 | 10% | 0% | 100% | 190 KB | 2 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 380 | 12,371 | 16.9 | 33% | 0% | 92% | 149 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 346 | 1,642 | 15.1 | 24% | 0% | 100% | 126 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 346 | 935 | 5.2 | 13% | 23% | 92% | 763 KB | 7 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 289 | 4,032 | 3.0 | 17% | 0% | 94% | 697 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 242 | 14,385 | 3.5 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 224 | 72,109 | 31.9 | 4% | 0% | 11% | 3,975 KB | 1 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 179 | 808 | 7.5 | 31% | 0% | 99% | 271 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 149 | 218 | 0.0 | 0% | 0% | 0% | 673 KB | 3 (+3) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 135 | 420 | 0.0 | 0% | 0% | 93% | 269 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 83 | 707 | 15.6 | 29% | 0% | 96% | 93 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F E | 77 | 21,496 | 4.3 | 34% | 0% | 88% | 23 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,233 | 11.2 | 0% | 88% | 20% | 7,014 KB | 21 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 69 | 1,681 | 3.5 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F D | 50 | 1,572 | 0.0 | 15% | 0% | 33% | 554 KB | 29 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 46 | 3,363 | 10.1 | 8% | 0% | 97% | 249 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 42 | 33,153 | 5.5 | 0% | 0% | 97% | 952 KB | 2 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 18 | 726 | 25.6 | 40% | 0% | 99% | 981 KB | 2 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 18 | 3,390 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 14 | 2,903 | 40.0 | 58% | 0% | 100% | 598 KB | 5 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 14 | 25,074 | 25.4 | 0% | 0% | 99% | 635 KB | 2 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 7 | 5,384 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 5 | 936 | 3.2 | 0% | 0% | 99% | 608 KB | 1 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F C C | 4 | 5,550 | 0.0 | 80% | 28% | 100% | 2,121 KB | 0 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F C B | – | – | 66.7 | 79% | 30% | 100% | 3,196 KB | 160 (+4) |
| [purlis/purlis](https://github.com/purlis/purlis) | F F B | – | – | 55.0 | 55% | 18% | 96% | 965 KB | 12 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F B | 0 | 0 | 48.3 | 0% | 0% | 97% | 1,125 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 17,870 | 34.7 | 64% | 0% | 100% | 178 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 34 | 30.8 | 0% | 0% | 85% | 263 KB | 1,259 (+2) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 1,302 | 24.2 | 43% | 0% | 99% | 703 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 23.5 | 55% | 0% | 89% | 2,290 KB | 1,551 (+5) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | 0 | 5,272 | 20.5 | 19% | 0% | 100% | 192 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 18.4 | – | – | 91% | 306 KB | 7 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 1,719 | 17.9 | 33% | 0% | 99% | 295 KB | 2 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 0 | 1,348 | 17.5 | 32% | 0% | 99% | 578 KB | 2 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 17.3 | – | – | 100% | 703 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 0 | 17.2 | 11% | 0% | 76% | 1,770 KB | 6 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | 0 | 0 | 17.0 | – | – | 100% | 42 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 16.5 | – | – | 79% | 416 KB | 9 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 2,412 | 16.4 | 17% | 0% | 92% | 574 KB | 2 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 16.3 | 39% | 23% | 98% | 1,044 KB | 4 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | 0 | 13,255 | 16.1 | 0% | 0% | 66% | 324 KB | 40,955 (+32) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | F F B | 0 | 47,226 | 15.7 | 3% | 0% | 100% | 261 KB | 2 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 432 | 15.2 | 0% | 0% | 87% | 137 KB | 1 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 531 | 15.0 | 0% | 0% | 76% | 16 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 72 | 12.9 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 12.5 | 0% | 0% | 100% | 154 KB | 4 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 848 | 11.8 | 29% | 0% | 100% | 1,060 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,263 | 11.6 | 0% | 0% | 94% | 943 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 366 | 10.4 | 23% | 0% | 0% | 348 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 4,327 | 9.7 | 28% | 0% | 99% | 221 KB | 7 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 9.4 | – | – | 98% | 165 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 9.3 | 38% | 0% | 88% | 710 KB | 4 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 151 | 9.1 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 998 | 8.6 | 0% | 0% | 96% | 123 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 8.4 | 32% | 0% | 0% | 206 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 2,148 | 7.5 | 0% | 0% | 100% | 168 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F D B | – | – | 7.4 | 61% | 30% | 79% | 86 KB | 7 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 0 | 305 | 7.2 | 0% | 0% | 98% | 48 KB | 2 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,831 | 6.6 | 0% | 0% | 93% | 1,170 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 5.8 | – | – | 100% | 160 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | – | – | 5.5 | – | – | 100% | 25 KB | 19 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | – | – | 5.3 | – | – | 72% | 396 KB | 2 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 22 | 5.2 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 5.1 | – | – | 100% | 41 KB | 2 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 573 | 4.9 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 4.7 | – | – | 100% | 403 KB | 2 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 4.6 | – | – | 99% | 87 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | F F B | 0 | 845 | 4.5 | 0% | 0% | 97% | 551 KB | 12 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 4.4 | – | – | 96% | 99 KB | 1 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 4.4 | – | – | 95% | 385 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 818 | 4.0 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 0 | 4.0 | – | – | 98% | 54 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 15 | 3.6 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 242 | 3.5 | 0% | 0% | 87% | 489 KB | 89 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 2,365 | 3.4 | 0% | 0% | 87% | 739 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 3.2 | – | – | 99% | 98 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 0 | 2.9 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 2.9 | – | – | – | 710 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 6 | 2.8 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 36 | 2.8 | 0% | 0% | 97% | 504 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 2.8 | 0% | 0% | 89% | 163 KB | 15 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 5 | 2.7 | 0% | 0% | 91% | 43 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 2.6 | – | – | 99% | 80 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 2.5 | – | – | 95% | 8,119 KB | 1 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 723 | 2.3 | 0% | 0% | 98% | 104 KB | 4 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 1,404 | 2.1 | 0% | 0% | 88% | 602 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 1,796 | 1.9 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 215 | 1.8 | 85% | 0% | 99% | 156 KB | 2 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 1.5 | – | – | 53% | 3,052 KB | 2 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 1.5 | – | – | 80% | 83 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 1.4 | – | – | 93% | 576 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 7,808 | 1.4 | 0% | 0% | 62% | 46 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 1.3 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 1,492 | 1.0 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 476 | 0.6 | 0% | 0% | – | 14 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 0 | 630 | 0.6 | 0% | 0% | 68% | 52 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.4 | – | – | 96% | 122 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.4 | 46% | 27% | 0% | 13,975 KB | 463 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.2 | – | – | 20% | 154 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.2 | – | – | – | 311 KB | 4 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C C | – | – | 0.2 | 75% | 74% | 69% | 896 KB | 7 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F C | 0 | 373 | 0.1 | 0% | 0% | 88% | 175 KB | 109 (-5) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,341 (+4) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 78% | 9% | 50% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 0 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | – | – | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 369 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.0 | – | – | 98% | 42 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 88% | 33% | 94% | 42,600 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 956 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 58 | 0.0 | 0% | 0% | 6% | 158 KB | 122 (+0) |
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
