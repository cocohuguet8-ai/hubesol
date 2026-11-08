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
    # *word* = one-tile mistake; *two words* = mistake spanning several tiles (errorSpan)
    a = sent.index('*'); b = sent.index('*', a + 1)
    assert sent.count('*') == 2, sent
    pre, mid, post = sent[:a], sent[a+1:b], sent[b+1:]
    pt = pre.split(' ')[:-1] if pre.endswith(' ') or pre == '' else pre.split(' ')
    # glue punctuation directly attached to the starred part
    pre_toks = [t for t in pre.split(' ')]
    left = pre_toks[-1] if pre_toks else ''
    pre_toks = pre_toks[:-1]
    mid_toks = mid.split(' ')
    mid_toks[0] = left + mid_toks[0]
    post_toks = post.split(' ')
    mid_toks[-1] = mid_toks[-1] + post_toks[0]
    post_toks = post_toks[1:]
    toks = [x.replace('_', '\u00a0') for x in pre_toks + mid_toks + post_toks]
    i = len(pre_toks); span = [i, i + len(mid_toks) - 1]
    return toks, i, (span if span[1] > span[0] else None), left, post.split(' ')[0]


AUXSET = set("""will won’t ’ll would wouldn’t ’d had hadn’t have has haven’t hasn’t can can’t could couldn’t may might
must mustn’t should shouldn’t ought need needn’t is are was were be been being do does did don’t doesn’t didn’t""".split())
FORM_BY_HUB = {'prepositions': 'preposition', 'articles': 'article', 'nouns-determiners': 'word'}
FORM_BY_SLUG = {'reflexive-pronouns': 'pronoun', 'compound-nouns': 'noun'}
NO_AUX = {'inversion-in-conditionals'}

def hub_of(slug):
    import glob, re
    for f in glob.glob(f'{R}/src/content/lessons/*/{slug}.md'):
        m = re.search(r'^hubSlug: "([^"]+)"', open(f).read(), re.M)
        if m: return m.group(1)
    return ''

COMMON = set('''i you he she it we they this that these those there here what when where why who which how a an the my your his her our their
some any every each no all both many much one do does did is are was were be have has had will would can could should must may might
not never always yesterday today tomorrow last next if unless when as please let let’s don’t'''.split())

KNOWN = set('''Paris London Rome Madrid Barcelona Girona Lleida Tarragona Valencia Lisbon Berlin Tokyo York Spain France Italy Germany Portugal
Japan China England Britain Scotland Wales Ireland Europe Asia Africa America English French Spanish Catalan German Italian Chinese Japanese
Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April June July August September October November December
Christmas Easter Anna Ben Tom Sam Pau Marc Laia Joan Nil Marta Maria Pere Pol Biel Sara Lucas Leo Lucy Grandma Grandpa Mum Dad Mr Mrs Ms'''.split())

def proper_nouns(L):
    import re
    texts = [L.BODY]
    def walk(o):
        if isinstance(o, str): texts.append(o)
        elif isinstance(o, dict): [walk(v) for v in o.values()]
        elif isinstance(o, (list, tuple)): [walk(v) for v in o]
    for name in ('GAP', 'ORDER', 'MATCH', 'MC', 'ERR', 'LC'): walk(getattr(L, name))
    blob = '\n'.join(texts)
    lower = set(re.findall(r"\b[a-z][\w’']*", blob))
    midcap = set(re.findall(r"(?<=[a-z,;] )([A-Z][\wÀ-ÿ]+)", blob))
    firsts = set()
    for it in list(L.ORDER[2]) + list(L.LC['order']):
        w = it[1].split(' ')[0].rstrip('.,!?')
        if w[:1].isupper() and "’" not in w and "'" not in w and (w in KNOWN or (w in midcap and w.lower() not in lower and w.lower() not in COMMON)): firsts.add(w)
    return sorted(firsts)

def build(slug):
    spec = importlib.util.spec_from_file_location('L', f'/home/claude/gen/lessons/{slug}.py')
    L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L)
    d = {'tense': slug, 'lessonTitle': L.TITLE,
         'grammar': {'orderAux': {'words': [] if slug in NO_AUX else [w for w in L.AUX[0] if w.lower() in AUXSET],
                                  'label': L.AUX[1], 'primary': L.AUX[2] if L.AUX[2].lower() in AUXSET and slug not in NO_AUX else '',
                                  'proper': proper_nouns(L)}}}
    hub = hub_of(slug); form = FORM_BY_SLUG.get(slug) or FORM_BY_HUB.get(hub)
    t, sub, items = L.GAP
    qs = []
    for use, s, hint, ex in items:
        b, a, ans = parse_fill(s)
        qs.append({'use': use, 'before': b, 'after': a, 'hint': hint, 'answers': variants(ans), 'display': ans[0], 'explain': ex})
    d['gapFill'] = {'title': t, 'subtitle': sub, 'questions': qs}
    if form: d['gapFill']['formLabel'] = form
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
        toks, i, sp, _pre, _suf = err_item(s, corr)
        corr = (_pre if not corr.startswith(_pre) else '') + corr + (_suf if not corr.endswith(_suf) else '')
        o = {'tokens': toks, 'errorIndex': i, 'correction': corr, 'type': typ, 'message': msg}
        if sp: o['errorSpan'] = sp
        its.append(o)
    d['errorCorrection'] = {'title': t, 'subtitle': sub, 'items': its}
    lc = L.LC; ck, cl = lc['custom']
    items = []
    for use, s, hint, ex, wn in lc['fill']:
        b, a, ans = parse_fill(s)
        items.append({'type': 'fill', 'use': use, 'sentText': (f'{b} {{{{blank}}}}' + ('' if a[:1] in '.,!?;:' else ' ') + a).strip(), 'hint': hint,
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
        toks, i, sp, _pre, _suf = err_item(s, corr)
        corr = (_pre if not corr.startswith(_pre) else '') + corr + (_suf if not corr.endswith(_suf) else '')
        o = {'type': 'error', 'use': use, 'tokens': toks, 'errorIndex': i, 'correction': corr, 'message': msg}
        if sp: o['errorSpan'] = sp
        items.append(o)
    d['levelCheck'] = {'title': 'How well do you know it?', 'subtitle': lc['subtitle'],
                       'categoryLabels': {'fill': 'Fill in the blank', 'order': 'Word order', ck: cl, 'mc': 'Grammar choices', 'error': 'Spot the mistake'},
                       'categoryOrder': ['fill', 'order', ck, 'mc', 'error'], 'items': items}
    if form: d['levelCheck']['formLabel'] = form
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
