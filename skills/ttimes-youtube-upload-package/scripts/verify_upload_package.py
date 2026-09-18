#!/usr/bin/env python3
"""Validate TTimes upload-package hashtags and pinned comment."""
from __future__ import annotations
import argparse, re
from pathlib import Path

TS_RX = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+?)\s*$")

def seconds(ts: str) -> int:
    p=[int(x) for x in ts.split(':')]
    return p[0]*60+p[1] if len(p)==2 else p[0]*3600+p[1]*60+p[2]

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('--hashtags',required=True); ap.add_argument('--comment',required=True); a=ap.parse_args()
    errors=[]; warnings=[]
    hashtag_text=Path(a.hashtags).read_text(encoding='utf-8').strip().replace('\n',' ')
    parts=[x.strip() for x in hashtag_text.split(',') if x.strip()]
    bad=[x for x in parts if not re.fullmatch(r'[^\s,#]+',x)]
    hash_prefixed=[x for x in parts if x.startswith('#')]
    tags=parts
    unique=[]
    for tag in tags:
        if tag not in unique: unique.append(tag)
    if len(unique)<10: errors.append(f'need at least 10 unique tags; found {len(unique)}')
    if bad: errors.append(f'invalid comma-separated tag entries: {bad}')
    if hash_prefixed: errors.append(f'tags must not include # prefixes: {hash_prefixed}')
    if len(tags)!=len(unique): warnings.append('duplicate hashtags found')
    if len(tags)>1 and hashtag_text.count(',')<len(tags)-1: errors.append('hashtags must be comma-separated')

    comment=Path(a.comment).read_text(encoding='utf-8').strip()
    header='📌오늘의 주제 모아보기📌'
    if header not in comment: errors.append('missing topic header')
    if not comment.endswith('시청해 주셔서 감사합니다😍\n좋아요와 구독은 큰 힘이 됩니다😘'):
        errors.append('missing or altered fixed thank-you lines')
    sep='================================='
    if sep in comment:
        before=comment.split(sep,1)[0].strip()
        if not before: errors.append('separator present without front-ad copy')
    elif comment and not comment.startswith(header):
        errors.append('comment has content before topic header but no separator')

    chapters=[]
    for n,line in enumerate(comment.splitlines(),1):
        m=TS_RX.match(line)
        if m:
            ts,title=m.groups(); chapters.append((seconds(ts),ts,title,n))
    if len(chapters)<3: errors.append(f'need at least 3 chapter timestamps; found {len(chapters)}')
    if chapters and chapters[0][0]!=0: errors.append('first timestamp must start at 00:00')
    for i,x in enumerate(chapters):
        if i and x[0]<=chapters[i-1][0]: errors.append(f'line {x[3]}: timestamps not ascending')
        if i and x[0]-chapters[i-1][0]<10: errors.append(f'line {x[3]}: chapter shorter than 10 seconds')
        if x[2].endswith(('.', '。')): warnings.append(f'line {x[3]}: final period in chapter title')
    for x in errors: print('ERROR',x)
    for x in warnings: print('WARN',x)
    print(f'hashtags={len(unique)} chapters={len(chapters)} ad={sep in comment} errors={len(errors)} warnings={len(warnings)}')
    return 1 if errors else 0

if __name__=='__main__': raise SystemExit(main())
