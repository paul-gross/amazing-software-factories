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
_173 repos, last measured 2026-10-13. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (173)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 95,052 | 139,760 | 57.7 | 24% | 54% | 94% | 2,962 KB | 1,738 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 65,519 | 92,238 | 31.0 | 77% | 42% | 98% | 231 KB | 1 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 64,701 | 67,317 | 57.9 | 86% | 63% | 72% | 680 KB | 14 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A E B | 58,284 | 73,306 | 22.0 | 81% | 22% | 98% | 610 KB | 10 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | A F B | 50,970 | 292,534 | 72.6 | 25% | 55% | 89% | 563 KB | 2 |
| [tale-project/tale](https://github.com/tale-project/tale) | A D B | 50,856 | 95,694 | 31.7 | 64% | 27% | 80% | 2,584 KB | 34 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A C A | 49,188 | 62,170 | 78.0 | 76% | 50% | 87% | 158 KB | 14 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | A E C | 43,667 | 94,995 | 40.7 | 53% | 43% | 94% | 2,378 KB | 4 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 42,939 | 49,444 | 25.2 | 56% | 48% | 95% | 703 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 42,695 | 147,371 | 0.2 | 40% | 11% | 31% | 1,271 KB | 431 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 38,275 | 49,198 | 17.8 | 79% | 0% | 97% | 94 KB | 16 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 36,307 | 2,168,659 | 74.6 | 0% | 0% | 76% | 3,975 KB | 1 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | B E B | 32,115 | 45,749 | 0.0 | 52% | 18% | 86% | 608 KB | 1 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B C B | 31,402 | 37,600 | 143 | 74% | 79% | 100% | 3,166 KB | 1 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B D B | 30,533 | 36,213 | 72.5 | 60% | 27% | 98% | 601 KB | 0 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 27,229 | 26,615 | 0.0 | 89% | 68% | – | 225 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | B D D | 26,949 | 26,896 | 10.1 | 62% | 49% | – | 81 KB | 2 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B C C | 26,625 | 75,340 | 0.2 | 72% | 48% | 100% | 291 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B F B | 26,423 | 69,603 | 20.9 | 55% | 9% | 100% | 750 KB | 31 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B C B | 25,809 | 38,578 | 27.3 | 75% | 45% | 100% | 1,306 KB | 91 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 25,007 | 69,892 | 31.7 | 48% | 13% | 100% | 54 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | B E A | 25,007 | 40,836 | 11.5 | 56% | 6% | 93% | 236 KB | 5 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 24,013 | 32,549 | 31.8 | 72% | 18% | 95% | 599 KB | 22 |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B D B | 23,668 | 26,968 | 12.5 | 64% | 32% | 99% | 699 KB | 9 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | B E F | 23,046 | 236,977 | 0.0 | 61% | 27% | – | 8,190 KB | 0 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 22,922 | 44,200 | 88.6 | 36% | 42% | 46% | 314 KB | 3 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 22,632 | 48,349 | 39.2 | 90% | 48% | 100% | 353 KB | 2 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B E B | 22,476 | 37,584 | 15.5 | 57% | 66% | 91% | 429 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B C A | 22,385 | 40,512 | 0.2 | 72% | 28% | 99% | 163 KB | 9 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B E D | 22,351 | 47,392 | 0.0 | 59% | 74% | – | 1,191 KB | 3 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 22,059 | 34,528 | 23.4 | 83% | 50% | 86% | 364 KB | 9 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B D D | 20,599 | 52,239 | 21.5 | 62% | 54% | 34% | 3,082 KB | 96 |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | B E F | 20,583 | 376,986 | 7.0 | 54% | 5% | – | 331 KB | 4 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 20,307 | 56,126 | 44.3 | 70% | 38% | 99% | 146 KB | 1 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | B F A | 20,146 | 33,513 | 30.2 | 70% | 28% | 97% | 146 KB | 4 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E C | 19,002 | 88,862 | 19.7 | 59% | 43% | 64% | 304 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 18,992 | 20,503 | 32.0 | 26% | 0% | 100% | 404 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 18,933 | 44,464 | 24.5 | 39% | 44% | 100% | 448 KB | 18 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C F D | 18,657 | 37,324 | 0.0 | 70% | 0% | 43% | 240 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C C C | 17,806 | 48,002 | 28.7 | 77% | 0% | 98% | 102 KB | 114 (+1) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C D B | 17,556 | 26,228 | 49.0 | 64% | 72% | 99% | 571 KB | 2 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C D D | 17,523 | 31,225 | 0.0 | 69% | 31% | 42% | 265 KB | 0 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 17,518 | 642,105 | 0.0 | 86% | 0% | 0% | 3,283 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C B C | 17,081 | 42,226 | 0.0 | 82% | 15% | 50% | 455 KB | 1 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 16,386 | 17,040 | 39.1 | 0% | 68% | 100% | 66 KB | 60 (+1) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 16,191 | 20,271 | 56.0 | 80% | 66% | 98% | 4,310 KB | 15 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 15,975 | 32,828 | 0.0 | 53% | 15% | – | 776 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 15,685 | 27,217 | 21.2 | 57% | 47% | 98% | 114 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 15,620 | 28,827 | 12.7 | 73% | 39% | 78% | 126 KB | 5 (+1) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 15,616 | 31,130 | 57.0 | 59% | 66% | 100% | 768 KB | 6,272 (+13) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 14,806 | 22,788 | 33.9 | 80% | 39% | 78% | 1,340 KB | 3 |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C C B | 14,767 | 150,552 | 27.9 | 82% | 6% | 84% | 1,403 KB | 0 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C B C | 14,435 | 19,663 | 18.8 | 84% | 45% | 96% | 116 KB | 32 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 13,889 | 18,300 | 85.2 | 20% | 49% | 76% | 340 KB | 48 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 13,877 | 43,624 | 164 | 49% | 11% | 89% | 2,294 KB | 3 |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C D A | 13,637 | 38,395 | 0.0 | 65% | 12% | 94% | 211 KB | 0 |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C D A | 13,630 | 21,781 | 33.8 | 69% | 48% | 97% | 273 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 13,329 | 24,345 | 26.1 | 51% | 27% | 99% | 571 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C E B | 12,963 | 23,401 | 28.4 | 40% | 28% | 100% | 223 KB | 6 |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C E B | 12,796 | 40,711 | 24.2 | 40% | 16% | 97% | 377 KB | 9 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C F B | 12,515 | 115,645 | 17.8 | 32% | 4% | 100% | 1,414 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | C C D | 12,453 | 23,174 | 0.0 | 85% | 0% | 30% | 17 KB | 0 |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C E C | 12,279 | 19,629 | 7.0 | 59% | 19% | 95% | 107 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 12,186 | 13,341 | 19.1 | 81% | 17% | 93% | 529 KB | 1 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 12,185 | 15,563 | 4.5 | 0% | 0% | 99% | 380 KB | 127 (+1) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 11,995 | 100,838 | 20.0 | 31% | 15% | 97% | 112 KB | 3 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | C D B | 11,924 | 15,218 | 23.9 | 64% | 66% | 98% | 103 KB | 4 |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C E B | 11,781 | 24,846 | 28.4 | 56% | 13% | 100% | 6,926 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C D C | 11,721 | 19,107 | 0.0 | 68% | 18% | 86% | 816 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D A | 11,206 | 14,993 | 32.7 | 68% | 38% | 86% | 102 KB | 228 (-1) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 10,036 | 20,719 | 48.7 | 16% | 54% | 98% | 670 KB | 3 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D E B | 9,926 | 23,569 | 20.2 | 56% | 21% | 99% | 1,753 KB | 5 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D E B | 9,702 | 18,137 | 5.8 | 45% | 37% | 81% | 387 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D D D | 9,637 | 14,527 | 15.6 | 67% | 20% | – | 374 KB | 0 |
| [floor/teamcli](https://github.com/floor/teamcli) | D E B | 9,388 | 11,847 | 7.6 | 49% | 2% | 77% | 67 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | D E A | 9,340 | 9,536 | 12.5 | 54% | 0% | 98% | 149 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D F B | 9,317 | 24,424 | 13.0 | 61% | 0% | 90% | 759 KB | 4 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 9,308 | 12,984 | 24.5 | 53% | 22% | 92% | 700 KB | 4 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D D C | 9,218 | 15,082 | 10.0 | 62% | 46% | 92% | 112 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,175 | 13,059 | 7.9 | 46% | 14% | 100% | 489 KB | 11 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D E C | 8,914 | 13,944 | 15.3 | 59% | 24% | 100% | 615 KB | 8 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D E A | 8,568 | 14,026 | 9.5 | 50% | 7% | 99% | 110 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D F B | 8,264 | 24,077 | 19.2 | 78% | 33% | 100% | 1,029 KB | 6 |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 8,164 | 15,796 | 35.5 | 13% | 9% | 84% | 649 KB | 36 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | D F D | 8,150 | 15,783 | 11.1 | 74% | 0% | – | 115 KB | 0 |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F C | 7,658 | 9,670 | 18.5 | 51% | 24% | 67% | 359 KB | 6 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | D F C | 7,591 | 32,703 | 47.8 | 67% | 11% | 93% | 324 KB | 3 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | D E B | 7,480 | 13,360 | 24.0 | 47% | 40% | 98% | 964 KB | 93 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D E B | 6,825 | 31,416 | 0.0 | 56% | 41% | 99% | 398 KB | 1 |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D E C | 6,791 | 9,006 | 8.7 | 47% | 0% | 91% | 94 KB | 3 (+2) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 6,721 | 24,612 | 0.0 | 12% | 0% | – | 189 KB | 26 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,698 | 23,034 | 0.0 | 52% | 0% | 100% | 435 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 6,696 | 8,440 | 13.3 | 79% | 46% | 100% | 92 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D E D | 6,430 | 14,642 | 0.0 | 70% | 42% | 12% | 200 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 6,335 | 11,862 | 1.7 | 42% | 32% | 74% | 3,086 KB | 533 (+4) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D E D | 6,183 | 9,763 | 0.0 | 75% | 0% | – | 108 KB | 0 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | D E C | 6,133 | 29,180 | 1.1 | 52% | 0% | 68% | 290 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D E B | 6,064 | 15,302 | 17.2 | 53% | 0% | 83% | 385 KB | 19 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D E C | 6,016 | 10,865 | 23.2 | 43% | 0% | 97% | 514 KB | 17 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 5,884 | 14,213 | 9.9 | 53% | 0% | 97% | 236 KB | 2 |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D D B | 5,846 | 10,078 | 13.7 | 63% | 34% | 100% | 994 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D E C | 5,743 | 9,525 | 0.0 | 60% | 31% | 69% | 1,015 KB | 32 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D F C | 5,644 | 9,340 | 13.1 | 38% | 8% | 100% | 403 KB | 2 |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D F C | 5,467 | 18,030 | 0.0 | 45% | 40% | 100% | 219 KB | 1 |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 5,457 | 7,890 | 26.9 | 74% | 17% | – | 332 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D E B | 5,291 | 13,031 | 14.9 | 68% | 0% | 91% | 1,158 KB | 13 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | D F A | 5,271 | 6,879 | 21.2 | 63% | 0% | 100% | 73 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,258 | 10,628 | 28.1 | 58% | 11% | 88% | 1,492 KB | 69,941 |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 5,234 | 33,670 | 10.4 | 30% | 0% | 94% | 67 KB | 1 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 5,088 | 7,044 | 19.8 | 40% | 14% | 100% | 531 KB | 5 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F D | 4,754 | 66,297 | 8.2 | 49% | 18% | 2% | 411 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E D C | 4,383 | 16,099 | 0.0 | 60% | 25% | 56% | 140 KB | 107 (+1) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 4,288 | 6,465 | 28.6 | 35% | 0% | 52% | 92 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 4,166 | 11,173 | 8.6 | 28% | 10% | 96% | 757 KB | 2 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 3,919 | 6,828 | 29.7 | 63% | 0% | 100% | 129 KB | 20 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,783 | 8,281 | 9.2 | 57% | 9% | 98% | 329 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E C | 3,636 | 10,961 | 17.2 | 76% | 32% | 51% | 63 KB | 10 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E C C | 3,626 | 15,556 | 19.9 | 77% | 58% | 100% | 157 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,987 | 7,020 | 0.0 | 2% | 0% | 33% | 397 KB | 455 |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 2,735 | 7,934 | 49.6 | 71% | 8% | 90% | 170 KB | 8 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 2,700 | 7,339 | 0.1 | 26% | 15% | 0% | 427 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F D | 2,689 | 56,465 | 0.7 | 36% | 21% | 46% | 5,230 KB | 1 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,639 | 4,134 | 42.2 | 58% | 40% | 98% | 282 KB | 2 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E E B | 2,511 | 14,149 | 18.1 | 43% | 0% | 100% | 120 KB | 0 |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E E C | 2,503 | 13,822 | 19.8 | 71% | 0% | 89% | 302 KB | 22 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,318 | 5,675 | 26.0 | 47% | 0% | 47% | 94 KB | 0 |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,244 | 9,207 | 28.3 | 36% | 15% | 100% | 617 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | E F D | 2,159 | 8,856 | 23.2 | 77% | 0% | 0% | 153 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 2,100 | 9,255 | 24.2 | 27% | 24% | 98% | 123 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 2,075 | 9,619 | 24.4 | 0% | 0% | 100% | 489 KB | 27 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,942 | 6,571 | 11.6 | 24% | 21% | 96% | 216 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,857 | 4,059 | 13.7 | 78% | 0% | 92% | 260 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | E F D | 1,817 | 5,780 | 0.0 | 74% | 11% | – | 202 KB | 4 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E E A | 1,779 | 4,058 | 29.8 | 72% | 0% | 97% | 117 KB | 1 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 1,692 | 5,013 | 0.1 | 52% | 0% | 86% | 237 KB | 3 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 1,651 | 4,461 | 12.5 | 37% | 12% | – | 55 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | E E D | 1,648 | 3,455 | 0.0 | 80% | 0% | – | 80 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | E F C | 1,600 | 11,484 | 6.9 | 44% | 0% | 98% | 42 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,573 | 2,390 | 0.2 | 66% | 6% | 13% | 613 KB | 3 |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,485 | 1,457 | 15.9 | 53% | 0% | 100% | 154 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 1,448 | 15,247 | 17.4 | 51% | 15% | 99% | 593 KB | 11 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,441 | 2,948 | 2.4 | 25% | 22% | 99% | 7,014 KB | 18 |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 1,330 | 7,888 | 5.6 | 10% | 13% | 81% | 466 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,254 | 5,259 | 24.9 | 22% | 31% | 98% | 508 KB | 0 |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 1,241 | 10,034 | 16.0 | 62% | 0% | – | 408 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,149 | 10,838 | 13.4 | 55% | 32% | 100% | 953 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 421 | 1,384 | 0.0 | 26% | 7% | – | 18 KB | 0 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 341 | 658 | 7.6 | 0% | 0% | 76% | 72 KB | 4 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 316 | 44,400 | 12.5 | 69% | 40% | 99% | 66 KB | 3 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 308 | 4,820 | 0.0 | 31% | 0% | – | 15 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F C | 307 | 8,584 | 6.9 | 45% | 20% | 99% | 43 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 189 | 4,348 | 0.0 | 18% | 0% | 0% | 473 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 167 | 1,463 | 0.0 | 40% | 0% | – | 59 KB | 1 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 73 | 1,664 | 3.4 | 67% | 0% | 100% | 59 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 38 | 1,507 | 10.7 | 55% | 0% | 100% | 173 KB | 216 (+1) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 400,557 | 36.8 | 30% | 0% | 100% | 703 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 2,253 | 35.8 | 30% | 0% | 100% | 847 KB | 3 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F D B | – | – | 29.7 | 62% | 49% | 87% | 1,997 KB | 1,370 (+6) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F E B | – | – | 23.5 | 58% | 7% | 100% | 1,042 KB | 0 |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 19.8 | 49% | 21% | 93% | 892 KB | 4 |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F E B | – | – | 15.5 | 61% | 0% | 98% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 1,725 | 13.6 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 884 | 6.8 | 0% | 0% | 95% | 150 KB | 346 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 3.4 | 64% | 82% | 0% | 1,061 KB | 457 (+2) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F E D | 0 | 0 | 1.4 | 76% | 29% | – | 5,619 KB | 0 |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 72% | 91% | 87% | 812 KB | 4 |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 7,723 | 0.2 | 49% | 0% | 86% | 1,449 KB | 1,094 (+1) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 1,465 | 0.2 | 18% | 0% | 6% | 904 KB | 1,270 (+5) |
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
