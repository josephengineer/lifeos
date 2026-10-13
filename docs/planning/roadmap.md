# Phased roadmap

No delivery dates are committed. Each phase advances only when its gate passes
and the founder approves the next scope. Catalog phase assignments define scope
within the broad modules; later enhancements are not silently pulled into MVP.

| Phase | Implementation plan | Acceptance and tests | Release gate |
| --- | --- | --- | --- |
| 0 Foundation | Documents, full feature traceability, repo standards, templates, documentation CI | Validator passes; proposals/limitations accurate; founder reviews decisions | Approved foundation PR, remote CI and repository governance established |
| 1 Universal foundation | Execute 20-item ordered backlog: app/config, English resources, themes/navigation, monolith BFF/session gates, identity, personal workspace, profile | Unit/component, auth/revocation/RLS integration, browser flows and actual Android/iOS smoke/build evidence | Founder accepts ADR-0005/0006 and verified identity/isolation; no major vault work before approval |
| 2 Document vault | Private intake/quarantine, metadata CRUD, preview, tags/search; approved OCR and reviewable extraction | Upload abuse, storage denial, pipeline retries, multilingual fixtures, manual outage path | Private access and safe processing demonstrated; provider/privacy decisions accepted |
| 3 Tasks/reminders | Task CRUD/subtasks, due dates/recurrence, calendar/list, linked records, server delivery | DST/recurrence units, outbox/retry integration, closed-app delivery and device flows | Delivery targets, retry/reconciliation and notification controls verified |
| 4 Commercial MVP | Contracts, subscriptions, purchases/warranties, simple dashboard, export/deletion, onboarding, approved billing, operations | Record calculations, deletion/export sweeps, restore exercise, payment sandbox, E2E and accessibility | Founder beta approval; no critical vulnerabilities; privacy/store/billing/recovery readiness reviewed |
| 5 AI assistant | Scoped chat/Q&A, references, summaries, suggestions, conversation deletion | Grounding/abstention, injection/isolation, latency/cost and outage evaluations | Approved providers and evaluation thresholds; controlled rollout evidence |
| 6 Collaboration/integrations | Family/business membership, permissions, sharing, selected provider connections | Role matrices, revoked membership/tokens, webhook/replay and conflict tests | Per-integration feasibility/consent and tenant isolation verified |
| 7 Automation | Versioned proposals, approvals, safe execution/retries, audit and cancellation | Forged approval, payload edits, unknown outcomes, duplicate execution and recovery | Explicit action-level approval policy and verified execution evidence; no blanket autonomy |

Phase 4 research includes prices/tier limits, store subscription policy and payment
provider feasibility. Commercial activation is blocked until founder approval.
Advanced business/enterprise integrations may need separate later gates.

## Priorities

P0 Critical is an urgent security/reliability or release blocker; P1 High is core
phase scope; P2 Medium is a useful enhancement; P3 Low is exploratory/future.
Priority does not imply delivery date. All capabilities begin Planned.
