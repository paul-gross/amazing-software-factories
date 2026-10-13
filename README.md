# Amazing software factories

An open analysis of software factory repos on GitHub: projects built by fleets of AI coding agents rather than a
person at a keyboard, tracked over time to see which concepts are emerging and where they're heading.

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

<!-- BEGIN GENERATED -->
_161 repos, last measured 2026-10-13. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (161)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 90,256 | 114,911 | 54.8 | 16% | 14% | 96% | 2,955 KB | 1,738 (+1) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 65,519 | 92,238 | 31.0 | 77% | 42% | 98% | 231 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 62,863 | 162,862 | 0.2 | 49% | 10% | 27% | 1,271 KB | 431 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A E B | 58,284 | 73,306 | 22.0 | 81% | 22% | 98% | 610 KB | 10 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 56,936 | 66,480 | 56.4 | 85% | 59% | 89% | 676 KB | 14 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A D B | 50,856 | 95,694 | 31.7 | 64% | 27% | 80% | 2,584 KB | 34 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A B A | 47,707 | 62,807 | 73.1 | 80% | 54% | 100% | 158 KB | 14 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | A E C | 40,736 | 71,427 | 39.2 | 56% | 64% | 94% | 2,345 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 38,275 | 49,198 | 17.8 | 79% | 0% | 97% | 94 KB | 16 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 36,307 | 2,168,659 | 74.6 | 0% | 0% | 76% | 3,975 KB | 1 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B C C | 33,835 | 78,323 | 0.2 | 77% | 48% | 98% | 279 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | B E B | 32,115 | 45,749 | 0.0 | 52% | 18% | 86% | 608 KB | 1 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B C B | 31,402 | 37,600 | 143 | 74% | 79% | 100% | 3,166 KB | 1 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | B E C | 30,848 | 49,548 | 25.5 | 74% | 0% | 94% | 102 KB | 113 (+3) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B D B | 30,533 | 36,213 | 72.5 | 60% | 27% | 98% | 601 KB | 0 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B E B | 30,421 | 45,174 | 22.7 | 43% | 20% | 98% | 697 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 27,662 | 69,985 | 31.5 | 49% | 7% | 97% | 54 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | B D D | 26,949 | 26,896 | 10.1 | 62% | 49% | – | 81 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B F B | 26,423 | 69,603 | 20.9 | 55% | 9% | 100% | 750 KB | 31 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B C B | 25,809 | 38,578 | 27.3 | 75% | 45% | 100% | 1,306 KB | 91 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 25,667 | 27,151 | 0.0 | 83% | 64% | – | 225 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B F D | 24,859 | 41,204 | 0.0 | 66% | 0% | 44% | 239 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | B E B | 24,353 | 50,160 | 23.3 | 62% | 14% | 97% | 377 KB | 9 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 24,013 | 32,549 | 31.8 | 72% | 18% | 95% | 599 KB | 22 |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B D B | 23,668 | 26,968 | 12.5 | 64% | 32% | 99% | 699 KB | 9 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B C B | 23,332 | 149,035 | 27.7 | 75% | 31% | 84% | 1,403 KB | 0 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 23,310 | 41,788 | 88.1 | 34% | 44% | 46% | 314 KB | 3 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | B E F | 23,046 | 236,977 | 0.0 | 61% | 27% | – | 8,190 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 22,632 | 48,349 | 39.2 | 90% | 48% | 100% | 353 KB | 2 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 21,495 | 30,234 | 22.6 | 88% | 51% | 88% | 364 KB | 9 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | B E C | 21,034 | 32,792 | 1.1 | 46% | 13% | 68% | 290 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B E D | 21,015 | 43,453 | 0.0 | 56% | 62% | – | 1,191 KB | 3 (+1) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B D B | 20,362 | 36,605 | 14.5 | 68% | 55% | 91% | 428 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 20,307 | 56,126 | 44.3 | 70% | 38% | 99% | 146 KB | 1 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | B F A | 20,146 | 33,513 | 30.2 | 70% | 28% | 97% | 146 KB | 4 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C C D | 19,349 | 35,074 | 0.0 | 70% | 13% | – | 776 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E C | 19,082 | 92,069 | 18.7 | 55% | 41% | 65% | 304 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | C E F | 18,951 | 376,844 | 7.0 | 54% | 7% | – | 331 KB | 4 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 18,933 | 44,464 | 24.5 | 39% | 44% | 100% | 448 KB | 18 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C D D | 17,523 | 31,225 | 0.0 | 69% | 31% | 42% | 265 KB | 0 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 17,518 | 642,105 | 0.0 | 86% | 0% | 0% | 3,283 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | C D A | 17,057 | 43,549 | 11.5 | 62% | 52% | 93% | 236 KB | 5 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C C C | 16,773 | 80,270 | 0.0 | 70% | 13% | 50% | 451 KB | 1 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 15,647 | 21,929 | 54.1 | 76% | 42% | 91% | 4,310 KB | 15 |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 15,635 | 30,727 | 12.3 | 74% | 38% | 79% | 117 KB | 4 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | C F A | 15,346 | 12,815 | 13.3 | 50% | 0% | 98% | 149 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 14,885 | 17,028 | 14.2 | 52% | 39% | 100% | 567 KB | 0 |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 14,806 | 22,788 | 33.9 | 80% | 39% | 78% | 1,340 KB | 3 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C D B | 14,761 | 25,424 | 50.0 | 70% | 70% | 98% | 573 KB | 2 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C B C | 14,435 | 19,663 | 18.8 | 84% | 45% | 96% | 116 KB | 32 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C E A | 14,400 | 104,210 | 19.6 | 42% | 12% | 96% | 108 KB | 3 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 13,889 | 18,300 | 85.2 | 20% | 49% | 76% | 340 KB | 48 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 13,877 | 43,624 | 164 | 49% | 11% | 89% | 2,294 KB | 3 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 13,877 | 29,537 | 55.7 | 63% | 70% | 100% | 768 KB | 6,259 (+26) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | C E B | 13,714 | 17,314 | 25.4 | 56% | 26% | 92% | 700 KB | 4 |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | C C A | 13,652 | 36,692 | 0.1 | 77% | 26% | 99% | 163 KB | 9 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C D A | 13,637 | 38,395 | 0.0 | 65% | 12% | 94% | 211 KB | 0 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 13,224 | 17,506 | 37.7 | 0% | 63% | 90% | 66 KB | 59 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C E A | 12,787 | 17,936 | 5.6 | 44% | 31% | 95% | 386 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C F B | 12,515 | 115,645 | 17.8 | 32% | 4% | 100% | 1,414 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C E C | 12,375 | 19,233 | 30.4 | 52% | 0% | 100% | 399 KB | 0 |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C E B | 12,328 | 26,821 | 12.3 | 60% | 0% | 89% | 744 KB | 4 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 12,186 | 13,341 | 19.1 | 81% | 17% | 93% | 529 KB | 1 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 12,185 | 15,563 | 4.5 | 0% | 0% | 99% | 380 KB | 127 (+1) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C C A | 12,132 | 20,725 | 33.2 | 72% | 48% | 96% | 273 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | C D B | 11,924 | 15,218 | 23.9 | 64% | 66% | 98% | 103 KB | 4 |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 11,806 | 25,464 | 20.1 | 55% | 11% | 98% | 113 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C E B | 11,781 | 24,846 | 28.4 | 56% | 13% | 100% | 6,926 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C D C | 11,721 | 19,107 | 0.0 | 68% | 18% | 86% | 816 KB | 1 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C E C | 11,338 | 18,885 | 6.3 | 51% | 20% | 96% | 106 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C A | 11,204 | 14,725 | 32.9 | 71% | 25% | 85% | 102 KB | 229 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 10,036 | 20,719 | 48.7 | 16% | 54% | 98% | 670 KB | 3 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D E B | 9,926 | 23,569 | 20.2 | 56% | 21% | 99% | 1,753 KB | 5 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 9,860 | 15,016 | 34.9 | 15% | 0% | 92% | 649 KB | 36 |
| [floor/teamcli](https://github.com/floor/teamcli) | D E B | 9,711 | 18,892 | 7.5 | 44% | 1% | 80% | 67 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D D C | 9,218 | 15,082 | 10.0 | 62% | 46% | 92% | 112 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,175 | 13,059 | 7.9 | 46% | 14% | 100% | 489 KB | 11 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D E C | 8,914 | 13,944 | 15.3 | 59% | 24% | 100% | 615 KB | 8 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D D A | 8,568 | 19,293 | 8.8 | 63% | 16% | 99% | 110 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | D F D | 8,150 | 15,783 | 11.1 | 74% | 0% | – | 115 KB | 0 |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 7,658 | 9,590 | 19.5 | 52% | 8% | 80% | 359 KB | 6 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | D F C | 7,591 | 32,703 | 47.8 | 67% | 11% | 93% | 324 KB | 3 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | D E B | 7,569 | 13,047 | 22.9 | 53% | 43% | 99% | 964 KB | 93 (+2) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 7,051 | 9,617 | 22.8 | 39% | 12% | 99% | 653 KB | 17 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D E C | 6,791 | 9,006 | 8.7 | 47% | 0% | 91% | 94 KB | 3 (+2) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,698 | 23,034 | 0.0 | 52% | 0% | 100% | 435 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 6,696 | 8,440 | 13.3 | 79% | 46% | 100% | 92 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D D D | 6,321 | 11,827 | 0.0 | 62% | 0% | – | 97 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E B | 6,155 | 13,945 | 15.2 | 66% | 5% | 91% | 1,158 KB | 13 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 6,068 | 20,803 | 0.0 | 10% | 0% | – | 189 KB | 26 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D E B | 6,064 | 15,302 | 17.2 | 53% | 0% | 83% | 385 KB | 19 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D E C | 5,806 | 10,177 | 1.2 | 49% | 35% | 77% | 3,061 KB | 529 (+3) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D F C | 5,644 | 9,340 | 13.1 | 38% | 8% | 100% | 403 KB | 2 |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | D F A | 5,472 | 8,080 | 21.4 | 59% | 0% | 100% | 73 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D F C | 5,467 | 18,030 | 0.0 | 45% | 40% | 100% | 219 KB | 1 |
| [Disinto/disinto](https://github.com/Disinto/disinto) | D C D | 5,303 | 5,550 | 0.0 | 72% | 25% | – | 80 KB | 0 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,258 | 10,628 | 28.1 | 58% | 11% | 88% | 1,492 KB | 69,941 |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 5,234 | 33,670 | 10.4 | 30% | 0% | 94% | 67 KB | 1 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | E D C | 4,999 | 6,808 | 0.0 | 64% | 39% | 69% | 1,001 KB | 32 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E C D | 4,967 | 7,647 | 26.0 | 76% | 16% | – | 327 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 4,787 | 6,434 | 18.4 | 39% | 9% | 100% | 528 KB | 5 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E F B | 4,760 | 7,821 | 12.9 | 34% | 37% | 100% | 992 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F D | 4,754 | 66,297 | 8.2 | 49% | 18% | 2% | 411 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E D C | 4,383 | 16,099 | 0.0 | 60% | 25% | 56% | 140 KB | 107 (+1) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 4,288 | 6,465 | 28.6 | 35% | 0% | 52% | 92 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 4,027 | 10,480 | 8.4 | 39% | 10% | 92% | 755 KB | 2 |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 3,919 | 6,828 | 29.7 | 63% | 0% | 100% | 129 KB | 20 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 3,895 | 9,460 | 24.2 | 0% | 0% | 100% | 489 KB | 27 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,783 | 8,281 | 9.2 | 57% | 9% | 98% | 329 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | E F B | 3,690 | 9,347 | 0.0 | 79% | 20% | 84% | 200 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E C | 3,636 | 10,961 | 17.2 | 76% | 32% | 51% | 63 KB | 10 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E C C | 3,626 | 15,556 | 19.9 | 77% | 58% | 100% | 157 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,987 | 7,020 | 0.0 | 2% | 0% | 33% | 397 KB | 455 |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 2,959 | 8,297 | 0.1 | 24% | 41% | 0% | 425 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,912 | 10,707 | 28.8 | 44% | 12% | 100% | 617 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E B D | 2,865 | 6,388 | 0.0 | 88% | 9% | – | 202 KB | 4 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 2,735 | 7,934 | 49.6 | 71% | 8% | 90% | 170 KB | 8 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E D A | 2,703 | 4,728 | 31.7 | 68% | 14% | 97% | 117 KB | 1 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,639 | 4,134 | 42.2 | 58% | 40% | 98% | 282 KB | 2 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E E B | 2,511 | 14,149 | 18.1 | 43% | 0% | 100% | 120 KB | 0 |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 2,305 | 95,699 | 0.6 | 44% | 24% | 55% | 5,159 KB | 1 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 2,282 | 12,936 | 19.7 | 43% | 0% | 89% | 302 KB | 22 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 2,167 | 3,864 | 0.1 | 44% | 0% | 97% | 228 KB | 3 (+1) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | E F D | 2,159 | 8,856 | 23.2 | 77% | 0% | 0% | 153 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 2,142 | 5,704 | 12.3 | 40% | 5% | – | 55 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | E E C | 1,992 | 12,564 | 6.9 | 57% | 0% | 98% | 42 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,942 | 6,571 | 11.6 | 24% | 21% | 96% | 216 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,857 | 4,059 | 13.7 | 78% | 0% | 92% | 260 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,573 | 2,390 | 0.2 | 66% | 6% | 13% | 613 KB | 3 |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 1,475 | 8,398 | 23.5 | 43% | 23% | 98% | 123 KB | 1 |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 1,448 | 15,247 | 17.4 | 51% | 15% | 99% | 593 KB | 11 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,441 | 2,948 | 2.4 | 25% | 22% | 99% | 7,014 KB | 18 |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 1,330 | 7,888 | 5.6 | 10% | 13% | 81% | 466 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 1,241 | 10,034 | 16.0 | 62% | 0% | – | 408 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E E A | 1,195 | 2,484 | 16.6 | 64% | 0% | 99% | 154 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,149 | 10,838 | 13.4 | 55% | 32% | 100% | 953 KB | 0 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 902 | 5,051 | 0.0 | 38% | 0% | – | 15 KB | 0 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 341 | 658 | 7.6 | 0% | 0% | 76% | 72 KB | 4 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F C | 307 | 8,584 | 6.9 | 45% | 20% | 99% | 43 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 211 | 25,360 | 12.2 | 57% | 0% | 99% | 66 KB | 3 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 189 | 4,282 | 0.0 | 0% | 0% | 0% | 473 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 167 | 1,657 | 0.0 | 38% | 0% | – | 59 KB | 1 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 98 | 1,629 | 3.3 | 89% | 0% | 100% | 59 KB | 1 |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 38 | 1,163 | 11.0 | 39% | 0% | 100% | 173 KB | 215 (+2) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 24 | 10,720 | 0.2 | 39% | 0% | 86% | 1,449 KB | 1,093 (+3) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 2,769 | 38.2 | 35% | 0% | 100% | 847 KB | 3 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 396,662 | 35.7 | 30% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 28.9 | 62% | 52% | 84% | 1,977 KB | 1,364 (+6) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F E B | – | – | 23.5 | 58% | 7% | 100% | 1,042 KB | 0 |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F E B | – | – | 15.4 | 62% | 0% | 98% | 723 KB | 5 (+1) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 1,725 | 13.6 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 884 | 6.8 | 0% | 0% | 95% | 150 KB | 346 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 3.0 | 63% | 69% | 0% | 1,061 KB | 455 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F E D | 0 | 0 | 1.4 | 76% | 29% | – | 5,619 KB | 0 |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 72% | 91% | 87% | 812 KB | 4 |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 2,111 | 0.2 | 24% | 0% | 3% | 904 KB | 1,265 (+4) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 70% | 17% | 97% | 14,566 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 2,324 | 0.1 | 33% | 0% | 100% | 133 KB | 7 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D D | – | – | 0.0 | 63% | 42% | 47% | 72 KB | 5 (+0) |
<!-- END GENERATED -->

## Running it

The list is kept up to date by two scripts, each of which pulls, runs, commits and pushes:

```sh
scripts/daily.sh      # find new candidates and screen them (steps 1 and 2)
scripts/hourly.sh     # recheck waiting repos (steps 3 and 4) and measure the listed ones
```

Classifying newly listed repos is run by hand with `python -m asf classify`, which needs the `claude` CLI signed in;
[context/classify-workflow.md](context/classify-workflow.md) has the steps.

You need Python 3.11 or newer, git, and a GitHub token (`GH_TOKEN`, or a signed-in `gh`). There are no other
dependencies. [context/](context/index.md) has the details for running and maintaining it, written for people and
coding agents alike.

## License

The code is [MIT](LICENSE). The data and reports are [CC BY 4.0](LICENSE-DATA).
