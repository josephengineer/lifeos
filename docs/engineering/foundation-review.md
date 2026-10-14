# Foundation findings and current disposition

Updated 2026-10-13 for [draft PR #19](https://github.com/josephengineer/lifeos/pull/19).
This is the implementing agent's review, not independent human approval. P1 means
high-priority security/design risk; P2 means a documentation/tooling defect. A
corrected requirement is not an implemented or tested application control.

| Finding | Severity | Reviewed correction | Current status / remaining risk |
| --- | --- | --- | --- |
| R01: document-linked tasks preceded task dependencies | P2 | DOC-019 moved to Phase 3 with DOC-001/TASK-001/TASK-007 prerequisites; catalog/roadmap aligned | Documentation resolved; all capabilities remain Planned |
| R02: workspace-key rule conflicted with account records | P2 | Separate account records, explicit owner_user_id and matching personal owner membership; workspace-owned documents use created_by attribution | Principles approved under ADR-0006; detailed design gates, ADR-0002 and actual FK/RLS/ownership tests pending |
| R03: quarantine allowed an unspecified post-scan replacement path | P1 | Seal bytes before scan, preserve immutable originals, separate derivatives, deny client/worker original writes; add hashes and race/provenance tests | ADR-0006 principles approved; component design/threat/test gates and Phase 2 verification pending; privileged operator risk remains |
| R04: CI whitespace command inspected no committed changes | P2 | First-parent committed diff with fetch-depth 2; synthetic bad feature/merge commits detected | Tooling resolved and remotely passed on the preceding reviewed head; recheck current head after updates |
| R05: stale verification text and incomplete Project resolution | P2 | Record empty bootstrap, draft PR and check evidence; document manual Projects setup and protection entitlement denial | Historical documentation fixed; new public review finds protection unconfigured, not unavailable; Projects permission remains unresolved |
| R06: logout could imply immediate JWT invalidation | P1 | ADR-0005 now compares official SDK with BFF alternatives and recommends provider-session/account gates without a duplicate issuer | Security objectives conditionally approved; web storage/timeout/final architecture and runtime evidence pending; issued JWTs/in-flight data cannot be recalled |

References: [ADR index](../adr/README.md),
[auth ADR](../adr/0005-authentication-and-sessions.md),
[ownership/provenance ADR](../adr/0006-workspace-ownership-and-document-provenance.md),
[database design](../architecture/database.md), [CI design](ci.md),
[GitHub governance](github-governance.md), [verification](verification.md).

## Additional consistency corrections

- Replaced mandatory one-reviewer/CODEOWNERS guidance with zero required reviews
  for the solo account, while retaining explicit founder merge authorization.
- Replaced the earlier BFF assumption with an official-SDK-first comparison;
  synchronized API/data/environment/backlog references. No reusable signed
  download URLs are planned; file intake does not require an auth session issuer.
- Aligned INT-009 payment-provider feasibility to Phase 4 billing, matching the
  integration plan's existing exception; other integrations remain later.
- Distinguished internal provenance from Phase 2 and later user-facing version
  history. Analysis never changes original file bytes.
- Expanded the proposed Phase 1 backlog from 17 to 20 small items without starting
  implementation; new IDs preserve existing GitHub issue references.

## Open risks and recommendation

Accept or amend the proposed ADRs before treating their designs as settled.
Auth storage/timeout choices, scanner/worker limits, privacy/retention, operational
targets and billing/store feasibility remain phase-gated decisions. Public GitHub Free supports protection, but the current absence of rules
leaves branch safety unenforced; see public-repository-review.md. No compliance,
production security, native build or implemented feature claim is made.

The final [readiness report](phase-0-readiness.md) states merge conditions and the
approval request. Keep this PR unmerged and Phase 1 unstarted until explicitly
authorized. No board/protection setting change follows automatically from review.
