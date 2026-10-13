# ADR-0006: Workspace ownership and immutable document provenance

Date: 2026-10-10. Status: Proposed, decision-ready; founder approval pending.
Clarifies ADR-0002 and findings R02/R03. No database or storage implementation exists.

## Recommendation and ownership

A workspace owns its domain records. The user who uploads a document is its
creator, not an independent authorization owner. Keep `workspace.owner_user_id`
as the single accountable owner at launch and in the initial collaboration model.

For `type=personal`, require exactly one active owner membership matching
owner_user_id, one personal workspace per user and no invitations or ownership
transfer. Provision atomically and repair idempotently. Disallow direct client
changes to owner, type and memberships. Deletion of the owner is restricted until
the personal workspace's cleanup has completed.

Future family/business workspaces are separately created; never automatically
convert a personal workspace or reveal its existing records on an invitation.
The initial creator becomes accountable owner, but uploading does not grant an
independent right to administer the workspace. Business legal ownership/processor
obligations are separate from this technical account role and need future terms.

## Future permission model (Phase 6, not launch work)

| Role | Read | Create/update | Manage members | Transfer/delete workspace |
| --- | --- | --- | --- | --- |
| Owner | All workspace records | Yes | Yes | Reauthenticated, explicit workflow |
| Admin | All workspace records | Yes | Non-owner roles only | No |
| Editor | All workspace records | Yes; explicit delete permission defined per entity | No | No |
| Viewer | All workspace records | No | No | No |

This first shared-workspace model is intentionally visible to all its members:
no misleading claim of private items inside a shared space. Personal items remain
in separate personal workspaces. Advanced per-record business policies are a later
catalog capability requiring a new role/ACL design and negative tests.

Controlled sharing of a personal document uses explicit grants to authenticated
recipients (no anonymous public links). Proposed `document_grants` reference the
source workspace, document and recipient with read permission, expiry and revocation.
Only that document and its approved derived display artifacts are visible; grants
do not reveal source workspace listings, chats, sibling files or search indexes.
Initial grants are read-only; no transitive re-sharing. This is a Phase 6 proposal.

Revoking membership or a grant stops new authorized reads, downloads, retrieval and
jobs; previous downloads cannot be recalled. Cross-workspace moves are not an
in-place workspace_id update. An explicit copy reauthorizes source/destination,
creates new identities/provenance and explains retention of both copies. Sharing
does not transfer ownership. No global hash-based deduplication that leaks existence.

Owner transfer for a shared workspace is an atomic, reauthenticated transaction:
target is an active accepting member, owner_user_id and role memberships change
together, last-owner removal is rejected, audit recorded and risky queued actions
reauthorized. On account deletion, a sole shared-workspace owner must explicitly
transfer ownership or choose a separately confirmed workspace deletion before
account cleanup commits. Never cascade-delete other members' records implicitly.
Remove ordinary memberships and minimize creator attribution while retaining
workspace-owned records per approved retention/terms. Resolve those terms before
collaboration launch; no shared account-deletion policy is claimed as law.

## Original bytes and derived information

Every uploaded file has an immutable version with a random storage key and
server-computed digest/byte length. Initial intake is through the authenticated
gateway from ADR-0005. Untrusted quarantine is never previewed or sent to AI.
After upload completes, seal the bytes into a new server-only immutable key,
verify its digest, then scan that exact sealed version. Do not scan a mutable
upload key and later assume it still contains the same bytes. Only accepted
versions are eligible for serving, OCR or analysis. Scan metadata is server-owned.

Preserve originals byte-for-byte. OCR text, thumbnails, sanitized previews,
redacted exports, embeddings, structured fields and summaries are separate
artifacts referencing the immutable source version. OCR/AI workers can read
accepted originals and write only their derivative area through a narrow adapter;
they cannot overwrite, rename, promote or delete original objects. Broad service
credentials would defeat this boundary and are not permitted in extraction workers.

