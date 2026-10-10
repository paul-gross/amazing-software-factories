"""The pure logic: path classification, people, lines, weekly rollups, the clock, link extraction, the screen's totals,
admission, tiers, citations."""
import contextlib
import io
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from asf import discover, grade, judge, lines, measure, rubric, watch
from asf.__main__ import baseline, prior_weeks


def commit(login=None, name=None, adds=10, dels=0, parents=1, when="2026-10-08T12:00:00Z", prs=1, headline="feat: x"):
    return dict(author=dict(name=name or login, user=dict(login=login) if login else None), additions=adds,
                deletions=dels, parents=dict(totalCount=parents), committedDate=when,
                associatedPullRequests=dict(totalCount=prs), messageHeadline=headline)


class Paths(unittest.TestCase):
    def test_source_test_and_neither(self):
        self.assertEqual(measure.classify("src/app/server.py"), "source")
        self.assertEqual(measure.classify("tests/test_server.py"), "test")
        self.assertEqual(measure.classify("web/src/board.spec.ts"), "test")
        self.assertIsNone(measure.classify("node_modules/x/index.js"))
        self.assertIsNone(measure.classify("engine/native/vectors/big.rs"))
        self.assertIsNone(measure.classify("types/api.d.ts"))

    def test_styles_pages_and_shell_scripts_are_code_and_data_is_not(self):
        for path in ("web/src/app.scss", "site/index.html", "scripts/deploy.sh", "web/theme.css"):
            self.assertEqual(measure.classify(path), "source", path)
        for path in ("package-lock.json", "config.yaml", "README.md", "Cargo.lock", "data/rows.csv"):
            self.assertIsNone(measure.classify(path), path)
        self.assertIsNone(measure.classify("README.md"))

    def test_structure_reports_largest_and_tenth(self):
        files = [(f"src/f{i}.py", (i + 1) * 1024) for i in range(12)] + [("tests/test_a.py", 6 * 1024)]
        s = measure.structure(files)
        self.assertEqual(s["largest_file"], "src/f11.py")
        self.assertEqual(s["largest_file_kb"], 12)
        self.assertEqual(s["tenth_largest_file_kb"], 3)
        self.assertEqual(s["source_files"], 12)


def tallied(nodes, total=None, complete=True, merged=None):
    return measure.tally(nodes, len(nodes) if total is None else total, complete, merged)


class People(unittest.TestCase):
    def test_one_person_among_many_contributors(self):
        p = measure.people(tallied([commit("lead")] * 999 + [commit("other")]))
        self.assertEqual(p["lead_human"], "lead")
        self.assertGreaterEqual(p["lead_human_share"], 0.99)
        self.assertEqual(p["human_authors"], 2)

    def test_bots_are_left_out_of_the_one_person_test(self):
        p = measure.people(tallied([commit("fleet[bot]")] * 70 + [commit("owner")] * 30))
        self.assertEqual(p["lead_human_share"], 1.0)
        self.assertEqual(p["bot_commit_share"], 0.7)

    def test_identities_no_account_claims_are_machine_work(self):
        nodes = [commit(name="agent-7")] * 40 + [commit(name="CI")] * 40 + [commit("owner")] * 20
        p = measure.people(tallied(nodes))
        self.assertEqual((p["lead_human"], p["human_authors"]), ("owner", 1))
        self.assertEqual(p["bot_commit_share"], 0.8)

    def test_a_repository_with_no_human_authors_is_all_machine(self):
        p = measure.people(tallied([commit(name="agent-7")] * 10))
        self.assertIsNone(p["lead_human_share"])
        self.assertEqual(p["bot_commit_share"], 1.0)

    def test_merge_commits_do_not_count_as_authorship(self):
        nodes = [commit("maintainer", parents=2)] * 50 + [commit("author")] * 5
        self.assertEqual(measure.people(tallied(nodes))["lead_human"], "author")


