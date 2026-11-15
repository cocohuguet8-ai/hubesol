# Auditoria SEMÀNTICA mecànica de les lliçons HubESOL: busca les classes d'errades que Learner Review troba repetidament.
# Ús (des de l'arrel del repo):  python3 claude/skills/audit_semantic.py .            (totes les lliçons)
#                                python3 claude/skills/audit_semantic.py . past-perfect since-vs-for
import json,glob,os,re,sys,collections
R=sys.argv[1]; ONLY=set(sys.argv[2:])
FUNC={'a','an','the','in','on','at','by','for','since','during','while','until','to','of','with','from','into','about','some','any','much','many','one','than','as','too','enough','few','little','all','both','each','every','no','who','which','that','whose','when','where','because','if','so','but','and','or','before','after','already','yet','just','still','ever','never','always','usually','often','not'}
CONTR=[('have','’ve'),('has','’s'),('had','’d'),('is','’s'),('are','’re'),('am','’m'),('will','’ll'),('would','’d'),('not','n’t')]
NOTVERB={'bring','sing','swing','sting','wing','string','cling','fling','sling','during','morning','evening','something','anything','nothing','everything','thing','king','spring','ring','wedding','building','meeting','feeling','shopping','cooking','swimming','running','reading','painting','clothing'}
EMB={'ask','asks','asked','know','knew','knows','wonder','wondered','wonders','say','said','tell','told','see','saw','remember','remembered','explain','explained','understand','understood','decide','decided','forget','forgot'}
PROP={'January','February','March','April','May','August','September','October','November','December','I','TV','Mum','Dad','Anna','Ben','Tom','Sam','Maria','Paul','Lucy','Girona','English','Spanish','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','June','July','London','Paris','Lisbon','Rome','Barcelona','Christmas'}
P=collections.defaultdict(list)   # slug -> [(classe, detall)]
def add(s,c,d): P[s].append((c,d))
def norm(x): return re.sub(r'[’\']',"'",x.lower()).strip()
def check_alts(s,where,tokens,alts):
    CANON={w.strip('.,?!') for w in tokens[1:] if w[0].isupper()}
    end=tokens[-1][-1] if tokens[-1][-1] in '.?!' else None
    if end is None: add(s,'ordre: frase sense signe final',f'{where} {tokens}')
    sub=re.compile(r'^(when|because|before|after|until|while|if|by|as|once|since|although)$',re.I)
    for a in alts or []:
        for i,w in enumerate(a[:-1]):
            if w[-1] in '.?!': add(s,'ordre: alternativa amb punt/interrogant a mig frase (la revisió final queda mal puntuada)',f'{where} {" ".join(a)}')
        if a[-1][-1] not in '.?!': add(s,'ordre: alternativa sense signe final',f'{where} {" ".join(a)}')
        if a[0][0].isupper() and a[0].strip('.,?!') not in PROP and not a[0].startswith('I’'): add(s,'ordre: alternativa començada amb majúscula',f'{where} {" ".join(a)}')
        for w in a[1:]:
            if w[0].isupper() and w.strip('.,?!') not in PROP and w.strip('.,?!') not in CANON and not w.startswith('I’') : add(s,'ordre: majúscula a mig frase a una alternativa',f'{where} {" ".join(a)}'); break
    # clàusula subordinada sense alternativa permutada
    q0=tokens[0].lower(); stmt=end=='.' and q0 not in ('who','what','when','where','why','how','which','do','does','did','is','are','was','were','have','has','had','can','could','will','would','should')
    has_clause=stmt and ((q0 in ('when','because','before','after','until','while','by') and any(w.endswith(',') for w in tokens[:-1])) or (q0 not in ('when','because','before','after','until','while','by') and any(2<=i<=len(tokens)-3 and w.lower() in ('when','because','before','after','until','while') for i,w in enumerate(tokens) if not (set(x.lower() for x in tokens[:i]) & EMB))))
    if has_clause and not alts: add(s,'ordre: frase amb dues clàusules sense alternativa (ordre permutat rebutjat)',f'{where} {" ".join(tokens)}')
def check_fill(s,where,it,ans,disp,hint,explain,use,extra_text=''):
    a=[norm(x) for x in ans]; d=norm(disp)
    if norm(use) in a or norm(use)==d: add(s,'etiqueta «use» que dóna la resposta',f'{where} use={use!r} resposta={disp!r}')

