# No-Tread Patterns

These are patterns that are not automatically invalid, but are crowded enough that they need a duplicate gate before PoC work.

## JIT Escrow Availability

- Pattern: collection fails because just-in-time escrow funding cannot happen in the exact needed state.
- Known overlap: `TRST-M-2`.
- Continue only if: the variant bypasses the post-audit mitigation or uses a materially different call path.

## Callback Gas Griefing

- Pattern: payer or receiver callbacks consume gas, return huge data, or change behavior after acceptance.
- Known overlap: `TRST-H-1`, `TRST-M-4`, `TRST-L-8`, `TRST-L-9`.
- Continue only if: current callback bounds or gas checks can still be bypassed.

## ERC165 / Interface Assumption Bugs

- Pattern: malformed interface responses escape expected validation.
- Known overlap: `TRST-H-2`.
- Continue only if: a different interface gate still mishandles malformed or changing support.

## Deposit-To / Dust Griefing

- Pattern: third-party deposits distort escrow state or thaw behavior.
- Known overlap: `TRST-M-1`, `TRST-L-4`.
- Continue only if: dust can cause meaningful locked funds, payout failure, or repeated disruption after thresholds.

## Escrow Mode Degradation

- Pattern: one agreement changes global escrow mode or funding guarantees.
- Known overlap: `TRST-M-3`.
- Continue only if: an untrusted actor can force degradation or create a direct fund-loss path.
