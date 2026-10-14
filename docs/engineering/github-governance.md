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
| Default main | Empty bootstrap cdc1d64; protected=true |
| Classic main protection endpoint | Active rule returned for main |
| Repository rulesets / effective main rulesets | Empty lists; classic protection applies |
| Required PR | Enabled |
| Required CI | Foundation checks, GitHub Actions app ID 15368; matches emitted job |
| Up-to-date enforcement | strict=true |
| Administrator enforcement | enforce_admins.enabled=true; no bypass allowances returned |
| Force pushes / deletion | Both disabled |
| Mandatory approvals | 0; matches solo-founder policy; Code Owners and last-push approval off |
| Signed commits | Disabled by founder; existing unsigned heads are permitted by this setting |
| Conversation resolution | Required |
| Published CI | Two successful Foundation checks runs on b4540e3 |
| Private vulnerability reporting | Disabled at public audit; no setting change authorized |

The subsequent founder configuration change resolves the approval/signing
mismatches: zero required approvals, signatures disabled. All requested protection
settings now match. Privacy/publication review and final explicit merge approval
remain outstanding. PR #19 is still draft, with API merge state clean.

This is configuration readback, not a destructive enforcement test. No direct
push, force push, deletion or unauthorized merge probe was attempted. Initial
absence of protection in the public review is historical; this readback follows
the founder's configuration change.

## Exact setup for the founder

No plan upgrade is needed. After separate authorization to change settings:

1. Open repository Settings -> Branches -> Edit the existing main protection rule.
2. Target exactly `main`; enable Require a pull request before merging.
3. Leave Require approvals unchecked: zero mandatory approvals. Leave Code Owners,
   stale-approval and most-recent-push approval requirements off.
4. Require status checks; select the exact `Foundation checks` check, source
   GitHub Actions where available. Require branches to be up to date.
5. Require conversation resolution; enable Do not allow bypassing the above settings.
6. Leave Allow force pushes, Allow deletions and Lock branch unchecked.
7. Leave Require signed commits disabled under the current founder decision.
8. Save, then read back the main rule. Avoid conflicting overlapping rules.

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
verify final-head CI and latest-main ancestry, recheck protection,
then request final explicit merge authorization. Earlier conditional approval is
not permission to merge. ADR-0005 implementation remains undecided and ADR-0006
component gates remain binding. No Phase 1 implementation or deployment follows.