class Lines(unittest.TestCase):
    def test_complete_window_sums_exactly(self):
        r = measure.rates(tallied([commit("a", adds=300, dels=100)] * 10), days=10)
        self.assertEqual((r["added_per_day"], r["deleted_per_day"], r["net_per_day"]), (300, 100, 200))
        self.assertFalse(r["lines_estimated"])

    def test_a_window_past_the_read_limit_extrapolates(self):
        r = measure.rates(tallied([commit("a", adds=100)] * 10, total=40, complete=False), days=10)
        self.assertEqual(r["added_per_day"], 400)
        self.assertTrue(r["lines_estimated"])

    def test_merge_commits_add_no_lines(self):
        t = tallied([commit("a", adds=100), commit("a", adds=5000, parents=2)])
        self.assertEqual(measure.rates(t, days=1)["added_per_day"], 100)


class Weeks(unittest.TestCase):
    def test_four_weeks_combine_into_the_month(self):
        weeks = [tallied([commit("lead", adds=1000)] * 70 + [commit("fleet[bot]", adds=500)] * 30, merged=80)] * 3
        weeks.append(tallied([commit("lead", adds=1000)] * 70 + [commit("other", adds=10)] * 30, merged=60))
        month = measure.combine(weeks)
        self.assertEqual((month["commits"], month["merged_prs"], month["authored"]), (400, 300, 400))
        self.assertEqual(month["added"], 3 * 85000 + 70300)
        r = measure.rates(month, days=28)
        self.assertEqual(r["lead_human_share"], round(280 / 310, 3))
        self.assertEqual(r["bot_commit_share"], round(90 / 400, 3))

    def test_a_week_without_a_pull_request_count_leaves_the_month_without_one(self):
        month = measure.combine([tallied([commit("a")], merged=5), tallied([commit("a")], merged=None)])
        self.assertIsNone(month["merged_prs"])

    def test_a_sampled_week_makes_the_month_an_estimate(self):
        month = measure.combine([tallied([commit("a")]), tallied([commit("a")] * 2, total=9, complete=False)])
        self.assertFalse(month["complete"])
        self.assertEqual(month["added"], 10 + 90)


class History(unittest.TestCase):
    day = date(2026, 10, 26)

    def test_three_prior_weekly_snapshots_make_the_month(self):
        snaps = {"2026-10-19": {"a/b": dict(week_tally="w1")}, "2026-10-13": {"A/B": dict(week_tally="w2")},
                 "2026-10-05": {"a/b": dict(week_tally="w3")}}
        self.assertEqual(prior_weeks("a/b", snaps, self.day), ["w1", "w2", "w3"])

    def test_a_missing_week_stops_the_run_of_weeks(self):
        snaps = {"2026-10-19": {"a/b": dict(week_tally="w1")}, "2026-10-05": {"a/b": dict(week_tally="w3")}}
        self.assertEqual(prior_weeks("a/b", snaps, self.day), ["w1"])

    def test_a_recent_screen_supplies_the_baseline(self):
        screens = {"a/b": dict(screened="2026-10-20", month_tally="m")}
        self.assertEqual(baseline("A/B", screens, self.day), "m")
        self.assertIsNone(baseline("a/b", dict(screens, **{"a/b": dict(screened="2026-10-01", month_tally="m")}),
                                   self.day))


