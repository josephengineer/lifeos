# Privacy and data processing design

Status: Proposal for product/technical review, not a legal compliance opinion.
Jurisdiction, hosting region, processor contracts and legal basis need qualified
review before public release. No real user data has been processed by this project.

| Data class | Purpose and access | Retention/deletion proposal |
| --- | --- | --- |
| Identity/profile | Account operation; account holder and constrained services | Active account; erase or minimize through verified deletion |
| Documents/metadata | User storage and administrative records; workspace-scoped | User-controlled active/trash lifecycle; trash window pending approval |
| OCR/extractions/vectors | Optional search/AI assistance; scoped workers | Delete/invalidate with source and applicable AI preference changes |
| Tasks/reminders/device tokens | Scheduling and delivery | User lifecycle; expire invalid device tokens and obsolete deliveries |
| Conversations | User-requested assistance/history | User-controlled deletion, independent retention choice |
| OAuth tokens | Authorized integrations only | Revoke and remove on disconnect, expiry or account deletion |
| Audit/operational logs | Security, debugging and reliability | Minimum redacted records; window and access policy pending approval |
| Billing records | Subscription administration | Jurisdiction-specific obligations; segregate required retained records |
| Backups | Recovery | Bounded approved expiry; deletion ledger reapplied on restore |

Collect only needed fields. Avoid unnecessary health, identity-number or family
details. Documents may contain sensitive information; do not send content to
analytics, logs or providers by default. Push/email notifications should use
generic previews unless the user chooses more detail. Do not infer document
language from the English application locale.

Before AI/integration processing, explain purpose, provider, transmitted fields,
retention, region and controls. Record consent/preferences versions and recheck
them when a job runs. Provider terms, training use and deletion support must be
verified independently. Opt-out must preserve manual product functionality.

## Export workflow

Reauthenticate -> authorize request -> create scoped snapshot job -> include
document originals and machine-readable metadata/relationships -> deliver through
expiring authenticated access -> expire artifact. Protect against export link
leakage and exclude other members' private items. Document partial failures.

## Deletion workflow

Reauthenticate and confirm -> mark account deletion pending -> stop new processing
and revoke sessions/integrations -> inventory rows, objects, versions, text,
vectors, chats, queues and exports -> delete or segregate legally retained records
-> retry failures -> verify manifest -> confirm outcome. Clarify billing cancellation
and retained receipts before final confirmation. Define any reversal window before
implementation. Never report success while cleanup is still incomplete.

Backups may retain deleted records until expiry. Explain this to users, prevent
normal access and reapply deletion records after restore. Third-party deletion
must be tracked separately. Final retention periods, response targets, residency
and processor agreements are founder/legal decisions, not fabricated defaults.
