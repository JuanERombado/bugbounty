"""Run local seeded vulnerable fixtures through Foundry."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import utc_now_iso
from .test_runner import run_foundry_command


def run_fixture_slice(
    workspace: Path,
    fixture: str,
    run_id: str | None = None,
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    fixture_dir = workspace / "test_fixtures" / fixture
    if not fixture_dir.exists():
        raise ValueError(f"Unknown fixture: {fixture}")

    resolved_run_id = run_id or f"{fixture}-fixture-slice"
    run_dir = workspace / "targets" / "fixtures" / "runs" / resolved_run_id
    vulnerable = run_foundry_command(
        fixture_dir,
        run_dir / "vulnerable-result.json",
        ["test", "--match-contract", "VulnerableVaultInvariantTest", "-vv"],
        timeout_seconds,
    )
    fixed = run_foundry_command(
        fixture_dir,
        run_dir / "fixed-result.json",
        ["test", "--match-contract", "FixedVaultInvariantTest", "-vv"],
        timeout_seconds,
    )

    vulnerable_failed = vulnerable["returncode"] != 0
    fixed_passed = fixed["returncode"] == 0
    if vulnerable_failed and fixed_passed:
        status = "reproduced"
        rationale = "Seeded vulnerable invariant failed and fixed-contract invariant passed."
    elif not vulnerable_failed and fixed_passed:
        status = "clean"
        rationale = "Both vulnerable and fixed runs passed; the seeded bug was not reproduced."
    else:
        status = "fixture_setup_failed"
        rationale = "The fixed contract did not pass, so the fixture or environment needs repair."

    judgment = {
        "run_id": resolved_run_id,
        "fixture": fixture,
        "judged_at": utc_now_iso(),
        "status": status,
        "rationale": rationale,
        "vulnerable_result": str(run_dir / "vulnerable-result.json"),
        "fixed_result": str(run_dir / "fixed-result.json"),
        "reproduced": status == "reproduced",
        "report_ready": False,
        "safety_note": "Seeded local fixture only. This is pipeline evidence, not bounty evidence.",
    }
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "judgment.json").write_text(json.dumps(judgment, indent=2) + "\n", encoding="utf-8")
    return judgment
