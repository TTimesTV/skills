# Formal Review Checklist and Skeleton

## Preflight

- [ ] Read the project rubric rather than inferring weights from prior reviews.
- [ ] Record exact credit string and evidence grade.
- [ ] Confirm whether the route is material-only or caption-and-material.
- [ ] Record video duration, dimensions/codecs, hash, and full-decode status.
- [ ] Locate the canonical CC path; it may be nested under `videos/<id>/cc/` rather than a root `cc/` directory.
- [ ] Count regular frames, scene candidates, and contact sheets from the manifest.

## Full-review evidence

- [ ] Read the complete CC chronologically.
- [ ] Inspect every regular contact sheet from first to last.
- [ ] Inspect every scene-candidate sheet from first to last.
- [ ] Recheck decisive time ranges against CC and closer frames.
- [ ] Build a runtime-spanning chronological summary.

## Finding schema

```markdown
### ① HH:MM–HH:MM / concise finding title
- **화면 객체:** exact visible material
- **동시 발화 기능:** what spoken beat it serves
- **판정:** **강점/약점.** why it succeeds or fails as planning
- **PD 개선점:** concrete replacement, addition, or retained practice
```

Minimum: 3 strengths, 2 weaknesses. Prefer 5–6 strengths and 3–5 weaknesses for long-form episodes when the evidence supports them.

## Material-only scope block

```markdown
- **크레딧:** `exact string` — **D1/D2 ...**
- **자료 전용 범위 확인:** 자료만 명시된 영상이므로 자료 선택·발화 싱크·증거·설명 기능만 채점한다. `글·자료`의 `글`은 강조자막 크레딧으로 추정하지 않는다.
- **강조자막 선택:** `확인 불가·총점 제외`
- **강조자막 문구:** `확인 불가·총점 제외`
```

## Material-only score block

```markdown
| 평가 항목 | 원점수 | 자료 전용 배점 | 판단 |
|---|---:|---:|---|
| 자료 선택 | **__/100** | 25/65 | ... |
| 발화 싱크 | **__/100** | 20/65 | ... |
| 증거·설명 기능 | **__/100** | 20/65 | ... |
| 강조자막 선택 | **확인 불가·총점 제외** | 제외 | 자막 크레딧 없음 |
| 강조자막 문구 | **확인 불가·총점 제외** | 제외 | 자막 크레딧 없음 |

`(selection×25 + sync×20 + function×20) ÷ 65 = exact result`

# **총점: rounded/100**
```

## Scoring distinctions

- **Selection deduction:** needed object is absent, weak, generic, or the wrong source type.
- **Sync deduction:** shown object mismatches the spoken actor/action/time/meaning or arrives too early/late.
- **Function deduction:** object is on topic but cannot prove or explain the strength/structure of the claim.
- Missing evidence with otherwise correct timing usually lowers selection/function more than sync.

## Final deterministic checks

- [ ] Output file exists at the exact requested path.
- [ ] `자료 전용 범위 확인` appears when required.
- [ ] `확인 불가·총점 제외` appears for both caption dimensions when required.
- [ ] Credit string matches the supplied evidence exactly.
- [ ] Formula recomputes to the displayed total.
- [ ] Duration and review-frame counts match the manifest.
- [ ] Chronological summary spans opening through ending.
- [ ] Every finding has all five required components.
- [ ] Final priorities are concrete and ordered.
- [ ] Evidence-limit section distinguishes ASR/small-text limits from unresolved authorship.
