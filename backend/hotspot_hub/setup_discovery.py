"""Lightweight Solidity setup discovery for real harness planning."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .models import utc_now_iso

ACCESS_CONTROL_WORDS = [
    "admin",
    "auth",
    "authorize",
    "authorized",
    "controller",
    "governor",
    "guardian",
    "onlyowner",
    "owner",
    "pause",
    "permission",
    "role",
]

ACCOUNTING_VALUE_WORDS = [
    "accounting",
    "allocation",
    "balance",
    "claim",
    "collect",
    "deposit",
    "escrow",
    "fee",
    "payment",
    "reward",
    "share",
    "slash",
    "stake",
    "token",
    "transfer",
    "withdraw",
]


def discover_setup(
    source_path: Path,
    out_path: Path,
    *,
    target: str,
    run_id: str,
    repo_root: Path,
    contract_path: str,
    contract_name: str,
) -> dict[str, Any]:
    """Extract shallow setup hints from a Solidity file and write JSON."""

    text = source_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    contract_declaration = _contract_declaration(text, lines, contract_name)
    payload = {
        "run_id": run_id,
        "target": target,
        "repo_root": str(repo_root),
        "contract_path": contract_path,
        "contract_name": contract_name,
        "source_file": str(source_path),
        "generated_at": utc_now_iso(),
        "contract_declaration_line": contract_declaration,
        "constructor_signature": _constructor_signature(text),
        "inherited_contracts": _inherited_contracts(contract_declaration),
        "imports": _imports(text),
        "external_public_functions": _external_public_functions(text),
        "modifiers": _modifiers(text),
        "access_control_words": _matched_words(text, ACCESS_CONTROL_WORDS),
        "accounting_value_words": _matched_words(text, ACCOUNTING_VALUE_WORDS),
        "notes": [
            "Regex-only discovery for harness planning; this is not a security finding.",
            "Use these hints to choose constructor args, mocks, actor roles, and one real invariant.",
        ],
    }
    payload["summary"] = {
        "import_count": len(payload["imports"]),
        "external_public_function_count": len(payload["external_public_functions"]),
        "modifier_count": len(payload["modifiers"]),
        "has_constructor": payload["constructor_signature"] is not None,
        "has_access_control_hints": bool(payload["access_control_words"]),
        "has_accounting_value_hints": bool(payload["accounting_value_words"]),
    }

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return payload


def _contract_declaration(text: str, lines: list[str], contract_name: str) -> dict[str, Any] | None:
    pattern = re.compile(rf"\b(?:abstract\s+)?contract\s+{re.escape(contract_name)}\b[^\{{;]*", flags=re.DOTALL)
    match = pattern.search(text)
    if match:
        line_no = text[: match.start()].count("\n") + 1
        return {"line": line_no, "text": _compact(match.group(0))}

    fallback = re.compile(rf"^\s*(?:abstract\s+)?contract\s+{re.escape(contract_name)}\b[^\{{;]*")
    for line_no, line in enumerate(lines, start=1):
        match = fallback.search(line)
        if match:
            return {"line": line_no, "text": match.group(0).strip()}
    return None


def _constructor_signature(text: str) -> str | None:
    match = re.search(r"\bconstructor\s*\([^)]*\)\s*(?:[^{;]*)", text, flags=re.MULTILINE | re.DOTALL)
    if not match:
        return None
    return _compact(match.group(0))


def _inherited_contracts(contract_declaration: dict[str, Any] | None) -> list[str]:
    if not contract_declaration:
        return []
    text = contract_declaration["text"]
    if " is " not in text:
        return []
    inherited = text.split(" is ", 1)[1]
    return [item.strip() for item in inherited.split(",") if item.strip()]


def _imports(text: str) -> list[str]:
    imports = []
    for match in re.finditer(r"^\s*import\s+(.+?);", text, flags=re.MULTILINE):
        imports.append(_compact(match.group(0)))
    return imports


def _external_public_functions(text: str) -> list[dict[str, str]]:
    functions = []
    pattern = re.compile(
        r"\bfunction\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)\s*(external|public)\b([^;{]*)",
        flags=re.MULTILINE | re.DOTALL,
    )
    for match in pattern.finditer(text):
        functions.append(
            {
                "name": match.group(1),
                "visibility": match.group(3),
                "signature": _compact(match.group(0)),
            }
        )
    return functions


def _modifiers(text: str) -> list[dict[str, str]]:
    modifiers = []
    for match in re.finditer(r"\bmodifier\s+([A-Za-z_][A-Za-z0-9_]*)\s*(\([^)]*\))?", text):
        modifiers.append({"name": match.group(1), "signature": _compact(match.group(0))})
    return modifiers


def _matched_words(text: str, words: list[str]) -> list[str]:
    lowered = text.lower()
    return sorted({word for word in words if word in lowered})


def _compact(value: str) -> str:
    return " ".join(value.split())
