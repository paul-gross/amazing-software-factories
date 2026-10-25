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
_293 repos, last measured 2026-10-25. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (293)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A D A | 67,219 | 97,408 | 30.0 | 68% | 31% | 87% | 192 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | A C D | 58,002 | 170,514 | 0.2 | 78% | 21% | 27% | 1,271 KB | 440 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | A E B | 44,908 | 67,513 | 9.3 | 56% | 23% | 81% | 288 KB | 331 (+1) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A C A | 44,358 | 80,159 | 61.9 | 72% | 28% | 95% | 210 KB | 121 (+1) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 44,279 | 77,915 | 170 | 20% | 35% | 89% | 2,294 KB | 3 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 42,379 | 41,066 | 72.8 | 0% | 0% | 92% | 3,145 KB | 2,026 (+7) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 40,797 | 43,485 | 51.6 | 59% | 18% | 85% | 923 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A E B | 40,166 | 56,595 | 33.8 | 58% | 20% | 90% | 569 KB | 11 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 35,017 | 73,734 | 58.6 | 9% | 0% | 90% | 3,975 KB | 1 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B D A | 34,544 | 79,187 | 73.3 | 67% | 34% | 96% | 169 KB | 2 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B E B | 34,056 | 52,228 | 17.9 | 59% | 0% | 88% | 240 KB | 2 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | B E B | 29,906 | 35,107 | 24.9 | 62% | 0% | 100% | 628 KB | 0 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 29,130 | 32,349 | 30.8 | 73% | 29% | 88% | 363 KB | 9 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 27,627 | 135,168 | 108 | 47% | 0% | 49% | 306 KB | 4 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B D C | 26,830 | 31,944 | 33.8 | 65% | 26% | 100% | 315 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F C | 26,791 | 29,743 | 106 | 28% | 50% | 76% | 361 KB | 57 (+5) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 26,720 | 31,486 | 32.3 | 43% | 29% | 98% | 1,403 KB | 91 (-1) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B E B | 26,652 | 33,259 | 94.8 | 41% | 11% | 91% | 3,809 KB | 72 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B D B | 26,366 | 46,879 | 12.1 | 66% | 36% | 93% | 781 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B E C | 25,545 | 42,344 | 71.5 | 56% | 23% | 95% | 548 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B D A | 25,112 | 41,591 | 72.4 | 62% | 20% | 100% | 60 KB | 0 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B C B | 24,666 | 29,705 | 26.9 | 76% | 2% | 86% | 698 KB | 0 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B E B | 24,634 | 37,328 | 22.3 | 49% | 23% | 100% | 574 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B D B | 24,443 | 128,027 | 28.4 | 61% | 49% | 99% | 951 KB | 33 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B E B | 24,104 | 27,307 | 31.1 | 45% | 26% | 99% | 1,060 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 24,050 | 65,926 | 47.5 | 43% | 65% | 100% | 59 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F C | 23,166 | 65,113 | 24.1 | 43% | 0% | 51% | 4,722 KB | 96 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 23,146 | 36,910 | 109 | 50% | 16% | 98% | 276 KB | 15 (+1) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 22,348 | 40,106 | 18.2 | 37% | 23% | 92% | 6,732 KB | 125 (+1) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | B C B | 22,341 | 26,599 | 33.1 | 75% | 48% | 91% | 1,545 KB | 3 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B D B | 21,741 | 206,417 | 91.9 | 67% | 25% | 100% | 606 KB | 2 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B E D | 21,570 | 24,677 | 0.0 | 57% | 63% | – | 308 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | B D C | 21,516 | 42,746 | 13.7 | 65% | 38% | 86% | 431 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B C D | 20,466 | 36,920 | 0.0 | 74% | 53% | – | 1,218 KB | 3 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B B C | 20,246 | 24,195 | 22.8 | 82% | 17% | 94% | 701 KB | 9 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 19,306 | 527,054 | 0.0 | 79% | 74% | 0% | 3,286 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C E B | 19,146 | 31,008 | 16.2 | 71% | 0% | 98% | 86 KB | 6 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | C F B | 18,681 | 44,334 | 0.0 | 19% | 44% | 90% | 674 KB | 1 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C E B | 17,559 | 28,386 | 176 | 48% | 55% | 100% | 2,762 KB | 1 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C E C | 17,030 | 23,034 | 26.1 | 44% | 10% | 100% | 178 KB | 33 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 16,998 | 28,301 | 64.1 | 42% | 65% | 78% | 275 KB | 6,421 (+8) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 16,879 | 167,394 | 33.5 | 85% | 41% | 94% | 158 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C B A | 16,644 | 32,487 | 49.2 | 84% | 36% | 99% | 346 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,327 | 35,884 | 36.1 | 0% | 15% | 100% | 225 KB | 7 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B C | 16,213 | 38,894 | 9.7 | 83% | 67% | 100% | 101 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | C E B | 15,840 | 66,022 | 1.2 | 56% | 32% | 96% | 3,340 KB | 7 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C F D | 15,705 | 21,889 | 34.5 | 75% | 24% | 100% | 599 KB | 22 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C C C | 15,662 | 34,168 | 22.3 | 75% | 5% | 86% | 761 KB | 5 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,352 | 20,142 | 5.4 | 4% | 15% | 99% | 426 KB | 137 (+2) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C B B | 14,983 | 21,418 | 0.0 | 82% | 42% | 75% | 291 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 14,833 | 56,103 | 43.2 | 30% | 16% | 99% | 83 KB | 2 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | C F D | 14,321 | 23,809 | 7.9 | 34% | 0% | – | 100 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | C E C | 13,615 | 19,191 | 67.0 | 52% | 7% | 97% | 691 KB | 14 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 13,265 | 22,797 | 0.0 | 50% | 22% | – | 319 KB | 2 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C C B | 12,925 | 15,234 | 13.2 | 76% | 23% | 94% | 1,191 KB | 13 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C C D | 12,761 | 15,932 | 8.7 | 82% | 0% | 18% | 196 KB | 3 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 12,717 | 15,092 | 0.0 | 82% | 28% | – | 227 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C F B | 12,305 | 17,657 | 13.1 | 9% | 15% | 97% | 589 KB | 2 (+1) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C B B | 12,097 | 25,211 | 28.6 | 82% | 42% | 75% | 1,376 KB | 70,313 (+21) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 12,058 | 34,284 | 72.1 | 51% | 44% | 25% | 837 KB | 16 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | C F A | 12,032 | 13,893 | 46.8 | 0% | 14% | 95% | 67 KB | 62 (+1) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C E B | 12,008 | 23,600 | 20.4 | 73% | 0% | 100% | 962 KB | 1 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 11,994 | 36,487 | 31.9 | 82% | 0% | 100% | 2,190 KB | 5 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 11,960 | 14,445 | 0.0 | 59% | 41% | 30% | 308 KB | 262 (+5) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C B A | 11,870 | 16,435 | 33.3 | 80% | 54% | 86% | 102 KB | 230 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C E B | 11,867 | 27,006 | 35.6 | 50% | 45% | 100% | 1,311 KB | 8 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 11,235 | 12.7 | 39% | 0% | 94% | 718 KB | 9 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C E B | 11,486 | 28,878 | 38.5 | 54% | 13% | 92% | 571 KB | 37 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 11,453 | 16,690 | 24.7 | 81% | 46% | 99% | 200 KB | 6 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | C E D | 11,413 | 21,188 | 0.0 | 53% | 23% | 28% | 154 KB | 111 (+1) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | C E D | 11,254 | 31,398 | 0.0 | 51% | 7% | 0% | 601 KB | 1 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 10,987 | 20,405 | 41.2 | 39% | 19% | 96% | 249 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | C E C | 10,840 | 19,978 | 33.6 | 53% | 48% | 99% | 562 KB | 5 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C D C | 10,723 | 63,903 | 14.1 | 62% | 5% | 76% | 468 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | C E A | 10,632 | 25,082 | 19.1 | 70% | 0% | 96% | 90 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | C F B | 10,391 | 16,444 | 28.4 | 12% | 14% | 92% | 152 KB | 8 (+1) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | C F B | 10,084 | 70,506 | 19.5 | 0% | 14% | 84% | 213 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | C F B | 10,002 | 11,408 | 14.7 | 36% | 40% | 94% | 325 KB | 162 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 9,881 | 10,777 | 0.2 | 22% | 0% | 73% | 152 KB | 29 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F C | 9,873 | 15,585 | 0.0 | 38% | 29% | 57% | 240 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D E B | 9,605 | 17,390 | 23.0 | 72% | 20% | 92% | 1,072 KB | 5 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | D F C | 9,464 | 22,465 | 24.9 | 59% | 0% | 100% | 463 KB | 19 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 9,329 | 10,023 | 20.2 | 13% | 4% | 88% | 700 KB | 4 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | D F B | 9,234 | 31,225 | 34.4 | 23% | 21% | 97% | 877 KB | 4 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D C A | 9,150 | 20,538 | 15.8 | 78% | 50% | 93% | 130 KB | 5 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D D C | 9,059 | 33,076 | 0.0 | 63% | 21% | 100% | 488 KB | 1 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | D C A | 8,998 | 21,826 | 26.0 | 78% | 29% | 96% | 172 KB | 6 (+1) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D C B | 8,895 | 10,638 | 19.9 | 72% | 63% | 100% | 566 KB | 1 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 8,678 | 8,079 | 2.0 | 6% | 0% | 77% | 42 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 8,569 | 12,206 | 5.2 | 36% | 50% | 79% | 3,592 KB | 545 (+1) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,546 | 13,168 | 0.2 | 43% | 21% | 100% | 357 KB | 2 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 8,527 | 105,688 | 16.5 | 56% | 0% | 100% | 247 KB | 2 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | D F C | 7,816 | 10,356 | 15.8 | 35% | 0% | 95% | 8,119 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D E B | 7,656 | 106,010 | 39.0 | 74% | 11% | 96% | 1,431 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D F B | 7,584 | 11,789 | 37.0 | 38% | 14% | 99% | 696 KB | 2 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | D F B | 7,549 | 13,806 | 39.5 | 26% | 48% | 83% | 330 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D E C | 7,541 | 14,469 | 14.2 | 69% | 0% | 94% | 371 KB | 2 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D D A | 7,180 | 9,502 | 38.0 | 69% | 0% | 100% | 122 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D E B | 7,083 | 218,577 | 31.9 | 50% | 13% | 95% | 1,414 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | D F A | 6,947 | 16,521 | 38.9 | 27% | 0% | 99% | 240 KB | 9 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D F C | 6,813 | 23,690 | 20.0 | 37% | 0% | 90% | 43 KB | 16 (+1) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | D E C | 6,667 | 11,958 | 0.0 | 64% | 0% | 100% | 472 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 6,623 | 22,327 | 0.0 | 29% | 0% | – | 824 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D D C | 6,526 | 8,186 | 15.6 | 70% | 24% | 91% | 140 KB | 1 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D E B | 6,445 | 10,700 | 0.0 | 64% | 3% | 95% | 589 KB | 1 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D D B | 6,425 | 14,434 | 27.4 | 66% | 34% | 98% | 1,172 KB | 0 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D F A | 6,256 | 9,806 | 17.9 | 39% | 32% | 90% | 148 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | D F D | 6,240 | 22,806 | 29.4 | 3% | 0% | 100% | 158 KB | 1 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D E C | 5,948 | 7,137 | 23.8 | 59% | 0% | 80% | 959 KB | 1 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | D E C | 5,939 | 10,255 | 19.9 | 67% | 0% | 98% | 41 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D E D | 5,872 | 8,843 | 39.9 | 56% | 0% | – | 421 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | D F C | 5,722 | 27,957 | 11.8 | 80% | 6% | 98% | 150 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D E C | 5,683 | 50,342 | 0.0 | 53% | 14% | 50% | 479 KB | 1 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | D D D | 5,594 | 7,443 | 0.0 | 62% | 17% | – | 3,234 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | D C B | 5,518 | 13,246 | 7.3 | 81% | 0% | 80% | 616 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 5,506 | 5,906 | 73.0 | 73% | 17% | 100% | 789 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | D E D | 5,397 | 9,184 | 46.4 | 48% | 31% | – | 387 KB | 3 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D E D | 5,294 | 8,004 | 0.8 | 69% | 47% | 0% | 164 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,226 | 11,932 | 3.7 | 56% | 0% | 90% | 319 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D F C | 5,146 | 11,557 | 10.8 | 57% | 0% | 100% | 49 KB | 3 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E C B | 4,947 | 6,159 | 24.1 | 77% | 14% | 100% | 106 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 4,827 | 12,642 | 9.0 | 45% | 59% | 72% | 70 KB | 13 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 4,777 | 20,071 | 10.1 | 65% | 7% | 0% | 141 KB | 14 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F A | 4,750 | 15,973 | 26.0 | 33% | 0% | 99% | 377 KB | 49 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E F E | 4,739 | 9,932 | 22.2 | 27% | 7% | 87% | 1,155 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 4,374 | 5,219 | 0.1 | 14% | 14% | 86% | 904 KB | 2 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E E A | 4,329 | 10,447 | 10.8 | 53% | 0% | 92% | 256 KB | 0 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 4,318 | 8,374 | 0.3 | 45% | 18% | 0% | 509 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | E F C | 4,303 | 6,852 | 19.9 | 59% | 0% | 95% | 311 KB | 4 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,260 | 5,118 | 23.8 | 30% | 0% | 96% | 815 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | E C B | 3,922 | 7,007 | 14.8 | 74% | 4% | 100% | 4,314 KB | 21 (+1) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 3,897 | 5,148 | 11.1 | 17% | 0% | – | 83 KB | 2 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,865 | 10,384 | 0.0 | 10% | 8% | 0% | 451 KB | 4 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 3,679 | 11,439 | 25.7 | 53% | 28% | 99% | 178 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | E F C | 3,672 | 43,409 | 19.4 | 9% | 3% | 64% | 155 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E C C | 3,628 | 7,566 | 11.2 | 71% | 19% | 98% | 124 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 3,599 | 5,752 | 16.3 | 30% | 0% | 100% | 136 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E E D | 3,540 | 5,646 | 37.2 | 54% | 7% | – | 198 KB | 3 (+1) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E D B | 3,521 | 13,423 | 38.0 | 64% | 0% | 97% | 107 KB | 4 (-1) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E C B | 3,492 | 4,919 | 40.6 | 71% | 12% | 94% | 140 KB | 8 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E E A | 3,459 | 137,751 | 0.0 | 81% | 0% | 93% | 211 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 3,447 | 8,995 | 0.0 | 39% | 28% | 96% | 432 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 3,370 | 7,208 | 20.4 | 25% | 15% | 95% | 272 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 3,334 | 13,469 | 20.0 | 68% | 17% | 99% | 625 KB | 11 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E F C | 3,259 | 78,934 | 29.1 | 55% | 27% | 54% | 99 KB | 1 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 3,212 | 6,042 | 14.8 | 52% | 0% | 76% | 1,538 KB | 6 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E E B | 3,170 | 10,360 | 12.3 | 66% | 0% | 100% | 396 KB | 12 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F B | 3,156 | 6,648 | 17.2 | 6% | 0% | 81% | 377 KB | 7 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 3,001 | 12,865 | 21.9 | 26% | 46% | 92% | 215 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 2,991 | 4,150 | 10.6 | 29% | 25% | 98% | 518 KB | 1 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E E A | 2,974 | 4,309 | 12.2 | 71% | 14% | 93% | 161 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 2,962 | 12,081 | 13.0 | 28% | 18% | 98% | 236 KB | 5 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,957 | 5,081 | 1.8 | 76% | 0% | 100% | 183 KB | 7 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 2,927 | 24,553 | 0.0 | 36% | 0% | – | 200 KB | 28 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 2,903 | 5,210 | 19.9 | 33% | 8% | 95% | 502 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 2,878 | 3,820 | 9.8 | 62% | 0% | 94% | 86 KB | 1 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 2,833 | 6,293 | 25.2 | 27% | 10% | 93% | 69 KB | 10 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,782 | 10,313 | 7.1 | 12% | 33% | 97% | 534 KB | 11 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E D B | 2,702 | 3,516 | 43.5 | 69% | 48% | 100% | 316 KB | 2 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E F C | 2,696 | 10,622 | 22.6 | 60% | 0% | 100% | 346 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 2,695 | 5,490 | 13.9 | 0% | 10% | 76% | 268 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,656 | 5,151 | 18.1 | 41% | 24% | 98% | 386 KB | 2 (+1) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 2,561 | 9,640 | 28.3 | 30% | 28% | 99% | 427 KB | 17 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,556 | 3,890 | 17.8 | 39% | 0% | 99% | 127 KB | 23 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F C | 2,554 | 7,757 | 1.2 | 47% | 14% | 94% | 5,596 KB | 1 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | E F B | 2,541 | 17,590 | 37.9 | 40% | 0% | 81% | 413 KB | 9 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E C E | 2,523 | 12,305 | 15.1 | 74% | 33% | 100% | 1,056 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 2,468 | 3,403 | 36.7 | 33% | 7% | 99% | 221 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,395 | 7,525 | 6.5 | 57% | 10% | 98% | 134 KB | 231 (+3) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,371 | 8,055 | 10.7 | 47% | 0% | 0% | 285 KB | 24 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E F B | 2,329 | 20,921 | 6.5 | 46% | 27% | 78% | 83 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E E D | 2,320 | 8,888 | 0.0 | 57% | 36% | – | 725 KB | 2 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E E A | 2,282 | 3,680 | 16.5 | 53% | 43% | 99% | 447 KB | 12 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 2,263 | 3,012 | 15.4 | 39% | 28% | 100% | 213 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,051 | 8,330 | 0.1 | 46% | 0% | 84% | 395 KB | 3 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | E F B | 2,018 | 2,937 | 24.8 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E F C | 1,991 | 48,733 | 15.8 | 16% | 0% | 100% | 378 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 1,934 | 5,838 | 19.5 | 0% | 0% | 98% | 489 KB | 52 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,900 | 2,121 | 21.8 | 19% | 33% | 97% | 824 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,834 | 2,948 | 26.4 | 51% | 0% | 80% | 203 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,819 | 4,535 | 0.0 | 50% | 0% | 42% | 266 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | E F C | 1,802 | 8,155 | 41.8 | 34% | 0% | 52% | 3,052 KB | 2 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,777 | 4,056 | 34.8 | 37% | 0% | 100% | 403 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | E F B | 1,771 | 3,081 | 8.5 | 51% | 0% | 80% | 552 KB | 2 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 1,683 | 53,670 | 0.0 | 51% | 26% | – | 8,190 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,561 | 4,645 | 22.2 | 34% | 0% | 100% | 152 KB | 1 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 1,555 | 2,234 | 11.2 | 56% | 0% | 100% | 66 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | E E D | 1,553 | 5,145 | 0.0 | 82% | 0% | 0% | 322 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F B | 1,542 | 20,640 | 0.0 | 14% | 5% | 82% | 554 KB | 28 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 1,504 | 14,793 | 35.2 | 65% | 0% | 73% | 188 KB | 0 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E E A | 1,486 | 7,465 | 24.6 | 52% | 0% | 96% | 393 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E E D | 1,469 | 10,514 | 3.9 | 64% | 0% | – | 296 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 1,437 | 3,141 | 22.4 | 33% | 38% | 97% | 544 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | E F C | 1,426 | 2,895 | 0.0 | 45% | 0% | 93% | 266 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,421 | 6,459 | 26.6 | 0% | 16% | 100% | 526 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,290 | 2,637 | 5.2 | 14% | 25% | 97% | 7,014 KB | 18 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F D | 1,207 | 31,790 | 0.3 | 82% | 0% | 29% | 1,471 KB | 1,107 (+2) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,166 | 7,847 | 6.1 | 43% | 10% | 93% | 288 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 1,153 | 1,728 | 15.3 | 32% | 0% | – | 50 KB | 3 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 1,047 | 3,566 | 8.7 | 41% | 0% | 98% | 342 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | E F E | 1,040 | 20,846 | 5.0 | 71% | 7% | 74% | 149 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,027 | 3,497 | 12.3 | 30% | 11% | 91% | 551 KB | 2 (+1) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 983 | 3,217 | 9.7 | 0% | 0% | 99% | 99 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | F F B | 959 | 2,035 | 29.6 | 60% | 0% | 100% | 980 KB | 104 (+2) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F E C | 885 | 4,916 | 7.2 | 70% | 0% | 100% | 151 KB | 2 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 847 | 4,180 | 7.0 | 19% | 0% | 96% | 522 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 821 | 2,806 | 13.1 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 796 | 4,340 | 13.1 | 0% | 0% | – | 411 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F D | 750 | 2,533 | 28.2 | 47% | 0% | 47% | 100 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F E C | 706 | 2,648 | 17.2 | 72% | 0% | 98% | 426 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 688 | 5,984 | 28.6 | 17% | 0% | 94% | 317 KB | 159 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 666 | 813 | 0.0 | 21% | 0% | 33% | 398 KB | 461 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 645 | 796,255 | 48.6 | 12% | 0% | 100% | 703 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 513 | 11,111 | 0.0 | 28% | 0% | 99% | 478 KB | 6 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 492 | 2,648 | 20.1 | 28% | 0% | 91% | 442 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 482 | 2,285 | 26.8 | 38% | 0% | 99% | 122 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 421 | 761 | 0.1 | 62% | 16% | 0% | 648 KB | 3 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 374 | 6,888 | 0.0 | 16% | 0% | – | 144 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 239 | 2,615 | 0.0 | 24% | 0% | 0% | 1,153 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 222 | 1,574 | 0.0 | 40% | 18% | 98% | 414 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 193 | 2,713 | 11.4 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 186 | 3,061 | 2.4 | 49% | 0% | 100% | 163 KB | 11 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 107 | 3,456 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 94 | 10,191 | 17.3 | 36% | 0% | 93% | 576 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 89 | 3,950 | 26.9 | 19% | 0% | 100% | 617 KB | 1 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 88 | 1,871 | 17.6 | 0% | 0% | 92% | 303 KB | 23 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 76 | 3,766 | 13.0 | 50% | 0% | 99% | 298 KB | 5 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 54 | 655 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 19 | 2,909 | 16.4 | 40% | 0% | 95% | 66 KB | 3 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 39.0 | 78% | 27% | 86% | 2,197 KB | 1,438 (+2) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 2,975 | 32.7 | 0% | 0% | 91% | 2,600 KB | 36 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | 0 | 13,254 | 26.6 | 51% | 0% | 98% | 231 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F C B | – | – | 23.6 | 82% | 43% | 98% | 976 KB | 4 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | 0 | 860 | 21.9 | 61% | 0% | 98% | 363 KB | 1 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F E C | – | – | 21.4 | 59% | 19% | 94% | 342 KB | 4 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 21.2 | 5% | 0% | 20% | 279 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | F F A | 0 | 6,488 | 19.6 | 2% | 0% | 97% | 219 KB | 5 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 146 | 18.9 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 17.8 | – | – | 97% | 94 KB | 16 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 8 | 15.5 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 5,897 | 14.4 | 0% | 0% | – | 226 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | – | – | 14.0 | – | – | – | 55 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 2,957 | 14.0 | 0% | 0% | 97% | 49 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 0 | 2,875 | 12.8 | 0% | 0% | 98% | 43 KB | 1 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 11.5 | 0% | 0% | 98% | 723 KB | 5 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 0 | 1,915 | 11.3 | 30% | 0% | 89% | 6,579 KB | 8 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 3,487 | 9.9 | 21% | 0% | 89% | 38 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 8.7 | – | – | 98% | 149 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 2,119 | 8.2 | 0% | 0% | 96% | 122 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 954 | 7.7 | 18% | 0% | 96% | 787 KB | 2 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 7.5 | – | – | 90% | 195 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 7.4 | – | – | – | 115 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | – | – | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F C | – | – | 6.8 | 42% | 0% | 57% | 206 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 17,926 | 6.2 | 20% | 0% | 96% | 24 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 5.5 | 60% | 72% | 0% | 1,879 KB | 458 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 2,155 | 4.8 | 0% | 0% | 74% | 161 KB | 2 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 347 | 4.6 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 0 | 653 | 3.4 | 25% | 0% | 100% | 1,117 KB | 5 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1 | 3.1 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 7,401 | 2.7 | 29% | 0% | 100% | 258 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,308 | 1.9 | 0% | 0% | 33% | 140 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 0 | 0 | 1.8 | – | – | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 0 | 1.4 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 71% | 11% | 78% | 816 KB | 5 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 74% | 34% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 94 | 0.1 | 0% | 0% | 15% | 904 KB | 1,289 (+1) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 0 | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 0 | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | F E D | 0 | 0 | 0.0 | 53% | 56% | 32% | 1,085 KB | 34 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F C | – | – | 0.0 | 29% | 11% | 64% | 84 KB | 5 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 596 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,893 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
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
