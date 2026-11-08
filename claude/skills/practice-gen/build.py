# Construeix practice JSON + reescriu el cos .md d'una lliçó a partir de gen/lessons/<slug>.py
import json, re, sys, glob, importlib.util
R = '/home/claude/hubesol'
BLANK = '<span class="blank">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>'
P20 = [0,1,2,3,1,2,3,0,2,3,0,1,3,0,1,2,0,1,2,3]
LONG = {'won’t':'will not','wouldn’t':'would not','don’t':'do not','doesn’t':'does not','didn’t':'did not',
        'isn’t':'is not','aren’t':'are not','wasn’t':'was not','weren’t':'were not','hadn’t':'had not',
        'haven’t':'have not','hasn’t':'has not','can’t':'cannot','couldn’t':'could not','shouldn’t':'should not',
        'mustn’t':'must not','needn’t':'need not','mightn’t':'might not','I’m':'I am','it’s':'it is'}

def variants(ans):
    out = []
    for a in ans:
        for v in (a, a.replace('’', "'"), a.replace('’', '')):
            if v not in out: out.append(v)
        lf = a
        for k, v in LONG.items(): lf = re.sub(r'(?<![A-Za-z])' + re.escape(k) + r'(?![A-Za-z])', v, lf)
        if lf != a and lf not in out: out.append(lf)
    return out

def parse_fill(s):
    m = re.search(r'\[\[(.+?)\]\]', s)
    ans = m.group(1).split('|')
    return s[:m.start()].rstrip(), s[m.end():].lstrip(), ans

def place(item, pos):
    use, text, ch, reasons, explain = item
    assert len(ch) == 4 and len(reasons) == 3, text
    choices = ch[1:]; wr = list(reasons)
    choices.insert(pos, ch[0]); wr.insert(pos, '')
    return use, text, choices, wr, explain

def err_item(sent, corr):
    toks = [x.replace('_', '\u00a0') for x in sent.split(' ')]
    idx = [i for i, t in enumerate(toks) if '*' in t]
    assert len(idx) == 1, sent
    i = idx[0]; toks[i] = toks[i].replace('*', '')
    return toks, i

def build(slug):
    spec = importlib.util.spec_from_file_location('L', f'/home/claude/gen/lessons/{slug}.py')
    L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    d = {'tense': slug, 'lessonTitle': L.TITLE,
         'grammar': {'orderAux': {'words': L.AUX[0], 'label': L.AUX[1], 'primary': L.AUX[2]}}}
    t, sub, items = L.GAP
    qs = []
    for use, s, hint, ex in items:
        b, a, ans = parse_fill(s)
        qs.append({'use': use, 'before': b, 'after': a, 'hint': hint, 'answers': variants(ans), 'display': ans[0], 'explain': ex})
    d['gapFill'] = {'title': t, 'subtitle': sub, 'questions': qs}
    t, sub, items = L.ORDER
    ss = []
    for it in items:
        use, s = it[0], it[1]; o = {'use': use, 'tokens': s.split(' ')}
        if len(it) > 2 and it[2]: o['alts'] = [x.split(' ') for x in it[2]]
        ss.append(o)
    d['wordOrder'] = {'title': t, 'subtitle': sub, 'sentences': ss}
    m = dict(L.MATCH); pairs = m.pop('pairs')
    d['matching'] = {**m, 'pairs': [{'left': a, 'right': b} for a, b in pairs]}
    t, sub, items = L.MC
    qs = []
    for k, it in enumerate(items):
        use, text, ch, wr, ex = place(it, P20[k])
        qs.append({'use': use, 'text': text.replace('___', BLANK), 'choices': ch, 'correct': ch.index(it[2][0]), 'wrongReasons': wr, 'explain': ex})
    d['timedMC'] = {'title': t, 'subtitle': sub, 'timeLimit': 15, 'showHintVerb': False, 'questions': qs}
    t, sub, items = L.ERR
    its = []
    for typ, s, corr, msg in items:
        toks, i = err_item(s, corr)
        its.append({'tokens': toks, 'errorIndex': i, 'correction': corr, 'type': typ, 'message': msg})
    d['errorCorrection'] = {'title': t, 'subtitle': sub, 'items': its}
    lc = L.LC; ck, cl = lc['custom']
    items = []
    for use, s, hint, ex, wn in lc['fill']:
        b, a, ans = parse_fill(s)
        items.append({'type': 'fill', 'use': use, 'sentText': f'{b} {{{{blank}}}} {a}'.strip(), 'hint': hint,
                      'answers': variants(ans), 'display': ans[0], 'explain': ex, 'wrongNote': wn})
    for it in lc['order']:
        o = {'type': 'order', 'use': it[0], 'tokens': it[1].split(' ')}
        if len(it) > 2 and it[2]: o['alts'] = [x.split(' ') for x in it[2]]
        items.append(o)
    for typ, key, pp in ((ck, 'customItems', [1,3,0,2]), ('mc', 'mc', [2,0,3,1])):
        for k, it in enumerate(lc[key]):
            use, text, ch, wr, ex = place(it, pp[k])
            items.append({'type': typ, 'use': use, 'text': text.replace('___', '{{blank}}'), 'choices': ch,
                          'correct': ch.index(it[2][0]), 'wrongReasons': wr, 'explain': ex})
    for use, s, corr, msg in lc['error']:
        toks, i = err_item(s, corr)
        items.append({'type': 'error', 'use': use, 'tokens': toks, 'errorIndex': i, 'correction': corr, 'message': msg})
    d['levelCheck'] = {'title': 'How well do you know it?', 'subtitle': lc['subtitle'],
                       'categoryLabels': {'fill': 'Fill in the blank', 'order': 'Word order', ck: cl, 'mc': 'Grammar choices', 'error': 'Spot the mistake'},
                       'categoryOrder': ['fill', 'order', ck, 'mc', 'error'], 'items': items}
    json.dump(d, open(f'{R}/src/data/practice/{slug}-practice.json', 'w'), ensure_ascii=False, indent=2)
    if hasattr(L, 'QUIZ_COMMON'):
        qp = f'{R}/src/data/quizzes/{slug}-quiz-1.json'
        qz = json.load(open(qp))
        for n, c in L.QUIZ_COMMON.items():
            qz['items'][n]['common'] = [{'answer': a, 'why': w} for a, w in c]
        json.dump(qz, open(qp, 'w'), ensure_ascii=False, indent=2)
    p = glob.glob(f'{R}/src/content/lessons/*/{slug}.md')[0]
    txt = open(p).read()
    fm, body = re.match(r'---\n(.*?)\n---\n', txt, re.S).group(1), None
    fm = re.sub(r'^next:.*\n?', '', fm, flags=re.M)
    nt, nh = L.NEXT
    fm = fm.replace('\ndraft:', f'\nnext: {{ title: "{nt}", href: "{nh}" }}\ndraft:')
    if 'next:' not in fm: fm += f'\nnext: {{ title: "{nt}", href: "{nh}" }}'
    for k, v in getattr(L, 'FM', {}).items():
        fm = re.sub(rf'^{k}: .*$', f'{k}: {json.dumps(v, ensure_ascii=False)}', fm, flags=re.M)
    open(p, 'w').write(f'---\n{fm}\n---\n\n{L.BODY.strip()}\n')
    print('built', slug)

if __name__ == '__main__':
    for s in sys.argv[1:]: build(s)
