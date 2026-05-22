# L1GNS GNS1 Test Plan

## Question

What happens if an owner sends an active but uncurated subgraph to L2?

## Why This Is First

`sendSubgraphToL2` divides by total subgraph signal, so zero signal is the simplest edge case.

## Local-Only Setup

- File to use: `external/thegraph-contracts/packages/contracts-test/tests/unit/gns.test.ts`
- Contract under test: `L1GNS`
- Flow: publish a new subgraph, do not mint signal, then call `sendSubgraphToL2`.

## Expected Safe Behavior

Either the function should reject with a clear message before division or support zero-signal migration without value movement.

## Candidate-Bug Behavior

If the function reverts from division by zero, empty subgraphs cannot migrate through this path.

## Likely Severity

Low unless it blocks meaningful value, ownership, or recovery.

## Command

```powershell
node targets/thegraph/pocs/l1gns-gns1-harness.js
```

## Result

Rejected as a bounty candidate for now.

The model confirms the zero-signal path would divide by zero, but an uncurated subgraph has no curation value at risk and this looks like a migration limitation rather than a medium/high/critical impact.

## Next Step

Move to GNS2/GNS3 and model retryable expiry after L1 state is finalized.
