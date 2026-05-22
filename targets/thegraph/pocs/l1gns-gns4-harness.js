// Local-only model for GNS4: rounding in L1GNS owner/curator migration split.

const assert = require("assert");

function splitTokens({ ownerSignal, totalSignal, curationTokens }) {
  const tokensForL2 = (ownerSignal * curationTokens) / totalSignal;
  const withdrawableGRT = curationTokens - tokensForL2;
  return { tokensForL2, withdrawableGRT };
}

function distributeRemainingCurators({ curatorSignals, withdrawableGRT }) {
  let remainingSignal = curatorSignals.reduce((sum, value) => sum + value, 0n);
  let remainingGRT = withdrawableGRT;
  const payouts = [];

  for (const signal of curatorSignals) {
    const payout = (signal * remainingGRT) / remainingSignal;
    payouts.push(payout);
    remainingGRT -= payout;
    remainingSignal -= signal;
  }

  return { payouts, remainingGRT, remainingSignal };
}

function runCaseSingleSplitConservesTokens() {
  const curationTokens = 1000n;
  const split = splitTokens({ ownerSignal: 1n, totalSignal: 3n, curationTokens });

  assert.strictEqual(split.tokensForL2 + split.withdrawableGRT, curationTokens);
  return {
    name: "owner split conserves total tokens",
    tokensForL2: split.tokensForL2.toString(),
    withdrawableGRT: split.withdrawableGRT.toString(),
    total: (split.tokensForL2 + split.withdrawableGRT).toString(),
  };
}

function runCaseSequentialCuratorWithdrawalsConsumeAll() {
  const curationTokens = 1000n;
  const split = splitTokens({ ownerSignal: 1n, totalSignal: 4n, curationTokens });
  const distribution = distributeRemainingCurators({
    curatorSignals: [1n, 1n, 1n],
    withdrawableGRT: split.withdrawableGRT,
  });

  assert.strictEqual(distribution.remainingGRT, 0n);
  assert.strictEqual(distribution.remainingSignal, 0n);
  return {
    name: "sequential curator transfers consume remaining dust",
    ownerTokensForL2: split.tokensForL2.toString(),
    curatorPayouts: distribution.payouts.map(String),
    remainingGRT: distribution.remainingGRT.toString(),
  };
}

function runCaseUnevenSignalsConsumeAll() {
  const curationTokens = 1001n;
  const split = splitTokens({ ownerSignal: 7n, totalSignal: 23n, curationTokens });
  const distribution = distributeRemainingCurators({
    curatorSignals: [3n, 5n, 8n],
    withdrawableGRT: split.withdrawableGRT,
  });

  assert.strictEqual(distribution.remainingGRT, 0n);
  assert.strictEqual(distribution.remainingSignal, 0n);
  return {
    name: "uneven sequential curator transfers consume all remaining GRT",
    ownerTokensForL2: split.tokensForL2.toString(),
    curatorPayouts: distribution.payouts.map(String),
    remainingGRT: distribution.remainingGRT.toString(),
  };
}

const cases = [
  runCaseSingleSplitConservesTokens(),
  runCaseSequentialCuratorWithdrawalsConsumeAll(),
  runCaseUnevenSignalsConsumeAll(),
];

console.log(
  JSON.stringify(
    {
      hypothesis: "GNS4",
      result:
        "rounding can affect individual payout order by tiny amounts, but remaining withdrawable state is conserved and consumed by the last claimant",
      cases,
    },
    null,
    2,
  ),
);
