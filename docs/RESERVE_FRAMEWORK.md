# Reserve framework

**Version:** `reserve-strategy-0.2.0` (draft)  
**Positioning:** Illustrative reserve ranges and holding periods for strategy education.  
**Non-claim:** Not mathematically optimal; not calibrated to real losses.

---

## 1. Why reserves for digital goods

Digital goods create delayed and contingent exposures: disputes after consumption, prepaid balances, subscription renewals, creator payables, and interruption from content/platform events. Rolling reserves and settlement delay are tools to keep **exposure-based** protection aligned with those lags—not merely with last month’s revenue.

## 2. Inputs to illustrative reserve

- Dispute and refund rates  
- Prepaid / outstanding obligation ratios  
- Growth vs merchant age  
- Content-risk indicator  
- Cross-border share  
- Transferability of virtual assets  
- Existing reserve and settlement delay  
- Data confidence  

## 3. Illustrative bands (demonstration)

| Risk posture | Illustrative reserve rate range | Holding period (days) |
|--------------|----------------------------------|------------------------|
| Low | 0–5% | 7–14 |
| Moderate controls | 5–12% | 14–30 |
| Elevated / review | 10–20% | 30–60 |
| Severe (if still processing) | 15–30% | 60–90 |

Exact selection will be rule-based in policy YAML (Phase 3). Amounts, when shown, are `rate × monthly_payment_volume` for intuition only.

## 4. Interaction examples

- High prepaid exposure with low current disputes → still non-zero reserve consideration.  
- Content severe + platform dependency high → prefer longer hold even if dispute rate is moderate.  
- Mature subscription, low growth, high confidence → lower band; standard monitoring may suffice.

## 5. Reduce-control and escalation conditions

**Reduce when (examples):** sustained improvement in disputes/complaints; content-risk down; tenure/confidence up; obligations funded; no integrity events.  
**Escalate when:** dispute spike; content/removal events; obligation ratio jump; viral growth without control headroom; data confidence drop.

## 6. Limitations

Friction costs of reserves are real but not monetized in this lab. Production calibration requires internal loss, dispute timing, settlement, and merchant-performance data plus legal/model-risk review.
