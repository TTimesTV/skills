# Compact attribute-matrix labels

Use for short graphic labels that compare two architectures across parallel attributes, e.g. cloud vs on-device.

## Keep the requested visual grammar

If the PD asks for a pattern like:

```text
고성능 · 고비용 · 000
저성능 · 저비용 · 000
```

return the third attribute in equally compact visual form. Do not replace the card with a policy explanation.

Preferred when the axis is explicitly security level:

```text
클라우드
고성능 · 고비용 · 보안성↓

온디바이스
저성능 · 저비용 · 보안성↑
```

`보안성` means the degree of security and is grammatically compatible with `↑/↓`. `보안` names the field/system itself; `보안↑/↓` is shorter editorial shorthand but less precise.

## Accuracy boundary

Cloud is not universally insecure and on-device is not universally secure. If the source claim is actually about data custody, use `보안 통제↓/↑` or `외부 전송/기기 내 처리`. But when the PD explicitly needs a simple security axis and the source supports that simplification, do not derail the caption with a lecture.

## Rejection behavior

When the PD says a proposal is `지루하다`, `현학적이다`, or asks for the same visual pattern, immediately return one revised copy block. Explain terminology only when asked separately.
