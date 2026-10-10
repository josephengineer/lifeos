# Ordered Phase 1 backlog

Status: Planned. Execute only after founder approval of Phase 1 scope and ADRs.
Each item is a separate small issue/PR; split again if implementation grows.
Order is dependency-aware, not a commitment to parallel implementation or dates.
All items are P1 High unless stated otherwise. Feature IDs refer to the catalog.

Common Definition of Done for every item: acceptance satisfied, relevant tests
executed, CI passes, security and English/localization reviewed, docs/status
updated, diff reviewed, founder-approved PR squash-merged and post-merge checks
verified. Use synthetic data only. Each issue below inherits this definition.

## P1-01: Validate and pin the universal toolchain

Type: Research. Features: foundation for all Phase 1 features.
Context: package compatibility and build constraints are unverified.
Desired behavior/scope: select Expo/React Native/Router/TypeScript, supported
Node/npm and compatible test tools using current official docs; record versions
and Windows/macOS/EAS constraints in an ADR update. No paid provisioning.
Acceptance: exact compatibility evidence and reproducible scaffold command are
recorded; alternatives and native validation requirements are explicit.
Dependencies: approved ADR-0001 and D03/D10 decisions as relevant.
Tests: disposable synthetic scaffold web export and supported platform smoke;
record unavailable native runs without asserting success.
Security/privacy: review dependency provenance and server/client secret boundaries.

## P1-02: Create the minimal Expo workspace and lockfile

Type: Feature. Features: universal application foundation.
Context: no runnable app exists. Desired behavior/scope: scaffold one app with
Router, strict TypeScript, npm workspaces and a single lockfile; avoid feature screens.
Acceptance: clean install and local web start work; strict typecheck passes;
thin routes render one English resource-backed placeholder on supported targets.
Dependencies: P1-01 and Phase 1 approval.
Tests: clean npm ci, typecheck and actual web export; platform smoke where available.
Security/privacy: only public client configuration; no production connections.

## P1-03: Introduce real application CI checks

Type: Feature. Features: engineering quality baseline.
Context: Phase 0 only checks documents. Desired behavior/scope: add formatter,
lint, typecheck, a meaningful unit/component test, dependency audit and web export;
pin runtime and install with lockfile integrity; add npm Dependabot.
Acceptance: actual jobs run on PRs and fail on a controlled type/lint/test defect;
required status names are documented; no no-op/skipped success claims.
Dependencies: P1-02. Tests: local scripts plus remote CI evidence.
Security/privacy: read-only PR permissions, no secrets, action pins, critical audit gate.

## P1-04: Establish typed configuration and trust boundaries

Type: Feature. Features: ID-001 foundation.
Context: incorrect environment configuration can expose secrets or production.
Desired behavior/scope: Zod-validated public configuration, separate server schema
and explicit local/staging/production identity; redacted errors.
Acceptance: invalid/missing config fails clearly; production is never the default;
client bundles/import graph cannot include server credentials.
Dependencies: P1-02, P1-03. Tests: valid/invalid config and bundle-boundary negative cases.
Security/privacy: no values from real secrets in fixtures or logs.

## P1-05: Centralize English copy and locale formatting

Type: Feature. Features: SET-004.
Context: launch language is English while document languages vary.
Desired behavior/scope: typed English resources, interpolation/plurals, date/number
formatting and error-code mapping; establish notification/email resource conventions.
Acceptance: screens use resource keys; locale remains en; missing keys are caught;
document language metadata is independent of UI language.
Dependencies: P1-02. Tests: plural/missing-key and date-only/time-zone formatting cases.
Security/privacy: no raw provider error or sensitive value interpolated into user errors.

## P1-06: Add theme tokens and accessible base components

Type: Feature. Features: SET-003.
Context: shared screens need consistent accessible primitives.
Desired behavior/scope: semantic light/dark tokens and Button/TextField/Text only;
theme choice/system handling and focus/error/disabled behavior.
Acceptance: preference persists; keyboard and screen-reader labels work; dynamic
text and contrast are reviewed on the initial components.
Dependencies: P1-05. Tests: component state tests and recorded browser/native inspection.
Security/privacy: no private values in component demos or screenshots.

## P1-07: Build responsive navigation and standard state views

Type: Feature. Features: universal shell supporting HOME-001 later.
Context: route behavior needs parity across form factors.
Desired behavior/scope: shared route shell, phone/wide layouts, loading/empty/error
views and not-found handling; no document/task implementation.
Acceptance: navigation and back/deep links work; unauthorized routes show safe
UX; route guards are documented as separate from server authorization.
Dependencies: P1-05, P1-06. Tests: route/back/deep-link and narrow/wide keyboard smoke.
Security/privacy: sensitive content is absent before session resolution.

## P1-08: Add local profile and personal workspace migrations

Type: Feature. Features: ID-004; groundwork for ID-011 without workspace switching.
Context: identity data needs a tenant boundary before CRUD.
Desired behavior/scope: profiles, personal workspaces, owner memberships and
minimal preferences with constraints, RLS and synthetic seeds.
Acceptance: one personal workspace per owner, composite tenant constraints,
default-deny grants and no client role/owner mutation; clean reset reproducible.
Dependencies: P1-04 and approved ADR-0002.
Tests: migration reset/upgrade; anonymous, owner and second-user read/write matrix.
Security/privacy: local database only; no security-sensitive hosted permission changes.

