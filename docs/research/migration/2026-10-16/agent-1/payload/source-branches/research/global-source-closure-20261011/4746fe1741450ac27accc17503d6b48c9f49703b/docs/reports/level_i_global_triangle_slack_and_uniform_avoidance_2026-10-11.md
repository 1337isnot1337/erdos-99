<!-- theorem-state: {"artifact_id":"ART-92863FDB258E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Level I — global triangle slack and uniform triangle avoidance

**Date:** 2026-10-11  
**Base commit:** `ab6dd333`  
**State version:** `2026-10-10.audit.234`  
**Run type:** independent global closing-proof research  
**Target:** Level I, outside the route-specific A/B/C reductions  
**Classification:** proved candidate awaiting promotion; report remains unreviewed  
**Level I:** OPEN

The problem statement in `docs/problem/statement.md` supplies the definitions and
quantifiers. The new argument below uses elementary planar geometry only. It does
not import another worker's solution or depend on an unpromoted research report.
The no-positive-gap phenomenon was already recorded in Section 9.1 of the Das
literature audit. The source-uniform quantitative bound and complete short-triple
avoidance argument below strengthen that observation; they do not settle Level I.

## 1. An exact global quantity

For a unit-separated labelled configuration P with n>=3, define

\[
 T(P)=\min_{i<j<k}
 \bigl(|p_i-p_j|^2+|p_i-p_k|^2+|p_j-p_k|^2-3\bigr).
\]

Every summand is nonnegative. Thus T(P)>0 if and only if P contains no unit
equilateral triangle. This includes every label, including contact isolates.

Let \(\mathcal P_n(R)\) be the set of labelled configurations with minimum
separation exactly one, p_1=0, and diameter at most R. When R>=D(n), this set
is nonempty and compact: every label lies in the closed radius-R disk, all pair
inequalities are closed, and the minimum-pair-distance equality is closed.
Define the attained maximum

\[
 \Gamma_n(R)=\max_{P\in\mathcal P_n(R)}T(P).
\]

The exact Level I endpoint is

\[
 \exists n_0\ \forall n\ge n_0:\quad \Gamma_n(D(n))=0.
\tag{1}
\]

Indeed all members of \(\mathcal P_n(D(n))\) are global minimizers. The maximum
is zero precisely when every one of them has a unit triangle. A disproof requires
\(\Gamma_n(D(n))>0\) for an unbounded sequence of n. No local source extraction,
representative choice, or stress normalization is built into this formulation.

Candidate chain for a closing result:

```text
an eventual zero theorem for the global maximum Gamma_n(D(n))
  -> every optimal full source has zero triangle slack
  -> every sufficiently large global minimizer has a unit triangle.
```

The theorem below concerns R>D(n), so it is an obstruction to an approximate
version of that chain, not its missing endpoint proof.

## 2. Source-uniform normalized avoidance

**Candidate theorem.** Let P be any n-point planar configuration, n>=3, with
minimum separation exactly one and diameter D. Write M=binom(n,3). For every
0<t<=1/32 there is s in [t/2,t] for which the following full-source placement
has minimum separation exactly one:

\[
 q_i=\frac{(x_i,\sqrt{1+s}\,y_i)}{m_s},\qquad
 m_s^2=\min_{i<j}\bigl((x_i-x_j)^2+(1+s)(y_i-y_j)^2\bigr).
\]

It satisfies

\[
 \operatorname{diam}Q\le\sqrt{1+t}\,D,
 \qquad T(Q)\ge\frac{t}{16M}>0.
\tag{2}
\]

No inactive-pair gap, prescribed orientation, contact graph, or global optimality
hypothesis is required. All labels are retained, and all lower and upper pairs
are controlled. The normalization is essential: simply dilating a minimizer
and then restoring its minimum separation would restore its unit triangles.

### Proof

For an edge e put

\[
 a_e=|p_i-p_j|^2,\qquad b_e=(y_i-y_j)^2,
 \qquad d_e(s)=a_e+s b_e.
\]

Since a_e>=1, 0<=b_e<=a_e, and some a_e=1,

\[
 1\le m_s^2\le1+s\le1+t.
\tag{3}
\]

Every normalized squared distance is d_e(s)/m_s^2>=1. Also d_e(s)<=
(1+t)a_e, which proves the diameter bound.

Call a triple short if all three a_e<=9/8. For a short triple, its area A
satisfies A>=sqrt(3)/4. In squared-side variables a,b,c in [1,9/8], Heron's
formula gives

\[
 16A^2=2(ab+ac+bc)-a^2-b^2-c^2.
\]

Each partial derivative is positive on this box, since b+c-a>=7/8. Its
minimum is therefore at a=b=c=1, giving 16A^2>=3. In particular the triangle
is nondegenerate.

Let h be the triple's vertical extent and L its longest side. Its horizontal
extent is at most L, and a triangle in its coordinate bounding rectangle has
area at most half the rectangle area. Thus h>=2A/L>=sqrt(2/3).
The three vertical differences have absolute values h,u,h-u for some 0<=u<=h.
Their squares have range at least 3h^2/4>=1/2. Consequently two edges e,f
of this triple satisfy

\[
 |b_e-b_f|\ge1/2.
\tag{4}
\]

For each short triple select one such edge pair and put
\(\ell(s)=a_e-a_f+s(b_e-b_f)\). Set tau=t/(16M). The set

\[
 \{s:|\ell(s)|<(1+t)\tau\}
\]

is an open interval of length at most 4(1+t)tau. The union over all short
triples has total length at most

\[
 4(1+t)M\tau=(1+t)t/4\le33t/128<t/2.
\]

It cannot cover [t/2,t]. Choose s in the complement. For every short triple,
its normalized triangle slack is at least its largest-minus-smallest squared
edge length, hence at least

\[
 |\ell(s)|/m_s^2\ge\tau.
\]

For a triple that is not short, some original squared edge exceeds 9/8.
Its normalized squared length exceeds

\[
 \frac{9}{8(1+t)}\ge\frac{12}{11}.
\]

The other two normalized lengths are at least one, so this triple has slack
greater than 1/11>tau. This proves (2). In particular all newly possible
unit triangles are excluded, rather than only breaking the old unit triangles.

## 3. Consequences for the global endpoint

For any R>D(n), set

\[
 t=\min\left\{\frac1{32},\frac{R^2/D(n)^2-1}{2}\right\}>0.
\]

Apply (2) to a global minimizer. Its transformed diameter is strictly below R,
and

\[
 \Gamma_n(R)\ge\frac{t}{16\binom n3}>0.
\tag{5}
\]

In particular the infimum diameter among minimum-separation-one triangle-free
n-point configurations is exactly D(n), for every n>=3. This infimum is attained
if and only if \(\Gamma_n(D(n))>0\). When the conjecture holds, the infimum is
not attained. There is no possible strict comparison between these two infimum
values, even for a single cardinality where every global minimizer has a triangle.

One further elementary compactness fact is useful. Gamma_n is nondecreasing and
right-continuous on [D(n),infinity). To check the endpoint, take R_j decreasing
to R and maximizers P_j. Compactness gives a convergent subsequence with limit
in \(\mathcal P_n(R)\). Continuity of T shows that the limiting Gamma value
is at most Gamma_n(R); monotonicity gives the reverse inequality. The same
argument works at every R>=D(n).

Thus (5) does not force Gamma_n(D(n))>0. Its lower bound tends to zero as
R decreases to D(n). Conversely, convergence to the optimal diameter never
forces triangle-free approximants to attain it.

## 4. Exact verification and limits

The companion script
`research/verify_level_i_uniform_triangle_avoidance_2026_10_11.py` implements
interval avoidance and all-pair/all-triple verification with exact rational
squared distances. Its fixtures include triangular-lattice patches, rational
rotations of a square patch, a collinear packing, and a normalized triangle that
becomes exactly equilateral at a naive anisotropic parameter inside [t/2,t].
The latter checks the new-triangle failure that continuity-only arguments can
miss. It also checks the positive normalization margin and the interval-length
budget. These finite checks do not certify fixture optimality or prove (1).

**Exact remaining obligation:** establish (1), or construct and certify actual
triangle-free global minimizers for unbounded n. Neither positivity immediately
above D(n), a dense packing construction, nor a limiting triangle-free sequence
settles that obligation. No theorem-state promotion or Level I closure is claimed.
