# ADR-0002: Workspace isolation and private storage

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: Personal information must stay isolated, with future household/team
workspaces possible without a rushed multi-tenant retrofit.

Decision proposal: explicit workspace membership, non-null tenant keys, composite
foreign keys, default-deny RLS and private buckets. Start with personal owners
only. Reauthorize privileged use cases and job execution independently. ADR-0005
specifies session gates; ADR-0006 specifies single accountable ownership, grants
and immutable original/derived file separation. These proposals supplement this ADR.

Alternatives: user_id-only ownership complicates future collaboration; a database
per user adds operational complexity; public object URLs violate the privacy goal.

Consequences: policy and cross-tenant negative tests become release gates.
Initial gateway streams avoid reusable signed URLs; any later signed capability
has a bounded revocation window requiring a new review. Privileged service keys bypass RLS
and demand narrow exposure and explicit checks. No isolation is implemented yet.

Evidence: [database design](../architecture/database.md) and official Supabase
sources in [validation](../architecture/sources.md).
