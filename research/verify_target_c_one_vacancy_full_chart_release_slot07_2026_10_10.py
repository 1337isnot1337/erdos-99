#!/usr/bin/env python3
"""Exact whole-segment checks for four-stage actual-source chart release.

Reruns the companion arithmetic fixtures on import. This script tests finite
complete charts and arbitrary exterior-contact diagnostics, not canonical
extraction, global optimality, a stress-transversal hypothesis, or restoration.
Every pair along each linear segment is checked by its exact quadratic minimum.
"""
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path
from verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10 import Q, fixtures, dist2, norm2

def add(p,q): return (p[0]+q[0],p[1]+q[1])
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def mul(t,p): return (t*p[0],t*p[1])
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
def minimum(xs):
    z=None
    for x in xs:
        if z is None or (x-z).sign()<0: z=x
    assert z is not None
    return z
def maximum(xs): return -minimum(-x for x in xs)
def axial(p,c,s):
    b=p[1]/s
    return p[0]-c*b,b
def inside(p,c,s,m,n,strict=False):
    a,b=axial(p,c,s)
    return all(x.sign()>0 if strict else x.sign()>=0 for x in (a,m-a,b,n-b))
def segment_min(p,q,dp,dq):
    r=sub(p,q); v=sub(dp,dq)
    A=norm2(v); B=2*dot(r,v); C=norm2(r)
    candidates=[C,A+B+C]
    if A.sign()>0:
        t=-B/(2*A)
        if t.sign()>0 and (1-t).sign()>0: candidates.append(C-B*B/(4*A))
    return minimum(candidates)

angle_cases=[fixtures[0],fixtures[1],('obtuse_13_85',-fixtures[1][1],fixtures[1][2]),
             fixtures[4],('obtuse_critical',-fixtures[4][1],fixtures[4][2]),
             fixtures[7],('obtuse_8_17',-fixtures[7][1],fixtures[7][2]),fixtures[6]]
counts={k:0 for k in ('source_pairs','segment_pairs','endpoint_pairs','strict_chart_pairs',
                     'strict_chart_upper_pairs','side_normal_unit_neighbors','corner_unit_neighbors',
                     'retained_isolates','bare_strict_diameter_sources')}
