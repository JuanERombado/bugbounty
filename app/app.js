const targets = {
  thegraph: {
    name: "The Graph",
    paidSeverities: "High and Critical",
    assets: [
      { rank: 1, score: 41, name: "L1Staking", tags: ["staking", "rewards", "accounting", "access-control", "delegation"] },
      { rank: 2, score: 37, name: "BridgeEscrow", tags: ["bridge", "cross-chain", "escrow", "accounting"] },
      { rank: 3, score: 29, name: "Curation", tags: ["curation", "accounting", "state-transition", "economic"] },
      { rank: 4, score: 27, name: "ArbitrumInbox", tags: ["bridge", "cross-chain", "message-validation"] },
      { rank: 5, score: 25, name: "RewardsManager", tags: ["rewards", "accounting", "state-transition"] },
      { rank: 6, score: 22, name: "DisputeManager", tags: ["disputes", "state-transition", "access-control"] },
    ],
  },
  template: {
    name: "New bounty template",
    paidSeverities: "Fill from bounty page",
    assets: [
      { rank: 1, score: 0, name: "Add scoped asset", tags: ["scope", "impact", "local-test"] },
      { rank: 2, score: 0, name: "Add second asset", tags: ["accounting", "permissions"] },
    ],
  },
};

const reportSections = [
  ["Title", "A clear one-line claim about the bug and impact."],
  ["Summary", "What breaks, who is affected, and why it matters."],
  ["In-scope asset", "Exact asset name, address or identifier, and source from the bounty page."],
  ["Accepted impact", "Exact paid impact wording and why the PoC demonstrates it."],
  ["Affected code", "Files, functions, and relevant state variables."],
  ["Root cause", "The smallest explanation of the broken assumption."],
  ["Local reproduction", "Commands, dependencies, config, and steps triage can rerun."],
  ["PoC code", "Complete local PoC, not a partial script or scanner claim."],
  ["Expected vs actual", "What should happen, what happens instead, and test output."],
  ["Impact", "Funds, permissions, privacy, or participant actions affected."],
  ["Suggested fix", "Concrete mitigation direction without over-prescribing."],
  ["Scope checklist", "Asset, impact, rules, audits, and local-only proof checked."],
];

const readinessGates = [
  "Asset is explicitly in scope.",
  "Impact is explicitly accepted and worth report time.",
  "Known audits and listed exclusions have been checked.",
  "Duplicate risk has been checked across audits, issues, PRs, commits, docs, tests, and public discussions.",
  "PoC is complete, runnable, and local-only.",
  "Steps include dependencies, commands, configs, and expected output.",
  "Report is not a placeholder, scanner dump, or AI-only claim.",
];

const processProgress = [
  { label: "Scope", state: "done" },
  { label: "Rank", state: "done" },
  { label: "Map", state: "done" },
  { label: "Hypothesize", state: "done" },
  { label: "Duplicate", state: "active" },
  { label: "Local PoC", state: "active" },
  { label: "Impact", state: "next" },
  { label: "Report", state: "locked" },
];

const processBranches = [
  {
    name: "Start",
    status: "done",
    result: "The Graph scope, accepted impacts, and guardrails are captured.",
    children: [
      {
        name: "High-value contract lanes",
        status: "done",
        result: "Staking, bridge, curation, rewards, disputes, token locks, and payments were prioritized.",
        children: [
          {
            name: "Rejected or covered lanes",
            status: "done",
            result: "Most earlier hypotheses were rejected, marked low, or found covered by existing tests.",
            children: [
              { name: "L1Staking", status: "closed", result: "H1/H2/H3/H5 rejected by local tests." },
              { name: "Bridge and Curation", status: "closed", result: "Main value-movement hypotheses rejected." },
              { name: "Rewards and Disputes", status: "closed", result: "Existing suites cover the tested edges." },
              { name: "GraphTokenLockWallet", status: "watch", result: "One primitive found, but impact is not submission-ready." },
              { name: "HorizonStaking", status: "watch", result: "One low delayed-withdrawal edge noted." },
            ],
          },
          {
            name: "Current payments lane",
            status: "active",
            result: "We are tracing escrow, collector, and agreement-manager accounting.",
            children: [
              { name: "PaymentsEscrow", status: "done", result: "Core thaw, collect, and balance invariants are covered by tests." },
              { name: "RecurringCollector", status: "done", result: "Collector claim math is heavily tested; no strong new issue yet." },
              { name: "RecurringAgreementManager", status: "closed", result: "RAM1 stopped at duplicate gate due Trust audit TRST-M-2 overlap." },
            ],
          },
        ],
      },
      {
        name: "Next decision",
        status: "next",
        result: "Move to the next payments path unless we find a materially new RAM1 bypass.",
        children: [
          { name: "Primary next branch", status: "next", result: "Review SubgraphService payment flow and agreement lifecycle edges." },
          { name: "RAM1 variant only", status: "watch", result: "Continue only if we can show a post-TRST-M-2 bypass, not the same guard condition." },
        ],
      },
    ],
  },
];

