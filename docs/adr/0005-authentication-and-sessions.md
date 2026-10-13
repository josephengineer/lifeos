# ADR-0005: Supabase Auth with server-managed application sessions

Date: 2026-10-10. Status: Proposed, decision-ready; founder approval pending.
Resolves the design proposal for D15; complements ADR-0001/0002. Nothing here
is implemented or security-verified. Accepting this ADR does not start Phase 1.

## Context and recommendation

LifeOS handles private documents on web, Android and iOS. Issued JWTs are not
inherently revoked by clearing a client session. A common authorization boundary
is preferable to three subtly different revocation policies.

Recommend a backend-for-frontend (BFF), implemented as the API module of the
existing modular monolith. All three Expo clients authenticate and access private
data through it. Supabase Auth remains the identity/password/verification provider.
Supabase access and refresh tokens stay encrypted on the server. Clients receive
only opaque, revocable LifeOS session credentials. This is not a new frontend,
microservice fleet or replacement identity provider. No custom password database.

Web can remain an Expo static export with same-origin `/api` routing to the BFF;
SSR is not required. Native clients use that API over TLS through platform adapters.
Select hosting, key management and request/upload limits in the Phase 1 spike
before committing to a provider or paid resource (D16).

## Alternatives

| Option | Advantages | Tradeoffs / reason not recommended |
| --- | --- | --- |
| Browser/native Supabase SDK with direct JWT access | Fewest server components; native SDK refresh support | Browser JS can access persistent credentials; direct API/storage revocation must be enforced everywhere; more token transport variants |
| Web BFF; native Supabase tokens in SecureStore | HttpOnly browser protection; familiar native SDK | Two refresh/revocation protocols and larger negative-test matrix |
| BFF and opaque sessions on all platforms (recommended) | One session gate, no Supabase refresh tokens on devices, server-controlled revocation | Additional latency, session database/key-management work, server availability dependency and a concentrated credential target |

A conventional Supabase SSR client with browser-readable cookies is not equivalent
to this BFF. The BFF must own the token exchange/refresh path; do not merely add
HttpOnly to cookies that the browser SDK expects to refresh.

## Platform storage and transport

| Platform | Stored credential | Required handling |
| --- | --- | --- |
| Web | Opaque `__Host-lifeos_session` cookie | Secure, HttpOnly, SameSite=Lax, Path=/, no Domain; no session tokens in localStorage/sessionStorage/IndexedDB; TLS outside explicitly isolated local development |
| Android | Opaque LifeOS bearer credential in Expo SecureStore | Platform-protected storage, backup exclusion, no AsyncStorage or logs; memory-only copy while sending API calls |
| iOS | Opaque LifeOS bearer credential in Expo SecureStore | Keychain with WHEN_UNLOCKED_THIS_DEVICE_ONLY where supported; no cloud migration of session; clear surviving credentials on detected fresh install |
| Server | Encrypted Supabase access/refresh pair | Restricted secret table, encryption key outside DB, versioned key rotation, no tokens in logs/backups in plaintext; only session service decrypts |

Native secure storage failure means reauthentication, never fallback to plaintext.
Reinstall behavior and backup exclusions require device tests; secure storage does
not protect a fully compromised device. No mandatory biometric binding initially;
optional local app locking is a separate future decision. The session handle is
a bearer secret even though it is opaque. Do not place it in deep links or URLs.

Generate 256-bit random handles and store only their cryptographic digest in the
session index. Rotate on login, reauthentication and privilege/security events.
Invalidate the old handle atomically. Browser cookies are sent automatically, so
unsafe methods (including login/logout) require Origin checks and a session-bound
CSRF token; protect pre-login flows with a separate short-lived challenge. SameSite
and CORS are supplemental, not authorization. Native bearer routes do not accept
cookie authentication; reject requests supplying conflicting credential modes.

Use restrictive CSP and no sensitive response caching (`Cache-Control: no-store`).
Avoid third-party scripts on authenticated web surfaces. HttpOnly reduces token
exfiltration but cannot stop XSS from acting through the victim's browser.

## Sign-in, registration and recovery

