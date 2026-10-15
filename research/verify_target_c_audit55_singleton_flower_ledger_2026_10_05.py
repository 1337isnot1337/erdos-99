#!/usr/bin/env python3
from fractions import Fraction as F

def check_singleton_composition():
    checks=0
    # Small exhaustive integer packets satisfying the exact hull-depletion ledger.
    for m in range(4):
      for u in range(4):
       x=m+u
       for E in range(x+1):
        G=x-E
        for P5 in range(4):
         for X in range(3):
          cap=x+m+2*P5+4*X+3
          for Sg in range(min(cap,5)+1):
           for S0 in range(3):
            for sig in range(4):
             for d in range(3):
              for k in range(3):
               for q in range(2,6):
                PF=q+E
                b=PF+G
                for r4 in range(1,5):
                 # Solve S.10 for M; retain integral nonnegative solutions.
                 lhs=5*m+4*(Sg+S0)+2*sig+5*d
                 num=lhs-2*b+8*r4-5*k-2*X
                 if num < 0 or num % 5: continue
                 M=num//5
                 for rb in range(r4+1):
                  if M-S0 < 2*rb: continue
                  # GH.2
                  L=13*E+11*G+8*P5+14*X+2*sig+5*d+12
                  R=2*PF-8*r4+10*rb+S0+5*k
                  assert L >= R, (m,u,E,G,P5,X,Sg,S0,sig,d,k,q,r4,M,rb,L,R)
                  checks+=1
    return checks

def check_flower_payment():
    checks=0
    for r4 in range(1,8):
     for rb in range(r4+1):
      delta=F(r4-rb)
      for sig in range(0,8):
       a=F(sig,2)
       psi=F(sig)*(3*F(r4)+a)/(2*F(r4)+a)
       assert F(sig) <= psi <= F(3*sig,2)
       for eta in range(4):
        for m in range(4):
         for d in range(3):
          for X in range(3):
           for Sg in range(3):
            for k in range(7):
             lower=F(rb)-F(3*eta,2)-F(m,2)+F(k,2)-F(d,2)-X-2*Sg
             upper=F(r4)+1+a*(3*F(r4)+a)/(2*F(r4)+a)
             if lower > upper: continue
             rhs=2*delta+2+psi+3*eta+m+d+2*X+4*Sg
             assert F(k) <= rhs, (r4,rb,sig,eta,m,d,X,Sg,k,lower,upper,rhs)
             coarse=2*delta+2+F(3*sig,2)+3*eta+m+d+2*X+4*Sg
             assert F(k) <= coarse
             checks+=1
    return checks

def check_blocker_rearrangement():
    checks=0
    for T in range(1,30):
     total=T*(T-1)//2
     for M in range(0,15):
      # Only packets satisfying the blocker missing-pair premise.
      need=F(T*max(M-2,0),2)
      for R in range(total+1):
       miss=total-R
       if F(miss) < need: continue
       # For M>=2 the exact theorem yields this displayed upper bound.
       if M>=2:
        assert F(M) <= F(T+1)-F(2*R,T), (T,M,R)
       checks+=1
    return checks

def check_balanced_constants():
    # If k/D >= kap and each defect <= cD, (4) forces kap <= 23c/2.
    for num in range(1,30):
      kap=F(num,20)
      c=F(2,23)*kap
      rhs=F(3,2)*c+3*c+c+2*c+4*c
      assert rhs == kap
    # GH.3 coefficient sum.
    assert 13+11+8+14+2 == 48
    return 29

if __name__=="__main__":
    a=check_singleton_composition()
    b=check_flower_payment()
    c=check_blocker_rearrangement()
    d=check_balanced_constants()
    print(f"PASS: {a} exact good-hull singleton/depletion ledger packets")
    print(f"PASS: {b} exact full-flower k-payment packets and Psi bounds")
    print(f"PASS: {c} blocker missing-pair rearrangement packets")
    print(f"PASS: {d} balanced coefficient identities")
    print("SCOPE: algebra/cancellation only; geometric endpoint-fan, pentagon-turn and projective-blocker proofs are analytic")
