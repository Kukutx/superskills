from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from tools.check_sources import (
    collect_sources,
    online_findings,
    render_report,
    review_findings,
)

REGISTER = (
    "# Sources\n\n"
    "| Source | Canonical URL | Used for | Last reviewed |\n"
    "| --- | --- | --- | --- |\n"
    "| Docs | https://docs.example.org/ | engine behavior | 2026-09 |\n"
    "| Repo | https://github.com/example/repo | patterns | 2026-01 |\n\n"
    "- Unregistered anchor\n  - https://example.org/guide\n"
)


class CheckSourcesTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        path = self.root / "maintenance/development/foo/sources.md"
        path.parent.mkdir(parents=True)
        path.write_text(REGISTER, encoding="utf-8")
        self.sources = collect_sources(self.root)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_collects_registered_and_prose_urls(self) -> None:
        self.assertEqual(
            [("https://docs.example.org/", "2026-09"), ("https://github.com/example/repo", "2026-01"),
             ("https://example.org/guide", None)],
            [(source.url, source.reviewed) for source in self.sources],
        )

    def test_only_reviews_older_than_limit_are_reported(self) -> None:
        findings = review_findings(self.sources, date(2026, 10, 4), 6)
        self.assertEqual(["https://github.com/example/repo"], [finding.source.url for finding in findings])
        self.assertIn("9 months ago", findings[0].reason)

    def test_online_reports_missing_pages_and_archived_repositories(self) -> None:
        def fetch(url: str) -> tuple[int, dict]:
            if url == "https://api.github.com/repos/example/repo":
                return 200, {"archived": True}
            if url == "https://example.org/guide":
                return 404, {}
            return 200, {}

        reasons = [finding.reason for finding in online_findings(self.sources, fetch)]
        self.assertEqual(["repository is archived", "no longer exists (HTTP 404)"], reasons)

    def test_bot_protection_status_is_not_reported(self) -> None:
        self.assertEqual([], online_findings(self.sources, lambda url: (429, {})))

    def test_unreachable_source_is_a_finding_not_a_crash(self) -> None:
        def fetch(url: str) -> tuple[int, dict]:
            raise TimeoutError("timed out")

        self.assertEqual(3, len(online_findings(self.sources, fetch)))

    def test_report_states_when_everything_is_current(self) -> None:
        self.assertIn("All registered sources are current.", render_report([], 3, online=True))


if __name__ == "__main__":
    unittest.main()
