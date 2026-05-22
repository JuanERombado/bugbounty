// Local-only model for GNS1: sendSubgraphToL2 with zero total signal.

const assert = require("assert");

function sendSubgraphToL2Model({ ownerNSignal, totalSignal, curationTokens }) {
  if (totalSignal === 0n) {
    throw new Error("division by zero");
  }

  const tokensForL2 = (ownerNSignal * curationTokens) / totalSignal;
  return {
    tokensForL2,
    withdrawableGRT: curationTokens - tokensForL2,
    ownerNSignalAfter: 0n,
    totalSignalAfter: totalSignal - ownerNSignal,
    disabled: true,
    transferredToL2: true,
  };
}

function runCaseUncuratedSubgraph() {
  let error;
  try {
    sendSubgraphToL2Model({ ownerNSignal: 0n, totalSignal: 0n, curationTokens: 0n });
  } catch (err) {
    error = err.message;
  }

  assert.strictEqual(error, "division by zero");
  return { name: "active uncurated subgraph", error };
}

function runCaseCuratedSubgraph() {
  const result = sendSubgraphToL2Model({
    ownerNSignal: 90n,
    totalSignal: 100n,
    curationTokens: 1000n,
  });

  assert.strictEqual(result.tokensForL2, 900n);
  assert.strictEqual(result.withdrawableGRT, 100n);
  return {
    name: "curated subgraph",
    result: {
      tokensForL2: result.tokensForL2.toString(),
      withdrawableGRT: result.withdrawableGRT.toString(),
      disabled: result.disabled,
      transferredToL2: result.transferredToL2,
    },
  };
}

const cases = [runCaseUncuratedSubgraph(), runCaseCuratedSubgraph()];

console.log(
  JSON.stringify(
    {
      hypothesis: "GNS1",
      result: "model confirms zero-signal transfer would hit division by zero, but impact appears low without funds at risk",
      cases,
    },
    null,
    2,
  ),
);
