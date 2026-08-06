const API_BASE = (window.MCR_CONFIG && window.MCR_CONFIG.apiBaseUrl) || "http://127.0.0.1:8000";

const FALLBACK_DECISION = {
  merchant_id: "SYN-CONTROLS-001",
  action: "APPROVE_WITH_CONTROLS",
  risk_score: 48.2,
  probability_of_adverse_outcome: 0.092,
  loss_given_default: 0.53,
  exposure_at_default: 82500,
  expected_loss: 4021.35,
  reserve_rate: 0.05,
  reserve_amount: 5500,
  reason_codes: [
    { code: "RAPID_GROWTH", label: "Rapid TPV growth vs thin history", contribution: 8.1 },
    { code: "ELEVATED_REFUNDS", label: "Elevated refund rate", contribution: 6.4 },
    { code: "TRANSFERABLE_ASSETS", label: "Transferable virtual assets", contribution: 5.2 },
  ],
  hard_policy_flags: [],
  model_version: "scorecard-0.1.0",
  policy_version: "policy-0.1.0",
  assumptions: [
    "Static fallback — live API unavailable. Figures are representative, not a live calculation.",
    "Baseline scorecard is illustrative until Phase 2 validation.",
  ],
  requires_human_review: false,
  request_id: "static-fallback",
};

document.getElementById("footer-api").textContent = API_BASE;

const select = document.getElementById("merchant-select");
const statusEl = document.getElementById("status");
const errorEl = document.getElementById("error");
const fallbackEl = document.getElementById("fallback");
const decisionRoot = document.getElementById("decision-root");
const emptyState = document.getElementById("empty-state");

let merchants = [];

function money(n) {
  return new Intl.NumberFormat("en-US", {
    style: "currency",
    currency: "USD",
    maximumFractionDigits: 0,
  }).format(n);
}

function pct(n, digits = 2) {
  return `${(n * 100).toFixed(digits)}%`;
}

function setStatus(msg) {
  statusEl.textContent = msg;
}

function showError(msg) {
  errorEl.hidden = false;
  errorEl.textContent = msg;
}

function clearError() {
  errorEl.hidden = true;
  errorEl.textContent = "";
}

function renderDecision(d) {
  emptyState.hidden = true;
  decisionRoot.hidden = false;
  document.getElementById("footer-model").textContent = d.model_version;
  document.getElementById("footer-policy").textContent = d.policy_version;

  const reasons = (d.reason_codes || [])
    .map(
      (r) => `<li><div><div>${r.label}</div><div class="code">${r.code}</div></div>
        <span class="code">+${Number(r.contribution).toFixed(1)}</span></li>`
    )
    .join("");

  const flags =
    (d.hard_policy_flags || []).length === 0
      ? "None"
      : d.hard_policy_flags.map((f) => `<div>${f}</div>`).join("");

  decisionRoot.innerHTML = `
    <article class="decision-card">
      <p class="decision-action" data-action="${d.action}">${d.action.replaceAll("_", " ")}</p>
      <div class="meta-row">
        <span>${d.merchant_id}</span>
        <span>score ${Number(d.risk_score).toFixed(1)}</span>
        <span>req ${d.request_id}</span>
        <span>review ${d.requires_human_review ? "required" : "not required"}</span>
      </div>

      <p class="section-num">03 · Economics</p>
      <div class="econ-grid">
        <div class="econ-item"><span>PD</span><strong>${pct(d.probability_of_adverse_outcome, 2)}</strong></div>
        <div class="econ-item"><span>LGD</span><strong>${pct(d.loss_given_default, 1)}</strong></div>
        <div class="econ-item"><span>EAD</span><strong>${money(d.exposure_at_default)}</strong></div>
        <div class="econ-item"><span>Expected loss</span><strong>${money(d.expected_loss)}</strong></div>
        <div class="econ-item"><span>Reserve rate</span><strong>${pct(d.reserve_rate, 2)}</strong></div>
        <div class="econ-item"><span>Reserve amount</span><strong>${money(d.reserve_amount)}</strong></div>
      </div>

      <p class="section-num">04 · Drivers</p>
      <ul class="reasons">${reasons || "<li>No material adverse drivers surfaced.</li>"}</ul>

      <p class="section-num">05 · Policy flags</p>
      <div class="flags">${flags}</div>

      <p class="section-num">06 · Assumptions</p>
      <ul class="assumptions">${(d.assumptions || []).map((a) => `<li>${a}</li>`).join("")}</ul>
    </article>
  `;
}

