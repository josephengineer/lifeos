# ADR-0001: Modular monolith and universal client

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: A small team must deliver web, Android and iOS without duplicating
business logic. The initial product has closely related personal administration domains.

Decision proposal: Expo/React Native/Router with strict TypeScript, modular domain
packages, typed Zod boundaries and Supabase-backed persistence. Use a single
repository and npm workspace lockfile once an app exists. ADR-0005 adds an API/BFF
inside the same monolith; select its hosting/key management in the Phase 1 spike.
Select worker hosting separately before document processing. This remains one
universal Expo frontend, not a separate web application architecture.

Alternatives: separate native/web apps increase platform-specific flexibility and
cost; microservices introduce deployment and transaction complexity too early.

Consequences: platform adapters and device testing remain necessary. Shared
packages must keep server secrets and SDKs outside client bundles. Package version
compatibility and SSR requirements still need validation.

Evidence: [official sources](../architecture/sources.md). Revisit if platform
requirements materially diverge or worker limits prevent required processing.
