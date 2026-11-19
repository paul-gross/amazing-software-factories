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
_350 repos, last measured 2026-11-19. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (350)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 90,414 | 103,019 | 76.1 | 69% | 47% | 87% | 418 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A C B | 71,813 | 96,643 | 63.6 | 76% | 3% | 100% | 326 KB | 3 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 39,609 | 1,333,736 | 0.0 | 84% | 47% | 0% | 3,286 KB | 1 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 39,209 | 50,569 | 15.3 | 37% | 32% | 97% | 8,727 KB | 144 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B C B | 36,140 | 68,993 | 85.4 | 76% | 4% | 93% | 503 KB | 1 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 32,902 | 116,227 | 160 | 54% | 67% | 55% | 311 KB | 4 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B F B | 32,512 | 52,501 | 37.6 | 61% | 19% | 100% | 3,820 KB | 2,128 (+2) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 31,660 | 57,063 | 225 | 34% | 0% | 97% | 2,437 KB | 5 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B E D | 31,102 | 45,323 | 0.0 | 61% | 28% | 0% | 3,899 KB | 3 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 29,484 | 55,526 | 48.0 | 80% | 35% | 99% | 882 KB | 5 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 29,028 | 54,787 | 0.0 | 70% | 55% | – | 1,152 KB | 2 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B F A | 27,928 | 32,104 | 63.6 | 12% | 1% | 94% | 429 KB | 87 (+1) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | B C D | 25,747 | 141,415 | 0.0 | 77% | 0% | 28% | 308 KB | 846 (+2) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B F B | 25,219 | 31,001 | 28.1 | 33% | 24% | 97% | 497 KB | 1,685 (+8) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E D | 24,359 | 75,092 | 0.0 | 49% | 0% | 46% | 5,368 KB | 450 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | B C C | 23,858 | 83,267 | 32.4 | 73% | 10% | 62% | 147 KB | 3 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 23,121 | 33,064 | 24.4 | 58% | 46% | 97% | 1,927 KB | 159 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B E B | 21,577 | 40,072 | 0.1 | 52% | 23% | 85% | 3,966 KB | 7 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,238 | 35,548 | 0.0 | 41% | 43% | – | 544 KB | 2 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | B C C | 21,213 | 42,026 | 32.0 | 72% | 31% | 100% | 3,196 KB | 6 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B F B | 20,850 | 26,550 | 52.0 | 39% | 46% | 95% | 158 KB | 1 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | B D A | 20,730 | 44,958 | 0.0 | 66% | 20% | 85% | 392 KB | 0 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B E B | 20,324 | 145,769 | 71.0 | 40% | 14% | 97% | 1,554 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F C | 19,023 | 27,665 | 0.0 | 25% | 19% | 85% | 20,387 KB | 2 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | C C A | 18,800 | 26,915 | 13.9 | 82% | 39% | 94% | 254 KB | 5 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | C F B | 18,202 | 29,539 | 101 | 30% | 38% | 92% | 5,972 KB | 85 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 17,773 | 45,784 | 7.2 | 15% | 31% | 96% | 617 KB | 19 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C B B | 17,686 | 20,076 | 24.9 | 83% | 44% | 90% | 597 KB | 6 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 17,544 | 17,684 | 0.0 | 71% | 7% | 2% | 469 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C E C | 17,250 | 33,176 | 38.6 | 41% | 33% | 68% | 1,503 KB | 70,994 (+14) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C C | 17,075 | 33,268 | 27.9 | 78% | 28% | 51% | 103 KB | 234 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 16,894 | 71,862 | 0.0 | 44% | 35% | – | 1,119 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 16,658 | 23,353 | 24.2 | 45% | 36% | 100% | 606 KB | 22 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 15,815 | 37,666 | 90.9 | 59% | 34% | 97% | 360 KB | 74 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 15,743 | 37,279 | 23.5 | 42% | 35% | 100% | 1,178 KB | 39 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C E A | 15,667 | 22,970 | 154 | 56% | 28% | 100% | 258 KB | 22 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | C F D | 15,539 | 30,261 | 0.0 | 5% | 0% | 33% | 284 KB | 465 (+1) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 15,212 | 28,145 | 21.3 | 78% | 26% | 100% | 198 KB | 35 (+1) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 14,623 | 20,999 | 22.0 | 31% | 60% | – | 122 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C C B | 14,494 | 22,657 | 133 | 77% | 56% | 100% | 2,581 KB | 0 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C D B | 14,108 | 17,459 | 42.3 | 63% | 55% | 98% | 957 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 13,823 | 32,862 | 21.2 | 87% | 20% | 86% | 363 KB | 11 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 13,802 | 27,445 | 33.6 | 74% | 14% | 100% | 469 KB | 10 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 12,165 | 17,195 | 28.0 | 35% | 7% | 99% | 1,012 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C D D | 11,004 | 15,987 | 0.0 | 65% | 64% | 13% | 1,652 KB | 38 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 10,840 | 15,165 | 28.3 | 64% | 0% | 100% | 135 KB | 1 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 10,600 | 22,859 | 7.6 | 0% | 0% | 100% | 535 KB | 142 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C C A | 10,564 | 17,671 | 71.5 | 86% | 21% | 92% | 28 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 10,554 | 24,052 | 40.4 | 27% | 2% | 100% | 281 KB | 1 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | C C A | 10,503 | 14,269 | 23.1 | 72% | 36% | 93% | 229 KB | 1 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | C F B | 10,169 | 39,247 | 17.5 | 57% | 0% | 99% | 1,129 KB | 49 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C F B | 10,164 | 42,717 | 61.5 | 35% | 40% | 75% | 510 KB | 6,720 (+4) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C C D | 10,075 | 13,398 | 84.4 | 72% | 3% | – | 476 KB | 3 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D D B | 9,712 | 14,415 | 40.9 | 69% | 41% | 100% | 2,473 KB | 5 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | D F B | 9,663 | 18,143 | 3.2 | 48% | 4% | 99% | 1,488 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D A C | 9,645 | 12,822 | 0.0 | 93% | 6% | 100% | 4,357 KB | 15 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | D E B | 9,324 | 16,085 | 25.0 | 56% | 7% | 97% | 608 KB | 3 (+3) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D E A | 9,321 | 21,715 | 19.0 | 76% | 16% | 87% | 155 KB | 4 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D C B | 9,308 | 16,499 | 15.3 | 76% | 27% | 100% | 1,145 KB | 9 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D E B | 9,256 | 16,014 | 6.8 | 56% | 22% | 85% | 742 KB | 9 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | D E A | 9,108 | 8,490 | 12.4 | 52% | 0% | 100% | 370 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C A | 9,029 | 12,126 | 45.4 | 71% | 12% | 99% | 338 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 8,935 | 12,802 | 18.2 | 34% | 0% | 97% | 262 KB | 9 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 8,647 | 9,939 | 14.0 | 16% | 0% | 97% | 631 KB | 13 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D E A | 8,631 | 26,213 | 18.2 | 45% | 0% | 92% | 303 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 8,490 | 9,423 | 9.3 | 68% | 0% | 88% | 710 KB | 4 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D D B | 8,451 | 56,926 | 32.1 | 67% | 15% | 98% | 617 KB | 1 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D F D | 8,208 | 49,182 | 9.1 | 48% | 0% | 25% | 250 KB | 16 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D D A | 8,203 | 58,892 | 19.5 | 68% | 31% | 94% | 41 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D F B | 8,059 | 21,071 | 35.6 | 70% | 0% | 100% | 178 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | D C D | 8,041 | 21,216 | 0.1 | 74% | 2% | 0% | 255 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | D D C | 7,860 | 18,757 | 20.1 | 66% | 12% | 100% | 425 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D F B | 7,693 | 14,422 | 18.8 | 37% | 2% | 72% | 105 KB | 4 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D F B | 7,614 | 18,757 | 25.1 | 44% | 0% | 99% | 1,902 KB | 3 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 7,569 | 33,097 | 0.0 | 70% | 4% | 97% | 650 KB | 0 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 7,509 | 13,412 | 5.3 | 23% | 0% | 100% | 2,284 KB | 0 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | D C B | 7,235 | 14,810 | 0.0 | 76% | 35% | 86% | 225 KB | 133 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 7,130 | 17,430 | 19.4 | 49% | 4% | 93% | 315 KB | 159 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 7,113 | 25,735 | 0.0 | 68% | 20% | 50% | 570 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | D F A | 6,888 | 17,773 | 29.5 | 12% | 0% | 86% | 242 KB | 137 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D E B | 6,735 | 7,055 | 15.3 | 42% | 0% | 96% | 609 KB | 1 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 6,722 | 11,032 | 13.3 | 41% | 32% | 94% | 388 KB | 184 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 6,637 | 12,629 | 12.1 | 0% | 0% | 98% | 574 KB | 96 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | D D C | 6,417 | 12,516 | 0.0 | 63% | 31% | 75% | 1,175 KB | 51 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D B B | 5,916 | 7,598 | 0.0 | 84% | 65% | 82% | 399 KB | 3 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F D | 5,913 | 10,411 | 0.4 | 8% | 39% | 0% | 283 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D F A | 5,781 | 6,773 | 29.3 | 78% | 0% | 95% | 59 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D E B | 5,618 | 8,742 | 17.9 | 59% | 19% | 91% | 425 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 5,409 | 78,035 | 12.1 | 34% | 5% | 97% | 1,414 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 5,364 | 18,145 | 43.9 | 0% | 5% | 100% | 235 KB | 7 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E E C | 4,961 | 8,242 | 22.6 | 42% | 18% | 100% | 388 KB | 18 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E E B | 4,924 | 23,027 | 40.2 | 46% | 20% | 100% | 75 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 4,660 | 8,762 | 20.3 | 39% | 0% | 94% | 49 KB | 23,945 (+12) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E B B | 4,562 | 7,374 | 51.8 | 84% | 62% | 100% | 235 KB | 9 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E F D | 4,431 | 7,612 | 68.2 | 81% | 10% | – | 294 KB | 3 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E E C | 4,266 | 9,010 | 17.9 | 55% | 42% | 100% | 628 KB | 0 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 4,120 | 3,691 | 18.8 | 15% | 0% | 100% | 322 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,100 | 63,047 | 16.7 | 3% | 0% | 100% | 261 KB | 2 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,008 | 10,980 | 7.5 | 5% | 13% | 93% | 378 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 4,002 | 7,309 | 0.0 | 48% | 9% | 73% | 137 KB | 1 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,873 | 11,313 | 0.1 | 12% | 8% | 86% | 411 KB | 2 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | E F C | 3,759 | 12,054 | 23.5 | 30% | 0% | 86% | 521 KB | 21 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 3,688 | 16,676 | 11.7 | 43% | 8% | 100% | 913 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | E F D | 3,656 | 9,973 | 10.2 | 56% | 0% | 3% | 229 KB | 11 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E E C | 3,614 | 17,656 | 15.8 | 64% | 0% | 88% | 479 KB | 25 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 3,561 | 6,568 | 11.4 | 0% | 0% | 98% | 544 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 3,421 | 4,959 | 38.9 | 7% | 0% | 100% | 66 KB | 3 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | E F B | 3,367 | 14,560 | 21.2 | 40% | 0% | 99% | 158 KB | 5 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 3,349 | 4,588 | 13.1 | 28% | 8% | 98% | 74 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 2,982 | 3,649 | 0.8 | 57% | 11% | 28% | 257 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E E F | 2,910 | 91,157 | 0.0 | 54% | 0% | – | 8,190 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E E D | 2,905 | 39,782 | 0.0 | 59% | 0% | – | 216 KB | 31 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 2,773 | 6,845 | 2.1 | 62% | 35% | 88% | 4,247 KB | 562 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E F B | 2,723 | 24,489 | 0.0 | 31% | 0% | 96% | 590 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 2,694 | 5,298 | 10.9 | 58% | 47% | 88% | 173 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,648 | 4,843 | 4.2 | 41% | 0% | – | 201 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F B | 2,541 | 8,706 | 21.4 | 11% | 0% | 100% | 192 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 2,523 | 55,300 | 7.0 | 77% | 0% | 100% | 1,179 KB | 6 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E E D | 2,521 | 3,960 | 0.1 | 56% | 0% | 0% | 601 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,479 | 6,348 | 15.2 | 0% | 21% | 80% | 312 KB | 1 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 2,397 | 3,606 | 8.8 | 26% | 0% | 78% | 274 KB | 1 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 2,376 | 3,080 | 14.5 | 39% | 0% | 87% | 158 KB | 1 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,360 | 3,252 | 30.4 | 70% | 2% | 100% | 512 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 2,350 | 16,649 | 14.2 | 56% | 0% | 95% | 431 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,298 | 2,935 | 22.0 | 28% | 0% | – | 454 KB | 1 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 2,242 | 13,469 | 34.2 | 2% | 0% | 100% | 605 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 2,242 | 3,260 | 12.0 | 33% | 0% | 100% | 269 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 2,231 | 4,938 | 17.8 | 0% | 6% | 96% | 68 KB | 64 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,201 | 3,091 | 17.0 | 18% | 0% | 97% | 106 KB | 1 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 2,162 | 4,055 | 20.6 | 31% | 0% | 97% | 258 KB | 4 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 2,148 | 2,967 | 4.1 | 0% | 0% | 71% | 302 KB | 353 (+3) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E E D | 2,137 | 4,855 | 19.2 | 45% | 6% | – | 63 KB | 4 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,107 | 2,825 | 3.2 | 12% | 0% | 94% | 728 KB | 3 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E D A | 2,092 | 3,691 | 6.4 | 70% | 0% | 99% | 236 KB | 5 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | E F C | 2,064 | 5,004 | 11.4 | 24% | 0% | 99% | 885 KB | 3 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E D D | 1,980 | 10,800 | 0.0 | 68% | 36% | 42% | 268 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 1,968 | 4,823 | 12.7 | 38% | 0% | 70% | 169 KB | 2 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 1,949 | 5,715 | 17.3 | 51% | 33% | 84% | 540 KB | 12 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,925 | 3,382 | 10.5 | 76% | 0% | 100% | 361 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,842 | 8,072 | 22.6 | 11% | 18% | 96% | 322 KB | 1 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E F D | 1,831 | 58,925 | 1.9 | 14% | 0% | 0% | 6,837 KB | 1 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,728 | 4,362 | 14.5 | 36% | 0% | 97% | 386 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F C | 1,688 | 3,869 | 11.1 | 61% | 0% | 57% | 1,261 KB | 13 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,607 | 4,384 | 9.3 | 69% | 0% | 77% | 1,042 KB | 2 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,591 | 11,193 | 5.8 | 51% | 0% | 100% | 4,314 KB | 35 (+1) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F B | 1,572 | 1,890 | 16.4 | 41% | 21% | 86% | 670 KB | 2 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E F C | 1,513 | 2,130 | 26.4 | 62% | 0% | 94% | 924 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | E F B | 1,476 | 16,168 | 20.9 | 29% | 6% | 89% | 705 KB | 50 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 1,476 | 10,475 | 0.0 | 29% | 0% | – | 320 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,403 | 5,018 | 1.0 | 54% | 11% | 92% | 5,637 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,382 | 2,185 | 10.0 | 8% | 0% | 95% | 105 KB | 3 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F A | 1,297 | 4,794 | 3.1 | 23% | 0% | 85% | 167 KB | 2 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E E E | 1,220 | 61,598 | 0.0 | 61% | 0% | 50% | 192 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,180 | 4,722 | 3.1 | 18% | 0% | 94% | 697 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,160 | 4,726 | 22.7 | 12% | 30% | 98% | 595 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,160 | 3,415 | 8.0 | 0% | 0% | 93% | 518 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | E F B | 1,143 | 11,135 | 4.0 | 0% | 0% | 90% | 2,640 KB | 45 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 1,088 | 6,680 | 15.2 | 5% | 0% | 99% | 169 KB | 13 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 1,017 | 1,594 | 7.5 | 74% | 26% | 98% | 485 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 1,003 | 3,693 | 41.2 | 48% | 0% | 100% | 598 KB | 5 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,003 | 3,279 | 0.0 | 46% | 9% | 70% | 304 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F E C | 985 | 1,864 | 2.2 | 41% | 0% | 90% | 1,468 KB | 1,119 (-1) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 934 | 1,521 | 0.0 | 51% | 59% | 100% | 515 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 920 | 2,598 | 21.4 | 12% | 0% | 100% | 190 KB | 2 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 914 | 3,223 | 6.9 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 902 | 8,760 | 24.1 | 42% | 18% | 98% | 363 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 883 | 153,591 | 110 | 5% | 0% | 92% | 378 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 874 | 2,052 | 26.4 | 35% | 14% | 97% | 998 KB | 121 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 848 | 2,237 | 0.0 | 35% | 0% | – | 1,027 KB | 1 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 833 | 11,429 | 11.9 | 79% | 0% | 96% | 393 KB | 2 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | F F B | 813 | 14,577 | 48.9 | 35% | 10% | 100% | 1,439 KB | 8 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | F F A | 725 | 3,500 | 15.7 | 58% | 0% | 99% | 162 KB | 6 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 723 | 1,760 | 7.4 | 30% | 0% | 98% | 6,579 KB | 8 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 709 | 2,809 | 6.1 | 36% | 0% | 100% | 45 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 706 | 4,889 | 5.4 | 35% | 0% | 100% | 100 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 703 | 2,668 | 24.8 | 15% | 0% | 94% | 573 KB | 2 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 633 | 10,694 | 0.0 | 0% | 0% | 0% | 1,276 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F E A | 598 | 1,580 | 9.3 | 67% | 0% | 98% | 451 KB | 14 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 560 | 2,188 | 14.1 | 32% | 0% | 84% | 1,116 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 511 | 1,733 | 11.1 | 0% | 0% | 99% | 215 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 456 | 8,663 | 11.6 | 26% | 0% | 99% | 634 KB | 11 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 438 | 73,465 | 31.5 | 4% | 0% | 73% | 3,975 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 421 | 1,303 | 3.4 | 0% | 0% | 100% | 173 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 405 | 4,069 | 10.8 | 21% | 0% | 97% | 249 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 348 | 12,244 | 16.6 | 14% | 0% | 94% | 149 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 258 | 590 | 7.8 | 0% | 0% | 100% | 98 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 252 | 739 | 16.2 | 29% | 0% | 96% | 93 KB | 0 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 250 | 1,846 | 9.5 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 241 | 1,501 | 19.1 | 17% | 0% | 99% | 295 KB | 2 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F D | 232 | 1,764 | 0.0 | 13% | 0% | 33% | 554 KB | 29 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 228 | 886 | 27.9 | 37% | 0% | 99% | 981 KB | 2 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 204 | 694 | 4.9 | 21% | 37% | 91% | 677 KB | 7 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 179 | 808 | 7.9 | 31% | 0% | 97% | 270 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 130 | 2,321 | 2.7 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 123 | 25,101 | 26.4 | 17% | 0% | 100% | 635 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 118 | 3,228 | 2.3 | 31% | 0% | 78% | 656 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 103 | 1,424 | 2.1 | 16% | 0% | 88% | 602 KB | 2 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 91 | 838 | 0.5 | 0% | 0% | 100% | 52 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F E | 77 | 23,949 | 4.2 | 34% | 0% | 88% | 23 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,197 | 11.3 | 0% | 100% | 21% | 7,014 KB | 21 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 63 | 1,469 | 6.0 | 57% | 0% | 99% | 102 KB | 258 (+3) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 50 | 274 | 0.0 | 0% | 0% | 93% | 269 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 39 | 8,388 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 9 | 33,465 | 5.5 | 0% | 0% | 96% | 941 KB | 2 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 8 | 835 | 15.1 | 0% | 0% | 100% | 126 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F C C | 4 | 2,949 | 0.0 | 79% | 81% | 100% | 2,083 KB | 0 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F D B | – | – | 69.9 | 67% | 28% | 100% | 3,196 KB | 155 (+15) |
| [purlis/purlis](https://github.com/purlis/purlis) | F E B | – | – | 55.6 | 61% | 16% | 100% | 964 KB | 12 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F D | 0 | 0 | 52.2 | – | – | 100% | 1,122 KB | 0 (-1) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 34 | 28.9 | 0% | 0% | 85% | 263 KB | 1,257 (+2) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 3,796 | 26.6 | 76% | 0% | 99% | 703 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 23.6 | 44% | 0% | 90% | 2,290 KB | 1,546 (+6) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 19.6 | – | – | 100% | 703 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 18.8 | – | – | 79% | 416 KB | 9 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | 0 | 528 | 18.8 | 0% | 0% | 100% | 42 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 0 | 1,472 | 18.5 | 14% | 0% | 99% | 578 KB | 2 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 18.2 | – | – | 91% | 306 KB | 7 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 0 | 18.0 | 63% | 0% | 76% | 1,770 KB | 6 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 432 | 17.0 | 0% | 0% | 87% | 137 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 16.5 | 49% | 33% | 92% | 1,044 KB | 4 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 3,053 | 16.3 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 683 | 16.0 | 22% | 0% | 76% | 16 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | 0 | 16,521 | 15.9 | 50% | 0% | 66% | 324 KB | 40,923 (+32) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 13.7 | 39% | 0% | 100% | 154 KB | 4 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 848 | 12.6 | 29% | 0% | 100% | 1,060 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,263 | 12.1 | 0% | 0% | 94% | 935 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 349 | 11.1 | 24% | 0% | 0% | 348 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 10.8 | 51% | 32% | 96% | 86 KB | 7 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | 0 | 0 | 10.0 | – | – | 98% | 165 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 185 | 9.0 | 0% | 0% | 96% | 123 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 8.4 | 32% | 0% | 0% | 206 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 1,483 | 8.4 | 0% | 0% | 97% | 221 KB | 7 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 0 | 605 | 7.9 | 0% | 0% | 99% | 43 KB | 2 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 2,591 | 7.9 | 0% | 0% | 100% | 168 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,348 | 7.0 | 36% | 0% | 94% | 1,170 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 125 | 6.5 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 5.8 | – | – | 100% | 160 KB | 2 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 5.6 | – | – | 100% | 41 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | – | – | 5.6 | – | – | 100% | 25 KB | 19 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 0 | 5.6 | – | – | 99% | 87 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | – | – | 5.3 | – | – | 72% | 396 KB | 2 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 5.2 | – | – | 100% | 403 KB | 2 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 573 | 4.9 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 0 | 66 | 4.7 | 0% | 0% | 95% | 385 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | F F B | 0 | 705 | 4.7 | 0% | 0% | 97% | 550 KB | 12 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 15 | 4.6 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 4.6 | – | – | 95% | 8,119 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 4.6 | – | – | 99% | 98 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 4.5 | – | – | 99% | 80 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 4.5 | – | – | 96% | 99 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 0 | 4.5 | – | – | 98% | 54 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 320 | 4.1 | 0% | 0% | 87% | 489 KB | 89 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 927 | 4.0 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 1,779 | 3.6 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 13,541 | 3.5 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 0 | 935 | 3.4 | 0% | 0% | 99% | 608 KB | 1 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 1,791 | 3.4 | 0% | 0% | 86% | 739 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 6 | 3.2 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 36 | 3.2 | 0% | 0% | 97% | 504 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 3.1 | 0% | 0% | 89% | 163 KB | 15 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 38 | 3.0 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 3.0 | – | – | – | 710 KB | 1 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 5 | 2.9 | 0% | 0% | 91% | 43 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 2.6 | – | – | 93% | 576 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 2.6 | – | – | 80% | 83 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 726 | 2.3 | 0% | 0% | 98% | 104 KB | 4 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F C C | 0 | 172 | 2.1 | 86% | 0% | 98% | 156 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 1.5 | – | – | 53% | 3,052 KB | 2 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 9,408 | 1.4 | 0% | 0% | 60% | 46 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 1.4 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 1,276 | 1.1 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 476 | 0.9 | 0% | 0% | – | 14 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.4 | – | – | – | 311 KB | 4 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.4 | – | – | 96% | 122 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.4 | 44% | 65% | 0% | 2,040 KB | 463 (-1) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.2 | – | – | 20% | 154 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F C | 0 | 352 | 0.1 | 0% | 0% | 82% | 175 KB | 114 (+25) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.1 | 74% | 76% | 90% | 895 KB | 7 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,337 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 61% | 12% | 50% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 0 | 0.0 | – | – | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | – | – | 0.0 | – | – | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F F | 0 | 0 | 0.0 | – | – | – | – | 0 (-3) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 161 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 3,281 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.0 | – | – | 69% | 290 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.0 | – | – | 98% | 42 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.0 | 70% | 36% | 94% | 42,342 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 2,875 | 0.0 | 24% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 0 | 0.0 | – | – | – | 110 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 4,267 | 0.0 | 20% | 0% | 6% | 158 KB | 122 (+0) |
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
