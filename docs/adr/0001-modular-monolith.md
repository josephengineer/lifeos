# ADR-0001: Modular monolith and universal client

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: A small team must deliver web, Android and iOS without duplicating
business logic. The initial product has closely related personal administration domains.

Decision proposal: Expo/React Native/Router with strict TypeScript, modular domain
packages, typed Zod boundaries and Supabase-backed persistence. Use a single
repository and npm workspace lockfile once an app exists. ADR-0005 recommends
evaluating the official SDK first; a custom auth gateway is not approved.
Custom business APIs remain part of the monolith; validate hosting as needed.
Select worker hosting separately before document processing. This remains one
universal Expo frontend, not a separate web application architecture.

Alternatives: separate native/web apps increase platform-specific flexibility and
cost; microservices introduce deployment and transaction complexity too early.

Consequences: platform adapters and device testing remain necessary. Shared
packages must keep server secrets and SDKs outside client bundles. Package version
compatibility and SSR requirements still need validation.

Evidence: [official sources](../architecture/sources.md). Revisit if platform
requirements materially diverge or worker limits prevent required processing.

## P1-01 universal architecture evidence: 2026-10-14

Founder approved the direction and bounded research; this ADR's implementation
proposal remains subject to final acceptance. SDK 57/Router 57 support one client
with thin routes, shared domain packages and platform adapters. Disposable web
static export and Android/iOS JS bundle exports passed; native binaries/device
behavior were not tested. Recommend static web initially, with no private data in
build-time HTML. SSR/BFF hosting requires a specific need; separate web/native
applications and microservices remain higher-maintenance alternatives.

Exact core pins and toolchain blockers are in [ADR-0004](0004-foundation-tooling.md)
and the [research report](../research/p1-01-toolchain.md). Windows handles JS and
Android tooling; iOS native compilation/simulation needs macOS/Xcode or separately
approved cloud builds. iOS 16.4+ device support needs founder confirmation.