const statusLabels = {
  done: "Done",
  active: "Working",
  candidate: "Candidate",
  next: "Next",
  watch: "Watch",
  closed: "Closed",
};

const pipeline = [
  ["Define report target", "Report sections", "Start from the submission sections you must eventually prove.", "targets/thegraph/reports/submission-first-workflow.md"],
  ["Gate scope and impact", "Eligibility decision", "Reject ideas that cannot map to an in-scope asset and accepted impact.", "targets/thegraph/scope/thegraph.scope.json"],
  ["Gate exclusions", "Rule decision", "Block ideas that require prohibited testing or out-of-scope behavior.", "targets/thegraph/scope/thegraph.scope.json"],
  ["Gate known issues", "Audit decision", "Known audit issues are filtered before PoC work.", "targets/thegraph/audits/audit-sources.md"],
  ["Rank bounty potential", "Ranked assets", "Score assets by value, complexity, and high-critical relevance.", "scripts/rank_assets.py"],
  ["Map code", "Code map", "Index contracts, functions, modifiers, and likely review surfaces.", "scripts/map_contracts.py"],
  ["Explain one contract", "Plain-English model", "Explain the contract before hypothesizing.", "prompts/contract-explainer.md"],
  ["Threat-model one asset", "Attack surface", "Focus on funds, permissions, state transitions, and cross-chain assumptions.", "prompts/threat-modeler.md"],
  ["Write one hypothesis", "Testable claim", "Create one small claim that can be confirmed or rejected.", "prompts/bug-hypothesis-generator.md"],
  ["Gate duplicate risk", "Duplicate decision", "Search public known sources by root cause, code symbols, tests, commits, issues, audits, and docs.", "prompts/duplicate-risk-gate.md"],
  ["Plan one local PoC", "PoC plan", "Turn the claim into setup, action, assertion, and rejection criteria.", "prompts/poc-test-planner.md"],
  ["Build evidence dossier", "Finding dossier", "Collect scope proof, root cause, commands, output, and environment notes.", "prompts/evidence-builder.md"],
  ["Check readiness", "Ready or blocked", "Run the readiness checker before drafting a report.", "scripts/check_submission_readiness.py"],
  ["Draft report", "Report draft", "Draft only after the readiness check passes on a real dossier.", "prompts/immunefi-report-drafter.md"],
];

