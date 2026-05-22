# GraphTokenLockWallet Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## TLW1: Uneven Period Math Can Overstate Releasable Tokens

- Status: confirmed-low
- Asset: GraphTokenLockWallet / GraphTokenLock
- Hypothesis: when `duration` or `managedAmount` is not evenly divisible by `periods`, `availableAmount` can exceed `managedAmount` near the end and `release` can consume surplus as if it were scheduled.
- Why it might matter: release accounting could push `releasedAmount` above `managedAmount`, breaking later outstanding/surplus calculations.
- Impact if true: accounting breakage or fund misclassification.
- Scope caution: only the beneficiary can call `release`, and surplus is also beneficiary-withdrawable.
- Minimal local test idea: model uneven `duration`, `periods`, and extra balance, then see if `releasedAmount > managedAmount`.
- Result: local model and Hardhat test confirm that exact-`endTime` release can consume surplus and set `releasedAmount > managedAmount`.
- Candidate severity: likely low because only the beneficiary can trigger it and the extra tokens are surplus they could withdraw anyway.
- Evidence file: `external/thegraph-contracts/packages/token-distribution/test/tokenLock.test.ts`.

## TLW2: Revocation After Edge-Case Release Can Underflow Outstanding Accounting

- Status: confirmed-low
- Asset: GraphTokenLockWallet / GraphTokenLock
- Hypothesis: if `releasedAmount` exceeds `managedAmount`, later calls to `totalOutstandingAmount` or `surplusAmount` may underflow.
- Why it might matter: underflow can block surplus withdrawal or other balance views.
- Impact if true: beneficiary funds may become harder to recover.
- Scope caution: depends on TLW1 being reachable.
- Minimal local test idea: run TLW1, then call outstanding/surplus calculations after release.
- Result: confirmed as a consequence of TLW1; `totalOutstandingAmount()` reverts with `SafeMath: subtraction overflow` after over-release.
- Candidate severity: likely low unless it can trap funds or break a high-value integration.

## TLW3: Removed Token Destinations Keep Existing Allowance

- Status: confirmed
- Asset: GraphTokenLockWallet / GraphTokenLockManager
- Hypothesis: removing a destination from the manager does not automatically revoke allowances already granted by wallets.
- Why it might matter: a formerly approved protocol destination may retain token-pulling power.
- Impact if true: stale allowance risk.
- Scope caution: beneficiary can call `revokeProtocol`, and manager changes are governance/owner actions.
- Minimal local test idea: approve a destination, remove it from manager, then check the token allowance remains nonzero.
- Current result: local model confirms `revokeProtocol` cannot revoke destinations that the manager no longer returns.
- Current interpretation: worth a Hardhat test because stale allowance can matter if a removed destination later becomes unsafe.
- Result: Hardhat test confirms the removed destination keeps `MaxUint256` allowance after `revokeProtocol`.
- Follow-up result: a test-only removed destination with a callable `transferFrom` path can still pull wallet funds after removal and after `revokeProtocol`.
- Candidate severity: potentially meaningful if destination removal is used as a safety/deauthorization mechanism and a real old destination can still pull funds, but not submission-ready until a real in-scope destination path is identified.
- Evidence file: `external/thegraph-contracts/packages/token-distribution/test/tokenLockWallet.test.ts`.

## TLW4: Function Selector Collision Can Forward To An Unexpected Target

- Status: rejected
- Asset: GraphTokenLockWallet / GraphTokenLockManager
- Hypothesis: manager authorization is keyed only by `bytes4 msg.sig`, so a selector collision could route unexpected calldata to an authorized target.
- Why it might matter: fallback forwarding is a trust boundary.
- Impact if true: unintended protocol call from wallet.
- Scope caution: manager owner chooses allowed signatures and targets; target function behavior still matters.
- Minimal local test idea: enumerate authorized selectors and compare against wallet/internal selectors and high-risk target selectors.
- Result: local selector check found zero collisions across the wallet functions and known manager-authorized signatures from staking, transfer tools, Horizon staking, and SubgraphService.
- Evidence file: `targets/thegraph/pocs/graphtokenlockwallet-tlw4-selector-check.js`.

## TLW5: Owner Can Change Manager After Beneficiary Acceptance

- Status: confirmed-behavior
- Asset: GraphTokenLockWallet
- Hypothesis: the owner can change the manager even after the beneficiary accepts the lock, changing future allowed calls and approval destinations.
- Why it might matter: accepted beneficiaries may assume protocol-call permissions are stable.
- Impact if true: governance/owner trust risk.
- Scope caution: owner authority is likely intended for distribution administration.
- Minimal local test idea: accept lock, change manager, and confirm forwarding/approval behavior follows the new manager.
- Result: Hardhat test confirms an accepted lock can be pointed to a new manager; future `approveProtocol` uses the new manager's destinations and fallback authorization follows the new manager.
- Candidate severity: likely low or intended-admin behavior unless documentation or trust assumptions say acceptance should freeze the manager.
- Evidence file: `external/thegraph-contracts/packages/token-distribution/test/tokenLockWallet.test.ts`.

## Picked First Test

TLW1 is first because it directly touches release accounting and can be modeled without live contracts.

## Next Step

Close the GraphTokenLockWallet pass by running the focused tests together, then choose the next high-value asset.
