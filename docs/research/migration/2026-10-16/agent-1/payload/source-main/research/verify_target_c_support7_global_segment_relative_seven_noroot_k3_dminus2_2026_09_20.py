#!/usr/bin/env python3
"""Exact closure of the seven-no-root D=-2, k=3 Target-C density branch.

The seven-no-root depth-two deletion theorem shows that a hypothetical
D=-2 counterexample has a coefficient-constraint space P such that deleting
any one or any two no-root coordinates preserves rank(P). The exact identity
D=7+p+3d-3k shows that k=3 forces d=p=0 and rank(P)=4.

This verifier uses deletion shadows instead of scanning all 4,546,114
seven-subset S7 orbits. Its four stages are `five`, `merge-five`, `six`, and
`seven`. A full run finds 340 five-row d=0,p=0 rank-four states on 74 of the
20,451 five-cycle orbit representatives; their synchronized six-row extensions
reduce to 47 normalized states on three cycle sets; all 4,653 seventh-cycle
extensions fail the required pair-deletion rank condition.

All coefficient-space calculations are exact Fraction operations through the
committed base verifier. Complete-block ranks use the already certified
2^127-1 modular/Hadamard exact-rank framework; this verifier introduces no new
T-space relation-row type.
"""
from argparse import ArgumentParser
from collections import Counter
from pathlib import Path
import contextlib, importlib.util, io, pickle, time

HERE=Path(__file__).resolve().parent
RESEARCH=HERE if HERE.name=='research' else HERE/'research'
BASE=RESEARCH/'verify_target_c_support7_global_segment_relative_five_noroot_k3_containment_2026_09_20.py'
spec=importlib.util.spec_from_file_location('seven_noroot_k3_base',BASE)
G=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(G)
P0=G.P0; R=G.R; K=G.K

def cycle_key(desc):
 d=list(desc); return tuple(sorted(tuple(sorted((d[i],d[(i+1)%4]))) for i in range(4)))
def touched_blocks(ext):
 return tuple(b for b in range(35) if any(R.QCOMP[e][b]!=(0,0) for e in ext))
def project_space(space,drops):
 if isinstance(drops,int): drops=(drops,)
 D=set(drops)
 return R.rowspace_key(tuple(tuple(x for j,x in enumerate(row) if j not in D) for row in space))
def permute_space(space,old_ext,new_ext):
 pos={e:i for i,e in enumerate(old_ext)}
 return R.rowspace_key(tuple(tuple(row[pos[e]] for e in new_ext) for row in space))

class DeficiencyCache:
 def __init__(self): self.cache={}
 def __call__(self,complete):
  complete=tuple(sorted(complete)); basis=self.cache.get(complete)
  if basis is None:
   basis=G.rref_basis_mod([P0.COMPLETE_T[b] for b in complete]); self.cache[complete]=basis
  return len(complete)-len(basis)

def five_parent_candidates(ext,deficiency):
 touched=touched_blocks(ext); empty={b:R.local_constraint_key(ext,b,0) for b in touched}; spaces={()}
 for b in touched:
  E=empty[b]; nxt=set(spaces)
  for s in spaces:
   u=R.union_key(s,E)
   if len(u)<=4: nxt.add(u)
  spaces=nxt
 out=[]
 for P in spaces:
  if len(P)!=4: continue
  complete=tuple(b for b in touched if not R.is_subspace(empty[b],P))
  if deficiency(complete)!=0: continue
  generated=()
  for b in touched:
   if R.is_subspace(empty[b],P): generated=R.union_key(generated,empty[b])
  assert generated==P
  out.append((P,complete,touched))
 return tuple(out)

