# P1-01: Universal toolchain research

Date: 2026-10-14. Status: In Review; research authorized, production implementation
not authorized. Tracks [issue #2](https://github.com/josephengineer/lifeos/issues/2).
The approved direction does not approve every proposed ADR or a custom auth system.

## Recommendation and limits

Use one Expo SDK 57 / React Native / Router client for web, Android and iOS, with
strict TypeScript, modular domain packages and platform adapters. Keep a single npm
workspace lockfile when P1-02 is authorized. Prefer the official Supabase SDK and
server-side RLS/account/session authorization, without a duplicate session issuer.
No evidence currently justifies a universal custom authentication gateway.

Core bundle/compiler feasibility is positive, but the full toolchain is NOT
production-ready: lint compatibility and high-severity dependency audit findings
need resolution. P1-01 has produced research evidence, not a verified app.
Do not start P1-02 automatically. Authorize a narrow research remediation pass
before approving scaffolding. Native builds and live auth/RLS remain untested.

## Exact version evidence

Primary evidence: [Expo compatibility matrix](https://docs.expo.dev/versions/latest/),
[SDK 57 release](https://expo.dev/changelog/sdk-57),
[React Native releases](https://reactnative.dev/versions.html),
[Node releases](https://nodejs.org/en/about/previous-releases),
[TypeScript](https://www.typescriptlang.org/).
Exact patches were read from publisher metadata on npm and resolved in the
disposable lockfile. Latest means the stable tag observed on this date.

| Component | Latest observed | Recommended research pin / rationale |
| --- | --- | --- |
| Expo | 57.0.29 | 57.0.29, stable SDK 57 |
| React Native | 0.87.1 | 0.86.3, SDK 57 target; do not independently upgrade |
| Expo Router | 57.0.27 | 57.0.27, SDK 57 template |
| React / React DOM | 19.3.1 | 19.2.3 for both, matching Expo |
| React Native Web | 0.21.4 | 0.21.4, resolved within Expo's 0.21 range |
| TypeScript | 7.0.2 | 6.0.3, template baseline; parser 8.71.2 requires <6.1 |
| Node.js | 26.12.0 Current | 24.22.0 LTS, used for probes |
| npm | bundled version | 11.19.1 bundled with tested Node 24.22.0 |
| create-expo-app | 5.0.0 | 5.0.0 with expo-template-default 57.0.31 |
| Supabase JS | 2.117.3 | Candidate 2.117.3, Node >=22; not runtime-tested |
| Expo SecureStore | 57.0.4 | Candidate 57.0.4; native tests required |

Expo targets RN 0.86, React 19.2.3, RN Web 0.21 and Node >=22.13.x for SDK 57.
The template selects RN 0.86.3, including release-note fixes. SDK 57 requires
Android 7+ and iOS 16.4+; published Xcode minimum is 26.4. Confirm device-market
fit. Xcode 27 needs SDK-57 scene-support configuration; do not silently select
the latest build image. Pin a compatible image after native-build approval.

Reproducible publisher metadata:
[Expo](https://registry.npmjs.org/expo/57.0.29),
[template](https://registry.npmjs.org/expo-template-default/57.0.31),
[Router](https://registry.npmjs.org/expo-router/57.0.27),
[parser](https://registry.npmjs.org/@typescript-eslint/parser/8.71.2),
[Supabase](https://registry.npmjs.org/@supabase/supabase-js/2.117.3).
Peer ranges establish declared compatibility; probes provide bounded execution
evidence. Native compatibility cannot be inferred from exports.

## Universal architecture

[Expo Router](https://docs.expo.dev/router/introduction/) supports shared routing.
Use thin routes and shared domain/use-case packages; isolate storage, callbacks,
notifications and device APIs. Server secrets/admin clients must not enter client
bundles. Platform files are acceptable; do not fork the entire web application.

Start with static web delivery as a candidate. [Static rendering](https://docs.expo.dev/router/web/static-rendering/)
builds pages at export time: never embed private user/session data in generated
HTML. Authenticated data loads after session resolution and server authorization.
True SSR adds hosting and cache-isolation work and needs a product requirement.

[Expo monorepos](https://docs.expo.dev/guides/monorepos/) support workspaces. Keep
one React/RN installation and root lockfile. The demo template is not a production
architecture: do not copy its example screens and experimental UI wholesale.
Separate apps offer more platform flexibility but duplicate work; bare RN shifts
integration maintenance to the founder. Neither is justified by current scope.

## Authentication comparison

| Option | Security / storage | Operations and recommendation |
| --- | --- | --- |
| Official SDK everywhere | Native protected adapter; web memory-only candidate or persistent JS storage after risk acceptance; tokens remain accessible to active JS | Simplest candidate; provider issuance/refresh, no added proxy; server gates still required |
| SDK plus official SSR | Browser/server share provider tokens; ordinary SSR cookies are not a server-only vault | Only for justified rendering needs; server hosting, cache isolation and refresh coordination |
| Native SDK plus web-only BFF | HttpOnly web cookie reduces token extraction; CSRF/origin and lifecycle controls remain necessary | Fallback for unacceptable browser token risk; extra proxy, latency, keys and outages |
| Custom sessions everywhere | Additional credentials, provider-token vault and refresh coordination | Highest burden; needs a demonstrated failed requirement and founder approval |

[Supabase RN quickstart](https://supabase.com/docs/guides/auth/quickstarts/react-native)
uses configurable storage and foreground refresh. [Expo integration](https://docs.expo.dev/guides/using-supabase/)
uses SQLite persistence and offers provisioning. Neither quickstart is LifeOS's
security policy; no integration-connect command was run. Publishable keys/project
URLs are client configuration; secret/service credentials are not.

Recommend [SecureStore](https://docs.expo.dev/versions/latest/sdk/securestore/) for
native persistence, with backup exclusion, cleanup and explicit failures. Native
stores can reject large payloads: test session size, atomic writes, biometric
changes, lock/unlock, reinstall and recovery. No plaintext fallback. iOS/Android
persistence differs and requires device tests. Memory-only web reduces persistence
exposure but not XSS and loses sessions on reload; founder must accept the UX/risk.

[SSR guidance](https://supabase.com/docs/guides/auth/server-side/advanced-guide)
does not make browser refresh credentials HttpOnly by default. Verified claims
establish identity, not all authorization. Direct database access must be protected
independently of APIs. Use allowlisted callbacks, PKCE where applicable, redacted
logs and non-enumerating recovery UX.

[Sessions](https://supabase.com/docs/guides/auth/sessions) expose session_id and
auth.sessions linkage. Built-in lifetime controls require Pro+, act on refresh,
and do not define human-idle timeouts. A narrow server-owned helper checking
session/user binding plus account state is a candidate for RLS/APIs. Grants,
search_path, provider schema coupling and query cost need testing.
[Sign-out](https://supabase.com/docs/guides/auth/signout) revokes refresh sessions;
already-issued JWTs can survive without live enforcement. Specify local/global
scope, deny revoked/deletion-pending sessions, clear private caches, and never
claim offline logout confirms server revocation.

[RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) must
enforce authoritative workspace membership/ownership on every data path. Test
anonymous, wrong-user, forged workspace/session, revoked session and privileged
helper boundaries. RLS does not cover Auth endpoints: fresh-auth/reset and direct
provider paths need P1-18 evidence. ADR-0006 schema/threat/tests precede P1-08;
document immutability remains a Phase 2 gate.

[Signing keys](https://supabase.com/docs/guides/auth/signing-keys) stay provider
managed. Define admin-key custody, rotation/JWKS cache behavior and recovery;
restored state must not silently reactivate revoked access. SDK-first avoids a
second token-vault/key-recovery domain. No recovery/auth tests are claimed here.

## Windows, testing and CI

Windows supports JS/web and local Android development with Android Studio/JDK/SDK.
[iOS Simulator](https://docs.expo.dev/workflow/ios-simulator/) needs macOS/Xcode.
EAS cloud iOS builds can be initiated from Windows, subject to account/signing/cost
approval. [Local EAS builds](https://docs.expo.dev/build-reference/local-builds/)
do not officially support Windows/WSL. No native toolchain or cloud resource was
provisioned during this research.

| Tool | Evaluated pin / result | Recommendation |
| --- | --- | --- |
| jest-expo / Jest | 57.0.6 / 29.7.0; synthetic RN test passed | Candidate; latest Jest 30.5.2 not assumed interchangeable with preset's Jest-29 internals |
| RN Testing Library | 14.1.0 with test-renderer 1.2.0 | Pin renderer; auto-resolved 1.3.1 required React 19.3 via reconciler |
| ESLint / Expo config | 10.12.0 / 57.0.2 crashes react/display-name; 9.39.5 runs but deprecated | Blocking maintenance decision; do not silently approve deprecated pin or disable rules |
| TypeScript | 6.0.3 passes after environment generation and explicit Jest imports | Strict checking; TS 7 upgrade blocked by parser peers |
| Prettier | 3.9.10 observed, not executed | Formatting candidate |
| Playwright | 1.64.1 observed, not executed | Browser journeys after app exists; native E2E separate |

Sources: [Jest](https://docs.expo.dev/develop/unit-testing/),
[Router tests](https://docs.expo.dev/router/reference/testing/),
[ESLint](https://docs.expo.dev/guides/using-eslint/),
[TypeScript](https://docs.expo.dev/guides/typescript/).
Future CI: reviewed lockfile/npm ci, format/lint/type/tests/audit/web export, then
native jobs when authorized. Preserve Foundation checks, pinned actions, minimal
permissions and redacted artifacts. New required jobs need separate settings approval.

## Disposable evidence

No generated app, dependencies, lockfile or credentials entered this repository.
Synthetic template/logs remain in a temporary directory outside the checkout.
Node 24.22.0 official Windows archive matched published SHA256; no global runtime
changed. Install scripts were disabled; CLI/build commands were explicitly invoked.

Reproduce in an empty disposable directory with Node 24.22.0/npm 11.19.1:

```text
npx --yes create-expo-app@5.0.0 probe --template expo-template-default@57.0.31 --no-install
cd probe
npm install --ignore-scripts --no-fund --no-audit
npx expo install --check
npx expo customize tsconfig.json
npx tsc --noEmit
npx expo export --platform web
npx expo export --platform android --output-dir dist-android
npx expo export --platform ios --output-dir dist-ios
```

- Clean npm ci with scripts disabled reproduced the disposable lockfile; tsc and
  the synthetic Jest test passed afterward.
- Dependency alignment passed; expo-doctor 1.20.4 passed 21/21 checks.
- Initial tsc failed on CSS declarations, including after web export. Generating
  expo-env.d.ts via expo customize tsconfig.json resolved that failure.
- Web export emitted four routes; Android/iOS exports emitted Hermes bundles.
  These do NOT compile/install native binaries or prove device UI behavior.
- One synthetic Text accessibility-role test passed with the pinned Jest stack.
  Explicit @jest/globals imports resolved missing test/expect types.
- Full template ESLint 9 failed react-hooks/set-state-in-effect in its hydration
  demo; the synthetic test lint passed. ESLint 10 failed at rule runtime.
- Final audit: 64 affected package entries (48 high, 16 moderate, zero critical).
  These include transitive/metavulnerability chains, not 64 independent exploits.
  The initial renderer configuration had 65 entries.
- Native builds/devices, browser interaction, live Supabase auth/storage/revocation/
  RLS, restore, latency and load tests were NOT run.

## Dependency maintenance gate

Audit advisories concern braces, node-forge, decode-uri-component, sprintf-js and
uuid. See [bounded machine-readable evidence](p1-01-evidence.json). Triage build
and runtime input reachability before implementation. Do not run force fixes:
audit suggestions include Expo 44/RN 0.72 downgrades violating the matrix.
No such fixes were applied; no production exposure exists from this probe.

Resolve ESLint-10 plugin compatibility and high findings in a bounded research
pass: upstream updates, tested compatibility adapters or a smaller scaffold.
Rerun clean install/type/lint/test/export/audit. Permanent overrides need evidence
and a removal plan. Pin versions/lockfile only with implementation approval;
group Expo updates, review dependency PRs and never auto-merge them.

## Expected costs

Research used local compute/public metadata with no paid resource. Prices are
dated USD list prices, not authorization or a full budget. [Supabase](https://supabase.com/pricing)
Free is $0; Pro starts at $25/month with $10 compute credit. One Micro example
totals $25; adding a $10 Micro gives an illustrative two-project base of $35,
before usage/add-ons/tax. Selected session controls may require Pro; no purchase.

[EAS](https://expo.dev/pricing) Free lists 15 Android and 15 iOS builds with a
low-priority queue; Starter is $19/month plus usage with $45 build credit.
[GitHub Actions](https://docs.github.com/en/billing/concepts/product-billing/github-actions)
standard public-repository runners are free; larger runners/storage overages are
separate. A BFF adds hosting, secrets/monitoring and maintenance, without a reliable
price absent workload/runtime choices. SMTP, domain, devices/Apple signing,
backup/PITR, egress and later OCR/AI are extra budget lines. No service was created.

## Next decision

Accept SDK 57 as a research baseline, not a production-ready lockfile. Keep ADR-0005
undecided until P1-18 and explicit web/expiry decisions. Confirm iOS 16.4+ support
and future native-build access. Authorize a P1-01 remediation follow-up for the
lint/dependency blockers before P1-02. Issue #2 remains In Review; this research
PR requires explicit founder merge approval.
