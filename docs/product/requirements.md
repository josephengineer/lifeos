# Product requirements

Status: Planned. Owner: founder. Scope baseline: 2026-10-10.

## Launch outcome

An individual can authenticate, privately store and retrieve documents, maintain
important records, and receive reminders without relying on AI. Web, Android
and iOS are supported targets; parity must be verified on each platform.

## Commercial MVP boundary (Phases 1-4)

Include email authentication and verification, profile/settings, a personal
workspace, private PDF/image upload and management, metadata/text search,
reviewable OCR/classification, tasks and dependable reminders, manual contracts,
subscriptions, receipts/warranties, simple dashboard, export/deletion, onboarding,
operational monitoring and a founder-approved billing path. Ship AI processing
only after provider/privacy approval; its absence must not block manual paths.

Defer conversational/cross-document AI to Phase 5, shared workspaces and selected
integrations to Phase 6, consequential external workflows to Phase 7. No MVP
autonomous payments, bank connections, sensitive irreversible actions, custom
widgets or advanced business permissions. Features in the catalog assigned a
later phase are not promised at beta.

## Acceptance boundaries

- Users cannot read or modify another workspace via API, storage, search, jobs
  or guessed identifiers; prove this with negative integration tests.
- Recommended platform auth design is Supabase Auth behind the monolith BFF with
  server-managed sessions (ADR-0005); founder acceptance is pending. RLS remains
  enforced even for direct endpoints. Phase 1 includes the server session baseline.
- Personal workspace ownership is explicit and cannot be reassigned implicitly.
  OCR/AI produce separate derived records and never rewrite original file bytes
  (ADR-0006). Family/business sharing remains Phase 6.
- Uploads remain quarantined until validation; rejected files are not previewed
  or sent to OCR/AI. Manual categorization works during provider outages.
- Dates preserve date-only versus instant semantics; reminders survive closed
  apps, worker retries, time-zone changes and daylight-saving transitions.
- English localization covers every user-facing surface, including errors,
  emails, notifications and AI defaults. Document language is independent.
- Core screens support keyboard/screen-reader use, responsive layouts, light and
  dark themes, and consistent loading, empty, error and success states.
- Export/deletion, restore procedures and incident ownership are verified before
  public beta. No compliance or security marketing claims without review.
- Inferred fields include provenance and remain unconfirmed until reviewed.
  Annual subscription estimates disclose assumptions, currency and billing cycle.
- Warranty records distinguish seller/manufacturer promises from statutory rights.

## Proposed nonfunctional objectives

Set upload caps, availability, latency, job-delivery SLOs, RPO/RTO and retention
with the founder before implementation/release; see [decisions](../planning/decisions.md).
Measure redacted operation timings and failure counts. Prefer bounded pagination,
explicit rate limits, retry budgets, and recoverable errors. Offline editing and
sync conflict resolution are out of MVP scope; network failures must preserve
safe form state without silently claiming a server save.

## Traceability and changes

Every catalog capability has an ID, priority, phase, dependencies, story,
acceptance criterion and status. Issues reference these IDs. Scope changes need
founder agreement; architecture changes need an ADR. No timeline advances a phase
without its [release gate](../planning/roadmap.md).
