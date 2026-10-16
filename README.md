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
_219 repos, last measured 2026-10-16. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (219)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 86,381 | 119,614 | 68.4 | 35% | 69% | 87% | 3,038 KB | 1,919 (+39) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 63,430 | 87,935 | 25.7 | 72% | 19% | 94% | 626 KB | 11 (+1) |
| [tale-project/tale](https://github.com/tale-project/tale) | A C B | 57,641 | 95,416 | 35.6 | 75% | 50% | 89% | 2,599 KB | 35 (+1) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | A C C | 51,600 | 61,920 | 52.8 | 78% | 57% | 95% | 611 KB | 2 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | A F B | 49,554 | 708,253 | 77.1 | 37% | 50% | 100% | 570 KB | 2 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | A C A | 46,181 | 63,270 | 89.3 | 78% | 52% | 100% | 162 KB | 14 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A D B | 45,091 | 79,530 | 30.8 | 66% | 21% | 98% | 231 KB | 1 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A E B | 43,508 | 50,150 | 31.4 | 77% | 57% | 95% | 735 KB | 1 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | A B C | 42,475 | 54,404 | 60.9 | 87% | 31% | 96% | 691 KB | 14 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B D C | 39,686 | 94,237 | 50.6 | 68% | 38% | 68% | 2,528 KB | 4 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B B C | 38,149 | 43,539 | 25.8 | 84% | 41% | 82% | 364 KB | 9 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | B F D | 37,970 | 900,452 | 67.7 | 4% | 0% | – | 3,975 KB | 1 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B F B | 37,183 | 50,035 | 36.8 | 29% | 4% | 100% | 531 KB | 37 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B C D | 35,108 | 38,451 | 32.6 | 79% | 64% | 100% | 599 KB | 22 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 33,850 | 106,852 | 24.2 | 56% | 24% | 99% | 824 KB | 31 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B E D | 33,303 | 29,157 | 0.0 | 58% | 0% | – | 265 KB | 0 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D C | 33,244 | 108,333 | 8.6 | 64% | 33% | 65% | 691 KB | 4 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B D B | 31,567 | 44,019 | 30.4 | 68% | 43% | 100% | 1,321 KB | 91 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | B C C | 31,309 | 57,594 | 36.8 | 71% | 0% | 93% | 119 KB | 116 (+1) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | B F C | 30,858 | 84,957 | 0.2 | 37% | 0% | 57% | 1,271 KB | 439 (+5) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D B | 28,544 | 36,266 | 157 | 65% | 55% | 100% | 3,214 KB | 1 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B B A | 28,507 | 56,034 | 41.1 | 81% | 52% | 100% | 353 KB | 2 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B E A | 26,339 | 60,026 | 48.2 | 82% | 35% | 99% | 155 KB | 2 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B E B | 24,987 | 30,280 | 13.4 | 47% | 0% | 99% | 705 KB | 9 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 24,896 | 96,939 | 95.4 | 24% | 17% | 46% | 310 KB | 3 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | B C A | 23,316 | 35,333 | 27.1 | 75% | 38% | 100% | 147 KB | 4 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B E B | 22,791 | 70,359 | 32.8 | 51% | 14% | 93% | 56 KB | 0 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | B E A | 22,385 | 29,929 | 0.7 | 57% | 50% | 100% | 163 KB | 11 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | B E B | 22,016 | 30,008 | 8.3 | 58% | 0% | 90% | 86 KB | 6 (+1) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B C C | 21,165 | 43,022 | 151 | 73% | 8% | 89% | 2,294 KB | 3 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | B E C | 20,323 | 44,758 | 26.8 | 54% | 37% | 96% | 454 KB | 18 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B C C | 20,298 | 32,940 | 0.2 | 76% | 47% | 100% | 312 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | B E A | 20,124 | 28,055 | 23.7 | 55% | 0% | 97% | 116 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | B B D | 20,008 | 17,840 | 0.0 | 81% | 17% | 0% | 601 KB | 1 |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | C F A | 19,865 | 27,304 | 19.2 | 56% | 0% | 97% | 94 KB | 16 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 19,698 | 28,034 | 33.8 | 30% | 26% | 100% | 413 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | C F D | 19,679 | 17,846 | 9.8 | 56% | 0% | – | 82 KB | 2 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | C F D | 19,083 | 48,450 | 23.7 | 34% | 49% | 34% | 3,082 KB | 96 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C E C | 19,002 | 84,732 | 23.1 | 55% | 46% | 100% | 309 KB | 0 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C A D | 18,495 | 22,300 | 0.0 | 90% | 40% | – | 226 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | C C B | 17,890 | 28,552 | 46.7 | 72% | 37% | 100% | 559 KB | 2 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 17,760 | 44,300 | 0.0 | 72% | 62% | – | 1,193 KB | 3 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 17,076 | 34,199 | 0.0 | 71% | 16% | 51% | 455 KB | 1 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 16,833 | 18,980 | 32.7 | 63% | 46% | 84% | 1,402 KB | 3 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C E C | 16,805 | 22,727 | 9.1 | 59% | 34% | 96% | 109 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 16,441 | 27,996 | 12.2 | 36% | 8% | 90% | 2,899 KB | 116 (+1) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C D D | 16,350 | 24,783 | 0.5 | 68% | 59% | – | 161 KB | 0 |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C E D | 15,924 | 564,305 | 0.0 | 75% | 0% | 0% | 3,283 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C D A | 15,224 | 45,103 | 28.8 | 62% | 17% | 100% | 393 KB | 0 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 14,833 | 19,030 | 56.6 | 51% | 62% | 98% | 768 KB | 6,341 (+26) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | C C C | 14,782 | 20,136 | 36.2 | 76% | 26% | 59% | 240 KB | 9 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 14,604 | 27,188 | 26.3 | 25% | 30% | 100% | 225 KB | 7 (+1) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C F B | 14,510 | 22,948 | 6.6 | 28% | 35% | 78% | 570 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C D | 13,669 | 26,702 | 0.0 | 75% | 0% | 33% | 251 KB | 0 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | C E A | 13,553 | 17,695 | 35.6 | 55% | 40% | 93% | 301 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C E C | 13,329 | 26,901 | 32.1 | 54% | 25% | 100% | 592 KB | 0 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C B C | 13,284 | 18,250 | 60.2 | 83% | 70% | 100% | 4,310 KB | 15 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | C F B | 13,282 | 25,753 | 16.6 | 48% | 14% | 95% | 434 KB | 0 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F C | 13,282 | 20,948 | 0.0 | 49% | 20% | 63% | 220 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | C D B | 12,778 | 27,009 | 22.2 | 69% | 65% | 100% | 1,068 KB | 6 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | C C D | 12,634 | 20,835 | 0.0 | 83% | 29% | 42% | 266 KB | 0 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C D C | 12,631 | 19,166 | 0.0 | 66% | 13% | 86% | 856 KB | 1 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | C F B | 12,496 | 24,146 | 16.1 | 50% | 21% | 96% | 808 KB | 4 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 12,394 | 15,279 | 89.1 | 31% | 58% | 76% | 345 KB | 48 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 12,364 | 38,982 | 28.8 | 24% | 18% | 97% | 387 KB | 9 (+0) |
| [integry/propr](https://github.com/integry/propr) | C E B | 12,104 | 16,847 | 12.1 | 50% | 8% | 100% | 4,314 KB | 18 (+1) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 11,995 | 64,129 | 21.8 | 39% | 0% | 89% | 118 KB | 3 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 11,866 | 17,484 | 18.5 | 70% | 38% | 100% | 124 KB | 32 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | C E B | 11,591 | 21,090 | 12.9 | 82% | 47% | 78% | 127 KB | 5 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 11,234 | 27,528 | 15.9 | 26% | 13% | 95% | 67 KB | 2 (+1) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | C C A | 11,206 | 14,993 | 29.0 | 76% | 65% | 94% | 102 KB | 230 (+1) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C C D | 11,173 | 14,072 | 0.0 | 72% | 36% | 39% | 229 KB | 196 (+28) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C E B | 10,936 | 22,961 | 20.1 | 58% | 26% | 100% | 1,826 KB | 5 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | C F B | 10,724 | 14,561 | 14.3 | 45% | 22% | 99% | 661 KB | 11 |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 10,639 | 11,486 | 20.6 | 67% | 23% | 97% | 540 KB | 1 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C E B | 10,492 | 17,331 | 0.0 | 54% | 0% | 93% | 588 KB | 1 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C E C | 10,052 | 43,060 | 25.4 | 52% | 11% | 94% | 718 KB | 5 |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D D C | 9,961 | 12,375 | 10.9 | 65% | 28% | 97% | 6,579 KB | 8 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,870 | 14,897 | 8.1 | 32% | 17% | 100% | 517 KB | 11 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D F B | 9,805 | 264,917 | 30.0 | 70% | 3% | 88% | 1,428 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D E C | 9,715 | 43,599 | 3.8 | 58% | 5% | 100% | 1,116 KB | 5 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 9,529 | 13,104 | 43.0 | 0% | 39% | 97% | 66 KB | 61 (+1) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D C C | 9,430 | 14,096 | 0.0 | 79% | 52% | 62% | 866 KB | 32 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D E B | 9,405 | 13,503 | 27.7 | 66% | 11% | 72% | 186 KB | 0 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 9,310 | 10,433 | 0.0 | 50% | 0% | – | 776 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D C D | 9,095 | 14,923 | 24.4 | 72% | 26% | – | 378 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D F C | 8,916 | 11,335 | 16.6 | 37% | 28% | 100% | 636 KB | 9 (+1) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F A | 8,658 | 16,535 | 4.9 | 0% | 0% | 99% | 397 KB | 129 (+1) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D E B | 8,615 | 19,412 | 74.0 | 45% | 29% | 100% | 699 KB | 0 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D C D | 8,486 | 13,042 | 8.1 | 85% | 30% | 28% | 119 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | D F B | 8,474 | 212,736 | 19.3 | 29% | 8% | 100% | 1,414 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | D F B | 8,227 | 11,973 | 42.3 | 15% | 51% | 100% | 807 KB | 4 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | D F B | 8,094 | 21,132 | 19.3 | 55% | 22% | 100% | 1,058 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D C F | 7,978 | 254,657 | 0.0 | 70% | 35% | – | 8,190 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D E D | 7,837 | 9,193 | 8.5 | 52% | 26% | 25% | 189 KB | 2 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | D F C | 7,806 | 9,908 | 25.6 | 31% | 0% | 96% | 293 KB | 4 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 7,658 | 15,415 | 18.0 | 50% | 7% | 75% | 361 KB | 7 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 7,582 | 7,453 | 22.6 | 64% | 45% | 79% | 803 KB | 1 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 7,555 | 14,745 | 20.9 | 32% | 8% | 100% | 257 KB | 1 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D D C | 7,469 | 20,506 | 3.0 | 64% | 15% | 90% | 319 KB | 1 |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | D E B | 7,324 | 13,047 | 34.1 | 60% | 0% | 83% | 1,413 KB | 2 |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D E A | 7,169 | 33,092 | 12.1 | 47% | 0% | 100% | 236 KB | 5 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | D E B | 7,160 | 11,979 | 31.5 | 68% | 0% | 97% | 105 KB | 4 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | D C B | 6,806 | 7,266 | 16.4 | 78% | 50% | 100% | 94 KB | 0 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 6,791 | 7,682 | 10.1 | 18% | 8% | 93% | 98 KB | 3 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D C B | 6,715 | 14,985 | 20.1 | 77% | 0% | 88% | 700 KB | 4 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D B B | 6,616 | 10,661 | 29.0 | 84% | 25% | 92% | 1,502 KB | 70,076 (+44) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D E C | 6,466 | 9,075 | 25.0 | 60% | 0% | 100% | 403 KB | 2 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 6,335 | 16,125 | 2.4 | 34% | 43% | 66% | 3,212 KB | 534 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D E A | 6,309 | 9,089 | 7.9 | 49% | 42% | 95% | 241 KB | 0 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | D E A | 6,298 | 21,834 | 11.9 | 52% | 36% | 99% | 127 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | D C C | 6,209 | 15,157 | 8.1 | 78% | 22% | 93% | 107 KB | 10 (+2) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | D E B | 6,085 | 12,304 | 26.9 | 55% | 36% | 99% | 972 KB | 93 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F B | 5,817 | 10,999 | 18.0 | 30% | 0% | 97% | 383 KB | 19 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | D F A | 5,690 | 15,693 | 0.0 | 50% | 0% | 95% | 211 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D E C | 5,533 | 8,998 | 22.5 | 48% | 21% | 99% | 548 KB | 5 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 5,467 | 15,330 | 0.0 | 62% | 13% | 98% | 226 KB | 1 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | D D D | 5,292 | 11,324 | 0.0 | 61% | 12% | 0% | 349 KB | 4 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D E C | 5,187 | 7,768 | 25.6 | 52% | 0% | 96% | 516 KB | 17 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | D D C | 5,099 | 6,042 | 10.6 | 67% | 0% | 91% | 115 KB | 1 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | D E B | 5,064 | 14,269 | 19.7 | 74% | 30% | 83% | 66 KB | 10 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E B A | 4,843 | 5,819 | 19.4 | 82% | 41% | 100% | 387 KB | 9 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 4,809 | 12,215 | 0.0 | 39% | 45% | 91% | 397 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 4,749 | 10,923 | 8.9 | 39% | 10% | 98% | 787 KB | 2 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 4,732 | 16,078 | 18.5 | 50% | 61% | 100% | 171 KB | 0 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 4,562 | 34,515 | 0.8 | 60% | 28% | 37% | 5,272 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E E B | 4,496 | 11,790 | 12.2 | 60% | 6% | 96% | 49 KB | 0 |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F C | 4,383 | 13,198 | 0.0 | 17% | 56% | 51% | 142 KB | 107 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E C A | 4,146 | 6,418 | 13.4 | 76% | 6% | 97% | 434 KB | 1 |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E F D | 3,949 | 4,905 | 28.2 | 60% | 30% | – | 343 KB | 2 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E E D | 3,920 | 22,767 | 0.0 | 59% | 0% | – | 189 KB | 28 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | E E C | 3,796 | 21,351 | 0.0 | 60% | 0% | 100% | 441 KB | 1 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 3,780 | 7,523 | 25.8 | 17% | 10% | 96% | 125 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E E B | 3,774 | 9,367 | 0.0 | 50% | 11% | 100% | 340 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | E E D | 3,730 | 8,812 | 0.0 | 66% | 0% | – | 108 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 3,716 | 12,332 | 24.6 | 8% | 0% | 92% | 489 KB | 28 (+1) |
| [floor/teamcli](https://github.com/floor/teamcli) | E E B | 3,624 | 8,095 | 9.0 | 51% | 2% | 98% | 76 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E E C | 3,542 | 4,879 | 23.4 | 59% | 29% | 95% | 544 KB | 0 |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E E C | 3,412 | 16,942 | 19.0 | 50% | 42% | 98% | 406 KB | 0 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 3,332 | 6,575 | 4.3 | 46% | 10% | 95% | 7,014 KB | 18 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E D B | 3,279 | 19,475 | 9.9 | 69% | 12% | 94% | 531 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,144 | 5,597 | 18.6 | 8% | 15% | 100% | 386 KB | 1 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 3,086 | 16,121 | 13.8 | 31% | 0% | 100% | 240 KB | 2 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 3,012 | 6,319 | 9.5 | 47% | 5% | 98% | 329 KB | 0 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,890 | 7,690 | 29.2 | 56% | 0% | 47% | 97 KB | 0 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | E D E | 2,758 | 6,844 | 20.3 | 66% | 6% | 94% | 549 KB | 0 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 2,722 | 4,882 | 13.7 | 36% | 0% | – | 43 KB | 3 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E F B | 2,693 | 4,626 | 0.1 | 38% | 0% | 89% | 268 KB | 3 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,590 | 6,358 | 0.1 | 55% | 22% | 71% | 153 KB | 29 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 2,560 | 4,669 | 44.3 | 55% | 30% | 100% | 299 KB | 2 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | E F D | 2,501 | 6,352 | 1.0 | 49% | 0% | – | 92 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F B | 2,462 | 11,836 | 13.6 | 58% | 0% | 92% | 1,196 KB | 13 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E C E | 2,259 | 18,337 | 20.0 | 80% | 10% | 99% | 613 KB | 11 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,139 | 7,905 | 28.9 | 0% | 14% | 100% | 617 KB | 1 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,113 | 11,294 | 10.4 | 57% | 0% | 95% | 313 KB | 2 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 2,062 | 3,540 | 0.2 | 60% | 0% | 100% | 142 KB | 7 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E E D | 1,932 | 4,872 | 0.2 | 49% | 17% | 0% | 435 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,884 | 2,999 | 18.5 | 48% | 60% | 97% | 574 KB | 1 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,871 | 4,592 | 11.9 | 31% | 28% | 80% | 225 KB | 1 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 1,864 | 4,766 | 13.8 | 34% | 0% | – | 96 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | E D B | 1,774 | 8,297 | 45.4 | 67% | 4% | 97% | 131 KB | 8 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,751 | 4,714 | 23.1 | 0% | 0% | 98% | 119 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | E F D | 1,651 | 2,220 | 13.8 | 35% | 20% | – | 55 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,578 | 1,994 | 15.2 | 18% | 0% | 97% | 268 KB | 0 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,572 | 6,499 | 15.8 | 41% | 0% | 100% | 190 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,456 | 4,738 | 14.0 | 39% | 0% | 98% | 129 KB | 0 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,408 | 5,833 | 0.0 | 60% | 15% | – | 435 KB | 2 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E F D | 1,348 | 1,809 | 0.2 | 48% | 30% | 0% | 628 KB | 3 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 1,299 | 4,523 | 23.7 | 67% | 0% | 100% | 129 KB | 22 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 1,271 | 69,707 | 5.1 | 30% | 0% | 97% | 24 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,259 | 3,231 | 1.9 | 31% | 0% | 33% | 61 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E E D | 1,193 | 29,205 | 9.0 | 67% | 0% | 21% | 460 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 882 | 1,997 | 27.2 | 75% | 0% | 100% | 136 KB | 1 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 790 | 9,916 | 20.1 | 50% | 0% | 88% | 303 KB | 22 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 693 | 1,177 | 6.2 | 0% | 0% | 94% | 72 KB | 4 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 669 | 3,668 | 24.4 | 10% | 18% | 96% | 526 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 669 | 3,183 | 0.0 | 52% | 0% | – | 202 KB | 4 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 638 | 1,079 | 15.2 | 46% | 0% | 99% | 154 KB | 0 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | F F D | 591 | 6,452 | 0.0 | 39% | 0% | 33% | 397 KB | 458 (+2) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 587 | 3,833 | 11.8 | 23% | 0% | – | 115 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 568 | 7,463 | 12.5 | 46% | 0% | 100% | 961 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F E B | 481 | 1,588 | 8.5 | 73% | 0% | 100% | 173 KB | 220 (+1) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 443 | 2,689 | 1.3 | 0% | 0% | 68% | 290 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 323 | 26,926 | 13.8 | 17% | 20% | 96% | 66 KB | 3 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 241 | 2,608 | 5.6 | 0% | 0% | 81% | 466 KB | 0 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 218 | 8,890 | 1.6 | 68% | 18% | 65% | 149 KB | 0 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 149 | 517 | 1.1 | 28% | 0% | 100% | 111 KB | 2 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 143 | 7,497 | 15.6 | 34% | 0% | – | 408 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | 141 | 909 | 2.8 | 65% | 0% | 100% | 59 KB | 1 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 128 | 29,592 | 6.4 | 0% | 0% | 88% | 151 KB | 345 (-2) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 82 | 3,249 | 0.0 | 24% | 0% | 0% | 473 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 55 | 6,715 | 11.1 | 55% | 10% | 98% | 43 KB | 1 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 32 | 394 | 0.0 | 34% | 0% | – | 18 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 644,345 | 42.0 | 30% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F C B | – | – | 36.5 | 76% | 44% | 88% | 1,999 KB | 1,394 (+3) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 397 | 33.3 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | 0 | 3,013 | 26.0 | 0% | 0% | 52% | 92 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 419 | 23.2 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 21.0 | 39% | 14% | 99% | 1,104 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F A | 0 | 2,299 | 20.7 | 71% | 0% | 100% | 73 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 20.6 | 45% | 32% | 94% | 947 KB | 4 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 16.2 | 22% | 0% | 98% | 723 KB | 5 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 1,503 | 12.6 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 4,387 | 12.2 | 30% | 0% | 98% | 149 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 7.7 | 56% | 0% | 100% | 341 KB | 4 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 1,266 | 7.1 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F B D | – | – | 5.2 | 82% | 72% | 0% | 1,061 KB | 457 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F C B | – | – | 0.9 | 76% | 3% | 79% | 812 KB | 5 (+1) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F E D | 0 | 33 | 0.3 | 52% | 0% | – | 245 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 7,558 | 0.2 | 47% | 0% | 86% | 1,451 KB | 1,096 (+2) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 650 | 0.2 | 17% | 0% | 8% | 904 KB | 1,278 (+3) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F C E | – | – | 0.2 | 77% | 10% | 96% | 18,461 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 2,662 | 0.0 | 14% | 0% | 0% | 110 KB | 0 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 0 | 2,780 | 0.0 | 0% | 0% | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 2,449 | 0.0 | 74% | 0% | – | 80 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 346 | 0.0 | 0% | 0% | – | 59 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D D | – | – | 0.0 | 68% | 64% | 49% | 72 KB | 5 (+0) |
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
