#!/usr/bin/env python3
"""Exact finite checks for actual-source row and side-pin release.

The companion verifier is imported and rerun deliberately to recheck the
internal exact-arithmetic/capacity fixtures. This file checks 68 additional
finite sources and endpoints, with off-lattice exterior unit contacts,
retained contact isolates, or a loaded released pin. It samples each stage;
the report proves its whole path and the universal inward-normal lemma.
Four square diagnostic packets additionally certify a normalized stress,
survival after the literal deletion, row-nullity-one uniqueness, and a strict
fourth finite step. No canonical source, canonical extraction, or refill is certified.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10 import Q, fixtures, dist2, norm2, rank

def minimum(items):
    items=list(items)
    assert items
    best=items[0]
    for x in items[1:]:
        if (x-best).sign()<0: best=x
    return best

def maximum(items): return -minimum(-x for x in items)

def rigidity_rows(points,edges):
    rows=[]
    for i,j in edges:
        row=[Q(0)]*(2*len(points))
        dx,dy=points[i][0]-points[j][0],points[i][1]-points[j][1]
        row[2*i],row[2*i+1],row[2*j],row[2*j+1]=dx,dy,-dx,-dy
        rows.append(row)
    return rows

def full_row_solve(rows,rhs):
    a=[list(row)+[value] for row,value in zip(rows,rhs)]
    pivots=[]; r=0
    for col in range(len(rows[0])):
        pivot=next((i for i in range(r,len(a)) if a[i][col]),None)
        if pivot is None: continue
        a[r],a[pivot]=a[pivot],a[r]
        z=a[r][col]; a[r]=[x/z for x in a[r]]
        for i in range(len(a)):
            if i!=r and a[i][col]:
                z=a[i][col]; a[i]=[x-z*y for x,y in zip(a[i],a[r])]
        pivots.append(col); r+=1
        if r==len(a): break
    assert r==len(rows)
    sol=[Q(0)]*len(rows[0])
    for i,col in enumerate(pivots): sol[col]=a[i][-1]
    assert all(sum((x*y for x,y in zip(row,sol)),Q(0))==b for row,b in zip(rows,rhs))
    return sol

def inside(p,c,s,k,strict=False):
    b=p[1]/s; a=p[0]-c*b
    vals=(1+b,1-b,a+b+1,k-a-b,a-b+1,k-a+b)
    return all(x.sign()>0 if strict else x.sign()>=0 for x in vals)

counts={'source_pairs':0,'endpoint_pairs':0,'strict_endpoint_pairs':0,
        'path_sample_pairs':0,'inward_unit_neighbor_checks':0,
        'retained_isolate_checks':0,'loaded_pin_sources':0,
        'positive_stress_sources':0,'certified_strict_descent_pairs':0}
records=[]
for name,c,s in fixtures:
    for k in (2,5):
        wax=[(-1,0)]+[(j,-1) for j in range(k)]+[(k,0)]+[(j,1) for j in reversed(range(k))]
        wall=[(Q(a)+b*c,b*s) for a,b in wax]
        row=[(Q(j),Q(0)) for j in range(k)]
        base=wall+row
        modes=['off_lattice_contacts_and_isolate','loaded_top_pin']
        if name=='square': modes.append('positive_boundary_stress')
        for mode in modes:
            if mode=='off_lattice_contacts_and_isolate':
                extra=[(Q(a)+b*c,b*s) for a,b in ((-1,-1),(-1,1),(k,-1),(k,1))]
                extra += [(Q(j)+c,s+1) for j in range(k)]
                extra += [(Q(j)-c,-s-1) for j in range(k)]
                extra += [(Q(F(k-1,2)),s+Q(F(5,2)))]
            elif mode=='loaded_top_pin': extra=[(Q(3*k),Q(-100*k))]
            else: extra=[(Q(a),Q(b)) for a,b in ((-1,-1),(-1,1),(k,-1),(k,1))]
            old=base+extra
            old_contacts=[]; old_dist=[]
            for i,j in combinations(range(len(old)),2):
                d2=dist2(old[i],old[j]); old_dist.append(d2)
                assert (d2-1).sign()>=0
                counts['source_pairs']+=1
                if d2==1: old_contacts.append((i,j))
            D2=maximum(old_dist)
            contact_set=set(old_contacts)
            assert not any(all(tuple(sorted(e)) in contact_set for e in combinations(t,2))
                           for t in combinations(range(len(old)),3))
            diameters=[(i,j) for i,j in combinations(range(len(old)),2) if dist2(old[i],old[j])==D2]
            if mode=='off_lattice_contacts_and_isolate':
                isolate_id=len(old)-1
                assert not any(isolate_id in e for e in old_contacts)
            elif mode=='loaded_top_pin':
                assert diameters==[(2*k+1,len(old)-1)]
                counts['loaded_pin_sources']+=1
            else:
                assert D2==Q((k+1)**2+4)
                assert len(diameters)==2
                beta={e:Q(F(1,2)) for e in diameters}
                alpha={}
                for i,j in old_contacts:
                    p,q=old[i],old[j]
                    if p[1]==q[1] and p[1] in (Q(-1),Q(1)): alpha[(i,j)]=Q(F(k+1,2))
                    elif p[0]==q[0] and p[0] in (Q(-1),Q(k)): alpha[(i,j)]=Q(1)
                balance=[[Q(0),Q(0)] for _ in old]
                for e,value in list(alpha.items())+[(e,-b) for e,b in beta.items()]:
                    i,j=e
                    for axis in (0,1):
                        force=value*(old[i][axis]-old[j][axis])
                        balance[i][axis]+=force; balance[j][axis]-=force
                assert all(x==0 for v in balance for x in v)
                assert sum(beta.values(),Q(0))==1 and sum(alpha.values(),Q(0))==D2
                old_rows=rigidity_rows(old,old_contacts+diameters)
                assert rank(old_rows)==len(old_rows)-1
                deleted_id=len(wall)+k-1
                assert not any(deleted_id in e for e in list(alpha)+list(beta))
                core=set(i for e in alpha for i in e)
                assert len(core)==2*k+6
                assert len(alpha)+len(beta)<2*len(core)-3
                if k==2:
                    tri=[(a,b) for a in range(-2,3) for b in range(-2,3)
                         if a*a+b*b+a*b<=3][:len(old)]
                    assert len(tri)==len(old)
                    def gram(p,q):
                        a,b=p[0]-q[0],p[1]-q[1]
                        return a*a+b*b+a*b
                    assert min(gram(p,q) for p,q in combinations(tri,2))>=1
                    competitor_d2=max(gram(p,q) for p,q in combinations(tri,2))
                else:
                    grid=[(i%5,i//5) for i in range(len(old))]
                    competitor_d2=max((p[0]-q[0])**2+(p[1]-q[1])**2 for p,q in combinations(grid,2))
                assert (D2-competitor_d2).sign()>0
                counts['positive_stress_sources']+=1
            for pattern in ('one_top_pin','all_side_pins'):
                ids=[2*k+1] if pattern=='one_top_pin' else list(range(1,k+1))+list(range(k+2,2*k+2))
                pin_sign={i:(-1 if i<=k else 1) for i in ids}
                # Positive sign means top/outward +n; inward movement subtracts it.
                depths={i:Q(1)+Q(F(t+1,len(ids)+1)) for t,i in enumerate(ids)}
                fixed_ids=[i for i in range(len(old)) if i<len(wall) and i not in ids or i>=len(base)]
                fixed=[old[i] for i in fixed_ids]
                delta=(1-2*c)/100
                z=[(Q(j)+delta*s,-delta*c) for j in range(k-1)]
                gap=minimum(dist2(p,g)-1 for p in z for g in wall)
                eps=F(1,128); M=Q(k+2)
                for _ in range(96):
                    packet=[(p[0],p[1]+(-1)**j*eps) for j,p in enumerate(z)]
                    if (gap-4*M*eps).sign()>0 and all(inside(p,c,s,k,True) for p in packet): break
                    eps/=2
                else: raise AssertionError('row packet epsilon failed')
                assert all((dist2(p,g)-1).sign()>0 for p in packet for g in wall)
                assert all((dist2(p,q)-1).sign()>0 for p,q in combinations(packet,2))
                normal_checks=0
                for i in ids:
                    for j in fixed_ids:
                        if dist2(old[i],old[j])==1:
                            assert (pin_sign[i]*(old[j][1]-old[i][1])).sign()>=0
                            normal_checks+=1
                counts['inward_unit_neighbor_checks']+=normal_checks
                margins=[dist2(p,old[i])-1 for p in packet for i in ids]
                for i in ids:
                    for j in fixed_ids:
                        d2=dist2(old[i],old[j])
                        if d2!=1: margins.append(d2-1)
                for i,j in combinations(ids,2):
                    d2=dist2(old[i],old[j])
                    if d2!=1: margins.append(d2-1)
                gmin=minimum(margins)
                assert gmin.sign()>0
                M=Q(500*k)
                assert all((M*M-d2).sign()>0 for d2 in old_dist)
                tau=F(1,1024)
                for _ in range(96):
                    pins=[(old[i][0],old[i][1]-pin_sign[i]*tau*depths[i]) for i in ids]
                    if (gmin-32*M*tau).sign()>0 and all(inside(p,c,s,k,True) for p in pins): break
                    tau/=2
                else: raise AssertionError('pin tau failed')
                new=fixed+packet+pins
                assert len(new)==len(old)-1
                moved_start=len(fixed)
                final_d=[]
                for i,j in combinations(range(len(new)),2):
                    d2=dist2(new[i],new[j]); final_d.append(d2)
                    counts['endpoint_pairs']+=1
                    assert (d2-1).sign()>=0 and (D2-d2).sign()>=0
                    if i>=moved_start or j>=moved_start:
                        assert (d2-1).sign()>0 and (D2-d2).sign()>0
                        counts['strict_endpoint_pairs']+=1
                if mode=='loaded_top_pin': assert (D2-maximum(final_d)).sign()>0
                elif mode=='off_lattice_contacts_and_isolate':
                    assert fixed_ids[-1]==isolate_id and new[len(fixed)-1]==old[isolate_id]
                    counts['retained_isolate_checks']+=1
                stress_certificate=None
                if mode=='positive_boundary_stress':
                    T=set(range(len(wall),len(base)))|set(ids)
                    assert any(i in T or j in T for i,j in alpha)
                    assert maximum(final_d)==D2
                    nc=[(i,j) for i,j in combinations(range(len(new)),2) if dist2(new[i],new[j])==1]
                    nh=[(i,j) for i,j in combinations(range(len(new)),2) if dist2(new[i],new[j])==D2]
                    rr=rigidity_rows(new,nc+nh)
                    assert rank(rr)==len(rr)
                    vel=full_row_solve(rr,[Q(1)]*len(nc)+[Q(-1)]*len(nh))
                    step=F(1,1024)
                    for _ in range(256):
                        strict=[(p[0]+step*vel[2*i],p[1]+step*vel[2*i+1]) for i,p in enumerate(new)]
                        dd=[dist2(p,q) for p,q in combinations(strict,2)]
                        if all((d-1).sign()>0 and (D2-d).sign()>0 for d in dd): break
                        step/=2
                    else: raise AssertionError('strict fourth step failed')
                    counts['certified_strict_descent_pairs']+=len(dd)
                    stress_certificate={'normalized_stress_unique_by_row_nullity_one':True,
                                        'beta_each':'1/2','horizontal_alpha':str(F(k+1,2)),
                                        'vertical_alpha':'1','survives_literal_interior_deletion':True,
                                        'released_set_hits_stress':True,'positive_core_vertices':len(core),
                                        'selected_row_count':len(alpha)+len(beta),
                                        'canonical_required_rank':2*len(core)-3,
                                        'nonglobal_competitor_diameter_squared':competitor_d2,
                                        'endpoint_active_row_rank':len(rr),'strict_step':str(step),
                                        'velocity':[v.serial() for v in vel],
                                        'strict_diameter_squared':maximum(dd).serial()}
                for stage,t in ((1,F(0)),(1,F(1,2)),(1,F(1)),
                                (2,F(1,2)),(2,F(1)),(3,F(1,2)),(3,F(1))):
                    if stage==1:
                        rows=[(Q(j)+t*delta*s,-t*delta*c) for j in range(k-1)]
                        pp=[old[i] for i in ids]
                    elif stage==2:
                        rows=[(p[0],p[1]+t*(-1)**j*eps) for j,p in enumerate(z)]
                        pp=[old[i] for i in ids]
                    else:
                        rows=packet
                        pp=[(old[i][0],old[i][1]-pin_sign[i]*t*tau*depths[i]) for i in ids]
                    current=fixed+rows+pp
                    assert all(inside(p,c,s,k) for p in rows+pp)
                    for i,j in combinations(range(len(current)),2):
                        d2=dist2(current[i],current[j]); counts['path_sample_pairs']+=1
                        assert (d2-1).sign()>=0 and (D2-d2).sign()>=0
                records.append({'angle_fixture':name,'k':k,'exterior':mode,'released_pins':pattern,
                                'old_population':len(old),'new_population':len(new),
                                'literal_deletions':1,'released_labels':k-1+len(ids),
                                'epsilon':str(eps),'tau':str(tau),'old_diameter_squared':D2.serial(),
                                'endpoint_diameter_squared':maximum(final_d).serial(),
                                'inward_unit_neighbors_checked':normal_checks,
                                'stress_certificate':stress_certificate})

cert={'arithmetic':'Q(sqrt(15)); exact rational and algebraic signs',
      'counts':counts,'fixtures':records,
      'limits':'Finite sources, endpoints and stage samples only. Whole-path feasibility and universal inward-normal/source-stress implications are proved analytically in the report. No global minimizer, stress-transversal extraction or final-label restoration is certified.'}
out=Path(__file__).with_name('target_c_one_vacancy_side_pin_release_slot07_certificate_2026_10_10.json')
out.write_text(json.dumps(cert,indent=2)+'\n')
print('PASS: one-vacancy pin release '+json.dumps(counts)+'; '+str(len(records))+' fixtures.')
