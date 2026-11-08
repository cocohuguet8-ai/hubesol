# extend.py <file> <section> : allarga explicacions curtes afegint una frase segons el tipus
import sys, importlib.util as u
p, sec, minlen = sys.argv[1], sys.argv[2], int(sys.argv[3])
ext = eval(open(sys.argv[4]).read())
s=u.spec_from_file_location('L',p);L=u.module_from_spec(s);s.loader.exec_module(L)
t=open(p).read()
items = getattr(L, sec)[2] if sec in ('MC','ERR','GAP') else None
idx = {'MC':4,'ERR':3,'GAP':3}[sec]
n=0
for it in items:
    ex=it[idx]
    if len(ex)<minlen:
        add=ext.get(it[0], ext.get('*'))
        new=ex.rstrip()+add
        for q in ("'"+ex+"')", "'"+ex+"'),"):
            if q in t:
                t=t.replace(q, q.replace(ex,new),1); n+=1; break
open(p,'w').write(t); print('extended',n)
