from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.eval_coverage import coverage_report, main


class EvalCoverageTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write_skill("development/foo")
        self.write_skill("development/bar")
        self.write(
            "maintenance/development/foo/behavioral-evals.md",
            "# Foo behavioral evals\n\n"
            "| ID | Prompt | Primary | Secondary | Must avoid |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| foo-001 | test | `development/foo` | none | none |\n",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_skill(self, route: str) -> None:
        category, name = route.split("/", 1)
        self.write(
            f"plugins/{category}/skills/{name}/SKILL.md",
            f"---\nname: {name}\ndescription: Test {name}.\n---\n\n# {name.title()}\n",
        )

    def test_report_lists_skills_without_maintenance_and_without_rows(self) -> None:
        report = coverage_report(self.root)
        self.assertEqual(2, report.total_skills)
        self.assertEqual(["development/bar"], report.no_maintenance)
        self.assertEqual(["development/bar"], report.no_eval_rows)
        self.assertEqual(1, report.with_eval_rows)
        self.assertEqual(1, report.total_eval_rows)
        self.assertEqual([], report.categories_without_evals)

    def test_main_runs_and_exits_zero(self) -> None:
        self.assertEqual(0, main(["--root", str(self.root)]))


if __name__ == "__main__":
    unittest.main()
