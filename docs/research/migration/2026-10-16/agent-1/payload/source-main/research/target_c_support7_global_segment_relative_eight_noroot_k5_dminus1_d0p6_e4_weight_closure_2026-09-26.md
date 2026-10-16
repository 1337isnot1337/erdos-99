# Target C: close p6 e4 by empty-space rank and generalized weights

Date: 2026-09-26

In the final eight-no-root k=5, D=-1, d_root=0, p=6 branch, the existing reduction gives rank(P)=3, generalized weights at least (2,4,5), six touched singleton replacements, no selected pair, and e touched actual-empty blocks. The face-local span bound gives nu(T)<=e+1. For e=4, nu(T)<=5, so the committed support-nullity classification leaves only m=3,4,5,6 with 10,38,108,2 S7 support orbits respectively.

For an empty block b, let E_b be its local constraint space and I_b its coordinate support. If some containing support has multiplicity at least two, then dim E_b=2 and d2(P)>=4 forces |I_b|>=4. Otherwise d1(P)>=2 forces |I_b|>=2. If a,b are both forced rank-two empties, their planes in P intersect nontrivially, so d1(P)>=2 forces |I_a intersect I_b|>=2.

The exact support/multiplicity quotient has 2608 S7-orbits. These necessary incidence conditions leave 183 orbits and 1731 candidate empty quadruples:
- m=4, (3,3,1,1): 2 assignments, 3 quadruples;
- m=5, (3,2,1,1,1): 150 assignments, 363 quadruples;
- m=5, (2,2,2,1,1): 15 assignments, 15 quadruples;
- m=6, (3,1,1,1,1,1): 6 assignments, 1260 quadruples;
- m=6, (2,2,1,1,1,1): 10 assignments, 90 quadruples.

All phase choices give 24,561 phase configurations and 404,865 phase/quadruple pairs. For A the four empty blocks, set U(A)=sum E_b. Rank over F2 is used only as a one-way lower bound: rank_F2(U)>3 implies rank_Q(U)>3. This rejects 404,047 pairs. Exact rational reduction of the remaining 818 gives rank_Q(U)=3 in every case, hence P=U.

The exact generalized-weight census of those 818 spaces is
(2,3,4): 768
(2,3,5): 50.
Every case violates d2(P)>=4. Thus e=4 is empty.

The finite certificate is exhaustive. No external relation-rank computation is used. Combined with the committed e=2 and e=3 closures, the p=6 branch is reduced to e>=5. This does not close Target C or Erdos Problem #99.
