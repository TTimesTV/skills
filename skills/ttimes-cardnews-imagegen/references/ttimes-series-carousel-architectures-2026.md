# TTimes 2026 series-specific carousel architectures

## Principle

A series is not a palette swap. It changes the editorial unit, page count, evidence hierarchy, body-card grammar, and closing function. Apply the named-series identity and the production format together.

The counts below are recommended starting ranges, not hard limits. Add or remove pages only when the source contains an independent claim/evidence/mechanism that changes the argument.

## 1. 이중학의 사람과 기술 × host–guest conversation

**Default:** 5–7 cards.

```text
cover: organizational tension/question
→ host's framing question
→ guest's diagnosis or lived example
→ mechanism: why the organization behaves this way
→ leadership choice/trade-off
→ practical operating principle
→ verified guest closing quote
```

For a compact five-card version:

```text
1 cover
2 problem/tension
3 guest example + mechanism
4 leadership implication/action
5 verified guest quote + profile
```

Rules:

- Card protagonist is the guest unless the package explicitly profiles the host.
- Host speech may frame the question or editorial spine, but must not be attributed to the guest.
- The middle should privilege the guest's answer; do not build three cards from the host's commentary.
- Body visuals should translate organizational dynamics: coordination load, priority trade-offs, workflow, tacit knowledge, motivation, responsibility.
- Use `이중학의 사람과 기술` purple/navy identity consistently.
- Closing card requires audio-confirmed guest wording and role.

## 2. 박영선의 테크토크 × host–guest technology/industry conversation

**Default:** 6–8 cards.

```text
cover: market or technology inflection
→ incumbent problem / demand shift
→ core technology mechanism
→ guest/company differentiator
→ competitive landscape
→ bottleneck / commercialization condition
→ Korea/industry implication
→ guest outlook quote
```

Rules:

- Put mechanism and industrial consequence before biography.
- Use actual diagrams/data for `PROVE`; ImageGen only illustrates mechanism or atmosphere.
- Preserve host-in-badge + guest-as-hero visual grammar.
- Teal/black identity is a starting family, not a fixed hex.

## 3. 강수진 × recurring one-person AI expert / occasional demonstration

**Page count:** variable after title-first subagent conference. When UI/output is the editorial spine, route to F4 instead of the generic one-person layout.

```text
cover: surprising AI behavior or practical question
→ observed failure/odd behavior
→ experiment or prompt setup
→ output/result
→ why the model behaved that way
→ actionable prompting/use rule
→ warning or practical takeaway
```

Rules:

- Causal sequence matters: problem → test → result → cause → action.
- When real UI/output exists, it outranks decorative illustration.
- Do not turn anecdotal model behavior into a universal claim.
- Green/navy recurring-expert identity; add an approved series badge when needed because observed thumbnails often omit one.

## 4. 30년 개발자의 기업 분석 × recurring one-person company analysis

**Page count:** variable after title-first subagent conference.

```text
cover: company/industry judgment question
→ company position and business structure
→ technical or economic engine
→ competitor comparison
→ moat / dependency / bottleneck
→ valuation or industry implication
→ counterpoint
→ analyst verdict/quote
```

Rules:

- Retain company names and comparison denominator.
- Separate product category, customer, revenue engine, and end-use.
- Use company logos and sourced charts accurately; ImageGen must not invent evidence.
- Preserve season badge and teal/navy competitive-analysis identity.

## 5. AI, 안 해보면 모른다 × hands-on demo/tutorial

**Default:** 5–7 cards.

```text
cover: finished result first
→ input/tool stack
→ key step 1
→ key step 2 / workflow
→ failure or limitation
→ reproducible prompt/settings
→ final result + practical verdict
```

Rules:

- Result and UI are primary; presenter face is secondary.
- Preserve exact tool/model/version and settings where visible.
- Do not replace a real result with an ImageGen imitation.
- Use generated visuals only for transitions or missing conceptual layers.

## 6. 티타임즈 주간브리핑 × news briefing

**Default:** 5–8 cards depending on issue count.

```text
cover: event + central issue
→ what happened
→ verified numbers/evidence
→ stakeholder map
→ why now
→ market/industry implication
→ counter-signal
→ next variable / update condition
```

Rules:

- No forced personality quote at the end.
- Source/date/denominator are mandatory for risky claims.
- Company/event graphics, black/red identity, and briefing badge dominate.
- Multiple unrelated events should become separate labeled blocks, not one overlong narrative.

## 7. General one-person expert

**Page count:** variable after title-first subagent conference.

```text
cover thesis
→ premise
→ explanation
→ evidence/example
→ counterpoint
→ implication
→ verified expert quote or conclusion
```

Do not imitate a named-series badge or palette without that series. Load `one-person-square-carousel-template.md`; typography follows the approved format registry, while presenter/evidence composition and episode visuals remain layout variables.

## 8. General conversation / panel

**Default:** 6–9 cards.

```text
cover tension
→ moderator question
→ speaker A position
→ speaker B position
→ agreement/disagreement mechanism
→ evidence
→ unresolved trade-off
→ synthesis
→ correctly attributed closing
```

Track every quote by speaker. A paragraph boundary is not attribution evidence.

## 9. Field report/event coverage

**Default:** 5–8 cards.

```text
cover: place/event + observed change
→ establishing scene
→ direct observation
→ interview evidence
→ product/demo proof
→ local reaction
→ industry implication
→ what to watch next
```

Real location/event imagery is identity evidence and must not be replaced by generated faux reportage.

## Common production contract

- 1:1 final canvas for square carousel when requested.
- Cover uses the exact article `_list_` image and current thumbnail/series grammar.
- Newly created body-card core visuals use ImageGen unless real UI/photo/chart evidence is required.
- Korean text, numbers, quotes, sources, and logos are deterministic overlays.
- Page count follows independent editorial beats, not a fixed quota.
- Thumbnail wording is preserved unless the explicit wording-edit gate fires.
- Closing role differs by series: guest quote, expert verdict, practical result, or next variable.
