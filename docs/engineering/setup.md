# Development setup

## Phase 0 (available now)

Use Git and Python 3.11+. Clone the private repository after it is bootstrapped,
or use the existing checkout. No npm packages, cloud account or environment values
are needed for documentation checks.

```text
git status --short --branch
python scripts/check_foundation.py
git diff --check
```

Use UTF-8, LF and final newlines. The checker validates local document paths,
catalog IDs/statuses/traceability and required files. It does not validate external
links, all Markdown syntax, YAML semantics or application behavior.

## Phase 1 setup plan

Select an Expo-compatible supported Node version; pin it in the repository and
CI, create npm workspaces and commit a single lockfile. Document `npm ci`, lint,
typecheck, test and web export commands when real scripts exist. Select SDK
versions from current official compatibility guidance rather than this proposal.

Use separate Supabase local development and staging projects. Provision local
schema from reviewed migrations and synthetic seed data. Commit only example
configuration; `.env.example` names are proposals, not operational setup today.
Publishable client values are public. Server secrets belong to server secret
stores, never `EXPO_PUBLIC_*` values or client imports.

Native Android needs an emulator/device and toolchain. iOS local simulator/build
validation requires macOS/Xcode; this Windows machine cannot prove it. EAS is a
candidate build path subject to account/signing/cost approval. Document actual
development-build commands only after setup is implemented and tested.

## Environment matrix

| Environment | Data/config | Allowed operations |
| --- | --- | --- |
| Local | Synthetic data, local credentials | Recreate DB, migrations, tests |
| Staging/preview | Separate managed project, synthetic/sanitized fixtures | Release rehearsal and integration sandboxes |
| Production | Dedicated project/secrets, approved region | Explicitly approved releases and migrations only |

Never default to production. Validate environment identity before migrations.
Store backups and credentials separately; do not copy production data into tests.
