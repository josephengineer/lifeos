# Git workflow and GitHub configuration

Use lightweight GitHub Flow. Work begins with an issue and acceptance criteria,
then a descriptive `codex/<topic>` branch, small coherent implementation, relevant
tests/docs, Conventional Commit, authorized push and PR. Review diff, CI and
security. The founder approves before squash merge; verify post-merge CI.
Never force-push, overwrite important branches or bypass failing checks.

## Empty-repository bootstrap

Completed with explicit founder approval: main contains only empty bootstrap
commit `cdc1d64cbf47c71b3af1573032cddb51f59c43dc`. The foundation is on
`codex/phase-0-foundation` in [draft PR #19](https://github.com/josephengineer/lifeos/pull/19).
No documentation or application files were placed directly on main. The original
local-only history was preserved locally; the published foundation was replayed
with GitHub noreply author metadata and shared ancestry. No force push was used.
This bootstrap approval does not authorize a merge or Phase 1 implementation.

## Founder branch-protection checklist

After main exists and the Foundation workflow has run, open repository Settings
and configure a branch rule/ruleset targeting main using controls your plan offers.

1. Require PRs before integration; disallow direct pushes, force pushes and deletion.
2. Require the actual emitted `Foundation checks` status, confirmed from a run.
   Add app checks when implemented; do not select nonexistent check names.
3. Require conversation resolution where offered. Require review of the most
   recent change and dismiss stale approval where appropriate.
4. Require one eligible human approval and CODEOWNERS review where supported.
   Configure admin/bypass restrictions deliberately; do not assume admins are covered.
5. Use squash merge, and restrict who can integrate. Verify with a disposable PR
   that failing checks/direct pushes are actually blocked.
6. Enable secret scanning/push protection where available for the private repo
   and current plan. Enable dependency alerts/update PRs. Review cost before upgrades.

Private repository protections depend on GitHub plan. If unavailable, retain a
documented human merge gate; it is weaker than enforced protection. Do not buy
a plan or change security-sensitive permissions without founder approval.

GitHub prevents authors approving their own PR. If the only account is both
author and founder, document founder approval in the PR and retain manual gating,
or establish an independently authorized contributor/reviewer before enforcing
an impossible approval rule. Do not create an automation identity or grant access
without approval. CODEOWNERS alone does not enforce approval.

## Issues and project board

Use type labels Epic, Feature, Bug, Security, Documentation, Technical debt and
Research; priority labels P0 Critical, P1 High, P2 Medium and P3 Low. Labels are
descriptive and do not override security-reporting privacy. Create one issue per
small deliverable from the ordered backlog, with linked dependencies and feature IDs.

Create a private GitHub Project with Status values Backlog, Ready, In Progress,
In Review, Blocked and Done. Ready needs explicit scope and resolved dependencies;
Blocked records an owner/action; Done requires tests, CI, review and approved merge.
Do not make the board public. Project authorization is separate from repository
access; record inability to provision rather than claiming a board exists.

### Resolving the missing Projects permission

The existing credential was denied Projects access. No scope changes or alternate
credentials were attempted. To proceed manually, the founder can open their GitHub
profile, choose Projects -> New project -> Board, name it LifeOS, and verify its
visibility is Private in project settings. Configure the six Status values above,
add issues #1-18 and PR #19, and link the board to this repository. Keep Phase 1 in
Backlog until approved, and Phase 0 In Review while the PR remains unmerged.
See [GitHub's project creation guide](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project).

If API management is desired later, the founder must explicitly authorize an
appropriate credential. For classic tokens, `read:project` permits reads and
`project` permits reads and mutations; use the supported least-privilege equivalent
for other credential types. Update authentication through the normal credential
manager, never by pasting a token into chat or committing it. This permission is
optional for the current PR; no bypass or permission change is part of this task.
See [GitHub's Projects API authentication guidance](https://docs.github.com/en/issues/planning-and-tracking-with-projects/automating-your-project/using-the-api-to-manage-projects).

Official guidance: [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
and [Actions security](https://docs.github.com/en/actions/reference/security/secure-use).
