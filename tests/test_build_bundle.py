from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.build_bundle import BUNDLE_FORMAT, BundleError, build_bundle


class BundleBuilderTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.write("gpts/test/project-instructions.md", "# Instructions\n")
        self.write("plugins/meta/skills/skill-router/SKILL.md", "# Router\n")
        self.write("plugins/development/skills/foo/SKILL.md", "# Foo\n")
        self.write("plugins/development/skills/foo/references/details.md", "# Details\n")
        self.write("maintenance/development/foo/sources.md", "SECRET\n")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def test_builds_minimal_bundle_and_excludes_maintenance(self) -> None:
        output = self.root / "dist" / "test"
        summary = build_bundle(
            root=self.root,
            profile="gpts/test",
            skills=["development/foo"],
            references=["development/foo:details"],
            output=output,
        )

        self.assertEqual(output.resolve(), summary.output)
        self.assertTrue((output / "gpts/test/project-instructions.md").is_file())
        self.assertTrue((output / "plugins/meta/skills/skill-router/SKILL.md").is_file())
        self.assertTrue((output / "plugins/development/skills/foo/SKILL.md").is_file())
        self.assertTrue((output / "plugins/development/skills/foo/references/details.md").is_file())
        self.assertFalse((output / "maintenance").exists())

        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(BUNDLE_FORMAT, manifest["format"])
        self.assertEqual(["development/foo"], manifest["skills"])
        self.assertEqual(["development/foo:details.md"], manifest["references"])
        self.assertTrue(all("/maintenance/" not in f"/{item['path']}/" for item in manifest["files"]))

    def test_category_brings_every_skill_and_reference_in_it(self) -> None:
        self.write("plugins/development/skills/bar/SKILL.md", "# Bar\n")
        self.write("plugins/writing/skills/baz/SKILL.md", "# Baz\n")
        output = self.root / "out"
        build_bundle(root=self.root, profile="gpts/test", category_names=["development"], output=output)

        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(["development"], manifest["categories"])
        self.assertEqual(["development/bar", "development/foo"], manifest["skills"])
        self.assertEqual(["development/foo:details.md"], manifest["references"])
        self.assertTrue((output / "plugins/development/skills/foo/references/details.md").is_file())
        self.assertFalse((output / "plugins/writing").exists())
        self.assertFalse((output / "maintenance").exists())

    def test_category_and_single_skills_combine(self) -> None:
        self.write("plugins/writing/skills/baz/SKILL.md", "# Baz\n")
        output = self.root / "out"
        build_bundle(
            root=self.root,
            profile="gpts/test",
            skills=["writing/baz"],
            category_names=["development"],
            output=output,
        )
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(["development/foo", "writing/baz"], manifest["skills"])

    def test_router_catalog_lists_only_bundled_skills(self) -> None:
        self.write("plugins/writing/skills/baz/SKILL.md", "# Baz\n")
        self.write(
            "plugins/meta/skills/skill-router/SKILL.md",
            "# Router\n\n## Catalog\n\n| Intent | Skill |\n| --- | --- |\n"
            "| do foo | `development/foo` |\n| do baz | `writing/baz` |\n\n"
            "## Important boundaries\n\nfoo -> foo; baz -> baz\n",
        )
        output = self.root / "out"
        build_bundle(root=self.root, profile="gpts/test", skills=["development/foo"], output=output)
        router = (output / "plugins/meta/skills/skill-router/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("| do foo | `development/foo` |", router)
        self.assertNotIn("`writing/baz`", router)
        self.assertIn("carries only the Skills listed above", router)
        self.assertIn("## Important boundaries\n\nfoo -> foo; baz -> baz\n", router)

        build_bundle(
            root=self.root, profile="gpts/test", skills=["development/foo", "writing/baz"], output=output
        )
        router = (output / "plugins/meta/skills/skill-router/SKILL.md").read_text(encoding="utf-8")
        self.assertIn("`writing/baz`", router)
        self.assertNotIn("carries only the Skills listed above", router)

    def test_unknown_category_and_empty_selection_fail(self) -> None:
        with self.assertRaisesRegex(BundleError, "category does not exist: finance"):
            build_bundle(root=self.root, profile="gpts/test", category_names=["finance"], output=self.root / "out")
        with self.assertRaisesRegex(BundleError, "at least one --skill or --category"):
            build_bundle(root=self.root, profile="gpts/test", output=self.root / "out")

    def test_reference_requires_selected_owner(self) -> None:
        with self.assertRaisesRegex(BundleError, "is not selected"):
            build_bundle(
                root=self.root,
                profile="gpts/test",
                skills=["meta/skill-router"],
                references=["development/foo:details"],
                output=self.root / "out",
            )

    def test_refuses_to_replace_unknown_directory(self) -> None:
        output = self.root / "out"
        output.mkdir()
        (output / "unrelated.txt").write_text("keep", encoding="utf-8")
        with self.assertRaisesRegex(BundleError, "refusing to replace"):
            build_bundle(
                root=self.root,
                profile="gpts/test",
                skills=["development/foo"],
                output=output,
            )
        self.assertEqual("keep", (output / "unrelated.txt").read_text(encoding="utf-8"))

    def test_known_bundle_can_be_rebuilt(self) -> None:
        output = self.root / "out"
        for _ in range(2):
            build_bundle(
                root=self.root,
                profile="gpts/test",
                skills=["development/foo"],
                output=output,
            )
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(BUNDLE_FORMAT, manifest["format"])


if __name__ == "__main__":
    unittest.main()
