"""Conservative result judge for local validation runs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .models import utc_now_iso


def judge_foundry_result(queue_payload: dict[str, Any], run_payload: dict[str, Any], out_path: Path) -> dict[str, Any]:
    if run_payload["returncode"] != 0:
        status = "needs_repair"
        rationale = "The generated scaffold did not compile or tests failed before real contract wiring."
        next_action = "Repair the harness before interpreting this as security evidence."
    else:
        status = "promising_scaffold"
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
