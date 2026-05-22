"""Tiny local dashboard server for the Bug Bounty Workbench."""

from __future__ import annotations

import argparse
import json
import mimetypes
import sys
import threading
import uuid
from dataclasses import dataclass, field
from datetime import UTC, datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

from .subprocess_tools import run_command
from .target_initializer import initialize_target


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
APP_ROOT = WORKSPACE_ROOT / "app"
MAX_RESULT_CHARS = 24_000


@dataclass
class DashboardJob:
    id: str
    action: str
    label: str
    command: list[str]
    cwd: Path
    timeout_seconds: int
    status: str = "queued"
    created_at: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    started_at: str | None = None
    finished_at: str | None = None
    returncode: int | None = None
    elapsed_seconds: float | None = None
    stdout: str = ""
    stderr: str = ""
    error: str | None = None

    def to_dict(self, include_output: bool = True) -> dict:
        stdout = self.stdout
        stderr = self.stderr
        if include_output:
            stdout = _tail(stdout, MAX_RESULT_CHARS)
            stderr = _tail(stderr, MAX_RESULT_CHARS)
        else:
            stdout = ""
            stderr = ""
        return {
            "id": self.id,
            "action": self.action,
            "label": self.label,
            "command": self.command,
            "cwd": str(self.cwd),
            "timeout_seconds": self.timeout_seconds,
            "status": self.status,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "returncode": self.returncode,
            "elapsed_seconds": self.elapsed_seconds,
            "stdout": stdout,
            "stderr": stderr,
            "error": self.error,
        }


JOBS: dict[str, DashboardJob] = {}
JOBS_LOCK = threading.Lock()


