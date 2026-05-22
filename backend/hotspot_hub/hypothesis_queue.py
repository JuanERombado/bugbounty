"""Small hypothesis queue for local exploit-validation runs."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .models import utc_now_iso


@dataclass(frozen=True)
class HypothesisCandidate:
    id: str
    title: str
    bug_class: str
    paid_impact_path: str
    invariant: str
    local_test_goal: str
    rejection_rule: str
    status: str = "queued"


def make_run_id(contract_name: str) -> str:
    stamp = utc_now_iso().replace(":", "").replace("+", "Z").split(".")[0]
    slug = re.sub(r"[^a-z0-9]+", "-", contract_name.lower()).strip("-") or "contract"
    return f"{stamp}-{slug}"


def default_invariant_candidates(contract_name: str, contract_path: str) -> list[HypothesisCandidate]:
    prefix = re.sub(r"[^A-Z0-9]+", "", contract_name.upper())[:8] or "HYP"
    return [
        HypothesisCandidate(
            id=f"{prefix}-INV-1",
            title=f"{contract_name} value conservation across collect/withdraw paths",
            bug_class="escrow solvency mismatch",
            paid_impact_path="unauthorized or incorrect movement of funds",
            invariant="Tracked balances plus paid/withdrawn amounts should never exceed deposits or escrowed funds.",
            local_test_goal="Model deposits, collection, cancellation, and withdrawal-like actions, then assert conservation after every sequence.",
            rejection_rule="Reject if the real contract already enforces conservation or the scenario cannot map to an accepted paid impact.",
        ),
        HypothesisCandidate(
            id=f"{prefix}-INV-2",
            title=f"{contract_name} authorization/state-transition invariant",
            bug_class="unauthorized role/state transition",
            paid_impact_path="unauthorized action that changes payment, allocation, or agreement state",
            invariant="Only the intended actor should move an agreement, allocation, payment destination, or claim state into a value-affecting status.",
            local_test_goal="Fuzz caller roles and lifecycle orderings, then assert unauthorized callers cannot produce value-affecting state changes.",
            rejection_rule="Reject if unauthorized calls revert or only produce non-paid informational effects.",
        ),
        HypothesisCandidate(
            id=f"{prefix}-INV-3",
            title=f"{contract_name} bounded-rate and overflow invariant",
            bug_class="reward/accounting mismatch",
            paid_impact_path="payer cap bypass, locked funds, or blocked fee collection",
            invariant=f"Inputs accepted by {contract_name} should not overflow before downstream caps, slippage checks, or collection limits apply.",
            local_test_goal=f"Use boundary values around rate, entity count, elapsed time, and slippage for {contract_path}, then assert collection is capped, recoverable, or safely reverted.",
            rejection_rule="Reject if overflow requires unrealistic self-harm terms and a safer collection path always recovers funds.",
        ),
    ]


def write_queue(path: Path, run_id: str, target: str, contract_name: str, contract_path: str, candidates: list[HypothesisCandidate]) -> dict[str, Any]:
    payload = {
        "run_id": run_id,
        "target": target,
        "contract_name": contract_name,
        "contract_path": contract_path,
        "created_at": utc_now_iso(),
        "candidates": [asdict(candidate) for candidate in candidates],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload
