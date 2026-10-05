from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.build_live_evals import LiveEvalError, build

FOO_EVALS = (
    "# Evals\n\n| ID | Prompt | Primary | Secondary | Must avoid |\n"
    "| --- | --- | --- | --- | --- |\n"
    "| foo-001 | “线上报错，为什么？” | `development/foo` | none | inventing a stack trace |\n"
    "| foo-002 | “8 向移动” | `details.md` | none | none |\n"
    "| foo-003 | 用户已经上传完整日志。 | `development/foo` | none | none |\n"
    "| foo-004 | “改一下动画” | matching runtime owner | none | none |\n"
    "| foo-005 | “帮我 review 这个 PR” | `development/bar` | none | foo as a substitute for review |\n"
    "| foo-006 | “把按钮文案改成发布” | none | none | foo for a plain copy change |\n"
    "| foo-007 | “随便聊聊” | none | none | nothing named here |\n"
)
ROUTER_EVALS = (
    "# Evals\n\n| ID | Prompt | Primary | Secondary | Must avoid |\n"
    "| --- | --- | --- | --- | --- |\n"
    "| router-001 | “这个接口为什么 500？” | `development/foo` | none | bar instead of reproduction |\n"
    "| router-002 | “找 5 个跳伞视频” | `research/finder` | none | none |\n"
)


class BuildLiveEvalsTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for route in ("development/foo", "development/bar", "meta/skill-router", "research/finder"):
            category, name = route.split("/")
            self.write(
                f"plugins/{category}/skills/{name}/SKILL.md",
                f"---\nname: {name}\ndescription: Test.\n---\n",
            )
        self.write("plugins/development/skills/foo/references/details.md", "# Details\n")
        self.write("maintenance/development/foo/behavioral-evals.md", FOO_EVALS)
        self.write("maintenance/meta/skill-router/behavioral-evals.md", ROUTER_EVALS)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def read(self, relative: str) -> str:
        return (self.root / "dist/live-evals" / relative).read_text(encoding="utf-8")

    def test_rows_are_classified_and_context_dependent_rows_are_skipped(self) -> None:
        cases = {case.case_id: case.kind for case in build(self.root)}
        self.assertEqual(
            {
                "foo-001": "behavior",
                "foo-002": "reference",
                "foo-005": "route",
                "foo-006": "negative",
                "router-001": "route",
                "router-002": "route",
            },
            cases,
        )

    def test_only_research_routes_get_web_tools_and_a_web_tag(self) -> None:
        build(self.root)
        web = self.read("evals/router-002/prompt.md")
        self.assertIn("allowed_tools: [Skill, Read, Glob, Grep, WebSearch, WebFetch]", web)
        self.assertIn("tags: [route, web]", web)
        plain = self.read("evals/router-001/prompt.md")
        self.assertNotIn("WebSearch", plain)
        self.assertIn("tags: [route]", plain)

    def test_route_case_uses_bare_utterance_and_forbids_named_neighbor(self) -> None:
        build(self.root)
        self.assertTrue(self.read("evals/router-001/prompt.md").rstrip().endswith("\n这个接口为什么 500？"))
        self.assertIn('(?:[\\w-]+:)?foo"', self.read("evals/router-001/graders/route.md"))
        forbidden = self.read("evals/router-001/graders/avoid-bar.md")
        self.assertIn('(?:[\\w-]+:)?bar"', forbidden)
        self.assertIn("max: 0", forbidden)

    def test_route_to_another_skill_from_a_skill_table_is_a_cold_route(self) -> None:
        build(self.root)
        self.assertTrue(self.read("evals/foo-005/prompt.md").rstrip().endswith("\n帮我 review 这个 PR"))
        self.assertIn('(?:[\\w-]+:)?bar"', self.read("evals/foo-005/graders/route.md"))
        self.assertIn("max: 0", self.read("evals/foo-005/graders/avoid-foo.md"))

    def test_negative_case_only_forbids_the_skills_named_in_must_avoid(self) -> None:
        build(self.root)
        self.assertTrue(self.read("evals/foo-006/prompt.md").rstrip().endswith("\n把按钮文案改成发布"))
        graders = sorted(path.name for path in (self.root / "dist/live-evals/evals/foo-006/graders").iterdir())
        self.assertEqual(["avoid-foo.md"], graders)
        self.assertIn("max: 0", self.read("evals/foo-006/graders/avoid-foo.md"))
        self.assertFalse((self.root / "dist/live-evals/evals/foo-007").exists())

    def test_behavior_case_names_owner_and_judges_must_avoid(self) -> None:
        build(self.root)
        self.assertIn("使用 foo Skill 处理这个任务：线上报错，为什么？", self.read("evals/foo-001/prompt.md"))
        judge = self.read("evals/foo-001/graders/behavior.md")
        self.assertIn("type: llm", judge)
        self.assertIn("inventing a stack trace", judge)

    def test_reference_case_names_owner_and_requires_the_reference_read(self) -> None:
        build(self.root)
        self.assertIn("使用 foo Skill 处理这个任务：8 向移动", self.read("evals/foo-002/prompt.md"))
        grader = self.read("evals/foo-002/graders/reference.md")
        self.assertIn("tool: Read", grader)
        self.assertIn("details", grader)

    def test_plugin_is_flat_and_carries_only_runtime_files(self) -> None:
        build(self.root)
        output = self.root / "dist/live-evals"
        manifest = json.loads((output / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertNotIn("skills", manifest)
        self.assertTrue((output / "skills/foo/references/details.md").is_file())
        self.assertTrue((output / "skills/skill-router/SKILL.md").is_file())
        self.assertFalse(any(path.name == "behavioral-evals.md" for path in (output / "skills").rglob("*")))

    def test_only_builds_the_selected_cases_and_rejects_unreplayable_ids(self) -> None:
        self.assertEqual(["foo-002"], [case.case_id for case in build(self.root, only=["foo-002"])])
        self.assertEqual(["foo-002"], [path.name for path in (self.root / "dist/live-evals/evals").iterdir()])
        with self.assertRaisesRegex(LiveEvalError, "foo-003"):
            build(self.root, only=["foo-003"])

    def test_output_must_be_a_generated_directory_under_dist(self) -> None:
        for output in (self.root.parent, self.root / "plugins", self.root / "dist"):
            with self.assertRaises(LiveEvalError):
                build(self.root, output)
        self.assertTrue((self.root / "plugins/development/skills/foo/SKILL.md").is_file())

    def test_rebuild_drops_stale_cases_but_keeps_earlier_run_reports(self) -> None:
        build(self.root)
        report = self.root / "dist/live-evals/evals/results/2026-01-01/report.html"
        report.parent.mkdir(parents=True)
        report.write_text("report", encoding="utf-8")
        build(self.root, only=["foo-002"])
        self.assertEqual(["foo-002", "results"], sorted(path.name for path in report.parents[2].iterdir()))
        self.assertTrue(report.is_file())


if __name__ == "__main__":
    unittest.main()
