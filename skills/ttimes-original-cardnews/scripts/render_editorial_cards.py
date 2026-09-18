"""Evidence-first editorial carousel renderer. No fabricated photographs.
Usage: python render.py /absolute/path/cards.json /absolute/path/output
"""
from pathlib import Path
import sys,json,math,hashlib
from PIL import Image,ImageDraw,ImageFont,ImageOps
S=2;W=1080;H=1350
PAPER='#F4F1E9';INK='#142724';GREEN='#07594A';RED='#E6513D';MUTED='#656F66';LINE='#CECFC3';WHITE='#FFFFFF';PALE='#DFE8DC'
GOTHIC='/System/Library/Fonts/AppleSDGothicNeo.ttc';NUM='/System/Library/Fonts/Avenir Next.ttc'
FONTS={}
def font(size,bold=False,num=False):
 key=(size,bold,num)
 if key not in FONTS:FONTS[key]=ImageFont.truetype(NUM if num else GOTHIC,round(size*S),index=(8 if bold else 7) if num else (6 if bold else 0))
 return FONTS[key]
class Canvas:
 def __init__(self,bg,page,total):
  self.im=Image.new('RGB',(W*S,H*S),bg);self.d=ImageDraw.Draw(self.im);self.boxes=[];self.page=page;self.total=total;self.bg=bg
 def rect(self,xy,color):self.d.rectangle(tuple(round(v*S) for v in xy),fill=color)
 def line(self,xy,color=LINE,width=1):self.d.line(tuple(round(v*S) for v in xy),fill=color,width=round(width*S))
 def text(self,x,y,text,size=36,color=INK,bold=False,width=936,leading=1.24,num=False):
  f=font(size,bold,num);yy=y
  for paragraph in str(text).split('\n'):
   words=paragraph.split(' ');lines=[];line=''
   for word in words:
    proposed=(line+' '+word).strip()
    if self.d.textlength(proposed,font=f)<=width*S:line=proposed
    else:
     if line:lines.append(line)
     if self.d.textlength(word,font=f)>width*S:raise ValueError(f'Unbreakable text on page {self.page}: {word}')
     line=word
   lines.append(line)
   for line in lines:
    self.d.text((round(x*S),round(yy*S)),line,font=f,fill=color,anchor='lt')
    box=self.d.textbbox((round(x*S),round(yy*S)),line,font=f,anchor='lt');b=[v/S for v in box]
    assert b[0]>=0 and b[1]>=0 and b[2]<=W and b[3]<=H,(self.page,line,b)
    self.boxes.append({'text':line,'size':size,'box':b})
    yy+=size*leading
  return yy
 def title(self,lines,y=160,color=INK,size=84):
  yy=y
  for line in lines:yy=self.text(72,yy,line,size,color,True,leading=1.16)
  return yy
 def header(self,kicker,dark=False,logo=None):
  color=PAPER if dark else INK
  self.text(72,58,kicker,25,color,True)
  if logo:
   im=Image.open(logo).convert('RGBA');im=im.resize((134*S,round(134*S*im.height/im.width)),Image.Resampling.LANCZOS);self.im.paste(im,(874*S,49*S),im)
  else:self.text(887,58,'AI BRIEF',23,color,True,width=140,num=True)
  self.line((72,111,1008,111),color,1)
 def footer(self,source,dark=False):
  col='#C4D2CB' if dark else MUTED
  if source:self.text(72,1240,source,22,col,width=850,leading=1.1)
  self.line((72,1303,1008,1303),'#66897D' if dark else LINE,1)
  self.line((72,1303,72+936*self.page/self.total,1303),PAPER if dark else RED,4)
  self.text(914,1273,f'{self.page:02}/{self.total:02}',22,col,True,width=94,num=True)
 def image(self,p,box):
  x,y,w,h=box;im=Image.open(p).convert('RGB');im=ImageOps.fit(im,(w*S,h*S),method=Image.Resampling.LANCZOS,centering=(.5,.47));self.im.paste(im,(x*S,y*S))
 def save(self,p):self.im.resize((W,H),Image.Resampling.LANCZOS).save(p)
def render_page(p,manifest,root,total):
 layout=p['layout'];dark=layout in ['number','workplace'];c=Canvas(GREEN if dark else PAPER,p['id'],total)
 c.header(p['kicker'],dark,root/manifest['logo'] if layout in ['cover','discussion'] else None)
 if layout=='cover':
  yy=151
  for i,line in enumerate(p['title']):yy=c.text(72,yy,line,90,RED if i==1 else INK,True,leading=1.16)
  c.text(72,482,p['byline'],25,MUTED)
  c.image(root/manifest['photo'],(0,515,1080,650))
  c.rect((72,1108,792,1207),PAPER)
  c.text(94,1128,p['deck'].replace('\n','  '),32,INK,True,width=688,leading=1.2)
  c.text(72,1222,p['photo_credit'],20,MUTED)
  c.text(72,1252,p['photo_note'],20,MUTED)
  c.footer('')
 elif layout=='policy':
  c.title(p['title'],size=84)
  c.text(70,366,p['stat'],150,RED,True,leading=1)
  c.text(400,435,p['stat_label'],35,INK,True,width=590)
  c.text(72,536,p['scope'],28,MUTED)
  for i,(label,body) in enumerate(p['rows']):
   y=600+i*166;c.line((72,y-27,1008,y-27));c.text(72,y,label,36,GREEN,True,width=255);c.text(348,y,body,35,INK,width=660,leading=1.35)
  c.text(72,1117,p['note'],27,MUTED,leading=1.4);c.footer(p['source'])
 elif layout=='contrast':
  c.title(p['title'],size=80);c.text(72,382,p['context'],29,MUTED)
  for i,m in enumerate(p['metrics']):
   y=492+i*310;col=GREEN if i==0 else RED
   c.line((72,y-31,1008,y-31));c.text(62,y,m['value'],175,col,True,num=True,width=540)
   c.text(610,y+38,m['label'],43,INK,True,width=397,leading=1.45)
  c.text(72,1135,p['note'],28,MUTED,leading=1.35);c.footer(p['source'])
 elif layout=='compare':
  c.title(p['title'],size=86)
  for i,q in enumerate(p['panels']):
   x=72+i*484;bg=INK if i==0 else GREEN;c.rect((x,442,x+452,902),bg)
   c.text(x+32,476,q['label'],29,PAPER,True,width=388)
   c.text(x+32,550,q['headline'],48,PAPER,True,width=388,leading=1.3)
   c.line((x+32,704,x+420,704),'#70877C')
   c.text(x+32,744,q['body'],31,PAPER,width=388,leading=1.42)
  c.text(72,958,p['conclusion'],43,GREEN,True,leading=1.35)
  c.text(72,1116,p['note'],27,MUTED,leading=1.38);c.footer(p['source'])
 elif layout=='number':
  c.title(p['title'],size=86,color=PAPER)
  c.text(67,450,p['value'],152,PAPER,True,width=950)
  c.text(72,658,p['metric'],41,'#BEE0BA',True)
  c.line((72,764,1008,764),'#7AA38B')
  c.text(72,813,p['body'],37,PAPER,leading=1.52)
  c.text(72,1094,p['note'],26,'#CCE0D5',leading=1.4);c.footer(p['source'],True)
 elif layout=='limits':
  c.title(p['title'],size=78)
  for i,(label,body) in enumerate(p['rows']):
   y=508+i*178;c.text(72,y,f'{i+1:02}',37,RED,True,num=True,width=88)
   c.text(176,y,label,38,INK,True,width=832)
   c.text(176,y+63,body,32,MUTED,width=832,leading=1.38)
  c.rect((72,1081,1008,1198),PALE);c.text(96,1100,p['conclusion'],34,GREEN,True,width=888,leading=1.28);c.footer(p['source'])
 elif layout=='steps':
  c.title(p['title'],size=78);c.text(72,388,p['intro'],33,MUTED)
  for i,(n,title,body) in enumerate(p['steps']):
   y=511+i*218;c.text(70,y,n,72,RED,True,num=True,width=150)
   c.text(244,y+5,title,43,INK,True,width=764)
   c.text(244,y+81,body,32,MUTED,width=764,leading=1.38)
   if i<2:c.line((244,y+170,1008,y+170))
  c.text(72,1153,p['note'],26,MUTED,leading=1.32);c.footer(p['source'])
 elif layout=='workplace':
  c.title(p['title'],size=79,color=PAPER)
  c.line((72,421,235,421),'#ABD1B0',5)
  c.title(p['question'],y=485,size=85,color='#BEE0BA')
  c.text(72,808,p['body'],38,PAPER,leading=1.53)
  c.text(72,1118,p['note'],26,'#CCE0D5',leading=1.38);c.footer(p['source'],True)
 elif layout=='discussion':
  c.title(p['title'],size=78);c.text(72,487,p['intro'],29,MUTED)
  for i,(n,t) in enumerate(p['options']):
   y=609+i*128;c.rect((72,y-8,145,y+67),GREEN);c.text(91,y+6,n,43,PAPER,True,num=True,width=55)
   c.text(179,y+8,t,35,INK,True,width=820)
   c.line((179,y+89,1008,y+89))
  c.text(72,1056,p['closing'],35,INK,True,leading=1.5)
  c.footer(p['source'])
 else:raise ValueError(layout)
 return c

def main():
 manifest_path=Path(sys.argv[1]).resolve();out=Path(sys.argv[2]).resolve();out.mkdir(parents=True,exist_ok=True)
 root=manifest_path.parent;m=json.loads(manifest_path.read_text());pages=m['pages'];assert m['size']==[W,H];assert [p['id'] for p in pages]==list(range(1,len(pages)+1));assert len({p['id'] for p in pages})==len(pages)
 basename=m.get('output_basename','cardnews');assert basename and Path(basename).name==basename
 pdf=out/(basename+'.pdf')
 for p in pages:
  assert all(k in m['sources'] for k in p['source_ids'])
  for field,maxcount in {'rows':3,'steps':3,'options':3,'panels':2,'metrics':2}.items():
   if field in p:assert len(p[field])<=maxcount,(p['id'],field,'layout capacity exceeded')
 records=[]
 for p in pages:
  c=render_page(p,m,root,len(pages));path=out/f"{p['id']:02d}.png";c.save(path)
  records.append({'page':p['id'],'file':str(path),'layout':p['layout'],'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'text_boxes':c.boxes,'source_ids':p['source_ids']})
 ims=[Image.open(x['file']).convert('RGB') for x in records]
 ims[0].save(pdf,save_all=True,append_images=ims[1:],resolution=144)
 sheet=Image.new('RGB',(1080,450*math.ceil(len(ims)/3)),PAPER)
 for i,im in enumerate(ims):sheet.paste(im.resize((360,450),Image.Resampling.LANCZOS),((i%3)*360,(i//3)*450))
 sheet.save(out/'전체미리보기.jpg',quality=95)
 (out/'render_manifest.json').write_text(json.dumps({'input':str(manifest_path),'size':[W,H],'count':len(records),'pages':records},ensure_ascii=False,indent=2))
 print(json.dumps({'cards':len(records),'dimensions':[W,H],'pdf':str(pdf)},ensure_ascii=False))
if __name__=='__main__':main()
