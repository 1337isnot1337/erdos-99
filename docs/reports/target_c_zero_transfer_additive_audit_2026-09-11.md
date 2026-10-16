<!-- theorem-state: {"artifact_id":"ART-7418A55D25E0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: audit of the all-terminal zero-transfer exclusion

**Date:** 2026-09-11  
**Status:** STILL OPEN; hold report  
**Target:** C-II  
**Dependencies:** promoted C53/C63 normalization, the C53 circular split representation and interval-sign lemma, C34, C26/C35, and promoted SEPq

## Result

For the C-II contact-minimal, then diameter-pair-minimal source, let \(B\) be the
loaded endpoints of the relative-interior C53 stress and let

\[
K=Q^{\mathsf T}\Lambda^+Q.
\]

If \(D\ge9\), then

\[
\min_{e\ne f}K_{ef}=0
\]

is impossible. The proof applies without \(s_Z=0\), without a forest or cyclic
assumption on \(H\), and without discarding contact-isolated source points.

The proof below audits and slightly corrects the earlier additive report: a split
with zero crossing vector need not be impossible. It has zero contribution to \(K\)
and is simply omitted from the positive split representation.

## Proof

Use the legal C53 projective orientation and order the diameter edges as
\(e_0<\cdots<e_{m-1}\). Write their vectors as

\[
u_i=a_i(1,t_i),\qquad a_i>0,\qquad t_0<\cdots<t_{m-1},
\]

and put \(\gamma_i=a_i\beta_i\). C53 gives

\[
M:=\Gamma(\Beta^{-1}-K)\Gamma\succeq0,\qquad M\mathbf1=Mt=0,
\]

with

\[
M_{ij}=-\gamma_i\gamma_jK_{ij}\quad(i\ne j).
\]

If every off-diagonal \(K_{ij}\ge0\), then \(M\) is a Laplacian with nonnegative
edge weights \(w_{ij}=\gamma_i\gamma_jK_{ij}\). Therefore

\[
0=t^{\mathsf T}Mt
=\sum_{i<j}w_{ij}(t_i-t_j)^2.
\]

The slopes are distinct, so every \(w_{ij}=0\). Thus

\[
K=\Beta^{-1}.
\tag{A.1}
\]

Let \(W\) be the effective-resistance metric of the actual connected
circular-planar contact network. The C53 split theorem gives

\[
W=\sum_A\lambda_A\delta_A,\qquad \lambda_A\ge0,
\]

over circular interval splits. If

\[
z_A=Q^{\mathsf T}\mathbf1_A,
\]

then centering the split metric gives

\[
K=\sum_A\lambda_Az_Az_A^{\mathsf T}.
\tag{A.2}
\]

Splits with \(z_A=0\) have no contribution and will be ignored.

For \(i<j<k\), the C53 interval-sign lemma is

\[
z_k(z_i-z_j)\le0,\qquad z_i(z_k-z_j)\le0.
\tag{A.3}
\]

There are at least three diameter edges: C34 gives

\[
2|B|\ge\lceil D\rceil+2,
\]

so \(D\ge9\) implies \(|B|\ge6\), and every loaded terminal is incident to an
actual diameter edge. In particular \(m\ge3\).

Fix a gap \(i,i+1\). Since (A.1) makes \(K\) diagonal, for \(r<i\), (A.3) with
\((r,i,i+1)\) gives termwise

\[
z_r(z_i-z_{i+1})\ge0,
\]

while for \(r>i+1\), (A.3) gives

\[
z_r(z_i-z_{i+1})\le0.
\]

Consequently the identity

\[
0=K_{r i}-K_{r,i+1}
=\sum_A\lambda_Az_{A,r}(z_{A,i}-z_{A,i+1})
\tag{A.4}
\]

is a sum of terms with one common sign on each side of the gap. Every positive
split therefore satisfies

\[
z_{A,i}\ne z_{A,i+1}
\quad\Longrightarrow\quad
\operatorname{supp}z_A\subseteq\{i,i+1\}.
\tag{A.5}
\]

If a split vector has support on two coordinates, one of the neighboring gaps
compares a nonzero coordinate with a zero coordinate and applies (A.5), forcing
the support into a different two-coordinate set. Since \(m\ge3\), this is
impossible. Hence every positive split vector is either constant, singleton
supported, or zero.

A nonzero constant vector cannot occur. All other nonzero split vectors are
singleton supported, so they contribute no off-diagonal entries to (A.2), whereas
a constant vector contributes

\[
\lambda_A z_{A,r}z_{A,s}>0
\]

to every off-diagonal entry. This contradicts the diagonal form (A.1). Thus every
positive split is singleton supported.

A singleton split separates one loaded terminal from all the others. Summing these
split metrics gives numbers \(r_i\ge0\) with

\[
W_{ij}=r_i+r_j\qquad(i\ne j).
\tag{A.6}
\]

This is a statement about the actual contact network, not an independently chosen
star scaffold.

SEPq now applies to the actual positive contact network. It gives a contact vertex
\(z\) such that every component of \(C-z\) contains at most one loaded terminal,
and hence

\[
\deg_C(z)\ge
\begin{cases}
|B|,&z\notin B,\\
|B|-1,&z\in B.
\end{cases}
\]

C26/C35 give \(\deg_C(z)\le5\) for unloaded \(z\) and
\(\deg_C(z)\le3\) for loaded \(z\). Since \(|B|\ge6\), both alternatives are
impossible. This proves the claim.

## Exact surviving obstruction

The audit closes only the equality alternative. The C53 alternatives are now

\[
\min_{e\ne f}K_{ef}<0.
\]

The proof supplies no quantitative lower bound on the negative entry or on its
split weight. The weighted four-cycle common-block regression remains applicable:
its cross transfer can be negative, zero, or positive as the four edge resistances
vary. Thus bridge-block topology alone cannot replace the missing strict-negative
response estimate.

The result is a new C-II branch theorem, not a Level I settlement.
