# First-Pass Attack Map

This map is for local-only research. It is not a finding list.

## Priority 1: L1Staking

- Why: staking, delegation, reward eligibility, and accounting state interact directly with participant funds.
- Plain-English risk: a bad state transition could make the contract account for stake, delegation, allocation, or withdrawals incorrectly.
- First local tests: delegation accounting invariants, unstake/withdraw timing, allocation close paths, reward update ordering, permissioned function boundaries.
- Out-of-scope traps: basic governance majority attacks, centralization complaints, and slashing-only impact without accepted direct fund-loss framing.

## Priority 2: BridgeEscrow

- Why: escrow plus bridge assumptions can create high-impact fund movement bugs.
- Plain-English risk: funds may be locked, released, or accounted for under the wrong cross-chain assumption.
- First local tests: authorized gateway boundaries, escrow balance invariants, replay-like local message simulations, failed bridge message accounting.
- Out-of-scope traps: testing public bridge deployments or third-party bridge systems directly.

## Priority 3: Curation

- Why: curation uses economic share math and touches curator funds.
- Plain-English risk: mint/burn/share math could transfer value incorrectly if edge cases break invariants.
- First local tests: round-trip signal mint/burn, reserve ratio extremes, tax accounting, reward update ordering.
- Out-of-scope traps: natural unprofitable curation behavior is explicitly out of scope.

## Priority 4: ArbitrumInbox and Messenger Logic

- Why: cross-chain message sender and aliasing assumptions are subtle.
- Plain-English risk: caller identity or message replay assumptions may differ between local, L1, and L2 contexts.
- First local tests: sender alias helpers, inbox caller restrictions, message target/callvalue assumptions.
- Out-of-scope traps: sending real public L1/L2 transactions.

## Priority 5: RewardsManager

- Why: accepted impacts focus on user funds in protocol smart contracts, and rewards are a core accounting surface.
- Plain-English risk: accrual, claiming, or distribution can drift from stake and allocation state.
- First local tests: double-claim prevention, stale allocation state, reward snapshot updates, zero/edge allocation behavior.
- Out-of-scope traps: speculative token price impact.

## Priority 6: DisputeManager

- Why: dispute lifecycle transitions can affect participants and permissions.
- Plain-English risk: a dispute could be created, accepted, rejected, or finalized by the wrong actor or in the wrong state.
- First local tests: lifecycle transition matrix, role checks, repeated action prevention, dispute deposit accounting.
- Out-of-scope traps: known audit issues and slashing-only impact framing.

## Priority 7: BillingConnector and L1GNS

- Why: connectors and registry-style contracts are trust-boundary surfaces.
- Plain-English risk: the wrong caller or stale registry state could cause unwanted participant actions.
- First local tests: caller restrictions, ownership transfer paths, registry update ordering, connector target assumptions.
- Out-of-scope traps: best-practice-only critiques.

## Next 3 Tasks

1. Read `targets/thegraph/code-map/contracts-map.md` entries for `L1Staking`, `BridgeEscrow`, and `Curation`.
2. Use `prompts/contract-explainer.md` on one contract at a time.
3. Convert only one hypothesis into one local test before moving to the next idea.
