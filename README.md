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
_206 repos, last measured 2026-10-12. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (206)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 110,458 | 126,941 | 46.6 | 12% | 15% | 97% | 2,582 KB | 1,737 |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 83,969 | 135,581 | 31.0 | 73% | 42% | 98% | 220 KB | 1 (+1) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A E D | 72,907 | 178,176 | 0.2 | 59% | 12% | 27% | 1,271 KB | 431 |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 52,764 | 2,208,426 | 75.4 | 4% | 16% | 36% | 3,975 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A D B | 51,865 | 64,067 | 18.2 | 61% | 47% | 99% | 592 KB | 9 |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | A C C | 51,503 | 77,356 | 0.2 | 74% | 24% | 82% | 261 KB | 0 |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A E A | 47,027 | 63,596 | 68.3 | 66% | 56% | 100% | 154 KB | 14 (+0) |
| [autonomous-ai/openharness](https://github.com/autonomous-ai/openharness) | A C C | 45,843 | 87,580 | 32.8 | 75% | 38% | 69% | 3,823 KB | 1,220 |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A C C | 43,215 | 62,387 | 54.3 | 73% | 17% | 100% | 665 KB | 14 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | A C D | 42,092 | 858,793 | 0.0 | 76% | 38% | 0% | 3,283 KB | 1 |
| [UnknownAlienHuman/eliot-swarm-controller](https://github.com/UnknownAlienHuman/eliot-swarm-controller) | A F E | 40,407 | 60,230 | 0.2 | 66% | 0% | 88% | 280 KB | 0 |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 40,143 | 45,977 | 20.6 | 46% | 6% | 100% | 709 KB | 1 (+1) |
| [tale-project/tale](https://github.com/tale-project/tale) | B C C | 38,447 | 57,680 | 25.8 | 73% | 26% | 55% | 2,567 KB | 33 |
| [csitea/csi-spl](https://github.com/csitea/csi-spl) | B B B | 38,247 | 56,053 | 0.0 | 84% | 48% | 96% | 150 KB | 1 |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B E C | 34,623 | 60,291 | 36.5 | 58% | 73% | 79% | 2,306 KB | 4 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B D B | 33,549 | 177,930 | 26.6 | 67% | 32% | 86% | 1,403 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | B E B | 32,115 | 45,749 | 0.0 | 52% | 18% | 86% | 608 KB | 1 |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | B D B | 31,911 | 45,237 | 69.7 | 67% | 7% | 99% | 569 KB | 0 |
| [kontourai/station](https://github.com/kontourai/station) | B D B | 30,940 | 58,270 | 29.4 | 64% | 10% | 97% | 941 KB | 3 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | B C B | 29,723 | 64,358 | 22.7 | 72% | 11% | 96% | 375 KB | 9 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | B E A | 28,449 | 53,060 | 15.7 | 78% | 0% | 97% | 94 KB | 16 (+1) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B C D | 26,462 | 48,295 | 0.0 | 78% | 48% | 44% | 248 KB | 0 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 25,266 | 25,763 | 0.0 | 76% | 42% | – | 226 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B D A | 25,132 | 57,183 | 35.9 | 64% | 45% | 100% | 112 KB | 1 |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | B B B | 25,049 | 28,484 | 11.1 | 84% | 57% | 86% | 421 KB | 0 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F C | 24,396 | 48,623 | 87.4 | 37% | 15% | 50% | 314 KB | 3 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 24,013 | 32,549 | 31.8 | 72% | 18% | 95% | 599 KB | 22 |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 23,195 | 48,808 | 30.1 | 51% | 10% | 95% | 54 KB | 0 |
| [wangbinquan/agent-workflow](https://github.com/wangbinquan/agent-workflow) | B B D | 22,229 | 83,889 | 0.0 | 83% | 58% | 45% | 671 KB | 57 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 22,100 | 36,363 | 0.0 | 68% | 58% | – | 1,189 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 22,093 | 35,324 | 132 | 66% | 55% | 100% | 3,079 KB | 1 |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 21,696 | 32,654 | 24.5 | 34% | 26% | 98% | 1,245 KB | 89 (+1) |
| [Maurdekye/orgtree](https://github.com/Maurdekye/orgtree) | B D D | 21,533 | 32,013 | 0.0 | 62% | 29% | 0% | 2,025 KB | 128 |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 21,495 | 24,581 | 21.5 | 78% | 51% | 73% | 364 KB | 9 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | B F F | 21,231 | 226,755 | 0.0 | 52% | 8% | – | 8,190 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B E A | 21,227 | 35,532 | 0.1 | 57% | 3% | 100% | 163 KB | 9 |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | B E F | 20,583 | 347,265 | 6.8 | 55% | 9% | – | 331 KB | 4 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B D B | 20,082 | 27,762 | 11.3 | 63% | 40% | 98% | 688 KB | 9 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | C F C | 19,781 | 46,415 | 20.5 | 67% | 0% | 94% | 100 KB | 110 (+7) |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | C F B | 19,600 | 25,339 | 13.9 | 18% | 14% | 94% | 239 KB | 74,293 |
| [ste-bah/archon-cli](https://github.com/ste-bah/archon-cli) | C E D | 19,465 | 28,518 | 0.0 | 56% | 42% | 34% | 61 KB | 7 |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C E A | 19,053 | 30,138 | 32.2 | 62% | 23% | 96% | 138 KB | 4 |
| [joshualeestone/kosmos](https://github.com/joshualeestone/kosmos) | C D B | 18,546 | 26,323 | 50.0 | 67% | 15% | 100% | 5,355 KB | 1 |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 18,268 | 22,674 | 85.1 | 23% | 50% | 76% | 340 KB | 48 |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | C F C | 17,791 | 36,662 | 1.0 | 38% | 0% | 72% | 290 KB | 0 |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E D | 17,784 | 71,167 | 16.0 | 62% | 47% | 20% | 304 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C D D | 17,523 | 31,225 | 0.0 | 69% | 31% | 42% | 265 KB | 0 |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,940 | 28,436 | 10.6 | 37% | 0% | 85% | 2,739 KB | 114 |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 16,550 | 37,878 | 23.0 | 37% | 0% | 94% | 434 KB | 17 |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 16,462 | 126,471 | 0.0 | 68% | 39% | 50% | 451 KB | 1 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C D A | 16,446 | 23,366 | 5.3 | 63% | 27% | 96% | 375 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | C E A | 16,101 | 34,807 | 10.5 | 67% | 19% | 93% | 236 KB | 5 |
| [zhiyuan-zhang0206/Ava](https://github.com/zhiyuan-zhang0206/Ava) | C C B | 16,075 | 47,480 | 48.5 | 72% | 9% | 99% | 516 KB | 1 |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | C E A | 15,925 | 18,478 | 13.7 | 83% | 22% | 98% | 149 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 15,857 | 32,046 | 0.0 | 66% | 1% | – | 699 KB | 0 |
| [kamilio/hey-boss](https://github.com/kamilio/hey-boss) | C E D | 15,719 | 16,587 | 0.0 | 58% | 22% | 39% | 653 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 15,647 | 21,929 | 54.1 | 76% | 42% | 91% | 4,310 KB | 15 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C D B | 15,555 | 31,767 | 53.4 | 64% | 70% | 100% | 768 KB | 6,233 |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C E B | 15,323 | 25,970 | 27.6 | 53% | 11% | 100% | 6,926 KB | 0 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C C B | 15,013 | 24,566 | 51.0 | 76% | 69% | 98% | 573 KB | 2 (+0) |
| [martin-janci/claude-fleet](https://github.com/martin-janci/claude-fleet) | C D D | 14,886 | 47,233 | 23.9 | 61% | 26% | 41% | 741 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 14,885 | 17,028 | 14.2 | 52% | 39% | 100% | 567 KB | 0 |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 14,806 | 22,788 | 33.9 | 80% | 39% | 78% | 1,340 KB | 3 |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C D A | 14,466 | 21,794 | 35.6 | 64% | 50% | 99% | 335 KB | 2 |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F C | 14,389 | 18,621 | 35.0 | 0% | 32% | 67% | 66 KB | 59 |
| [eiaserinnys/soulstream](https://github.com/eiaserinnys/soulstream) | C C B | 14,335 | 21,519 | 15.6 | 77% | 12% | 97% | 603 KB | 2 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | C E C | 13,877 | 43,624 | 164 | 49% | 11% | 89% | 2,294 KB | 3 |
| [ikihsan/think-free](https://github.com/ikihsan/think-free) | C C D | 13,836 | 143,092 | 0.0 | 82% | 22% | 7% | 141 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C D A | 13,637 | 38,395 | 0.0 | 65% | 12% | 94% | 211 KB | 0 |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 13,565 | 17,076 | 4.5 | 0% | 0% | 97% | 356 KB | 126 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,425 | 20,104 | 18.6 | 72% | 56% | 98% | 116 KB | 32 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 13,266 | 17,114 | 15.8 | 62% | 24% | 90% | 1,158 KB | 13 (+0) |
| [bassseamoor/render-queue](https://github.com/bassseamoor/render-queue) | C C E | 13,195 | 57,297 | 1.7 | 71% | 3% | 0% | 4,831 KB | 0 (+0) |
| [busytools/forge](https://github.com/busytools/forge) | C E C | 12,621 | 21,807 | 14.8 | 49% | 49% | 100% | 841 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C E A | 12,431 | 93,626 | 17.9 | 48% | 10% | 97% | 107 KB | 3 |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C D A | 12,299 | 20,815 | 31.9 | 66% | 50% | 96% | 260 KB | 0 (+0) |
| [sathyassn/codeflow](https://github.com/sathyassn/codeflow) | C D B | 12,106 | 17,112 | 2.1 | 68% | 2% | 95% | 600 KB | 0 |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 11,940 | 21,770 | 49.2 | 35% | 22% | 99% | 654 KB | 3 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | C D B | 11,924 | 15,218 | 23.9 | 64% | 66% | 98% | 103 KB | 4 |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C F A | 11,848 | 20,624 | 17.2 | 37% | 12% | 98% | 110 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C B | 11,818 | 25,850 | 12.3 | 87% | 30% | 80% | 77 KB | 4 |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C E C | 11,735 | 21,220 | 0.0 | 54% | 21% | 86% | 804 KB | 1 (+0) |
| [gtfo-ai/platform](https://github.com/gtfo-ai/platform) | C E C | 11,391 | 18,237 | 0.0 | 44% | 35% | 100% | 220 KB | 2 (+0) |
| [jessegall/agent-journal](https://github.com/jessegall/agent-journal) | C E D | 11,278 | 17,156 | 0.5 | 40% | 11% | 96% | 80 KB | 2 (+0) |
| [mbadali25/useful-claude-add-ons](https://github.com/mbadali25/useful-claude-add-ons) | C E B | 11,249 | 918,622 | 15.5 | 48% | 0% | 95% | 231 KB | 2 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C A | 11,204 | 16,126 | 34.4 | 70% | 23% | 86% | 102 KB | 229 (+2) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | C C C | 10,885 | 16,685 | 9.2 | 71% | 33% | 92% | 112 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C E C | 10,689 | 25,978 | 10.0 | 52% | 0% | 81% | 729 KB | 4 |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | C C B | 10,568 | 14,541 | 21.9 | 78% | 68% | 100% | 956 KB | 91 |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 10,333 | 13,831 | 18.0 | 78% | 76% | 94% | 519 KB | 1 |
| [floor/teamcli](https://github.com/floor/teamcli) | C E B | 10,293 | 20,970 | 7.5 | 42% | 10% | 81% | 67 KB | 2 (+0) |
| [korczis/prismatic-majordomus](https://github.com/korczis/prismatic-majordomus) | C E B | 10,087 | 83,340 | 11.2 | 56% | 41% | 93% | 317 KB | 0 |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D D B | 9,447 | 16,072 | 7.8 | 67% | 14% | 100% | 468 KB | 11 |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D D C | 9,313 | 14,686 | 5.1 | 66% | 19% | 96% | 104 KB | 0 (+0) |
| [Nortropic/nortropic-webb-pro](https://github.com/Nortropic/nortropic-webb-pro) | D E F | 9,216 | 43,729 | 0.0 | 54% | 14% | – | 712 KB | 0 |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D D B | 9,025 | 17,043 | 19.3 | 64% | 0% | 84% | 383 KB | 19 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D D B | 8,864 | 22,512 | 18.8 | 68% | 23% | 99% | 1,725 KB | 5 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D D A | 8,568 | 19,871 | 7.6 | 64% | 18% | 99% | 110 KB | 0 (+0) |
| [marcioapm/dude](https://github.com/marcioapm/dude) | D F B | 8,394 | 14,543 | 2.4 | 3% | 0% | 80% | 1,179 KB | 1 |
| [backspring-labs/squad-ops](https://github.com/backspring-labs/squad-ops) | D F A | 8,380 | 14,442 | 17.2 | 39% | 0% | 100% | 324 KB | 0 |
| [scode/farhelm](https://github.com/scode/farhelm) | D F B | 8,321 | 20,649 | 39.7 | 4% | 8% | 97% | 1,525 KB | 0 |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | D F D | 8,150 | 15,783 | 11.1 | 74% | 0% | – | 115 KB | 0 |
| [omarenserat1980/MySimpleProject](https://github.com/omarenserat1980/MySimpleProject) | D E C | 8,062 | 10,178 | 3.7 | 40% | 6% | 99% | 136 KB | 1 |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | D D A | 7,989 | 11,452 | 29.4 | 67% | 32% | 97% | 129 KB | 20 |
| [prime-radiant-inc/evener](https://github.com/prime-radiant-inc/evener) | D F A | 7,939 | 18,947 | 68.2 | 21% | 12% | 98% | 308 KB | 171 |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D E C | 7,931 | 9,392 | 7.6 | 49% | 0% | 96% | 94 KB | 1 |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D C C | 7,510 | 11,772 | 13.2 | 70% | 31% | 100% | 601 KB | 8 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 7,504 | 11,503 | 19.9 | 50% | 0% | 85% | 359 KB | 6 (+0) |
| [Rubentxu/software-development-decision-kernel](https://github.com/Rubentxu/software-development-decision-kernel) | D F D | 7,460 | 14,368 | 0.3 | 28% | 0% | – | 239 KB | 1 |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 7,397 | 14,742 | 23.6 | 29% | 33% | 92% | 643 KB | 17 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [ThomasHendrickx/aeolus-fleet](https://github.com/ThomasHendrickx/aeolus-fleet) | D E B | 7,299 | 12,941 | 10.0 | 54% | 25% | 98% | 431 KB | 0 |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 7,201 | 12,882 | 0.0 | 77% | 18% | 81% | 293 KB | 0 |
| [gutohuida/AgentWeave](https://github.com/gutohuida/AgentWeave) | D F B | 7,153 | 26,035 | 0.0 | 47% | 18% | 82% | 13,387 KB | 4 (+0) |
| [777genius/agent-teams-ai](https://github.com/777genius/agent-teams-ai) | D F A | 7,060 | 14,992 | 7.9 | 51% | 5% | 99% | 201 KB | 2,254 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D E B | 7,008 | 8,486 | 12.3 | 82% | 0% | 100% | 89 KB | 0 (+0) |
| [Peyday007/V5](https://github.com/Peyday007/V5) | D F B | 6,751 | 8,749 | 3.2 | 38% | 4% | 83% | 332 KB | 0 |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D C D | 6,721 | 9,275 | 24.2 | 71% | 65% | – | 612 KB | 2 |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | D E D | 6,693 | 12,358 | 0.0 | 59% | 2% | – | 94 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | D E C | 6,523 | 25,719 | 41.0 | 47% | 13% | 100% | 322 KB | 3 (+1) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D E C | 6,507 | 8,408 | 27.0 | 54% | 0% | 52% | 92 KB | 1 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,299 | 28,553 | 0.0 | 42% | 41% | 100% | 432 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | D E A | 5,894 | 9,144 | 21.5 | 62% | 0% | 100% | 73 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D C D | 5,887 | 12,710 | 23.2 | 78% | 0% | 0% | 153 KB | 1 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D F C | 5,644 | 9,340 | 13.1 | 38% | 8% | 100% | 403 KB | 2 |
| [bastani-inc/atomic](https://github.com/bastani-inc/atomic) | D F B | 5,479 | 7,140 | 13.2 | 4% | 15% | 99% | 534 KB | 856 |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D F C | 5,467 | 18,030 | 0.0 | 45% | 40% | 100% | 219 KB | 1 |
| [ehojune/bioinfo-team-3d](https://github.com/ehojune/bioinfo-team-3d) | D E B | 5,466 | 8,037 | 9.8 | 50% | 0% | 98% | 352 KB | 2 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | D C D | 5,303 | 5,550 | 0.0 | 72% | 25% | – | 80 KB | 0 |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 5,283 | 7,316 | 16.4 | 50% | 33% | 100% | 527 KB | 5 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D E B | 5,258 | 10,628 | 28.1 | 58% | 11% | 88% | 1,492 KB | 69,941 |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | D E D | 5,210 | 110,209 | 7.4 | 55% | 32% | 2% | 403 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | D E D | 5,119 | 9,223 | 0.0 | 73% | 13% | – | 202 KB | 4 |
| [donvargax/itos](https://github.com/donvargax/itos) | D E B | 5,042 | 16,868 | 0.0 | 53% | 34% | 94% | 99 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 4,965 | 9,340 | 24.1 | 0% | 0% | 100% | 489 KB | 27 |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E E B | 4,760 | 7,843 | 12.5 | 52% | 34% | 100% | 991 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 4,727 | 23,493 | 0.2 | 68% | 0% | 86% | 1,449 KB | 1,090 |
| [Dicklesworthstone/frankenterm](https://github.com/Dicklesworthstone/frankenterm) | E D D | 4,518 | 19,771 | 0.2 | 66% | 3% | 17% | 5,859 KB | 121 (+0) |
| [OpenHCSDev/agent-comms](https://github.com/OpenHCSDev/agent-comms) | E C D | 4,303 | 354,216 | 25.6 | 76% | 8% | 0% | 65 KB | 0 |
| [ubiquity/sentinel](https://github.com/ubiquity/sentinel) | E E B | 3,923 | 7,823 | 2.5 | 70% | 5% | 84% | 276 KB | 0 |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 3,840 | 11,593 | 28.6 | 31% | 9% | 100% | 617 KB | 1 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E B B | 3,830 | 6,259 | 42.1 | 85% | 46% | 97% | 247 KB | 2 |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E E D | 3,822 | 7,640 | 11.7 | 48% | 7% | – | 55 KB | 0 |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | E C C | 3,760 | 4,681 | 0.0 | 71% | 45% | 70% | 1,000 KB | 32 (+1) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 3,457 | 5,205 | 21.5 | 74% | 17% | 100% | 159 KB | 0 |
| [d41ly/coding-governance](https://github.com/d41ly/coding-governance) | E E D | 3,358 | 26,505 | 0.0 | 83% | 0% | 24% | 1,077 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 3,174 | 5,172 | 7.5 | 80% | 14% | 99% | 327 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E E C | 3,174 | 9,035 | 0.5 | 51% | 34% | 95% | 2,862 KB | 526 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E C C | 3,139 | 9,962 | 16.0 | 89% | 36% | 52% | 65 KB | 10 (+0) |
| [gthgomez/Babel](https://github.com/gthgomez/Babel) | E E B | 3,083 | 11,447 | 3.5 | 50% | 23% | 93% | 170 KB | 1 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 3,035 | 10,525 | 15.2 | 29% | 13% | – | 408 KB | 0 |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,987 | 7,020 | 0.0 | 2% | 0% | 33% | 397 KB | 455 |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E E B | 2,908 | 7,528 | 11.0 | 44% | 35% | 97% | 216 KB | 1 |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 2,832 | 97,459 | 0.5 | 53% | 11% | 63% | 4,989 KB | 1 |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 2,735 | 8,865 | 51.4 | 73% | 7% | 96% | 169 KB | 7 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E E A | 2,721 | 4,716 | 32.1 | 80% | 20% | 100% | 117 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 2,673 | 8,816 | 0.3 | 32% | 34% | 0% | 425 KB | 0 |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 2,593 | 9,378 | 5.1 | 66% | 9% | 81% | 466 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E E B | 2,511 | 14,149 | 18.1 | 43% | 0% | 100% | 120 KB | 0 |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 2,503 | 14,418 | 20.5 | 39% | 23% | 90% | 302 KB | 22 (+0) |
| [FS-GG/.github](https://github.com/FS-GG/.github) | E F C | 2,405 | 9,618 | 25.0 | 53% | 0% | 96% | 247 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | E F C | 2,396 | 36,411 | 8.2 | 44% | 0% | 94% | 67 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,263 | 16,683 | 0.0 | 3% | 0% | – | 189 KB | 26 |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 2,183 | 3,961 | 0.1 | 48% | 0% | 97% | 193 KB | 2 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | E F C | 2,100 | 22,347 | 6.9 | 45% | 0% | 98% | 42 KB | 0 |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 2,092 | 5,316 | 13.5 | 72% | 0% | 84% | 258 KB | 0 (+0) |
| [aganesy/QFAI](https://github.com/aganesy/QFAI) | E E C | 2,031 | 6,650 | 29.1 | 61% | 0% | 96% | 153 KB | 4 |
| [RoyCoding8/Stray-repo](https://github.com/RoyCoding8/Stray-repo) | E F D | 1,644 | 8,670 | 0.0 | 61% | 0% | 33% | 107 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,573 | 2,390 | 0.2 | 66% | 6% | 13% | 613 KB | 3 |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E E A | 1,543 | 4,203 | 16.5 | 75% | 10% | 99% | 154 KB | 0 (+0) |
| [jl-cmd-projects/claude-dev-env](https://github.com/jl-cmd-projects/claude-dev-env) | E F A | 1,523 | 6,842 | 20.2 | 78% | 3% | 94% | 201 KB | 7 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,441 | 2,948 | 2.4 | 25% | 22% | 99% | 7,014 KB | 18 |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F C | 1,415 | 14,421 | 0.0 | 47% | 0% | 59% | 140 KB | 105 |
| [chenchaoyi/gtmux](https://github.com/chenchaoyi/gtmux) | E E A | 1,333 | 6,940 | 18.1 | 72% | 4% | 99% | 266 KB | 2 |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E C E | 1,201 | 10,602 | 13.5 | 78% | 30% | 100% | 953 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F E B | 936 | 3,348 | 13.1 | 69% | 0% | 91% | 306 KB | 7 |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 679 | 4,267 | 38.2 | 48% | 0% | 100% | 845 KB | 3 |
| [Badmaniren/my-userbot](https://github.com/Badmaniren/my-userbot) | F D C | 652 | 4,210 | 0.0 | 66% | 54% | 100% | 93 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 466 | 2,166 | 0.2 | 38% | 0% | 3% | 904 KB | 1,261 |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F B | 365 | 3,498 | 7.4 | 0% | 0% | 81% | 71 KB | 4 |
| [yta883539-code/ai_company](https://github.com/yta883539-code/ai_company) | F F B | 358 | 3,346 | 0.0 | 29% | 0% | 100% | 148 KB | 0 |
| [obselate/tokate](https://github.com/obselate/tokate) | F F C | 332 | 12,389 | 4.9 | 37% | 0% | 100% | 43 KB | 1 |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F E B | 198 | 24,699 | 11.7 | 64% | 23% | 97% | 66 KB | 3 (+0) |
| [GLORIFIER7/GLORIFIER](https://github.com/GLORIFIER7/GLORIFIER) | F F E | 151 | 3,992 | 6.0 | 50% | 5% | 100% | 180 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 132 | 4,350 | 0.0 | 0% | 0% | 0% | 473 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 125 | 1,636 | 0.0 | 41% | 0% | – | 59 KB | 1 (+1) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 30 | 757 | 12.0 | 25% | 0% | 98% | 174 KB | 213 |
| [Daisuke134/life-manager](https://github.com/Daisuke134/life-manager) | F F B | – | – | 75.4 | 34% | 94% | 98% | 484 KB | 8 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 343,497 | 31.9 | 0% | 0% | 100% | 703 KB | 0 |
| [aburan28/crypto-autoresearcher](https://github.com/aburan28/crypto-autoresearcher) | F F E | – | – | 27.3 | 39% | 37% | – | 5,977 KB | 1 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 26.4 | 46% | 33% | 89% | 1,966 KB | 1,358 |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F E B | – | – | 23.5 | 58% | 7% | 100% | 1,042 KB | 0 |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F E A | – | – | 19.0 | 76% | 0% | 96% | 120 KB | 4 |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,803 | 6.7 | 0% | 0% | 95% | 150 KB | 346 |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 3.0 | 55% | 71% | 0% | 1,061 KB | 455 |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F E D | 0 | 0 | 1.4 | 76% | 29% | – | 5,619 KB | 0 |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 72% | 91% | 87% | 812 KB | 4 |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F D E | – | – | 0.2 | 68% | 16% | 97% | 14,566 KB | 0 |
| [hansunghee7/solar-bible](https://github.com/hansunghee7/solar-bible) | F F E | 0 | 1,323 | 0.1 | 0% | 0% | 100% | 20 KB | 0 (+0) |
| [newbiezzzzz/leverage-system](https://github.com/newbiezzzzz/leverage-system) | F F D | 0 | 21,995 | 0.1 | 0% | 0% | 65% | 33 KB | 0 |
| [pom11/hscc](https://github.com/pom11/hscc) | F F B | 0 | 1,111 | 0.1 | 0% | 0% | 100% | 133 KB | 6 |
| [jcraig949jfi/Prometheus](https://github.com/jcraig949jfi/Prometheus) | F E D | – | – | 0.0 | 59% | 65% | 98% | 3,754 KB | 3 |
| [layibabalola/softwarefactory-fleet-doctrine](https://github.com/layibabalola/softwarefactory-fleet-doctrine) | F F D | 0 | 1,649 | 0.0 | 0% | 0% | 35% | 300 KB | 1 (+0) |
| [mwetmor/reincarnated-collaboration](https://github.com/mwetmor/reincarnated-collaboration) | F E E | – | – | 0.0 | 47% | 0% | 100% | 9,472 KB | 0 (+0) |
| [oatarabay-app-link/Dashboard-](https://github.com/oatarabay-app-link/Dashboard-) | F E F | 0 | 3,501 | 0.0 | 42% | 22% | – | 8,144 KB | 0 |
| [sase-org/sase](https://github.com/sase-org/sase) | F E D | – | – | 0.0 | 52% | 40% | 49% | 72 KB | 5 |
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
