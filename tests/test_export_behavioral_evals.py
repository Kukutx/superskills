from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.export_behavioral_evals import EvalExportError, export_cases


class EvalExporterTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_eval(self, route: str, content: str) -> None:
        path = self.root / "skills" / route / "maintenance" / "behavioral-evals.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_exports_header_aliases_to_one_shape(self) -> None:
        self.write_eval(
            "meta/skill-router",
            "# Evals\n\n| Case | User task | Expected primary | Secondary only when | Must avoid |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| router-001 | 帮我写简历 | `writing/resume-writing` | none | inventing facts |\n",
        )
        records = export_cases(self.root)
        self.assertEqual(1, len(records))
        self.assertEqual("router-001", records[0]["id"])
        self.assertEqual("帮我写简历", records[0]["prompt"])
        self.assertEqual("writing/resume-writing", records[0]["primary"])
        self.assertEqual("meta/skill-router", records[0]["source_skill"])

    def test_requires_at_least_one_parseable_case(self) -> None:
        self.write_eval("development/foo", "# Narrative only\n")
        with self.assertRaisesRegex(EvalExportError, "no parseable"):
            export_cases(self.root)

    def test_duplicate_explicit_ids_fail(self) -> None:
        table = (
            "# Evals\n\n| ID | Prompt | Primary |\n"
            "| --- | --- | --- |\n"
            "| duplicate | one | a/b |\n"
            "| duplicate | two | a/b |\n"
        )
        self.write_eval("development/foo", table)
        with self.assertRaisesRegex(EvalExportError, "duplicate behavioral eval IDs"):
            export_cases(self.root)


if __name__ == "__main__":
    unittest.main()
