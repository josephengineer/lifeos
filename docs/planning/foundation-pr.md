# docs: establish LifeOS product and engineering foundation

Closes #1.

LifeOS starts with an empty repository and a broad product brief. This change
adds a reviewable Phase 0 baseline: full feature traceability, phased scope,
architecture/security/privacy proposals, repository conventions and an ordered
Phase 1 backlog. It introduces a working documentation validator and a minimal
pinned, read-only GitHub Actions workflow.

No product runtime, cloud resources, billing rules, deployments or license grants
are introduced. All product features remain Planned. See
[verification](../engineering/verification.md) for exact executed checks and limitations.

Review [founder decisions](decisions.md), especially architecture, bootstrap,
licensing, private-repository protection availability and human approval ownership.
The repository needs an approved initial base commit before this PR can be opened.

Security: no secrets or real user data; CI does not receive secrets or deploy.
Rollback: reverting the foundation commit removes documents/tooling only, with
no database or production effects. Founder approval is required before merge.
