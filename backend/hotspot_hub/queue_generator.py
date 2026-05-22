"""Generate safe worker queues from hotspot reports."""

from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


DEFAULT_MAX_HOTSPOTS = 5


def generate_hotspot_worker_queue(
    report_path: Path,
    out_path: Path,
    target: str,
    max_hotspots: int = DEFAULT_MAX_HOTSPOTS,
    mode: str = "prompt",
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    """Generate a bounded local-only worker queue from a Hotspot Hub report."""
    if mode not in {"prompt", "local-llm", "foundry-scaffold"}:
        raise ValueError("Queue mode must be 'prompt', 'local-llm', or 'foundry-scaffold'")

    report = json.loads(report_path.read_text(encoding="utf-8"))
    hotspots = report.get("hotspots", [])[:max_hotspots]
    run_id = f"{target}-hotspot-queue-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"

    jobs = []
    for index, hotspot in enumerate(hotspots, start=1):
        path = hotspot["path"]
        contract_name = _contract_name(path)
        job_id = f"{index:02d}-{_safe_id(contract_name)}-{mode}"
        if mode == "prompt":
            command = [
                "python",
                "-m",
                "backend.hotspot_hub.cli",
                "prompt",
                str(report_path),
                path,
            ]
            notes = "Build a compact LLM-ready analysis prompt for this ranked hotspot."
            cwd = "."
        elif mode == "local-llm":
            command = [
                "python",
                "-m",
                "backend.hotspot_hub.cli",
                "llm",
                "analyze-hotspot",
                str(report_path),
                path,
            ]
            notes = "Analyze this ranked hotspot with the local LM Studio model."
            cwd = "."
        else:
            command = [
                "python",
                "-m",
                "backend.hotspot_hub.cli",
                "validate",
                "foundry-slice",
                "--target",
                target,
                "--contract-name",
                contract_name,
                "--contract-path",
                _full_contract_path(report, path),
                "--run-id",
                f"auto-{_safe_id(contract_name)}-{index:02d}",
            ]
            notes = "Generate and run the existing Foundry scaffold slice; this is workflow evidence, not bug evidence."
            cwd = "."

        jobs.append(
            {
                "job_id": job_id,
                "kind": "command",
                "cwd": cwd,
                "command": command,
                "timeout_seconds": timeout_seconds,
                "hypothesis_id": f"AUTO-{index:02d}",
                "notes": notes,
                "hotspot": {
                    "path": path,
                    "score": hotspot.get("score"),
                    "tags": hotspot.get("tags", []),
                    "reasons": hotspot.get("reasons", []),
                },
            }
        )

    queue = {
        "run_id": run_id,
        "target": target,
        "mode": mode,
        "source_report": str(report_path),
        "stop_on_promising": False,
        "jobs": jobs,
        "safety_note": "Generated queue is local-only and bounded. Review before long runs.",
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(queue, indent=2) + "\n", encoding="utf-8")
    return queue


def _contract_name(path: str) -> str:
    stem = Path(path).stem
    return stem or "Hotspot"


def _full_contract_path(report: dict[str, Any], path: str) -> str:
    root = Path(report["target"]["root"])
    return str(root / path)


def _safe_id(value: str) -> str:
    safe = "".join(char.lower() if char.isalnum() else "-" for char in value)
    while "--" in safe:
        safe = safe.replace("--", "-")
    return safe.strip("-") or "hotspot"
