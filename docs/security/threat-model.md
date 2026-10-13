# Security threat model

Status: Planned controls, not a security assessment. Owner: engineering; risk
acceptance: founder. Review each new trust boundary and before beta.

## Assets, actors and boundaries

Protect document bytes/text, identity/session credentials, financial metadata,
reminder details, conversations, integration tokens, approvals and audit evidence.
Actors include legitimate users, other tenants, malicious uploaders, compromised
accounts, providers and privileged operators. Boundaries run between client/Auth,
API/database, object storage/worker, worker/AI and integrations/external effects.
Client code, documents, provider callbacks and model output are untrusted.

| Threat | Proposed control | Required verification | Residual risk |
| --- | --- | --- | --- |
| Cross-tenant reads/writes or guessed IDs | RLS, server checks, composite tenant FKs | Two-user CRUD/storage/search/jobs denial tests | Privileged service paths can bypass RLS |
| Session theft/account takeover | ADR-0005 BFF, opaque platform handles, server token vault, active-session RLS gates, reauth and rate limits | CSRF, expiry, refresh/revoke races, direct JWT bypass, reset replay and native reinstall | Compromised device/browser/server and in-flight operations remain risks |
| Privilege escalation | No client membership/role writes, narrow grants | Crafted role/owner/workspace mutation tests | Operator credentials require separate governance |
| Public or leaked document access | Private buckets, authenticated gateway streams, ADR-0006 workspace/grant checks | Anonymous and cross-tenant denial, revoked-session/member/grant reads | Previously downloaded bytes cannot be revoked |
| Malicious PDFs/images, decompression bombs or bytes swapped after scan | Size/type/signature limits, quarantine, immutable finalized versions, scanner, resource-bound parsers | Mismatch, oversized, malformed, scanner-failure and post-scan overwrite fixtures | New parser exploits; scanner is not a guarantee |
| Prompt injection/data exfiltration | Scope before retrieval, no document authority, tool allowlists | Multilingual malicious files and forged citation tests | Model errors and incomplete detection |
| Forged approval or duplicate action | Immutable approval hash, reauth, idempotency, reconciliation | Altered payload, expiry and timeout/retry tests | Some providers lack strong idempotency |
| SSRF via files/model/provider URLs | Approved destinations, bounded fetch, private-network denial | Redirect, loopback and metadata-host tests | DNS/provider changes need ongoing review |
| XSS/CSRF and unsafe previews | No raw active HTML; safe rendering, web session strategy, CSRF controls as applicable | Malicious text/filename/preview and session-flow tests | Browser extension compromise |
| Secret or personal-data leakage | Server-only secret stores, log allowlists, secret scanning | Bundle/log/commit inspection and negative fixtures | Operators and support exports need training |
| Denial of service/cost abuse | Quotas, rate/size limits, backpressure, bounded AI/job budgets | Load and retry-storm tests | Distributed abuse requires monitoring |
| Forged webhook/paid entitlement | Signature validation, event deduplication, server-only updates | Replay, stale and invalid-signature tests | Provider outage/delayed events |
| Lost data or incomplete deletion | Backup/restore exercises, lifecycle manifests, retried cleanup | Restore bytes+metadata; deletion sweep across derivatives | Backup expiration delays and provider retention |
| Dependency/CI compromise | Lockfiles, action SHA pins, minimal token permissions, review | Audit, pin verification, no secrets on PRs | Unknown upstream compromise |

## Release and response gates

No known critical vulnerabilities at merge/release. Triage high findings and
record owner, mitigation, deadline and founder acceptance before release. No
blanket audit suppression. Require tenant isolation evidence, upload rejection,
log redaction, secret separation and restore/deletion exercises before beta.

Require encrypted transport and verify provider encryption-at-rest configuration
and backup handling. Do not claim end-to-end encryption: server-side OCR/AI needs
access to plaintext. Do not describe the system as production-secure or compliant
based on these plans. Data region, scanner, token storage, session strategy and
incident notification obligations remain open decisions.

ADR-0005/0006 are recommended designs awaiting founder acceptance. A server token
vault creates a concentrated credential target and the no-cache session gate adds
availability/latency costs. Benchmark and review secret-table grants, key rotation,
RLS helpers and worker credentials before implementation is considered Verified.