const severities = {
  Critical: {
    focus: "Direct, significant loss of user funds or protocol-held funds.",
    tactics: [
      "Trace every way value enters, exits, or changes owner.",
      "Model invariants around total balances, escrowed balances, shares, and claims.",
      "Test cross-chain message assumptions with local mocks.",
      "Look for state transitions that can be repeated, skipped, or reordered.",
    ],
    localAnalyzers: [
      "Balance invariant test generator",
      "Cross-chain sender simulation checklist",
      "Privileged function reachability map",
    ],
    learningGoal: "Think like an accountant and a state-machine debugger.",
  },
  High: {
    focus: "Fund-loss paths, participant impersonation, or sensitive private information exposure.",
    tactics: [
      "Map roles, operators, delegates, keepers, arbiters, and gateways.",
      "Test caller confusion across proxies, messengers, and extension contracts.",
      "Review stale state, replay-like paths, signature domain assumptions, and authorization bypasses.",
      "Compare docs, tests, and implementation for mismatched assumptions.",
    ],
    localAnalyzers: [
      "Access-control matrix",
      "Role transition checklist",
      "Existing-test gap finder",
    ],
    learningGoal: "Find where a trusted identity or assumption can be confused.",
  },
  Medium: {
    focus: "Meaningful protocol bugs that may not meet paid high-critical impact.",
    tactics: [
      "Find griefing, accounting drift, loss of rewards below threshold, or broken lifecycle paths.",
      "Use mediums as training ground, then ask what would need to change for high impact.",
      "Check whether the bounty actually pays medium before spending report time.",
    ],
    localAnalyzers: [
      "Lifecycle edge-case checklist",
      "Rounding and precision test ideas",
      "Impact-upgrade worksheet",
    ],
    learningGoal: "Use medium ideas to build taste and proof discipline.",
  },
  Low: {
    focus: "Low-risk correctness, hygiene, or best-practice issues.",
    tactics: [
      "Treat lows as learning notes unless the program pays them.",
      "Do not submit best-practice critiques when out of scope.",
      "Convert observations into future high-value hypotheses when possible.",
    ],
    localAnalyzers: [
      "Best-practice filter",
      "False-positive tracker",
      "Learning-note template",
    ],
    learningGoal: "Build pattern recognition without wasting submission cycles.",
  },
};

const experts = [
  {
    name: "nnez",
    signal: "Elite All Star; public page says one in every 2.4 reports is a valid critical.",
    pattern: "Critical conversion matters more than noisy breadth.",
    habits: ["Critical-first triage", "Aggressive weak-idea rejection", "Report only with decisive local proof"],
  },
  {
    name: "Haxatron",
    signal: "Elite All Star; described by Immunefi as strong on Layer 1s with 39 highs and crits.",
    pattern: "Layer and consensus-adjacent assumptions deserve dedicated review lanes.",
    habits: ["L1/L2 boundary review", "State-machine analysis", "Minimal decisive PoCs"],
  },
  {
    name: "usmannk",
    signal: "Elite All Star; Immunefi describes 7 confirmed criticals and $3.1M earnings.",
    pattern: "A strong workflow should preserve patience for rare, high-impact paths.",
    habits: ["Max-impact framing", "Funds-at-risk accounting", "Known-issue elimination"],
  },
  {
    name: "LonelySloth",
    signal: "Elite All Star; Immunefi says one in 2.8 reports is a valid critical.",
    pattern: "High selectivity is a skill: the system should help say no quickly.",
    habits: ["Impact gate before testing", "Audit gate before coding", "Small hypothesis queue"],
  },
  {
    name: "shadowHunter",
    signal: "Elite All Star; Immunefi describes 61 bugs across 153 unique projects hunted.",
    pattern: "Breadth builds pattern recognition when paired with disciplined scope checks.",
    habits: ["Reusable target setup", "Protocol-family playbooks", "False-positive tracking"],
  },
  {
    name: "walker",
    signal: "Elite All Star; Immunefi calls out $1.1M and 9 criticals.",
    pattern: "Bad tests are a hunting surface: compare intended invariants with existing coverage.",
    habits: ["Test-suite gap mining", "Invariant extraction", "Regression-style PoCs"],
  },
  {
    name: "General elite pattern",
    signal: "All Stars are selected for high impact, discipline, and consistent results.",
    pattern: "The workflow should create fewer, stronger hypotheses and reject weak ones early.",
    habits: ["Scope gate first", "Audit gate second", "Local proof third"],
  },
];

