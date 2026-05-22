# L1GNS Hypotheses

Status legend: `new`, `testing`, `rejected`, `confirmed`.

## GNS1: Uncurated Subgraph Transfer Divides By Zero

- Status: rejected
- Asset: L1GNS
- Hypothesis: `sendSubgraphToL2` divides by `totalSignal`, so an active subgraph with no signal may revert unexpectedly.
- Why it might matter: migration can be blocked for empty but valid subgraphs.
- Impact if true: availability/UX issue, likely not high severity unless it blocks valuable migration state.
- Scope caution: no fund loss unless paired with another state transition.
- Minimal local test idea: publish a new subgraph without minting signal, then call `sendSubgraphToL2` and check the revert.
- Result: local model confirms zero total signal reaches a division-by-zero path.
- Rejection reason: an uncurated subgraph has no curation value at risk, so this is currently a low-severity migration limitation rather than a bounty-grade issue.

## GNS2: Retryable Expiration Can Burn L1 Ownership Before L2 Finalization

- Status: rejected
- Asset: L1GNS / L2GNS
- Hypothesis: `sendSubgraphToL2` finalizes L1 state before the L2 transfer is finished, so an expired retryable could leave the owner with no L1 owner path and no finished L2 subgraph.
- Why it might matter: the owner NFT is burned and the L1 subgraph is disabled after the gateway accepts the transfer.
- Impact if true: owner migration loss or stuck subgraph state.
- Scope caution: retryable expiry is known Arbitrum behavior and comments warn about ticket parameters/refunds.
- Minimal local test idea: model or test gateway acceptance without L2 completion, then verify whether any local recovery path exists.
- Current result: local model confirms L1 state is finalized before L2 completion.
- Current interpretation: high-interest, but not yet reportable without a forced failure or honest-user-loss path beyond expected retryable-ticket risk.
- Evidence that rejects it as a standalone candidate: existing tests confirm the L1 state is intentionally finalized after send, and the bridge/Arbitrum retryable lifecycle is expected to be managed by the caller.
- Rejection reason: documented cross-chain operational risk, not a forced protocol bug as currently framed.

## GNS3: Curator L2 Balance Can Be Lost If The Retryable Expires

- Status: rejected
- Asset: L1GNS
- Hypothesis: `sendCuratorBalanceToBeneficiaryOnL2` zeroes a curator's L1 signal before L2 redemption is guaranteed.
- Why it might matter: the source explicitly warns the caller must redeem the retryable or the signal will be lost.
- Impact if true: curator fund loss from expired retryable.
- Scope caution: this is documented in the function comments, so it may be intended user responsibility rather than a hidden vulnerability.
- Minimal local test idea: model L1 signal zeroing with no L2 execution and confirm no L1 recovery path.
- Current result: local model confirms curator L1 signal and withdrawable balance are reduced before L2 completion is guaranteed.
- Current interpretation: likely documented behavior unless a forced expiry/failure path exists.
- Evidence that rejects it as a standalone candidate: the source comment explicitly warns that the caller must ensure the retryable ticket is redeemed before expiration or signal will be lost.
- Rejection reason: documented user-managed retryable risk, not a hidden vulnerability without a forced-failure path.

## GNS4: Rounding In Owner/Curator Split Can Strand Dust

- Status: rejected
- Asset: L1GNS
- Hypothesis: integer division in `tokensForL2 = ownerNSignal * curationTokens / totalSignal` can leave rounding dust that is not fairly attributed.
- Why it might matter: migration splits value between the owner and remaining curators.
- Impact if true: tiny accounting loss or unfair allocation.
- Scope caution: likely low severity unless dust can be amplified.
- Minimal local test idea: model uneven signal splits and compare owner plus withdrawable totals to burned curation tokens.
- Result: local model shows the owner split conserves total tokens, and sequential curator transfers consume remaining dust through the last claimant.
- Rejection reason: rounding affects exact per-claim timing but does not create or strand value in the modeled flow.

## GNS5: Curator Balance Arriving Before L2 Finish Is Returned Instead Of Minted

- Status: rejected
- Asset: L1GNS / L2GNS
- Hypothesis: if a curator transfers balance before `finishSubgraphTransferFromL1`, L2 returns tokens to the beneficiary instead of minting signal.
- Why it might matter: ordering affects whether the beneficiary gets liquid GRT or L2 curation signal.
- Impact if true: expected but surprising state-dependent value form.
- Scope caution: L2GNS tests already cover return-to-beneficiary behavior.
- Minimal local test idea: review existing L2GNS tests and mark rejected if covered.
- Evidence that rejects it: existing L2GNS tests cover not-finished, nonexistent, L2-native, deprecated, and active finished subgraph cases.
- Result: tokens are returned to the beneficiary when signal cannot be safely minted.
- Rejection reason: behavior is intentional and covered by tests.

## Picked First Test

GNS1 was checked first because it only needed one active uncurated subgraph and no bridge execution.

## Next Step

L1GNS pass result: all five starter hypotheses are rejected or documented behavior, with local evidence.

Next best target: `GraphTokenLockWallet`, because it is the next ranked asset and has token custody plus access-control behavior.
