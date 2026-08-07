# Source register — Digital Goods Merchant Risk Strategy Lab

**Version:** 0.2.0  
**As-of date:** 2026-08-07  
**Scope:** US-centered digital payment platform with cross-border considerations  
**Positioning:** Employer-neutral; no company’s internal methodology is reproduced

## Purpose

This register supports factual claims about laws, payment risk mechanisms, identity signals, digital-goods structures, subscription conduct, content/IP exposure and external-platform dependencies. The project’s taxonomy, scoring logic, reserve logic, control selection and synthetic scenarios are original analysis and are not attributed to any payment company.

## Evidence rules

1. Prefer statutes, regulators, card networks, standards bodies and first-party platform policies.
2. Use commercial market reports only for directional context, never as sole support for a decision rule.
3. Record an access date and the exact claim supported.
4. Do not convert a source’s examples into production thresholds.
5. Separate four claim types in research prose:
   - **Evidence** — directly supported by an external source.
   - **Inference** — Charlene’s conclusion from one or more evidence items.
   - **Hypothesis** — a mechanism that requires real platform data to test.
   - **Demonstration assumption** — a synthetic input used to show system behavior.
6. A source describing another platform’s product rules is evidence about that ecosystem, not evidence that a payment processor should copy the rule.

## Priority evidence register

