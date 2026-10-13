# ADR-0005: Supabase authentication and session architecture comparison

Updated: 2026-10-13. Status: **Conditionally approved security objectives;
implementation architecture not approved.**

Founder decision: compare the custom gateway with official Supabase approaches
and choose the simplest design meeting LifeOS requirements. A custom session
system needs concrete evidence of necessity. This revision replaces the earlier
all-platform BFF recommendation, preserved in Git history. No Phase 1 work,
hosting purchase or implementation is authorized.

## Recommendation and approved objectives

Recommend evaluating official `supabase-js` on all Expo targets, with platform
storage adapters and server-enforced authorization. Supabase owns identity,
session issuance and refresh. Use its session identifier in a narrow authorization
check; do not add opaque LifeOS credentials, a duplicate issuer, a provider-token
vault or a distributed refresh service without evidence of need.

Preserve the approved objectives: credential protection, tenant isolation,
server-side revocation, honest offline behavior and verified deletion. Keeping
every provider token off clients was an earlier design choice, not an accepted
product requirement. JavaScript-visible web tokens and persistence UX need an
explicit founder decision before auth implementation. If unacceptable, evaluate
a web-only BFF before imposing one on native.

A bounded file-intake/preview service can still be needed for safe immutable
uploads. It can accept provider JWTs without issuing sessions or proxying every
database request. The universal Expo frontend and modular monolith remain.

## Official baseline versus LifeOS additions

Official native examples use the SDK's configurable storage and foreground
refresh lifecycle. Quickstart AsyncStorage/SQLite persistence is not LifeOS's
production storage policy. Native needs protected storage. Static Expo web can
use the same SDK without SSR. If SSR becomes necessary, `@supabase/ssr` shares
tokens between browser and server; it is not a server-only HttpOnly token vault.

SDK login does not replace RLS, current membership, account lifecycle checks,
safe previews or negative tests. A valid JWT proves identity, not authorization
or current session state. A provider-session check can detect sign-out without
building another credential lifecycle.

## Comparison

| Concern | Official SDK on native/web: recommended candidate | Web BFF plus native SDK | Custom opaque sessions everywhere: earlier proposal |
| --- | --- | --- | --- |
| Security/storage | Native protected provider tokens; browser JS reads runtime tokens; memory-only avoids persistent web tokens, not XSS | HttpOnly web cookie reduces token extraction; native retains provider tokens; web CSRF controls needed | Server-held provider tokens, but opaque client secrets remain stealable; concentrated vault target |
| Logout/revocation | Provider sign-out plus live session/account gates at data boundaries; SDK refresh | Same gates plus web-session lifecycle | Registry, epochs, refresh locking and provider cleanup must agree |
| Server authorization | Verified JWT, authoritative membership/account/session state, RLS/private storage | Same plus cookie/bearer separation | Same; gateway alone does not protect direct provider endpoints |
| Complexity | Lowest: SDK adapters, small authorization helper and business APIs | Medium: two transports and web session operations | Highest: issuer, token vault, locks, rotation, expiry, cleanup and recovery |
| Hosting/maintenance | Existing Supabase/business hosting; no mandatory auth proxy; storage-adapter and RLS maintenance | Extra web proxy/vault hosting and observability | Every target depends on gateway, vault/key services; potential extra file bandwidth/compute |
| Performance/availability | Direct data path; session checks add DB work; Auth needed for login/refresh; fail closed if authorization state unavailable | Web adds hop/dependency, native direct | Extra hop and gateway/session-store dependency for all platforms |
| Key management/recovery | Provider signing keys plus server admin-key and native-key custody; no additional refresh-token vault | Adds web vault key rotation/restore | Adds vault recovery, restored-session invalidation and crash-safe refresh coordination everywhere |

No reliable monetary estimate exists before region, usage, file limits and hosting
selection. Supabase's built-in timebox/inactivity controls require Pro or above;
that is independent of GitHub Pro. No paid Supabase plan is approved. Benchmark
latency, availability and cost in authorized research.

## Proposed platform storage

- Android: reviewed SDK storage adapter backed by Expo SecureStore; exclude
  credentials from backups. No plaintext AsyncStorage/SQLite token fallback.
- iOS: protected Keychain storage, device-only/unlocked where supported. Test
  reinstall persistence and fresh-install cleanup. Test realistic maximum session
  sizes and atomic updates. If secure-store limits require encrypted secondary
  storage, review a maintained adapter rather than invent encryption or assume
  tutorial code is production-ready. Secure-storage failures require login.
- Web: recommend `persistSession: false` and memory-only access/refresh tokens
  initially. Full reload/new tab requires sign-in; losing local tokens does not
  confirm server logout. Founder must accept this UX and active-XSS exposure.
  PKCE redirects may need a bounded single-use verifier/state store, which must
  not persist access/refresh tokens. Validate callbacks across reloads/devices.
  Persistent browser storage requires a separate risk decision.
- Server: verified user JWTs and user-scoped data adapters for ordinary operations;
  admin/service keys only in approved secret stores. No new refresh-token vault.

TLS, no-store private responses, restrictive CSP, dependency review, no raw active
document content and no token/request-body logging are required. Avoid third-party
scripts on authenticated surfaces. Memory-only tokens remain accessible to active
XSS; HttpOnly reduces extraction but does not prevent acting through a browser.
Bearer APIs must not silently accept ambient cookies. Any future cookie transport
needs Origin/CSRF protection including login, and separate review.

## Authorization and lifecycle

| Event/boundary | Required behavior and gate |
| --- | --- |
| Identity | Verify signature, issuer, audience, expiry and subject; never trust payload user IDs or unverified session objects |
| Private operation | Active account, verified identity, current workspace membership/action permissions; equivalent default-deny RLS and storage gates on direct SDK paths |
| Provider revocation | Narrow fixed-search-path helper derives auth.uid() and JWT session_id, checks matching provider session/user, denies missing state; no client access to auth tables or arbitrary identity parameters |
| Current logout | Explicit SDK signOut with scope=local; only report server sign-out after provider acknowledgement; clear local credentials/private caches/history |
| All-device logout | Explicit global scope after fresh reauthentication; test concurrent login/refresh and affected-session boundary; never rely on the SDK's default global scope |
| Refresh | SDK-managed refresh and native foreground lifecycle; test concurrent calls, resume, network loss and revoked refresh tokens |
| Offline logout | Erase local credentials/caches; English notice that server revocation was not confirmed; fresh login may request global logout; selected-device UI stays Phase 4 |
| Recovery | Rate limits, non-enumerating English errors, allowlisted single-use callbacks; prove recovery credentials cannot bypass intended authorization; revoke affected sessions after reset and require login |
| Sensitive actions | Fresh verified credential challenge, proposed five-minute freshness and action binding; a refreshed JWT is not reauthentication; provider-supported flow must be reviewed |
| Deletion | Phase 4 request atomically marks server-owned deletion_pending before async provider/data cleanup; data boundaries/jobs deny inactive accounts despite valid JWTs; verify cleanup before claiming completion |

The proposed account guard stores lifecycle state, not tokens. Missing state
fails closed and clients cannot change it. Narrow server operations may coordinate
deletion and provider administration; privileged keys bypass RLS and must not be
default CRUD credentials. Do not mutate provider-owned auth schemas/session rows
or grant clients direct access. Review helper ownership, schema dependencies,
recursion, query plans and provider upgrades. Direct SDK login is expected, not a
bypass: only verified active identities with valid session/membership get data.

RLS does not govern Supabase Auth's own account-management endpoints. The spike
must test direct password/email change and global-signout calls, not only LifeOS
screens. Require provider-supported reauthentication/security settings for the
chosen sensitive-account policy. If an exposed provider endpoint bypasses a hard
LifeOS requirement, record it as a concrete gap for an alternative design; do not
claim a client confirmation or database helper fixes that boundary.

