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
_344 repos, last measured 2026-11-24. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (344)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A F A | 94,951 | 106,194 | 83.6 | 34% | 26% | 90% | 384 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A E A | 63,465 | 76,446 | 64.5 | 66% | 0% | 94% | 430 KB | 88 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 58,194 | 74,690 | 35.0 | 38% | 27% | 92% | 4,263 KB | 2,133 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A E C | 46,389 | 86,627 | 225 | 55% | 54% | 100% | 2,294 KB | 5 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | A F B | 41,796 | 49,751 | 103 | 25% | 7% | 85% | 6,125 KB | 89 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 36,456 | 164,123 | 153 | 82% | 26% | 55% | 316 KB | 4 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C B | 36,189 | 54,471 | 43.1 | 74% | 69% | 100% | 890 KB | 5 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B C B | 32,316 | 86,096 | 97.4 | 72% | 17% | 99% | 538 KB | 1 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 25,512 | 46,263 | 86.7 | 18% | 52% | 96% | 127 KB | 74 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 25,283 | 1,753,877 | 0.0 | 86% | 20% | 0% | 3,286 KB | 0 (-1) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B C D | 25,005 | 33,912 | 0.0 | 77% | 28% | 0% | 4,298 KB | 3 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 24,222 | 37,832 | 0.0 | 72% | 26% | – | 1,003 KB | 2 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 23,202 | 34,995 | 22.8 | 56% | 58% | 96% | 2,032 KB | 157 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D C | 23,159 | 28,608 | 137 | 65% | 33% | 93% | 5,251 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 23,030 | 22,657 | 24.9 | 87% | 8% | 87% | 597 KB | 7 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | B D D | 22,262 | 51,627 | 0.0 | 68% | 49% | 28% | 308 KB | 851 (+2) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,905 | 49,365 | 0.0 | 48% | 60% | – | 575 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B E B | 20,639 | 39,630 | 64.8 | 80% | 0% | 92% | 330 KB | 2 (-1) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | B F C | 20,430 | 32,840 | 0.0 | 29% | 59% | 86% | 20,387 KB | 2 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B F B | 20,011 | 23,095 | 51.8 | 36% | 44% | 82% | 158 KB | 1 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 19,552 | 37,979 | 20.4 | 85% | 39% | 90% | 363 KB | 11 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C F D | 18,735 | 108,368 | 0.1 | 38% | 0% | 8% | 255 KB | 0 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 18,566 | 24,871 | 159 | 61% | 0% | 100% | 279 KB | 24 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C D C | 18,037 | 23,071 | 24.5 | 66% | 39% | 98% | 615 KB | 22 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | C E B | 17,821 | 23,523 | 16.9 | 66% | 0% | 93% | 297 KB | 7 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C E D | 17,674 | 39,617 | 25.4 | 59% | 24% | 19% | 111 KB | 234 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C C B | 17,278 | 135,173 | 91.0 | 81% | 6% | 96% | 1,570 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 16,654 | 25,671 | 27.6 | 44% | 53% | 97% | 1,041 KB | 1 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C D B | 15,802 | 21,256 | 41.8 | 66% | 47% | 98% | 1,033 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 15,633 | 24,189 | 40.3 | 33% | 0% | 100% | 605 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C C B | 15,569 | 25,833 | 0.0 | 70% | 11% | 76% | 397 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C E C | 15,019 | 33,461 | 17.2 | 64% | 8% | 98% | 8,727 KB | 146 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 62,016 | 30.6 | 45% | 12% | 62% | 65 KB | 3 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C D B | 14,647 | 33,560 | 17.8 | 62% | 32% | 99% | 834 KB | 51 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 13,887 | 46,709 | 59.3 | 50% | 43% | 100% | 505 KB | 6,747 (+3) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,559 | 20,082 | 18.8 | 76% | 35% | 100% | 224 KB | 36 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 13,273 | 31,353 | 7.1 | 32% | 46% | 95% | 629 KB | 19 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | C F A | 13,206 | 24,137 | 13.8 | 74% | 26% | 94% | 255 KB | 5 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C E C | 12,788 | 20,023 | 21.0 | 42% | 49% | 100% | 490 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | C E B | 12,755 | 23,518 | 39.4 | 58% | 24% | 100% | 76 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 12,122 | 19,090 | 32.3 | 63% | 42% | 97% | 654 KB | 1 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 12,092 | 15,916 | 33.5 | 60% | 54% | 100% | 473 KB | 10 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C C B | 11,942 | 15,078 | 0.0 | 72% | 30% | 83% | 262 KB | 135 (+1) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 11,002 | 37,836 | 33.6 | 34% | 23% | 98% | 352 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | C F D | 10,786 | 22,944 | 0.0 | 0% | 0% | 33% | 1,692 KB | 465 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C D C | 10,341 | 31,844 | 32.7 | 64% | 15% | 73% | 3,196 KB | 6 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D F A | 9,898 | 30,826 | 18.9 | 52% | 0% | 93% | 155 KB | 4 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D F C | 9,587 | 18,577 | 39.8 | 28% | 33% | 69% | 1,530 KB | 71,086 (+23) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | D F C | 9,316 | 17,300 | 20.7 | 11% | 0% | 92% | 523 KB | 21 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D C B | 9,310 | 16,467 | 0.1 | 72% | 40% | 76% | 4,139 KB | 7 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 10,652 | 6.6 | 20% | 17% | 89% | 751 KB | 9 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D E C | 9,181 | 13,217 | 0.0 | 58% | 4% | 86% | 376 KB | 2 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D E A | 9,165 | 11,547 | 24.7 | 56% | 19% | 96% | 254 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D E F | 9,147 | 83,552 | 0.0 | 74% | 57% | – | 8,190 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 8,863 | 17,244 | 22.8 | 68% | 0% | – | 122 KB | 2 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 8,851 | 14,037 | 5.1 | 62% | 0% | 100% | 2,284 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F B | 8,822 | 19,415 | 8.5 | 0% | 0% | 99% | 548 KB | 151 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D E D | 8,677 | 40,064 | 0.0 | 66% | 0% | – | 1,119 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 8,337 | 17,931 | 9.9 | 75% | 33% | 40% | 239 KB | 11 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 8,288 | 15,702 | 11.1 | 18% | 8% | 96% | 577 KB | 96 (+1) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 8,269 | 11,487 | 12.4 | 16% | 19% | 96% | 544 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | D C D | 8,140 | 11,628 | 0.0 | 74% | 49% | 4% | 474 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 7,897 | 44,293 | 37.4 | 52% | 24% | 99% | 617 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D E C | 7,739 | 53,653 | 0.0 | 59% | 21% | 51% | 574 KB | 1 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D C B | 7,564 | 11,334 | 21.5 | 75% | 6% | 95% | 158 KB | 5 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 7,443 | 17,408 | 18.6 | 26% | 0% | 84% | 340 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D F D | 7,437 | 17,655 | 6.0 | 22% | 8% | 25% | 269 KB | 16 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | D E B | 7,328 | 40,908 | 20.8 | 84% | 18% | 100% | 1,200 KB | 42 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D F C | 7,264 | 10,020 | 11.6 | 61% | 0% | 58% | 1,263 KB | 13 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D F C | 7,043 | 18,836 | 8.2 | 41% | 0% | 100% | 4,357 KB | 15 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D D A | 6,899 | 11,541 | 55.4 | 62% | 0% | 99% | 59 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 6,622 | 10,047 | 24.1 | 32% | 17% | 100% | 367 KB | 18 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D E C | 6,331 | 12,349 | 0.0 | 44% | 27% | 54% | 1,660 KB | 38 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 6,308 | 15,280 | 42.5 | 11% | 22% | 99% | 237 KB | 7 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D C B | 6,267 | 8,411 | 0.0 | 75% | 40% | 96% | 401 KB | 3 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 6,114 | 8,759 | 13.4 | 70% | 17% | 98% | 1,160 KB | 9 (+1) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 6,099 | 10,852 | 14.3 | 50% | 0% | 96% | 49 KB | 23,982 (+2) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 5,622 | 6,352 | 0.1 | 28% | 18% | 0% | 606 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 5,495 | 9,730 | 17.6 | 2% | 8% | 97% | 68 KB | 64 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 5,459 | 9,302 | 80.9 | 75% | 29% | – | 480 KB | 3 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | D F C | 5,086 | 10,989 | 0.0 | 49% | 17% | 71% | 141 KB | 0 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E C B | 4,781 | 10,718 | 34.2 | 75% | 22% | 100% | 2,514 KB | 5 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 4,780 | 9,046 | 2.2 | 25% | 11% | 74% | 461 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E D C | 4,730 | 13,194 | 0.0 | 61% | 32% | 74% | 5,688 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 4,562 | 11,377 | 63.0 | 73% | 34% | 98% | 247 KB | 8 (-1) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,464 | 7,743 | 0.0 | 57% | 38% | 73% | 138 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 4,459 | 22,546 | 0.0 | 43% | 5% | 97% | 715 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | E F B | 4,451 | 26,457 | 0.0 | 77% | 0% | 71% | 5,368 KB | 451 (+1) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F B | 4,305 | 6,678 | 4.9 | 8% | 0% | 79% | 201 KB | 2 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E C C | 4,300 | 10,014 | 18.0 | 75% | 33% | 90% | 546 KB | 26 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,299 | 7,424 | 32.8 | 60% | 0% | 100% | 64 KB | 3 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E E B | 4,289 | 9,419 | 19.3 | 58% | 0% | 86% | 94 KB | 4 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E F A | 4,274 | 35,035 | 18.2 | 43% | 0% | 94% | 42 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,253 | 4,926 | 14.4 | 22% | 0% | 96% | 166 KB | 1 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E F B | 3,657 | 7,390 | 25.3 | 55% | 0% | 100% | 1,936 KB | 3 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 3,655 | 4,972 | 12.2 | 29% | 13% | 90% | 391 KB | 186 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 3,567 | 8,152 | 0.5 | 8% | 22% | 10% | 282 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 3,545 | 21,029 | 11.5 | 25% | 18% | 100% | 941 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 3,509 | 8,370 | 4.8 | 43% | 0% | 100% | 1,536 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E E B | 3,452 | 29,902 | 15.4 | 46% | 36% | 98% | 1,129 KB | 49 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E E C | 3,404 | 4,477 | 23.5 | 53% | 0% | 98% | 967 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 3,293 | 54,368 | 8.5 | 38% | 0% | 99% | 339 KB | 6 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E F C | 3,276 | 5,815 | 15.3 | 56% | 16% | 88% | 688 KB | 2 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 3,163 | 5,888 | 9.2 | 57% | 14% | 80% | 1,116 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 3,159 | 3,280 | 2.8 | 0% | 0% | 87% | 740 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F C | 3,049 | 5,931 | 0.0 | 2% | 0% | 89% | 195 KB | 104 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 2,951 | 3,517 | 8.3 | 27% | 23% | 82% | 518 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 2,884 | 7,375 | 2.2 | 35% | 36% | 94% | 1,468 KB | 1,121 (+1) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E E B | 2,861 | 6,942 | 17.1 | 66% | 19% | 82% | 433 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E E B | 2,745 | 4,250 | 6.0 | 63% | 15% | 97% | 102 KB | 260 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | E F A | 2,686 | 5,583 | 8.7 | 52% | 0% | 100% | 370 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 2,660 | 5,368 | 10.3 | 33% | 18% | 100% | 469 KB | 14 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 2,643 | 14,933 | 0.0 | 60% | 20% | 42% | 268 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,548 | 16,989 | 0.0 | 18% | 0% | – | 226 KB | 31 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,537 | 103,552 | 4.8 | 13% | 0% | 89% | 24 KB | 0 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 2,516 | 9,085 | 6.4 | 4% | 21% | 93% | 378 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 2,505 | 5,837 | 11.0 | 66% | 9% | 96% | 179 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,479 | 5,033 | 9.3 | 17% | 0% | 79% | 312 KB | 1 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 2,310 | 2,817 | 5.8 | 73% | 0% | 98% | 236 KB | 6 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 2,216 | 2,487 | 12.9 | 51% | 0% | 96% | 431 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 2,174 | 6,007 | 16.9 | 5% | 0% | 98% | 628 KB | 1 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F C | 2,172 | 9,320 | 2.9 | 14% | 0% | 69% | 685 KB | 351 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E F B | 2,155 | 26,074 | 0.0 | 40% | 0% | 98% | 590 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 2,115 | 7,178 | 7.6 | 64% | 6% | 100% | 4,314 KB | 40 (+5) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 2,032 | 4,818 | 13.3 | 0% | 0% | 97% | 644 KB | 13 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 1,994 | 3,399 | 18.2 | 35% | 11% | 99% | 258 KB | 3 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | E F A | 1,974 | 4,482 | 26.5 | 66% | 0% | 100% | 135 KB | 1 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E E D | 1,959 | 7,800 | 3.6 | 61% | 0% | 0% | 6,837 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F A | 1,938 | 5,887 | 16.7 | 50% | 0% | 95% | 262 KB | 9 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E C C | 1,749 | 7,484 | 0.0 | 75% | 26% | 100% | 2,368 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 1,748 | 20,200 | 0.1 | 4% | 0% | 45% | 1,312 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 1,726 | 2,385 | 4.3 | 51% | 0% | 97% | 553 KB | 12 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,712 | 6,731 | 21.2 | 26% | 0% | 100% | 602 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 1,672 | 5,728 | 19.5 | 43% | 13% | 76% | 1,792 KB | 6 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,665 | 3,751 | 8.2 | 31% | 0% | 97% | 53 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | E F A | 1,661 | 9,191 | 58.6 | 57% | 5% | 99% | 29 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,628 | 19,738 | 21.0 | 10% | 0% | 96% | 363 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 1,611 | 5,807 | 1.5 | 13% | 23% | 94% | 4,341 KB | 572 (+2) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,555 | 1,490 | 11.5 | 78% | 17% | 100% | 366 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 1,475 | 3,904 | 18.9 | 36% | 10% | 95% | 644 KB | 3 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 1,420 | 2,684 | 8.4 | 20% | 0% | 99% | 6,579 KB | 9 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,367 | 1,883 | 7.2 | 62% | 27% | 88% | 1,054 KB | 2 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,223 | 2,666 | 22.6 | 12% | 7% | 96% | 324 KB | 1 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E E E | 1,220 | 8,034 | 0.0 | 71% | 0% | 38% | 197 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,212 | 38,880 | 6.4 | 50% | 0% | 98% | 1,094 KB | 2 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 1,186 | 2,928 | 0.0 | 38% | 0% | 75% | 1,175 KB | 52 (+1) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,168 | 4,256 | 10.8 | 54% | 0% | 100% | 161 KB | 7 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 1,166 | 6,746 | 47.1 | 10% | 17% | 100% | 1,451 KB | 8 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F C | 1,132 | 6,371 | 17.0 | 14% | 55% | 64% | 540 KB | 12 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,109 | 2,511 | 0.0 | 0% | 0% | – | 1,044 KB | 1 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F B | 1,076 | 3,301 | 25.1 | 14% | 0% | 84% | 242 KB | 139 (+1) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,059 | 2,070 | 5.5 | 0% | 0% | 93% | 768 KB | 8 (+1) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,043 | 1,393 | 25.0 | 31% | 0% | 99% | 1,004 KB | 124 (+4) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,004 | 3,227 | 8.3 | 25% | 15% | 80% | 275 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | F F B | 967 | 1,137 | 12.0 | 0% | 0% | 99% | 338 KB | 1 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 901 | 4,299 | 0.2 | 52% | 0% | 0% | 52 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 883 | 239,308 | 103 | 6% | 0% | 82% | 378 KB | 4 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 833 | 2,675 | 16.0 | 61% | 6% | 97% | 393 KB | 1 (-1) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F C | 826 | 13,342 | 6.4 | 37% | 0% | 100% | 100 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 815 | 977 | 0.0 | 62% | 8% | 100% | 532 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 715 | 1,637 | 7.5 | 47% | 0% | 100% | 98 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | F F B | 676 | 1,256 | 16.4 | 0% | 0% | 97% | 106 KB | 1 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 660 | 1,966 | 12.4 | 40% | 0% | 96% | 95 KB | 0 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | F D C | 655 | 2,627 | 31.3 | 63% | 3% | 100% | 512 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | F F A | 614 | 2,663 | 41.6 | 41% | 0% | 99% | 340 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 594 | 1,879 | 15.2 | 14% | 0% | 100% | 126 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 543 | 26,915 | 18.5 | 23% | 41% | 94% | 153 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 430 | 7,319 | 7.2 | 46% | 16% | 98% | 485 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 421 | 1,839 | 3.6 | 0% | 0% | 100% | 173 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | F F A | 381 | 3,656 | 13.2 | 7% | 13% | 100% | 386 KB | 2 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F E E | 357 | 9,641 | 10.3 | 47% | 0% | 98% | 635 KB | 11 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 310 | 1,911 | 6.5 | 0% | 0% | 96% | 127 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 273 | 3,794 | 1.2 | 19% | 0% | 82% | 685 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 224 | 15,217 | 34.5 | 18% | 0% | 7% | 3,975 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 209 | 3,636 | 3.3 | 11% | 0% | 95% | 728 KB | 3 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 169 | 1,153 | 11.5 | 0% | 0% | 98% | 885 KB | 3 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 143 | 1,684 | 10.4 | 10% | 0% | 100% | 105 KB | 3 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 113 | 9,540 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 67 | 1,194 | 10.9 | 0% | 0% | 98% | 74 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 55 | 516 | 8.2 | 0% | 0% | 97% | 1,414 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 54 | 1,325 | 5.5 | 0% | 0% | 100% | 45 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 51 | 2,761 | 12.8 | 31% | 0% | 99% | 181 KB | 15 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 42 | 1,660 | 0.0 | 11% | 0% | – | 69 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | F F B | 35 | 13,902 | 13.5 | 27% | 0% | 100% | 269 KB | 2 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 14 | 673 | 15.1 | 0% | 0% | 99% | 636 KB | 2 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 13 | 1,227 | 13.1 | 10% | 0% | 99% | 578 KB | 2 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | F F D | 1 | 1,068 | 17.5 | 24% | 0% | – | 63 KB | 4 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 1 | 1,719 | 1.3 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F F B | – | – | 53.1 | 48% | 17% | 90% | 979 KB | 12 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F C B | – | – | 46.2 | 70% | 0% | 99% | 3,196 KB | 165 (+2) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F B | 0 | 1,342 | 45.1 | 0% | 0% | 100% | 2,702 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 0 | 97 | 34.3 | 0% | 0% | 100% | 598 KB | 5 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 25 | 32.0 | 50% | 0% | 100% | 178 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | – | – | 30.9 | – | – | 85% | 263 KB | 1,260 (+1) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 227 | 29.1 | 0% | 0% | 97% | 497 KB | 1,702 (+3) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 23.3 | 72% | 50% | 91% | 2,290 KB | 1,570 (+7) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | – | – | 22.2 | – | – | 99% | 703 KB | 2 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 0 | 684 | 20.1 | 43% | 0% | 99% | 981 KB | 2 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | – | – | 18.8 | – | – | 100% | 192 KB | 0 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 0 | 325 | 17.9 | 0% | 0% | – | 454 KB | 1 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 1,636 | 17.4 | 24% | 0% | 99% | 295 KB | 2 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 0 | 263 | 17.3 | 0% | 0% | 100% | 190 KB | 2 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 0 | 2,561 | 17.0 | 0% | 0% | 93% | 315 KB | 159 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 16.2 | 31% | 23% | 92% | 1,046 KB | 4 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 16.0 | – | – | 91% | 306 KB | 7 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | – | – | 14.8 | – | – | 100% | 42 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | – | – | 13.5 | – | – | 66% | 324 KB | 41,030 (+24) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 3,254 | 12.5 | 0% | 0% | 84% | 42 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 11.9 | – | – | 100% | 703 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 0 | 0 | 10.7 | – | – | 26% | 7,014 KB | 22 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 469 | 10.4 | 0% | 0% | 0% | 348 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 237 | 9.9 | 0% | 0% | 94% | 948 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 9.5 | – | – | 88% | 710 KB | 4 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 506 | 9.5 | 0% | 0% | 100% | 1,060 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 0 | 502 | 8.9 | 0% | 0% | 100% | 269 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 0 | 916 | 8.7 | 24% | 0% | 96% | 215 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 7.9 | 19% | 0% | 0% | 206 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 1,228 | 7.6 | 15% | 0% | 97% | 249 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 7.6 | – | – | 79% | 416 KB | 9 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F E B | – | – | 7.6 | 54% | 72% | 91% | 86 KB | 7 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 113 | 7.4 | 0% | 0% | 91% | 577 KB | 2 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 0 | 456 | 7.0 | 0% | 0% | 99% | 271 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 6.5 | 0% | 0% | 100% | 154 KB | 4 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 0 | 6.5 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 1,746 | 6.4 | 0% | 0% | 100% | 180 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 5.9 | – | – | 98% | 165 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,499 | 5.1 | 0% | 0% | 90% | 1,009 KB | 0 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F B | 0 | 377 | 5.0 | 0% | 0% | 84% | 137 KB | 1 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 606 | 4.5 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,906 | 4.2 | 18% | 0% | – | 201 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 4.1 | – | – | 96% | 99 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 844 | 4.0 | 0% | 0% | 89% | 2,640 KB | 48 (+1) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 0 | 3.9 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 48 | 3.7 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 3.5 | – | – | 99% | 87 KB | 0 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 573 | 3.5 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 3.3 | – | – | 100% | 160 KB | 2 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 1,333 | 3.2 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | – | – | 3.2 | – | – | 87% | 489 KB | 89 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 3.0 | – | – | 99% | 98 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 18 | 2.9 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 2.8 | – | – | 95% | 385 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 56 | 2.6 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 0 | 1,353 | 2.6 | 30% | 0% | 94% | 697 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 1,674 | 2.6 | 0% | 0% | 100% | 399 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 2.5 | – | – | 100% | 403 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 763 | 2.5 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 0 | 976 | 2.4 | 0% | 0% | 99% | 633 KB | 1 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 657 | 2.3 | 0% | 0% | 87% | 642 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 0 | 2.3 | – | – | 100% | 25 KB | 19 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 2.3 | – | – | – | 710 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | – | – | 2.3 | – | – | 97% | 504 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | – | – | 2.2 | – | – | 98% | 104 KB | 4 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 2.1 | – | – | 100% | 41 KB | 2 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | – | – | 2.1 | – | – | 95% | 66 KB | 3 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | – | – | 2.0 | – | – | 89% | 163 KB | 15 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 0 | 1.9 | – | – | 91% | 43 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 229 | 1.5 | 0% | 0% | 91% | 3,845 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 3,500 | 1.4 | 0% | 0% | 67% | 46 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 363 | 1.1 | 0% | 0% | 93% | 156 KB | 2 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | – | – | 1.0 | – | – | 75% | 336 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 0.8 | – | – | 80% | 83 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | F F D | 0 | 2,241 | 0.8 | 38% | 0% | 37% | 275 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 0.7 | – | – | 99% | 80 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 0.6 | – | – | 90% | 319 KB | 1 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F A | 0 | 0 | 0.5 | – | – | 100% | 29 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 0.5 | 27% | 37% | 0% | 1,110 KB | 467 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 41% | 76% | 84% | 907 KB | 7 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 51 | 0.1 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.1 | – | – | 20% | 154 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 0.1 | – | – | 53% | 3,052 KB | 2 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 0.1 | – | – | 95% | 8,119 KB | 1 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D C | – | – | 0.1 | 62% | 43% | 52% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.0 | – | – | – | 311 KB | 4 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 0 | 603 | 0.0 | 0% | 0% | 72% | 554 KB | 31 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | 0 | 1 | 0.0 | 0% | 0% | – | 320 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 225 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 0 | 51 | 0.0 | 0% | 0% | 0% | 673 KB | 3 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 0 | 5,349 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 87% | 49% | 94% | 45,801 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 59 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 2 | 0.0 | 0% | 0% | 7% | 158 KB | 123 (+0) |
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
