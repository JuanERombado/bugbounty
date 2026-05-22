# L1GNS GNS4 Test Plan

## Question

Can rounding in the owner/curator split strand or create GRT during L1-to-L2 migration?

## Why It Matters

The split uses integer division, so tiny dust differences are expected unless the remaining state absorbs them safely.

## Command

```powershell
node targets/thegraph/pocs/l1gns-gns4-harness.js
```

## Result

Rejected as a bounty candidate.

The model shows the owner split conserves total tokens, and sequential curator transfers consume remaining dust because each transfer recalculates against the current remaining `withdrawableGRT` and signal.

## Next Step

Check GNS5, then close the L1GNS pass if existing tests already cover the ordering behavior.
