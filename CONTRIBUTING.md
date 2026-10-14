# Contributing

Access is invitation-only pending the founder's license decision. Read
[AGENTS.md](AGENTS.md), [workflow](docs/engineering/git-workflow.md) and
[testing strategy](docs/engineering/testing.md).

Start from an issue with a problem, desired behavior, scope, dependencies,
acceptance criteria, tests, privacy considerations and Definition of Done. Use
one cohesive branch and PR per small outcome. Discuss architectural changes in
an ADR before implementing them. Preserve uncommitted work belonging to others.

Before requesting review, run applicable local checks and inspect the diff for
secrets, personal data, compatibility, authorization and misleading status claims.
Document test failures and unexecuted checks. Use synthetic fixtures only.

Use strict TypeScript once introduced, avoid `any`, and validate input at trust
boundaries. Components should not contain business rules or literal UI copy.
Use descriptive names, explicit error handling and redacted structured logs.
Breaking changes require migration, rollout and rollback plans.

The founder reviews every PR before squash merge. AI review is supplementary.
Never bypass failing checks or merge known critical vulnerabilities. Production
deployment, store publishing and sensitive changes require explicit approval.
