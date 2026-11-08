import importlib.util, re, sys, glob, os
exec(open('/home/claude/gen/build.py').read().split('def build(slug)')[0])
bad=re.compile(r"\b(must|can|might|could|should|will|would|may|can’t|mustn’t|couldn’t|shouldn’t|won’t)\s+to\b",re.I)
def norm(x): return re.sub(r"[^\w’' ]"," ",x.lower()).split()
def load(slug):
    sp=importlib.util.spec_from_file_location('L',f'lessons/{slug}.py'); L=importlib.util.module_from_spec(sp); sp.loader.exec_module(L); return L
out=[]
slugs=sys.argv[1:] or sorted(os.path.basename(f)[:-3] for f in glob.glob('lessons/*.py'))
for slug in slugs:
    L=load(slug)
    items=[('EC',)+tuple(x) for x in L.ERR[2]]+[('LC',)+tuple(x) for x in L.LC['error']]
    for n,(src,typ,s,corr,msg) in enumerate(items,1):
        toks,i,spn,_p,_s=err_item(s,corr); sp=spn or [i,i]; corr=(_p if not corr.startswith(_p) else '')+corr+(_s if not corr.endswith(_s) else '')
        fx=' '.join(toks[:sp[0]]+[corr]+toks[sp[1]+1:])
        w=norm(fx); fxs=' '.join(w)
        reasons=[]
        if bad.search(fx): reasons.append('modal+to')
        if any(w[k]==w[k+1] and w[k] not in('had','that') for k in range(len(w)-1)): reasons.append('repeat')
        quotes=[' '.join(norm(q)) for q in re.findall(r"‘([^’]*(?:’[a-z][^’]*)*)’",msg)]
        quotes=[q for q in quotes if len(q.split())>=2]
        if quotes and not any(q in fxs for q in quotes): reasons.append('msg≠fix')
        if s.rstrip()[-1] in '.!?' and fx.rstrip()[-1] not in '.!?': reasons.append('nopunct')
        if reasons: out.append(f"{slug} {src}{n} [{','.join(reasons)}] {s}  →{corr}  ⇒ {fx}  ||{msg}")
print(len(out)); print('\n'.join(out))
