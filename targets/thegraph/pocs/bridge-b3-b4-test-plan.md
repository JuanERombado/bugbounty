# Bridge B3/B4 Test Plan

## Hypothesis

Mint allowance or mixed escrow-plus-mint accounting might allow more L1 GRT to be released than the bridge should permit.

## Local Test Shape

1. Deposit GRT into escrow through `outboundTransfer`.
2. Configure a small L2 mint allowance.
3. Withdraw more GRT than escrow contains, forcing the gateway to mint only the shortfall.
4. Attempt a second withdrawal for more than the remaining allowance.
5. Assert the second withdrawal reverts.

## Expected Safe Result

The first withdrawal mints only the shortfall, and the second withdrawal cannot reuse already-consumed allowance.

## Vulnerable Result

The second withdrawal succeeds even though it exceeds remaining allowance.

## Test Result

- Test added: `does not reuse consumed L2 mint allowance after a mixed escrow and mint withdrawal`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/gateway/l1GraphTokenGateway.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/gateway/l1GraphTokenGateway.test.ts --grep "does not reuse consumed"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

After the first withdrawal consumes escrow and mints the shortfall, `totalMintedFromL2` prevents that allowance from being reused by a later withdrawal.

## Next Step

Close this bridge pass unless we want to explore governance/operational B5, then move to the next ranked asset: `Curation`.
