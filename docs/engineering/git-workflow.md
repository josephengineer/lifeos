# Git workflow and GitHub configuration

Use lightweight GitHub Flow. Work begins with an issue and acceptance criteria,
then a descriptive `codex/<topic>` branch, small coherent implementation, relevant
tests/docs, Conventional Commit, authorized push and PR. Review diff, CI and
security. The founder approves before squash merge; verify post-merge CI.
Never force-push, overwrite important branches or bypass failing checks.

## Empty-repository bootstrap

The existing private repository has no commits or main branch. The prepared
foundation lives on `codex/phase-0-foundation`. A PR requires an actual base branch
with shared history. Obtain founder approval for a minimal empty initial commit
on main, then replay the foundation commits onto that base on the feature branch,
push both without force, and open the documentation PR. No product or foundation
feature changes should be committed directly to main. Reinspect remote refs
before bootstrap; if somebody populated the repository, preserve that history
and adapt the branch normally. Do not push the orphan feature branch first and
accidentally make it the only/default integration branch.

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

Official guidance: [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
and [Actions security](https://docs.github.com/en/actions/reference/security/secure-use).
