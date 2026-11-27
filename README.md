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
_340 repos, last measured 2026-11-27. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (340)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 103,280 | 102,936 | 91.5 | 56% | 28% | 90% | 421 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A D C | 64,271 | 112,900 | 218 | 61% | 20% | 100% | 2,294 KB | 5 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 60,831 | 83,711 | 42.6 | 35% | 16% | 83% | 4,907 KB | 2,139 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A C C | 43,519 | 191,126 | 157 | 86% | 22% | 55% | 316 KB | 4 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B D B | 36,331 | 46,816 | 66.0 | 62% | 0% | 100% | 336 KB | 2 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 32,410 | 42,869 | 21.9 | 46% | 59% | 98% | 2,065 KB | 157 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B C B | 32,274 | 86,413 | 94.2 | 77% | 34% | 97% | 565 KB | 1 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 31,096 | 38,742 | 97.6 | 8% | 40% | 98% | 130 KB | 76 (+1) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 27,688 | 45,889 | 0.0 | 74% | 25% | – | 1,011 KB | 2 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | B D D | 25,161 | 45,659 | 24.9 | 66% | 22% | 0% | 115 KB | 234 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B D D | 25,005 | 31,516 | 0.0 | 64% | 43% | 0% | 4,332 KB | 3 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | B E B | 24,798 | 53,722 | 33.8 | 51% | 41% | 93% | 358 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | B C B | 24,611 | 32,201 | 20.9 | 75% | 61% | 96% | 297 KB | 7 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D C | 23,624 | 31,257 | 134 | 68% | 28% | 95% | 5,251 KB | 0 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | B E C | 22,890 | 78,559 | 0.1 | 68% | 32% | 50% | 574 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | B D B | 22,659 | 25,134 | 42.8 | 64% | 50% | 98% | 660 KB | 1 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B F C | 22,638 | 31,242 | 25.4 | 33% | 42% | 100% | 528 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,905 | 49,365 | 0.0 | 48% | 60% | – | 575 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 21,824 | 38,479 | 40.6 | 70% | 45% | 100% | 898 KB | 5 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B B D | 21,267 | 108,925 | 0.1 | 87% | 32% | 47% | 5,368 KB | 450 (-1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C C C | 19,309 | 32,805 | 19.5 | 77% | 21% | 92% | 363 KB | 11 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | C E B | 18,706 | 43,278 | 44.0 | 59% | 22% | 99% | 617 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C F D | 18,415 | 23,334 | 10.0 | 42% | 28% | 32% | 254 KB | 11 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C C C | 18,037 | 27,773 | 27.1 | 72% | 35% | 99% | 615 KB | 22 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | C F B | 17,467 | 21,689 | 9.2 | 37% | 0% | 100% | 1,133 KB | 1 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | C F B | 17,387 | 30,238 | 101 | 25% | 9% | 93% | 6,167 KB | 91 (+1) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F C | 17,334 | 25,416 | 0.0 | 26% | 18% | 76% | 20,387 KB | 2 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C E D | 16,984 | 106,170 | 0.1 | 47% | 4% | 0% | 255 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 16,933 | 35,606 | 0.0 | 76% | 19% | 0% | 3,286 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | C F B | 16,742 | 30,218 | 32.5 | 18% | 0% | 97% | 527 KB | 1,717 (+10) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 16,437 | 29,586 | 158 | 18% | 0% | 87% | 281 KB | 24 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C F C | 16,030 | 24,005 | 0.0 | 40% | 37% | 100% | 4,357 KB | 15 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C B B | 15,802 | 20,829 | 40.0 | 85% | 50% | 100% | 1,039 KB | 0 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 15,344 | 19,066 | 19.7 | 72% | 37% | 99% | 331 KB | 37 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 62,016 | 30.6 | 45% | 12% | 62% | 65 KB | 3 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 14,492 | 23,421 | 59.9 | 40% | 53% | 84% | 510 KB | 6,766 (+3) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F D | 14,111 | 16,208 | 0.0 | 33% | 20% | 43% | 413 KB | 0 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | C F A | 13,616 | 47,877 | 56.2 | 22% | 3% | 94% | 430 KB | 89 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F C | 12,322 | 29,429 | 8.5 | 31% | 31% | 91% | 637 KB | 19 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 12,318 | 26,623 | 0.0 | 62% | 0% | 28% | 308 KB | 850 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C D C | 12,100 | 12,201 | 30.1 | 67% | 0% | 100% | 473 KB | 10 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 11,737 | 18,414 | 9.4 | 8% | 46% | 99% | 556 KB | 153 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 11,284 | 25,313 | 19.2 | 80% | 18% | 100% | 1,200 KB | 42 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C C B | 11,220 | 13,511 | 0.0 | 71% | 50% | 86% | 265 KB | 137 (+1) |
| [arul28/ADE](https://github.com/arul28/ADE) | C C C | 10,836 | 16,501 | 17.1 | 84% | 9% | 99% | 8,727 KB | 147 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 10,536 | 19,083 | 38.3 | 26% | 12% | 100% | 605 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C C C | 10,465 | 13,686 | 25.6 | 77% | 33% | 100% | 1,067 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | D F D | 9,268 | 20,123 | 0.0 | 11% | 2% | 33% | 1,692 KB | 468 (+2) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 10,444 | 6.9 | 0% | 41% | 87% | 751 KB | 9 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D E A | 9,165 | 12,047 | 26.0 | 44% | 22% | 100% | 267 KB | 1 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 9,042 | 29,640 | 17.8 | 57% | 2% | 98% | 834 KB | 53 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D D C | 8,809 | 15,477 | 5.1 | 63% | 30% | 100% | 2,284 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 8,732 | 13,906 | 67.1 | 66% | 30% | 99% | 263 KB | 8 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 8,288 | 10,979 | 9.6 | 23% | 12% | 100% | 577 KB | 97 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D E A | 8,214 | 16,617 | 18.1 | 57% | 0% | 94% | 155 KB | 3 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | D E C | 7,933 | 10,043 | 33.6 | 59% | 19% | 92% | 3,196 KB | 6 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D F B | 7,933 | 12,810 | 0.0 | 42% | 0% | 77% | 4,244 KB | 7 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | D C B | 7,693 | 16,877 | 26.2 | 85% | 0% | 100% | 597 KB | 8 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 7,605 | 16,136 | 13.8 | 57% | 36% | 94% | 255 KB | 5 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D F B | 7,553 | 59,280 | 8.8 | 54% | 10% | 99% | 339 KB | 6 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D F D | 7,401 | 17,384 | 3.9 | 29% | 1% | 25% | 270 KB | 20 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D F C | 7,264 | 15,067 | 9.9 | 64% | 9% | 61% | 1,265 KB | 13 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D C A | 6,986 | 12,743 | 61.0 | 74% | 0% | 100% | 59 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 6,904 | 7,414 | 10.7 | 32% | 0% | 96% | 544 KB | 0 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 6,899 | 19,329 | 11.9 | 52% | 0% | 100% | 270 KB | 2 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 6,788 | 5,756 | 0.1 | 29% | 6% | 0% | 606 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D E B | 6,685 | 13,221 | 50.9 | 41% | 41% | 82% | 158 KB | 1 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 6,425 | 14,241 | 0.0 | 36% | 42% | 86% | 378 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | D F D | 6,326 | 5,722 | 0.0 | 74% | 0% | 4% | 474 KB | 0 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,302 | 11,742 | 40.0 | 0% | 32% | 99% | 237 KB | 7 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 6,099 | 8,912 | 16.5 | 23% | 0% | 98% | 42 KB | 24,010 (+15) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 6,039 | 16,256 | 0.0 | 62% | 18% | 97% | 717 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,906 | 13,056 | 39.1 | 53% | 30% | 75% | 1,510 KB | 71,141 (+24) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | D F D | 5,778 | 47,742 | 0.1 | 3% | 14% | 45% | 1,312 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 5,714 | 5,455 | 12.2 | 65% | 11% | 97% | 1,162 KB | 9 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 5,681 | 7,565 | 22.8 | 38% | 0% | 100% | 371 KB | 18 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D E B | 5,600 | 8,481 | 21.1 | 81% | 0% | 100% | 158 KB | 5 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D E D | 5,466 | 39,663 | 0.0 | 52% | 0% | – | 1,163 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D C C | 5,347 | 11,484 | 16.5 | 82% | 17% | 62% | 448 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D E D | 5,256 | 11,434 | 0.0 | 53% | 24% | 41% | 1,669 KB | 38 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E D B | 4,967 | 10,004 | 32.7 | 68% | 12% | 100% | 2,578 KB | 5 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 4,730 | 13,494 | 0.3 | 56% | 8% | 98% | 5,692 KB | 1 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E E B | 4,551 | 8,125 | 11.7 | 42% | 18% | 80% | 386 KB | 188 (+1) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,464 | 7,743 | 0.0 | 57% | 38% | 73% | 138 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E C B | 4,400 | 8,796 | 25.9 | 71% | 17% | 99% | 1,944 KB | 3 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 4,396 | 6,389 | 6.5 | 7% | 19% | 93% | 378 KB | 0 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 4,339 | 10,135 | 0.6 | 3% | 12% | 9% | 266 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 4,336 | 8,370 | 16.7 | 9% | 38% | 85% | 68 KB | 66 (+1) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 4,300 | 10,544 | 16.8 | 52% | 12% | 92% | 577 KB | 26 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E D B | 4,289 | 10,869 | 20.0 | 68% | 0% | 85% | 96 KB | 5 (+1) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F C | 4,249 | 18,794 | 3.0 | 24% | 0% | 68% | 3,327 KB | 354 (+1) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F A | 4,218 | 9,933 | 5.7 | 13% | 0% | 90% | 225 KB | 2 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E E F | 4,043 | 67,531 | 0.0 | 42% | 37% | – | 8,190 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | E F B | 3,971 | 14,175 | 17.6 | 36% | 0% | 82% | 340 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 3,946 | 5,875 | 4.0 | 67% | 0% | 97% | 551 KB | 12 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,897 | 4,468 | 13.7 | 32% | 0% | 95% | 168 KB | 1 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | E F B | 3,730 | 17,277 | 34.9 | 63% | 0% | 96% | 2,702 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | E F B | 3,550 | 4,130 | 9.6 | 0% | 0% | 88% | 790 KB | 5 (+1) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F C | 3,507 | 6,810 | 0.0 | 4% | 0% | 89% | 194 KB | 102 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 3,452 | 25,306 | 15.9 | 25% | 0% | 97% | 1,129 KB | 50 (+1) |
| [quadseven/loom](https://github.com/quadseven/loom) | E E C | 3,376 | 3,837 | 21.2 | 56% | 12% | 96% | 1,003 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F C | 3,276 | 5,216 | 14.3 | 54% | 0% | 88% | 688 KB | 2 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 3,248 | 5,605 | 10.6 | 16% | 23% | 100% | 492 KB | 14 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E E B | 3,204 | 13,868 | 38.4 | 67% | 37% | 100% | 76 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E B A | 3,062 | 4,864 | 0.0 | 80% | 18% | 89% | 403 KB | 3 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 2,894 | 4,418 | 79.5 | 56% | 30% | – | 485 KB | 3 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 2,695 | 6,785 | 0.9 | 57% | 0% | 74% | 461 KB | 2 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 2,668 | 6,019 | 28.5 | 58% | 0% | 100% | 64 KB | 3 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | E F B | 2,656 | 4,521 | 12.4 | 35% | 0% | 75% | 61 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 2,643 | 9,915 | 0.0 | 58% | 0% | 42% | 268 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E E E | 2,613 | 9,363 | 24.4 | 59% | 8% | 76% | 1,792 KB | 6 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F C | 2,609 | 7,048 | 16.6 | 34% | 53% | 55% | 540 KB | 12 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 2,563 | 4,857 | 5.2 | 53% | 0% | 92% | 1,116 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,548 | 11,869 | 0.0 | 0% | 0% | – | 228 KB | 31 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,537 | 99,588 | 4.9 | 7% | 0% | 91% | 24 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 2,525 | 3,903 | 3.4 | 29% | 0% | 100% | 181 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 2,343 | 3,705 | 1.8 | 7% | 21% | 87% | 4,444 KB | 575 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | E E D | 2,275 | 9,038 | 0.2 | 40% | 0% | 36% | 52 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 2,242 | 9,224 | 0.0 | 24% | 21% | 72% | 141 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,171 | 3,337 | 6.3 | 56% | 18% | 100% | 100 KB | 261 (+1) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E E B | 2,155 | 7,987 | 0.0 | 64% | 0% | 81% | 590 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 2,013 | 5,499 | 16.5 | 12% | 0% | 98% | 628 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 2,013 | 20,005 | 13.9 | 0% | 0% | 98% | 637 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | E F B | 2,011 | 3,245 | 4.3 | 24% | 0% | 92% | 665 KB | 2 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E F D | 1,959 | 6,874 | 3.9 | 53% | 0% | 0% | 6,837 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 1,948 | 3,809 | 5.5 | 72% | 0% | 99% | 236 KB | 6 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E F A | 1,895 | 32,978 | 19.0 | 33% | 0% | 96% | 43 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E C C | 1,811 | 9,661 | 0.0 | 74% | 80% | 100% | 2,501 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,736 | 4,341 | 7.9 | 35% | 0% | 97% | 53 KB | 2 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,712 | 7,926 | 21.2 | 24% | 0% | 100% | 606 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 1,674 | 3,590 | 20.0 | 50% | 5% | 97% | 393 KB | 1 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,566 | 3,465 | 5.0 | 13% | 0% | 91% | 768 KB | 9 (+1) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E C B | 1,555 | 3,272 | 11.5 | 82% | 16% | 100% | 371 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,545 | 2,365 | 7.9 | 12% | 0% | 100% | 4,314 KB | 42 (+1) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 1,535 | 2,881 | 0.9 | 23% | 0% | 39% | 282 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,503 | 2,074 | 24.2 | 66% | 0% | 98% | 1,009 KB | 127 (+1) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,497 | 17,055 | 21.5 | 29% | 0% | 99% | 363 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 1,395 | 3,750 | 13.4 | 0% | 0% | 97% | 644 KB | 15 (+1) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,392 | 2,469 | 22.6 | 12% | 11% | 99% | 324 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 1,321 | 4,924 | 10.4 | 25% | 10% | 96% | 180 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,307 | 1,850 | 8.1 | 38% | 17% | 83% | 151 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 1,277 | 6,542 | 2.2 | 6% | 0% | 95% | 1,468 KB | 1,125 (+1) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 1,275 | 1,816 | 7.8 | 24% | 0% | 100% | 116 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 1,259 | 5,954 | 21.5 | 56% | 0% | – | 124 KB | 2 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,241 | 15,571 | 11.3 | 31% | 0% | 100% | 951 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,225 | 1,602 | 9.1 | 14% | 0% | 100% | 161 KB | 7 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E E E | 1,183 | 8,096 | 0.0 | 63% | 0% | 46% | 198 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 1,166 | 7,597 | 46.7 | 8% | 58% | 100% | 1,452 KB | 8 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 1,036 | 2,292 | 8.6 | 32% | 0% | 96% | 95 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,004 | 3,839 | 8.5 | 32% | 19% | 85% | 275 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | F F B | 967 | 1,134 | 10.8 | 0% | 0% | 99% | 339 KB | 1 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | F F C | 895 | 2,830 | 6.7 | 46% | 27% | 85% | 1,073 KB | 2 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 889 | 16,303 | 12.3 | 48% | 0% | 76% | 5,530 KB | 41,081 (+23) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 826 | 12,346 | 6.0 | 51% | 0% | 100% | 100 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 815 | 1,014 | 0.0 | 50% | 8% | 100% | 542 KB | 0 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | F F C | 772 | 1,790 | 0.0 | 37% | 0% | 75% | 1,175 KB | 53 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | F F B | 711 | 1,720 | 16.7 | 12% | 0% | 99% | 258 KB | 3 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | F F A | 711 | 5,387 | 14.8 | 55% | 24% | 99% | 262 KB | 8 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 688 | 2,462 | 8.1 | 27% | 0% | 99% | 6,579 KB | 9 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | F F B | 676 | 2,501 | 17.3 | 38% | 0% | 97% | 121 KB | 1 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | F D C | 655 | 2,649 | 29.6 | 63% | 34% | 100% | 512 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 638 | 1,039 | 2.5 | 0% | 0% | 87% | 740 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | F F C | 588 | 14,036 | 18.5 | 16% | 0% | 86% | 523 KB | 21 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 574 | 1,481 | 8.5 | 0% | 0% | 100% | 105 KB | 3 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | F F B | 552 | 2,506 | 15.3 | 22% | 0% | 95% | 644 KB | 3 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 543 | 58,376 | 20.2 | 29% | 30% | 93% | 154 KB | 0 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | F F A | 493 | 1,803 | 51.6 | 46% | 0% | 99% | 29 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 473 | 3,759 | 0.1 | 30% | 10% | – | 67 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 430 | 1,072 | 7.0 | 44% | 0% | 98% | 485 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | F F A | 394 | 4,770 | 23.9 | 80% | 0% | 100% | 136 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | F F A | 394 | 722 | 11.9 | 0% | 18% | 100% | 386 KB | 2 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | F F C | 372 | 1,589 | 11.7 | 52% | 0% | 100% | 431 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 364 | 1,807 | 16.1 | 13% | 0% | 100% | 126 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 357 | 5,459 | 10.8 | 26% | 0% | 98% | 635 KB | 11 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | F F A | 277 | 361 | 41.0 | 0% | 0% | 99% | 340 KB | 1 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 263 | 2,245 | 2.8 | 0% | 0% | 99% | 650 KB | 1 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 225 | 11,086 | 7.0 | 0% | 0% | 97% | 1,414 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 224 | 39,781 | 34.6 | 4% | 0% | 14% | 3,975 KB | 1 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 176 | 274,473 | 101 | 0% | 0% | 87% | 378 KB | 3 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | F F B | 173 | 10,030 | 88.5 | 15% | 0% | 96% | 1,570 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 169 | 691 | 11.9 | 0% | 0% | 97% | 885 KB | 3 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 140 | 1,508 | 0.0 | 0% | 0% | – | 1,044 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 133 | 10,603 | 0.0 | 31% | 0% | 0% | 254 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 127 | 440 | 14.2 | 47% | 0% | – | 454 KB | 1 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | F F B | 112 | 1,871 | 25.3 | 17% | 0% | 82% | 242 KB | 141 (+1) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 54 | 1,800 | 5.6 | 24% | 0% | 100% | 45 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 35 | 3,402 | 12.0 | 0% | 0% | 97% | 185 KB | 16 (+1) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F C | 13 | 641 | 11.3 | 17% | 0% | 99% | 578 KB | 2 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F E B | – | – | 51.7 | 54% | 16% | 78% | 991 KB | 12 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F E B | – | – | 42.8 | 60% | 0% | 99% | 3,196 KB | 167 (+1) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 41 | 31.9 | 44% | 0% | 100% | 178 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | – | – | 30.2 | – | – | 85% | 263 KB | 1,263 (+1) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 0 | 31 | 27.2 | 0% | 0% | 100% | 598 KB | 5 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 22.6 | 56% | 58% | 88% | 2,290 KB | 1,586 (+4) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | – | – | 21.3 | – | – | 99% | 703 KB | 3 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 0 | 98 | 16.1 | 0% | 0% | 100% | 190 KB | 2 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 16.0 | 22% | 39% | 74% | 1,050 KB | 4 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | – | – | 15.8 | – | – | 100% | 192 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | F F D | 0 | 96 | 15.5 | 0% | 0% | – | 63 KB | 3 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 0 | 0 | 15.3 | 0% | 0% | 99% | 981 KB | 2 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 15.2 | – | – | 91% | 306 KB | 8 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 0 | 86 | 14.8 | 0% | 0% | 96% | 316 KB | 159 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 463 | 14.6 | 0% | 0% | 99% | 308 KB | 2 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | – | – | 11.9 | – | – | 100% | 42 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 9.9 | – | – | 100% | 703 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 0 | 208 | 9.6 | 63% | 0% | 32% | 7,014 KB | 21 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 0 | 104 | 9.4 | 0% | 0% | 96% | 75 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 117 | 9.1 | 0% | 0% | 94% | 948 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 0 | 9.0 | 0% | 0% | 100% | 1,060 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 0 | 64 | 8.2 | 0% | 0% | 100% | 269 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 468 | 8.0 | 0% | 0% | 0% | 348 KB | 1 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 0 | 907 | 7.8 | 27% | 0% | 96% | 215 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 973 | 7.3 | 0% | 0% | 100% | 180 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | F F B | 0 | 3,903 | 6.5 | 0% | 0% | 79% | 312 KB | 1 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 6.1 | – | – | 100% | 154 KB | 4 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 6.0 | 24% | 0% | 0% | 206 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 5.7 | 58% | 25% | 91% | 86 KB | 7 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 260 | 5.6 | 0% | 0% | 90% | 577 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 5.4 | – | – | 98% | 165 KB | 0 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 0 | 5.1 | – | – | 44% | 144 KB | 16 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 0 | 2,841 | 5.0 | 0% | 0% | 100% | 370 KB | 0 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F B | 0 | 6,872 | 4.7 | 44% | 0% | 100% | 1,536 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 922 | 4.3 | 0% | 0% | 96% | 127 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 4.2 | – | – | – | 201 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 432 | 4.2 | 0% | 0% | 89% | 2,640 KB | 49 (+1) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 0 | 4.0 | 0% | 0% | 97% | 249 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 48 | 3.6 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 7,970 | 3.4 | 0% | 0% | 91% | 635 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 0 | 3.3 | – | – | 97% | 243 KB | 9 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 3.3 | – | – | 99% | 87 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 0 | 154 | 3.2 | 0% | 0% | 99% | 271 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 0 | 3.2 | – | – | 89% | 489 KB | 89 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 0 | 3.0 | – | – | 68% | 26 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | – | – | 2.9 | – | – | 100% | 101 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 2.8 | – | – | 96% | 99 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 1,892 | 2.7 | 0% | 0% | 95% | 728 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 763 | 2.5 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 0 | 2.4 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 2.4 | – | – | 79% | 416 KB | 9 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 133 | 2.4 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F B | 0 | 845 | 2.4 | 0% | 0% | 84% | 137 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 0 | 14 | 2.2 | 0% | 0% | 94% | 697 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 0 | 2.1 | 0% | 0% | 98% | 104 KB | 4 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 2.0 | – | – | 99% | 98 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 2,555 | 2.0 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 0 | 1.9 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 1.7 | – | – | – | 710 KB | 1 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 1.7 | – | – | 95% | 385 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 1.6 | – | – | 100% | 160 KB | 2 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 6,688 | 1.4 | 0% | 0% | 96% | 46 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 229 | 1.4 | 0% | 0% | 91% | 3,845 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 227 | 1.3 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 309 | 1.2 | 0% | 0% | 100% | 25 KB | 19 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 1.2 | – | – | 100% | 403 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 2,960 | 1.2 | 35% | 0% | 82% | 685 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | – | – | 1.1 | – | – | 91% | 43 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | – | – | 1.1 | – | – | 95% | 66 KB | 4 (+1) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | – | – | 1.1 | – | – | 97% | 504 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | – | – | 0.9 | – | – | 75% | 336 KB | 1 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 0.9 | 18% | 23% | 0% | 1,120 KB | 468 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 329 | 0.7 | 0% | 0% | 94% | 156 KB | 2 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F A | 0 | 4,357 | 0.6 | 0% | 0% | 100% | 29 KB | 0 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 0.5 | – | – | 80% | 83 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | – | – | 0.5 | – | – | – | 56 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | – | – | 0.3 | – | – | 90% | 319 KB | 1 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | – | – | 0.3 | – | – | 89% | 163 KB | 16 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 54% | 82% | 92% | 930 KB | 7 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 51 | 0.1 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.1 | – | – | 20% | 154 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 0.1 | – | – | 100% | 41 KB | 2 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 0 | 638 | 0.0 | 0% | 0% | 71% | 554 KB | 31 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | – | – | 0.0 | – | – | – | 320 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 0.0 | – | – | 95% | 8,119 KB | 1 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 330 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | – | – | 0.0 | – | – | 0% | 673 KB | 3 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 52% | 40% | 56% | 88 KB | 6 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 0 | 93 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 84% | 46% | 94% | 45,801 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 59 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.0 | – | – | 0% | 518 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 0 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 951 | 0.0 | 0% | 0% | 7% | 158 KB | 125 (+0) |
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
