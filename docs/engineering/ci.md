# Continuous integration design

## Implemented Phase 0 workflow

`.github/workflows/foundation.yml` runs on pull requests, main/codex pushes and
manual dispatch. It grants contents:read only, disables persisted checkout
credentials, pins checkout to a full commit SHA, sets a timeout and cancels stale
runs. It runs the dependency-free repository validator and whitespace check.
The hosted runner provides Python; the validator requires 3.11+. No secrets or
application dependencies are needed. Dependabot tracks action updates weekly.

The pin must be verified against the official action repository; review updates
before merging. Never use pull_request_target to execute untrusted PR code with
secrets. No deployment or publishing runs in this workflow.

## Phase 1 additions (required with the app)

| Check | Implementation requirement |
| --- | --- |
| Dependency installation | Pin Node/npm; commit lockfile; use npm ci and fail on mismatch |
| Formatting | Enforce chosen formatter across TS/JSON/Markdown |
| Lint | Include hooks/import boundaries and localization rules |
| Type checking | tsc with strict configuration, no emit |
| Unit tests | Run real domain/component suites; no pass-with-no-tests flag |
| Integration | Local isolated Supabase migrations/RLS/auth tests when those are introduced |
| Vulnerabilities | Audit production and development dependencies; triage high findings, block critical |
| Web build | Execute actual Expo web export and retain useful failure evidence |
| Security | Secret scanning plus bundle/server-boundary checks; supported dependency review |
| Native | Actual Android/iOS builds and smoke evidence at platform gates, costs/signing approved |

Add npm Dependabot entries only when manifests exist. Required status names must
match real jobs. Do not add skipped/no-op app jobs merely to make branch protection
appear comprehensive. E2E and costly platform builds can run on release candidates
or selected PRs while critical deterministic checks remain required on every PR.

Avoid credentials for untrusted PRs. Keep staging/production environments separate,
use minimal scoped credentials only for explicitly approved release jobs and retain
redacted artifacts for an approved period. External action availability, plan
restrictions and spending are validation tasks, not assumed capabilities.
