# Common Web3 Bounty Tactics and Procedures

Use this as a learning map, not a scanner checklist.

## Critical and High Lanes

- Value-flow tracing: follow every token, share, escrow, claim, mint, burn, and withdrawal path.
- State-machine review: find actions that can happen twice, happen out of order, or happen after a terminal state.
- Access-control review: map who can call privileged functions and how that identity can be confused.
- Cross-chain review: test local message sender, replay, aliasing, and finalization assumptions.
- Accounting invariants: assert that internal balances match token balances and that total shares map to total value.
- Oracle and external dependency review: model stale, delayed, or manipulated inputs without attacking live third parties.
- Upgrade and proxy review: check initializer, storage layout, admin, pause, and implementation-boundary assumptions.
- Test-suite gap mining: compare existing tests with the protocol's promised invariants.

## Medium and Low Lanes

- Rounding and precision drift.
- Broken lifecycle edge cases with limited impact.
- Griefing that does not rise to direct fund loss.
- Documentation and implementation mismatches.
- Best-practice observations, which are often out of scope.

## Repeatable Procedure

1. Scope gate: is the asset in scope?
2. Impact gate: does the idea map to a paid impact?
3. Rule gate: is any required step out of scope?
4. Audit gate: is it already known?
5. Local model: can the behavior be reproduced locally?
6. Minimal PoC: can one test prove the issue?
7. Report gate: can the impact be explained without exaggeration?
