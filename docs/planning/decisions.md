# Open founder decisions

These are reviewable proposals, not assumed approvals. Continue documentation
work while decisions are pending; stop only dependent implementation or operations.

| ID | Decision | Recommended proposal | Needed before |
| --- | --- | --- | --- |
| D01 | Repository bootstrap | Approved and executed: empty main commit only, foundation branch push and draft PR; no merge approval | Completed bootstrap; PR review remains open |
| D02 | License and rights holder | Repository public by founder choice; no open-source license selected; confirm ownership and public business-document scope | External contributions/distribution |
| D03 | Stack and architecture | ADRs 0001-0004 remain Proposed; ADR-0005 goals conditionally approved, final architecture pending; ADR-0006 principles approved with component gates | Accept documentation deferrals before Phase 0 merge; approve implementation scope separately |
| D04 | Initial launch audience/regions | Individual adults first; choose jurisdictions and hosting region with privacy review | Provider provisioning/beta |
| D05 | Hosting/jobs/OCR | Validate runtime limits and scanning options in a spike; approve costs separately | Phase 2 pipelines |
| D06 | AI provider/data use | Opt-in scoped processing; approve provider, region, retention and terms | Any real data sent to AI |
| D07 | Retention/deletion | Define trash, log, backup, conversation and deletion windows; legal review where needed | Personal-data beta |
| D08 | Billing and store approach | Validate tiers/quotas/prices and current store rules before integrating | Billing implementation/activation |
| D09 | GitHub protection/review | Founder selected public repository/GitHub Free; protection active on 2026-10-14 with required PR/CI/strict/no-force/no-delete/admin enforcement; zero approvals and signatures disabled verified by subsequent API readback | Enable/verify approved protection before merge; no manual exception accepted |
| D10 | Native signing/build spending | Founder-controlled accounts, isolated credentials, explicit build budget | EAS/native distribution |
| D11 | Reliability targets | Agree reminder SLO, availability, RPO/RTO, upload caps and rate limits | Implementation acceptance/beta |
| D12 | Brand/accessibility | Approve design direction; target accessible English-only launch | Shared UI components |
| D13 | Support/security ownership | Confirm reporting contact, incident owner and emergency authority | Public beta |
| D14 | Phase 1 scope | Approve ordered backlog without starting later modules | Application scaffolding |
| D15 | Authentication/session architecture | Security goals conditionally approved. Recommend official SDK first; founder still decides web token exposure/persistence, timeout semantics/values and final architecture after evidence; custom session system needs concrete necessity | Final auth approval before implementation; research requires Phase 1 authorization |
| D16 | Auth feasibility and operations | P1-01/18 validates SDK storage/session checks, recovery, latency and costs; custom gateway/vault hosting only if justified and separately approved | Before dependent auth implementation or purchase |
| D17 | Ownership and provenance | Principles approved: explicit ownership/isolation, immutable originals, separate derivatives, provenance, server authorization and retention/deletion; exact schema/threat/test and policy gates remain | Per-component design before coding; executed tests before verification |

Commercial prices, legal compliance, integration availability and security assurance
are explicitly unresolved. No paid purchase, deployment, permissions change or
production operation is authorized by these proposals alone.
