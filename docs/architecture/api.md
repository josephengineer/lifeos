# API design

Status: Proposed interface contracts; no endpoints are implemented.

Use versioned JSON contracts for custom server APIs, validated with Zod on entry
and for untrusted provider responses. All Expo clients use the monolith API/BFF;
server user-scoped data adapters remain subject to RLS. Use cookie+CSRF for web
and an opaque SecureStore bearer handle for native, never browser/mobile Supabase
refresh tokens. See [ADR-0005](../adr/0005-authentication-and-sessions.md).

| Proposed operation | Authorization and behavior |
| --- | --- |
| POST /v1/auth/register, /login, /recover | BFF calls Supabase Auth; bounded/rate-limited, non-enumerating, web login CSRF protection |
| POST /v1/auth/callback, /reauthenticate | Bound single-use callback or fresh credentials; rotate opaque handle |
| POST /v1/auth/logout, /logout-all | Commit app revocation before provider cleanup; all-device path requires fresh reauth |
| GET /v1/auth/session | Safe session state only; no provider tokens; expired/revoked session denied |
| GET /v1/me | Current identity only; profile and accessible personal workspace |
| PATCH /v1/me/preferences | Allowlisted fields, locale=en, validated time zone |
| POST /v1/workspaces/:id/upload-intents | Active membership, quota/type/size bounds, one-use gateway intake ID, no storage bearer URL |
| POST /v1/workspaces/:id/uploads/:intent | Bounded authenticated byte intake into quarantine; seal before scan |
| POST /v1/workspaces/:id/documents/:doc/finalize | Ownership, actual object verification, enqueue quarantine job |
| GET /v1/workspaces/:id/documents/:doc/download | Reauthorize accepted version and stream bytes through gateway; no-store |
| POST /v1/workspaces/:id/tasks | Validate dates, linked records and workspace FKs |
| POST /v1/me/exports | Recent reauthentication, rate limit, async status |
| POST /v1/me/deletion-requests | Recent reauthentication, explicit confirmation, staged cleanup |
| POST /v1/workspaces/:id/assistant/queries | AI consent and scope, quotas, cited answer or abstention |
| POST /v1/actions/:id/approvals | Exact immutable proposal version, eligible approver, expiry |
| POST /v1/actions/:id/execute | Valid approval, reauthorization, duplicate prevention |

All custom operations resolve actor from verified session, never payload user_id.
Bound field lengths, arrays, page sizes, request bytes and timeouts. Use stable
error codes and request IDs: `VALIDATION_FAILED`, `UNAUTHENTICATED`, `NOT_FOUND`,
`CONFLICT`, `RATE_LIMITED`, `PROVIDER_UNAVAILABLE`. Do not leak cross-tenant
existence through resource errors. Map errors to English localization at clients.

Proposed success envelope: `{ "data": {...}, "requestId": "..." }`.
Error envelope: `{ "error": { "code": "..." }, "requestId": "..." }`.
List responses include `nextCursor`; cursors are scoped to query and workspace.
Asynchronous operations return 202 and a scoped status resource; acceptance is
not completion. Mutations use operation/idempotency keys where retries can
duplicate effects. Bind stored keys to actor, workspace and request hash; reuse
with a different payload returns conflict. Concurrency-sensitive updates use
record versions to prevent silent overwrites.

Webhooks require provider signature/timestamp validation, replay deduplication
and transactional event recording before acknowledging. Billing entitlements
derive from verified events; clients cannot set paid status. Provider-specific
signature rules and retry windows require current documentation at implementation.

Record contract compatibility and migration paths. Prefer additive evolution;
breaking clients require version overlap and retirement communication. Never log
authorization headers, signed URLs, raw files or request bodies with personal data.
