# Architecture overview

Status: Proposed; see [ADR-0001](../adr/0001-modular-monolith.md).

One universal Expo/React Native application, Expo Router and strict TypeScript
form the client. A modular monolith owns business rules. Supabase provides Auth,
PostgreSQL and private object storage. Privileged operations and AI execute on
the server. Background workers run independently of client application lifetime.
Hosting, worker runtime and package versions remain open decisions.

## Proposed repository layout

```text
apps/universal/            Expo app; route files are thin composition layers
  app/                    Expo Router routes and layouts
  src/features/           Identity, vault, tasks, contracts, settings UI
  src/platform/           Secure session storage, camera, push, file adapters
packages/domain/          Pure rules, value objects, permission decisions
packages/contracts/       Zod request/response schemas and error codes
packages/i18n/en/          English UI, notification and email resources
packages/ui/              Shared accessible components and theme tokens
server/                   Authorized use cases, provider adapters, job handlers
supabase/migrations/      Reviewed schema, grants, RLS and storage policy changes
supabase/tests/           SQL isolation and migration tests
tests/                    Synthetic fixtures, integration and E2E suites
docs/                     Product, architecture, security and delivery
scripts/                  Repository checks and developer utilities
```

Only `docs/`, `scripts/` and repository configuration exist in Phase 0. Do not
create empty runtime packages or install dependencies solely to imply progress.
Start with npm workspaces and one lockfile in Phase 1 if approved; extract a
package only when it gives a useful boundary. No microservice split is planned.

## Dependency rules

UI calls use cases through typed interfaces. Domain code imports no React,
Supabase, network or native SDK. Contracts validate wire data; persistence and
provider adapters implement ports. Server-only code must never be reachable from
the client dependency graph. Tests verify domain rules without devices or services.

## Data flow and trust boundaries

1. Client authenticates using Supabase Auth. Client route guards improve UX but
   never substitute for authorization.
2. Ordinary user reads/writes may use the Supabase API with user JWT and RLS.
   Complex mutations go through authenticated server use cases. Both use the
   same domain invariants; transactional invariants also live in the database.
3. Server verifies identity, active membership and resource ownership, validates
   input, then applies a transaction. Never trust a client-supplied workspace ID.
4. Upload intent binds a random object key, workspace, expected size/type and
   short expiry. File bytes land in private quarantine. A worker validates and
   scans before promotion; preview and extraction consume only accepted files.
5. Committed work emits an outbox job. Workers claim leases, recheck authorization
   and consent, use bounded retry/backoff and record a redacted outcome.
6. AI sees only authorized necessary content after consent and scan approval.
   Structured suggestions return for human review; no document can authorize tools.

Native session storage, camera capture, push registration and file selection use
platform adapters. Web session strategy must address XSS/CSRF and be validated
before implementation. Do not assume web storage matches native secure storage.

## Reliability and operations

Use transactional outbox, unique operation keys, leases with recovery, dead-letter
handling and job attempt limits. Delivery to an external provider is at-least-once;
do not claim exactly-once effects without provider idempotency/reconciliation.
Record accepted versus delivered notification outcomes separately. Use request/job
IDs and sanitized codes in logs, never documents, tokens or signed URLs.

Separate local, staging and production projects, storage and credentials. Preview
clients never point at production. Founder approval gates production migrations
and deployments. Schema changes use expand/migrate/contract and tested rollback
or forward-repair strategies. Backup restoration must include file bytes as well
as database metadata; see [release](../engineering/release.md).

## Tradeoffs and limits

Shared UI reduces duplication but camera, notifications, browser accessibility
and native lifecycle still need platform testing. RLS reduces accidental exposure
but privileged service credentials bypass normal boundaries. Managed services do
not establish compliance. A dedicated worker runtime may become necessary for
large OCR jobs; validate runtime limits before selecting it.