| ID | Evidence area | Source | Supported use | Important limitation | Status |
|----|---------------|--------|---------------|----------------------|--------|
| REG-001 | Online subscriptions | [15 U.S.C. §8403 — negative option marketing](https://uscode.house.gov/view.xhtml?edition=prelim&num=0&req=%28title%3A15+section%3A8403+edition%3Aprelim%29) | Online negative-option offers require clear material terms, informed consent and a simple mechanism to stop recurring charges. | Legal requirements must be reviewed as of publication; not legal advice. | Accepted |
| REG-002 | Subscription enforcement | [DOJ — Adobe ROSCA settlement announcement, 2026](https://www.justice.gov/opa/pr/adobe-agrees-150-million-settlement-and-injunction-resolve-alleged-violations-restore-online) | Demonstrates continuing US enforcement attention to subscription disclosure and cancellation practices. | Allegations and settlement terms are not a universal underwriting standard. | Accepted |
| REG-003 | Cross-border sanctions | [OFAC — Sanctions Compliance Guidance for Instant Payment Systems](https://ofac.treasury.gov/system/files/126/instant_payment_systems_compliance_guidance_brochure.pdf) | Supports a risk-based sanctions program and the relevance of cross-border design, controls, testing and auditing. | Written for sanctions compliance; not a merchant credit model. | Accepted |
| REG-004 | Stored-value geolocation case | [OFAC — instant-payments guidance and Tango Card settlement notice](https://ofac.treasury.gov/recent-actions/20220930_33) | Shows why IP, email and geolocation signals can matter for restricted-jurisdiction screening in stored-value products. | A historical enforcement matter; IP cannot be used as a sole risk determinant. | Accepted |
| ID-001 | Identity and enrollment fraud | [NIST SP 800-63A-4](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959881) | Supports device fingerprinting, transaction analytics, IP/geolocation and velocity as possible fraud-management inputs. | Government digital-identity guidance, not payment-platform calibration. Privacy assessment is required. | Accepted |
| ID-002 | Session and account monitoring | [NIST SP 800-63B-4](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=959882) | Supports ongoing evaluation of usage, timing, device, browser, geolocation and IP characteristics for possible fraud. | Signals carry privacy implications and may not independently prove fraud. | Accepted |
| NET-001 | Acquirer fraud/dispute monitoring | [Visa — Visa Acquirer Monitoring Program](https://corporate.visa.com/en/sites/visa-perspectives/security-trust/introducing-visa-acquirer-monitoring-program.html) | Establishes that fraud and dispute performance create portfolio-level monitoring and remediation concerns for acquirers. | Public overview omits complete operating rules and thresholds. | Accepted |
| NET-002 | Digital-goods dispute evidence | [Visa Developer — Order Insight Digital](https://developer.visa.com/capabilities/visa-cardholder-purchase-inquiry) | Supports the relevance of merchant, order and digital-goods details in resolving purchase inquiries and disputes. | Product documentation; outcome statistics require separate validation before prominent use. | Accepted with caution |
| PLATFORM-001 | In-app virtual goods | [Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Context only for external distribution dependency and product-structure comparison. App-store billing is excluded from the modeled payment flow. | Apple ecosystem policy, not a general payment rule. Policies change. | Context only |
| PLATFORM-002 | Android digital purchases | [Google Play Payments Policy](https://support.google.com/googleplay/android-developer/answer/9858738?hl=en) | Context only for external distribution dependency and product-structure comparison. App-store billing is excluded from the modeled payment flow. | Google Play policy, not a processor methodology. Policies vary by country and program. | Context only |
| PLATFORM-003 | Coin and virtual-item structure | [TikTok US Virtual Items Policy](https://t.tiktok.com/legal/page/us/virtual-items/en) | Provides a first-party example of Coins, Gifts, Diamonds and Points, including restrictions on transfer, cash equivalence and age. | Structural case evidence only; not evidence of TikTok’s fraud or reserve practices. | Accepted |
| IP-001 | AI and copyright | [US Copyright Office — Copyright and Artificial Intelligence](https://www.copyright.gov/ai/) | Supports the claim that AI-generated outputs, digital replicas and training uses create active copyright and policy questions. | Does not imply every AI merchant is high risk; each business model requires review. | Accepted |
| MARKET-001 | Short-drama category scale | [Sensor Tower — State of Short Drama Apps 2026](https://sensortower.com/blog/state-of-short-drama-apps-2026-report) | Directional evidence of category scale, cross-border growth and changing monetization. | Measures estimated app-store activity; direct web payment volume is excluded. | Context only |
| PRODUCT-001 | Short-drama virtual currency | [ReelShort — Terms of Use](https://www.reelshort.com/user-agreement.html) | First-party evidence that a short-drama service may use earned or purchased virtual currency and virtual goods. | One merchant's public terms; not a sector-wide rule or risk benchmark. | Accepted |
| NET-003 | Digital consumption evidence | [Stripe — analysis of product-not-received dispute evidence](https://stripe.com/blog/analyzing-the-evidence-that-helps-businesses-win-product-not-received-disputes) | Supports the relevance of digital activity, usage and provisioning logs in dispute response. | Observational association from Stripe data; does not guarantee outcomes or reproduce an internal risk method. | Accepted with caution |
| NET-004 | Digital-goods evidence practices | [Stripe — dispute evidence best practices](https://docs.stripe.com/disputes/best-practices) | Supports use of access logs, IP/system evidence, checkout terms and refund-policy evidence. | Operational guidance, not a reserve or underwriting framework. | Accepted |
| PRODUCT-002 | AI prepaid service credits | [OpenAI — Service Credit Terms](https://openai.com/policies/service-credit-terms/) | First-party example distinguishing prepaid and promotional credits, advance payment, expiry and transfer restrictions. | One provider's terms; not a sector-wide standard or accounting conclusion. | Accepted |
| PRODUCT-003 | Usage-based billing | [Stripe — usage-based billing lifecycle](https://docs.stripe.com/billing/subscriptions/usage-based/how-it-works) | Supports the structural distinction among usage ingestion, metering, billing and monitoring. | Product documentation; not evidence of merchant loss rates. | Accepted |
| PRODUCT-004 | Subscription and usage structures | [Stripe — subscription integration design](https://docs.stripe.com/billing/subscriptions/design-an-integration) | Supports flat, tiered, usage-based and credit-burndown structures used in the AI chapter. | Product-design examples, not a required control framework. | Accepted |
| SECURITY-001 | Cloud-native API protection | [NIST — Guidelines for API Protection for Cloud-Native Systems](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=961660) | Supports MFA, adaptive authentication and differentiated key/token controls for API systems. | Security guidance; does not determine merchant payment outcomes. | Accepted |

## Sources requiring additional work

| Research need | Preferred source type | Reason |
|---------------|-----------------------|--------|
| Short-drama refund and cancellation outcomes | First-party terms, regulator actions and structured complaint research | Monetization structure is documented; outcome prevalence and causality remain unvalidated. |
| Web-fiction creator and prepaid obligations | First-party platform terms and public filings | Needed to distinguish customer credits from creator payouts. |
| Gaming account takeover and virtual-item transfer | Card-network, platform-security or peer-reviewed sources | Needed to support transferability and recoverability mechanisms. |
| AI credit, refund and overage outcome prevalence | Public filings, enforcement matters or structured empirical research | Product structures are documented; sector-wide outcome rates remain unvalidated. |
| Reserve friction and merchant attrition | Academic or high-quality empirical research | Required before monetizing the commercial cost of controls. |
| Chargeback timing distributions | Network or peer-reviewed evidence | Required before assigning evidence-based holding periods; until then periods remain demonstration assumptions. |

## Excluded methodology sources

Public materials from named payment companies may be reviewed for general industry context, but this project does not claim to implement or reproduce their internal methods. They should not be cited as the origin of the project’s scorecard, reserve formula, thresholds or control policy.

## Review cadence

- Recheck legal, card-network and platform-policy sources before each public release.
- Record superseded URLs and changed claims in the project changelog.
- Downgrade a claim to **Hypothesis** when a source cannot be verified.
