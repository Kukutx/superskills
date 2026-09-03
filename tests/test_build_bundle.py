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
        self.write("skills/meta/skill-router/skill.md", "# Router\n")
        self.write("skills/development/foo/skill.md", "# Foo\n")
        self.write("skills/development/foo/references/details.md", "# Details\n")
        self.write("skills/development/foo/maintenance/sources.md", "SECRET\n")

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
        self.assertTrue((output / "skills/meta/skill-router/skill.md").is_file())
        self.assertTrue((output / "skills/development/foo/skill.md").is_file())
        self.assertTrue((output / "skills/development/foo/references/details.md").is_file())
        self.assertFalse((output / "skills/development/foo/maintenance/sources.md").exists())

        manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(BUNDLE_FORMAT, manifest["format"])
        self.assertEqual(["development/foo"], manifest["skills"])
        self.assertEqual(["development/foo:details.md"], manifest["references"])
        self.assertTrue(all("/maintenance/" not in f"/{item['path']}/" for item in manifest["files"]))

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
