from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.validate_repo import validate_repository


class ValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.add_skill("development/foo")
        self.write_router(["development/foo"])

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def add_skill(self, route: str, body: str = "# Foo\n") -> Path:
        category, name = route.split("/", 1)
        return self.write(
            f"skills/{route}/skill.md",
            f"---\nname: {name}\ndescription: Test {name}.\n---\n\n{body}",
        )

    def write_router(self, routes: list[str], suffix: str = "") -> None:
        rows = "\n".join(f"| test | `{route}` |" for route in routes)
        self.write(
            "skills/meta/skill-router/skill.md",
            "---\nname: skill-router\ndescription: Route tests.\n---\n\n"
            "# Router\n\n## Catalog\n\n| Intent | Skill |\n| --- | --- |\n"
            f"{rows}\n\n## Boundaries\n\n{suffix}\n",
        )

    def error_text(self) -> str:
        return "\n".join(validate_repository(self.root).errors)

    def test_valid_repository_passes(self) -> None:
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertEqual(2, result.skill_count)

    def test_catalog_does_not_accept_route_mentioned_outside_catalog(self) -> None:
        self.write_router([], suffix="Use `development/foo` for this case.")
        self.assertIn("Catalog missing", self.error_text())

    def test_duplicate_catalog_route_fails(self) -> None:
        self.write_router(["development/foo", "development/foo"])
        self.assertIn("Catalog duplicates", self.error_text())

    def test_stale_catalog_route_fails(self) -> None:
        self.write_router(["development/foo", "development/missing"])
        self.assertIn("Catalog references missing", self.error_text())

    def test_malformed_nested_skill_entrypoint_fails(self) -> None:
        self.write(
            "skills/development/foo/nested/skill.md",
            "---\nname: nested\ndescription: Invalid.\n---\n",
        )
        self.assertIn("malformed Skill entrypoint", self.error_text())

    def test_orphan_reference_requires_real_discovery_path(self) -> None:
        self.write("skills/development/foo/references/details.md", "# Details\n")
        self.add_skill("development/foo", "# Foo\n\nDetails: details.md\n<!-- `references/details.md` -->\n")
        self.assertIn("orphan runtime reference", self.error_text())

    def test_standard_markdown_reference_link_is_accepted(self) -> None:
        self.write("skills/development/foo/references/details.md", "# Details\n")
        self.add_skill("development/foo", "# Foo\n\nRead [details](references/details.md).\n")
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)

    def test_broken_standard_markdown_link_fails(self) -> None:
        self.add_skill("development/foo", "# Foo\n\nRead [missing](references/missing.md).\n")
        self.assertIn("broken Markdown path references/missing.md", self.error_text())

    def test_maintenance_file_cannot_live_in_references(self) -> None:
        self.write("skills/development/foo/references/sources.md", "# Sources\n")
        self.add_skill("development/foo", "# Foo\n\nRead `references/sources.md`.\n")
        self.assertIn("maintenance material is in references", self.error_text())

    def test_behavioral_eval_missing_local_route_fails(self) -> None:
        self.write(
            "skills/development/foo/maintenance/behavioral-evals.md",
            "# Evals\n\n| ID | Prompt | Primary | Secondary | Must avoid |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| foo-001 | test | `development/missing` | none | none |\n",
        )
        self.assertIn("references missing local Skill development/missing", self.error_text())

    def test_legacy_behavioral_eval_headers_fail(self) -> None:
        self.write(
            "skills/development/foo/maintenance/behavioral-evals.md",
            "# Evals\n\n| Prompt | Expected route | Must avoid |\n"
            "| --- | --- | --- |\n"
            "| test | `development/foo` | none |\n",
        )
        self.assertIn("must contain a canonical", self.error_text())

    def test_unknown_maintenance_file_fails(self) -> None:
        self.write("skills/development/foo/maintenance/examples.md", "# Examples\n")
        self.assertIn("unsupported maintenance file", self.error_text())

    def test_missing_frontmatter_is_reported(self) -> None:
        self.write("skills/development/foo/skill.md", "# No metadata\n")
        text = self.error_text()
        self.assertIn("missing opening frontmatter delimiter", text)
        self.assertIn("missing frontmatter name", text)


if __name__ == "__main__":
    unittest.main()
