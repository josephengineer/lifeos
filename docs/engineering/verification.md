# Foundation verification

Date: 2026-10-10. Scope: Phase 0 only. Product features remain Planned.

This is a chronological evidence record. Earlier BFF recommendations and all-ADRs-
Proposed statements describe their review revision; the founder-decision follow-up
below and current ADRs supersede those proposals, not the historical test results.

## Environment inspection

- Working directory initially contained only `.git`; no application or existing commits.
- Remote: `josephengineer/lifeos`, verified private via authenticated GitHub API.
- Remote refs were empty at the initial inspection. The founder subsequently
  approved an empty main bootstrap and a foundation PR; see publication below.
- Local feature branch: `codex/phase-0-foundation`.
- Available local tools: Python 3.14.0, Node 22.21.0 and Git. GitHub CLI unavailable;
  Git credentials allowed repository metadata access without printing secrets.

## Verification evidence

- `python scripts/check_foundation.py`: PASS for required files, UTF-8/LF hygiene,
  local file links, JSON/Markdown agreement and feature coverage of the source brief.
- `git diff --cached --check`: PASS for the staged foundation; reviewed staged
  file inventory, workflow/configuration diff and generated catalog/backlog output.
- 187 product capabilities across all 15 modules, including six explicit Life
  Areas capabilities from the source prose. All product statuses remain Planned.
- Isolated temporary-copy mutation probes: PASS; detected a broken local link,
  an invalid feature status and a removed source capability.
- Final story-wording edits exposed two Markdown/JSON synchronization errors.
  Regenerated rows by feature ID and reran the validator successfully; no product
  behavior was affected. The correction is recorded in a follow-up local commit.
- Repository YAML parsed successfully with the locally available PyYAML package;
  workflow triggers, read-only permissions and disabled checkout credential
  persistence were inspected. PyYAML is not a foundation runtime dependency.
- Post-review whitespace probe: the committed-change command rejected a synthetic
  bad-whitespace feature commit and a two-parent PR-style merge. A clean-worktree
  diff missed both, confirming why the workflow needed correction.
- Official `actions/checkout` v4.2.2 ref resolved to the workflow's full pinned SHA
  `11bd71901bbe5b1630ceea73d27597364c9af683`.
- Initially created [Phase 0 issue #1](https://github.com/josephengineer/lifeos/issues/1)
  and 17 Phase 1 issues; the final architecture review expands the proposed backlog
  to 20 Phase 1 issues with three BFF/session items. See the current
  [GitHub backlog](../planning/github-backlog.md). All remain open and unstarted.
- Configured requested type/priority labels and applied labels to the work issues.

Android/iOS builds and all application tests have not run. No application or
managed service exists to test. The GitHub plan/protection availability has not
been inferred from the account name. The final read-only checks confirm that main
is unprotected and GitHub denies private protection/rulesets with an upgrade
requirement; see [governance evidence](github-governance.md). No repository settings,
production systems or billing rules have been changed.

GitHub Project access was denied because the available credential lacks Projects
scopes. No board was created or changed. Repository access does not imply Projects
access. The founder can create the private board manually using the documented
statuses or explicitly authorize the necessary access later; no token scope was changed.

## Authorized publication and sensitive-content review

- Rechecked authenticated GitHub metadata immediately before pushing: private=true.
- Main contains only the empty root commit
  `cdc1d64cbf47c71b3af1573032cddb51f59c43dc`; zero tracked files. Foundation files
  were pushed only to `codex/phase-0-foundation`, without force-pushing.
- Opened [draft PR #19](https://github.com/josephengineer/lifeos/pull/19) targeting
  main, initially linked issue #1 and 17 Phase 1 issues, and included a per-module
  capability-count table. Issues #20-22 now track the three proposed BFF/session
  items; reviewed publication evidence is recorded separately below.
  No issue is Done and Phase 1 remains unapproved.
- Gitleaks 8.30.1, downloaded from its official release and checked against its
  SHA-256 digest, scanned the two original local commits: zero findings. No scan
  data was uploaded to a third-party scanning service.
- Reviewed the initial 50 tracked text files for personal email addresses,
  user-directory paths, binary/customer documents, credential files and secret
  material; no content findings. Original Git metadata used a personal email.
  Published commits use the verified GitHub noreply identity instead; original
  history is retained locally and was not pushed.
- Content checks are bounded evidence, not a guarantee against all sensitive data.
  Rerun the scanner on the published branch after review corrections.

## Remote CI evidence

For initial published revision `a1099be069be92f6e02adbf3b746644b518be307`, GitHub
reported success for both the [push run](https://github.com/josephengineer/lifeos/actions/runs/38074436310)
and [PR run](https://github.com/josephengineer/lifeos/actions/runs/38074481655).
These runs precede the post-creation review fixes, including the meaningful committed
whitespace check. They do not prove a later revision passes. The latest head's
results are recorded in the [PR checks](https://github.com/josephengineer/lifeos/pull/19/checks)
and the PR description after checking GitHub directly. No CI success implies
application, native, RLS/storage, deployment or compliance verification.

## Pending completion gates

Founder review of the [findings](foundation-review.md), current-head CI, protection
availability and the solo-founder governance decision; explicitly approved merge and
post-merge checks. Bootstrap/push authorization does not approve merge or Phase 1.

## Resumed Phase 0 review: 2026-10-13

Reviewed all 26 interrupted tracked changes and four new drafts, preserving valid
work. Added PROJECT_STATUS and its maintenance rule. Corrected stale publication
and Project issue references, the Phase 1 spike gate, and Phase 1 versus Phase 4
session-management UI wording. ADRs remain Proposed; added operational costs,
refresh/restore/key recovery gates, safe-preview requirements and grant-version
decisions. All 20 live Phase 1 issue bodies match the corresponding local sections
after whitespace normalization. No issue was recreated or closed.

Executed local checks:

| Check | Result |
| --- | --- |
| `python scripts/check_foundation.py` | PASS: artifacts, UTF-8/LF, links, source traceability and Markdown/JSON agreement |
| Catalog count/status assertions | PASS: 187 Planned capabilities, all 15 modules |
| PyYAML 6.0.3 BaseLoader with duplicate-key rejection | PASS: all three YAML files; workflow trigger/permission assertions |
| actionlint 1.7.12 | PASS: foundation workflow, no diagnostics; official release archive SHA-256 verified |
| `git diff --check` | PASS: working diff whitespace |
| Temporary-copy validator mutations | PASS: missing PROJECT_STATUS, broken link and invalid status detected; restored fixture passes |
| Sensitive-content inventory | PASS: 56 repository text files; no binary/customer attachments, personal path/email or credential filename matches |
| Gitleaks 8.30.1 directory scan | PASS: reviewed working-tree snapshot, zero findings |
| Gitleaks 8.30.1 branch history scan | PASS: published foundation history from origin/main to reviewed HEAD, zero findings; backup branch excluded from publication |

The first temporary mutation harness restored files with Windows CRLF, so its
restored-fixture assertion failed. Corrected only the temporary harness to preserve
LF and reran successfully; repository content was not changed by those probes.
The first directory scan could not run because that failed harness had not created
its snapshot; it subsequently ran successfully as recorded above.

Static workflow validation is not a native build or application security test.
No application, auth/session, RLS/storage, device, scanner or deployment checks
have run. Sensitive-content review is bounded evidence, not a universal guarantee.
Publication requires a staged whitespace check, scan of the new commit and a fresh
private-repository check before pushing. Exact new SHA and remote CI are recorded
in the publication follow-up and PR description after execution.

### Review publication evidence

Published review commit `d5a5c5a6e6f7a54495d411fa42f7c430ccb3d79e` to the existing
foundation branch without force push. Staged and committed whitespace checks
passed; a refreshed working-tree scan and branch history scan including the new
commit returned zero findings. Privacy was rechecked immediately before push.
Updated draft PR #19 with all six findings, six proposed ADRs, 187-capability
summary, all 21 work issues and explicit executed/unrun checks.

GitHub reports both runs completed successfully for that exact review SHA:

- [Pull-request run 38450517559](https://github.com/josephengineer/lifeos/actions/runs/38450517559).
- [Push run 38450512405](https://github.com/josephengineer/lifeos/actions/runs/38450512405).

This evidence/status follow-up is a later documentation commit and requires its
own CI. The PR description records its final SHA and results after verification;
the runs above are not claimed to validate later edits. Main remains the empty
bootstrap, the PR remains draft/unmerged and no repository setting was changed.

## Founder-decision follow-up: 2026-10-13

Recorded ADR-0005 conditional approval of security objectives only and ADR-0006
principle approval with component design/threat/test gates. Compared official
SDK/native/web/SSR guidance with web-only and universal BFF alternatives. Recommend
official SDK research first; browser persistence/XSS, exact timeouts and direct
provider account-operation controls remain unresolved implementation decisions.
No opaque issuer or refresh-token vault is assumed. No runtime spike was executed.

Synchronized architecture/API/data/security/setup/roadmap/backlog references and
all 20 existing Phase 1 issue titles/body sections; each remains open and Planned.
P1-18 is now Research. Added the final Phase 0 approval checklist and exact Pro/main
protection steps. Founder preference does not authorize purchase or settings changes.

Executed before publication: foundation validator and working diff whitespace
checks passed; all three YAML files parsed with unique-key/trigger/permission
assertions; actionlint 1.7.12 passed; catalog remained 187 Planned capabilities in
15 modules. Isolated missing-status/broken-link/invalid-status mutation probes
passed. Sensitive inventory covered 57 text files with no personal-path/email,
binary/customer attachment or credential filename findings. Gitleaks 8.30.1 scanned
the reviewed-tree snapshot with zero findings. Staged/committed checks and exact
new-head CI publication results are recorded in the PR description after execution.

Read-only GitHub inspection still returned private=true, main protected=false,
and HTTP 403 upgrade requirements for protection/rulesets. PR #19 remained draft
and unmerged at baseline 54a1b56. New documentation commits must pass fresh CI;
old runs do not validate them. No settings, subscriptions, deployment or Phase 1
implementation changed. No application/native/RLS/storage/auth tests have run.
