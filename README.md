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
_150 repos, last measured 2026-10-12. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (150)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 110,458 | 126,941 | 46.6 | 12% | 15% | 97% | 2,582 KB | 1,737 |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 72,907 | 178,176 | 0.2 | 59% | 12% | 27% | 1,271 KB | 431 |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | A C C | 51,503 | 77,356 | 0.2 | 74% | 24% | 82% | 261 KB | 0 |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 49,971 | 116,447 | 31.0 | 76% | 39% | 98% | 220 KB | 1 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A E A | 47,027 | 63,596 | 68.3 | 66% | 56% | 100% | 154 KB | 14 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A D B | 47,024 | 82,109 | 29.9 | 62% | 25% | 92% | 2,572 KB | 34 (+1) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 45,138 | 73,403 | 20.7 | 73% | 26% | 99% | 608 KB | 10 (+1) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A C C | 43,215 | 62,387 | 54.3 | 73% | 17% | 100% | 665 KB | 14 |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 40,143 | 45,977 | 20.6 | 46% | 6% | 100% | 709 KB | 1 (+1) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 38,535 | 2,201,681 | 75.4 | 4% | 16% | 42% | 3,975 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B E C | 34,623 | 60,291 | 36.5 | 58% | 73% | 79% | 2,306 KB | 4 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B D B | 33,549 | 177,930 | 26.6 | 67% | 32% | 86% | 1,403 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | B E B | 32,115 | 45,749 | 0.0 | 52% | 18% | 86% | 608 KB | 1 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 31,834 | 36,438 | 139 | 68% | 70% | 100% | 3,135 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B B A | 31,361 | 62,407 | 41.8 | 84% | 38% | 100% | 118 KB | 1 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | B C B | 29,723 | 64,358 | 22.7 | 72% | 11% | 96% | 375 KB | 9 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 28,449 | 53,060 | 15.7 | 78% | 0% | 97% | 94 KB | 16 (+1) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B E B | 27,886 | 37,078 | 72.1 | 59% | 11% | 98% | 596 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B C D | 26,462 | 48,295 | 0.0 | 78% | 48% | 44% | 248 KB | 0 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 25,266 | 25,763 | 0.0 | 76% | 42% | – | 226 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B B B | 25,049 | 28,484 | 11.1 | 84% | 57% | 86% | 421 KB | 0 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F C | 24,396 | 48,623 | 87.4 | 37% | 15% | 50% | 314 KB | 3 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 24,013 | 32,549 | 31.8 | 72% | 18% | 95% | 599 KB | 22 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B D D | 23,933 | 598,718 | 0.0 | 67% | 0% | 0% | 3,283 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 23,195 | 48,808 | 30.1 | 51% | 10% | 95% | 54 KB | 0 |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B E B | 23,115 | 27,004 | 11.7 | 58% | 37% | 98% | 688 KB | 9 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | B E A | 22,614 | 36,889 | 31.0 | 65% | 24% | 98% | 139 KB | 4 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 22,100 | 36,363 | 0.0 | 68% | 58% | – | 1,189 KB | 2 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 21,696 | 32,654 | 24.5 | 34% | 26% | 98% | 1,245 KB | 89 (+1) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 21,649 | 45,711 | 38.0 | 84% | 46% | 100% | 350 KB | 2 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 21,495 | 24,581 | 21.5 | 78% | 51% | 73% | 364 KB | 9 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B E A | 21,227 | 35,532 | 0.1 | 57% | 3% | 100% | 163 KB | 9 |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | B E F | 20,583 | 347,265 | 6.8 | 55% | 9% | – | 331 KB | 4 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | B E F | 20,572 | 233,822 | 0.0 | 61% | 20% | – | 8,190 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C F C | 19,781 | 46,415 | 20.5 | 67% | 0% | 94% | 100 KB | 110 (+7) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | C F C | 17,791 | 36,662 | 1.0 | 38% | 0% | 72% | 290 KB | 0 |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E D | 17,784 | 71,167 | 16.0 | 62% | 47% | 20% | 304 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C D D | 17,523 | 31,225 | 0.0 | 69% | 31% | 42% | 265 KB | 0 |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 17,364 | 42,141 | 23.8 | 38% | 36% | 95% | 448 KB | 18 (+1) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 16,462 | 126,471 | 0.0 | 68% | 39% | 50% | 451 KB | 1 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C D A | 16,446 | 23,366 | 5.3 | 63% | 27% | 96% | 375 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | C E A | 16,101 | 34,807 | 10.5 | 67% | 19% | 93% | 236 KB | 5 |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | C E A | 15,925 | 18,478 | 13.7 | 83% | 22% | 98% | 149 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 15,857 | 32,046 | 0.0 | 66% | 1% | – | 699 KB | 0 |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 15,647 | 21,929 | 54.1 | 76% | 42% | 91% | 4,310 KB | 15 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 15,555 | 31,767 | 53.4 | 64% | 70% | 100% | 768 KB | 6,233 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C C B | 15,013 | 24,566 | 51.0 | 76% | 69% | 98% | 573 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 14,951 | 19,848 | 84.2 | 24% | 56% | 76% | 340 KB | 48 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C E B | 14,914 | 26,406 | 27.2 | 52% | 12% | 100% | 6,926 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 14,885 | 17,028 | 14.2 | 52% | 39% | 100% | 567 KB | 0 |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 14,806 | 22,788 | 33.9 | 80% | 39% | 78% | 1,340 KB | 3 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F C | 14,389 | 18,621 | 35.0 | 0% | 32% | 67% | 66 KB | 59 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 13,877 | 43,624 | 164 | 49% | 11% | 89% | 2,294 KB | 3 |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C D A | 13,637 | 38,395 | 0.0 | 65% | 12% | 94% | 211 KB | 0 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 13,565 | 17,076 | 4.5 | 0% | 0% | 97% | 356 KB | 126 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,425 | 20,104 | 18.6 | 72% | 56% | 98% | 116 KB | 32 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 13,266 | 17,114 | 15.8 | 62% | 24% | 90% | 1,158 KB | 13 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C E A | 12,431 | 93,626 | 17.9 | 48% | 10% | 97% | 107 KB | 3 |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C D A | 12,299 | 20,815 | 31.9 | 66% | 50% | 96% | 260 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | C D B | 11,924 | 15,218 | 23.9 | 64% | 66% | 98% | 103 KB | 4 |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C F A | 11,848 | 20,624 | 17.2 | 37% | 12% | 98% | 110 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 11,818 | 25,850 | 12.3 | 87% | 30% | 80% | 77 KB | 4 |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C E C | 11,735 | 21,220 | 0.0 | 54% | 21% | 86% | 804 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C A | 11,204 | 16,126 | 34.4 | 70% | 23% | 86% | 102 KB | 229 (+2) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 11,110 | 24,508 | 42.4 | 48% | 12% | 98% | 324 KB | 3 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C E C | 10,689 | 25,978 | 10.0 | 52% | 0% | 81% | 729 KB | 4 |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | C C B | 10,568 | 14,541 | 21.9 | 78% | 68% | 100% | 956 KB | 91 |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | C C C | 10,474 | 16,047 | 9.6 | 74% | 35% | 92% | 112 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 10,333 | 13,831 | 18.0 | 78% | 76% | 94% | 519 KB | 1 |
| [floor/teamcli](https://github.com/floor/teamcli) | C E B | 10,293 | 20,970 | 7.5 | 42% | 10% | 81% | 67 KB | 2 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 10,109 | 21,043 | 48.3 | 40% | 25% | 99% | 665 KB | 3 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D D C | 9,313 | 14,686 | 5.1 | 66% | 19% | 96% | 104 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,099 | 15,605 | 8.0 | 62% | 14% | 100% | 473 KB | 11 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D D A | 8,568 | 19,871 | 7.6 | 64% | 18% | 99% | 110 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | D F D | 8,150 | 15,783 | 11.1 | 74% | 0% | – | 115 KB | 0 |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D C B | 7,932 | 22,535 | 19.1 | 73% | 19% | 99% | 1,753 KB | 5 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D C C | 7,510 | 11,772 | 13.2 | 70% | 31% | 100% | 601 KB | 8 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 7,504 | 11,503 | 19.9 | 50% | 0% | 85% | 359 KB | 6 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 7,397 | 14,742 | 23.6 | 29% | 33% | 92% | 643 KB | 17 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | D E A | 7,275 | 8,435 | 29.6 | 67% | 0% | 99% | 129 KB | 20 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 7,201 | 12,882 | 0.0 | 77% | 18% | 81% | 293 KB | 0 |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 6,721 | 9,275 | 24.2 | 71% | 65% | – | 612 KB | 2 |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D E D | 6,693 | 12,358 | 0.0 | 59% | 2% | – | 94 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,529 | 26,393 | 0.0 | 43% | 0% | 100% | 435 KB | 1 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D E C | 6,507 | 8,408 | 27.0 | 54% | 0% | 52% | 92 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D E B | 6,195 | 16,253 | 18.0 | 58% | 0% | 84% | 384 KB | 19 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | D E A | 5,894 | 9,144 | 21.5 | 62% | 0% | 100% | 73 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D C D | 5,887 | 12,710 | 23.2 | 78% | 0% | 0% | 153 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 5,849 | 7,207 | 12.8 | 76% | 0% | 100% | 89 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D F C | 5,644 | 9,340 | 13.1 | 38% | 8% | 100% | 403 KB | 2 |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D F C | 5,467 | 18,030 | 0.0 | 45% | 40% | 100% | 219 KB | 1 |
| [Disinto/disinto](https://github.com/Disinto/disinto) | D C D | 5,303 | 5,550 | 0.0 | 72% | 25% | – | 80 KB | 0 |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 5,283 | 7,316 | 16.4 | 50% | 33% | 100% | 527 KB | 5 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,258 | 10,628 | 28.1 | 58% | 11% | 88% | 1,492 KB | 69,941 |
| [tampajohn/chug](https://github.com/tampajohn/chug) | D E D | 5,119 | 9,223 | 0.0 | 73% | 13% | – | 202 KB | 4 |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 4,965 | 9,340 | 24.1 | 0% | 0% | 100% | 489 KB | 27 |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E E D | 4,858 | 94,290 | 8.0 | 54% | 34% | 2% | 403 KB | 1 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E E B | 4,760 | 7,843 | 12.5 | 52% | 34% | 100% | 991 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 4,727 | 23,493 | 0.2 | 68% | 0% | 86% | 1,449 KB | 1,090 |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | E F C | 3,944 | 7,944 | 8.0 | 46% | 0% | 91% | 94 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 3,840 | 11,593 | 28.6 | 31% | 9% | 100% | 617 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E E D | 3,822 | 7,640 | 11.7 | 48% | 7% | – | 55 KB | 0 |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,783 | 6,598 | 7.9 | 42% | 8% | 99% | 327 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | E C C | 3,760 | 4,681 | 0.0 | 71% | 45% | 70% | 1,000 KB | 32 (+1) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F C | 3,643 | 15,703 | 0.0 | 35% | 0% | 57% | 140 KB | 106 (+1) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 3,457 | 5,205 | 21.5 | 74% | 17% | 100% | 159 KB | 0 |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E E C | 3,174 | 9,035 | 0.5 | 51% | 34% | 95% | 2,862 KB | 526 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E A D | 3,043 | 10,972 | 16.6 | 92% | 32% | 40% | 65 KB | 10 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 3,006 | 38,753 | 9.4 | 36% | 0% | 94% | 67 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,987 | 7,020 | 0.0 | 2% | 0% | 33% | 397 KB | 455 |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 2,832 | 97,459 | 0.5 | 53% | 11% | 63% | 4,989 KB | 1 |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 2,735 | 8,865 | 51.4 | 73% | 7% | 96% | 169 KB | 7 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E E A | 2,721 | 4,716 | 32.1 | 80% | 20% | 100% | 117 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 2,673 | 8,816 | 0.3 | 32% | 34% | 0% | 425 KB | 0 |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E C B | 2,668 | 5,248 | 42.2 | 79% | 40% | 96% | 267 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 2,593 | 9,378 | 5.1 | 66% | 9% | 81% | 466 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E E B | 2,511 | 14,149 | 18.1 | 43% | 0% | 100% | 120 KB | 0 |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 2,503 | 14,418 | 20.5 | 39% | 23% | 90% | 302 KB | 22 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,263 | 16,683 | 0.0 | 3% | 0% | – | 189 KB | 26 |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 2,183 | 3,961 | 0.1 | 48% | 0% | 97% | 193 KB | 2 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | E F C | 2,100 | 22,347 | 6.9 | 45% | 0% | 98% | 42 KB | 0 |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 2,092 | 5,316 | 13.5 | 72% | 0% | 84% | 258 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,871 | 6,397 | 11.0 | 38% | 22% | 97% | 216 KB | 1 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,573 | 2,390 | 0.2 | 66% | 6% | 13% | 613 KB | 3 |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E E A | 1,543 | 4,203 | 16.5 | 75% | 10% | 99% | 154 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,441 | 2,948 | 2.4 | 25% | 22% | 99% | 7,014 KB | 18 |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,318 | 11,365 | 13.7 | 67% | 29% | 100% | 953 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 679 | 4,267 | 38.2 | 48% | 0% | 100% | 845 KB | 3 |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 466 | 2,166 | 0.2 | 38% | 0% | 3% | 904 KB | 1,261 |
| [obselate/tokate](https://github.com/obselate/tokate) | F F C | 463 | 11,555 | 6.5 | 57% | 0% | 100% | 43 KB | 1 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 365 | 755 | 7.9 | 0% | 0% | 77% | 72 KB | 4 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 341 | 9,269 | 15.3 | 41% | 0% | – | 408 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F E B | 198 | 24,699 | 11.7 | 64% | 23% | 97% | 66 KB | 3 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 132 | 4,350 | 0.0 | 0% | 0% | 0% | 473 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 125 | 1,636 | 0.0 | 41% | 0% | – | 59 KB | 1 (+1) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 30 | 757 | 12.0 | 25% | 0% | 98% | 174 KB | 213 |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 343,497 | 31.9 | 0% | 0% | 100% | 703 KB | 0 |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 26.4 | 46% | 33% | 89% | 1,966 KB | 1,358 |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F E B | – | – | 23.5 | 58% | 7% | 100% | 1,042 KB | 0 |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F E A | – | – | 19.0 | 76% | 0% | 96% | 120 KB | 4 |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 2,087 | 12.5 | 35% | 0% | 91% | 306 KB | 7 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,114 | 6.8 | 0% | 0% | 95% | 150 KB | 346 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 3.0 | 55% | 71% | 0% | 1,061 KB | 455 |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F E D | 0 | 0 | 1.4 | 76% | 29% | – | 5,619 KB | 0 |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 72% | 91% | 87% | 812 KB | 4 |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 76% | 16% | 97% | 14,566 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 2,174 | 0.1 | 34% | 0% | 100% | 133 KB | 7 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 60% | 40% | 52% | 72 KB | 5 (+0) |
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