## P1-09: Implement idempotent identity provisioning

Type: Feature. Features: ID-001, ID-004.
Context: partial signup must not create missing or duplicate personal workspaces.
Desired behavior/scope: transactional provisioning path and repeatable recovery
for profile/workspace/membership creation; narrow privileged grants.
Acceptance: retry yields one complete personal workspace; failed transactions
leave no partial tenant data; identities cannot choose another owner.
Dependencies: P1-08. Tests: retry, rollback, concurrent signup and spoofed-owner cases.
Security/privacy: audit only reference IDs and outcome codes.

## P1-10: Implement platform session adapters

Type: Feature. Features: ID-001.
Context: web and native have different storage/session threats.
Desired behavior/scope: reviewed web session approach and native secure-storage
adapter, expiry/refresh and logout cleanup; record decision before integration.
Acceptance: expired/revoked sessions fail safely; background/resume works;
logout clears local private state; credentials never appear in logs.
Dependencies: P1-04, P1-07. Tests: expiry/refresh failure, logout and platform adapter tests.
Security/privacy: review XSS/CSRF implications and storage limitations explicitly.

## P1-11: Add email registration and verification

Type: Feature. Features: ID-001, ID-002.
Context: new users need a verified identity and recoverable signup.
Desired behavior/scope: localized forms, verification callback and resend recovery
using development mail capture; connect idempotent provisioning.
Acceptance: verified signup reaches its own workspace; expired/replayed links
fail safely; generic responses avoid account enumeration.
Dependencies: P1-05, P1-09, P1-10.
Tests: valid/invalid signup, resend limits, deep-link callbacks and cross-user denial.
Security/privacy: rate limits and callback allowlists; no live marketing or customer mail.

## P1-12: Add login, logout and route/session recovery

Type: Feature. Features: ID-001.
Context: returning users need reliable access without stale private screens.
Desired behavior/scope: email login/logout, verification-required UX, session
restoration and interrupted navigation recovery.
Acceptance: errors are localized and non-enumerating; logout prevents subsequent
private reads; back navigation cannot reveal cached private content.
Dependencies: P1-10, P1-11. Tests: successful/failed login, expiry and logout E2E.
Security/privacy: bounded retries, no passwords in telemetry and server authorization.

## P1-13: Add secure password reset

Type: Feature. Features: ID-003.
Context: lost credentials need a safe recovery flow.
Desired behavior/scope: generic reset request, allowlisted callback, single-use
token handling, password update and approved session invalidation behavior.
Acceptance: expired/reused links cannot reset; reset request does not enumerate
accounts; completion follows the documented session policy.
Dependencies: P1-11, P1-12. Tests: replay/expiry, invalid callback and session revocation.
Security/privacy: rate limiting; test-mail capture only; no tokens in URLs/log artifacts.

## P1-14: Add profile and account preference editing

Type: Feature. Features: ID-004, ID-005, SET-001, SET-003, SET-004.
Context: users need their display name, timezone and supported preferences.
Desired behavior/scope: allowlisted profile edits, theme and English settings;
exclude billing, integrations and advanced device management.
Acceptance: only own fields change; invalid zones are rejected; errors retain
input; server changes persist across sessions and platforms.
Dependencies: P1-05, P1-06, P1-08, P1-12.
Tests: validation/component tests and second-user mutation denial integration.
Security/privacy: collect minimal profile fields; no client-controlled roles.

## P1-15: Complete identity isolation and browser journey evidence

Type: Feature. Features: ID-001 through ID-005; Phase 1 settings.
Context: individual checks do not prove the complete auth boundary.
Desired behavior/scope: automate browser registration/verification/login/reset/
profile/logout with two synthetic identities and a clean isolated database.
Acceptance: all supported flows pass and cross-user reads/writes are denied;
CI artifacts are redacted; keyboard/a11y issues are resolved or release-blocking.
Dependencies: P1-13, P1-14. Tests: E2E plus actual database RLS matrix and CI.
Security/privacy: no live accounts, personal documents or session tokens in artifacts.

## P1-16: Verify Android and iOS foundation builds

Type: Feature. Features: Phase 1 platform parity.
Context: web success does not prove native functionality.
Desired behavior/scope: configure development builds after signing/cost approval
and execute actual Android/iOS builds plus device/simulator auth/navigation smoke.
Acceptance: build IDs, versions and smoke evidence are recorded separately for
each platform; unavailable platform evidence blocks claiming that platform verified.
Dependencies: P1-15, D10. Tests: real builds, callbacks, secure session persistence,
logout, themes, text scaling and screen-reader smoke on both platforms.
Security/privacy: signing credentials in approved stores; no app-store publishing.

## P1-17: Review Phase 1 gate and prepare Phase 2 issues

Type: Documentation. Features: phase readiness.
Context: feature generation alone must not advance delivery status.
Desired behavior/scope: review acceptance, actual CI/native evidence, isolation,
remaining risks and updated docs; prepare small vault issues and provider decisions.
Acceptance: founder has a concrete Phase 1 report and Phase 2 proposal; unresolved
release blockers remain visible; no Phase 2 implementation begins automatically.
Dependencies: P1-15, P1-16. Tests: inspect traceability, evidence and final CI results.
Security/privacy: record unresolved session/storage/provider risks without sensitive data.