async function loadSamples() {
  try {
    const res = await fetch("./samples.json");
    if (!res.ok) throw new Error("Could not load sample merchants");
    merchants = await res.json();
  } catch {
    merchants = [
      {
        merchant_id: "SYN-CONTROLS-001",
        industry_subtype: "game_publisher",
        geography_tier: "tier_2",
        tenure_months: 14,
        verification_status: "verified",
        avg_monthly_tpv: 80000,
        projected_monthly_tpv: 110000,
        tpv_growth_3m: 0.9,
        tpv_volatility: 0.85,
        chargeback_rate: 0.012,
        refund_rate: 0.11,
        fraud_alert_rate: 0.018,
        unauthorized_claim_rate: 0.008,
        negative_balance_flag: false,
        instant_delivery_share: 0.75,
        subscription_share: 0.25,
        virtual_asset_transferability: true,
        refund_window_days: 30,
        new_user_share: 0.45,
        repeat_purchase_rate: 0.4,
        device_concentration: 0.35,
        cash_buffer_months: 1.8,
        cross_border_share: 0.4,
        decision_timestamp: "2026-08-01T12:00:00Z",
        _intended_action: "APPROVE_WITH_CONTROLS",
      },
    ];
    setStatus("Using embedded sample (file fetch blocked — serve via local HTTP).");
  }

  select.innerHTML = merchants
    .map((m) => {
      const intent = m._intended_action || "";
      return `<option value="${m.merchant_id}">${m.merchant_id}${intent ? " · " + intent : ""}</option>`;
    })
    .join("");
}

function selectedMerchant() {
  const id = select.value;
  const raw = merchants.find((m) => m.merchant_id === id);
  if (!raw) return null;
  const payload = {};
  for (const [k, v] of Object.entries(raw)) {
    if (!k.startsWith("_")) payload[k] = v;
  }
  return payload;
}

async function runDecision() {
  clearError();
  fallbackEl.classList.remove("visible");
  const payload = selectedMerchant();
  if (!payload) {
    showError("No merchant selected.");
    return;
  }
  setStatus("Running decision…");
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 8000);
  try {
    const res = await fetch(`${API_BASE}/v1/merchants/decision`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
      signal: controller.signal,
    });
    clearTimeout(timer);
    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      throw new Error(err.message || `API error ${res.status}`);
    }
    const data = await res.json();
    renderDecision(data);
    setStatus(`Decision complete · ${data.action}`);
  } catch (err) {
    clearTimeout(timer);
    const msg =
      err.name === "AbortError"
        ? "Request timed out."
        : err.message || "API unavailable.";
    showError(msg);
    setStatus("Showing static fallback.");
    fallbackEl.classList.add("visible");
    fallbackEl.textContent =
      "Live API unreachable. Displaying a representative static decision so the case remains understandable offline.";
    renderDecision({ ...FALLBACK_DECISION, merchant_id: payload.merchant_id });
  }
}

async function checkHealth() {
  clearError();
  setStatus("Checking health…");
  try {
    const res = await fetch(`${API_BASE}/health`);
    if (!res.ok) throw new Error(`Health check failed (${res.status})`);
    const data = await res.json();
    setStatus(`API ${data.status} · model ${data.model_version} · policy ${data.policy_version}`);
  } catch (err) {
    showError(err.message || "Health check failed");
    setStatus("API unavailable");
  }
}

document.getElementById("run-decision").addEventListener("click", runDecision);
document.getElementById("check-health").addEventListener("click", checkHealth);

await loadSamples();
