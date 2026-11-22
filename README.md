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
_344 repos, last measured 2026-11-22. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (344)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A F A | 90,586 | 92,563 | 79.1 | 36% | 31% | 90% | 448 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A D A | 56,994 | 71,270 | 68.6 | 64% | 0% | 94% | 429 KB | 87 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | A F B | 41,796 | 55,808 | 108 | 22% | 32% | 92% | 6,076 KB | 88 (+1) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 38,304 | 62,659 | 216 | 28% | 0% | 100% | 2,294 KB | 5 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B D B | 36,909 | 86,623 | 99.4 | 64% | 4% | 96% | 509 KB | 1 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B F B | 35,291 | 67,191 | 32.9 | 30% | 38% | 97% | 4,218 KB | 2,133 (-1) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 32,902 | 116,227 | 160 | 54% | 67% | 55% | 311 KB | 4 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B E C | 32,613 | 41,594 | 17.5 | 69% | 31% | 90% | 8,727 KB | 146 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B D B | 32,100 | 38,944 | 23.6 | 70% | 47% | 100% | 2,010 KB | 158 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B D B | 30,662 | 52,184 | 44.3 | 68% | 70% | 99% | 890 KB | 5 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 27,114 | 41,147 | 0.0 | 71% | 32% | – | 998 KB | 2 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B C D | 26,044 | 2,050,755 | 0.0 | 83% | 46% | 0% | 3,286 KB | 1 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B C D | 25,005 | 35,543 | 0.0 | 79% | 28% | 0% | 4,254 KB | 3 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,905 | 49,365 | 0.0 | 48% | 60% | – | 575 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B E B | 20,641 | 62,009 | 63.3 | 75% | 0% | 100% | 328 KB | 3 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B C B | 20,458 | 37,167 | 17.7 | 72% | 29% | 99% | 834 KB | 51 (+1) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | B F C | 20,430 | 32,666 | 0.0 | 29% | 59% | 87% | 20,387 KB | 2 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B E B | 20,011 | 23,241 | 50.6 | 44% | 42% | 87% | 158 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C D C | 19,907 | 27,585 | 140 | 70% | 55% | 100% | 5,251 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C B B | 19,669 | 24,140 | 25.9 | 82% | 57% | 79% | 597 KB | 7 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 19,555 | 36,207 | 20.5 | 82% | 41% | 91% | 363 KB | 11 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C C | 18,308 | 38,089 | 32.9 | 72% | 27% | 97% | 3,196 KB | 6 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C E A | 18,278 | 24,763 | 156 | 59% | 0% | 99% | 278 KB | 24 (+2) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C B D | 17,674 | 30,578 | 25.9 | 80% | 28% | 28% | 109 KB | 234 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C B B | 17,661 | 139,149 | 92.6 | 82% | 27% | 96% | 1,570 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | C C A | 17,462 | 30,091 | 15.3 | 86% | 19% | 95% | 255 KB | 5 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C C B | 17,457 | 29,386 | 0.0 | 72% | 12% | 84% | 397 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 16,654 | 25,986 | 28.1 | 36% | 22% | 98% | 1,041 KB | 1 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 16,167 | 39,492 | 86.1 | 21% | 34% | 88% | 173 KB | 74 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 15,633 | 22,453 | 40.5 | 34% | 0% | 100% | 605 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C E D | 15,152 | 104,914 | 0.1 | 51% | 0% | 6% | 255 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 62,016 | 30.6 | 45% | 12% | 62% | 65 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 13,679 | 24,186 | 19.8 | 66% | 29% | 99% | 211 KB | 36 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C E B | 13,585 | 21,102 | 43.7 | 52% | 47% | 98% | 999 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 13,495 | 23,268 | 23.0 | 49% | 11% | – | 122 KB | 2 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | C E B | 12,755 | 24,314 | 40.2 | 67% | 21% | 100% | 75 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C D C | 12,666 | 17,078 | 20.0 | 61% | 4% | 96% | 474 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 12,571 | 45,642 | 59.4 | 51% | 42% | 96% | 515 KB | 6,744 (+10) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C F B | 12,509 | 53,873 | 21.6 | 65% | 18% | 100% | 1,195 KB | 41 (+1) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 12,508 | 18,911 | 23.6 | 57% | 36% | 97% | 610 KB | 22 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C D C | 12,126 | 18,541 | 34.6 | 63% | 22% | 100% | 473 KB | 10 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 11,859 | 38,697 | 6.4 | 22% | 49% | 100% | 628 KB | 19 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C C B | 11,519 | 18,261 | 0.1 | 74% | 48% | 84% | 4,075 KB | 7 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | C F D | 10,786 | 32,905 | 0.0 | 0% | 0% | 33% | 1,692 KB | 465 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 10,554 | 26,792 | 32.2 | 26% | 13% | 94% | 330 KB | 1 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [subgentic/coral](https://github.com/subgentic/coral) | C C B | 10,255 | 13,840 | 0.0 | 76% | 38% | 77% | 261 KB | 133 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D F B | 9,940 | 21,501 | 43.5 | 27% | 34% | 74% | 1,526 KB | 71,046 (+15) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D E A | 9,898 | 33,870 | 19.5 | 63% | 18% | 91% | 155 KB | 4 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | D F B | 9,838 | 11,012 | 27.8 | 38% | 0% | 97% | 497 KB | 1,692 (+3) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | D E B | 9,429 | 33,726 | 0.0 | 74% | 0% | 71% | 5,368 KB | 450 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 9,420 | 11,895 | 0.0 | 61% | 5% | 86% | 374 KB | 2 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 12,962 | 6.3 | 10% | 17% | 87% | 745 KB | 9 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 9,131 | 21,441 | 18.6 | 21% | 0% | 84% | 340 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F B | 9,061 | 18,041 | 7.8 | 0% | 0% | 100% | 546 KB | 150 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D E A | 8,876 | 10,640 | 24.3 | 55% | 20% | 90% | 247 KB | 1 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D E D | 8,677 | 40,434 | 0.0 | 67% | 0% | – | 1,119 KB | 0 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D F C | 8,382 | 10,667 | 9.2 | 60% | 0% | 100% | 4,357 KB | 15 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 8,332 | 18,883 | 11.1 | 15% | 5% | 97% | 577 KB | 95 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | D C D | 8,140 | 11,382 | 0.0 | 81% | 8% | 4% | 474 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D C B | 8,049 | 14,965 | 23.9 | 71% | 0% | 99% | 641 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 7,905 | 55,612 | 36.2 | 56% | 14% | 100% | 617 KB | 1 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D E B | 7,564 | 14,061 | 21.8 | 80% | 6% | 95% | 158 KB | 5 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D F B | 7,553 | 90,603 | 8.4 | 55% | 0% | 99% | 339 KB | 6 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 7,532 | 46,789 | 0.0 | 67% | 23% | 50% | 573 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 7,509 | 10,340 | 5.0 | 67% | 0% | 100% | 2,284 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D E D | 7,437 | 29,675 | 7.0 | 53% | 4% | 25% | 268 KB | 16 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 7,418 | 11,860 | 80.6 | 84% | 24% | – | 481 KB | 3 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 7,277 | 8,944 | 12.1 | 21% | 24% | 96% | 544 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E C | 7,264 | 10,787 | 12.3 | 63% | 0% | 58% | 1,263 KB | 13 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 6,995 | 11,801 | 13.4 | 70% | 17% | 98% | 1,160 KB | 8 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | D F B | 6,787 | 10,830 | 2.5 | 30% | 10% | 74% | 461 KB | 2 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 6,785 | 10,338 | 23.4 | 24% | 17% | 100% | 367 KB | 18 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D E A | 6,604 | 9,372 | 48.6 | 66% | 28% | 96% | 59 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | D F A | 6,481 | 13,759 | 61.7 | 74% | 2% | 99% | 29 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D D C | 6,331 | 9,400 | 0.0 | 65% | 48% | 59% | 1,660 KB | 38 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,308 | 14,025 | 42.8 | 12% | 4% | 100% | 237 KB | 7 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D C B | 6,237 | 8,854 | 0.0 | 73% | 49% | 90% | 401 KB | 3 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F D | 6,202 | 10,296 | 0.5 | 5% | 24% | 5% | 284 KB | 1 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 6,099 | 11,057 | 15.4 | 48% | 0% | 98% | 49 KB | 23,980 (+10) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 5,584 | 13,536 | 9.9 | 68% | 51% | 15% | 239 KB | 11 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D E B | 5,211 | 11,335 | 18.9 | 57% | 0% | 91% | 94 KB | 4 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E B B | 4,967 | 9,869 | 37.0 | 81% | 28% | 100% | 2,491 KB | 5 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 4,551 | 6,942 | 12.4 | 30% | 38% | 88% | 391 KB | 186 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 4,464 | 12,175 | 62.7 | 79% | 60% | 100% | 247 KB | 9 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,464 | 7,743 | 0.0 | 57% | 38% | 73% | 138 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,396 | 9,676 | 6.4 | 10% | 18% | 93% | 378 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F B | 4,364 | 8,832 | 4.8 | 21% | 0% | 81% | 201 KB | 2 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 4,336 | 6,059 | 18.2 | 3% | 4% | 99% | 68 KB | 64 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | E F A | 4,318 | 6,333 | 9.9 | 55% | 0% | 100% | 370 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,253 | 4,699 | 14.2 | 22% | 0% | 94% | 164 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,233 | 7,081 | 31.8 | 66% | 0% | 100% | 63 KB | 3 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 4,129 | 8,647 | 0.6 | 50% | 33% | 76% | 5,688 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 4,051 | 27,981 | 0.0 | 36% | 3% | 97% | 709 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E E F | 4,043 | 68,730 | 0.0 | 86% | 0% | – | 8,190 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 3,867 | 21,320 | 0.0 | 23% | 0% | – | 226 KB | 31 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | E F C | 3,759 | 15,168 | 22.3 | 11% | 0% | 85% | 523 KB | 21 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E C C | 3,614 | 9,232 | 17.7 | 77% | 0% | 89% | 529 KB | 26 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 3,605 | 5,022 | 13.3 | 7% | 0% | 97% | 644 KB | 13 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E F A | 3,533 | 36,955 | 18.5 | 50% | 0% | 94% | 42 KB | 0 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 3,509 | 7,120 | 4.4 | 37% | 0% | 100% | 1,536 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 3,452 | 29,232 | 16.1 | 49% | 10% | 99% | 1,129 KB | 49 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E F B | 3,431 | 4,955 | 24.0 | 70% | 0% | 99% | 1,927 KB | 3 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 3,364 | 16,864 | 13.5 | 44% | 0% | 100% | 233 KB | 7 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E F D | 3,235 | 5,340 | 0.1 | 22% | 0% | 0% | 606 KB | 1 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 3,163 | 5,474 | 10.5 | 60% | 0% | 79% | 1,116 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 3,088 | 4,146 | 8.4 | 18% | 52% | 86% | 518 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | E F A | 3,085 | 6,033 | 27.4 | 81% | 0% | 100% | 135 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 2,982 | 4,613 | 15.8 | 54% | 0% | 98% | 628 KB | 1 (+1) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E F B | 2,976 | 26,601 | 0.0 | 36% | 27% | 97% | 590 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,963 | 7,994 | 10.7 | 26% | 0% | 79% | 312 KB | 1 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E E B | 2,861 | 5,627 | 17.0 | 44% | 23% | 87% | 433 KB | 1 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E E C | 2,829 | 3,227 | 21.7 | 67% | 0% | 91% | 962 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 2,754 | 6,184 | 1.7 | 12% | 38% | 90% | 4,322 KB | 570 (+1) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,745 | 3,680 | 6.3 | 40% | 0% | 97% | 102 KB | 260 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,648 | 4,466 | 4.2 | 48% | 0% | – | 201 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,537 | 34,596 | 4.5 | 41% | 0% | 89% | 24 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E D C | 2,505 | 6,131 | 11.1 | 65% | 8% | 95% | 179 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 2,435 | 3,792 | 2.2 | 38% | 38% | 92% | 1,468 KB | 1,120 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,360 | 2,970 | 31.9 | 43% | 3% | 100% | 512 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 2,333 | 11,588 | 7.8 | 69% | 3% | 100% | 4,314 KB | 35 (+1) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E D B | 2,307 | 7,902 | 21.0 | 62% | 7% | 95% | 644 KB | 3 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E E C | 2,282 | 6,859 | 0.0 | 46% | 37% | 75% | 1,175 KB | 51 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 2,242 | 2,689 | 6.1 | 73% | 0% | 99% | 236 KB | 6 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F C | 2,234 | 4,577 | 16.5 | 53% | 16% | 88% | 686 KB | 2 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 2,216 | 2,239 | 13.6 | 68% | 0% | 96% | 431 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 2,162 | 3,858 | 18.8 | 44% | 28% | 97% | 258 KB | 3 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F B | 1,967 | 4,666 | 25.0 | 13% | 0% | 82% | 242 KB | 138 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E F D | 1,959 | 13,193 | 2.9 | 49% | 0% | 0% | 6,837 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 1,949 | 5,631 | 17.8 | 14% | 48% | 88% | 540 KB | 12 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,944 | 12,952 | 11.1 | 6% | 11% | 100% | 932 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 1,803 | 14,413 | 0.0 | 58% | 32% | 42% | 268 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F C | 1,748 | 15,314 | 0.1 | 3% | 0% | 67% | 1,295 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,728 | 4,427 | 13.8 | 29% | 50% | 100% | 386 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 1,649 | 5,903 | 1.5 | 57% | 0% | 82% | 685 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E C B | 1,595 | 1,754 | 10.7 | 78% | 0% | 100% | 361 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,392 | 3,171 | 22.8 | 9% | 39% | 96% | 324 KB | 1 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,367 | 2,003 | 7.8 | 52% | 30% | 87% | 1,054 KB | 2 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,315 | 12,024 | 22.0 | 38% | 0% | 94% | 363 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E C C | 1,291 | 5,871 | 0.0 | 76% | 27% | 100% | 2,184 KB | 0 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,216 | 4,557 | 0.0 | 58% | 6% | 70% | 141 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,214 | 6,794 | 21.5 | 27% | 0% | 99% | 596 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,168 | 4,257 | 11.9 | 54% | 0% | 99% | 161 KB | 7 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,163 | 3,660 | 9.2 | 28% | 16% | 75% | 274 KB | 1 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | E F A | 1,128 | 6,438 | 43.4 | 43% | 0% | 99% | 340 KB | 1 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 1,119 | 2,701 | 2.8 | 0% | 0% | 87% | 740 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,101 | 2,155 | 0.0 | 0% | 0% | – | 1,044 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,088 | 1,970 | 3.6 | 0% | 0% | 99% | 173 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,069 | 34,608 | 5.8 | 38% | 0% | 99% | 1,064 KB | 2 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,059 | 2,037 | 5.6 | 0% | 14% | 93% | 763 KB | 7 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 1,014 | 2,507 | 15.1 | 20% | 0% | 100% | 322 KB | 1 (+1) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F C C | 954 | 1,478 | 0.0 | 70% | 18% | 100% | 523 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | F F B | 889 | 2,254 | 16.8 | 0% | 0% | 97% | 106 KB | 1 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 883 | 226,539 | 104 | 5% | 0% | 90% | 378 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 874 | 1,375 | 25.3 | 48% | 0% | 96% | 1,001 KB | 120 (-1) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 861 | 1,682 | 7.4 | 36% | 0% | 100% | 98 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | F F B | 813 | 12,002 | 48.6 | 39% | 14% | 100% | 1,445 KB | 8 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 782 | 2,488 | 0.6 | 20% | 0% | 0% | 52 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 772 | 1,745 | 12.5 | 42% | 0% | 99% | 393 KB | 2 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 743 | 3,215 | 7.4 | 11% | 0% | 99% | 6,579 KB | 9 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F C | 621 | 4,731 | 0.0 | 1% | 0% | 89% | 195 KB | 104 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | F F A | 618 | 4,096 | 16.6 | 34% | 0% | 96% | 262 KB | 9 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F F A | 598 | 3,219 | 9.7 | 45% | 0% | 100% | 469 KB | 14 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 539 | 7,332 | 7.0 | 20% | 18% | 98% | 485 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 498 | 1,838 | 5.7 | 11% | 0% | 100% | 45 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 386 | 11,792 | 5.8 | 11% | 0% | 100% | 100 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 375 | 10,474 | 17.1 | 34% | 0% | 92% | 149 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 357 | 9,601 | 10.9 | 29% | 0% | 99% | 635 KB | 11 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | F F C | 348 | 4,764 | 2.9 | 0% | 0% | 66% | 303 KB | 351 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 258 | 1,869 | 12.8 | 44% | 0% | 96% | 93 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 252 | 1,345 | 0.0 | 47% | 0% | 33% | 197 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | F F B | 247 | 759 | 4.1 | 27% | 0% | 97% | 553 KB | 12 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 243 | 1,662 | 14.8 | 15% | 0% | 100% | 126 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 234 | 41,450 | 35.7 | 21% | 5% | 11% | 3,975 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 225 | 43,854 | 10.4 | 22% | 0% | 97% | 1,414 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 216 | 1,165 | 10.3 | 30% | 0% | 100% | 269 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 209 | 3,861 | 3.5 | 11% | 0% | 95% | 728 KB | 3 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 179 | 801 | 7.2 | 18% | 0% | 99% | 271 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 169 | 1,151 | 11.7 | 0% | 0% | 99% | 885 KB | 3 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 138 | 1,705 | 11.4 | 0% | 0% | 98% | 74 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | F F D | 132 | 1,328 | 18.8 | 44% | 0% | – | 63 KB | 4 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 123 | 416 | 17.5 | 0% | 0% | 100% | 190 KB | 2 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 113 | 8,847 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,300 | 10.9 | 0% | 88% | 20% | 7,014 KB | 21 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 75 | 3,363 | 2.9 | 19% | 0% | 94% | 697 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 69 | 1,681 | 3.4 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 68 | 161 | 0.0 | 0% | 0% | 0% | 673 KB | 3 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 50 | 290 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 46 | 3,354 | 9.2 | 9% | 0% | 97% | 249 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | F F B | 35 | 28,153 | 14.8 | 0% | 0% | 100% | 267 KB | 2 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 35 | 986 | 13.1 | 47% | 0% | 99% | 178 KB | 15 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 30 | 1,262 | 0.0 | 15% | 0% | – | 66 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 7 | 1,138 | 19.2 | 16% | 0% | – | 454 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 1 | 16,494 | 22.7 | 0% | 0% | 99% | 636 KB | 2 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 1 | 1,719 | 1.3 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F D B | – | – | 59.3 | 61% | 8% | 100% | 3,196 KB | 163 (+1) |
| [purlis/purlis](https://github.com/purlis/purlis) | F F B | – | – | 54.0 | 65% | 24% | 94% | 976 KB | 12 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F B | 0 | 517 | 45.5 | 0% | 0% | 98% | 1,106 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 0 | 101 | 35.8 | 0% | 0% | 100% | 598 KB | 5 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 5,817 | 32.7 | 17% | 0% | 100% | 178 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 0 | 31.2 | – | – | 85% | 263 KB | 1,259 (+1) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 23.8 | 76% | 51% | 90% | 2,290 KB | 1,563 (+4) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 0 | 23.0 | – | – | 99% | 703 KB | 2 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 0 | 664 | 21.6 | 43% | 0% | 99% | 981 KB | 2 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | 0 | 296 | 20.2 | 0% | 0% | 100% | 192 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 0 | 8,641 | 19.1 | 40% | 0% | 93% | 315 KB | 159 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 1,636 | 17.8 | 24% | 0% | 99% | 295 KB | 2 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 0 | 17.6 | 12% | 0% | 76% | 1,770 KB | 6 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 17.1 | – | – | 91% | 306 KB | 7 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 16.2 | 42% | 24% | 99% | 1,046 KB | 4 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | – | – | 15.6 | – | – | 100% | 42 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 0 | 716 | 14.8 | 21% | 0% | 99% | 578 KB | 2 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | – | – | 14.6 | – | – | 66% | 324 KB | 41,006 (+17) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 45 | 13.2 | 46% | 81% | 82% | 29 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 12.9 | – | – | 100% | 703 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 12.1 | – | – | 79% | 416 KB | 9 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 542 | 11.5 | 0% | 0% | 94% | 943 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 0 | 10.5 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 377 | 10.1 | 40% | 0% | 0% | 348 KB | 1 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 1,939 | 10.0 | 27% | 0% | 92% | 576 KB | 2 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 716 | 9.6 | 31% | 0% | 100% | 1,060 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 9.4 | 0% | 0% | 88% | 710 KB | 4 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 0 | 1,599 | 9.2 | 22% | 0% | 96% | 215 KB | 1 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 0 | 1,149 | 9.0 | 0% | 0% | 100% | 105 KB | 3 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 378 | 8.9 | 0% | 0% | 87% | 137 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 1,734 | 8.2 | 0% | 0% | 96% | 127 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 8.1 | 44% | 0% | 0% | 206 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 8.0 | 0% | 0% | 100% | 154 KB | 4 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 7.9 | – | – | 98% | 165 KB | 0 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 37 | 7.8 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 0 | 1,978 | 7.7 | 30% | 0% | 97% | 53 KB | 2 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 7.2 | 60% | 37% | 78% | 86 KB | 7 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 1,746 | 6.9 | 0% | 0% | 100% | 180 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,761 | 5.9 | 0% | 0% | 92% | 1,170 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 1,834 | 5.1 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 573 | 4.5 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 4.3 | – | – | 96% | 99 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 4.2 | – | – | 100% | 160 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | – | – | 4.1 | – | – | 100% | 25 KB | 19 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 9,560 | 4.0 | 0% | 0% | 90% | 2,640 KB | 47 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 48 | 3.7 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 3.5 | – | – | 99% | 87 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 3.4 | – | – | 95% | 385 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 2,969 | 3.2 | 0% | 0% | 100% | 399 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 0 | 3.2 | – | – | 87% | 489 KB | 89 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 3.1 | – | – | 100% | 403 KB | 2 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 3.0 | – | – | 99% | 98 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 18 | 2.9 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 0 | 868 | 2.8 | 0% | 0% | 99% | 608 KB | 1 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 2.7 | – | – | – | 710 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 763 | 2.6 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 36 | 2.6 | 0% | 0% | 97% | 504 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 5 | 2.5 | 0% | 0% | 91% | 43 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 0 | 2.5 | – | – | 95% | 66 KB | 3 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 6 | 2.5 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 2.4 | – | – | 89% | 163 KB | 15 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 0 | 2.2 | – | – | 98% | 104 KB | 4 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 2.1 | – | – | 100% | 41 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 129 | 1.9 | 0% | 0% | 86% | 629 KB | 2 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 1,586 | 1.7 | 0% | 0% | 91% | 3,845 KB | 1 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 0 | 1.5 | – | – | 75% | 336 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 5,155 | 1.4 | 0% | 0% | 76% | 46 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 1.2 | – | – | 99% | 80 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 307 | 1.2 | 0% | 0% | 95% | 156 KB | 2 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 0.9 | – | – | 80% | 83 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 0.9 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | F F D | 0 | 700 | 0.8 | 36% | 0% | 36% | 272 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 0 | 0.5 | – | – | 100% | 28 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 0.5 | 34% | 38% | 0% | 1,110 KB | 467 (+3) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 0.2 | – | – | 95% | 8,119 KB | 1 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.2 | 72% | 83% | 87% | 900 KB | 7 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.1 | – | – | 20% | 154 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 0.1 | – | – | 53% | 3,052 KB | 2 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 61% | 7% | 50% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 0 | 0.0 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.0 | – | – | – | 311 KB | 4 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F D | 0 | 604 | 0.0 | 0% | 0% | 48% | 554 KB | 31 (+1) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | 0 | 2,777 | 0.0 | 43% | 0% | – | 320 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | 0 | 4,949 | 0.0 | 12% | 0% | 28% | 308 KB | 849 (+1) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 0 | 5,349 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 82% | 39% | 94% | 44,100 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 59 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 0 | 0.0 | – | – | 6% | 158 KB | 123 (+1) |
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
