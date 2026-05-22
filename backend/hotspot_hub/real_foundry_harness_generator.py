"""Generate Foundry harnesses that import real target contracts."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def generate_real_foundry_harness(
    project_dir: Path,
    *,
    workspace: Path,
    target: str,
    repo_root: Path,
    contract_path: str,
    contract_name: str,
    hypothesis_id: str,
    run_id: str,
) -> list[Path]:
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "test").mkdir(exist_ok=True)

    repo_root = repo_root.resolve()
    contract_import = _normalize_import(contract_path)
    metadata = {
        "run_id": run_id,
        "target": target,
        "repo_root": str(repo_root),
        "contract_path": contract_path,
        "contract_name": contract_name,
        "hypothesis_id": hypothesis_id,
        "status": "real_harness_generated",
        "report_ready": False,
    }

    written = [
        _write(project_dir / "foundry.toml", _foundry_toml(workspace, repo_root, contract_path)),
        _write(project_dir / "test" / f"{contract_name}RealHarness.t.sol", _test_source(contract_import, contract_name, hypothesis_id)),
        _write(project_dir / "README.md", _readme(metadata)),
        _write(project_dir / "harness.json", json.dumps(metadata, indent=2) + "\n"),
    ]
    return written


def _write(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def _normalize_import(contract_path: str) -> str:
    return contract_path.replace("\\", "/").lstrip("/")


def _foundry_toml(workspace: Path, repo_root: Path, contract_path: str) -> str:
    workspace_s = workspace.resolve().as_posix()
    repo_s = repo_root.resolve().as_posix()
    package_root = _package_root(repo_root, contract_path)
    package_s = package_root.resolve().as_posix()
    return f"""[profile.default]
src = "src"
test = "test"
out = "out"
libs = ["lib", "{package_s}/node_modules", "{repo_s}/node_modules", "{repo_s}/lib"]
solc_version = "0.8.27"
optimizer = true
optimizer_runs = 200
remappings = [
  "@graphprotocol/={repo_s}/packages/",
  "@openzeppelin/={package_s}/node_modules/@openzeppelin/",
  "packages/={repo_s}/packages/",
  "forge-std/={package_s}/node_modules/forge-std/src/",
  "external/={workspace_s}/external/"
]

[fmt]
line_length = 120
tab_width = 4
bracket_spacing = true
"""


def _package_root(repo_root: Path, contract_path: str) -> Path:
    parts = Path(contract_path).parts
    if len(parts) >= 2 and parts[0] == "packages":
        candidate = repo_root / parts[0] / parts[1]
        if candidate.exists():
            return candidate
    return repo_root


def _test_source(contract_import: str, contract_name: str, hypothesis_id: str) -> str:
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{{contract_name}}} from "{contract_import}";

contract {contract_name}RealHarnessTest {{
    {contract_name} internal target;

    // Hypothesis: {hypothesis_id}
    // This file only proves whether a real-contract harness can compile.
    // Replace this constructor path with mocks/setup before interpreting runtime failures.
    function test_{_safe_identifier(hypothesis_id)}_realHarnessCompiles() public view {{
        target;
    }}
}}
"""


def _safe_identifier(value: str) -> str:
    safe = "".join(char if char.isalnum() else "_" for char in value)
    return safe.strip("_") or "hypothesis"


def _readme(metadata: dict[str, Any]) -> str:
    return f"""# Real Foundry Harness

Target: `{metadata["target"]}`

Contract: `{metadata["contract_name"]}`

Hypothesis: `{metadata["hypothesis_id"]}`

This harness imports the real contract path and runs `forge test`.

Statuses are conservative:

- `compile_failed`: imports/remappings/mocks need work.
- `harness_needs_mocks`: constructor or setup is not wired.
- `clean`: generated compile smoke passed.

Generated tests alone are never report-ready.
"""
