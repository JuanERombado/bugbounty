# HorizonStaking HZ3 Test Plan

## Question

Can an earlier long thaw request block a later already-expired thaw request after the provision thawing period is shortened?

## Why It Matters

Thaw requests are fulfilled in creation order, not by expiration time.

## Result

Confirmed in a local JS model: after the shortened period passes, the later request is expired but `getThawedTokens` returns zero because the earlier request is still unexpired.

A Solidity Foundry test was added to the local repo, but it could not be run here because `forge` is not installed.

## Commands

```powershell
node targets/thegraph/pocs/horizonstaking-hz3-harness.js
```

```powershell
cd external/thegraph-contracts/packages/horizon
forge test --match-test testThaw_ShortenedPeriodLaterExpiredRequestBlockedByEarlierRequest
```

## Candidate Severity

Likely low because the later request is delayed, not stolen, and the behavior requires provision parameter changes accepted by the verifier.

## Next Step

Test HZ1: delegation share rounding near `MIN_DELEGATION`.
