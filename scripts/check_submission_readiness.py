#!/usr/bin/env python3
"""Check whether a finding dossier is ready to become an Immunefi report draft."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_TRUE_CHECKS = [
    ("asset.in_scope", ("asset", "in_scope")),
    ("scope_checks.asset_in_scope", ("scope_checks", "asset_in_scope")),
    ("scope_checks.impact_in_scope", ("scope_checks", "impact_in_scope")),
    ("scope_checks.not_known_issue", ("scope_checks", "not_known_issue")),
    ("scope_checks.not_out_of_scope", ("scope_checks", "not_out_of_scope")),
    ("scope_checks.local_only", ("scope_checks", "local_only")),
    ("poc.complete", ("poc", "complete")),
]

REQUIRED_TEXT = [
    ("title", ("title",)),
    ("impact.accepted_impact", ("impact", "accepted_impact")),
    ("impact.impact_fit", ("impact", "impact_fit")),
    ("evidence.root_cause", ("evidence", "root_cause")),
    ("evidence.test_output", ("evidence", "test_output")),
    ("evidence.environment", ("evidence", "environment")),
    ("poc.local_command", ("poc", "local_command")),
    ("poc.expected_result", ("poc", "expected_result")),
    ("poc.actual_result", ("poc", "actual_result")),
    ("report.summary", ("report", "summary")),
    ("report.suggested_fix", ("report", "suggested_fix")),
]


def get_nested(data: dict, path: tuple[str, ...]):
    current = data
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dossier", type=Path)
    args = parser.parse_args()

    data = json.loads(args.dossier.read_text(encoding="utf-8"))
    failures = []

    for label, path in REQUIRED_TRUE_CHECKS:
        if get_nested(data, path) is not True:
            failures.append(f"{label} must be true")

    for label, path in REQUIRED_TEXT:
        value = get_nested(data, path)
        if not isinstance(value, str) or not value.strip():
            failures.append(f"{label} must be filled")

    steps = get_nested(data, ("report", "steps_to_reproduce"))
    if not isinstance(steps, list) or not steps:
        failures.append("report.steps_to_reproduce must include at least one step")

    poc_files = get_nested(data, ("poc", "files"))
    if not isinstance(poc_files, list) or not poc_files:
        failures.append("poc.files must include at least one local PoC file")

    if failures:
        print("NOT READY")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("READY")
    print("This dossier has the minimum evidence fields for report drafting.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
