# Public repository security and merge-readiness review

Date: 2026-10-14. Published head inspected: b4540e3167dc112d6f9412018579e169f6b2cadd.
Scope: public LifeOS source/history and governance. No application exists.

## Evidence and scope

Anonymous GitHub API confirmed public visibility. A fresh public mirror fetched
all advertised branch and PR refs: main, codex/phase-0-foundation, pull/19/head and
pull/19/merge. No tags or releases existed. This avoids confusing a local-only
backup branch with published history. Reachability inventory: seven commits
(including the empty root and GitHub-generated test merge), 130 distinct file
blobs across 57 paths. Every historical blob was checked for binary content,
personal paths/emails and sensitive filenames; no such content flags were found.
Gitleaks 8.30.1 scanned all reachable history, reporting five content-bearing
commits and zero secret findings. Metadata review is separate from secret scanning.

Current source consists of product/engineering documents, synthetic configuration
and repository tooling. No live customer records, contracts, financial amounts,
private keys or database dumps were identified. Product strategy, 187-capability
catalog, founder brief, roadmap, threat model and architecture are publicly exposed
business information. Confidentiality intent cannot be determined by a scanner;
founder confirmation of that publication scope remains necessary.

All 22 issue/PR bodies were additionally checked for personal paths/email patterns;
none were found. There were no issue/review comments or Actions artifacts returned
by the inspected endpoints. This does not certify every historical Actions log,
unadvertised/unreachable object, cached page, fork or third-party copy.

## Findings

| ID | Severity | Finding | Disposition |
| --- | --- | --- | --- |
| PUB-01 | P1 privacy | GitHub-generated pull/19/merge author metadata contains a personal email | Value omitted; hold new publication pending founder privacy review and reinspection |
| PUB-02 | P1 governance | main unprotected; no classic rule or ruleset; Foundation checks not required | Configure the documented Free/public main rule under separate authorization; verify readback |
| PUB-03 | P2 disclosure | Public product strategy/brief/security design; no confidential customer/business records identified | Founder confirms publication scope and resolves licensing/ownership separately |
| PUB-04 | P2 reporting | Private vulnerability reporting disabled; no dedicated public reporting contact | Founder chooses/enables a safe reporting path; no permission changes made |

All six commits on the published branches use GitHub noreply author/committer
addresses. The extra generated PR merge commit has the personal author address;
its GitHub committer address is noreply. Earlier branch-only identity scans did
not establish privacy of generated PR refs. No raw address is copied into this
report, PR text or additional tracked files.

## Privacy remediation instructions

The founder should review GitHub Settings -> Emails -> Keep my email addresses
private, and optionally Block command line pushes that expose my email. Local Git
already uses the GitHub noreply identity. After confirmation, inspect new generated
merge metadata as well as branch commits. These settings are preventative and do
not remove already published objects. GitHub Support may need to assess removal
of cached or PR references; no removal guarantee is made. Do not rewrite shared
history or change visibility without separate instructions. See GitHub's
[email guidance](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)
and [sensitive-data removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## PR and architecture state

PR #19 is open, draft and unmerged. Published head contains the latest main
cdc1d64; behind main: zero commits. GitHub reports mergeable, which is not an
authorization or protection guarantee. Existing head CI passed:

- [PR run 38453001615](https://github.com/josephengineer/lifeos/actions/runs/38453001615).
- [Push run 38452990109](https://github.com/josephengineer/lifeos/actions/runs/38452990109).

Both emit Foundation checks from GitHub Actions (app ID 15368). Workflow uses
read-only contents permission, a pinned checkout action, no persisted credential,
no secrets/deployment and pull_request rather than pull_request_target. Public
contributions still require review before execution/merge; this is not application
security verification.

ADR-0005 security objectives are conditionally approved, implementation undecided
pending official-SDK assessment. No custom session system without concrete need
and approval. ADR-0006 principles are approved with pre-code design/threat/test
gates and executed verification before completion. English application copy and
private user storage requirements are unchanged.

## Initial readiness snapshot (superseded by follow-ups below)

Not ready to merge: resolve PUB-01 publication handling and the PUB-02 follow-up gates,
confirm public business-document scope, publish reviewed updates and verify fresh
CI, then obtain final explicit merge authorization. Local documentation updates
are deliberately not pushed while generated-metadata privacy is unresolved.
No settings changed, force push, merge, Phase 1 implementation or deployment.

## Follow-up after founder configured protection: 2026-10-14

PUB-02's initial missing-rule finding is superseded: main now has active classic
protection requiring PRs, Foundation checks from Actions app 15368, strict
up-to-date branches and admin enforcement, with force pushes/deletion disabled.
One mandatory approving review conflicts with the zero-approval solo-founder
policy. Required signatures are also enabled, while published and pending heads
are unsigned. These gates remain unresolved; see the governance report.
PR #19 remains draft and GitHub now reports its merge state as blocked.
Pending local f619a5e author/committer are both GitHub noreply; the existing
generated merge ref still exposes personal author metadata. No push, settings
change or merge was performed during this follow-up.

## Subsequent protection and exact-email review: 2026-10-14

GitHub API confirms active classic main protection: required PRs, Foundation
checks from Actions app 15368, strict up-to-date branches, admin enforcement,
no force pushes/deletion, zero required approvals and signatures disabled.
Conversation resolution remains required; no rulesets apply. PR #19 is draft,
unmerged, merge state clean; both checks on b4540e3 succeed, base remains cdc1d64.

A new anonymous public mirror contains four advertised refs and 181 reachable
objects: seven commits, 44 trees and 130 blobs. Case-insensitive exact-email
inspection of every raw object found only the author field of commit
`070b72ac3355813c2de9d30998e993ed6cd446db`, reachable only through
`refs/pull/19/merge`. Neither main nor foundation branch history nor
`refs/pull/19/head` contains it; all six branch commits use noreply author and
committer metadata. No blob or tree contains the address. The raw email is not
reproduced in this report.

Two known local backup commits containing the address were probed anonymously
by SHA and returned HTTP 404. They remain local and must not be pushed. This
cannot enumerate unadvertised/unreachable GitHub objects, prior generated merge
commits, caches or external copies. The synthetic merge object itself is already
public Git history, although it is not part of either published branch history.
Pending f619a5e author and committer both use the configured GitHub noreply address.

Recommendation: do not rewrite clean published branches. First confirm account
Settings -> Emails -> Keep my email addresses private (optionally enable blocking
command-line email exposure too). GitHub documents noreply for future web-based
operations; regenerated test-merge metadata still needs inspection, not assumption.
After explicit publication authorization, push the reviewed work normally and
inspect the regenerated PR merge ref, author/committer fields and fresh CI.
Regeneration does not prove the old object was purged. If removal of the old
public object is required, ask GitHub Support about this SHA/PR; Support eligibility
and deletion are not guaranteed. refs/pull is read-only to users. Do not force-push,
close/reopen the PR or rewrite branches as a purported erasure solution.

Sources: [email privacy](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address)
and [retained PR refs and removal limitations](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
No push, commit, settings change, merge, Phase 1 work or deployment occurred.
Existing uncommitted work was preserved and current status statements updated.

## Publication authorization: 2026-10-14

The founder confirmed Keep my email addresses private is enabled and explicitly
authorized committing and pushing reviewed documentation to the existing Phase 0
branch, preserving history. This lifts the publication hold; it does not authorize
merge or assert that the historical exposed object has been erased. Reinspect the
new generated merge ref and CI after publication. No application work is authorized.