Human metadata edits and confirmed extracted fields are separate records and do
not rewrite file bytes. Reanalysis adds a versioned analysis run; never silently
overwrites user-confirmed facts. Replacing a document creates a new quarantined
file version and updates the current-version pointer only after acceptance. New
active suggestions target the new version; old results stay bound to their old
source, are excluded from current retrieval and are never relabeled as new evidence.
User-facing version-history UI can remain Phase 5 while internal provenance exists
from Phase 2. Account/source deletion removes originals and derivatives under the
approved retention policy: immutability is not indefinite or legally mandated retention.

## Proposed data constraints

| Entity | Required fields / constraints |
| --- | --- |
| workspaces | id, type, owner_user_id, status; FK owner deletion restricted; personal-owner partial uniqueness |
| memberships | workspace_id + user_id unique; role, status, revoked_at; transactional owner consistency |
| documents | workspace_id, id, created_by, current_version_id, title/lifecycle; workspace owns it, creator is attribution |
| document_versions | workspace_id, id, document_id, storage_key unique, sha256, byte_length, detected_mime, source_language, sealed_at, scan_status; content fields immutable |
| analysis_runs | workspace_id, id, document_version_id, provider/model/prompt/extractor versions, consent version, state, timestamps |
| derived_artifacts | workspace_id, id, analysis_run_id, source_version_id, kind, object/ref, digest; no original storage key reuse |
| extracted_fields | workspace_id, source_version_id, analysis_run_id, typed value, page/offset, uncertainty, review state |
| confirmed_fields | workspace_id, record/field, value, confirming actor/time, source_version_id when relevant; independent of extractor writes |
| document_grants | Phase 6 only: source workspace/document, recipient user, permission=read, expiry/revoked_at, granting actor |

All child relations enforce matching workspace and parent identifiers with
composite FKs, including document/current_version membership and artifact/run/source
consistency. Storage key naming is not authorization. Account-level profiles,
sessions/preferences and export/deletion requests remain user-scoped exceptions.

## Tests and alternatives

Phase 1: unique personal owner, duplicate/retried provisioning, mismatched owner
membership, owner spoofing and cross-account access. Phase 2: hash originals
before/after OCR/AI/manual confirmation; deny overwrite/promotion by clients and
workers; race upload/finalize/scan; mismatched derivative tenant/source; rescan and
replacement provenance; rejected-file exclusion; deletion sweeps and gateway reads.
Phase 6: full role matrix, grant expiry/revocation, source-listing denial, revoked
member jobs/search, owner transfer races, last-owner protection and shared deletion.

Alternatives: uploader-owned shared files complicate departure and business
continuity; implicit whole-workspace sharing exposes personal data; rewriting
originals loses evidence; object-store legal-hold/WORM introduces retention conflicts
and costs not justified for MVP. Recommend application-enforced immutability with
separate originals/derivatives and narrow roles. Privileged infrastructure operators
can still alter storage; no claim of regulatory WORM or cryptographic proof of truth.

Founder decision: accept this ownership/sharing/provenance model or revise it
before schema implementation. Later legal terms, role details and sharing UI remain
gated to their phases. [Database design](../architecture/database.md),
[privacy](../security/privacy.md) and [ADR-0005](0005-authentication-and-sessions.md)
define the adjacent boundaries.

## Operational costs and unresolved implementation decisions

Originals, versions and derivatives increase storage/backup size; scanning,
hashing and reanalysis consume worker time. Owner and composite-FK invariants add
migration/test complexity. Separate derivative storage and restricted workers are
deliberate security costs; deduplication must not weaken provenance or disclose
another tenant's content.

Phase 1 must choose transactional owner enforcement and provisioning recovery.
Phase 2 must define sealing/copy failure recovery, scanner limits, derivative
quotas, garbage collection and deletion manifests. Safe preview must sanitize
active content into a separate derivative; never execute original HTML/SVG or
active PDF in the application origin. Define MIME/nosniff and attachment behavior,
and validate the sandbox or isolated preview origin before enabling preview.
Scanning alone does not make browser rendering safe. Include malicious active
content and unsafe MIME fixtures in Phase 2 tests.

Before Phase 6, decide whether grants pin a version or follow replacements;
recommend pinned versions with explicitly renewed sharing to avoid exposing future
uploads. Specify display derivatives, copy/export rights, editor delete rights,
owner departure and retention terms. No advanced business ACL or legal retention
policy is implied by this proposal.
