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
