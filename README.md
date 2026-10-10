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

A repo that passes is on the list for good. It's measured every day from then on, even through a slow week, and its
grades will say so if it slows down. A model reads each new one to decide what it is: a factory building itself, a
project being built by one, or not software at all (docs, data, proofs). Only the first two are listed.

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
_519 repos, last measured 2026-10-10. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (47)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F C | 105,316 | 132,586 | 51.0 | 13% | 28% | 64% | 2,537 KB | 1,734 |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A E B | 69,369 | 129,090 | 31.0 | 78% | 22% | 98% | 220 KB | 0 |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A D D | 62,554 | 155,963 | 0.2 | 62% | 12% | 27% | 1,271 KB | 430 |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A D C | 55,726 | 56,194 | 56.2 | 69% | 15% | 96% | 235 KB | 13 |
| [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) | A D C | 46,353 | 84,349 | 34.5 | 68% | 36% | 69% | 3,823 KB | 1,204 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 24,631 | 34,828 | 140 | 64% | 49% | 100% | 3,000 KB | 0 |
| [wangbinquan/agent-workflow](https://github.com/wangbinquan/agent-workflow) | B B D | 24,416 | 87,427 | 0.0 | 87% | 74% | 47% | 613 KB | 57 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | B F B | 23,679 | 30,669 | 14.5 | 17% | 51% | 99% | 239 KB | 74,199 |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 22,518 | 23,472 | 0.0 | 71% | 45% | – | 225 KB | 0 |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 21,783 | 23,643 | 88.1 | 26% | 51% | 76% | 340 KB | 45 |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | B E B | 20,463 | 30,341 | 28.1 | 46% | 35% | 79% | 1,966 KB | 1,354 |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 17,930 | 38,226 | 23.8 | 26% | 6% | 97% | 236 KB | 17 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 17,481 | 52,564 | 170 | 41% | 8% | 89% | 2,294 KB | 3 |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | C D A | 17,391 | 44,870 | 15.8 | 68% | 0% | 90% | 94 KB | 15 |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | C F B | 17,305 | 33,861 | 25.7 | 29% | 21% | 92% | 1,228 KB | 88 |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [joshualeestone/kosmos](https://github.com/joshualeestone/kosmos) | C E B | 16,925 | 24,015 | 52.7 | 58% | 18% | 98% | 1,433 KB | 1 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | C F C | 16,915 | 39,874 | 89.1 | 31% | 15% | 50% | 314 KB | 3 |
| [Maurdekye/orgtree](https://github.com/Maurdekye/orgtree) | C D D | 16,892 | 32,042 | 0.0 | 66% | 7% | 0% | 2,025 KB | 112 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 16,705 | 32,625 | 56.3 | 60% | 58% | 97% | 768 KB | 6,222 |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C E A | 16,691 | 27,961 | 32.9 | 58% | 21% | 93% | 138 KB | 4 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 16,308 | 17,462 | 4.9 | 0% | 0% | 96% | 355 KB | 126 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 15,003 | 16,557 | 36.0 | 0% | 5% | 92% | 66 KB | 56 |
| [agentmuxai/agentmux](https://github.com/agentmuxai/agentmux) | C E C | 13,826 | 26,334 | 43.5 | 54% | 38% | 97% | 316 KB | 19 |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C E A | 13,728 | 42,367 | 21.8 | 80% | 0% | 90% | 100 KB | 103 |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 13,658 | 27,953 | 12.3 | 86% | 41% | 80% | 77 KB | 3 |
| [melodic-software/claude-code-plugins](https://github.com/melodic-software/claude-code-plugins) | C F C | 13,600 | 65,004 | 49.5 | 28% | 0% | 98% | 239 KB | 23 |
| [marcioapm/dude](https://github.com/marcioapm/dude) | C F B | 11,245 | 14,780 | 2.8 | 3% | 0% | 83% | 108 KB | 1 |
| [coder/xum](https://github.com/coder/xum) | C E B | 10,589 | 18,669 | 34.4 | 42% | 15% | 99% | 940 KB | 2,051 |
| [github/gh-aw](https://github.com/github/gh-aw) | C E C | 10,523 | 42,989 | 27.6 | 50% | 48% | 62% | 229 KB | 5,369 |
| [prime-radiant-inc/evener](https://github.com/prime-radiant-inc/evener) | C F A | 10,364 | 19,821 | 69.0 | 43% | 12% | 98% | 306 KB | 171 |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 7,164 | 10,597 | 24.2 | 9% | 0% | 97% | 489 KB | 27 |
| [scode/farhelm](https://github.com/scode/farhelm) | D F B | 6,444 | 20,849 | 40.0 | 4% | 0% | 97% | 1,486 KB | 0 |
| [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) | D F A | 5,840 | 14,739 | 7.5 | 52% | 5% | 99% | 201 KB | 2,254 |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 5,580 | 16,683 | 0.0 | 3% | 0% | – | 183 KB | 25 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E C | 5,470 | 12,891 | 35.8 | 57% | 0% | 68% | 182 KB | 2 |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | D F D | 5,197 | 7,112 | 0.0 | 2% | 0% | 33% | 397 KB | 454 |
| [bastani-inc/atomic](https://github.com/bastani-inc/atomic) | E F B | 3,627 | 6,627 | 13.9 | 4% | 16% | 95% | 534 KB | 854 |
| [cristicretu/diri](https://github.com/cristicretu/diri) | E F D | 3,601 | 17,907 | 14.8 | 4% | 0% | 50% | 547 KB | 430 |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 3,572 | 25,209 | 0.2 | 70% | 0% | 86% | 572 KB | 1,090 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | E F B | 3,545 | 5,195 | 12.9 | 49% | 15% | 79% | 1,213 KB | 20,269 |
| [receptron/mulmoterminal](https://github.com/receptron/mulmoterminal) | E F A | 2,106 | 4,036 | 20.2 | 27% | 0% | 98% | 113 KB | 237 |
| [razzant/claudexor](https://github.com/razzant/claudexor) | E F B | 2,050 | 7,415 | 2.3 | 0% | 0% | 89% | 298 KB | 497 |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 435 | 2,166 | 0.2 | 38% | 0% | 3% | 904 KB | 1,261 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 305 | 3,471 | 7.9 | 0% | 0% | 81% | 71 KB | 4 |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 58 | 725 | 12.2 | 19% | 0% | 98% | 174 KB | 212 |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 2,093 | 6.7 | 0% | 0% | 96% | 150 KB | 346 |

### Built by an assembly line (75)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [OneUptime/oneuptime](https://github.com/OneUptime/oneuptime) | A E B | 213,539 | 337,794 | 28.1 | 58% | 44% | 92% | 668 KB | 7,717 |
| [stella/stella](https://github.com/stella/stella) | A B A | 95,509 | 129,095 | 74.7 | 82% | 84% | 100% | 473 KB | 258 |
| [kaeawc/auto-mobile](https://github.com/kaeawc/auto-mobile) | A E D | 72,685 | 100,142 | 93.9 | 48% | 47% | 9% | 342 KB | 51 |
| [artificial-hedge/dipcatcher](https://github.com/artificial-hedge/dipcatcher) | A C D | 67,627 | 1,284,334 | 102 | 82% | 8% | 33% | 469 KB | 0 |
| [lamontaes/Political-Game-Git](https://github.com/lamontaes/Political-Game-Git) | A F D | 65,753 | 310,615 | 97.5 | 41% | 1% | 27% | 10,357 KB | 0 |
| [OreStudio/OreStudio](https://github.com/OreStudio/OreStudio) | A F C | 64,285 | 155,509 | 33.5 | 23% | 52% | 75% | 9,839 KB | 28 |
| [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | A E B | 58,241 | 72,826 | 67.8 | 53% | 0% | 100% | 971 KB | 7,111 |
| [workingdir/ornadb](https://github.com/workingdir/ornadb) | A F D | 56,205 | 75,505 | 128 | 61% | 1% | 8% | 1,862 KB | 5 |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 55,106 | 1,424,223 | 73.3 | 8% | 14% | 67% | 3,975 KB | 1 |
| [ubugeeei-prod/vize](https://github.com/ubugeeei-prod/vize) | A D A | 51,232 | 144,674 | 54.4 | 69% | 20% | 94% | 300 KB | 902 |
| [metasequoiaime/msime](https://github.com/metasequoiaime/msime) | A B B | 50,506 | 72,974 | 214 | 88% | 14% | 100% | 488 KB | 593 |
| [skmtmst/line-harness-oss](https://github.com/skmtmst/line-harness-oss) | A F B | 46,287 | 112,840 | 41.5 | 37% | 29% | 100% | 4,345 KB | 0 |
| [kirklandsig/halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | A D E | 46,080 | 87,344 | 9.2 | 67% | 10% | 100% | 371 KB | 45 |
| [UnknownAlienHuman/eliot-memory-os](https://github.com/UnknownAlienHuman/eliot-memory-os) | A F D | 45,874 | 82,609 | 125 | 54% | 0% | 0% | 1,898 KB | 0 |
| [evgunter/cad](https://github.com/evgunter/cad) | A B B | 43,573 | 88,994 | 75.2 | 89% | 40% | 100% | 703 KB | 0 |
| [everruns/everruns](https://github.com/everruns/everruns) | A F C | 42,671 | 69,170 | 32.1 | 33% | 55% | 93% | 157 KB | 54 |
| [EffortlessMetrics/ripr-swarm](https://github.com/EffortlessMetrics/ripr-swarm) | A C D | 41,909 | 98,923 | 39.6 | 78% | 38% | 95% | 1,975 KB | 0 |
| [Smarter-Poker/Smarter-Poker-Club-Arena](https://github.com/Smarter-Poker/Smarter-Poker-Club-Arena) | B E B | 37,518 | 303,917 | 73.3 | 58% | 56% | 100% | 2,646 KB | 0 |
| [Oteryn/Oteryn-Game](https://github.com/Oteryn/Oteryn-Game) | B E C | 33,233 | 2,133,161 | 38.8 | 70% | 0% | 100% | 485 KB | 0 |
| [moxnixmdj/verification-capsule-runner](https://github.com/moxnixmdj/verification-capsule-runner) | B F D | 32,427 | 145,131 | 39.3 | 44% | 2% | 13% | 305 KB | 0 |
| [6ZoSo9/void-node](https://github.com/6ZoSo9/void-node) | B F E | 30,655 | 36,549 | 33.1 | 32% | 43% | 97% | 3,761 KB | 0 |
| [objectstack-ai/objectstack](https://github.com/objectstack-ai/objectstack) | B C B | 29,919 | 45,478 | 87.8 | 80% | 39% | 100% | 2,308 KB | 70 |
| [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite) | B C B | 28,283 | 39,695 | 61.1 | 70% | 48% | 92% | 1,902 KB | 416 |
| [buster14a/buster](https://github.com/buster14a/buster) | B F B | 25,194 | 76,080 | 50.4 | 16% | 28% | 99% | 3,137 KB | 0 |
| [lazyxu/xdrive](https://github.com/lazyxu/xdrive) | B F B | 23,893 | 30,887 | 41.1 | 3% | 13% | 94% | 272 KB | 0 |
| [Hanz0Hatt0r1/nfs-shift-decompilation](https://github.com/Hanz0Hatt0r1/nfs-shift-decompilation) | B E B | 23,551 | 46,578 | 55.6 | 56% | 19% | 100% | 227 KB | 1 |
| [tokuhirom/mutsu](https://github.com/tokuhirom/mutsu) | B E E | 22,140 | 52,848 | 103 | 47% | 8% | 100% | 1,579 KB | 27 |
| [hashgraph-online/hol-guard](https://github.com/hashgraph-online/hol-guard) | B E B | 21,993 | 91,982 | 26.3 | 43% | 52% | 94% | 1,491 KB | 836 |
| [JovieInc/Jovie](https://github.com/JovieInc/Jovie) | B E A | 21,630 | 69,054 | 102 | 50% | 6% | 91% | 313 KB | 1 |
| [Raynos/project-wildshard-singleplayer](https://github.com/Raynos/project-wildshard-singleplayer) | B F C | 21,468 | 631,834 | 0.0 | 82% | 0% | 59% | 92 KB | 0 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | B F D | 21,183 | 31,200 | 27.4 | 22% | 8% | 0% | 546 KB | 41,747 |
| [AlexanderMattTurner/agent-glovebox](https://github.com/AlexanderMattTurner/agent-glovebox) | B F A | 20,609 | 45,826 | 51.7 | 36% | 21% | 95% | 161 KB | 67 |
| [kuu-lab/swifty-kotlin](https://github.com/kuu-lab/swifty-kotlin) | C F B | 19,339 | 28,055 | 55.8 | 20% | 8% | 100% | 340 KB | 2 |
| [tioperfumes07/IH35-TMS](https://github.com/tioperfumes07/IH35-TMS) | C D C | 19,044 | 34,645 | 155 | 62% | 19% | 78% | 399 KB | 0 |
| [FueledByChai/fueledbychai-rs](https://github.com/FueledByChai/fueledbychai-rs) | C E D | 17,540 | 24,228 | 5.2 | 50% | 0% | – | 101 KB | 1 |
| [carrick-sh/carrick](https://github.com/carrick-sh/carrick) | C F C | 17,334 | 52,384 | 1.9 | 17% | 2% | 80% | 558 KB | 2 |
| [uttrflow/uttrflow-swift](https://github.com/uttrflow/uttrflow-swift) | C E A | 17,020 | 38,552 | 111 | 59% | 23% | 100% | 208 KB | 6 |
| [edsaperia/witch](https://github.com/edsaperia/witch) | C E C | 16,669 | 26,454 | 20.9 | 60% | 0% | 98% | 128 KB | 0 |
| [HectorBailey/byte-tactics](https://github.com/HectorBailey/byte-tactics) | C C E | 16,264 | 52,163 | 115 | 74% | 7% | 100% | 505 KB | 29 |
| [joefrancisGA/ArchLucid](https://github.com/joefrancisGA/ArchLucid) | C D D | 16,124 | 21,235 | 53.3 | 68% | 1% | 32% | 5,075 KB | 0 |
| [pch/rawmakase](https://github.com/pch/rawmakase) | C E E | 15,071 | 22,647 | 11.1 | 42% | 53% | 96% | 220 KB | 723 |
| [web-everything/web-everything](https://github.com/web-everything/web-everything) | C E B | 14,722 | 29,208 | 90.8 | 48% | 37% | 99% | 519 KB | 0 |
| [rubys/roundhouse](https://github.com/rubys/roundhouse) | C E B | 14,480 | 30,156 | 15.7 | 44% | 42% | 97% | 431 KB | 429 |
| [max-sixty/leaf](https://github.com/max-sixty/leaf) | C E B | 13,544 | 28,350 | 52.5 | 43% | 62% | 73% | 108 KB | 5 |
| [Open-MBEE/OpenSysML](https://github.com/Open-MBEE/OpenSysML) | C E B | 12,719 | 55,319 | 26.9 | 41% | 40% | 100% | 208 KB | 37 |
| [melian-agent/melian](https://github.com/melian-agent/melian) | C F C | 12,468 | 20,719 | 3.3 | 8% | 0% | 100% | 98 KB | 0 |
| [evilsysadmin/chess-studio](https://github.com/evilsysadmin/chess-studio) | C F B | 12,297 | 55,376 | 132 | 2% | 41% | 96% | 256 KB | 1 |
| [openclaw/openclaw-enterprise](https://github.com/openclaw/openclaw-enterprise) | C C C | 12,249 | 19,275 | 52.8 | 71% | 24% | 90% | 510 KB | 376 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | C B C | 11,960 | 17,065 | 36.6 | 82% | 17% | 97% | 1,568 KB | 59,744 |
| [JakeChampion/lang](https://github.com/JakeChampion/lang) | C C C | 11,520 | 69,323 | 61.5 | 74% | 42% | 94% | 987 KB | 1 |
| [agentydragon/ducktape](https://github.com/agentydragon/ducktape) | D E B | 8,654 | 20,846 | 104 | 50% | 30% | 98% | 163 KB | 10 |
| [vznjs/vx](https://github.com/vznjs/vx) | D F C | 7,796 | 15,246 | 107 | 58% | 0% | 96% | 129 KB | 6 |
| [storytree-ai/storytree](https://github.com/storytree-ai/storytree) | D A B | 7,550 | 37,557 | 35.9 | 90% | 34% | 85% | 61 KB | 0 |
| [kentcdodds/kody](https://github.com/kentcdodds/kody) | D E A | 7,180 | 11,113 | 19.9 | 54% | 33% | 99% | 125 KB | 752 |
| [Dicklesworthstone/franken_engine](https://github.com/Dicklesworthstone/franken_engine) | D F D | 6,582 | 11,705 | 0.0 | 22% | 0% | 20% | 6,964 KB | 31 |
| [Nishfleet/0509](https://github.com/Nishfleet/0509) | E F A | 4,868 | 10,398 | 67.9 | 63% | 21% | 99% | 79 KB | 0 |
| [justinlindh/human-in-the-loop](https://github.com/justinlindh/human-in-the-loop) | E F B | 4,723 | 6,055 | 50.3 | 56% | 0% | 99% | 138 KB | 2 |
| [mboogerd/computenet](https://github.com/mboogerd/computenet) | E E B | 4,605 | 12,422 | 19.5 | 50% | 15% | 80% | 178 KB | 0 |
| [ravelius/Matkakirja](https://github.com/ravelius/Matkakirja) | E E D | 4,310 | 41,585 | 60.1 | 53% | 49% | 100% | 8,133 KB | 0 |
| [ScriptedAlchemy/tracedecay](https://github.com/ScriptedAlchemy/tracedecay) | E E C | 4,264 | 24,489 | 51.1 | 44% | 22% | 68% | 1,976 KB | 80 |
| [Dicklesworthstone/annus-mirabilis.com](https://github.com/Dicklesworthstone/annus-mirabilis.com) | E F D | 4,038 | 10,491 | 0.0 | 57% | 0% | 0% | 1,235 KB | 6 |
| [postmark-town/postmark](https://github.com/postmark-town/postmark) | E F C | 3,640 | 158,602 | 24.5 | 34% | 28% | 100% | 161 KB | 19 |
| [WangPantopus/skinny-pantopus](https://github.com/WangPantopus/skinny-pantopus) | E E C | 2,830 | 7,100 | 72.6 | 58% | 1% | 81% | 598 KB | 0 |
| [CambrianTech/continuum](https://github.com/CambrianTech/continuum) | E F C | 2,633 | 3,474 | 30.7 | 60% | 0% | 99% | 621 KB | 32 |
| [keeptxred/TexasDefined](https://github.com/keeptxred/TexasDefined) | E F E | 2,425 | 3,408 | 49.8 | 28% | 41% | 97% | 288 KB | 1 |
| [gunb-ai/gunbc](https://github.com/gunb-ai/gunbc) | E B E | 2,392 | 55,850 | 65.4 | 88% | 32% | 80% | 1,989 KB | 4 |
| [chidionyema/idp](https://github.com/chidionyema/idp) | E F B | 1,843 | 18,618 | 81.6 | 21% | 0% | 97% | 2,933 KB | 1 |
| [orbi-build/orbi-website](https://github.com/orbi-build/orbi-website) | E F B | 1,175 | 2,542 | 17.4 | 3% | 0% | 95% | 79 KB | 0 |
| [Fronthub-pl/arrowz](https://github.com/Fronthub-pl/arrowz) | E F B | 1,041 | 5,003 | 5.3 | 0% | 11% | 100% | 122 KB | 0 |
| [day8/re-frame2](https://github.com/day8/re-frame2) | F C C | 473 | 6,588 | 45.8 | 73% | 1% | 100% | 390 KB | 51 |
| [garden-co/jazz](https://github.com/garden-co/jazz) | F F B | 219 | 1,084 | 19.8 | 0% | 0% | 92% | 659 KB | 204 |
| [makr-code/ThemisDB](https://github.com/makr-code/ThemisDB) | F F E | 212 | 226,441 | 12.4 | 0% | 16% | 80% | 54 KB | 9 |
| [mas-bandwidth/nova-tools](https://github.com/mas-bandwidth/nova-tools) | F F B | 0 | 0 | 73.0 | 0% | 0% | 76% | 232 KB | 6 |
| [wieslawsoltes/SharpForge](https://github.com/wieslawsoltes/SharpForge) | F F C | 0 | 672,791 | 26.0 | 35% | 0% | 100% | 120 KB | 20 |
| [kierandrewett/gnoblin](https://github.com/kierandrewett/gnoblin) | F F C | 0 | 5,228 | 1.9 | 25% | 0% | 83% | 645 KB | 5 |

### Awaiting classification (397)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [boxabirds/awesome-local-ai](https://github.com/boxabirds/awesome-local-ai) | A D D | 125,464 | 421,336 | 0.0 | 61% | 57% | 41% | 699 KB | 52 |
| [BigRain-11122/BigMoney](https://github.com/BigRain-11122/BigMoney) | A C F | 86,093 | 1,193,879 | 0.0 | 78% | 70% | – | 2,920 KB | 1 |
| [armanisadeghi/ai-matrx](https://github.com/armanisadeghi/ai-matrx) | A D D | 67,749 | 234,567 | 1.2 | 65% | 42% | 0% | 4,489 KB | 3 |
| [detain/sugarcraft](https://github.com/detain/sugarcraft) | A E C | 67,088 | 80,245 | 2.5 | 57% | 21% | 56% | 962 KB | 4 |
| [clintongormley/waitron](https://github.com/clintongormley/waitron) | A C A | 61,080 | 171,691 | 40.7 | 70% | 59% | 99% | 372 KB | 1 |
| [bei612/kailo-plus](https://github.com/bei612/kailo-plus) | A D D | 56,739 | 3,793,228 | 0.0 | 61% | 19% | 0% | 17,984 KB | 0 |
| [aakshintala/fiber](https://github.com/aakshintala/fiber) | A E B | 55,423 | 63,839 | 24.1 | 53% | 16% | 73% | 282 KB | 0 |
| [aavidad/VEC_Diputacion_app](https://github.com/aavidad/VEC_Diputacion_app) | A E B | 54,563 | 65,905 | 30.0 | 46% | 36% | 95% | 620 KB | 0 |
| [Ascending-AI/lash](https://github.com/Ascending-AI/lash) | A C C | 54,182 | 158,863 | 40.2 | 72% | 28% | 68% | 988 KB | 8 |
| [dbn1972/civitasone-suite](https://github.com/dbn1972/civitasone-suite) | A E D | 50,223 | 67,592 | 25.9 | 51% | 0% | 48% | 878 KB | 0 |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A C A | 49,711 | 56,403 | 67.1 | 74% | 0% | 100% | 135 KB | 14 |
| [CathedralOS/Omega](https://github.com/CathedralOS/Omega) | A D D | 49,359 | 107,361 | 0.1 | 67% | 33% | – | 111 KB | 0 |
| [Cloudgeni-ai/opengeni](https://github.com/Cloudgeni-ai/opengeni) | A E D | 48,348 | 75,711 | 48.6 | 59% | 22% | 37% | 3,273 KB | 198 |
| [dancxjo/conduit](https://github.com/dancxjo/conduit) | A C C | 48,326 | 59,824 | 50.3 | 76% | 29% | 77% | 166 KB | 1 |
| [dork-labs/dorkos](https://github.com/dork-labs/dorkos) | A C A | 45,180 | 83,217 | 31.7 | 75% | 25% | 100% | 334 KB | 10 |
| [adrienm7/ergopti](https://github.com/adrienm7/ergopti) | A C C | 42,684 | 123,411 | 0.0 | 70% | 29% | 59% | 287 KB | 14 |
| [adams-shaun/gorge](https://github.com/adams-shaun/gorge) | A C D | 40,764 | 86,340 | 0.0 | 88% | 2% | 0% | 157 KB | 3 |
| [BiomaAI/veoveo](https://github.com/BiomaAI/veoveo) | B C C | 39,426 | 70,621 | 0.0 | 73% | 7% | 72% | 1,783 KB | 3 |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B E C | 38,880 | 57,584 | 34.0 | 56% | 72% | 84% | 2,296 KB | 4 |
| [csitea/csi-spl](https://github.com/csitea/csi-spl) | B B B | 38,247 | 56,053 | 0.0 | 84% | 48% | 96% | 150 KB | 1 |
| [believeinoakland/bio](https://github.com/believeinoakland/bio) | B F C | 37,773 | 179,193 | 0.4 | 46% | 4% | 100% | 14,182 KB | 0 |
| [Agent-StrongHold/Project-mAIstro](https://github.com/Agent-StrongHold/Project-mAIstro) | B C B | 37,526 | 45,884 | 21.2 | 72% | 17% | 100% | 1,548 KB | 0 |
| [carbonphysicsai/Carbon](https://github.com/carbonphysicsai/Carbon) | B E B | 35,197 | 119,139 | 23.8 | 41% | 58% | 100% | 1,159 KB | 2 |
| [defnotean/wildercord](https://github.com/defnotean/wildercord) | B C D | 32,597 | 43,228 | 0.0 | 76% | 19% | 48% | 243 KB | 0 |
| [AquilaXk/easyconvert](https://github.com/AquilaXk/easyconvert) | B E A | 31,368 | 42,031 | 9.9 | 74% | 0% | 96% | 357 KB | 1 |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B E B | 30,102 | 46,281 | 18.2 | 61% | 7% | 90% | 707 KB | 0 |
| [aislopware/slopty](https://github.com/aislopware/slopty) | B E D | 30,045 | 44,070 | 0.0 | 84% | 0% | 38% | 415 KB | 0 |
| [davidarcher/rimgovernor](https://github.com/davidarcher/rimgovernor) | B E D | 29,614 | 464,893 | 0.0 | 51% | 24% | 12% | 112 KB | 0 |
| [biginkc/sandra](https://github.com/biginkc/sandra) | B E B | 28,532 | 43,076 | 11.0 | 42% | 22% | 94% | 862 KB | 0 |
| [bilo-io/midnite-studio](https://github.com/bilo-io/midnite-studio) | B E B | 28,313 | 27,947 | 15.7 | 58% | 0% | 79% | 300 KB | 0 |
| [dongdongbh/Mindwtr](https://github.com/dongdongbh/Mindwtr) | B E C | 25,593 | 37,888 | 0.3 | 56% | 45% | 53% | 1,592 KB | 2,232 |
| [CausalityHQ/borsuk](https://github.com/CausalityHQ/borsuk) | B E D | 25,150 | 292,863 | 0.0 | 85% | 10% | 0% | 2,055 KB | 3 |
| [adriancova/polymarket-bot-v2](https://github.com/adriancova/polymarket-bot-v2) | B E A | 24,941 | 28,093 | 3.1 | 69% | 0% | 93% | 281 KB | 0 |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 24,013 | 32,549 | 31.8 | 72% | 18% | 95% | 599 KB | 22 |
| [Allternit/allternit-platform](https://github.com/Allternit/allternit-platform) | B E D | 23,091 | 32,800 | 40.6 | 71% | 24% | 96% | 1,108 KB | 1 |
| [CarstVaartjes/vonk-forge](https://github.com/CarstVaartjes/vonk-forge) | B E D | 23,068 | 108,680 | 19.7 | 47% | 4% | 48% | 154 KB | 5 |
| [dbowm91/i2pr](https://github.com/dbowm91/i2pr) | B F D | 23,010 | 36,902 | 0.4 | 37% | 32% | 36% | 444 KB | 1 |
| [boomytc/AmazMe](https://github.com/boomytc/AmazMe) | B E D | 22,748 | 82,568 | 2.7 | 52% | 40% | – | 265 KB | 0 |
| [aosama/astronomical](https://github.com/aosama/astronomical) | B E B | 22,694 | 27,203 | 12.3 | 64% | 0% | 100% | 32 KB | 22 |
| [colophon-group/jobseek](https://github.com/colophon-group/jobseek) | B D A | 22,207 | 51,345 | 18.5 | 68% | 0% | 100% | 264 KB | 203 |
| [benhook1013/FireMUD](https://github.com/benhook1013/FireMUD) | B B C | 22,199 | 27,587 | 10.6 | 89% | 26% | 98% | 374 KB | 11 |
| [CSE-Sudo/on-care](https://github.com/CSE-Sudo/on-care) | B F B | 21,830 | 25,756 | 24.4 | 25% | 6% | 100% | 325 KB | 0 |
| [afterburn25/Coding_Agent](https://github.com/afterburn25/Coding_Agent) | B C D | 21,498 | 41,921 | 0.2 | 74% | 46% | 0% | 676 KB | 0 |
| [Ameyanagi/ReShiki](https://github.com/Ameyanagi/ReShiki) | B F C | 21,374 | 32,051 | 6.6 | 28% | 0% | 100% | 113 KB | 99 |
| [Aspis0/devboule-v2](https://github.com/Aspis0/devboule-v2) | B D B | 21,307 | 25,230 | 0.0 | 70% | 0% | 86% | 248 KB | 0 |
| [digitopvn/clarkcant](https://github.com/digitopvn/clarkcant) | B D A | 21,047 | 28,727 | 16.0 | 64% | 22% | 100% | 270 KB | 2 |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | B C C | 20,760 | 23,181 | 26.9 | 77% | 15% | 100% | 1,670 KB | 5,128 |
| [brandongit2/scenic-roads](https://github.com/brandongit2/scenic-roads) | C E F | 19,961 | 23,516 | 0.0 | 59% | 0% | – | 418 KB | 0 |
| [asckye/TIA_Portal_Openness_MCP](https://github.com/asckye/TIA_Portal_Openness_MCP) | C D C | 19,839 | 152,859 | 0.0 | 66% | 12% | 67% | 260 KB | 2 |
| [1CatAI/1Cat-vLLM](https://github.com/1CatAI/1Cat-vLLM) | C D C | 19,300 | 47,124 | 10.5 | 69% | 15% | 96% | 7,146 KB | 1,268 |
| [appandflow/stim](https://github.com/appandflow/stim) | C E B | 18,956 | 23,098 | 41.4 | 58% | 20% | 100% | 520 KB | 80 |
| [abarva-platform/abarva](https://github.com/abarva-platform/abarva) | C E C | 18,644 | 36,614 | 58.9 | 52% | 33% | 100% | 5,548 KB | 0 |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E D | 18,517 | 28,059 | 15.2 | 66% | 45% | 22% | 304 KB | 0 |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C E B | 18,287 | 26,094 | 49.1 | 43% | 17% | 100% | 653 KB | 3 |
| [asadarafat/streamskope](https://github.com/asadarafat/streamskope) | C F C | 18,004 | 21,448 | 4.3 | 38% | 44% | 100% | 68 KB | 0 |
| [capyatelier/capycanvas](https://github.com/capyatelier/capycanvas) | C E C | 17,712 | 42,465 | 0.2 | 58% | 0% | 91% | 803 KB | 35 |
| [cortexkit/magic-context](https://github.com/cortexkit/magic-context) | C E C | 17,524 | 47,273 | 0.6 | 57% | 50% | 82% | 1,819 KB | 2,300 |
| [BabychPV/ECR](https://github.com/BabychPV/ECR) | C C B | 17,384 | 30,271 | 12.6 | 77% | 8% | 100% | 2,093 KB | 0 |
| [daniel-ospina/tortoise](https://github.com/daniel-ospina/tortoise) | C B B | 17,334 | 23,776 | 33.8 | 83% | 41% | 91% | 1,719 KB | 6 |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | C E A | 17,281 | 23,281 | 6.8 | 56% | 14% | 99% | 110 KB | 0 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C C B | 17,079 | 29,343 | 52.2 | 80% | 73% | 98% | 574 KB | 2 |
| [DocMorphic/cmux-app](https://github.com/DocMorphic/cmux-app) | C C D | 17,023 | 30,530 | 0.0 | 78% | 4% | 67% | 2,260 KB | 0 |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | C C A | 16,950 | 20,217 | 13.3 | 76% | 24% | 98% | 149 KB | 0 |
| [BrannMolvik/premier-league-manager-2001-research](https://github.com/BrannMolvik/premier-league-manager-2001-research) | C C C | 16,470 | 23,694 | 16.5 | 70% | 36% | 65% | 213 KB | 0 |
| [Artistlvelup/Artist-level-up](https://github.com/Artistlvelup/Artist-level-up) | C E E | 16,183 | 34,813 | 0.0 | 55% | 34% | 99% | 914 KB | 0 |
| [Cyb3rb1ade/PLUR1BUS-Harness](https://github.com/Cyb3rb1ade/PLUR1BUS-Harness) | C F D | 15,956 | 46,425 | 8.9 | 32% | 39% | 45% | 247 KB | 0 |
| [and1truong/phpun](https://github.com/and1truong/phpun) | C C E | 15,568 | 32,479 | 2.1 | 79% | 11% | 99% | 485 KB | 0 |
| [bassseamoor/render-queue](https://github.com/bassseamoor/render-queue) | C C E | 15,428 | 57,065 | 1.7 | 70% | 12% | 0% | 4,831 KB | 0 |
| [damianvtran/local-operator](https://github.com/damianvtran/local-operator) | C E D | 15,189 | 17,417 | 38.7 | 59% | 35% | 45% | 3,145 KB | 217 |
| [cyberchronos00/code-graph](https://github.com/cyberchronos00/code-graph) | C D D | 15,186 | 22,217 | 0.0 | 70% | 0% | – | 219 KB | 4 |
| [blairham/sh](https://github.com/blairham/sh) | C D B | 15,030 | 17,943 | 85.5 | 60% | 2% | 99% | 2,640 KB | 1 |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 14,885 | 17,028 | 14.2 | 52% | 39% | 100% | 567 KB | 0 |
| [code-yeongyu/senpi](https://github.com/code-yeongyu/senpi) | C D B | 14,833 | 22,116 | 25.5 | 62% | 15% | 98% | 433 KB | 474 |
| [Dicklesworthstone/asupersync](https://github.com/Dicklesworthstone/asupersync) | C E D | 14,575 | 16,940 | 0.0 | 60% | 39% | 13% | 2,284 KB | 282 |
| [beefsack/plasma-auto-tiler](https://github.com/beefsack/plasma-auto-tiler) | C F B | 14,112 | 21,098 | 0.0 | 62% | 0% | 98% | 850 KB | 0 |
| [arif-rachim/renox](https://github.com/arif-rachim/renox) | C E B | 14,106 | 30,208 | 7.0 | 54% | 41% | 84% | 108 KB | 0 |
| [BigRain-11122/Bigmedia](https://github.com/BigRain-11122/Bigmedia) | C C D | 13,927 | 50,908 | 0.0 | 87% | 3% | – | 66 KB | 0 |
| [designathan1988/app-roadcraft-v2](https://github.com/designathan1988/app-roadcraft-v2) | C E D | 13,772 | 107,308 | 0.0 | 66% | 14% | – | 796 KB | 0 |
| [busytools/forge](https://github.com/busytools/forge) | C E C | 13,749 | 23,245 | 14.4 | 50% | 46% | 100% | 813 KB | 0 |
| [bigfarts/nettai](https://github.com/bigfarts/nettai) | C E F | 13,676 | 63,160 | 0.0 | 70% | 43% | – | 146 KB | 0 |
| [aurigax-ai/ostia](https://github.com/aurigax-ai/ostia) | C F B | 13,589 | 25,135 | 8.6 | 36% | 0% | 83% | 301 KB | 1 |
| [bdgrz/compliance](https://github.com/bdgrz/compliance) | C E B | 13,241 | 20,411 | 13.1 | 68% | 0% | 100% | 594 KB | 1 |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C D C | 13,114 | 12,682 | 12.4 | 64% | 21% | 100% | 603 KB | 8 |
| [Angriff36/capsule](https://github.com/Angriff36/capsule) | C C C | 13,089 | 352,147 | 0.1 | 79% | 54% | 86% | 5,160 KB | 0 |
| [DocMorphic/strep](https://github.com/DocMorphic/strep) | C B B | 13,072 | 17,186 | 0.0 | 86% | 25% | 84% | 411 KB | 0 |
| [chio-labs/sqlbuild](https://github.com/chio-labs/sqlbuild) | C E B | 12,793 | 25,461 | 14.9 | 70% | 15% | 99% | 146 KB | 41 |
| [altumur/server-vms-course](https://github.com/altumur/server-vms-course) | C E D | 12,767 | 28,847 | 0.0 | 54% | 26% | – | 361 KB | 0 |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C D A | 12,232 | 21,076 | 30.7 | 66% | 48% | 91% | 253 KB | 0 |
| [daihaya000/LeafCodePi](https://github.com/daihaya000/LeafCodePi) | C E D | 12,056 | 22,799 | 0.4 | 57% | 21% | – | 472 KB | 0 |
| [benagricola/placemat](https://github.com/benagricola/placemat) | C E D | 12,049 | 120,779 | 0.0 | 43% | 0% | – | 775 KB | 0 |
| [carrick-tools/carrick](https://github.com/carrick-tools/carrick) | C C B | 11,913 | 13,035 | 15.8 | 77% | 30% | 99% | 1,020 KB | 5 |
| [DavidAlexKelly/anchor-foundry](https://github.com/DavidAlexKelly/anchor-foundry) | C C B | 11,810 | 12,274 | 20.0 | 85% | 48% | 87% | 1,124 KB | 0 |
| [celox-sim/celox](https://github.com/celox-sim/celox) | C E C | 11,549 | 30,835 | 10.6 | 48% | 24% | 100% | 260 KB | 10 |
| [dbhq-uk/6502](https://github.com/dbhq-uk/6502) | C E B | 11,533 | 17,850 | 1.2 | 45% | 0% | 98% | 53 KB | 0 |
| [B055OB/boontrack-inbox](https://github.com/B055OB/boontrack-inbox) | C E D | 11,497 | 12,397 | 0.0 | 48% | 24% | – | 219 KB | 0 |
| [CrispStrobe/bw-board](https://github.com/CrispStrobe/bw-board) | C E B | 11,276 | 412,790 | 15.2 | 44% | 4% | 98% | 952 KB | 1 |
| [bex-co/bex](https://github.com/bex-co/bex) | C F B | 11,228 | 26,342 | 0.0 | 37% | 52% | 90% | 545 KB | 569 |
| [bigduu/Bamboo-agent](https://github.com/bigduu/Bamboo-agent) | C D D | 11,188 | 16,274 | 6.8 | 60% | 28% | 44% | 1,164 KB | 20 |
| [AshishKumar4/dew](https://github.com/AshishKumar4/dew) | C C A | 11,088 | 28,860 | 0.1 | 72% | 38% | 100% | 112 KB | 1 |
| [dongnguyenvie/BashCut](https://github.com/dongnguyenvie/BashCut) | C D D | 11,032 | 20,232 | 5.5 | 61% | 18% | 100% | 79 KB | 61 |
| [augments-labs/crucible-code](https://github.com/augments-labs/crucible-code) | C C C | 10,969 | 15,077 | 17.1 | 73% | 0% | 100% | 102 KB | 0 |
| [dogancanyildiz/kenet](https://github.com/dogancanyildiz/kenet) | C E B | 10,738 | 18,319 | 5.6 | 41% | 0% | 95% | 30 KB | 0 |
| [armanisadeghi/matrx-extend](https://github.com/armanisadeghi/matrx-extend) | C B B | 10,728 | 109,165 | 0.1 | 84% | 17% | 76% | 793 KB | 0 |
| [canias7/isibi-app](https://github.com/canias7/isibi-app) | C E C | 10,222 | 20,774 | 0.1 | 42% | 26% | 100% | 2,397 KB | 0 |
| [DankerMu/open-wb](https://github.com/DankerMu/open-wb) | C F B | 10,191 | 17,746 | 22.7 | 39% | 45% | 98% | 1,144 KB | 0 |
| [ahrav/eidnara](https://github.com/ahrav/eidnara) | C E C | 10,191 | 16,013 | 9.7 | 54% | 34% | 64% | 1,713 KB | 0 |
| [by77er/distributed_agents_environments](https://github.com/by77er/distributed_agents_environments) | C E D | 10,161 | 29,762 | 0.0 | 67% | 0% | – | 436 KB | 0 |
| [alexeygrigorev/cloudflare-agent-git](https://github.com/alexeygrigorev/cloudflare-agent-git) | C E C | 10,061 | 50,691 | 0.0 | 57% | 14% | 100% | 118 KB | 0 |
| [danielriosgarza/PlatosCave](https://github.com/danielriosgarza/PlatosCave) | C B D | 10,008 | 28,829 | 8.8 | 89% | 67% | – | 82 KB | 0 |
| [cordel-app/gymdesk](https://github.com/cordel-app/gymdesk) | D C B | 9,787 | 17,126 | 15.9 | 70% | 8% | 89% | 120 KB | 0 |
| [BryceCurran86/PlanReader-3D](https://github.com/BryceCurran86/PlanReader-3D) | D E B | 9,726 | 11,505 | 18.4 | 48% | 10% | 100% | 370 KB | 0 |
| [Drakosfire/DungeonMindBuddy](https://github.com/Drakosfire/DungeonMindBuddy) | D C D | 9,601 | 16,529 | 10.7 | 72% | 28% | – | 238 KB | 1 |
| [cepeter-job/SillyTavern-Telegram-Bridge](https://github.com/cepeter-job/SillyTavern-Telegram-Bridge) | D E A | 9,597 | 38,515 | 14.0 | 43% | 42% | 97% | 58 KB | 2 |
| [AffineFoundation/affine](https://github.com/AffineFoundation/affine) | D C D | 9,524 | 13,220 | 1.6 | 77% | 37% | – | 95 KB | 5 |
| [benniejoseph/OmniAgentOS](https://github.com/benniejoseph/OmniAgentOS) | D C B | 9,487 | 231,548 | 3.8 | 72% | 9% | 98% | 448 KB | 0 |
| [777genius/agent-notifications](https://github.com/777genius/agent-notifications) | D D A | 9,405 | 15,715 | 8.0 | 69% | 45% | 95% | 141 KB | 816 |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D E B | 9,392 | 24,379 | 18.6 | 58% | 20% | 99% | 1,714 KB | 5 |
| [666666666666gao/Re-ID](https://github.com/666666666666gao/Re-ID) | D C F | 9,171 | 1,283,755 | 0.0 | 72% | 0% | – | 4,877 KB | 0 |
| [APKiwiOrg/KhaozEngine](https://github.com/APKiwiOrg/KhaozEngine) | D E B | 9,068 | 19,693 | 0.1 | 45% | 14% | 83% | 176 KB | 0 |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D E C | 9,064 | 11,755 | 4.3 | 42% | 26% | 97% | 94 KB | 0 |
| [beamivalice/sushi](https://github.com/beamivalice/sushi) | D E D | 9,054 | 13,111 | 0.3 | 59% | 10% | 0% | 2,847 KB | 196 |
| [bitty-terminal/bitty](https://github.com/bitty-terminal/bitty) | D C C | 9,051 | 11,160 | 21.0 | 77% | 22% | 100% | 309 KB | 2 |
| [angelcreator113/Episode-Canonical-Control-Record](https://github.com/angelcreator113/Episode-Canonical-Control-Record) | D E B | 8,907 | 14,464 | 31.8 | 54% | 75% | 100% | 540 KB | 0 |
| [brsbl/moss-multi](https://github.com/brsbl/moss-multi) | D F D | 8,888 | 36,664 | 0.1 | 74% | 0% | 67% | 45 KB | 0 |
| [ariefsaid/gordi-mos](https://github.com/ariefsaid/gordi-mos) | D D B | 8,870 | 15,899 | 13.6 | 61% | 2% | 73% | 332 KB | 1 |
| [dimpurr/chat-stasher](https://github.com/dimpurr/chat-stasher) | D E B | 8,808 | 13,323 | 0.0 | 52% | 16% | 100% | 793 KB | 0 |
| [Ashwani1611/shvya-ai](https://github.com/Ashwani1611/shvya-ai) | D D B | 8,794 | 13,312 | 18.6 | 63% | 30% | 97% | 127 KB | 0 |
| [donvargax/itos](https://github.com/donvargax/itos) | D E B | 8,790 | 18,307 | 0.0 | 46% | 32% | 73% | 89 KB | 0 |
| [boburning/portcove](https://github.com/boburning/portcove) | D E B | 8,738 | 10,326 | 27.3 | 57% | 8% | 94% | 536 KB | 6 |
| [aalzriqat/Auto](https://github.com/aalzriqat/Auto) | D D A | 8,685 | 12,754 | 7.1 | 64% | 33% | 90% | 359 KB | 2 |
| [dmukayev/lubao](https://github.com/dmukayev/lubao) | D E D | 8,620 | 16,009 | 0.0 | 65% | 0% | – | 164 KB | 0 |
| [1deter/forest-speedrun-tool](https://github.com/1deter/forest-speedrun-tool) | D E C | 8,508 | 15,474 | 0.0 | 56% | 0% | 100% | 137 KB | 1 |
| [bhrumom/fabushi-desktop](https://github.com/bhrumom/fabushi-desktop) | D E C | 8,482 | 17,916 | 1.3 | 66% | 0% | 67% | 607 KB | 0 |
| [DavidObando/gsharp](https://github.com/DavidObando/gsharp) | D D B | 8,467 | 11,694 | 10.1 | 64% | 30% | 97% | 652 KB | 565 |
| [backspring-labs/squad-ops](https://github.com/backspring-labs/squad-ops) | D F A | 8,380 | 14,442 | 17.2 | 39% | 0% | 100% | 324 KB | 0 |
| [compiled-run/dragoncss](https://github.com/compiled-run/dragoncss) | D E D | 8,358 | 1,149,738 | 6.2 | 44% | 0% | 96% | 2,676 KB | 0 |
| [AbnerCruz/Ecosystem](https://github.com/AbnerCruz/Ecosystem) | D D B | 8,330 | 19,086 | 6.6 | 61% | 10% | 81% | 378 KB | 0 |
| [deltahdl/deltahdl](https://github.com/deltahdl/deltahdl) | D B D | 8,186 | 12,906 | 0.0 | 84% | 66% | 3% | 51 KB | 0 |
| [Dicklesworthstone/frankenpandas](https://github.com/Dicklesworthstone/frankenpandas) | D F C | 8,129 | 10,890 | 0.1 | 82% | 4% | 100% | 9,726 KB | 21 |
| [287113535qq-cmyk/sg-capture-runner](https://github.com/287113535qq-cmyk/sg-capture-runner) | D E D | 7,926 | 79,976 | 0.0 | 78% | 11% | – | 68 KB | 0 |
| [beanpool-org/beanpool](https://github.com/beanpool-org/beanpool) | D C C | 7,650 | 19,055 | 32.9 | 74% | 17% | 97% | 524 KB | 1 |
| [coachhornsby/fbis](https://github.com/coachhornsby/fbis) | D E C | 7,595 | 35,150 | 25.5 | 52% | 3% | 64% | 453 KB | 1 |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D E C | 7,551 | 8,002 | 27.4 | 57% | 3% | 52% | 92 KB | 1 |
| [diff-lab-com/shannon-agent](https://github.com/diff-lab-com/shannon-agent) | D E C | 7,533 | 16,887 | 9.5 | 52% | 10% | 86% | 383 KB | 1 |
| [doctorjei/kanibako-cli](https://github.com/doctorjei/kanibako-cli) | D E B | 7,463 | 10,208 | 0.0 | 55% | 44% | 82% | 534 KB | 7 |
| [adysbgy/celestial-pointing](https://github.com/adysbgy/celestial-pointing) | D E B | 7,427 | 12,033 | 0.0 | 71% | 0% | 85% | 470 KB | 0 |
| [antallusion/pirates](https://github.com/antallusion/pirates) | D F C | 7,375 | 12,295 | 0.0 | 43% | 53% | 98% | 454 KB | 0 |
| [cshaxu/nxvm](https://github.com/cshaxu/nxvm) | D F C | 7,371 | 27,355 | 0.0 | 65% | 0% | 74% | 759 KB | 218 |
| [angeles725/sdd-investigacion](https://github.com/angeles725/sdd-investigacion) | D E C | 7,359 | 11,089 | 17.9 | 56% | 22% | 100% | 177 KB | 0 |
| [21bcarlisle-arch/synthetic-enterprise](https://github.com/21bcarlisle-arch/synthetic-enterprise) | D B C | 7,311 | 381,118 | 0.0 | 86% | 71% | 96% | 1,215 KB | 2 |
| [burin-labs/harn](https://github.com/burin-labs/harn) | D E C | 7,241 | 14,808 | 23.4 | 55% | 20% | 79% | 20,439 KB | 27 |
| [daryljanzen/shadow-of-existence](https://github.com/daryljanzen/shadow-of-existence) | D E E | 7,174 | 19,210 | 9.6 | 46% | 38% | 73% | 875 KB | 1 |
| [dimakis/mitzo](https://github.com/dimakis/mitzo) | D E A | 7,155 | 21,332 | 9.5 | 49% | 0% | 95% | 285 KB | 0 |
| [ali-ulu/huqan](https://github.com/ali-ulu/huqan) | D E B | 7,148 | 13,576 | 29.6 | 59% | 58% | 97% | 67 KB | 7 |
| [alimardon123/edel](https://github.com/alimardon123/edel) | D F D | 7,118 | 11,211 | 5.2 | 42% | 0% | 77% | 101 KB | 1 |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 7,047 | 40,946 | 7.6 | 35% | 0% | 94% | 67 KB | 1 |
| [alexkads/VintageLightbox](https://github.com/alexkads/VintageLightbox) | D D D | 6,932 | 13,702 | 0.0 | 70% | 6% | 0% | 581 KB | 0 |
| [bpeppersjr/datahub](https://github.com/bpeppersjr/datahub) | D D D | 6,879 | 458,520 | 0.0 | 64% | 41% | – | 512 KB | 0 |
| [andyl-technologies/aos](https://github.com/andyl-technologies/aos) | D E D | 6,847 | 62,421 | 15.9 | 58% | 15% | – | 1,521 KB | 8 |
| [cranthony/time-tracker-client](https://github.com/cranthony/time-tracker-client) | D E C | 6,744 | 10,900 | 4.9 | 63% | 19% | 100% | 141 KB | 0 |
| [a11ign/a11ign](https://github.com/a11ign/a11ign) | D D A | 6,705 | 12,398 | 50.6 | 67% | 39% | 98% | 118 KB | 0 |
| [chunbaefatherjunbae/tactical-recon](https://github.com/chunbaefatherjunbae/tactical-recon) | D F E | 6,666 | 12,650 | 1.2 | 40% | 0% | 91% | 279 KB | 0 |
| [Artexis10/exomem](https://github.com/Artexis10/exomem) | D C B | 6,650 | 16,643 | 13.4 | 72% | 20% | 90% | 613 KB | 10 |
| [Deveadra/katcha](https://github.com/Deveadra/katcha) | D E C | 6,628 | 10,435 | 9.9 | 51% | 2% | 99% | 136 KB | 0 |
| [davide-matasci/myos](https://github.com/davide-matasci/myos) | D F E | 6,582 | 12,034 | 6.8 | 38% | 54% | 95% | 89 KB | 1 |
| [dnilgis/agsist](https://github.com/dnilgis/agsist) | D F E | 6,582 | 72,020 | 0.0 | 9% | 6% | 74% | 445 KB | 1 |
| [dmille6/minecraft-ai-test](https://github.com/dmille6/minecraft-ai-test) | D E D | 6,418 | 14,017 | 0.0 | 48% | 12% | – | 591 KB | 0 |
| [cleat-team/cleat](https://github.com/cleat-team/cleat) | D E A | 6,350 | 8,222 | 41.9 | 60% | 22% | 100% | 384 KB | 0 |
| [botiverse/antiproton](https://github.com/botiverse/antiproton) | D E D | 6,092 | 8,344 | 26.5 | 57% | 0% | – | 262 KB | 28 |
| [Diabl0269/agentsynth](https://github.com/Diabl0269/agentsynth) | D E E | 5,997 | 14,344 | 17.0 | 44% | 0% | 100% | 63 KB | 6 |
| [atomeam/void-loop](https://github.com/atomeam/void-loop) | D E C | 5,859 | 10,913 | 6.4 | 71% | 0% | 90% | 552 KB | 0 |
| [anurag-duddu/specimen-digitization-app](https://github.com/anurag-duddu/specimen-digitization-app) | D E C | 5,817 | 17,104 | 5.2 | 59% | 3% | 100% | 120 KB | 0 |
| [chester-hill-solutions/callcaster](https://github.com/chester-hill-solutions/callcaster) | D B B | 5,812 | 106,014 | 14.6 | 82% | 20% | 89% | 749 KB | 2 |
| [caura-ai/caura](https://github.com/caura-ai/caura) | D F B | 5,804 | 7,649 | 17.0 | 34% | 15% | 100% | 744 KB | 498 |
| [buffyfan9303-spec/NURI-HOLDEM](https://github.com/buffyfan9303-spec/NURI-HOLDEM) | D E B | 5,769 | 9,102 | 7.3 | 54% | 14% | 86% | 411 KB | 0 |
| [cheminisifeddine/allomokawil](https://github.com/cheminisifeddine/allomokawil) | D B D | 5,713 | 8,625 | 0.0 | 88% | 61% | – | 126 KB | 0 |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D F C | 5,644 | 9,340 | 13.1 | 38% | 8% | 100% | 403 KB | 2 |
| [devantler-tech/platform](https://github.com/devantler-tech/platform) | D E B | 5,641 | 8,931 | 21.8 | 58% | 6% | 96% | 310 KB | 33 |
| [57974422j-art/AiMarketing](https://github.com/57974422j-art/AiMarketing) | D E F | 5,558 | 10,264 | 0.0 | 53% | 19% | – | 463 KB | 2 |
| [arkadianet/ergo](https://github.com/arkadianet/ergo) | D D B | 5,507 | 46,420 | 7.6 | 61% | 0% | 98% | 220 KB | 4 |
| [devhusdk/rules_dx](https://github.com/devhusdk/rules_dx) | D C D | 5,475 | 9,741 | 24.9 | 80% | 13% | 0% | 168 KB | 1 |
| [antpan5608-san/game-fengshen](https://github.com/antpan5608-san/game-fengshen) | D D D | 5,443 | 145,698 | 0.0 | 68% | 56% | – | 377 KB | 0 |
| [Dicklesworthstone/frankensqlite](https://github.com/Dicklesworthstone/frankensqlite) | D F D | 5,405 | 8,882 | 0.0 | 66% | 0% | 36% | 12,458 KB | 243 |
| [Disinto/disinto](https://github.com/Disinto/disinto) | D C D | 5,303 | 5,550 | 0.0 | 72% | 25% | – | 80 KB | 0 |
| [bk-squared/rfx](https://github.com/bk-squared/rfx) | D E B | 5,265 | 9,713 | 14.4 | 66% | 25% | 97% | 238 KB | 9 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,258 | 10,628 | 28.1 | 58% | 11% | 88% | 1,492 KB | 69,941 |
| [CorbanuCore/CorbanuTerminal](https://github.com/CorbanuCore/CorbanuTerminal) | D C C | 5,234 | 30,889 | 5.2 | 78% | 0% | 84% | 560 KB | 0 |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 5,211 | 7,657 | 16.3 | 48% | 23% | 99% | 525 KB | 5 |
| [capthvnsen/alans-way](https://github.com/capthvnsen/alans-way) | E D B | 4,837 | 6,711 | 2.8 | 69% | 0% | 81% | 151 KB | 32 |
| [atgreen/evergreen](https://github.com/atgreen/evergreen) | E E B | 4,817 | 8,360 | 4.9 | 50% | 37% | 86% | 1,878 KB | 53 |
| [AnonymousKoo/avuhz-infra](https://github.com/AnonymousKoo/avuhz-infra) | E E D | 4,730 | 14,693 | 19.4 | 43% | 7% | – | 43 KB | 0 |
| [DobbyVPN/DobbyVPN](https://github.com/DobbyVPN/DobbyVPN) | E E C | 4,688 | 7,342 | 0.0 | 49% | 13% | 87% | 210 KB | 66 |
| [awaku7/agentcli](https://github.com/awaku7/agentcli) | E E B | 4,674 | 9,150 | 6.6 | 45% | 7% | 96% | 186 KB | 12 |
| [666666666666gao/RGB-T](https://github.com/666666666666gao/RGB-T) | E C F | 4,647 | 2,793,657 | 0.0 | 83% | 26% | – | 877 KB | 0 |
| [aowvn-10diem/aowvn-monika](https://github.com/aowvn-10diem/aowvn-monika) | E D E | 4,635 | 38,038 | 4.9 | 63% | 3% | 99% | 2,778 KB | 0 |
| [aanrizal01/ispsync-platform](https://github.com/aanrizal01/ispsync-platform) | E E F | 4,632 | 9,921 | 0.0 | 53% | 0% | – | 1,717 KB | 0 |
| [asdaq-samir/flight_plan](https://github.com/asdaq-samir/flight_plan) | E E B | 4,625 | 7,632 | 0.9 | 66% | 51% | 100% | 84 KB | 0 |
| [aerol-ai/microvm](https://github.com/aerol-ai/microvm) | E F B | 4,610 | 14,123 | 8.0 | 25% | 6% | 94% | 334 KB | 28 |
| [Ammar0909291/My-tutor](https://github.com/Ammar0909291/My-tutor) | E F B | 4,602 | 19,083 | 0.0 | 34% | 8% | 100% | 3,716 KB | 0 |
| [cristianoneta/neta-dao](https://github.com/cristianoneta/neta-dao) | E F E | 4,598 | 19,592 | 8.2 | 6% | 0% | 98% | 1,659 KB | 0 |
| [aloworld-org/alo-os](https://github.com/aloworld-org/alo-os) | E D D | 4,596 | 12,508 | 20.0 | 67% | 43% | – | 129 KB | 0 |
| [DealAppSeo/repid-engine](https://github.com/DealAppSeo/repid-engine) | E D B | 4,564 | 5,466 | 16.6 | 66% | 38% | 99% | 868 KB | 0 |
| [cmcoffee/oddjob](https://github.com/cmcoffee/oddjob) | E F B | 4,524 | 5,814 | 0.0 | 52% | 14% | 78% | 476 KB | 2 |
| [Cotal-AI/Cotal](https://github.com/Cotal-AI/Cotal) | E B E | 4,511 | 25,804 | 40.3 | 84% | 42% | 52% | 643 KB | 316 |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E E A | 4,459 | 10,939 | 20.5 | 55% | 6% | 88% | 359 KB | 6 |
| [Blackwellboy/little-chits](https://github.com/Blackwellboy/little-chits) | E E B | 4,429 | 4,770 | 4.4 | 47% | 0% | 100% | 186 KB | 22 |
| [akienm/cairn](https://github.com/akienm/cairn) | E E D | 4,423 | 83,936 | 0.0 | 58% | 33% | – | 202 KB | 0 |
| [ckopsa/waymark](https://github.com/ckopsa/waymark) | E E B | 4,253 | 4,817 | 33.4 | 45% | 11% | 93% | 375 KB | 0 |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E E B | 4,222 | 14,443 | 28.4 | 48% | 16% | 100% | 617 KB | 1 |
| [benletchford/systemless](https://github.com/benletchford/systemless) | E F C | 4,095 | 6,315 | 47.0 | 34% | 10% | 100% | 1,182 KB | 48 |
| [david-dabert/workout-vision](https://github.com/david-dabert/workout-vision) | E C A | 4,085 | 8,102 | 2.0 | 87% | 25% | 95% | 293 KB | 1 |
| [devantler-tech/ksail](https://github.com/devantler-tech/ksail) | E E B | 4,033 | 5,376 | 14.5 | 79% | 0% | 100% | 506 KB | 165 |
| [Abzum-NZ/Abzum-Vortex](https://github.com/Abzum-NZ/Abzum-Vortex) | E B D | 4,028 | 7,839 | 28.2 | 86% | 25% | 100% | 315 KB | 0 |
| [danielsimonjr/Universal-Physics-Tensor](https://github.com/danielsimonjr/Universal-Physics-Tensor) | E F B | 4,024 | 51,056 | 8.8 | 48% | 11% | 97% | 152 KB | 0 |
| [BigBIueWhale/rustdesk_fork](https://github.com/BigBIueWhale/rustdesk_fork) | E E E | 3,990 | 7,292 | 0.0 | 60% | 2% | 33% | 1,815 KB | 6 |
| [2AMLogic/klayout-tools](https://github.com/2AMLogic/klayout-tools) | E D B | 3,903 | 9,494 | 19.7 | 64% | 33% | 96% | 665 KB | 5 |
| [alplabai/alp-sdk](https://github.com/alplabai/alp-sdk) | E E B | 3,834 | 11,620 | 16.1 | 50% | 0% | 99% | 553 KB | 5 |
| [dikuwa/scolapro](https://github.com/dikuwa/scolapro) | E E C | 3,783 | 7,572 | 15.0 | 66% | 50% | 99% | 58 KB | 0 |
| [ASC-Community/AngouriMath](https://github.com/ASC-Community/AngouriMath) | E B B | 3,754 | 4,419 | 16.8 | 84% | 25% | 100% | 1,837 KB | 831 |
| [adrianfzh/adrianmathtuition-website](https://github.com/adrianfzh/adrianmathtuition-website) | E F D | 3,742 | 30,808 | 0.2 | 44% | 7% | 0% | 1,215 KB | 0 |
| [christopherdonini/spatial-ide](https://github.com/christopherdonini/spatial-ide) | E E A | 3,658 | 17,280 | 5.2 | 48% | 51% | 98% | 239 KB | 0 |
| [crypt0rr/EdgeWatch](https://github.com/crypt0rr/EdgeWatch) | E D A | 3,651 | 5,988 | 15.6 | 63% | 28% | 97% | 107 KB | 5 |
| [Almenning/Flyt-app](https://github.com/Almenning/Flyt-app) | E E C | 3,629 | 10,727 | 1.2 | 52% | 5% | 93% | 713 KB | 0 |
| [cwahli/Health-tracker](https://github.com/cwahli/Health-tracker) | E E D | 3,456 | 6,491 | 18.7 | 56% | 33% | 45% | 365 KB | 0 |
| [choir-hip/go-choir](https://github.com/choir-hip/go-choir) | E E B | 3,451 | 7,695 | 0.1 | 63% | 4% | 96% | 287 KB | 0 |
| [CarstVaartjes/vonk-forge-recipes](https://github.com/CarstVaartjes/vonk-forge-recipes) | E F C | 3,401 | 8,648 | 29.7 | 48% | 11% | 98% | 496 KB | 0 |
| [Admin-Adher/Norva](https://github.com/Admin-Adher/Norva) | E E C | 3,393 | 19,477 | 13.1 | 59% | 15% | 98% | 7,443 KB | 0 |
| [chad04220/Solace-Express](https://github.com/chad04220/Solace-Express) | E E C | 3,390 | 9,527 | 0.0 | 48% | 44% | 65% | 762 KB | 0 |
| [devantler-tech/monorepo](https://github.com/devantler-tech/monorepo) | E D C | 3,357 | 5,030 | 16.3 | 69% | 35% | 100% | 342 KB | 1 |
| [dehuadong/seeaihub-server-next](https://github.com/dehuadong/seeaihub-server-next) | E E C | 3,327 | 9,441 | 0.0 | 57% | 46% | 64% | 364 KB | 0 |
| [Disable-OP/Local-Blockman-GO-1.24.4](https://github.com/Disable-OP/Local-Blockman-GO-1.24.4) | E E D | 3,270 | 15,648 | 0.0 | 72% | 0% | 6% | 272 KB | 1 |
| [arodrigos/shoot-my-starship](https://github.com/arodrigos/shoot-my-starship) | E E A | 3,267 | 3,816 | 4.7 | 66% | 67% | 97% | 147 KB | 0 |
| [chenguangwu/chenguangwu.github.io](https://github.com/chenguangwu/chenguangwu.github.io) | E E E | 3,233 | 87,576 | 0.0 | 67% | 0% | 93% | 1,052 KB | 0 |
| [dawnop/dawn-lang](https://github.com/dawnop/dawn-lang) | E E D | 3,217 | 21,383 | 12.7 | 56% | 36% | 97% | 332 KB | 154 |
| [ai-2070/net](https://github.com/ai-2070/net) | E F B | 3,146 | 10,363 | 8.8 | 27% | 0% | 85% | 3,059 KB | 3 |
| [big-dimple/dachoupai](https://github.com/big-dimple/dachoupai) | E E C | 3,084 | 111,730 | 2.0 | 73% | 0% | 100% | 218 KB | 0 |
| [apmantza/pi-lens](https://github.com/apmantza/pi-lens) | E F A | 2,986 | 24,434 | 23.1 | 36% | 12% | 98% | 449 KB | 466 |
| [40oleg/nona](https://github.com/40oleg/nona) | E F C | 2,931 | 12,588 | 3.0 | 35% | 0% | 94% | 901 KB | 0 |
| [bluejetty/draft](https://github.com/bluejetty/draft) | E E C | 2,885 | 4,791 | 9.9 | 57% | 47% | 95% | 1,241 KB | 0 |
| [bruceleeroy266/barber-study-pro](https://github.com/bruceleeroy266/barber-study-pro) | E E C | 2,841 | 6,758 | 11.5 | 74% | 20% | 100% | 523 KB | 0 |
| [as20394569/dawn-adventure](https://github.com/as20394569/dawn-adventure) | E E F | 2,804 | 20,108 | 0.0 | 44% | 44% | – | 5,145 KB | 0 |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 2,782 | 15,383 | 21.1 | 42% | 12% | 91% | 301 KB | 22 |
| [calcit-lang/calcit](https://github.com/calcit-lang/calcit) | E E C | 2,777 | 5,153 | 19.3 | 44% | 16% | 99% | 862 KB | 148 |
| [9529360-cpu/stardust-hermes](https://github.com/9529360-cpu/stardust-hermes) | E E B | 2,731 | 5,721 | 8.7 | 51% | 9% | 97% | 639 KB | 0 |
| [cemdizdar85-arch/mevzuat-radar](https://github.com/cemdizdar85-arch/mevzuat-radar) | E E E | 2,682 | 1,428,568 | 0.0 | 49% | 27% | 78% | 328 KB | 1 |
| [1377385356/openxiangda](https://github.com/1377385356/openxiangda) | E B C | 2,661 | 7,137 | 0.0 | 82% | 74% | 94% | 293 KB | 0 |
| [Dj-Shortcut/mw2-rust-skate-rewrite](https://github.com/Dj-Shortcut/mw2-rust-skate-rewrite) | E E E | 2,641 | 102,011 | 6.5 | 44% | 0% | 100% | 290 KB | 0 |
| [ChasePlank/aside](https://github.com/ChasePlank/aside) | E C D | 2,628 | 5,100 | 0.0 | 83% | 36% | – | 7,223 KB | 0 |
| [DanielOpazoD/vexus-sim](https://github.com/DanielOpazoD/vexus-sim) | E D A | 2,595 | 4,621 | 7.4 | 61% | 0% | 87% | 126 KB | 0 |
| [diy-accounting-uk/submit.diyaccounting.co.uk](https://github.com/diy-accounting-uk/submit.diyaccounting.co.uk) | E F B | 2,575 | 7,017 | 8.4 | 58% | 0% | 99% | 1,032 KB | 0 |
| [CultureBotAI/CellStructureMech](https://github.com/CultureBotAI/CellStructureMech) | E E E | 2,559 | 86,913 | 31.1 | 91% | 0% | 100% | 492 KB | 0 |
| [ArchonMegalon/chummer-android](https://github.com/ArchonMegalon/chummer-android) | E C B | 2,504 | 5,479 | 18.7 | 75% | 46% | 100% | 1,235 KB | 0 |
| [daymade/claude-code-skills](https://github.com/daymade/claude-code-skills) | E E C | 2,455 | 4,161 | 13.4 | 54% | 67% | 99% | 152 KB | 1,451 |
| [DaisukeDaisuke/dq9-AT](https://github.com/DaisukeDaisuke/dq9-AT) | E E E | 2,342 | 8,298 | 0.0 | 45% | 19% | 91% | 101 KB | 0 |
| [atomrat46-code/Pulsekit-public](https://github.com/atomrat46-code/Pulsekit-public) | E C D | 2,336 | 5,826 | 2.4 | 80% | 14% | – | 166 KB | 0 |
| [BlueSkyz-Labs/SGPS-Marketing](https://github.com/BlueSkyz-Labs/SGPS-Marketing) | E B A | 2,328 | 4,202 | 13.6 | 85% | 7% | 90% | 56 KB | 0 |
| [dlrjs9702-dot/omok-live](https://github.com/dlrjs9702-dot/omok-live) | E E B | 2,325 | 4,294 | 6.4 | 61% | 0% | 85% | 535 KB | 0 |
| [davemt74-lang/otro](https://github.com/davemt74-lang/otro) | E F C | 2,317 | 4,387 | 8.5 | 36% | 15% | 100% | 119 KB | 0 |
| [BashfulBits/city-meeting-podcasts](https://github.com/BashfulBits/city-meeting-podcasts) | E E B | 2,302 | 231,268 | 7.6 | 59% | 33% | 97% | 486 KB | 2 |
| [BuRnEd4AiM/HA-Floorplanner](https://github.com/BuRnEd4AiM/HA-Floorplanner) | E C C | 2,259 | 4,603 | 6.0 | 76% | 0% | 96% | 1,498 KB | 7 |
| [CompleteTech-LLC-AI-Research/pokemon-harness](https://github.com/CompleteTech-LLC-AI-Research/pokemon-harness) | E F C | 2,233 | 9,802 | 8.0 | 34% | 0% | 99% | 41 KB | 0 |
| [CorbinVentures/Rich-City-League](https://github.com/CorbinVentures/Rich-City-League) | E E E | 2,232 | 3,859 | 13.6 | 55% | 0% | 99% | 171 KB | 2 |
| [Dicklesworthstone/frankenterm](https://github.com/Dicklesworthstone/frankenterm) | E E D | 2,122 | 19,341 | 0.2 | 72% | 0% | 17% | 5,858 KB | 121 |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E C B | 2,111 | 4,764 | 7.5 | 83% | 0% | 99% | 327 KB | 0 |
| [BrucePerens/hams_open](https://github.com/BrucePerens/hams_open) | E F D | 2,094 | 8,487 | 8.1 | 48% | 0% | 100% | 181 KB | 2 |
| [cuihairu/unidict](https://github.com/cuihairu/unidict) | E E C | 2,050 | 5,177 | 0.0 | 55% | 0% | 74% | 71 KB | 0 |
| [aganesy/QFAI](https://github.com/aganesy/QFAI) | E E C | 2,031 | 6,650 | 29.1 | 61% | 0% | 96% | 153 KB | 4 |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E E A | 2,030 | 4,535 | 32.5 | 74% | 9% | 100% | 117 KB | 1 |
| [AH100-1/skylens-stream-rs](https://github.com/AH100-1/skylens-stream-rs) | E E C | 2,020 | 4,599 | 2.6 | 64% | 0% | 100% | 161 KB | 0 |
| [dangkhoaow/freetoolonline-web-test](https://github.com/dangkhoaow/freetoolonline-web-test) | E C E | 1,943 | 3,311 | 0.0 | 78% | 62% | 97% | 2,798 KB | 0 |
| [beorn/yrd](https://github.com/beorn/yrd) | E C C | 1,921 | 2,652 | 0.0 | 71% | 4% | 80% | 251 KB | 1 |
| [asterix88/myshopmanual](https://github.com/asterix88/myshopmanual) | E E C | 1,910 | 2,487 | 1.6 | 55% | 0% | 98% | 53 KB | 0 |
| [danieljbrooks/draft-zero](https://github.com/danieljbrooks/draft-zero) | E F D | 1,891 | 3,645 | 0.0 | 51% | 0% | – | 159 KB | 3 |
| [ai-engineers-guild/ai-stp](https://github.com/ai-engineers-guild/ai-stp) | E F A | 1,879 | 13,789 | 15.2 | 56% | 13% | 96% | 225 KB | 5 |
| [buildcage/isolated-run](https://github.com/buildcage/isolated-run) | E E C | 1,835 | 7,666 | 18.3 | 56% | 23% | 60% | 46 KB | 0 |
| [danonbrez/Holofractal_Harmonicode](https://github.com/danonbrez/Holofractal_Harmonicode) | E E C | 1,777 | 182,440 | 8.7 | 48% | 46% | 90% | 427 KB | 0 |
| [doppler-dsp/doppler](https://github.com/doppler-dsp/doppler) | E F B | 1,700 | 42,134 | 12.1 | 63% | 7% | 100% | 143 KB | 1 |
| [biubiu52011/Pixel-Tetsudo](https://github.com/biubiu52011/Pixel-Tetsudo) | E E E | 1,634 | 8,254 | 0.2 | 66% | 20% | 84% | 5,458 KB | 0 |
| [claymore666/docker-net-dhcp](https://github.com/claymore666/docker-net-dhcp) | E F B | 1,614 | 3,408 | 7.9 | 36% | 0% | 88% | 95 KB | 14 |
| [andygmassey/CM051-Home-Hub-Installer](https://github.com/andygmassey/CM051-Home-Hub-Installer) | E D B | 1,558 | 5,804 | 17.6 | 69% | 0% | 100% | 2,052 KB | 0 |
| [chunxiaoxx/nautilus-compass](https://github.com/chunxiaoxx/nautilus-compass) | E E D | 1,520 | 11,040 | 0.0 | 50% | 39% | 0% | 566 KB | 1,260 |
| [CultureBotAI/HabitatMech](https://github.com/CultureBotAI/HabitatMech) | E F E | 1,515 | 22,867 | 30.8 | 77% | 0% | 100% | 1,206 KB | 0 |
| [divinedavis/Find-A-Crib](https://github.com/divinedavis/Find-A-Crib) | E F D | 1,475 | 5,952 | 0.0 | 0% | 11% | 90% | 536 KB | 0 |
| [2AMLogic/gf180-pll](https://github.com/2AMLogic/gf180-pll) | E E C | 1,467 | 4,614 | 7.5 | 51% | 39% | 98% | 665 KB | 0 |
| [aurlooij-afk/AI-INFINITY](https://github.com/aurlooij-afk/AI-INFINITY) | E E D | 1,462 | 23,722 | 0.4 | 54% | 0% | 83% | 405 KB | 0 |
| [d41ly/coding-governance](https://github.com/d41ly/coding-governance) | E F D | 1,439 | 22,195 | 0.0 | 83% | 0% | 33% | 1,057 KB | 0 |
| [Donh91/Investering-Framework-Archive-v1](https://github.com/Donh91/Investering-Framework-Archive-v1) | E F E | 1,437 | 115,806 | 19.1 | 38% | 6% | 89% | 65 KB | 2 |
| [ai93560137/20260918](https://github.com/ai93560137/20260918) | E F D | 1,422 | 44,728 | 2.0 | 25% | 0% | 100% | 553 KB | 0 |
| [berkmancenter/keyring-wallet](https://github.com/berkmancenter/keyring-wallet) | E E A | 1,345 | 1,567 | 10.8 | 51% | 5% | 98% | 97 KB | 15 |
| [chenchaoyi/gtmux](https://github.com/chenchaoyi/gtmux) | E E A | 1,333 | 6,940 | 18.1 | 72% | 4% | 99% | 266 KB | 2 |
| [davidk15042001/Lulu-Growth-OS-Frontend](https://github.com/davidk15042001/Lulu-Growth-OS-Frontend) | E C E | 1,314 | 3,094 | 0.0 | 83% | 39% | 100% | 161 KB | 0 |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 1,273 | 8,845 | 52.6 | 73% | 8% | 96% | 173 KB | 7 |
| [automaster5013/AgentTrust](https://github.com/automaster5013/AgentTrust) | E F B | 1,190 | 2,578 | 0.0 | 62% | 0% | 78% | 113 KB | 1 |
| [bcesteticaavancada/bcesteticaavancada-alt](https://github.com/bcesteticaavancada/bcesteticaavancada-alt) | E E B | 1,167 | 2,499 | 0.5 | 61% | 7% | 78% | 30 KB | 0 |
| [dominator509/axiom](https://github.com/dominator509/axiom) | E E C | 1,143 | 2,331 | 3.2 | 93% | 17% | 98% | 871 KB | 0 |
| [BFi-AI-247/bfi-ai-247.github.io](https://github.com/BFi-AI-247/bfi-ai-247.github.io) | E E E | 1,122 | 4,771 | 0.0 | 46% | 80% | 39% | 38 KB | 1 |
| [bi421/QROS](https://github.com/bi421/QROS) | E F B | 1,112 | 1,847 | 17.8 | 32% | 0% | 99% | 62 KB | 0 |
| [abangrenderofficial-oss/mdab-129](https://github.com/abangrenderofficial-oss/mdab-129) | E E E | 1,073 | 2,597 | 1.6 | 53% | 0% | 0% | 43 KB | 0 |
| [Alex-Farley/formula-1-data](https://github.com/Alex-Farley/formula-1-data) | E F B | 1,023 | 5,273 | 11.9 | 52% | 0% | 98% | 370 KB | 3 |
| [bonoj/Repository](https://github.com/bonoj/Repository) | F E E | 988 | 9,398 | 0.0 | 45% | 37% | 97% | 426 KB | 0 |
| [avra-lang/avra](https://github.com/avra-lang/avra) | F F C | 957 | 240,436 | 15.5 | 60% | 17% | 100% | 349 KB | 0 |
| [AhmedPeaRL/maximal-one](https://github.com/AhmedPeaRL/maximal-one) | F F D | 921 | 8,164 | 0.0 | 43% | 7% | 82% | 48 KB | 0 |
| [delight0517/selah-bible-meditation](https://github.com/delight0517/selah-bible-meditation) | F E E | 867 | 4,127 | 11.4 | 52% | 10% | 100% | 661 KB | 0 |
| [busshin-it/shinka-dungeon](https://github.com/busshin-it/shinka-dungeon) | F F C | 826 | 165,836 | 0.8 | 28% | 0% | 98% | 851 KB | 0 |
| [burgmanshidde-ancienttrees/ancienttrees](https://github.com/burgmanshidde-ancienttrees/ancienttrees) | F F E | 816 | 45,259 | 0.1 | 14% | 24% | 80% | 784 KB | 0 |
| [Dj-Lee2/farmnow](https://github.com/Dj-Lee2/farmnow) | F B F | 805 | 3,024 | 0.0 | 85% | 81% | – | 1,587 KB | 0 |
| [cpunion/loom-lang](https://github.com/cpunion/loom-lang) | F D A | 791 | 8,127 | 11.1 | 60% | 53% | 98% | 103 KB | 0 |
| [dp-web4/SAGE](https://github.com/dp-web4/SAGE) | F F C | 783 | 1,696 | 8.5 | 0% | 0% | 100% | 2,253 KB | 28 |
| [96kiwi96kiwi-lang/paper-play-ground-13](https://github.com/96kiwi96kiwi-lang/paper-play-ground-13) | F B D | 777 | 1,178 | 0.2 | 87% | 62% | – | 42 KB | 0 |
| [1525745393/EmbyTok-Flutter](https://github.com/1525745393/EmbyTok-Flutter) | F E C | 776 | 2,867 | 0.0 | 53% | 14% | 93% | 126 KB | 3 |
| [covaultxyz/meridian-demos](https://github.com/covaultxyz/meridian-demos) | F B F | 776 | 272,021 | 0.0 | 86% | 81% | – | 188 KB | 0 |
| [by-openclaw/go-acp](https://github.com/by-openclaw/go-acp) | F F B | 755 | 16,937 | 8.8 | 37% | 0% | 97% | 147 KB | 0 |
| [alisheraz-sudo/Rizvi-Dashboard-V5](https://github.com/alisheraz-sudo/Rizvi-Dashboard-V5) | F E E | 687 | 2,608 | 0.1 | 60% | 3% | 100% | 108 KB | 0 |
| [antoniovairo-rgb/Carrier-manager-](https://github.com/antoniovairo-rgb/Carrier-manager-) | F C B | 668 | 5,733 | 0.0 | 75% | 40% | 98% | 6,877 KB | 0 |
| [alessiobaljak/agentic_trading_system](https://github.com/alessiobaljak/agentic_trading_system) | F F D | 661 | 5,782 | 0.0 | 17% | 0% | 46% | 241 KB | 0 |
| [chenrui333/homebrew-tap](https://github.com/chenrui333/homebrew-tap) | F D E | 639 | 2,922 | 65.2 | 68% | 15% | 98% | 92 KB | 10 |
| [dentar1997/AeroUchet](https://github.com/dentar1997/AeroUchet) | F F E | 620 | 2,419 | 6.8 | 50% | 0% | 100% | 158 KB | 0 |
| [Badmaniren/my-userbot](https://github.com/Badmaniren/my-userbot) | F D C | 554 | 4,132 | 0.0 | 68% | 43% | 100% | 93 KB | 0 |
| [amillimatrix-eng/CARBON-Creation-Hub](https://github.com/amillimatrix-eng/CARBON-Creation-Hub) | F F C | 536 | 9,307 | 0.1 | 22% | 0% | 90% | 28 KB | 1 |
| [agotrancoso-create/agotrancoso-loja](https://github.com/agotrancoso-create/agotrancoso-loja) | F E E | 483 | 1,180 | 2.2 | 44% | 0% | 67% | 42 KB | 0 |
| [AshokSachdev7/richdeals](https://github.com/AshokSachdev7/richdeals) | F F F | 441 | 2,652 | 0.0 | 28% | 0% | – | 443 KB | 0 |
| [billradar/rustdesk-custom](https://github.com/billradar/rustdesk-custom) | F F C | 424 | 2,235 | 3.4 | 27% | 38% | 100% | 28 KB | 0 |
| [dakleyer/structural-awareness-contributions](https://github.com/dakleyer/structural-awareness-contributions) | F F E | 421 | 75,433 | 0.1 | 27% | 0% | 78% | 36 KB | 0 |
| [DEimos12-bi/genzhype-scraper](https://github.com/DEimos12-bi/genzhype-scraper) | F F E | 365 | 1,950 | 0.0 | 0% | 0% | 87% | 561 KB | 0 |
| [BigRain-11122/BigDomain](https://github.com/BigRain-11122/BigDomain) | F F D | 359 | 6,839 | 0.0 | 51% | 0% | – | 424 KB | 0 |
| [BunnyBear1419/asphalt-gauntlet-bot](https://github.com/BunnyBear1419/asphalt-gauntlet-bot) | F E D | 334 | 1,593 | 0.7 | 66% | 0% | 70% | 2,149 KB | 0 |
| [2ty9p66r46-del/english-practice](https://github.com/2ty9p66r46-del/english-practice) | F E E | 334 | 1,269 | 0.6 | 45% | 0% | 100% | 240 KB | 0 |
| [davidcollier77-code/Luckypickcanada](https://github.com/davidcollier77-code/Luckypickcanada) | F F D | 314 | 3,114 | 12.0 | 37% | 15% | 98% | 75 KB | 1 |
| [ashivam-dot/creature-receipts](https://github.com/ashivam-dot/creature-receipts) | F F D | 310 | 29,359 | 0.1 | 20% | 0% | – | 109 KB | 0 |
| [Arthur5243/Split.](https://github.com/Arthur5243/Split.) | F F F | 279 | 968 | 0.0 | 0% | 9% | – | 874 KB | 1 |
| [carefulgovernment/HOMFLY](https://github.com/carefulgovernment/HOMFLY) | F F D | 260 | 21,193 | 0.0 | 43% | 0% | – | 41 KB | 0 |
| [birdnofoots/Mi11Pro-Droidspaces-Kernel-KSU](https://github.com/birdnofoots/Mi11Pro-Droidspaces-Kernel-KSU) | F F E | 218 | 2,470 | 0.0 | 58% | 0% | 29% | 44 KB | 0 |
| [Ackerman-00/fedora-nexus](https://github.com/Ackerman-00/fedora-nexus) | F F E | 208 | 4,065 | 0.0 | 29% | 17% | 0% | 145 KB | 0 |
| [davidnoehmke/Shop-V5.1](https://github.com/davidnoehmke/Shop-V5.1) | F F C | 203 | 1,336 | 5.9 | 41% | 0% | 84% | 37 KB | 0 |
| [doublehidenblade/game-dev-central](https://github.com/doublehidenblade/game-dev-central) | F F D | 123 | 7,969 | 9.5 | 17% | 0% | – | 156 KB | 0 |
| [1sl2tp/1988](https://github.com/1sl2tp/1988) | F E E | 106 | 6,916 | 7.6 | 64% | 0% | 76% | 575 KB | 0 |
| [125337/ios](https://github.com/125337/ios) | F F E | 76 | 2,815 | 0.0 | 25% | 11% | 92% | 222 KB | 0 |
| [docker-hardened-images/catalog](https://github.com/docker-hardened-images/catalog) | F F F | 70 | 11,578 | 0.0 | 24% | 0% | – | 20 KB | 252 |
| [a0953883367/wude-ai-stock-v6](https://github.com/a0953883367/wude-ai-stock-v6) | F F B | 58 | 537,619 | 2.0 | 0% | 0% | 97% | 200 KB | 0 |
| [254684589-max/ooglex-site](https://github.com/254684589-max/ooglex-site) | F F E | 56 | 29,122 | 6.8 | 7% | 0% | 86% | 5,592 KB | 1 |
| [Aivoro-Solution/CortexFlow](https://github.com/Aivoro-Solution/CortexFlow) | F F F | 15 | 4,474 | 0.0 | 0% | 0% | – | 30 KB | 0 |
| [beheshti2025hesam-prog/btc_tabdeal_public_test](https://github.com/beheshti2025hesam-prog/btc_tabdeal_public_test) | F F B | 13 | 57,289 | 3.5 | 6% | 0% | 100% | 11 KB | 0 |
| [Daisuke134/life-manager](https://github.com/Daisuke134/life-manager) | F F B | – | – | 71.5 | 24% | – | 92% | 484 KB | 8 |
| [adhithyan15/coding-adventures](https://github.com/adhithyan15/coding-adventures) | F B E | – | – | 69.9 | 90% | 31% | 97% | 10 KB | 1 |
| [DomLynch/RPG-game](https://github.com/DomLynch/RPG-game) | F F A | – | – | 59.8 | 1% | 85% | 90% | 359 KB | 0 |
| [aquaproj/aqua-registry](https://github.com/aquaproj/aqua-registry) | F D F | 0 | 203 | 57.9 | 65% | 50% | – | 22 KB | 387 |
| [bitnami/containers](https://github.com/bitnami/containers) | F F F | 0 | 1,363 | 44.7 | 0% | 0% | – | 75 KB | 4,468 |
| [ai4curation/ai-gene-review](https://github.com/ai4curation/ai-gene-review) | F C E | – | – | 41.9 | 71% | 4% | 86% | 95,965 KB | 24 |
| [brycejmurrin/f1-game](https://github.com/brycejmurrin/f1-game) | F D B | – | – | 39.2 | 66% | 19% | 82% | 589 KB | 0 |
| [bichikim/web](https://github.com/bichikim/web) | F F A | – | – | 34.0 | 38% | 17% | 100% | 308 KB | 9 |
| [critterpass/critterpass](https://github.com/critterpass/critterpass) | F C C | – | – | 30.3 | 71% | 19% | 78% | 1,926 KB | 2 |
| [copse-dev/agent-pane](https://github.com/copse-dev/agent-pane) | F E C | – | – | 28.2 | 51% | 25% | 100% | 318 KB | 1 |
| [a-jay85/IBL5](https://github.com/a-jay85/IBL5) | F D B | – | – | 27.8 | 68% | 48% | 98% | 293 KB | 0 |
| [aburan28/crypto-autoresearcher](https://github.com/aburan28/crypto-autoresearcher) | F F E | – | – | 27.4 | 28% | 50% | 82% | 5,977 KB | 1 |
| [briar-systems/mach](https://github.com/briar-systems/mach) | F F C | 0 | 51,463 | 26.9 | 0% | 0% | 61% | 7 KB | 140 |
| [cehinds/AshenSpire](https://github.com/cehinds/AshenSpire) | F C C | – | – | 26.3 | 71% | 24% | 100% | 3,925 KB | 1 |
| [D-sorganization/UpstreamDrift](https://github.com/D-sorganization/UpstreamDrift) | F B C | – | – | 25.2 | 81% | 11% | 56% | 152 KB | 3 |
| [damianvtran/local-operator-ui](https://github.com/damianvtran/local-operator-ui) | F C C | – | – | 25.0 | 71% | 19% | 99% | 1,771 KB | 26 |
| [ChengshuLi/WorldAtlas](https://github.com/ChengshuLi/WorldAtlas) | F C D | – | – | 17.5 | 73% | 40% | 100% | 2,323 KB | 0 |
| [christianspliid-ui/threadbare](https://github.com/christianspliid-ui/threadbare) | F C B | – | – | 13.7 | 78% | 0% | 78% | 11,946 KB | 0 |
| [dennismueller10x-sudo/vision-universe-research](https://github.com/dennismueller10x-sudo/vision-universe-research) | F E C | – | – | 13.1 | 43% | 62% | 96% | 12,482 KB | 0 |
| [aqm857886159/Nomi](https://github.com/aqm857886159/Nomi) | F B B | – | – | 12.6 | 84% | 33% | 99% | 1,061 KB | 559 |
| [anon987654321/pub4](https://github.com/anon987654321/pub4) | F F D | – | – | 9.0 | 1% | – | 0% | 2,131 KB | 2 |
| [christfriedbalizou/homelab](https://github.com/christfriedbalizou/homelab) | F F D | 0 | 1,213 | 8.9 | 0% | 0% | 78% | 6 KB | 9 |
| [BlueAzur-Hub/erith-ia-memory](https://github.com/BlueAzur-Hub/erith-ia-memory) | F D E | – | – | 6.4 | 69% | 44% | 98% | 3,298 KB | 0 |
| [bemrick2/CollegePrep](https://github.com/bemrick2/CollegePrep) | F E B | – | – | 6.2 | 51% | 45% | 100% | 123 KB | 0 |
| [6-Bit-01/BARCODE-SYSTEM-OVERRIDE](https://github.com/6-Bit-01/BARCODE-SYSTEM-OVERRIDE) | F E E | – | – | 5.8 | 46% | 0% | 100% | 310 KB | 0 |
| [Blackcat-Informatics/purrdf](https://github.com/Blackcat-Informatics/purrdf) | F C C | – | – | 3.7 | 73% | 13% | 65% | 1,072 KB | 48 |
| [bitcoinforu2-ui/Wallet500](https://github.com/bitcoinforu2-ui/Wallet500) | F D C | – | – | 3.6 | 69% | 85% | 85% | 105 KB | 1 |
| [coldshalamov/SpaceFace](https://github.com/coldshalamov/SpaceFace) | F F D | – | – | 3.6 | 34% | 3% | 33% | 4,677 KB | 0 |
| [b7n0de/proofbundle](https://github.com/b7n0de/proofbundle) | F F A | 0 | 87 | 3.5 | 0% | 0% | 100% | 227 KB | 2 |
| [AlecKriebel/Math](https://github.com/AlecKriebel/Math) | F E E | – | – | 3.2 | 45% | 10% | 93% | 102 KB | 0 |
| [DDCoder23/The-last-signal-](https://github.com/DDCoder23/The-last-signal-) | F E C | – | – | 0.8 | 49% | 40% | 64% | 84 KB | 2 |
| [ClassesOver/sm](https://github.com/ClassesOver/sm) | F F D | 0 | 2,009 | 0.5 | 0% | 0% | – | 192 KB | 0 |
| [blackmad/map-recall2](https://github.com/blackmad/map-recall2) | F E D | – | – | 0.2 | 60% | 26% | 18% | 1,851 KB | 0 |
| [darkapoparka/cars](https://github.com/darkapoparka/cars) | F E D | – | – | 0.2 | 50% | 4% | 9% | 573 KB | 0 |
| [devilgest1704/sda-scanner](https://github.com/devilgest1704/sda-scanner) | F B E | – | – | 0.2 | 88% | 16% | 92% | 41 KB | 0 |
| [dossijeo/wild-guardians-africa](https://github.com/dossijeo/wild-guardians-africa) | F C C | – | – | 0.2 | 76% | 54% | 55% | 692 KB | 0 |
| [Balty1991/BETPREDICT](https://github.com/Balty1991/BETPREDICT) | F D E | – | – | 0.1 | 61% | 69% | 91% | 405 KB | 0 |
| [ahmetrasit/prose_generation](https://github.com/ahmetrasit/prose_generation) | F E C | – | – | 0.0 | 47% | 0% | 100% | 465 KB | 1 |
| [akisumann/3210-pokemon](https://github.com/akisumann/3210-pokemon) | F F F | 0 | 23,543 | 0.0 | 0% | 0% | – | 86 KB | 0 |
| [alexshen0125-tech/foodmax-scm-purchasing-prototypes](https://github.com/alexshen0125-tech/foodmax-scm-purchasing-prototypes) | F A E | 0 | 73 | 0.0 | 98% | 98% | 100% | 1,515 KB | 0 |
| [AntPAllen/js-wf](https://github.com/AntPAllen/js-wf) | F D B | – | – | 0.0 | 69% | 78% | 88% | 83 KB | 0 |
| [BaileyPillon/pyrefly-reprise](https://github.com/BaileyPillon/pyrefly-reprise) | F E D | – | – | 0.0 | 59% | 29% | 0% | 6,555 KB | 0 |
| [bartlangelaan/techpref.dev](https://github.com/bartlangelaan/techpref.dev) | F C E | 0 | 13,364 | 0.0 | 73% | 45% | 86% | 14 KB | 0 |
| [benswift/slop-university](https://github.com/benswift/slop-university) | F F D | 0 | 1,571 | 0.0 | 0% | 0% | 100% | 41 KB | 0 |
| [bojieli/OpenTallas](https://github.com/bojieli/OpenTallas) | F F E | – | – | 0.0 | 30% | 100% | 0% | 808 KB | 2 |
| [Carnot-EBM/carnot-ebm](https://github.com/Carnot-EBM/carnot-ebm) | F C E | – | – | 0.0 | 88% | 73% | 0% | 561 KB | 2 |
| [chaotic-aur/packages](https://github.com/chaotic-aur/packages) | F F F | 0 | 362 | 0.0 | 0% | 0% | – | 53 KB | 427 |
| [coffeethencode/masstech-notices-evidence](https://github.com/coffeethencode/masstech-notices-evidence) | F A F | 0 | 0 | 0.0 | 97% | 94% | – | 60 KB | 0 |
| [danielzh1nt0/ipanema-analysis](https://github.com/danielzh1nt0/ipanema-analysis) | F E C | – | – | 0.0 | 64% | 4% | 93% | 194 KB | 0 |
| [davidburgoscarpeno/minepedia](https://github.com/davidburgoscarpeno/minepedia) | F F F | 0 | 3,314 | 0.0 | 0% | 0% | – | 129 KB | 0 |
| [dead-baron/city-life-auto](https://github.com/dead-baron/city-life-auto) | F C D | – | – | 0.0 | 71% | 0% | – | 322 KB | 0 |
| [derekbreden/homesodamachine](https://github.com/derekbreden/homesodamachine) | F E E | – | – | 0.0 | 44% | 35% | 22% | 21,464 KB | 1 |
| [Dicklesworthstone/mcp_agent_mail_rust](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) | F F D | 0 | 3,433 | 0.0 | 32% | 0% | 1% | 3,751 KB | 186 |
| [Ding-Ding-Projects/BambuStudio](https://github.com/Ding-Ding-Projects/BambuStudio) | F E E | – | – | 0.0 | 60% | 0% | 88% | 8,278 KB | 0 |
| [dnilgis/bids](https://github.com/dnilgis/bids) | F A C | – | – | 0.0 | 91% | 93% | 52% | 1,464 KB | 0 |
<!-- END GENERATED -->

## Running it

The list is kept up to date by two scripts, each of which pulls, runs, commits and pushes:

```sh
scripts/weekly.sh     # find new candidates and screen them (steps 1 and 2)
scripts/hourly.sh     # recheck waiting repos (steps 3 and 4) and measure the listed ones
```

Classifying newly listed repos is run by hand with `python -m asf classify`, which needs the `claude` CLI signed in;
[context/classify-workflow.md](context/classify-workflow.md) has the steps.

You need Python 3.11 or newer, git, and a GitHub token (`GH_TOKEN`, or a signed-in `gh`). There are no other
dependencies. [context/](context/index.md) has the details for running and maintaining it, written for people and
coding agents alike.

## License

The code is [MIT](LICENSE). The data and reports are [CC BY 4.0](LICENSE-DATA).