def scan_five(start,end):
 keys,orbits,orbit_sizes,augmentation_candidates=K.five_no_root_orbits()
 assert len(orbits)==20451 and sum(orbit_sizes)==96560646 and augmentation_candidates==20475
 assert 0<=start<=end<=len(orbits)
 key_to_global={cycle_key(R.DESC[e]):e for e in R.NO_ROOT}; deficiency=DeficiencyCache(); parents=[]; dist=Counter(); t0=time.time()
 for oi in range(start,end):
  local=orbits[oi]; ext=tuple(key_to_global[keys[i]] for i in local); cand=five_parent_candidates(ext,deficiency); dist[len(cand)]+=1
  for P,C,T in cand: parents.append((oi,tuple(local),ext,P,C,T))
 return tuple(parents),dist,len(deficiency.cache),time.time()-t0

def extend_parent_to_six(ext6,parent_P,deficiency):
 touched=touched_blocks(ext6); empty={b:R.local_constraint_key(ext6,b,0) for b in touched}
 eligible=[(b,E) for b,E in empty.items() if R.is_subspace(project_space(E,5),parent_P)]; spaces={()}
 for _b,E in eligible:
  nxt=set(spaces)
  for s in spaces:
   u=R.union_key(s,E)
   if len(u)<=4:nxt.add(u)
  spaces=nxt
 out=[]
 for P in spaces:
  if len(P)!=4 or project_space(P,5)!=parent_P:continue
  if any(len(project_space(P,i))!=4 for i in range(6)):continue
  complete=tuple(b for b in touched if not R.is_subspace(empty[b],P))
  if deficiency(complete)!=0:continue
  generated=()
  for b in touched:
   if R.is_subspace(empty[b],P):generated=R.union_key(generated,empty[b])
  assert generated==P
  out.append((P,complete,touched))
 return tuple(out),len(spaces),len(eligible)

def scan_six(five_parents):
 deficiency=DeficiencyCache();counts=Counter();raw=[];maxspaces=maxelig=0;t0=time.time()
 for _oi,_local,ext5,P5,_C5,_T5 in five_parents:
  for extra in R.NO_ROOT:
   if extra in ext5:continue
   ext6=tuple(ext5)+(extra,);counts['extensions']+=1
   cand,nsp,ne=extend_parent_to_six(ext6,P5,deficiency);maxspaces=max(maxspaces,nsp);maxelig=max(maxelig,ne);counts['raw_candidates']+=len(cand)
   for P6,C6,T6 in cand:
    sext=tuple(sorted(ext6));raw.append((sext,permute_space(P6,ext6,sext),C6,T6))
 unique={(x[0],x[1]):x for x in raw}
 return tuple(unique.values()),counts,maxspaces,maxelig,len(deficiency.cache),time.time()-t0

def extend_parent_to_seven(ext7,parent_P):
 touched=touched_blocks(ext7); eligible=[]
 for b in touched:
  E=R.local_constraint_key(ext7,b,0)
  if R.is_subspace(project_space(E,6),parent_P):eligible.append(E)
 spaces={()}
 for E in eligible:
  nxt=set(spaces)
  for s in spaces:
   u=R.union_key(s,E)
   if len(u)<=4:nxt.add(u)
  spaces=nxt
 cand=tuple(P for P in spaces if len(P)==4 and project_space(P,6)==parent_P and all(len(project_space(P,i))==4 for i in range(7)))
 return cand,len(spaces),len(eligible)

def scan_seven(six_parents):
 counts=Counter();minrank=Counter();badcount=Counter();badextra=Counter();survivors=[];maxspaces=maxelig=0;t0=time.time()
 for ext6,P6,_C6,_T6 in six_parents:
  assert tuple(ext6)==tuple(sorted(ext6))
  for extra in R.NO_ROOT:
   if extra in ext6:continue
   ext7=tuple(ext6)+(extra,);counts['extensions']+=1
   cand,nsp,ne=extend_parent_to_seven(ext7,P6);maxspaces=max(maxspaces,nsp);maxelig=max(maxelig,ne);counts['single_deletion_synchronized_candidates']+=len(cand)
   for P7 in cand:
    ranks=[(i,j,len(project_space(P7,(i,j)))) for i in range(7) for j in range(i+1,7)]
    m=min(r for _i,_j,r in ranks);bad=tuple((i,j) for i,j,r in ranks if r<4)
    minrank[m]+=1;badcount[len(bad)]+=1;badextra[sum(6 in q for q in bad)]+=1
    if not bad:survivors.append((ext7,P7))
 return counts,minrank,badcount,badextra,tuple(survivors),maxspaces,maxelig,time.time()-t0

