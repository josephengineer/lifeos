# GitHub governance: public repository on GitHub Free

Inspected 2026-10-14. The founder changed LifeOS from private to public.
The agent did not change visibility, billing, permissions or protection settings.
This supersedes the earlier private-repository/GitHub Pro preference.

GitHub Free supports protected branches in public repositories. Pro is no longer
required for this configuration. This is an entitlement statement; the account's
actual billing plan was not inspected or changed. Private application storage and
tenant isolation requirements are unchanged by public source visibility.

## Observed configuration

| Read-only evidence | Result |
| --- | --- |
| Anonymous repository API | visibility=public, private=false; source readable without credentials |
| Default main | Empty bootstrap cdc1d64; protected=false |
| Classic main protection endpoint | HTTP 404: Branch not protected |
| Repository rulesets | Empty list |
| Effective rules for main | Empty list |
| Required PR / current CI / up-to-date enforcement | Not configured |
| Force-push / deletion / admin-bypass prevention | Not enforced by branch protection |
| Mandatory external reviews | No protection review requirement; does not compensate for missing PR rule |
| Emitted CI job | Foundation checks, GitHub Actions app ID 15368; passing on published b4540e3 |
| Private vulnerability reporting | Disabled; no setting change authorized |

**Merge blocker:** visibility alone does not configure protection. Successful CI
is informational until the check is required. No destructive push/delete or
unauthorized merge probe was attempted; missing settings already establish that
the requested protections are absent. No claim of enforced protection is made.

## Exact setup for the founder

No plan upgrade is needed. After separate authorization to change settings:

1. Open repository Settings -> Branches -> Add classic branch protection rule.
2. Target exactly `main`; enable Require a pull request before merging.
3. Leave Require approvals unchecked: zero mandatory approvals. Leave Code Owners,
   stale-approval and most-recent-push approval requirements off.
4. Require status checks; select the exact `Foundation checks` check, source
   GitHub Actions where available. Require branches to be up to date.
5. Require conversation resolution; enable Do not allow bypassing the above settings.
6. Leave Allow force pushes, Allow deletions and Lock branch unchecked.
7. Save, then read back the main rule. Avoid conflicting overlapping rules.

Expected readback: PR rule present, approval count 0, status context Foundation
checks (app ID 15368 where specified), strict=true, enforce_admins.enabled=true,
force pushes/deletions disabled and no bypass actors. Also inspect effective
rulesets for additional constraints. Admins can still edit settings themselves;
the rule prevents operation-level bypass, not the owner's ability to change policy.
Do not test force-pushing or deleting main. Any disposable enforcement test needs
a separately approved setup. Founder still explicitly approves each merge.

Official sources: [protection availability](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
and [classic rule setup](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).

## Public-content and reporting gates

Read the [public exposure review](public-repository-review.md). Product plans and
security architecture are now public business material. Confirm this scope is
intentional; do not place customer documents, credentials, confidential agreements
or unreleased commercial figures in this repository. No open-source license has
been selected by changing visibility.

GitHub's generated PR merge ref exposed personal author metadata. The report
omits its value. Before another push, the founder should review GitHub Settings ->
Emails -> Keep my email addresses private and optionally block command-line pushes
that expose personal email. Recheck regenerated PR metadata; changing preferences
does not erase old Git objects or external copies. No history rewrite is authorized.

Private vulnerability reporting is disabled and a dedicated contact is unresolved;
see SECURITY.md. Enabling it requires separate settings authorization.
The Project-board permission remains a separate unresolved task; a public code
repository does not require making the planning board public.

## Merge conditions

Confirm email/privacy disposition, publish the reviewed documentation safely,
verify final-head CI and latest-main ancestry, configure/read back protection,
then request final explicit merge authorization. Earlier conditional approval is
not permission to merge. ADR-0005 implementation remains undecided and ADR-0006
component gates remain binding. No Phase 1 implementation or deployment follows.
