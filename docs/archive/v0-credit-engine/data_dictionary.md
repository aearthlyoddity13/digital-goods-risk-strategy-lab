# Data dictionary

**Version:** 0.1.0  
**Leakage rule:** Fields marked `decision_input` may be used at decision time. Fields marked `outcome_only` must never enter the decision engine.

## Merchant request features (`decision_input`)

| Field | Type | Range / enum | Timing | Use |
|-------|------|--------------|--------|-----|
| `merchant_id` | string | non-empty, ≤64 | Decision time | Identifier |
| `industry_subtype` | enum | `game_publisher`, `short_form_entertainment`, `web_fiction`, `ai_application`, `subscription_product`, `virtual_items`, `other_digital` | Decision time | Segment / LGD prior |
| `geography_tier` | enum | `tier_1`, `tier_2`, `tier_3`, `cross_border_heavy` | Decision time | Geo risk component |
| `tenure_months` | int | 0–600 | Decision time | Viability |
| `verification_status` | enum | `unverified`, `partial`, `verified` | Decision time | Hard policy / score |
| `avg_monthly_tpv` | float | ≥0 | Trailing known | Volume / EAD |
| `projected_monthly_tpv` | float | ≥0 | Decision-time projection | EAD |
| `tpv_growth_3m` | float | −1–10 | Trailing | Growth volatility |
| `tpv_volatility` | float | 0–5 | Trailing | Volatility |
| `chargeback_rate` | float | 0–1 | Trailing known | Payment quality |
| `refund_rate` | float | 0–1 | Trailing known | Payment quality |
| `fraud_alert_rate` | float | 0–1 | Trailing known | Payment quality |
| `unauthorized_claim_rate` | float | 0–1 | Trailing known | Payment quality |
| `negative_balance_flag` | bool | — | Known at decision | Hard policy / viability |
| `instant_delivery_share` | float | 0–1 | Known | Product structure |
| `subscription_share` | float | 0–1 | Known | Product structure |
| `virtual_asset_transferability` | bool | — | Known | Product structure |
| `refund_window_days` | int | 0–365 | Known | EAD timing |
| `new_user_share` | float | 0–1 | Trailing | Behavior |
| `repeat_purchase_rate` | float | 0–1 | Trailing | Behavior |
| `device_concentration` | float | 0–1 | Trailing | Behavior (higher = riskier) |
| `cash_buffer_months` | float | 0–36 | Estimate at decision | Resilience |
| `cross_border_share` | float | 0–1 | Trailing | Geo |
| `decision_timestamp` | datetime (UTC) | ISO-8601 | Decision time | Observation cutoff |

## Outcome fields (`outcome_only` — validation Phase 2)

| Field | Type | Use |
|-------|------|-----|
| `adverse_event_90d` | bool | Label |
| `loss_amount_180d` | float | Realized loss |
| `recovery_amount` | float | Recovery |

## Decision response fields

| Field | Type | Description |
|-------|------|-------------|
| `merchant_id` | string | Echo |
| `action` | enum | `APPROVE` / `APPROVE_WITH_CONTROLS` / `MANUAL_REVIEW` / `DECLINE` |
| `risk_score` | float | 0–100 (higher = riskier) |
| `probability_of_adverse_outcome` | float | 0–1 calibrated PD |
| `loss_given_default` | float | 0–1 |
| `exposure_at_default` | float | Currency units |
| `expected_loss` | float | PD × LGD × EAD |
| `reserve_rate` | float | 0–1 recommended holdback |
| `reserve_amount` | float | Currency |
| `reason_codes` | list[{code,label,contribution}] | Top drivers |
| `hard_policy_flags` | list[string] | Rule hits |
| `model_version` | string | e.g. `scorecard-0.1.0` |
| `policy_version` | string | e.g. `policy-0.1.0` |
| `assumptions` | list[string] | Warnings / assumptions |
| `requires_human_review` | bool | Review queue flag |
| `request_id` | string | Traceability |
