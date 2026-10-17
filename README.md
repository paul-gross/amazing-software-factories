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
_219 repos, last measured 2026-10-17. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (219)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 86,381 | 121,237 | 70.1 | 35% | 65% | 87% | 3,038 KB | 1,946 (+27) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 62,305 | 83,368 | 27.0 | 72% | 35% | 94% | 521 KB | 11 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A C B | 57,641 | 99,115 | 35.2 | 70% | 6% | 91% | 2,600 KB | 35 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A B B | 48,677 | 53,681 | 33.8 | 82% | 56% | 95% | 738 KB | 1 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | A D C | 46,204 | 187,070 | 9.3 | 68% | 24% | 54% | 718 KB | 4 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | A B C | 44,436 | 48,340 | 27.6 | 84% | 80% | 94% | 364 KB | 9 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | A A C | 42,532 | 56,648 | 54.5 | 92% | 51% | 100% | 608 KB | 2 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A C B | 42,311 | 76,879 | 30.6 | 80% | 24% | 98% | 231 KB | 1 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 41,483 | 50,569 | 61.2 | 84% | 32% | 100% | 691 KB | 14 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A D C | 41,418 | 66,454 | 45.3 | 68% | 8% | 98% | 119 KB | 116 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B D C | 39,308 | 95,464 | 54.2 | 62% | 41% | 62% | 1,720 KB | 4 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 38,890 | 58,929 | 90.3 | 75% | 36% | 94% | 162 KB | 14 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 37,970 | 984,625 | 69.4 | 8% | 0% | 100% | 3,975 KB | 1 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B F B | 34,749 | 696,253 | 80.2 | 39% | 35% | 100% | 572 KB | 2 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B B D | 34,143 | 31,720 | 31.4 | 83% | 3% | 98% | 599 KB | 22 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B F D | 33,303 | 30,612 | 0.0 | 40% | 0% | – | 265 KB | 0 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 31,883 | 38,564 | 162 | 61% | 56% | 100% | 3,234 KB | 1 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B C B | 31,567 | 43,977 | 31.5 | 75% | 44% | 100% | 1,322 KB | 91 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 30,943 | 112,247 | 25.6 | 53% | 43% | 100% | 829 KB | 31 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 30,886 | 109,455 | 97.1 | 22% | 19% | 46% | 310 KB | 3 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B F C | 30,858 | 55,053 | 0.2 | 34% | 0% | 60% | 1,271 KB | 439 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B C A | 28,507 | 59,085 | 41.9 | 75% | 50% | 100% | 355 KB | 2 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | B E B | 27,379 | 32,174 | 19.3 | 62% | 13% | 93% | 808 KB | 4 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B E A | 26,339 | 62,753 | 52.6 | 84% | 32% | 100% | 156 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 25,786 | 103,252 | 36.4 | 38% | 13% | 100% | 55 KB | 0 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B C C | 25,628 | 43,838 | 154 | 77% | 9% | 89% | 2,294 KB | 3 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B E B | 25,327 | 90,770 | 27.2 | 52% | 42% | 87% | 330 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B F B | 24,071 | 42,245 | 36.5 | 36% | 4% | 99% | 531 KB | 37 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | B B A | 23,316 | 35,078 | 27.0 | 80% | 49% | 96% | 147 KB | 4 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B F B | 23,115 | 30,411 | 13.4 | 55% | 0% | 99% | 706 KB | 9 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 22,901 | 54,840 | 22.6 | 39% | 36% | 34% | 3,082 KB | 96 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,792 | 30,420 | 45.6 | 76% | 38% | 100% | 558 KB | 2 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | B C D | 20,008 | 18,284 | 0.0 | 74% | 0% | 0% | 601 KB | 1 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 19,698 | 27,235 | 34.4 | 31% | 22% | 100% | 418 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | C E A | 19,620 | 26,375 | 0.7 | 49% | 42% | 100% | 163 KB | 11 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C E D | 18,616 | 24,621 | 0.6 | 55% | 62% | – | 161 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | C F A | 18,440 | 27,089 | 19.2 | 56% | 0% | 97% | 94 KB | 16 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C C D | 18,247 | 18,957 | 0.0 | 87% | 23% | – | 226 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | C F B | 18,107 | 21,819 | 8.4 | 52% | 0% | 85% | 86 KB | 6 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 17,992 | 42,480 | 27.6 | 52% | 37% | 97% | 454 KB | 18 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 17,076 | 40,510 | 0.0 | 61% | 12% | 50% | 467 KB | 1 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 16,995 | 41,685 | 0.0 | 73% | 64% | – | 1,192 KB | 3 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C D C | 16,805 | 20,909 | 9.3 | 61% | 36% | 95% | 109 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,441 | 25,056 | 12.4 | 29% | 8% | 91% | 2,913 KB | 117 (+1) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | C E B | 16,417 | 30,245 | 22.7 | 64% | 21% | 100% | 1,060 KB | 0 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 16,067 | 31,522 | 27.2 | 24% | 24% | 100% | 225 KB | 7 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C E A | 15,685 | 24,540 | 29.3 | 53% | 0% | 100% | 117 KB | 1 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E C | 15,500 | 21,673 | 57.7 | 43% | 60% | 63% | 768 KB | 6,349 (+8) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C C A | 15,224 | 47,206 | 29.2 | 72% | 18% | 100% | 393 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | C C C | 14,210 | 24,055 | 37.7 | 89% | 24% | 59% | 240 KB | 9 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 13,275 | 25,840 | 34.4 | 52% | 9% | 100% | 599 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | C C D | 13,262 | 18,302 | 27.0 | 78% | 51% | – | 378 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C B C | 13,125 | 20,079 | 66.8 | 86% | 71% | 100% | 4,357 KB | 15 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F C | 12,722 | 20,776 | 0.0 | 38% | 21% | 54% | 220 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 12,586 | 15,644 | 0.0 | 82% | 53% | 34% | 866 KB | 32 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C C D | 12,549 | 16,723 | 0.0 | 85% | 7% | 42% | 266 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 12,364 | 25,520 | 32.4 | 40% | 39% | 97% | 387 KB | 9 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C E D | 12,179 | 486,418 | 0.0 | 61% | 0% | 0% | 3,283 KB | 1 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 11,866 | 16,341 | 19.9 | 74% | 34% | 100% | 124 KB | 32 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C D C | 11,735 | 13,633 | 0.0 | 66% | 36% | 86% | 858 KB | 1 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | C F B | 11,720 | 22,955 | 17.0 | 38% | 16% | 91% | 436 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C F B | 11,591 | 20,808 | 13.0 | 74% | 0% | 82% | 127 KB | 5 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 11,218 | 26,025 | 20.6 | 57% | 23% | 100% | 1,869 KB | 5 (+0) |
| [integry/propr](https://github.com/integry/propr) | C E B | 11,146 | 14,339 | 12.6 | 61% | 8% | 100% | 4,314 KB | 18 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 10,792 | 21,001 | 0.0 | 71% | 0% | 20% | 255 KB | 0 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 10,779 | 14,549 | 89.9 | 28% | 60% | 76% | 345 KB | 48 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C F B | 10,754 | 21,319 | 7.0 | 44% | 25% | 77% | 573 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C C B | 10,639 | 11,429 | 21.3 | 77% | 24% | 98% | 548 KB | 1 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 10,630 | 17,434 | 33.4 | 67% | 46% | 86% | 1,459 KB | 3 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C F B | 10,494 | 23,545 | 23.0 | 61% | 46% | 98% | 1,077 KB | 6 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C F B | 10,492 | 16,979 | 0.0 | 29% | 0% | 95% | 588 KB | 1 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 10,246 | 49,612 | 22.9 | 48% | 0% | 89% | 118 KB | 3 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 10,104 | 26,368 | 16.2 | 20% | 14% | 95% | 67 KB | 2 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C E C | 10,052 | 44,277 | 25.5 | 59% | 13% | 94% | 736 KB | 5 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C C D | 10,031 | 11,667 | 0.0 | 76% | 43% | 41% | 241 KB | 208 (+12) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D C C | 9,962 | 23,086 | 0.2 | 75% | 35% | 100% | 328 KB | 2 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,870 | 14,294 | 8.2 | 35% | 22% | 100% | 517 KB | 11 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 9,529 | 12,751 | 44.9 | 0% | 38% | 85% | 66 KB | 61 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D E B | 9,405 | 13,161 | 27.3 | 64% | 11% | 73% | 203 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | D E A | 9,009 | 14,210 | 36.3 | 50% | 46% | 92% | 324 KB | 0 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | D C B | 8,911 | 22,737 | 10.8 | 71% | 38% | 96% | 539 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | D F B | 8,787 | 16,191 | 40.4 | 17% | 42% | 100% | 837 KB | 4 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 8,770 | 14,780 | 10.1 | 54% | 0% | – | 82 KB | 2 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F A | 8,658 | 16,391 | 4.6 | 0% | 0% | 97% | 398 KB | 129 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D D | 8,486 | 13,136 | 10.0 | 65% | 29% | 30% | 124 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D E C | 8,479 | 10,392 | 10.9 | 57% | 0% | 91% | 6,579 KB | 8 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D F C | 8,396 | 11,533 | 17.3 | 35% | 27% | 100% | 643 KB | 9 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D F B | 8,257 | 114,634 | 30.8 | 36% | 4% | 93% | 1,428 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 8,238 | 238,216 | 19.6 | 32% | 16% | 100% | 1,414 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D E B | 8,224 | 14,414 | 74.6 | 50% | 32% | 100% | 708 KB | 0 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D E C | 8,179 | 11,748 | 28.0 | 62% | 0% | 100% | 403 KB | 2 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 7,837 | 9,826 | 8.2 | 66% | 22% | 24% | 190 KB | 2 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 7,767 | 15,969 | 16.9 | 25% | 9% | 85% | 361 KB | 7 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 7,561 | 11,728 | 13.9 | 64% | 0% | 100% | 695 KB | 11 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 7,555 | 14,983 | 21.0 | 34% | 15% | 99% | 265 KB | 1 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D F A | 7,169 | 22,428 | 13.1 | 34% | 0% | 100% | 236 KB | 5 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D C A | 6,927 | 12,501 | 28.8 | 78% | 38% | 94% | 102 KB | 230 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 6,806 | 6,885 | 17.2 | 78% | 50% | 99% | 95 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 6,791 | 8,053 | 10.2 | 17% | 23% | 95% | 99 KB | 4 (+1) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D C B | 6,715 | 15,287 | 21.1 | 80% | 0% | 88% | 700 KB | 4 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D C B | 6,616 | 11,317 | 28.0 | 78% | 32% | 82% | 1,477 KB | 70,119 (+43) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,535 | 22,941 | 0.0 | 76% | 0% | 100% | 441 KB | 1 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 6,335 | 18,104 | 2.9 | 13% | 47% | 87% | 3,275 KB | 539 (+3) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D D C | 6,324 | 15,289 | 9.7 | 66% | 19% | 81% | 139 KB | 11 (+1) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D E A | 6,298 | 26,107 | 13.4 | 56% | 36% | 89% | 129 KB | 0 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 6,143 | 10,727 | 0.0 | 42% | 10% | 99% | 370 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 6,139 | 15,143 | 3.1 | 59% | 18% | 90% | 319 KB | 1 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D F B | 6,013 | 9,635 | 31.5 | 73% | 0% | 98% | 106 KB | 4 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D D A | 5,899 | 9,951 | 8.6 | 66% | 44% | 94% | 241 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | D E C | 5,630 | 16,790 | 18.2 | 48% | 54% | 100% | 171 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 5,606 | 10,212 | 18.1 | 28% | 0% | 71% | 383 KB | 19 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 5,533 | 8,888 | 23.2 | 34% | 24% | 99% | 553 KB | 5 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 5,315 | 10,865 | 0.0 | 40% | 42% | 93% | 398 KB | 1 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D E F | 5,282 | 194,319 | 0.0 | 65% | 0% | – | 8,190 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | D B A | 5,216 | 6,280 | 19.4 | 86% | 60% | 100% | 389 KB | 10 (+1) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,192 | 6,759 | 22.5 | 76% | 6% | 84% | 850 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | D C B | 5,064 | 12,965 | 20.4 | 83% | 54% | 84% | 67 KB | 10 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | D C D | 5,027 | 11,496 | 0.0 | 77% | 12% | 0% | 355 KB | 4 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 4,912 | 10,673 | 28.3 | 46% | 30% | 99% | 973 KB | 95 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E E C | 4,894 | 6,540 | 26.0 | 49% | 0% | 100% | 467 KB | 17 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 4,786 | 5,191 | 29.8 | 55% | 14% | – | 350 KB | 2 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 4,749 | 10,141 | 8.9 | 40% | 10% | 98% | 787 KB | 2 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 4,661 | 10,893 | 26.9 | 18% | 10% | 95% | 127 KB | 1 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 4,562 | 34,591 | 0.8 | 54% | 28% | 44% | 5,509 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 4,450 | 5,335 | 14.2 | 53% | 0% | – | 44 KB | 3 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E E A | 4,385 | 7,177 | 13.8 | 66% | 28% | 98% | 464 KB | 1 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 4,141 | 14,652 | 0.0 | 18% | 60% | 49% | 143 KB | 108 (+1) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | E F D | 4,058 | 8,915 | 0.0 | 58% | 0% | – | 776 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 3,716 | 8,669 | 24.4 | 0% | 0% | 95% | 489 KB | 28 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,677 | 6,364 | 19.1 | 18% | 13% | 100% | 386 KB | 1 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 3,624 | 8,556 | 12.4 | 34% | 2% | 97% | 79 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 3,385 | 4,092 | 24.0 | 22% | 22% | 95% | 544 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 3,332 | 6,111 | 4.3 | 38% | 11% | 95% | 7,014 KB | 18 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F C | 3,147 | 38,973 | 3.7 | 37% | 0% | 100% | 1,116 KB | 5 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 3,086 | 11,990 | 13.8 | 28% | 0% | 100% | 240 KB | 2 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E B E | 3,076 | 24,468 | 20.9 | 83% | 43% | 99% | 613 KB | 11 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E F B | 3,032 | 10,852 | 12.8 | 45% | 0% | 96% | 49 KB | 0 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 3,019 | 5,351 | 0.3 | 50% | 0% | 100% | 142 KB | 7 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,953 | 19,199 | 11.0 | 57% | 0% | 95% | 314 KB | 2 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | E D E | 2,758 | 7,124 | 20.4 | 68% | 11% | 94% | 555 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 2,723 | 14,892 | 19.1 | 54% | 40% | 98% | 403 KB | 1 (+1) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,693 | 4,944 | 0.1 | 38% | 0% | 86% | 309 KB | 3 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,648 | 8,372 | 1.0 | 58% | 0% | – | 92 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,590 | 6,666 | 0.1 | 58% | 8% | 73% | 153 KB | 29 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,560 | 4,785 | 46.5 | 45% | 26% | 97% | 301 KB | 2 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 2,493 | 3,643 | 19.2 | 45% | 60% | 97% | 624 KB | 1 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F B | 2,462 | 12,141 | 14.1 | 24% | 0% | 90% | 1,182 KB | 13 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 2,417 | 6,015 | 9.7 | 47% | 5% | 98% | 329 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E C C | 2,405 | 5,301 | 11.0 | 71% | 0% | 92% | 115 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,318 | 6,130 | 28.8 | 55% | 0% | 47% | 97 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E E D | 2,292 | 25,559 | 0.0 | 55% | 18% | – | 189 KB | 28 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 2,170 | 4,986 | 12.9 | 35% | 21% | 79% | 225 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,092 | 6,150 | 29.4 | 4% | 0% | 100% | 617 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 1,890 | 4,198 | 0.2 | 34% | 20% | 0% | 443 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,751 | 10,974 | 25.7 | 17% | 0% | 98% | 119 KB | 0 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 1,726 | 2,900 | 14.1 | 21% | 0% | – | 96 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,657 | 12,571 | 0.0 | 26% | 0% | 95% | 211 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 1,651 | 2,000 | 14.0 | 13% | 0% | – | 55 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,578 | 4,581 | 19.1 | 11% | 0% | 98% | 271 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,543 | 6,346 | 16.7 | 40% | 0% | 100% | 210 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,456 | 3,721 | 14.4 | 9% | 0% | 99% | 129 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | E F D | 1,353 | 6,987 | 0.0 | 54% | 0% | – | 108 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E F D | 1,348 | 1,667 | 0.2 | 41% | 29% | 0% | 633 KB | 3 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 1,299 | 3,595 | 23.0 | 46% | 0% | 98% | 129 KB | 23 (+1) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,272 | 4,280 | 0.0 | 61% | 0% | – | 475 KB | 2 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 1,271 | 68,323 | 5.1 | 34% | 0% | 99% | 24 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,259 | 3,143 | 1.9 | 32% | 0% | 33% | 61 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F D | 945 | 29,007 | 9.2 | 57% | 0% | 46% | 495 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 882 | 2,678 | 27.0 | 63% | 0% | 100% | 138 KB | 1 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | F D B | 832 | 5,105 | 45.5 | 66% | 5% | 94% | 133 KB | 8 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 795 | 7,191 | 14.9 | 35% | 0% | – | 408 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 693 | 1,144 | 6.3 | 0% | 0% | 96% | 72 KB | 4 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 638 | 1,006 | 15.1 | 50% | 0% | 100% | 154 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 608 | 3,679 | 24.3 | 16% | 19% | 99% | 526 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 591 | 3,741 | 0.0 | 56% | 0% | 33% | 397 KB | 458 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 568 | 7,532 | 12.5 | 42% | 0% | 100% | 975 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 481 | 1,544 | 7.7 | 50% | 0% | 100% | 173 KB | 220 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 443 | 2,757 | 1.3 | 0% | 0% | 68% | 290 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 372 | 5,537 | 20.0 | 17% | 0% | 88% | 303 KB | 22 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 340 | 1,992 | 0.0 | 19% | 0% | – | 202 KB | 4 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 323 | 22,355 | 14.2 | 15% | 9% | 92% | 66 KB | 3 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F E A | 315 | 964 | 2.6 | 71% | 0% | 100% | 59 KB | 1 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 296 | 30,820 | 6.5 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 149 | 934 | 2.4 | 32% | 0% | 98% | 122 KB | 2 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 92 | 8,038 | 1.7 | 58% | 26% | 73% | 149 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 82 | 3,412 | 0.0 | 60% | 0% | 0% | 473 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 58 | 374 | 30.1 | 31% | 0% | 100% | 847 KB | 3 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 33 | 7,873 | 11.8 | 68% | 9% | 98% | 43 KB | 1 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 6 | 1,266 | 11.8 | 40% | 0% | – | 115 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 1,763,176 | 45.5 | 32% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F B B | – | – | 36.7 | 81% | 36% | 87% | 2,005 KB | 1,399 (+5) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | 0 | 752 | 28.0 | 0% | 0% | 52% | 92 KB | 1 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F C | 0 | 4,642 | 24.4 | 50% | 0% | 95% | 293 KB | 4 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 46 | 23.5 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F D B | – | – | 21.2 | 63% | 30% | 94% | 960 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 20.2 | 25% | 22% | 99% | 1,104 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F A | 0 | 0 | 19.8 | – | – | 94% | 83 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 16.3 | 22% | 0% | 98% | 723 KB | 5 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 1,783 | 12.2 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 2 | 12.1 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 8.9 | 22% | 0% | 100% | 341 KB | 4 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 295 | 7.2 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 2,437 | 5.6 | 0% | 0% | 81% | 466 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F E D | – | – | 5.3 | 52% | 67% | 0% | 1,061 KB | 457 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 76% | 3% | 79% | 812 KB | 5 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 2,402 | 0.3 | 35% | 0% | – | 245 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 5,246 | 0.2 | 0% | 0% | 76% | 1,463 KB | 1,097 (+1) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.2 | 84% | 26% | 96% | 20,534 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 681 | 0.1 | 15% | 0% | 8% | 904 KB | 1,279 (+1) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,675 | 0.0 | 12% | 0% | 0% | 110 KB | 0 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 0 | 306 | 0.0 | 0% | 0% | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 129 | 0.0 | 0% | 0% | – | 80 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 264 | 0.0 | 0% | 0% | – | 59 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D D | – | – | 0.0 | 64% | 40% | 18% | 72 KB | 5 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 120 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
