"""Conservative result judge for local validation runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import utc_now_iso


def judge_foundry_result(queue_payload: dict[str, Any], run_payload: dict[str, Any], out_path: Path) -> dict[str, Any]:
    if run_payload["returncode"] != 0:
        status = "generated_scaffold_failed"
        rationale = "The generated placeholder scaffold did not compile or tests failed before real contract wiring."
        next_action = "Repair the harness before interpreting this as security evidence."
    else:
        status = "scaffold_only"
        rationale = "The scaffold compiles and runs, but it uses a placeholder harness and is not evidence of a bug."
        next_action = "Wire the strongest hypothesis into the real local contract harness and rerun."

    payload = {
        "run_id": queue_payload["run_id"],
        "judged_at": utc_now_iso(),
        "status": status,
        "rationale": rationale,
        "next_action": next_action,
        "surviving_candidates": [item["id"] for item in queue_payload["candidates"]] if run_payload["returncode"] == 0 else [],
        "reproduced": False,
        "report_ready": False,
        "safety_note": "Local scaffold result only. Do not submit or test live systems.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def judge_real_foundry_result(
    run_id: str,
    run_payload: dict[str, Any],
    out_path: Path,
    *,
    target: str,
    contract_name: str,
    hypothesis_id: str,
) -> dict[str, Any]:
    stdout = run_payload.get("stdout", "")
    stderr = run_payload.get("stderr", "")
    combined = f"{stdout}\n{stderr}".lower()
    if run_payload["returncode"] == 0:
        status = "clean"
        if hypothesis_id.upper().startswith("SMOKE"):
            rationale = "The real-contract compile smoke passed. No invariant failure was demonstrated."
            next_action = "Replace the smoke test with a real setup, mocks, and invariant before drawing security conclusions."
        else:
            rationale = "The real-contract harness and local invariant passed. No issue was reproduced for this hypothesis."
            next_action = "Record this hypothesis as rejected/clean and move to the next highest-value invariant."
    elif "compiler run failed" in combined or "compilation failed" in combined or "error (" in combined:
        status = "compile_failed"
        rationale = "The real harness failed at compile/import/remapping time."
        next_action = "Fix remappings or add mocks. Do not treat compile failures as security findings."
    elif "constructor" in combined or "abstract contract" in combined:
        status = "harness_needs_mocks"
        rationale = "The harness compiled far enough to need target-specific setup or mocks."
        next_action = "Add constructor parameters, mocks, or deployment setup."
    elif "invariant" in combined and ("fail" in combined or "revert" in combined):
        status = "invariant_failed_promising"
        rationale = "A real-harness invariant appears to have failed locally, but impact and setup still need review."
        next_action = "Minimize the failing case, map accepted impact, and run duplicate-risk checks."
    else:
        status = "test_failed"
        rationale = "The real harness test failed, but not in a way that can be classified as a promising invariant failure."
        next_action = "Inspect stdout/stderr and repair only the harness."

    payload = {
        "run_id": run_id,
        "judged_at": utc_now_iso(),
        "target": target,
        "contract_name": contract_name,
        "hypothesis_id": hypothesis_id,
        "status": status,
        "rationale": rationale,
        "next_action": next_action,
        "reproduced": status == "reproduced_local",
        "report_ready": False,
        "report_ready_false": True,
        "safety_note": "Local real-harness result only. No live systems were tested.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload
