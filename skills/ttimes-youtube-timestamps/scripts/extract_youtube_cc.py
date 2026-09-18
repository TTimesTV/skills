#!/usr/bin/env python3
"""Collect YouTube CC and prepare TTimes chapter-boundary candidates.
Usage: python3 extract_youtube_cc.py URL --out-dir OUTPUT
Requires yt-dlp; stdlib only otherwise.
"""
from __future__ import annotations
import argparse, collections, json, math, re, subprocess, sys
from pathlib import Path

TS_RX=re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s+(.+?)\s*$")
MARKERS=("그럼","그러면","그렇다면","이번에는","다음","이제","한편","반면","궁금","왜","어떻게","무엇","어떤","정리","마지막","말씀","질문","쉽게 말","예를 들","결국","핵심","바로","먼저")
STOP={"그","이","저","것","거","좀","수","등","더","또","및","때","중","있다","있는","있고","합니다","하면","해서","그런","이런","저런","정말","제가","저희","우리","그게","이게","근데","네","예","뭐","어","아"}

def run(cmd,timeout=180):
 p=subprocess.run(cmd,capture_output=True,text=True,timeout=timeout)
 if p.returncode: raise RuntimeError(f"command failed ({p.returncode}): {' '.join(cmd)}\n{p.stderr[-1200:]}")
 return p.stdout

def fmt(s):
 s=max(0,int(round(s))); h,r=divmod(s,3600); m,x=divmod(r,60)
 return f"{h}:{m:02d}:{x:02d}" if h else f"{m:02d}:{x:02d}"

def choose(meta,preferred="ko"):
 man=meta.get("subtitles") or {}; auto=meta.get("automatic_captions") or {}
 for lang in [preferred,f"{preferred}-orig","ko","ko-orig"]:
  if lang in man:return lang,True
 for lang in [f"{preferred}-orig",preferred,"ko-orig","ko"]:
  if lang in auto:return lang,False
 for table,is_man in ((man,True),(auto,False)):
  for lang in table:
   if lang.endswith("-orig") or lang in {"en","ja","zh-Hans","zh-Hant"}:return lang,is_man
 raise RuntimeError("No usable manual or automatic captions found")

def download(url,out,vid,lang,manual):
 flag="--write-subs" if manual else "--write-auto-subs"
 run(["yt-dlp","--skip-download",flag,"--sub-langs",lang,"--sub-format","json3","--no-warnings","-o",str(out/"%(id)s.%(ext)s"),url])
 p=out/f"{vid}.{lang}.json3"
 if not p.exists():
  hits=sorted(out.glob(f"{vid}.{lang}*.json3"))
  if not hits:raise RuntimeError(f"caption file missing: {p}")
  p=hits[0]
 return p

def parse(path):
 data=json.loads(path.read_text(encoding="utf-8")); out=[]
 for ev in data.get("events",[]):
  if "tStartMs" not in ev:continue
  text=re.sub(r"\s+"," ","".join(x.get("utf8","") for x in ev.get("segs",[])).replace("\n"," ")).strip()
  if text:
   st=ev["tStartMs"]/1000; en=(ev["tStartMs"]+ev.get("dDurationMs",0))/1000
   out.append({"start":st,"end":max(st,en),"text":text})
 return out

def desc_chapters(desc):
 out=[]
 for line in (desc or "").splitlines():
  m=TS_RX.match(line)
  if m:
   p=[int(x) for x in m.group(1).split(":")]; s=p[-1]+60*p[-2]+(3600*p[-3] if len(p)==3 else 0)
   out.append({"timestamp":m.group(1),"seconds":s,"title":m.group(2)})
 return out

def tokens(text):
 xs=re.findall(r"[가-힣A-Za-z0-9][가-힣A-Za-z0-9+._-]{1,}",text.lower())
 return collections.Counter(x for x in xs if x not in STOP and len(x)>=2)

def cosine(a,b):
 if not a or not b:return 0.0
 dot=sum(v*b.get(k,0) for k,v in a.items()); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
 return dot/(na*nb) if na and nb else 0.0

def text_between(cues,a,b):return " ".join(c["text"] for c in cues if c["end"]>=a and c["start"]<=b)
def silence(cues,t,r=8):
 gaps=[]; prev=None
 for c in cues:
  if c["start"]>t+r:break
  if prev is not None and c["start"]>=t-r:gaps.append(max(0,c["start"]-prev))
  prev=c["end"]
 return min(max(gaps,default=0),3)

def candidates(cues,duration):
 raw=[]
 for t in range(50,max(51,int(duration)-40),10):
  before=text_between(cues,t-55,t); after=text_between(cues,t,t+55); shift=1-cosine(tokens(before),tokens(after)); opening=text_between(cues,t-5,t+18)
  marker=min(.24,sum(1 for x in MARKERS if x in opening)*.055); question=.18 if any(x in opening for x in ("까요","습니까","뭔가","왜","어떻게","무엇")) else 0; gap=min(.03,silence(cues,t)*.01)
  raw.append({"seconds":float(t),"score":shift+marker+question+gap,"shift":shift,"context":opening})
 maxima=[]
 for i,x in enumerate(raw):
  near=raw[max(0,i-2):i]+raw[i+1:i+3]
  if all(x["score"]>=y["score"] for y in near):maxima.append(x)
 maxima.sort(key=lambda x:x["score"],reverse=True); target=max(7,min(10,round(duration/240)+2)); wanted=min(22,max(12,(target-2)*3)); picked=[]; min_gap=75 if duration<1800 else 90
 for x in maxima:
  if all(abs(x["seconds"]-y["seconds"])>=min_gap for y in picked):
   picked.append(x)
   if len(picked)>=wanted:break
 picked.sort(key=lambda x:x["seconds"])
 for x in picked:
  t=x["seconds"]; x["timestamp"]=fmt(t); x["before"]=text_between(cues,max(0,t-22),t); x["after"]=text_between(cues,t,min(duration,t+42))
 return picked

def outputs(out,meta,cc,lang,manual,cues):
 duration=float(meta.get("duration") or cues[-1]["end"]); actual=desc_chapters(meta.get("description") or ""); cand=candidates(cues,duration)
 (out/"metadata.json").write_text(json.dumps({"id":meta["id"],"title":meta.get("title"),"url":meta.get("webpage_url"),"duration":duration,"cc_language":lang,"cc_type":"manual" if manual else "automatic","cc_file":cc.name,"existing_description_chapters":actual},ensure_ascii=False,indent=2),encoding="utf-8")
 with (out/"transcript.tsv").open("w",encoding="utf-8") as f:
  f.write("start\tend\ttext\n")
  for c in cues:f.write(f"{c['start']:.3f}\t{c['end']:.3f}\t{c['text']}\n")
 lines=[f"# {meta.get('title')}","",f"- URL: {meta.get('webpage_url')}",f"- Duration: {fmt(duration)}",f"- CC: {'manual' if manual else 'automatic'} `{lang}`","","## First 90 seconds — classify promo/highlight/intro manually","",text_between(cues,0,min(90,duration)),"","## Candidate body boundaries","","Candidates are not final chapters. Snap selected boundaries to the first exact CC cue of the question/transition.",""]
 for c in cand:lines += [f"### {c['timestamp']} · score {c['score']:.3f}",f"- Before: {c['before']}",f"- After: {c['after']}",""]
 if actual:lines += ["## Existing description chapters — reference only",""]+[f"{x['timestamp']} {x['title']}" for x in actual]+[""]
 (out/"chapter_source_pack.md").write_text("\n".join(lines),encoding="utf-8")
 with (out/"candidate_boundaries.tsv").open("w",encoding="utf-8") as f:
  f.write("timestamp\tseconds\tscore\tshift\tcontext\n")
  for c in cand:
   context=re.sub(r'\s+',' ',c['context']).replace(chr(9),' ')
   f.write(f"{c['timestamp']}\t{c['seconds']:.1f}\t{c['score']:.4f}\t{c['shift']:.4f}\t{context}\n")

def main():
 ap=argparse.ArgumentParser();ap.add_argument("url");ap.add_argument("--out-dir",required=True);ap.add_argument("--language",default="ko");a=ap.parse_args();out=Path(a.out_dir).expanduser().resolve();out.mkdir(parents=True,exist_ok=True)
 meta=json.loads(run(["yt-dlp","-J","--skip-download","--no-warnings",a.url],240));lang,manual=choose(meta,a.language);cc=download(a.url,out,meta["id"],lang,manual);cues=parse(cc)
 if not cues:raise RuntimeError("Caption file contained no usable timed text")
 outputs(out,meta,cc,lang,manual,cues);print(json.dumps({"status":"ok","id":meta["id"],"cc":f"{'manual' if manual else 'automatic'}:{lang}","cues":len(cues),"out_dir":str(out)},ensure_ascii=False));return 0
if __name__=="__main__":
 try:raise SystemExit(main())
 except Exception as e:print(f"ERROR: {e}",file=sys.stderr);raise SystemExit(1)
