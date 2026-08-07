const API_BASE = (window.MCR_CONFIG && window.MCR_CONFIG.apiBaseUrl) || "http://127.0.0.1:8000";

const PERIOD_LABELS = {
  P0_BASELINE: "Baseline",
  P1_EARLY_SIGNAL: "Early signal",
  P2_STRESS: "Stress",
  P3_OUTCOME: "Outcome",
};
const CATEGORY_LABELS = {
  short_drama: "Short drama · coin economy",
  ai_subscription: "AI service · subscription / credits",
  ai_api: "AI service · API usage",
  web_fiction: "Web fiction · creator economy",
  games: "Games · web store",
};

const state = { catalog: [], scenarioKey: "", period: "P0_BASELINE", scale: "dollar", postureData: null, compareData: null };
const $ = (id) => document.getElementById(id);
const scenarioSelect = $("scenario-select");
const stage = $("analysis-stage");

$("footer-api").textContent = `API · ${API_BASE.replace(/^https?:\/\//, "")}`;

function escapeHtml(value) {
  return String(value ?? "").replace(/[&<>'"]/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" })[character]);
}
function money(value, compact = false) {
  return new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: compact ? 1 : 0, notation: compact ? "compact" : "standard" }).format(value || 0);
}
function pct(value, digits = 1) { return `${((value || 0) * 100).toFixed(digits)}%`; }
function score(value) { return Number(value || 0).toFixed(0); }
function decisionLabel(value) { return String(value || "—").replaceAll("_", " "); }
function selectedScenario() { return state.catalog.find((item) => item.scenario_key === state.scenarioKey); }
function currentView(item) { return state.scale === "dollar" ? item.dollar_view || item.dollar_commercial_view : item.normalized_view || item.normalized_commercial_view; }

async function api(path, options = {}) {
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), 9000);
  try {
    const headers = { ...(options.headers || {}) };
    if (options.body && !headers["Content-Type"]) headers["Content-Type"] = "application/json";
    const response = await fetch(`${API_BASE}${path}`, { ...options, headers, signal: controller.signal });
    if (!response.ok) throw new Error(`API request failed (${response.status})`);
    return await response.json();
  } finally { clearTimeout(timeout); }
}

function renderCatalog() {
  scenarioSelect.innerHTML = state.catalog.map((item) => `<option value="${escapeHtml(item.scenario_key)}">${escapeHtml(item.name)}</option>`).join("");
  scenarioSelect.value = state.scenarioKey;
  renderPeriods();
  renderScenarioFacts();
}
function renderPeriods() {
  const scenario = selectedScenario();
  $("period-track").innerHTML = scenario.periods.map((period, index) => `<button type="button" class="period-button ${period === state.period ? "is-active" : ""}" data-period="${escapeHtml(period)}" aria-pressed="${period === state.period}"><span>0${index + 1} · ${escapeHtml(PERIOD_LABELS[period] || period)}</span></button>`).join("");
  document.querySelectorAll(".period-button").forEach((button) => button.addEventListener("click", async () => { state.period = button.dataset.period; renderPeriods(); await runAssessment(); }));
}
function renderScenarioFacts() {
  const scenario = selectedScenario();
  $("scenario-facts").innerHTML = `<div><span>Case</span><strong>${escapeHtml(scenario.scenario_key)}</strong></div><div><span>Category</span><strong>${escapeHtml(CATEGORY_LABELS[scenario.merchant_category] || scenario.merchant_category)}</strong></div><div><span>Merchant</span><strong>${escapeHtml(scenario.merchant_id)}</strong></div><div><span>Periods</span><strong>${scenario.periods.length} observations</strong></div>`;
}

