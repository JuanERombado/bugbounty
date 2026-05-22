"""Small subprocess helpers for scanner adapters."""

from __future__ import annotations

import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class CommandResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    elapsed_seconds: float


def command_exists(binary: str, cwd: str | Path | None = None) -> bool:
    root = Path(cwd) if cwd is not None else Path.cwd()
    return shutil.which(binary) is not None or find_local_binary(binary, root) is not None


def find_local_binary(binary: str, cwd: Path) -> str | None:
    if binary.lower() in {"python", "python.exe", "pip", "pip.exe"}:
        return None

    names = [binary]
    if not binary.lower().endswith(".exe"):
        names.append(f"{binary}.exe")

    for root in [cwd, *cwd.parents]:
        for tool_dir in (root / ".tools").glob("*"):
            scripts_dir = tool_dir / "Scripts"
            bin_dir = tool_dir / "bin"
            for candidate_dir in (scripts_dir, bin_dir, tool_dir):
                for name in names:
                    candidate = candidate_dir / name
                    if candidate.exists():
                        return str(candidate)
    return None


def local_tool_paths(cwd: Path) -> list[str]:
    paths: list[str] = []
    for root in [cwd, *cwd.parents]:
        tools_root = root / ".tools"
        if not tools_root.exists():
            continue
        for tool_dir in tools_root.glob("*"):
            if not tool_dir.is_dir():
                continue
            for candidate_dir in (tool_dir / "Scripts", tool_dir / "bin", tool_dir):
                if candidate_dir.exists():
                    paths.append(str(candidate_dir))
    return paths


def run_command(command: list[str], cwd: str, timeout_seconds: int = 120) -> CommandResult:
    resolved_command = list(command)
    cwd_path = Path(cwd)
    resolved_binary = find_local_binary(command[0], cwd_path) or shutil.which(command[0])
    if resolved_binary:
        resolved_command[0] = resolved_binary
    env = os.environ.copy()
    extra_paths = local_tool_paths(cwd_path)
    if extra_paths:
        env["PATH"] = os.pathsep.join([*extra_paths, env.get("PATH", "")])
    use_shell = Path(resolved_command[0]).suffix.lower() in {".bat", ".cmd"}
    command_arg = subprocess.list2cmdline(resolved_command) if use_shell else resolved_command
    started = time.perf_counter()
    completed = subprocess.run(
        command_arg,
        cwd=cwd,
        env=env,
        shell=use_shell,
        capture_output=True,
        text=True,
        timeout=timeout_seconds,
        check=False,
    )
    elapsed = time.perf_counter() - started
    return CommandResult(
        command=resolved_command,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
        elapsed_seconds=elapsed,
    )
