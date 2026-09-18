#!/usr/bin/env python3
"""Generate broad adjacent-cue candidates for broken Korean protected phrases.

Usage:
  python audit_protected_phrase_splits.py caption_body.txt

This is deliberately a high-recall candidate generator, not an auto-fixer.
Every hit must be human-adjudicated with neighboring cues. Zero regex hits alone
is never a pass; the operator must still read every adjacent pair manually.
"""
from pathlib import Path
import argparse
import re
import sys

ap = argparse.ArgumentParser()
ap.add_argument("body")
a = ap.parse_args()
p = Path(a.body)
lines = [x.strip() for x in p.read_text().splitlines() if x.strip()]

DEP = "것|거|걸|건|게|데|바|줄|리|뿐|만큼|대로|듯|척|체|만|법|터|셈|뻔|지|때|수"
BOUND = "정도|경우|점|차원|때문|방식|형태|수준|단계|상황|과정|측면|입장|관점|의미|이유|결과|전망|가능성|목적|쪽"
PRED = "같|있|없|아니|되|돼|이다|이에요|예요|였|이라고|라는|알|모르|보이|느껴|말|생각|해야|한다|했습니다"
DETERMINERS = {
    "이런", "그런", "저런", "어떤", "모든", "같은", "큰", "작은", "새로운",
    "다른", "한", "두", "첫", "많은", "적은", "있는", "없는", "하는", "되는",
    "된", "받은", "갈", "올", "할", "될", "만든", "만드는",
}
DISCOURSE = (
    "그리고", "그래서", "그런데", "근데", "하지만", "다만", "그러면", "그렇죠",
    "아니면", "물론", "대신", "즉", "네", "아니요",
)
VERBISH = re.compile(
    r"(?:다|요|죠|니다|는데|거든요|잖아요|했고|하며|해서|하려고|됩니다|"
    r"있어요|없어요|합니다|했습니다|했어요|이에요|예요)(?:[?!])?$"
)

out = []

def add(cat, i, x, y):
    out.append((i, cat, x, y))

for i, (x, y) in enumerate(zip(lines, lines[1:]), 1):
    last = x.split()[-1]
    first = y.split()[0]

    # Adnominal -> dependent/bound noun.
    if re.search(r"(?:는|은|ㄴ|던|을|ㄹ|같은|있는|없는|하는|되는|된|할|될)$", last) and re.match(
        rf"^(?:{DEP}|{BOUND})(?:$|\s|[이가은는도를의에])", y
    ):
        add("관형형→의존/결합명사", i, x, y)

    # Explicit determiner stranded from a following noun phrase.
    if last in DETERMINERS and not y.startswith(DISCOURSE):
        add("관형어→명사 후보", i, x, y)

    # Broad adnominal ending: intentionally high recall because explicit word lists miss forms.
    if re.search(r"(?:는|은|던|을|ㄹ|같은|있는|없는|하는|되는|받은|만든)$", last) and not y.startswith(DISCOURSE) and not re.match(rf"^(?:{PRED})", y):
        add("광의 관형형→명사 후보", i, x, y)

    # Dependent noun/topic form stranded from its predicate/complement.
    if re.search(rf"(?:^|\s)(?:{DEP})(?:이|가|은|는|도|만|을|를|의|에|으로|로|처럼|부터|까지)?$", x) and re.match(rf"^(?:{PRED})", y):
        add("의존명사→서술부", i, x, y)

    # High-confidence modal/dependent-noun newline failures.
    if re.search(r"(?:할|될|볼|쓸|받을|올|갈|나올|끼울) 수(?:가|는|도|만)?$", x) and re.match(r"^(?:있|없)", y):
        add("수 결합구", i, x, y)

    # Subject/topic cue followed by a predicate-bearing continuation. Broad by design.
    if re.search(r"(?:이|가|은|는)$", last) and VERBISH.search(y):
        add("주어·화제→서술부 후보", i, x, y)

    # Object/adverbial cue followed by a predicate-bearing continuation.
    if re.search(r"(?:을|를|에|에서|에게|한테|로|으로|보다|까지|부터|처럼|와|과)$", last) and VERBISH.search(y):
        add("목적어·부사어→서술어 후보", i, x, y)

    # Number/counter and fixed bound expressions.
    if re.search(r"(?:한|약|대략|무려|불과|한두|두세|몇|수십|수백|수천|수만)$", x) and re.match(r"^[0-9일이삼사오육칠팔구십백천만억조]", y):
        add("수량 결합구", i, x, y)

    # Auxiliaries and predicate tails: broad, manual adjudication required.
    if re.search(r"(?:고|게|어|아|지|해)$", last) and re.match(r"^(?:있|없|되|돼|보|주|놓|두|가|오|버리|내|말|싶)", y):
        add("보조용언 후보", i, x, y)

seen = set()
for i, cat, x, y in out:
    key = (i, cat)
    if key in seen:
        continue
    seen.add(key)
    print(f"{i}\t{cat}\t{x}\t{y}")
print(f"# body_lines={len(lines)} candidates={len(seen)}", file=sys.stderr)
