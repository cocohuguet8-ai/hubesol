import re,sys
from docx import Document
from docx.shared import Pt,RGBColor,Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
PINK=RGBColor(0xEE,0x15,0x59); DARK=RGBColor(0x1F,0x1F,0x24); GREY=RGBColor(0x6B,0x6B,0x72)
HF='Poppins'; BF='Poppins'
def font(r,name,size,color=None,bold=None,italic=None):
    r.font.name=name; r._element.rPr.rFonts.set(qn('w:eastAsia'),name)
    r.font.size=Pt(size)
    if color is not None: r.font.color.rgb=color
    if bold is not None: r.bold=bold
    if italic is not None: r.italic=italic
def shade(el,fill):
    p=el.get_or_add_pPr() if hasattr(el,'get_or_add_pPr') else el
    s=OxmlElement('w:shd'); s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),fill); p.append(s)
def cellshade(cell,fill):
    tcPr=cell._element.get_or_add_tcPr(); s=OxmlElement('w:shd'); s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),fill); tcPr.append(s)
def inline(p,text,size=10.5,color=DARK,base_bold=False):
    toks=re.split(r'(\*\*[^*]+\*\*|\[[^\]]+\]\{\.underline\}|\*[^*]+\*)',text)
    for t in toks:
        if not t: continue
        if t.startswith('**'): r=p.add_run(t[2:-2]); font(r,BF,size,PINK if False else color,True)
        elif t.startswith('['): r=p.add_run(t[1:t.index(']')]); font(r,BF,size,color,base_bold); r.underline=True
        elif t.startswith('*'): r=p.add_run(t[1:-1]); font(r,BF,size,color,base_bold,True)
        else: r=p.add_run(t); font(r,BF,size,color,base_bold)
def border(p,side,color='EE1559',sz=12):
    pPr=p._p.get_or_add_pPr(); b=OxmlElement('w:pBdr'); e=OxmlElement('w:'+side)
    e.set(qn('w:val'),'single'); e.set(qn('w:sz'),str(sz)); e.set(qn('w:space'),'4'); e.set(qn('w:color'),color); b.append(e); pPr.append(b)
src=open(sys.argv[1],encoding='utf8').read().split('\n'); out=sys.argv[2]; teacher=len(sys.argv)>3
d=Document(); s=d.sections[0]; s.page_width=Cm(21); s.page_height=Cm(29.7)
s.left_margin=s.right_margin=Cm(2); s.top_margin=Cm(1.4); s.bottom_margin=Cm(1.3)
st=d.styles['Normal']; st.font.name=BF; st.font.size=Pt(10.5)
# header band
hp=s.header.paragraphs[0]; r=hp.add_run('ch'); font(r,HF,13,PINK,True); r=hp.add_run(' Formació'); font(r,HF,13,GREY,False)
r=hp.add_run('\tGrammar & Vocabulary · A2'); font(r,HF,8,GREY)
hp.paragraph_format.tab_stops.add_tab_stop(Cm(17),alignment=2)
border(hp,'bottom','EE1559',8)
fp=s.footer.paragraphs[0]; fp.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=fp.add_run('chformacio.com · Successful English Teaching'); font(r,HF,8,GREY)
i=0; prevhead=False
def para(txt='',after=3,before=0):
    p=d.add_paragraph(); p.paragraph_format.space_after=Pt(after); p.paragraph_format.space_before=Pt(before); p.paragraph_format.line_spacing=1.1
    return p
