# HorizonStaking First-Pass Notes

## What We Checked

- Staking and provisioning value movement.
- Delegation share accounting.
- Slashing while provider or delegator funds are thawing.
- Thaw request ordering after provision parameter changes.
- Legacy SubgraphService compatibility paths.
- Permissionless legacy force withdrawal.

## Main Result

No high- or medium-confidence report candidate yet.

The only confirmed new behavior is HZ3: a later thaw request can be expired but temporarily blocked behind an earlier unexpired request after the thawing period is shortened.

## Why HZ3 Is Probably Low

- The code comment already acknowledges this ordering behavior.
- Funds are delayed, not stolen.
- The delay ends when the earlier request expires.
- It requires provision parameter changes that involve the service provider and verifier flow.

## Verification Gap

The local Foundry test was added, but `forge` is not installed in this environment, so only the JS model was run.

## Next Step

Move to a payments/accounting surface with clearer direct-value impact, such as `SubgraphService`, `PaymentsEscrow`, `RecurringCollector`, or `AllocationExchange`.
