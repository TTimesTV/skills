# Final-upload package handoff corrections

## In-chat delivery is primary

When the producer asks whether an upload package is ready, return all copy-ready metadata blocks directly in chat. A saved local bundle is optional backup and does not replace the in-chat handoff.

## Never reuse body-only `00:00` on a prefixed final

If chapters were derived from a first cut or body-only SRT, do not present its `00:00` as the final upload's first body chapter when the final may contain a front ad, highlight, intro, or other prefix.

Required sequence:

1. Preserve the verified semantic body chapters from the cut.
2. Inspect the actual final-upload prefix.
3. Verify the exact final body offset.
4. Add the real prefix chapters.
5. Shift every body chapter by the verified offset.
6. Validate and only then label timestamps final.

If the final prefix cannot be inspected, deliver the supplied title/body/tag metadata immediately but mark timestamps pending. Never guess the offset or describe cut-relative chapters as verified final timestamps.
