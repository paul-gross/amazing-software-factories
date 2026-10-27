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
_361 repos, last measured 2026-10-27. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [goat-si/goat](https://github.com/goat-si/goat) | A E B | 63,481 | 101,420 | 26.6 | 45% | 11% | 100% | 3,173 KB | 5 |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 59,345 | 91,285 | 33.8 | 43% | 25% | 87% | 198 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | A B B | 55,922 | 93,282 | 23.5 | 85% | 12% | 100% | 817 KB | 4 |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 51,732 | 201,276 | 118 | 65% | 0% | 51% | 307 KB | 4 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A D D | 50,387 | 153,689 | 0.2 | 63% | 36% | 26% | 1,271 KB | 440 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 49,535 | 57,972 | 72.9 | 2% | 0% | 99% | 3,150 KB | 2,040 (+8) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 44,279 | 80,957 | 170 | 20% | 35% | 89% | 2,294 KB | 4 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | A C B | 42,033 | 53,493 | 0.0 | 71% | 47% | 82% | 188 KB | 111 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A D B | 41,990 | 49,172 | 53.8 | 64% | 59% | 92% | 924 KB | 1 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A E A | 41,255 | 91,864 | 61.1 | 66% | 2% | 95% | 210 KB | 122 (+1) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | B D B | 34,158 | 47,749 | 32.9 | 65% | 28% | 92% | 591 KB | 11 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | B E D | 31,579 | 90,225 | 0.0 | 57% | 50% | 0% | 296 KB | 0 |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C D | 30,512 | 37,673 | 30.5 | 74% | 32% | 87% | 363 KB | 10 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 30,373 | 71,541 | 58.6 | 13% | 0% | 83% | 3,975 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B E A | 30,038 | 40,691 | 77.1 | 52% | 21% | 93% | 60 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | B E A | 29,467 | 56,700 | 29.9 | 71% | 61% | 99% | 49 KB | 23,772 |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | B C D | 29,298 | 66,491 | 0.0 | 79% | 24% | – | 191 KB | 0 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | B D A | 29,277 | 38,247 | 27.0 | 62% | 43% | 94% | 312 KB | 1 |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B D B | 28,641 | 66,128 | 9.7 | 67% | 24% | 76% | 292 KB | 332 (+1) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 28,515 | 40,565 | 17.4 | 26% | 40% | 96% | 6,732 KB | 125 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B E B | 28,221 | 40,499 | 26.4 | 44% | 20% | 99% | 574 KB | 0 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B E A | 28,171 | 92,358 | 33.0 | 49% | 12% | 90% | 404 KB | 80 |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | B E A | 27,071 | 43,301 | 12.8 | 73% | 4% | 92% | 353 KB | 0 |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F C | 26,762 | 31,827 | 103 | 30% | 63% | 76% | 361 KB | 68 (+11) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B D C | 26,730 | 28,959 | 32.4 | 62% | 42% | 100% | 315 KB | 0 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 26,720 | 31,174 | 32.1 | 43% | 33% | 100% | 1,403 KB | 91 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 26,473 | 30,486 | 94.7 | 39% | 12% | 92% | 3,814 KB | 73 (+1) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B D B | 26,366 | 43,092 | 12.1 | 61% | 0% | 89% | 781 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B D C | 25,545 | 43,896 | 72.3 | 64% | 52% | 93% | 548 KB | 2 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 24,586 | 525,219 | 0.0 | 81% | 64% | 0% | 3,286 KB | 1 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | B B D | 23,779 | 52,471 | 0.0 | 82% | 34% | 28% | 248 KB | 0 |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B D B | 23,604 | 29,140 | 28.4 | 64% | 2% | 85% | 700 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 23,300 | 86,327 | 28.9 | 56% | 48% | 100% | 966 KB | 33 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 21,641 | 55,977 | 49.3 | 36% | 49% | 100% | 59 KB | 0 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B E B | 21,284 | 24,097 | 41.1 | 58% | 19% | 92% | 515 KB | 1 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B C C | 20,926 | 36,556 | 23.4 | 74% | 15% | 94% | 712 KB | 9 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B F B | 20,830 | 39,279 | 18.2 | 53% | 0% | 76% | 260 KB | 2 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 20,466 | 37,057 | 0.0 | 79% | 52% | – | 1,222 KB | 3 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 20,376 | 39,021 | 111 | 50% | 16% | 100% | 293 KB | 16 (+1) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B E B | 20,111 | 27,510 | 17.3 | 68% | 0% | 97% | 361 KB | 1,586 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C C B | 19,975 | 216,737 | 1.3 | 71% | 28% | 98% | 3,340 KB | 7 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 19,155 | 28,275 | 26.8 | 55% | 47% | 99% | 178 KB | 33 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F B | 18,681 | 42,791 | 0.0 | 28% | 30% | 91% | 674 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | C F B | 18,209 | 72,380 | 20.3 | 0% | 12% | 84% | 213 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C C B | 17,645 | 20,994 | 24.5 | 70% | 18% | 91% | 1,074 KB | 6 (+1) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | C D B | 17,380 | 24,147 | 42.0 | 67% | 38% | 98% | 549 KB | 2 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C B B | 17,298 | 38,642 | 22.2 | 81% | 40% | 86% | 767 KB | 5 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | C F E | 17,171 | 36,662 | 45.6 | 40% | 36% | 97% | 20,146 KB | 1 |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 17,071 | 25,931 | 0.0 | 54% | 43% | 100% | 4,357 KB | 15 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 16,998 | 24,896 | 66.3 | 40% | 64% | 87% | 275 KB | 6,435 (+14) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | C E D | 16,893 | 20,094 | 0.0 | 47% | 4% | – | 315 KB | 0 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 16,721 | 165,804 | 34.7 | 85% | 44% | 99% | 158 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,327 | 36,406 | 36.7 | 1% | 43% | 100% | 225 KB | 7 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C C C | 16,213 | 40,703 | 10.3 | 74% | 63% | 100% | 102 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | C C A | 15,844 | 49,047 | 68.2 | 71% | 10% | 97% | 169 KB | 2 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F D | 15,705 | 21,984 | 33.2 | 58% | 32% | 100% | 599 KB | 22 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,352 | 21,910 | 5.7 | 6% | 26% | 97% | 433 KB | 137 (-1) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 15,342 | 24,082 | 38.8 | 38% | 52% | 99% | 1,340 KB | 8 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C C A | 15,288 | 29,385 | 48.0 | 78% | 38% | 100% | 346 KB | 2 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B B | 15,151 | 27,475 | 0.0 | 89% | 57% | 72% | 302 KB | 0 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | C D D | 15,108 | 24,145 | 0.1 | 67% | 23% | 27% | 2,793 KB | 2 |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C D C | 14,656 | 41,195 | 14.1 | 62% | 41% | 71% | 431 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 14,525 | 27,875 | 42.9 | 10% | 10% | 98% | 249 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | C D B | 14,342 | 194,883 | 95.8 | 66% | 23% | 94% | 609 KB | 2 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | C E C | 14,322 | 15,002 | 10.7 | 68% | 8% | 100% | 49 KB | 3 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C B B | 14,219 | 18,988 | 19.9 | 81% | 22% | 70% | 608 KB | 1 |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D A | 14,023 | 18,305 | 35.4 | 64% | 61% | 86% | 102 KB | 232 (+1) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | C E A | 13,880 | 14,872 | 11.6 | 45% | 0% | 92% | 257 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C C B | 13,855 | 26,105 | 33.5 | 79% | 55% | 89% | 1,386 KB | 70,367 (+36) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 13,741 | 25,157 | 3.0 | 40% | 0% | 95% | 2,284 KB | 0 |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C E B | 13,468 | 17,971 | 31.2 | 68% | 28% | 94% | 1,550 KB | 3 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 13,278 | 31,136 | 43.3 | 18% | 1% | 100% | 83 KB | 2 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 13,153 | 50,074 | 42.0 | 44% | 0% | 81% | 414 KB | 9 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | C F A | 12,998 | 36,941 | 52.8 | 39% | 55% | 95% | 133 KB | 1 |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C E B | 12,949 | 19,940 | 181 | 57% | 54% | 100% | 2,377 KB | 1 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C C B | 12,925 | 16,023 | 13.8 | 78% | 21% | 87% | 1,201 KB | 13 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | C B B | 12,794 | 16,091 | 8.6 | 81% | 27% | 99% | 363 KB | 1 |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C F B | 12,734 | 12,095 | 39.0 | 48% | 11% | 100% | 792 KB | 2 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | C C B | 12,710 | 41,206 | 5.9 | 77% | 31% | 84% | 21 KB | 0 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C C B | 12,613 | 19,246 | 39.2 | 74% | 1% | 98% | 196 KB | 1 |
| [preloop/preloop](https://github.com/preloop/preloop) | C E B | 12,590 | 16,629 | 21.5 | 52% | 0% | 94% | 524 KB | 81 (+1) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | C F C | 12,528 | 56,955 | 24.0 | 40% | 0% | 54% | 4,722 KB | 96 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C D D | 12,158 | 24,439 | 0.0 | 64% | 26% | 26% | 154 KB | 113 (+1) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | C E B | 12,141 | 118,580 | 14.2 | 64% | 30% | 96% | 126 KB | 4 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 12,058 | 35,819 | 72.2 | 48% | 50% | 25% | 837 KB | 16 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C E B | 12,008 | 22,364 | 20.2 | 66% | 0% | 100% | 936 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C E B | 11,801 | 210,941 | 44.2 | 59% | 36% | 94% | 1,431 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C E D | 11,794 | 20,927 | 0.4 | 59% | 10% | – | 413 KB | 1 |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 10,814 | 12.5 | 44% | 0% | 94% | 718 KB | 9 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 11,423 | 19,005 | 35.3 | 78% | 36% | 100% | 2,202 KB | 5 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | C E A | 11,379 | 12,002 | 27.3 | 74% | 32% | 100% | 162 KB | 5 |
| [qiangli/yoke](https://github.com/qiangli/yoke) | C E D | 11,254 | 30,060 | 0.0 | 52% | 8% | 0% | 601 KB | 1 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 10,949 | 13,375 | 0.0 | 88% | 34% | – | 227 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C E A | 10,851 | 142,944 | 0.0 | 67% | 0% | 93% | 211 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 10,723 | 96,511 | 15.7 | 50% | 7% | 84% | 485 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 10,633 | 26,572 | 25.1 | 51% | 21% | 97% | 466 KB | 19 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | C F B | 10,576 | 19,859 | 24.4 | 36% | 0% | 97% | 628 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | C F B | 10,391 | 14,326 | 28.8 | 18% | 16% | 91% | 160 KB | 8 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 10,191 | 16,527 | 0.0 | 54% | 12% | – | 319 KB | 2 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 9,895 | 14,819 | 8.7 | 48% | 0% | 16% | 197 KB | 4 (+1) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D E B | 9,272 | 14,975 | 0.4 | 74% | 7% | 79% | 374 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C B | 9,150 | 23,421 | 17.2 | 78% | 47% | 83% | 130 KB | 5 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 9,090 | 18,612 | 36.4 | 60% | 48% | 99% | 566 KB | 5 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 9,064 | 11,091 | 16.9 | 72% | 42% | 93% | 147 KB | 1 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D C C | 9,059 | 34,086 | 0.0 | 78% | 36% | 100% | 492 KB | 1 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | D C A | 8,998 | 20,455 | 24.3 | 71% | 33% | 97% | 177 KB | 6 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D F C | 8,920 | 24,427 | 21.8 | 48% | 0% | 88% | 43 KB | 16 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D C B | 8,878 | 23,160 | 36.8 | 74% | 14% | 95% | 571 KB | 37 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D E B | 8,762 | 15,864 | 31.6 | 50% | 11% | 99% | 1,060 KB | 0 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 8,678 | 9,010 | 24.7 | 47% | 0% | 100% | 598 KB | 0 |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 8,678 | 7,914 | 2.1 | 8% | 0% | 79% | 1,423 KB | 1 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | D C A | 8,671 | 10,771 | 25.5 | 77% | 39% | 99% | 200 KB | 6 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 8,527 | 44,375 | 17.9 | 36% | 0% | 99% | 251 KB | 2 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | D E C | 8,454 | 19,219 | 0.0 | 75% | 6% | 100% | 1,023 KB | 0 |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D E B | 8,448 | 9,488 | 19.1 | 57% | 55% | 100% | 568 KB | 1 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | D F A | 8,435 | 37,097 | 41.4 | 39% | 0% | 99% | 240 KB | 9 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | D F E | 8,260 | 12,477 | 15.7 | 66% | 0% | 68% | 330 KB | 1 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | D E C | 8,130 | 25,202 | 0.0 | 59% | 29% | 97% | 923 KB | 28 |
| [apiad/aegis](https://github.com/apiad/aegis) | D C C | 8,033 | 13,005 | 10.3 | 78% | 23% | 68% | 343 KB | 22 |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | D D C | 8,013 | 19,506 | 0.0 | 70% | 18% | 63% | 535 KB | 1 |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | D F C | 7,858 | 10,356 | 15.3 | 35% | 0% | 95% | 8,119 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 7,842 | 9,086 | 17.5 | 21% | 0% | 70% | 377 KB | 7 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D E B | 7,838 | 10,788 | 14.9 | 40% | 40% | 93% | 325 KB | 164 (+2) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | D F C | 7,809 | 14,871 | 6.6 | 40% | 2% | 91% | 3,845 KB | 1 |
| [Gharib89/skills](https://github.com/Gharib89/skills) | D E B | 7,795 | 18,579 | 9.0 | 79% | 0% | 95% | 45 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,760 | 11,362 | 5.3 | 33% | 42% | 83% | 3,721 KB | 547 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | D E D | 7,745 | 19,558 | 1.3 | 54% | 4% | 79% | 85 KB | 1 |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 7,719 | 17,993 | 3.8 | 67% | 0% | 90% | 319 KB | 1 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D F D | 7,550 | 13,683 | 5.5 | 51% | 47% | – | 459 KB | 2 |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D E B | 7,463 | 13,226 | 9.2 | 77% | 32% | 99% | 89 KB | 0 |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 7,457 | 10,306 | 5.9 | 38% | 27% | 93% | 388 KB | 0 |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D D C | 7,338 | 7,809 | 24.8 | 64% | 56% | 91% | 961 KB | 1 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D D C | 7,305 | 14,157 | 14.6 | 63% | 0% | 97% | 372 KB | 2 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | D E D | 7,205 | 23,864 | 10.5 | 55% | 6% | 0% | 142 KB | 15 (+1) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F B | 7,204 | 12,622 | 46.6 | 0% | 15% | 82% | 67 KB | 62 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D C A | 7,180 | 10,203 | 37.6 | 78% | 0% | 100% | 125 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | D F C | 7,156 | 76,028 | 5.1 | 28% | 0% | 90% | 78 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 7,083 | 194,732 | 32.5 | 33% | 12% | 93% | 1,414 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | D F D | 6,885 | 8,260 | 0.0 | 35% | 0% | 30% | 308 KB | 278 (+4) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F A | 6,883 | 19,677 | 27.7 | 60% | 0% | 100% | 377 KB | 49 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | D F A | 6,801 | 13,187 | 19.1 | 80% | 0% | 97% | 90 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 6,767 | 8,870 | 42.0 | 17% | 60% | 84% | 333 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | D E B | 6,761 | 20,157 | 5.7 | 41% | 38% | 81% | 680 KB | 1 |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D D C | 6,757 | 11,522 | 0.1 | 67% | 9% | 100% | 371 KB | 2 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 6,623 | 19,178 | 0.0 | 24% | 0% | – | 824 KB | 0 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D F C | 6,516 | 40,907 | 0.0 | 56% | 11% | 50% | 483 KB | 1 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D F B | 6,445 | 9,137 | 0.0 | 72% | 2% | 93% | 590 KB | 1 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D C B | 6,323 | 13,912 | 13.1 | 72% | 6% | 98% | 361 KB | 2 |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D F C | 6,240 | 21,614 | 28.6 | 11% | 19% | 78% | 161 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | D F B | 6,100 | 20,766 | 15.1 | 68% | 0% | 96% | 86 KB | 6 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | D F B | 6,098 | 16,529 | 4.8 | 35% | 6% | 91% | 261 KB | 1,236 |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | D E B | 6,013 | 7,226 | 9.9 | 53% | 53% | 99% | 80 KB | 0 |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D E C | 5,939 | 9,620 | 20.8 | 55% | 0% | 100% | 41 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D C B | 5,923 | 11,882 | 0.0 | 71% | 38% | 79% | 246 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | D E B | 5,889 | 21,669 | 14.8 | 58% | 34% | 81% | 518 KB | 18 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D F D | 5,675 | 7,897 | 40.8 | 65% | 0% | – | 434 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | D F D | 5,594 | 6,931 | 0.0 | 60% | 0% | – | 3,234 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D F B | 5,544 | 6,370 | 69.7 | 58% | 11% | 100% | 794 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D F A | 5,436 | 7,728 | 19.0 | 44% | 19% | 97% | 156 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D F D | 5,397 | 12,016 | 51.5 | 38% | 28% | – | 397 KB | 3 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | D F A | 5,392 | 5,591 | 20.6 | 34% | 0% | 100% | 152 KB | 1 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D D B | 5,373 | 14,853 | 29.4 | 68% | 68% | 100% | 1,172 KB | 0 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | D F B | 5,354 | 12,023 | 31.5 | 67% | 0% | 100% | 78 KB | 3 |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D C C | 5,271 | 8,669 | 11.1 | 86% | 0% | 98% | 129 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D C D | 5,253 | 5,570 | 0.8 | 77% | 54% | 0% | 168 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | D F D | 5,249 | 8,371 | 0.3 | 47% | 18% | 0% | 518 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D F B | 5,244 | 7,405 | 7.5 | 56% | 0% | 81% | 616 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 5,198 | 10,103 | 0.1 | 25% | 10% | 86% | 906 KB | 2 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | E F B | 4,938 | 12,587 | 33.1 | 0% | 0% | 100% | 884 KB | 4 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E F B | 4,935 | 5,697 | 24.1 | 68% | 15% | 100% | 106 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E D | 4,827 | 11,125 | 10.5 | 42% | 55% | 49% | 42 KB | 13 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E F E | 4,739 | 9,714 | 21.5 | 48% | 7% | 85% | 1,169 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 4,522 | 9,516 | 66.0 | 39% | 14% | 97% | 695 KB | 14 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | E F D | 4,303 | 6,684 | 1.4 | 55% | 0% | – | 311 KB | 3 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,260 | 6,804 | 24.4 | 25% | 0% | 96% | 840 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 4,144 | 11,682 | 0.0 | 13% | 39% | 0% | 451 KB | 4 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E C B | 3,951 | 6,840 | 9.5 | 87% | 5% | 95% | 415 KB | 2 |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E E B | 3,943 | 5,282 | 20.4 | 60% | 22% | 92% | 1,116 KB | 1 |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 3,929 | 4,691 | 23.4 | 46% | 7% | 100% | 194 KB | 0 |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E C C | 3,749 | 9,366 | 1.8 | 72% | 9% | 99% | 5,601 KB | 1 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E E A | 3,743 | 4,146 | 16.2 | 42% | 20% | 99% | 450 KB | 12 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F C | 3,672 | 42,846 | 19.4 | 9% | 1% | 64% | 155 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,599 | 4,978 | 16.7 | 34% | 0% | 96% | 139 KB | 0 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E D C | 3,573 | 6,161 | 24.6 | 67% | 9% | 95% | 512 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E E B | 3,521 | 11,397 | 38.8 | 43% | 0% | 98% | 107 KB | 4 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 3,520 | 26,258 | 12.6 | 57% | 8% | 98% | 163 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E D B | 3,492 | 5,710 | 39.6 | 65% | 11% | 99% | 140 KB | 8 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E E C | 3,437 | 11,821 | 24.0 | 53% | 0% | 100% | 351 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 3,370 | 5,488 | 19.9 | 21% | 0% | 95% | 273 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F C | 3,358 | 5,037 | 0.0 | 22% | 45% | 97% | 432 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | E F B | 3,309 | 6,408 | 17.3 | 11% | 0% | 88% | 700 KB | 4 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 3,259 | 79,586 | 30.8 | 53% | 35% | 54% | 99 KB | 1 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | E C D | 3,200 | 9,722 | 0.3 | 74% | 21% | – | 53 KB | 0 |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 3,194 | 17,245 | 22.3 | 13% | 40% | 91% | 215 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 3,166 | 51,189 | 16.6 | 19% | 15% | 99% | 378 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 3,021 | 10,012 | 24.9 | 31% | 10% | 89% | 69 KB | 10 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | E F A | 3,007 | 12,031 | 18.5 | 64% | 4% | 100% | 41 KB | 3 |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 2,977 | 8,818 | 11.8 | 52% | 0% | 100% | 396 KB | 12 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E E B | 2,973 | 3,659 | 10.2 | 47% | 22% | 100% | 523 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 2,962 | 9,461 | 13.5 | 41% | 21% | 98% | 236 KB | 5 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,895 | 4,278 | 2.1 | 57% | 0% | 100% | 183 KB | 7 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 2,874 | 6,412 | 0.0 | 18% | 0% | 100% | 472 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,782 | 9,969 | 7.1 | 13% | 0% | 93% | 545 KB | 11 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E E B | 2,737 | 10,431 | 16.5 | 52% | 0% | 94% | 90 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,723 | 17,243 | 16.2 | 45% | 52% | 99% | 386 KB | 2 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E D B | 2,702 | 3,102 | 43.8 | 66% | 52% | 100% | 319 KB | 2 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F C | 2,695 | 6,435 | 14.2 | 6% | 10% | 68% | 269 KB | 1 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 2,686 | 17,894 | 23.5 | 47% | 0% | 99% | 178 KB | 0 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E E D | 2,575 | 5,154 | 38.7 | 54% | 10% | – | 198 KB | 3 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,574 | 11,600 | 13.4 | 11% | 0% | 96% | 589 KB | 2 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 2,561 | 7,100 | 27.8 | 30% | 42% | 100% | 407 KB | 17 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 2,477 | 5,452 | 7.3 | 38% | 0% | 96% | 522 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 2,470 | 3,218 | 14.3 | 70% | 0% | 100% | 4,314 KB | 22 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,395 | 7,939 | 6.8 | 56% | 10% | 98% | 134 KB | 231 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,371 | 7,816 | 10.5 | 41% | 0% | 0% | 285 KB | 25 (+1) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E F B | 2,329 | 20,707 | 6.5 | 36% | 27% | 78% | 83 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 2,263 | 2,989 | 14.9 | 36% | 26% | 100% | 215 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 2,173 | 7,434 | 0.0 | 55% | 32% | – | 741 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 2,128 | 7,100 | 21.2 | 30% | 42% | 99% | 544 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,100 | 5,004 | 21.0 | 13% | 34% | 97% | 88 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E E E | 2,099 | 9,053 | 15.4 | 53% | 9% | 100% | 1,056 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,051 | 8,014 | 0.1 | 29% | 5% | 84% | 395 KB | 3 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 2,048 | 3,345 | 19.9 | 57% | 0% | 95% | 502 KB | 0 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E D E | 2,040 | 11,894 | 19.5 | 70% | 20% | 99% | 626 KB | 11 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,935 | 2,502 | 31.0 | 64% | 6% | 99% | 980 KB | 109 (+3) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,935 | 3,875 | 9.8 | 68% | 17% | 90% | 161 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | E F B | 1,916 | 10,158 | 2.1 | 43% | 38% | 99% | 41 KB | 0 |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,902 | 3,473 | 15.3 | 29% | 10% | 100% | 61 KB | 0 |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | E E E | 1,898 | 5,105 | 0.0 | 79% | 0% | 100% | 497 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 1,772 | 2,948 | 17.8 | 42% | 0% | 99% | 127 KB | 23 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,735 | 13,456 | 0.0 | 0% | 0% | – | 200 KB | 28 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,714 | 2,555 | 9.8 | 26% | 0% | 95% | 87 KB | 1 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E F B | 1,707 | 6,033 | 5.0 | 33% | 15% | 99% | 57 KB | 1 |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F B | 1,673 | 16,391 | 22.6 | 48% | 0% | 83% | 153 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F B | 1,524 | 22,957 | 0.0 | 13% | 30% | 96% | 554 KB | 29 (+1) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 1,504 | 9,258 | 32.6 | 93% | 0% | 73% | 188 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 1,486 | 8,198 | 24.4 | 51% | 0% | 100% | 393 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E D D | 1,469 | 10,543 | 4.0 | 67% | 10% | – | 296 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,454 | 3,772 | 0.0 | 43% | 0% | 42% | 266 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,421 | 5,362 | 27.5 | 0% | 19% | 100% | 526 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,421 | 2,236 | 25.5 | 52% | 45% | 81% | 203 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,361 | 3,380 | 5.4 | 10% | 17% | 67% | 7,014 KB | 18 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 1,355 | 2,609 | 37.0 | 10% | 0% | 97% | 234 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,343 | 8,423 | 6.3 | 42% | 10% | 93% | 288 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 1,321 | 1,307 | 10.6 | 9% | 0% | 100% | 67 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 1,249 | 31,731 | 0.2 | 32% | 0% | 31% | 1,473 KB | 1,108 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,233 | 8,050 | 5.9 | 7% | 0% | 99% | 76 KB | 2 |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,228 | 2,339 | 15.7 | 8% | 0% | – | 53 KB | 3 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | E F C | 1,195 | 1,988 | 0.0 | 37% | 0% | 99% | 437 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 1,115 | 4,189 | 10.7 | 0% | 0% | – | 86 KB | 2 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,047 | 4,127 | 8.5 | 57% | 0% | 98% | 342 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | E F E | 1,040 | 26,426 | 5.0 | 69% | 7% | 86% | 149 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,027 | 2,510 | 12.5 | 9% | 0% | 94% | 571 KB | 2 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 922 | 5,516 | 0.2 | 6% | 0% | 76% | 152 KB | 29 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 869 | 2,299 | 0.0 | 44% | 0% | 94% | 268 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | 867 | 4,735 | 0.0 | 78% | 0% | 0% | 324 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 790 | 2,592 | 4.9 | 0% | 0% | 74% | 161 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 788 | 1,179 | 8.5 | 0% | 0% | 80% | 552 KB | 2 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 785 | 2,239 | 23.9 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 775 | 4,098 | 1.4 | 58% | 0% | 96% | 52 KB | 0 |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 737 | 4,410 | 11.5 | 2% | 0% | 99% | 92 KB | 1 |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F D | 708 | 2,124 | 26.9 | 46% | 0% | 47% | 100 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 685 | 4,042 | 12.8 | 0% | 0% | – | 411 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 666 | 3,277 | 0.0 | 11% | 0% | 33% | 399 KB | 462 (+1) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F E C | 620 | 2,495 | 17.1 | 67% | 0% | 98% | 426 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 541 | 2,652 | 28.5 | 26% | 0% | 98% | 122 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 534 | 11,170 | 4.6 | 22% | 0% | 91% | 650 KB | 6 |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 487 | 1,094 | 3.5 | 10% | 0% | 100% | 1,118 KB | 5 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 482 | 420,804 | 50.4 | 14% | 0% | 100% | 703 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | 421 | 2,104 | 34.5 | 40% | 8% | 100% | 403 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 421 | 1,673 | 13.7 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 406 | 56,104 | 0.0 | 48% | 12% | – | 8,190 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 374 | 6,888 | 0.0 | 16% | 0% | – | 144 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 372 | 589 | 0.1 | 62% | 18% | 0% | 655 KB | 3 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 321 | 4,295 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 309 | 1,544 | 20.1 | 0% | 0% | 91% | 442 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 308 | 4,351 | 15.1 | 59% | 0% | 76% | 1,538 KB | 6 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 301 | 9,427 | 11.6 | 46% | 12% | 94% | 5,219 KB | 40,285 |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 300 | 9,572 | 0.0 | 33% | 4% | 99% | 478 KB | 6 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 239 | 3,473 | 0.0 | 18% | 0% | 0% | 1,157 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 236 | 1,011 | 20.4 | 0% | 0% | 12% | 279 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 222 | 4,409 | 7.2 | 39% | 0% | 98% | 151 KB | 2 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 158 | 3,273 | 29.8 | 72% | 0% | 99% | 317 KB | 159 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 106 | 75,203 | 0.0 | 31% | 0% | – | 110 KB | 0 |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 90 | 2,181 | 16.3 | 0% | 0% | 93% | 314 KB | 23 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 57 | 702 | 6.9 | 55% | 0% | 83% | 15 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 18 | 9,669 | 16.8 | 16% | 0% | 93% | 576 KB | 1 (+1) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 1 | 1,731 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 3,675 | 41.8 | 0% | 0% | 52% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 38.4 | 58% | 32% | 85% | 2,197 KB | 1,443 (+2) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 2,616 | 32.6 | 0% | 0% | 91% | 2,600 KB | 36 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | 0 | 4,554 | 26.6 | 16% | 0% | 98% | 231 KB | 1 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F E C | – | – | 22.9 | 50% | 15% | 96% | 342 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | 0 | 849 | 21.9 | 62% | 0% | 98% | 363 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F D B | – | – | 21.0 | 62% | 0% | 97% | 980 KB | 4 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | F F A | 0 | 9,688 | 19.6 | 14% | 0% | 97% | 221 KB | 5 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 2,256 | 18.9 | 0% | 0% | 98% | 489 KB | 54 (+2) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 17.8 | – | – | 97% | 94 KB | 16 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 0 | 720 | 17.6 | 0% | 0% | 100% | 617 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 1,457 | 16.4 | 0% | 0% | 96% | 66 KB | 3 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 5 | 16.1 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 6,206 | 14.4 | 0% | 0% | – | 416 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 472 | 14.0 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 2,949 | 14.0 | 0% | 0% | 97% | 49 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 13.6 | – | – | – | 55 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 0 | 494 | 12.8 | 0% | 0% | 98% | 43 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 3,543 | 11.6 | 53% | 0% | 99% | 298 KB | 5 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 486 | 11.4 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 0 | 303 | 11.3 | 15% | 0% | 90% | 6,579 KB | 8 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 53 | 9.9 | 0% | 0% | 89% | 38 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 9.9 | 0% | 0% | 98% | 723 KB | 5 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 936 | 9.6 | 0% | 0% | 99% | 99 KB | 4 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 2,052 | 8.2 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 7.9 | – | – | 98% | 149 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 10,940 | 7.9 | 40% | 0% | – | 100 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 885 | 7.4 | 20% | 0% | 96% | 787 KB | 2 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F C | – | – | 7.0 | 22% | 0% | 58% | 206 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 6.6 | – | – | 90% | 195 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 868 | 5.8 | 0% | 0% | 96% | 24 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 5.7 | 28% | 31% | 0% | 1,879 KB | 458 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 5.6 | – | – | – | 115 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 126 | 4.2 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F E E | 0 | 907 | 3.7 | 51% | 51% | 22% | 115 KB | 0 |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1 | 2.8 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 4,058 | 2.7 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 713 | 2.7 | 0% | 0% | 96% | 163 KB | 12 (+1) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,163 | 1.8 | 0% | 0% | 33% | 141 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 1.8 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 0 | 1.4 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 62% | 0% | 79% | 816 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 76% | 11% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 583 | 0.1 | 0% | 0% | 15% | 904 KB | 1,294 (+3) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | F F D | 0 | 5,144 | 0.0 | 46% | 0% | 24% | 1,113 KB | 34 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 564 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F B | – | – | 0.0 | 32% | 0% | 73% | 84 KB | 5 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 641 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | 0 | 11,438 | 0.0 | 39% | 0% | 100% | 1,234 KB | 12 |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 0 | 0.0 | – | – | – | 18 KB | 0 (+0) |
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
