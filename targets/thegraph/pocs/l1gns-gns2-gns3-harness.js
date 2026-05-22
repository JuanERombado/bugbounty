// Local-only model for GNS2/GNS3: L1 state after L2 retryable is accepted but never completed.

const assert = require("assert");

function sendSubgraphToL2({ ownerSignal, otherSignal, curationTokens }) {
  const totalSignal = ownerSignal + otherSignal;
  assert(totalSignal > 0n, "needs signal");

  const tokensForL2 = (ownerSignal * curationTokens) / totalSignal;
  return {
    l1: {
      ownerSignal: 0n,
      otherSignal,
      totalSignal: otherSignal,
      withdrawableGRT: curationTokens - tokensForL2,
      disabled: true,
      nftExists: false,
      transferredToL2: true,
    },
    l2: {
      retryableExecuted: false,
      subgraphReceived: false,
      transferFinished: false,
      ownerSignal: 0n,
    },
    bridge: {
      tokensForL2,
    },
  };
}

function sendCuratorBalanceToL2(state, { curatorSignal, beneficiary }) {
  assert(state.l1.transferredToL2, "subgraph must be transferred");
  assert(curatorSignal > 0n, "curator needs signal");
  assert(state.l1.totalSignal > 0n, "subgraph needs remaining signal");

  const tokensForL2 = (curatorSignal * state.l1.withdrawableGRT) / state.l1.totalSignal;
  state.l1.otherSignal -= curatorSignal;
  state.l1.totalSignal -= curatorSignal;
  state.l1.withdrawableGRT -= tokensForL2;

  return {
    l1: state.l1,
    l2: {
      retryableExecuted: false,
      beneficiary,
      curatorSignalMinted: 0n,
    },
    bridge: {
      tokensForL2,
    },
  };
}

function runCaseOwnerRetryableNeverCompletes() {
  const state = sendSubgraphToL2({
    ownerSignal: 90n,
    otherSignal: 10n,
    curationTokens: 1000n,
  });

  assert.strictEqual(state.l1.ownerSignal, 0n, "owner L1 signal should be zero");
  assert.strictEqual(state.l1.disabled, true, "L1 subgraph should be disabled");
  assert.strictEqual(state.l1.nftExists, false, "L1 NFT should be burned");
  assert.strictEqual(state.l2.transferFinished, false, "L2 transfer should not be finished");
  return {
    name: "owner retryable never completes",
    l1: stringifyBigInts(state.l1),
    l2: stringifyBigInts(state.l2),
    bridge: stringifyBigInts(state.bridge),
  };
}

function runCaseCuratorRetryableNeverCompletes() {
  const afterOwnerSend = sendSubgraphToL2({
    ownerSignal: 90n,
    otherSignal: 10n,
    curationTokens: 1000n,
  });
  const state = sendCuratorBalanceToL2(afterOwnerSend, {
    curatorSignal: 10n,
    beneficiary: "otherOnL2",
  });

  assert.strictEqual(state.l1.otherSignal, 0n, "curator L1 signal should be zero");
  assert.strictEqual(state.l1.withdrawableGRT, 0n, "withdrawable balance should be reduced");
  assert.strictEqual(state.l2.retryableExecuted, false, "L2 execution should not be assumed");
  return {
    name: "curator retryable never completes",
    l1: stringifyBigInts(state.l1),
    l2: stringifyBigInts(state.l2),
    bridge: stringifyBigInts(state.bridge),
  };
}

function stringifyBigInts(value) {
  return Object.fromEntries(Object.entries(value).map(([key, val]) => [key, typeof val === "bigint" ? val.toString() : val]));
}

const cases = [runCaseOwnerRetryableNeverCompletes(), runCaseCuratorRetryableNeverCompletes()];

console.log(
  JSON.stringify(
    {
      hypotheses: ["GNS2", "GNS3"],
      result:
        "model confirms L1 state finalizes before L2 completion; this is high-interest but likely documented retryable-ticket risk",
      cases,
    },
    null,
    2,
  ),
);
