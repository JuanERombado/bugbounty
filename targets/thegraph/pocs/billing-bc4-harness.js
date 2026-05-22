// Local-only model for BC4: can a reverting gateway strand GRT in BillingConnector?
// It models EVM transaction rollback with explicit snapshots.

const assert = require("assert");

class RevertingGateway extends Error {
  constructor(message) {
    super(message);
    this.name = "RevertingGateway";
  }
}

class MockToken {
  constructor() {
    this.balances = new Map([
      ["alice", 100],
      ["BillingConnector", 0],
    ]);
    this.allowances = new Map();
  }

  snapshot() {
    return {
      balances: new Map(this.balances),
      allowances: new Map(this.allowances),
    };
  }

  restore(snapshot) {
    this.balances = new Map(snapshot.balances);
    this.allowances = new Map(snapshot.allowances);
  }

  balanceOf(account) {
    return this.balances.get(account) || 0;
  }

  allowance(owner, spender) {
    return this.allowances.get(`${owner}:${spender}`) || 0;
  }

  transferFrom(owner, to, amount) {
    assert(this.balanceOf(owner) >= amount, "insufficient balance");
    this.balances.set(owner, this.balanceOf(owner) - amount);
    this.balances.set(to, this.balanceOf(to) + amount);
    return true;
  }

  approve(spender, amount) {
    this.allowances.set(`BillingConnector:${spender}`, amount);
    return true;
  }
}

class MockGateway {
  constructor({ shouldRevert }) {
    this.shouldRevert = shouldRevert;
    this.calls = [];
  }

  outboundTransfer(amount) {
    this.calls.push({ amount });
    if (this.shouldRevert) {
      throw new RevertingGateway("gateway reverted");
    }
    return "0x";
  }
}

function addToL2Transactional({ token, gateway, owner, amount }) {
  const snapshot = token.snapshot();
  try {
    token.transferFrom(owner, "BillingConnector", amount);
    token.approve("L1TokenGateway", amount);
    gateway.outboundTransfer(amount);
    return { ok: true };
  } catch (error) {
    token.restore(snapshot);
    return { ok: false, error: error.message };
  }
}

function runCaseGatewayReverts() {
  const token = new MockToken();
  const gateway = new MockGateway({ shouldRevert: true });

  const result = addToL2Transactional({ token, gateway, owner: "alice", amount: 40 });

  assert.strictEqual(result.ok, false, "transaction should fail");
  assert.strictEqual(token.balanceOf("alice"), 100, "alice balance should roll back");
  assert.strictEqual(token.balanceOf("BillingConnector"), 0, "connector should not keep tokens");
  assert.strictEqual(token.allowance("BillingConnector", "L1TokenGateway"), 0, "allowance should roll back");
  return { name: "gateway reverts", result, aliceBalance: token.balanceOf("alice"), connectorBalance: token.balanceOf("BillingConnector") };
}

function runCaseGatewaySucceeds() {
  const token = new MockToken();
  const gateway = new MockGateway({ shouldRevert: false });

  const result = addToL2Transactional({ token, gateway, owner: "alice", amount: 40 });

  assert.strictEqual(result.ok, true, "transaction should succeed");
  assert.strictEqual(token.balanceOf("alice"), 60, "alice balance should decrease");
  assert.strictEqual(token.balanceOf("BillingConnector"), 40, "model keeps tokens until gateway internals move them");
  return { name: "gateway succeeds", result, aliceBalance: token.balanceOf("alice"), connectorBalance: token.balanceOf("BillingConnector") };
}

const cases = [runCaseGatewayReverts(), runCaseGatewaySucceeds()];

console.log(
  JSON.stringify(
    {
      hypothesis: "BC4",
      result: "model confirms a reverting gateway rolls back prior token pull and approval",
      cases,
    },
    null,
    2,
  ),
);
