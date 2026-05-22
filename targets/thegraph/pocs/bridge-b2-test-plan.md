# Bridge B2 Test Plan

## Hypothesis

Router-path calldata might bypass the callhook allowlist and attach arbitrary callhook data to a bridge transfer.

## Local Test Shape

1. Configure the local L1 bridge harness.
2. Encode router-style data with a real `from` address and non-empty callhook bytes.
3. Call `outboundTransfer` as the router.
4. Assert the call reverts with `CALL_HOOK_DATA_NOT_ALLOWED`.
5. Assert no GRT moves into escrow.

## Expected Safe Result

Router-submitted non-empty callhook data is rejected because the router cannot be callhook-allowlisted.

## Vulnerable Result

Router-submitted callhook data is accepted and can trigger unexpected destination-side execution.

## Test Result

- Test added: `rejects nonempty callhook data sent through the router path`
- File: `external/thegraph-contracts/packages/contracts-test/tests/unit/gateway/l1GraphTokenGateway.test.ts`
- Command: `pnpm exec hardhat test --network hardhat tests/unit/gateway/l1GraphTokenGateway.test.ts --grep "rejects nonempty callhook"`
- Result: `1 passing`
- Finding status: rejected.

## What We Learned

The router path cannot attach callhook data unless the router is allowlisted, and the configured router is deliberately kept out of the callhook allowlist.

## Next Step

Test B3/B4 together by stressing mint allowance and partial escrow shortfall accounting.
