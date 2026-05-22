#!/usr/bin/env python3
"""Rank in-scope assets for local bug bounty investigation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


WEIGHTS = {
    "staking": 10,
    "rewards": 10,
    "bridge": 10,
    "cross-chain": 10,
    "escrow": 9,
    "curation": 8,
    "disputes": 8,
    "accounting": 8,
    "state-transition": 7,
    "access-control": 7,
    "permission": 7,
    "message-validation": 7,
    "delegation": 6,
    "economic": 6,
    "billing": 5,
    "registry": 4,
    "token": 3,
    "governance": 3,
}


def score_asset(asset: dict) -> tuple[int, list[str]]:
    fields = " ".join(
        [
            asset.get("name", ""),
            asset.get("category", ""),
            asset.get("notes", ""),
            " ".join(asset.get("priority_tags", [])),
        ]
    ).lower()
    matched = [key for key in WEIGHTS if key in fields]
    return sum(WEIGHTS[key] for key in matched), matched


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scope_json", type=Path)
    parser.add_argument("--markdown", type=Path, default=Path("targets/thegraph/assets/ranked-assets.md"))
    parser.add_argument("--json", type=Path, default=Path("targets/thegraph/assets/ranked-assets.json"))
    args = parser.parse_args()

    data = json.loads(args.scope_json.read_text(encoding="utf-8"))
    ranked = []
    for asset in data["assets_in_scope"]:
        score, matched = score_asset(asset)
        ranked.append({**asset, "rank_score": score, "matched_weight_terms": matched})
    ranked.sort(key=lambda item: (-item["rank_score"], item["name"], item.get("chain", "")))

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(ranked, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Ranked Assets",
        "",
        "Local-only investigation priority for The Graph. Re-run `scripts/rank_assets.py` after updating scope.",
        "",
        "| Rank | Score | Asset | Chain | Why first |",
        "| ---: | ---: | --- | --- | --- |",
    ]
    for index, asset in enumerate(ranked, start=1):
        why = ", ".join(asset["matched_weight_terms"]) or "manual review"
        lines.append(
            f"| {index} | {asset['rank_score']} | {asset['name']} | {asset.get('chain', '')} | {why} |"
        )
    args.markdown.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {args.markdown}")
    print(f"Wrote {args.json}")
    for index, asset in enumerate(ranked[:10], start=1):
        print(f"{index:>2}. {asset['name']} ({asset.get('chain', '')}) score={asset['rank_score']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
