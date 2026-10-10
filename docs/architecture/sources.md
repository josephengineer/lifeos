# Official-source validation

Reviewed 2026-10-10. These sources validate architectural capabilities only;
they do not verify this application's implementation or select package versions.

| Source | Verified implication | Remaining validation |
| --- | --- | --- |
| [Expo Router introduction](https://docs.expo.dev/router/introduction/) | Shared file-based routing for web, Android and iOS | Choose mutually compatible SDK/React/Router versions and run platform spikes |
| [EAS Build](https://docs.expo.dev/build/introduction/) | Candidate managed mobile build path | Account, signing, quotas/costs and actual builds |
| [Zod](https://zod.dev/) and [TypeScript strict mode](https://www.typescriptlang.org/tsconfig/strict.html) | Typed runtime schemas and strict static checks fit the proposed trust boundaries | Pin compatible versions; type inference does not replace authorization |
| [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) | Database policies support row-level access enforcement | Write and test each tenant policy; privileged paths need independent checks |
| [Storage buckets](https://supabase.com/docs/guides/storage/buckets/fundamentals) | Private downloads require authenticated access or signed URLs | Configure buckets/policies and test denied access and expiry |
| [Storage access control](https://supabase.com/docs/guides/storage/security/access-control) | Storage authorization uses RLS; service credentials can bypass it | Prevent client secret exposure and constrain workers |
| [Supabase function limits](https://supabase.com/docs/guides/functions/limits) | Hosted functions have resource and execution limits | Benchmark OCR workloads; choose a durable worker runtime before pipeline implementation |
| [Protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) | Private-repository protection depends on GitHub plan; admin bypass is configurable | Verify current account plan and exact available controls |
| [Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) | Minimize permissions and pin actions to full commit SHA | Keep pins updated and review dependency changes |

Do not infer SSR hosting, background worker duration, OCR support, store billing
eligibility or regulatory compliance from these documents. These need specific
research tasks and current official references before implementation. Versions
and integration APIs are deliberately not guessed in Phase 0.
