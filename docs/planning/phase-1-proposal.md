# Phase 1 implementation proposal

Status: Proposed, not authorized. Prepared after the approved Phase 0 merge on
2026-10-14. This is a sequencing and acceptance proposal, not implementation.
The existing [20-item backlog](phase-1-backlog.md) remains authoritative for
item-level scope, feature IDs, dependencies, tests and common Definition of Done.
No issue is recreated, closed or started by this proposal; all 187 capabilities
remain Planned. No dates, package versions, hosting prices or capacity claims
are invented before research.

## Outcome and scope

Deliver a universal Expo/React Native/Router foundation for Web, Android and iOS:
strict TypeScript, modular domain boundaries, typed configuration, centralized
English copy, accessible themes/navigation, verified identity flows, a personal
workspace with explicit ownership, and minimal profile/preferences. Use Supabase
Auth as the research baseline, not a pre-approved custom session gateway.

Exclude vault intake/OCR/AI, document derivatives, tasks/reminders, billing,
family/business collaboration, integrations, device-management UI and account
deletion workflow. Later-phase concepts may shape schema constraints but do not
justify implementing their features now. No production provisioning, real customer
data, live mail, paid builds, app-store publication or deployment is authorized.

## Recommended approval sequence

Approve only P1-01 research (#2) first: official compatibility evidence, platform
constraints and a reproducible disposable scaffold with synthetic data. Confirm
ADR-0001 assumptions and development-toolchain decisions before running it.
This is a separate requested authorization, not work performed in this task.
Research may recommend versions; it must not silently accept other ADRs or provision
paid/hosted services. Record unavailable native evidence as a limitation.

After reviewing that evidence, approve the bounded scaffold/quality/shell tranche.
Before local identity migrations, finalize ADR-0002 and the personal-ownership
part of ADR-0006. After migrations/config exist, authorize P1-18's synthetic SDK
assessment separately. Its evidence and founder decision on ADR-0005 block
production-shaped authentication/session implementation. This respects the
existing dependency on P1-04/P1-08 rather than treating SDK research as a completed
precondition today. A documentation-only threat/schema specification can precede
P1-08; principle approval alone is insufficient to code the schema.

## Twenty issues and deliverables

Each row is a separate small PR, subdivided only if needed with stable traceability.
The wave labels are review checkpoints; they do not replace dependencies.

| Wave / item | Existing issue | Deliverable and acceptance evidence | Depends on / approval gate |
| --- | --- | --- | --- |
| A / P1-01 | [#2](https://github.com/josephengineer/lifeos/issues/2) | Pin a supported universal toolchain from official sources; record commands, alternatives, Windows/macOS constraints and disposable export/smoke evidence | Research authorization; ADR-0001, D03/D10 as relevant |
| B / P1-02 | [#3](https://github.com/josephengineer/lifeos/issues/3) | Minimal single Expo app, Router, strict TS, workspaces/lockfile; clean install, typecheck and real web export; one English resource-backed placeholder | P1-01 and explicit tranche approval |
| B / P1-03 | [#4](https://github.com/josephengineer/lifeos/issues/4) | Real lint/type/unit/component/audit/export CI with pinned runtime; demonstrate controlled defects fail | P1-02; new required-check settings need separate permission |
| B / P1-04 | [#5](https://github.com/josephengineer/lifeos/issues/5) | Typed Zod public/server configuration, safe environment defaults and redacted errors; invalid config and client-secret boundary tests | P1-02, P1-03 |
| B / P1-05 | [#6](https://github.com/josephengineer/lifeos/issues/6) | Typed English UI/error resources, interpolation/plural/date/time-zone formatting and mail/notification conventions | P1-02; uploaded language remains independent |
| B / P1-06 | [#7](https://github.com/josephengineer/lifeos/issues/7) | Light/dark tokens, Button/TextField/Text with persistent preference; keyboard, labels, text scaling and state tests | P1-05; founder design direction |
| B / P1-07 | [#8](https://github.com/josephengineer/lifeos/issues/8) | Phone/wide shell and loading/empty/error/not-found views; back/deep-link and keyboard evidence, no private pre-session content | P1-05, P1-06; route guards never replace server authorization |
| C / P1-08 | [#9](https://github.com/josephengineer/lifeos/issues/9) | Local profile/workspace/owner-membership migrations with tenant constraints and default-deny RLS; reset/upgrade and two-user denial matrix | P1-04; approved ADR-0002 and finalized ADR-0006 schema/threat/tests |
| C / P1-09 | [#10](https://github.com/josephengineer/lifeos/issues/10) | Transactional idempotent provisioning; retry, concurrent signup, rollback and spoofed-owner tests | P1-08 |
| C / P1-18 | [#20](https://github.com/josephengineer/lifeos/issues/20) | Synthetic official SDK feasibility report: protected native storage, web candidate, callbacks, revocation, provider authorization and recovery; compare simpler alternatives before BFF | P1-01, P1-04, P1-08; separate research approval |
| D / P1-19 | [#21](https://github.com/josephengineer/lifeos/issues/21) | Server account/provider-session gates shared by RLS/APIs; mismatch, revoked JWT, private-table, tenant and outage tests | P1-09, P1-18; final ADR-0005 decision and ADR-0006 gates |
| D / P1-20 | [#22](https://github.com/josephengineer/lifeos/issues/22) | SDK refresh, current/global sign-out and agreed expiry; race/replay/expiry/retry/deletion-pending denial tests | P1-19; accepted timeout semantics |
| D / P1-10 | [#11](https://github.com/josephengineer/lifeos/issues/11) | Platform storage/session adapters, private-cache cleanup and honest offline logout; background/resume and already-issued-token replay evidence | P1-04, P1-07, P1-20; ADR-0005/D15 |
| E / P1-11 | [#12](https://github.com/josephengineer/lifeos/issues/12) | English registration/verification/resend through SDK and development mail capture; callback replay/expiry/rate-limit/tenant tests | P1-05, P1-09, P1-10 |
| E / P1-12 | [#13](https://github.com/josephengineer/lifeos/issues/13) | Login/logout/restoration and navigation recovery; non-enumerating errors, server denial after logout and no stale private back-navigation | P1-10, P1-11 |
| E / P1-13 | [#14](https://github.com/josephengineer/lifeos/issues/14) | Generic reset request, allowlisted single-use callbacks and approved invalidation; replay/expiry/bad-callback tests | P1-11, P1-12 |
| E / P1-14 | [#15](https://github.com/josephengineer/lifeos/issues/15) | Own-profile/timezone/theme/English preferences with allowlisted fields; validation, persistence and second-user mutation denial | P1-05, P1-06, P1-08, P1-12 |
| F / P1-15 | [#16](https://github.com/josephengineer/lifeos/issues/16) | Two-identity browser signup/login/reset/profile/logout journeys plus actual RLS matrix; redacted CI artifacts and accessibility evidence | P1-13, P1-14 |
| F / P1-16 | [#17](https://github.com/josephengineer/lifeos/issues/17) | Actual Android and iOS builds plus device/simulator callback/storage/logout/theme/accessibility smoke; separate platform evidence | P1-15, D10; explicit signing/cost authorization |
| F / P1-17 | [#18](https://github.com/josephengineer/lifeos/issues/18) | Acceptance/security/CI/native review and small Phase 2 proposal; report remaining blockers without implementing vault work | P1-15, P1-16; founder gate review |

## Architecture and security decision gates

ADR-0005 remains implementation-undecided. Measure whether official SDK storage,
provider-session checks and server account gates satisfy the requirements before
considering a web-only BFF or universal gateway. Record XSS/token exposure, CSRF
where relevant, browser persistence/reload UX, native backup/reinstall behavior,
current versus global logout, expiry versus human inactivity, password reset and
fresh-auth enforcement on direct provider paths. JWT signature validity is not
revocation evidence. No custom issuer or refresh-token vault without a concrete
failed requirement, alternatives and explicit approval.

The feasibility report must include provider-schema coupling and grants, query
cost/latency, outage behavior, hosting/maintenance costs, key ownership/rotation
and recovery responsibilities. Use measured evidence or clearly labeled estimates;
no paid plan or service is selected automatically. Storage access-path tests join
the Phase 2 implementation gate where storage does not yet exist.

ADR-0006 principles remain accepted, implementation details gated. Before P1-08,
specify exactly-one-owner membership, one personal workspace per owner, prohibited
personal transfer, tenant keys, default-deny policies, transactional races and
privileged service boundaries. Threat/test specifications must cover forged owner
IDs and concurrent provisioning. Immutable originals and derivative provenance
stay mandatory for Phase 2; do not create document pipelines during Phase 1.

ADRs 0001-0004 remain Proposed until explicitly accepted as needed. Resolve native
build/signing access and budget before P1-16. Private security reporting/contact,
license/ownership and Project-board permissions remain tracked follow-ups; no
settings, scopes, visibility or subscription changes follow from this proposal.

## Validation, completion and rollback

Each issue needs acceptance evidence, meaningful negative tests, relevant local
and remote CI, diff/security/localization review, updated status/docs, explicit
founder merge approval and verified post-merge checks. Existing Foundation checks
remain required; propose application check requirements only after stable jobs
actually run, then obtain settings authorization. Keep PR permissions read-only,
actions pinned and secrets absent from fork workflows and artifacts.

Phase 1 is complete only when supported browser flows, tenant isolation, refresh/
logout/reset behavior and both native platforms have executed evidence. A missing
iOS/macOS environment is a visible verification blocker, not a passing check.
Outstanding critical vulnerabilities block completion; noncritical deferrals need
explicit risk ownership. No compliance or production-readiness claim follows from
local tests. A later beta needs separate retention, deletion, backup/restore,
provider and operational approval.

Use one issue/branch/PR at a time by default for the solo-founder workflow. Pause
dependent work at failed architecture or test gates; do not compensate by building
later features. Reviewable reverts use normal PRs; do not rewrite published history
or run destructive production migrations. Track build cost and scope growth per
tranche; provide estimates only after P1-01 evidence.

## Requested next decision

Approve P1-01 (#2) research only, with its documented prerequisites and synthetic,
nonproduction boundaries. Review its evidence before authorizing P1-02 onward.
Approval of this proposal document itself is not Phase 1 execution authorization.
