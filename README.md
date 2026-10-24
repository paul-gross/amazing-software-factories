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
_293 repos, last measured 2026-10-24. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (293)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 67,219 | 97,408 | 30.0 | 68% | 31% | 87% | 192 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A D D | 58,002 | 160,692 | 0.2 | 64% | 22% | 32% | 1,271 KB | 440 (+1) |
| [purlis/purlis](https://github.com/purlis/purlis) | A E B | 51,054 | 60,808 | 34.8 | 55% | 19% | 82% | 559 KB | 11 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A C A | 48,725 | 87,611 | 61.2 | 70% | 21% | 95% | 210 KB | 120 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | A F B | 44,908 | 60,414 | 8.8 | 51% | 5% | 83% | 288 KB | 330 (+1) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 42,379 | 41,066 | 72.8 | 0% | 0% | 92% | 3,145 KB | 2,026 (+7) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 41,657 | 252,759 | 59.0 | 18% | 0% | 87% | 3,975 KB | 1 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 41,533 | 56,708 | 165 | 24% | 3% | 89% | 2,294 KB | 3 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 40,797 | 44,531 | 51.9 | 58% | 19% | 92% | 894 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 34,702 | 77,246 | 71.9 | 77% | 34% | 96% | 169 KB | 2 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B D B | 34,114 | 52,203 | 16.6 | 62% | 0% | 88% | 240 KB | 2 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B E B | 30,710 | 32,753 | 31.1 | 46% | 23% | 99% | 1,060 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F C | 30,397 | 81,356 | 24.2 | 39% | 38% | 53% | 4,722 KB | 96 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | B D B | 29,906 | 40,082 | 25.2 | 65% | 32% | 100% | 628 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 29,130 | 32,349 | 30.8 | 73% | 29% | 88% | 363 KB | 9 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 28,366 | 39,507 | 26.6 | 80% | 5% | 87% | 685 KB | 0 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 28,230 | 37,892 | 96.8 | 38% | 10% | 92% | 3,784 KB | 72 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 27,627 | 135,168 | 108 | 47% | 0% | 49% | 306 KB | 4 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B D C | 26,830 | 31,944 | 33.8 | 65% | 26% | 100% | 315 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 25,786 | 68,710 | 45.8 | 40% | 60% | 100% | 59 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B E C | 25,545 | 42,344 | 70.3 | 49% | 24% | 91% | 546 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B D A | 25,121 | 69,391 | 69.0 | 62% | 20% | 99% | 60 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 24,886 | 34,154 | 49.0 | 72% | 33% | 99% | 346 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B D B | 24,568 | 133,180 | 27.8 | 66% | 59% | 99% | 931 KB | 33 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B E B | 23,509 | 33,215 | 19.7 | 51% | 26% | 100% | 542 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B D B | 23,507 | 220,935 | 91.6 | 61% | 25% | 95% | 600 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 23,421 | 26,633 | 104 | 15% | 40% | 76% | 361 KB | 52 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 23,146 | 35,259 | 107 | 58% | 16% | 100% | 219 KB | 14 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B E B | 22,849 | 43,835 | 10.9 | 52% | 37% | 92% | 781 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 22,348 | 42,373 | 18.4 | 31% | 20% | 93% | 6,732 KB | 124 (+3) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | B C B | 22,341 | 26,770 | 34.7 | 72% | 66% | 90% | 1,545 KB | 3 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 21,971 | 18,723 | 0.0 | 84% | 25% | – | 226 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B E D | 21,570 | 24,677 | 0.0 | 57% | 63% | – | 308 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | B E C | 21,516 | 42,148 | 13.4 | 60% | 39% | 76% | 431 KB | 0 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C C | 20,492 | 36,798 | 22.6 | 78% | 4% | 84% | 757 KB | 5 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 20,466 | 34,685 | 0.0 | 65% | 42% | – | 1,218 KB | 3 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B C C | 20,246 | 25,008 | 22.6 | 87% | 29% | 94% | 683 KB | 9 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | C F B | 19,921 | 29,832 | 33.2 | 30% | 29% | 98% | 1,380 KB | 92 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 19,306 | 510,671 | 0.0 | 73% | 65% | 0% | 3,283 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C C B | 19,146 | 32,904 | 16.2 | 77% | 24% | 98% | 86 KB | 6 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E A | 18,827 | 30,806 | 63.6 | 44% | 61% | 93% | 275 KB | 6,413 (+10) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C C B | 18,773 | 27,320 | 20.7 | 74% | 0% | 100% | 962 KB | 1 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C D C | 18,594 | 85,092 | 13.4 | 66% | 5% | 78% | 464 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 18,249 | 23,885 | 27.5 | 78% | 28% | 97% | 172 KB | 5 (+1) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F B | 18,180 | 42,714 | 0.0 | 11% | 58% | 92% | 416 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C F B | 17,635 | 31,538 | 175 | 40% | 49% | 100% | 2,730 KB | 1 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 17,480 | 32,997 | 33.8 | 28% | 20% | 97% | 877 KB | 4 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 17,472 | 21,363 | 5.2 | 17% | 15% | 100% | 426 KB | 135 (+1) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 16,879 | 176,719 | 31.6 | 86% | 42% | 98% | 158 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,566 | 42,476 | 34.5 | 2% | 14% | 100% | 225 KB | 7 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 16,234 | 26,264 | 0.0 | 47% | 44% | – | 319 KB | 2 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C C D | 15,705 | 21,327 | 34.5 | 74% | 22% | 99% | 599 KB | 22 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 15,122 | 57,865 | 42.4 | 33% | 29% | 99% | 78 KB | 2 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B C | 14,996 | 35,434 | 9.0 | 80% | 39% | 100% | 101 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B B | 14,983 | 21,418 | 0.0 | 82% | 42% | 75% | 291 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C B B | 14,725 | 21,399 | 28.1 | 81% | 50% | 82% | 1,367 KB | 70,292 (+14) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C F C | 14,718 | 21,205 | 25.1 | 58% | 10% | 100% | 176 KB | 33 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | C F D | 14,321 | 23,809 | 7.9 | 34% | 0% | – | 100 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | C E C | 13,615 | 19,191 | 67.0 | 52% | 7% | 97% | 691 KB | 14 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 13,530 | 13,645 | 0.0 | 62% | 4% | 94% | 589 KB | 1 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C F B | 12,305 | 19,201 | 13.1 | 8% | 26% | 97% | 589 KB | 1 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 11,994 | 45,658 | 28.9 | 84% | 0% | 100% | 2,178 KB | 5 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 11,960 | 14,445 | 0.0 | 59% | 41% | 30% | 308 KB | 262 (+5) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 11,744 | 18,471 | 38.0 | 37% | 43% | 74% | 330 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 13,707 | 12.7 | 48% | 0% | 94% | 718 KB | 9 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C D D | 11,623 | 14,420 | 8.4 | 67% | 0% | 21% | 195 KB | 3 (+1) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C E B | 11,486 | 28,878 | 38.5 | 54% | 13% | 92% | 571 KB | 37 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 11,453 | 20,288 | 24.1 | 89% | 39% | 99% | 200 KB | 6 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C E D | 11,413 | 18,290 | 0.0 | 44% | 9% | 28% | 154 KB | 110 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 11,266 | 33,577 | 72.0 | 55% | 44% | 25% | 837 KB | 16 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | C E D | 11,254 | 31,398 | 0.0 | 51% | 7% | 0% | 601 KB | 1 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | C C A | 11,126 | 29,375 | 19.1 | 77% | 2% | 96% | 90 KB | 1 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C C A | 11,114 | 21,031 | 15.7 | 74% | 49% | 93% | 129 KB | 5 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 10,987 | 20,648 | 40.9 | 31% | 42% | 100% | 249 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | C E C | 10,840 | 19,978 | 33.6 | 53% | 48% | 99% | 562 KB | 5 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C B A | 10,456 | 14,932 | 32.5 | 83% | 51% | 86% | 102 KB | 230 (+1) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 10,319 | 23,222 | 33.5 | 34% | 45% | 100% | 1,289 KB | 8 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | C F B | 10,084 | 71,862 | 17.6 | 32% | 15% | 82% | 213 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | C F B | 10,021 | 16,633 | 27.6 | 5% | 17% | 96% | 142 KB | 7 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | C F B | 10,002 | 12,195 | 15.1 | 29% | 35% | 96% | 326 KB | 162 (+1) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 9,881 | 10,777 | 0.2 | 22% | 0% | 73% | 152 KB | 29 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F C | 9,873 | 15,585 | 0.0 | 38% | 29% | 57% | 240 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D E B | 9,605 | 17,390 | 23.0 | 72% | 20% | 92% | 1,072 KB | 5 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | D F C | 9,464 | 24,830 | 25.5 | 48% | 0% | 99% | 459 KB | 19 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 9,393 | 389,559 | 31.2 | 29% | 8% | 95% | 1,414 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 9,329 | 10,023 | 20.2 | 13% | 4% | 88% | 700 KB | 4 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D E B | 9,209 | 55,650 | 1.2 | 55% | 18% | 72% | 3,340 KB | 7 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D F B | 9,101 | 13,103 | 36.3 | 39% | 44% | 99% | 647 KB | 2 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 9,059 | 34,990 | 0.0 | 58% | 11% | 100% | 488 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 8,569 | 12,206 | 5.2 | 36% | 50% | 79% | 3,592 KB | 545 (+1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,546 | 13,168 | 0.2 | 43% | 21% | 100% | 357 KB | 2 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 8,527 | 105,688 | 16.5 | 56% | 0% | 100% | 247 KB | 2 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D B B | 8,448 | 10,473 | 20.7 | 80% | 65% | 100% | 560 KB | 1 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D C B | 8,015 | 13,802 | 13.1 | 76% | 23% | 91% | 1,191 KB | 13 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | D F C | 7,726 | 8,649 | 21.9 | 53% | 0% | 96% | 311 KB | 4 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D E B | 7,656 | 106,010 | 39.0 | 74% | 11% | 96% | 1,431 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D C C | 7,541 | 14,913 | 14.7 | 72% | 6% | 94% | 365 KB | 2 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D E A | 7,180 | 9,538 | 36.5 | 58% | 0% | 100% | 122 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 7,002 | 12,567 | 46.9 | 0% | 18% | 96% | 67 KB | 61 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | D F A | 6,883 | 68,668 | 26.1 | 30% | 0% | 100% | 377 KB | 49 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D E C | 6,813 | 24,902 | 18.7 | 40% | 4% | 100% | 43 KB | 15 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | D E C | 6,667 | 11,958 | 0.0 | 64% | 0% | 100% | 472 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 6,623 | 22,327 | 0.0 | 29% | 0% | – | 824 KB | 0 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D C B | 6,441 | 12,938 | 25.9 | 72% | 36% | 99% | 1,172 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D C | 6,309 | 8,471 | 15.2 | 68% | 20% | 50% | 140 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D E A | 6,256 | 10,191 | 15.6 | 52% | 30% | 89% | 148 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D F D | 6,240 | 22,595 | 28.4 | 3% | 0% | 100% | 158 KB | 1 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 6,222 | 7,807 | 75.1 | 75% | 16% | 99% | 782 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D E C | 5,948 | 7,137 | 23.8 | 59% | 0% | 80% | 959 KB | 1 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D E C | 5,939 | 11,264 | 19.3 | 60% | 0% | 100% | 41 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D C C | 5,883 | 7,643 | 15.2 | 75% | 25% | 94% | 134 KB | 1 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D E B | 5,801 | 12,547 | 8.1 | 49% | 59% | 94% | 70 KB | 13 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | D F C | 5,722 | 27,957 | 11.8 | 80% | 6% | 98% | 150 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | D D B | 5,692 | 9,965 | 14.9 | 67% | 30% | 100% | 4,314 KB | 20 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D E C | 5,683 | 50,342 | 0.0 | 53% | 14% | 50% | 479 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D F D | 5,675 | 8,144 | 37.8 | 35% | 0% | – | 421 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D F B | 5,635 | 5,909 | 24.4 | 27% | 19% | 98% | 815 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | D D D | 5,594 | 7,443 | 0.0 | 62% | 17% | – | 3,234 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D C B | 5,518 | 13,246 | 7.3 | 81% | 0% | 80% | 616 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 5,397 | 9,184 | 46.4 | 48% | 31% | – | 387 KB | 3 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D E D | 5,294 | 10,542 | 0.8 | 50% | 36% | 0% | 164 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | D F C | 5,289 | 12,764 | 41.8 | 28% | 0% | 52% | 3,052 KB | 2 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,226 | 10,504 | 3.8 | 30% | 0% | 90% | 319 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D F C | 5,146 | 11,557 | 10.8 | 57% | 0% | 100% | 49 KB | 3 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,011 | 11,300 | 20.1 | 8% | 0% | 98% | 489 KB | 52 (+3) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E E B | 4,989 | 7,824 | 19.9 | 51% | 5% | 96% | 499 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E E B | 4,815 | 6,077 | 24.0 | 68% | 14% | 100% | 106 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 4,751 | 9,967 | 0.0 | 34% | 24% | 97% | 432 KB | 0 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E F E | 4,739 | 9,950 | 22.8 | 40% | 6% | 98% | 1,121 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 4,325 | 4,780 | 20.1 | 42% | 0% | 99% | 127 KB | 23 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 4,318 | 8,374 | 0.3 | 45% | 18% | 0% | 509 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,159 | 8,440 | 20.7 | 26% | 18% | 96% | 272 KB | 1 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 4,136 | 12,971 | 26.2 | 49% | 42% | 99% | 174 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | E F C | 4,042 | 4,653 | 9.7 | 27% | 0% | 99% | 99 KB | 4 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E E D | 4,027 | 17,832 | 9.5 | 59% | 6% | 0% | 137 KB | 14 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 4,008 | 9,412 | 10.8 | 49% | 0% | 0% | 285 KB | 24 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | E F B | 3,981 | 7,101 | 1.8 | 6% | 0% | 76% | 42 KB | 1 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 3,897 | 6,450 | 10.6 | 57% | 0% | – | 83 KB | 2 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E F B | 3,758 | 21,364 | 6.4 | 53% | 25% | 77% | 78 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F D | 3,672 | 43,696 | 19.2 | 9% | 3% | 42% | 140 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E C C | 3,628 | 8,217 | 11.4 | 79% | 20% | 98% | 124 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,599 | 5,752 | 16.3 | 30% | 0% | 100% | 136 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,576 | 6,867 | 0.0 | 18% | 9% | 0% | 451 KB | 4 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 3,550 | 5,372 | 20.1 | 19% | 0% | 90% | 436 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E E D | 3,540 | 5,646 | 37.2 | 54% | 7% | – | 198 KB | 3 (+1) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E D B | 3,521 | 13,423 | 38.3 | 64% | 0% | 97% | 107 KB | 5 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 3,520 | 7,356 | 26.2 | 0% | 15% | 100% | 526 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 3,492 | 5,430 | 41.4 | 71% | 25% | 90% | 140 KB | 8 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 3,341 | 4,197 | 11.3 | 27% | 24% | 98% | 518 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 3,334 | 16,606 | 21.8 | 49% | 15% | 99% | 625 KB | 11 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 3,302 | 5,642 | 9.8 | 38% | 18% | 94% | 86 KB | 1 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 3,297 | 53,714 | 30.0 | 62% | 0% | 54% | 99 KB | 1 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 3,238 | 5,362 | 1.8 | 62% | 0% | 100% | 182 KB | 7 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 3,212 | 6,870 | 14.4 | 44% | 0% | 76% | 1,538 KB | 6 (+1) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 3,207 | 14,336 | 13.0 | 44% | 15% | 97% | 236 KB | 5 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 3,203 | 4,738 | 12.8 | 67% | 12% | 100% | 161 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F B | 3,156 | 6,618 | 16.5 | 7% | 0% | 84% | 377 KB | 7 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 3,129 | 4,123 | 36.5 | 44% | 6% | 99% | 221 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 3,116 | 4,307 | 0.0 | 16% | 20% | 86% | 878 KB | 2 (+1) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 3,080 | 8,872 | 38.6 | 21% | 0% | 100% | 240 KB | 9 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 3,003 | 7,789 | 12.4 | 67% | 0% | 100% | 396 KB | 12 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,927 | 24,553 | 0.0 | 36% | 0% | – | 200 KB | 28 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 2,833 | 6,475 | 25.0 | 27% | 10% | 94% | 69 KB | 10 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,782 | 11,144 | 7.2 | 6% | 40% | 99% | 529 KB | 11 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E F A | 2,739 | 6,625 | 9.9 | 46% | 0% | 95% | 252 KB | 0 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E D B | 2,702 | 5,041 | 43.5 | 68% | 28% | 100% | 316 KB | 2 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E F C | 2,696 | 9,226 | 20.6 | 34% | 0% | 100% | 346 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,656 | 7,541 | 19.0 | 31% | 23% | 98% | 386 KB | 1 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 2,642 | 4,414 | 12.1 | 11% | 10% | 91% | 551 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 2,586 | 10,427 | 28.9 | 26% | 26% | 100% | 427 KB | 17 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F C | 2,554 | 6,244 | 0.9 | 49% | 6% | 92% | 5,596 KB | 1 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | E F B | 2,541 | 25,619 | 36.4 | 61% | 0% | 97% | 405 KB | 9 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E D E | 2,523 | 12,841 | 15.5 | 68% | 34% | 100% | 1,056 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | E F C | 2,461 | 3,590 | 0.0 | 40% | 20% | 93% | 266 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,395 | 7,426 | 6.8 | 59% | 5% | 98% | 134 KB | 228 (+3) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E F C | 2,384 | 8,745 | 14.0 | 40% | 0% | 94% | 8,119 KB | 1 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E E C | 2,371 | 3,806 | 10.9 | 61% | 0% | 100% | 66 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 2,320 | 8,664 | 0.0 | 46% | 35% | – | 706 KB | 2 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E E A | 2,282 | 3,128 | 16.8 | 51% | 49% | 99% | 446 KB | 12 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 2,238 | 4,756 | 26.8 | 53% | 0% | 82% | 203 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,051 | 7,245 | 0.1 | 65% | 0% | 84% | 395 KB | 3 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | E F B | 2,018 | 2,937 | 25.0 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 1,994 | 2,944 | 15.5 | 46% | 27% | 100% | 202 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 1,991 | 70,305 | 15.5 | 14% | 0% | 99% | 378 KB | 1 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,900 | 2,121 | 21.8 | 19% | 33% | 97% | 824 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,819 | 4,767 | 0.0 | 51% | 0% | 42% | 266 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,806 | 4,460 | 33.9 | 34% | 0% | 100% | 403 KB | 2 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,780 | 4,006 | 9.1 | 32% | 0% | 95% | 342 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 1,778 | 10,566 | 24.9 | 54% | 0% | 94% | 393 KB | 0 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | E F B | 1,771 | 3,081 | 8.5 | 51% | 0% | 80% | 552 KB | 2 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 1,693 | 52,536 | 0.0 | 54% | 27% | – | 8,190 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,665 | 137,227 | 0.0 | 73% | 0% | 97% | 211 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,561 | 4,645 | 22.2 | 34% | 0% | 100% | 152 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,561 | 2,512 | 16.1 | 24% | 13% | – | 49 KB | 3 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 1,504 | 14,945 | 36.2 | 65% | 0% | 73% | 188 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,490 | 10,907 | 22.2 | 30% | 37% | 94% | 215 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E E D | 1,469 | 10,571 | 3.6 | 65% | 0% | – | 296 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 1,420 | 2,038 | 23.3 | 40% | 26% | 97% | 544 KB | 0 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E E C | 1,343 | 9,086 | 6.3 | 43% | 16% | 93% | 289 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,290 | 2,916 | 5.2 | 15% | 27% | 95% | 7,014 KB | 18 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F B | 1,251 | 15,606 | 0.0 | 15% | 6% | 78% | 554 KB | 28 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 1,207 | 31,790 | 0.3 | 82% | 0% | 29% | 1,471 KB | 1,107 (+2) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 1,018 | 3,656 | 29.7 | 50% | 0% | 47% | 100 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,010 | 1,833 | 0.0 | 23% | 0% | 33% | 398 KB | 461 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 959 | 2,035 | 29.6 | 60% | 0% | 100% | 980 KB | 104 (+2) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F B | 921 | 6,181 | 14.1 | 0% | 10% | 77% | 257 KB | 1 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F D C | 901 | 3,143 | 17.8 | 61% | 7% | 98% | 426 KB | 1 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F D C | 900 | 5,123 | 7.2 | 61% | 0% | 99% | 151 KB | 2 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | 867 | 4,712 | 0.0 | 73% | 0% | 0% | 316 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 864 | 19,648 | 4.8 | 71% | 7% | 72% | 149 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 821 | 7,564 | 12.5 | 79% | 0% | 96% | 32 KB | 1 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 812 | 16,150 | 14.0 | 17% | 0% | – | 411 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 777 | 4,617 | 11.4 | 52% | 0% | 97% | 56 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 688 | 5,984 | 28.6 | 17% | 0% | 94% | 317 KB | 159 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 645 | 796,255 | 48.6 | 12% | 0% | 100% | 703 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 568 | 2,684 | 27.2 | 35% | 0% | 100% | 122 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | F F A | 550 | 14,521 | 21.1 | 32% | 0% | 95% | 219 KB | 5 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 548 | 990 | 0.1 | 70% | 12% | 0% | 635 KB | 3 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 462 | 6,978 | 0.0 | 16% | 0% | – | 111 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 440 | 4,005 | 11.3 | 49% | 0% | 89% | 6,579 KB | 8 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 301 | 5,929 | 0.0 | 25% | 0% | 80% | 478 KB | 6 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 283 | 1,617 | 0.0 | 29% | 33% | 98% | 404 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 239 | 2,584 | 0.0 | 24% | 0% | 0% | 1,135 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 186 | 3,061 | 2.4 | 49% | 0% | 100% | 163 KB | 11 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 167 | 10,221 | 17.8 | 43% | 0% | 93% | 576 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 147 | 26,819 | 6.2 | 12% | 0% | 96% | 24 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 136 | 12,083 | 33.1 | 42% | 0% | 91% | 2,600 KB | 36 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 121 | 1,618 | 8.7 | 28% | 0% | 96% | 787 KB | 2 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 107 | 3,456 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 89 | 4,332 | 28.0 | 22% | 0% | 100% | 617 KB | 1 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 88 | 1,871 | 17.6 | 0% | 0% | 92% | 303 KB | 23 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 76 | 3,766 | 13.0 | 50% | 0% | 99% | 298 KB | 5 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 54 | 655 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 31 | 2,014 | 6.3 | 0% | 0% | 96% | 522 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 19 | 2,748 | 17.1 | 39% | 0% | 96% | 66 KB | 3 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 39.0 | 78% | 27% | 86% | 2,197 KB | 1,438 (+2) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | 0 | 21,545 | 27.0 | 64% | 0% | 98% | 231 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F C B | – | – | 23.6 | 82% | 43% | 98% | 976 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | 0 | 1,466 | 21.9 | 69% | 0% | 98% | 363 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 21.1 | 0% | 0% | 41% | 279 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 256 | 20.5 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F E C | – | – | 18.2 | 48% | 32% | 94% | 342 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 18.0 | – | – | 97% | 94 KB | 16 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 8 | 15.2 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 14.8 | 0% | 0% | 98% | 723 KB | 5 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 19,798 | 14.2 | 0% | 0% | – | 224 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 14.0 | – | – | – | 55 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 2,957 | 14.0 | 0% | 0% | 97% | 49 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 0 | 3,372 | 12.8 | 0% | 0% | 98% | 43 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 4,713 | 9.9 | 25% | 0% | 89% | 38 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 8.7 | – | – | 98% | 149 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | 0 | 0 | 8.7 | – | – | 90% | 195 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 8.6 | – | – | – | 115 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 1,975 | 8.1 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | – | – | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F C | – | – | 6.5 | 53% | 0% | 57% | 206 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 5.4 | 59% | 53% | 0% | 1,790 KB | 458 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 347 | 4.9 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 2,155 | 4.8 | 0% | 0% | 74% | 161 KB | 2 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 3 | 3.5 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 0 | 653 | 3.4 | 25% | 0% | 100% | 1,117 KB | 5 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 10,168 | 2.7 | 24% | 0% | 100% | 258 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,308 | 1.9 | 0% | 0% | 33% | 140 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 0 | 610 | 1.8 | 0% | 0% | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 184 | 1.4 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 73% | 31% | 78% | 816 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 0.5 | 0% | 0% | – | 92 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.2 | 81% | 72% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 94 | 0.1 | 0% | 0% | 15% | 904 KB | 1,289 (+1) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 291 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | 0% | 0% | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | F E D | 0 | 0 | 0.0 | 53% | 56% | 32% | 1,085 KB | 34 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F C | – | – | 0.0 | 33% | 25% | 59% | 84 KB | 5 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 596 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,893 | 0.0 | 0% | 0% | – | 112 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 2 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
