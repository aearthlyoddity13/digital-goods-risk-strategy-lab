# Cursor master prompt — publish P1 on the portfolio website

Copy the prompt below into Cursor from the portfolio website repository.

---

Implement the **Digital Goods Merchant Risk Strategy Lab** as a flagship case-study route in my existing portfolio website.

## Source of truth

Read these P1 documents before editing:

- `docs/PORTFOLIO_PUBLICATION_PACKAGE.md` — authoritative public architecture, exact copy, visibility policy, interaction specification and acceptance criteria.
- `docs/PORTFOLIO_CASE_STUDY.md` — supporting case-study evidence.
- `docs/SHORT_DRAMA_RISK_DEEP_DIVE.md` — short-drama analysis.
- `docs/AI_SERVICES_RISK_DEEP_DIVE.md` — AI-services analysis.
- `docs/LIMITATIONS_AND_ETHICS.md` and `docs/MODEL_CARD.md` — claim and governance boundaries.
- `docs/API_SPECIFICATION.md` — lab integration contract.

If these files are outside the website repository, ask me for the local P1 path and read them there. Do not invent findings, metrics, credentials, links or production URLs.

## Objective

Create one polished route at `/work/digital-goods-risk-strategy-lab`. It must let a recruiter understand the project in 60 seconds, reward a five-minute case-study read and provide optional technical depth. Short drama, AI services, scenario evidence and the interactive lab are layers of this one project—not separate competing project cards.

## Required implementation

1. Apply the exact section order and approved copy from `PORTFOLIO_PUBLICATION_PACKAGE.md`.
2. Add the project to the homepage and Work index as a flagship item with the strongest available hierarchy.
3. Embed the existing strategy lab as a real interactive component. Configure the API through an environment variable; do not hard-code localhost or a deployment URL.
4. Add a designed timeout/error fallback with a static result summary and a standalone-lab link. Never leave an indefinite spinner or blank iframe.
5. Add a sticky right-side section navigator for the long page. Labels must remain fully visible and the component must never cover body text. The active section should update from actual section intersections.
6. Keep methodology, full scenario detail and technical documentation behind progressive disclosure, while synthetic-data and predictive-accuracy limitations remain visible.
7. Add correct metadata, canonical URL, Open Graph content, breadcrumb schema and project/article structured data using the production domain already configured in the website.
8. Preserve the existing portfolio navigation, responsive system, typography tokens and accessibility conventions unless a documented conflict requires a deliberate change.

## Visual direction

Use the existing **Obsidian Chrome** system: onyx canvas, blue-slate elevated surfaces, alabaster text and a restrained warm-metal accent. The page should feel like an editorial financial-research instrument, not a generic SaaS landing page or card dashboard.

- Use a 12-column editorial grid and asymmetrical spans.
- Keep long-form text at `60–72ch`; let scenario evidence and the lab expand wider.
- Use serif display type for theses and findings, sans for UI/body and mono for model metadata.
- Prefer ruled sections, typographic hierarchy and spatial contrast over repeated rounded cards.
- Limit color to semantic use. Avoid gradients, glow effects, glassmorphism and decorative chart junk unless they already belong to the site’s approved design system.

## Motion direction

Add a coherent motion layer across the whole route using the website’s existing animation stack; use React Bits or GSAP only when compatible with the project and bundle strategy.

- Sequentially reveal the five decision stages on entry.
- Animate model bars and scenario deltas on first view and on user-triggered changes.
- Animate the section navigator’s progress and active state.
- Use restrained clip/mask reveals for section headings and smooth transitions for tabs or accordions.
- Do not add scroll-jacking, perpetual parallax, cursor gimmicks or motion that delays reading.
- Respect `prefers-reduced-motion` and preserve all content without JavaScript animation.

## Public-content rules

- Never display `draft`, `pending`, internal versions, TODOs, backlog content, audit notes, test fixtures or developer instructions.
- Do not publish raw calibration tables, the research-to-model gap audit, sprint documents or internal runbooks.
- Do not claim predictive accuracy, production readiness or use of real merchant data.
- Label synthetic and illustrative results at first meaningful appearance and inside the lab.
- Do not use employer logos or imply that PayPal, Stripe or another company sponsored or supplied methods/data.
- Use a quiet final CTA: lab, source code and next project. Do not use “hire me” language.

## Engineering standards

- First inspect the current architecture, route conventions, content model, design tokens and motion utilities. Extend existing systems instead of creating parallel one-off patterns.
- Build reusable typed components for the section navigator, evidence strip, decision stages, scenario comparison, capability columns, disclosure and lab fallback.
- Keep public copy in the project’s established content/data layer rather than scattering it across components.
- Preserve semantic heading order, keyboard operation, visible focus states, WCAG AA contrast and screen-reader labels.
- Lazy-load the interactive lab if appropriate, prevent layout shift and set a bounded loading timeout.
- Add tests for route rendering, content visibility, absence of internal labels, navigation targets, error fallback and reduced-motion behavior.
- Run typecheck, lint, tests and production build. Fix regressions within scope.

## Required workflow and deliverables

Before coding, return a concise implementation map listing the files you will change and how the existing lab will be integrated. Then implement without waiting unless you encounter a real product decision or missing required URL.

After implementation, provide:

1. changed files and architecture summary;
2. public sections/routes added;
3. lab/API configuration instructions;
4. motion and reduced-motion behavior;
5. automated checks run and results;
6. remaining manual QA using Chrome, Edge and Safari at `1440`, `1280`, `1024`, `768` and `390px`;
7. any missing real links or assets that block publication.

Do not publish or deploy automatically. Stop after a verified local production build so I can review it.

---
