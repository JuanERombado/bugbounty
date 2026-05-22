"""Run generated real Foundry harness slices."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .hypothesis_queue import make_run_id
from .real_foundry_harness_generator import generate_real_foundry_harness
from .result_judge import judge_real_foundry_result
from .test_runner import run_foundry_tests


def run_real_foundry_slice(
    workspace: Path,
    *,
    target: str,
    repo_root: Path,
    contract_path: str,
    contract_name: str,
    hypothesis_id: str,
    run_id: str | None = None,
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    resolved_run_id = run_id or f"real-{make_run_id(contract_name)}-{hypothesis_id.lower()}"
    run_dir = workspace / "targets" / target / "runs" / resolved_run_id
    generated_dir = workspace / "targets" / target / "pocs" / "generated" / resolved_run_id
    generated_files = generate_real_foundry_harness(
        generated_dir,
        workspace=workspace,
        target=target,
        repo_root=(workspace / repo_root) if not repo_root.is_absolute() else repo_root,
        contract_path=contract_path,
        contract_name=contract_name,
        hypothesis_id=hypothesis_id,
        run_id=resolved_run_id,
    )
    run_payload = run_foundry_tests(generated_dir, run_dir / "foundry-result.json", timeout_seconds)
    judgment = judge_real_foundry_result(
        resolved_run_id,
        run_payload,
        run_dir / "judgment.json",
        target=target,
        contract_name=contract_name,
        hypothesis_id=hypothesis_id,
    )
    return {
        "run_id": resolved_run_id,
        "status": judgment["status"],
        "generated_dir": str(generated_dir),
        "run_dir": str(run_dir),
        "generated_files": [str(path) for path in generated_files],
        "result_file": str(run_dir / "foundry-result.json"),
        "judgment_file": str(run_dir / "judgment.json"),
        "report_ready": False,
        "next_action": judgment["next_action"],
    }
