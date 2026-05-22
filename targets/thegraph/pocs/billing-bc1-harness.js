// Local-only model of BillingConnector._addToL2 for BC1.
// This does not touch any chain; it checks the call sequence we want to port into Solidity tests.

const assert = require("assert");

class MockToken {
  constructor({ transferFromReturns = true, approveReturns = true } = {}) {
    this.transferFromReturns = transferFromReturns;
    this.approveReturns = approveReturns;
    this.transferFromCalls = [];
    this.approveCalls = [];
  }

  transferFrom(owner, to, amount) {
    this.transferFromCalls.push({ owner, to, amount });
    return this.transferFromReturns;
  }

  approve(spender, amount) {
    this.approveCalls.push({ spender, amount });
    return this.approveReturns;
  }
}

class MockGateway {
  constructor() {
    this.outboundTransferCalls = [];
  }

  outboundTransfer(token, to, amount, maxGas, gasPriceBid, data, value) {
    this.outboundTransferCalls.push({ token, to, amount, maxGas, gasPriceBid, data, value });
    return "0x";
  }
}

function billingConnectorAddToL2({ token, gateway, owner, destination, amount }) {
  // Mirrors BillingConnector.sol lines 219-232: return values are not checked.
  token.transferFrom(owner, "BillingConnector", amount);
  const extraData = { destination };
  const data = { maxSubmissionCost: 1, extraData };
  token.approve("L1TokenGateway", amount);
  gateway.outboundTransfer("GraphToken", "L2Billing", amount, 100000, 1, data, 0);
  return { event: "TokensSentToL2", owner, destination, amount };
}

function runCase(name, tokenOptions) {
  const token = new MockToken(tokenOptions);
  const gateway = new MockGateway();
  const result = billingConnectorAddToL2({
    token,
    gateway,
    owner: "alice",
    destination: "aliceOnL2",
    amount: 100,
  });

  assert.strictEqual(token.transferFromCalls.length, 1, `${name}: transferFrom not called`);
  assert.strictEqual(token.approveCalls.length, 1, `${name}: approve not called`);
  assert.strictEqual(gateway.outboundTransferCalls.length, 1, `${name}: gateway not called`);
  assert.strictEqual(result.event, "TokensSentToL2", `${name}: event missing`);
  return { name, gatewayCalled: true, emitted: result.event };
}

const cases = [
  runCase("transferFrom returns false", { transferFromReturns: false }),
  runCase("approve returns false", { approveReturns: false }),
];

console.log(JSON.stringify({ hypothesis: "BC1", result: "model confirms connector continues after false return", cases }, null, 2));
