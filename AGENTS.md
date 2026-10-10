# Repository rules

- Read the relevant docs and inspect the working tree before editing. Phase 0 is
  documentation and engineering tooling only; major feature work needs approval.
- The founder owns scope and final decisions. State a short plan, dependencies,
  acceptance criteria and risks before implementation. Use small issues and PRs.
- Use a descriptive `codex/` feature branch, Conventional Commits and GitHub Flow.
  Never commit feature work to main, overwrite existing work or force-push.
- Request founder approval before merging, production deployment, store publishing,
  production deletion/destructive migrations, purchases, billing-rule changes,
  security-sensitive permission changes or sending real data to a new provider.
- Proposed stack: strict TypeScript, Expo/React Native/Router, Supabase, Zod,
  modular monolith. Confirm versions and uncertain APIs with official docs.
- Keep domain logic outside UI; isolate platform dependencies behind adapters.
  Validate trust boundaries, use typed contracts, explicit errors and migrations.
- Launch UI and end-user documentation are English. Centralize all UI, email,
  notification and assistant-default copy in localization resources. Uploaded
  document language is independent. Support accessibility, themes and state views.
- Enforce server-side permissions and workspace isolation. Use private storage,
  least privilege and synthetic fixtures. Never put server secrets in clients,
  logs, commits or PR text. Uploaded files and model outputs are untrusted.
- AI suggestions require provenance and confirmation. External actions separate
  proposal, approval, execution and verified outcome; no autonomous MVP payments.
- Add meaningful tests with implementation. Run applicable checks, inspect the
  diff and record exact evidence. Never imply CI/native builds/security passed
  without execution. No fabricated coverage or compliance claims.
- Keep feature IDs, status, roadmap and ADRs current. Distinguish Planned,
  In Development, Implemented, Verified, Released and Deprecated.
- Phase 0 checks: `python scripts/check_foundation.py` and `git diff --check`.
  Follow [testing](docs/engineering/testing.md) as code is introduced.
- A task is Done only after acceptance criteria, tests, CI, security review,
  English/localization checks, docs, review and required approved merge. Record
  blockers and limitations; generating files alone is not Done.
