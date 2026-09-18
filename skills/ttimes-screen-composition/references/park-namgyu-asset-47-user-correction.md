# Park Nam-gyu asset 47 — caption ends while material continues

Date: 2026-07-17

Confirmed sequence:

```text
NVIDIA digital-twin material starts
+ three-line editorial caption
→ spoken captions SUPPRESS

memo: 영상은 계속, 강조자막은 끝

NVIDIA material continues
+ editorial caption ends
→ spoken captions resume immediately on the next blue speech
```

General rule: material and editorial-caption end points are independent. An editorial caption suppresses spoken captions only for its own assigned blue sync range. If the material persists after the editorial caption exits, spoken captions return while the material remains on screen.
