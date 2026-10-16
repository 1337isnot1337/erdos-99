#!/usr/bin/env python3
"""Exact effective discrete packets, wall-span stress, and finite bay refill.

Reruns companion arithmetic fixtures. Actual perturbed unit walls remain fixed.
The star diagnostics check an entire strict descent and a same-cardinality
refill. Their old bay was already spare, so they are nonglobal and noncanonical.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt
import json
from pathlib import Path
from verify_target_c_rhombic_vacancy_hop_slot07_2026_10_10 import Q, fixtures, dist2, norm2, rank

def add(p,q): return (p[0]+q[0],p[1]+q[1])
def sub(p,q): return (p[0]-q[0],p[1]-q[1])
def mul(t,p): return (t*p[0],t*p[1])
def dot(p,q): return p[0]*q[0]+p[1]*q[1]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
def minimum(xs):
    out=None
    for x in xs:
        if out is None or (x-out).sign()<0: out=x
    assert out is not None
    return out
def maximum(xs): return -minimum(-x for x in xs)
def le(a,b): return (b-a).sign()>=0
def orient(a,b,c): return cross(sub(b,a),sub(c,a))
def on_segment(p,a,b):
    return not orient(a,b,p) and all(le(minimum((a[d],b[d])),p[d]) and le(p[d],maximum((a[d],b[d]))) for d in (0,1))
def intersect(a,b,c,d):
    aa,bb,cc,dd=orient(a,b,c).sign(),orient(a,b,d).sign(),orient(c,d,a).sign(),orient(c,d,b).sign()
    return (aa*bb<0 and cc*dd<0) or (aa==0 and on_segment(c,a,b)) or (bb==0 and on_segment(d,a,b)) or (cc==0 and on_segment(a,c,d)) or (dd==0 and on_segment(b,c,d))
def winding(p,wall):
    out=0
    for a,b in zip(wall,wall[1:]+wall[:1]):
        assert not on_segment(p,a,b)
        o=orient(a,b,p).sign()
        if le(a[1],p[1]) and not le(b[1],p[1]) and o>0: out+=1
        if le(b[1],p[1]) and not le(a[1],p[1]) and o<0: out-=1
    return out
def convex_hull(points):
    # Sort by exact lexicographic comparisons.
    from functools import cmp_to_key
    def compare(p,q): return (p[0]-q[0]).sign() or (p[1]-q[1]).sign()
    pts=sorted(points,key=cmp_to_key(compare))
    for i in range(1,len(pts)): assert pts[i]!=pts[i-1]
    def half(xs):
      out=[]
      for p in xs:
        while len(out)>=2 and orient(out[-2],out[-1],p).sign()<=0: out.pop()
        out.append(p)
      return out
    return half(pts)[:-1]+half(list(reversed(pts)))[:-1]
def strict_in_hull(p,hull): return all(orient(a,b,p).sign()>0 for a,b in zip(hull,hull[1:]+hull[:1]))
def segment_min(p,q,dp,dq):
    r=sub(p,q); d=sub(dp,dq); A=norm2(d); B=2*dot(r,d); C=norm2(r)
    vals=[C,A+B+C]
    if A:
      t=-B/(2*A)
      if t.sign()>0 and (1-t).sign()>0: vals.append(C-B*B/(4*A))
    return minimum(vals)
def packet(c,s,m,n,hole_i=1,hole_j=1,base=None,amplitude=None):
    h=1-2*c if c.sign()>=0 else 1+2*c
    L=m+n; M=max(m,n); B=2*L; d=h/100 if amplitude is None else amplitude; t=d*d/(100*M*M*B)
    g=h*h/(10**7*L**3); eta=h*h/(10**8*L**3)
    out={}
    for j in range(1,n):
      for i in range(1,m):
        if (i,j)==(hole_i,hole_j): continue
        p=(Q(i)+j*c,j*s) if base is None else base[i,j]
        if j==hole_j:
          coeff=-F(i,hole_i) if i<hole_i else F(m-i,m-hole_i)
          p=add(p,mul(d*coeff,(-s,c)))
        elif i==hole_i:
          coeff=F(j,hole_j) if j<hole_j else -F(n-j,n-hole_j)
          p=add(p,(Q(0),d*coeff))
        else:
          sx=1 if i<hole_i else -1; sy=1 if j<hole_j else -1
          I=i if i<hole_i else m-i; J=j if j<hole_j else n-j
          p=add(p,(t*sx*I,t*(-sx*I*c+sy*J)/s))
        out[(i,j)]=p
        v=p[1]/s; u=p[0]-c*v
        assert all((z-F(1,2)).sign()>0 for z in (s*u,s*(m-u),s*v,s*(n-v)))
    return out,h,g,eta,d,t
def source_pairs(points):
    pairs={}; contacts=[]
    for i,j in combinations(range(len(points)),2):
      z=dist2(points[i],points[j]); assert (z-1).sign()>=0
      pairs[i,j]=z
      if z==1: contacts.append((i,j))
    nbr=[set() for _ in points]
    for i,j in contacts: nbr[i].add(j); nbr[j].add(i)
    assert all(not(nbr[i]&nbr[j]) for i,j in contacts)
    return pairs,contacts,maximum(pairs.values())
def grid_competitor(number):
    width=isqrt(number)
    if width*width<number: width+=1
    points=[(i%width,i//width) for i in range(number)]
    return points,max((a[0]-b[0])**2+(a[1]-b[1])**2 for a,b in combinations(points,2))

angles=[fixtures[0],fixtures[1],('obtuse_13_85',-fixtures[1][1],fixtures[1][2]),
        fixtures[4],('obtuse_critical',-fixtures[4][1],fixtures[4][2]),
        fixtures[7],('obtuse_8_17',-fixtures[7][1],fixtures[7][2]),fixtures[6]]
counts={x:0 for x in ('perturbed_source_pairs','reference_margin_pairs','perturbed_endpoint_pairs',
 'strict_packet_pairs','fixed_wall_edges','packet_winding_checks','retained_isolates',
 'pinned_positive_edges','pinned_equilibria','actual_grid_margin_pairs','actual_grid_endpoint_pairs',
 'actual_grid_strict_pairs','pinned_jump_path_failures','varied_source_pairs',
 'varied_endpoint_pairs','varied_strict_pairs','varied_margin_pairs','star_source_pairs','star_equilibria',
 'star_retained_contact_derivatives','star_segment_pairs','restored_full_pairs','old_bay_pairs')}
records=[]; varied_records=[]; star_records=[]
for name,c,s in angles:
 for m,n in ((3,3),(4,5),(8,6)):
  ref={(i,j):(Q(i)+j*c,j*s) for j in range(n+1) for i in range(m+1)}
  axes=list(ref)
  wall_axes=([(i,0) for i in range(m+1)]+[(m,j) for j in range(1,n+1)]
             +[(i,n) for i in reversed(range(m))]+[(0,j) for j in reversed(range(1,n))])
  Qpacket,h,g,eta,d,t2=packet(c,s,m,n)
  refwall=[ref[z] for z in wall_axes]
  for x,y in combinations(list(Qpacket.values()),2):
    assert (dist2(x,y)-(1+g)*(1+g)).sign()>=0; counts['reference_margin_pairs']+=1
  for x in Qpacket.values():
    for y in refwall:
      assert (dist2(x,y)-(1+g)*(1+g)).sign()>=0; counts['reference_margin_pairs']+=1
  for divisor in (10**12,10**13):
    assert not h.b
    rot_t=h.a*h.a/F(divisor*(m+n)**4)
    rc=Q((1-rot_t*rot_t)/(1+rot_t*rot_t)); rs=Q(2*rot_t/(1+rot_t*rot_t))
    ua=(rc,rs); va=(rc*c+rs*s,rc*s-rs*c)
    actual={}
    for i,j in axes:
      U=(Q(0),Q(0)) if i==0 else (rc+i-1,rs)
      V=(Q(0),Q(0)) if j==0 else (va[0]+(j-1)*c,va[1]+(j-1)*s)
      actual[i,j]=add(U,V)
      assert (eta*eta-dist2(actual[i,j],ref[i,j])).sign()>0
    actualwall=[actual[z] for z in wall_axes]
    for i in range(len(actualwall)):
      assert dist2(actualwall[i],actualwall[(i+1)%len(actualwall)])==1
      counts['fixed_wall_edges']+=1
      for j in range(i+1,len(actualwall)):
        if j==i+1 or (i==0 and j==len(actualwall)-1): continue
        assert not intersect(actualwall[i],actualwall[(i+1)%len(actualwall)],actualwall[j],actualwall[(j+1)%len(actualwall)])
    extra=[sub(actual[0,0],ua),sub(actual[0,n],ua),
           add(actual[m,0],(Q(1),Q(0))),add(actual[m,n],(Q(1),Q(0))),
           (Q(F(m,2))+F(n,2)*c,n*s+10)]
    old=[actual[z] for z in axes]+extra
    old_pairs,contacts,D2=source_pairs(old); counts['perturbed_source_pairs']+=len(old_pairs)
    assert not any(len(old)-1 in e for e in contacts); counts['retained_isolates']+=1
    for y in extra: assert winding(y,actualwall)==0
    # The old punctured interior has the positive pinned stress from the prior report.
    alpha=rs/s; gamma=(rc*s-rs*c)/s
    force={z:[Q(0),Q(0)] for z in Qpacket}
    pinned={}
    for j in range(1,n):
      for i in range(m):
        e=((i,j),(i+1,j))
        if (1,1) in e: continue
        pinned[e]=alpha*(i-1) if j==1 else Q(1) if i==0 else gamma
    for i in range(1,m):
      for j in range(n):
        e=((i,j),(i,j+1))
        if (1,1) in e: continue
        pinned[e]=alpha*(j-1) if i==1 else Q(1) if j==0 else gamma
    for (a,b),w in pinned.items():
      assert w.sign()>0; counts['pinned_positive_edges']+=1
      r=sub(actual[a],actual[b])
      for z,sgn in ((a,1),(b,-1)):
        if z in force:
          for dim in (0,1): force[z][dim]+=sgn*w*r[dim]
    assert all(z==[Q(0),Q(0)] for z in force.values()); counts['pinned_equilibria']+=len(force)
    fixed=actualwall+extra; new=fixed+list(Qpacket.values())
    assert len(new)==len(old)-1
    for p in Qpacket.values():
      assert winding(p,actualwall)==1; counts['packet_winding_checks']+=1
    for i,j in combinations(range(len(new)),2):
      z=dist2(new[i],new[j]); assert (z-1).sign()>=0 and (D2-z).sign()>=0
      counts['perturbed_endpoint_pairs']+=1
      if i>=len(fixed) or j>=len(fixed):
        assert (z-1).sign()>0 and (D2-z).sign()>0; counts['strict_packet_pairs']+=1
        if i<len(actualwall):
          wall_margin=1+F(9,10)*g
          assert (z-wall_margin*wall_margin).sign()>0
        if i>=len(actualwall) and i<len(fixed): assert (z-3).sign()>0
    competitor,comp_D2=grid_competitor(len(old)); assert (D2-comp_D2).sign()>0
    # Stronger actual-coordinate construction: the contact grid is exact, while
    # its directions differ. The first move is a discrete jump, not a path.
    epsilon=4*rs
    assert (h/(10**4*(m+n))-epsilon).sign()>0
    for z in axes: assert (epsilon*epsilon-dist2(actual[z],ref[z])).sign()>0
    for (i,j) in axes:
      for z in ((i+1,j),(i,j+1)):
        if z in actual: assert dist2(actual[i,j],actual[z])==1
    local_packet,_,_,_,local_d,local_t=packet(c,s,m,n,base=actual,amplitude=16*max(m,n)*epsilon)
    local_margin=local_t/3
    for p,q in combinations(list(local_packet.values()),2):
      assert (dist2(p,q)-(1+local_margin)*(1+local_margin)).sign()>0
      counts['actual_grid_margin_pairs']+=1
    for p in local_packet.values():
      for q in actualwall:
        assert (dist2(p,q)-(1+local_margin)*(1+local_margin)).sign()>0
        counts['actual_grid_margin_pairs']+=1
      assert winding(p,actualwall)==1
    local_new=fixed+list(local_packet.values())
    for i,j in combinations(range(len(local_new)),2):
      z=dist2(local_new[i],local_new[j]); assert (z-1).sign()>=0 and (D2-z).sign()>=0
      counts['actual_grid_endpoint_pairs']+=1
      if i>=len(fixed) or j>=len(fixed):
        assert (z-1).sign()>0 and (D2-z).sign()>0
        counts['actual_grid_strict_pairs']+=1
    displacement=maximum(dist2(local_packet[z],actual[z]) for z in local_packet)
    assert (local_d*local_d-displacement).sign()>=0 and displacement.sign()>0
    # The endpoints are certified, but the initial jump cannot be replaced by
    # its straight segment: at least one actual pinned contact falls below one.
    first_dp={z:sub(local_packet[z],actual[z]) if z[0]==1 or z[1]==1 else (Q(0),Q(0)) for z in local_packet}
    failed_jump=False
    for (za,zb) in pinned:
      da=first_dp.get(za,(Q(0),Q(0))); db=first_dp.get(zb,(Q(0),Q(0)))
      if (segment_min(actual[za],actual[zb],da,db)-1).sign()<0:
        failed_jump=True; break
    assert failed_jump; counts['pinned_jump_path_failures']+=1
    records.append({'angle':name,'m':m,'n':n,'rotation_parameter':str(rot_t),
      'h':h.serial(),'packet_margin':g.serial(),'coordinate_tolerance':eta.serial(),
      'first_amplitude':d.serial(),'second_amplitude':t2.serial(),
      'old_population':len(old),'new_population':len(new),'old_diameter_squared':D2.serial(),
      'smaller_competitor_diameter_squared':comp_D2,
      'pinned_positive_alpha':alpha.serial(),'pinned_positive_gamma':gamma.serial(),
      'actual_coordinate_error_bound':epsilon.serial(),'actual_first_jump':local_d.serial(),
      'actual_second_amplitude':local_t.serial(),'actual_packet_margin':local_margin.serial(),
      'actual_maximum_label_displacement_squared':displacement.serial()})

# Adversarial actual-grid charts much nearer the linear tolerance, with several
# varying train directions and three vacancy positions. Include near-triangular
# rational angles; these fixtures do not assume pinned stress.
varied_angles=angles+[]
for tan_half in (F(289,500),F(577351,10**6)):
  cc=Q((1-tan_half*tan_half)/(1+tan_half*tan_half)); ss=Q(2*tan_half/(1+tan_half*tan_half))
  assert cc.sign()>0 and (1-2*cc).sign()>0
  varied_angles += [('near_triangular_'+str(tan_half),cc,ss),('near_obtuse_'+str(tan_half),-cc,ss)]
for name,c,s in varied_angles:
 for m,n in ((3,3),(4,5),(8,6)):
  L=m+n; M=max(m,n); h=1-2*c if c.sign()>=0 else 1+2*c
  rt=h.a/F(100000*L*L); epsilon=Q(4*L*rt)
  assert (h/(10000*L)-epsilon).sign()>0
  def rotated(p,r):
    rr=Q((1-r*r)/(1+r*r)); zz=Q(2*r/(1+r*r))
    return (rr*p[0]-zz*p[1],zz*p[0]+rr*p[1])
  u_steps=[rotated((Q(1),Q(0)),(i%3-1)*rt) for i in range(1,m+1)]
  v_steps=[rotated((c,s),((2*j)%3-1)*rt) for j in range(1,n+1)]
  U=[(Q(0),Q(0))]; V=[(Q(0),Q(0))]
  for p in u_steps: U.append(add(U[-1],p))
  for p in v_steps: V.append(add(V[-1],p))
  actual={(i,j):add(U[i],V[j]) for j in range(n+1) for i in range(m+1)}
  wall_axes=([(i,0) for i in range(m+1)]+[(m,j) for j in range(1,n+1)]
             +[(i,n) for i in reversed(range(m))]+[(0,j) for j in reversed(range(1,n))])
  wall=[actual[z] for z in wall_axes]
  for z,p in actual.items():
    reference=(Q(z[0])+z[1]*c,z[1]*s)
    assert (epsilon*epsilon-dist2(p,reference)).sign()>0
    for q in ((z[0]+1,z[1]),(z[0],z[1]+1)):
      if q in actual: assert dist2(p,actual[q])==1
  for i in range(len(wall)):
    for j in range(i+1,len(wall)):
      if j==i+1 or (i==0 and j==len(wall)-1): continue
      assert not intersect(wall[i],wall[(i+1)%len(wall)],wall[j],wall[(j+1)%len(wall)])
  extra=[sub(actual[0,0],u_steps[0]),sub(actual[0,n],u_steps[0]),
         add(actual[m,0],u_steps[-1]),add(actual[m,n],u_steps[-1]),
         (Q(F(m,2))+F(n,2)*c,n*s+10)]
  old=list(actual.values())+extra
  pairs,contacts,D2=source_pairs(old); counts['varied_source_pairs']+=len(pairs)
  assert not any(len(old)-1 in e for e in contacts)
  fixed=wall+extra
  for a,b in ((1,1),(m-1,n-1),(m//2,n//2)):
    pck,_,_,_,dd,tt=packet(c,s,m,n,a,b,base=actual,amplitude=16*M*epsilon)
    margin=tt/3
    for p,q in combinations(list(pck.values()),2):
      assert (dist2(p,q)-(1+margin)*(1+margin)).sign()>0; counts['varied_margin_pairs']+=1
    for p in pck.values():
      assert winding(p,wall)==1
      for q in wall:
        assert (dist2(p,q)-(1+margin)*(1+margin)).sign()>0; counts['varied_margin_pairs']+=1
    endpoint=fixed+list(pck.values()); assert len(endpoint)==len(old)-1
    for i,j in combinations(range(len(endpoint)),2):
      z=dist2(endpoint[i],endpoint[j]); assert (z-1).sign()>=0 and (D2-z).sign()>=0
      counts['varied_endpoint_pairs']+=1
      if i>=len(fixed) or j>=len(fixed):
        assert (z-1).sign()>0 and (D2-z).sign()>0; counts['varied_strict_pairs']+=1
    jump=maximum(dist2(pck[z],actual[z]) for z in pck)
    assert (dd*dd-jump).sign()>=0
    _,comp_D2=grid_competitor(len(old)); assert (D2-comp_D2).sign()>0
    varied_records.append({'angle':name,'m':m,'n':n,'vacancy':[a,b],
      'maximum_train_rotation_parameter':str(rt),'coordinate_error_bound':epsilon.serial(),
      'allowed_coordinate_tolerance':(h/(10000*L)).serial(),'first_jump':dd.serial(),
      'second_amplitude':tt.serial(),'packet_margin':margin.serial(),
      'maximum_label_displacement_squared':jump.serial(),'old_diameter_squared':D2.serial(),
      'smaller_competitor_diameter_squared':comp_D2})

# A full-source stress and contraction diagnostic in the exact star-chain regime.
for name,c,s in angles:
  m=n=3; K=12; b=1; D=m+2*K
  ref={(i,j):(Q(i)+j*c,j*s) for j in range(n+1) for i in range(m+1)}
  axes=list(ref)
  extras=[(i,b) for i in range(-K,0)]+[(i,b) for i in range(m+1,m+K+1)]
  all_axes=axes+extras
  old=[ref[z] if z in ref else (Q(z[0])+z[1]*c,z[1]*s) for z in all_axes]
  ix={z:k for k,z in enumerate(all_axes)}
  old_pairs,contacts,D2=source_pairs(old); counts['star_source_pairs']+=len(old_pairs)
  assert D2==D*D
  diameters=[e for e,z in old_pairs.items() if z==D2]
  endpoints=tuple(sorted((ix[-K,b],ix[m+K,b])))
  assert diameters==[endpoints]
  weights={tuple(sorted((ix[i,b],ix[i+1,b]))):Q(D) for i in range(-K,m+K)}
  assert set(weights)<=set(contacts)
  force=[[Q(0),Q(0)] for _ in old]
  for e,w in list(weights.items())+[(endpoints,Q(-1))]:
    x,y=e; r=sub(old[x],old[y])
    for k,sgn in ((x,1),(y,-1)):
      for dim in (0,1): force[k][dim]+=sgn*w*r[dim]
  assert all(z==[Q(0),Q(0)] for z in force); counts['star_equilibria']+=len(old)
  assert sum(weights.values(),Q(0))==D2
  rows=[]
  for x,y in contacts+diameters:
    r=sub(old[x],old[y]); row=[Q(0)]*(2*len(old))
    for k,sgn in ((x,1),(y,-1)):
      row[2*k],row[2*k+1]=sgn*r[0],sgn*r[1]
    rows.append(row)
  assert len(rows)==49 and rank(rows)==48
  Qpacket,h,g,eta,d,t2=packet(c,s,m,n)
  fixed_axes=[z for z in all_axes if not (0<z[0]<m and 0<z[1]<n)]
  fixed=[old[ix[z]] for z in fixed_axes]
  retained=fixed+list(Qpacket.values())
  assert len(retained)==len(old)-1
  velocity=[]; wall_X={}
  for i,j in fixed_axes:
    if i<0: X=Q(K+2+i); Y=Q(b)
    elif i>m: X=Q(-K-2+i-m); Y=Q(b)
    else:
      X=Q(F(2*i-m,2)); Y=Q(j)
      if j==b and i==0: X=Q(K+2)
      if j==b and i==m: X=Q(-K-2)
      wall_X[i,j]=X
    velocity.append((X,(Y-c*X)/s))
  velocity += [(Q(0),Q(0)) for _ in Qpacket]
  retained_pairs,ret_contacts,ret_D2=source_pairs(retained); assert ret_D2==D2
  # Explicit radial signs for the whole actual active set.
  for x,y in ret_contacts:
    assert dot(sub(retained[x],retained[y]),sub(velocity[x],velocity[y]))==1
    counts['star_retained_contact_derivatives']+=1
  idx={z:k for k,z in enumerate(fixed_axes)}
  aa,bb=idx[-K,b],idx[m+K,b]
  Hwork=dot(sub(retained[aa],retained[bb]),sub(velocity[aa],velocity[bb]))
  assert Hwork==-4*D
  span=wall_X[m,b]-wall_X[0,b]; assert span==-2*(K+2)
  old_contact_work=Q(0)
  for x,y in ret_contacts:
    assert x<len(fixed_axes) and y<len(fixed_axes)
    za,zb=fixed_axes[x],fixed_axes[y]
    weight=weights.get(tuple(sorted((ix[za],ix[zb]))),Q(0))
    old_contact_work+=weight*dot(sub(retained[x],retained[y]),sub(velocity[x],velocity[y]))
  assert D*span==Hwork-old_contact_work and old_contact_work==2*K*D
  step=F(1,100)
  for attempt in range(150):
    dp=[mul(step,v) for v in velocity]; endpoint=[add(p,q) for p,q in zip(retained,dp)]
    good=True
    for x,y in combinations(range(len(retained)),2):
      z=dist2(endpoint[x],endpoint[y])
      if (segment_min(retained[x],retained[y],dp[x],dp[y])-1).sign()<0 or (z-1).sign()<=0 or (D2-z).sign()<=0:
        good=False; break
    if good: break
    step/=2
  else: raise AssertionError(('no finite star step',name))
  for x,y in combinations(range(len(retained)),2):
    assert (segment_min(retained[x],retained[y],dp[x],dp[y])-1).sign()>=0
    assert (D2-dist2(endpoint[x],endpoint[y])).sign()>0
    counts['star_segment_pairs']+=1
  # The separate bay is outside the old chart and was already strictly spare.
  bay=(Q(F(-5,2))+b*c,b*s+1)
  assert strict_in_hull(bay,convex_hull(old))
  for p in old:
    assert (dist2(bay,p)-1).sign()>0; counts['old_bay_pairs']+=1
  assert strict_in_hull(bay,convex_hull(endpoint))
  restored=endpoint+[bay]; assert len(restored)==len(old)
  restored_max=Q(0)
  for x,y in combinations(range(len(restored)),2):
    z=dist2(restored[x],restored[y]); assert (z-1).sign()>0 and (D2-z).sign()>0
    if (z-restored_max).sign()>0: restored_max=z
    counts['restored_full_pairs']+=1
  comp,comp_D2=grid_competitor(len(old)); assert (D2-comp_D2).sign()>0
  star_records.append({'angle':name,'original_population':len(old),'diameter':D,
    'normalized_beta':1,'chain_contact_weight':D,'full_row_count':len(rows),'full_row_rank':48,
    'selected_core_vertices':D+1,'selected_core_mixed_rank':D,'canonical_required_rank':2*(D+1)-3,
    'contracting_span_derivative':span.serial(),'diameter_radial_work':Hwork.serial(),
    'outside_chain_contact_work':old_contact_work.serial(),'finite_step':str(step),
    'bay':[z.serial() for z in bay],'restored_diameter_squared':restored_max.serial(),
    'smaller_competitor_diameter_squared':comp_D2,
    'restored_positions':[[z.serial() for z in p] for p in restored]})

out=Path(__file__).with_name('target_c_effective_fixed_wall_packet_slot07_certificate_2026_10_10.json')
out.write_text(json.dumps({'arithmetic':'exact rational and Q(sqrt(15))',
 'counts':counts,'perturbed_fixtures':records,'varied_actual_grid_fixtures':varied_records,'star_fixtures':star_records,
 'limits':'Finite actual charts, endpoints and star segments only. The star bay was already spare; no canonical extraction, new restoration payment, global optimality, or Level I resolution is certified.'},indent=2)+'\n')
print('PASS: effective packet '+json.dumps(counts)+'; '+str(len(records))+' perturbed, '+str(len(varied_records))+' varied and '+str(len(star_records))+' star fixtures.')
