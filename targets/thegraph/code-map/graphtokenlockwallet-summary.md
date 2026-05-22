# GraphTokenLockWallet Summary

## Plain-English Purpose

`GraphTokenLockWallet` holds GRT under a time-based release schedule while letting beneficiaries use locked tokens in approved protocol calls.

## Value Movement

- `release` transfers currently releasable scheduled tokens to the beneficiary.
- `withdrawSurplus` transfers extra tokens above outstanding scheduled obligations to the beneficiary.
- `revoke` lets the owner reclaim unvested tokens when the wallet is revocable.
- `cancelLock` lets the owner recover the full balance only before the beneficiary accepts the lock.
- `approveProtocol` gives manager-listed protocol destinations unlimited allowance from the wallet.
- `revokeProtocol` only clears allowances for destinations still listed by the current manager.
- The fallback forwards manager-authorized function calls from the beneficiary to approved protocol targets.

## Role Checks

- Only the beneficiary can release tokens, withdraw surplus, accept the lock, change beneficiary, approve protocol, revoke protocol, or use the forwarding fallback.
- Only the owner can cancel an unaccepted lock, revoke a revocable lock, or change the wallet's manager.
- Beneficiary acceptance blocks `cancelLock`, but it does not freeze the owner-controlled manager.
- Forwarded calls are blocked for revocable wallets.
- Forwarded calls require the manager to map `msg.sig` to a nonzero target contract.
- Manager owner controls token destinations and authorized function-selector targets.

## Accounting Invariants

- `releasedAmount + revokedAmount + totalOutstandingAmount` should not exceed `managedAmount`.
- `release` should not let scheduled accounting consume true surplus.
- Revocation should return only unvested scheduled tokens, not beneficiary surplus.
- `withdrawSurplus` should never reduce scheduled funds below outstanding obligations.
- Fallback calls should only be able to move tokens through intentionally authorized protocol functions.
- Removing a token destination should not leave it with practical wallet-spending power if removal is meant to deauthorize it.
- If acceptance is meant to finalize wallet trust assumptions, manager changes after acceptance should be explicitly intended and documented.

## First Things To Hunt

- Rounding in `amountPerPeriod` and `periodDuration`.
- Boundary behavior at exactly `endTime`.
- Surplus interaction with `release` and later `revoke`.
- Stale allowances after token destinations are removed from the manager.
- Function selector collisions in manager-authorized fallback calls.

## Next Step

Assess TLW3 against real manager destination history and real destination pull functions.
