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
_360 repos, last measured 2026-11-02. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (360)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A F C | 77,546 | 71,848 | 42.1 | 36% | 17% | 57% | 408 KB | 83 (+1) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,178 | 95,746 | 24.9 | 78% | 40% | 91% | 209 KB | 8 (+2) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A E C | 67,983 | 230,171 | 122 | 57% | 4% | 51% | 307 KB | 4 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A E B | 53,036 | 62,668 | 40.6 | 72% | 33% | 100% | 690 KB | 11 (+0) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 47,284 | 49,775 | 67.6 | 10% | 15% | 99% | 3,257 KB | 2,072 (+1) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 44,673 | 52,244 | 65.9 | 72% | 40% | 94% | 1,048 KB | 1 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B E D | 36,851 | 60,103 | 0.1 | 53% | 6% | 9% | 2,578 KB | 2 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B F C | 36,737 | 102,179 | 160 | 35% | 32% | 89% | 2,294 KB | 4 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B E A | 35,376 | 59,813 | 145 | 41% | 61% | 96% | 199 KB | 19 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | B D B | 32,519 | 50,796 | 0.0 | 66% | 45% | 78% | 221 KB | 115 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B B C | 31,797 | 55,074 | 34.6 | 86% | 58% | 59% | 798 KB | 4 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B B B | 29,699 | 48,956 | 54.8 | 85% | 20% | 91% | 568 KB | 1 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | B D C | 29,078 | 44,476 | 29.2 | 68% | 37% | 98% | 725 KB | 9 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | B F B | 28,324 | 50,170 | 102 | 35% | 30% | 91% | 4,656 KB | 79 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 27,903 | 46,646 | 41.6 | 64% | 61% | 96% | 547 KB | 2 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | B A B | 27,709 | 41,920 | 40.2 | 90% | 66% | 91% | 816 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | B E B | 27,646 | 205,382 | 1.4 | 59% | 42% | 89% | 3,340 KB | 7 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | B B D | 27,176 | 36,510 | 0.0 | 82% | 44% | 40% | 1,333 KB | 34 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B C B | 27,047 | 29,471 | 22.6 | 74% | 50% | 93% | 788 KB | 5 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | B E C | 25,140 | 33,066 | 28.5 | 60% | 36% | 97% | 363 KB | 10 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | B E D | 24,001 | 37,362 | 0.0 | 65% | 0% | – | 209 KB | 0 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | B F A | 23,542 | 42,322 | 44.9 | 54% | 20% | 97% | 230 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | B F B | 20,911 | 75,548 | 18.2 | 22% | 10% | 78% | 126 KB | 4 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | B C C | 20,879 | 25,056 | 25.5 | 77% | 31% | 99% | 180 KB | 33 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 20,613 | 30,802 | 31.0 | 34% | 37% | 100% | 1,495 KB | 94 (+1) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C D C | 19,570 | 42,623 | 23.5 | 68% | 27% | 94% | 314 KB | 0 (+0) |
| [arul28/ADE](https://github.com/arul28/ADE) | C F C | 19,505 | 27,645 | 18.5 | 11% | 12% | 87% | 6,732 KB | 130 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C C D | 19,327 | 22,595 | 57.9 | 73% | 25% | 25% | 822 KB | 16 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | C B A | 18,703 | 44,788 | 43.9 | 80% | 34% | 100% | 305 KB | 2 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | C F B | 17,804 | 24,947 | 23.1 | 17% | 0% | 100% | 549 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | C F C | 17,712 | 23,372 | 2.8 | 29% | 8% | 96% | 2,284 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | C C B | 17,400 | 22,975 | 0.0 | 71% | 18% | 79% | 321 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 16,469 | 67,267 | 7.1 | 10% | 0% | 95% | 456 KB | 140 (+1) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | C C B | 16,445 | 22,715 | 178 | 76% | 56% | 96% | 2,386 KB | 1 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | C F B | 16,362 | 20,522 | 20.4 | 46% | 0% | 97% | 383 KB | 1,598 (+4) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | C F B | 16,066 | 37,310 | 28.7 | 50% | 0% | 100% | 158 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | C E C | 15,699 | 27,916 | 16.4 | 44% | 48% | 67% | 520 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | C F B | 15,229 | 15,647 | 23.4 | 38% | 32% | 90% | 608 KB | 1 (+0) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C F C | 14,464 | 41,442 | 25.2 | 22% | 39% | 100% | 488 KB | 21 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | C F D | 14,416 | 24,011 | 12.8 | 63% | 0% | 0% | 144 KB | 15 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C B D | 13,995 | 34,723 | 0.0 | 81% | 51% | – | 1,233 KB | 3 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C E B | 13,942 | 22,415 | 100 | 50% | 48% | 76% | 373 KB | 74 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | C E B | 13,822 | 15,627 | 27.8 | 46% | 0% | 82% | 312 KB | 1 (+0) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | C C A | 13,498 | 88,926 | 18.0 | 76% | 24% | 99% | 353 KB | 0 (+0) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | C E B | 13,415 | 17,703 | 14.9 | 48% | 45% | 95% | 258 KB | 13 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | C F B | 12,856 | 11,295 | 8.0 | 44% | 0% | 98% | 363 KB | 1 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C E B | 12,609 | 17,531 | 0.0 | 76% | 15% | 78% | 287 KB | 0 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C B B | 12,386 | 91,301 | 30.5 | 86% | 21% | 99% | 1,056 KB | 35 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 12,374 | 23,061 | 44.8 | 5% | 3% | 96% | 249 KB | 0 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | C E C | 12,305 | 22,729 | 0.0 | 59% | 27% | 100% | 4,357 KB | 15 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | C C C | 12,292 | 14,038 | 23.1 | 77% | 17% | 100% | 42 KB | 0 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | C F C | 12,221 | 24,945 | 0.0 | 26% | 8% | 99% | 948 KB | 45 (+4) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | C E B | 12,064 | 14,970 | 13.4 | 48% | 17% | 93% | 1,202 KB | 13 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C E C | 11,945 | 36,797 | 32.1 | 57% | 63% | 65% | 1,425 KB | 70,577 (+22) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | C F B | 11,710 | 22,895 | 40.8 | 4% | 50% | 100% | 225 KB | 7 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | C F C | 11,572 | 39,329 | 0.0 | 49% | 2% | 100% | 550 KB | 1 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | C E D | 11,467 | 42,646 | 0.0 | 57% | 6% | – | 455 KB | 2 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 11,406 | 13,612 | 49.0 | 26% | 32% | 71% | 335 KB | 1 (+0) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 11,369 | 99,711 | 19.9 | 54% | 33% | 95% | 735 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | C D B | 11,332 | 12,950 | 47.6 | 62% | 22% | 98% | 916 KB | 2 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | C D A | 11,289 | 29,682 | 29.9 | 70% | 33% | 97% | 200 KB | 6 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | C C B | 11,189 | 14,613 | 66.3 | 82% | 2% | 96% | 682 KB | 0 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | C F B | 10,900 | 12,799 | 25.2 | 23% | 8% | 96% | 628 KB | 0 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | C E B | 10,883 | 204,377 | 34.0 | 55% | 53% | 89% | 198 KB | 9 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | C C A | 10,686 | 26,996 | 87.9 | 81% | 1% | 99% | 62 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | C F C | 10,581 | 552,203 | 44.5 | 8% | 0% | 100% | 703 KB | 0 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E C | 10,452 | 17,594 | 68.9 | 47% | 61% | 66% | 275 KB | 6,519 (+28) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D C D | 9,880 | 15,308 | 9.6 | 75% | 35% | 39% | 205 KB | 9 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 9,855 | 14,309 | 5.7 | 21% | 67% | 91% | 3,980 KB | 550 (+2) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D F A | 9,791 | 12,980 | 19.3 | 15% | 0% | 98% | 222 KB | 5 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | D F B | 9,591 | 8,855 | 7.3 | 44% | 0% | 92% | 27 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | D D B | 9,545 | 1,169,623 | 44.3 | 64% | 0% | 82% | 416 KB | 9 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | D E D | 9,433 | 17,777 | 29.6 | 79% | 11% | 97% | 599 KB | 22 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D E B | 9,394 | 20,684 | 18.5 | 55% | 46% | 82% | 141 KB | 5 (+0) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | D E D | 9,314 | 41,140 | 0.0 | 61% | 0% | 30% | 158 KB | 116 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 9,085 | 10,371 | 22.7 | 63% | 0% | 97% | 1,137 KB | 8 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | D F E | 8,905 | 42,694 | 58.7 | 4% | 0% | 68% | 3,975 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | D F D | 8,810 | 25,796 | 0.1 | 27% | 9% | 47% | 1,271 KB | 440 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | D E D | 8,754 | 16,187 | 0.0 | 65% | 0% | – | 373 KB | 0 (+0) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | D F D | 8,560 | 17,875 | 0.4 | 25% | 17% | – | 452 KB | 1 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | D F B | 8,312 | 35,010 | 16.8 | 32% | 0% | 99% | 252 KB | 2 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | D E C | 8,193 | 14,055 | 0.0 | 46% | 26% | 56% | 286 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | D B A | 8,167 | 9,554 | 40.6 | 83% | 2% | 100% | 130 KB | 1 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D F C | 7,986 | 14,818 | 0.6 | 33% | 22% | 69% | 307 KB | 2 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | D E D | 7,978 | 192,605 | 0.0 | 81% | 0% | 0% | 3,286 KB | 1 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | D F B | 7,960 | 59,375 | 11.0 | 35% | 11% | 90% | 532 KB | 19 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | D F B | 7,894 | 12,238 | 41.5 | 64% | 1% | 100% | 100 KB | 3 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D E A | 7,821 | 8,622 | 29.0 | 49% | 40% | 94% | 102 KB | 233 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | D E D | 7,739 | 13,995 | 14.0 | 67% | 12% | 40% | 7,014 KB | 19 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | D F B | 7,653 | 13,100 | 11.6 | 58% | 0% | 91% | 89 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | D F B | 7,528 | 13,233 | 9.1 | 10% | 0% | 73% | 296 KB | 339 (+1) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D F B | 7,520 | 9,772 | 27.9 | 41% | 28% | 100% | 1,631 KB | 3 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | D E B | 7,349 | 91,393 | 85.1 | 52% | 5% | 96% | 614 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | D F B | 7,224 | 16,462 | 50.0 | 0% | 48% | 98% | 59 KB | 0 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | D F B | 7,216 | 24,982 | 6.0 | 28% | 0% | 91% | 569 KB | 6 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | D B B | 7,171 | 13,028 | 14.7 | 80% | 40% | 96% | 388 KB | 2 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | D E D | 7,122 | 12,206 | 12.6 | 55% | 6% | 0% | 333 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D E D | 6,792 | 16,262 | 10.4 | 45% | 38% | – | 540 KB | 2 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D E D | 6,760 | 34,570 | 0.0 | 56% | 0% | – | 883 KB | 0 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D F B | 6,615 | 12,822 | 41.1 | 14% | 40% | 100% | 1,351 KB | 8 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D E B | 6,589 | 8,430 | 16.9 | 64% | 0% | 99% | 583 KB | 1 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | D D C | 6,516 | 20,858 | 0.0 | 62% | 18% | 50% | 560 KB | 1 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D F B | 6,508 | 11,256 | 27.9 | 57% | 3% | 81% | 324 KB | 160 (+1) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | D F C | 6,344 | 14,125 | 47.6 | 62% | 2% | 100% | 154 KB | 2 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | D F B | 6,102 | 5,031 | 19.5 | 30% | 0% | 92% | 452 KB | 0 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 6,075 | 8,703 | 19.2 | 0% | 20% | 100% | 544 KB | 0 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | D D B | 6,032 | 15,427 | 0.0 | 60% | 22% | 96% | 590 KB | 1 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F B | 5,900 | 8,091 | 17.0 | 53% | 25% | 84% | 382 KB | 7 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | D E C | 5,895 | 5,936 | 29.8 | 44% | 27% | 98% | 739 KB | 0 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 5,845 | 93,956 | 12.4 | 19% | 4% | – | 93 KB | 2 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | D F C | 5,838 | 8,807 | 7.1 | 35% | 29% | 93% | 413 KB | 0 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | D E B | 5,707 | 20,782 | 10.5 | 56% | 29% | 80% | 27 KB | 0 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 5,671 | 11,085 | 14.3 | 0% | 0% | 91% | 781 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D F C | 5,447 | 7,387 | 0.1 | 48% | 15% | 86% | 1,019 KB | 2 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D C A | 5,433 | 17,340 | 12.0 | 70% | 9% | 99% | 259 KB | 0 (+0) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | D F B | 5,242 | 5,260 | 0.1 | 66% | 0% | 74% | 376 KB | 1 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D F D | 5,232 | 13,536 | 0.0 | 76% | 0% | – | 200 KB | 29 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | D F B | 5,171 | 15,547 | 21.1 | 36% | 63% | 84% | 79 KB | 10 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | D E C | 5,091 | 9,892 | 76.0 | 59% | 14% | 90% | 549 KB | 2 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | E F B | 4,999 | 15,225 | 21.2 | 25% | 0% | 100% | 535 KB | 83 (+1) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 4,905 | 7,357 | 14.0 | 49% | 22% | 100% | 435 KB | 12 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | E F D | 4,861 | 10,784 | 51.9 | 10% | 3% | 84% | 20,146 KB | 1 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E F D | 4,855 | 12,700 | 0.0 | 20% | 0% | 0% | 601 KB | 1 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 4,743 | 16,099 | 16.4 | 19% | 13% | 100% | 386 KB | 2 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | E E B | 4,707 | 17,104 | 27.1 | 53% | 0% | 81% | 59 KB | 1 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | E C B | 4,703 | 100,303 | 39.9 | 71% | 8% | 74% | 1,431 KB | 0 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E D D | 4,666 | 7,314 | 50.7 | 68% | 2% | – | 413 KB | 3 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 4,608 | 5,119 | 3.3 | 62% | 0% | 100% | 203 KB | 7 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E F B | 4,597 | 24,125 | 36.4 | 65% | 8% | 100% | 2,222 KB | 5 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | E F B | 4,336 | 6,123 | 27.4 | 35% | 12% | 100% | 208 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | E F B | 4,323 | 5,872 | 24.1 | 13% | 11% | 96% | 160 KB | 10 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | E F B | 4,202 | 9,426 | 0.0 | 8% | 7% | 92% | 674 KB | 2 (+1) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | E F B | 4,194 | 8,541 | 23.4 | 7% | 5% | 100% | 852 KB | 0 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | E D A | 4,131 | 165,391 | 45.7 | 62% | 31% | 99% | 158 KB | 0 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E D A | 4,086 | 7,102 | 28.0 | 63% | 6% | 100% | 156 KB | 6 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E E C | 4,060 | 8,224 | 14.3 | 71% | 8% | 99% | 162 KB | 1 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 4,050 | 6,043 | 7.7 | 18% | 0% | 92% | 704 KB | 0 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | E F C | 4,002 | 7,519 | 44.2 | 40% | 32% | 100% | 588 KB | 5 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | E E C | 3,999 | 90,522 | 35.7 | 72% | 2% | 99% | 378 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E E C | 3,935 | 7,338 | 28.9 | 50% | 12% | 100% | 386 KB | 17 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 3,923 | 5,854 | 12.3 | 48% | 0% | 98% | 146 KB | 0 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | E F B | 3,798 | 8,196 | 27.6 | 42% | 0% | 98% | 571 KB | 37 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | E F D | 3,796 | 11,624 | 0.0 | 22% | 10% | 0% | 301 KB | 0 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | E F D | 3,709 | 4,497 | 0.9 | 78% | 31% | 0% | 184 KB | 0 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | E F A | 3,704 | 4,150 | 20.8 | 56% | 0% | 96% | 95 KB | 1 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | E F C | 3,637 | 12,366 | 25.9 | 20% | 0% | 67% | 175 KB | 0 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 3,580 | 6,666 | 19.8 | 0% | 0% | 78% | 284 KB | 2 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | E F C | 3,526 | 3,681 | 0.1 | 34% | 0% | 100% | 472 KB | 0 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E D C | 3,491 | 17,085 | 0.0 | 63% | 75% | 100% | 888 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | E F C | 3,485 | 8,487 | 15.0 | 30% | 32% | 99% | 165 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 3,405 | 6,957 | 7.4 | 38% | 7% | 92% | 544 KB | 11 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 3,397 | 4,794 | 0.0 | 29% | 0% | 33% | 402 KB | 465 (+1) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 3,374 | 9,580 | 0.0 | 54% | 4% | 0% | 1,216 KB | 0 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | E F A | 3,288 | 6,889 | 57.2 | 42% | 0% | 96% | 136 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | E F C | 3,123 | 8,812 | 9.7 | 33% | 0% | 95% | 105 KB | 2 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | E E B | 3,053 | 4,308 | 38.7 | 72% | 17% | 100% | 353 KB | 2 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | E E C | 3,013 | 6,103 | 34.0 | 57% | 15% | 96% | 512 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | E F C | 2,960 | 9,015 | 23.6 | 64% | 0% | 100% | 25 KB | 17 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F C | 2,956 | 22,702 | 25.5 | 16% | 0% | 54% | 4,722 KB | 96 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | E F D | 2,919 | 4,876 | 9.2 | 28% | 0% | 0% | 285 KB | 25 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | E C B | 2,890 | 12,044 | 33.4 | 78% | 56% | 97% | 32 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | E F B | 2,756 | 8,899 | 5.4 | 16% | 0% | 86% | 262 KB | 1,251 (+1) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 2,731 | 4,886 | 40.4 | 0% | 0% | 88% | 67 KB | 62 (-1) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | E E B | 2,727 | 7,731 | 9.0 | 67% | 0% | 99% | 88 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | E F A | 2,700 | 4,268 | 19.1 | 24% | 0% | 100% | 160 KB | 2 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | E E C | 2,686 | 13,246 | 20.5 | 57% | 0% | 99% | 187 KB | 0 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,620 | 15,216 | 15.6 | 21% | 37% | 92% | 383 KB | 2 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 2,529 | 3,417 | 17.5 | 23% | 0% | 99% | 142 KB | 1 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | E F B | 2,525 | 9,378 | 0.0 | 16% | 17% | 97% | 465 KB | 0 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E F D | 2,508 | 4,925 | 40.2 | 44% | 15% | – | 211 KB | 3 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | E F C | 2,481 | 5,337 | 34.4 | 47% | 0% | 97% | 270 KB | 0 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | E F B | 2,434 | 9,705 | 10.9 | 22% | 0% | 96% | 721 KB | 9 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | E F D | 2,391 | 19,169 | 45.7 | 42% | 20% | – | 440 KB | 1 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | E F A | 2,333 | 11,854 | 20.8 | 38% | 0% | 99% | 399 KB | 0 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F E | 2,317 | 17,324 | 0.2 | 45% | 0% | 88% | 1,483 KB | 1,114 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 2,288 | 2,950 | 8.2 | 44% | 22% | 100% | 350 KB | 0 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 2,269 | 5,888 | 0.0 | 50% | 13% | 0% | 474 KB | 4 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | E E B | 2,257 | 8,967 | 28.3 | 59% | 38% | 100% | 248 KB | 1 (+0) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 2,229 | 5,257 | 23.0 | 23% | 6% | 98% | 1,116 KB | 1 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E F B | 2,205 | 6,869 | 21.5 | 27% | 0% | 99% | 159 KB | 0 (+0) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 2,145 | 5,950 | 0.0 | 72% | 0% | 94% | 224 KB | 0 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 2,109 | 4,590 | 24.3 | 48% | 0% | 92% | 976 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E F D | 2,099 | 4,340 | 16.2 | 34% | 38% | – | 50 KB | 3 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 2,040 | 2,425 | 11.0 | 0% | 0% | – | 567 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 2,017 | 9,658 | 13.0 | 29% | 0% | 100% | 1,076 KB | 0 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | E F B | 2,000 | 5,538 | 4.3 | 35% | 0% | 97% | 43 KB | 0 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E B B | 1,988 | 3,878 | 34.3 | 80% | 55% | 86% | 986 KB | 114 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | E F B | 1,946 | 9,490 | 23.3 | 3% | 0% | 84% | 2,625 KB | 40 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E F D | 1,944 | 7,967 | 1.3 | 10% | 22% | 76% | 66 KB | 1 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | E F A | 1,902 | 4,119 | 13.8 | 52% | 0% | 97% | 61 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 1,897 | 5,904 | 17.6 | 41% | 17% | 76% | 1,585 KB | 6 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E F D | 1,879 | 4,793 | 0.0 | 46% | 0% | 42% | 267 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E F C | 1,823 | 12,901 | 13.5 | 45% | 10% | 94% | 352 KB | 23 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | E F A | 1,819 | 10,198 | 32.0 | 73% | 0% | 99% | 49 KB | 23,795 (+3) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,818 | 13,851 | 26.2 | 10% | 27% | 92% | 363 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 1,804 | 2,594 | 13.1 | 31% | 36% | 74% | 271 KB | 1 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | E F B | 1,798 | 4,893 | 12.1 | 12% | 0% | 96% | 658 KB | 2 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | E F B | 1,791 | 455,550 | 27.5 | 63% | 10% | 88% | 1,414 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 1,773 | 3,636 | 14.2 | 16% | 36% | 94% | 337 KB | 166 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,773 | 2,434 | 13.3 | 27% | 0% | 75% | 634 KB | 4 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | E E B | 1,758 | 11,493 | 22.9 | 41% | 16% | 86% | 92 KB | 0 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,746 | 5,854 | 19.2 | 0% | 31% | 96% | 284 KB | 1 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | E F C | 1,656 | 20,849 | 6.9 | 15% | 26% | 96% | 697 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | E F B | 1,638 | 20,129 | 2.9 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | E F D | 1,501 | 12,501 | 0.0 | 39% | 0% | 30% | 308 KB | 480 (+16) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | E F B | 1,495 | 3,411 | 18.5 | 48% | 0% | 99% | 504 KB | 0 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E F A | 1,432 | 9,206 | 13.9 | 53% | 0% | 95% | 236 KB | 5 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E F C | 1,431 | 8,104 | 1.8 | 57% | 0% | 91% | 5,602 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | E F C | 1,420 | 4,558 | 3.6 | 0% | 0% | 100% | 1,141 KB | 5 (+0) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E F C | 1,412 | 1,930 | 26.7 | 16% | 0% | 73% | 193 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 1,412 | 1,510 | 14.7 | 34% | 30% | 99% | 452 KB | 12 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | E F A | 1,398 | 26,559 | 34.3 | 59% | 0% | 98% | 240 KB | 9 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,346 | 5,859 | 22.0 | 29% | 26% | 97% | 100 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 1,328 | 2,572 | 12.6 | 34% | 34% | 100% | 4,314 KB | 28 (+1) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 1,318 | 3,243 | 14.8 | 47% | 0% | 99% | 127 KB | 23 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | E F C | 1,291 | 7,771 | 3.4 | 51% | 0% | 90% | 319 KB | 1 (+0) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | E F B | 1,283 | 2,248 | 13.1 | 33% | 6% | 97% | 474 KB | 3 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | E F C | 1,272 | 1,708 | 33.0 | 50% | 0% | 100% | 403 KB | 2 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E F C | 1,197 | 20,011 | 14.4 | 28% | 49% | 100% | 231 KB | 1 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | E F B | 1,150 | 7,438 | 38.5 | 69% | 0% | 98% | 203 KB | 1 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 1,111 | 3,631 | 6.2 | 76% | 0% | 99% | 132 KB | 240 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | E F C | 1,064 | 6,494 | 13.0 | 53% | 0% | 96% | 99 KB | 1 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,050 | 4,345 | 0.0 | 49% | 0% | – | 847 KB | 2 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 1,014 | 2,265 | 33.8 | 45% | 0% | 99% | 107 KB | 4 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | F F F | 951 | 91,775 | 0.0 | 44% | 0% | – | 8,190 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 944 | 1,323 | 57.3 | 44% | 0% | 99% | 695 KB | 14 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | F F A | 935 | 11,250 | 61.3 | 28% | 0% | 99% | 169 KB | 2 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 847 | 3,378 | 27.8 | 18% | 0% | 99% | 527 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 730 | 10,298 | 9.1 | 10% | 0% | 98% | 45 KB | 0 (+0) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | F F C | 685 | 8,124 | 29.0 | 54% | 16% | 99% | 530 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 642 | 12,556 | 0.0 | 36% | 0% | 94% | 554 KB | 29 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | 624 | 3,103 | 0.4 | 13% | 0% | 0% | 518 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F E C | 620 | 1,556 | 13.9 | 46% | 0% | 98% | 443 KB | 1 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F B | 607 | 2,378 | 11.9 | 81% | 0% | 98% | 5,242 KB | 40,482 (+29) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | 593 | 821 | 7.3 | 48% | 0% | 80% | 83 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 567 | 1,113 | 0.0 | 58% | 15% | 0% | 664 KB | 3 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 551 | 6,982 | 20.7 | 47% | 0% | 82% | 1,170 KB | 0 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | F F A | 523 | 23,133 | 59.6 | 0% | 0% | 93% | 241 KB | 124 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F E D | 487 | 927 | 0.0 | 58% | 17% | 0% | 324 KB | 0 (+0) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 456 | 1,010 | 29.3 | 48% | 0% | 100% | 1,060 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 443 | 2,279 | 5.3 | 5% | 0% | 90% | 3,845 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 427 | 6,170 | 17.8 | 36% | 0% | 99% | 632 KB | 11 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | 413 | 3,887 | 20.4 | 0% | 0% | 100% | 41 KB | 3 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 378 | 940 | 0.0 | 31% | 0% | 99% | 444 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | F F B | 310 | 2,464 | 11.1 | 0% | 0% | 95% | 104 KB | 2 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | F F B | 278 | 2,720 | 18.6 | 50% | 0% | 81% | 518 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | F F C | 270 | 1,026 | 10.2 | 62% | 0% | 61% | 6,579 KB | 8 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 248 | 40,643 | 5.0 | 0% | 0% | 86% | 149 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 240 | 2,320 | 4.4 | 39% | 0% | 14% | 115 KB | 0 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | F F A | 231 | 3,387 | 24.6 | 0% | 0% | 98% | 377 KB | 49 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 225 | 2,650 | 27.5 | 0% | 0% | 97% | 122 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 214 | 411 | 2.5 | 19% | 0% | 88% | 151 KB | 345 (+0) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | 141 | 1,227 | 0.9 | 44% | 0% | – | 53 KB | 0 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | F F C | 124 | 1,392 | 1.5 | 22% | 0% | 81% | 52 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | F F B | 114 | 1,363 | 0.1 | 0% | 0% | 77% | 152 KB | 29 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 92 | 398 | 7.4 | 0% | 0% | 98% | 99 KB | 4 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | 65 | 82,964 | 4.4 | 34% | 0% | 95% | 163 KB | 13 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 49 | 1,060 | 0.0 | 50% | 0% | – | 202 KB | 4 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 35 | 335 | 0.0 | 10% | 0% | 99% | 509 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 32 | 3,742 | 14.7 | 20% | 0% | 96% | 66 KB | 3 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 20 | 1,246 | 6.7 | 44% | 0% | 100% | 525 KB | 1 (+0) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | F F C | 9 | 277 | 9.1 | 0% | 0% | 100% | 72 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 4 | 1,043 | 6.3 | 0% | 0% | 92% | 159 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 1 | 133 | 12.0 | 0% | 0% | 83% | 15 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | 0 | 0 | 41.9 | 0% | 0% | 53% | 3,052 KB | 2 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 36.6 | 45% | 51% | 89% | 2,242 KB | 1,474 (+4) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | 0 | 2,104 | 26.7 | 0% | 0% | 99% | 884 KB | 5 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 23.9 | 12% | 0% | 100% | 342 KB | 4 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F C | 0 | 2,135 | 23.7 | 15% | 0% | 58% | 100 KB | 0 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | F F B | – | – | 22.3 | – | – | 98% | 231 KB | 1 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | F F C | – | – | 21.4 | – | – | 98% | 363 KB | 1 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F E B | – | – | 19.9 | 56% | 33% | 100% | 990 KB | 4 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | – | – | 17.4 | – | – | 97% | 94 KB | 16 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | 0 | 109 | 16.6 | 0% | 0% | 100% | 88 KB | 0 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 11 | 16.4 | 0% | 0% | 91% | 306 KB | 7 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | 0 | 946 | 16.0 | 0% | 0% | 74% | 332 KB | 1 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F F B | – | – | 15.0 | 70% | 0% | 91% | 86 KB | 6 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 85 | 13.7 | 0% | 0% | 96% | 32 KB | 1 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | F F E | 0 | 0 | 13.4 | – | – | 93% | 576 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 89 | 12.4 | 0% | 0% | 99% | 49 KB | 0 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | 0 | 297 | 12.3 | 0% | 0% | 95% | 8,119 KB | 1 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | F F B | 0 | 6,345 | 12.2 | 26% | 0% | 100% | 617 KB | 1 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 11.8 | – | – | 98% | 43 KB | 1 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | 0 | 0 | 11.5 | 0% | 0% | 88% | 700 KB | 4 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 46 | 11.3 | 0% | 0% | – | 55 KB | 0 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F E D | – | – | 11.1 | 49% | 0% | 0% | 206 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | 0 | 2,156 | 10.6 | 34% | 0% | 99% | 80 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | F F D | 0 | 1,898 | 10.5 | 0% | 0% | – | 414 KB | 0 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 534 | 9.9 | 0% | 0% | 97% | 56 KB | 1 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 569 | 9.9 | 0% | 0% | 93% | 41 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 0 | 9.2 | – | – | 98% | 489 KB | 57 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | – | – | 8.2 | – | – | 80% | 552 KB | 2 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F D | 0 | 3,591 | 8.1 | 0% | 0% | – | 100 KB | 0 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | F F A | 0 | 0 | 7.6 | – | – | 96% | 122 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 0 | 147 | 7.5 | 0% | 0% | 100% | 847 KB | 3 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 319 | 6.8 | 50% | 0% | 100% | 153 KB | 2 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 6.5 | – | – | 98% | 723 KB | 6 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | F F B | 0 | 946 | 6.3 | 0% | 0% | 96% | 804 KB | 2 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | – | – | 5.5 | – | – | 99% | 298 KB | 5 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F F B | 0 | 421 | 5.0 | 0% | 0% | 75% | 161 KB | 2 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 4.9 | – | – | 98% | 149 KB | 0 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F E | 0 | 0 | 4.6 | – | – | 98% | – | 0 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | – | – | 4.4 | – | – | – | 115 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | F F C | – | – | 4.3 | – | – | 90% | 195 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F C D | – | – | 4.0 | 74% | 100% | 0% | 758 KB | 461 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | F F C | 0 | 987,902 | 3.9 | 0% | 0% | 85% | 23 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 0 | 3.8 | – | – | 98% | 42 KB | 0 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 0 | 0 | 3.0 | – | – | 98% | 73 KB | 4 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | F F A | 0 | 0 | 2.9 | 0% | 0% | 100% | 258 KB | 0 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F D | 0 | 12 | 1.3 | 0% | 0% | – | 311 KB | 4 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | – | – | 1.3 | – | – | 69% | 290 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | 0 | 175 | 0.9 | 0% | 0% | 20% | 149 KB | 0 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F F A | – | – | 0.8 | – | – | 100% | 59 KB | 1 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.2 | 58% | 0% | 97% | 825 KB | 6 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F E E | – | – | 0.2 | 76% | 0% | 96% | 34,213 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 19 | 0.1 | 0% | 0% | 16% | 904 KB | 1,308 (+1) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.1 | 54% | 18% | 59% | 84 KB | 5 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | – | – | 0.1 | – | – | – | 92 KB | 0 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | F F E | 0 | 389 | 0.0 | 0% | 0% | 100% | 478 KB | 6 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 0 | 0 | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F F D | – | – | 0.0 | – | – | – | 1,157 KB | 2 (+0) |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | – | – | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 0 | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | F F D | – | – | 0.0 | – | – | – | 3,234 KB | 0 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | F F B | 0 | 3,382 | 0.0 | 0% | 0% | 80% | 446 KB | 3 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 117 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 0 | 1,849 | 0.0 | 8% | 0% | – | 159 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 99 | 0.0 | 0% | 0% | – | 66 KB | 1 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 0 | 873 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [tidepool-heavy-industries/tidepool](https://github.com/tidepool-heavy-industries/tidepool) | F F D | – | – | 0.0 | – | – | 100% | 1,234 KB | 12 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | – | – | 0.0 | – | – | – | 18 KB | 1 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | 0 | 164,352 | 0.0 | 0% | 0% | – | 110 KB | 0 (+0) |
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
