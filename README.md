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
_354 repos, last measured 2026-11-16. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (354)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 90,414 | 98,337 | 71.7 | 54% | 50% | 87% | 417 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A C B | 88,173 | 118,340 | 64.7 | 77% | 67% | 99% | 322 KB | 3 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A C D | 51,203 | 91,503 | 91.1 | 76% | 41% | 3% | 490 KB | 1 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B D D | 39,339 | 56,006 | 0.1 | 64% | 61% | 0% | 3,716 KB | 3 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B D B | 37,934 | 46,653 | 0.1 | 64% | 34% | 87% | 3,951 KB | 7 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B E C | 32,902 | 116,227 | 160 | 54% | 67% | 55% | 311 KB | 4 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B F B | 27,928 | 40,567 | 61.6 | 9% | 0% | 80% | 423 KB | 87 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B E C | 27,621 | 94,840 | 224 | 44% | 0% | 96% | 2,436 KB | 5 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E D | 26,024 | 92,077 | 0.0 | 48% | 19% | 46% | 5,368 KB | 449 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B E B | 25,911 | 32,760 | 35.7 | 52% | 27% | 99% | 3,763 KB | 2,121 (+4) |
| [arul28/ADE](https://github.com/arul28/ADE) | B E C | 25,886 | 47,251 | 15.2 | 63% | 39% | 93% | 8,727 KB | 144 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B F D | 25,810 | 61,189 | 16.8 | 25% | 0% | 25% | 250 KB | 16 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | B C D | 25,748 | 153,733 | 0.0 | 75% | 50% | 28% | 308 KB | 836 (+8) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B B D | 25,180 | 54,352 | 0.0 | 83% | 37% | – | 1,158 KB | 2 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 24,608 | 29,600 | 23.4 | 40% | 46% | 99% | 1,927 KB | 159 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B A D | 24,447 | 564,342 | 0.0 | 91% | 40% | 0% | 3,286 KB | 1 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B C B | 21,175 | 22,724 | 65.6 | 74% | 22% | 95% | 1,112 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C C | 20,324 | 146,283 | 57.2 | 81% | 23% | 67% | 1,547 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 19,956 | 20,707 | 0.0 | 78% | 24% | 4% | 446 KB | 0 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | C F B | 19,912 | 28,032 | 102 | 30% | 33% | 92% | 5,498 KB | 85 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C C B | 19,669 | 28,972 | 24.0 | 85% | 41% | 99% | 616 KB | 6 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C D D | 19,443 | 38,574 | 0.0 | 63% | 35% | – | 534 KB | 2 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | C E B | 19,063 | 72,141 | 6.5 | 80% | 0% | 100% | 1,188 KB | 6 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | C E B | 18,751 | 41,965 | 47.9 | 65% | 17% | 100% | 881 KB | 4 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C C | 17,075 | 36,805 | 29.9 | 76% | 37% | 64% | 103 KB | 234 (+1) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F C | 16,331 | 22,637 | 22.3 | 37% | 36% | 100% | 606 KB | 22 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 16,293 | 65,846 | 0.0 | 60% | 47% | – | 1,069 KB | 0 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 16,162 | 26,360 | 22.2 | 83% | 18% | 99% | 198 KB | 34 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 15,743 | 37,973 | 25.5 | 46% | 15% | 100% | 1,158 KB | 39 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 15,667 | 27,084 | 153 | 33% | 28% | 100% | 258 KB | 22 (+1) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C F D | 15,334 | 67,015 | 2.0 | 11% | 0% | 0% | 6,837 KB | 1 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C C | 15,201 | 23,293 | 31.8 | 76% | 33% | 95% | 3,196 KB | 6 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | C C B | 15,178 | 15,300 | 21.2 | 72% | 34% | 91% | 226 KB | 1 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C E B | 15,040 | 77,210 | 32.8 | 59% | 44% | 86% | 1,459 KB | 70,952 (+27) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F B | 14,950 | 29,768 | 8.0 | 0% | 9% | 98% | 516 KB | 142 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 67,438 | 33.9 | 42% | 6% | 62% | 169 KB | 2 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 14,588 | 19,529 | 49.6 | 38% | 44% | 90% | 158 KB | 1 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C F B | 14,354 | 58,156 | 3.0 | 38% | 29% | 99% | 1,488 KB | 0 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C B C | 14,325 | 16,223 | 0.0 | 82% | 6% | 100% | 4,357 KB | 15 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C C B | 14,231 | 18,487 | 44.4 | 74% | 66% | 99% | 942 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C D C | 13,802 | 23,792 | 34.0 | 69% | 11% | 100% | 464 KB | 10 (+1) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C E B | 13,516 | 42,288 | 7.1 | 55% | 20% | 95% | 596 KB | 19 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | C E B | 12,763 | 13,114 | 8.1 | 60% | 30% | 88% | 710 KB | 4 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 12,628 | 28,592 | 93.7 | 52% | 47% | 76% | 394 KB | 74 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C B B | 12,615 | 16,852 | 0.0 | 88% | 28% | 99% | 223 KB | 129 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C F B | 12,018 | 25,265 | 45.2 | 38% | 2% | 96% | 257 KB | 1 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 11,360 | 28,492 | 24.8 | 25% | 22% | 98% | 515 KB | 21 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C E A | 11,288 | 27,421 | 19.8 | 43% | 0% | 93% | 300 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | C F B | 11,198 | 15,126 | 21.9 | 59% | 0% | 92% | 104 KB | 4 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | C E C | 11,101 | 18,116 | 0.0 | 64% | 33% | 95% | 1,175 KB | 51 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | C D B | 11,051 | 24,951 | 38.3 | 68% | 37% | 100% | 178 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C D D | 11,004 | 16,143 | 0.0 | 62% | 66% | 7% | 1,652 KB | 38 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 10,840 | 20,113 | 31.3 | 52% | 1% | 100% | 135 KB | 1 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F C | 10,385 | 19,027 | 0.0 | 23% | 24% | 83% | 20,376 KB | 2 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 10,164 | 14,829 | 63.0 | 56% | 32% | 83% | 275 KB | 6,688 (+71) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 10,108 | 20,356 | 16.8 | 13% | 36% | – | 125 KB | 2 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C A B | 10,083 | 25,647 | 20.5 | 91% | 33% | 84% | 155 KB | 4 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D F B | 9,706 | 21,883 | 26.8 | 60% | 0% | 100% | 1,967 KB | 3 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D C B | 9,345 | 16,639 | 132 | 74% | 35% | 86% | 2,533 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | D D B | 9,324 | 14,989 | 25.5 | 63% | 2% | 96% | 608 KB | 0 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 9,266 | 13,132 | 0.0 | 80% | 41% | 80% | 363 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 13,754 | 5.8 | 65% | 0% | 87% | 742 KB | 9 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | D B C | 9,253 | 26,814 | 23.4 | 87% | 38% | 86% | 363 KB | 11 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | D F A | 9,208 | 42,348 | 34.9 | 30% | 0% | 87% | 242 KB | 136 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D B A | 9,029 | 13,911 | 45.4 | 85% | 36% | 96% | 338 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 8,935 | 14,599 | 18.2 | 37% | 19% | 94% | 262 KB | 9 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 8,927 | 15,047 | 38.3 | 72% | 23% | 100% | 2,396 KB | 5 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 8,647 | 9,695 | 14.6 | 16% | 0% | 97% | 628 KB | 13 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D E B | 8,451 | 40,753 | 28.2 | 55% | 19% | 100% | 617 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 8,390 | 15,709 | 5.3 | 25% | 25% | 100% | 2,284 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 8,342 | 14,053 | 11.2 | 48% | 11% | 95% | 250 KB | 5 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | D C A | 8,336 | 12,767 | 67.3 | 77% | 27% | 92% | 28 KB | 0 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | D E C | 8,201 | 15,538 | 0.1 | 44% | 0% | 62% | 255 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 7,857 | 15,891 | 18.9 | 53% | 0% | 93% | 315 KB | 159 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 7,848 | 36,379 | 20.8 | 54% | 3% | 97% | 705 KB | 49 (+1) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D B C | 7,532 | 34,759 | 0.0 | 86% | 29% | 50% | 570 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 7,506 | 17,945 | 0.0 | 53% | 0% | 97% | 643 KB | 0 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D F B | 7,264 | 16,587 | 22.2 | 36% | 0% | 98% | 158 KB | 5 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 7,213 | 9,890 | 80.9 | 49% | 4% | – | 473 KB | 3 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D F B | 6,735 | 6,821 | 14.9 | 54% | 15% | 99% | 605 KB | 1 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 6,722 | 11,047 | 13.4 | 46% | 10% | 97% | 375 KB | 184 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D D B | 6,657 | 10,812 | 17.5 | 66% | 35% | 92% | 425 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E B | 6,321 | 18,531 | 12.3 | 47% | 0% | 75% | 1,259 KB | 13 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | D E A | 6,163 | 6,834 | 13.5 | 54% | 0% | 100% | 370 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D E B | 6,102 | 14,665 | 16.0 | 82% | 0% | 99% | 1,145 KB | 9 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D F A | 6,058 | 7,567 | 24.5 | 81% | 0% | 92% | 59 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 5,544 | 57,081 | 14.6 | 62% | 0% | 97% | 393 KB | 2 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F D | 5,435 | 9,677 | 0.2 | 4% | 14% | 10% | 283 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 5,366 | 8,623 | 59.2 | 64% | 0% | – | 258 KB | 3 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 5,364 | 16,679 | 44.6 | 7% | 22% | 99% | 231 KB | 7 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 5,263 | 12,115 | 47.4 | 70% | 47% | 98% | 235 KB | 9 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D C B | 5,166 | 19,560 | 37.7 | 73% | 28% | 97% | 43 KB | 0 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | D E B | 5,160 | 9,513 | 29.0 | 77% | 0% | 99% | 703 KB | 2 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,860 | 12,682 | 22.1 | 19% | 15% | 97% | 320 KB | 1 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 4,756 | 19,251 | 16.9 | 65% | 0% | 93% | 431 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E E B | 4,578 | 46,596 | 14.2 | 62% | 9% | 96% | 1,414 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 4,487 | 8,773 | 2.9 | 59% | 48% | 95% | 4,205 KB | 562 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 4,468 | 7,078 | 22.8 | 28% | 0% | 88% | 49 KB | 23,927 (+5) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E F A | 4,443 | 37,783 | 19.1 | 40% | 43% | 96% | 42 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 4,312 | 9,560 | 19.7 | 54% | 14% | 100% | 628 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 4,256 | 4,893 | 0.8 | 62% | 20% | 28% | 257 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E E C | 4,252 | 19,158 | 15.7 | 63% | 34% | 92% | 473 KB | 25 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | E E C | 4,208 | 14,672 | 21.0 | 62% | 18% | 100% | 387 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,161 | 97,646 | 19.2 | 12% | 0% | 100% | 261 KB | 2 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 4,161 | 4,703 | 19.1 | 17% | 0% | 98% | 322 KB | 0 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 4,092 | 9,132 | 12.7 | 0% | 0% | 100% | 557 KB | 96 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E B B | 4,058 | 6,432 | 0.0 | 85% | 80% | 86% | 399 KB | 3 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,944 | 10,311 | 0.1 | 18% | 8% | 86% | 395 KB | 2 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | E F D | 3,839 | 95,461 | 30.6 | 0% | 0% | 57% | 3,975 KB | 1 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 3,708 | 6,153 | 46.7 | 68% | 0% | 100% | 598 KB | 5 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E E C | 3,567 | 5,559 | 22.2 | 42% | 21% | 100% | 388 KB | 18 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 3,561 | 4,706 | 11.3 | 30% | 0% | 98% | 544 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 3,392 | 15,709 | 47.8 | 39% | 15% | 98% | 1,429 KB | 8 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 3,349 | 5,042 | 13.6 | 24% | 0% | 98% | 74 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,294 | 6,542 | 7.8 | 5% | 21% | 93% | 378 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | E F C | 3,260 | 8,965 | 26.5 | 44% | 10% | 95% | 996 KB | 1 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 3,232 | 6,407 | 18.0 | 0% | 19% | 80% | 312 KB | 1 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,110 | 4,491 | 1.8 | 28% | 6% | 73% | 137 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 2,939 | 5,186 | 38.7 | 9% | 0% | 100% | 111 KB | 3 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,905 | 35,463 | 0.0 | 52% | 0% | – | 216 KB | 31 (+1) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | E F C | 2,878 | 148,839 | 16.4 | 39% | 0% | 66% | 324 KB | 40,865 (+23) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | E F C | 2,862 | 9,669 | 10.8 | 53% | 0% | 99% | 884 KB | 3 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E E D | 2,847 | 8,771 | 19.0 | 45% | 10% | – | 63 KB | 3 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E D B | 2,723 | 12,999 | 0.0 | 68% | 0% | 93% | 590 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 2,694 | 8,251 | 11.2 | 46% | 29% | 81% | 163 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,640 | 3,973 | 26.6 | 31% | 24% | – | 454 KB | 1 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 2,603 | 3,935 | 35.1 | 58% | 6% | 100% | 512 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F B | 2,541 | 8,706 | 27.2 | 11% | 0% | 100% | 192 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,449 | 3,501 | 17.2 | 18% | 11% | 97% | 106 KB | 1 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 2,428 | 10,666 | 0.0 | 28% | 0% | – | 320 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F C | 2,376 | 3,862 | 13.7 | 49% | 19% | 69% | 155 KB | 1 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | E E D | 2,348 | 12,148 | 10.6 | 61% | 0% | 3% | 228 KB | 10 (+1) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E D D | 2,305 | 9,763 | 0.0 | 65% | 31% | 42% | 268 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 2,294 | 6,140 | 19.5 | 42% | 26% | 84% | 540 KB | 11 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 2,245 | 5,948 | 37.4 | 8% | 0% | 100% | 190 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 2,242 | 11,540 | 40.4 | 2% | 3% | 100% | 605 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 2,148 | 2,383 | 5.4 | 0% | 0% | 73% | 300 KB | 350 (+1) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E B A | 2,092 | 3,873 | 6.7 | 86% | 61% | 100% | 236 KB | 5 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E D E | 2,068 | 87,093 | 0.0 | 63% | 20% | 55% | 188 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E C B | 2,044 | 4,454 | 9.9 | 72% | 42% | 100% | 360 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 2,022 | 3,013 | 6.4 | 28% | 0% | 97% | 6,579 KB | 8 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,003 | 7,377 | 16.1 | 9% | 0% | 99% | 169 KB | 13 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E E D | 1,924 | 3,023 | 0.1 | 57% | 23% | 0% | 601 KB | 1 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 1,768 | 10,585 | 0.0 | 4% | 0% | 0% | 1,275 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 1,689 | 4,176 | 3.1 | 71% | 0% | – | 201 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,607 | 4,321 | 10.2 | 57% | 0% | 79% | 1,035 KB | 2 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | E E C | 1,567 | 1,812 | 17.7 | 47% | 21% | 64% | 646 KB | 2 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 1,566 | 44,985 | 4.1 | 24% | 0% | 84% | 23 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 1,548 | 115,066 | 110 | 12% | 0% | 93% | 378 KB | 4 (+1) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,514 | 22,771 | 0.0 | 0% | 0% | 33% | 284 KB | 464 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 1,513 | 4,767 | 22.0 | 63% | 0% | 98% | 258 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 1,488 | 3,864 | 26.5 | 41% | 22% | 98% | 996 KB | 121 (+1) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,433 | 4,546 | 1.0 | 49% | 13% | 98% | 5,636 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 1,431 | 3,038 | 13.9 | 8% | 0% | 97% | 386 KB | 2 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,382 | 2,373 | 9.7 | 7% | 0% | 95% | 105 KB | 3 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F A | 1,361 | 5,052 | 2.1 | 24% | 0% | 94% | 165 KB | 2 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,357 | 11,493 | 6.2 | 43% | 0% | 100% | 4,314 KB | 34 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 1,303 | 8,550 | 0.0 | 69% | 0% | 6% | 158 KB | 120 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,271 | 2,738 | 9.4 | 24% | 0% | 87% | 274 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,160 | 2,479 | 7.9 | 27% | 0% | 97% | 518 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 1,155 | 1,790 | 9.8 | 46% | 30% | 95% | 457 KB | 14 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,126 | 1,536 | 4.2 | 0% | 0% | 99% | 168 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 1,101 | 2,525 | 20.2 | 0% | 0% | 94% | 68 KB | 63 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,093 | 2,944 | 31.1 | 50% | 0% | 94% | 573 KB | 2 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E F C | 1,017 | 1,539 | 7.6 | 69% | 14% | 98% | 483 KB | 0 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 1,003 | 1,912 | 0.0 | 14% | 36% | 72% | 301 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 934 | 2,378 | 2.4 | 20% | 0% | 88% | 602 KB | 2 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | F E C | 931 | 2,171 | 30.5 | 62% | 0% | 99% | 891 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 925 | 2,538 | 11.6 | 28% | 7% | 100% | 269 KB | 0 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | 910 | 5,733 | 19.5 | 26% | 0% | 100% | 42 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 909 | 787 | 8.4 | 23% | 0% | 100% | 98 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 902 | 6,815 | 24.0 | 42% | 55% | 99% | 363 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 885 | 104,467 | 0.0 | 63% | 0% | – | 8,190 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 848 | 2,367 | 0.0 | 20% | 0% | – | 1,021 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 845 | 2,309 | 9.8 | 48% | 0% | 100% | 168 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 843 | 2,127 | 0.0 | 80% | 0% | 83% | 554 KB | 29 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F E E | 834 | 8,072 | 11.7 | 87% | 6% | 99% | 634 KB | 11 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 786 | 10,529 | 11.7 | 50% | 0% | 100% | 898 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 782 | 1,015 | 25.5 | 30% | 0% | 96% | 704 KB | 13 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 770 | 2,793 | 7.2 | 34% | 0% | 99% | 45 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | F C C | 658 | 3,523 | 0.0 | 79% | 80% | 100% | 1,990 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 651 | 3,112 | 13.0 | 0% | 0% | 99% | 215 KB | 1 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F C | 577 | 816 | 0.1 | 0% | 0% | 82% | 173 KB | 54 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | F F A | 468 | 1,159 | 14.2 | 25% | 0% | 100% | 164 KB | 6 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 410 | 3,927 | 9.9 | 0% | 0% | 44% | 144 KB | 16 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 387 | 2,170 | 22.2 | 0% | 0% | 97% | 581 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 380 | 11,630 | 15.7 | 25% | 22% | 75% | 149 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 347 | 1,110 | 21.0 | 16% | 0% | 99% | 578 KB | 2 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 343 | 439 | 0.0 | 36% | 0% | 0% | 673 KB | 3 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 333 | 1,028 | 0.0 | 37% | 0% | 100% | 501 KB | 0 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 323 | 1,342 | 15.6 | 0% | 0% | 96% | 1,116 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | F F B | 286 | 2,366 | 5.3 | 36% | 0% | 98% | 550 KB | 12 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 260 | 594 | 5.4 | 24% | 0% | 66% | 643 KB | 7 (+1) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 252 | 1,399 | 18.1 | 65% | 0% | 96% | 93 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 248 | 565 | 16.4 | 25% | 0% | 100% | 1,060 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 241 | 2,077 | 23.9 | 32% | 0% | 99% | 295 KB | 2 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 230 | 1,143 | 2.9 | 29% | 0% | 98% | 104 KB | 4 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 208 | 786 | 17.8 | 48% | 0% | 76% | 16 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 208 | 4,509 | 0.0 | 32% | 0% | – | 202 KB | 5 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 201 | 1,030 | 8.6 | 0% | 0% | 99% | 43 KB | 2 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 175 | 52,215 | 35.7 | 42% | 0% | 100% | 635 KB | 2 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 175 | 3,908 | 5.0 | 46% | 0% | 100% | 425 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 130 | 897 | 4.1 | 0% | 0% | 92% | 3,845 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 118 | 3,228 | 2.4 | 31% | 0% | 79% | 625 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 101 | 621 | 9.4 | 0% | 0% | 97% | 270 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 91 | 4,509 | 0.6 | 29% | 0% | 100% | 52 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 85 | 3,029 | 10.4 | 18% | 0% | 97% | 249 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,163 | 11.4 | 0% | 100% | 20% | 7,014 KB | 21 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 75 | 2,330 | 3.6 | 9% | 0% | 94% | 697 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | F F B | 42 | 30,330 | 19.3 | 29% | 0% | 100% | 1,129 KB | 49 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 42 | 6,985 | 5.9 | 57% | 0% | 97% | 941 KB | 2 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 39 | 5,412 | 0.0 | 25% | 0% | 92% | 254 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 35 | 7,390 | 1.4 | 0% | 0% | 59% | 46 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 18 | 261 | 28.9 | 0% | 0% | 99% | 981 KB | 2 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 8 | 824 | 15.7 | 0% | 0% | 100% | 126 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 4 | 1,851 | 4.1 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F E B | – | – | 74.3 | 55% | 25% | 100% | 3,196 KB | 119 (+25) |
| [purlis/purlis](https://github.com/purlis/purlis) | F C B | – | – | 60.0 | 70% | 27% | 100% | 948 KB | 12 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 431 | 27.3 | 0% | 0% | 91% | 137 KB | 1 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 757 | 26.4 | 0% | 0% | 97% | 405 KB | 1,669 (+6) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | 0 | 137 | 24.5 | 0% | 0% | 85% | 263 KB | 1,254 (-1) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 24.0 | 62% | 0% | 91% | 2,290 KB | 1,539 (+5) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 21.8 | – | – | 100% | 703 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F B | 0 | 4,070 | 19.9 | 15% | 0% | 70% | 169 KB | 2 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 0 | 19.7 | 0% | 0% | 76% | 1,719 KB | 6 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 19.5 | – | – | 79% | 416 KB | 9 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 3,154 | 17.1 | 0% | 0% | 99% | 243 KB | 9 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 16.7 | – | – | 91% | 306 KB | 7 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F D B | – | – | 16.7 | 63% | 24% | 75% | 1,043 KB | 4 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 15.9 | 41% | 0% | 100% | 154 KB | 4 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F D B | – | – | 13.5 | 61% | 10% | 78% | 86 KB | 7 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 1,003 | 13.2 | 0% | 0% | 94% | 935 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 380 | 13.1 | 18% | 0% | 0% | 348 KB | 1 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | 0 | 716 | 12.0 | 57% | 0% | 98% | 165 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 0 | 0 | 12.0 | 0% | 0% | 99% | 98 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 9 | 11.3 | 0% | 0% | 100% | 25 KB | 19 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 10.6 | – | – | 100% | 41 KB | 2 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 276 | 10.1 | 0% | 0% | 75% | 336 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 188 | 9.6 | 0% | 0% | 95% | 123 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 4,684 | 9.4 | 47% | 0% | 99% | 221 KB | 7 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,664 | 8.9 | 47% | 0% | 94% | 1,170 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 8.2 | 0% | 0% | 0% | 206 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 8.1 | – | – | 95% | 8,119 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 60 | 7.6 | 0% | 0% | 99% | 87 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 2,616 | 7.5 | 0% | 0% | 100% | 101 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 7.2 | – | – | 99% | 80 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 0 | 0 | 7.2 | – | – | 96% | 99 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 7.0 | – | – | 100% | 160 KB | 2 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 0 | 609 | 6.8 | 0% | 0% | 99% | 104 KB | 255 (+1) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 8 | 6.3 | 0% | 0% | 69% | 26 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 15 | 5.9 | 0% | 0% | 95% | 66 KB | 3 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | 0 | 3,361 | 5.8 | 18% | 0% | 95% | 385 KB | 1 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 5.7 | – | – | 100% | 403 KB | 2 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | F F B | 0 | 0 | 5.5 | – | – | 72% | 396 KB | 2 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | – | – | 4.9 | – | – | 98% | 54 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 13,542 | 4.5 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 0 | 4.3 | – | – | 100% | 127 KB | 25 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 36 | 4.2 | 0% | 0% | 97% | 504 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 884 | 4.1 | 0% | 0% | 97% | 721 KB | 3 (+1) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 320 | 4.1 | 0% | 0% | 87% | 489 KB | 89 (+3) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 88 | 4.0 | 0% | 0% | 100% | 156 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 0 | 4.0 | 0% | 0% | 89% | 163 KB | 15 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 1,242 | 3.8 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 0 | 3.7 | – | – | 91% | 43 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | F F B | 0 | 0 | 3.6 | 0% | 0% | 86% | 739 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 1,887 | 3.4 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 0 | 183 | 3.4 | 0% | 0% | 99% | 608 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 3.4 | – | – | 80% | 83 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 3.0 | – | – | 53% | 3,052 KB | 2 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 102 | 3.0 | 0% | 0% | – | 710 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 2.6 | – | – | 93% | 576 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 11,289 | 2.5 | 0% | 0% | 90% | 2,640 KB | 44 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 476 | 2.2 | 0% | 0% | – | 14 KB | 0 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 2.1 | – | – | 98% | 363 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 0 | 1.7 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 0 | 1.2 | – | – | 100% | 298 KB | 5 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 0.8 | – | – | – | 311 KB | 4 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | – | – | – | 56 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.6 | – | – | – | 53 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 676 | 0.4 | 23% | 0% | 88% | 1,468 KB | 1,120 (-1) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 0.4 | – | – | 96% | 122 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 0.4 | 42% | 91% | 0% | 2,040 KB | 464 (+1) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.2 | – | – | 20% | 154 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.2 | – | – | 99% | 73 KB | 3 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 0.2 | – | – | 98% | 723 KB | 5 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F D B | – | – | 0.1 | 64% | 82% | 89% | 861 KB | 7 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,333 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 58% | 15% | 51% | 88 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 0 | 0.0 | – | – | 100% | 472 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | – | – | 0.0 | – | – | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 94 | 0.0 | 0% | 0% | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 234 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 154 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 2,383 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.0 | – | – | 69% | 290 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.0 | – | – | 98% | 42 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.0 | 54% | 37% | 94% | 41,257 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 0.0 | – | – | 98% | 231 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 19,673 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
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