class Clock(unittest.TestCase):
    def test_round_the_clock_is_a_quarter(self):
        nodes = [commit("a", when=f"2026-10-08T{h:02d}:00:00Z") for h in range(23, -1, -1)]
        self.assertAlmostEqual(measure.clock(nodes, 7)["quietest_6h_share"], 0.25, places=2)

    def test_active_days_never_exceed_the_window(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T23:00:00Z") for d in range(9, 1, -1)]
        self.assertEqual(measure.clock(nodes, 7)["active_days"], 7)

    def test_every_day_evenly_is_full_day_utilization(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in range(9, 2, -1) for h in range(23, -1, -1)]
        self.assertAlmostEqual(measure.clock(nodes, 7)["day_utilization"], 1.0, delta=0.05)

    def test_a_day_off_empties_the_quietest_day(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in (9, 8, 7, 5, 4, 3) for h in range(23, -1, -1)]
        self.assertAlmostEqual(measure.clock(nodes, 7)["day_utilization"], 0.0, delta=0.05)

    def test_days_since_the_last_commit_count_as_days_off(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in range(7, 0, -1) for h in range(23, -1, -1)]
        now = datetime(2026, 10, 9, 23, 59, tzinfo=timezone.utc)
        self.assertAlmostEqual(measure.clock(nodes, 7, now=now)["day_utilization"], 0.0, delta=0.05)

    def test_a_read_cut_at_its_limit_is_judged_on_the_days_it_reached(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in (9, 8) for h in range(23, -1, -1)]
        self.assertAlmostEqual(measure.clock(nodes, 7, complete=False)["day_utilization"], 1.0, delta=0.07)
        self.assertEqual(measure.clock(nodes[:6], 7, complete=False)["day_utilization"], None)

    def test_every_night_covered_is_seven_of_seven(self):
        nodes = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in range(9, 2, -1) for h in range(23, -1, -1)]
        c = measure.clock(nodes, 7, now=datetime(2026, 10, 10, 0, 0, tzinfo=timezone.utc))
        self.assertEqual((c["nights_seen"], c["nights_covered"]), (7, 7))

    def test_a_few_long_nights_do_not_cover_the_week(self):
        busy = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in range(9, 2, -1) for h in range(6, 24) for _ in range(20)]
        nights = [commit("a", when=f"2026-10-{d:02d}T{h:02d}:30:00Z") for d in (8, 6, 4) for h in range(6) for _ in range(4)]
        c = measure.clock(sorted(busy + nights, key=lambda n: n["committedDate"], reverse=True), 7,
                          now=datetime(2026, 10, 10, 0, 0, tzinfo=timezone.utc))
        self.assertEqual((c["nights_seen"], c["nights_covered"]), (7, 3))

    def test_commit_times_in_any_zone_count_in_utc(self):
        nodes = [commit("a", when="2026-10-08T20:30:00-07:00")]
        self.assertEqual(measure.clock(nodes, 7)["commits_by_2h_utc"][1], 1)

    def test_a_sleeper_has_an_empty_stretch(self):
        nodes = [commit("a", when=f"2026-10-08T{h:02d}:00:00Z") for h in range(20, 7, -1)]
        self.assertEqual(measure.clock(nodes, 7)["quietest_6h_share"], 0.0)


class Parallelism(unittest.TestCase):
    def test_overlapping_pull_requests_count_at_their_peak(self):
        pr = lambda opened, merged: dict(createdAt=f"2026-10-08T{opened:02d}:00:00Z", mergedAt=f"2026-10-08T{merged:02d}:00:00Z")
        self.assertEqual(measure.peak_open([pr(1, 5), pr(2, 6), pr(3, 4), pr(7, 8)]), 3)
        self.assertEqual(measure.peak_open([pr(1, 2), pr(3, 4)]), 1)


class Batches(unittest.TestCase):
    def test_a_failed_batch_splits_in_halves_until_only_the_heavy_repository_is_lost(self):
        asked = []
        def fake(query):
            names = [part.split('name: "')[1].split('"')[0] for part in query.split("repository(")[1:]]
            asked.append(names)
            if "heavy" in names:
                raise measure.GhError("HTTP 502")
            return {f"r{i}": {"name": n} for i, n in enumerate(names)}
        repos = [f"o/r{i}" for i in range(7)] + ["o/heavy"]
        real, measure.graphql = measure.graphql, fake
        try:
            with contextlib.redirect_stdout(io.StringIO()):
                out = measure._aliased([repos], lambda i, r: measure._repo(i, r, "name"), lambda r: r, 1)
        finally:
            measure.graphql = real
        self.assertEqual(sorted(out), sorted(repos[:7]))
        self.assertEqual([len(a) for a in asked], [8, 4, 4, 2, 2, 1, 1])


