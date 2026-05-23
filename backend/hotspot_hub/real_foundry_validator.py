"""Run generated real Foundry harness slices."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from .hypothesis_queue import make_run_id
from .real_foundry_harness_generator import generate_real_foundry_harness
from .result_judge import judge_real_foundry_result
from .setup_discovery import discover_setup
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
    resolved_repo_root = (workspace / repo_root) if not repo_root.is_absolute() else repo_root
    resolved_repo_root = resolved_repo_root.resolve()
    generated_files = generate_real_foundry_harness(
        generated_dir,
        workspace=workspace,
        target=target,
        repo_root=resolved_repo_root,
        contract_path=contract_path,
        contract_name=contract_name,
        hypothesis_id=hypothesis_id,
        run_id=resolved_run_id,
    )
    setup_discovery_file = run_dir / "setup-discovery.json"
    setup_discovery = discover_setup(
        resolved_repo_root / contract_path,
        setup_discovery_file,
        target=target,
        run_id=resolved_run_id,
        repo_root=resolved_repo_root,
        contract_path=contract_path,
        contract_name=contract_name,
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
    next_action_file = run_dir / "next-action.md"
    next_action_file.write_text(
        _next_action_markdown(
            judgment=judgment,
            setup_discovery=setup_discovery,
            setup_discovery_file=setup_discovery_file,
        ),
        encoding="utf-8",
    )
    return {
        "run_id": resolved_run_id,
        "status": judgment["status"],
        "generated_dir": str(generated_dir),
        "run_dir": str(run_dir),
        "generated_files": [str(path) for path in generated_files],
        "result_file": str(run_dir / "foundry-result.json"),
        "judgment_file": str(run_dir / "judgment.json"),
        "setup_discovery_file": str(setup_discovery_file),
        "next_action_file": str(next_action_file),
        "report_ready": False,
        "next_action": judgment["next_action"],
    }


def _next_action_markdown(
    *,
    judgment: dict[str, Any],
    setup_discovery: dict[str, Any],
    setup_discovery_file: Path,
) -> str:
    status = judgment["status"]
    compile_succeeded = status == "clean_compile_smoke"
    summary = setup_discovery["summary"]
    needed = _needed_setup(status)
    return f"""# Real Foundry Slice Next Action

Status: `{status}`

Import/compile succeeded: `{str(compile_succeeded).lower()}`

Setup discovery found:
- Contract declaration: `{_display(setup_discovery["contract_declaration_line"])}`
- Constructor present: `{str(summary["has_constructor"]).lower()}`
- Inherited contracts: `{", ".join(setup_discovery["inherited_contracts"]) or "none found"}`
- Imports: `{summary["import_count"]}`
- External/public functions: `{summary["external_public_function_count"]}`
- Modifiers: `{summary["modifier_count"]}`
- Access-control hints: `{", ".join(setup_discovery["access_control_words"]) or "none found"}`
- Accounting/value hints: `{", ".join(setup_discovery["accounting_value_words"]) or "none found"}`

Next manual harness step:
{judgment["next_action"]}

Likely setup need:
{needed}

Artifacts:
- Setup discovery: `{setup_discovery_file}`

Safety reminder:
This is local harness planning only, not bounty evidence and not report-ready.
"""


def _needed_setup(status: str) -> str:
    if status == "harness_needs_import_remappings":
        return "Fix remappings or dependency paths before behavior testing."
    if status == "harness_needs_constructor_args":
        return "Add constructor args, inherited constructor args, or proxy initializer setup."
    if status == "harness_needs_mocks":
        return "Add minimal local mocks/interfaces for external protocol dependencies."
    if status == "clean_compile_smoke":
        return "Choose one public/external behavior and replace the smoke test with a real invariant."
    if status == "compile_failed":
        return "Inspect compiler output to decide whether imports, constructor args, or mocks are blocking."
    return "Inspect stdout/stderr, then repair only the generated harness."


def _display(value: Any) -> str:
    if value is None:
        return "not found"
    if isinstance(value, dict):
        return value.get("text", str(value))
    return str(value)
