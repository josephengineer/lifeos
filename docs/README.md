# Documentation index

These are initial proposals as of 2026-10-10, not implemented product behavior.
The [verification record](engineering/verification.md) separates local evidence
from pending GitHub and product work.

## Product

- [Vision](product/vision.md)
- [Requirements and MVP scope](product/requirements.md)
- [Full feature catalog](product/feature-catalog.md)
- [User stories and acceptance conventions](product/user-stories.md)
- [Design system](product/design-system.md)

## Architecture and security

- [Architecture overview](architecture/overview.md)
- [Database design](architecture/database.md)
- [API design](architecture/api.md)
- [AI architecture](architecture/ai.md)
- [Official-source validation](architecture/sources.md)
- [ADR index](adr/README.md)
- [Threat model](security/threat-model.md)
- [Privacy and data processing](security/privacy.md)
- [Integration feasibility plan](architecture/integrations.md)

## Delivery

- [Roadmap and phase gates](planning/roadmap.md)
- [Ordered Phase 1 backlog](planning/phase-1-backlog.md)
- [Created GitHub issues](planning/github-backlog.md)
- [Open founder decisions](planning/decisions.md)
- [Phase 0 issue](planning/phase-0-issue.md)
- [Prepared PR description](planning/foundation-pr.md)
- [Development setup](engineering/setup.md)
- [Git workflow and GitHub protections](engineering/git-workflow.md)
- [Testing strategy](engineering/testing.md)
- [CI design](engineering/ci.md)
- [Release, rollback and incidents](engineering/release.md)
- [Verification record](engineering/verification.md)
- [Post-creation PR review](engineering/foundation-review.md)
- [Solo-founder GitHub governance](engineering/github-governance.md)
- [Final Phase 0 readiness report](engineering/phase-0-readiness.md)
- [Final Phase 0 approval checklist](engineering/phase-0-approval-checklist.md)
- [Current project status](../PROJECT_STATUS.md)
- [Public repository security review](engineering/public-repository-review.md)

- [Proposed Phase 1 implementation sequence](planning/phase-1-proposal.md)

- [P1-01 toolchain research and blockers](research/p1-01-toolchain.md)

## Status vocabulary

| Status | Evidence required |
| --- | --- |
| Planned | Catalog entry and agreed future scope; no implementation claim |
| In Development | Linked issue and active branch/PR |
| Implemented | Code exists and implementation acceptance is recorded |
| Verified | Relevant executed tests and CI evidence, reviewed controls |
| Released | Approved deployment/version and post-release evidence |
| Deprecated | Replacement, migration and retirement plan |

Delivery status is distinct from issue-board status. Done requires the full
Definition of Done, including approved merge when required. No feature is
Verified merely because its documentation passed validation.
