"""Run local validation commands and capture normalized artifacts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .subprocess_tools import run_command


def run_foundry_tests(project_dir: Path, out_path: Path, timeout_seconds: int = 180) -> dict[str, Any]:
    result = run_command(["forge", "test", "-vv"], cwd=str(project_dir), timeout_seconds=timeout_seconds)
    payload = {
        "runner": "foundry",
        "project_dir": str(project_dir),
        "command": result.command,
        "returncode": result.returncode,
        "elapsed_seconds": round(result.elapsed_seconds, 3),
        "stdout": result.stdout,
        "stderr": result.stderr,
        "passed": result.returncode == 0,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def run_foundry_command(
    project_dir: Path,
    out_path: Path,
    forge_args: list[str],
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    result = run_command(["forge", *forge_args], cwd=str(project_dir), timeout_seconds=timeout_seconds)
    payload = {
        "runner": "foundry",
        "project_dir": str(project_dir),
        "command": result.command,
        "returncode": result.returncode,
        "elapsed_seconds": round(result.elapsed_seconds, 3),
        "stdout": result.stdout,
        "stderr": result.stderr,
        "passed": result.returncode == 0,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload
