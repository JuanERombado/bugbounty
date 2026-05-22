#!/usr/bin/env python3
"""Create a lightweight Solidity contract map from a local repo clone."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CONTRACT_RE = re.compile(r"\b(contract|library|interface)\s+([A-Za-z_][A-Za-z0-9_]*)")
FUNCTION_RE = re.compile(r"\bfunction\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
MODIFIER_RE = re.compile(r"\bmodifier\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
EVENT_RE = re.compile(r"\bevent\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(")
BLOCK_COMMENT_RE = re.compile(r"/\*.*?\*/", re.DOTALL)
LINE_COMMENT_RE = re.compile(r"//.*")


def find_solidity_files(root: Path) -> list[Path]:
    ignored = {"node_modules", "lib", "cache", "out", "artifacts", ".git"}
    files = []
    for path in root.rglob("*.sol"):
        if any(part in ignored for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def strip_comments(text: str) -> str:
    text = BLOCK_COMMENT_RE.sub("", text)
    return LINE_COMMENT_RE.sub("", text)


def tags_for(path: Path, text: str, scope_terms: set[str]) -> list[str]:
    haystack = f"{path.as_posix()} {text[:4000]}".lower()
    tags = []
    for term in sorted(scope_terms):
        if term and term.lower() in haystack:
            tags.append(term)
    for term in ["staking", "rewards", "curation", "dispute", "bridge", "escrow", "billing", "governor"]:
        if term in haystack and term not in tags:
            tags.append(term)
    return tags[:12]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path, help="Local clone of graphprotocol/contracts or another in-scope repo")
    parser.add_argument("--scope", type=Path, default=Path("targets/thegraph/scope/thegraph.scope.json"))
    parser.add_argument("--out", type=Path, default=Path("targets/thegraph/code-map/contracts-map.md"))
    args = parser.parse_args()

    if not args.repo.exists():
        raise SystemExit(f"Repo path does not exist: {args.repo}")

    scope = json.loads(args.scope.read_text(encoding="utf-8")) if args.scope.exists() else {}
    scope_terms = {
        asset["name"].lower()
        for asset in scope.get("assets_in_scope", [])
        if asset.get("name")
    }
    for asset in scope.get("assets_in_scope", []):
        scope_terms.update(tag.lower() for tag in asset.get("priority_tags", []))

    rows = []
    for file_path in find_solidity_files(args.repo):
        text = file_path.read_text(encoding="utf-8", errors="ignore")
        code = strip_comments(text)
        contracts = [match.group(2) for match in CONTRACT_RE.finditer(code)]
        if not contracts:
            continue
        rows.append(
            {
                "path": file_path,
                "contracts": contracts,
                "functions": FUNCTION_RE.findall(code),
                "modifiers": MODIFIER_RE.findall(code),
                "events": EVENT_RE.findall(code),
                "tags": tags_for(file_path.relative_to(args.repo), text, scope_terms),
            }
        )

    rows.sort(key=lambda row: (0 if row["tags"] else 1, str(row["path"]).lower()))

    args.out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Contract Map",
        "",
        f"Source repo: `{args.repo}`",
        "",
        "Use this as an index, then ask AI to explain one high-priority contract at a time.",
        "",
    ]
    for row in rows:
        relative = row["path"].relative_to(args.repo)
        lines.extend(
            [
                f"## `{relative}`",
                "",
                f"- Contracts: {', '.join(row['contracts'])}",
                f"- Tags: {', '.join(row['tags']) if row['tags'] else 'none'}",
                f"- Functions: {', '.join(row['functions'][:25]) if row['functions'] else 'none'}",
                f"- Modifiers: {', '.join(row['modifiers'][:15]) if row['modifiers'] else 'none'}",
                f"- Events: {', '.join(row['events'][:15]) if row['events'] else 'none'}",
                "",
            ]
        )

    args.out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {args.out} with {len(rows)} Solidity files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