const analyzers = [
  {
    name: "Refresh asset ranking",
    command: "python scripts/rank_assets.py targets/thegraph/scope/thegraph.scope.json",
    note: "Regenerates the investigation queue from target scope JSON.",
  },
  {
    name: "Map local contracts",
    command: "python scripts/map_contracts.py external/thegraph-contracts --scope targets/thegraph/scope/thegraph.scope.json --out targets/thegraph/code-map/contracts-map.md",
    note: "Indexes contracts, functions, modifiers, events, and priority tags.",
  },
  {
    name: "Critical invariant worksheet",
    command: "Open prompts/threat-modeler.md, paste one asset and contract summary, then ask for accounting invariants only.",
    note: "Good first move for staking, rewards, curation, and escrow contracts.",
  },
  {
    name: "Local PoC planner",
    command: "Open prompts/poc-test-planner.md and paste one confirmed hypothesis candidate.",
    note: "Creates setup, action, assertion, and rejection criteria before coding.",
  },
  {
    name: "Duplicate-risk gate",
    command: "Open prompts/duplicate-risk-gate.md and fill targets/thegraph/reports/duplicate-risk-template.md for the lead.",
    note: "Checks audits, repo history, public discussions, tests, and docs before deeper PoC work.",
  },
  {
    name: "Submission readiness check",
    command: "python scripts/check_submission_readiness.py targets/thegraph/reports/finding-dossier.example.json",
    note: "Fails until a real dossier has scope proof, impact proof, a complete local PoC, and report evidence.",
  },
];

let activeTarget = "thegraph";
let activeSeverity = "Critical";

const views = {
  newproject: document.querySelector("#newprojectView"),
  submission: document.querySelector("#submissionView"),
  process: document.querySelector("#processView"),
  pipeline: document.querySelector("#pipelineView"),
  severity: document.querySelector("#severityView"),
  experts: document.querySelector("#expertsView"),
  assets: document.querySelector("#assetsView"),
  local: document.querySelector("#localView"),
};

function setView(name) {
  Object.values(views).forEach((view) => view.classList.remove("active"));
  views[name].classList.add("active");
  document.querySelectorAll(".nav-button").forEach((button) => {
    button.classList.toggle("active", button.dataset.view === name);
  });
  document.querySelector("#pageTitle").textContent = {
    newproject: "New Project",
    pipeline: "Pipeline",
    process: "Process Map",
    submission: "Submission Goal",
    severity: "Severity Playbooks",
    experts: "All Stars Patterns",
    assets: "Asset Queue",
    local: "Local Analyzers",
  }[name];
}

function escapeHTML(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function renderProjectResult(payload) {
  const result = document.querySelector("#projectInitResult");
  if (!payload.ok) {
    result.innerHTML = `
      <h2>Could Not Initialize</h2>
      <p>${escapeHTML(payload.error || "The initializer returned an unknown error.")}</p>
      <pre class="inline-command">python -m backend.hotspot_hub.cli target init "${escapeHTML(document.querySelector("#programUrl").value)}"</pre>
    `;
    return;
  }

  const warnings = payload.warnings?.length
    ? `<div><strong>Warnings</strong><span>${payload.warnings.map(escapeHTML).join("<br>")}</span></div>`
    : "";
  const files = [...(payload.written_files || []), ...(payload.skipped_files || [])]
    .map((file) => `<li>${escapeHTML(file)}</li>`)
    .join("");
  const next = (payload.next_steps || []).map((step) => `<li>${escapeHTML(step)}</li>`).join("");
  result.innerHTML = `
    <h2>${escapeHTML(payload.target_name)}</h2>
    <p>${escapeHTML(payload.preview?.summary || "Target foundation created.")}</p>
    <div class="detail-list">
      <div><strong>Target folder</strong><span>${escapeHTML(payload.target_dir)}</span></div>
      <div><strong>Status</strong><span>${escapeHTML(payload.preview?.status || "needs_manual_scope_review")}</span></div>
      <div><strong>Resources found</strong><span>${escapeHTML(payload.preview?.resource_count || 0)}</span></div>
      ${warnings}
    </div>
    <h3>Files</h3>
    <ul class="compact-list">${files}</ul>
    <h3>Next</h3>
    <ol class="compact-list">${next}</ol>
  `;
}

function initializeProjectForm() {
  const form = document.querySelector("#projectForm");
  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const result = document.querySelector("#projectInitResult");
    const programUrl = document.querySelector("#programUrl").value.trim();
    const targetName = document.querySelector("#targetName").value.trim();
    result.innerHTML = `
      <h2>Initializing</h2>
      <p>Fetching the public Immunefi page and creating the local workspace foundation.</p>
    `;

    try {
      const response = await fetch("/api/projects/initialize", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ programUrl, targetName }),
      });
      renderProjectResult(await response.json());
    } catch (error) {
      renderProjectResult({
        ok: false,
        error: `Dashboard API is not running. Start it with: python -m backend.hotspot_hub.server --host 127.0.0.1 --port 4173`,
      });
    }
  });
}

