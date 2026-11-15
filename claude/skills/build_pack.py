#!/usr/bin/env python3
"""Genera public/packs/<slug>-lesson-pack.pdf (resum + worksheet + answer key).
Ús: python3 claude/skills/build_pack.py <hub> <slug>"""
import sys, json, re
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.styles import ParagraphStyle
R = '/home/claude/hubesol'
hub, slug = sys.argv[1], sys.argv[2]
md = open(f'{R}/src/content/lessons/{hub}/{slug}.md', encoding='utf8').read()
fm, body = md.split('---', 2)[1:]
import yaml
f = yaml.safe_load(fm)
quiz = json.load(open(f'{R}/src/data/quizzes/{slug}-quiz-1.json'))
INDIGO = colors.HexColor('#4338ca')
def clean(t):
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t); t = re.sub(r'\*(.+?)\*', r'<i>\1</i>', t)
    return t.replace('→', '-&gt;').replace('&', '&amp;').replace('&amp;gt;', '&gt;').replace('<b>', '<b>')
base = ParagraphStyle('b', fontName='Helvetica', fontSize=10.5, leading=15)
h1 = ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=22, leading=26, spaceAfter=4)
h2 = ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=INDIGO, spaceBefore=10, spaceAfter=4)
small = ParagraphStyle('s', parent=base, fontSize=9.5, leading=13)
url = f'hubesol.com/grammar/{f["hubSlug"]}/{slug}/'
def page(c, d):
    c.saveState(); w, h = A4
    c.setFillColor(INDIGO); c.roundRect(15*mm, h-22*mm, 8*mm, 8*mm, 2, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont('Helvetica-Bold', 11); c.drawString(17.5*mm, h-19.7*mm, 'H')
    c.setFillColor(colors.black); c.setFont('Helvetica-Bold', 11); c.drawString(25*mm, h-19.7*mm, 'HubESOL')
    c.setFont('Helvetica', 9); c.setFillColor(colors.grey); c.drawRightString(w-15*mm, h-19.7*mm, url)
    c.drawString(15*mm, 10*mm, f'(c) HubESOL - free to use and print in the classroom with attribution. {url}')
    c.drawRightString(w-15*mm, 10*mm, f'Page {d.page}'); c.restoreState()
doc = BaseDocTemplate(f'{R}/public/packs/{slug}-lesson-pack.pdf', pagesize=A4, title=f['title']+' - Lesson Pack', author='HubESOL')
doc.addPageTemplates([PageTemplate(frames=[Frame(15*mm, 16*mm, 180*mm, 245*mm, id='f')], onPage=page)])
S = []
S += [Paragraph(f['title'], h1), Paragraph(f'<font color="#4338ca"><b>CEFR {f["level"]}</b></font> &nbsp; Lesson Pack - summary, worksheet &amp; answer key', base)]
S += [Paragraph('Quick answer', h2)]
box = [Paragraph(clean(f['answerLead']), base)] + [Paragraph(f'{i}&nbsp; {clean(p)}', base) for i, p in enumerate(f['answerPoints'], 1)] + [Paragraph(clean(f['answerNote']), base)]
t = Table([[box]], colWidths=[180*mm]); t.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#eef2ff')), ('BOX', (0,0), (-1,-1), .6, INDIGO), ('LEFTPADDING', (0,0), (-1,-1), 8), ('TOPPADDING', (0,0), (-1,-1), 6), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
S.append(t)
rows = []
for l in body.split('\n'):
    if l.startswith('|'): rows.append(l)
    elif rows: break
if rows:
    S.append(Paragraph('At a glance', h2))
    data = [[Paragraph(clean(c.strip()), small) for c in r.strip('|').split('|')] for r in rows if not re.match(r'^\|[\s\-:|]+\|$', r)]
    n = len(data[0]); tb = Table(data, colWidths=[180*mm/n]*n)
    tb.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e0e7ff')), ('GRID', (0,0), (-1,-1), .4, colors.lightgrey), ('VALIGN', (0,0), (-1,-1), 'TOP')])); S.append(tb)
S.append(Paragraph('Learning objectives', h2))
for o in f['teacherObjectives']: S.append(Paragraph('&bull; ' + clean(o), base))
S.append(PageBreak())
S.append(Paragraph('Practice worksheet', h2))
S.append(Paragraph(f'Circle the correct option. {f["title"]} - CEFR {f["level"]}', small)); S.append(Spacer(1, 6))
S.append(Paragraph('Name: ______________________________ &nbsp;&nbsp;&nbsp;&nbsp; Date: __________________', base)); S.append(Spacer(1, 8))
mc = [i for i in quiz['items'] if i.get('type') != 'write'][:10]
for n, it in enumerate(mc, 1):
    q = Paragraph(f'<b>{n}.</b> {clean(it["question"])}', base)
    o = [Paragraph('ABCD'[k] + '. ' + clean(x), base) for k, x in enumerate(it['options'])]
    ot = Table([[o[0], o[1]], [o[2], o[3]]], colWidths=[90*mm, 90*mm])
    S.append(KeepTogether([q, ot, Spacer(1, 4)]))
S.append(PageBreak())
S.append(Paragraph('Answer key', h2))
for n, it in enumerate(mc, 1):
    a = it['answer']
    S.append(Paragraph(f'<b>{n}. {"ABCD"[a]}</b> - {clean(it["options"][a])}. {clean(it["explanations"][a])}', small)); S.append(Spacer(1, 3))
doc.build(S)
print('pack', slug)
