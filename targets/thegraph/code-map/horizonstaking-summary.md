# HorizonStaking Summary

## Plain-English Purpose

`HorizonStaking` is the newer staking system where service providers stake GRT, lock portions of that stake into verifier provisions, and delegators delegate GRT to those provisions.

## Value Movement

- `stake` and `stakeTo` pull GRT from the caller into staking and increase a service provider's total stake.
- `unstake` immediately withdraws idle stake back to the service provider.
- `provision` moves idle provider stake into a slashable verifier-specific provision.
- `thaw` starts removing provider stake from a provision; `deprovision` completes removal after the thawing period.
- `delegate` pulls GRT from the caller into a delegation pool and mints delegation shares.
- `undelegate` burns delegation shares and creates a thaw request; `withdrawDelegated` pays thawed GRT back.
- `slash` burns provider stake first, may pay a verifier cut, and can slash delegation only after delegation slashing is enabled.

## Role Checks

- Service providers can operate on their own provisions.
- Operators can act for a service provider only when authorized for the verifier.
- Verifiers can slash their own provision for a service provider.
- Governor controls allowed locked verifiers, max thawing period, and whether delegation slashing is enabled.
- Legacy SubgraphService paths use special legacy delegation/operator storage.

## Accounting Invariants

- A service provider's `tokensProvisioned` should not exceed `tokensStaked`.
- Provision `tokens` should cover `tokensThawing`.
- Delegation pool `tokens` should cover `tokensThawing`.
- Pool shares should track token ownership through delegation, undelegation, slashing, and withdrawal.
- Slashing should never let verifier rewards exceed the configured max cut.
- Thaw request fulfillment should not lose or unlock more value than intended.

## First Things To Hunt

- Rounding around delegation share minting and undelegation share burning.
- Slashing while provider or delegator tokens are thawing.
- Thaw request ordering when thawing periods are changed.
- Legacy SubgraphService compatibility paths.
- Operator authorization edge cases across verifier-specific and legacy storage.

## Next Step

Generate local-only hypotheses and start with the smallest accounting edge case.
