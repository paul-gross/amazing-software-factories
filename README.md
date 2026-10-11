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
is only about software factories, so only the first two are listed and measured. Until a repo has been read, it isn't
shown.

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
_122 repos, last measured 2026-10-11. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (47)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 110,458 | 126,941 | 46.6 | 12% | 15% | 97% | 2,582 KB | 1,737 |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 72,907 | 178,176 | 0.2 | 59% | 12% | 27% | 1,271 KB | 431 |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A E B | 69,369 | 129,090 | 31.0 | 78% | 22% | 98% | 220 KB | 0 |
| [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) | A C C | 45,843 | 87,580 | 32.8 | 75% | 38% | 69% | 3,823 KB | 1,220 |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A C C | 43,215 | 62,387 | 54.3 | 73% | 17% | 100% | 665 KB | 14 |
| [wangbinquan/agent-workflow](https://github.com/wangbinquan/agent-workflow) | B B D | 24,416 | 87,427 | 0.0 | 87% | 74% | 47% | 613 KB | 57 |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 22,518 | 23,472 | 0.0 | 71% | 45% | – | 225 KB | 0 |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 22,378 | 48,075 | 14.1 | 77% | 0% | 99% | 94 KB | 15 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 22,093 | 35,324 | 132 | 66% | 55% | 100% | 3,079 KB | 1 |
| [Maurdekye/orgtree](https://github.com/Maurdekye/orgtree) | B D D | 21,533 | 32,013 | 0.0 | 62% | 29% | 0% | 2,025 KB | 128 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | C F B | 19,600 | 25,339 | 13.9 | 18% | 14% | 94% | 239 KB | 74,293 |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C E A | 19,053 | 30,138 | 32.2 | 62% | 23% | 96% | 138 KB | 4 |
| [joshualeestone/kosmos](https://github.com/joshualeestone/kosmos) | C D B | 18,546 | 26,323 | 50.0 | 67% | 15% | 100% | 5,355 KB | 1 |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 18,268 | 22,674 | 85.1 | 23% | 50% | 76% | 340 KB | 48 |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | C F B | 17,305 | 33,861 | 25.7 | 29% | 21% | 92% | 1,228 KB | 88 |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | C F C | 16,915 | 39,874 | 89.1 | 31% | 15% | 50% | 314 KB | 3 |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 16,550 | 37,878 | 23.0 | 37% | 0% | 94% | 434 KB | 17 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 15,555 | 31,767 | 53.4 | 64% | 70% | 100% | 768 KB | 6,233 |
| [coder/xum](https://github.com/coder/xum) | C E B | 14,444 | 17,987 | 33.7 | 45% | 23% | 100% | 953 KB | 2,051 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F C | 14,389 | 18,621 | 35.0 | 0% | 32% | 67% | 66 KB | 59 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 13,877 | 43,624 | 164 | 49% | 11% | 89% | 2,294 KB | 3 |
| [agentmuxai/agentmux](https://github.com/agentmuxai/agentmux) | C E C | 13,826 | 26,334 | 43.5 | 54% | 38% | 97% | 316 KB | 19 |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C E A | 13,728 | 42,367 | 21.8 | 80% | 0% | 90% | 100 KB | 103 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 12,185 | 17,462 | 4.8 | 0% | 14% | 96% | 355 KB | 126 |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 11,818 | 25,850 | 12.3 | 87% | 30% | 80% | 77 KB | 4 |
| [melodic-software/claude-code-plugins](https://github.com/melodic-software/claude-code-plugins) | D F C | 9,125 | 52,125 | 48.2 | 28% | 0% | 100% | 239 KB | 23 |
| [marcioapm/dude](https://github.com/marcioapm/dude) | D F B | 8,394 | 14,543 | 2.4 | 3% | 0% | 80% | 1,179 KB | 1 |
| [scode/farhelm](https://github.com/scode/farhelm) | D F B | 8,321 | 20,649 | 39.7 | 4% | 8% | 97% | 1,525 KB | 0 |
| [prime-radiant-inc/evener](https://github.com/prime-radiant-inc/evener) | D F A | 7,939 | 18,947 | 68.2 | 21% | 12% | 98% | 308 KB | 171 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) | D F A | 5,840 | 14,739 | 7.5 | 52% | 5% | 99% | 201 KB | 2,254 |
| [bastani-inc/atomic](https://github.com/bastani-inc/atomic) | D F B | 5,479 | 7,140 | 13.2 | 4% | 15% | 99% | 534 KB | 856 |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 4,965 | 9,340 | 24.1 | 0% | 0% | 100% | 489 KB | 27 |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 4,727 | 23,493 | 0.2 | 68% | 0% | 86% | 1,449 KB | 1,090 |
| [cristicretu/diri](https://github.com/cristicretu/diri) | E F D | 3,853 | 12,334 | 14.7 | 0% | 0% | 50% | 547 KB | 431 |
| [getpaseo/paseo](https://github.com/getpaseo/paseo) | E E B | 3,408 | 4,889 | 12.8 | 49% | 20% | 79% | 1,213 KB | 20,421 |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,987 | 7,020 | 0.0 | 2% | 0% | 33% | 397 KB | 455 |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,263 | 16,683 | 0.0 | 3% | 0% | – | 189 KB | 26 |
| [razzant/claudexor](https://github.com/razzant/claudexor) | E F B | 2,103 | 7,464 | 2.0 | 0% | 0% | 87% | 298 KB | 501 |
| [receptron/mulmoterminal](https://github.com/receptron/mulmoterminal) | E F A | 1,438 | 3,639 | 19.9 | 33% | 0% | 99% | 113 KB | 238 |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 466 | 2,166 | 0.2 | 38% | 0% | 3% | 904 KB | 1,261 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 365 | 3,498 | 7.4 | 0% | 0% | 81% | 71 KB | 4 |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 30 | 757 | 12.0 | 25% | 0% | 98% | 174 KB | 213 |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 26.4 | 46% | 33% | 89% | 1,966 KB | 1,358 |
| [github/gh-aw](https://github.com/github/gh-aw) | F E B | – | – | 26.3 | 48% | 58% | 75% | 232 KB | 5,379 |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,803 | 6.7 | 0% | 0% | 95% | 150 KB | 346 |

### Built by an assembly line (75)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [stella/stella](https://github.com/stella/stella) | A B B | 99,456 | 127,938 | 72.0 | 81% | 79% | 100% | 575 KB | 259 |
| [kaeawc/auto-mobile](https://github.com/kaeawc/auto-mobile) | A E B | 81,759 | 112,374 | 90.0 | 47% | 47% | 81% | 422 KB | 51 |
| [artificial-hedge/dipcatcher](https://github.com/artificial-hedge/dipcatcher) | A C D | 67,627 | 1,284,334 | 102 | 82% | 8% | 33% | 469 KB | 0 |
| [Oteryn/Oteryn-Game](https://github.com/Oteryn/Oteryn-Game) | A C C | 66,864 | 2,124,641 | 38.8 | 71% | 0% | 100% | 535 KB | 0 |
| [kirklandsig/halo2-decompiled](https://github.com/kirklandsig/halo2-decompiled) | A D E | 61,974 | 84,846 | 8.4 | 70% | 32% | 100% | 372 KB | 54 |
| [workingdir/ornadb](https://github.com/workingdir/ornadb) | A F D | 56,205 | 75,505 | 128 | 61% | 1% | 8% | 1,862 KB | 5 |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 55,106 | 1,424,223 | 73.3 | 8% | 14% | 67% | 3,975 KB | 1 |
| [BuilderIO/agent-native](https://github.com/BuilderIO/agent-native) | A E B | 54,596 | 79,812 | 64.8 | 52% | 0% | 98% | 985 KB | 7,120 |
| [ubugeeei-prod/vize](https://github.com/ubugeeei-prod/vize) | A D A | 51,232 | 144,674 | 54.4 | 69% | 20% | 94% | 300 KB | 902 |
| [UnknownAlienHuman/eliot-memory-os](https://github.com/UnknownAlienHuman/eliot-memory-os) | A F D | 45,874 | 82,609 | 125 | 54% | 0% | 0% | 1,898 KB | 0 |
| [evgunter/cad](https://github.com/evgunter/cad) | A C B | 41,176 | 90,527 | 71.6 | 80% | 41% | 100% | 715 KB | 0 |
| [EffortlessMetrics/ripr-swarm](https://github.com/EffortlessMetrics/ripr-swarm) | A B D | 40,500 | 100,918 | 39.0 | 82% | 47% | 92% | 1,975 KB | 0 |
| [Smarter-Poker/Smarter-Poker-Club-Arena](https://github.com/Smarter-Poker/Smarter-Poker-Club-Arena) | B E B | 37,518 | 303,917 | 73.3 | 58% | 56% | 100% | 2,646 KB | 0 |
| [everruns/everruns](https://github.com/everruns/everruns) | B F C | 35,841 | 64,089 | 30.4 | 30% | 29% | 88% | 157 KB | 56 |
| [metasequoiaime/msime](https://github.com/metasequoiaime/msime) | B A B | 35,115 | 62,087 | 206 | 91% | 14% | 77% | 516 KB | 627 |
| [lazyxu/xdrive](https://github.com/lazyxu/xdrive) | B F B | 30,775 | 39,514 | 36.0 | 14% | 33% | 80% | 288 KB | 0 |
| [6ZoSo9/void-node](https://github.com/6ZoSo9/void-node) | B F E | 30,655 | 36,549 | 33.1 | 32% | 43% | 97% | 3,761 KB | 0 |
| [buster14a/buster](https://github.com/buster14a/buster) | B F B | 29,541 | 85,225 | 47.0 | 16% | 23% | 94% | 3,182 KB | 0 |
| [LTplus-AG/ifc-lite](https://github.com/LTplus-AG/ifc-lite) | B C B | 28,163 | 39,732 | 59.9 | 73% | 44% | 99% | 1,902 KB | 418 |
| [objectstack-ai/objectstack](https://github.com/objectstack-ai/objectstack) | B B B | 24,031 | 41,976 | 84.8 | 82% | 37% | 100% | 2,308 KB | 70 |
| [rubys/roundhouse](https://github.com/rubys/roundhouse) | B F C | 23,622 | 31,159 | 13.3 | 38% | 45% | 75% | 442 KB | 432 |
| [carrick-sh/carrick](https://github.com/carrick-sh/carrick) | B F C | 22,396 | 69,896 | 1.8 | 24% | 2% | 76% | 558 KB | 2 |
| [tokuhirom/mutsu](https://github.com/tokuhirom/mutsu) | B E E | 22,140 | 52,848 | 103 | 47% | 8% | 100% | 1,579 KB | 27 |
| [Hanz0Hatt0r1/nfs-shift-decompilation](https://github.com/Hanz0Hatt0r1/nfs-shift-decompilation) | B E B | 21,808 | 49,661 | 52.7 | 49% | 36% | 100% | 227 KB | 1 |
| [JovieInc/Jovie](https://github.com/JovieInc/Jovie) | B E A | 21,630 | 69,054 | 102 | 50% | 6% | 91% | 313 KB | 1 |
| [tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) | B F D | 21,183 | 31,200 | 27.4 | 22% | 8% | 0% | 546 KB | 41,747 |
| [hashgraph-online/hol-guard](https://github.com/hashgraph-online/hol-guard) | B F B | 21,014 | 92,481 | 24.0 | 44% | 52% | 96% | 1,572 KB | 845 |
| [AlexanderMattTurner/agent-glovebox](https://github.com/AlexanderMattTurner/agent-glovebox) | B F A | 20,609 | 45,826 | 51.7 | 36% | 21% | 95% | 161 KB | 67 |
| [FueledByChai/fueledbychai-rs](https://github.com/FueledByChai/fueledbychai-rs) | C D D | 19,932 | 27,322 | 4.8 | 65% | 11% | – | 101 KB | 1 |
| [tioperfumes07/IH35-TMS](https://github.com/tioperfumes07/IH35-TMS) | C D C | 19,044 | 34,645 | 155 | 62% | 19% | 78% | 399 KB | 0 |
| [uttrflow/uttrflow-swift](https://github.com/uttrflow/uttrflow-swift) | C E A | 17,020 | 38,552 | 111 | 59% | 23% | 100% | 208 KB | 6 |
| [pch/rawmakase](https://github.com/pch/rawmakase) | C E E | 16,187 | 22,390 | 10.8 | 42% | 17% | 97% | 221 KB | 938 |
| [kuu-lab/swifty-kotlin](https://github.com/kuu-lab/swifty-kotlin) | C F B | 15,836 | 30,037 | 52.0 | 17% | 6% | 100% | 340 KB | 2 |
| [max-sixty/leaf](https://github.com/max-sixty/leaf) | C D B | 15,665 | 29,962 | 51.2 | 63% | 57% | 97% | 393 KB | 5 |
| [web-everything/web-everything](https://github.com/web-everything/web-everything) | C E B | 14,722 | 29,208 | 90.8 | 48% | 37% | 99% | 519 KB | 0 |
| [evilsysadmin/chess-studio](https://github.com/evilsysadmin/chess-studio) | C F B | 14,553 | 55,288 | 130 | 2% | 41% | 92% | 256 KB | 1 |
| [openclaw/openclaw-enterprise](https://github.com/openclaw/openclaw-enterprise) | C C C | 14,204 | 20,909 | 47.9 | 73% | 34% | 100% | 519 KB | 389 |
| [joefrancisGA/ArchLucid](https://github.com/joefrancisGA/ArchLucid) | C D D | 12,902 | 23,388 | 50.5 | 67% | 14% | 10% | 5,075 KB | 0 |
| [JakeChampion/lang](https://github.com/JakeChampion/lang) | C C C | 12,473 | 66,934 | 60.1 | 77% | 14% | 100% | 988 KB | 1 |
| [moxnixmdj/verification-capsule-runner](https://github.com/moxnixmdj/verification-capsule-runner) | C F D | 11,579 | 137,335 | 37.8 | 31% | 2% | 24% | 305 KB | 0 |
| [Open-MBEE/OpenSysML](https://github.com/Open-MBEE/OpenSysML) | D F B | 9,121 | 48,054 | 26.2 | 38% | 42% | 98% | 214 KB | 37 |
| [agentydragon/ducktape](https://github.com/agentydragon/ducktape) | D E B | 8,654 | 20,846 | 104 | 50% | 30% | 98% | 163 KB | 10 |
| [HectorBailey/byte-tactics](https://github.com/HectorBailey/byte-tactics) | D F E | 8,562 | 59,022 | 110 | 72% | 4% | 100% | 505 KB | 33 |
| [vznjs/vx](https://github.com/vznjs/vx) | D F C | 7,796 | 15,246 | 107 | 58% | 0% | 96% | 129 KB | 6 |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | D C B | 7,669 | 15,887 | 35.7 | 76% | 21% | 96% | 1,568 KB | 60,400 |
| [storytree-ai/storytree](https://github.com/storytree-ai/storytree) | D A B | 7,550 | 37,557 | 35.9 | 90% | 34% | 85% | 61 KB | 0 |
| [melian-agent/melian](https://github.com/melian-agent/melian) | D F C | 7,202 | 20,815 | 3.3 | 9% | 0% | 100% | 98 KB | 0 |
| [mboogerd/computenet](https://github.com/mboogerd/computenet) | D E B | 6,711 | 12,502 | 19.4 | 57% | 38% | 79% | 388 KB | 0 |
| [Dicklesworthstone/franken_engine](https://github.com/Dicklesworthstone/franken_engine) | D F D | 6,552 | 11,611 | 0.0 | 20% | 0% | 20% | 7,071 KB | 31 |
| [kentcdodds/kody](https://github.com/kentcdodds/kody) | D E A | 6,279 | 10,164 | 18.2 | 56% | 41% | 100% | 125 KB | 759 |
| [Dicklesworthstone/annus-mirabilis.com](https://github.com/Dicklesworthstone/annus-mirabilis.com) | D F D | 6,039 | 11,523 | 0.0 | 51% | 0% | 0% | 1,235 KB | 7 |
| [ScriptedAlchemy/tracedecay](https://github.com/ScriptedAlchemy/tracedecay) | D E C | 5,918 | 21,991 | 48.7 | 48% | 16% | 71% | 1,977 KB | 80 |
| [postmark-town/postmark](https://github.com/postmark-town/postmark) | E F E | 4,402 | 155,937 | 23.4 | 40% | 28% | 100% | 18,331 KB | 19 |
| [Nishfleet/0509](https://github.com/Nishfleet/0509) | E E A | 4,331 | 10,333 | 66.6 | 65% | 18% | 98% | 79 KB | 0 |
| [WangPantopus/skinny-pantopus](https://github.com/WangPantopus/skinny-pantopus) | E E C | 2,830 | 7,100 | 72.6 | 58% | 1% | 81% | 598 KB | 0 |
| [keeptxred/TexasDefined](https://github.com/keeptxred/TexasDefined) | E F E | 2,589 | 6,275 | 46.9 | 28% | 40% | 93% | 628 KB | 1 |
| [gunb-ai/gunbc](https://github.com/gunb-ai/gunbc) | E B E | 2,392 | 55,850 | 65.4 | 88% | 32% | 80% | 1,989 KB | 4 |
| [chidionyema/idp](https://github.com/chidionyema/idp) | E F B | 1,255 | 3,922 | 79.1 | 12% | 0% | 99% | 2,933 KB | 1 |
| [Fronthub-pl/arrowz](https://github.com/Fronthub-pl/arrowz) | F F B | 860 | 5,325 | 5.2 | 0% | 10% | 100% | 122 KB | 0 |
| [makr-code/ThemisDB](https://github.com/makr-code/ThemisDB) | F F E | 706 | 233,344 | 12.2 | 0% | 17% | 75% | 54 KB | 9 |
| [orbi-build/orbi-website](https://github.com/orbi-build/orbi-website) | F F C | 678 | 2,426 | 16.9 | 18% | 0% | 94% | 79 KB | 0 |
| [day8/re-frame2](https://github.com/day8/re-frame2) | F E C | 470 | 18,994 | 45.3 | 53% | 0% | 100% | 390 KB | 51 |
| [garden-co/jazz](https://github.com/garden-co/jazz) | F F B | 125 | 620 | 19.8 | 0% | 0% | 92% | 659 KB | 204 |
| [lamontaes/Political-Game-Git](https://github.com/lamontaes/Political-Game-Git) | F F D | – | – | 97.3 | 7% | 55% | 36% | 10,357 KB | 0 |
| [mas-bandwidth/nova-tools](https://github.com/mas-bandwidth/nova-tools) | F F B | 0 | 111 | 71.6 | 0% | 0% | 76% | 232 KB | 6 |
| [ravelius/Matkakirja](https://github.com/ravelius/Matkakirja) | F E D | – | – | 58.2 | 56% | 38% | 100% | 8,133 KB | 0 |
| [justinlindh/human-in-the-loop](https://github.com/justinlindh/human-in-the-loop) | F F B | – | – | 49.9 | 24% | 23% | 99% | 138 KB | 2 |
| [skmtmst/line-harness-oss](https://github.com/skmtmst/line-harness-oss) | F F B | – | – | 41.1 | 33% | 100% | 100% | 4,345 KB | 0 |
| [CambrianTech/continuum](https://github.com/CambrianTech/continuum) | F F C | – | – | 30.2 | 58% | 0% | 100% | 633 KB | 32 |
| [OreStudio/OreStudio](https://github.com/OreStudio/OreStudio) | F F C | – | – | 29.8 | 0% | 70% | 81% | 9,839 KB | 28 |
| [OneUptime/oneuptime](https://github.com/OneUptime/oneuptime) | F C B | – | – | 27.2 | 70% | 88% | 100% | 668 KB | 7,725 |
| [wieslawsoltes/SharpForge](https://github.com/wieslawsoltes/SharpForge) | F F C | 0 | 672,791 | 26.0 | 35% | 0% | 100% | 120 KB | 20 |
| [edsaperia/witch](https://github.com/edsaperia/witch) | F E C | – | – | 20.2 | 43% | 33% | 98% | 128 KB | 0 |
| [kierandrewett/gnoblin](https://github.com/kierandrewett/gnoblin) | F E C | – | – | 1.5 | 70% | 0% | 100% | 645 KB | 5 |
| [Raynos/project-wildshard-singleplayer](https://github.com/Raynos/project-wildshard-singleplayer) | F E C | – | – | 0.0 | 58% | 91% | 71% | 109 KB | 0 |
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
