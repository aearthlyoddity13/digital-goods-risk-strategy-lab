# Data dictionary

**Version:** 0.4.0
**Disclaimer:** Demonstration data: aggregated and synthetic. No confidential merchant, customer or payment-platform data is used.

## Scenario input fields (`decision_input`)

| Field | Type | Range | Description |
|-------|------|-------|-------------|
| `archetype_id` | string | — | Synthetic archetype identifier |
| `scenario_id` | string | — | Period/scenario key |
| `period_label` | enum | `normal`,`growth`,`stress`,`deterioration` | Scenario class |
| `merchant_category` | enum | `short_drama`,`web_fiction`,`games`,`ai_subscription`,`ai_api`,`virtual_goods`,`digital_subscription`,`other_digital` | Category |
| `merchant_age_months` | int | 0–600 | Operating age |
| `operating_regions` | list[str] | ISO-like codes | Regions (aggregated) |
| `revenue_model` | enum | `coins_unlock`,`subscription`,`virtual_currency`,`trial_subscription`,`usage_api`,`mixed` | Monetization |
| `monthly_payment_volume` | float | ≥0 | Aggregated volume |
| `monthly_attempted_payment_volume` | float | ≥0 | Synthetic web-payment volume attempted before approval effects |
| `payment_approval_rate` | float | 0–1 | Approved share of attempted web-payment volume |
| `successful_fulfillment_rate` | float | 0–1 | Approved payments with successful entitlement/access fulfillment |
| `mom_volume_growth` | float | −1–10 | Month-over-month growth |
| `volume_volatility` | float | 0–5 | Volatility index |
| `average_ticket_size` | float | ≥0 | Average ticket |
| `transactions_per_customer` | float | ≥0 | Intensity |
| `transaction_frequency` | float | ≥0 | Txns per customer-month (proxy) |
| `new_customer_share` | float | 0–1 | New customers |
| `cross_border_share` | float | 0–1 | Cross-border share |
| `subscription_share` | float | 0–1 | Subscription mix |
| `prepaid_virtual_value_exposure` | float | ≥0 | Prepaid/virtual obligation proxy (currency) |
| `prepaid_exposure_ratio` | float | 0–2 | Obligation / monthly volume |
| `purchased_coin_value` | float | ≥0 | Customer-funded short-drama coin value purchased in the period |
| `consumed_purchased_coin_value` | float | ≥0 | Purchased coin value consumed through episode unlocks |
| `refunded_purchased_coin_value` | float | ≥0 | Purchased coin value refunded in the period |
| `unused_purchased_coin_value` | float | ≥0 | Non-expiring customer-funded coin obligation remaining |
| `promotional_coin_value` | float | ≥0 | Merchant-funded promotional coins tracked separately from purchased coins |
| `purchased_service_credit_value` | float | ≥0 | Customer-funded AI service credits purchased in the period |
| `consumed_service_credit_value` | float | ≥0 | Purchased service-credit value consumed through documented usage |
| `refunded_service_credit_value` | float | ≥0 | Purchased service-credit value refunded in the period |
| `unused_service_credit_value` | float | ≥0 | Remaining purchased service-credit obligation |
| `promotional_service_credit_value` | float | ≥0 | Merchant-funded AI promotional credits, separated from customer-funded principal |
| `post_consumption_dispute_share` | float | 0–1 | Share of disputed volume occurring after recorded consumption |
| `renewal_dispute_share` | float | 0–1 | Share of disputed volume associated with trial conversion or renewal |
| `renewal_disclosure_score` | float | 0–1 | Synthetic analyst assessment of trial/renewal disclosure clarity |
| `usage_meter_reconciliation_rate` | float | 0–1 | Share of aggregate billed usage reconciling to validated meter records |
| `anomalous_usage_share` | float | 0–1 | Aggregated usage share exhibiting documented anomaly patterns |
| `account_or_key_compromise_indicator` | float | 0–1 | Aggregate evidence strength for account or API-key compromise |
| `postpaid_usage_exposure_ratio` | float | 0–2 | Uncollected usage/service-cost exposure relative to monthly payment volume |
| `refund_rate` | float | 0–1 | Refund rate |
| `dispute_rate` | float | 0–1 | Dispute/chargeback proxy |
| `fraud_loss_proxy` | float | 0–1 | Fraud loss / volume proxy |
| `payment_decline_rate` | float | 0–1 | Decline rate |
| `retry_rate` | float | 0–1 | Retry intensity |
| `new_device_share` | float | 0–1 | Share of activity from devices new to the account/merchant |
| `high_risk_session_share` | float | 0–1 | Aggregated sessions with supporting IP/device/geographic risk indicators |
| `complaint_rate` | float | 0–1 | Complaint rate |
| `content_risk_indicator` | float | 0–1 | Aggregated content/integrity risk |
| `product_customer_concentration` | float | 0–1 | Concentration |
| `platform_dependency` | float | 0–1 | Single-platform dependence |
| `service_reliability` | float | 0–1 | Reliability (higher = better) |
| `support_response_within_sla` | float | 0–1 | Share of sampled cases answered within the stated service level |
| `outstanding_customer_obligation` | float | ≥0 | Contingent customer obligations |
| `current_reserve_rate` | float | 0–1 | Existing reserve |
| `settlement_delay_days` | int | 0–90 | Current delay |
| `data_confidence_level` | enum | `low`,`medium`,`high` | Sufficiency |
| `virtual_asset_transferability` | bool | — | Giftable/transferable value |
| `assessment_timestamp` | datetime | UTC | Observation cutoff |

Legacy v0 credit-engine fields are archived in `docs/archive/v0-credit-engine/data_dictionary.md`.

## Assessment output fields

| Field | Description |
|-------|-------------|
| `decision` | `APPROVE` / `APPROVE_WITH_CONTROLS` / `MANUAL_REVIEW` / `DECLINE` |
| `risk_level` | `low` / `moderate` / `elevated` / `high` / `severe` |
| `illustrative_risk_score` | 0–100 band input (illustrative) |
| `primary_risk_drivers` | List of {code, label, detail} |
| `protective_factors` | List of strings |
| `recommended_controls` | List of control enums |
| `illustrative_reserve` | {min_rate, max_rate, holding_days_min, holding_days_max, rationale} |
| `conditions_to_reduce_controls` | List |
| `escalation_triggers` | List |
| `confidence` | Data-sufficiency assessment |
| `methodology_version` | String |
| `policy_version` | String |
| `synthetic_data_disclaimer` | Fixed disclosure string |
| `limitations` | Explicit limitation bullets |
