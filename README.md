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
_122 repos, last measured 2026-10-09. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

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
| [arul28/ADE](https://github.com/arul28/ADE) | B F B | 23,381 | 28,223 | 11.2 | 39% | 0% | 84% | 2,711 KB | 114 |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 22,518 | 23,472 | 0.0 | 71% | 45% | – | 225 KB | 0 |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 21,783 | 23,643 | 88.1 | 26% | 51% | 76% | 340 KB | 45 |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | B E B | 20,463 | 30,341 | 28.1 | 46% | 35% | 79% | 1,966 KB | 1,354 |
| [agentmuxai/agentmux](https://github.com/agentmuxai/agentmux) | C D C | 19,332 | 27,046 | 45.2 | 60% | 37% | 89% | 314 KB | 19 |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 17,930 | 38,226 | 23.8 | 26% | 6% | 97% | 236 KB | 17 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 17,481 | 52,564 | 170 | 41% | 8% | 89% | 2,294 KB | 3 |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | C D A | 17,391 | 44,870 | 15.8 | 68% | 0% | 90% | 94 KB | 15 |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | C F B | 17,305 | 33,861 | 25.7 | 29% | 21% | 92% | 1,228 KB | 88 |
| [joshualeestone/kosmos](https://github.com/joshualeestone/kosmos) | C E B | 16,925 | 24,015 | 52.7 | 58% | 18% | 98% | 1,433 KB | 1 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | C F C | 16,915 | 39,874 | 89.1 | 31% | 15% | 50% | 314 KB | 3 |
| [Maurdekye/orgtree](https://github.com/Maurdekye/orgtree) | C D D | 16,892 | 32,042 | 0.0 | 66% | 7% | 0% | 2,025 KB | 112 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 16,705 | 32,625 | 56.3 | 60% | 58% | 97% | 768 KB | 6,222 |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C E A | 16,691 | 27,961 | 32.9 | 58% | 21% | 93% | 138 KB | 4 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 16,308 | 17,462 | 4.9 | 0% | 0% | 96% | 355 KB | 126 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 15,003 | 16,557 | 36.0 | 0% | 5% | 92% | 66 KB | 56 |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C E A | 13,728 | 42,367 | 21.8 | 80% | 0% | 90% | 100 KB | 103 |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 13,658 | 27,953 | 12.3 | 86% | 41% | 80% | 77 KB | 3 |
| [melodic-software/claude-code-plugins](https://github.com/melodic-software/claude-code-plugins) | C F C | 13,600 | 65,004 | 49.5 | 28% | 0% | 98% | 239 KB | 23 |
| [marcioapm/dude](https://github.com/marcioapm/dude) | C F B | 11,245 | 14,780 | 2.8 | 3% | 0% | 83% | 108 KB | 1 |
| [coder/xum](https://github.com/coder/xum) | C E B | 10,589 | 18,669 | 34.4 | 42% | 15% | 99% | 940 KB | 2,051 |
| [github/gh-aw](https://github.com/github/gh-aw) | C E C | 10,523 | 42,989 | 27.6 | 50% | 48% | 62% | 229 KB | 5,369 |
| [prime-radiant-inc/evener](https://github.com/prime-radiant-inc/evener) | C F A | 10,364 | 19,821 | 69.0 | 43% | 12% | 98% | 306 KB | 171 |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 7,164 | 10,597 | 24.2 | 9% | 0% | 97% | 489 KB | 27 |
| [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) | D F A | 6,973 | 14,334 | 8.0 | 53% | 5% | 98% | 202 KB | 2,249 |
| [scode/farhelm](https://github.com/scode/farhelm) | D F B | 6,444 | 20,849 | 40.0 | 4% | 0% | 97% | 1,486 KB | 0 |
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
| [artificial-hedge/dipcatcher](https://github.com/artificial-hedge/dipcatcher) | A F D | 72,280 | 1,289,855 | 103 | 71% | 7% | 29% | 469 KB | 0 |
| [lamontaes/Political-Game-Git](https://github.com/lamontaes/Political-Game-Git) | A F D | 65,753 | 310,615 | 97.5 | 41% | 1% | 27% | 10,357 KB | 0 |
| [OreStudio/OreStudio](https://github.com/OreStudio/OreStudio) | A F C | 64,285 | 155,509 | 33.5 | 23% | 52% | 75% | 9,839 KB | 28 |
| [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | A E B | 58,241 | 72,826 | 67.8 | 53% | 0% | 100% | 971 KB | 7,111 |
| [workingdir/ornadb](https://github.com/workingdir/ornadb) | A F D | 56,205 | 75,505 | 128 | 61% | 1% | 8% | 1,862 KB | 5 |
| [ubugeeei-prod/vize](https://github.com/ubugeeei-prod/vize) | A D A | 51,232 | 144,674 | 54.4 | 69% | 20% | 94% | 300 KB | 902 |
| [metasequoiaime/msime](https://github.com/metasequoiaime/msime) | A B B | 50,506 | 72,974 | 214 | 88% | 14% | 100% | 488 KB | 593 |
| [skmtmst/line-harness-oss](https://github.com/skmtmst/line-harness-oss) | A F B | 46,287 | 112,840 | 41.5 | 37% | 29% | 100% | 4,345 KB | 0 |
| [kirklandsig/halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | A D E | 46,080 | 87,344 | 9.2 | 67% | 10% | 100% | 371 KB | 45 |
| [UnknownAlienHuman/eliot-memory-os](https://github.com/UnknownAlienHuman/eliot-memory-os) | A F D | 45,874 | 82,609 | 125 | 54% | 0% | 0% | 1,898 KB | 0 |
| [evgunter/cad](https://github.com/evgunter/cad) | A B B | 43,573 | 88,994 | 75.2 | 89% | 40% | 100% | 703 KB | 0 |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 42,820 | 1,420,889 | 75.4 | 10% | 16% | 46% | 3,975 KB | 1 |
| [everruns/everruns](https://github.com/everruns/everruns) | A F C | 42,671 | 69,170 | 32.1 | 33% | 55% | 93% | 157 KB | 54 |
| [EffortlessMetrics/ripr-swarm](https://github.com/EffortlessMetrics/ripr-swarm) | A C D | 41,909 | 98,923 | 39.6 | 78% | 38% | 95% | 1,975 KB | 0 |
| [Smarter-Poker/Smarter-Poker-Club-Arena](https://github.com/Smarter-Poker/Smarter-Poker-Club-Arena) | B E B | 37,518 | 303,917 | 73.3 | 58% | 56% | 100% | 2,646 KB | 0 |
| [Oteryn/Oteryn-Game](https://github.com/Oteryn/Oteryn-Game) | B E C | 33,233 | 2,133,161 | 38.8 | 70% | 0% | 100% | 485 KB | 0 |
| [moxnixmdj/verification-capsule-runner](https://github.com/moxnixmdj/verification-capsule-runner) | B F D | 32,427 | 145,131 | 39.3 | 44% | 2% | 13% | 305 KB | 0 |
| [objectstack-ai/objectstack](https://github.com/objectstack-ai/objectstack) | B C B | 29,919 | 45,478 | 87.8 | 80% | 39% | 100% | 2,308 KB | 70 |
| [6ZoSo9/void-node](https://github.com/6ZoSo9/void-node) | B F E | 29,722 | 42,992 | 33.5 | 33% | 49% | 100% | 3,762 KB | 0 |
| [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite) | B C B | 28,283 | 39,695 | 61.1 | 70% | 48% | 92% | 1,902 KB | 416 |
| [AlexanderMattTurner/agent-glovebox](https://github.com/AlexanderMattTurner/agent-glovebox) | B E A | 25,751 | 56,590 | 54.4 | 41% | 21% | 99% | 161 KB | 67 |
| [buster14a/buster](https://github.com/buster14a/buster) | B F B | 25,194 | 76,080 | 50.4 | 16% | 28% | 99% | 3,137 KB | 0 |
| [lazyxu/xdrive](https://github.com/lazyxu/xdrive) | B F B | 23,893 | 30,887 | 41.1 | 3% | 13% | 94% | 272 KB | 0 |
| [Hanz0Hatt0r1/nfs-shift-decompilation](https://github.com/Hanz0Hatt0r1/nfs-shift-decompilation) | B E B | 23,551 | 46,578 | 55.6 | 56% | 19% | 100% | 227 KB | 1 |
| [tokuhirom/mutsu](https://github.com/tokuhirom/mutsu) | B E E | 22,140 | 52,848 | 103 | 47% | 8% | 100% | 1,579 KB | 27 |
| [hashgraph-online/hol-guard](https://github.com/hashgraph-online/hol-guard) | B E B | 21,993 | 91,982 | 26.3 | 43% | 52% | 94% | 1,491 KB | 836 |
| [JovieInc/Jovie](https://github.com/JovieInc/Jovie) | B E A | 21,630 | 69,054 | 102 | 50% | 6% | 91% | 313 KB | 1 |
| [Raynos/project-wildshard-singleplayer](https://github.com/Raynos/project-wildshard-singleplayer) | B F C | 21,468 | 631,834 | 0.0 | 82% | 0% | 59% | 92 KB | 0 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | B F D | 21,183 | 31,200 | 27.4 | 22% | 8% | 0% | 546 KB | 41,747 |
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
| [agentydragon/ducktape](https://github.com/agentydragon/ducktape) | D E B | 8,459 | 21,136 | 109 | 58% | 29% | 99% | 163 KB | 10 |
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
