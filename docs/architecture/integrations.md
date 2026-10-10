# Integration feasibility plan

All entries are Planned research. No OAuth connection or provider capability is
implemented or verified. Phase 6 or later unless explicitly approved for billing.

| Provider/channel | Candidate use | Required feasibility evidence |
| --- | --- | --- |
| Gmail | Selected email/attachment import, approved draft preparation | Read versus draft/send scopes, verification requirements, revocation |
| Outlook | Mail import and approved drafts | Microsoft Graph delegated scopes, tenant consent and licensing |
| Google Calendar | Read selected events, approved event writes | Least-privilege scopes, recurrence/time-zone mapping, duplicate handling |
| Microsoft Calendar | Selected calendar sync | Graph permissions, webhook expiry, conflict/retry behavior |
| Google Drive | User-selected document import | File selection scope, export formats, shared-file permissions |
| OneDrive | User-selected file import | Graph file scopes, personal/business differences |
| Dropbox | Selected file import | Scoped access, download constraints and revocation |
| Email forwarding | Inbound document capture | Sender spoofing, alias rotation, malware quarantine and abuse limits |
| Payment providers | Founder-approved subscriptions | Webhooks, refunds, taxes, entitlements and applicable storefront rules |
| Automation services | Approved workflow execution | Per-action scope, idempotency, audit evidence and cancellation limits |
| Open banking | Potential account-linked discovery | Availability, licensing/partner eligibility, jurisdiction and sensitive-data review |

For each provider, create a research issue with official URLs and verification
date, exact required scopes, sandbox proof, cost/limits, data destination, consent
screen, token lifecycle and failure scenarios. Never promise an API action merely
because a provider has an API. Store refresh tokens in server-side encrypted secret
storage with rotation; clients receive only connection status. Revoke tokens and
cancel queued work on disconnect. Webhooks reauthorize their linked workspace.

Default to user-selected imports. Bulk mailbox/file discovery requires separate
consent and a minimization review. Test with synthetic accounts; real personal data
must not go to a new provider without explicit founder approval and user consent.
