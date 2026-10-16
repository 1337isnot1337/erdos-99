#!/usr/bin/env python3
from collections import Counter
import argparse, contextlib, importlib.util, io, pickle, time
from pathlib import Path
HERE=Path('.').resolve(); BASE=HERE/'research'/'verify_target_c_support7_global_segment_relative_six_noroot_k5_2026_09_20.py'
spec=importlib.util.spec_from_file_location('S',BASE); S=importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()): spec.loader.exec_module(S)
R=S.R

def load_cover(cache):
    if cache:
        with open(cache,'rb') as f: keys,cover,info=pickle.load(f)
        assert len(keys)==105 and len(cover)==325955 and len(info)==105
        return keys,cover,info
    keys,five,osz,aug=S.K.five_no_root_orbits(); assert len(five)==20451 and sum(osz)==96560646 and aug==20475
    cover=S.six_augmentation_cover(keys,five); _,info=S.local_cycle_data(keys); assert len(cover)==325955
    return keys,cover,info

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--cover-cache'); a=ap.parse_args(); t0=time.time()
    assert R.lucas_lehmer_127(); assert max(sum(x*x for x in row) for row in S.COMPLETE_T)==12; assert R.P*R.P>12**15
    keys,cover,info=load_cover(a.cover_cache); rc={}
    def deficiency(C):
        C=tuple(C); d=rc.get(C)
        if d is None: d=len(C)-R.rank_mod([S.COMPLETE_T[b] for b in C]); rc[C]=d
        return d
    def six_data(ext,line):
        vals,lines,empty,singles=S.block_profile(ext,info)
        if line not in lines: return None
        C=tuple(sorted(b for b in vals if empty[b]!=line)); d=deficiency(C)
        cap=sum(any(x is None or x==line for x in singles[b]) for b in C)
        return d,cap
    def seven_data(ext,line):
        vals={}
        for pos,e in enumerate(ext):
            for b,x,y in info[e]:
                vals.setdefault(b,[[0,0] for _ in range(7)]); vals[b][pos]=[x,y]
        C=[]; cap=[]
        for b,v in vals.items():
            x=S.primitive_line(tuple(z[0] for z in v)); y=S.primitive_line(tuple(z[1] for z in v))
            if (x is None or x==line) and (y is None or y==line): continue
            C.append(b)
            for lx,ly in R.LOCAL:
                n=S.primitive_line(tuple(lx*z[1]-ly*z[0] for z in v))
                if n is None or n==line:
                    cap.append(b); break
        C=tuple(sorted(C)); return deficiency(C),tuple(sorted(cap))
    high={}; hp=Counter(); support2=0
    for idx,ext in enumerate(cover):
        vals,lines,empty,singles=S.block_profile(ext,info)
        for line in lines:
            if sum(x!=0 for x in line)!=2: continue
            support2+=1; C=tuple(sorted(b for b in vals if empty[b]!=line))
            if deficiency(C)!=3: continue
            cap=sum(any(x is None or x==line for x in singles[b]) for b in C)
            if cap>=7: high[(tuple(ext),line)]=cap; hp[cap]+=1
        if (idx+1)%100000==0: print('cover',idx+1,'high',len(high),'elapsed',round(time.time()-t0,1),flush=True)
    assert dict(sorted(hp.items()))=={7:76,8:114,9:139,10:64}; assert len(high)==393
    seen=set(); st=Counter(); surv=[]
    for ext6,line6 in high:
        coeff=dict(zip(ext6,line6))
        for new in range(105):
            if new in coeff: continue
            ext7=tuple(sorted(ext6+(new,))); line7=S.primitive_line(tuple(coeff.get(e,0) for e in ext7))
            assert line7 is not None and sum(x!=0 for x in line7)==2
            key=(ext7,line7)
            if key in seen: continue
            seen.add(key); st['children']+=1
            zeros=[j for j,x in enumerate(line7) if x==0]; caps=[]; ok=True
            for j in zeros:
                sd=six_data(ext7[:j]+ext7[j+1:],S.primitive_line(line7[:j]+line7[j+1:]))
                if sd is None or sd[0]!=3 or sd[1]<7: ok=False; break
                caps.append(sd[1])
            if not ok: continue
            st['all5_d3cap7']+=1
            if sum(c>=8 for c in caps)<2: continue
            st['two_cap8']+=1
            d7,cb=seven_data(ext7,line7); st[f'global_d{d7}']+=1
            if d7==3 and len(cb)>=10: surv.append((ext7,line7,len(cb),tuple(sorted(caps)))); st['global_d3cap10']+=1
    print('support2_states_scanned',support2); print('support2_d3_cap7',dict(sorted(hp.items()))); print('support2_d3_cap7_total',len(high)); print('stages',dict(st)); print('survivor_count',len(surv));
    for x in surv[:20]: print('SURV',x)
    print('unique_complete_sets_ranked',len(rc)); print('hadamard_exact_rank_bound',R.P*R.P>12**15); print('elapsed',round(time.time()-t0,2)); assert not surv; print('PASS: final seven-no-root k6,p10 support-two branch closed')
if __name__=='__main__': main()