function renderScores(assessment) {
  $("risk-score").textContent = score(assessment.risk_exposure_score);
  $("strength-score").textContent = score(assessment.merchant_strength_score);
  $("value-score").textContent = score(assessment.commercial_value_score);
  $("risk-level").textContent = `${assessment.risk_level} residual risk`;
  requestAnimationFrame(() => {
    $("risk-bar").style.width = `${assessment.risk_exposure_score}%`;
    $("strength-bar").style.width = `${assessment.merchant_strength_score}%`;
    $("value-bar").style.width = `${assessment.commercial_value_score}%`;
  });
}

function renderWaterfall(view) {
  const rows = [
    ["Attempted payment volume", view.attempted_volume, "base"],
    ["Approved payment volume", view.approved_volume, "base"],
    ["Sustainable payment volume", view.sustainable_payment_volume, "result"],
    ["Gross platform revenue", view.gross_platform_revenue, "base"],
    ["Fraud + dispute loss", view.expected_fraud_loss + view.expected_dispute_principal_loss + view.expected_dispute_operating_cost, "cost"],
    ["Uncovered exposure", view.expected_uncovered_exposure, "cost"],
    ["Review + opportunity cost", view.monitoring_and_review_cost + view.false_positive_opportunity_cost, "cost"],
    ["Control-adjusted contribution", view.control_adjusted_platform_contribution, "result"],
  ];
  const maximum = Math.max(...rows.map((row) => Math.abs(row[1])), 1);
  $("waterfall").innerHTML = rows.map(([label, value, type]) => `<div class="waterfall-row ${type}"><span>${escapeHtml(label)}</span><div class="waterfall-track"><div class="waterfall-fill" style="width:${Math.max(0.5, Math.abs(value) / maximum * 100)}%"></div></div><strong>${state.scale === "dollar" ? money(value, maximum >= 1000000) : money(value)}</strong></div>`).join("");
  $("scale-label").textContent = state.scale === "dollar" ? `${money(view.attempted_volume, true)} monthly attempted volume` : "Normalized per $100 attempted";
}

function renderPostures(postureData) {
  $("posture-grid").innerHTML = postureData.postures.map((posture) => {
    const recommended = posture.posture === postureData.recommended_posture;
    const view = currentView(posture);
    return `<article class="posture-card ${recommended ? "recommended" : ""}"><div class="posture-badge"><span>${escapeHtml(posture.posture.replaceAll("_", " "))}</span>${recommended ? "<em>Recommended</em>" : `<span>${posture.within_risk_appetite ? "Within appetite" : "Outside appetite"}</span>`}</div><h4>${escapeHtml(posture.label)}</h4><p>${escapeHtml(posture.description)}</p><div class="posture-stat"><span>Residual risk</span><strong>${score(posture.residual_risk_score)} / 100</strong></div><div class="posture-stat"><span>Approval rate</span><strong>${pct(posture.effective_approval_rate)}</strong></div><div class="posture-stat"><span>Reserve / hold</span><strong>${pct(posture.reserve_rate)} · ${posture.holding_days}d</strong></div><div class="posture-stat"><span>Adjusted contribution</span><strong>${state.scale === "dollar" ? money(view.control_adjusted_platform_contribution, true) : money(view.control_adjusted_platform_contribution)}</strong></div></article>`;
  }).join("");
}

function renderExplanation(assessment, comparison) {
  const explanations = comparison?.delta_explanation || ["Baseline period establishes the starting decision and control package."];
  $("delta-explanation").innerHTML = explanations.map((item) => `<p class="delta-callout">${escapeHtml(item)}</p>`).join("");
  const drivers = assessment.primary_risk_drivers.length ? assessment.primary_risk_drivers.map((driver) => `${driver.label}${driver.value !== null && driver.value !== undefined ? ` · ${typeof driver.value === "number" ? Number(driver.value).toFixed(3) : driver.value}` : ""}`) : ["No material adverse drivers surfaced in this period."];
  $("driver-list").innerHTML = drivers.map((item) => `<li>${escapeHtml(item)}</li>`).join("");
  const view = currentView(assessment);
  $("reserve-headline").textContent = assessment.reserve.rate ? "Temporary protection while evidence accumulates" : "Standard settlement treatment";
  $("reserve-facts").innerHTML = `<div><span>Reserve rate</span><strong>${pct(assessment.reserve.rate)}</strong></div><div><span>Funds reserved</span><strong>${state.scale === "dollar" ? money(view.reserved_funds, true) : money(view.reserved_funds)}</strong></div><div><span>Holding period</span><strong>${assessment.reserve.holding_days} days</strong></div>`;
  $("control-list").innerHTML = assessment.recommended_controls.map((item) => `<li>${escapeHtml(item.replaceAll("_", " "))}</li>`).join("");
}