while i<len(src):
    l=src[i].rstrip()
    if not l.strip() or l.strip()=='---': i+=1; continue
    if l.startswith('# '):
        p=para(after=2,before=2); r=p.add_run(l[2:].upper()); font(r,HF,20,PINK,True); prevhead=False
    elif l.startswith('## '):
        t=l[3:]; p=para(after=6,before=14)
        if t.startswith('PART B') and not teacher: p.paragraph_format.page_break_before=True
        m=re.match(r'(PART [AB])\s*·\s*(.*)',t)
        if m:
            r=p.add_run(m.group(1)); font(r,HF,8.5,GREY,True); p.add_run('\n'); r=p.add_run(m.group(2).capitalize() if m.group(2).isupper() else m.group(2)); font(r,HF,14,DARK,True)
            # keep case: restore original nice casing
            r.text=m.group(2).split(':')[0].title()+(': '+m.group(2).split(':',1)[1].strip().lower() if ':' in m.group(2) else '') if m.group(2).isupper() else m.group(2)
        else:
            r=p.add_run(t); font(r,HF,14,DARK,True)
        border(p,'bottom','EE1559',10); prevhead=False
    elif l.startswith('Name:'):
        p=para(after=8); r=p.add_run(l.replace('  ','      ')); font(r,BF,10,GREY)
    elif re.match(r'^\*\*\d+ ',l):
        m=re.match(r'^\*\*(\d+) (.*)\*\*$',l); p=para(after=4,before=15)
        r=p.add_run(m.group(1)+'  '); font(r,HF,12,PINK,True)
        inline(p,m.group(2),10.5,DARK,True); p.paragraph_format.keep_with_next=True; prevhead=True
        if m.group(1)=='4' and not teacher: p.paragraph_format.page_break_before=True
    elif l.startswith('> '):
        block=[]
        while i<len(src) and src[i].startswith('> '): block.append(src[i][2:]); i+=1
        t=d.add_table(rows=1,cols=1); c=t.rows[0].cells[0]; cellshade(c,'FDE8EF'); c.paragraphs[0].text=''
        for k,b in enumerate(block):
            p=c.paragraphs[0] if k==0 else c.add_paragraph(); p.paragraph_format.space_after=Pt(2); p.paragraph_format.line_spacing=1.3; inline(p,b,10.5)
        para(after=2); prevhead=False; continue
    elif l.startswith('|'):
        rows=[]
        while i<len(src) and src[i].startswith('|'):
            if not re.match(r'^\|[-| ]+\|$',src[i]): rows.append([c.strip() for c in src[i].strip('|').split('|')])
            i+=1
        if rows[0][0]=='' and rows[0][1:]==['A','B','C']:
            t=d.add_table(rows=len(rows)-1,cols=4); t.autofit=False
            tblPr=t._tbl.tblPr
            for ri,row in enumerate(rows[1:]):
                tr=t.rows[ri]; trPr=tr._tr.get_or_add_trPr(); trPr.append(OxmlElement('w:cantSplit'))
                for ci,w_ in enumerate((Cm(2.2),Cm(4.9),Cm(4.9),Cm(4.9))): tr.cells[ci].width=w_
                for ci,tx in enumerate(row):
                    c=tr.cells[ci]; c.paragraphs[0].text=''; p=c.paragraphs[0]
                    p.paragraph_format.space_before=Pt(3); p.paragraph_format.space_after=Pt(3)
                    tcPr=c._element.get_or_add_tcPr(); b=OxmlElement('w:tcBorders'); e=OxmlElement('w:bottom')
                    e.set(qn('w:val'),'single'); e.set(qn('w:sz'),'4'); e.set(qn('w:color'),'F6B8CC'); b.append(e); tcPr.append(b)
                    if ri%2==0: cellshade(c,'FFF3F7')
                    if ci==0:
                        p.alignment=WD_ALIGN_PARAGRAPH.CENTER; r=p.add_run(tx); font(r,HF,9.5,PINK,True)
                    else:
                        r=p.add_run('ABC'[ci-1]+'   '); font(r,HF,9.5,PINK,True)
                        r=p.add_run(tx); font(r,BF,10,DARK,(ri==0 and ci==1))
            para(after=2); prevhead=False; continue
        t=d.add_table(rows=len(rows),cols=len(rows[0])); t.style='Table Grid'
        for ri,row in enumerate(rows):
            for ci,tx in enumerate(row):
                c=t.rows[ri].cells[ci]; c.paragraphs[0].text=''; p=c.paragraphs[0]; p.paragraph_format.space_after=Pt(1)
                if ri==0: cellshade(c,'EE1559'); inline(p,tx,9.5,RGBColor(255,255,255),True)
                else: inline(p,tx,9.5)
                if ci==0 and ri>0: cellshade(c,'FDE8EF')
        para(after=2); prevhead=False; continue
    elif re.match(r'^\d+ .+ ____ [A-H] ',l):
        rows=[]
        while i<len(src) and re.match(r'^\d+ .+ ____ [A-H] ',src[i]):
            m=re.match(r'^(\d+) (.+?) ____ ([A-H]) (.*)$',src[i]); rows.append(m.groups()); i+=1
        t=d.add_table(rows=len(rows),cols=2); t.autofit=False
        for ri,(n,w,k,df) in enumerate(rows):
            tr=t.rows[ri]; trPr=tr._tr.get_or_add_trPr(); cs=OxmlElement('w:cantSplit'); trPr.append(cs)
            for ci,w_ in enumerate((Cm(7.5),Cm(9.5))): tr.cells[ci].width=w_
            c0,c1=tr.cells; cellshade(c0,'FDE8EF')
            p=c0.paragraphs[0]; p.paragraph_format.space_after=Pt(4); p.paragraph_format.keep_with_next=True
            r=p.add_run(n+'  '); font(r,BF,10.5,PINK,True); r=p.add_run(w+'  ______'); font(r,BF,10.5,DARK)
            p=c1.paragraphs[0]; p.paragraph_format.space_after=Pt(4); p.paragraph_format.keep_with_next=True
            r=p.add_run(k+'  '); font(r,BF,10.5,PINK,True); r=p.add_run(df); font(r,BF,10.5,DARK)
        for c in t.rows[-1].cells: c.paragraphs[0].paragraph_format.keep_with_next=False
        para(after=2); prevhead=False; continue
    elif prevhead and ' · ' in l and not re.match(r'^\d',l):
        t=d.add_table(rows=1,cols=1); c=t.rows[0].cells[0]; cellshade(c,'FDE8EF'); p=c.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
        inline(p,l.replace('`',''),10.5,PINK,True); para(after=2); prevhead=False
    else:
        p=para(after=4)
        m=re.match(r'^(\d+|[A-H]:|Example:)\s+(.*)',l)
        if m and not teacher:
            r=p.add_run(m.group(1)+'  '); font(r,BF,10.5,PINK,True); inline(p,m.group(2),10.5)
        else:
            inline(p,l,10.5)
        if 'Dubtes' in l: pass
        prevhead=False
    i+=1
d.save(out)
