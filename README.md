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
_361 repos, last measured 2026-10-28. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 69,503 | 241,658 | 122 | 54% | 0% | 51% | 307 KB | 4 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | A E B | 65,797 | 108,896 | 33.9 | 48% | 39% | 100% | 3,196 KB | 6 (+1) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A D D | 50,387 | 152,187 | 0.2 | 65% | 16% | 27% | 1,271 KB | 440 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 49,535 | 61,666 | 72.6 | 6% | 42% | 91% | 3,150 KB | 2,047 (+7) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 44,279 | 99,996 | 172 | 31% | 23% | 89% | 2,294 KB | 4 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A D B | 41,990 | 48,445 | 56.4 | 69% | 59% | 93% | 958 KB | 1 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E B | 41,857 | 81,586 | 35.5 | 62% | 38% | 82% | 198 KB | 0 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | A B B | 41,396 | 84,532 | 25.8 | 85% | 12% | 100% | 780 KB | 4 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B B B | 35,788 | 50,355 | 0.0 | 82% | 50% | 83% | 201 KB | 113 (+1) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | B F A | 35,099 | 82,302 | 60.8 | 47% | 0% | 95% | 210 KB | 122 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | B E B | 32,170 | 41,194 | 33.6 | 46% | 36% | 90% | 604 KB | 11 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B E A | 30,038 | 32,382 | 81.6 | 55% | 19% | 99% | 60 KB | 0 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 29,514 | 34,529 | 31.7 | 39% | 29% | 100% | 1,416 KB | 92 (+1) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | B C D | 29,298 | 67,340 | 0.0 | 77% | 43% | – | 201 KB | 0 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | B F B | 28,876 | 108,230 | 21.0 | 1% | 10% | 84% | 213 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 28,515 | 40,360 | 17.7 | 36% | 17% | 83% | 6,732 KB | 127 (+2) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | B E A | 28,133 | 89,364 | 32.3 | 46% | 13% | 100% | 404 KB | 80 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 27,737 | 33,326 | 96.0 | 29% | 64% | 91% | 3,859 KB | 77 (+1) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | B E A | 27,477 | 34,287 | 28.1 | 58% | 45% | 91% | 312 KB | 1 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | B C A | 27,226 | 54,600 | 14.1 | 84% | 3% | 88% | 353 KB | 0 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | B F A | 25,861 | 52,092 | 30.1 | 56% | 18% | 99% | 49 KB | 23,779 (+7) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B D C | 25,545 | 40,505 | 73.0 | 66% | 10% | 88% | 549 KB | 2 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | B E D | 25,171 | 32,459 | 0.0 | 55% | 16% | 31% | 268 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B E C | 24,903 | 29,217 | 102 | 42% | 65% | 76% | 371 KB | 74 (+2) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B D B | 24,666 | 29,708 | 30.4 | 69% | 2% | 82% | 706 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B B D | 24,586 | 463,485 | 0.0 | 86% | 0% | 0% | 3,286 KB | 1 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C D | 24,539 | 36,628 | 30.9 | 70% | 22% | 89% | 363 KB | 10 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B D C | 24,332 | 36,371 | 26.4 | 66% | 15% | 99% | 722 KB | 9 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B B B | 24,151 | 39,982 | 22.1 | 86% | 41% | 86% | 767 KB | 5 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B C B | 23,649 | 112,407 | 30.9 | 78% | 46% | 94% | 986 KB | 33 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B B C | 23,056 | 29,503 | 0.0 | 88% | 58% | 60% | 309 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | B E A | 22,910 | 25,225 | 12.7 | 53% | 15% | 91% | 257 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | B E A | 22,565 | 40,427 | 40.5 | 43% | 2% | 98% | 240 KB | 9 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B D C | 22,374 | 26,652 | 29.6 | 65% | 45% | 100% | 315 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B E B | 21,771 | 56,551 | 9.7 | 59% | 27% | 76% | 293 KB | 334 (+2) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B D B | 21,284 | 26,442 | 43.0 | 62% | 18% | 94% | 526 KB | 1 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | B F C | 21,041 | 32,043 | 44.9 | 9% | 7% | 99% | 249 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 20,521 | 54,219 | 57.8 | 4% | 0% | 0% | 3,975 KB | 1 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | B E D | 20,497 | 80,653 | 0.0 | 49% | 52% | 0% | 296 KB | 0 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B F A | 20,376 | 39,487 | 116 | 38% | 17% | 98% | 296 KB | 16 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B F B | 20,111 | 24,647 | 17.3 | 72% | 0% | 97% | 361 KB | 1,588 (+2) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C D B | 19,968 | 219,551 | 1.4 | 70% | 42% | 87% | 3,340 KB | 7 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 19,642 | 36,815 | 0.0 | 85% | 67% | – | 1,222 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 19,155 | 25,908 | 25.4 | 59% | 35% | 100% | 179 KB | 33 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | C E B | 19,056 | 34,919 | 41.6 | 59% | 69% | 98% | 549 KB | 2 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F B | 18,180 | 37,684 | 0.0 | 33% | 5% | 92% | 674 KB | 1 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 18,121 | 28,052 | 0.0 | 50% | 41% | 100% | 4,357 KB | 15 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C C B | 17,645 | 20,702 | 24.5 | 72% | 0% | 91% | 1,105 KB | 8 (+2) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 17,585 | 28,438 | 21.1 | 74% | 31% | 92% | 197 KB | 6 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | C F E | 17,171 | 35,975 | 46.0 | 43% | 12% | 96% | 20,146 KB | 1 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | C F B | 17,094 | 26,054 | 13.0 | 38% | 0% | 93% | 781 KB | 0 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | C C C | 16,964 | 17,745 | 10.4 | 74% | 7% | 100% | 49 KB | 3 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C C A | 16,644 | 31,840 | 46.4 | 73% | 41% | 98% | 346 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,327 | 36,431 | 37.6 | 1% | 49% | 97% | 225 KB | 7 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C E B | 16,287 | 156,400 | 44.2 | 59% | 18% | 78% | 416 KB | 9 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C C B | 16,257 | 20,919 | 21.2 | 76% | 35% | 71% | 608 KB | 1 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | C E D | 15,918 | 26,530 | 0.1 | 64% | 9% | 36% | 2,883 KB | 2 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F D | 15,705 | 21,747 | 31.9 | 52% | 24% | 100% | 599 KB | 22 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | C B B | 15,481 | 40,434 | 38.8 | 87% | 14% | 97% | 200 KB | 8 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C C A | 15,466 | 177,252 | 38.2 | 80% | 20% | 100% | 158 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,352 | 20,075 | 5.8 | 7% | 0% | 95% | 439 KB | 138 (+1) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 15,342 | 23,109 | 39.6 | 38% | 54% | 100% | 1,344 KB | 8 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 14,940 | 23,232 | 65.1 | 45% | 66% | 97% | 275 KB | 6,444 (+9) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 14,464 | 31,311 | 25.5 | 51% | 18% | 86% | 480 KB | 21 (+1) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C D A | 14,023 | 18,234 | 36.4 | 64% | 44% | 88% | 102 KB | 232 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C C B | 13,855 | 25,662 | 33.2 | 77% | 46% | 88% | 1,393 KB | 70,401 (+34) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | C E B | 13,828 | 144,421 | 92.4 | 55% | 28% | 99% | 611 KB | 2 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | C E A | 13,685 | 35,883 | 64.0 | 74% | 0% | 100% | 169 KB | 2 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C C B | 13,573 | 20,061 | 42.1 | 75% | 1% | 98% | 196 KB | 1 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 13,398 | 51,705 | 50.5 | 25% | 52% | 100% | 59 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C E B | 12,949 | 20,601 | 184 | 56% | 54% | 99% | 2,355 KB | 1 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | C B B | 12,794 | 15,902 | 8.8 | 87% | 30% | 99% | 363 KB | 1 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C F B | 12,728 | 13,926 | 41.6 | 52% | 9% | 99% | 798 KB | 2 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | C E B | 12,590 | 20,331 | 21.5 | 40% | 0% | 96% | 528 KB | 81 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | C F C | 12,528 | 56,610 | 25.7 | 33% | 0% | 53% | 4,722 KB | 96 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C E D | 12,439 | 22,778 | 0.4 | 52% | 14% | – | 414 KB | 1 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 12,222 | 17,008 | 0.0 | 55% | 25% | 30% | 308 KB | 281 (+3) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 12,064 | 13,247 | 14.3 | 59% | 23% | 84% | 1,202 KB | 13 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C F D | 12,058 | 30,189 | 71.8 | 32% | 29% | 25% | 837 KB | 16 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 12,051 | 17,028 | 38.0 | 79% | 36% | 100% | 2,202 KB | 5 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C C C | 11,968 | 19,644 | 15.3 | 71% | 41% | 64% | 500 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | C E D | 11,959 | 15,992 | 0.0 | 49% | 0% | – | 315 KB | 0 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C E B | 11,801 | 211,776 | 43.8 | 58% | 33% | 95% | 1,431 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 10,769 | 11.4 | 46% | 0% | 92% | 718 KB | 9 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | C C A | 11,673 | 35,528 | 6.7 | 72% | 25% | 87% | 21 KB | 0 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C E D | 11,413 | 24,147 | 0.0 | 54% | 29% | 24% | 154 KB | 114 (+1) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | C E A | 11,379 | 12,279 | 27.9 | 78% | 32% | 100% | 162 KB | 5 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 10,949 | 12,573 | 0.0 | 89% | 36% | – | 203 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | C F B | 10,900 | 33,378 | 18.3 | 49% | 0% | 76% | 260 KB | 2 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | C D A | 10,851 | 144,774 | 0.0 | 66% | 6% | 93% | 211 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 10,723 | 97,446 | 16.8 | 60% | 38% | 97% | 506 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 10,712 | 13,390 | 25.8 | 85% | 43% | 100% | 200 KB | 6 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [ijun17/centralu](https://github.com/ijun17/centralu) | C F B | 10,456 | 14,867 | 25.1 | 37% | 0% | 96% | 628 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | C F B | 10,391 | 13,689 | 29.5 | 18% | 16% | 94% | 160 KB | 10 (+2) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | C F C | 10,373 | 27,412 | 0.0 | 30% | 24% | 99% | 923 KB | 28 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C E D | 10,074 | 35,307 | 11.6 | 47% | 5% | 0% | 142 KB | 15 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | C E B | 10,021 | 24,152 | 8.6 | 46% | 39% | 83% | 680 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D C D | 9,882 | 15,020 | 8.3 | 73% | 0% | 29% | 198 KB | 8 (+4) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 9,836 | 23,224 | 2.6 | 16% | 0% | 80% | 1,423 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D C B | 9,393 | 475,330 | 33.9 | 71% | 6% | 86% | 1,414 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 9,073 | 15,897 | 38.0 | 55% | 51% | 100% | 563 KB | 5 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C B | 9,063 | 19,380 | 17.5 | 78% | 51% | 84% | 133 KB | 5 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | D C D | 9,057 | 17,495 | 0.0 | 75% | 19% | 43% | 535 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D E D | 8,959 | 13,636 | 0.0 | 46% | 15% | 0% | 601 KB | 1 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D E B | 8,850 | 13,819 | 30.2 | 63% | 30% | 95% | 1,556 KB | 3 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | D C B | 8,817 | 22,512 | 35.1 | 75% | 2% | 100% | 571 KB | 37 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D F B | 8,788 | 114,809 | 14.3 | 50% | 15% | 83% | 126 KB | 4 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 8,527 | 57,705 | 19.0 | 40% | 0% | 99% | 251 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F C | 8,463 | 9,159 | 21.2 | 14% | 33% | 98% | 544 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D C C | 8,448 | 27,813 | 0.0 | 81% | 19% | 100% | 503 KB | 1 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D B B | 8,383 | 15,456 | 13.4 | 87% | 5% | 95% | 361 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D F C | 8,233 | 15,426 | 22.5 | 66% | 0% | 89% | 43 KB | 17 (+1) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 7,980 | 11,466 | 10.4 | 73% | 4% | 70% | 343 KB | 22 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D D B | 7,953 | 13,919 | 0.4 | 64% | 9% | 70% | 376 KB | 1 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D B C | 7,879 | 9,972 | 15.7 | 86% | 22% | 94% | 147 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | D F B | 7,850 | 12,938 | 33.7 | 59% | 0% | 99% | 79 KB | 3 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F D | 7,842 | 9,680 | 18.3 | 19% | 0% | 80% | 377 KB | 7 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D E B | 7,837 | 9,160 | 15.0 | 41% | 28% | 92% | 329 KB | 164 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D E B | 7,790 | 15,432 | 10.0 | 80% | 40% | 99% | 89 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,755 | 8,681 | 5.3 | 15% | 48% | 89% | 3,781 KB | 546 (-1) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 7,719 | 17,165 | 3.7 | 75% | 0% | 90% | 319 KB | 1 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | D E A | 7,671 | 14,016 | 55.3 | 46% | 33% | 96% | 135 KB | 1 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 7,573 | 12,166 | 6.7 | 37% | 42% | 93% | 385 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | D F C | 7,567 | 13,617 | 6.7 | 28% | 2% | 91% | 3,845 KB | 1 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D C C | 7,338 | 7,476 | 24.9 | 76% | 60% | 96% | 960 KB | 1 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D D D | 7,309 | 15,326 | 6.7 | 61% | 37% | – | 484 KB | 2 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D F C | 7,303 | 22,581 | 3.0 | 39% | 8% | 96% | 2,284 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 7,231 | 10,834 | 0.1 | 22% | 10% | 86% | 906 KB | 2 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 7,159 | 7,481 | 25.7 | 50% | 0% | 100% | 640 KB | 0 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | D F C | 7,156 | 76,075 | 5.5 | 47% | 0% | 91% | 78 KB | 0 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F B | 6,778 | 12,583 | 45.1 | 0% | 15% | 82% | 67 KB | 62 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D D C | 6,757 | 10,912 | 0.1 | 70% | 9% | 94% | 381 KB | 2 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D E B | 6,666 | 12,402 | 31.4 | 54% | 4% | 100% | 1,060 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | D E C | 6,658 | 20,303 | 0.0 | 50% | 13% | 100% | 958 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 6,644 | 8,737 | 42.9 | 4% | 51% | 80% | 334 KB | 1 (+1) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | D F B | 6,583 | 40,852 | 20.8 | 37% | 0% | 86% | 155 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F A | 6,546 | 15,109 | 27.3 | 61% | 0% | 100% | 377 KB | 49 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 6,516 | 39,329 | 0.0 | 63% | 10% | 50% | 483 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D E B | 6,444 | 8,479 | 17.9 | 78% | 0% | 100% | 569 KB | 1 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | D F B | 6,420 | 13,768 | 9.1 | 60% | 0% | 96% | 45 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | D E D | 6,280 | 15,912 | 1.3 | 47% | 2% | 76% | 85 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | D F B | 6,100 | 19,370 | 15.1 | 69% | 0% | 91% | 86 KB | 6 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D B B | 6,057 | 7,637 | 0.0 | 84% | 2% | 90% | 590 KB | 1 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | D E D | 6,029 | 12,102 | 0.0 | 44% | 3% | – | 321 KB | 2 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D F C | 5,958 | 8,621 | 15.2 | 56% | 0% | 88% | 376 KB | 2 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D E C | 5,939 | 9,949 | 20.8 | 56% | 28% | 100% | 39 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D E B | 5,923 | 11,651 | 0.0 | 64% | 12% | 73% | 246 KB | 0 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | D E B | 5,889 | 20,985 | 14.4 | 52% | 33% | 80% | 518 KB | 19 (+1) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D F C | 5,852 | 13,757 | 10.7 | 34% | 48% | 52% | 42 KB | 13 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D F B | 5,544 | 6,618 | 65.9 | 65% | 11% | 100% | 797 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | D E B | 5,468 | 6,205 | 10.1 | 49% | 25% | 99% | 80 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 5,397 | 11,139 | 52.2 | 50% | 34% | – | 401 KB | 3 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D C B | 5,362 | 15,819 | 30.6 | 73% | 69% | 100% | 1,172 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D C C | 5,265 | 8,919 | 11.4 | 70% | 0% | 99% | 137 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D F B | 5,244 | 6,367 | 7.5 | 57% | 0% | 88% | 670 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | D F E | 5,196 | 9,882 | 15.7 | 18% | 0% | 69% | 332 KB | 1 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | D E B | 5,086 | 14,184 | 18.2 | 77% | 0% | 85% | 90 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | D F B | 5,067 | 5,967 | 17.1 | 29% | 20% | 96% | 139 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 5,052 | 20,148 | 43.9 | 5% | 2% | 100% | 83 KB | 2 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | E C A | 4,988 | 8,064 | 37.5 | 78% | 0% | 100% | 126 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 4,942 | 8,075 | 0.2 | 38% | 19% | 0% | 518 KB | 0 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 4,881 | 7,089 | 23.1 | 38% | 17% | 90% | 1,116 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 4,865 | 15,118 | 23.5 | 42% | 11% | 84% | 76 KB | 10 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E F E | 4,739 | 7,215 | 22.4 | 39% | 7% | 84% | 1,169 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | E F B | 4,634 | 7,757 | 33.1 | 0% | 0% | 99% | 884 KB | 4 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E C D | 4,600 | 5,183 | 0.9 | 80% | 47% | 0% | 179 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 4,347 | 7,579 | 41.2 | 70% | 0% | – | 440 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E E B | 4,336 | 6,383 | 23.2 | 59% | 12% | 100% | 199 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,194 | 7,749 | 25.1 | 18% | 0% | 100% | 840 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | E F C | 4,007 | 7,974 | 64.4 | 28% | 7% | 97% | 695 KB | 14 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,845 | 28,452 | 16.1 | 38% | 44% | 100% | 386 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 3,749 | 9,037 | 1.8 | 67% | 0% | 100% | 5,602 KB | 1 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E E A | 3,743 | 4,061 | 16.2 | 46% | 14% | 99% | 450 KB | 12 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,576 | 9,954 | 0.0 | 29% | 12% | 0% | 467 KB | 4 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E E C | 3,485 | 27,290 | 12.9 | 68% | 11% | 99% | 165 KB | 1 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E E C | 3,437 | 12,045 | 24.4 | 52% | 11% | 100% | 352 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E F B | 3,240 | 3,695 | 23.3 | 64% | 0% | 100% | 132 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 3,194 | 18,158 | 22.9 | 17% | 41% | 90% | 215 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 3,166 | 48,518 | 17.1 | 21% | 7% | 98% | 378 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 3,085 | 10,044 | 38.6 | 37% | 0% | 98% | 107 KB | 4 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 3,050 | 5,461 | 10.2 | 12% | 0% | – | 87 KB | 2 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | E F A | 3,007 | 11,122 | 20.0 | 69% | 4% | 100% | 41 KB | 3 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 2,977 | 5,947 | 11.7 | 32% | 0% | 100% | 398 KB | 12 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E E B | 2,973 | 3,447 | 9.6 | 43% | 1% | 100% | 523 KB | 1 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | E E D | 2,955 | 6,992 | 0.4 | 74% | 24% | – | 53 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,943 | 3,185 | 42.1 | 60% | 23% | 98% | 329 KB | 2 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E F C | 2,918 | 5,870 | 25.6 | 57% | 10% | 95% | 512 KB | 0 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 2,874 | 5,337 | 0.0 | 12% | 0% | 100% | 472 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | E F B | 2,872 | 12,965 | 5.0 | 28% | 0% | 86% | 261 KB | 1,243 (+7) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E E B | 2,827 | 3,689 | 9.8 | 71% | 3% | 91% | 438 KB | 2 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,782 | 6,374 | 7.1 | 33% | 0% | 91% | 542 KB | 11 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 2,686 | 17,085 | 22.0 | 40% | 0% | 98% | 178 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 2,659 | 4,436 | 19.6 | 5% | 0% | 100% | 152 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E E D | 2,575 | 5,647 | 39.8 | 55% | 34% | – | 198 KB | 3 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F C | 2,512 | 4,489 | 0.0 | 29% | 36% | 97% | 439 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | E F C | 2,477 | 5,452 | 7.3 | 38% | 0% | 96% | 522 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 2,476 | 6,611 | 19.3 | 35% | 8% | 95% | 46 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E F C | 2,401 | 6,379 | 13.8 | 26% | 0% | 95% | 8,119 KB | 1 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 2,374 | 20,173 | 14.7 | 39% | 23% | 100% | 216 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 2,374 | 2,365 | 14.0 | 60% | 0% | 100% | 4,314 KB | 22 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,373 | 3,043 | 18.0 | 16% | 0% | 100% | 127 KB | 23 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,371 | 7,623 | 9.8 | 35% | 0% | 0% | 285 KB | 25 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 2,355 | 4,742 | 19.9 | 26% | 0% | 98% | 273 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E F B | 2,329 | 20,517 | 6.6 | 30% | 26% | 80% | 83 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 2,317 | 32,296 | 0.2 | 33% | 0% | 31% | 1,473 KB | 1,110 (+2) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | E F D | 2,290 | 12,117 | 0.0 | 18% | 0% | – | 824 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,251 | 3,450 | 2.1 | 44% | 0% | 100% | 192 KB | 7 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 2,249 | 6,533 | 6.6 | 10% | 8% | 67% | 7,014 KB | 18 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,138 | 5,053 | 21.5 | 12% | 41% | 97% | 88 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E B E | 2,110 | 12,613 | 18.1 | 80% | 28% | 99% | 632 KB | 11 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,080 | 6,203 | 13.5 | 0% | 0% | 96% | 590 KB | 2 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,051 | 7,963 | 0.1 | 26% | 0% | 84% | 395 KB | 3 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 2,040 | 7,344 | 15.4 | 0% | 0% | – | 526 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | E F B | 2,000 | 11,277 | 2.9 | 62% | 31% | 100% | 42 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,935 | 3,139 | 9.9 | 61% | 21% | 90% | 161 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 1,920 | 3,684 | 6.5 | 39% | 14% | 98% | 134 KB | 231 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 1,880 | 4,460 | 8.7 | 58% | 34% | 98% | 343 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F C | 1,878 | 5,528 | 14.9 | 18% | 16% | 61% | 271 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,819 | 4,623 | 0.0 | 36% | 48% | 42% | 266 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E C D | 1,813 | 7,623 | 4.1 | 82% | 14% | – | 298 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,804 | 7,373 | 14.9 | 55% | 0% | 100% | 1,061 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,735 | 14,814 | 0.0 | 0% | 16% | – | 200 KB | 28 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E F B | 1,707 | 6,414 | 6.0 | 39% | 12% | 100% | 57 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E E A | 1,673 | 11,601 | 21.6 | 57% | 0% | 86% | 153 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,561 | 2,608 | 14.8 | 7% | 0% | – | 47 KB | 3 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 1,555 | 58,177 | 28.6 | 17% | 0% | 54% | 99 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 1,547 | 6,032 | 26.4 | 29% | 25% | 97% | 405 KB | 17 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 1,493 | 4,705 | 30.3 | 66% | 0% | 73% | 188 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E E A | 1,486 | 8,219 | 23.9 | 56% | 0% | 99% | 399 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 1,432 | 8,523 | 13.1 | 40% | 22% | 96% | 236 KB | 5 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,415 | 3,802 | 27.0 | 0% | 0% | 97% | 526 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,360 | 2,125 | 9.7 | 14% | 0% | 94% | 90 KB | 1 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 1,355 | 4,285 | 40.1 | 74% | 0% | 96% | 248 KB | 0 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 1,336 | 2,508 | 20.5 | 35% | 0% | 98% | 502 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,334 | 2,685 | 15.0 | 28% | 0% | 99% | 61 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 1,321 | 1,426 | 10.4 | 8% | 0% | 100% | 67 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,316 | 2,466 | 25.4 | 53% | 47% | 84% | 250 KB | 0 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F B | 1,233 | 6,611 | 6.0 | 6% | 0% | 99% | 80 KB | 2 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,166 | 7,335 | 6.4 | 16% | 14% | 95% | 337 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F B | 1,123 | 22,269 | 0.0 | 35% | 39% | 96% | 554 KB | 29 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | E F D | 1,121 | 5,429 | 0.0 | 60% | 0% | – | 3,234 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E D D | 1,050 | 5,837 | 0.0 | 66% | 0% | – | 803 KB | 2 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | E F E | 1,040 | 40,703 | 5.0 | 47% | 15% | 82% | 149 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 983 | 2,171 | 0.0 | 56% | 0% | 100% | 497 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 959 | 2,468 | 32.2 | 64% | 6% | 96% | 980 KB | 110 (+1) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 915 | 7,982 | 29.0 | 20% | 23% | 60% | 161 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 882 | 1,730 | 3.7 | 8% | 0% | 100% | 1,119 KB | 5 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F E D | 867 | 4,782 | 0.0 | 83% | 9% | 0% | 324 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 845 | 1,871 | 0.0 | 30% | 0% | 99% | 437 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 809 | 2,203 | 9.7 | 38% | 19% | 91% | 6,579 KB | 8 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 790 | 2,601 | 4.9 | 0% | 0% | 74% | 161 KB | 2 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F D | 708 | 2,124 | 26.9 | 47% | 0% | 47% | 100 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 685 | 3,294 | 11.9 | 0% | 0% | – | 414 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 666 | 3,491 | 0.0 | 20% | 0% | 33% | 399 KB | 462 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 634 | 4,807 | 0.0 | 10% | 0% | 0% | 1,155 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 620 | 2,419 | 16.9 | 38% | 0% | 98% | 428 KB | 1 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 583 | 2,244 | 13.1 | 44% | 0% | 87% | 625 KB | 3 (+1) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F B | 561 | 18,147 | 20.3 | 50% | 0% | 100% | 963 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 541 | 2,560 | 27.5 | 14% | 0% | 97% | 122 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | 534 | 11,785 | 5.0 | 25% | 0% | 91% | 650 KB | 6 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 521 | 3,726 | 1.4 | 51% | 0% | 96% | 52 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 482 | 124,407 | 49.4 | 20% | 0% | 100% | 703 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 477 | 4,702 | 15.7 | 16% | 0% | 88% | 700 KB | 4 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 462 | 6,541 | 0.0 | 11% | 0% | – | 144 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | 421 | 2,069 | 34.9 | 67% | 9% | 100% | 403 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 421 | 1,673 | 13.7 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 412 | 1,419 | 0.0 | 21% | 0% | 94% | 268 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 406 | 69,906 | 0.0 | 37% | 0% | – | 8,190 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 372 | 604 | 0.1 | 62% | 18% | 0% | 658 KB | 3 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 309 | 1,149 | 20.5 | 0% | 0% | 92% | 444 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 301 | 9,274 | 11.4 | 46% | 12% | 94% | 5,221 KB | 40,319 (+34) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 300 | 8,881 | 0.0 | 17% | 6% | 85% | 478 KB | 6 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 236 | 716 | 19.9 | 0% | 0% | 12% | 279 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 222 | 4,138 | 7.2 | 54% | 0% | 100% | 151 KB | 2 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 158 | 3,469 | 30.1 | 59% | 0% | 94% | 317 KB | 159 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 158 | 2,587 | 0.2 | 12% | 0% | 76% | 152 KB | 29 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 90 | 2,673 | 14.9 | 0% | 0% | 98% | 320 KB | 23 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 77 | 2,347 | 10.8 | 55% | 0% | 99% | 92 KB | 1 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 12 | 4,833 | 19.1 | 13% | 0% | 96% | 90 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 12 | 2,174 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 1 | 287 | 7.7 | 0% | 0% | 83% | 15 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 3,356 | 41.8 | 0% | 0% | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 38.3 | 52% | 28% | 88% | 2,197 KB | 1,447 (+4) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 2,051 | 30.6 | 0% | 0% | 88% | 2,600 KB | 36 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | 0 | 0 | 26.2 | – | – | 98% | 231 KB | 1 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 1,485 | 23.1 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F E C | – | – | 22.9 | 48% | 0% | 100% | 342 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | 0 | 264 | 21.9 | 0% | 0% | 98% | 363 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 21.1 | 65% | 0% | 98% | 980 KB | 4 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | F F A | 0 | 11,999 | 19.7 | 12% | 0% | 97% | 221 KB | 5 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 0 | 2,682 | 18.0 | 0% | 0% | 100% | 617 KB | 1 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 17.6 | – | – | 97% | 94 KB | 16 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 2,219 | 17.6 | 0% | 0% | 98% | 489 KB | 55 (+1) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 0 | 9,513 | 16.8 | 15% | 0% | 93% | 576 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 1,479 | 16.4 | 0% | 0% | 96% | 66 KB | 3 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 0 | 16.2 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | F F E | 0 | 2,276 | 15.2 | 42% | 0% | 76% | 1,538 KB | 6 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 2,232 | 14.0 | 0% | 0% | 97% | 49 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 0 | 0 | 12.8 | – | – | 98% | 43 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 12.4 | 0% | 0% | – | 55 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 514 | 12.4 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 465 | 11.4 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 1,136 | 10.0 | 0% | 0% | 99% | 298 KB | 5 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 49 | 9.9 | 0% | 0% | 88% | 38 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 420 | 9.7 | 0% | 0% | 99% | 99 KB | 4 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 888 | 8.5 | 0% | 0% | 80% | 552 KB | 2 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 8.3 | 0% | 0% | 98% | 723 KB | 6 (+1) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 2,035 | 8.2 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 10,088 | 8.1 | 0% | 0% | – | 100 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 7.3 | – | – | 98% | 149 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 367 | 7.2 | 0% | 0% | 96% | 787 KB | 2 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 7.0 | 10% | 0% | 4% | 206 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 6.5 | – | – | 90% | 195 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 1 | 5.4 | 0% | 0% | 96% | 24 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 4.8 | – | – | – | 115 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 4.8 | 28% | 35% | 0% | 1,879 KB | 458 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 4.1 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 0 | 863 | 4.1 | 0% | 0% | 95% | 163 KB | 13 (+1) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F E E | 0 | 1,913 | 3.8 | 58% | 51% | 17% | 115 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 2 | 2.9 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 1 | 2.7 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 1.6 | – | – | 100% | 59 KB | 1 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,163 | 1.4 | 0% | 0% | 33% | 144 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | 0 | 5,760 | 1.4 | 64% | 0% | – | 311 KB | 3 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 0 | 1.4 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 78% | 0% | 93% | 816 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 80% | 15% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 556 | 0.1 | 0% | 0% | 16% | 904 KB | 1,298 (+4) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F D | – | – | 0.1 | 29% | 0% | 49% | 84 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | F F D | 0 | 10,234 | 0.0 | 41% | 0% | 30% | 1,151 KB | 34 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 314 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 881 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | 0 | 1,963 | 0.0 | 0% | 0% | 100% | 1,234 KB | 12 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 202,195 | 0.0 | 28% | 0% | – | 110 KB | 0 (+0) |
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