def _tail(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return f"... truncated ...\n{value[-limit:]}"


class WorkbenchHandler(BaseHTTPRequestHandler):
    server_version = "BugBountyWorkbench/0.1"

    def do_GET(self) -> None:
        path = self.path.split("?", 1)[0]
        if path.startswith("/api/"):
            if path == "/api/status":
                self.write_json(workbench_status())
                return
            if path == "/api/jobs":
                self.write_json({"ok": True, "jobs": list_jobs()})
                return
            if path.startswith("/api/jobs/"):
                self.get_job(path.rsplit("/", 1)[-1])
                return
            self.write_json({"ok": False, "error": "Unknown API route"}, HTTPStatus.NOT_FOUND)
            return
        self.serve_static(path)

    def do_POST(self) -> None:
        if self.path == "/api/projects/initialize":
            self.initialize_project()
            return
        if self.path == "/api/jobs/start":
            self.start_job()
            return
        self.write_json({"ok": False, "error": "Unknown API route"}, HTTPStatus.NOT_FOUND)

    def initialize_project(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
            program_url = payload.get("programUrl", "")
            target_name = payload.get("targetName") or None
            result = initialize_target(program_url, WORKSPACE_ROOT, target_name)
            self.write_json(result)
        except ValueError as exc:
            self.write_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
        except json.JSONDecodeError:
            self.write_json({"ok": False, "error": "Request body must be valid JSON."}, HTTPStatus.BAD_REQUEST)
        except Exception as exc:  # pragma: no cover - defensive UI boundary.
            self.write_json({"ok": False, "error": f"Initialization failed: {exc}"}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def start_job(self) -> None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8") or "{}")
            job = create_job(payload.get("action", ""), payload)
            self.write_json({"ok": True, "job": job.to_dict(include_output=False)})
        except ValueError as exc:
            self.write_json({"ok": False, "error": str(exc)}, HTTPStatus.BAD_REQUEST)
        except json.JSONDecodeError:
            self.write_json({"ok": False, "error": "Request body must be valid JSON."}, HTTPStatus.BAD_REQUEST)
        except Exception as exc:  # pragma: no cover - defensive UI boundary.
            self.write_json({"ok": False, "error": f"Job start failed: {exc}"}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def get_job(self, job_id: str) -> None:
        with JOBS_LOCK:
            job = JOBS.get(job_id)
        if not job:
            self.write_json({"ok": False, "error": "Job not found."}, HTTPStatus.NOT_FOUND)
            return
        self.write_json({"ok": True, "job": job.to_dict()})

    def serve_static(self, raw_path: str) -> None:
        relative = "index.html" if raw_path in {"", "/"} else unquote(raw_path.lstrip("/"))
        candidate = (APP_ROOT / relative).resolve()
        if not str(candidate).startswith(str(APP_ROOT.resolve())) or not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return

        content_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        data = candidate.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def write_json(self, payload: dict, status: HTTPStatus = HTTPStatus.OK) -> None:
        data = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")


def workbench_status() -> dict:
    return {
        "ok": True,
        "workspace": str(WORKSPACE_ROOT),
        "lm_studio_url": "http://127.0.0.1:1234/v1",
        "hotspot_report_exists": (WORKSPACE_ROOT / "targets/thegraph/code-map/hotspot-report.json").exists(),
        "local_llm_queue_exists": (WORKSPACE_ROOT / "queues/thegraph-local-llm.worker.json").exists(),
        "latest_runs": latest_runs(),
        "jobs": list_jobs(include_output=False),
    }


def latest_runs(limit: int = 8) -> list[dict]:
    runs_root = WORKSPACE_ROOT / "targets" / "thegraph" / "runs"
    if not runs_root.exists():
        return []
    items = []
    for path in runs_root.iterdir():
        if not path.is_dir():
            continue
        summary = path / "worker-summary.json"
        judgment = path / "judgment.json"
        items.append(
            {
                "name": path.name,
                "modified": datetime.fromtimestamp(path.stat().st_mtime, UTC).isoformat(),
                "has_worker_summary": summary.exists(),
                "has_judgment": judgment.exists(),
            }
        )
    return sorted(items, key=lambda item: item["modified"], reverse=True)[:limit]


def list_jobs(include_output: bool = False) -> list[dict]:
    with JOBS_LOCK:
        jobs = list(JOBS.values())
    return [job.to_dict(include_output=include_output) for job in sorted(jobs, key=lambda item: item.created_at, reverse=True)]


def create_job(action: str, payload: dict) -> DashboardJob:
    specs = job_specs()
    if action not in specs:
        raise ValueError(f"Unsupported action: {action}")
    spec = specs[action]
    job = DashboardJob(
        id=uuid.uuid4().hex[:12],
        action=action,
        label=spec["label"],
        command=spec["command"],
        cwd=spec.get("cwd", WORKSPACE_ROOT),
        timeout_seconds=spec.get("timeout", 300),
    )
    with JOBS_LOCK:
        JOBS[job.id] = job
    thread = threading.Thread(target=run_dashboard_job, args=(job.id,), daemon=True)
    thread.start()
    return job


def job_specs() -> dict[str, dict]:
    py = sys.executable
    return {
        "llm_ping": {
            "label": "Check LM Studio",
            "command": [py, "-m", "backend.hotspot_hub.cli", "llm", "ping"],
            "timeout": 90,
        },
        "tool_status": {
            "label": "Check Local Tools",
            "command": [py, "-m", "backend.hotspot_hub.cli", "tools", "status"],
            "timeout": 180,
        },
        "scan_hotspots": {
            "label": "Scan Hotspots",
            "command": [
                py,
                "-m",
                "backend.hotspot_hub.cli",
                "scan",
                "external/thegraph-contracts",
                "--out",
                "targets/thegraph/code-map/hotspot-report.json",
            ],
            "timeout": 900,
        },
        "generate_local_llm_queue": {
            "label": "Generate Local LLM Queue",
            "command": [
                py,
                "-m",
                "backend.hotspot_hub.cli",
                "worker",
                "generate",
                "targets/thegraph/code-map/hotspot-report.json",
                "--out",
                "queues/thegraph-local-llm.worker.json",
                "--max-hotspots",
                "5",
                "--mode",
                "local-llm",
            ],
            "timeout": 120,
        },
        "run_local_llm_queue": {
            "label": "Run Local LLM Queue",
            "command": [py, "-m", "backend.hotspot_hub.cli", "worker", "run", "queues/thegraph-local-llm.worker.json"],
            "timeout": 1800,
        },
        "run_smoke_queue": {
            "label": "Run Smoke Queue",
            "command": [py, "-m", "backend.hotspot_hub.cli", "worker", "run", "queues/thegraph-smoke.worker.json"],
            "timeout": 900,
        },
    }


def run_dashboard_job(job_id: str) -> None:
    with JOBS_LOCK:
        job = JOBS[job_id]
        job.status = "running"
        job.started_at = datetime.now(UTC).isoformat()
    try:
        result = run_command(job.command, cwd=str(job.cwd), timeout_seconds=job.timeout_seconds)
        with JOBS_LOCK:
            job.returncode = result.returncode
            job.elapsed_seconds = round(result.elapsed_seconds, 3)
            job.stdout = result.stdout
            job.stderr = result.stderr
            job.status = "succeeded" if result.returncode == 0 else "failed"
            job.finished_at = datetime.now(UTC).isoformat()
    except Exception as exc:  # pragma: no cover - defensive thread boundary.
        with JOBS_LOCK:
            job.error = str(exc)
            job.status = "failed"
            job.finished_at = datetime.now(UTC).isoformat()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the local Bug Bounty Workbench dashboard")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=4173, type=int)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    server = ThreadingHTTPServer((args.host, args.port), WorkbenchHandler)
    print(f"Bug Bounty Workbench running at http://{args.host}:{args.port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping dashboard server.")
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
