# Testing strategy

Status: Foundation validation is implemented; application tests are planned.

## Layers and release evidence

| Layer | Scenarios | Gate |
| --- | --- | --- |
| Unit | Notice dates, recurrence/DST, currency/billing periods, classification mapping, permissions, AI schemas | Deterministic rules pass with boundary/error cases |
| Integration | Auth provisioning, user/tenant DB and storage, migrations, typed APIs, outbox leases, notification retries | Local isolated synthetic services and negative authorization evidence |
| E2E | Register/verify/login/logout/reset; upload/review; tasks/reminders; export/deletion; later billing sandbox | Browser and relevant native critical journeys pass |
| Security | Cross-tenant CRUD/search/jobs, malicious uploads, injection, session reset/revocation, webhook replay | No known critical issues; residual risks reviewed |
| Accessibility/platform | Keyboard, screen readers, dynamic text, themes, responsive layouts, deep links | Target platform evidence recorded for changed flows |
| Operations | Worker restart, provider outage, rate limits, restore, deletion retry, deployment recovery | Rehearsal proves approved operational targets |

For dates test month/year boundaries, leap years, DST gaps/overlaps, end-of-month
billing, user zone changes and date-only values. Pin clocks/time zones in tests.
For jobs inject failures before/after provider acceptance and lease expiry; verify
logical deduplication and unknown-outcome handling, not a false exactly-once claim.

Use synthetic fixtures only, deterministic seeds, isolated tenant identities and
provider test accounts. Never include real customer PDFs or production dumps.
Avoid implementation-mirroring tests and invented coverage thresholds. Choose
tools during Phase 1 (unit runner, React Native component tests, browser E2E and
native runner) after compatibility validation; do not pretend they run now.

## Evidence protocol

Each PR records command, revision, environment, result, relevant logs/artifacts and
limitations. Local pass is not remote CI pass; web export is not native build pass;
unit policy logic is not database RLS verification. Required failed checks block
merge. Flaky tests need an owner and repair; no silent blanket skipping.

## Foundation gate

The mandatory planned auth matrix is in
[ADR-0005](../adr/0005-authentication-and-sessions.md): native reinstall/storage,
CSRF, refresh/revoke races, direct-provider JWT bypass, idle/absolute expiry and
deletion_pending denial. The planned ownership/immutability matrix is in
[ADR-0006](../adr/0006-workspace-ownership-and-document-provenance.md): matching
personal owner, original-byte hash preservation across OCR/AI, extraction-worker
write denial, sealed-upload race tests, source/derived tenant FKs and future shared
role/grant/transfer/deletion cases. These are release requirements, not executed tests.

`python scripts/check_foundation.py` validates required artifacts, all 15 module
catalogs, feature IDs/statuses, source-vision traceability, local links and text
hygiene. `git diff --check` complements it. Mutation probes should demonstrate
failure for a broken link, missing feature entry and invalid feature status when
the validator is first introduced. These checks assess documents, not product code.
