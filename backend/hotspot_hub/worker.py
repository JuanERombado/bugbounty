"""Bounded local research worker for evidence-producing jobs."""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from .subprocess_tools import run_command


ALLOWED_JOB_TYPES = {"command"}
DEFAULT_TIMEOUT_SECONDS = 300
MAX_TIMEOUT_SECONDS = 24 * 60 * 60


@dataclass(frozen=True)
class WorkerJob:
    job_id: str
    kind: str
    command: list[str]
    cwd: Path
    timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS
    hypothesis_id: str | None = None
    notes: str = ""


def run_worker_queue(queue_path: Path, workspace: Path, out_dir: Path | None = None, max_jobs: int | None = None) -> dict[str, Any]:
    """Run bounded local jobs from a JSON queue and write normalized artifacts."""
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    jobs = [_parse_job(item, workspace) for item in queue.get("jobs", [])]
    selected_jobs = jobs[:max_jobs] if max_jobs is not None else jobs
    run_id = queue.get("run_id") or _timestamp_run_id("worker")
    output_dir = out_dir or workspace / "targets" / queue.get("target", "unknown") / "runs" / run_id
    output_dir.mkdir(parents=True, exist_ok=True)
    started_at = datetime.now(UTC).isoformat()

    results = []
    for job in selected_jobs:
        result = _run_job(job, workspace, output_dir)
        results.append(result)
        if queue.get("stop_on_promising") and _is_promising(result):
            break

    summary = {
        "run_id": run_id,
        "queue_path": str(queue_path),
        "started_at": started_at,
        "jobs_requested": len(jobs),
        "jobs_run": len(results),
        "results": results,
        "safety_note": "Local commands only. Do not use this worker for live-system testing.",
    }
    (output_dir / "worker-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


def _parse_job(payload: dict[str, Any], workspace: Path) -> WorkerJob:
    kind = payload.get("kind", "command")
    if kind not in ALLOWED_JOB_TYPES:
        raise ValueError(f"Unsupported worker job kind: {kind}")

    command = payload.get("command")
    if not isinstance(command, list) or not command or not all(isinstance(part, str) for part in command):
        raise ValueError("Worker job command must be a non-empty list of strings")

    timeout = int(payload.get("timeout_seconds", DEFAULT_TIMEOUT_SECONDS))
    if timeout < 1 or timeout > MAX_TIMEOUT_SECONDS:
        raise ValueError(f"Worker job timeout must be between 1 and {MAX_TIMEOUT_SECONDS} seconds")

    cwd = _resolve_inside_workspace(workspace, payload.get("cwd", "."))
    return WorkerJob(
        job_id=payload.get("job_id") or _timestamp_run_id("job"),
        kind=kind,
        command=command,
        cwd=cwd,
        timeout_seconds=timeout,
        hypothesis_id=payload.get("hypothesis_id"),
        notes=payload.get("notes", ""),
    )


def _run_job(job: WorkerJob, workspace: Path, output_dir: Path) -> dict[str, Any]:
    result = run_command(job.command, cwd=str(job.cwd), timeout_seconds=job.timeout_seconds)
    payload = {
        "job_id": job.job_id,
        "hypothesis_id": job.hypothesis_id,
        "kind": job.kind,
        "cwd": str(job.cwd),
        "command": result.command,
        "returncode": result.returncode,
        "elapsed_seconds": round(result.elapsed_seconds, 3),
        "passed": result.returncode == 0,
        "promising": result.returncode != 0,
        "notes": job.notes,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
    job_file = output_dir / f"{_safe_file_name(job.job_id)}.json"
    job_file.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    payload["artifact"] = str(job_file.relative_to(workspace))
    return payload


def _resolve_inside_workspace(workspace: Path, value: str) -> Path:
    root = workspace.resolve()
    candidate = (root / value).resolve() if not Path(value).is_absolute() else Path(value).resolve()
    if not (candidate == root or root in candidate.parents):
        raise ValueError(f"Worker cwd must stay inside workspace: {candidate}")
    return candidate


def _is_promising(result: dict[str, Any]) -> bool:
    return bool(result.get("promising"))


def _timestamp_run_id(prefix: str) -> str:
    return f"{prefix}-{datetime.now(UTC).strftime('%Y%m%d-%H%M%S')}"


def _safe_file_name(value: str) -> str:
    return "".join(char if char.isalnum() or char in {"-", "_"} else "-" for char in value).strip("-") or "job"
