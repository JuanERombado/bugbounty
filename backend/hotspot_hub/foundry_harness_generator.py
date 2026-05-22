"""Generate a Foundry scaffold for validating queued hypotheses."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def generate_foundry_scaffold(project_dir: Path, queue_payload: dict[str, Any]) -> list[Path]:
    project_dir.mkdir(parents=True, exist_ok=True)
    (project_dir / "src").mkdir(exist_ok=True)
    (project_dir / "test").mkdir(exist_ok=True)

    written = [
        _write(project_dir / "foundry.toml", _foundry_toml()),
        _write(project_dir / "src" / "ValidationHarness.sol", _harness_source(queue_payload)),
        _write(project_dir / "test" / "GeneratedInvariant.t.sol", _test_source(queue_payload)),
        _write(project_dir / "README.md", _readme(queue_payload)),
        _write(project_dir / "hypotheses.json", json.dumps(queue_payload, indent=2) + "\n"),
    ]
    return written


def _write(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def _foundry_toml() -> str:
    return """[profile.default]
src = "src"
test = "test"
out = "out"
libs = ["lib"]
solc_version = "0.8.27"
optimizer = true
optimizer_runs = 200

[fmt]
line_length = 100
tab_width = 4
bracket_spacing = true
"""


def _harness_source(queue_payload: dict[str, Any]) -> str:
    contract_name = queue_payload["contract_name"]
    contract_path = queue_payload["contract_path"]
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

/// @notice Placeholder harness for {contract_name}.
/// @dev Replace this model with imports/mocks for: {contract_path}
contract ValidationHarness {{
    uint256 public deposits;
    uint256 public paidOut;
    uint256 public lastRate;
    address public authorizedActor;
    bool public valueAffectingState;

    constructor() {{
        authorizedActor = msg.sender;
    }}

    function modelDeposit(uint256 amount) external {{
        amount = bound(amount, 0, 1e30);
        deposits += amount;
    }}

    function modelCollect(uint256 elapsed, uint256 rate, uint256 entities) external {{
        elapsed = bound(elapsed, 0, 365 days);
        rate = bound(rate, 0, 1e24);
        entities = bound(entities, 0, 1e9);
        lastRate = rate;

        uint256 requested = elapsed * rate * (entities + 1);
        if (requested > deposits - paidOut) {{
            requested = deposits - paidOut;
        }}
        paidOut += requested;
    }}

    function modelUnauthorizedStateChange(address caller) external {{
        if (caller == authorizedActor) {{
            valueAffectingState = true;
        }}
    }}

    function solvencyHolds() external view returns (bool) {{
        return paidOut <= deposits;
    }}

    function bound(uint256 value, uint256 min, uint256 max) internal pure returns (uint256) {{
        if (max <= min) return min;
        return min + (value % (max - min + 1));
    }}
}}
"""


def _test_source(queue_payload: dict[str, Any]) -> str:
    candidates = queue_payload["candidates"]
    comments = "\n".join(
        f"// {item['id']}: {item['title']}\n// Invariant: {item['invariant']}\n// Rejection: {item['rejection_rule']}"
        for item in candidates
    )
    return f"""// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import {{ValidationHarness}} from "../src/ValidationHarness.sol";

contract GeneratedInvariantTest {{
    ValidationHarness internal harness;

    function setUp() public {{
        harness = new ValidationHarness();
    }}

{comments}

    function test_INV_1_valueConservationSkeleton() public {{
        harness.modelDeposit(100 ether);
        harness.modelCollect(1 days, 1 ether, 3);
        require(harness.solvencyHolds(), "value conservation failed");
    }}

    function test_INV_2_authorizationSkeleton() public {{
        harness.modelUnauthorizedStateChange(address(0xBEEF));
        require(!harness.valueAffectingState(), "unauthorized state transition");
    }}

    function test_INV_3_boundedRateSkeleton() public {{
        harness.modelDeposit(type(uint128).max);
        harness.modelCollect(type(uint32).max, type(uint96).max, type(uint32).max);
        require(harness.solvencyHolds(), "bounded-rate accounting failed");
    }}
}}
"""


def _readme(queue_payload: dict[str, Any]) -> str:
    return f"""# Generated Foundry Validation Scaffold

Target: `{queue_payload["target"]}`

Contract: `{queue_payload["contract_name"]}`

Source path: `{queue_payload["contract_path"]}`

This is a compile-and-run scaffold, not a confirmed PoC.

Next step: replace `src/ValidationHarness.sol` with real imports, mocks, and calls, then keep only tests that can prove or reject paid-impact behavior locally.
"""