The BFF validates/rate-limits English-localized forms and calls Supabase Auth over
TLS with a per-request client. Never log passwords, callback codes or session data.
Only a verified identity can activate an ordinary LifeOS session. Create its
personal workspace through idempotent provisioning before returning private data.
Rate limits cover credential stuffing, signup, resend and reset; errors do not
enumerate accounts.

Use PKCE/state-bound, exact-allowlisted callbacks where a code-exchange flow is
supported. Verification/reset callbacks are short-lived and single-use. Recovery
authorization is restricted to password reset, not general data access. On success,
invalidate existing application sessions and require a fresh login. A native
callback transfers a one-use, short-lived completion code bound to the initiating
challenge, not tokens; prefer verified universal/app links. No arbitrary redirects.
Validate the exact Supabase exchange APIs in the Phase 1 spike. Social providers
remain cataloged for later scope and must not silently link accounts by email.

## Proposed lifecycle policy (part of the approval request)

| Event / bound | Proposed behavior |
| --- | --- |
| Access-token expiry | Configure Supabase JWT lifetime to 10 minutes after validating platform/provider support; signature, issuer, audience, expiry, subject and session_id are checked |
| Refresh | BFF refreshes shortly before expiry, with one distributed refresh operation per Supabase session; atomically persist the rotated pair using version checks |
| LifeOS idle / absolute expiry | 7 days without foreground user activity / 30 days since sign-in; enforce in DB on every access, not only cleanup jobs; background refresh/jobs do not extend them |
| Sensitive reauthentication | Verified credentials within 5 minutes for export, deletion, global logout, ownership transfer and connecting sensitive services; rotate handle and bind action to current session |
| Current-device logout | Commit revocation first, then revoke the corresponding provider session/refresh capability and clear client storage/caches; repeated logout is safe |
| All-device logout / compromised account | Increment account auth_version, revoke all app sessions, invalidate provider refresh sessions and cancel unapproved external execution |
| Refresh failure | Invalid/reused refresh credentials close the session; transient provider failure returns a recoverable unavailable state without treating the user as authorized indefinitely |
| Account deletion | Reauthenticate, atomically mark deletion_pending and bump auth_version, deny data/refresh, queue provider revocation and cleanup; never report completed deletion before verification |

Refresh locks plus compare-and-swap must prevent a response racing with revocation
from reactivating a session. Check account status, auth_version and revoked_at
again before persisting refreshed credentials. Time comes from the server/DB.
Do not rely on provider paid-plan session timeout features for these LifeOS bounds.
The values above are proposed security/product defaults, not existing settings.

Offline logout immediately clears local credentials and cached private UI, but
cannot guarantee server revocation. Show an English notice that server sign-out
could not be confirmed; a fresh authenticated session can request all-device logout.
Selected-device management UI remains Phase 4; do not promise it at Phase 1 launch.
Do not retain a supposedly erased bearer token just to retry it.
If the server committed revocation but provider cleanup failed, LifeOS access is
denied and provider cleanup retries; distinguish that from an unreachable server.

## Session data and authorization

Proposed account-scoped tables (not migrations):

- `account_security(user_id, status, auth_version)`; server-owned lifecycle fields.
- `app_sessions(id, user_id, handle_digest, supabase_session_id, auth_version,
  created_at, last_user_activity_at, idle_expires_at, absolute_expires_at,
  revoked_at, reauthenticated_at, platform, credential_version)`.
- `session_credentials(session_id, encrypted_provider_tokens, key_version,
  refresh_version)`; private schema, unavailable to browser/native/database roles.

For every request the BFF checks the handle, authoritative account/session state,
expiry, current workspace membership and per-action resource permissions (or a
narrow read-only document grant once ADR-0006 sharing is implemented). No
positive authorization cache initially. Reject absent/deleted/revoked state;
database/session-store outage fails closed for private operations.

Use user-scoped Supabase JWTs for ordinary database work so RLS still applies.
RLS and storage policies must also require the mapped active app session matching
`auth.uid()` and the JWT `session_id`, account auth_version, and resource membership
or an explicitly supported read-only grant. A grant cannot authorize workspace lists.
A narrowly granted fixed-search-path helper can evaluate private session state
without exposing credential records. It must derive identity from verified claims,
not arbitrary client-supplied user/session parameters; review and benchmark it.
It also checks provider session existence for sign-out invalidation; application
expiry checks remain independent. Expiry cleanup is not the enforcement mechanism.

