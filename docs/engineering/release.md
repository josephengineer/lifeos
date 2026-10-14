# Release, rollback and incident process

Status: Planned. No environments or releases are provisioned.

## Release candidate

Engineering verifies phase acceptance, CI, security findings, migrations, privacy
controls, English copy, accessibility and platform evidence. Produce a versioned
candidate from a reviewed commit. Staging uses separate credentials and synthetic
data. Rehearse install/update, critical journeys, server jobs and provider failures.
Document remaining risks and obtain founder sign-off before production deployment,
production migrations, paid resources or store submission.

Before beta, select monitoring/alert owners and measurable availability, reminder
delivery, recovery-point and recovery-time objectives. Verify backup frequency,
retention and encryption against those targets. Restore database metadata AND
private object bytes into an isolated environment; validate relationships,
authorization and deletion-ledger replay. Database backup alone is insufficient.

## Migration and rollback

Use additive schema changes first, deploy compatible code, migrate data with
bounded resumable jobs, then remove obsolete fields only after old clients expire.
Test clean setup and upgrade from the previous supported schema. Document every
irreversible migration and get separate approval. Take verified backups before
risky approved changes. Rollback to a known-good artifact only when schema/client
compatibility allows; otherwise use a reviewed forward fix. Disable optional AI
or integration features via operational controls without breaking manual workflows.

## Release and post-release

Founder approves artifact/revision, environment, migration and rollback plan.
Record approver/time, execute the approved operation, verify health and synthetic
smoke flows, watch error/job metrics and update changelog/status only after evidence.
Native store submission and review are separate from a successful build. Never
mark Android/iOS verified based solely on web tests or an EAS configuration file.

## Incident response

The founder coordinates response until an on-call owner is appointed. Record
timeline and scope; contain exposure by approved access changes or feature shutdown;
preserve minimal redacted evidence; rotate affected secrets; assess user/provider
impact; restore safely; verify isolation and record a postmortem with follow-up
issues. Seek qualified advice for jurisdiction-specific reporting obligations.
Do not publish claims, notify third parties or transmit private data without the
appropriate authorization. Establish emergency authority and contact routes before beta.
