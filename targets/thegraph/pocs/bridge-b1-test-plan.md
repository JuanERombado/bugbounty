# Bridge B1 Test Plan

## Hypothesis

A failed retryable-ticket creation might move GRT into `BridgeEscrow` without creating a valid L2 ticket.

## Local Test Shape

1. Configure the local L1 bridge harness.
2. Approve the L1 gateway to spend the sender's GRT.
3. Force the bridge/inbox path to fail after `outboundTransfer` starts.
4. Assert the transaction reverts.
5. Assert sender and escrow GRT balances are unchanged.

## Expected Safe Result

The whole transaction reverts, including the GRT transfer into escrow.

## Vulnerable Result

The sender loses GRT to escrow while no L2 retryable ticket is created.

## Test Result

- Test added: `rolls back escrow transfer if retryable ticket creation fails`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/gateway/l1GraphTokenGateway.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/gateway/l1GraphTokenGateway.test.ts --grep "rolls back escrow"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

The GRT transfer into escrow and retryable-ticket creation are atomic, so a failed retryable creation does not trap the sender's GRT in escrow.

## Next Step

Test B2: confirm that router-path calldata cannot bypass the callhook allowlist.
