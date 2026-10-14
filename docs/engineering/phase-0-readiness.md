# Phase 0 architecture, security and governance readiness

Updated 2026-10-14 after public visibility review. Phase 0 remains In Review.
[Draft PR #19](https://github.com/josephengineer/lifeos/pull/19) contains documentation
and foundation tooling only. No Phase 1 work, deployment or publishing is authorized.

## Decisions recorded

- ADR-0005: security objectives conditionally approved; final architecture is not.
  The revised comparison recommends official Supabase SDK first, protected native
  storage and memory-only web as a candidate. Browser XSS/persistence UX, timeout
  semantics and runtime evidence remain gates. No custom session system without
  concrete necessity, alternatives and explicit approval.
- ADR-0006: ownership/isolation, immutable originals, separate derivatives,
  provenance, server authorization and retention/deletion principles approved.
  Detailed component designs, threat models and test specifications must be
  finalized before coding; actual tests are required before verification.
- GitHub: founder selected public source on GitHub Free; no Pro purchase needed.
  Main protection is still absent. Required PR/CI/strict/no-force/no-delete/admin
  controls need separate configuration authorization. No manual exception accepted.
  Public review also found personal author metadata in the generated PR merge ref;
  resolve privacy handling before publishing more updates.
- ADRs 0001-0004 remain Proposed. Accepting the documentation with explicit deferrals
  is distinct from approving application implementation or selecting all policies.

See the [decision register](../planning/decisions.md), [auth comparison](../adr/0005-authentication-and-sessions.md),
[ownership gates](../adr/0006-workspace-ownership-and-document-provenance.md) and
[exact GitHub setup](github-governance.md).

## Findings and consistency

The [six-finding table](foundation-review.md) records corrections and remaining
risks. R01/R04/R05 documentation/tooling defects are corrected. R02/R03 principles
are accepted but controls are unimplemented. R06 objectives are conditionally
accepted; the simpler candidate must prove its authorization and revocation behavior.

All 187 capabilities across 15 modules remain Planned. PRD/catalog/roadmap retain
the task dependency and Phase 4 billing research corrections. One universal Expo
client remains; English UI/email/notification/error/assistant-default resources
remain mandatory, independent of uploaded document language.

The 20-item planned backlog retains stable IDs. P1-18 now evaluates official SDK
feasibility; P1-19 gates provider-session/RLS authorization; P1-20 uses approved
SDK lifecycle behavior. No issue authorizes an opaque issuer or vault by default.
Later detailed issues, code localization and runtime security evidence remain future work.

## Remaining gates and risks

- Before merge: public-content/privacy disposition, safely published updates,
  current-head CI and founder review; active protection now verified with zero mandatory approvals
  and signatures disabled; recheck before merge; explicit merge instruction.
- Before Phase 1: separate research/scope approval. Before dependent auth coding:
  SDK evidence, accepted final architecture, web persistence/XSS and exact expiry
  policy; provider-session helper, reset/fresh-auth and recovery designs.
- Before ownership/file components: ADR-0006 schema/threat/test specifications,
  safe preview and immutable intake/worker boundaries; actual tests before completion.
- Before beta: regions/provider terms, retention/deletion/restore, licensing,
  billing/store feasibility, support and real browser/native security evidence.
- Before collaboration: roles, pinned versus changing shared versions, owner
  transfer/departure and retention terms.
- Residual: active XSS can steal SDK web tokens; protected native storage does not
  defeat compromised devices. Provider session checks add database load/availability
  dependence. Revocation cannot recall downloaded bytes or all in-flight actions.

## Evidence and recommendation

[Verification](verification.md) contains dated executed checks. Current revision
and completed CI results belong in the [PR checks](https://github.com/josephengineer/lifeos/pull/19/checks)
and PR description; earlier runs never validate later changes. Application tests,
native builds, deployed RLS/storage/auth and restore tests have not run.

Use the [final approval checklist](phase-0-approval-checklist.md).
Recommend approval of the Phase 0 documentation baseline with explicit unresolved
implementation gates, followed by a separately authorized merge once protection
is verified. Neither principle approval nor merge approval starts Phase 1.
