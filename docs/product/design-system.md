# Design system proposal

Status: Planned. No component library or visual identity is implemented.

Use a calm information-first layout with visible next actions and provenance.
Define semantic tokens for background, surface, text, muted text, accent, border,
focus, warning, danger and success. Define light and dark token sets; components
consume semantic names. Propose a 4-unit spacing grid and a small readable type
scale; validate with actual devices before freezing values.

Shared components: Button, TextField, Select, Card, ListRow, Dialog, Banner,
Skeleton, EmptyState and ErrorState. Every interactive component needs loading,
disabled, focus and error behavior. Errors explain recovery and preserve input.
Destructive actions name their consequence and allow cancellation before submit.

Navigation: compact bottom-level destinations on phones; wider navigation rail
on tablets/desktops, with shared route identity. Decide breakpoints from content
tests, not device names. Avoid hover-only controls. Dates display in the user's
format/time zone; original contract date-only values remain unshifted.

Target WCAG 2.2 AA as a design objective, not a certification. Check contrast,
visible focus, keyboard order, reduced motion, dynamic text sizes and screen
reader names. Validate touch targets against platform guidance in Phase 1.

English resources live in `packages/i18n/en/` in the proposed application.
Use semantic keys, interpolation and pluralization; never concatenate sentences.
Map server error codes to localized UI messages. Email/push templates and default
assistant instructions use the same language policy. Store document-language
metadata separately and present unsupported OCR languages honestly.

AI values use explicit labels such as Suggested and Confirmed, with source and
edit controls. Never use color alone to express certainty, urgency or status.
