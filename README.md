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
_361 repos, last measured 2026-11-07. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A F A | 85,158 | 76,301 | 53.9 | 38% | 17% | 86% | 410 KB | 87 (+1) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | A E B | 49,635 | 103,113 | 66.5 | 51% | 20% | 100% | 548 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | A B A | 45,588 | 64,246 | 48.5 | 81% | 33% | 100% | 303 KB | 3 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 42,291 | 218,124 | 121 | 40% | 6% | 53% | 309 KB | 4 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | A C D | 42,278 | 73,864 | 0.0 | 74% | 31% | – | 450 KB | 2 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | A C D | 41,921 | 66,255 | 0.1 | 71% | 57% | 43% | 2,752 KB | 3 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A F A | 41,700 | 68,203 | 62.3 | 74% | 0% | 91% | 241 KB | 128 (+1) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A F A | 41,433 | 51,819 | 152 | 36% | 30% | 100% | 213 KB | 19 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | A C B | 40,811 | 220,334 | 1.2 | 82% | 4% | 98% | 3,340 KB | 7 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 38,703 | 184,649 | 170 | 11% | 4% | 100% | 2,294 KB | 5 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | B E B | 38,273 | 42,705 | 58.2 | 47% | 60% | 98% | 3,391 KB | 2,102 (+4) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B D B | 34,860 | 44,819 | 51.8 | 70% | 29% | 75% | 348 KB | 0 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B D B | 29,316 | 40,545 | 39.0 | 65% | 25% | 99% | 814 KB | 4 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 28,169 | 30,514 | 28.8 | 71% | 48% | 82% | 363 KB | 11 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | B C C | 27,956 | 37,697 | 68.7 | 76% | 44% | 64% | 1,079 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | B E C | 27,820 | 23,796 | 31.4 | 55% | 4% | 98% | 193 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B F B | 27,392 | 30,859 | 13.3 | 28% | 0% | 74% | 363 KB | 2 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 27,190 | 36,456 | 28.6 | 27% | 57% | 100% | 1,694 KB | 109 (+13) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B D B | 24,825 | 41,250 | 0.0 | 68% | 62% | 81% | 221 KB | 119 (+1) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | B D B | 23,475 | 250,922 | 44.3 | 68% | 23% | 82% | 1,435 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B B B | 22,666 | 27,169 | 23.6 | 82% | 42% | 96% | 839 KB | 6 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B F B | 22,649 | 31,134 | 19.9 | 47% | 8% | 87% | 781 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B C B | 22,561 | 32,671 | 102 | 74% | 32% | 92% | 4,783 KB | 80 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | B E D | 21,938 | 42,231 | 44.0 | 54% | 34% | 25% | 822 KB | 16 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B F D | 20,772 | 36,793 | 0.0 | 21% | 27% | 48% | 5,368 KB | 446 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C D C | 18,732 | 132,351 | 35.3 | 61% | 15% | 62% | 267 KB | 1 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C D D | 17,046 | 54,696 | 0.0 | 62% | 34% | – | 1,012 KB | 0 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C B B | 17,010 | 23,804 | 54.2 | 86% | 42% | 92% | 869 KB | 0 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C F D | 16,515 | 22,595 | 15.0 | 30% | 0% | 27% | 144 KB | 15 (+1) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 16,214 | 42,882 | 9.0 | 14% | 6% | 97% | 544 KB | 19 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 15,405 | 25,923 | 88.4 | 56% | 48% | 100% | 4,357 KB | 15 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,566 | 23,523 | 7.6 | 10% | 18% | 94% | 467 KB | 140 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 14,473 | 36,445 | 34.5 | 86% | 56% | 93% | 200 KB | 6 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 14,317 | 20,292 | 24.3 | 52% | 44% | 100% | 187 KB | 34 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C A | 14,136 | 22,755 | 16.4 | 79% | 36% | 87% | 144 KB | 4 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 14,105 | 20,416 | 0.0 | 80% | 32% | 28% | 359 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E C | 14,085 | 18,154 | 96.7 | 43% | 26% | 76% | 376 KB | 73 (-1) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C E B | 13,712 | 21,130 | 31.0 | 58% | 23% | 76% | 102 KB | 233 (+1) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 13,679 | 35,228 | 0.0 | 78% | 38% | – | 1,118 KB | 2 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | C E D | 13,629 | 52,405 | 57.0 | 68% | 0% | – | 446 KB | 3 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | C F D | 13,487 | 17,474 | 57.7 | 24% | 42% | 92% | 20,146 KB | 1 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C B A | 13,463 | 35,226 | 53.3 | 88% | 30% | 95% | 468 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 13,344 | 85,409 | 26.6 | 49% | 45% | 99% | 507 KB | 21 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F B | 12,885 | 16,271 | 0.0 | 40% | 37% | 76% | 324 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | C F B | 12,814 | 38,831 | 15.3 | 2% | 21% | 85% | 2,636 KB | 42 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 12,722 | 25,351 | 41.9 | 9% | 45% | 99% | 225 KB | 7 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | C F B | 12,255 | 25,324 | 58.8 | 27% | 0% | 99% | 3,196 KB | 34 (+1) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 12,236 | 21,445 | 65.9 | 41% | 12% | 98% | 275 KB | 6,560 (+5) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F C | 12,229 | 16,349 | 26.8 | 54% | 0% | 98% | 599 KB | 22 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 12,103 | 150,980 | 0.0 | 62% | 43% | 50% | 563 KB | 1 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C C B | 11,983 | 54,703 | 30.7 | 78% | 26% | 100% | 1,140 KB | 37 (+1) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 11,483 | 24,505 | 17.4 | 30% | 15% | 92% | 8,727 KB | 136 (+1) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 11,315 | 16,703 | 26.6 | 65% | 33% | 98% | 1,825 KB | 3 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 11,169 | 19,063 | 52.0 | 14% | 0% | 100% | 154 KB | 2 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C E C | 11,020 | 28,890 | 31.6 | 54% | 0% | 100% | 463 KB | 9 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C F C | 10,762 | 14,756 | 20.8 | 29% | 24% | 98% | 737 KB | 0 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 10,678 | 17,232 | 3.8 | 47% | 33% | 99% | 2,284 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 10,453 | 19,148 | 0.0 | 75% | 40% | 31% | 1,585 KB | 36 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | C C B | 10,240 | 31,241 | 14.3 | 72% | 34% | 80% | 30 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D F B | 9,632 | 9,768 | 22.5 | 58% | 0% | 99% | 1,150 KB | 8 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | D E B | 9,568 | 17,775 | 166 | 54% | 3% | 100% | 2,406 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 9,519 | 12,968 | 14.2 | 76% | 50% | 98% | 165 KB | 0 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | D F B | 9,470 | 19,518 | 21.3 | 5% | 0% | 73% | 312 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 9,089 | 35,986 | 0.0 | 29% | 0% | – | 203 KB | 30 (+2) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D E B | 8,750 | 18,877 | 15.7 | 49% | 33% | 99% | 258 KB | 4 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | D E A | 8,434 | 29,157 | 84.9 | 69% | 10% | 100% | 62 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D D B | 8,312 | 65,004 | 18.4 | 67% | 0% | 100% | 257 KB | 2 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | D F D | 8,233 | 53,938 | 0.0 | 39% | 3% | 32% | 158 KB | 117 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D C B | 8,166 | 10,258 | 13.2 | 70% | 19% | 88% | 1,230 KB | 13 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 7,938 | 12,612 | 36.7 | 65% | 63% | 96% | 216 KB | 9 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D E B | 7,591 | 8,743 | 33.0 | 64% | 0% | 99% | 1,060 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | D F C | 7,366 | 145,807 | 107 | 37% | 43% | 92% | 378 KB | 2 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D E B | 7,316 | 17,531 | 21.1 | 56% | 16% | 96% | 126 KB | 5 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 7,135 | 13,063 | 7.4 | 11% | 34% | 93% | 362 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | D F D | 7,120 | 8,321 | 1.3 | 12% | 17% | 76% | 66 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D D D | 7,012 | 13,902 | 10.7 | 62% | 36% | 12% | 224 KB | 9 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D F B | 6,660 | 22,529 | 23.8 | 27% | 12% | 96% | 634 KB | 48 (+2) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D F B | 6,635 | 23,457 | 13.6 | 24% | 29% | 100% | 617 KB | 1 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D E B | 6,494 | 12,767 | 15.6 | 46% | 0% | 97% | 458 KB | 13 (+1) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 6,486 | 21,533 | 12.8 | 40% | 16% | – | 100 KB | 2 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D F B | 6,403 | 8,382 | 12.1 | 62% | 22% | 95% | 107 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | D D B | 6,368 | 9,740 | 6.9 | 62% | 19% | 100% | 212 KB | 7 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D F D | 6,323 | 7,721 | 0.9 | 69% | 24% | 0% | 240 KB | 0 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | D F C | 6,266 | 17,035 | 26.6 | 45% | 9% | 100% | 322 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | D D C | 6,229 | 12,680 | 35.5 | 68% | 43% | 94% | 537 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | D F D | 6,173 | 47,714 | 0.1 | 27% | 0% | 90% | 1,468 KB | 1,120 (+1) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | D F D | 6,096 | 7,189 | 1.2 | 38% | 8% | 0% | 3,638 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D E B | 6,074 | 9,728 | 45.3 | 47% | 51% | 83% | 335 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D E A | 6,071 | 9,317 | 38.3 | 63% | 6% | 97% | 131 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D D C | 6,031 | 6,856 | 5.5 | 62% | 6% | 86% | 4,026 KB | 554 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D E F | 5,928 | 230,031 | 0.0 | 56% | 12% | – | 8,190 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D D B | 5,893 | 12,516 | 0.0 | 69% | 15% | 88% | 374 KB | 3 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 5,839 | 9,645 | 0.0 | 14% | 6% | 84% | 674 KB | 2 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 5,739 | 11,393 | 19.9 | 20% | 0% | 98% | 223 KB | 5 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D E A | 5,579 | 23,988 | 0.0 | 45% | 0% | 94% | 254 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D C B | 5,535 | 14,603 | 32.1 | 72% | 51% | 76% | 1,411 KB | 70,745 (+9) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D F D | 5,372 | 8,549 | 51.1 | 73% | 13% | – | 225 KB | 3 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,352 | 18,325 | 7.3 | 0% | 0% | 87% | 489 KB | 58 (+1) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D E B | 5,314 | 8,732 | 55.3 | 43% | 0% | 98% | 974 KB | 2 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D F D | 5,290 | 9,726 | 15.1 | 20% | 46% | – | 614 KB | 2 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D E B | 5,206 | 7,649 | 36.2 | 83% | 45% | 100% | 2,287 KB | 5 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | D F B | 5,188 | 16,300 | 25.9 | 17% | 24% | 100% | 597 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D B B | 5,121 | 6,193 | 14.9 | 80% | 49% | 100% | 593 KB | 1 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 4,993 | 9,401 | 27.2 | 21% | 4% | 100% | 628 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,823 | 17,860 | 23.1 | 40% | 9% | 98% | 911 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 4,759 | 9,133 | 10.4 | 46% | 0% | 73% | 6,579 KB | 8 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E B | 4,676 | 8,366 | 28.1 | 76% | 0% | 82% | 59 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E C B | 4,613 | 6,366 | 16.0 | 81% | 0% | 93% | 395 KB | 2 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | E F D | 4,582 | 9,796 | 0.0 | 46% | 0% | – | 403 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E E D | 4,389 | 15,157 | 15.1 | 76% | 19% | 45% | 527 KB | 0 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,350 | 7,283 | 35.2 | 57% | 6% | 100% | 100 KB | 3 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 4,323 | 6,866 | 21.0 | 12% | 11% | 95% | 165 KB | 12 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 4,209 | 4,843 | 15.0 | 56% | 0% | 99% | 42 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 4,204 | 5,570 | 0.1 | 20% | 12% | 86% | 1,038 KB | 2 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 4,192 | 4,501 | 16.8 | 38% | 35% | – | 61 KB | 3 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F B | 4,173 | 6,480 | 14.4 | 12% | 4% | 98% | 544 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | E F B | 4,156 | 8,686 | 47.5 | 7% | 22% | 100% | 605 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,147 | 5,183 | 14.1 | 12% | 0% | 98% | 147 KB | 1 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | E D A | 4,030 | 168,340 | 55.8 | 65% | 21% | 100% | 158 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,980 | 6,657 | 16.5 | 4% | 40% | 98% | 386 KB | 2 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 3,796 | 9,349 | 17.6 | 56% | 25% | 99% | 215 KB | 1 (+1) |
| [quadseven/loom](https://github.com/quadseven/loom) | E E C | 3,713 | 6,245 | 35.1 | 75% | 29% | 98% | 798 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F A | 3,686 | 15,277 | 43.9 | 44% | 0% | 92% | 169 KB | 2 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 3,655 | 6,140 | 13.7 | 24% | 17% | 95% | 343 KB | 172 (+1) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 3,604 | 4,977 | 25.8 | 59% | 19% | 99% | 313 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 3,534 | 9,865 | 20.1 | 28% | 20% | 100% | 289 KB | 1 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 3,526 | 12,056 | 0.1 | 30% | 0% | 100% | 472 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E F B | 3,497 | 14,451 | 0.0 | 58% | 2% | 96% | 590 KB | 1 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 3,481 | 8,705 | 20.7 | 10% | 0% | 100% | 541 KB | 88 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 3,469 | 6,458 | 8.2 | 36% | 7% | 99% | 350 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 3,420 | 6,984 | 11.1 | 35% | 4% | 73% | 131 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 3,380 | 27,884 | 12.1 | 32% | 28% | 96% | 382 KB | 25 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F B | 3,359 | 53,237 | 29.5 | 10% | 0% | 77% | 189 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | E F B | 3,340 | 6,759 | 11.4 | 44% | 0% | 100% | 95 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E E E | 3,228 | 11,193 | 23.9 | 48% | 44% | 76% | 1,699 KB | 6 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 3,207 | 3,600 | 13.1 | 60% | 17% | 100% | 260 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 3,173 | 4,500 | 31.5 | 55% | 4% | 99% | 354 KB | 2 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 3,123 | 10,156 | 10.7 | 9% | 0% | 74% | 105 KB | 3 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 3,078 | 5,755 | 43.4 | 34% | 33% | 100% | 590 KB | 5 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E F B | 3,053 | 7,348 | 11.6 | 39% | 0% | 98% | 54 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 2,903 | 6,213 | 40.0 | 31% | 28% | 100% | 1,392 KB | 8 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 2,896 | 18,123 | 25.6 | 4% | 47% | 98% | 363 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E C B | 2,883 | 9,974 | 32.3 | 78% | 57% | 100% | 33 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 2,882 | 3,278 | 25.6 | 32% | 0% | 94% | 49 KB | 23,851 (+10) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 2,882 | 5,363 | 6.7 | 13% | 0% | 88% | 739 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 2,700 | 12,135 | 27.7 | 15% | 0% | 86% | 987 KB | 115 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F B | 2,608 | 4,574 | 32.4 | 0% | 0% | 80% | 67 KB | 63 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E F C | 2,555 | 13,267 | 13.2 | 60% | 29% | 95% | 150 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,498 | 10,561 | 0.0 | 59% | 0% | 97% | 559 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E F B | 2,482 | 4,015 | 19.4 | 53% | 0% | 99% | 93 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F A | 2,482 | 9,055 | 16.0 | 42% | 0% | 85% | 382 KB | 9 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F A | 2,475 | 39,820 | 25.3 | 8% | 0% | 100% | 380 KB | 49 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,445 | 10,725 | 0.1 | 10% | 0% | 84% | 153 KB | 60 (-12) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,428 | 8,494 | 0.0 | 8% | 3% | 0% | 1,273 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 2,426 | 4,240 | 25.1 | 42% | 0% | 99% | 163 KB | 6 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | E F B | 2,363 | 4,128 | 6.7 | 42% | 0% | 96% | 363 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 2,363 | 7,288 | 0.0 | 43% | 30% | 42% | 267 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,350 | 6,884 | 6.0 | 68% | 0% | 99% | 549 KB | 12 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 2,167 | 5,635 | 23.6 | 23% | 45% | 100% | 391 KB | 17 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 2,135 | 7,837 | 0.0 | 2% | 0% | 84% | 948 KB | 48 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 2,125 | 3,137 | 0.0 | 5% | 18% | 73% | 291 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 2,122 | 2,281 | 4.7 | 0% | 0% | 100% | 166 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 1,985 | 3,048 | 20.6 | 33% | 0% | 90% | 608 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E E D | 1,957 | 3,360 | 43.1 | 81% | 30% | – | 440 KB | 1 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 1,897 | 2,400 | 49.6 | 31% | 55% | 98% | 704 KB | 13 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,885 | 7,780 | 12.0 | 39% | 0% | 100% | 1,072 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 1,849 | 6,483 | 15.1 | 31% | 0% | 90% | 458 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | E F C | 1,830 | 4,263 | 60.4 | 18% | 16% | 95% | 562 KB | 2 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E F E | 1,796 | 26,019 | 0.0 | 23% | 0% | 88% | 139 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 1,764 | 6,325 | 15.9 | 0% | 0% | 99% | 399 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | E F C | 1,754 | 3,457 | 24.5 | 22% | 27% | 100% | 42 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 1,752 | 38,750 | 40.9 | 23% | 0% | 100% | 212 KB | 1 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,702 | 3,020 | 21.8 | 32% | 28% | 97% | 104 KB | 1 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 1,654 | 33,867 | 0.0 | 2% | 4% | 0% | 303 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 1,622 | 5,126 | 0.1 | 40% | 14% | 38% | 376 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F B | 1,605 | 11,076 | 3.1 | 32% | 0% | 100% | 1,149 KB | 5 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,591 | 6,754 | 17.4 | 67% | 0% | 100% | 518 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 1,567 | 11,884 | 21.0 | 66% | 49% | 84% | 540 KB | 10 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 1,471 | 2,627 | 32.6 | 41% | 18% | 96% | 512 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | E F C | 1,366 | 1,948 | 21.2 | 0% | 0% | 100% | 25 KB | 18 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F B | 1,307 | 6,942 | 22.1 | 41% | 13% | 100% | 126 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 1,262 | 2,341 | 18.0 | 43% | 0% | 100% | 168 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E E C | 1,248 | 12,260 | 6.4 | 70% | 11% | 95% | 697 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F B | 1,235 | 6,466 | 27.3 | 15% | 0% | 99% | 167 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F B | 1,220 | 9,009 | 8.5 | 35% | 0% | 74% | 299 KB | 341 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F B | 1,209 | 3,089 | 25.1 | 4% | 0% | 74% | 327 KB | 160 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E B C | 1,195 | 5,768 | 0.0 | 85% | 82% | 98% | 1,964 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 1,159 | 2,564 | 13.6 | 56% | 0% | 99% | 381 KB | 2 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 1,142 | 9,682 | 9.6 | 63% | 0% | 94% | 721 KB | 9 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E E D | 1,123 | 8,396 | 0.0 | 80% | 23% | – | 972 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | E F B | 1,038 | 24,328 | 68.1 | 17% | 0% | 96% | 616 KB | 2 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | E F A | 1,008 | 1,466 | 22.1 | 46% | 0% | 99% | 96 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 980 | 56,820 | 21.9 | 16% | 0% | 90% | 1,414 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 871 | 5,266 | 0.0 | 28% | 0% | 33% | 402 KB | 462 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 782 | 2,309 | 4.9 | 0% | 0% | 93% | 3,845 KB | 1 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 776 | 21,963 | 0.0 | 37% | 0% | 88% | 554 KB | 29 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 740 | 2,884 | 5.5 | 7% | 0% | 90% | 936 KB | 2 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | F F C | 733 | 1,758 | 17.0 | 71% | 0% | 83% | 998 KB | 2 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | F F B | 691 | 2,321 | 26.2 | 0% | 0% | 96% | 107 KB | 4 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 631 | 791 | 0.0 | 71% | 41% | 0% | 670 KB | 3 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | F E A | 590 | 897 | 14.1 | 51% | 0% | 100% | 457 KB | 13 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | F F D | 579 | 5,855 | 0.0 | 3% | 0% | 0% | 601 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 548 | 2,618 | 7.8 | 57% | 0% | 100% | 132 KB | 244 (+1) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | F F B | 537 | 1,915 | 20.8 | 0% | 0% | 97% | 1,116 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | 465 | 1,382 | 0.0 | 29% | 0% | 0% | 342 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F E E | 442 | 8,868 | 18.8 | 66% | 15% | 99% | 632 KB | 11 (+0) |
| [integry/propr](https://github.com/integry/propr) | F F B | 439 | 2,080 | 9.6 | 48% | 0% | 100% | 4,314 KB | 30 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 430 | 1,156 | 24.5 | 0% | 0% | 99% | 240 KB | 10 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 415 | 9,949 | 14.9 | 43% | 0% | 94% | 5,248 KB | 40,660 (+14) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 401 | 1,211 | 13.7 | 15% | 0% | 100% | 61 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | F F D | 374 | 72,422 | 0.0 | 72% | 0% | 0% | 3,286 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 365 | 1,155 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 357 | 1,883 | 13.9 | 20% | 0% | 100% | 79 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | F F D | 352 | 867 | 22.6 | 27% | 0% | 32% | 4,722 KB | 110 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 312 | 999,990 | 4.9 | 2% | 0% | 84% | 23 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 309 | 1,476 | 30.3 | 11% | 0% | 96% | 270 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F C | 258 | 3,030 | 11.6 | 28% | 0% | 62% | 274 KB | 1 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 243 | 2,649 | 7.0 | 47% | 0% | 99% | 571 KB | 1 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 240 | 847 | 6.1 | 0% | 0% | – | 690 KB | 1 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 233 | 2,069 | 0.0 | 47% | 0% | – | 80 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 213 | 2,577 | 6.8 | 0% | 0% | 99% | 100 KB | 4 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 193 | 439 | 8.6 | 0% | 0% | 63% | 638 KB | 4 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 167 | 2,008 | 25.6 | 0% | 0% | 98% | 553 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 145 | 1,578 | 35.5 | 0% | 0% | 96% | 249 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F E | 121 | 31,004 | 32.0 | 0% | 0% | 19% | 3,975 KB | 1 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 96 | 751 | 12.7 | 68% | 0% | 98% | 450 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 76 | 1,702 | 14.5 | 0% | 0% | 34% | 7,014 KB | 20 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 45 | 1,250 | 9.5 | 38% | 0% | 0% | 285 KB | 25 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | F F C | 35 | 783 | 1.3 | 0% | 0% | 99% | 5,608 KB | 1 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 20 | 130 | 0.0 | 0% | 0% | 99% | 444 KB | 0 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F B | 10 | 2,299 | 7.8 | 36% | 0% | 79% | 27 KB | 0 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 7 | 4,982 | 11.6 | 16% | 0% | 96% | 99 KB | 1 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 7 | 43,091 | 4.8 | 0% | 0% | 73% | 149 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 2 | 2,721 | 12.6 | 5% | 0% | 0% | 348 KB | 1 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 1 | 136 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F B B | – | – | 52.4 | 81% | 69% | 94% | 793 KB | 11 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F A | 0 | 531 | 51.8 | 0% | 0% | 96% | 136 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 354,623 | 42.8 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 40.8 | – | – | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 35.9 | 42% | 26% | 90% | 2,272 KB | 1,496 (+2) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | 0 | 196,496 | 30.4 | 24% | 0% | 79% | 416 KB | 9 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | 0 | 251 | 26.1 | 30% | 0% | 100% | 403 KB | 2 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 27 | 22.9 | 0% | 0% | 97% | 383 KB | 1,612 (+2) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 21.6 | – | – | 99% | 884 KB | 5 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 21.4 | 33% | 15% | 100% | 1,032 KB | 4 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | 0 | 775 | 20.8 | 0% | 0% | 99% | 504 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 0 | 594 | 20.5 | 0% | 0% | 95% | 122 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 18.4 | 0% | 0% | 98% | 154 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | 0 | 4 | 17.6 | 0% | 0% | 100% | 41 KB | 2 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | 0 | 1,112 | 17.3 | 38% | 0% | 100% | 566 KB | 2 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 1,103 | 17.2 | 0% | 0% | 88% | 1,170 KB | 0 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 0 | 17,591 | 16.4 | 65% | 0% | 99% | 355 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 356 | 16.4 | 0% | 0% | 76% | 335 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 11 | 16.1 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F F B | – | – | 15.5 | 38% | 0% | 93% | 86 KB | 6 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 14.8 | – | – | 98% | 363 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 281 | 14.6 | 57% | 0% | 76% | 15 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 0 | 548 | 13.9 | 0% | 0% | 100% | 160 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | – | – | 13.7 | – | – | 96% | 32 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 552 | 13.0 | 24% | 0% | 96% | 66 KB | 3 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 13.0 | 56% | 0% | 0% | 206 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | – | – | 10.9 | – | – | 93% | 576 KB | 1 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 0 | 10.9 | 0% | 0% | 95% | 8,119 KB | 1 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 10.6 | – | – | 99% | 80 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 0 | 2,535 | 9.8 | 20% | 0% | 97% | 663 KB | 2 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 332 | 9.8 | 0% | 0% | 96% | 45 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 11 | 8.9 | 0% | 0% | 97% | 57 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | F F A | 0 | 114 | 8.8 | 0% | 0% | 97% | 236 KB | 5 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 1,059 | 8.3 | 0% | 0% | – | 100 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 0 | 2,509 | 8.0 | 0% | 0% | 98% | 45 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | – | – | 8.0 | – | – | 88% | 700 KB | 4 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 339 | 8.0 | 0% | 0% | 99% | 87 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 7.9 | – | – | 97% | 94 KB | 16 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 559 | 7.8 | 0% | 0% | 99% | 127 KB | 23 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 0 | 121 | 7.4 | 0% | 0% | 80% | 83 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 419 | 7.0 | 22% | 0% | 99% | 156 KB | 2 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 0 | 1,559 | 7.0 | 33% | 0% | – | 415 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 0 | 0 | 6.8 | 0% | 0% | 89% | 682 KB | 6 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | – | – | 6.5 | – | – | – | 311 KB | 4 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | – | – | 5.2 | – | – | 80% | 552 KB | 2 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | – | – | 5.2 | – | – | 75% | 161 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 2 | 4.5 | 0% | 0% | 90% | 163 KB | 14 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | 0 | 22 | 4.3 | 0% | 0% | 97% | 43 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | – | – | 4.3 | – | – | 96% | 122 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 3.7 | – | – | 90% | 195 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F B D | – | – | 3.5 | 82% | 72% | 0% | 2,040 KB | 460 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F B | 0 | 1,949 | 3.4 | 0% | 0% | 86% | 262 KB | 1,252 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 3.2 | – | – | 98% | 723 KB | 5 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 105 | 3.2 | 0% | 0% | – | 56 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 563 | 3.2 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | 0 | 1,313 | 3.2 | 0% | 0% | 90% | 319 KB | 1 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 3.0 | – | – | 99% | 298 KB | 5 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 0 | 2.8 | – | – | 100% | 258 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 20,065 | 2.6 | 0% | 0% | 99% | 579 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 2.6 | – | – | 98% | 231 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 85 | 2.3 | 0% | 0% | 88% | 151 KB | 351 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 14 | 2.1 | 0% | 0% | 99% | 73 KB | 3 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F D | 0 | 1,255 | 1.5 | 0% | 0% | 9% | 52 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 1.3 | – | – | – | 115 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 0 | 0 | 0.9 | 0% | 0% | – | 53 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 238 | 0.7 | 0% | 0% | 20% | 154 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | – | – | 0.6 | – | – | 98% | 42 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.5 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 0.4 | – | – | 69% | 290 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.4 | – | – | 0% | 518 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F F B | – | – | 0.2 | 82% | 0% | 83% | 846 KB | 7 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | – | – | 0.1 | – | – | 16% | 904 KB | 1,316 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F D | – | – | 0.1 | 59% | 34% | 50% | 87 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,371 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 103 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 99 | 0.0 | 0% | 0% | – | 66 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 5,664 | 0.0 | 80% | 0% | 0% | 254 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | F F D | 0 | 0 | 0.0 | – | – | 30% | 308 KB | 737 (+17) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.0 | 49% | 0% | 94% | 34,213 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 13 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 43,164 | 0.0 | 0% | 0% | – | 110 KB | 1 (+0) |
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
