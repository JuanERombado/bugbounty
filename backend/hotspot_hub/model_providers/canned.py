"""Deterministic fallback hypotheses."""

from __future__ import annotations


class CannedProvider:
    name = "canned"

    def generate(self, hotspot_report: dict, max_items: int = 5) -> list[dict]:
        hotspots = hotspot_report.get("hotspots", [])[:max_items]
        items = []
        for index, hotspot in enumerate(hotspots, start=1):
            path = hotspot.get("path", "unknown")
            tags = hotspot.get("tags", [])
            focus = _focus_from_tags(tags)
            items.append(
                {
                    "id": f"CANNED-{index:03d}",
                    "source": self.name,
                    "hotspot_path": path,
                    "title": f"{focus} invariant review for {path.split('/')[-1]}",
                    "hypothesis": _hypothesis_for_focus(focus),
                    "local_test_idea": _test_for_focus(focus),
                    "rejection_rule": "Reject if a local test shows the invariant is already enforced or the behavior maps only to self-approved/user-error conditions.",
                    "report_ready": False,
                }
            )
        return items


def _focus_from_tags(tags: list[str]) -> str:
    lowered = {tag.lower() for tag in tags}
    if {"bridge", "cross-chain"} & lowered:
        return "cross-chain message/accounting"
    if {"access-control", "permission", "roles"} & lowered:
        return "access-control"
    if {"accounting", "rewards", "staking", "escrow", "curation"} & lowered:
        return "value-accounting"
    return "state-transition"


def _hypothesis_for_focus(focus: str) -> str:
    return {
        "cross-chain message/accounting": "A local message or retryable-ticket edge can finalize accounting on one side without enforceable success on the other side.",
        "access-control": "A caller, operator, or proxy boundary may allow a non-authorized actor to make a value-affecting state transition.",
        "value-accounting": "Deposits, withdrawals, shares, rewards, or claims can drift from contract balance or protocol accounting after an edge-case sequence.",
        "state-transition": "A lifecycle transition can be repeated, skipped, or reordered in a way that violates the intended state machine.",
    }[focus]


def _test_for_focus(focus: str) -> str:
    return {
        "cross-chain message/accounting": "Build local mocks for both sides and assert no balance/credit changes survive failed message execution.",
        "access-control": "Fuzz caller identities and assert unauthorized actors cannot change value-affecting state.",
        "value-accounting": "Run a local invariant over deposit/withdraw/claim/cancel sequences and assert conservation after every step.",
        "state-transition": "Model allowed states and assert invalid transitions revert and valid transitions cannot be replayed.",
    }[focus]
