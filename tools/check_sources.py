#!/usr/bin/env python3
"""Report maintenance sources that are due for review or no longer resolve."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Callable, Sequence

if __package__:
    from .layout import MAINTENANCE_DIR
    from .validator_markdown import parse_markdown_tables
else:
    from layout import MAINTENANCE_DIR
    from validator_markdown import parse_markdown_tables

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAX_AGE_MONTHS = 3
# Other error statuses (403, 429, 5xx) are bot protection or transient, not evidence the source moved.
GONE_STATUSES = {404, 410}
URL_RE = re.compile(r"https?://[^\s|)>\]]+")
REVIEWED_RE = re.compile(r"^(\d{4})-(\d{2})$")
GITHUB_REPO_RE = re.compile(r"^https://github\.com/([^/\s]+)/([^/\s#?]+?)(?:\.git)?/?$")
USER_AGENT = "superskills-source-check"
TIMEOUT_SECONDS = 20

Fetch = Callable[[str], tuple[int, dict]]


@dataclass(frozen=True)
class Source:
    file: str
    url: str
    reviewed: str | None


@dataclass(frozen=True)
class Finding:
    source: Source
    reason: str


def collect_sources(root: Path) -> list[Source]:
    sources: list[Source] = []
    for path in sorted((root / MAINTENANCE_DIR).glob("*/*/sources.md")):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        reviewed_by_url: dict[str, str] = {}
        for table in parse_markdown_tables(text):
            if "canonical url" not in table.headers or "last reviewed" not in table.headers:
                continue
            url_index = table.headers.index("canonical url")
            reviewed_index = table.headers.index("last reviewed")
            for row in table.rows:
                match = URL_RE.search(row[url_index])
                if match:
                    reviewed_by_url[match.group(0)] = row[reviewed_index].strip()
        for url in dict.fromkeys(URL_RE.findall(text)):
            sources.append(Source(relative, url, reviewed_by_url.get(url)))
    return sources


def months_between(reviewed: str, today: date) -> int | None:
    match = REVIEWED_RE.fullmatch(reviewed)
    if not match:
        return None
    return (today.year - int(match.group(1))) * 12 + today.month - int(match.group(2))


def review_findings(sources: Sequence[Source], today: date, max_age_months: int) -> list[Finding]:
    findings: list[Finding] = []
    for source in sources:
        if source.reviewed is None:
            continue
        age = months_between(source.reviewed, today)
        if age is None:
            findings.append(Finding(source, f"Last reviewed `{source.reviewed}` is not YYYY-MM"))
        elif age > max_age_months:
            findings.append(Finding(source, f"last reviewed {source.reviewed}, {age} months ago"))
    return findings


def http_fetch(url: str) -> tuple[int, dict]:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json, */*"}
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith("https://api.github.com/"):
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read() if url.startswith("https://api.github.com/") else b""
            return response.status, json.loads(body) if body else {}
    except urllib.error.HTTPError as error:
        return error.code, {}


def online_findings(sources: Sequence[Source], fetch: Fetch = http_fetch) -> list[Finding]:
    findings: list[Finding] = []
    for source in sources:
        repo = GITHUB_REPO_RE.fullmatch(source.url)
        target = f"https://api.github.com/repos/{repo.group(1)}/{repo.group(2)}" if repo else source.url
        try:
            status, payload = fetch(target)
        except (urllib.error.URLError, TimeoutError, OSError) as error:
            findings.append(Finding(source, f"could not be reached ({error})"))
            continue
        if status in GONE_STATUSES:
            findings.append(Finding(source, f"no longer exists (HTTP {status})"))
        elif repo and payload.get("archived"):
            findings.append(Finding(source, "repository is archived"))
    return findings


def render_report(findings: Sequence[Finding], checked: int, online: bool) -> str:
    mode = "review age, missing pages and archived repositories" if online else "review age only"
    lines = ["# Skill source freshness", "", f"Checked {checked} sources ({mode})."]
    if not findings:
        return "\n".join([*lines, "", "All registered sources are current."]) + "\n"
    lines += [
        "",
        "Re-read each source below, update the owning Skill only where a decision actually changes, "
        "then set its `Last reviewed` month. Nothing here is applied automatically.",
    ]
    by_file: dict[str, list[Finding]] = {}
    for finding in findings:
        by_file.setdefault(finding.source.file, []).append(finding)
    for file, items in by_file.items():
        lines += ["", f"## `{file}`", ""]
        lines += [f"- {item.source.url} — {item.reason}" for item in items]
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--max-age-months", type=int, default=DEFAULT_MAX_AGE_MONTHS)
    parser.add_argument("--online", action="store_true", help="Also request every source URL.")
    parser.add_argument("--report", type=Path, help="Write the Markdown report to this path.")
    parser.add_argument("--github-output", type=Path, help="Append findings=<true|false> for a workflow step.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    sources = collect_sources(args.root.resolve())
    findings = review_findings(sources, date.today(), args.max_age_months)
    if args.online:
        findings += online_findings(sources)
    report = render_report(findings, len(sources), args.online)
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(report, encoding="utf-8")
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as output:
            output.write(f"findings={'true' if findings else 'false'}\n")
    sys.stdout.reconfigure(encoding="utf-8")
    print(report, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
