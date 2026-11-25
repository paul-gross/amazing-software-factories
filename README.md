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
_343 repos, last measured 2026-11-25. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (343)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | A E A | 95,460 | 112,716 | 86.9 | 56% | 25% | 92% | 405 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | A C A | 71,140 | 100,410 | 24.2 | 78% | 60% | 92% | 225 KB | 8 (+0) |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | A E C | 64,042 | 106,570 | 223 | 57% | 29% | 100% | 2,294 KB | 5 (+0) |
| [daintreehq/daintree](https://github.com/daintreehq/daintree) | A D A | 63,465 | 76,693 | 63.6 | 67% | 3% | 94% | 430 KB | 89 (+1) |
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 60,831 | 77,603 | 39.1 | 25% | 20% | 88% | 4,386 KB | 2,137 (+4) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | A D B | 45,551 | 51,954 | 0.2 | 60% | 21% | 97% | 140 KB | 81 (+14) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | A C C | 43,519 | 191,126 | 157 | 86% | 22% | 55% | 316 KB | 4 (+0) |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | B C C | 39,145 | 134,200 | 66.1 | 78% | 50% | 61% | 1,742 KB | 4 (+0) |
| [Synapsium-Labs/ccrc-pwa](https://github.com/Synapsium-Labs/ccrc-pwa) | B B B | 36,189 | 51,738 | 42.4 | 84% | 61% | 100% | 895 KB | 5 (+0) |
| [ticoteam/tico](https://github.com/ticoteam/tico) | B C B | 32,283 | 89,435 | 96.6 | 76% | 37% | 98% | 564 KB | 1 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B F B | 31,040 | 38,560 | 22.5 | 49% | 53% | 96% | 2,038 KB | 157 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B E B | 30,578 | 41,613 | 65.0 | 76% | 0% | 91% | 334 KB | 2 (+0) |
| [hornjason/pai-harness](https://github.com/hornjason/pai-harness) | B F B | 30,140 | 39,726 | 28.2 | 39% | 5% | 97% | 597 KB | 0 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | B D D | 27,688 | 43,693 | 0.0 | 68% | 27% | – | 1,008 KB | 2 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | B D D | 27,437 | 116,913 | 14.7 | 69% | 49% | 6% | 246 KB | 4 (+0) |
| [bllshttng/fno](https://github.com/bllshttng/fno) | B D C | 26,047 | 37,585 | 41.7 | 66% | 38% | 96% | 546 KB | 2 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | B F B | 25,495 | 35,555 | 89.1 | 8% | 49% | 87% | 130 KB | 75 (+1) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | B C D | 25,283 | 1,540,611 | 0.0 | 78% | 23% | 0% | 3,286 KB | 0 (+0) |
| [rrnewton/agent-utils](https://github.com/rrnewton/agent-utils) | B C D | 25,005 | 34,305 | 0.0 | 78% | 40% | 0% | 4,328 KB | 3 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | B C B | 24,611 | 28,507 | 19.2 | 80% | 0% | 92% | 297 KB | 7 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B D C | 23,624 | 33,866 | 139 | 62% | 28% | 100% | 5,251 KB | 0 (+0) |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,596 | 27,897 | 44.1 | 77% | 40% | 97% | 552 KB | 2 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | B D D | 22,262 | 49,557 | 0.0 | 62% | 46% | 28% | 308 KB | 850 (-1) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 21,905 | 49,365 | 0.0 | 48% | 60% | – | 575 KB | 2 (+0) |
| [alexec/Agents](https://github.com/alexec/Agents) | B E D | 21,849 | 36,813 | 64.4 | 50% | 54% | 81% | 20,146 KB | 1 (+0) |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | B F C | 20,430 | 29,396 | 0.0 | 31% | 60% | 82% | 20,387 KB | 2 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | B E C | 20,322 | 73,258 | 19.2 | 57% | 9% | 69% | 318 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | B D D | 20,306 | 42,483 | 25.1 | 67% | 49% | 13% | 112 KB | 234 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | C B C | 19,552 | 38,970 | 19.6 | 85% | 34% | 90% | 363 KB | 11 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C B D | 18,738 | 19,738 | 0.0 | 84% | 37% | – | 203 KB | 0 (+0) |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | C F B | 18,466 | 21,649 | 52.4 | 31% | 49% | 78% | 158 KB | 1 (+0) |
| [hivecommons/hive](https://github.com/hivecommons/hive) | C F B | 18,424 | 43,801 | 101 | 26% | 7% | 84% | 6,147 KB | 90 (+1) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | C E C | 18,037 | 22,653 | 24.3 | 59% | 44% | 100% | 615 KB | 22 (+0) |
| [vantt/forgent](https://github.com/vantt/forgent) | C F D | 17,057 | 104,272 | 0.1 | 42% | 0% | 6% | 255 KB | 0 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | C F A | 16,437 | 20,399 | 157 | 22% | 0% | 99% | 281 KB | 24 (+0) |
| [xianxu/ariadne](https://github.com/xianxu/ariadne) | C B D | 16,324 | 43,706 | 0.0 | 86% | 66% | – | 102 KB | 0 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | C C B | 15,802 | 21,591 | 40.9 | 70% | 47% | 99% | 1,036 KB | 0 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | C F B | 15,615 | 26,136 | 40.0 | 32% | 29% | 100% | 605 KB | 0 (+0) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | C D B | 15,586 | 22,073 | 37.4 | 66% | 46% | 97% | 655 KB | 1 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 15,542 | 51,058 | 59.7 | 48% | 49% | 98% | 505 KB | 6,752 (+5) |
| [arul28/ADE](https://github.com/arul28/ADE) | C E C | 15,019 | 33,437 | 17.0 | 67% | 8% | 95% | 8,727 KB | 147 (+1) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | C E C | 14,808 | 62,016 | 30.6 | 45% | 12% | 62% | 65 KB | 3 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | C E B | 14,441 | 30,313 | 17.9 | 59% | 12% | 99% | 834 KB | 53 (+2) |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C E C | 14,111 | 17,183 | 0.0 | 52% | 17% | 55% | 397 KB | 0 (+0) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 13,679 | 18,988 | 19.1 | 77% | 44% | 100% | 229 KB | 37 (+1) |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [SocialGouv/iterion](https://github.com/SocialGouv/iterion) | C F B | 13,047 | 30,974 | 7.4 | 32% | 47% | 86% | 629 KB | 19 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C B A | 12,909 | 217,522 | 61.1 | 90% | 42% | 100% | 158 KB | 0 (+0) |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 12,788 | 22,761 | 22.9 | 31% | 41% | 100% | 514 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | C C B | 12,531 | 18,103 | 24.5 | 84% | 0% | 88% | 597 KB | 7 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | C C C | 12,092 | 14,225 | 32.4 | 73% | 29% | 100% | 473 KB | 10 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | C E B | 11,284 | 42,610 | 19.7 | 87% | 17% | 99% | 1,202 KB | 42 (+0) |
| [subgentic/coral](https://github.com/subgentic/coral) | C D B | 11,273 | 13,940 | 0.0 | 64% | 40% | 87% | 264 KB | 136 (+1) |
| [schiste/Aethyme](https://github.com/schiste/Aethyme) | C E C | 11,047 | 24,663 | 26.8 | 45% | 24% | 92% | 1,041 KB | 1 (+0) |
| [yeetsoft/hatch](https://github.com/yeetsoft/hatch) | C E B | 11,002 | 41,365 | 31.0 | 41% | 44% | 92% | 357 KB | 1 (+0) |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C C D | 10,792 | 34,640 | 0.0 | 74% | 0% | 49% | 5,368 KB | 451 (+0) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 10,486 | 52,484 | 0.0 | 58% | 23% | 50% | 574 KB | 1 (+0) |
| [JosiahAllard/Agentic-Project_Manager-Kit](https://github.com/JosiahAllard/Agentic-Project_Manager-Kit) | C B D | 10,464 | 18,086 | 0.0 | 84% | 11% | – | 443 KB | 0 |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D C B | 9,832 | 97,446 | 90.2 | 80% | 4% | 96% | 1,570 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | D D C | 9,701 | 11,055 | 32.9 | 62% | 17% | 86% | 3,196 KB | 6 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D F C | 9,648 | 40,290 | 0.0 | 40% | 25% | 100% | 550 KB | 1 (+0) |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | D F B | 9,392 | 18,033 | 39.4 | 28% | 23% | 76% | 1,531 KB | 71,098 (+12) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | D F C | 9,316 | 17,308 | 19.7 | 11% | 0% | 93% | 523 KB | 21 (+0) |
| [platform-q-ai/quecto](https://github.com/platform-q-ai/quecto) | D D C | 9,286 | 14,960 | 9.0 | 68% | 5% | 100% | 49 KB | 3 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | D F B | 9,256 | 11,384 | 6.9 | 11% | 20% | 88% | 751 KB | 9 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | D D C | 9,181 | 14,558 | 0.0 | 68% | 16% | 86% | 376 KB | 2 (+0) |
| [coleam00/Archon](https://github.com/coleam00/Archon) | D F A | 9,175 | 13,284 | 16.0 | 46% | 0% | 99% | 42 KB | 23,995 (+8) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [apiad/aegis](https://github.com/apiad/aegis) | D C B | 9,043 | 10,188 | 10.6 | 78% | 4% | 72% | 343 KB | 22 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | D F D | 8,974 | 19,856 | 0.0 | 0% | 0% | 33% | 1,692 KB | 467 (+2) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | D F B | 8,939 | 18,334 | 42.9 | 9% | 43% | 96% | 237 KB | 7 (+0) |
| [martinambrus/haive](https://github.com/martinambrus/haive) | D C A | 8,884 | 18,774 | 13.7 | 84% | 31% | 94% | 255 KB | 5 (+0) |
| [gbvraju/agk](https://github.com/gbvraju/agk) | D D A | 8,876 | 11,064 | 25.1 | 60% | 18% | 100% | 259 KB | 1 (+0) |
| [Richards-LLC/cassy](https://github.com/Richards-LLC/cassy) | D E C | 8,851 | 15,135 | 5.1 | 57% | 30% | 100% | 2,284 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | D F B | 8,822 | 20,234 | 8.7 | 0% | 49% | 100% | 552 KB | 151 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D F D | 8,337 | 17,316 | 10.0 | 54% | 33% | 44% | 245 KB | 11 (+0) |
| [preloop/preloop](https://github.com/preloop/preloop) | D F B | 8,332 | 18,428 | 10.0 | 19% | 8% | 88% | 577 KB | 96 (+0) |
| [ztrange/veri](https://github.com/ztrange/veri) | D E B | 8,197 | 17,496 | 38.7 | 60% | 26% | 100% | 76 KB | 0 (+0) |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | D C D | 8,140 | 11,135 | 0.0 | 79% | 0% | 4% | 474 KB | 0 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | D C F | 8,002 | 69,010 | 0.0 | 70% | 31% | – | 8,190 KB | 0 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D D B | 7,933 | 10,886 | 0.0 | 69% | 0% | 75% | 4,148 KB | 7 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | D F B | 7,897 | 32,390 | 38.2 | 20% | 31% | 100% | 617 KB | 1 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | D F B | 7,553 | 59,539 | 9.0 | 50% | 22% | 99% | 339 KB | 6 (+0) |
| [alexwaumann/code-foundry](https://github.com/alexwaumann/code-foundry) | D F B | 7,443 | 16,963 | 18.0 | 30% | 0% | 84% | 340 KB | 0 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | D F D | 7,401 | 18,337 | 5.3 | 33% | 17% | 25% | 269 KB | 18 (+2) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 7,385 | 12,485 | 22.2 | 77% | 0% | – | 124 KB | 2 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | D F B | 7,277 | 10,024 | 11.4 | 26% | 9% | 96% | 544 KB | 0 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | D F C | 7,264 | 9,906 | 10.9 | 59% | 0% | 59% | 1,264 KB | 13 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | D E B | 7,235 | 9,240 | 26.0 | 62% | 17% | 100% | 1,937 KB | 3 (+0) |
| [yotamleo-org/Himmel](https://github.com/yotamleo-org/Himmel) | D E C | 7,043 | 19,569 | 8.4 | 41% | 0% | 100% | 4,357 KB | 15 (+0) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | D C A | 6,986 | 12,743 | 61.0 | 74% | 0% | 100% | 59 KB | 1 (+0) |
| [tdduydev/xdev-hive](https://github.com/tdduydev/xdev-hive) | D F B | 6,903 | 84,844 | 21.0 | 1% | 0% | 84% | 213 KB | 0 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | D F C | 6,622 | 9,779 | 24.8 | 38% | 19% | 100% | 368 KB | 18 (+0) |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | D D B | 6,614 | 13,125 | 64.5 | 67% | 31% | 97% | 259 KB | 8 (+0) |
| [crewship-ai/crewship](https://github.com/crewship-ai/crewship) | D C B | 6,444 | 9,354 | 21.4 | 79% | 0% | 100% | 158 KB | 5 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D B B | 6,309 | 8,397 | 16.1 | 83% | 22% | 100% | 151 KB | 0 (+0) |
| [zajca/pohunek](https://github.com/zajca/pohunek) | D D B | 6,019 | 7,472 | 13.5 | 63% | 18% | 98% | 1,160 KB | 9 (+0) |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | D B B | 5,916 | 7,019 | 0.0 | 80% | 44% | 95% | 401 KB | 3 (+0) |
| [VargaFoundation/choregos](https://github.com/VargaFoundation/choregos) | D F B | 5,901 | 24,640 | 27.6 | 33% | 0% | 76% | 270 KB | 0 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D E A | 5,832 | 29,242 | 18.5 | 59% | 0% | 92% | 155 KB | 3 (-1) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | D F D | 5,685 | 32,905 | 0.0 | 69% | 0% | – | 1,147 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 7,216 | 21.0 | 40% | 24% | 59% | 388 KB | 20 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D E B | 5,494 | 18,737 | 0.0 | 47% | 26% | 97% | 715 KB | 0 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | D E D | 5,256 | 10,918 | 0.0 | 60% | 25% | 49% | 1,663 KB | 38 (+0) |
| [ToanMobile/agent-workbench](https://github.com/ToanMobile/agent-workbench) | D E C | 5,189 | 6,734 | 14.8 | 52% | 0% | 88% | 688 KB | 2 (+0) |
| [akiojin/gwt](https://github.com/akiojin/gwt) | E C B | 4,781 | 10,478 | 31.9 | 74% | 25% | 100% | 2,514 KB | 5 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | E F B | 4,780 | 9,823 | 2.3 | 38% | 11% | 74% | 461 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E D C | 4,730 | 13,158 | 0.0 | 64% | 32% | 80% | 5,689 KB | 1 (+0) |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E B D | 4,553 | 6,537 | 81.3 | 80% | 38% | – | 480 KB | 3 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | E F B | 4,551 | 6,606 | 12.0 | 37% | 16% | 87% | 389 KB | 187 (+1) |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | E E C | 4,464 | 7,743 | 0.0 | 57% | 38% | 73% | 138 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | E C D | 4,431 | 8,082 | 66.4 | 82% | 20% | – | 294 KB | 3 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | E F A | 4,336 | 7,746 | 16.5 | 2% | 38% | 98% | 68 KB | 65 (+1) |
| [taskqorg/taskq](https://github.com/taskqorg/taskq) | E C C | 4,306 | 50,938 | 31.0 | 75% | 0% | 95% | 538 KB | 0 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | E C C | 4,300 | 10,365 | 18.1 | 75% | 33% | 91% | 546 KB | 26 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E D B | 4,289 | 9,282 | 19.1 | 65% | 0% | 82% | 94 KB | 4 (+0) |
| [developmentconexus-ops/conexus](https://github.com/developmentconexus-ops/conexus) | E F A | 4,274 | 24,057 | 18.1 | 60% | 0% | 94% | 40 KB | 0 (+0) |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 4,253 | 5,200 | 14.0 | 21% | 19% | 95% | 168 KB | 1 (+0) |
| [l4ci/rota](https://github.com/l4ci/rota) | E F B | 4,233 | 7,039 | 31.4 | 49% | 0% | 100% | 64 KB | 3 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | E F B | 4,218 | 9,614 | 5.3 | 24% | 0% | 82% | 201 KB | 2 (+0) |
| [diy-agent/diy](https://github.com/diy-agent/diy) | E F C | 3,898 | 6,750 | 6.4 | 4% | 19% | 93% | 378 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 3,544 | 7,683 | 5.7 | 23% | 0% | 95% | 102 KB | 1 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F C | 3,507 | 6,553 | 0.0 | 4% | 0% | 89% | 195 KB | 102 (-2) |
| [SimulatorLife/AutoDev](https://github.com/SimulatorLife/AutoDev) | E F D | 3,468 | 8,188 | 0.5 | 8% | 15% | 10% | 285 KB | 1 (+0) |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | E F B | 3,452 | 28,812 | 15.2 | 38% | 10% | 98% | 1,129 KB | 49 (+0) |
| [quadseven/loom](https://github.com/quadseven/loom) | E E C | 3,404 | 4,333 | 22.7 | 55% | 12% | 96% | 983 KB | 0 (+0) |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | E F B | 3,400 | 7,695 | 4.8 | 40% | 0% | 100% | 1,536 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | E F C | 3,342 | 12,600 | 2.6 | 23% | 0% | 67% | 685 KB | 351 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | E F B | 3,243 | 4,721 | 6.2 | 52% | 15% | 97% | 102 KB | 260 (+0) |
| [qiangli/yoke](https://github.com/qiangli/yoke) | E F D | 3,235 | 5,519 | 0.1 | 25% | 10% | 0% | 606 KB | 1 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | E F C | 3,204 | 6,708 | 1.7 | 12% | 22% | 91% | 4,402 KB | 574 (+2) |
| [GCamposGit/DarkFactory](https://github.com/GCamposGit/DarkFactory) | E F B | 3,163 | 5,708 | 6.5 | 58% | 0% | 87% | 1,116 KB | 0 (+0) |
| [cLazyZombie/aaa](https://github.com/cLazyZombie/aaa) | E F C | 3,141 | 10,328 | 0.0 | 49% | 17% | 71% | 141 KB | 0 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | E E C | 2,935 | 3,350 | 14.1 | 59% | 41% | 100% | 252 KB | 1 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | E F C | 2,884 | 7,075 | 2.2 | 33% | 30% | 94% | 1,468 KB | 1,122 (+1) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E F B | 2,866 | 3,948 | 8.9 | 72% | 0% | 100% | 716 KB | 0 (+0) |
| [laceyenterprises/adversarial-review](https://github.com/laceyenterprises/adversarial-review) | E C B | 2,861 | 8,906 | 16.6 | 78% | 20% | 72% | 435 KB | 1 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E F A | 2,660 | 5,427 | 10.2 | 33% | 17% | 100% | 478 KB | 14 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | E E D | 2,643 | 14,023 | 0.0 | 62% | 0% | 42% | 268 KB | 0 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | E F E | 2,613 | 8,689 | 22.2 | 53% | 7% | 76% | 1,792 KB | 6 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | E F C | 2,609 | 7,048 | 16.6 | 34% | 53% | 55% | 540 KB | 12 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 2,543 | 30,935 | 0.1 | 3% | 0% | 45% | 1,312 KB | 0 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,537 | 100,791 | 4.8 | 7% | 0% | 91% | 24 KB | 0 (+0) |
| [keanji-x/neige-calm](https://github.com/keanji-x/neige-calm) | E F B | 2,479 | 4,989 | 8.1 | 17% | 0% | 79% | 312 KB | 1 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | E F B | 2,360 | 4,546 | 4.1 | 70% | 0% | 97% | 552 KB | 12 (+0) |
| [Amit-Roy/agent-console](https://github.com/Amit-Roy/agent-console) | E F B | 2,357 | 11,336 | 9.1 | 66% | 0% | 86% | 680 KB | 1 (+0) |
| [ottojung/viche](https://github.com/ottojung/viche) | E F C | 2,275 | 7,075 | 0.2 | 29% | 0% | 90% | 52 KB | 0 (+0) |
| [zeyxx/CYNIC](https://github.com/zeyxx/CYNIC) | E E C | 2,271 | 3,736 | 1.3 | 41% | 0% | 76% | 83 KB | 1 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | E E A | 2,263 | 3,003 | 5.7 | 63% | 0% | 98% | 236 KB | 6 (+0) |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | E F B | 2,234 | 5,433 | 12.0 | 38% | 0% | 71% | 169 KB | 2 (+0) |
| [ijun17/centralu](https://github.com/ijun17/centralu) | E F C | 2,174 | 5,867 | 16.9 | 14% | 0% | 98% | 628 KB | 1 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | E E B | 2,155 | 12,181 | 0.0 | 56% | 0% | 92% | 590 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | E F B | 2,115 | 7,155 | 7.6 | 66% | 0% | 100% | 4,314 KB | 40 (+0) |
| [yukimemi/magi](https://github.com/yukimemi/magi) | E F C | 1,861 | 2,776 | 7.0 | 29% | 25% | 92% | 1,069 KB | 2 (+0) |
| [mindattic/MindAttic.Orchestrator](https://github.com/mindattic/MindAttic.Orchestrator) | E D C | 1,811 | 11,275 | 0.0 | 66% | 53% | 100% | 2,432 KB | 0 (+0) |
| [stranske/Orchestrator](https://github.com/stranske/Orchestrator) | E F C | 1,810 | 2,116 | 12.2 | 61% | 0% | 100% | 431 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | E F D | 1,789 | 33,186 | 23.4 | 56% | 6% | 50% | 3,082 KB | 110 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | E F B | 1,776 | 2,861 | 8.1 | 47% | 28% | 81% | 151 KB | 0 (+0) |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | E F A | 1,762 | 7,082 | 24.2 | 27% | 0% | 93% | 121 KB | 3 (+0) |
| [TrebuchetDynamics/autowork](https://github.com/TrebuchetDynamics/autowork) | E F D | 1,741 | 10,006 | 0.0 | 17% | 7% | 0% | 535 KB | 1 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | E F C | 1,712 | 7,897 | 22.0 | 16% | 0% | 100% | 602 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | E F D | 1,665 | 7,714 | 0.0 | 0% | 0% | – | 226 KB | 31 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | E F D | 1,649 | 4,309 | 0.0 | 47% | 15% | 0% | 474 KB | 4 (+0) |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | E F A | 1,628 | 20,597 | 21.0 | 21% | 0% | 98% | 363 KB | 0 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E E B | 1,555 | 1,416 | 11.1 | 82% | 18% | 100% | 366 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | E E C | 1,523 | 5,520 | 11.0 | 53% | 10% | 96% | 180 KB | 1 (+0) |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E F B | 1,479 | 1,795 | 25.3 | 59% | 0% | 100% | 1,005 KB | 126 (+2) |
| [megamen32/agent-herder](https://github.com/megamen32/agent-herder) | E E D | 1,475 | 6,114 | 3.6 | 58% | 0% | 0% | 6,837 KB | 1 (+0) |
| [handline-dev/handline](https://github.com/handline-dev/handline) | E F A | 1,434 | 11,329 | 28.2 | 48% | 5% | 99% | 46 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | E F B | 1,420 | 2,696 | 8.4 | 35% | 0% | 99% | 6,579 KB | 9 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | E F B | 1,404 | 2,911 | 18.3 | 37% | 13% | 99% | 258 KB | 3 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | E F B | 1,395 | 3,196 | 13.1 | 0% | 0% | 97% | 644 KB | 14 (+1) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | E F A | 1,389 | 4,486 | 25.8 | 74% | 0% | 100% | 135 KB | 1 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | E F E | 1,378 | 18,080 | 12.0 | 25% | 18% | 100% | 941 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | E F C | 1,371 | 2,472 | 5.1 | 0% | 0% | 91% | 768 KB | 8 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 1,284 | 14,699 | 12.3 | 39% | 0% | 100% | 266 KB | 2 (+0) |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E F C | 1,275 | 1,796 | 7.4 | 35% | 0% | 100% | 107 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | E F B | 1,259 | 4,166 | 7.6 | 44% | 0% | 97% | 53 KB | 2 (+0) |
| [pmark/arcadia](https://github.com/pmark/arcadia) | E F B | 1,223 | 2,535 | 22.6 | 10% | 9% | 96% | 324 KB | 1 (+0) |
| [AnEntrypoint/gm](https://github.com/AnEntrypoint/gm) | E C E | 1,220 | 8,294 | 0.0 | 77% | 0% | 45% | 198 KB | 1 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 1,212 | 11,699 | 7.3 | 52% | 0% | 100% | 1,101 KB | 1 (-1) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F C | 1,206 | 12,532 | 6.4 | 43% | 0% | 100% | 100 KB | 0 (+0) |
| [JacobStephens2/thirdshift](https://github.com/JacobStephens2/thirdshift) | E F B | 1,199 | 2,952 | 17.5 | 26% | 0% | 95% | 644 KB | 3 (+0) |
| [on-par/software-factory](https://github.com/on-par/software-factory) | E F A | 1,168 | 2,033 | 10.3 | 56% | 0% | 100% | 161 KB | 7 (+0) |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | E F B | 1,166 | 7,126 | 46.8 | 9% | 33% | 100% | 1,451 KB | 8 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | E F B | 1,119 | 2,410 | 2.8 | 0% | 0% | 87% | 740 KB | 0 (+0) |
| [gvergnaud/bise](https://github.com/gvergnaud/bise) | E F C | 1,005 | 1,882 | 0.0 | 32% | 0% | 75% | 1,175 KB | 53 (+1) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | F F C | 996 | 3,324 | 18.6 | 53% | 5% | 97% | 393 KB | 1 (+0) |
| [sourabhJainR/AUREN](https://github.com/sourabhJainR/AUREN) | F F B | 967 | 1,338 | 11.4 | 0% | 0% | 99% | 338 KB | 1 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | F F A | 925 | 3,277 | 53.8 | 28% | 0% | 99% | 29 KB | 0 (+0) |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | F F C | 889 | 5,439 | 13.1 | 32% | 0% | 69% | 5,449 KB | 41,048 (+18) |
| [AutoDevJapan/cc-pc-tools-rs](https://github.com/AutoDevJapan/cc-pc-tools-rs) | F F A | 840 | 5,065 | 7.4 | 47% | 0% | 100% | 370 KB | 0 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F E C | 815 | 1,016 | 0.0 | 61% | 8% | 100% | 535 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | F F B | 809 | 2,495 | 8.1 | 23% | 20% | 85% | 275 KB | 1 (+0) |
| [G-Eskayo/marvin](https://github.com/G-Eskayo/marvin) | F F B | 737 | 1,822 | 10.3 | 9% | 0% | 100% | 105 KB | 3 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | F F A | 711 | 5,693 | 16.0 | 56% | 19% | 99% | 262 KB | 9 (+0) |
| [gilcambe/nexia](https://github.com/gilcambe/nexia) | F E C | 655 | 2,720 | 31.1 | 54% | 32% | 100% | 512 KB | 0 (+0) |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | F F B | 652 | 1,324 | 16.0 | 0% | 0% | 97% | 121 KB | 1 (+0) |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | F F D | 618 | 1,988 | 0.0 | 0% | 0% | – | 1,044 KB | 1 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | F F B | 594 | 1,914 | 15.4 | 20% | 0% | 100% | 126 KB | 0 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | F F C | 593 | 1,815 | 23.7 | 48% | 0% | 99% | 705 KB | 13 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F F E | 543 | 43,220 | 19.3 | 33% | 48% | 92% | 154 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | F F C | 430 | 7,278 | 6.9 | 50% | 0% | 98% | 485 KB | 0 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | F F A | 381 | 1,261 | 12.6 | 8% | 14% | 100% | 386 KB | 2 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | F F E | 357 | 7,552 | 10.3 | 54% | 0% | 98% | 635 KB | 11 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | F F B | 310 | 1,911 | 6.5 | 0% | 0% | 96% | 127 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 298 | 3,339 | 0.0 | 9% | 0% | – | 69 KB | 0 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | F F B | 294 | 2,131 | 43.6 | 10% | 0% | 99% | 2,702 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | F F A | 285 | 543 | 41.5 | 0% | 0% | 99% | 340 KB | 1 (+0) |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 273 | 3,794 | 1.2 | 19% | 0% | 82% | 685 KB | 0 (+0) |
| [timerloggedout-spec/termux-monorepo](https://github.com/timerloggedout-spec/termux-monorepo) | F F C | 266 | 262,204 | 103 | 6% | 0% | 90% | 378 KB | 3 (-1) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | F F B | 244 | 895 | 9.4 | 0% | 0% | 90% | 459 KB | 0 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 239 | 1,768 | 3.4 | 0% | 0% | 100% | 173 KB | 0 (+0) |
| [KelpCoin/DreamLedger](https://github.com/KelpCoin/DreamLedger) | F F E | 238 | 1,363 | 3.8 | 11% | 0% | 21% | 115 KB | 0 (+0) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | F F D | 224 | 15,212 | 33.8 | 18% | 0% | 21% | 3,975 KB | 1 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | F F B | 222 | 2,952 | 25.4 | 16% | 0% | 82% | 242 KB | 140 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | F F B | 184 | 1,022 | 14.3 | 0% | 0% | 97% | 637 KB | 2 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 169 | 919 | 11.5 | 0% | 0% | 98% | 885 KB | 3 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F D | 113 | 9,024 | 0.0 | 0% | 0% | 0% | 254 KB | 0 (+0) |
| [0xb1ob/picp](https://github.com/0xb1ob/picp) | F F B | 83 | 1,663 | 10.6 | 62% | 0% | 96% | 95 KB | 0 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | F F B | 55 | 414 | 7.2 | 0% | 0% | 97% | 1,414 KB | 0 (+0) |
| [Gharib89/skills](https://github.com/Gharib89/skills) | F F B | 36 | 1,171 | 5.4 | 0% | 0% | 100% | 45 KB | 0 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | F F B | 35 | 3,627 | 11.9 | 32% | 0% | 97% | 185 KB | 15 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | F F B | 28 | 1,213 | 12.8 | 10% | 0% | 99% | 578 KB | 2 (+0) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | F F B | 17 | 2,511 | 3.2 | 15% | 0% | 95% | 728 KB | 2 (-1) |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 17 | 3,424 | 0.0 | 54% | 0% | 96% | 70 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 15 | 2,553 | 2.4 | 18% | 0% | 88% | 151 KB | 351 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | F F B | 5 | 2,293 | 2.9 | 6% | 0% | 99% | 639 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | F F B | – | – | 53.2 | 65% | 16% | 99% | 982 KB | 12 (+0) |
| [goat-si/goat](https://github.com/goat-si/goat) | F F B | – | – | 45.9 | 72% | 0% | 99% | 3,196 KB | 166 (+1) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | F F C | 0 | 97 | 32.6 | 0% | 0% | 100% | 598 KB | 5 (+0) |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | F F B | 0 | 40 | 32.1 | 50% | 0% | 100% | 178 KB | 0 (+0) |
| [razzant/ouroboros](https://github.com/razzant/ouroboros) | F F B | 0 | 227 | 31.5 | 0% | 0% | 97% | 497 KB | 1,704 (+2) |
| [modu-ai/moai-adk](https://github.com/modu-ai/moai-adk) | F F C | – | – | 30.6 | – | – | 85% | 263 KB | 1,260 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F E B | – | – | 23.0 | 59% | 52% | 81% | 2,290 KB | 1,574 (+4) |
| [zach-source/claude-factory](https://github.com/zach-source/claude-factory) | F F B | – | – | 22.0 | – | – | 99% | 703 KB | 3 (+1) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | F F B | – | – | 20.6 | – | – | 99% | 884 KB | 5 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | F F B | 0 | 289 | 17.5 | 53% | 0% | 99% | 981 KB | 2 (+0) |
| [gustavomhss/hugr-orchestra](https://github.com/gustavomhss/hugr-orchestra) | F F B | – | – | 17.2 | – | – | 100% | 192 KB | 0 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | F F D | 0 | 269 | 17.1 | 0% | 0% | – | 454 KB | 1 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | F F D | 0 | 145 | 16.9 | 0% | 0% | – | 63 KB | 4 (+0) |
| [Sharper-Flow/concord](https://github.com/Sharper-Flow/concord) | F F A | 0 | 1,639 | 16.9 | 24% | 0% | 99% | 308 KB | 2 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | F F C | 0 | 263 | 16.8 | 0% | 0% | 100% | 190 KB | 2 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | F F A | 0 | 1,994 | 16.8 | 0% | 0% | 93% | 315 KB | 159 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | F F D | 0 | 0 | 16.2 | 10% | 0% | 12% | 279 KB | 0 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F F B | – | – | 16.0 | 27% | 24% | 77% | 1,051 KB | 4 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | – | – | 15.2 | – | – | 91% | 306 KB | 8 (+1) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | F F C | – | – | 12.9 | – | – | 100% | 42 KB | 0 (+0) |
| [wecreates/Money-factory](https://github.com/wecreates/Money-factory) | F F B | 0 | 4,025 | 12.4 | 36% | 0% | 74% | 61 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | – | – | 11.6 | – | – | 100% | 703 KB | 0 (+0) |
| [Egoushka/chargehand](https://github.com/Egoushka/chargehand) | F F A | 0 | 1,006 | 10.9 | 0% | 0% | 97% | 74 KB | 1 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F F D | 0 | 469 | 10.2 | 0% | 0% | 0% | 348 KB | 1 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | F F B | – | – | 9.6 | – | – | 88% | 710 KB | 4 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | F F D | 0 | 0 | 9.5 | – | – | 28% | 7,014 KB | 21 (-1) |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | F F B | 0 | 0 | 9.4 | – | – | 100% | 1,060 KB | 0 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | F F B | 0 | 310 | 9.2 | 0% | 0% | 94% | 948 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | – | – | 9.1 | – | – | 98% | 43 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | F F A | 0 | 103 | 8.4 | 0% | 0% | 100% | 269 KB | 0 (+0) |
| [feigi/fleet-plugin](https://github.com/feigi/fleet-plugin) | F F C | 0 | 907 | 8.2 | 27% | 0% | 96% | 215 KB | 1 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F F D | – | – | 7.9 | 24% | 0% | 0% | 206 KB | 0 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | F F C | 0 | 2,727 | 7.8 | 0% | 0% | 100% | 180 KB | 0 (+0) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | F D B | – | – | 7.3 | 61% | 62% | 93% | 86 KB | 7 (+0) |
| [AISquare-Studio/aisquare-cli](https://github.com/AISquare-Studio/aisquare-cli) | F F B | – | – | 6.7 | – | – | 89% | 682 KB | 6 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F D | – | – | 6.5 | 0% | 0% | 100% | 154 KB | 4 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | F F C | 0 | 113 | 6.4 | 0% | 0% | 90% | 577 KB | 2 (+0) |
| [marioatcloudvane/litefactory](https://github.com/marioatcloudvane/litefactory) | F F D | 0 | 0 | 5.9 | – | – | 44% | 144 KB | 16 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | F F C | – | – | 5.8 | – | – | 98% | 165 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | F F C | 0 | 1,132 | 5.5 | 15% | 0% | 97% | 249 KB | 0 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | F F B | – | – | 5.4 | – | – | 79% | 416 KB | 9 (+0) |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,057 | 4.2 | 0% | 0% | – | 201 KB | 0 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | F F B | 0 | 0 | 4.0 | – | – | 89% | 2,640 KB | 48 (+0) |
| [henningfutrell/hopper](https://github.com/henningfutrell/hopper) | F F B | 0 | 377 | 3.9 | 0% | 0% | 84% | 137 KB | 1 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | F F C | 0 | 165 | 3.8 | 0% | 0% | 99% | 271 KB | 0 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | F F B | 0 | 48 | 3.7 | 0% | 0% | 98% | 54 KB | 0 (+0) |
| [myungjoo/HIL-Claw](https://github.com/myungjoo/HIL-Claw) | F F B | 0 | 0 | 3.6 | – | – | 100% | 101 KB | 0 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F B | – | – | 3.5 | – | – | 99% | 87 KB | 0 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | F F A | 0 | 0 | 3.4 | 0% | 0% | 97% | 243 KB | 9 (+0) |
| [repairman29/chump](https://github.com/repairman29/chump) | F F E | 0 | 7,617 | 3.3 | 0% | 0% | 92% | 635 KB | 0 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | F F B | 0 | 0 | 3.2 | – | – | 89% | 489 KB | 89 (+0) |
| [masseater/msa](https://github.com/masseater/msa) | F F C | 0 | 71 | 3.1 | 0% | 0% | 68% | 26 KB | 0 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | F F B | 0 | 692 | 3.1 | 0% | 0% | 83% | 1,423 KB | 1 (+0) |
| [illideristudios/chief-of-stuff](https://github.com/illideristudios/chief-of-stuff) | F F C | – | – | 3.0 | – | – | 96% | 99 KB | 1 (+0) |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | F F B | 0 | 18 | 2.9 | 0% | 0% | 99% | 59 KB | 3 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | F F D | 0 | 1,333 | 2.9 | 0% | 0% | 0% | 286 KB | 25 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | – | – | 2.8 | – | – | 100% | 160 KB | 2 (+0) |
| [benmarte/talos](https://github.com/benmarte/talos) | F F B | 0 | 1,002 | 2.8 | 17% | 0% | 91% | 665 KB | 2 (+0) |
| [rahulnakmol/agentic-ayudha](https://github.com/rahulnakmol/agentic-ayudha) | F F A | – | – | 2.6 | – | – | 99% | 98 KB | 0 (+0) |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | F F C | 0 | 763 | 2.5 | 0% | 0% | 99% | 50 KB | 1 (+0) |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | F F C | 0 | 1,127 | 2.5 | 10% | 0% | 94% | 697 KB | 0 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | F F A | 0 | 50 | 2.3 | 0% | 0% | 100% | 127 KB | 25 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | F F A | 0 | 2,538 | 2.2 | 0% | 0% | 100% | 399 KB | 0 (+0) |
| [sidorenkoalex/artel](https://github.com/sidorenkoalex/artel) | F F B | – | – | 2.2 | – | – | 95% | 385 KB | 0 (-1) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | F F C | – | – | 2.1 | – | – | 100% | 403 KB | 2 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | F F C | 0 | 0 | 2.1 | – | – | 98% | 104 KB | 4 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | F F B | – | – | 2.0 | – | – | 97% | 504 KB | 0 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | – | – | 1.9 | – | – | 98% | 149 KB | 0 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | F F C | 0 | 287 | 1.9 | 0% | 0% | 100% | 25 KB | 19 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | F F D | – | – | 1.8 | – | – | – | 710 KB | 1 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | – | – | 1.7 | – | – | 95% | 66 KB | 3 (+0) |
| [byronxlg/unattended](https://github.com/byronxlg/unattended) | F F B | – | – | 1.4 | – | – | 91% | 43 KB | 0 (+0) |
| [G-ACE-inc/server-core](https://github.com/G-ACE-inc/server-core) | F F C | 0 | 4,667 | 1.4 | 0% | 0% | 74% | 46 KB | 0 (+0) |
| [Userfrom1995/RandomLabs](https://github.com/Userfrom1995/RandomLabs) | F F C | 0 | 229 | 1.4 | 0% | 0% | 91% | 3,845 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 0 | 1,670 | 1.3 | 0% | 0% | 100% | 298 KB | 5 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 0 | 345 | 1.1 | 0% | 0% | 81% | 156 KB | 2 (+0) |
| [frontiermaxxing/Nitely](https://github.com/frontiermaxxing/Nitely) | F F E | – | – | 1.0 | – | – | 75% | 336 KB | 1 (+0) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | F F D | 0 | 1,962 | 0.9 | 36% | 0% | 38% | 279 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F F D | – | – | 0.8 | 16% | 41% | 0% | 1,110 KB | 467 (+0) |
| [marwanvx/dovet](https://github.com/marwanvx/dovet) | F F B | – | – | 0.7 | – | – | 80% | 83 KB | 0 (+0) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 0 | 0 | 0.7 | 0% | 0% | – | 56 KB | 0 (+0) |
| [bwsalmon/silo](https://github.com/bwsalmon/silo) | F F A | 0 | 2,185 | 0.6 | 0% | 0% | 100% | 29 KB | 0 (+0) |
| [cbundy/dev-system](https://github.com/cbundy/dev-system) | F F A | – | – | 0.6 | – | – | 100% | 41 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | F F A | – | – | 0.6 | – | – | 89% | 163 KB | 16 (+1) |
| [codethread/hive](https://github.com/codethread/hive) | F F D | – | – | 0.5 | – | – | – | 53 KB | 0 (+0) |
| [Disesfgewu/multiagentSystem](https://github.com/Disesfgewu/multiagentSystem) | F F B | – | – | 0.5 | – | – | 99% | 80 KB | 0 (+0) |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | F F C | – | – | 0.5 | – | – | 90% | 319 KB | 1 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F F B | – | – | 0.2 | 26% | 74% | 72% | 921 KB | 7 (+0) |
| [alfianisnan26/claudepilot](https://github.com/alfianisnan26/claudepilot) | F F C | 0 | 51 | 0.1 | 0% | 0% | 100% | 472 KB | 0 (+0) |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | F F D | – | – | 0.1 | – | – | 20% | 154 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | F F C | – | – | 0.1 | – | – | 53% | 3,052 KB | 2 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F C | – | – | 0.1 | – | – | 95% | 8,119 KB | 1 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | – | – | 0.1 | – | – | 99% | 73 KB | 3 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | F F D | – | – | 0.1 | – | – | 0% | 518 KB | 0 (+0) |
| [AnEntrypoint/rs-plugkit](https://github.com/AnEntrypoint/rs-plugkit) | F F E | 0 | 0 | 0.0 | 0% | 0% | 99% | 509 KB | 0 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | – | – | 0.0 | – | – | 0% | 110 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | – | – | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | F F B | 0 | 603 | 0.0 | 0% | 0% | 75% | 554 KB | 31 (+0) |
| [fabrig-ai/temper](https://github.com/fabrig-ai/temper) | F F D | 0 | 25,282 | 0.0 | 62% | 0% | – | 209 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | F F D | – | – | 0.0 | – | – | 0% | 342 KB | 0 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | F F D | 0 | 0 | 0.0 | 0% | 0% | – | 320 KB | 0 (+0) |
| [jonathanbranam/bridle](https://github.com/jonathanbranam/bridle) | F F C | 0 | 426 | 0.0 | 0% | 0% | 96% | 269 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | – | – | 0.0 | – | – | – | 159 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | F F D | 0 | 29 | 0.0 | 0% | 0% | 0% | 673 KB | 3 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F E C | – | – | 0.0 | 55% | 54% | 53% | 88 KB | 6 (+1) |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | F F A | 0 | 3,515 | 0.0 | 0% | 0% | 92% | 254 KB | 0 (+0) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F B E | – | – | 0.0 | 88% | 44% | 94% | 45,801 KB | 0 (+0) |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 0 | 59 | 0.0 | 0% | 0% | – | 202 KB | 5 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | F F D | 0 | 2,785 | 0.0 | 0% | 0% | – | 116 KB | 0 (+0) |
| [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin) | F F F | – | – | 0.0 | – | – | – | 110 KB | 0 (-1) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | F F D | 0 | 951 | 0.0 | 0% | 0% | 7% | 158 KB | 124 (+1) |
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
