# User stories

The [feature catalog](feature-catalog.md) records a story and minimum acceptance
criterion for every capability. Criteria there describe the first reviewable
behavior, not complete implementation test plans. Each implementation issue adds
happy-path, invalid-input, permission-denied and recovery scenarios.

## Core journey examples

1. As an individual, I register, verify my email and return to my own workspace.
   An expired verification link gives an English recovery path; a second account
   cannot retrieve the first account's profile or workspace records.
2. As a document owner, I upload a receipt and later retrieve it. Valid synthetic
   PDF/image files pass quarantine; oversized or mismatched files fail clearly;
   unauthorized users cannot obtain bytes or a download capability.
3. As a busy person, I confirm a suggested renewal date and schedule a reminder.
   Source page and uncertainty are visible; a correction persists; server-side
   retries create at most one logical reminder occurrence.
4. As a subscriber, I compare my recurring costs. Monthly and annual estimates
   explain billing assumptions and do not silently combine different currencies.
5. As an account holder, I export or delete my data after reauthentication.
   Export access expires; deletion shows progress and residual backup retention;
   failed cleanup is retried and never represented as complete.
6. As an AI user, I ask about an agreement. Answers cite accessible sources and
   abstain when unsupported; malicious document instructions cause no actions.
7. As a future household member, I see only items explicitly shared with me.
   Removing membership revokes future retrieval and pending job access.

## Cross-cutting acceptance

Test English resources, keyboard/screen-reader flow, narrow/wide layout, both
themes, offline/error recovery and workspace denial for each relevant journey.
Use synthetic names, files, email addresses and payment-provider test modes.
