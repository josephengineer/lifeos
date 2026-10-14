# ADR-0004: Foundation tooling and licensing

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: The initial repository is empty. Phase 0 needs executable checks without
installing an application merely to claim build coverage.

Decision proposal: use a dependency-free Python documentation validator and a
minimal pinned GitHub Actions workflow. Add npm lockfile installation, formatting,
lint, strict types, tests, audit and web export with the first application issue.
Reserve mobile checks for actual builds with approved signing and cost decisions.

Alternatives: installing a full app now exceeds scope; no CI would allow broken
documentation links and missing traceability. Third-party Markdown tooling may be
added if the simple checker no longer meets repository needs.

Consequences: current checks do not establish application/security correctness or
full Markdown/YAML conformance. No open-source license is selected; founder must
decide license and legal ownership before external contributions or distribution.

Visibility update 2026-10-14: the founder made the repository public. This does not
select a license; review public business-document scope and ownership explicitly.
The original brief's private-repository instruction is preserved as historical
source material and superseded by the founder's later visibility decision.

## P1-01 evidence update: 2026-10-14

Status remains Proposed. Founder authorized research, not production implementation.
Recommend the tested core: Node 24.22.0 LTS/npm 11.19.1, Expo 57.0.29,
React Native 0.86.3, Router 57.0.27, React/DOM 19.2.3, RN Web 0.21.4 and
TypeScript 6.0.3. Scaffold reference: create-expo-app 5.0.0 with default template
57.0.31. These are research pins, not an approved production lockfile.

Alternatives: standalone RN 0.87.1/React 19.3.1 exceed the Expo matrix; Node
26.12.0 is Current rather than LTS; TypeScript 7.0.2 exceeds current parser's
<6.1 peer range. Do not independently choose every latest version. An older SDK
reduces runway and does not automatically solve current transitive advisories.

Jest 29.7.0/jest-expo 57.0.6/RNTL 14.1.0/test-renderer 1.2.0 passed a disposable
component probe. Latest renderer 1.3.1 mismatched React. ESLint 10.12.0 with Expo
config 57.0.2 crashed a React rule; 9.39.5 runs but is deprecated. Full template
lint also detects a hydration-hook error. No lint stack is unconditionally approved.

Consequences/gates: 48 high and 16 moderate audit entries remain in the disposable
lockfile. Resolve or explicitly assess them before scaffold adoption; no forced
major downgrades or blanket suppressions. Keep exact pins/lockfile review, dependency
PRs, standard public Actions runners and least privilege. No paid resources.
[Research](../research/p1-01-toolchain.md) records official sources, compatibility,
costs, alternatives, successful probes and failures. Native builds/auth/restore
are untested; founder decision and research-PR merge remain pending.
