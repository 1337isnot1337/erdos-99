# Target C: nine-no-root k=4 reduction

Date: 2026-09-27

Status: proof-level reduction. This does not close the nine-no-root layer, Target C-II, or Erdos Problem #99.

Let B=R union E be a hypothetical counterexample with exactly nine no-root four-cycles, |E|=9, and D(X)=|X|-3 delta(X).

Current main proves D(A)>=0 for every family with at most eight no-root cycles. For any e in E, the standard deletion identity is

D(B\{e})=D(B)-1+3m_e,  m_e in {0,1}.

Since B\{e} has eight no-root rows, D(B\{e})>=0. The case m_e=0 would force D(B)>=1, impossible. Hence m_e=1 for every e and D(B)+2>=0. Therefore

D(B) in {-2,-1}.

The root-block identity is

D(B)=9+p+3 d_root-3k.

Since p,d_root>=0, k<=3 gives D(B)>=0. Thus every nine-no-root counterexample has k>=4.

For k=4,

D(B)=p+3 d_root-3,

so the entire k=4 arithmetic frontier is exactly

- D=-2, d_root=0, p=1;
- D=-1, d_root=0, p=2.

For any nonempty deletion S subset E, |S|=s, let q_S=r_Q(B)-r_Q(B\S). Every external row is an M-coloop, so the committed all-depth identity gives

D(B\S)=D(B)+2s-3q_S>=0.

If P<=Q^9 is the external coefficient-constraint space, q_S is the shortened-subcode dimension supported in S. Therefore

d_j(P)>=ceil((3j-D(B))/2).

In the k=4 layer rank(P)=5. Hence

D=-2: (d1,d2,d3,d4,d5)>=(3,4,6,7,9),
D=-1: (d1,d2,d3,d4,d5)>=(2,4,5,7,8).

Now let T be the touched triangle-block set and C the touched complete blocks. The face-local identity puts all four independent external relation lifts in H(T), so

rank H(T)-rank H(C)>=4.

Both k=4 branches have d_root=0, hence rank H(C)=|C|. Since the full ground-root triangle-row space has rank 15,

|C|<=11.

This sharpens the support search before any orbit enumeration.

For D=-2,p=1, at most one selected incomplete block is touched. If h=|T| and e is the number of touched actual-empty blocks, then e>=h-12. Every actual-empty block has at least three external incidences by d1(P)>=3. The nine no-root cycles give 36 incidences, so

36>=3e+(h-e)=h+2e>=3h-24,

hence

h<=20.

For D=-1,p=2, at most two selected incomplete blocks are touched, so e>=h-13. Every actual-empty block has at least two incidences, giving

36>=2e+(h-e)=h+e>=2h-13,

hence

h<=24.

Thus the first open nine-no-root layer begins with only two k=4 finite searches:

1. D=-2,d_root=0,p=1, rank(P)=5, generalized weights >=(3,4,6,7,9), h<=20.
2. D=-1,d_root=0,p=2, rank(P)=5, generalized weights >=(2,4,5,7,8), h<=24.

A bounded unpruned prototype generation of all size-nine support orbits did not finish within the local execution budget, so no orbit count or computational closure is claimed. The next exact certificate should prune by touched-block count before canonicalization or use a faster exact canonical augmentation.
