#!/usr/bin/env python3
from __future__ import annotations
from hashlib import sha256
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

W = H = 1080
BODY_TOP_H = 520
NUMBER_BADGE = {'shape': 'square', 'size': 92, 'radius': 0}
BODY_LOGO_ENABLED = False
CLOSING_LOGO_POSITION = 'bottom-center'
CLOSING_USES_LIST_IMAGE = False
GENERAL_COVER_TITLE_PX = 80
GENERAL_BODY_TITLE_PX = 80
GENERAL_BODY_PX = 40
GENERAL_CLOSING_QUOTE_PX = 50
GENERAL_PROFILE_PX = 30
NAVY='#07112D'; GRID='#182344'; WHITE='#F5F4F2'; MUTED='#D7DBE8'; TEAL='#42E6D0'; PROFILE='#B8BED2'


def file_hash(path: Path) -> str:
    return sha256(Path(path).read_bytes()).hexdigest()


def crop_fill(im: Image.Image, w: int, h: int, ax: float=.5, ay: float=.5) -> Image.Image:
    im=im.convert('RGB'); scale=max(w/im.width,h/im.height); nw,nh=round(im.width*scale),round(im.height*scale)
    im=im.resize((nw,nh),Image.Resampling.LANCZOS); x=max(0,min(nw-w,round((nw-w)*ax))); y=max(0,min(nh-h,round((nh-h)*ay)))
    return im.crop((x,y,x+w,y+h))


def font(path: Path, size: int, weight: int|None=None) -> ImageFont.FreeTypeFont:
    f=ImageFont.truetype(str(path),size)
    if weight is not None:
        try:f.set_variation_by_axes([weight])
        except:pass
    return f


def fit_title(lines, font_path: Path, start=68, minimum=44, max_width=944):
    for size in range(start,minimum-1,-1):
        f=font(font_path,size)
        if max(f.getlength(x) for x in lines)<=max_width:return f,size
    raise ValueError(f'title does not fit: {lines}')


def wrap_korean(text: str, f, max_width: int) -> list[str]:
    lines=[];cur=''
    for word in text.split(' '):
        trial=word if not cur else cur+' '+word
        if f.getlength(trial)<=max_width:cur=trial
        else:
            if cur:lines.append(cur)
            cur=word
    if cur:lines.append(cur)
    return lines


def draw_inline_marker(draw, x, y, text, f, color=TEAL):
    b=draw.textbbox((x,y),text,font=f)
    draw.rectangle((b[0]-7,b[1]-7,b[2]+10,b[3]+8),fill=color)
    draw.text((x,y),text,font=f,fill=NAVY)


def draw_square_number(draw, n, black_font: Path, top_h=BODY_TOP_H):
    x,y,s=62,top_h-46,92;draw.rectangle((x,y,x+s,y+s),fill=WHITE,outline=NAVY,width=4)
    f=font(black_font,40);b=draw.textbbox((0,0),str(n),font=f)
    draw.text((x+(s-(b[2]-b[0]))/2-b[0],y+(s-(b[3]-b[1]))/2-b[1]),str(n),font=f,fill=NAVY)


def render_body_card(*, image: Path, title_lines: list[str], body: str, highlight: str, number: int, output: Path, black_font: Path, variable_font: Path):
    c=Image.new('RGBA',(W,H),NAVY);c.paste(crop_fill(Image.open(image),W,BODY_TOP_H),(0,0));d=ImageDraw.Draw(c)
    for x in range(0,W+1,48):d.line((x,BODY_TOP_H,x,H),fill=GRID,width=1)
    for y in range(BODY_TOP_H,H+1,48):d.line((0,y,W,y),fill=GRID,width=1)
    draw_square_number(d,number,black_font)
    ts=GENERAL_BODY_TITLE_PX;tf=font(black_font,ts)
    if max(tf.getlength(line) for line in title_lines)>944:raise ValueError(f'80px title does not fit; revise semantic line breaks: {title_lines}')
    y=585;gap=round(ts*1.13)
    for i,line in enumerate(title_lines):d.text((68,y+i*gap),line,font=tf,fill=TEAL)
    y+=len(title_lines)*gap+28;bf=font(variable_font,GENERAL_BODY_PX,560);bb=font(variable_font,GENERAL_BODY_PX,720);lg=56
    for line in wrap_korean(body,bf,944):d.text((68,y),line,font=bf,fill=MUTED);y+=lg
    y+=12
    for line in wrap_korean(highlight,bb,944):draw_inline_marker(d,68,y,line,bb);y+=lg
    if y>1040:raise ValueError(f'body exceeds safe area: {y}')
    output.parent.mkdir(parents=True,exist_ok=True);c.convert('RGB').save(output,'PNG',optimize=True)
    return {'bottom_y':y,'title_size':ts}


def render_closing_card(*, background: Path, list_image: Path, quote_white: str, quote_highlight: str, profile: str, output: Path, black_font: Path, logo_path: Path):
    if file_hash(background)==file_hash(list_image):raise ValueError('closing background must differ from _list_')
    bg=crop_fill(Image.open(background),W,H);bg=ImageEnhance.Brightness(bg).enhance(.56).convert('RGBA');veil=Image.new('RGBA',(W,H),(3,14,24,65));bg=Image.alpha_composite(bg,veil);d=ImageDraw.Draw(bg)
    qf=font(black_font,GENERAL_CLOSING_QUOTE_PX)
    if max(qf.getlength(line) for line in (quote_white,quote_highlight))>860:raise ValueError('50px closing quote does not fit; revise semantic line breaks')
    for text,y,marked in [(quote_white,330,False),(quote_highlight,455,True)]:
        b=d.textbbox((0,0),text,font=qf);x=(W-(b[2]-b[0]))//2-b[0]
        if marked:
            pb=d.textbbox((x,y),text,font=qf);d.rectangle((pb[0]-23,pb[1]-14,pb[2]+23,pb[3]+14),fill=TEAL);d.text((x,y),text,font=qf,fill=NAVY)
        else:d.text((x,y),text,font=qf,fill=WHITE)
    pf=font(black_font,GENERAL_PROFILE_PX);b=d.textbbox((0,0),profile,font=pf);d.text(((W-(b[2]-b[0]))//2-b[0],655),profile,font=pf,fill=PROFILE)
    logo=Image.open(logo_path).convert('RGBA');tw=220;logo=logo.resize((tw,round(logo.height*tw/logo.width)),Image.Resampling.LANCZOS);bg.alpha_composite(logo,((W-tw)//2,909))
    output.parent.mkdir(parents=True,exist_ok=True);bg.convert('RGB').save(output,'PNG',optimize=True)
