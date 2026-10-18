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
_268 repos, last measured 2026-10-18. Sorted by code lines on the median day. The [site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._

### Assembly lines (268)

| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization | Main CI green | Largest file | Stars (week) |
|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|
| [GoogleCloudPlatform/scion](https://github.com/GoogleCloudPlatform/scion) | A F B | 86,381 | 114,207 | 69.2 | 33% | 21% | 87% | 3,038 KB | 1,963 (+17) |
| [Apeloff1/Skeleton](https://github.com/Apeloff1/Skeleton) | A F D | 79,533 | 1,182,698 | 71.1 | 41% | 0% | 97% | 3,975 KB | 1 (+0) |
| [purlis/purlis](https://github.com/purlis/purlis) | A C B | 62,305 | 75,386 | 28.2 | 72% | 24% | 100% | 527 KB | 11 (+0) |
| [uw-syfi/vibesys](https://github.com/uw-syfi/vibesys) | A D C | 58,364 | 84,286 | 50.8 | 69% | 7% | 100% | 119 KB | 116 (+0) |
| [tale-project/tale](https://github.com/tale-project/tale) | A E B | 53,949 | 77,356 | 35.1 | 40% | 8% | 91% | 2,600 KB | 35 (+0) |
| [ifdotpy/codex-studio](https://github.com/ifdotpy/codex-studio) | A D C | 46,204 | 184,177 | 9.4 | 65% | 24% | 55% | 724 KB | 4 (+0) |
| [itismyfield/AgentDesk](https://github.com/itismyfield/AgentDesk) | A B C | 44,436 | 50,426 | 28.2 | 86% | 82% | 94% | 364 KB | 9 (+0) |
| [bogdan-alexandrescu/SwarmCloud](https://github.com/bogdan-alexandrescu/SwarmCloud) | A C B | 43,508 | 48,258 | 35.0 | 73% | 48% | 92% | 765 KB | 1 (+0) |
| [thisisjun786/codex-relay-workflow](https://github.com/thisisjun786/codex-relay-workflow) | A B B | 42,748 | 78,101 | 31.0 | 80% | 23% | 98% | 231 KB | 1 (+0) |
| [verkyyi/claude-fleet](https://github.com/verkyyi/claude-fleet) | A A C | 42,532 | 57,972 | 55.9 | 91% | 44% | 98% | 608 KB | 2 (+0) |
| [manaty/ameesh](https://github.com/manaty/ameesh) | A C B | 41,734 | 63,336 | 16.6 | 81% | 0% | 92% | 553 KB | 0 |
| [compoundingtech/smalltalk](https://github.com/compoundingtech/smalltalk) | A D C | 40,658 | 104,090 | 57.7 | 63% | 38% | 79% | 1,727 KB | 4 (+0) |
| [rjwalters/loom](https://github.com/rjwalters/loom) | B B C | 37,507 | 45,301 | 65.9 | 86% | 31% | 96% | 691 KB | 14 (+0) |
| [curie-eng/curie](https://github.com/curie-eng/curie) | B F B | 37,183 | 46,712 | 37.0 | 12% | 5% | 94% | 534 KB | 37 (+0) |
| [constellation-works/orbit](https://github.com/constellation-works/orbit) | B C A | 34,167 | 50,546 | 91.0 | 77% | 17% | 100% | 163 KB | 14 (+0) |
| [buildd-ai/buildd](https://github.com/buildd-ai/buildd) | B E B | 32,920 | 677,916 | 83.1 | 52% | 42% | 93% | 573 KB | 2 (+0) |
| [joemooney/aida](https://github.com/joemooney/aida) | B E C | 32,154 | 51,975 | 25.7 | 58% | 18% | 95% | 738 KB | 5 (+0) |
| [craigoley/remudero](https://github.com/craigoley/remudero) | B E B | 32,065 | 41,351 | 168 | 60% | 55% | 100% | 3,078 KB | 1 (+0) |
| [vtmocanu/uzi](https://github.com/vtmocanu/uzi) | B E B | 31,567 | 42,775 | 32.4 | 74% | 34% | 100% | 1,328 KB | 91 (+0) |
| [ThomasMichon/copilot-extensions](https://github.com/ThomasMichon/copilot-extensions) | B F D | 30,886 | 107,774 | 98.3 | 24% | 14% | 46% | 310 KB | 3 (+0) |
| [Latand/delegatus](https://github.com/Latand/delegatus) | B E B | 30,668 | 116,779 | 26.8 | 47% | 42% | 100% | 843 KB | 31 (+0) |
| [bobmatnyc/trusty-tools](https://github.com/bobmatnyc/trusty-tools) | B B D | 29,261 | 32,651 | 33.5 | 84% | 3% | 100% | 599 KB | 22 (+0) |
| [Gulliby-development/baked](https://github.com/Gulliby-development/baked) | B E B | 27,431 | 44,960 | 27.4 | 50% | 32% | 100% | 555 KB | 2 |
| [zajca/pohunek](https://github.com/zajca/pohunek) | B F B | 27,379 | 29,424 | 19.4 | 45% | 15% | 94% | 808 KB | 4 (+0) |
| [OmniNode-ai/omnimarket](https://github.com/OmniNode-ai/omnimarket) | B D A | 26,756 | 55,188 | 43.8 | 61% | 48% | 100% | 354 KB | 2 (+0) |
| [upyoke/yoke](https://github.com/upyoke/yoke) | B F B | 26,392 | 96,277 | 37.1 | 33% | 13% | 100% | 55 KB | 0 (+0) |
| [deeeed/farmslot](https://github.com/deeeed/farmslot) | B C A | 25,851 | 32,978 | 19.8 | 76% | 39% | 100% | 200 KB | 6 |
| [James3014/Nexus-new](https://github.com/James3014/Nexus-new) | B D B | 25,789 | 35,385 | 24.5 | 68% | 20% | 100% | 1,060 KB | 0 (+0) |
| [cjjutba/kernel](https://github.com/cjjutba/kernel) | B E C | 25,629 | 55,814 | 36.0 | 50% | 35% | 66% | 3,052 KB | 2 |
| [jeong-sik/masc](https://github.com/jeong-sik/masc) | B E C | 25,628 | 42,329 | 159 | 54% | 4% | 89% | 2,294 KB | 3 (+0) |
| [HJewkes/titan-platform](https://github.com/HJewkes/titan-platform) | B A A | 25,628 | 66,761 | 57.6 | 90% | 35% | 92% | 60 KB | 0 |
| [charlieanna/autocode](https://github.com/charlieanna/autocode) | B E B | 25,327 | 50,247 | 30.9 | 45% | 50% | 77% | 330 KB | 0 (+0) |
| [thefrederiksen/devthrottle](https://github.com/thefrederiksen/devthrottle) | B F D | 25,270 | 63,607 | 22.8 | 40% | 33% | 34% | 3,082 KB | 96 (+0) |
| [shep-pm/shep-kelpie](https://github.com/shep-pm/shep-kelpie) | B C C | 25,057 | 26,875 | 15.2 | 72% | 4% | 96% | 40 KB | 0 |
| [thoerwink8/fleet-dao](https://github.com/thoerwink8/fleet-dao) | B E A | 25,037 | 59,042 | 55.1 | 85% | 32% | 100% | 163 KB | 2 (+0) |
| [kuhlman-labs/fishhawk](https://github.com/kuhlman-labs/fishhawk) | B F B | 24,987 | 30,934 | 14.4 | 59% | 0% | 99% | 706 KB | 9 (+0) |
| [natepiano/claude_commands](https://github.com/natepiano/claude_commands) | B E D | 23,055 | 35,502 | 0.0 | 47% | 36% | – | 293 KB | 2 |
| [rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | B E A | 22,840 | 109,885 | 22.6 | 76% | 3% | 97% | 371 KB | 48 |
| [bllshttng/footnote](https://github.com/bllshttng/footnote) | B C B | 22,792 | 30,061 | 43.9 | 77% | 38% | 98% | 555 KB | 2 (+0) |
| [medici-finance/assay](https://github.com/medici-finance/assay) | B F B | 22,072 | 38,389 | 28.5 | 17% | 17% | 100% | 225 KB | 7 (+0) |
| [janoist1/projectman](https://github.com/janoist1/projectman) | B F D | 21,430 | 28,540 | 0.0 | 42% | 0% | – | 277 KB | 0 (+0) |
| [BlackBeltTechnology/pi-agent-dashboard](https://github.com/BlackBeltTechnology/pi-agent-dashboard) | B F A | 21,250 | 46,401 | 6.5 | 61% | 8% | 92% | 257 KB | 321 |
| [favcrm/cadence](https://github.com/favcrm/cadence) | C F C | 19,698 | 30,284 | 34.4 | 35% | 24% | 100% | 424 KB | 0 (+0) |
| [sjawhar/legion](https://github.com/sjawhar/legion) | C C A | 19,558 | 33,776 | 26.9 | 77% | 47% | 98% | 152 KB | 4 (+0) |
| [dreadnought-foundry/bureau-pipeline](https://github.com/dreadnought-foundry/bureau-pipeline) | C E B | 18,983 | 24,954 | 23.9 | 44% | 6% | 99% | 793 KB | 0 |
| [noahdgrant/nightshift](https://github.com/noahdgrant/nightshift) | C F A | 18,874 | 25,888 | 11.6 | 71% | 3% | 100% | 50 KB | 0 |
| [arul28/ADE](https://github.com/arul28/ADE) | C F B | 18,501 | 21,012 | 14.3 | 6% | 5% | 95% | 3,001 KB | 119 (+1) |
| [jikig-ai/soleur](https://github.com/jikig-ai/soleur) | C E C | 17,992 | 44,010 | 27.9 | 47% | 37% | 99% | 455 KB | 18 (+0) |
| [TheCrimsonKing92/mcg-agent-orchestrator](https://github.com/TheCrimsonKing92/mcg-agent-orchestrator) | C C D | 17,935 | 18,654 | 0.0 | 79% | 25% | – | 226 KB | 0 (+0) |
| [picoduck/wollipog](https://github.com/picoduck/wollipog) | C D B | 16,889 | 23,757 | 33.6 | 63% | 43% | 86% | 1,490 KB | 3 (+0) |
| [taneliang/farcooler](https://github.com/taneliang/farcooler) | C F B | 16,690 | 21,745 | 0.0 | 36% | 0% | 96% | 589 KB | 1 (+0) |
| [loopx-project/loopx](https://github.com/loopx-project/loopx) | C E B | 16,522 | 26,161 | 59.2 | 44% | 56% | 98% | 768 KB | 6,355 (+6) |
| [MeloMar-IT/spaghetti-code-foundry](https://github.com/MeloMar-IT/spaghetti-code-foundry) | C E D | 16,350 | 23,381 | 0.6 | 49% | 66% | 0% | 161 KB | 0 (+0) |
| [fpresta0607/code-goblins](https://github.com/fpresta0607/code-goblins) | C F A | 15,685 | 22,991 | 29.7 | 50% | 0% | 100% | 118 KB | 1 (+0) |
| [rxm7706/local-recipes](https://github.com/rxm7706/local-recipes) | C D A | 15,224 | 46,666 | 28.4 | 68% | 21% | 100% | 393 KB | 0 (+0) |
| [dimipaun/fugaro](https://github.com/dimipaun/fugaro) | C E A | 15,010 | 32,148 | 14.9 | 54% | 32% | 89% | 129 KB | 0 (+0) |
| [mssoka/gru-command](https://github.com/mssoka/gru-command) | C D B | 14,510 | 19,568 | 7.6 | 61% | 20% | 78% | 586 KB | 0 (+0) |
| [Kangentic/kangentic](https://github.com/Kangentic/kangentic) | C F A | 14,395 | 20,100 | 4.7 | 19% | 0% | 97% | 399 KB | 129 (+0) |
| [hcipengm/cogneva](https://github.com/hcipengm/cogneva) | C B D | 14,230 | 17,842 | 0.0 | 88% | 56% | 35% | 880 KB | 32 (+0) |
| [leodearden/dark-factory](https://github.com/leodearden/dark-factory) | C C D | 14,189 | 35,935 | 0.0 | 77% | 48% | – | 1,189 KB | 3 (+0) |
| [thewoolleyman/livespec-orchestrator-beads-fabro](https://github.com/thewoolleyman/livespec-orchestrator-beads-fabro) | C C A | 13,990 | 89,731 | 19.2 | 77% | 25% | 100% | 158 KB | 0 |
| [fmogensen/ASF](https://github.com/fmogensen/ASF) | C E C | 13,417 | 35,815 | 55.1 | 44% | 17% | 98% | 325 KB | 3 (+0) |
| [cdknorow/coral](https://github.com/cdknorow/coral) | C E B | 13,192 | 27,276 | 0.2 | 53% | 8% | 98% | 155 KB | 53 |
| [yotamleo/Himmel](https://github.com/yotamleo/Himmel) | C C C | 13,125 | 20,524 | 68.5 | 72% | 67% | 100% | 4,357 KB | 15 (+0) |
| [digitaldrywood/detent](https://github.com/digitaldrywood/detent) | C F D | 12,996 | 22,229 | 63.1 | 26% | 34% | 25% | 837 KB | 16 |
| [smithersai/smithers](https://github.com/smithersai/smithers) | C F C | 12,867 | 30,811 | 0.2 | 55% | 0% | 66% | 1,271 KB | 439 (+0) |
| [HJewkes/agent-chat](https://github.com/HJewkes/agent-chat) | C C C | 12,744 | 17,256 | 34.9 | 73% | 12% | 100% | 216 KB | 0 |
| [Small-Tale/hotsheet2](https://github.com/Small-Tale/hotsheet2) | C F D | 12,722 | 23,529 | 0.0 | 12% | 21% | 30% | 220 KB | 0 (+0) |
| [shubhodeep1/coding-workflows](https://github.com/shubhodeep1/coding-workflows) | C D B | 12,693 | 16,476 | 44.5 | 61% | 30% | 100% | 1,623 KB | 2 (+0) |
| [wsp-labs/wsp](https://github.com/wsp-labs/wsp) | C E A | 12,559 | 23,906 | 0.7 | 60% | 38% | 100% | 163 KB | 11 (+0) |
| [ElectricJack/agent-queue](https://github.com/ElectricJack/agent-queue) | C F B | 12,364 | 23,845 | 32.4 | 41% | 0% | 97% | 387 KB | 9 (+0) |
| [Simon-McIntosh/reckon](https://github.com/Simon-McIntosh/reckon) | C F D | 12,179 | 345,250 | 0.0 | 55% | 0% | 0% | 3,283 KB | 1 (+0) |
| [integry/propr](https://github.com/integry/propr) | C E B | 12,104 | 16,928 | 13.1 | 62% | 7% | 100% | 4,314 KB | 19 (+1) |
| [michal-ciechan/Antiphon](https://github.com/michal-ciechan/Antiphon) | C E C | 11,998 | 55,544 | 0.0 | 65% | 21% | 50% | 470 KB | 1 (+0) |
| [raiki61/works-factory](https://github.com/raiki61/works-factory) | C E C | 11,992 | 31,779 | 8.0 | 75% | 0% | 99% | 262 KB | 1 |
| [code-yeongyu/oh-my-openagent](https://github.com/code-yeongyu/oh-my-openagent) | C B B | 11,954 | 15,525 | 29.5 | 82% | 26% | 81% | 1,496 KB | 70,162 (+20) |
| [rimio-ai/rimz](https://github.com/rimio-ai/rimz) | C C C | 11,866 | 15,151 | 21.5 | 74% | 34% | 100% | 124 KB | 32 (+0) |
| [serious-alchemy/arbiter](https://github.com/serious-alchemy/arbiter) | C C B | 11,720 | 23,640 | 18.0 | 78% | 17% | 91% | 436 KB | 0 (+0) |
| [BlueTeam-OU/agent-fabric](https://github.com/BlueTeam-OU/agent-fabric) | C E C | 11,708 | 17,238 | 9.5 | 43% | 34% | 95% | 109 KB | 0 (+0) |
| [a11ign/agent-org](https://github.com/a11ign/agent-org) | C F C | 11,505 | 23,155 | 36.4 | 40% | 9% | 100% | 599 KB | 0 (+0) |
| [handarbeit/fabrik](https://github.com/handarbeit/fabrik) | C F D | 11,499 | 23,332 | 10.1 | 48% | 27% | 0% | 281 KB | 24 |
| [brandonapol/saddle](https://github.com/brandonapol/saddle) | C F B | 11,496 | 12,459 | 10.8 | 58% | 0% | 97% | 56 KB | 0 |
| [akiojin/gwt](https://github.com/akiojin/gwt) | C C B | 11,212 | 24,685 | 22.8 | 75% | 17% | 100% | 1,880 KB | 5 (+0) |
| [atomantic/PortOS](https://github.com/atomantic/PortOS) | C F B | 11,179 | 14,614 | 91.0 | 26% | 68% | 76% | 347 KB | 48 (+0) |
| [floor/teamcli](https://github.com/floor/teamcli) | C F B | 11,037 | 11,877 | 14.8 | 32% | 2% | 97% | 108 KB | 2 (+0) |
| [Eden-Sun/agents-manager](https://github.com/Eden-Sun/agents-manager) | C D C | 10,825 | 11,906 | 0.0 | 68% | 16% | 86% | 869 KB | 1 (+0) |
| [Johnprempeh2/gs-agentic-manager](https://github.com/Johnprempeh2/gs-agentic-manager) | C D B | 10,685 | 407,918 | 25.1 | 62% | 9% | 100% | 1,414 KB | 0 (+0) |
| [cristiangirlea/harness](https://github.com/cristiangirlea/harness) | C F B | 10,503 | 11,254 | 7.3 | 75% | 0% | 93% | 87 KB | 0 |
| [beyond10x/conductor](https://github.com/beyond10x/conductor) | C F A | 10,290 | 20,302 | 2.2 | 51% | 0% | 100% | 258 KB | 0 |
| [xiechimon/pacman](https://github.com/xiechimon/pacman) | C F A | 10,246 | 35,512 | 23.8 | 34% | 0% | 89% | 118 KB | 3 (+0) |
| [pullboard-dev/pullboard](https://github.com/pullboard-dev/pullboard) | C C D | 10,233 | 10,994 | 0.0 | 75% | 42% | 38% | 264 KB | 210 (+2) |
| [Agrim-Intelligence/sigma](https://github.com/Agrim-Intelligence/sigma) | C C B | 10,161 | 24,358 | 11.0 | 72% | 11% | 96% | 559 KB | 0 (+0) |
| [akmaier/agent-m](https://github.com/akmaier/agent-m) | C F C | 10,104 | 29,268 | 17.9 | 23% | 2% | 95% | 67 KB | 2 (+0) |
| [creedants/pstack-t3](https://github.com/creedants/pstack-t3) | C D C | 10,081 | 18,811 | 11.1 | 65% | 36% | 80% | 147 KB | 11 (+0) |
| [wwind123/coding-review-agent-loop](https://github.com/wwind123/coding-review-agent-loop) | D F B | 9,792 | 15,133 | 8.5 | 35% | 16% | 100% | 519 KB | 11 (+0) |
| [rafalpodles/board-planner](https://github.com/rafalpodles/board-planner) | D F C | 9,649 | 8,600 | 10.6 | 20% | 21% | 99% | 99 KB | 4 (+0) |
| [rick-dev-creator/avala](https://github.com/rick-dev-creator/avala) | D F B | 9,632 | 28,630 | 1.1 | 63% | 16% | 75% | 33 KB | 1 |
| [songsid/AgEnD](https://github.com/songsid/AgEnD) | D E B | 9,620 | 16,705 | 24.5 | 46% | 50% | 100% | 1,152 KB | 8 (+2) |
| [swarmgraph/yoyodyne](https://github.com/swarmgraph/yoyodyne) | D C B | 9,429 | 10,528 | 22.0 | 78% | 26% | 99% | 553 KB | 1 (+0) |
| [perfectuser21/cecelia](https://github.com/perfectuser21/cecelia) | D F B | 9,405 | 12,870 | 28.2 | 55% | 12% | 73% | 203 KB | 0 (+0) |
| [fullsend-ai/fullsend](https://github.com/fullsend-ai/fullsend) | D F B | 9,391 | 14,908 | 13.8 | 26% | 38% | 98% | 318 KB | 158 |
| [qiangli/yoke](https://github.com/qiangli/yoke) | D C D | 9,278 | 16,071 | 0.0 | 71% | 0% | 0% | 601 KB | 1 (+0) |
| [griffinwork40/agent-afk](https://github.com/griffinwork40/agent-afk) | D F A | 9,198 | 11,698 | 44.9 | 0% | 40% | 94% | 67 KB | 61 (+0) |
| [stabem/GraphHelm](https://github.com/stabem/GraphHelm) | D C D | 9,095 | 18,252 | 29.4 | 71% | 52% | – | 384 KB | 0 (+0) |
| [mrinaldi2/gravity](https://github.com/mrinaldi2/gravity) | D E D | 9,059 | 11,177 | 0.3 | 68% | 0% | 30% | 17 KB | 0 (+0) |
| [Volpestyle/clankie](https://github.com/Volpestyle/clankie) | D E C | 8,945 | 17,397 | 0.2 | 55% | 41% | 100% | 335 KB | 2 (+0) |
| [dmz006/datawatch](https://github.com/dmz006/datawatch) | D E C | 8,940 | 36,242 | 1.2 | 52% | 41% | 94% | 3,340 KB | 7 |
| [cryptob1/graphyard](https://github.com/cryptob1/graphyard) | D F A | 8,801 | 10,985 | 36.1 | 38% | 12% | 87% | 323 KB | 0 (+0) |
| [coreplanelabs/switchboard](https://github.com/coreplanelabs/switchboard) | D F B | 8,787 | 17,374 | 36.1 | 15% | 38% | 100% | 839 KB | 4 (+0) |
| [kasofsk/chuggy](https://github.com/kasofsk/chuggy) | D F D | 8,770 | 12,564 | 10.9 | 55% | 0% | – | 82 KB | 2 (+0) |
| [ShiftLead/shiftlead](https://github.com/ShiftLead/shiftlead) | D F B | 8,647 | 12,493 | 0.0 | 50% | 10% | 98% | 397 KB | 0 (+0) |
| [kryptobaseddev/cleo](https://github.com/kryptobaseddev/cleo) | D E A | 8,642 | 15,706 | 27.1 | 71% | 36% | 100% | 316 KB | 160 |
| [agent-sh/tower-crane](https://github.com/agent-sh/tower-crane) | D D D | 8,486 | 12,010 | 12.2 | 68% | 31% | 37% | 128 KB | 0 (+0) |
| [ellmos-ai/bach](https://github.com/ellmos-ai/bach) | D F C | 8,479 | 9,473 | 10.2 | 58% | 0% | 91% | 6,579 KB | 8 (+0) |
| [dmlguq456/hearting](https://github.com/dmlguq456/hearting) | D F C | 8,470 | 12,150 | 17.7 | 33% | 31% | 100% | 650 KB | 9 (+0) |
| [widoriezebos/agentic-tools](https://github.com/widoriezebos/agentic-tools) | D D D | 8,280 | 13,092 | 0.0 | 69% | 14% | 42% | 266 KB | 0 (+0) |
| [takecchi/alteroid](https://github.com/takecchi/alteroid) | D C B | 8,224 | 10,803 | 75.6 | 75% | 40% | 100% | 726 KB | 0 (+0) |
| [tkadauke/syrus](https://github.com/tkadauke/syrus) | D D D | 7,837 | 9,883 | 8.2 | 67% | 17% | 31% | 191 KB | 2 (+0) |
| [david-engelmann/maidan](https://github.com/david-engelmann/maidan) | D F A | 7,767 | 15,221 | 17.3 | 26% | 9% | 93% | 361 KB | 7 (+0) |
| [itsOmidKarami/kraft](https://github.com/itsOmidKarami/kraft) | D F B | 7,710 | 12,571 | 28.6 | 19% | 11% | 95% | 134 KB | 1 (+0) |
| [Jason-Vaughan/TangleClaw](https://github.com/Jason-Vaughan/TangleClaw) | D F B | 7,561 | 11,603 | 13.9 | 51% | 0% | 100% | 696 KB | 11 (+0) |
| [mixpeek/amux](https://github.com/mixpeek/amux) | D F C | 7,340 | 17,425 | 3.4 | 17% | 45% | 86% | 3,373 KB | 540 (+1) |
| [mickeyyaya/evolve-loop](https://github.com/mickeyyaya/evolve-loop) | D F B | 7,311 | 20,532 | 8.7 | 58% | 0% | 77% | 86 KB | 6 (+0) |
| [syntropic137/syntropic137](https://github.com/syntropic137/syntropic137) | D F A | 7,169 | 17,030 | 12.6 | 34% | 0% | 100% | 236 KB | 5 (+0) |
| [cbusillo/codex-skills](https://github.com/cbusillo/codex-skills) | D F C | 7,102 | 10,574 | 25.1 | 29% | 33% | 99% | 557 KB | 5 (+0) |
| [Cuarroc/ProjectA](https://github.com/Cuarroc/ProjectA) | D E C | 6,973 | 11,810 | 31.7 | 49% | 0% | 100% | 403 KB | 2 (+0) |
| [paul-gross/blizzard](https://github.com/paul-gross/blizzard) | D F A | 6,928 | 12,379 | 13.5 | 28% | 0% | 91% | 128 KB | 5 (+0) |
| [itkadr-git/myrmidon](https://github.com/itkadr-git/myrmidon) | D F B | 6,811 | 83,268 | 31.2 | 35% | 8% | 96% | 1,429 KB | 0 (+0) |
| [beadhive/beadhive](https://github.com/beadhive/beadhive) | D E D | 6,721 | 33,303 | 0.0 | 49% | 16% | – | 192 KB | 28 (+0) |
| [HarnessDesk/HarnessDesk](https://github.com/HarnessDesk/HarnessDesk) | D F B | 6,715 | 15,061 | 21.2 | 77% | 0% | 88% | 700 KB | 4 (+0) |
| [mobasak/fabrik](https://github.com/mobasak/fabrik) | D E C | 6,535 | 21,255 | 0.0 | 75% | 0% | 100% | 457 KB | 1 (+0) |
| [rafarc21/fleetflare](https://github.com/rafarc21/fleetflare) | D E B | 6,398 | 11,311 | 17.3 | 56% | 13% | 100% | 499 KB | 0 |
| [pmark/arcadia](https://github.com/pmark/arcadia) | D F B | 6,374 | 11,702 | 21.0 | 23% | 18% | 97% | 268 KB | 1 (+0) |
| [ldecorps/swarmforgevc](https://github.com/ldecorps/swarmforgevc) | D D C | 6,353 | 18,397 | 0.0 | 70% | 13% | 100% | 226 KB | 1 (+0) |
| [FairladyZ625/harness-anything](https://github.com/FairladyZ625/harness-anything) | D D A | 6,306 | 11,238 | 29.4 | 65% | 38% | 87% | 102 KB | 230 (+0) |
| [8007342/tillandsias](https://github.com/8007342/tillandsias) | D E E | 6,155 | 16,322 | 11.8 | 57% | 37% | 76% | 1,492 KB | 5 |
| [UndefinedDatabase/remedy](https://github.com/UndefinedDatabase/remedy) | D F C | 6,139 | 13,125 | 3.1 | 56% | 19% | 90% | 319 KB | 1 (+0) |
| [nedschorus/nedschorus](https://github.com/nedschorus/nedschorus) | D E D | 6,119 | 9,788 | 35.4 | 66% | 2% | – | 188 KB | 2 |
| [hisamekms/dagq](https://github.com/hisamekms/dagq) | D F D | 6,105 | 14,693 | 0.0 | 50% | 0% | 18% | 268 KB | 0 (+0) |
| [ihsan-sa/autobox](https://github.com/ihsan-sa/autobox) | D D D | 6,083 | 12,898 | 0.0 | 64% | 10% | 0% | 310 KB | 0 |
| [yukimemi/magi](https://github.com/yukimemi/magi) | D F C | 5,808 | 6,920 | 22.9 | 70% | 6% | 93% | 884 KB | 1 (+0) |
| [Agent-Clubhouse/Goobers](https://github.com/Agent-Clubhouse/Goobers) | D C C | 5,731 | 18,048 | 36.6 | 81% | 0% | 59% | 240 KB | 9 (+0) |
| [platypeeps/sd-ai-command-pack](https://github.com/platypeeps/sd-ai-command-pack) | D E C | 5,630 | 16,398 | 17.7 | 47% | 50% | 100% | 171 KB | 0 (+0) |
| [hurttlocker/o8](https://github.com/hurttlocker/o8) | D F C | 5,606 | 10,421 | 18.6 | 46% | 0% | 64% | 383 KB | 19 (+0) |
| [maba-pag/owlbear](https://github.com/maba-pag/owlbear) | D C D | 5,508 | 9,997 | 4.1 | 73% | 26% | – | 140 KB | 0 |
| [phanlemanh/acceptance-gate-kit](https://github.com/phanlemanh/acceptance-gate-kit) | D F C | 5,491 | 20,829 | 6.5 | 36% | 47% | 91% | 234 KB | 0 |
| [hivecommons/hive](https://github.com/hivecommons/hive) | D F B | 5,316 | 18,130 | 98.4 | 24% | 2% | 92% | 3,502 KB | 68 |
| [sainteye/clawdline](https://github.com/sainteye/clawdline) | D F B | 5,315 | 7,186 | 0.0 | 20% | 45% | 100% | 398 KB | 1 (+0) |
| [Derek-X-Wang/wefty](https://github.com/Derek-X-Wang/wefty) | D B A | 5,251 | 8,952 | 8.9 | 81% | 46% | 96% | 241 KB | 0 (+0) |
| [knacklabs/symphony-forge](https://github.com/knacklabs/symphony-forge) | D C B | 5,064 | 12,817 | 20.6 | 74% | 36% | 95% | 67 KB | 10 (+0) |
| [lukemcqueen/hermes-cortex](https://github.com/lukemcqueen/hermes-cortex) | D C D | 5,027 | 10,313 | 0.0 | 76% | 12% | 0% | 392 KB | 4 (+0) |
| [newsdayads/tigeriq-ai-lab](https://github.com/newsdayads/tigeriq-ai-lab) | D E B | 5,023 | 6,209 | 48.2 | 44% | 22% | 99% | 301 KB | 2 (+0) |
| [kamilkreiser/Wednesday](https://github.com/kamilkreiser/Wednesday) | E E F | 4,986 | 109,772 | 0.0 | 69% | 0% | – | 8,190 KB | 0 (+0) |
| [minhtri2710/munsu](https://github.com/minhtri2710/munsu) | E F A | 4,981 | 7,381 | 5.5 | 24% | 0% | 95% | 102 KB | 1 |
| [Sfaiug/agentkit](https://github.com/Sfaiug/agentkit) | E E D | 4,918 | 5,761 | 31.6 | 54% | 11% | – | 357 KB | 2 (+0) |
| [ShipfoxHQ/shipfox](https://github.com/ShipfoxHQ/shipfox) | E F B | 4,900 | 13,948 | 25.1 | 10% | 17% | 95% | 489 KB | 28 (+0) |
| [EchoRaven/env-gen](https://github.com/EchoRaven/env-gen) | E D D | 4,860 | 4,969 | 0.0 | 65% | 36% | – | 3,234 KB | 0 |
| [giantswarm/beekeeper](https://github.com/giantswarm/beekeeper) | E C B | 4,853 | 6,548 | 18.1 | 78% | 52% | 99% | 96 KB | 0 (+0) |
| [argszero/emrg](https://github.com/argszero/emrg) | E B A | 4,843 | 6,000 | 18.7 | 81% | 55% | 100% | 392 KB | 10 (+0) |
| [Dicklesworthstone/ntm](https://github.com/Dicklesworthstone/ntm) | E F D | 4,783 | 4,948 | 0.0 | 46% | 0% | 33% | 397 KB | 459 (+0) |
| [Consiliency/agent-harness](https://github.com/Consiliency/agent-harness) | E F B | 4,635 | 9,395 | 9.5 | 27% | 13% | 98% | 787 KB | 2 (+0) |
| [passioncode-ai/fabric](https://github.com/passioncode-ai/fabric) | E E D | 4,562 | 33,555 | 0.8 | 54% | 10% | 45% | 5,509 KB | 1 (+0) |
| [sbluemin/fleet-harness](https://github.com/sbluemin/fleet-harness) | E F C | 4,460 | 9,033 | 26.6 | 42% | 0% | 100% | 467 KB | 17 (+0) |
| [andromarces/agent-loops](https://github.com/andromarces/agent-loops) | E E D | 4,450 | 5,572 | 15.8 | 48% | 0% | – | 46 KB | 3 (+0) |
| [chetwerikoff/orchestrator-pack](https://github.com/chetwerikoff/orchestrator-pack) | E E A | 4,385 | 6,733 | 13.5 | 59% | 28% | 98% | 467 KB | 1 (+0) |
| [dark-factory-build/dark-factory](https://github.com/dark-factory-build/dark-factory) | E E C | 4,368 | 6,685 | 25.1 | 58% | 12% | 99% | 357 KB | 1 |
| [sleep2agi/agent-network](https://github.com/sleep2agi/agent-network) | E E B | 4,296 | 9,697 | 28.9 | 52% | 30% | 96% | 978 KB | 97 (+2) |
| [vilmire/adhdev](https://github.com/vilmire/adhdev) | E F D | 4,004 | 12,896 | 0.0 | 12% | 10% | 49% | 146 KB | 108 (+0) |
| [jordansmall/spindrift](https://github.com/jordansmall/spindrift) | E F B | 3,406 | 6,589 | 32.1 | 51% | 0% | 99% | 106 KB | 4 (+0) |
| [Cheekyfellastef/stephan-os](https://github.com/Cheekyfellastef/stephan-os) | E F C | 3,385 | 4,097 | 23.8 | 26% | 10% | 95% | 544 KB | 0 (+0) |
| [scbrown/shantytown](https://github.com/scbrown/shantytown) | E C B | 3,356 | 4,310 | 8.2 | 76% | 70% | 100% | 703 KB | 0 |
| [genaforvena/mishe-tauftauf](https://github.com/genaforvena/mishe-tauftauf) | E E B | 3,266 | 6,466 | 0.1 | 52% | 38% | 85% | 309 KB | 3 (+0) |
| [djimit/djimitflo](https://github.com/djimit/djimitflo) | E F A | 3,144 | 8,248 | 19.6 | 33% | 13% | 100% | 386 KB | 1 (+0) |
| [kurone-kito/idd-skill](https://github.com/kurone-kito/idd-skill) | E B E | 3,076 | 24,159 | 21.4 | 90% | 47% | 99% | 613 KB | 11 (+0) |
| [pom11/hscc](https://github.com/pom11/hscc) | E F B | 3,019 | 5,223 | 0.5 | 27% | 0% | 100% | 142 KB | 7 (+0) |
| [stranske/Workflows](https://github.com/stranske/Workflows) | E F C | 2,953 | 20,114 | 11.5 | 60% | 0% | 97% | 328 KB | 2 (+0) |
| [fmanimashaun/claude-skills](https://github.com/fmanimashaun/claude-skills) | E D E | 2,758 | 6,831 | 19.8 | 65% | 9% | 94% | 555 KB | 0 (+0) |
| [saymyname-app/agent-factory](https://github.com/saymyname-app/agent-factory) | E D C | 2,681 | 10,702 | 18.2 | 60% | 40% | 98% | 403 KB | 1 (+0) |
| [drmoisan/drm-copilot](https://github.com/drmoisan/drm-copilot) | E F C | 2,605 | 67,128 | 4.9 | 27% | 0% | 99% | 24 KB | 0 (+0) |
| [AndrewDryga/coop](https://github.com/AndrewDryga/coop) | E F B | 2,590 | 5,579 | 0.1 | 35% | 6% | 74% | 152 KB | 29 (+0) |
| [vamseeachanta/workspace-hub](https://github.com/vamseeachanta/workspace-hub) | E F C | 2,526 | 4,629 | 4.8 | 39% | 17% | 94% | 7,014 KB | 18 (+0) |
| [JKershaw/LinearViewer](https://github.com/JKershaw/LinearViewer) | E F B | 2,486 | 9,195 | 13.9 | 36% | 0% | 100% | 241 KB | 2 (+0) |
| [MoonLadderStudios/MoonMind](https://github.com/MoonLadderStudios/MoonMind) | E F B | 2,462 | 7,682 | 14.2 | 31% | 0% | 89% | 1,186 KB | 13 (+0) |
| [volkb79-2/vbpub](https://github.com/volkb79-2/vbpub) | E F D | 2,440 | 6,513 | 0.0 | 49% | 0% | – | 776 KB | 0 (+0) |
| [MattFlower/limitless](https://github.com/MattFlower/limitless) | E F C | 2,405 | 3,222 | 11.2 | 68% | 0% | 93% | 115 KB | 1 (+0) |
| [nexus-substrate/nexus-agents](https://github.com/nexus-substrate/nexus-agents) | E F A | 2,366 | 4,321 | 23.3 | 45% | 0% | 100% | 129 KB | 23 (+0) |
| [popcre/ai-devops](https://github.com/popcre/ai-devops) | E F D | 2,318 | 6,482 | 27.9 | 55% | 0% | 47% | 97 KB | 0 (+0) |
| [devbasex/ai-plugins](https://github.com/devbasex/ai-plugins) | E F B | 2,244 | 6,929 | 29.3 | 28% | 0% | 100% | 617 KB | 1 (+0) |
| [Claudfather/Claudlobby](https://github.com/Claudfather/Claudlobby) | E F B | 2,242 | 5,897 | 9.9 | 48% | 0% | 98% | 329 KB | 0 (+0) |
| [nikhilsoman/synlynk](https://github.com/nikhilsoman/synlynk) | E F B | 2,170 | 5,858 | 13.0 | 36% | 31% | 80% | 228 KB | 1 (+0) |
| [turbokast/mythhelm](https://github.com/turbokast/mythhelm) | E E B | 2,013 | 5,686 | 12.8 | 51% | 0% | 97% | 49 KB | 0 (+0) |
| [martin-beck/agent-workflow-coordinator](https://github.com/martin-beck/agent-workflow-coordinator) | E F C | 2,001 | 6,431 | 21.8 | 28% | 0% | 90% | 195 KB | 0 |
| [ptr727/ProjectTemplate](https://github.com/ptr727/ProjectTemplate) | E F B | 1,947 | 3,265 | 19.8 | 45% | 65% | 97% | 624 KB | 1 (+0) |
| [trung-via/AIOS-renew](https://github.com/trung-via/AIOS-renew) | E F D | 1,890 | 3,583 | 0.2 | 60% | 18% | 0% | 453 KB | 0 (+0) |
| [Tolkoton/claude-cli-config](https://github.com/Tolkoton/claude-cli-config) | E F D | 1,889 | 8,166 | 0.0 | 31% | 0% | – | 112 KB | 0 |
| [kinoko34077/devflow](https://github.com/kinoko34077/devflow) | E E C | 1,882 | 4,504 | 8.3 | 41% | 12% | 100% | 66 KB | 0 |
| [repairman29/chump](https://github.com/repairman29/chump) | E E E | 1,856 | 2,692 | 20.9 | 51% | 0% | 87% | 1,103 KB | 0 |
| [bajoicheg/g-cdc](https://github.com/bajoicheg/g-cdc) | E F D | 1,621 | 3,859 | 1.9 | 52% | 0% | 33% | 61 KB | 0 (+0) |
| [yogata/agent-dev-flow](https://github.com/yogata/agent-dev-flow) | E F D | 1,583 | 18,336 | 15.0 | 38% | 0% | – | 408 KB | 0 (+0) |
| [Zennay/zCloud](https://github.com/Zennay/zCloud) | E F C | 1,578 | 4,532 | 19.1 | 11% | 0% | 99% | 276 KB | 0 (+0) |
| [DraconDev/pi-goal-list-loop-audit](https://github.com/DraconDev/pi-goal-list-loop-audit) | E F D | 1,549 | 4,578 | 0.0 | 39% | 0% | 28% | 554 KB | 27 |
| [ArcavenAE/marvel](https://github.com/ArcavenAE/marvel) | E F B | 1,456 | 4,216 | 14.6 | 10% | 0% | 99% | 129 KB | 0 (+0) |
| [dronrider/devkit](https://github.com/dronrider/devkit) | E F D | 1,450 | 3,670 | 0.0 | 57% | 0% | 0% | 1,105 KB | 0 |
| [shine2lay/temper-ai](https://github.com/shine2lay/temper-ai) | E F A | 1,406 | 11,160 | 0.0 | 24% | 0% | 95% | 211 KB | 0 (+0) |
| [kriscendobot/garden](https://github.com/kriscendobot/garden) | E E D | 1,348 | 1,628 | 0.1 | 57% | 33% | 0% | 634 KB | 3 (+0) |
| [mrflxxxme/wizard](https://github.com/mrflxxxme/wizard) | E F A | 1,281 | 11,871 | 7.8 | 55% | 0% | 98% | 122 KB | 0 |
| [leshchenko1979/agent-factories](https://github.com/leshchenko1979/agent-factories) | E F D | 1,272 | 4,397 | 0.0 | 54% | 0% | – | 532 KB | 2 (+0) |
| [R4yHarris/github-agent-roster](https://github.com/R4yHarris/github-agent-roster) | E F D | 1,255 | 2,604 | 14.1 | 0% | 0% | – | 96 KB | 0 (+0) |
| [melvenac/Self-Improving-Agent](https://github.com/melvenac/Self-Improving-Agent) | E F B | 1,207 | 10,798 | 27.0 | 15% | 0% | 100% | 119 KB | 0 (+0) |
| [jacobhausler/hermes-workflows](https://github.com/jacobhausler/hermes-workflows) | F F C | 945 | 29,246 | 9.7 | 30% | 0% | 59% | 514 KB | 1 (+0) |
| [ArtVsMark/Engineering-Pipeline-Mechanisms](https://github.com/ArtVsMark/Engineering-Pipeline-Mechanisms) | F F A | 882 | 2,481 | 26.1 | 76% | 0% | 100% | 148 KB | 1 (+0) |
| [racecraft-lab/racecraft-plugins-public](https://github.com/racecraft-lab/racecraft-plugins-public) | F F A | 873 | 2,636 | 12.8 | 64% | 0% | 99% | 296 KB | 5 |
| [chnlich/charlie-bot](https://github.com/chnlich/charlie-bot) | F E B | 832 | 3,430 | 44.5 | 65% | 5% | 90% | 139 KB | 8 (+0) |
| [ilgyu-yi/gitjig-pi](https://github.com/ilgyu-yi/gitjig-pi) | F E A | 798 | 1,574 | 2.7 | 48% | 0% | 100% | 59 KB | 1 (+0) |
| [Flip-Engineering/baton](https://github.com/Flip-Engineering/baton) | F E D | 748 | 8,738 | 0.3 | 68% | 0% | – | 276 KB | 1 (+0) |
| [jcoble/mac-command-bar](https://github.com/jcoble/mac-command-bar) | F F D | 734 | 3,040 | 7.8 | 52% | 0% | 97% | 8,119 KB | 1 |
| [Round-Block/bisellium](https://github.com/Round-Block/bisellium) | F F A | 706 | 5,530 | 18.6 | 50% | 0% | 100% | 215 KB | 0 (+0) |
| [CodySwannGT/lisa](https://github.com/CodySwannGT/lisa) | F F C | 693 | 35,872 | 3.7 | 45% | 0% | 100% | 1,116 KB | 5 (+0) |
| [HiromiShikata/npm-cli-github-issue-tower-defence-management](https://github.com/HiromiShikata/npm-cli-github-issue-tower-defence-management) | F F A | 638 | 1,485 | 15.4 | 48% | 0% | 100% | 161 KB | 0 (+0) |
| [teststuffstash/homelab](https://github.com/teststuffstash/homelab) | F F C | 608 | 4,697 | 24.7 | 5% | 18% | 99% | 526 KB | 0 (+0) |
| [Khyretos/kreative-kompanion](https://github.com/Khyretos/kreative-kompanion) | F F D | 579 | 6,046 | 0.0 | 53% | 0% | – | 108 KB | 0 (+0) |
| [euron8/ai-dlc](https://github.com/euron8/ai-dlc) | F F E | 568 | 7,112 | 12.9 | 47% | 0% | 100% | 976 KB | 0 (+0) |
| [orbi-build/orbi](https://github.com/orbi-build/orbi) | F F B | 481 | 1,563 | 7.4 | 57% | 0% | 100% | 174 KB | 220 (+0) |
| [AviGopal/substrate](https://github.com/AviGopal/substrate) | F F C | 391 | 1,371 | 0.0 | 10% | 0% | 98% | 363 KB | 0 |
| [Minntooos/Compounding-Loop](https://github.com/Minntooos/Compounding-Loop) | F F B | 365 | 4,110 | 0.0 | 64% | 0% | 78% | 70 KB | 0 |
| [tampajohn/chug](https://github.com/tampajohn/chug) | F F D | 340 | 1,774 | 0.0 | 21% | 0% | – | 202 KB | 4 (+0) |
| [5throck/ai-workspace-standards](https://github.com/5throck/ai-workspace-standards) | F F C | 274 | 4,656 | 19.8 | 20% | 0% | 88% | 303 KB | 23 (+1) |
| [renatobardi/oute-agent](https://github.com/renatobardi/oute-agent) | F F D | 211 | 1,488 | 14.0 | 15% | 0% | – | 55 KB | 0 (+0) |
| [ekayaprod/jules-agent-roster](https://github.com/ekayaprod/jules-agent-roster) | F F B | 188 | 21,540 | 14.5 | 20% | 0% | 92% | 66 KB | 3 (+0) |
| [unxed/lunobot](https://github.com/unxed/lunobot) | F F C | 149 | 1,438 | 3.4 | 36% | 0% | 98% | 128 KB | 2 (+0) |
| [marius-patrik/DarkFactory](https://github.com/marius-patrik/DarkFactory) | F F A | 107 | 876 | 6.3 | 0% | 0% | 97% | 72 KB | 4 (+0) |
| [a3ka/dev-harness](https://github.com/a3ka/dev-harness) | F E E | 92 | 8,010 | 1.9 | 76% | 12% | 65% | 149 KB | 0 (+0) |
| [MoRen9527/TriMetaverse](https://github.com/MoRen9527/TriMetaverse) | F F E | 82 | 4,008 | 0.0 | 42% | 0% | 0% | 473 KB | 0 (+0) |
| [ShiroDoromoto/amenbo](https://github.com/ShiroDoromoto/amenbo) | F F C | 58 | 374 | 29.2 | 31% | 0% | 100% | 847 KB | 3 (+0) |
| [shuhei-suzuki/rururunx](https://github.com/shuhei-suzuki/rururunx) | F F C | 50 | 1,726 | 1.3 | 0% | 0% | 68% | 290 KB | 0 (+0) |
| [obselate/tokate](https://github.com/obselate/tokate) | F F D | 32 | 6,617 | 12.0 | 53% | 0% | 100% | 43 KB | 1 (+0) |
| [boundring/hngh](https://github.com/boundring/hngh) | F F D | 5 | 2,671 | 0.0 | 24% | 0% | 0% | 110 KB | 0 (+0) |
| [RetryYN/HELIX-HARNESS](https://github.com/RetryYN/HELIX-HARNESS) | F F C | 0 | 1,949,069 | 47.4 | 0% | 0% | 100% | 703 KB | 0 (+0) |
| [gastownhall/gascity](https://github.com/gastownhall/gascity) | F B B | – | – | 36.9 | 83% | 31% | 84% | 2,018 KB | 1,404 (+5) |
| [CartagoGit/DelendAI](https://github.com/CartagoGit/DelendAI) | F F C | 0 | 0 | 27.6 | 0% | 0% | 52% | 92 KB | 1 (+0) |
| [intellibitz/susi](https://github.com/intellibitz/susi) | F F D | 0 | 1,227 | 24.7 | 0% | 0% | 0% | 153 KB | 1 (+0) |
| [Colonizer-dev/harness](https://github.com/Colonizer-dev/harness) | F F C | 0 | 3,565 | 22.9 | 32% | 0% | 94% | 294 KB | 4 (+0) |
| [Simple-With-Us/BotFleet](https://github.com/Simple-With-Us/BotFleet) | F D B | – | – | 21.3 | 70% | 33% | 98% | 961 KB | 4 (+0) |
| [marcogallotta/switchstand](https://github.com/marcogallotta/switchstand) | F F A | 0 | 496 | 20.6 | 0% | 0% | 100% | 84 KB | 0 (+0) |
| [portpowered/you-agent-factory](https://github.com/portpowered/you-agent-factory) | F F A | 0 | 23,522 | 19.2 | 73% | 0% | 97% | 94 KB | 16 (+0) |
| [nateprich-projects/command-center](https://github.com/nateprich-projects/command-center) | F F B | – | – | 18.2 | 14% | 0% | 99% | 1,120 KB | 0 (+0) |
| [parsoFish/forge-studio](https://github.com/parsoFish/forge-studio) | F F B | – | – | 15.5 | 22% | 0% | 98% | 723 KB | 5 (+0) |
| [aphrollo/aphrollo-tools](https://github.com/aphrollo/aphrollo-tools) | F F A | 0 | 351 | 12.2 | 0% | 0% | 98% | 149 KB | 0 (+0) |
| [fontanierh/atelier](https://github.com/fontanierh/atelier) | F F C | – | – | 12.1 | 28% | 0% | 100% | 341 KB | 4 (+0) |
| [sabbour/agentweaver](https://github.com/sabbour/agentweaver) | F F B | 0 | 0 | 12.0 | – | – | 91% | 306 KB | 7 (+0) |
| [jubbydev/tandem](https://github.com/jubbydev/tandem) | F F D | 0 | 111 | 11.6 | 0% | 0% | – | 115 KB | 0 (+0) |
| [SnowsonZ/delivery-harness](https://github.com/SnowsonZ/delivery-harness) | F F C | 0 | 23 | 7.4 | 0% | 0% | 98% | 42 KB | 0 (+0) |
| [automagik-dev/genie](https://github.com/automagik-dev/genie) | F F A | 0 | 15,037 | 6.5 | 0% | 0% | 88% | 151 KB | 345 (+0) |
| [PASAKON/Agents-Core](https://github.com/PASAKON/Agents-Core) | F D B | – | – | 5.8 | 64% | 0% | 83% | 206 KB | 0 |
| [kodmial/continuum](https://github.com/kodmial/continuum) | F F C | 0 | 1,865 | 5.6 | 0% | 0% | 81% | 466 KB | 0 (+0) |
| [OpenAgentsInc/openagents](https://github.com/OpenAgentsInc/openagents) | F D D | – | – | 5.4 | 64% | 55% | 0% | 1,213 KB | 457 (+0) |
| [manuel-alvarez-alvarez/ariadne](https://github.com/manuel-alvarez-alvarez/ariadne) | F D B | 0 | 0 | 3.3 | 61% | 52% | 87% | 149 KB | 2 |
| [sinsan-develop/Anvil](https://github.com/sinsan-develop/Anvil) | F F D | 0 | 1,902 | 1.0 | 0% | 0% | – | 92 KB | 0 (+0) |
| [jianghailong-xy/orbit](https://github.com/jianghailong-xy/orbit) | F E B | – | – | 0.9 | 51% | 5% | 79% | 812 KB | 5 (+0) |
| [asklokesh/loki-mode](https://github.com/asklokesh/loki-mode) | F F C | 0 | 12,041 | 0.2 | 0% | 0% | 80% | 1,464 KB | 1,098 (+1) |
| [tamago2022/tamago-shinchoku](https://github.com/tamago2022/tamago-shinchoku) | F D E | – | – | 0.2 | 66% | 36% | 96% | 21,047 KB | 0 (+0) |
| [Runfusion/Fusion](https://github.com/Runfusion/Fusion) | F F D | 0 | 681 | 0.1 | 15% | 0% | 9% | 904 KB | 1,279 (+0) |
| [CodexOperator/AGI](https://github.com/CodexOperator/AGI) | F D D | 0 | 0 | 0.0 | 62% | 0% | – | 1,157 KB | 1 |
| [cogito5170/baseline](https://github.com/cogito5170/baseline) | F F D | 0 | 0 | 0.0 | – | – | – | 15 KB | 0 (+0) |
| [Disinto/disinto](https://github.com/Disinto/disinto) | F F D | 0 | 0 | 0.0 | – | – | – | 80 KB | 0 (+0) |
| [leshchenko1979/opencrabs-dev-factory](https://github.com/leshchenko1979/opencrabs-dev-factory) | F F D | 0 | 337 | 0.0 | 0% | 0% | – | 59 KB | 1 (+0) |
| [sase-org/sase](https://github.com/sase-org/sase) | F D D | – | – | 0.0 | 61% | 14% | 38% | 72 KB | 5 (+0) |
| [ttmouse/dsh-muse](https://github.com/ttmouse/dsh-muse) | F F D | 0 | 42 | 0.0 | 0% | 0% | – | 18 KB | 0 (+0) |
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
