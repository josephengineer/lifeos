# Open founder decisions

These are reviewable proposals, not assumed approvals. Continue documentation
work while decisions are pending; stop only dependent implementation or operations.

| ID | Decision | Recommended proposal | Needed before |
| --- | --- | --- | --- |
| D01 | Repository bootstrap | Approved and executed: empty main commit only, foundation branch push and draft PR; no merge approval | Completed bootstrap; PR review remains open |
| D02 | License and rights holder | Keep private/no open-source grant; confirm proprietary notice and ownership | External contributions/distribution |
| D03 | Stack and architecture | Accept proposed ADRs 0001-0006, including one universal Expo client and the monolith BFF; no implementation approval implied | Phase 0 architecture acceptance / Phase 1 implementation |
| D04 | Initial launch audience/regions | Individual adults first; choose jurisdictions and hosting region with privacy review | Provider provisioning/beta |
| D05 | Hosting/jobs/OCR | Validate runtime limits and scanning options in a spike; approve costs separately | Phase 2 pipelines |
| D06 | AI provider/data use | Opt-in scoped processing; approve provider, region, retention and terms | Any real data sent to AI |
| D07 | Retention/deletion | Define trash, log, backup, conversation and deletion windows; legal review where needed | Personal-data beta |
| D08 | Billing and store approach | Validate tiers/quotas/prices and current store rules before integrating | Billing implementation/activation |
| D09 | GitHub protection/review | GitHub currently requires an upgrade for private protection/rulesets; choose eligible plan + separately approved zero-reviewer protection, or explicitly accept manual Phase 0 governance risk | Before Phase 0 merge |
| D10 | Native signing/build spending | Founder-controlled accounts, isolated credentials, explicit build budget | EAS/native distribution |
| D11 | Reliability targets | Agree reminder SLO, availability, RPO/RTO, upload caps and rate limits | Implementation acceptance/beta |
| D12 | Brand/accessibility | Approve design direction; target accessible English-only launch | Shared UI components |
| D13 | Support/security ownership | Confirm reporting contact, incident owner and emergency authority | Public beta |
| D14 | Phase 1 scope | Approve ordered backlog without starting later modules | Application scaffolding |
| D15 | Authentication/session architecture | Accept ADR-0005: opaque platform sessions, server-only Supabase tokens, RLS session gates; proposed 10-minute JWT / 7-day idle / 30-day absolute / 5-minute reauth | Phase 0 decision; Phase 1 implementation/test gate |
| D16 | BFF hosting/key management | Approve design direction now; select compatible hosting, encrypted token storage and streaming limits in P1-01 before implementation or purchases | Phase 1 server baseline |
| D17 | Ownership and provenance | Accept ADR-0006 single accountable owner, separate personal/shared spaces, immutable originals and versioned derivatives | Phase 0 decision; schema gate |

Commercial prices, legal compliance, integration availability and security assurance
are explicitly unresolved. No paid purchase, deployment, permissions change or
production operation is authorized by these proposals alone.