Durable reminders reauthorize account, membership, task and consent independently
of interactive sessions. Logout alone does not cancel legitimate reminders;
deletion, lost membership and revoked integration consent stop dependent jobs.

## Expiry and revocation limitations

Provider sign-out invalidates refresh capability while issued JWTs may remain
cryptographically valid. Supabase documents checking session_id against its session
table to detect sign-out. JWT signature/expiry verification alone does not do this.
Custom APIs, direct REST/RPC and Phase 2 storage must prove parity. Realtime remains
deferred. Fail closed when authoritative state cannot be checked.

The earlier 10-minute JWT / 7-day human-idle / 30-day absolute / 5-minute fresh-auth
bounds were proposals, not approved settings. Provider inactivity measures refresh,
not human activity; timeouts are applied at refresh and session-row existence alone
does not enforce exact deadlines. Do not claim equivalence with strict human-idle
limits. Founder must choose semantics and bounds before implementation. Prefer
provider controls if their documented residual access-token window is acceptable.
If strict next-request deadline enforcement is required, evaluate minimal
server-owned deadline/activity metadata alongside provider sessions first. This
extension needs approval but does not inherently need a token vault or new issuer.

Initial file access remains authenticated and reauthorized, with no reusable
signed bearer URLs. A file gateway can accept provider JWTs. Sealed intake and safe
preview are Phase 2 gates independent of auth transport. Already authorized
transactions, streams and delivered bytes cannot be recalled. Sensitive mutation
ordering versus revocation needs an explicit transactional rule and honest boundary.

## Implementation gates and trigger for a custom gateway

After separate Phase 1 research authorization, P1-01/P1-18 must produce:

1. Pinned SDK/Expo compatibility; native storage size/atomicity, backup/reinstall
   evidence; web refresh/reload, callback and multi-tab behavior.
2. Issued-JWT replay denial after local/global sign-out, reset and deletion_pending,
   with refresh races and outages across custom/direct REST/RPC. Add storage in
   Phase 2. Test two tenants, invalid claims and absent authorization state.
3. Founder acceptance of web token exposure/persistence and exact timeout semantics;
   evidence for restricted recovery and fresh-auth flows without bypass.
4. Key rotation/restore procedures: fail closed during recovery; invalidate restored
   sessions or force reauthentication through a supported mechanism before traffic
   resumes; reapply deletion/revocation records. Native key loss requires login.
   Benchmark helper latency and document provider/hosting plan costs.
5. A concrete failed requirement, reproducible evidence, simpler alternatives and
   renewed founder approval before implementing any custom session system.

No runtime experiments have run in Phase 0. Source review supports the simpler
candidate but does not demonstrate production safety. Persistent HttpOnly web
sessions, if required, justify evaluating a web-only BFF. An all-platform gateway
needs an additional demonstrated cross-platform requirement.

## Official sources reviewed 2026-10-13

- [React Native Auth quickstart](https://supabase.com/docs/guides/auth/quickstarts/react-native): configurable SDK storage and foreground refresh.
- [Expo quickstart](https://supabase.com/docs/guides/getting-started/quickstarts/expo-react-native) and [Expo integration guide](https://docs.expo.dev/guides/using-supabase/): supported baseline, not production storage assurance.
- [Expo SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/): platform backup, reinstall and storage constraints.
- [SSR advanced guide](https://supabase.com/docs/guides/auth/server-side/advanced-guide): shared browser/server tokens, distinct from a server-only HttpOnly BFF.
- [Supabase sessions](https://supabase.com/docs/guides/auth/sessions): provider session checks and paid timeout/enforcement limits.
- [Sign-out API](https://supabase.com/docs/reference/javascript/auth-signout): explicit scopes and issued-JWT limitations.

Storage choices, the authorization helper and implementation gates are LifeOS
recommendations derived from these sources, not guarantees supplied by providers.
