"""Exploratory floating LP discovery; requires NumPy and SciPy.

Numerically selected zero rows and random second-order candidates are
not exact certificates or exhaustive feasibility results. The script
writes discovery JSONL and any positive candidates under /tmp.
"""
from fractions import Fraction as F
from itertools import combinations
import json
import numpy as np
from scipy.optimize import linprog


def dot(r,a):
    return r[0]*(a[0]+a[1]/2)+r[1]*(a[0]/2+a[1])


def square(r):
    return r[0]*r[0]+r[0]*r[1]+r[1]*r[1]


def run(m,roots=True,relative=False,deleted_corner=False,omit_center=False):
    rad=m-1
    pts=[(i,j) for i in range(-rad,rad+1) for j in range(-rad,rad+1)
         if abs(i+j)<=rad]
    if omit_center:
        pts=[p for p in pts if p!=(0,0)]
    n=len(pts)
    basis=[(-1,1),(-1,0),(0,-1),(1,-1),(1,0),(0,1)]
    corner=(m,0)
    wall=[]
    c=F(m*(m*m-1),6)
    for side,w in enumerate(basis):
        for i in range(m):
            q=(corner[0]+i*w[0],corner[1]+i*w[1])
            bow=i*(m-i)
            jcoef=(F(-w[0]-2*w[1],3),F(2*w[0]+w[1],3))
            q1=(-bow*jcoef[0],-bow*jcoef[1])
            prefix=sum((2*j-m+1)**2 for j in range(i))
            q2=(-c*F(corner[0],m)-F(prefix,2)*w[0],
                -c*F(corner[1],m)-F(prefix,2)*w[1])
            wall.append((q,q1,q2,'wall',side*m+i))
            if roots and i in range(2,m-1,3):
                avg=2*i-m
                root1=(q1[0]+3*jcoef[0],q1[1]+3*jcoef[1])
                root2=(q2[0]-3*avg*w[0],q2[1]-3*avg*w[1])
                wall.append((q,root1,root2,'root',side*m+i))
        corner=(corner[0]+m*w[0],corner[1]+m*w[1])
    assert corner==(m,0)
    if deleted_corner:
        wall=[record for record in wall if not (record[3]=='wall' and record[4]==0)]
    rows=[]
    rhs=[]
    constraints=[]
    sides=lambda p:[p[0],-p[0],p[1],-p[1],p[0]+p[1],-p[0]-p[1]]
    for i,j in combinations(range(n),2):
        r=(pts[i][0]-pts[j][0],pts[i][1]-pts[j][1])
        if square(r)!=1:
            continue
        boundary=any(a==b==rad for a,b in zip(sides(pts[i]),sides(pts[j])))
        row=np.zeros(2*n+1)
        row[2*i:2*i+2]=[-r[0]-r[1]/2,-r[0]/2-r[1]]
        row[2*j:2*j+2]=-row[2*i:2*i+2]
        row[-1]=0 if boundary else 1
        rows.append(row)
        rhs.append(0.)
        constraints.append(('pair',i,j,r,None,None))
    for i,p in enumerate(pts):
        for q,q1,q2,kind,index in wall:
            r=(p[0]-q[0],p[1]-q[1])
            if square(r)!=1:
                continue
            row=np.zeros(2*n+1)
            row[2*i:2*i+2]=[-r[0]-r[1]/2,-r[0]/2-r[1]]
            iscorner=q1==(0,0) and kind=='wall'
            row[-1]=0 if iscorner else 1
            rows.append(row)
            rhs.append(float(-dot(r,q1)))
            constraints.append(('wall',i,None,r,q1,q2))
    rows=np.array(rows)
    rhs=np.array(rhs)
    objective=np.zeros(2*n+1)
    objective[-1]=-1
    bounds=[(-10*m*m,10*m*m)]*(2*n)+[(0,None)]
    result=linprog(objective,A_ub=rows,b_ub=rhs,bounds=bounds,method='highs')
    if not result.success:
        return {'M':m,'roots':roots,'stage1':result.message}
    forced_count=None
    if relative:
        first_bounds=bounds[:-1]+[(0,0)]
        forced=[]
        for row_index,row in enumerate(rows):
            objective=row.copy()
            objective[-1]=0
            extreme=linprog(objective,A_ub=rows,b_ub=rhs,bounds=first_bounds,method='highs')
            assert extreme.success,extreme.message
            slack=rhs[row_index]-row@extreme.x
            forced.append(slack<1e-6)
        forced_count=int(sum(forced))
        rows=rows.copy()
        rows[:,-1]=[0 if f else 1 for f in forced]
        objective=np.zeros(2*n+1)
        objective[-1]=-1
        result=linprog(objective,A_ub=rows,b_ub=rhs,bounds=bounds,method='highs')
        assert result.success,result.message
    optimum=result.x[-1]
    if omit_center and relative and forced_count==0 and optimum>1e-7:
        filename=f'/tmp/e99-first-strict-vacancy-M{m}.json'
        answer={'M':m,'roots':roots,'deleted_corner':deleted_corner,'omit_center':True,
                'points':pts,'stage1_margin':float(optimum),'first':result.x[:-1].reshape(n,2).tolist(),
                'classification':'floating discovery; exact reconstruction required'}
        with open(filename,'w') as f:
            json.dump(answer,f)
        return {k:v for k,v in answer.items() if k not in ('points','first')}|{'candidate_file':filename}
    candidates=[result.x]
    rng=np.random.default_rng(99+m)
    objectives=[np.sum(rows,axis=0)]+[rng.normal(size=2*n+1) for k in range(30)]
    for pinned_margin in (max(0,optimum/2),0):
        random_bounds=bounds[:-1]+[(pinned_margin,pinned_margin)]
        for objective in objectives:
            objective[-1]=0
            extreme=linprog(objective,A_ub=rows,b_ub=rhs,bounds=random_bounds,method='highs')
            if extreme.success:
                candidates.append(extreme.x)
    best=None
    best_nested_ratio=None
    for candidate in candidates:
        first=candidate[:-1].reshape(n,2)
        velocity={p:first[i] for i,p in enumerate(pts)}
        rays=[(1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1)]
        energies=[]
        for radius in range(m):
            energy=0.
            for i,j in combinations(range(n),2):
                a,z=pts[i],pts[j]
                on_ring=lambda p:max(abs(p[0]),abs(p[1]),abs(p[0]+p[1]))==radius
                if on_ring(a) and on_ring(z) and square((a[0]-z[0],a[1]-z[1]))==1:
                    energy+=3*square(first[i]-first[j])
            for e in rays:
                for radius_index in range(radius,m):
                    a=tuple(radius_index*x for x in e)
                    z=tuple((radius_index+1)*x for x in e)
                    diff=velocity[a]-(np.zeros(2) if radius_index==m-1 else velocity[z])
                    energy+=3*square(diff)
            energies.append(energy/float(12*c))
        nested_ratio=float(min(energies))
        if best_nested_ratio is None or nested_ratio>best_nested_ratio:
            best_nested_ratio=nested_ratio
            if nested_ratio>1-1e-8:
                with open(f'/tmp/e99-nested-energy-equality-M{m}-roots{int(roots)}-corner{int(deleted_corner)}.json','w') as f:
                    json.dump({'M':m,'roots':roots,'points':pts,'first':first.tolist(),
                               'energy_ratios':energies,'classification':'floating first-order candidate only'},f)
        second_rows=[]
        second_rhs=[]
        for kind,i,j,r,q1,q2 in constraints:
            diff=first[i]-first[j] if kind=='pair' else first[i]-np.array(q1,dtype=float)
            initial=float(dot(r,diff))
            if initial>1e-7:
                continue
            assert initial>-1e-6,initial
            row=np.zeros(2*n+1)
            row[2*i:2*i+2]=[-r[0]-r[1]/2,-r[0]/2-r[1]]
            if kind=='pair':
                row[2*j:2*j+2]=-row[2*i:2*i+2]
            row[-1]=1
            second_rows.append(row)
            second_rhs.append(float(1.5*square(diff)-(0 if kind=='pair' else dot(r,q2))))
        objective=np.zeros(2*n+1)
        objective[-1]=-1
        second=linprog(objective,A_ub=np.array(second_rows),b_ub=np.array(second_rhs),
                       bounds=[(-10*m**5,10*m**5)]*(2*n)+[(None,None)],method='highs')
        if second.success and (best is None or second.x[-1]>best[0]):
            best=(second.x[-1],first,second.x[:-1].reshape(n,2),len(second_rows))
    answer={'M':m,'roots':roots,'deleted_corner':deleted_corner,'points':n,'stage1_margin':optimum,
            'relative_interior':relative,'forced_first_zero_constraints':forced_count,
            'maximum_sampled_minimum_nested_energy_ratio':best_nested_ratio,
            'candidate_count':len(candidates),'best_stage2_margin':None if best is None else best[0],
            'critical_constraints':None if best is None else best[-1]}
    if best is not None and best[0]>1e-7:
        filename=f'/tmp/e99-nonaffine-discovery-M{m}-roots{int(roots)}-corner{int(deleted_corner)}.json'
        with open(filename,'w') as f:
            json.dump(dict(answer,points=pts,first=best[1].tolist(),second=best[2].tolist()),f)
        answer['candidate_file']=filename
    return answer


if __name__=='__main__':
    with open('/tmp/e99-three-direction-nonaffine-relative-results.jsonl','w') as f:
        for m in (3,4,5,6):
            for roots in (False,True):
                answer=run(m,roots,True)
                line=json.dumps(answer)
                f.write(line+'\n')
                f.flush()
                print(line,flush=True)
