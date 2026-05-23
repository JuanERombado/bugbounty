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
        status = "clean_compile_smoke"
        rationale = "The real-contract compile smoke passed. No invariant failure or security impact was demonstrated."
        next_action = "Replace the smoke test with real deployment setup, mocks, actors, and one local invariant."
    elif "source not found" in combined or "file not found" in combined:
        status = "harness_needs_import_remappings"
        rationale = "The real harness could not resolve one or more imported source files."
        next_action = "Fix Foundry remappings or dependency paths before adding behavior tests."
    elif "wrong argument count" in combined or "no arguments passed to base constructor" in combined:
        status = "harness_needs_constructor_args"
        rationale = "The harness needs constructor or inherited constructor arguments before it can deploy the target."
        next_action = "Add the required constructor arguments or proxy initializer wiring with local-only mocks."
    elif "identifier not found" in combined or "member not found" in combined:
        status = "harness_needs_mocks"
        rationale = "The real harness references symbols or members that need imports, mocks, interfaces, or setup wiring."
        next_action = "Add minimal local mocks/interfaces and repair only the harness."
    elif "constructor" in combined or "abstract contract" in combined:
        status = "harness_needs_constructor_args"
        rationale = "The harness compiled far enough to expose target-specific deployment requirements."
        next_action = "Add constructor parameters, inherited setup, proxy initialization, or mocks."
    elif "invariant" in combined and ("fail" in combined or "revert" in combined):
        status = "invariant_failed_promising"
        rationale = "A real-harness invariant appears to have failed locally, but impact and setup still need review."
        next_action = "Minimize the failing case, map accepted impact, and run duplicate-risk checks."
    elif "compiler run failed" in combined or "compilation failed" in combined or "error (" in combined:
        status = "compile_failed"
        rationale = "The real harness failed at compile time but did not match a more specific setup category."
        next_action = "Inspect stdout/stderr and repair remappings, imports, constructor setup, or mocks."
    else:
        status = "runtime_test_failed"
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