def save(path,value):
 with open(path,'wb') as f:pickle.dump(value,f,protocol=pickle.HIGHEST_PROTOCOL)
def load(path):
 with open(path,'rb') as f:return pickle.load(f)

def main():
 ap=ArgumentParser();sub=ap.add_subparsers(dest='stage',required=True)
 p=sub.add_parser('five');p.add_argument('--start',type=int,default=0);p.add_argument('--end',type=int,default=20451);p.add_argument('--output',required=True)
 p=sub.add_parser('merge-five');p.add_argument('--inputs',nargs='+',required=True);p.add_argument('--output',required=True)
 p=sub.add_parser('six');p.add_argument('--input',required=True);p.add_argument('--output',required=True)
 p=sub.add_parser('seven');p.add_argument('--input',required=True)
 a=ap.parse_args()
 assert R.lucas_lehmer_127(); B=max(sum(x*x for x in row) for row in P0.COMPLETE_T);assert B==12 and R.P*R.P>B**15
 if a.stage=='five':
  parents,dist,ncache,secs=scan_five(a.start,a.end);save(a.output,parents)
  print('PASS: five-row boundary shard');print('orbit_range',a.start,a.end);print('states',len(parents));print('orbits_with_states',sum(v for k,v in dist.items() if k));print('states_per_orbit_distribution',dict(sorted(dist.items())));print('complete_rank_cache_size',ncache);print('seconds',round(secs,3));print('output',a.output);return
 if a.stage=='merge-five':
  parents=tuple(x for path in a.inputs for x in load(path));pairs={(x[0],x[3]) for x in parents};assert len(pairs)==len(parents)
  if len(parents)==340:assert len({x[0] for x in parents})==74
  save(a.output,parents);print('PASS: merged five-row boundary shards');print('states',len(parents));print('orbit_representatives_with_states',len({x[0] for x in parents}));print('output',a.output);return
 if a.stage=='six':
  five=tuple(load(a.input));parents,c,nsp,ne,ncache,secs=scan_six(five)
  if len(five)==340:
   assert c['extensions']==34000 and c['raw_candidates']==63 and len(parents)==47 and len({x[0] for x in parents})==3
   assert dict(sorted(Counter(len(x[2]) for x in parents).items()))=={5:15,6:32}
  save(a.output,parents);print('PASS: six-row synchronized boundary extension');print('five_parent_states',len(five));print('counts',dict(c));print('normalized_six_states',len(parents));print('six_cycle_sets',len({x[0] for x in parents}));print('complete_block_census',dict(sorted(Counter(len(x[2]) for x in parents).items())));print('max_intermediate_spaces',nsp);print('max_eligible_blocks',ne);print('complete_rank_cache_size',ncache);print('seconds',round(secs,3));print('output',a.output);return
 if a.stage=='seven':
  six=tuple(load(a.input));c,mr,bc,be,surv,nsp,ne,secs=scan_seven(six)
  if len(six)==47:
   assert c['extensions']==4653 and c['single_deletion_synchronized_candidates']==4653
   assert dict(sorted(mr.items()))=={3:4653};assert dict(sorted(bc.items()))=={1:36,2:39,3:24,4:1212,6:3342};assert dict(sorted(be.items()))=={0:4653};assert not surv
  print('PASS: seven-no-root D=-2,k=3,d=0,p=0 branch closed');print('six_parent_states',len(six));print('counts',dict(c));print('minimum_pair_projection_rank_census',dict(sorted(mr.items())));print('bad_pair_count_census',dict(sorted(bc.items())));print('bad_pairs_involving_added_coordinate_census',dict(sorted(be.items())));print('depth_two_survivors',len(surv));print('max_intermediate_spaces',nsp);print('max_eligible_blocks',ne);print('seconds',round(secs,3));return
if __name__=='__main__':main()
