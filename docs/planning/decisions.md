# Open founder decisions

These are reviewable proposals, not assumed approvals. Continue documentation
work while decisions are pending; stop only dependent implementation or operations.

| ID | Decision | Recommended proposal | Needed before |
| --- | --- | --- | --- |
| D01 | Repository bootstrap | Approved and executed: empty main commit only, foundation branch push and draft PR; no merge approval | Completed bootstrap; PR review remains open |
| D02 | License and rights holder | Keep private/no open-source grant; confirm proprietary notice and ownership | External contributions/distribution |
| D03 | Stack and architecture | Accept ADRs 0001-0004, Expo + Supabase modular monolith | Phase 1 implementation |
| D04 | Initial launch audience/regions | Individual adults first; choose jurisdictions and hosting region with privacy review | Provider provisioning/beta |
| D05 | Hosting/jobs/OCR | Validate runtime limits and scanning options in a spike; approve costs separately | Phase 2 pipelines |
| D06 | AI provider/data use | Opt-in scoped processing; approve provider, region, retention and terms | Any real data sent to AI |
| D07 | Retention/deletion | Define trash, log, backup, conversation and deletion windows; legal review where needed | Personal-data beta |
| D08 | Billing and store approach | Validate tiers/quotas/prices and current store rules before integrating | Billing implementation/activation |
| D09 | GitHub protection/review | Verify plan; approve main protections and eligible reviewer arrangements | Integration and merge |
| D10 | Native signing/build spending | Founder-controlled accounts, isolated credentials, explicit build budget | EAS/native distribution |
| D11 | Reliability targets | Agree reminder SLO, availability, RPO/RTO, upload caps and rate limits | Implementation acceptance/beta |
| D12 | Brand/accessibility | Approve design direction; target accessible English-only launch | Shared UI components |
| D13 | Support/security ownership | Confirm reporting contact, incident owner and emergency authority | Public beta |
| D14 | Phase 1 scope | Approve ordered backlog without starting later modules | Application scaffolding |
| D15 | Session revocation boundary | Select and test enforcement for issued JWTs on APIs, direct DB/storage and client caches; do not assume sign-out instantly invalidates access tokens | P1-10 and identity release gate |

Commercial prices, legal compliance, integration availability and security assurance
are explicitly unresolved. No paid purchase, deployment, permissions change or
production operation is authorized by these proposals alone.
