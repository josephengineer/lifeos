# ADR-0002: Workspace isolation and private storage

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: Personal information must stay isolated, with future household/team
workspaces possible without a rushed multi-tenant retrofit.

Decision proposal: explicit workspace membership, non-null tenant keys, composite
foreign keys, default-deny RLS and private buckets. Start with personal owners
only. Reauthorize privileged use cases and job execution independently.

Alternatives: user_id-only ownership complicates future collaboration; a database
per user adds operational complexity; public object URLs violate the privacy goal.

Consequences: policy and cross-tenant negative tests become release gates.
Signed URLs have a bounded revocation window. Privileged service keys bypass RLS
and demand narrow exposure and explicit checks. No isolation is implemented yet.

Evidence: [database design](../architecture/database.md) and official Supabase
sources in [validation](../architecture/sources.md).
