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
_293 repos, last measured 2026-10-23. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (293)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 60,466 | 80,846 | 24.6 | 64% | 9% | 91% | 165 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 52,174 | 366,406 | 59.5 | 15% | 2% | 88% | 3,975 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A D B | 51,054 | 58,939 | 34.2 | 61% | 17% | 87% | 544 KB | 11 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A E A | 51,030 | 85,092 | 59.5 | 58% | 50% | 98% | 184 KB | 118 (+1) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 43,539 | 46,965 | 70.3 | 6% | 0% | 73% | 3,078 KB | 2,010 (+9) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 43,508 | 46,384 | 44.7 | 74% | 23% | 88% | 823 KB | 1 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A F C | 41,533 | 50,953 | 163 | 25% | 4% | 89% | 2,294 KB | 3 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B F B | 36,869 | 56,145 | 8.3 | 48% | 6% | 81% | 281 KB | 329 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | B E B | 36,401 | 170,644 | 17.1 | 43% | 12% | 92% | 213 KB | 0 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B C A | 35,571 | 78,537 | 69.9 | 72% | 35% | 96% | 169 KB | 2 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 33,990 | 95,387 | 24.5 | 36% | 33% | 39% | 4,722 KB | 96 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 32,930 | 48,536 | 25.1 | 82% | 56% | 90% | 650 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B D D | 32,675 | 78,175 | 0.2 | 68% | 20% | 38% | 1,271 KB | 439 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B E B | 30,710 | 36,473 | 31.1 | 53% | 46% | 100% | 1,060 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | B D B | 29,906 | 39,175 | 24.8 | 65% | 22% | 99% | 628 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 29,535 | 99,606 | 12.7 | 62% | 35% | 19% | 726 KB | 4 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B C C | 29,130 | 33,689 | 31.6 | 79% | 41% | 91% | 363 KB | 9 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B F B | 27,821 | 34,972 | 176 | 39% | 44% | 96% | 2,716 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 27,794 | 93,841 | 43.5 | 40% | 58% | 100% | 55 KB | 0 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 27,667 | 129,151 | 97.2 | 0% | 0% | 46% | 306 KB | 4 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | B F B | 27,480 | 28,288 | 27.6 | 71% | 0% | 98% | 231 KB | 1 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B E C | 26,730 | 30,355 | 35.7 | 52% | 24% | 100% | 315 KB | 0 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B D A | 26,610 | 40,646 | 103 | 67% | 16% | 99% | 218 KB | 14 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 25,309 | 29,111 | 31.5 | 29% | 23% | 100% | 1,374 KB | 92 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 24,886 | 37,520 | 48.6 | 75% | 47% | 100% | 354 KB | 2 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B D C | 24,127 | 38,841 | 65.3 | 61% | 26% | 85% | 559 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B D B | 23,649 | 110,584 | 27.6 | 61% | 43% | 100% | 890 KB | 33 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 23,636 | 33,471 | 99.3 | 34% | 11% | 92% | 3,661 KB | 72 (+1) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B D B | 23,507 | 258,081 | 93.1 | 67% | 36% | 95% | 584 KB | 2 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | B F A | 23,218 | 31,655 | 62.3 | 33% | 62% | 96% | 275 KB | 6,393 (+9) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | B C B | 22,341 | 26,023 | 34.2 | 76% | 53% | 91% | 1,545 KB | 3 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B B D | 21,971 | 19,375 | 0.0 | 88% | 26% | – | 226 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 21,810 | 39,221 | 18.2 | 34% | 32% | 96% | 6,732 KB | 121 (+1) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B F D | 21,652 | 26,559 | 0.0 | 36% | 32% | – | 298 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B E B | 21,098 | 43,071 | 9.4 | 54% | 35% | 96% | 781 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | B E B | 20,830 | 49,221 | 15.1 | 48% | 0% | 88% | 240 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B E A | 20,251 | 67,290 | 65.8 | 52% | 22% | 90% | 60 KB | 0 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C C B | 19,742 | 30,641 | 20.9 | 78% | 29% | 100% | 962 KB | 1 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | C F D | 19,680 | 34,523 | 7.8 | 34% | 29% | – | 100 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 19,623 | 36,590 | 33.3 | 26% | 19% | 96% | 877 KB | 4 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C E B | 19,146 | 32,167 | 15.8 | 69% | 0% | 98% | 86 KB | 6 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 18,738 | 28,238 | 0.0 | 50% | 43% | – | 320 KB | 2 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 18,594 | 83,269 | 12.9 | 65% | 0% | 76% | 427 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | C D C | 18,557 | 31,802 | 66.4 | 68% | 4% | 100% | 691 KB | 14 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C B A | 18,249 | 24,503 | 27.6 | 85% | 27% | 97% | 170 KB | 4 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C D D | 18,026 | 466,590 | 0.0 | 70% | 38% | 0% | 3,283 KB | 1 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C D D | 17,342 | 28,965 | 0.0 | 60% | 45% | – | 1,218 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C D C | 17,030 | 22,617 | 24.2 | 68% | 8% | 100% | 162 KB | 33 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C A A | 16,879 | 129,938 | 29.7 | 92% | 70% | 100% | 158 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | C F D | 16,841 | 55,502 | 18.5 | 18% | 2% | 41% | 140 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 16,779 | 23,927 | 102 | 17% | 40% | 76% | 358 KB | 52 (+1) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,327 | 31,635 | 33.0 | 5% | 20% | 100% | 225 KB | 7 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C C C | 16,213 | 33,061 | 7.5 | 72% | 37% | 100% | 100 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C F B | 16,055 | 16,764 | 0.0 | 46% | 4% | 97% | 589 KB | 1 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 15,789 | 20,886 | 21.0 | 78% | 57% | 96% | 668 KB | 9 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C B B | 15,521 | 18,750 | 13.6 | 90% | 19% | 84% | 1,188 KB | 13 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C C A | 15,321 | 21,980 | 23.7 | 82% | 37% | 99% | 200 KB | 6 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C E A | 15,063 | 19,355 | 2.7 | 59% | 0% | 100% | 258 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 15,033 | 19,501 | 5.1 | 19% | 17% | 100% | 422 KB | 134 (+1) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 14,663 | 59,797 | 42.0 | 33% | 4% | 100% | 78 KB | 2 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C C C | 14,656 | 44,944 | 13.4 | 82% | 8% | 56% | 431 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | C E A | 14,568 | 32,235 | 18.0 | 64% | 0% | 96% | 90 KB | 1 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C E C | 14,354 | 29,382 | 22.5 | 71% | 4% | 86% | 757 KB | 5 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 14,289 | 20,611 | 0.0 | 79% | 56% | 34% | 1,053 KB | 32 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C F D | 13,211 | 18,441 | 0.0 | 80% | 9% | 14% | 278 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 13,188 | 21,710 | 36.2 | 33% | 38% | 84% | 330 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | C E B | 12,906 | 21,761 | 13.4 | 55% | 40% | 90% | 537 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C F B | 12,305 | 18,676 | 12.8 | 43% | 25% | 97% | 589 KB | 1 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 11,994 | 48,301 | 27.0 | 79% | 0% | 100% | 2,112 KB | 5 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 11,770 | 48,974 | 0.0 | 56% | 12% | 52% | 479 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C F B | 11,726 | 28,590 | 37.6 | 32% | 15% | 98% | 570 KB | 37 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 11,720 | 15,774 | 12.8 | 72% | 0% | 96% | 718 KB | 9 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C C D | 11,623 | 15,602 | 8.9 | 70% | 24% | 23% | 195 KB | 2 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C D D | 11,607 | 33,127 | 72.5 | 65% | 44% | 25% | 837 KB | 16 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | C F A | 11,362 | 77,647 | 26.3 | 33% | 0% | 95% | 377 KB | 49 (+1) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | C E C | 11,355 | 20,696 | 0.0 | 73% | 13% | 100% | 472 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C C D | 11,338 | 18,181 | 34.8 | 72% | 5% | 100% | 599 KB | 22 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | C E C | 11,323 | 19,728 | 17.7 | 67% | 0% | 96% | 41 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C C B | 11,213 | 18,387 | 29.1 | 78% | 55% | 79% | 1,445 KB | 70,278 (+28) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C D A | 11,114 | 21,547 | 15.6 | 66% | 11% | 95% | 129 KB | 5 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C F D | 11,074 | 25,467 | 0.0 | 40% | 0% | – | 824 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C E B | 10,925 | 413,153 | 30.3 | 48% | 9% | 97% | 1,414 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | C E C | 10,844 | 17,588 | 31.9 | 54% | 22% | 100% | 560 KB | 5 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C B D | 10,754 | 14,947 | 7.8 | 81% | 0% | – | 613 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | C D C | 10,729 | 35,812 | 0.0 | 68% | 11% | 100% | 488 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 10,639 | 12,168 | 20.8 | 69% | 63% | 100% | 557 KB | 1 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 10,633 | 29,409 | 26.9 | 46% | 0% | 95% | 458 KB | 19 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 10,267 | 17,306 | 40.3 | 34% | 19% | 100% | 251 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C E D | 10,230 | 14,097 | 0.0 | 59% | 42% | 36% | 308 KB | 248 (+2) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | C D D | 10,105 | 8,802 | 0.0 | 66% | 14% | – | 3,234 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | C F B | 10,002 | 12,986 | 14.8 | 21% | 35% | 97% | 326 KB | 161 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D E B | 9,605 | 19,427 | 21.8 | 57% | 19% | 90% | 1,044 KB | 5 (+1) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D F B | 9,578 | 19,863 | 32.1 | 30% | 50% | 100% | 1,250 KB | 8 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 9,342 | 29,997 | 0.0 | 30% | 0% | 0% | 601 KB | 1 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F D | 9,329 | 10,631 | 20.2 | 28% | 11% | – | 700 KB | 4 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 9,322 | 36,997 | 0.0 | 16% | 60% | 96% | 407 KB | 1 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D F B | 9,101 | 14,090 | 33.4 | 37% | 37% | 99% | 638 KB | 2 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D F B | 8,940 | 48,214 | 1.2 | 33% | 28% | 87% | 3,340 KB | 7 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D E A | 8,663 | 12,421 | 15.0 | 58% | 48% | 93% | 148 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D C C | 8,573 | 24,515 | 15.0 | 71% | 25% | 95% | 347 KB | 2 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F D | 8,527 | 82,652 | 16.6 | 45% | 0% | – | 245 KB | 2 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | D F D | 8,455 | 15,216 | 10.8 | 49% | 0% | 0% | 285 KB | 24 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,010 | 12,621 | 0.2 | 51% | 26% | 100% | 353 KB | 2 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D F B | 7,823 | 19,911 | 13.4 | 34% | 18% | 75% | 236 KB | 5 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 7,710 | 14,069 | 28.6 | 6% | 11% | 100% | 134 KB | 7 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | D E B | 7,704 | 7,882 | 10.0 | 44% | 8% | 94% | 86 KB | 1 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D E A | 7,676 | 13,255 | 34.8 | 49% | 0% | 100% | 121 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D E B | 7,656 | 34,525 | 35.0 | 71% | 16% | 97% | 1,431 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,340 | 14,635 | 5.0 | 36% | 44% | 83% | 3,516 KB | 543 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 7,002 | 12,434 | 48.6 | 0% | 46% | 89% | 67 KB | 61 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D E C | 6,813 | 26,473 | 18.6 | 52% | 6% | 99% | 58 KB | 15 (+0) |
| [integry/propr](https://github.com/integry/propr) | D E B | 6,785 | 11,197 | 15.2 | 55% | 36% | 100% | 4,314 KB | 20 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 6,752 | 10,593 | 0.1 | 34% | 3% | 73% | 152 KB | 29 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D D B | 6,425 | 11,728 | 24.3 | 68% | 40% | 100% | 1,172 KB | 0 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D C A | 6,361 | 13,213 | 31.0 | 71% | 35% | 90% | 102 KB | 229 (-2) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D D | 6,309 | 10,016 | 14.7 | 66% | 16% | 39% | 140 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 6,293 | 8,050 | 76.8 | 78% | 12% | 99% | 765 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | D C C | 6,198 | 31,334 | 11.5 | 90% | 20% | 98% | 143 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | D E D | 6,054 | 12,823 | 0.7 | 51% | 28% | 0% | 164 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F D | 5,884 | 15,321 | 0.0 | 23% | 28% | 47% | 221 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D E D | 5,872 | 12,127 | 37.1 | 51% | 0% | – | 421 KB | 1 (+1) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,808 | 6,641 | 23.8 | 44% | 0% | 87% | 950 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 5,743 | 11,310 | 0.0 | 38% | 24% | 98% | 424 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D F B | 5,635 | 5,835 | 24.4 | 14% | 12% | 90% | 808 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 5,394 | 9,679 | 21.5 | 30% | 15% | 95% | 271 KB | 1 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | D F C | 5,369 | 14,949 | 40.4 | 38% | 0% | 52% | 3,052 KB | 2 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | D E E | 5,315 | 11,520 | 14.9 | 40% | 68% | 76% | 1,538 KB | 5 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,226 | 7,593 | 3.7 | 2% | 0% | 90% | 319 KB | 1 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D F C | 5,146 | 13,021 | 10.8 | 54% | 0% | 100% | 49 KB | 3 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D E C | 5,060 | 5,870 | 14.0 | 60% | 32% | 94% | 128 KB | 1 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,059 | 14,666 | 21.1 | 12% | 0% | 98% | 489 KB | 29 (+1) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E C B | 4,989 | 8,165 | 19.8 | 71% | 4% | 96% | 499 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | E F A | 4,857 | 9,127 | 29.0 | 20% | 14% | 100% | 316 KB | 159 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 4,827 | 12,452 | 7.4 | 50% | 47% | 97% | 70 KB | 13 (-2) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E E B | 4,789 | 5,793 | 22.9 | 70% | 14% | 96% | 104 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 4,786 | 6,960 | 42.0 | 47% | 6% | – | 378 KB | 3 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 4,518 | 7,837 | 10.6 | 49% | 5% | – | 83 KB | 2 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E E C | 4,383 | 8,283 | 13.5 | 44% | 0% | 94% | 8,119 KB | 1 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | E F B | 4,380 | 6,091 | 19.9 | 16% | 14% | 90% | 436 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E F C | 4,374 | 4,974 | 0.0 | 21% | 16% | 86% | 873 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 4,325 | 6,606 | 24.6 | 40% | 0% | 99% | 127 KB | 23 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | E F C | 4,303 | 7,429 | 23.9 | 59% | 0% | 96% | 311 KB | 4 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E D C | 4,284 | 16,414 | 37.7 | 63% | 8% | 73% | 188 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 4,253 | 13,210 | 25.9 | 46% | 39% | 99% | 175 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | E F C | 4,042 | 4,971 | 9.6 | 24% | 0% | 99% | 99 KB | 4 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 4,027 | 7,456 | 8.5 | 58% | 17% | – | 137 KB | 14 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | E F B | 3,981 | 6,345 | 1.7 | 4% | 0% | 75% | 42 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 3,930 | 8,998 | 36.0 | 74% | 6% | – | 198 KB | 2 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,865 | 8,353 | 0.0 | 16% | 9% | 0% | 436 KB | 4 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E E B | 3,758 | 6,727 | 5.6 | 53% | 13% | 77% | 78 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | E F B | 3,681 | 15,960 | 33.2 | 38% | 0% | 91% | 2,600 KB | 36 (+1) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 3,638 | 6,958 | 0.3 | 54% | 10% | 0% | 472 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,628 | 10,599 | 10.9 | 54% | 43% | 97% | 111 KB | 0 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E E C | 3,603 | 6,542 | 37.3 | 55% | 3% | 99% | 221 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 3,566 | 7,272 | 1.8 | 58% | 22% | 100% | 182 KB | 7 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E E B | 3,521 | 12,446 | 37.2 | 71% | 0% | 96% | 106 KB | 5 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 3,520 | 7,263 | 25.9 | 0% | 16% | 100% | 526 KB | 0 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 3,446 | 5,132 | 0.0 | 44% | 0% | 42% | 266 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 3,402 | 11,236 | 29.4 | 30% | 22% | 100% | 427 KB | 17 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E E C | 3,383 | 34,586 | 0.3 | 82% | 0% | 94% | 1,468 KB | 1,104 (+4) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 3,347 | 5,814 | 43.7 | 59% | 25% | 99% | 310 KB | 2 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 3,341 | 4,190 | 11.8 | 1% | 30% | 98% | 518 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E E E | 3,334 | 19,508 | 22.7 | 76% | 12% | 99% | 625 KB | 11 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E E E | 3,321 | 9,496 | 22.0 | 44% | 5% | 93% | 1,115 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 3,203 | 3,972 | 13.9 | 54% | 0% | 100% | 161 KB | 0 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E E B | 3,199 | 5,526 | 27.2 | 47% | 0% | 81% | 203 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | E E C | 3,194 | 4,707 | 0.0 | 51% | 43% | 93% | 266 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F B | 3,156 | 7,295 | 17.8 | 17% | 0% | 76% | 375 KB | 7 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 3,080 | 12,483 | 35.1 | 35% | 0% | 93% | 240 KB | 9 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 3,021 | 7,682 | 25.1 | 38% | 24% | 97% | 69 KB | 10 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 2,977 | 8,384 | 13.2 | 57% | 0% | 100% | 396 KB | 12 (+1) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 2,910 | 10,722 | 6.3 | 35% | 15% | 93% | 267 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E E B | 2,890 | 4,381 | 40.8 | 66% | 24% | 92% | 142 KB | 8 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,782 | 11,242 | 7.8 | 11% | 49% | 99% | 530 KB | 11 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | E F A | 2,780 | 22,587 | 21.8 | 27% | 0% | 95% | 218 KB | 5 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | E E D | 2,764 | 12,215 | 3.4 | 60% | 0% | – | 296 KB | 1 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | E F A | 2,749 | 6,466 | 2.0 | 55% | 0% | 100% | 163 KB | 11 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 2,743 | 3,831 | 14.9 | 9% | 0% | 100% | 134 KB | 0 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E D A | 2,739 | 7,074 | 9.5 | 62% | 0% | 97% | 249 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E F D | 2,696 | 9,509 | 18.6 | 67% | 0% | 100% | 343 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,656 | 6,154 | 19.4 | 33% | 22% | 100% | 386 KB | 1 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,626 | 3,683 | 0.1 | 53% | 0% | 84% | 391 KB | 3 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 2,624 | 6,951 | 33.2 | 44% | 0% | 100% | 403 KB | 2 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | E F B | 2,541 | 29,019 | 35.1 | 57% | 0% | 99% | 405 KB | 9 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | E F B | 2,528 | 3,334 | 8.9 | 52% | 0% | 80% | 552 KB | 2 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E D E | 2,523 | 13,055 | 14.9 | 65% | 35% | 100% | 1,012 KB | 0 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E E D | 2,500 | 19,163 | 0.0 | 55% | 7% | 36% | 154 KB | 110 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,395 | 7,361 | 7.2 | 61% | 0% | 100% | 176 KB | 225 (+1) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E E C | 2,371 | 4,043 | 10.2 | 57% | 0% | 100% | 66 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E D A | 2,282 | 3,530 | 16.5 | 63% | 44% | 99% | 451 KB | 12 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E E A | 2,263 | 14,583 | 24.8 | 58% | 0% | 100% | 393 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | E F B | 2,243 | 6,917 | 11.4 | 67% | 0% | 97% | 56 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 2,241 | 7,607 | 21.0 | 27% | 0% | 59% | 278 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 2,235 | 4,082 | 29.5 | 50% | 0% | 100% | 980 KB | 101 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 2,179 | 3,330 | 16.0 | 36% | 13% | – | 49 KB | 3 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 1,994 | 4,992 | 15.9 | 39% | 17% | 100% | 194 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,947 | 2,919 | 20.8 | 11% | 30% | 97% | 766 KB | 1 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F D | 1,914 | 7,826 | 0.9 | 59% | 6% | – | 5,522 KB | 1 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,735 | 27,276 | 0.0 | 43% | 0% | – | 200 KB | 28 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 1,693 | 47,357 | 0.0 | 35% | 15% | – | 8,190 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | E F D | 1,451 | 6,819 | 0.0 | 43% | 0% | 0% | 315 KB | 0 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 1,437 | 2,441 | 23.4 | 36% | 24% | 97% | 544 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 1,425 | 9,084 | 17.4 | 59% | 6% | 98% | 417 KB | 1 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,406 | 121,703 | 0.0 | 76% | 0% | 96% | 211 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 1,368 | 3,195 | 0.0 | 21% | 0% | 33% | 397 KB | 461 (+1) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | E F C | 1,253 | 2,381 | 22.2 | 82% | 0% | 98% | 363 KB | 1 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F C | 1,251 | 11,391 | 0.0 | 30% | 6% | 56% | 554 KB | 28 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 1,220 | 5,024 | 28.0 | 42% | 0% | 47% | 100 KB | 0 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,149 | 4,649 | 25.0 | 61% | 0% | 100% | 149 KB | 1 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,109 | 9,315 | 27.9 | 3% | 0% | 100% | 122 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | E F D | 1,087 | 4,890 | 13.7 | 58% | 0% | – | 298 KB | 5 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | E F B | 1,032 | 2,315 | 24.1 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,027 | 3,585 | 11.6 | 6% | 11% | 91% | 536 KB | 1 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,027 | 2,692 | 5.0 | 17% | 30% | 94% | 7,014 KB | 18 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | F F B | 963 | 2,296 | 9.0 | 47% | 0% | 95% | 342 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F D C | 954 | 2,806 | 6.6 | 65% | 0% | 100% | 151 KB | 2 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 935 | 6,740 | 0.0 | 30% | 0% | – | 646 KB | 2 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F B | 921 | 6,072 | 14.2 | 9% | 8% | 73% | 257 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 878 | 3,972 | 9.1 | 38% | 0% | 97% | 787 KB | 2 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 821 | 12,769 | 11.8 | 54% | 0% | 96% | 26 KB | 1 (+1) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 812 | 16,368 | 14.3 | 15% | 0% | – | 411 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 788 | 16,145 | 3.8 | 62% | 8% | 78% | 149 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 780 | 8,979 | 21.7 | 34% | 34% | 98% | 215 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 723 | 3,372 | 0.0 | 29% | 0% | 0% | 1,121 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F E D | 707 | 1,224 | 0.1 | 63% | 9% | 0% | 635 KB | 3 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 555 | 9,152 | 0.0 | 52% | 0% | – | 111 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 528 | 2,607 | 13.6 | 16% | 0% | 97% | 49 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 440 | 4,239 | 11.4 | 48% | 0% | 89% | 6,579 KB | 8 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 294 | 2,186,139 | 47.9 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 283 | 1,623 | 0.0 | 29% | 0% | 98% | 384 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 264 | 18,437 | 26.1 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 216 | 619 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 200 | 26,818 | 6.1 | 12% | 0% | 96% | 24 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F E E | 167 | 1,078 | 18.5 | 61% | 0% | 94% | 555 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 159 | 6,018 | 9.9 | 20% | 0% | 90% | 38 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 109 | 4,957 | 29.1 | 19% | 0% | 100% | 617 KB | 1 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 107 | 372 | 4.9 | 0% | 0% | 98% | 72 KB | 4 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 88 | 2,806 | 18.5 | 0% | 0% | 89% | 303 KB | 23 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 82 | 4,100 | 0.0 | 42% | 0% | 0% | 254 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 82 | 857 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 36 | 3,638 | 16.8 | 30% | 0% | 96% | 66 KB | 3 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 35 | 9,457 | 0.0 | 35% | 0% | 39% | 478 KB | 6 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 28 | 190,054 | 10.4 | 13% | 0% | 100% | 378 KB | 1 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F D | 15 | 593 | 3.4 | 0% | 0% | – | 1,116 KB | 5 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 39.1 | 77% | 37% | 89% | 2,197 KB | 1,431 (+7) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | – | – | 30.9 | – | – | 52% | 92 KB | 1 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 264 | 22.5 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F B B | – | – | 22.4 | 80% | 47% | 99% | 976 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 18.5 | – | – | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 16.3 | 34% | 32% | 99% | 342 KB | 4 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 14.8 | 3% | 0% | 98% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 8 | 14.5 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 20,004 | 14.2 | 0% | 0% | – | 223 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 57 | 14.0 | 0% | 0% | – | 55 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | 0 | 199 | 13.4 | 26% | 0% | 90% | 195 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 0 | 5,479 | 12.8 | 29% | 0% | 98% | 43 KB | 1 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 0 | 12.1 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 0 | 0 | 9.9 | – | – | – | 115 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 5,837 | 7.8 | 40% | 0% | 97% | 122 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F B | – | – | 6.3 | 53% | 0% | 72% | 206 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 241 | 5.8 | 0% | 0% | 70% | 466 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 5.4 | 66% | 51% | 0% | 1,790 KB | 458 (+1) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 2,002 | 4.8 | 0% | 0% | 80% | 154 KB | 2 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,279 | 3.5 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 0 | 837 | 1.8 | 32% | 0% | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 804 | 1.3 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 1.0 | 0% | 0% | – | 92 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 71% | 11% | 78% | 816 KB | 5 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 77% | 69% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 133 | 0.1 | 0% | 0% | 9% | 904 KB | 1,283 (+1) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,174 | 0.0 | 0% | 0% | 33% | 61 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 1,737 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | 5% | 0% | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F F C | – | – | 0.0 | 34% | 21% | 55% | 84 KB | 5 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 0.0 | – | – | 98% | 42 KB | 0 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 3,626 | 0.0 | 0% | 0% | – | 112 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 4 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
