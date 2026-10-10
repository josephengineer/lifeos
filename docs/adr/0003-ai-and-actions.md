# ADR-0003: AI suggestions and approved actions

Date: 2026-10-10. Status: Proposed. Approver: founder, pending.

Context: Document-derived suggestions can be incorrect or maliciously influenced;
external effects can be consequential and difficult to reverse.

Decision proposal: AI remains optional and server-side. Keep inferred values and
source evidence separate from confirmed facts. Use scoped retrieval, schema
validation and an explicit proposal/approval/execution/confirmation state machine.

Alternatives: automatic extraction overwrites and unrestricted model tools reduce
interaction but create unacceptable integrity and authorization risks.

Consequences: review adds friction; deterministic manual workflows and uncertainty
states are required. Approval binds the exact payload and does not bypass access
checks. Provider timeouts can create unknown outcomes requiring reconciliation.

Evidence: [AI architecture](../architecture/ai.md) and
[threat model](../security/threat-model.md). No provider selected or AI capability built.
