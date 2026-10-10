# Database design

Status: Conceptual proposal; no migrations or tables have been created.

## Core model

| Entity | Key fields and relations | Initial phase |
| --- | --- | --- |
| profiles | user_id references auth identity; display name, time zone | 1 |
| workspaces | id, type=personal, owner_id, lifecycle state | 1 |
| memberships | workspace_id + user_id unique, role, revoked_at | 1 |
| preferences | user_id, theme, notification/AI preferences, locale=en | 1 |
| documents | id, workspace_id, owner_id, title, category, lifecycle | 2 |
| document_versions | id, workspace_id, document_id, object key, hash, size, scan state | 2 |
| extracted_fields | workspace_id, version_id, field key/value, source location, confidence, confirmation | 2 |
| tags/document_tags | workspace-scoped tag and document links | 2 |
| tasks | id, workspace_id, title, parent_id, due date/instant, status | 3 |
| reminders | id, workspace_id, task_id, zone, recurrence, next due instant | 3 |
| reminder_occurrences | reminder_id + occurrence key unique, delivery state | 3 |
| contracts | workspace_id, parties, dates, notice rules, amount, currency | 4 |
| subscriptions | workspace_id, billing interval, amount, currency, renewal, status | 4 |
| purchases/warranties | workspace_id, seller, purchase date, amount, warranty terms | 4 |
| assets/life_areas | workspace_id, label, category, related records | 4+ |
| record_links | workspace_id and explicit typed foreign keys to supported entities | 3+ |
| conversations/messages | workspace_id, user_id, retention and source references | 5 |
| integrations | workspace_id, provider, scope and consent; server-only token reference | 6 |
| action_proposals/approvals/executions | payload hash, approver, expiry, outcome and idempotency key | 7 |
| outbox_jobs | type, workspace_id, reference IDs, state, attempts, lease, next_attempt_at | 2+ |
| audit_events | scope type, workspace_id or account user_id, actor, action, target ID, time, redacted outcome | 1+ |
| export/deletion_requests | user_id, verified request, stage, retries, completion evidence | 4 |
| billing_accounts/entitlements | workspace_id, provider refs, plan, event version | 4 |

## Invariants

Workspace-owned domain rows have a non-null workspace ID. Account-level profiles,
preferences and account export/deletion requests instead use the authenticated
user ID and owner-only policies. Audit records declare account or workspace scope,
with a constraint requiring exactly the corresponding scope key. Never authorize
account records by a client-selected workspace. Unique `(workspace_id, id)` parent
keys and composite foreign keys prevent cross-workspace relationships.
Membership is queried from authoritative database state, not client claims.
One personal workspace per owner at launch uses a partial unique index; provisioning
identity/profile/workspace/membership is idempotent and transactionally consistent.
Invitation and role-management APIs do not exist until collaboration is approved.

Enable default-deny RLS on exposed tables and apply both read predicates and
write `WITH CHECK` constraints. Clients cannot mutate roles, owner IDs, billing
entitlements, scan/processing states, approved hashes or audit events. Test
anonymous, owner, other user, revoked member
and privileged job paths. Policies should avoid recursive membership lookups.
Any security-definer function gets fixed search_path, narrow grants and review.

Storage keys use random IDs under a workspace prefix, never identifying filenames.
Storage policies verify database access; a prefix alone is not authorization.
Membership revocation blocks new downloads; already issued signed URLs can remain
valid until expiry. Keep lifetimes short and document that residual risk.

Uploaded object versions are immutable after finalization. Clients cannot overwrite
or promote an accepted version. Finalization binds the exact server-verified bytes
and digest to a version; scan, preview and extraction all refer to that version.
Replacement creates a fresh quarantined version and requires a new scan. Test
overwrite attempts and changes between upload, scan and promotion; never trust a
client-supplied content hash or an editable accepted flag.

Use UUID identifiers, timestamptz for instants and `date` for date-only obligations.
Store an IANA zone plus recurrence definition where local wall time matters. Money
uses integer minor units with currency metadata; currencies need not have two
decimals. Do not aggregate currencies without an explicit conversion policy.

Confirmed and inferred values remain separate, with source version/page/offset,
extractor version and confirming actor/time. Derived data invalidates on source
replacement/deletion. Soft trash is not completed account deletion.

## Indexing, migrations and recovery

Index membership lookups, workspace/status/date listing and due job scans. Use
cursor pagination; introduce tenant-filtered full-text/semantic indexes only with
isolation tests. Add uniqueness for outbox/idempotency and provider event IDs.

Migrations must recreate a clean synthetic database, upgrade the previous schema,
validate constraints/RLS and rehearse destructive paths in staging. Document
rollback/forward repair for every breaking migration. Account cleanup must cover
rows, objects, extracted text, indexes, vectors, queues and provider-held content.
See [privacy](../security/privacy.md) for retention and backup caveats.
