# Compara cada lliçó de HubESOL amb les mostres «good» (Past Simple 9,5 i Past Continuous 9,6).
# Ús: python3 claude/skills/audit_good.py .   (des de l arrel del repo)
import json,glob,os,re,sys,collections
R=sys.argv[1]; G=['past-simple','past-continuous']
LIST={'gapFill':'questions','wordOrder':'sentences','matching':'pairs','timedMC':'questions','errorCorrection':'items','levelCheck':'items'}
gold={g:json.load(open(f'{R}/src/data/practice/{g}-practice.json')) for g in G}
def tkey(a,it): return (a, it.get('type') if a=='levelCheck' else None)
always=collections.defaultdict(lambda:None); union=collections.defaultdict(set); goldEmpty=collections.defaultdict(set)
for g in gold.values():
    for a,l in LIST.items():
        for it in g[a][l]:
            k=tkey(a,it); ks=set(it)
            always[k]=ks if always[k] is None else always[k]&ks; union[k]|=ks
            for f,v in it.items():
                if v in ('',[],None): goldEmpty[k].add(f)
def L(d,a,f): 
    v=[len(it[f]) for it in d[a][LIST[a]] if isinstance(it.get(f),str)]; return sum(v)/len(v) if v else 0
gl={(a,f):sum(L(g,a,f) for g in gold.values())/2 for a,f in [('gapFill','explain'),('timedMC','explain'),('errorCorrection','message'),('levelCheck','explain')]}
out={}
for f in sorted(glob.glob(f'{R}/src/data/practice/*-practice.json')):
    s=os.path.basename(f)[:-14]
    if s in G: continue
    d=json.load(open(f)); P=collections.Counter()
    for a,l in LIST.items():
        items=d.get(a,{}).get(l,[])
        if len(items)!=20: P[f'{a}: {len(items)} ítems (good 20)']+=1
        for i,it in enumerate(items):
            k=tkey(a,it)
            if always[k] is None: P[f'{a}: tipus «{k[1]}» que no és a les mostres']+=1; continue
            for m in sorted(always[k]-set(it)): P[f'{a}: falta «{m}»']+=1
            for x in sorted(set(it)-union[k]): P[f'{a}: camp extra «{x}»']+=1
            for fld,v in it.items():
                if v in ('',[],None) and fld not in goldEmpty[k]: P[f'{a}: «{fld}» buit']+=1
            if a=='timedMC' or (a=='levelCheck' and 'choices' in it):
                ch=it.get('choices',[]); wr=it.get('wrongReasons') or {}
                n=len([x for x in (wr.values() if isinstance(wr,dict) else wr) if x])
                if n<len(ch)-1: P[f'{a}: falten explicacions d\'opcions incorrectes']+=1
                for c in ch:
                    if re.search(r'\b(are|is|do|does|did|was|were)\s+(you|he|she|they|we|it|I)\s+been\b',str(c),re.I): P[f'{a}: forma inexistent «{c}»']+=1
    t=d['timedMC']
    if t.get('timeLimit')!=15: P[f'timedMC: timeLimit {t.get("timeLimit")} (good 15)']+=1
    if t.get('showHintVerb') is not False: P[f'timedMC: showHintVerb {t.get("showHintVerb")} (good false)']+=1
    if len(d['levelCheck'].get('categoryOrder',[]))!=5: P['levelCheck: no té 5 categories']+=1
    for (a,fl),gv in gl.items():
        v=L(d,a,fl)
        if v<0.6*gv: P[f'{a}.{fl} massa curt: {v:.0f} car. de mitjana (good {gv:.0f})']+=1
    out[s]=P
for s,P in out.items():
    print(f'## {s}'); [print(f'  - {k} ×{n}') for k,n in P.items()] or print('  OK')
# --- lliçó .md i quiz vs mostres good ---
def fm(p):
    t=open(p).read(); m=re.match(r'---\n(.*?)\n---\n(.*)',t,re.S)
    keys=[l.split(':')[0] for l in m.group(1).splitlines() if re.match(r'^\w',l)]
    return set(keys),len(re.findall(r'^##+ ',m.group(2),re.M)),len(m.group(2))
def qz(s):
    it=json.load(open(f'{R}/src/data/quizzes/{s}-quiz-1.json'))['items']; return len(it), set().union(*[set(q) for q in it])
gl={s:fm(f'{R}/src/content/lessons/verb-tenses/{s}.md') for s in G}; gq={s:qz(s) for s in G}
gk=gl[G[0]][0]&gl[G[1]][0]; mh=min(v[1] for v in gl.values()); ml=min(v[2] for v in gl.values()); mq=min(v[0] for v in gq.values()); qk=gq[G[0]][1]&gq[G[1]][1]
print('\n# Lliçó i quiz')
for s in out:
    p=glob.glob(f'{R}/src/content/lessons/*/{s}.md')[0]; k,h,Ln=fm(p); n,ks=qz(s); P=[]
    if gk-k: P.append(f'frontmatter sense {sorted(gk-k)}')
    if h<mh: P.append(f'{h} apartats (good ≥{mh})')
    if Ln<0.6*ml: P.append(f'text {Ln} car. (good ≥{ml})')
    if n<mq: P.append(f'quiz {n} preguntes (good ≥{mq})')
    if qk-ks: P.append(f'quiz sense {sorted(qk-ks)}')
    print(f'## {s}:', '; '.join(P) or 'OK')