class Links(unittest.TestCase):
    def test_extracts_repositories_and_skips_reserved_paths(self):
        md = ("See [a](https://github.com/acme/factory) and https://github.com/acme/factory.git, "
              "[topic](https://github.com/topics/agents), [b](https://github.com/x-y/z.js/tree/main).")
        self.assertEqual(discover.links(md), ["acme/factory", "x-y/z.js"])


class Totals(unittest.TestCase):
    def facts(self, **over):
        return dict(dict(archived=False, fork=False, code_bytes=500 * 1024, commits=600, weeks=[150, 150, 150, 150]),
                    **over)

    def test_sustained_work_passes(self):
        self.assertTrue(watch.passes_totals(self.facts(), days=28))

    def test_one_burst_week_does_not_carry_a_quiet_month(self):
        self.assertFalse(watch.passes_totals(self.facts(weeks=[580, 10, 5, 5]), days=28))

    def test_one_quiet_week_is_allowed(self):
        self.assertTrue(watch.passes_totals(self.facts(weeks=[200, 200, 190, 10]), days=28))

    def test_a_new_repository_is_held_only_to_the_weeks_it_has_existed(self):
        now = datetime(2026, 10, 9, tzinfo=timezone.utc)
        young = self.facts(created="2026-09-30T00:00:00Z", commits=3075, weeks=[3075, 0, 0, 0])
        self.assertTrue(watch.passes_totals(young, days=28, now=now))
        self.assertFalse(watch.passes_totals(dict(young, created=None), days=28, now=now))
        self.assertFalse(watch.passes_totals(dict(young, commits=60, weeks=[60, 0, 0, 0]), days=28, now=now))

    def test_forks_archives_and_tiny_code_are_dropped(self):
        for over in (dict(fork=True), dict(archived=True), dict(code_bytes=20 * 1024), dict(commits=100)):
            self.assertFalse(watch.passes_totals(self.facts(**over), days=28), over)


class Recent(unittest.TestCase):
    def test_a_scheduled_job_collapses_to_one_message(self):
        headlines = [f"Auto update playlist Fri Oct  9 17:{m:02d}:44 UTC 2026" for m in range(30)] + \
                    [f"[bot] update tracker.db [skip ci] {n}" for n in range(30)]
        self.assertAlmostEqual(measure.variety(headlines), 2 / 60, places=3)

    def test_counters_and_hashes_are_blanked(self):
        self.assertEqual(measure.template("KVI Update 294023"), measure.template("KVI Update 293851"))
        self.assertEqual(measure.template("Merge 3fa9c2e1b into main"), measure.template("Merge 0d1e2f3a4 into main"))

    def test_a_factory_keeps_its_variety(self):
        headlines = ["challenge.sh: keep the harness's screenshots", "fix(board): stop double render (#412)",
                     "tracker: record mesh severity field", "feat(cli): add fallback verb (#413)"]
        self.assertEqual(measure.variety(headlines), 1.0)

    def recent(self, **over):
        return dict(dict(sampled=100, variety=0.9, lead_human_share=0.95, machine_share=0.5), **over)

    def test_varied_work_by_one_person_passes(self):
        self.assertTrue(watch.passes_recent(self.recent()))
        self.assertTrue(watch.passes_recent(self.recent(lead_human_share=None, machine_share=1.0)))

    def test_repetition_a_team_or_too_few_commits_fail(self):
        for over in (dict(variety=0.1), dict(lead_human_share=0.7), dict(sampled=5)):
            self.assertFalse(watch.passes_recent(self.recent(**over)), over)


class Gate(unittest.TestCase):
    def test_work_through_most_nights_passes(self):
        self.assertTrue(watch.runs_unattended(dict(night_utilization=0.45, nights_covered=5)))

    def test_a_sleeper_or_a_few_long_nights_do_not(self):
        self.assertFalse(watch.runs_unattended(dict(night_utilization=0.05, nights_covered=7)))
        self.assertFalse(watch.runs_unattended(dict(night_utilization=0.9, nights_covered=3)))

    def test_slot_counts_read_like_the_commits_they_count(self):
        end = "2026-10-08T10:00:00Z"
        slots = [3] * 84
        c = measure.slot_clock(slots, end)
        self.assertEqual((c["night_utilization"], c["nights_covered"], c["day_utilization"]), (1.0, 7, 1.0))
        asleep = [0 if i % 12 in (0, 1, 2) else 3 for i in range(84)]
        self.assertEqual(measure.slot_clock(asleep, end)["nights_covered"], 0)


