#!/usr/bin/env python3
"""Exact arithmetic/combinatorial checks for the post-#667 Target-C synthesis.

This verifier checks only algebra, interval arithmetic, the high-degree defect
conversion, and the elementary cycle-matching claim. It does not certify the
analytic #667 depletion theorem, Groemer stability, source optimality, or
C-II/Level-I closure.
"""
from fractions import Fraction as F
from itertools import combinations

def atan_interval(x, terms):
    partial = sum(((-1)**j)*x**(2*j+1)/F(2*j+1) for j in range(terms))
    nxt = ((-1)**terms)*x**(2*terms+1)/F(2*terms+1)
    return min(partial, partial+nxt), max(partial, partial+nxt)

def pi_interval():
    a,b = atan_interval(F(1,5),28)
    c,d = atan_interval(F(1,239),9)
    return 16*a-4*d, 16*b-4*c

def sqrt_interval(x, lo, hi, steps=100):
    for _ in range(steps):
        m = (lo+hi)/2
        if m*m < x:
            lo = m
        else:
            hi = m
    return lo,hi

def constant_checks():
    p_lo,p_hi = pi_interval()
    rt3_lo,rt3_hi = sqrt_interval(F(3),F(17,10),F(18,10))
    delta_lo = p_lo/(2*rt3_hi)
    delta_hi = p_hi/(2*rt3_lo)
    s_lo,_ = sqrt_interval(delta_lo,F(9,10),F(1))
    _,s_hi = sqrt_interval(delta_hi,F(9,10),F(1))

    base_lo = 2*(p_lo+s_lo)
    base_hi = 2*(p_hi+s_hi)
    mu_lo = (p_lo+s_lo)/2
    mu_hi = (p_hi+s_hi)/2
    tstar_lo = (3*p_lo+2*s_lo)/5
    tstar_hi = (3*p_hi+2*s_hi)/5

    assert base_lo > F(81878,10000)
    assert base_hi < F(81879,10000)
    assert mu_lo > F(20469,10000)
    assert mu_hi < F(20470,10000)
    assert base_lo/F(15) > F(54585,100000)
    assert base_lo/F(12) > F(68231,100000)
    assert base_lo/F(6) > F(136463,100000)
    assert tstar_lo > F(226588,100000)

    budget = 5*F(1,2)+4*F(13,20)+2*F(3,2)
    assert budget == F(81,10)
    assert budget < base_lo

    # This is retained only as the deliberately weaker one-step calculation
    # described in the report before the exact terminal bootstrap is fed back.
    terminal = F(1959852849540479,10**15)
    mterm_lo = 3*p_lo+2*s_lo-5*terminal
    mterm_hi = 3*p_hi+2*s_hi-5*terminal
    assert mterm_lo > F(153013,100000)
    assert mterm_hi < F(153015,100000)
    assert mterm_lo/2 > F(76506,100000)

    return {
        "base": (float(base_lo),float(base_hi)),
        "mu_hull": (float(mu_lo),float(mu_hi)),
        "equal_m": float(base_lo/15),
        "equal_S": float(base_lo/12),
        "equal_sigma": float(base_lo/6),
        "terminal_t_threshold": (float(tstar_lo),float(tstar_hi)),
        "weaker_terminal_m_step": (float(mterm_lo),float(mterm_hi)),
    }

def ledger_checks():
    checked = 0
    bootstrap = 0
    for q in range(3,22):
      for x in range(q+1):
       b = q+x
       for k in range((q-x)//2+1):
        Q = q-x-2*k
        for f in range(Q+1):
         T = q-k+2*f
         for m in range(x+1):
          good = q-m
          for d in range(min(2,good//2)+1):
           G = good-d
           M = T-G
           if M < 0:
            continue
           z = F((q+2*f)%9+1,3)  # formal z=2*sqrt(R_4)
           tau = F(T)-z
           r = Q-f
           lhs = 5*m+4*tau+5*d
           rhs = 2*b-4*z+5*M+5*k+2*r
           assert lhs == rhs

           for S in (0,min(T,1),min(T,max(0,T//2)),T):
            sigma = 2*(F(T-S)-z)
            assert 5*m+4*S+2*sigma+5*d == rhs

           assert m == M+2*b+5*k-4*q+2*r-d
           assert m == M+2*b+k+2*r-d-4*(q-k)

           u = x-m
           assert u >= 0
           assert 2*(q-k) == M+3*k+m+2*u+2*r-d
           assert 5*(q-k) == 3*q+M+m+2*u+2*r-d
           bootstrap += 1
           checked += 1
    return checked, bootstrap

def second_depletion_checks():
    checked = 0
    for M in range(1,30):
      for S0 in range(M+1):
       for root_bulk_num in range(0,10):
        root_bulk = F(root_bulk_num,2)
        if F(M-S0) < 2*root_bulk:
            continue
        for b in range(3,12):
         for k in range(3):
          for r in range(3):
           root_R = F(root_bulk_num+1,2)
           exact_rhs = 2*b-8*root_R+5*M+5*k+2*r
           lower_rhs = 2*b-8*root_R+5*S0+10*root_bulk+5*k+2*r
           assert exact_rhs >= lower_rhs
           checked += 1
    return checked

def high_degree_tail_checks():
    checked = 0
    # T_M=sum(d-4) for d>M and r_M=sum(d-5)=T_M-f_tail.
    # Since every d-4 >= M-3, f_tail <= T_M/(M-3), hence
    # r_M >= T_M*(1-1/(M-3)).
    for M in range(5,16):
      degs = list(range(M+1,M+8))
      for mask in range(1,1<<len(degs)):
       chosen = [degs[i] for i in range(len(degs)) if mask>>i&1]
       Tm = sum(d-4 for d in chosen)
       rm = sum(d-5 for d in chosen)
       assert rm*(M-3) >= Tm*(M-4)
       checked += 1
    return checked

def max_cycle_matching(q, mask):
    edges = [i for i in range(q) if mask>>i&1]
    best = 0
    for r in range(len(edges)+1):
      for sel in combinations(edges,r):
       used = set()
       ok = True
       for i in sel:
        a,b = i,(i+1)%q
        if a in used or b in used:
         ok = False
         break
        used.add(a)
        used.add(b)
       if ok:
        best = max(best,r)
    return best,len(edges)

def cycle_matching_checks():
    checked = 0
    for q in range(3,11):
      for mask in range(1<<q):
       nu,r = max_cycle_matching(q,mask)
       assert nu >= r//2
       checked += 1
    return checked

def main():
    constants = constant_checks()
    ledgers,bootstrap = ledger_checks()
    second = second_depletion_checks()
    tails = high_degree_tail_checks()
    cycles = cycle_matching_checks()
    print("PASS constants:",constants)
    print("PASS exact synthesis ledgers:",ledgers)
    print("PASS terminal bootstrap identities:",bootstrap)
    print("PASS second-depletion substitutions:",second)
    print("PASS high-degree tail conversions:",tails)
    print("PASS cycle edge-subset matching cases:",cycles)
    print("NOTE: analytic depletion/Groemer/global-minimality claims are not certified here.")

if __name__ == "__main__":
    main()
