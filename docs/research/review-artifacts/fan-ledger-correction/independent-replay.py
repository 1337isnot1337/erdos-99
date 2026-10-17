#!/usr/bin/env python3
"""Independent seed-63 correction checks; imports no repository code.

Geometry uses coordinates scaled by 35 and denominator-cleared inequalities.
Sector membership uses the explicit three finite regions and their complement,
not the proposed checker's polygon ray algorithm. Matchings use a separate
augmenting search. Exact numerical Schur checks use Fraction elimination.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json
import random
import subprocess
import sys
import time

REPO = None
SHA = None
QUNIT = 35 * 35


def check(ok, message):
    if not ok:
        raise RuntimeError(message)


def q(v):
    a, b = v
    return a*a + a*b + b*b


def physical_row(z):
    return (35*z[0]+7, 35*z[1]+5)


def physical_source(x):
    return (35*x[0], 35*x[1])


def segment_clearance(p, a, b):
    """Sign equals squared distance to scaled segment minus 35^2."""
    u = (p[0]-a[0], p[1]-a[1])
    d = (b[0]-a[0], b[1]-a[1])
    d2 = q(d)
    dot2 = 2*u[0]*d[0] + u[0]*d[1] + u[1]*d[0] + 2*u[1]*d[1]
    if dot2 <= 0:
        return q(u)-QUNIT
    if dot2 >= 2*d2:
        return q((u[0]-d[0], u[1]-d[1]))-QUNIT
    return 4*d2*(q(u)-QUNIT)-dot2*dot2


def sector(p):
    # Invoked only on points outside the fan, within the closed hull.
    u, v = p
    if u <= 70 and v <= 35:
        return 0  # AB rectangle in lattice coordinates.
    if u <= 35 and v >= 35:
        return 2  # CA strip, clipped by the hull.
    if u >= 35 and v >= 35 and u+v <= 105:
        return 3  # Open triangle abc, with edges already removed.
    return 1  # BC, the remaining connected sector.


def fixture(m):
    x = {(i,j) for i in range(m+1) for j in range(m+1-i)}
    corners = [(0,0),(35*m,0),(0,35*m)]
    hull_edges = list(zip(corners, corners[1:]+corners[:1]))
    y = set()
    for i in range(-3,m+4):
        for j in range(-3,m+4):
            p = physical_row((i,j))
            if p[0]>=0 and p[1]>=0 and sum(p)<=35*m:
                y.add((i,j))
            else:
                c = [segment_clearance(p,a,b) for a,b in hull_edges]
                check(all(t != 0 for t in c), f'collar equality {m,i,j}')
                if min(c)<0:
                    y.add((i,j))
    z = {r for r in y if min(physical_row(r))>0 and sum(physical_row(r))<35*m}
    o = y-z
    adj = {}
    inv = defaultdict(set)
    for p in x:
        p35 = physical_source(p)
        candidates = {(p[0]+a,p[1]+b) for a in range(-2,3) for b in range(-2,3)}
        adj[p] = {r for r in candidates if q((physical_row(r)[0]-p35[0],
                                              physical_row(r)[1]-p35[1])) < QUNIT}
        check(adj[p] <= y, f'neighbor outside collar {m,p}')
        for r in adj[p]:
            inv[r].add(p)
    check(y == set(inv), f'collar has omitted or isolated rows {m}')
    expected_o = {(-1,j) for j in range(m+1)} | {(i,-1) for i in range(m+1)}
    expected_o |= {(i,m-i) for i in range(m+1)}
    check(o==expected_o, f'exterior formula {m}')
    deep = {p for p in x if adj[p] <= z}
    check(deep=={p for p in x if min(p)>=1 and sum(p)<=m-1}, f'depth {m}')
    check(all(p in adj[p] and p in z for p in deep), f'deep independence {m}')
    edges = [((0,1),(1,1)),((1,1),(2,1)),((2,0),(2,1)),((2,1),(1,2))]
    edges += [((1,j),(1,j+1)) for j in range(1,m-1)]
    fan = {p for e in edges for p in e}
    scaled_edges = [(physical_source(a),physical_source(b)) for a,b in edges]
    tube = {r for r in y if min(segment_clearance(physical_row(r),a,b)
                               for a,b in scaled_edges)<0}
    tz,to = tube&z,tube&o
    check(tz=={(0,j) for j in range(m)} | {(1,j) for j in range(m-1)} | {(2,0),(2,1)},
          f'interior tube {m}')
    check(to=={(-1,1),(2,-1),(1,m-1)}, f'exterior tube {m}')
    check(all(len(inv[r])==1 for r in o), f'exterior leaf rule {m}')
    return dict(m=m,x=x,y=y,z=z,o=o,adj=adj,inv=inv,deep=deep,fan=fan,tz=tz,to=to)


def predecessor(f):
    m=f['m']
    mu={r:r for r in f['z']}
    mu[(0,1)]=(1,1)
    mu[(2,0)]=(2,1)
    for j in range(1,m-2):
        mu[(1,j)]=(1,j+1)
    mu[(1,m-2)]=(2,m-2)
    for i in range(2,m-1):
        mu[(i,1)]=(i+1,1)
    return mu


def relaxed(f, submitted=True):
    mu={}
    for i,j in f['z']:
        if i==0 and j>=1:
            mu[(i,j)]=(0,j+1)
        elif i>=2 or (i==1 and j>=(2 if submitted else 1)):
            mu[(i,j)]=(i+1,j)
        else:
            mu[(i,j)]=(i,j)
    return mu


def ledger(f,mu):
    check(set(mu)==f['z'], 'matching rows')
    b=set(mu.values())
    check(len(b)==len(mu), 'matching injectivity')
    check(all(r in f['adj'][p] for r,p in mu.items()), 'matching incidence')
    c=f['x']-b
    removed=f['fan']|{mu[r] for r in f['tz']}
    survivors=f['x']-removed
    ci=Counter(sector(physical_source(p)) for p in c-removed)
    bi=Counter(sector(physical_source(p)) for p in b-removed)
    zi=Counter(sector(physical_row(r)) for r in f['z']-f['tz'])
    check(bi==zi, 'sector matching balance')
    oi=Counter()
    iso=0
    for r in f['o']-f['to']:
        neighbors=f['inv'][r]&survivors
        check(len(neighbors)<=1, 'exterior leaf after deletion')
        if neighbors:
            oi[sector(physical_source(next(iter(neighbors))))]+=1
        else:
            iso+=1
    xi=iso+sum(max(0,oi[i]-ci[i]) for i in range(4))
    value=xi-len(f['tz'])
    admissible=f['deep']<=b
    if admissible:
        check(not(c&f['deep']), 'admissible complement')
        check(all(oi[i]>=ci[i] for i in range(4)), 'terminal injection')
        check(value==len(c&f['fan'])-2<=1, 'all-admissible-basis formula')
    check(value<=f['m']-1, 'relaxed universal bound')
    return dict(admissible=admissible,value=value,missing_deep=sorted(f['deep']-b),
                Ci=[ci[i] for i in range(4)],Oi=[oi[i] for i in range(4)],
                Oiso=iso, Xi=xi,t=len(c&f['fan']))


def find_matching(f,b):
    mate={}
    candidates={r:sorted(f['inv'][r]&b) for r in f['z']}
    def aug(r,seen):
        for p in candidates[r]:
            if p in seen:
                continue
            seen.add(p)
            if p not in mate or aug(mate[p],seen):
                mate[p]=r
                return True
        return False
    for r in sorted(f['z'],key=lambda r:(len(candidates[r]),r)):
        if not aug(r,set()):
            return None
    return {r:p for p,r in mate.items()}


def exhaustive(m):
    f=fixture(m)
    x=sorted(f['x'])
    histogram=Counter()
    admissible_hist=Counter()
    attempted=0
    valid=0
    for omit in combinations(x,m+1):
        attempted+=1
        b=f['x']-set(omit)
        mu=find_matching(f,b)
        if mu is None:
            continue
        valid+=1
        d=ledger(f,mu)
        histogram[d['value']]+=1
        if d['admissible']:
            admissible_hist[d['value']]+=1
    check(max(histogram)==m-1, 'relaxed finite optimum')
    check(max(admissible_hist)==1, 'admissible finite optimum')
    return dict(M=m,attempted_bases=attempted,matchable_bases=valid,
                relaxed_histogram=dict(sorted(histogram.items())),
                admissible_histogram=dict(sorted(admissible_hist.items())),
                limitation='One independently found matching per basis; not every matching of each basis.')


def rank(a):
    if not a or not a[0]:
        return 0
    a=[[Fraction(v) for v in r] for r in a]
    row=0
    for col in range(len(a[0])):
        pivot=next((i for i in range(row,len(a)) if a[i][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        v=a[row][col]
        a[row]=[t/v for t in a[row]]
        for i in range(row+1,len(a)):
            v=a[i][col]
            if v:
                a[i]=[t-v*u for t,u in zip(a[i],a[row])]
        row+=1
        if row==len(a):
            break
    return row


def schur_test(m,kind):
    f=fixture(m)
    mu=predecessor(f) if kind=='predecessor' else relaxed(f)
    b=sorted(mu.values())
    c=sorted(f['x']-set(b))
    z=sorted(f['z'])
    o=sorted(f['o'])
    rng=random.Random(990000+m)
    entries={(r,p):Fraction(rng.randrange(1,101)) for r in sorted(f['y'])
             for p in sorted(f['inv'][r])}
    def entry(r,p):
        return entries.get((r,p),Fraction(0))
    a=[[entry(r,p) for p in b+c] for r in z]
    for k in range(len(z)):
        pivot=next((i for i in range(k,len(z)) if a[i][k]),None)
        check(pivot is not None, 'exact specialization basis determinant')
        a[k],a[pivot]=a[pivot],a[k]
        scale=a[k][k]
        a[k]=[v/scale for v in a[k]]
        for i in range(len(z)):
            if i!=k:
                scale=a[i][k]
                if scale:
                    a[i]=[v-scale*w for v,w in zip(a[i],a[k])]
    s=[[entry(r,p)-sum(entry(r,b[k])*a[k][len(z)+j] for k in range(len(z)))
        for j,p in enumerate(c)] for r in o]
    shallow=[j for j,p in enumerate(c) if p not in f['deep']]
    deep=[j for j,p in enumerate(c) if p in f['deep']]
    fullrank=rank(s)
    shallowrank=rank([[r[j] for j in shallow] for r in s])
    deeprank=rank([[r[j] for j in deep] for r in s])
    check(fullrank==m+1, 'full Schur exact rank')
    check(shallowrank==(m+1 if kind=='predecessor' else 3), 'boundary Schur exact rank')
    check(deeprank==(0 if kind=='predecessor' else m-2), 'omitted deep columns are not loops')
    return dict(M=m,basis=kind,full_rank=fullrank,boundary_rank=shallowrank,
                omitted_deep_rank=deeprank,actual_h=len(o)-fullrank,
                incorrect_boundary_only_h=len(o)-shallowrank,
                arithmetic='exact Fractions, nonzero integer edge specialization, seed '+str(990000+m))


def source_pins():
    sources=json.loads(subprocess.check_output([
        'git','show',SHA+':research-packages/target-a-fan-tube-ledger/SOURCES.json'],cwd=REPO))
    checked=[]
    for inp in sources['inputs']:
        commit=inp.get('commit',SHA)
        blob=subprocess.check_output(['git','show',commit+':'+inp['path']],cwd=REPO)
        h=hashlib.sha256(blob).hexdigest()
        check(h==inp['sha256'], 'source pin '+inp['path'])
        checked.append(dict(path=inp['path'],commit=commit,sha256=h))
    return checked


def main():
    global REPO, SHA
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,default=Path.cwd(),
                        help='Path within the Git repository; defaults to the current directory.')
    parser.add_argument('--sha',default='HEAD',
                        help='Immutable source commit to inspect; defaults to the current HEAD.')
    args=parser.parse_args()
    REPO=Path(subprocess.check_output(
        ['git','-C',str(args.repo),'rev-parse','--show-toplevel'],text=True).strip())
    SHA=subprocess.check_output(
        ['git','rev-parse','--verify',args.sha+'^{commit}'],cwd=REPO,text=True).strip()
    start=time.time()
    output={'reviewed_commit':SHA,'python':sys.version,'independence':'No repository Python code imported or edited.'}
    output['source_pins']=source_pins()
    output['local_tubes']={}
    for d in [(1,0),(0,1),(-1,1)]:
        rows=[]
        for i in range(-5,6):
            for j in range(-5,6):
                c=segment_clearance(physical_row((i,j)),(0,0),physical_source(d))
                check(c!=0,'local tube equality')
                if c<0:
                    rows.append((i,j))
        output['local_tubes'][str(d)]=rows
    output['ledgers']=[]
    for m in [4,5,6,7,10,21,33]:
        f=fixture(m)
        for kind,mu in [('predecessor',predecessor(f)),('submitted_relaxed',relaxed(f)),
                        ('independently_derived_relaxed',relaxed(f,False))]:
            d=ledger(f,mu)
            check(d['value']==(1 if kind=='predecessor' else m-1), 'witness optimum')
            output['ledgers'].append(dict(M=m,basis=kind,**d))
    print('Geometry and independent witness ledgers passed.',file=sys.stderr,flush=True)
    output['exhaustive']=exhaustive(5)
    print('Exhaustive M=5 basis search passed.',file=sys.stderr,flush=True)
    output['exact_schur']=[schur_test(m,k) for m in [5,6] for k in ['predecessor','relaxed']]
    output['result']='PASS'
    output['elapsed_seconds']=round(time.time()-start,3)
    print(json.dumps(output,indent=2,sort_keys=True))


if __name__=='__main__':
    main()