class Admission(unittest.TestCase):
    def test_a_team_is_not_one_person(self):
        self.assertFalse(watch.not_a_team(0.4, 0.0))

    def test_a_fleet_with_no_human_authors_is_not_a_team(self):
        self.assertTrue(watch.not_a_team(None, 1.0))

    def test_the_author_sample_gets_slack_on_the_one_person_test(self):
        self.assertFalse(watch.not_a_team(0.6, 0.0))
        self.assertTrue(watch.not_a_team(0.6, 0.0, threshold=0.8 * 0.6))


class Tiers(unittest.TestCase):
    def row(self, **over):
        row = dict(gates=dict(pr_runs_tests=True, pr_runs_lint=True, pr_runs_typecheck=True, boundary_tools=["ast-grep"],
                              strict_typing=True),
                   structure=dict(test_ratio=1.2, largest_file_kb=80, tenth_largest_file_kb=40),
                   ci=dict(ci_runs=100, green_share=0.9))
        for k, v in over.items():
            row[k] = dict(row[k], **v)
        return row

    def test_gated_and_holding(self):
        self.assertEqual(rubric.tier(self.row())["tier"], "Gated and holding")

    def test_a_red_main_and_a_giant_file_strain_a_gated_repository(self):
        row = self.row(ci=dict(green_share=0.1), structure=dict(largest_file_kb=2000, tenth_largest_file_kb=300))
        self.assertEqual(rubric.tier(row)["tier"], "Gated, under strain")

    def test_no_gates_is_lightly_gated(self):
        row = self.row(gates=dict(pr_runs_tests=False, pr_runs_lint=False, pr_runs_typecheck=False, boundary_tools=[],
                                  strict_typing=False), structure=dict(test_ratio=0.05))
        self.assertEqual(rubric.tier(row)["tier"], "Lightly gated")


