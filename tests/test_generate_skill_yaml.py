from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from tools.generate_openai_yaml import generate as generate_openai
from tools.generate_skill_yaml import derive_triggers, generate as generate_skill_yaml


class GeneratorTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        skill = self.root / "plugins/development/skills/foo"
        skill.mkdir(parents=True)
        (skill / "SKILL.md").write_text(
            "---\nname: foo\ndescription: Fix a broken build. Use when the build fails, not for a passing build.\n---\n\n# Foo\n",
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_skill_yaml_matches_frontmatter(self) -> None:
        generated = generate_skill_yaml(self.root)
        path = self.root / "plugins/development/skills/foo/skill.yaml"
        self.assertIn(path, generated)
        text = generated[path]
        self.assertIn("name: foo", text)
        self.assertIn("title: Foo", text)
        self.assertIn("description: Fix a broken build.", text)
        self.assertIn("category: development", text)
        self.assertIn("include_in_prompt: false", text)

    def test_triggers_come_from_use_when_clause(self) -> None:
        triggers = derive_triggers(
            "foo", "Fix a broken build. Use when the build fails, not for a passing build."
        )
        self.assertEqual(["foo", "the build fails"], triggers)

    def test_openai_yaml_serves_both_openai_agents(self) -> None:
        generated = generate_openai(self.root)
        path = self.root / "agents/development/foo/openai.yaml"
        self.assertIn(path, generated)
        text = generated[path]
        self.assertIn("display_name: Foo", text)
        self.assertIn("short_description: Fix a broken build.", text)
        self.assertIn("allow_implicit_invocation: true", text)
        self.assertIn("dependencies: []", text)

    def test_check_mode_detects_missing_file(self) -> None:
        from tools.generate_skill_yaml import main as skill_main

        self.assertEqual(1, skill_main(["--root", str(self.root), "--check"]))

    def test_single_skill_run_never_deletes_other_openai_files(self) -> None:
        from tools.generate_openai_yaml import main as openai_main

        second = self.root / "plugins/development/skills/bar"
        second.mkdir(parents=True)
        (second / "SKILL.md").write_text(
            "---\nname: bar\ndescription: Bar work.\n---\n\n# Bar\n",
            encoding="utf-8",
        )
        self.assertEqual(0, openai_main(["--root", str(self.root)]))
        self.assertEqual(
            0, openai_main(["--root", str(self.root), "--skill", "development/foo"])
        )
        self.assertTrue((self.root / "agents/development/bar/openai.yaml").is_file())
        self.assertTrue((self.root / "agents/development/foo/openai.yaml").is_file())


if __name__ == "__main__":
    unittest.main()
