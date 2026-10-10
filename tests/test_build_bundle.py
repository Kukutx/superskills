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
        self.write("skills/skill-router/SKILL.md", "# Router\n")
        self.write("skills/foo/SKILL.md", "# Foo\n")
        self.write("skills/foo/references/details.md", "# Details\n")
        self.write("skills/foo/maintenance/sources.md", "SECRET\n")

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
            skills=["foo"],
            references=["foo:details"],
            output=output,
        )

        self.assertEqual(output.resolve(), summary.output)
        self.assertTrue((output / "gpts/test/project-instructions.md").is_file())
        self.assertTrue((output / "skills/skill-router/SKILL.md").is_file())
        self.assertTrue((output / "skills/foo/SKILL.md").is_file())
        self.assertTrue((output / "skills/foo/references/details.md").is_file())
        self.assertFalse((output / "skills/foo/maintenance/sources.md").exists())

        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(BUNDLE_FORMAT, manifest["format"])
        self.assertEqual(["foo"], manifest["skills"])
        self.assertEqual(["foo:details.md"], manifest["references"])
        self.assertTrue(all("/maintenance/" not in f"/{item['path']}/" for item in manifest["files"]))

    def test_reference_requires_selected_owner(self) -> None:
        with self.assertRaisesRegex(BundleError, "is not selected"):
            build_bundle(
                root=self.root,
                profile="gpts/test",
                skills=["skill-router"],
                references=["foo:details"],
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
                skills=["foo"],
                output=output,
            )
        self.assertEqual("keep", (output / "unrelated.txt").read_text(encoding="utf-8"))

    def test_known_bundle_can_be_rebuilt(self) -> None:
        output = self.root / "out"
        for _ in range(2):
            build_bundle(
                root=self.root,
                profile="gpts/test",
                skills=["foo"],
                output=output,
            )
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(BUNDLE_FORMAT, manifest["format"])

    def test_all_skills_includes_every_skill_and_reference(self) -> None:
        output = self.root / "out"
        build_bundle(root=self.root, profile="gpts/test", skills=[], all_skills=True, output=output)
        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(["foo", "skill-router"], manifest["skills"])
        self.assertEqual(["foo:details.md"], manifest["references"])
        self.assertFalse((output / "skills/foo/maintenance/sources.md").exists())


if __name__ == "__main__":
    unittest.main()
