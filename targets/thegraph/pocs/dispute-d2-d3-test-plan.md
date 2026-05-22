# Dispute D2/D3 Test Plan

## Question

Do linked conflict disputes resolve both sides consistently, and what events are emitted when a draw resolves both?

## Local-Only Setup

- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/disputes/query.test.ts`
- Contract under test: `DisputeManager`
- Flow: create linked conflict disputes from two conflicting attestations, then accept or draw either side.

## Tests Added Or Tightened

- `should draw one dispute and resolve the related dispute`
- `resolves linked conflict disputes consistently from either side`
- `emits one draw event when drawing linked conflict disputes`

## Expected Safe Behavior

Accepting one side should finalize both disputes, and drawing one side should finalize both disputes.

## Result

Rejected as a candidate finding.

The state transitions are safe, but the draw path emits only one `DisputeDrawn` event even though both linked disputes become `Drawn`.

## Command

```powershell
pnpm exec hardhat test --network hardhat tests/unit/disputes/query.test.ts --grep "resolves linked conflict|emits one draw event|should draw one dispute"
```

## Evidence

- `3 passing`
- Accepting either side resolves the chosen side as `Accepted` and the twin as `Rejected`.
- Drawing either side resolves both disputes as `Drawn`.
- Drawing emits one `DisputeDrawn` event for the called dispute only.

## Next Step

Move to `BillingConnector` and map accounting, permissions, and withdrawal/payment flows.
