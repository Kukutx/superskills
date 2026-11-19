from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

from tools.build_manifests import ManifestError, set_version, stale_manifests, write_manifests
from tools.package_web_skills import PackageError, package


class DistributionTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for category in ("development", "writing"):
            self.write_plugin(category, f"Test {category}.")
        self.write("plugins/writing/skills/resume-writing/SKILL.md", "---\nname: resume-writing\ndescription: Test.\n---\n")
        self.write("plugins/development/skills/foo/SKILL.md", "---\nname: foo\ndescription: Test.\n---\n")
        self.write("plugins/development/skills/foo/references/details.md", "# Details\n")
        self.write("maintenance/development/foo/sources.md", "# Sources\n")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def write_plugin(self, category: str, description: str) -> None:
        manifest = {"name": f"superskills-{category}", "version": "1.0.0", "description": description}
        self.write(f"plugins/{category}/plugin.json", json.dumps(manifest))

    def load(self, relative: str) -> dict:
        return json.loads((self.root / relative).read_text(encoding="utf-8"))

    def test_both_marketplaces_list_every_category_plugin(self) -> None:
        write_manifests(self.root)
        claude = self.load(".claude-plugin/marketplace.json")
        codex = self.load(".agents/plugins/marketplace.json")
        self.assertEqual(
            [("superskills-development", "./plugins/development"), ("superskills-writing", "./plugins/writing")],
            [(plugin["name"], plugin["source"]) for plugin in claude["plugins"]],
        )
        self.assertEqual(
            ["./plugins/development", "./plugins/writing"],
            [plugin["source"]["path"] for plugin in codex["plugins"]],
        )
        self.assertEqual([], stale_manifests(self.root))

    def test_manifests_become_stale_when_a_plugin_changes(self) -> None:
        write_manifests(self.root)
        self.write_plugin("writing", "Changed.")
        self.assertEqual([".claude-plugin/marketplace.json"], stale_manifests(self.root))

    def test_set_version_updates_every_plugin(self) -> None:
        set_version(self.root, "1.2.0")
        versions = {self.load(f"plugins/{category}/plugin.json")["version"] for category in ("development", "writing")}
        self.assertEqual({"1.2.0"}, versions)
        with self.assertRaises(ManifestError):
            set_version(self.root, "next")

    def test_web_package_has_skill_folder_as_root_and_only_runtime_files(self) -> None:
        archives = package(self.root)
        self.assertEqual(["foo.zip", "resume-writing.zip"], sorted(path.name for path in archives))
        with zipfile.ZipFile(self.root / "dist/claude-web/foo.zip") as bundle:
            self.assertEqual(["foo/SKILL.md", "foo/references/details.md"], sorted(bundle.namelist()))

    def test_web_package_is_reproducible_and_can_select_skills(self) -> None:
        first = package(self.root, routes=["development/foo"])[0].read_bytes()
        second = package(self.root, routes=["development/foo"])[0].read_bytes()
        self.assertEqual(first, second)
        self.assertEqual(["foo.zip"], [path.name for path in (self.root / "dist/claude-web").glob("*.zip")])
        with self.assertRaises(PackageError):
            package(self.root, routes=["development/missing"])

    def test_web_package_leaves_unrelated_archives_in_the_output_directory(self) -> None:
        unrelated = self.root / "downloads" / "holiday-photos.zip"
        unrelated.parent.mkdir()
        unrelated.write_bytes(b"not ours")
        package(self.root, unrelated.parent)
        self.assertEqual(b"not ours", unrelated.read_bytes())
        self.assertTrue((unrelated.parent / "foo.zip").is_file())

    def test_web_package_failure_leaves_no_truncated_archive(self) -> None:
        with mock.patch.object(zipfile.ZipFile, "writestr", side_effect=OSError("disk full")):
            with self.assertRaises(OSError):
                package(self.root, routes=["development/foo"])
        self.assertEqual([], list((self.root / "dist/claude-web").iterdir()))


if __name__ == "__main__":
    unittest.main()