Clients cannot create registry entries, mutate membership/owner/state fields, or
use provider credentials directly through LifeOS endpoints. A direct Supabase login
that has no registered active app session must fail data/storage access. Restrict
table writes; invariant-bearing mutations use reviewed transactional functions.
Test direct REST, RPC, storage and any enabled realtime path, not just the BFF.
Realtime private feeds are deferred; no implicit open subscription permissions.

Service credentials bypass RLS: use separate narrowly reviewed administrative/job
adapters, never as the default CRUD client. Durable reminders are authorized by
the active account, workspace, task and consent, independently of the interactive
session that created them; ordinary logout must not cancel legitimate reminders.
Deletion, lost membership or revoked integration consent must stop dependent jobs.

## Revocation limits and file access

Supabase sign-out can leave an issued JWT cryptographically valid until expiry.
LifeOS therefore denies new authorization checks against revoked session state;
it does not claim to revoke the JWT signature itself. Without the matching RLS/
storage gates, a direct endpoint could still accept it. Prove parity before release.

Initial downloads/previews/exports are streamed through the authenticated gateway;
no public bucket or reusable signed download URL is issued. Uploads likewise use
bounded gateway intake into quarantine. Any later direct-upload/download capability
needs a separate reviewed expiry/revocation design. This costs bandwidth and may
constrain hosting; validate limits rather than silently introducing public URLs.

Requests already authorized, transactions in flight, downloaded copies and bytes
already delivered cannot be recalled. Recheck before sensitive mutation commit
under a shared account/session lock and before external execution; cancel active
streams best-effort. State the authorization-time boundary honestly. Operators,
compromised servers/devices and privileged credentials remain residual risks.

## Mandatory Phase 1 tests and gates

Test all platforms' login/verify/reset, refresh races, revoked/expired/forged handles,
JWT replay after app/provider revocation, direct Supabase login without registry,
cross-tenant access, CSRF/login-CSRF, callback replay/redirects, logout cache clearing,
offline logout messaging, secure-store reinstall/backup behavior and store outage.
Deletion_pending denies existing sessions immediately at the next check. Prove
all-device auth_version revocation, no privilege-field writes and no secrets in
client bundles/logs. Phase 2 adds the storage/stream equivalents before file intake.
No auth/RLS/device tests have been executed yet; they require approved Phase 1 work.

## Evidence and decision

Official sources initially checked 2026-10-10; Supabase sessions/sign-out and Expo
SecureStore rechecked 2026-10-13: [Supabase sessions](https://supabase.com/docs/guides/auth/sessions),
[SSR considerations](https://supabase.com/docs/guides/auth/server-side/advanced-guide),
[Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/),
[OWASP sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
and [CSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).
The BFF/registry, timeout choices and test gates are LifeOS design recommendations,
not guarantees supplied by those providers. Founder decision: accept, amend or
reject this proposal including its additional Phase 1 server work and D16 spike.

## Operational costs and unresolved implementation decisions

The BFF adds a network hop and authoritative session reads; RLS adds indexed
lookups. Streaming can incur storage egress plus gateway bandwidth/compute, and
needs bounded concurrency, sizes and timeouts. Ten-minute JWTs increase refresh
traffic compared with the provider's usual one-hour default. Costs cannot be
priced before hosting, usage and quotas are selected. Benchmark synthetic workloads
in approved Phase 1/2 work.

P1-01/D16 must select runtime/region, routing, key custody/rotation and recovery,
and supported SDK/callback APIs. P1-19/20 must specify refresh locking/crash
recovery, one-to-one provider-session mapping, explicit current-session provider
sign-out scope, cleanup retry limits and account/session lock ordering.
Reauthentication must prove a fresh credential check, not accept a refreshed JWT;
define cleanup of any extra provider session created by that check. Only the auth
service updates last activity: polling, refresh and direct RLS requests must not
extend idle expiry.

Validate verification/recovery links opened on another device: offer a safe
restart without weakening challenge binding. Define key-loss and database-restore
procedures that invalidate restored sessions before accepting traffic; restored
revoked credentials must not revive access. These are implementation gates, not
solved infrastructure.