class CodeLines(unittest.TestCase):
    LOG = ("\0" + "c1 2026-10-08 2026-10-08T03:00:00-07:00 c0\n:100644 100644 a1 b1 M\tsrc/a.py\n:000000 100644 00 b2 A\tlogo.png\n"
           ":100644 100644 a3 b3 R090\tsrc/old/b.py\tsrc/new/b.py\n\n12\t3\tsrc/a.py\n-\t-\tlogo.png\n4\t0\tsrc/{old => new}/b.py\n"
           "\0" + "c2 2026-10-07 2026-10-07T12:00:00Z c1\n:100644 100644 a4 b4 M\tREADME.md\n\n1\t1\tREADME.md\n")

    def test_log_pairs_blobs_with_line_counts_and_skips_binaries(self):
        self.assertEqual(lines.parse_log(self.LOG), [("c1", "2026-10-08", "src/a.py", 12, 3, "b1"),
                                                     ("c1", "2026-10-08", "src/new/b.py", 4, 0, "b3"),
                                                     ("c2", "2026-10-07", "README.md", 1, 1, "b4")])

    def test_a_commit_without_parents_adds_nothing(self):
        log = "\0" + "c9 2026-10-05 2026-10-05T03:04:11Z \n:000000 100644 00 b9 A\tsrc/all.go\n\n2430775\t0\tsrc/all.go\n" + self.LOG
        self.assertEqual(lines.parse_log(log), lines.parse_log(self.LOG))

    def test_the_clock_reads_only_commits_that_changed_code(self):
        self.assertEqual(lines.code_commit_times(self.LOG, lines.parse_log(self.LOG)), ["2026-10-08T03:00:00-07:00"])

    def test_a_file_rewritten_all_day_counts_by_its_real_growth(self):
        changes = [("c%d" % i, "d", "src/gen.ts", 10000, 9990, "x%d" % i) for i in range(500)] + [("c", "d", "src/app.py", 300, 0, "y")]
        t = lines.tally(changes, days=1)
        self.assertEqual(t["code_added_per_day"], 500 * 10 + 300)
        self.assertEqual(t["gross_source_added_per_day"], 500 * 10000 + 300)

    def test_identical_copies_count_once(self):
        changes = [("c", "d", f"snapshots/v{i}/engine.py", 19238, 0, "same") for i in range(3)]
        t = lines.tally(changes, days=1)
        self.assertEqual(t["code_added_per_day"], 19238)
        self.assertEqual(t["kept_out_per_day"]["copy"], 2 * 19238)

    def test_a_template_batch_is_not_written_code(self):
        changes = [("c", "d", f"plugins/p{i}.py", 18539, 0, f"b{i}") for i in range(8)] + [("c", "d", "src/real.py", 400, 0, "r")]
        t = lines.tally(changes, days=1)
        self.assertEqual(t["code_added_per_day"], 400)
        self.assertEqual(t["kept_out_per_day"]["template"], 8 * 18539)

    def test_docs_and_data_are_not_code(self):
        t = lines.tally([("c", "d", "docs/evidence/index.md", 59000, 0, "1"), ("c", "d", "api/openapi.json", 29000, 0, "2"),
                         ("c", "d", "tests/test_x.py", 200, 0, "3")], days=1)
        self.assertEqual(t["code_added_per_day"], 200)
        self.assertEqual(t["all_added_per_day"], 88200)

    def test_one_large_drop_does_not_carry_the_median_day(self):
        drop = [("c0", "d", "src/import.py", 70000, 0, "x")]
        steady = [(f"c{i}", "d", f"src/m{i}.py", 10000, 0, f"y{i}") for i in range(7)]
        t = lines.tally(drop, 7, days_of={"c0": 3})
        self.assertEqual((t["code_added_per_day"], t["code_added_daily_median"]), (10000, 0))
        t = lines.tally(steady, 7, days_of={f"c{i}": i for i in range(7)})
        self.assertEqual((t["code_added_per_day"], t["code_added_daily_median"], t["code_added_by_day"]), (10000, 10000, [10000] * 7))

    def test_generated_code_is_not_written_code(self):
        t = lines.tally([("c", "d", "pkg/ent/mutation.go", 12418, 0, "1"), ("c", "d", "pkg/hub/server.go", 300, 0, "2")],
                        days=1, made={"pkg/ent/mutation.go"})
        self.assertEqual(t["code_added_per_day"], 300)
        self.assertEqual(t["kept_out_per_day"]["generated"], 12418)

    def test_generators_are_known_by_their_markers_not_by_mentions(self):
        for head in ("// Code generated by ent, DO NOT EDIT.", "# @generated by protoc", "/* auto-generated file */"):
            self.assertTrue(lines.GENERATED.search(head), head)
        for head in ("# Generated with Claude Code", '"""Generate ideas from a seed."""', "// generated_ids are cached"):
            self.assertFalse(lines.GENERATED.search(head), head)

    def test_generated_reads_the_newest_version_of_each_code_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            git = ["git", "-c", "user.name=t", "-c", "user.email=t@t", "-C", tmp]
            lines.subprocess.run(git + ["init", "-q"], check=True)
            files = {"gen.go": "// Code generated by ent, DO NOT EDIT.\npackage ent\n", "app.go": "package app\n",
                     "notes.md": "<!-- DO NOT EDIT -->\n"}
            for name, text in files.items():
                Path(tmp, name).write_text(text)
            lines.subprocess.run(git + ["add", "."], check=True)
            lines.subprocess.run(git + ["commit", "-qm", "x"], check=True)
            blob = lambda n: lines.subprocess.run(git + ["rev-parse", f"HEAD:{n}"], check=True, capture_output=True,
                                                  text=True).stdout.strip()
            changes = [("c", "d", n, 2, 0, blob(n)) for n in files] + [("c", "d", "gone.go", 0, 5, "0" * 40)]
            self.assertEqual(lines.generated(Path(tmp, ".git"), changes), {"gen.go"})