function renderSubmissionGoal() {
  document.querySelector("#reportSections").innerHTML = reportSections
    .map(
      ([name, purpose], index) => `
        <article class="report-section">
          <span>${String(index + 1).padStart(2, "0")}</span>
          <div>
            <strong>${name}</strong>
            <p>${purpose}</p>
          </div>
        </article>
      `,
    )
    .join("");
  document.querySelector("#readinessDetail").innerHTML = `
    <h2>Readiness Gates</h2>
    <p>If any gate fails, the idea goes back to research or gets rejected.</p>
    <div class="detail-list">
      ${readinessGates.map((gate) => `<div><strong>Gate</strong><span>${gate}</span></div>`).join("")}
    </div>
  `;
}

function renderProcessMap() {
  document.querySelector("#progressRail").innerHTML = processProgress
    .map(
      (step, index) => `
        <div class="progress-step ${step.state}">
          <span>${String(index + 1).padStart(2, "0")}</span>
          <strong>${step.label}</strong>
        </div>
      `,
    )
    .join("");

  document.querySelector("#branchTree").innerHTML = processBranches.map(renderBranchNode).join("");

  document.querySelector("#processSummary").innerHTML = `
    <h2>Plain-English Summary</h2>
    <ol class="summary-list">
      <li>We start from the report we would need to submit, then work backward.</li>
      <li>Every idea must pass scope, impact, exclusion, known-issue, and duplicate-risk gates.</li>
      <li>We ranked high-value contracts, then tested one small hypothesis at a time.</li>
      <li>Most paths were rejected or downgraded, which is a useful result.</li>
      <li>RAM1 was stopped by the duplicate-risk gate because it overlaps Trust audit TRST-M-2.</li>
      <li>The next move is to review SubgraphService payment flow for a fresher path.</li>
    </ol>
    <div class="next-action">
      <strong>Next step</strong>
      <span>Move to SubgraphService unless RAM1 can be reframed as a materially new post-audit bypass.</span>
    </div>
  `;
}

function renderBranchNode(node) {
  const children = node.children?.length
    ? `<div class="branch-children">${node.children.map(renderBranchNode).join("")}</div>`
    : "";
  return `
    <article class="branch-node ${node.status}">
      <div class="branch-copy">
        <span>${statusLabels[node.status] || node.status}</span>
        <strong>${node.name}</strong>
        <p>${node.result}</p>
      </div>
      ${children}
    </article>
  `;
}

function renderPipeline() {
  const list = document.querySelector("#pipelineList");
  list.innerHTML = pipeline
    .map(
      ([name, output], index) => `
        <li>
          <button ${index === 0 ? 'class="active"' : ""} data-stage="${index}">
            <span class="stage-number">${String(index + 1).padStart(2, "0")}</span>
            <span class="stage-title">${name}</span>
            <span class="stage-status">${output}</span>
          </button>
        </li>
      `,
    )
    .join("");
  list.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-stage]");
    if (!button) return;
    document.querySelectorAll(".pipeline button").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    renderStage(Number(button.dataset.stage));
  });
  renderStage(0);
}

