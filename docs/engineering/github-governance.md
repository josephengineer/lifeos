# GitHub governance decision for a solo founder

Reinspected 2026-10-13 using authenticated, read-only GitHub REST requests.
No repository settings, subscriptions, permissions or visibility were changed.

Founder decision: **GitHub Pro with protected main is preferred.** Purchase and
settings changes remain unauthorized. No temporary manual exception was accepted.

## Observed evidence

| Read | Result |
| --- | --- |
| Repository metadata | Private, main is default, current credential has repository admin access |
| main branch | protected=false; still the zero-file bootstrap commit |
| GET branches/main/protection | HTTP 403: upgrade to GitHub Pro or make repository public to enable feature |
| GET rulesets | Same HTTP 403 upgrade requirement |
| GET rules/branches/main | Same HTTP 403 upgrade requirement |
| Merge settings | Squash, merge commit and rebase currently allowed; automatic branch deletion disabled |
| Account plan name | Not returned; do not invent an exact account subscription |

Admin access does not remove this availability restriction. GitHub's response is
evidence that protection/rulesets are unavailable for this private repository's
current entitlement. Do not make LifeOS public to obtain them and do not attempt
an alternate credential or endpoint as a bypass. The separate Projects permission
block remains unchanged; see [manual board setup](git-workflow.md).

## Exact plan requirement

The repository API identifies its owner as a **User**, not an organization.
For this private personal repository, **GitHub Pro** is the minimum paid personal
plan documented to support protected branches and branch/tag rulesets. GitHub Team
is the corresponding option for organization-owned private repositories;
Enterprise plans also support protection. An individual's Pro subscription does
not supply Team entitlement to an organization. No transfer is recommended.
Push rulesets are a separate feature and are not needed for the main branch rules.

Recommend GitHub Pro for the present ownership, then separately approve the
settings below. This identifies the required product, not the current plan: its
name was not returned. The 403 responses establish the enforcement limitation.
No subscription or price commitment is made. Official branch/ruleset documentation
was rechecked on 2026-10-13.

## Recommended configuration, if the founder enables a supported plan

Choose one active main ruleset (or equivalent classic protection), not overlapping
contradictory policies. Preview it before saving and verify it with a test PR.

| Setting | Recommendation |
| --- | --- |
| Target / enforcement | Exactly main; active enforcement, including admin where supported |
| Require pull request | On; no routine direct push or bypass |
| Required approvals | **0** for the solo-founder workflow |
| Require CODEOWNERS review | Off; keep CODEOWNERS informational |
| Latest-push approval / stale-review restrictions | Off where they would require a second person |
| Required status checks | Exact observed `Foundation checks`, from GitHub Actions where selectable; require branch up to date |
| Conversation resolution | On where available |
| Force pushes / non-fast-forward changes | Block |
| Deletion of main | Block |
| Merge strategy | Recommend squash only; configure separately after approval |
| Bypass list | No standing routine bypass; documented explicit emergency procedure |
| Restrict all updates / lock branch | Off; do not accidentally prevent legitimate PR merges |

Zero required approvals does not remove the human decision: the founder reviews
the diff, current-head CI and findings and explicitly authorizes the squash merge.
An author cannot provide an independent GitHub approval for their own PR. Do not
create a dummy reviewer or impose a CODEOWNERS requirement that deadlocks this
single-account repository. Reconsider one independent approval when a second
authorized human joins. AI review never substitutes for the founder's decision.

## Current-plan fallback and merge recommendation

Until enforcement is available, keep the repository private and all work on PR
branches. Manually require current-head CI success, resolve discussions, obtain
explicit founder approval, squash only, and never force-push/delete main. This is
a procedural control: it **cannot technically prevent** accidental direct pushes,
force pushes or deletion by an authorized account.

Recommend enabling a supported private-repository plan before merge, subject to
the founder's own purchase decision and separate approval of the exact settings.
Alternatively the founder may explicitly accept the documented manual-governance
risk for Phase 0 only. The founder now prefers Pro; the manual exception is not
selected. No purchase or configuration has been executed.
Do not represent unavailable enforcement as configured protection.

Sources checked: [protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
and [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets).
Exact UI labels and plan capabilities must be rechecked when configuration is approved.

## Exact founder setup instructions (not executed)

Purchase is a separate founder action: follow GitHub's
[personal-plan upgrade instructions](https://docs.github.com/en/billing/how-tos/manage-plan-and-licenses/upgrade-plan),
open profile **Settings -> Billing & Licensing -> Licensing -> Current plan ->
Upgrade -> Upgrade to Pro** for the repository-owning personal account, review the
displayed price/billing cycle and confirm only when ready. Keep LifeOS private.
This does not purchase Supabase Pro or authorize an agent to change settings.

After Pro is active and settings changes are explicitly authorized, use one classic
rule as the simplest configuration:

1. Repository **Settings -> Branches -> Add classic branch protection rule**.
2. Set **Branch name pattern** to exactly `main`.
3. Enable **Require a pull request before merging**. Leave **Require approvals**
   unchecked (zero approvals), Code Owners and latest-push approval unchecked.
4. Enable **Require status checks to pass before merging**, select the existing
   **Foundation checks** check and require the branch to be up to date.
5. Enable conversation resolution and **Do not allow bypassing the above settings**.
6. Leave **Allow force pushes**, **Allow deletions**, and **Lock branch** unchecked.
   Do not add deployment/merge-queue requirements or overlapping rules.
7. Review and click **Create** only under the separate settings authorization.

Read back the rule and check PR #19 shows the required check with no missing-review
requirement. Record enforcement evidence; never test deletion/force push on main.
Any disposable enforcement-test branch/rule needs its own authorized setup.
Use squash when a merge is eventually approved; changing repository-wide merge
options is separate. These steps follow the official
[classic protection guide](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).
