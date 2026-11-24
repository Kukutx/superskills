from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.build_manifests import write_manifests
from tools.validate_repo import validate_repository


class ValidatorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.add_skill("development/foo")
        self.write_router(["development/foo"])
        for category in ("development", "meta"):
            self.write_plugin(category)
        write_manifests(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def write_plugin(self, category: str, **overrides: str) -> None:
        manifest = {"name": f"superskills-{category}", "version": "1.0.0", "description": f"Test {category}."}
        self.write(f"plugins/{category}/plugin.json", json.dumps({**manifest, **overrides}))

    def add_skill(self, route: str, body: str = "# Foo\n", description: str | None = None) -> Path:
        category, name = route.split("/", 1)
        path = self.write(
            f"plugins/{category}/skills/{name}/SKILL.md",
            f"---\nname: {name}\ndescription: {description or f'Test {name}.'}\n---\n\n{body}",
        )
        self.write(
            f"plugins/{category}/skills/{name}/skill.yaml",
            f"name: {name}\ntitle: {name.replace('-', ' ').title()}\n"
            f"description: {description or f'Test {name}.'}\ncategory: {category}\n"
            "include_in_prompt: false\ntriggers:\n"
            f"- {name.replace('-', ' ')}\n",
        )
        return path

    def write_router(self, routes: list[str], suffix: str = "") -> None:
        rows = "\n".join(f"| test | `{route}` |" for route in routes)
        self.write(
            "plugins/meta/skills/skill-router/SKILL.md",
            "---\nname: skill-router\ndescription: Route tests.\n---\n\n"
            "# Router\n\n## Catalog\n\n| Intent | Skill |\n| --- | --- |\n"
            f"{rows}\n\n## Boundaries\n\n{suffix}\n",
        )
        self.write(
            "plugins/meta/skills/skill-router/skill.yaml",
            "name: skill-router\ntitle: Router\ndescription: Route tests.\n"
            "category: meta\ninclude_in_prompt: false\ntriggers:\n- skill router\n",
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
            "plugins/development/skills/foo/nested/SKILL.md",
            "---\nname: nested\ndescription: Invalid.\n---\n",
        )
        self.assertIn("malformed Skill entrypoint", self.error_text())

    def test_lowercase_entrypoint_fails(self) -> None:
        entrypoint = self.root / "plugins/development/skills/foo/SKILL.md"
        entrypoint.rename(entrypoint.with_name("renamed.md"))
        entrypoint.with_name("renamed.md").rename(entrypoint.with_name("skill.md"))
        self.assertIn("malformed Skill entrypoint", self.error_text())

    def test_description_over_web_upload_limit_fails(self) -> None:
        self.add_skill("development/foo", description="x" * 201)
        self.assertIn("description is 201 characters; the limit is 200", self.error_text())

    def test_description_that_breaks_yaml_fails(self) -> None:
        self.add_skill("development/foo", description="Godot work: movement and camera.")
        self.assertIn("plain YAML scalar", self.error_text())

    def test_extra_frontmatter_key_fails(self) -> None:
        self.write(
            "plugins/development/skills/foo/SKILL.md",
            "---\nname: foo\ndescription: Test.\nmetadata: x\n---\n\n# Foo\n",
        )
        self.assertIn("frontmatter only allows name and description", self.error_text())

    def test_same_skill_name_in_two_plugins_fails(self) -> None:
        self.add_skill("meta/foo")
        self.write_router(["development/foo", "meta/foo"])
        self.assertIn("duplicate frontmatter skill name 'foo'", self.error_text())

    def test_plugin_manifest_name_must_match_category(self) -> None:
        self.write_plugin("development", name="something-else")
        self.assertIn("name must be 'superskills-development'", self.error_text())

    def test_plugins_must_share_one_version(self) -> None:
        self.write_plugin("development", version="2.0.0")
        self.assertIn("plugins must share one version", self.error_text())

    def test_stale_marketplace_manifest_fails(self) -> None:
        self.write_plugin("development", description="Changed after generation.")
        self.assertIn("marketplace manifests are out of date", self.error_text())

    def test_unexpected_plugin_entry_fails(self) -> None:
        self.write("plugins/development/notes.md", "# Notes\n")
        self.assertIn("unexpected entries ['notes.md']", self.error_text())

    def test_orphan_reference_requires_real_discovery_path(self) -> None:
        self.write("plugins/development/skills/foo/references/details.md", "# Details\n")
        self.add_skill("development/foo", "# Foo\n\nDetails: details.md\n<!-- `references/details.md` -->\n")
        self.assertIn("orphan runtime reference", self.error_text())

    def test_standard_markdown_reference_link_is_accepted(self) -> None:
        self.write("plugins/development/skills/foo/references/details.md", "# Details\n")
        self.add_skill("development/foo", "# Foo\n\nRead [details](references/details.md).\n")
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)

    def test_broken_standard_markdown_link_fails(self) -> None:
        self.add_skill("development/foo", "# Foo\n\nRead [missing](references/missing.md).\n")
        self.assertIn("broken Markdown path references/missing.md", self.error_text())

    def test_maintenance_file_cannot_live_in_references(self) -> None:
        self.write("plugins/development/skills/foo/references/sources.md", "# Sources\n")
        self.add_skill("development/foo", "# Foo\n\nRead `references/sources.md`.\n")
        self.assertIn("maintenance material is in references", self.error_text())

    def test_maintenance_directory_inside_skill_fails(self) -> None:
        self.write("plugins/development/skills/foo/maintenance/sources.md", "# Sources\n")
        self.assertIn("unexpected entries ['maintenance']", self.error_text())

    def test_runtime_file_cannot_link_to_maintenance(self) -> None:
        self.write("maintenance/development/foo/sources.md", "# Sources\n")
        self.add_skill("development/foo", "# Foo\n\nSee `maintenance/development/foo/sources.md`.\n")
        self.assertIn("runtime file links to maintenance material", self.error_text())

    def test_maintenance_without_matching_skill_fails(self) -> None:
        self.write("maintenance/development/retired/sources.md", "# Sources\n")
        self.assertIn("maintenance has no matching Skill development/retired", self.error_text())

    def test_behavioral_eval_missing_local_route_fails(self) -> None:
        self.write(
            "maintenance/development/foo/behavioral-evals.md",
            "# Evals\n\n| ID | Prompt | Primary | Secondary | Must avoid |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| foo-001 | test | `development/missing` | none | none |\n",
        )
        self.assertIn("references missing local Skill development/missing", self.error_text())

    def test_legacy_behavioral_eval_headers_fail(self) -> None:
        self.write(
            "maintenance/development/foo/behavioral-evals.md",
            "# Evals\n\n| Prompt | Expected route | Must avoid |\n"
            "| --- | --- | --- |\n"
            "| test | `development/foo` | none |\n",
        )
        self.assertIn("must contain a canonical", self.error_text())

    def test_unknown_maintenance_file_fails(self) -> None:
        self.write("maintenance/development/foo/examples.md", "# Examples\n")
        self.assertIn("unsupported maintenance file", self.error_text())

    def test_missing_frontmatter_is_reported(self) -> None:
        self.write("plugins/development/skills/foo/SKILL.md", "# No metadata\n")
        text = self.error_text()
        self.assertIn("missing opening frontmatter delimiter", text)
        self.assertIn("missing frontmatter name", text)

    def test_reserved_word_in_name_fails(self) -> None:
        self.add_skill("development/claude-helper")
        self.write_router(["development/foo", "development/claude-helper"])
        self.assertIn("reserved word", self.error_text())

    def test_description_with_xml_tag_fails(self) -> None:
        self.add_skill("development/foo", description="Use <example> tags.")
        self.assertIn("must not contain XML tags", self.error_text())

    def test_long_entrypoint_is_an_advisory_not_an_error(self) -> None:
        self.add_skill("development/foo", "line\n" * 501)
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)
        self.assertTrue(any("exceeds 500 lines" in warning for warning in result.warnings))

    def write_authored_eval(self, case: str = "foo-honest", skill: str = "foo") -> None:
        base = f"maintenance/development/foo/evals/{case}"
        self.write(f"{base}/prompt.md", "---\ndescription: foo stays honest\nruns: 2\n---\n\nDo the task.\n")
        self.write(
            f"{base}/graders/skill-fired.md",
            f"---\ntype: tool_used\ntool: Skill\ninput_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'\n---\n",
        )
        self.write(f"{base}/graders/honest.md", "---\ntype: llm\n---\n\nPASS if honest.\n")

    def test_authored_eval_case_passes(self) -> None:
        self.write_authored_eval()
        result = validate_repository(self.root)
        self.assertTrue(result.ok, result.errors)

    def test_authored_eval_case_needs_prompt_and_graders(self) -> None:
        self.write("maintenance/development/foo/evals/empty-case/notes.md", "# Notes\n")
        text = self.error_text()
        self.assertIn("unexpected entries ['notes.md']", text)
        self.assertIn("eval case is missing prompt.md", text)
        self.assertIn("needs at least one grader", text)

    def test_authored_eval_grader_must_name_an_existing_skill(self) -> None:
        self.write_authored_eval(skill="retired-skill")
        self.assertIn("input_match does not name an existing Skill", self.error_text())

    def test_authored_eval_id_cannot_reuse_a_table_id(self) -> None:
        self.write_authored_eval(case="foo-001")
        self.write(
            "maintenance/development/foo/behavioral-evals.md",
            "# Evals\n\n| ID | Prompt | Primary | Secondary | Must avoid |\n"
            "| --- | --- | --- | --- | --- |\n"
            "| foo-001 | test | `development/foo` | none | none |\n",
        )
        self.assertIn("also used by behavioral eval tables: ['foo-001']", self.error_text())

    def test_missing_skill_yaml_fails(self) -> None:
        (self.root / "plugins/development/skills/foo/skill.yaml").unlink()
        self.assertIn("missing skill.yaml", self.error_text())

    def test_drifted_skill_yaml_fails(self) -> None:
        self.write(
            "plugins/development/skills/foo/skill.yaml",
            "name: foo\ntitle: Foo\ndescription: Something else.\n"
            "category: development\ninclude_in_prompt: false\ntriggers:\n- foo\n",
        )
        self.assertIn("description drifted from SKILL.md", self.error_text())

    def test_other_nested_maintenance_directory_fails(self) -> None:
        self.write("maintenance/development/foo/drafts/notes.md", "# Notes\n")
        self.assertIn("nested maintenance directories are not supported", self.error_text())


if __name__ == "__main__":
    unittest.main()
