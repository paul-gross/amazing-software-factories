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
_361 repos, last measured 2026-10-31. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (361)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [goat-si/goat](https://github.com/goat-si/goat) | A C B | 108,078 | 134,010 | 48.8 | 75% | 32% | 100% | 3,196 KB | 19 (+2) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A E A | 83,765 | 110,254 | 34.2 | 55% | 18% | 100% | 406 KB | 81 (+1) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 67,983 | 230,171 | 122 | 57% | 4% | 51% | 307 KB | 4 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 50,793 | 61,418 | 72.7 | 5% | 11% | 98% | 3,207 KB | 2,068 (+11) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A B A | 43,125 | 61,833 | 23.1 | 84% | 29% | 95% | 207 KB | 6 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 42,429 | 44,409 | 63.2 | 79% | 45% | 97% | 1,003 KB | 1 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | A D B | 42,276 | 231,008 | 1.4 | 64% | 33% | 85% | 3,340 KB | 7 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | A C D | 40,441 | 66,769 | 0.0 | 73% | 32% | – | 209 KB | 0 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 37,787 | 116,948 | 160 | 34% | 29% | 89% | 2,294 KB | 4 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B F A | 34,679 | 47,914 | 139 | 29% | 14% | 93% | 146 KB | 19 (+1) |
| [purlis/purlis](https://github.com/purlis/purlis) | B E B | 32,136 | 52,920 | 36.2 | 58% | 32% | 92% | 665 KB | 11 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B C C | 31,797 | 60,524 | 30.6 | 71% | 14% | 67% | 794 KB | 4 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B D B | 31,100 | 47,339 | 0.0 | 66% | 47% | 75% | 223 KB | 115 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 29,514 | 32,839 | 33.2 | 35% | 38% | 100% | 1,495 KB | 93 (+1) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B C C | 29,078 | 44,239 | 30.4 | 72% | 48% | 98% | 725 KB | 9 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B B B | 27,985 | 34,419 | 49.5 | 83% | 20% | 90% | 554 KB | 1 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 27,894 | 47,299 | 40.5 | 68% | 50% | 98% | 549 KB | 2 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 27,737 | 47,963 | 99.3 | 29% | 32% | 90% | 4,590 KB | 79 (+1) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B A B | 27,508 | 36,880 | 37.8 | 92% | 46% | 84% | 799 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B D B | 27,047 | 28,368 | 22.2 | 70% | 44% | 94% | 782 KB | 5 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B F D | 24,796 | 38,031 | 0.1 | 37% | 8% | 14% | 2,851 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B E B | 23,797 | 26,592 | 104 | 56% | 44% | 76% | 373 KB | 74 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B F A | 23,542 | 43,001 | 40.6 | 44% | 24% | 99% | 203 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | B E B | 23,060 | 28,069 | 19.4 | 58% | 4% | 97% | 383 KB | 1,593 (+2) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | B C C | 23,056 | 27,987 | 0.0 | 74% | 16% | 68% | 321 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | B E D | 22,991 | 28,849 | 0.0 | 71% | 0% | 13% | 1,275 KB | 34 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | B E A | 22,910 | 21,148 | 11.6 | 56% | 8% | 98% | 259 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B F D | 22,731 | 67,289 | 0.1 | 38% | 10% | 26% | 1,271 KB | 440 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B C C | 22,373 | 38,748 | 27.5 | 70% | 57% | 99% | 315 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B D D | 21,971 | 28,994 | 28.2 | 66% | 18% | 97% | 363 KB | 10 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | B E A | 20,279 | 22,185 | 28.6 | 58% | 49% | 90% | 312 KB | 1 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 19,505 | 25,545 | 18.6 | 24% | 13% | 86% | 6,732 KB | 130 (+1) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 19,300 | 26,053 | 24.9 | 79% | 27% | 100% | 179 KB | 33 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 19,125 | 37,912 | 0.0 | 82% | 46% | – | 1,231 KB | 3 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 17,712 | 23,891 | 3.1 | 44% | 7% | 96% | 2,284 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C B B | 17,557 | 102,002 | 30.7 | 87% | 37% | 99% | 1,038 KB | 35 (+1) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 17,542 | 294,041 | 0.0 | 84% | 0% | 0% | 3,286 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C C B | 17,202 | 24,329 | 183 | 77% | 48% | 100% | 2,385 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C C A | 16,444 | 43,239 | 45.8 | 79% | 50% | 100% | 303 KB | 2 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C E C | 15,699 | 26,816 | 16.3 | 55% | 48% | 74% | 520 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,352 | 71,188 | 6.9 | 5% | 0% | 96% | 446 KB | 139 (+1) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C D B | 15,229 | 19,776 | 23.1 | 64% | 60% | 90% | 608 KB | 1 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | C D D | 15,195 | 17,108 | 13.9 | 61% | 9% | 46% | 7,014 KB | 19 (+1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C C D | 15,025 | 15,467 | 0.0 | 80% | 34% | – | 204 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E C | 14,808 | 21,484 | 68.5 | 51% | 57% | 67% | 275 KB | 6,487 (+8) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 14,735 | 41,763 | 24.8 | 25% | 39% | 99% | 486 KB | 21 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C E D | 14,416 | 26,822 | 12.9 | 58% | 26% | 0% | 144 KB | 15 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | C D A | 13,498 | 84,643 | 17.1 | 67% | 31% | 99% | 353 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | C E B | 13,419 | 17,620 | 12.9 | 46% | 27% | 84% | 42 KB | 13 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C D D | 13,129 | 60,521 | 0.0 | 64% | 38% | 27% | 156 KB | 116 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 12,924 | 23,897 | 0.0 | 55% | 25% | 100% | 4,357 KB | 15 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | C D B | 12,794 | 14,791 | 8.6 | 69% | 0% | 99% | 363 KB | 1 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 12,645 | 32,364 | 40.8 | 3% | 49% | 99% | 225 KB | 7 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C D D | 12,595 | 18,734 | 65.4 | 60% | 29% | 25% | 822 KB | 16 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 12,374 | 25,774 | 48.9 | 5% | 7% | 96% | 249 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C D B | 12,266 | 1,026,635 | 45.4 | 70% | 33% | 82% | 416 KB | 9 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | C F C | 12,221 | 30,206 | 0.0 | 34% | 19% | 99% | 948 KB | 29 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 12,064 | 14,280 | 14.5 | 46% | 37% | 81% | 1,214 KB | 13 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C D B | 11,390 | 37,185 | 30.6 | 68% | 62% | 73% | 1,402 KB | 70,506 (+28) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | C E D | 11,348 | 24,470 | 0.4 | 44% | 21% | – | 448 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | C E B | 11,341 | 200,739 | 44.0 | 55% | 5% | 92% | 1,431 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C E B | 11,332 | 11,942 | 46.1 | 58% | 10% | 99% | 865 KB | 2 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 11,207 | 19,635 | 41.0 | 34% | 55% | 100% | 1,336 KB | 8 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | C D B | 11,072 | 138,411 | 88.0 | 60% | 9% | 96% | 614 KB | 2 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 11,010 | 15,338 | 0.0 | 49% | 0% | 30% | 308 KB | 448 (+9) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | C F B | 10,900 | 12,605 | 25.4 | 23% | 0% | 96% | 628 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | C E B | 10,883 | 203,786 | 32.8 | 51% | 24% | 92% | 197 KB | 9 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C D C | 10,723 | 97,408 | 18.9 | 60% | 35% | 99% | 654 KB | 0 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | C E D | 10,549 | 16,242 | 0.0 | 43% | 27% | 45% | 284 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C E A | 10,461 | 11,866 | 30.1 | 55% | 31% | 95% | 102 KB | 233 (+1) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C C A | 10,218 | 26,549 | 81.1 | 76% | 2% | 96% | 60 KB | 0 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | C F B | 10,021 | 21,791 | 9.0 | 72% | 0% | 83% | 680 KB | 1 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D B C | 9,880 | 16,712 | 9.0 | 82% | 32% | 52% | 203 KB | 8 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D D C | 9,878 | 12,933 | 22.4 | 67% | 18% | 100% | 42 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 9,791 | 13,380 | 19.8 | 15% | 0% | 97% | 221 KB | 5 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D E C | 9,739 | 17,300 | 24.3 | 68% | 0% | 67% | 175 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 9,630 | 13,274 | 0.0 | 34% | 6% | 94% | 674 KB | 1 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 9,548 | 11,334 | 49.0 | 15% | 36% | 92% | 335 KB | 1 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | D B B | 9,491 | 19,897 | 38.1 | 87% | 8% | 100% | 2,217 KB | 5 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,479 | 34,313 | 0.0 | 77% | 2% | 100% | 530 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 9,444 | 17,256 | 25.8 | 64% | 0% | 92% | 1,112 KB | 8 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D C C | 9,286 | 15,208 | 9.2 | 75% | 11% | 100% | 49 KB | 3 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D E B | 9,159 | 15,039 | 0.0 | 63% | 15% | 72% | 283 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C B | 9,063 | 19,755 | 16.9 | 70% | 59% | 80% | 138 KB | 5 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F E | 8,905 | 27,274 | 55.7 | 8% | 4% | 64% | 3,975 KB | 1 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | D E C | 8,798 | 14,661 | 75.4 | 60% | 10% | 89% | 549 KB | 2 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D F B | 8,788 | 146,315 | 15.5 | 53% | 17% | 100% | 126 KB | 4 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | D E D | 8,786 | 13,884 | 0.0 | 73% | 0% | – | 356 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D C A | 8,660 | 10,300 | 40.1 | 70% | 2% | 100% | 128 KB | 1 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | D F B | 8,589 | 31,945 | 26.1 | 51% | 0% | 98% | 158 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D E D | 8,551 | 18,321 | 9.8 | 56% | 29% | – | 536 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 8,463 | 10,653 | 21.0 | 0% | 23% | 100% | 544 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D B C | 8,233 | 14,292 | 23.2 | 80% | 7% | 99% | 25 KB | 17 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 8,209 | 10,607 | 18.5 | 50% | 37% | 80% | 382 KB | 7 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | D F B | 8,016 | 13,529 | 37.8 | 35% | 0% | 100% | 83 KB | 3 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | D F B | 7,960 | 50,860 | 12.3 | 18% | 20% | 87% | 532 KB | 19 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | D F B | 7,919 | 25,421 | 9.1 | 44% | 11% | 73% | 296 KB | 338 (+1) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,755 | 10,908 | 5.7 | 8% | 48% | 88% | 3,917 KB | 548 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D C B | 7,719 | 16,369 | 13.9 | 79% | 52% | 96% | 379 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 7,668 | 11,729 | 0.1 | 30% | 14% | 86% | 919 KB | 2 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D E B | 7,653 | 14,143 | 11.1 | 70% | 0% | 91% | 89 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 7,640 | 95,219 | 12.1 | 17% | 4% | – | 89 KB | 2 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | D F C | 7,624 | 26,895 | 25.7 | 20% | 0% | 54% | 4,722 KB | 96 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D C B | 7,522 | 8,121 | 0.3 | 71% | 0% | 72% | 376 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 7,302 | 21,147 | 51.5 | 6% | 54% | 100% | 59 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | D F B | 7,216 | 25,104 | 6.0 | 29% | 0% | 91% | 569 KB | 6 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | D F B | 7,168 | 18,943 | 20.8 | 39% | 24% | 84% | 77 KB | 10 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D E B | 7,162 | 9,004 | 65.1 | 62% | 4% | 100% | 800 KB | 0 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 7,159 | 7,412 | 28.9 | 55% | 0% | 98% | 679 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | D F D | 7,016 | 17,357 | 29.8 | 63% | 14% | 89% | 599 KB | 22 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | D E A | 6,919 | 9,944 | 29.1 | 75% | 4% | 100% | 156 KB | 5 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D F B | 6,692 | 8,889 | 17.2 | 59% | 0% | 99% | 580 KB | 1 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | D D C | 6,658 | 19,167 | 0.0 | 67% | 70% | 100% | 863 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 6,628 | 11,842 | 47.9 | 58% | 2% | – | 406 KB | 3 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 6,607 | 11,582 | 28.9 | 9% | 16% | 95% | 160 KB | 10 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 6,516 | 33,694 | 0.0 | 62% | 17% | 50% | 532 KB | 1 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 6,401 | 13,546 | 0.1 | 47% | 7% | 100% | 391 KB | 2 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 6,343 | 12,672 | 45.7 | 54% | 3% | 100% | 85 KB | 2 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D D B | 6,032 | 13,821 | 0.0 | 62% | 18% | 96% | 590 KB | 1 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | D F D | 6,029 | 12,752 | 0.0 | 36% | 4% | – | 390 KB | 2 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D F C | 5,958 | 18,261 | 15.8 | 20% | 34% | 96% | 383 KB | 2 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 5,838 | 9,121 | 7.1 | 36% | 23% | 93% | 403 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | D B A | 5,796 | 11,321 | 27.4 | 86% | 42% | 99% | 200 KB | 6 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | D E D | 5,690 | 36,116 | 0.0 | 41% | 5% | 0% | 300 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 5,671 | 15,201 | 14.0 | 41% | 0% | 93% | 781 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | D F B | 5,433 | 13,439 | 8.6 | 59% | 0% | 98% | 45 KB | 0 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 5,286 | 15,230 | 22.0 | 60% | 0% | 99% | 532 KB | 82 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | D F A | 5,272 | 9,109 | 57.2 | 39% | 0% | 96% | 135 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 5,232 | 13,851 | 0.0 | 70% | 0% | – | 200 KB | 29 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 5,136 | 8,423 | 43.4 | 0% | 0% | 94% | 67 KB | 63 (+1) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | D C B | 5,086 | 16,558 | 22.2 | 80% | 10% | 86% | 92 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | D F B | 5,067 | 5,187 | 17.8 | 10% | 17% | 96% | 141 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 4,991 | 27,495 | 16.3 | 23% | 14% | 100% | 386 KB | 2 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 4,983 | 34,505 | 19.0 | 32% | 0% | 99% | 251 KB | 2 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E C B | 4,927 | 14,002 | 33.1 | 72% | 56% | 99% | 1,172 KB | 0 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 4,905 | 9,815 | 13.1 | 14% | 25% | 99% | 415 KB | 12 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 4,881 | 15,720 | 30.8 | 64% | 0% | 99% | 49 KB | 23,789 (+6) |
| [alexec/Agents](https://github.com/alexec/Agents) | E F E | 4,861 | 19,115 | 49.0 | 42% | 2% | 95% | 20,146 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E F D | 4,855 | 6,502 | 0.0 | 27% | 0% | 0% | 601 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | E E B | 4,818 | 10,626 | 31.3 | 70% | 0% | 99% | 571 KB | 37 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E E B | 4,799 | 18,386 | 9.0 | 65% | 35% | 84% | 26 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 4,766 | 6,311 | 7.9 | 44% | 0% | 91% | 685 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | E F B | 4,754 | 3,978 | 10.6 | 47% | 0% | 99% | 80 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E F E | 4,739 | 7,705 | 21.8 | 40% | 0% | 84% | 1,170 KB | 0 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E B | 4,707 | 41,776 | 26.6 | 59% | 0% | 81% | 59 KB | 1 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | E B A | 4,650 | 180,794 | 43.1 | 84% | 25% | 96% | 158 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 4,548 | 5,594 | 20.0 | 8% | 0% | 100% | 160 KB | 2 (+1) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | E F B | 4,519 | 7,887 | 27.6 | 32% | 35% | 100% | 1,594 KB | 3 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E B D | 4,504 | 5,048 | 1.0 | 83% | 39% | 0% | 185 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 4,482 | 7,959 | 20.4 | 26% | 3% | 77% | 260 KB | 2 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 4,477 | 8,634 | 43.6 | 31% | 31% | 100% | 582 KB | 5 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 4,350 | 8,591 | 0.0 | 64% | 0% | 93% | 224 KB | 0 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E D B | 4,336 | 6,282 | 26.5 | 65% | 12% | 100% | 207 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 4,318 | 5,589 | 0.4 | 36% | 12% | 0% | 518 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 4,292 | 22,398 | 42.5 | 68% | 46% | – | 440 KB | 1 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 4,207 | 9,980 | 1.3 | 2% | 21% | 76% | 85 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,194 | 8,624 | 24.1 | 7% | 5% | 100% | 849 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E E B | 4,121 | 456,290 | 28.9 | 56% | 6% | 88% | 1,414 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E F C | 4,060 | 7,297 | 13.9 | 71% | 9% | 95% | 155 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,925 | 8,125 | 29.5 | 30% | 16% | 100% | 388 KB | 17 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,923 | 5,490 | 12.5 | 54% | 0% | 98% | 142 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F C | 3,829 | 9,862 | 0.0 | 32% | 18% | 97% | 468 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | E F B | 3,750 | 21,539 | 2.9 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | E F B | 3,452 | 7,463 | 6.3 | 55% | 0% | 96% | 27 KB | 0 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 3,429 | 10,432 | 40.5 | 71% | 0% | 98% | 198 KB | 1 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E D D | 3,416 | 8,402 | 7.7 | 70% | 10% | 0% | 333 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 3,405 | 7,109 | 7.4 | 40% | 0% | 91% | 544 KB | 11 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 3,397 | 5,774 | 0.0 | 26% | 0% | 33% | 399 KB | 464 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | E F B | 3,389 | 14,166 | 5.4 | 54% | 0% | 86% | 262 KB | 1,250 (+2) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 3,374 | 33,994 | 37.1 | 53% | 0% | 98% | 240 KB | 9 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 3,374 | 7,862 | 0.0 | 58% | 0% | 0% | 1,189 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 3,296 | 76,827 | 23.0 | 26% | 4% | 96% | 378 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E F B | 3,240 | 7,614 | 22.4 | 60% | 0% | 99% | 154 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 3,205 | 12,049 | 16.6 | 58% | 0% | 95% | 236 KB | 5 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 3,013 | 6,220 | 32.1 | 57% | 8% | 95% | 512 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E E A | 3,005 | 15,012 | 23.8 | 58% | 0% | 99% | 399 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,982 | 3,648 | 38.7 | 59% | 24% | 99% | 344 KB | 2 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E E C | 2,874 | 5,905 | 24.4 | 63% | 61% | 96% | 976 KB | 1 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 2,820 | 10,761 | 0.0 | 66% | 16% | 18% | 535 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | E F C | 2,742 | 385,166 | 46.7 | 10% | 0% | 100% | 703 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 2,632 | 7,740 | 13.8 | 26% | 15% | 99% | 165 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F A | 2,470 | 6,555 | 26.5 | 53% | 0% | 86% | 324 KB | 159 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 2,451 | 10,537 | 1.9 | 61% | 0% | 54% | 5,602 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E F D | 2,444 | 4,097 | 40.6 | 37% | 48% | – | 211 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 2,434 | 7,587 | 10.6 | 17% | 0% | 91% | 721 KB | 9 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,373 | 3,364 | 17.0 | 39% | 0% | 99% | 127 KB | 23 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,373 | 4,069 | 2.5 | 49% | 0% | 100% | 201 KB | 7 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | E F C | 2,370 | 12,074 | 3.3 | 64% | 0% | 90% | 319 KB | 1 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 2,355 | 5,470 | 19.6 | 5% | 0% | 95% | 277 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,346 | 4,270 | 6.2 | 69% | 7% | 97% | 134 KB | 239 (+1) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F C | 2,320 | 7,418 | 8.1 | 15% | 0% | 98% | 105 KB | 2 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,318 | 3,623 | 9.6 | 39% | 0% | 0% | 285 KB | 25 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 2,269 | 9,120 | 0.0 | 40% | 12% | 0% | 474 KB | 4 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 2,263 | 20,252 | 14.6 | 28% | 49% | 100% | 230 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | E E D | 2,257 | 8,105 | 28.3 | 50% | 28% | 35% | 213 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 2,245 | 2,261 | 8.5 | 58% | 11% | 99% | 344 KB | 0 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 2,229 | 5,756 | 25.0 | 24% | 19% | 92% | 1,116 KB | 1 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,138 | 5,373 | 21.1 | 5% | 28% | 97% | 95 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 2,080 | 3,522 | 12.6 | 42% | 0% | 96% | 644 KB | 2 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 2,040 | 2,624 | 11.9 | 0% | 0% | – | 567 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,017 | 9,938 | 13.8 | 26% | 0% | 100% | 1,069 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 2,013 | 16,268 | 20.9 | 61% | 0% | 99% | 186 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | E F B | 2,000 | 6,474 | 4.3 | 33% | 29% | 97% | 43 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,965 | 4,872 | 0.0 | 52% | 15% | 42% | 267 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E C B | 1,935 | 3,368 | 32.8 | 75% | 33% | 89% | 980 KB | 114 (+2) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,902 | 4,431 | 12.5 | 58% | 0% | 98% | 61 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 1,897 | 6,433 | 16.7 | 45% | 18% | 76% | 1,577 KB | 6 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F C | 1,878 | 4,131 | 14.4 | 31% | 18% | 69% | 271 KB | 1 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F B | 1,818 | 13,457 | 25.2 | 18% | 24% | 76% | 218 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,773 | 2,424 | 13.6 | 33% | 0% | 78% | 634 KB | 4 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | E E B | 1,765 | 3,329 | 30.4 | 42% | 0% | 100% | 1,060 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 1,663 | 3,554 | 19.0 | 54% | 0% | 99% | 504 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 1,662 | 6,359 | 15.4 | 17% | 42% | 91% | 335 KB | 166 (+1) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,656 | 16,759 | 7.1 | 11% | 30% | 96% | 697 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | E F D | 1,622 | 29,016 | 0.0 | 38% | 0% | – | 862 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,594 | 1,988 | 37.8 | 53% | 7% | 100% | 403 KB | 2 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 1,495 | 2,669 | 20.6 | 21% | 0% | 96% | 449 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,461 | 1,783 | 12.6 | 23% | 0% | 100% | 4,314 KB | 26 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,021 | 27.2 | 40% | 5% | 99% | 46 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 1,412 | 3,311 | 14.7 | 39% | 17% | 99% | 452 KB | 12 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,386 | 3,374 | 15.0 | 20% | 0% | – | 49 KB | 3 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 1,386 | 2,737 | 0.1 | 10% | 0% | 100% | 472 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 1,374 | 2,086 | 8.0 | 21% | 0% | 100% | 521 KB | 1 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 1,355 | 4,224 | 35.6 | 64% | 0% | 97% | 269 KB | 0 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E F B | 1,342 | 6,382 | 7.7 | 71% | 0% | 100% | 70 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F A | 1,326 | 7,885 | 61.8 | 69% | 0% | 99% | 169 KB | 2 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E F B | 1,309 | 1,921 | 12.1 | 24% | 6% | 95% | 461 KB | 3 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 1,253 | 2,192 | 30.9 | 23% | 0% | 73% | 193 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | E F A | 1,234 | 5,166 | 20.3 | 0% | 0% | 100% | 41 KB | 3 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F C | 1,191 | 4,560 | 3.6 | 0% | 0% | 100% | 1,127 KB | 5 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | E F A | 1,099 | 52,172 | 63.1 | 31% | 0% | 94% | 210 KB | 124 (+1) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 1,073 | 27,017 | 0.2 | 7% | 0% | 46% | 1,480 KB | 1,113 (+2) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E E B | 1,059 | 2,542 | 36.5 | 43% | 0% | 98% | 107 KB | 4 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,050 | 4,532 | 0.0 | 41% | 0% | – | 843 KB | 2 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,047 | 3,148 | 22.5 | 27% | 0% | 80% | 518 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,010 | 3,020 | 28.9 | 0% | 0% | 97% | 122 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 944 | 1,946 | 61.0 | 40% | 0% | 99% | 695 KB | 14 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 935 | 1,796 | 7.0 | 30% | 0% | 90% | 161 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | F F A | 904 | 5,347 | 25.2 | 49% | 0% | 100% | 377 KB | 49 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 903 | 3,585 | 27.2 | 17% | 0% | 97% | 527 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F E D | 867 | 1,674 | 0.0 | 57% | 27% | 0% | 324 KB | 0 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 811 | 1,748 | 0.9 | 54% | 0% | – | 53 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 810 | 9,985 | 13.6 | 34% | 0% | 96% | 331 KB | 23 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 781 | 83,122 | 4.4 | 33% | 0% | 95% | 163 KB | 13 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 759 | 1,150 | 7.3 | 44% | 39% | 80% | 83 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 689 | 4,267 | 5.7 | 24% | 0% | 90% | 3,845 KB | 1 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | F F D | 685 | 7,555 | 25.4 | 61% | 19% | 100% | 429 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F C | 642 | 11,912 | 0.0 | 32% | 0% | 64% | 554 KB | 29 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 588 | 1,187 | 0.0 | 23% | 0% | 99% | 444 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F B | 561 | 20,474 | 21.6 | 31% | 0% | 100% | 958 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 559 | 7,604 | 17.1 | 47% | 0% | 99% | 632 KB | 11 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 510 | 1,097 | 0.0 | 67% | 15% | 0% | 658 KB | 3 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 479 | 1,258 | 13.3 | 20% | 0% | 98% | 442 KB | 1 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | 448 | 3,082 | 11.0 | 34% | 0% | 96% | 98 KB | 1 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F B | 382 | 1,367 | 9.6 | 68% | 0% | 89% | 6,579 KB | 8 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 310 | 2,956 | 16.0 | 0% | 0% | 74% | 332 KB | 1 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F E B | 301 | 4,820 | 11.5 | 51% | 0% | 97% | 5,227 KB | 40,422 (+24) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 277 | 78,403 | 0.0 | 15% | 0% | – | 8,190 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 272 | 35,747 | 5.0 | 0% | 0% | 83% | 149 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 252 | 1,204 | 0.0 | 40% | 0% | – | 202 KB | 4 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 163 | 1,224 | 1.5 | 16% | 0% | 100% | 52 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 129 | 328 | 2.7 | 29% | 0% | 88% | 151 KB | 345 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F E E | 121 | 2,502 | 4.4 | 48% | 47% | 11% | 115 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 73 | 1,241 | 1.2 | 0% | 0% | 33% | 144 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 49 | 1,008 | 6.8 | 47% | 0% | 100% | 151 KB | 2 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 39 | 833 | 0.0 | 51% | 0% | 98% | 500 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 27 | 534 | 9.4 | 0% | 0% | 100% | 67 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | F F C | 27 | 4,378 | 0.0 | 37% | 0% | 64% | 409 KB | 3 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | 12 | 3,429 | 20.5 | 54% | 0% | 98% | 93 KB | 1 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 11 | 2,687 | 0.0 | 6% | 0% | – | 159 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 9 | 731 | 0.0 | 18% | 0% | 100% | 478 KB | 6 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 2 | 147 | 10.3 | 31% | 0% | 83% | 15 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 0 | 41.9 | 0% | 0% | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F F B | – | – | 38.4 | 31% | 39% | 88% | 2,208 KB | 1,466 (+5) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | 0 | 3,430 | 30.2 | 0% | 0% | 99% | 884 KB | 5 (+1) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 953 | 24.7 | 0% | 0% | 86% | 2,616 KB | 39 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 24.3 | 23% | 0% | 100% | 342 KB | 4 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 23.9 | – | – | 98% | 231 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F D | 0 | 1,078 | 22.8 | 73% | 0% | 47% | 100 KB | 0 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 21.4 | – | – | 98% | 363 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 20.7 | 52% | 0% | 100% | 988 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 19.1 | – | – | 97% | 94 KB | 16 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 144 | 19.0 | 0% | 0% | 100% | 88 KB | 0 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 0 | 17.3 | – | – | 91% | 306 KB | 7 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 0 | 3,876 | 15.7 | 25% | 0% | 96% | 66 KB | 3 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 1,716 | 15.0 | 0% | 0% | 88% | 700 KB | 4 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F F B | 0 | 15,895 | 15.0 | 52% | 0% | 91% | 86 KB | 6 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 0 | 1,783 | 14.2 | 0% | 0% | 93% | 576 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 1,362 | 13.7 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 13.5 | – | – | 98% | 43 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 0 | 2,787 | 13.2 | 0% | 0% | 100% | 617 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 111 | 13.0 | 0% | 0% | 98% | 49 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 2,326 | 12.5 | 10% | 0% | 95% | 8,119 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 535 | 12.0 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 25 | 11.8 | 0% | 0% | – | 55 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 931 | 11.0 | 0% | 0% | 98% | 489 KB | 57 (+2) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 0 | 1,913 | 10.9 | 0% | 0% | – | 414 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 0 | 1,447 | 10.5 | 0% | 0% | 94% | 94 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F E D | – | – | 10.2 | 42% | 0% | 0% | 206 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 465 | 9.9 | 0% | 0% | 97% | 41 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 309 | 8.5 | 0% | 0% | 80% | 552 KB | 2 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 359 | 8.4 | 0% | 0% | 99% | 99 KB | 4 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 2,035 | 8.2 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 3,821 | 8.1 | 0% | 0% | – | 100 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 514 | 7.5 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 6.9 | – | – | 98% | 149 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 6.8 | – | – | 98% | 723 KB | 6 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 6.7 | – | – | 99% | 298 KB | 5 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 5 | 6.1 | 0% | 0% | 96% | 787 KB | 2 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 5.4 | – | – | – | 115 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 3,438 | 5.4 | 29% | 0% | 98% | 522 KB | 0 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 461 | 5.1 | 0% | 0% | 75% | 161 KB | 2 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 4.8 | 23% | 6% | 0% | 472 KB | 460 (+2) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 4.5 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 4.3 | – | – | 90% | 195 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 2,052 | 4.2 | 0% | 0% | 93% | 23 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 3.8 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 0 | 2.9 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 0 | 1.5 | – | – | 69% | 290 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | 0 | 24 | 1.3 | 0% | 0% | – | 311 KB | 4 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 1.2 | – | – | 100% | 59 KB | 1 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 52% | 0% | 91% | 822 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.2 | 85% | 60% | 96% | 34,213 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 0 | 156 | 0.1 | 0% | 0% | 76% | 152 KB | 29 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 543 | 0.1 | 0% | 0% | 16% | 904 KB | 1,303 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E D | – | – | 0.1 | 55% | 0% | 48% | 84 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | 0 | 229 | 0.0 | 0% | 0% | – | 3,234 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 195 | 0.0 | 0% | 0% | 94% | 269 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 150 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 1,456 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 12 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 197,706 | 0.0 | 25% | 0% | – | 110 KB | 0 (+0) |
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
