#!/usr/bin/env python3
"""Create a new bounty target workspace from the generic template."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", help="Target name, for example 'The Graph' or 'Example Protocol'")
    parser.add_argument("--program-url", default="", help="Official bounty URL")
    args = parser.parse_args()

    slug = slugify(args.name)
    if not slug:
        raise SystemExit("Target name must contain at least one letter or number.")

    root = Path("targets") / slug
    for child in ["scope", "assets", "audits", "code-map", "hypotheses", "pocs", "reports"]:
        (root / child).mkdir(parents=True, exist_ok=True)

    scope = {
        "target": {
            "name": args.name,
            "program_url": args.program_url,
            "last_verified": "",
            "max_bounty_usd": 0,
            "notes": ["Fill this from the official bounty information, scope, and resources pages."],
        },
        "source_pages": [
            {"name": "Information", "url": args.program_url},
            {"name": "Scope", "url": ""},
            {"name": "Resources", "url": ""},
        ],
        "rules": {
            "hard_guardrails": [
                "Use local repo analysis, local tests, or local forks only.",
                "Do not attack live systems.",
                "Do not test against public mainnet or public testnet deployments.",
                "Do not generate traffic-heavy scanners.",
            ],
            "prohibited_activities": [],
            "out_of_scope": [],
            "reporting_requirements": [],
        },
        "impacts_in_scope": [],
        "assets_in_scope": [],
        "audits": [],
        "resources": [],
    }

    scope_path = root / "scope" / f"{slug}.scope.json"
    if not scope_path.exists():
        scope_path.write_text(json.dumps(scope, indent=2) + "\n", encoding="utf-8")

    (root / "hypotheses" / "README.md").write_text(
        "# Hypotheses\n\nTrack one testable local-only claim at a time.\n",
        encoding="utf-8",
    )
    (root / "reports" / "README.md").write_text(
        "# Reports\n\nDraft only after a confirmed local PoC.\n",
        encoding="utf-8",
    )

    print(f"Created {root}")
    print(f"Next: fill {scope_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