function renderResults() {
  const assessment = state.postureData.baseline_assessment;
  const scenario = selectedScenario();
  $("scenario-rubric").textContent = `${scenario.scenario_key} · ${PERIOD_LABELS[state.period]} · ${CATEGORY_LABELS[scenario.merchant_category] || scenario.merchant_category}`;
  $("scenario-name").textContent = scenario.name;
  $("decision-value").textContent = decisionLabel(assessment.decision);
  renderScores(assessment);
  renderWaterfall(currentView(assessment));
  renderPostures(state.postureData);
  renderExplanation(assessment, state.compareData);
  $("stage-placeholder").hidden = true;
  $("error-state").hidden = true;
  $("results").hidden = false;
  stage.setAttribute("aria-busy", "false");
}

async function runAssessment() {
  stage.setAttribute("aria-busy", "true");
  $("status").textContent = `Assessing ${state.scenarioKey} · ${PERIOD_LABELS[state.period]}…`;
  try {
    const posturePromise = api("/api/v1/compare-postures", { method: "POST", body: JSON.stringify({ scenario_key: state.scenarioKey, period: state.period }) });
    const comparePromise = state.period === "P0_BASELINE" ? Promise.resolve(null) : api("/api/v1/compare", { method: "POST", body: JSON.stringify({ baseline: { scenario_key: state.scenarioKey, period: "P0_BASELINE" }, candidate: { scenario_key: state.scenarioKey, period: state.period } }) });
    [state.postureData, state.compareData] = await Promise.all([posturePromise, comparePromise]);
    renderResults();
    $("status").textContent = `Model complete · ${decisionLabel(state.postureData.baseline_assessment.decision)}`;
  } catch (error) {
    $("results").hidden = true;
    $("stage-placeholder").hidden = true;
    $("error-state").hidden = false;
    stage.setAttribute("aria-busy", "false");
    $("status").textContent = error.name === "AbortError" ? "API request timed out." : "Strategy API unavailable.";
  }
}

function setScale(scale) {
  state.scale = scale;
  for (const [id, value] of [["view-dollar", "dollar"], ["view-normalized", "normalized"]]) {
    const active = value === scale;
    $(id).classList.toggle("is-active", active);
    $(id).setAttribute("aria-pressed", String(active));
  }
  if (state.postureData) renderResults();
}

async function initialize() {
  try {
    const data = await api("/api/v1/archetypes");
    state.catalog = data.items;
    state.scenarioKey = data.items[0].scenario_key;
    state.period = data.items[0].periods[0];
    renderCatalog();
    await runAssessment();
  } catch {
    $("stage-placeholder").hidden = true;
    $("error-state").hidden = false;
    stage.setAttribute("aria-busy", "false");
    $("status").textContent = "Strategy API unavailable.";
  }
}

scenarioSelect.addEventListener("change", async () => { state.scenarioKey = scenarioSelect.value; state.period = selectedScenario().periods[0]; renderPeriods(); renderScenarioFacts(); await runAssessment(); });
$("run-model").addEventListener("click", runAssessment);
$("view-dollar").addEventListener("click", () => setScale("dollar"));
$("view-normalized").addEventListener("click", () => setScale("normalized"));
$("retry").addEventListener("click", initialize);

await initialize();
