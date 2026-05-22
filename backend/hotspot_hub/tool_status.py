"""Tool discovery and disk usage reporting for the local workbench."""

from __future__ import annotations

import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from .subprocess_tools import find_local_binary, local_tool_paths, run_command


@dataclass(frozen=True)
class ToolSpec:
    name: str
    binary: str
    version_args: list[str]
    category: str
    priority: str
    purpose: str


@dataclass(frozen=True)
class ToolStatus:
    name: str
    binary: str
    category: str
    priority: str
    purpose: str
    installed: bool
    source: str | None
    version: str | None
    local_size_mb: float | None
    status: str


CORE_TOOLS = [
    ToolSpec("Python", "python", ["--version"], "runtime", "required", "Runs backend scripts and Python scanners."),
    ToolSpec("Node.js", "node", ["--version"], "runtime", "required", "Runs JS tooling, Hardhat, and frontend builds."),
    ToolSpec("npm", "npm", ["--version"], "runtime", "required", "Installs JavaScript dependencies."),
    ToolSpec("pnpm", "pnpm", ["--version"], "runtime", "high", "Installs target JavaScript dependencies with a shared package store."),
    ToolSpec("Git", "git", ["--version"], "runtime", "required", "Clones repositories and inspects history."),
    ToolSpec("Foundry forge", "forge", ["--version"], "smart-contract", "required", "Compiles and tests Solidity projects."),
    ToolSpec("Foundry cast", "cast", ["--version"], "smart-contract", "required", "Queries and encodes EVM data locally."),
    ToolSpec("Foundry anvil", "anvil", ["--version"], "smart-contract", "required", "Runs a local Ethereum dev chain."),
    ToolSpec("Solidity compiler", "solc", ["--version"], "smart-contract", "required", "Compiles Solidity contracts outside Foundry when scanners need a standalone compiler."),
    ToolSpec("solc-select", "solc-select", ["--version"], "smart-contract", "required", "Installs and switches exact Solidity compiler versions."),
    ToolSpec("Slither", "slither", ["--version"], "scanner", "required", "Runs Solidity static analysis."),
    ToolSpec("Semgrep", "semgrep", ["--version"], "scanner", "high", "Runs pattern-based static analysis."),
    ToolSpec("Echidna", "echidna", ["--version"], "fuzzer", "high", "Runs Solidity property fuzzing and invariant testing."),
    ToolSpec("Medusa", "medusa", ["--version"], "fuzzer", "high", "Runs fast Solidity fuzz campaigns."),
    ToolSpec("Halmos", "halmos", ["--version"], "symbolic", "medium", "Runs symbolic testing for Foundry-style tests."),
    ToolSpec("Mythril", "myth", ["--version"], "symbolic", "medium", "Runs EVM symbolic analysis for triage."),
    ToolSpec("Scribble", "scribble", ["--version"], "instrumentation", "medium", "Instruments Solidity assertions for runtime checking."),
    ToolSpec("Aderyn", "aderyn", ["--version"], "scanner", "medium", "Runs an additional Solidity static-analysis perspective."),
    ToolSpec("Surya", "surya", ["--version"], "mapping", "low", "Generates Solidity inheritance, call graph, and structure views."),
    ToolSpec("jq", "jq", ["--version"], "utility", "medium", "Inspects scanner JSON output from the terminal."),
    ToolSpec("Graphviz dot", "dot", ["-V"], "utility", "medium", "Renders call graphs and architecture diagrams."),
    ToolSpec("Docker", "docker", ["--version"], "isolation", "optional", "Runs isolated tools and reproducible environments."),
    ToolSpec("Cargo", "cargo", ["--version"], "runtime", "optional", "Builds Rust-based tools and fuzzers."),
]


def collect_tool_status(cwd: Path) -> dict[str, Any]:
    cwd = cwd.resolve()
    tools = [_status_for_tool(spec, cwd) for spec in CORE_TOOLS]
    local_dirs = _local_tool_dirs(cwd)
    return {
        "workspace": str(cwd),
        "python": sys.version.split()[0],
        "local_tool_paths": local_tool_paths(cwd),
        "local_tool_dirs": [
            {"name": path.name, "path": str(path), "size_mb": _dir_size_mb(path)}
            for path in local_dirs
        ],
        "local_tools_total_mb": round(sum(_dir_size_bytes(path) for path in local_dirs) / (1024 * 1024), 1),
        "tools": [asdict(tool) for tool in tools],
    }


def _status_for_tool(spec: ToolSpec, cwd: Path) -> ToolStatus:
    source = shutil.which("python") if spec.binary == "python" else find_local_binary(spec.binary, cwd) or shutil.which(spec.binary)
    installed = source is not None
    version = _version_for(spec, cwd) if installed else None
    local_size = _local_size_for_source(source, cwd) if source else None
    status = "installed" if installed else "missing"
    return ToolStatus(
        name=spec.name,
        binary=spec.binary,
        category=spec.category,
        priority=spec.priority,
        purpose=spec.purpose,
        installed=installed,
        source=source,
        version=version,
        local_size_mb=local_size,
        status=status,
    )


def _version_for(spec: ToolSpec, cwd: Path) -> str | None:
    try:
        result = run_command([spec.binary, *spec.version_args], cwd=str(cwd), timeout_seconds=30)
    except Exception as exc:  # noqa: BLE001 - status command should never crash on one bad tool.
        return f"version check failed: {exc}"

    text = (result.stdout or result.stderr).strip()
    if not text:
        return f"version check exited {result.returncode}"
    return text.splitlines()[0]


def _local_tool_dirs(cwd: Path) -> list[Path]:
    for root in [cwd, *cwd.parents]:
        tools_root = root / ".tools"
        if tools_root.exists():
            return sorted([path for path in tools_root.iterdir() if path.is_dir()])
    return []


def _local_size_for_source(source: str | None, cwd: Path) -> float | None:
    if not source:
        return None
    source_path = Path(source).resolve()
    for tool_dir in _local_tool_dirs(cwd):
        try:
            source_path.relative_to(tool_dir.resolve())
        except ValueError:
            continue
        return _dir_size_mb(tool_dir)
    return None


def _dir_size_mb(path: Path) -> float:
    return round(_dir_size_bytes(path) / (1024 * 1024), 1)


def _dir_size_bytes(path: Path) -> int:
    total = 0
    for item in path.rglob("*"):
        if item.is_file():
            try:
                total += item.stat().st_size
            except OSError:
                continue
    return total
