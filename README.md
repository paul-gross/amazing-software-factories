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
_293 repos, last measured 2026-10-22. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (293)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A C A | 65,334 | 68,945 | 22.3 | 70% | 7% | 87% | 153 KB | 0 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A D B | 63,155 | 65,067 | 33.6 | 61% | 13% | 100% | 523 KB | 11 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 56,281 | 399,850 | 62.8 | 14% | 2% | 96% | 3,975 KB | 1 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | A D D | 54,212 | 161,602 | 12.1 | 65% | 26% | 49% | 728 KB | 4 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A E A | 51,030 | 85,092 | 59.5 | 58% | 50% | 98% | 184 KB | 118 (+1) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 43,508 | 45,005 | 41.5 | 70% | 25% | 93% | 802 KB | 1 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 42,379 | 55,674 | 68.5 | 5% | 0% | 98% | 3,056 KB | 2,001 (+11) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B F B | 39,926 | 62,258 | 8.1 | 58% | 5% | 78% | 278 KB | 329 (+3) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 39,839 | 49,049 | 165 | 24% | 4% | 89% | 2,294 KB | 3 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | B C B | 39,683 | 35,296 | 28.2 | 74% | 0% | 98% | 231 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B D A | 36,652 | 86,013 | 68.6 | 64% | 34% | 93% | 169 KB | 2 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | B E B | 36,401 | 170,644 | 17.1 | 43% | 12% | 92% | 213 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B E B | 34,391 | 43,374 | 30.2 | 43% | 42% | 100% | 1,060 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 33,990 | 84,287 | 23.5 | 38% | 33% | 34% | 4,722 KB | 96 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 32,930 | 48,536 | 25.1 | 82% | 56% | 90% | 650 KB | 0 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B D D | 32,675 | 78,175 | 0.2 | 68% | 20% | 38% | 1,271 KB | 439 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 30,482 | 34,816 | 31.3 | 82% | 80% | 93% | 363 KB | 9 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | B F A | 30,425 | 109,817 | 25.2 | 58% | 0% | 95% | 377 KB | 48 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | B E C | 30,337 | 34,445 | 35.1 | 44% | 26% | 100% | 310 KB | 0 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B E B | 29,478 | 38,193 | 176 | 44% | 49% | 100% | 3,051 KB | 1 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 28,348 | 98,579 | 41.5 | 45% | 59% | 99% | 55 KB | 0 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | B F A | 28,309 | 27,170 | 22.3 | 46% | 0% | 95% | 218 KB | 5 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 28,040 | 61,701 | 96.1 | 0% | 0% | 46% | 306 KB | 4 (+1) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B D A | 26,942 | 47,012 | 102 | 63% | 15% | 100% | 219 KB | 14 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 25,309 | 29,111 | 31.5 | 29% | 23% | 100% | 1,374 KB | 92 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 25,145 | 41,661 | 48.6 | 74% | 71% | 99% | 354 KB | 2 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B C A | 25,121 | 69,093 | 63.5 | 75% | 50% | 87% | 60 KB | 0 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B D B | 24,369 | 321,032 | 93.2 | 70% | 39% | 98% | 582 KB | 2 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | B D B | 24,210 | 35,502 | 22.8 | 67% | 23% | 99% | 628 KB | 0 |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B D C | 24,127 | 38,841 | 65.3 | 61% | 26% | 85% | 559 KB | 2 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B D B | 23,649 | 110,584 | 27.6 | 61% | 43% | 100% | 890 KB | 33 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 23,636 | 33,471 | 99.3 | 34% | 11% | 92% | 3,661 KB | 72 (+1) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | B D D | 23,611 | 46,882 | 7.5 | 61% | 32% | – | 100 KB | 0 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | B C D | 21,971 | 19,972 | 0.0 | 84% | 25% | – | 226 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B F D | 21,570 | 27,394 | 0.0 | 39% | 28% | – | 289 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | B F C | 21,448 | 25,896 | 17.5 | 29% | 28% | 97% | 6,732 KB | 120 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | B E B | 21,098 | 43,071 | 9.4 | 54% | 35% | 96% | 781 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | C E C | 19,634 | 31,167 | 18.5 | 56% | 45% | 100% | 43 KB | 15 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 19,562 | 29,969 | 61.5 | 40% | 60% | 95% | 768 KB | 6,384 (+11) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 19,413 | 122,735 | 27.1 | 88% | 23% | 100% | 158 KB | 0 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 18,859 | 29,060 | 0.0 | 54% | 43% | – | 317 KB | 2 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C B B | 18,773 | 25,787 | 20.4 | 84% | 18% | 100% | 962 KB | 1 |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C C B | 18,589 | 25,001 | 34.0 | 71% | 51% | 91% | 1,530 KB | 3 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | C C C | 18,587 | 31,080 | 65.9 | 70% | 8% | 100% | 691 KB | 14 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | C C B | 18,391 | 34,111 | 15.1 | 71% | 33% | 91% | 235 KB | 2 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 18,249 | 26,098 | 27.5 | 76% | 27% | 96% | 170 KB | 4 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 17,742 | 34,744 | 32.9 | 26% | 35% | 99% | 876 KB | 4 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | C E C | 17,625 | 25,586 | 0.0 | 71% | 23% | 100% | 472 KB | 0 |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C D C | 17,030 | 23,352 | 23.5 | 68% | 8% | 99% | 137 KB | 33 (+1) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | C F D | 16,841 | 55,502 | 18.5 | 18% | 2% | 41% | 140 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 16,690 | 19,029 | 0.0 | 56% | 3% | 96% | 589 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C E C | 16,438 | 60,124 | 39.0 | 42% | 5% | 99% | 78 KB | 2 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C B A | 16,284 | 23,709 | 22.8 | 84% | 37% | 100% | 200 KB | 6 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C C C | 16,213 | 33,061 | 7.5 | 72% | 37% | 100% | 100 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,067 | 33,151 | 30.3 | 2% | 27% | 100% | 225 KB | 7 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C E B | 16,059 | 18,705 | 7.8 | 69% | 0% | 77% | 602 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C D D | 15,979 | 14,523 | 0.7 | 68% | 24% | 0% | 164 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 15,789 | 20,886 | 21.0 | 78% | 57% | 96% | 668 KB | 9 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C C D | 15,705 | 21,295 | 34.5 | 71% | 4% | 100% | 599 KB | 22 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C E A | 15,308 | 27,190 | 2.7 | 55% | 0% | 100% | 258 KB | 0 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 15,289 | 439,419 | 0.0 | 74% | 39% | 0% | 3,283 KB | 1 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 15,111 | 25,669 | 0.0 | 70% | 49% | – | 1,206 KB | 3 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C C B | 14,801 | 16,204 | 13.8 | 74% | 0% | 82% | 1,188 KB | 13 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,604 | 18,363 | 5.0 | 19% | 16% | 99% | 418 KB | 133 (+1) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | C E A | 14,568 | 32,422 | 17.6 | 60% | 0% | 97% | 90 KB | 1 |
| [joemooney/aida](https://github.com/joemooney/aida) | C E C | 14,354 | 28,411 | 22.9 | 58% | 4% | 89% | 755 KB | 5 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C C D | 14,289 | 20,386 | 0.0 | 79% | 59% | 41% | 1,000 KB | 32 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C F B | 13,808 | 25,004 | 12.4 | 82% | 0% | 98% | 86 KB | 6 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | C F B | 13,590 | 25,300 | 33.8 | 32% | 0% | 91% | 2,600 KB | 35 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 13,335 | 20,947 | 99.9 | 12% | 45% | 76% | 356 KB | 51 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 13,211 | 14,621 | 0.0 | 77% | 12% | 4% | 274 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 13,188 | 22,579 | 34.6 | 35% | 38% | 83% | 330 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C E D | 12,966 | 40,439 | 13.1 | 72% | 9% | 44% | 431 KB | 0 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | C E B | 12,906 | 21,761 | 13.4 | 55% | 40% | 90% | 537 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 12,764 | 35,906 | 71.5 | 59% | 41% | 25% | 837 KB | 16 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 12,115 | 16,495 | 34.5 | 40% | 20% | 100% | 119 KB | 1 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 12,084 | 16,215 | 12.8 | 71% | 0% | 97% | 718 KB | 9 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 11,889 | 48,531 | 0.0 | 69% | 12% | 50% | 479 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C F B | 11,726 | 35,650 | 37.4 | 28% | 13% | 99% | 570 KB | 37 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C D D | 11,386 | 14,379 | 8.7 | 65% | 16% | 25% | 194 KB | 2 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | C E C | 11,323 | 19,728 | 17.7 | 67% | 0% | 96% | 41 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 11,119 | 17,673 | 39.6 | 43% | 16% | 100% | 251 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C D A | 11,114 | 21,385 | 15.5 | 69% | 0% | 96% | 128 KB | 5 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C E B | 10,925 | 413,153 | 30.3 | 48% | 9% | 97% | 1,414 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C C B | 10,917 | 14,686 | 29.6 | 73% | 26% | 78% | 1,371 KB | 70,250 (+21) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 10,783 | 47,575 | 25.9 | 83% | 0% | 100% | 1,983 KB | 5 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | C D C | 10,729 | 37,215 | 0.0 | 62% | 10% | 100% | 487 KB | 1 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | C E C | 10,706 | 20,331 | 40.4 | 52% | 14% | 52% | 3,052 KB | 2 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 10,639 | 12,168 | 20.8 | 69% | 63% | 100% | 557 KB | 1 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 10,633 | 29,024 | 27.0 | 35% | 0% | 88% | 458 KB | 19 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | C F B | 10,582 | 13,923 | 14.1 | 21% | 37% | 97% | 326 KB | 161 (+3) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | D F D | 9,873 | 16,658 | 0.0 | 12% | 23% | 42% | 221 KB | 0 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 9,664 | 17,324 | 20.1 | 30% | 0% | 88% | 700 KB | 4 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D E B | 9,605 | 22,382 | 21.0 | 54% | 20% | 87% | 982 KB | 4 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D F B | 9,578 | 19,879 | 31.7 | 29% | 50% | 100% | 1,224 KB | 8 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 9,350 | 12,803 | 0.0 | 48% | 22% | 98% | 415 KB | 0 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D F D | 9,278 | 25,291 | 0.0 | 39% | 0% | 0% | 601 KB | 1 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | D E D | 9,267 | 12,254 | 0.0 | 51% | 30% | 37% | 308 KB | 246 (+2) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | D E B | 9,101 | 25,359 | 31.2 | 55% | 25% | 100% | 629 KB | 2 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [integry/propr](https://github.com/integry/propr) | D E B | 9,030 | 14,494 | 14.9 | 48% | 24% | 100% | 4,314 KB | 20 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | D E A | 8,971 | 35,401 | 24.8 | 60% | 18% | 99% | 393 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | D E B | 8,925 | 8,401 | 11.2 | 73% | 0% | 97% | 56 KB | 1 (+1) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | D F B | 8,911 | 16,956 | 12.6 | 44% | 22% | 97% | 589 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | D D A | 8,843 | 13,436 | 13.8 | 62% | 45% | 93% | 137 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 8,712 | 16,499 | 0.0 | 14% | 68% | 96% | 405 KB | 1 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | D D C | 8,573 | 23,632 | 15.3 | 66% | 21% | 98% | 330 KB | 2 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,546 | 12,359 | 0.2 | 53% | 20% | 100% | 352 KB | 2 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | D E D | 8,492 | 22,215 | 0.0 | 48% | 6% | 43% | 152 KB | 110 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | D F D | 8,455 | 16,012 | 10.8 | 46% | 6% | 0% | 285 KB | 24 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | D D B | 8,232 | 10,829 | 9.5 | 65% | 7% | 94% | 79 KB | 1 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | D F C | 8,169 | 15,273 | 11.8 | 58% | 0% | 100% | 18 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D E D | 7,890 | 13,786 | 37.0 | 60% | 57% | – | 421 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D E A | 7,823 | 18,962 | 13.0 | 44% | 24% | 90% | 236 KB | 5 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 7,710 | 14,069 | 28.6 | 6% | 11% | 100% | 134 KB | 7 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D F B | 7,656 | 25,055 | 33.8 | 79% | 7% | 100% | 1,430 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 7,551 | 15,987 | 31.1 | 48% | 29% | 100% | 560 KB | 5 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D E D | 7,512 | 25,850 | 0.0 | 47% | 0% | – | 824 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | D D D | 7,452 | 6,627 | 0.0 | 60% | 15% | – | 3,234 KB | 0 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,340 | 15,554 | 4.6 | 38% | 46% | 81% | 3,497 KB | 543 (-2) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 7,002 | 12,434 | 48.6 | 0% | 46% | 89% | 67 KB | 61 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D F C | 6,775 | 46,862 | 1.2 | 24% | 28% | 97% | 3,340 KB | 7 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | D F B | 6,752 | 11,041 | 0.1 | 30% | 3% | 73% | 152 KB | 29 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 6,698 | 8,339 | 76.9 | 74% | 12% | 100% | 762 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | D B C | 6,434 | 29,749 | 11.2 | 85% | 42% | 98% | 143 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D C A | 6,361 | 11,015 | 29.7 | 74% | 35% | 86% | 102 KB | 231 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D E D | 6,309 | 10,532 | 13.9 | 59% | 14% | 29% | 130 KB | 0 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D C D | 6,119 | 9,615 | 34.3 | 76% | 6% | – | 198 KB | 2 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | D E C | 5,851 | 9,448 | 36.9 | 72% | 7% | 99% | 221 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,808 | 6,831 | 23.7 | 34% | 0% | 90% | 950 KB | 1 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 5,739 | 7,196 | 1.6 | 3% | 0% | 77% | 42 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F A | 5,701 | 10,067 | 29.4 | 19% | 13% | 100% | 316 KB | 159 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | D D C | 5,648 | 16,933 | 38.1 | 63% | 8% | 73% | 319 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D F B | 5,635 | 7,208 | 24.1 | 27% | 13% | 90% | 805 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 5,606 | 7,540 | 21.0 | 35% | 23% | 99% | 388 KB | 20 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | D F B | 5,540 | 7,338 | 19.9 | 15% | 26% | 90% | 436 KB | 0 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | D F C | 5,537 | 79,939 | 11.1 | 72% | 0% | 80% | 417 KB | 0 |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,527 | 9,126 | 3.6 | 1% | 12% | 90% | 319 KB | 1 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 5,394 | 11,629 | 21.3 | 9% | 16% | 94% | 270 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | D F D | 5,336 | 7,318 | 0.0 | 50% | 0% | 42% | 266 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | D E E | 5,315 | 11,520 | 14.9 | 40% | 68% | 76% | 1,538 KB | 5 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D F C | 5,146 | 11,943 | 10.4 | 46% | 0% | 100% | 49 KB | 3 |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,059 | 14,397 | 21.6 | 12% | 0% | 98% | 489 KB | 28 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E D B | 4,989 | 10,042 | 19.4 | 69% | 3% | 96% | 499 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E E B | 4,935 | 5,930 | 21.9 | 73% | 13% | 100% | 103 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E B | 4,827 | 11,411 | 6.3 | 47% | 41% | 99% | 70 KB | 15 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E F D | 4,786 | 6,394 | 39.4 | 47% | 6% | – | 373 KB | 3 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 4,518 | 7,030 | 10.4 | 48% | 0% | – | 83 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | E E C | 4,374 | 5,897 | 0.0 | 52% | 12% | 86% | 871 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 4,290 | 5,323 | 24.2 | 44% | 0% | 99% | 127 KB | 23 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 4,288 | 12,439 | 29.2 | 28% | 21% | 100% | 468 KB | 17 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E F C | 4,136 | 13,185 | 25.5 | 39% | 41% | 99% | 169 KB | 0 |
| [ztrange/veri](https://github.com/ztrange/veri) | E D B | 4,102 | 9,580 | 23.1 | 70% | 0% | 100% | 1,172 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E E B | 4,047 | 7,934 | 1.6 | 69% | 20% | 100% | 182 KB | 7 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | E F C | 4,042 | 5,610 | 10.0 | 28% | 0% | 99% | 99 KB | 4 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | E F D | 4,027 | 7,456 | 8.5 | 58% | 17% | – | 137 KB | 14 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 4,014 | 6,083 | 28.1 | 34% | 0% | 83% | 203 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E F D | 3,888 | 12,780 | 17.1 | 40% | 0% | 100% | 317 KB | 0 |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 3,865 | 8,353 | 0.0 | 16% | 9% | 0% | 436 KB | 4 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 3,829 | 6,557 | 14.2 | 8% | 15% | 71% | 240 KB | 1 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | E E B | 3,758 | 6,727 | 5.6 | 53% | 13% | 77% | 78 KB | 0 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 3,726 | 12,785 | 36.2 | 62% | 0% | 96% | 106 KB | 5 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E E D | 3,638 | 6,849 | 0.3 | 59% | 10% | 0% | 453 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,628 | 11,370 | 10.2 | 53% | 43% | 97% | 111 KB | 0 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F B | 3,564 | 4,501 | 13.1 | 13% | 29% | 98% | 518 KB | 1 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 3,520 | 7,272 | 26.3 | 0% | 16% | 100% | 526 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 3,383 | 34,080 | 0.3 | 78% | 0% | 90% | 1,468 KB | 1,100 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E C E | 3,380 | 22,696 | 22.3 | 74% | 11% | 99% | 625 KB | 11 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 3,347 | 5,815 | 44.9 | 53% | 24% | 100% | 304 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | E F A | 3,347 | 7,667 | 1.6 | 48% | 0% | 100% | 163 KB | 11 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 3,341 | 85,695 | 16.0 | 59% | 0% | 99% | 245 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E D C | 3,330 | 4,744 | 13.4 | 67% | 10% | 95% | 123 KB | 1 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E E E | 3,321 | 9,532 | 22.0 | 43% | 36% | 98% | 1,109 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E E C | 3,273 | 7,391 | 32.6 | 57% | 0% | 90% | 403 KB | 2 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 3,203 | 3,761 | 14.0 | 48% | 0% | 100% | 161 KB | 0 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | E F A | 3,156 | 13,330 | 17.9 | 11% | 10% | 97% | 367 KB | 7 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | E C C | 3,086 | 4,971 | 0.0 | 72% | 45% | 96% | 266 KB | 0 |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 3,080 | 12,483 | 35.1 | 35% | 0% | 93% | 240 KB | 9 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F B | 3,021 | 8,562 | 24.4 | 36% | 22% | 96% | 69 KB | 10 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 3,003 | 10,421 | 14.2 | 47% | 0% | 100% | 696 KB | 11 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 2,910 | 11,669 | 6.6 | 31% | 16% | 93% | 267 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E E B | 2,890 | 4,381 | 40.8 | 66% | 24% | 92% | 142 KB | 8 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,781 | 13,568 | 8.0 | 6% | 49% | 100% | 530 KB | 11 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E E A | 2,739 | 5,677 | 9.8 | 58% | 0% | 93% | 247 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 2,656 | 7,597 | 18.9 | 30% | 20% | 100% | 386 KB | 1 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,626 | 3,869 | 0.1 | 45% | 0% | 84% | 363 KB | 3 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 2,598 | 12,994 | 24.4 | 34% | 0% | 89% | 118 KB | 3 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | E F B | 2,541 | 34,056 | 32.9 | 53% | 0% | 99% | 404 KB | 9 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | E F B | 2,528 | 3,346 | 8.9 | 51% | 9% | 80% | 524 KB | 2 |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E E E | 2,523 | 12,288 | 14.5 | 61% | 0% | 100% | 1,007 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 2,500 | 5,657 | 29.5 | 47% | 0% | 93% | 980 KB | 101 (+2) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | E F C | 2,447 | 2,826 | 23.2 | 77% | 0% | 98% | 363 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 2,395 | 6,894 | 7.4 | 67% | 0% | 100% | 175 KB | 224 (-1) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E E C | 2,371 | 4,196 | 9.8 | 43% | 0% | 100% | 66 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E D A | 2,282 | 3,643 | 16.1 | 67% | 42% | 100% | 418 KB | 12 (+1) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E F C | 2,258 | 6,299 | 11.3 | 36% | 0% | 86% | 8,119 KB | 1 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 2,241 | 7,975 | 20.9 | 25% | 0% | 81% | 278 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 2,216 | 10,050 | 11.4 | 17% | 10% | 83% | 535 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 2,179 | 3,275 | 15.8 | 36% | 0% | – | 49 KB | 3 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 2,128 | 2,737 | 23.3 | 21% | 22% | 97% | 544 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,078 | 5,906 | 29.8 | 17% | 0% | 100% | 617 KB | 1 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 2,002 | 4,560 | 0.0 | 43% | 0% | 33% | 397 KB | 460 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 1,994 | 4,992 | 15.9 | 39% | 17% | 100% | 194 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,947 | 3,031 | 20.4 | 11% | 28% | 97% | 652 KB | 1 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E C | 1,914 | 27,212 | 0.8 | 61% | 6% | 55% | 5,521 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 1,749 | 43,119 | 0.0 | 32% | 0% | – | 8,190 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,735 | 24,771 | 0.0 | 46% | 0% | – | 200 KB | 28 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,601 | 5,045 | 9.5 | 38% | 14% | 98% | 787 KB | 2 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | E F A | 1,596 | 5,082 | 13.4 | 82% | 0% | 99% | 298 KB | 5 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,456 | 3,117 | 14.9 | 0% | 0% | 100% | 134 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | E F D | 1,451 | 6,819 | 0.0 | 43% | 0% | 0% | 315 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 1,425 | 9,084 | 17.4 | 59% | 6% | 98% | 417 KB | 1 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,406 | 48,991 | 0.0 | 19% | 0% | 96% | 211 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F C | 1,251 | 4,433 | 0.0 | 30% | 0% | 63% | 554 KB | 28 (+1) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E D D | 1,229 | 1,322 | 0.1 | 61% | 25% | 0% | 635 KB | 3 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 1,220 | 5,024 | 28.0 | 42% | 0% | 47% | 100 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,195 | 2,658 | 4.9 | 42% | 37% | 94% | 7,014 KB | 18 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 1,149 | 4,669 | 25.5 | 61% | 0% | 100% | 148 KB | 1 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | E F C | 1,134 | 5,656 | 22.8 | 16% | 0% | 97% | 311 KB | 4 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,109 | 10,170 | 26.4 | 8% | 0% | 100% | 122 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F C | 1,084 | 5,796 | 11.5 | 51% | 0% | 89% | 6,579 KB | 8 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F D C | 954 | 2,665 | 6.3 | 63% | 30% | 100% | 150 KB | 2 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 935 | 6,740 | 0.0 | 30% | 0% | – | 646 KB | 2 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 796 | 17,961 | 14.5 | 13% | 0% | – | 411 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 788 | 13,649 | 2.9 | 68% | 8% | 80% | 149 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | F F B | 785 | 1,313 | 8.8 | 38% | 0% | 93% | 342 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 780 | 6,986 | 20.1 | 36% | 42% | 98% | 215 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 760 | 1,757 | 23.1 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 748 | 11,256 | 2.8 | 56% | 0% | – | 295 KB | 1 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | F F D | 723 | 3,372 | 0.0 | 29% | 0% | 0% | 1,121 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 675 | 7,709 | 9.9 | 17% | 0% | 90% | 38 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 555 | 9,152 | 0.0 | 52% | 0% | – | 111 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 528 | 1,796 | 13.1 | 24% | 0% | 98% | 49 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 301 | 9,782 | 0.0 | 32% | 0% | 100% | 478 KB | 6 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 283 | 1,480 | 0.0 | 0% | 0% | 98% | 384 KB | 0 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 264 | 18,437 | 26.1 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F D E | 225 | 1,736 | 20.1 | 65% | 5% | 94% | 555 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 200 | 27,254 | 6.0 | 6% | 0% | 96% | 24 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 171 | 582 | 4.9 | 0% | 0% | 97% | 72 KB | 4 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 164 | 3,482 | 18.7 | 47% | 0% | 88% | 303 KB | 23 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 134 | 858 | 0.0 | 0% | 0% | – | 202 KB | 4 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 102 | 4,922 | 0.0 | 34% | 0% | – | 112 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 82 | 4,527 | 0.0 | 40% | 0% | 0% | 473 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 74 | 9,984 | 3.5 | 29% | 0% | 100% | 1,116 KB | 5 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 54 | 505 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 36 | 3,690 | 16.0 | 16% | 0% | 96% | 66 KB | 3 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 28 | 190,054 | 10.4 | 13% | 0% | 100% | 378 KB | 1 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 7 | 6,352 | 12.8 | 24% | 0% | 98% | 43 KB | 1 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 2,255,134 | 49.6 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F B B | – | – | 38.9 | 81% | 34% | 88% | 2,197 KB | 1,424 (+8) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | – | – | 30.9 | – | – | 52% | 92 KB | 1 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 282 | 25.5 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F D B | – | – | 22.2 | 67% | 45% | 100% | 975 KB | 4 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 18.7 | – | – | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 15.6 | 35% | 14% | 100% | 342 KB | 4 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 14.8 | 3% | 0% | 98% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 3 | 14.3 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | 0 | 15,444 | 14.1 | 0% | 0% | – | 131 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 508 | 14.0 | 0% | 0% | – | 55 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | 0 | 443 | 13.6 | 53% | 0% | 90% | 195 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 0 | 12.2 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 0 | 1 | 10.4 | 0% | 0% | – | 115 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 5,837 | 7.8 | 40% | 0% | 97% | 122 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F B | – | – | 6.3 | 53% | 0% | 72% | 206 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 241 | 5.8 | 0% | 0% | 70% | 466 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 5.4 | 46% | 56% | 0% | 1,788 KB | 457 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 1,692 | 4.8 | 0% | 0% | 80% | 154 KB | 2 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,279 | 3.6 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 1,360 | 1.9 | 0% | 0% | 33% | 61 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 0 | 837 | 1.9 | 32% | 0% | 100% | 59 KB | 1 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 804 | 1.3 | 0% | 0% | 69% | 290 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 1.0 | 0% | 0% | – | 92 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 76% | 4% | 78% | 816 KB | 5 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F D E | – | – | 0.2 | 66% | 67% | 96% | 26,059 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 770 | 0.1 | 14% | 0% | 9% | 904 KB | 1,282 (+1) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 1,737 | 0.0 | 0% | 0% | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | 17% | 0% | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 40% | 20% | 55% | 84 KB | 5 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 6 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