records=[]
for name,c,s in angle_cases:
  for m,n,a,b in ((2,2,1,1),(3,4,1,2),(5,3,3,1)):
    axes=[(i,j) for j in range(n+1) for i in range(m+1)]
    chart=[(Q(i)+j*c,j*s) for i,j in axes]
    hole=axes.index((a,b))
    interior={k for k,(i,j) in enumerate(axes) if 0<i<m and 0<j<n and k!=hole}
    corners={axes.index(z) for z in ((0,0),(m,0),(0,n),(m,n))}
    sides=set(range(len(chart)))-interior-corners-{hole}
    normals={}
    for k in sides:
        i,j=axes[k]
        normals[k]=((Q(0),Q(-1)) if j==0 else (Q(0),Q(1)) if j==n
                    else (-s,c) if i==0 else (s,-c))
    corner_dirs={axes.index((0,0)):(1+c,s),axes.index((m,0)):(-1+c,s),
                 axes.index((0,n)):(1-c,-s),axes.index((m,n)):(-1-c,-s)}
    for mode in ('bare_chart','exterior_side_contacts_and_isolate','exterior_corner_contacts_and_isolate'):
      extra=[]
      if mode!='bare_chart':
        if mode=='exterior_side_contacts_and_isolate':
          extra=[add(chart[k],normals[k]) for k in sorted(sides)]
        else:
          extra=[add(chart[k],(Q(-1 if axes[k][0]==0 else 1),Q(0)))
                 for k in sorted(corners)]
        extra += [(Q(F(m,2))+c*F(n,2),n*s+Q(F(5,2)))]
      old=chart+extra
      D2=maximum(dist2(old[i],old[j]) for i,j in combinations(range(len(old)),2))
      contacts=[]
      for i,j in combinations(range(len(old)),2):
        z=dist2(old[i],old[j]); assert (z-1).sign()>=0
        counts['source_pairs']+=1
        if z==1: contacts.append((i,j))
      contact_set=set(contacts)
      assert not any(all(tuple(sorted(e)) in contact_set for e in combinations(t,2))
                     for t in combinations(range(len(old)),3))
      for k in sides:
        i,j=axes[k]
        own=(i,1) if j==0 else (i,n-1) if j==n else (1,j) if i==0 else (m-1,j)
        own_id=axes.index(own)
        for x,y in contacts:
          other=y if x==k else x if y==k else None
          if other is not None and other!=own_id:
            assert dot(sub(old[other],old[k]),normals[k]).sign()>=0
            counts['side_normal_unit_neighbors']+=1
      for k in corners:
        i,j=axes[k]
        adjacent={axes.index((i+1 if i==0 else i-1,j)),
                  axes.index((i,j+1 if j==0 else j-1))}
        for x,y in contacts:
          other=y if x==k else x if y==k else None
          if other is not None and other not in adjacent:
            assert dot(sub(old[other],old[k]),corner_dirs[k]).sign()<0
            counts['corner_unit_neighbors']+=1
      if extra:
        isolate=len(old)-1
        assert not any(isolate in edge for edge in contacts)
        counts['retained_isolates']+=1
      ids=[i for i in range(len(old)) if i!=hole]
      loc={k:j for j,k in enumerate(ids)}
      current=[old[k] for k in ids]
      released=set()
      stages=[]
      for stage in range(1,5):
        velocity=[(Q(0),Q(0)) for _ in ids]
        target=set()
        if stage==1:
          for k in interior:
            i,j=axes[k]
            if j==b:
              coeff=-F(i,a) if i<a else F(m-i,m-a)
              velocity[loc[k]]=mul(coeff,(-s,c)); target.add(k)
            elif i==a:
              coeff=F(j,b) if j<b else -F(n-j,n-b)
              velocity[loc[k]]=(Q(0),Q(coeff)); target.add(k)
        elif stage==2:
          for k in interior-released:
            i,j=axes[k]
            sx=1 if i<a else -1; sy=1 if j<b else -1
            I=i if i<a else m-i; J=j if j<b else n-j
            velocity[loc[k]]=(Q(sx*I),(-sx*I*c+sy*J)/s); target.add(k)
        elif stage==3:
          for h,k in enumerate(sorted(sides)):
            depth=Q(1+F(h,len(sides)+1))
            velocity[loc[k]]=mul(-depth,normals[k]); target.add(k)
        else:
          for k in corners:
            velocity[loc[k]]=corner_dirs[k]; target.add(k)
        amplitude=F(1,100)
        for attempt in range(100):
          displacement=[mul(amplitude,v) for v in velocity]
          candidate=[add(p,d) for p,d in zip(current,displacement)]
          bad=False
          for x,y in combinations(range(len(ids)),2):
            low=segment_min(current[x],current[y],displacement[x],displacement[y])
            final=dist2(candidate[x],candidate[y])
            if (low-1).sign()<0 or (D2-final).sign()<0:
                bad=True; break
            if ids[x] in released|target or ids[y] in released|target:
                if (final-1).sign()<=0 or (D2-final).sign()<=0:
                    bad=True; break
          if not bad and all(inside(candidate[loc[k]],c,s,m,n,strict=True)
                             for k in released|target): break
          amplitude/=2
        else: raise AssertionError(('no finite stage',name,m,n,mode,stage))
        segment_lowers=[]; stage_distances=[]; release_distances=[]
        for x,y in combinations(range(len(ids)),2):
          low=segment_min(current[x],current[y],displacement[x],displacement[y])
          final=dist2(candidate[x],candidate[y])
          assert (low-1).sign()>=0
          assert (D2-dist2(current[x],current[y])).sign()>=0
          assert (D2-final).sign()>=0
          segment_lowers.append(low); stage_distances.append(final)
          if ids[x] in released|target or ids[y] in released|target:
            release_distances.append(final)
          counts['segment_pairs']+=1
        released |= target
        current=candidate
        stages.append({'stage':stage,'amplitude':str(amplitude),'released_labels':len(released),
                       'whole_segment_minimum_squared':minimum(segment_lowers).serial(),
                       'endpoint_maximum_squared':maximum(stage_distances).serial(),
                       'released_endpoint_minimum_squared':minimum(release_distances).serial() if release_distances else None,
                       'released_endpoint_maximum_squared':maximum(release_distances).serial() if release_distances else None})
      assert released==set(range(len(chart)))-{hole}
      for k in ids:
        if k>=len(chart): assert current[loc[k]]==old[k]
      for x,y in combinations(range(len(ids)),2):
        z=dist2(current[x],current[y]); counts['endpoint_pairs']+=1
        assert (z-1).sign()>=0 and (D2-z).sign()>=0
        if ids[x] in released or ids[y] in released:
          assert (z-1).sign()>0 and (D2-z).sign()>0
          counts['strict_chart_pairs']+=1; counts['strict_chart_upper_pairs']+=1
      end_D2=maximum(dist2(current[i],current[j]) for i,j in combinations(range(len(ids)),2))
      if mode=='bare_chart':
        assert (D2-end_D2).sign()>0; counts['bare_strict_diameter_sources']+=1
      records.append({'angle':name,'m':m,'n':n,'vacancy':[a,b],'mode':mode,
                      'cos_phi':c.serial(),'sin_phi':s.serial(),
                      'old_population':len(old),'endpoint_population':len(ids),
                      'old_diameter_squared':D2.serial(),'endpoint_diameter_squared':end_D2.serial(),
                      'stages':stages})

out=Path(__file__).with_name('target_c_one_vacancy_full_chart_release_slot07_certificate_2026_10_10.json')
out.write_text(json.dumps({'arithmetic':'Q(sqrt(15)), exact quadratic segment minima',
                          'counts':counts,'fixtures':records,
                          'limits':'Finite whole paths only; no canonical extraction, normalized-stress transversal, full-population refill, or global optimality.'},indent=2)+'\n')
print('PASS: full-chart release '+json.dumps(counts)+'; '+str(len(records))+' fixtures.')
