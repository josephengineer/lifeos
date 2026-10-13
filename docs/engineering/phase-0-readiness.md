# Phase 0 architecture, security and governance readiness

Date: 2026-10-13. Status: Ready for founder decisions; merge not authorized.
Scope: documentation and Phase 0 tooling in [draft PR #19](https://github.com/josephengineer/lifeos/pull/19).
No Phase 1 implementation, deployment or publishing has begun.

## Findings and resolved documentation issues

The [six-finding table](foundation-review.md) records severity, corrections and
residual risks. R01/R04/R05 are corrected documentation/tooling findings. R02/R03
have explicit ownership and byte-preserving data-model proposals. R06 now has a
complete recommended cross-platform session architecture. Their application
controls still require acceptance, implementation and negative tests.

## Decisions requested

| ADR | Recommendation requiring founder decision |
| --- | --- |
| 0001 | Universal Expo/React Native/Router client, strict TypeScript and modular monolith; server BFF within that monolith |
| 0002 | Workspace isolation, private storage, RLS and narrow privileged paths, with account-scoped exceptions |
| 0003 | Optional grounded AI; separate suggestions, approvals, execution and verified outcomes |
| 0004 | Lightweight foundation checks; later real app CI; private/no open-source grant pending ownership/license confirmation |
| 0005 | Supabase Auth behind common BFF; opaque web/native handles, server token vault and session/RLS revocation gates; proposed timeout defaults |
| 0006 | Single accountable workspace owner; no implicit personal-to-shared exposure; sealed originals and separate versioned derivatives |

All six ADRs remain **Proposed**. ADR-0005 proposes 10-minute provider JWTs, 7-day idle
and 30-day absolute application sessions, and 5-minute sensitive reauthentication
freshness. These are proposed settings, not configured services. See the
[decision register](../planning/decisions.md) for D02/D03/D09/D15-D17 and later gates.

## Governance recommendation and blocker

Read-only GitHub checks found main unprotected and HTTP 403 upgrade requirements
for private branch protection and rulesets. Exact account plan name was unavailable.
The owner is a personal User account: GitHub Pro is the minimum relevant plan.
Keep the repository private. Prefer GitHub Pro plus an
approved main rule requiring PRs, current passing `Foundation checks`, resolved
conversations, and blocks on force pushes/deletion. Require **zero approving
reviews** and no mandatory CODEOWNERS/last-pusher approval for a solo account.

The alternative is an explicitly accepted manual-governance exception for Phase 0;
it cannot enforce those protections. No purchase, visibility change, permission
change or settings mutation was performed. Missing Projects access is separate
and does not prevent PR review; manual private-board instructions are documented.
See [inspection and exact proposed settings](github-governance.md).

## Documentation and issue consistency review

| Check | Result / limit |
| --- | --- |
| Full vision | 181 enumerated bullets plus six Life Areas prose capabilities = 187; all statuses Planned |
| PRD/catalog/roadmap | DOC-019 waits for tasks; payment feasibility aligns with Phase 4; family/business and advanced actions remain later phases |
| Universal architecture | One Expo client for web/Android/iOS; platform adapters; BFF is server infrastructure, not a second UI or microservice split |
| English launch | Centralized English UI/errors/onboarding/email/push/assistant defaults and end-user docs; provider auth templates included in signup issue; uploaded language remains independent |
| Ownership/provenance | Explicit personal owner; future shared-role/grant model; OCR/AI/manual confirmation do not overwrite originals |
| Backlog | 20 proposed Phase 1 items; original 17 IDs preserved, P1-18/19/20 inserted before P1-10 in dependency order; all unstarted |
| Implementation claims | Only Phase 0 documents/tooling and observed checks are described as created/executed; no application/security verification implied |

The BFF introduces real server complexity. Transport, registry/RLS and lifecycle
work were split into small proposed issues rather than hidden inside a UI-adapter
task. Later-phase detailed issues remain future work. Code-level localization
and security behavior cannot be verified before an application exists.

## Remaining risks and phase gates

- Before starting Phase 1: architecture acceptance and explicit scope approval.
  During authorized P1-01, before dependent implementation: choose hosting/key
  management and validate token-vault, RLS and latency feasibility. Implemented
  auth/revocation tests are Phase 1 completion gates, not Phase 0 claims.
- Before Phase 2: gateway upload limits, parser/scanner bounds, sealed-byte tests,
  worker privilege separation and provider processing consent.
- Before beta: region/legal review, retention/deletion, restore targets, support/
  incidents, billing/store feasibility and actual browser/native evidence.
- Before collaboration: shared ownership/departure/retention terms, role/grant
  negative tests and explicit owner transfer behavior.
- Ongoing: compromised devices/servers, downloaded files and in-flight effects
  cannot be retroactively revoked; no zero-risk or compliance claim.

## Checks, PR status and merge recommendation

The PR remains open and draft. Previous Foundation runs passed; the current head
must pass after this update. [Verification](verification.md) records prior evidence;
the [PR checks](https://github.com/josephengineer/lifeos/pull/19/checks) and PR
description identify the final tested revision. Earlier runs do not verify later
changes. Application tests, web/native builds, deployed RLS/storage, session
lifecycle and recovery checks have not run.

Recommend **conditional Phase 0 merge readiness**, not automatic approval:
accept/amend ADRs, choose governance, verify current-head CI, review the diff and
then provide a separate explicit merge instruction. Until then, keep the PR draft.
Approving a design or governance recommendation does not authorize buying a plan,
changing settings, merging, deploying or starting Phase 1.
