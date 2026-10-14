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
_195 repos, last measured 2026-10-14. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (195)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 91,868 | 138,507 | 61.4 | 23% | 51% | 73% | 2,969 KB | 1,810 (+72) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 77,450 | 101,177 | 31.0 | 83% | 42% | 98% | 231 KB | 1 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 64,701 | 66,939 | 59.9 | 85% | 65% | 86% | 680 KB | 14 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A D B | 60,062 | 77,590 | 23.6 | 70% | 23% | 96% | 616 KB | 10 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | A F B | 50,970 | 292,534 | 72.6 | 25% | 55% | 89% | 563 KB | 2 |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A C A | 48,946 | 63,907 | 85.9 | 79% | 48% | 98% | 162 KB | 14 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 42,904 | 47,923 | 27.5 | 53% | 49% | 97% | 716 KB | 1 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A B B | 42,494 | 91,730 | 33.0 | 82% | 30% | 88% | 2,585 KB | 34 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | A E C | 42,057 | 54,838 | 45.5 | 50% | 57% | 94% | 596 KB | 2 |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B E C | 37,574 | 92,092 | 42.8 | 50% | 43% | 97% | 2,376 KB | 4 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 36,307 | 2,156,779 | 75.0 | 0% | 0% | 77% | 3,975 KB | 1 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 34,143 | 37,537 | 33.5 | 71% | 62% | 100% | 599 KB | 22 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B E C | 33,869 | 133,797 | 0.2 | 40% | 0% | 65% | 1,271 KB | 432 (+1) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 33,850 | 100,279 | 22.4 | 64% | 26% | 100% | 753 KB | 31 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 32,360 | 48,720 | 19.5 | 83% | 0% | 97% | 94 KB | 16 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B C B | 31,751 | 38,277 | 145 | 78% | 78% | 100% | 3,163 KB | 1 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B C B | 31,567 | 45,341 | 27.9 | 76% | 59% | 100% | 1,306 KB | 91 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B D B | 30,100 | 36,022 | 73.4 | 60% | 16% | 97% | 624 KB | 0 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 27,229 | 26,882 | 0.0 | 86% | 68% | – | 225 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B C C | 26,625 | 75,340 | 0.2 | 72% | 48% | 100% | 291 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 25,737 | 50,537 | 45.1 | 75% | 46% | 98% | 154 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 25,007 | 69,892 | 31.7 | 48% | 13% | 100% | 54 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B E B | 24,011 | 36,389 | 16.0 | 62% | 37% | 92% | 430 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 23,992 | 51,639 | 39.9 | 84% | 66% | 100% | 353 KB | 2 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B E B | 23,115 | 27,314 | 12.9 | 57% | 31% | 99% | 703 KB | 9 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 22,574 | 47,599 | 0.0 | 65% | 62% | – | 1,193 KB | 3 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B C A | 22,385 | 40,512 | 0.2 | 72% | 28% | 99% | 163 KB | 9 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 22,059 | 34,528 | 23.4 | 83% | 50% | 86% | 364 KB | 9 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B E C | 21,165 | 52,166 | 154 | 59% | 29% | 89% | 2,294 KB | 3 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B F D | 20,755 | 41,145 | 0.0 | 60% | 0% | 42% | 248 KB | 0 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 20,435 | 72,888 | 90.4 | 32% | 44% | 46% | 310 KB | 3 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | B F C | 20,323 | 48,004 | 25.5 | 37% | 39% | 99% | 448 KB | 18 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C E D | 19,679 | 22,529 | 10.0 | 53% | 3% | – | 81 KB | 2 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 19,558 | 31,794 | 29.2 | 88% | 33% | 97% | 146 KB | 4 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | C E D | 19,083 | 46,168 | 22.7 | 45% | 56% | 34% | 3,082 KB | 96 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E C | 19,002 | 88,862 | 19.7 | 59% | 43% | 64% | 304 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 19,001 | 36,663 | 51.9 | 62% | 16% | 99% | 324 KB | 3 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 18,992 | 20,503 | 32.0 | 26% | 0% | 100% | 404 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C E C | 17,806 | 42,809 | 32.2 | 71% | 0% | 87% | 119 KB | 115 (+1) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C D B | 17,556 | 26,228 | 49.0 | 64% | 72% | 99% | 571 KB | 2 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C B C | 17,081 | 42,226 | 0.0 | 82% | 15% | 50% | 455 KB | 1 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 16,191 | 20,271 | 56.0 | 80% | 66% | 98% | 4,310 KB | 15 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 15,975 | 32,828 | 0.0 | 53% | 15% | – | 776 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 15,685 | 27,217 | 21.2 | 57% | 47% | 98% | 114 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 15,620 | 28,827 | 12.7 | 73% | 39% | 78% | 126 KB | 5 (+1) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 14,833 | 20,999 | 58.0 | 57% | 67% | 98% | 768 KB | 6,297 (+25) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C C B | 14,767 | 150,552 | 27.9 | 82% | 6% | 84% | 1,403 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C F A | 13,979 | 33,078 | 0.0 | 39% | 0% | 94% | 211 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C E A | 13,556 | 21,023 | 34.2 | 58% | 50% | 95% | 298 KB | 0 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,495 | 17,959 | 18.7 | 77% | 47% | 100% | 123 KB | 32 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 13,373 | 15,473 | 40.8 | 0% | 59% | 100% | 66 KB | 60 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 13,329 | 24,345 | 26.1 | 51% | 27% | 99% | 571 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 13,143 | 12,382 | 19.1 | 80% | 19% | 94% | 531 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C E D | 13,112 | 21,547 | 0.0 | 77% | 27% | 42% | 265 KB | 0 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 13,102 | 19,468 | 32.3 | 63% | 55% | 86% | 1,389 KB | 3 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 12,963 | 22,742 | 28.4 | 38% | 29% | 100% | 223 KB | 6 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | C E A | 12,953 | 36,492 | 11.5 | 57% | 0% | 91% | 236 KB | 5 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C E B | 12,796 | 40,711 | 24.2 | 40% | 16% | 97% | 377 KB | 9 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 12,476 | 16,826 | 86.1 | 19% | 51% | 76% | 340 KB | 48 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | C C D | 12,453 | 23,174 | 0.0 | 85% | 0% | 30% | 17 KB | 0 |
| [integry/propr](https://github.com/integry/propr) | C E B | 12,298 | 22,530 | 11.5 | 58% | 10% | 100% | 4,314 KB | 17 |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C D C | 12,174 | 21,057 | 7.6 | 60% | 59% | 95% | 109 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 11,995 | 100,879 | 21.0 | 43% | 14% | 97% | 112 KB | 3 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C C C | 11,735 | 18,532 | 0.0 | 74% | 12% | 86% | 844 KB | 1 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 11,730 | 576,356 | 0.0 | 87% | 0% | 0% | 3,283 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | C D D | 11,475 | 15,216 | 17.7 | 60% | 18% | – | 374 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D A | 11,206 | 14,993 | 32.7 | 68% | 38% | 86% | 102 KB | 228 (-1) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 11,012 | 31,639 | 11.3 | 40% | 21% | 89% | 2,756 KB | 114 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | C E F | 10,939 | 223,235 | 0.0 | 60% | 35% | – | 8,190 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 10,724 | 18,312 | 49.0 | 14% | 47% | 99% | 677 KB | 3 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C C B | 10,494 | 24,968 | 20.1 | 75% | 31% | 100% | 1,032 KB | 6 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 10,492 | 25,984 | 0.0 | 60% | 10% | 90% | 564 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C F B | 10,490 | 170,521 | 18.7 | 26% | 6% | 100% | 1,414 KB | 0 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 10,486 | 23,611 | 20.5 | 54% | 26% | 100% | 1,772 KB | 5 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 10,104 | 29,424 | 14.1 | 19% | 14% | 93% | 67 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | D E B | 9,780 | 24,206 | 27.9 | 71% | 14% | 100% | 6,926 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 9,680 | 9,458 | 9.4 | 43% | 0% | 89% | 97 KB | 3 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D F B | 9,656 | 13,140 | 5.9 | 36% | 11% | 81% | 387 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | D F F | 9,458 | 372,401 | 7.0 | 56% | 0% | – | 331 KB | 4 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | D E B | 9,388 | 11,847 | 7.6 | 49% | 2% | 77% | 67 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | D E A | 9,340 | 9,536 | 12.5 | 54% | 0% | 98% | 149 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D F B | 9,317 | 24,424 | 13.0 | 61% | 0% | 90% | 759 KB | 4 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D E C | 9,122 | 13,882 | 15.9 | 57% | 22% | 100% | 615 KB | 8 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,099 | 12,587 | 8.0 | 19% | 15% | 100% | 490 KB | 11 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | D D C | 8,887 | 18,714 | 18.0 | 67% | 39% | 98% | 398 KB | 0 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F A | 8,658 | 13,322 | 4.5 | 0% | 0% | 98% | 386 KB | 127 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D E A | 8,568 | 14,026 | 9.5 | 50% | 7% | 99% | 110 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D D C | 8,179 | 12,334 | 24.4 | 66% | 5% | 100% | 403 KB | 2 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 8,164 | 15,796 | 35.5 | 13% | 9% | 84% | 649 KB | 36 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F C | 7,658 | 9,670 | 18.5 | 51% | 24% | 67% | 359 KB | 6 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | D E B | 7,480 | 13,360 | 24.0 | 47% | 40% | 98% | 964 KB | 93 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | D E E | 7,388 | 7,495 | 19.0 | 56% | 6% | 95% | 549 KB | 0 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D E C | 7,173 | 13,796 | 27.8 | 71% | 17% | 68% | 185 KB | 0 |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D E B | 7,160 | 11,539 | 26.6 | 69% | 0% | 97% | 105 KB | 4 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D E C | 7,130 | 12,221 | 9.7 | 53% | 29% | 97% | 6,579 KB | 8 |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D F A | 7,111 | 8,750 | 7.0 | 36% | 0% | 96% | 238 KB | 0 |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 7,022 | 8,194 | 13.9 | 76% | 46% | 99% | 92 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 6,897 | 8,413 | 10.2 | 71% | 56% | 92% | 112 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 6,721 | 24,612 | 0.0 | 12% | 0% | – | 189 KB | 26 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 6,715 | 10,672 | 20.0 | 56% | 0% | 92% | 700 KB | 4 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D B B | 6,616 | 9,668 | 29.4 | 88% | 13% | 96% | 1,499 KB | 70,001 (+60) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F D | 6,604 | 17,610 | 0.0 | 62% | 27% | 44% | 200 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D E D | 6,594 | 7,955 | 0.0 | 70% | 0% | – | 108 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,540 | 21,299 | 0.0 | 55% | 0% | 100% | 435 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 6,530 | 12,058 | 17.4 | 54% | 0% | 87% | 385 KB | 19 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D E B | 6,374 | 15,238 | 19.4 | 58% | 5% | 100% | 238 KB | 1 |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 6,335 | 11,862 | 1.7 | 42% | 32% | 74% | 3,086 KB | 533 (+4) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 6,053 | 7,986 | 8.9 | 54% | 26% | 30% | 188 KB | 2 |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | D E C | 5,983 | 21,658 | 1.2 | 51% | 0% | 68% | 290 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D D B | 5,846 | 10,078 | 13.7 | 63% | 34% | 100% | 994 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D E C | 5,743 | 9,525 | 0.0 | 60% | 31% | 69% | 1,015 KB | 32 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D D C | 5,629 | 8,372 | 25.0 | 65% | 0% | 98% | 536 KB | 17 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D E C | 5,467 | 16,660 | 0.0 | 53% | 12% | 98% | 226 KB | 1 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 5,457 | 7,890 | 26.9 | 74% | 17% | – | 332 KB | 2 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D E B | 5,315 | 31,051 | 0.0 | 54% | 39% | 99% | 398 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | D F A | 5,271 | 6,879 | 21.2 | 63% | 0% | 100% | 73 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D D C | 5,200 | 38,692 | 3.9 | 62% | 6% | 100% | 1,116 KB | 5 |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | D F D | 5,164 | 13,100 | 11.7 | 61% | 0% | – | 115 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 5,088 | 8,400 | 20.6 | 39% | 22% | 100% | 543 KB | 5 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E C B | 4,297 | 11,395 | 17.8 | 76% | 37% | 75% | 64 KB | 10 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 4,288 | 5,699 | 27.5 | 23% | 0% | 52% | 92 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E E C | 4,226 | 17,124 | 0.0 | 58% | 43% | 51% | 142 KB | 107 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,090 | 7,505 | 14.9 | 41% | 0% | 99% | 140 KB | 0 |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 3,982 | 6,749 | 13.6 | 32% | 0% | – | 43 KB | 3 |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F D | 3,937 | 53,492 | 8.5 | 57% | 0% | 5% | 428 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 3,716 | 10,587 | 24.7 | 0% | 0% | 94% | 489 KB | 27 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,462 | 8,158 | 9.4 | 57% | 4% | 98% | 329 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 3,349 | 15,285 | 19.0 | 58% | 58% | 100% | 157 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E E A | 3,332 | 4,442 | 17.8 | 50% | 19% | 100% | 386 KB | 1 |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E E D | 3,302 | 6,712 | 13.2 | 56% | 0% | – | 96 KB | 0 |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 3,243 | 9,457 | 8.6 | 31% | 11% | 96% | 757 KB | 2 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,953 | 14,350 | 10.0 | 46% | 0% | 96% | 236 KB | 2 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E D B | 2,831 | 8,939 | 48.2 | 68% | 55% | 88% | 119 KB | 8 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,754 | 8,028 | 0.0 | 33% | 13% | 97% | 325 KB | 0 |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 2,689 | 12,221 | 0.7 | 54% | 19% | 40% | 5,234 KB | 1 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,664 | 4,659 | 42.5 | 59% | 29% | 99% | 285 KB | 2 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 2,614 | 5,857 | 0.2 | 33% | 15% | 0% | 427 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F B | 2,462 | 12,548 | 13.8 | 66% | 0% | 93% | 1,177 KB | 13 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,366 | 7,045 | 27.5 | 63% | 0% | 100% | 129 KB | 21 (+1) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,318 | 6,320 | 26.9 | 53% | 0% | 47% | 94 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,244 | 9,207 | 28.3 | 36% | 15% | 100% | 617 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,100 | 9,624 | 24.5 | 28% | 24% | 98% | 124 KB | 1 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 2,067 | 11,815 | 20.0 | 32% | 0% | 89% | 303 KB | 22 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 1,987 | 13,990 | 18.2 | 55% | 14% | 99% | 596 KB | 11 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,871 | 4,492 | 12.2 | 41% | 24% | 96% | 216 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 1,817 | 4,867 | 0.0 | 64% | 0% | – | 202 KB | 4 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E E A | 1,779 | 4,058 | 29.8 | 72% | 0% | 97% | 117 KB | 1 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 1,692 | 5,013 | 0.1 | 52% | 0% | 86% | 237 KB | 3 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,683 | 5,776 | 3.8 | 19% | 11% | 97% | 7,014 KB | 18 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 1,651 | 4,461 | 12.5 | 37% | 12% | – | 55 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | E E D | 1,648 | 3,455 | 0.0 | 80% | 0% | – | 80 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,624 | 2,505 | 13.7 | 42% | 0% | 97% | 267 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E F D | 1,573 | 2,399 | 0.2 | 56% | 26% | 10% | 626 KB | 3 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,551 | 2,421 | 16.9 | 54% | 27% | 97% | 417 KB | 1 |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,520 | 5,810 | 0.0 | 43% | 12% | – | 433 KB | 2 |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | E F C | 1,341 | 2,685 | 6.9 | 53% | 0% | 98% | 42 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,259 | 3,284 | 1.9 | 35% | 0% | 33% | 54 KB | 0 |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,207 | 3,186 | 20.1 | 24% | 0% | 100% | 120 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,149 | 10,314 | 13.0 | 60% | 0% | 100% | 953 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,089 | 4,836 | 24.5 | 19% | 33% | 99% | 511 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 916 | 3,206 | 5.6 | 3% | 0% | 81% | 466 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 638 | 1,164 | 15.6 | 48% | 0% | 100% | 154 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 591 | 6,921 | 0.0 | 3% | 0% | 33% | 397 KB | 456 (+1) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 421 | 1,384 | 0.0 | 26% | 7% | – | 18 KB | 0 |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 341 | 7,422 | 16.1 | 22% | 0% | – | 408 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 316 | 44,400 | 12.5 | 69% | 40% | 99% | 66 KB | 3 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F C | 313 | 6,852 | 8.4 | 43% | 28% | 98% | 43 KB | 1 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 308 | 4,820 | 0.0 | 31% | 0% | – | 15 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 189 | 4,377 | 0.0 | 17% | 0% | 0% | 473 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 177 | 1,510 | 10.3 | 58% | 0% | 100% | 173 KB | 217 (+1) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 167 | 1,463 | 0.0 | 40% | 0% | – | 59 KB | 1 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 159 | 9,172 | 1.5 | 62% | 0% | 25% | 149 KB | 0 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 111 | 737 | 7.7 | 0% | 0% | 94% | 72 KB | 4 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 68 | 745 | 3.2 | 60% | 0% | 100% | 59 KB | 1 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 62 | 2,849 | 0.0 | 31% | 0% | 0% | 109 KB | 0 |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 45 | 390 | 1.1 | 32% | 0% | 100% | 94 KB | 2 |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 26 | 3,320 | 23.2 | 68% | 0% | 0% | 153 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 13 | 2,398 | 0.1 | 33% | 0% | 100% | 133 KB | 7 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 420,720 | 38.9 | 30% | 0% | 100% | 703 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 2,253 | 35.8 | 30% | 0% | 100% | 847 KB | 3 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 31.0 | 60% | 49% | 85% | 1,999 KB | 1,380 (+10) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 22.0 | 33% | 12% | 100% | 1,068 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 19.8 | 49% | 21% | 93% | 892 KB | 4 |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 16.1 | 57% | 0% | 98% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 1,720 | 13.9 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 5 | 6.8 | 0% | 0% | 95% | 150 KB | 346 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 3.4 | 64% | 82% | 0% | 1,061 KB | 457 (+2) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 0 | 1.0 | 67% | 0% | – | 5,619 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 76% | 16% | 78% | 812 KB | 4 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F D D | 0 | 0 | 0.3 | 67% | 0% | – | 232 KB | 1 |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 7,723 | 0.2 | 49% | 0% | 86% | 1,449 KB | 1,094 (+1) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 162 | 0.2 | 0% | 0% | 6% | 904 KB | 1,273 (+3) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.2 | 52% | 22% | 97% | 14,566 KB | 0 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D C | – | – | 0.0 | 62% | 41% | 66% | 72 KB | 5 (+0) |
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
