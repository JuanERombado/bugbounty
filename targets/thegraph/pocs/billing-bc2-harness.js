// Local-only model of BillingConnector.removeOnL2 and L2 Billing.removeFromL1.
// This illustrates retryable-ticket semantics without touching any chain.

const assert = require("assert");

class MockInbox {
  constructor() {
    this.nextSeqNum = 1;
    this.tickets = [];
  }

  createRetryableTicket({ destAddr, refundTo, data, value }) {
    const ticket = {
      seqNum: this.nextSeqNum++,
      destAddr,
      refundTo,
      data,
      value,
      executed: false,
    };
    this.tickets.push(ticket);
    return ticket.seqNum;
  }
}

class MockL2Billing {
  constructor() {
    this.balances = new Map();
    this.events = [];
  }

  balanceOf(user) {
    return this.balances.get(user) || 0;
  }

  credit(user, amount) {
    this.balances.set(user, this.balanceOf(user) + amount);
  }

  removeFromL1({ from, to, amount, calledByConnectorAlias }) {
    assert.strictEqual(calledByConnectorAlias, true, "only L1 connector alias can call");

    if (this.balanceOf(from) < amount) {
      this.events.push({ event: "InsufficientBalanceForRemoval", from, to, amount });
      return false;
    }

    this.balances.set(from, this.balanceOf(from) - amount);
    this.events.push({ event: "TokensRemoved", from, to, amount });
    return true;
  }
}

function removeOnL2({ inbox, sender, to, amount, maxSubmissionCost }) {
  assert.notStrictEqual(amount, 0, "Must remove more than 0");
  assert.notStrictEqual(to, "0x0", "destination != 0");
  assert.notStrictEqual(to, sender, "destination != sender");
  assert.notStrictEqual(maxSubmissionCost, 0, "Submission cost must be > 0");

  const data = { selector: "removeFromL1", from: sender, to, amount };
  const seqNum = inbox.createRetryableTicket({
    destAddr: "L2Billing",
    refundTo: to,
    data,
    value: maxSubmissionCost,
  });

  return { event: "RemovalRequestSentToL2", from: sender, to, amount, seqNum };
}

function runCaseTicketCreatedButNotExecuted() {
  const inbox = new MockInbox();
  const l2Billing = new MockL2Billing();
  l2Billing.credit("alice", 100);

  const request = removeOnL2({ inbox, sender: "alice", to: "aliceWallet", amount: 50, maxSubmissionCost: 1 });

  assert.strictEqual(inbox.tickets.length, 1, "ticket not created");
  assert.strictEqual(l2Billing.balanceOf("alice"), 100, "L2 balance should be unchanged before execution");
  return { name: "ticket created but not executed", request, aliceBalance: l2Billing.balanceOf("alice") };
}

function runCaseExecutedWithInsufficientBalance() {
  const inbox = new MockInbox();
  const l2Billing = new MockL2Billing();
  l2Billing.credit("alice", 10);

  const request = removeOnL2({ inbox, sender: "alice", to: "aliceWallet", amount: 50, maxSubmissionCost: 1 });
  const ticket = inbox.tickets[0];
  const ok = l2Billing.removeFromL1({ ...ticket.data, calledByConnectorAlias: true });
  ticket.executed = true;

  assert.strictEqual(ok, false, "insufficient balance should not remove");
  assert.strictEqual(l2Billing.balanceOf("alice"), 10, "balance should not change on insufficient removal");
  return { name: "executed with insufficient balance", request, l2Events: l2Billing.events };
}

function runCaseExecutedSuccessfully() {
  const inbox = new MockInbox();
  const l2Billing = new MockL2Billing();
  l2Billing.credit("alice", 100);

  const request = removeOnL2({ inbox, sender: "alice", to: "aliceWallet", amount: 50, maxSubmissionCost: 1 });
  const ticket = inbox.tickets[0];
  const ok = l2Billing.removeFromL1({ ...ticket.data, calledByConnectorAlias: true });
  ticket.executed = true;

  assert.strictEqual(ok, true, "removal should succeed");
  assert.strictEqual(l2Billing.balanceOf("alice"), 50, "balance should be debited exactly once");
  return { name: "executed successfully", request, aliceBalance: l2Billing.balanceOf("alice"), l2Events: l2Billing.events };
}

const cases = [
  runCaseTicketCreatedButNotExecuted(),
  runCaseExecutedWithInsufficientBalance(),
  runCaseExecutedSuccessfully(),
];

console.log(
  JSON.stringify(
    {
      hypothesis: "BC2",
      result:
        "model confirms L1 request success is separate from L2 execution, but no unauthorized debit or wrong-recipient path appears",
      cases,
    },
    null,
    2,
  ),
);