function renderStage(index) {
  const [name, output, detail, tool] = pipeline[index];
  document.querySelector("#stageDetail").innerHTML = `
    <h2>${name}</h2>
    <p>${detail}</p>
    <div class="detail-list">
      <div><strong>Input</strong><span>${activeTarget === "thegraph" ? "The Graph Immunefi pages and local repo" : "New bounty information, scope, resources, and repos"}</span></div>
      <div><strong>Output</strong><span>${output}</span></div>
      <div><strong>Assistant handoff</strong><span>${tool}</span></div>
      <div><strong>Safety check</strong><span>Do this with local files, local tests, or local forks only.</span></div>
    </div>
  `;
}

function renderSeverities() {
  const tabs = document.querySelector("#severityTabs");
  tabs.innerHTML = Object.keys(severities)
    .map((name) => `<button class="${name === activeSeverity ? "active" : ""}" data-severity="${name}">${name}</button>`)
    .join("");
  tabs.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-severity]");
    if (!button) return;
    activeSeverity = button.dataset.severity;
    renderSeverityDetail();
    renderSeverities();
  }, { once: true });
  renderSeverityDetail();
}

function renderSeverityDetail() {
  const severity = severities[activeSeverity];
  document.querySelector("#severityDetail").innerHTML = `
    <h2>${activeSeverity}</h2>
    <p>${severity.focus}</p>
    <div class="severity-grid">
      <div class="severity-column">
        <h3>Tactics</h3>
        <ul>${severity.tactics.map((item) => `<li>${item}</li>`).join("")}</ul>
      </div>
      <div class="severity-column">
        <h3>Local analyzers</h3>
        <ul>${severity.localAnalyzers.map((item) => `<li>${item}</li>`).join("")}</ul>
      </div>
      <div class="severity-column">
        <h3>Learning goal</h3>
        <p>${severity.learningGoal}</p>
      </div>
    </div>
  `;
}

function renderExperts() {
  document.querySelector("#expertGrid").innerHTML = experts
    .map(
      (expert) => `
        <article class="expert-item">
          <div class="expert-meta"><span>${expert.name}</span><span>${expert.signal}</span></div>
          <h3>${expert.pattern}</h3>
          <ul>${expert.habits.map((habit) => `<li>${habit}</li>`).join("")}</ul>
        </article>
      `,
    )
    .join("");
}

function renderAssets() {
  const target = targets[activeTarget];
  document.querySelector("#assetCount").textContent = target.assets.length;
  document.querySelector("#assetTable").innerHTML = target.assets
    .map(
      (asset) => `
        <div class="asset-row">
          <span class="score">#${asset.rank}</span>
          <strong>${asset.name}</strong>
          <div class="tags">${asset.tags.map((tag) => `<span>${tag}</span>`).join("")}</div>
          <span class="score">${asset.score}</span>
        </div>
      `,
    )
    .join("");
}

function renderAnalyzers() {
  const list = document.querySelector("#analyzerList");
  list.innerHTML = analyzers
    .map(
      (item, index) => `
        <button class="analyzer-card ${index === 0 ? "active" : ""}" data-analyzer="${index}">
          <h3>${item.name}</h3>
          <p>${item.note}</p>
        </button>
      `,
    )
    .join("");
  list.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-analyzer]");
    if (!button) return;
    document.querySelectorAll(".analyzer-card").forEach((item) => item.classList.remove("active"));
    button.classList.add("active");
    renderCommand(Number(button.dataset.analyzer));
  });
  renderCommand(0);
}

function renderCommand(index) {
  const analyzer = analyzers[index];
  document.querySelector("#commandOutput").textContent = `${analyzer.name}\n\n${analyzer.command}\n\n${analyzer.note}\n\nSafety: run only against local files, local tests, or local forks.`;
}

document.querySelectorAll(".nav-button").forEach((button) => {
  button.addEventListener("click", () => setView(button.dataset.view));
});

document.querySelector("#targetSelect").addEventListener("change", (event) => {
  activeTarget = event.target.value;
  renderAssets();
  renderStage(0);
});

renderSubmissionGoal();
initializeProjectForm();
renderProcessMap();
renderPipeline();
renderSeverities();
renderExperts();
renderAssets();
renderAnalyzers();
