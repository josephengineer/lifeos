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

## Solo-founder protection recommendation

The [governance report](github-governance.md) records the read-only inspection and
exact recommended configuration. GitHub returned an upgrade requirement for both
private branch protection and rulesets; main is currently unprotected. No settings
were changed and the repository must remain private.

The founder now prefers GitHub Pro and this protection configuration. Purchase
and setting changes still need separate authorization; no manual exception is
accepted. Follow the exact steps in the governance report after that authorization.

If supported by the founder's chosen plan, require PRs and the observed
`Foundation checks` status, require an up-to-date branch and resolved conversations,
and block force pushes and deletion of main. Use **zero required approving reviews**
and leave mandatory CODEOWNERS/latest-push approval off for the solo account.
CODEOWNERS remains informational. The founder still explicitly authorizes every
merge; this human decision must not be confused with a self-approval in GitHub.

Do not configure a second-reviewer requirement, buy a plan, enable a ruleset or
change merge settings without approval. Until protection is available, the manual
PR/CI/approval policy cannot technically prevent an authorized account from pushing
or deleting main. Founder acceptance of that risk, or enabling an eligible plan
and approving protection configuration, is required before recommending merge.

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
add issues #1-18 and #20-22, plus PR #19, and link the board to this repository. Keep Phase 1 in
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
