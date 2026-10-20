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
_268 repos, last measured 2026-10-20. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (268)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 86,381 | 101,170 | 68.2 | 33% | 0% | 85% | 3,040 KB | 1,980 (+17) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 77,143 | 408,384 | 63.1 | 18% | 4% | 98% | 3,975 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A B B | 63,155 | 75,689 | 32.0 | 81% | 20% | 97% | 498 KB | 11 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A D C | 58,364 | 89,491 | 53.0 | 68% | 7% | 96% | 119 KB | 116 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | A D B | 54,265 | 190,362 | 10.1 | 66% | 26% | 77% | 727 KB | 4 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 43,508 | 44,613 | 35.8 | 77% | 30% | 85% | 776 KB | 1 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A B B | 42,152 | 55,098 | 30.3 | 86% | 39% | 98% | 231 KB | 1 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A E B | 40,027 | 41,426 | 0.2 | 52% | 10% | 95% | 132 KB | 67 (+11) |
| [tale-project/tale](https://github.com/tale-project/tale) | B F B | 39,085 | 39,072 | 34.5 | 31% | 4% | 91% | 2,600 KB | 35 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | B B C | 37,507 | 42,904 | 66.4 | 81% | 32% | 99% | 691 KB | 14 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B F B | 37,183 | 45,534 | 37.4 | 11% | 6% | 99% | 534 KB | 37 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 37,114 | 42,286 | 29.5 | 87% | 80% | 88% | 364 KB | 9 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B F A | 36,869 | 54,043 | 6.9 | 50% | 7% | 85% | 262 KB | 325 (+4) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B B B | 34,906 | 67,500 | 18.5 | 86% | 25% | 86% | 579 KB | 0 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | B C C | 33,632 | 50,394 | 56.4 | 79% | 23% | 100% | 606 KB | 2 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B E B | 31,883 | 43,269 | 176 | 51% | 62% | 100% | 3,000 KB | 1 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 30,886 | 105,060 | 98.7 | 10% | 0% | 44% | 310 KB | 3 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B D B | 30,710 | 40,291 | 26.8 | 64% | 53% | 100% | 1,060 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 30,668 | 147,757 | 27.0 | 54% | 40% | 100% | 846 KB | 33 (+2) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 30,397 | 72,282 | 22.9 | 38% | 34% | 34% | 3,082 KB | 96 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 30,221 | 120,172 | 61.2 | 70% | 42% | 61% | 1,736 KB | 4 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B D A | 29,822 | 74,083 | 62.5 | 62% | 32% | 99% | 166 KB | 2 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B E D | 29,715 | 32,588 | 0.0 | 51% | 24% | – | 280 KB | 0 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B B D | 28,306 | 29,449 | 34.0 | 84% | 3% | 98% | 599 KB | 22 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | B E B | 27,379 | 29,133 | 20.0 | 44% | 39% | 85% | 816 KB | 4 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 27,309 | 38,988 | 32.2 | 64% | 37% | 100% | 1,338 KB | 92 (+1) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B D B | 27,272 | 48,756 | 92.9 | 63% | 13% | 79% | 202 KB | 14 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B E B | 26,972 | 670,016 | 85.2 | 54% | 41% | 99% | 581 KB | 2 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | B C A | 25,851 | 35,084 | 20.9 | 80% | 57% | 98% | 200 KB | 6 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 25,838 | 89,350 | 38.8 | 38% | 13% | 99% | 55 KB | 0 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 25,628 | 37,511 | 162 | 34% | 4% | 89% | 2,294 KB | 3 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B B A | 25,628 | 65,582 | 59.8 | 87% | 50% | 100% | 60 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 25,200 | 36,097 | 45.2 | 72% | 54% | 100% | 354 KB | 2 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | B C C | 25,057 | 29,052 | 16.0 | 72% | 24% | 96% | 40 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | B E A | 22,840 | 109,544 | 22.4 | 72% | 0% | 99% | 377 KB | 48 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 20,938 | 36,700 | 0.0 | 46% | 28% | – | 296 KB | 2 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B D A | 20,794 | 45,839 | 17.2 | 63% | 12% | 87% | 146 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | B E C | 20,714 | 51,146 | 38.8 | 47% | 35% | 57% | 3,052 KB | 2 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B E C | 20,492 | 33,873 | 24.8 | 55% | 8% | 95% | 750 KB | 5 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E B | 19,948 | 23,985 | 32.3 | 42% | 37% | 78% | 330 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 19,877 | 30,933 | 61.1 | 50% | 54% | 94% | 768 KB | 6,368 (+13) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C E B | 19,706 | 34,230 | 29.1 | 52% | 25% | 100% | 571 KB | 2 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 19,698 | 30,009 | 34.5 | 30% | 24% | 100% | 435 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | C F C | 18,874 | 22,155 | 11.6 | 69% | 0% | 100% | 17 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 18,501 | 21,650 | 16.4 | 36% | 4% | 94% | 3,021 KB | 120 (+1) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C C D | 18,494 | 19,188 | 0.0 | 74% | 24% | – | 226 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 18,249 | 25,377 | 26.9 | 76% | 49% | 99% | 153 KB | 4 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | C C C | 18,037 | 15,901 | 35.6 | 74% | 9% | 100% | 217 KB | 0 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 17,992 | 33,330 | 26.7 | 41% | 0% | 100% | 457 KB | 19 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | C F B | 17,480 | 33,066 | 33.8 | 33% | 25% | 99% | 867 KB | 4 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | C F B | 17,287 | 26,296 | 13.8 | 51% | 0% | 99% | 706 KB | 9 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 16,889 | 21,518 | 32.9 | 62% | 42% | 91% | 1,494 KB | 3 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C F B | 16,690 | 20,521 | 0.0 | 40% | 0% | 96% | 589 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 16,438 | 57,003 | 28.2 | 44% | 1% | 100% | 75 KB | 2 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 16,375 | 97,867 | 22.3 | 89% | 21% | 100% | 158 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C E D | 16,350 | 21,870 | 0.6 | 50% | 17% | 0% | 164 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,067 | 34,162 | 28.2 | 18% | 31% | 100% | 225 KB | 7 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C C B | 16,060 | 21,025 | 7.6 | 70% | 20% | 78% | 586 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 15,775 | 22,541 | 32.4 | 52% | 0% | 97% | 392 KB | 9 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C E A | 15,063 | 23,636 | 2.5 | 63% | 0% | 100% | 258 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,604 | 23,366 | 4.8 | 16% | 23% | 96% | 405 KB | 131 (+2) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 14,189 | 29,169 | 0.0 | 79% | 41% | – | 1,189 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C B C | 13,757 | 17,589 | 22.5 | 85% | 33% | 100% | 137 KB | 32 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C C D | 12,935 | 398,538 | 0.0 | 88% | 18% | 0% | 3,283 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C E C | 12,852 | 45,466 | 0.2 | 67% | 0% | 67% | 1,271 KB | 439 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F D | 12,722 | 24,888 | 0.0 | 9% | 21% | 25% | 220 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 12,586 | 17,271 | 0.0 | 88% | 54% | 41% | 947 KB | 32 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C F A | 12,115 | 16,429 | 31.4 | 34% | 0% | 100% | 118 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | C E B | 12,104 | 17,862 | 14.2 | 59% | 44% | 100% | 4,314 KB | 20 (+1) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 12,102 | 17,811 | 97.9 | 25% | 56% | 76% | 353 KB | 49 (+1) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | C C C | 11,992 | 33,248 | 8.9 | 73% | 40% | 98% | 262 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C D C | 11,889 | 51,933 | 0.0 | 70% | 21% | 50% | 471 KB | 1 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C E D | 11,689 | 17,608 | 66.8 | 41% | 44% | 25% | 837 KB | 16 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | C F B | 11,603 | 23,141 | 14.9 | 77% | 2% | 97% | 140 KB | 2 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 11,505 | 19,895 | 38.2 | 49% | 10% | 100% | 251 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | C E B | 11,496 | 12,254 | 10.9 | 68% | 0% | 97% | 56 KB | 0 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C B B | 11,481 | 15,394 | 29.2 | 84% | 27% | 82% | 1,517 KB | 70,203 (+41) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | C C D | 11,386 | 11,348 | 8.5 | 77% | 13% | 28% | 192 KB | 2 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C F B | 11,345 | 25,712 | 10.5 | 68% | 0% | 98% | 86 KB | 6 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 11,202 | 38,410 | 24.5 | 80% | 3% | 100% | 1,889 KB | 5 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C D B | 10,925 | 478,224 | 27.4 | 67% | 9% | 100% | 1,414 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C F D | 10,792 | 18,263 | 0.0 | 59% | 13% | 18% | 268 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | C E D | 10,676 | 16,364 | 0.0 | 45% | 0% | – | 813 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | C E A | 10,564 | 20,132 | 0.8 | 57% | 42% | 100% | 163 KB | 11 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | C F B | 10,503 | 12,560 | 8.8 | 78% | 34% | 93% | 95 KB | 0 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C C D | 10,292 | 13,241 | 0.0 | 73% | 35% | 40% | 304 KB | 243 (+33) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C D B | 10,161 | 19,557 | 11.5 | 67% | 12% | 96% | 559 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C F A | 10,116 | 14,744 | 13.9 | 53% | 0% | 95% | 128 KB | 5 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D F C | 9,961 | 10,917 | 11.3 | 50% | 0% | 89% | 6,579 KB | 8 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | D D A | 9,896 | 39,560 | 25.1 | 68% | 15% | 99% | 393 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | D E C | 9,800 | 13,499 | 9.5 | 44% | 38% | 97% | 109 KB | 0 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D D C | 9,786 | 29,876 | 0.0 | 69% | 15% | 100% | 485 KB | 1 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D F B | 9,597 | 19,002 | 29.5 | 27% | 50% | 100% | 1,188 KB | 8 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 9,519 | 7,985 | 11.0 | 19% | 25% | 99% | 99 KB | 4 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 9,464 | 16,142 | 29.2 | 12% | 10% | 99% | 134 KB | 1 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D D B | 9,429 | 10,798 | 21.7 | 63% | 29% | 99% | 553 KB | 1 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | D F D | 9,375 | 22,259 | 10.4 | 40% | 28% | 0% | 285 KB | 24 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D E B | 9,329 | 16,479 | 20.5 | 42% | 0% | 88% | 700 KB | 4 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D E D | 9,278 | 13,533 | 0.0 | 51% | 0% | 0% | 601 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 9,198 | 10,910 | 45.5 | 0% | 44% | 93% | 67 KB | 61 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | D F A | 9,011 | 18,757 | 23.8 | 28% | 0% | 87% | 118 KB | 3 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | D E C | 8,801 | 15,322 | 37.2 | 51% | 9% | 73% | 318 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,731 | 15,110 | 0.2 | 44% | 15% | 100% | 343 KB | 2 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D E A | 8,642 | 17,342 | 29.1 | 63% | 32% | 100% | 316 KB | 159 (-1) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D D | 8,486 | 11,941 | 13.1 | 65% | 48% | 35% | 128 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D E C | 8,470 | 11,904 | 18.4 | 59% | 38% | 100% | 657 KB | 9 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | D F B | 8,406 | 14,916 | 19.1 | 50% | 19% | 88% | 436 KB | 0 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 8,218 | 17,898 | 8.5 | 37% | 24% | 100% | 530 KB | 11 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 7,943 | 9,203 | 76.6 | 78% | 51% | 100% | 741 KB | 0 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 7,561 | 12,181 | 14.5 | 67% | 0% | 100% | 696 KB | 11 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | D E E | 7,389 | 17,377 | 12.9 | 55% | 49% | 76% | 1,531 KB | 5 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,340 | 16,703 | 3.7 | 20% | 44% | 85% | 3,390 KB | 544 (+4) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D F A | 7,169 | 13,175 | 12.7 | 34% | 0% | 100% | 236 KB | 5 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 7,102 | 10,476 | 26.5 | 31% | 35% | 100% | 557 KB | 5 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D C C | 6,813 | 16,830 | 16.0 | 72% | 26% | 100% | 43 KB | 15 (+1) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D F B | 6,811 | 24,454 | 31.8 | 51% | 10% | 90% | 1,429 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D E D | 6,721 | 33,159 | 0.0 | 49% | 16% | – | 192 KB | 28 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D E C | 6,669 | 9,702 | 0.0 | 51% | 13% | 86% | 869 KB | 1 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | D C D | 6,540 | 10,841 | 0.0 | 71% | 18% | 42% | 266 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 6,492 | 13,622 | 0.0 | 48% | 9% | 100% | 404 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D E C | 6,466 | 8,920 | 32.2 | 42% | 0% | 98% | 403 KB | 2 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D D B | 6,361 | 10,494 | 28.5 | 70% | 36% | 85% | 102 KB | 231 (+1) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D E D | 6,342 | 13,856 | 33.1 | 61% | 57% | – | 421 KB | 0 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 6,153 | 8,440 | 0.0 | 19% | 39% | 96% | 402 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D D D | 6,119 | 10,069 | 35.1 | 65% | 1% | – | 188 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D F B | 6,096 | 9,305 | 14.4 | 28% | 0% | 86% | 1,186 KB | 13 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | D D D | 6,083 | 13,314 | 0.0 | 63% | 9% | 0% | 310 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 6,026 | 15,186 | 1.4 | 38% | 12% | 76% | 42 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D F A | 5,882 | 10,078 | 28.5 | 54% | 16% | 86% | 203 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 5,812 | 10,595 | 14.1 | 31% | 41% | 94% | 318 KB | 158 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,808 | 7,138 | 22.8 | 45% | 0% | 96% | 941 KB | 1 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | D F B | 5,699 | 13,580 | 24.0 | 43% | 9% | 92% | 802 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D E C | 5,683 | 47,364 | 1.2 | 44% | 34% | 91% | 3,340 KB | 7 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | D E C | 5,630 | 16,257 | 17.0 | 48% | 14% | 100% | 179 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 5,527 | 11,149 | 3.5 | 34% | 24% | 90% | 319 KB | 1 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D F B | 5,369 | 25,167 | 102 | 21% | 2% | 90% | 3,502 KB | 70 (+2) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 5,310 | 14,347 | 17.4 | 22% | 10% | 94% | 361 KB | 7 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 5,140 | 13,826 | 28.3 | 34% | 19% | 99% | 467 KB | 17 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 5,112 | 10,884 | 19.7 | 42% | 44% | 99% | 387 KB | 19 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | D E B | 5,060 | 6,779 | 47.3 | 52% | 29% | 99% | 303 KB | 2 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | D F B | 5,059 | 17,289 | 24.4 | 9% | 15% | 95% | 489 KB | 28 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E D B | 4,989 | 12,388 | 19.0 | 69% | 31% | 99% | 499 KB | 0 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E B B | 4,935 | 6,757 | 20.6 | 89% | 54% | 100% | 102 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 4,918 | 6,002 | 34.2 | 54% | 10% | – | 358 KB | 2 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | E D D | 4,860 | 4,878 | 0.0 | 61% | 19% | – | 3,234 KB | 0 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E E A | 4,826 | 9,650 | 4.5 | 60% | 25% | 94% | 140 KB | 15 (+13) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E E D | 4,783 | 5,126 | 0.0 | 48% | 25% | 33% | 397 KB | 460 (+1) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E E C | 4,655 | 17,456 | 6.6 | 52% | 26% | 93% | 257 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 4,562 | 33,136 | 0.8 | 53% | 3% | 46% | 5,519 KB | 1 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E C A | 4,559 | 4,562 | 17.0 | 77% | 48% | 100% | 396 KB | 11 (+1) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | E F D | 4,518 | 6,840 | 11.0 | 30% | 0% | – | 82 KB | 2 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 4,159 | 12,367 | 20.6 | 24% | 19% | 96% | 268 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 3,726 | 9,171 | 34.1 | 46% | 0% | 98% | 106 KB | 5 (+1) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 3,570 | 4,939 | 9.4 | 35% | 16% | 100% | 66 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E E B | 3,566 | 6,455 | 0.6 | 61% | 0% | 100% | 182 KB | 7 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E F A | 3,564 | 4,773 | 13.4 | 35% | 37% | 98% | 467 KB | 1 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E C E | 3,372 | 24,002 | 21.8 | 79% | 15% | 99% | 625 KB | 11 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E C B | 3,351 | 4,854 | 9.0 | 85% | 54% | 100% | 708 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 3,329 | 4,728 | 15.9 | 64% | 0% | – | 48 KB | 3 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E E B | 3,323 | 10,680 | 21.9 | 74% | 24% | 93% | 70 KB | 10 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 3,266 | 6,155 | 0.1 | 55% | 29% | 86% | 309 KB | 3 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 3,213 | 15,443 | 0.0 | 6% | 7% | 47% | 149 KB | 108 (-1) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 3,168 | 8,508 | 28.5 | 48% | 0% | 93% | 980 KB | 98 (+1) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,144 | 7,871 | 19.8 | 26% | 13% | 100% | 386 KB | 1 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 3,108 | 4,051 | 23.9 | 20% | 10% | 96% | 544 KB | 0 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 3,086 | 78,032 | 14.0 | 38% | 0% | 100% | 244 KB | 2 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E D C | 3,080 | 12,327 | 36.0 | 68% | 0% | 59% | 240 KB | 9 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E E C | 2,961 | 21,720 | 14.0 | 59% | 12% | 93% | 330 KB | 2 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E F C | 2,861 | 3,654 | 11.8 | 29% | 0% | 96% | 117 KB | 1 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E C D | 2,855 | 8,902 | 0.0 | 71% | 14% | 0% | 407 KB | 4 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | E C A | 2,739 | 5,992 | 9.5 | 75% | 24% | 91% | 241 KB | 0 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | E E C | 2,641 | 3,550 | 22.9 | 73% | 0% | 98% | 363 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E E A | 2,599 | 5,168 | 23.3 | 59% | 0% | 100% | 127 KB | 23 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,590 | 8,264 | 0.1 | 45% | 5% | 73% | 152 KB | 29 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | E E E | 2,461 | 3,494 | 21.4 | 47% | 0% | 94% | 1,109 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E F F | 2,374 | 105,112 | 0.0 | 49% | 0% | – | 8,190 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,355 | 8,179 | 29.5 | 53% | 0% | 100% | 617 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E E D | 2,318 | 6,263 | 27.4 | 57% | 0% | 47% | 97 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 2,242 | 6,086 | 13.4 | 26% | 15% | 73% | 229 KB | 1 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 2,216 | 15,185 | 11.1 | 12% | 10% | 67% | 520 KB | 1 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E D C | 2,112 | 9,946 | 17.6 | 62% | 44% | 98% | 404 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,018 | 9,031 | 13.8 | 60% | 0% | 100% | 996 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | E F D | 1,971 | 2,481 | 8.5 | 30% | 0% | 98% | 8,119 KB | 1 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,947 | 3,390 | 20.1 | 33% | 50% | 97% | 624 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E C D | 1,890 | 4,219 | 0.3 | 72% | 14% | 0% | 453 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | E E E | 1,745 | 5,742 | 20.6 | 40% | 11% | 94% | 555 KB | 0 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,601 | 7,259 | 9.6 | 25% | 11% | 99% | 787 KB | 2 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,578 | 7,660 | 20.3 | 10% | 0% | 98% | 276 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | E F A | 1,451 | 1,901 | 14.7 | 65% | 0% | 100% | 161 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E E D | 1,450 | 4,231 | 0.0 | 65% | 0% | 0% | 1,120 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,406 | 11,134 | 0.0 | 12% | 0% | 95% | 211 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,348 | 1,590 | 0.1 | 58% | 27% | 0% | 634 KB | 3 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 1,308 | 3,529 | 4.8 | 27% | 47% | 93% | 7,014 KB | 18 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,303 | 2,918 | 14.9 | 0% | 0% | 99% | 129 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,272 | 5,609 | 0.0 | 61% | 0% | – | 536 KB | 2 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,259 | 2,609 | 1.9 | 42% | 0% | 33% | 61 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F B | 1,251 | 4,397 | 0.0 | 41% | 0% | 82% | 554 KB | 27 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 1,209 | 1,826 | 14.1 | 0% | 0% | – | 131 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,207 | 11,120 | 27.3 | 14% | 0% | 100% | 119 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | E F C | 1,044 | 4,821 | 15.3 | 38% | 0% | 90% | 195 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F E C | 954 | 2,217 | 5.4 | 60% | 0% | 98% | 134 KB | 2 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 882 | 3,025 | 25.8 | 50% | 0% | 100% | 148 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | F E B | 832 | 3,944 | 43.9 | 65% | 6% | 86% | 140 KB | 8 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 796 | 17,324 | 14.1 | 24% | 0% | – | 408 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | F F B | 785 | 1,829 | 9.6 | 36% | 0% | 97% | 329 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 780 | 5,630 | 19.3 | 38% | 0% | 100% | 215 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 755 | 3,502 | 12.8 | 47% | 0% | 97% | 49 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 608 | 6,228 | 27.4 | 0% | 16% | 99% | 526 KB | 0 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 585 | 3,950 | 0.8 | 66% | 0% | – | 290 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 497 | 4,623 | 0.0 | 44% | 0% | 0% | 473 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 481 | 2,628 | 7.0 | 68% | 0% | 100% | 175 KB | 222 (+2) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 463 | 6,827 | 7.8 | 48% | 0% | 98% | 122 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 424 | 38,975 | 6.0 | 26% | 0% | 99% | 24 KB | 0 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 392 | 2,404 | 12.7 | 48% | 0% | 99% | 298 KB | 5 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 365 | 4,108 | 0.0 | 64% | 0% | 92% | 70 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 340 | 1,485 | 0.0 | 25% | 0% | – | 202 KB | 4 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 323 | 22,103 | 15.5 | 12% | 0% | 94% | 66 KB | 3 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 315 | 1,396 | 2.4 | 34% | 0% | 100% | 59 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 293 | 34,539 | 3.7 | 36% | 0% | 100% | 1,116 KB | 5 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 283 | 1,190 | 0.0 | 14% | 24% | 98% | 375 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 186 | 5,642 | 0.0 | 58% | 0% | – | 108 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 171 | 808 | 6.0 | 0% | 0% | 97% | 72 KB | 4 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 170 | 5,128 | 19.5 | 19% | 0% | 88% | 303 KB | 23 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 129 | 1,085 | 14.0 | 0% | 0% | – | 55 KB | 0 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 102 | 6,612 | 0.0 | 20% | 0% | – | 112 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 92 | 7,903 | 2.0 | 22% | 13% | 98% | 149 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 85 | 616 | 28.1 | 24% | 0% | 100% | 847 KB | 3 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 30 | 7,773 | 12.4 | 25% | 0% | 98% | 43 KB | 1 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 5 | 2,417 | 0.0 | 24% | 0% | 0% | 110 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 2,045,885 | 49.4 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F B B | – | – | 37.9 | 85% | 34% | 87% | 2,077 KB | 1,412 (+8) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | 0 | 0 | 28.0 | 0% | 0% | 52% | 92 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 1,223 | 24.7 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F C | 0 | 1,986 | 22.4 | 0% | 0% | 97% | 294 KB | 4 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F B B | – | – | 21.5 | 80% | 36% | 94% | 961 KB | 4 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F A | 0 | 737 | 21.3 | 0% | 0% | 100% | 87 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | 0 | 12,429 | 19.0 | 50% | 0% | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 14.6 | 2% | 0% | 98% | 723 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 13.1 | 31% | 0% | 98% | 342 KB | 4 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 3 | 12.6 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 0 | 12.2 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 0 | 2 | 11.6 | 0% | 0% | – | 115 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F D B | – | – | 6.1 | 62% | 0% | 83% | 206 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 64 | 5.6 | 0% | 0% | 84% | 462 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 5.4 | 52% | 74% | 0% | 1,707 KB | 457 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F E B | 0 | 0 | 4.7 | 41% | 41% | 84% | 149 KB | 2 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 1,278 | 4.2 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 0 | 912 | 1.3 | 0% | 0% | 68% | 290 KB | 0 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 1.0 | 0% | 0% | – | 92 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 51% | 6% | 78% | 812 KB | 5 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 28,281 | 0.2 | 78% | 0% | 88% | 1,465 KB | 1,100 (+2) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.2 | 45% | 77% | 96% | 23,932 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 681 | 0.1 | 15% | 0% | 9% | 904 KB | 1,280 (+1) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | 0 | 0 | 0.0 | 67% | 0% | – | 1,157 KB | 2 (+1) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 138 | 0.0 | 0% | 0% | – | 59 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 47% | 15% | 60% | 78 KB | 5 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 39 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
