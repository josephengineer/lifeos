# LifeOS

Your life. Organized. Simplified.

LifeOS is a planned personal life administration product for web, Android and iOS.
It will help individuals organize documents, agreements, subscriptions, purchases
and responsibilities, with optional AI assistance. Manual workflows must remain
useful when AI is unavailable.

## Current state

Phase 0 engineering foundation, prepared for founder review. No application,
database, authentication, AI, billing or deployment exists yet. Local documentation
checks are available; see the verification record and PR checks for remote CI.
Native builds and application tests have not run.
All product features are **Planned**. ADR-0005 objectives are conditionally approved;
its implementation is undecided. ADR-0006 principles have implementation gates.

## Start here

- [Documentation index](docs/README.md)
- [Product requirements](docs/product/requirements.md)
- [Complete feature catalog](docs/product/feature-catalog.md)
- [Architecture proposal](docs/architecture/overview.md)
- [Ordered Phase 1 backlog](docs/planning/phase-1-backlog.md)
- [Founder decisions](docs/planning/decisions.md)
- [Verification record](docs/engineering/verification.md)

## Verify the foundation

Use Python 3.11 or newer. No packages, credentials or service accounts are needed.

```text
python scripts/check_foundation.py
git diff --check
```

Read [setup](docs/engineering/setup.md), [CONTRIBUTING](CONTRIBUTING.md) and
[AGENTS](AGENTS.md) before working. CI currently checks repository structure,
local documentation links, text hygiene and feature traceability. Application
lint, type checking, tests and builds will be introduced with the application.

## Repository and licensing

The founder made [this repository](https://github.com/josephengineer/lifeos) public.
GitHub Free supports the intended protection, but main is not yet protected; see
[public review](docs/engineering/public-repository-review.md).
No open-source license is granted. Licensing and ownership notices await founder
confirmation; see [decisions](docs/planning/decisions.md). Do not upload secrets,
production data or real customer documents. Report security concerns using
[SECURITY.md](SECURITY.md).
