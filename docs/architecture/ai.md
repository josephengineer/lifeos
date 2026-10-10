# AI architecture

Status: Planned. Provider, models, regions, retention terms and spend are undecided.

The deterministic core stores documents and user-confirmed facts, performs
metadata search and manages tasks without model availability. AI processing is
server-only, opt-in for relevant data, quota-controlled and cancelable where
possible. Disabling AI blocks new jobs and prompts handling of derived data.

## Processing pipeline

Authorized private upload -> quarantine/scan -> text extraction/OCR -> language
identification -> optional classification/structured extraction -> schema checks
-> provenance storage -> user review. Store extractor/model/prompt versions and
source version/page/offset. Do not overwrite confirmed fields with new suggestions.
Confidence scores are signals, not calibrated guarantees; low support requires
review or abstention. OCR provider limits/language support require feasibility tests.

Retrieval first scopes by authenticated workspace and accessible record set, then
searches. Recheck access before constructing model context and returning citations.
Do not retrieve globally and filter only after generation. Deleted/revoked sources
must leave caches, vectors and conversation retrieval. Cache keys include scope,
permissions version, source version and model configuration.

## Prompt injection and tool boundaries

Treat source text, OCR and model responses as untrusted data. Delimit content and
instruct models to treat it as evidence; this is only one layer. Tool allowlists,
server-side authorization, bounded schemas and approval policies enforce actual
security. Never expose secrets or privileged credentials to prompts. Generated
URLs/tool parameters must not cause arbitrary network access or SSRF.

The assistant returns citations or states it cannot establish a fact. It must not
invent deadlines, cancellation completion or legal conclusions. Evaluate malicious
instructions in multilingual documents, fabricated citations, cross-workspace
questions and provider timeouts using synthetic fixtures.

## Future action state machine

`proposed -> awaiting_approval -> approved -> executing -> succeeded`

Alternatives: rejected, expired, canceled, failed or outcome_unknown. Approval
binds actor, immutable payload hash, scope and expiry; edits invalidate it.
Execution rechecks identity, permissions, current consent and provider capability.
Retries require idempotency or reconciliation; an ambiguous external response
enters outcome_unknown instead of blindly executing again. Success requires
verified provider/result evidence. Cancellation after an external effect may be
impossible and must be explained. No autonomous payments in the MVP.

## Quality and operations

Before enabling a capability, evaluate citation validity, field correctness,
abstention, authorization, injection resilience, latency and per-operation cost.
Founder-approved thresholds and privacy terms gate rollout. Circuit breakers and
bounded retries expose a recoverable state and preserve manual work. Record only
redacted metrics, model version and reference IDs in operational logs. Conversation
deletion includes associated derived artifacts within the documented retention policy.