class Grades(unittest.TestCase):
    def row(self, **over):
        row = dict(volume=dict(added_per_day=4000, merged_prs_per_day=30),
                   code_lines=dict(status="ok", code_added_daily_median=45000),
                   clock=dict(quietest_6h_share=0.24, day_utilization=0.95, nights_seen=7, nights_covered=7, active_days=7), prs=dict(peak_open_prs=1),
                   ci=dict(ci_runs=50, green_share=0.95), structure=dict(largest_file_kb=80, test_ratio=1.0),
                   gates=dict(pr_runs_tests=True, pr_runs_lint=True, pr_runs_typecheck=True))
        for k, v in over.items():
            row[k] = dict(row[k], **v)
        return row

    def test_each_axis_grades_on_its_own(self):
        g = grade.grades(self.row(clock=dict(quietest_6h_share=0.0, active_days=7)))
        self.assertEqual({a: g[a]["grade"] for a in grade.AXES}, dict(output="A", autonomy="F", discipline="A"))

    def test_one_miss_drops_a_letter_and_names_the_miss(self):
        g = grade.grade(self.row(clock=dict(quietest_6h_share=0.21)), "autonomy")
        self.assertEqual(g, dict(grade="B", missing={"night_utilization": dict(want=0.9, has=0.84)}))

    def test_night_utilization_is_the_quietest_hours_against_an_even_spread(self):
        self.assertEqual(grade.value(self.row(clock=dict(quietest_6h_share=0.25)), "night_utilization"), 1.0)
        self.assertEqual(grade.grade(self.row(clock=dict(quietest_6h_share=0.149)), "autonomy")["grade"], "F")
        self.assertEqual(grade.grade(self.row(clock=dict(quietest_6h_share=0.15)), "autonomy")["grade"], "D")

    def test_autonomy_needs_every_night(self):
        g = grade.grade(self.row(clock=dict(nights_covered=6)), "autonomy")
        self.assertEqual(g["grade"], "C")

    def test_autonomy_reads_the_code_commits_clock_when_the_clone_has_one(self):
        row = self.row(code_lines=dict(clock=dict(quietest_6h_share=0.1, day_utilization=0.95, nights_seen=7, nights_covered=7)))
        self.assertEqual(grade.value(row, "night_utilization"), 0.4)

    def test_autonomy_needs_both_round_the_clock_and_every_day(self):
        g = grade.grade(self.row(clock=dict(day_utilization=0.65)), "autonomy")
        self.assertEqual(g, dict(grade="D", missing={"day_utilization": dict(want=0.7, has=0.65)}))

    def test_serial_work_is_not_marked_down_for_one_open_pull_request_at_a_time(self):
        self.assertEqual(grade.grade(self.row(), "autonomy")["grade"], "A")

    def test_meeting_nothing_is_f_and_names_what_e_needs(self):
        g = grade.grade(self.row(code_lines=dict(code_added_daily_median=100)), "output")
        self.assertEqual(g, dict(grade="F", missing={"code_added_daily_median": dict(want=1000, has=100)}))


class Citations(unittest.TestCase):
    def test_counts_only_real_files_and_lines_inside_the_folder(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / "repo" / "src").mkdir(parents=True)
            (folder / "repo" / "src" / "a.py").write_text("one\ntwo\nthree\n")
            evidence = [dict(path="repo/src/a.py", line=2, note=""), dict(path="src/a.py", line=3, note=""),
                        dict(path="repo/src/a.py", line=99, note=""), dict(path="repo/missing.py", line=1, note=""),
                        dict(path="../../etc/passwd", line=1, note="")]
            j = dict(dimensions=dict(architecture=dict(evidence=evidence)))
            self.assertEqual(judge.verify(j, folder), dict(citations=5, valid=2, share=0.4))


if __name__ == "__main__":
    unittest.main()
