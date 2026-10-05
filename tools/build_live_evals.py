#!/usr/bin/env python3
"""Build a self-contained plugin plus live eval cases for `claude plugin eval`.

Behavioral eval tables stay the only authored source. A row is replayable when its
prompt is one quoted utterance; rows that depend on described context (uploaded
files, prior decisions) are skipped and remain human-review fixtures.

route      Primary is another Skill, or the row lives in the Router's table: the
           bare utterance must make the host invoke that Skill.
behavior   Primary is the Skill that owns the table: the Skill is named in the
           prompt and a judge checks the answer against Must avoid.
reference  Primary is a reference file: the Skill is named in the prompt and the
           reference must be read.
negative   Primary is `none`: the bare utterance must not make the host invoke any
           Skill named in Must avoid.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

if __package__:
    from .export_behavioral_evals import EvalExportError, export_cases
    from .layout import ROUTER_ROUTE, skill_dirs
else:
    from export_behavioral_evals import EvalExportError, export_cases
    from layout import ROUTER_ROUTE, skill_dirs

DEFAULT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = Path("dist/live-evals")
UTTERANCE_RE = re.compile(r"^[“\"]([^”\"]+)[”\"]$")
ROUTE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*/([a-z0-9]+(?:-[a-z0-9]+)*)$")
REFERENCE_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.md$")
CASE_ID_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
NO_SKILL = "none"
MAX_TURNS = 8
ALLOWED_TOOLS = "[Skill, Read, Glob, Grep]"
# A discovery or research request is only routed when the session can actually search;
# these tools still need the operator grant `--allow-tools WebSearch WebFetch` at run time.
WEB_CATEGORY = "research"
WEB_TOOLS = "[Skill, Read, Glob, Grep, WebSearch, WebFetch]"
WEB_MAX_TURNS = 4


class LiveEvalError(ValueError):
    """Raised when the live eval suite cannot be built safely."""


@dataclass(frozen=True)
class LiveCase:
    case_id: str
    kind: str
    prompt: str
    graders: dict[str, str]
    web: bool = False


def skill_grader(skill: str, *, forbidden: bool = False) -> str:
    bounds = "min: 0\nmax: 0\n" if forbidden else ""
    verdict = "must not be invoked" if forbidden else "must be invoked"
    return (
        "---\ntype: tool_used\ntool: Skill\n"
        f"input_match: '\"skill\"\\s*:\\s*\"(?:[\\w-]+:)?{skill}\"'\n{bounds}---\n\n"
        f"The `{skill}` Skill {verdict}.\n"
    )


def reference_grader(reference: str) -> str:
    return (
        "---\ntype: tool_used\ntool: Read\n"
        f"input_match: '{re.escape(reference)}'\n---\n\n"
        f"The `{reference}` reference must be read.\n"
    )


def behavior_grader(must_avoid: str) -> str:
    return (
        "---\ntype: llm\n---\n\n"
        f"The assistant itself must not do this: {must_avoid}.\n\n"
        "Fail only when the assistant actually does it. Declining it, warning against it or "
        "explaining why it is a bad idea is a pass, and so is asking for missing facts, "
        "refusing an unsafe request or stating a limitation.\n"
    )


def named(owner: str, utterance: str) -> str:
    return f"使用 {owner} Skill 处理这个任务：{utterance}"


def live_cases(records: Sequence[dict[str, object]], skill_names: Sequence[str]) -> list[LiveCase]:
    cases: list[LiveCase] = []
    for record in records:
        utterance = UTTERANCE_RE.fullmatch(str(record["prompt"]).strip())
        primary = str(record["primary"]).strip()
        case_id = str(record["id"])
        if not utterance or not CASE_ID_RE.fullmatch(case_id):
            continue
        source = str(record["source_skill"])
        owner = source.split("/", 1)[1]
        avoided = str(record["must_avoid"])
        route = ROUTE_RE.fullmatch(primary)
        named_in_avoid = [
            name for name in skill_names if re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", avoided)
        ]
        if primary == NO_SKILL:
            if named_in_avoid:
                graders = {f"avoid-{name}": skill_grader(name, forbidden=True) for name in named_in_avoid}
                cases.append(LiveCase(case_id, "negative", utterance.group(1), graders))
        elif route and primary == source and source != ROUTER_ROUTE:
            graders = {"route": skill_grader(owner), "behavior": behavior_grader(avoided)}
            cases.append(LiveCase(case_id, "behavior", named(owner, utterance.group(1)), graders))
        elif route:
            expected = route.group(1)
            graders = {"route": skill_grader(expected)}
            for name in named_in_avoid:
                if name != expected:
                    graders[f"avoid-{name}"] = skill_grader(name, forbidden=True)
            web = primary.split("/", 1)[0] == WEB_CATEGORY
            cases.append(LiveCase(case_id, "route", utterance.group(1), graders, web))
        elif REFERENCE_RE.fullmatch(primary):
            graders = {"reference": reference_grader(primary)}
            cases.append(LiveCase(case_id, "reference", named(owner, utterance.group(1)), graders))
    return cases


def build(
    root: Path | str = DEFAULT_ROOT,
    output: Path | str = DEFAULT_OUTPUT,
    only: Sequence[str] = (),
) -> list[LiveCase]:
    root = Path(root).resolve()
    output_path = Path(output)
    if not output_path.is_absolute():
        output_path = root / output_path
    output_path = output_path.resolve()
    # The output is rebuilt in place, so it may only ever be a generated directory.
    if root / "dist" not in output_path.parents:
        raise LiveEvalError("output must be a directory under dist/, such as dist/live-evals")

    sources = skill_dirs(root)
    cases = live_cases(export_cases(root), [path.name for path in sources])
    if only:
        unknown = sorted(set(only) - {case.case_id for case in cases})
        if unknown:
            raise LiveEvalError(f"not replayable or unknown case IDs: {unknown}")
        cases = [case for case in cases if case.case_id in set(only)]
    if not cases:
        raise LiveEvalError("no replayable behavioral eval cases found")

    # Replace the generated suite but keep evals/results, where earlier run reports live.
    evals_path = output_path / "evals"
    stale = [output_path / "skills", output_path / ".claude-plugin"]
    if evals_path.is_dir():
        stale += [path for path in evals_path.iterdir() if path.name != "results"]
    for path in stale:
        if path.is_dir():
            shutil.rmtree(path)
    for source in sources:
        shutil.copytree(source, output_path / "skills" / source.name)
    manifest = {
        "name": "superskills",
        "description": "All Superskills categories, assembled for live evaluation only.",
        "author": {"name": "Kukutx"},
    }
    manifest_path = output_path / ".claude-plugin" / "plugin.json"
    manifest_path.parent.mkdir(parents=True)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    for case in cases:
        case_dir = output_path / "evals" / case.case_id
        (case_dir / "graders").mkdir(parents=True)
        turns, tools, tags = (
            (WEB_MAX_TURNS, WEB_TOOLS, f"{case.kind}, web") if case.web else (MAX_TURNS, ALLOWED_TOOLS, case.kind)
        )
        (case_dir / "prompt.md").write_text(
            f"---\nmax_turns: {turns}\nallowed_tools: {tools}\ntags: [{tags}]\n---\n\n{case.prompt}\n",
            encoding="utf-8",
        )
        for name, content in case.graders.items():
            (case_dir / "graders" / f"{name}.md").write_text(content, encoding="utf-8")
    return cases


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--only", action="append", default=[], help="Build only this case ID; repeat as needed.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        cases = build(args.root, args.output, args.only)
    except (LiveEvalError, EvalExportError) as exc:
        print(f"live eval build failed: {exc}", file=sys.stderr)
        return 1
    counts = {kind: sum(case.kind == kind for case in cases) for kind in ("route", "behavior", "reference", "negative")}
    summary = ", ".join(f"{count} {kind}" for kind, count in counts.items())
    print(f"live evals built: {summary} cases -> {args.output.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