def check_mc(s,where,choices,correct,wr,text):
    if len(set(norm(c) for c in choices))!=len(choices): add(s,'opcions duplicades',f'{where} {choices}')
    if not (0<=correct<len(choices)): add(s,'índex correcte fora de rang',where)
    for c in choices:
        if ' ' in choices[correct] and not any(x.strip().startswith('to ') or re.fullmatch(r'[a-z]+ing',choices[correct].strip()) for x in choices) and re.fullmatch(r'[a-z]+ing',c.strip()) and c.strip() not in NOTVERB: add(s,'distractor impossible (-ing sol)',f'{where} {c!r}')
        if re.search(r'\b(are|is|do|does|did|was|were)\s+(you|he|she|they|we|it|I)\s+been\b',c,re.I): add(s,'distractor impossible',f'{where} {c!r}')
    wl=list(wr.values()) if isinstance(wr,dict) else (wr or [])
    if len([x for x in wl if x])<len(choices)-1: add(s,'falten wrongReasons',where)
    if wl and 0<=correct<len(wl) and wl[correct]: add(s,'wrongReason a l’opció correcta',where)
for f in sorted(glob.glob(f'{R}/src/data/practice/*-practice.json')):
    s=os.path.basename(f)[:-14]
    if ONLY and s not in ONLY: continue
    d=json.load(open(f))
    for i,q in enumerate(d.get('gapFill',{}).get('questions',[])):
        check_fill(s,f'gapFill Q{i+1}',q,q['answers'],q['display'],q.get('hint'),q.get('explain'),q.get('use',''))
    for i,q in enumerate(d.get('wordOrder',{}).get('sentences',[])):
        check_alts(s,f'wordOrder Q{i+1}',q['tokens'],q.get('alts'))
    for i,q in enumerate(d.get('timedMC',{}).get('questions',[])):
        check_mc(s,f'timedMC Q{i+1}',q['choices'],q['correct'],q.get('wrongReasons'),q['text'])
        if norm(q.get('use','')) in [norm(c) for c in q['choices']]: add(s,'etiqueta «use» coincideix amb una opció',f'timedMC Q{i+1}')
    for i,q in enumerate(d.get('levelCheck',{}).get('items',[])):
        w=f'levelCheck Q{i+1}({q["type"]})'
        if q['type']=='fill': check_fill(s,w,q,q['answers'],q['display'],q.get('hint'),q.get('explain'),q.get('use',''))
        elif q['type']=='order': check_alts(s,w,q['tokens'],q.get('alts'))
        elif 'choices' in q: check_mc(s,w,q['choices'],q['correct'],q.get('wrongReasons'),q.get('text',''))

def bad_open(l):
    pos=[m.start() for m in re.finditer(r'\*\*',l)]
    return [i for k,i in enumerate(pos) if k%2==0 and i>0 and l[i-1].isalnum() and i+2<len(l) and not l[i+2].isalnum() and l[i+2] not in ' *']
# lliçons .md: marques de negreta literals (** enganxat a lletra + apòstrof/puntuació) i taules desquadrades
for f in sorted(glob.glob(f'{R}/src/content/lessons/*/*.md')):
    s=os.path.basename(f)[:-3]
    if ONLY and s not in ONLY: continue
    for n,l in enumerate(open(f).read().splitlines(),1):
        for m in bad_open(l): add(s,'markdown: ** d’obertura enganxat a lletra i seguit de puntuació (asteriscs literals)',f'línia {n}: {l.strip()[:90]}')
        if l.count('**')%2: add(s,'markdown: nombre senar de ** a la línia',f'línia {n}: {l.strip()[:90]}')
tot=collections.Counter()
for s,l in P.items():
    print(f'## {s}: {len(l)} troballes')
    c=collections.Counter(k for k,_ in l)
    for k,n in c.items(): tot[k]+=n; print(f'  - {k} ×{n}  ex: {next(dd for kk,dd in l if kk==k)}')
print('\n# TOTAL per classe'); [print(f'{n:4d}  {k}') for k,n in tot.most_common()]
print(f'\nLliçons amb troballes: {len(P)}')
