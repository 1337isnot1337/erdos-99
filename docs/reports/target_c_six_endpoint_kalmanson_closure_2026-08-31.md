<!-- theorem-state: {"artifact_id":"ART-7F924C4FF364","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: arbitrary six-endpoint matching closure

**Date:** 2026-08-31  
**Run type:** exact response inequality / C-I subcase  
**Target:** the six-endpoint three-diameter matching left by C30-C32  
**Depends on:** C11 force-hull response identity, C30 response-inertia budget, and
the circular-planar Kalmanson inequalities

## LEVEL I STATUS

**STILL OPEN.**

This addendum proves the missing response inequality for the entire strictly convex
six-endpoint matching, not only for a regular hexagon. It also closes the equality
branch for any positive circular-planar contact realization: equality would force a
six-terminal star response, whose vanishing order-two circular minors force a
degree-six contact separator. The theorem below still does not turn a semidefinite
response defect into a finite same-diameter release for a direction-dependent
maximal-support stress.

## 1. Statement

Let (p_0,ldots,p_5) be six distinct vertices in strict convex cyclic order, and
let

\[
H=\{03,14,25\},
\qquad B=\operatorname{diag}(\beta_0,\beta_1,\beta_2),
\qquad \beta_i>0.
\tag{C50.1}
\]

Put (q_i=e_i-e_{i+3}), let (Q=(q_0\ q_1\ q_2)), and write

\[
L_H=QBQ^{\mathsf T},
\qquad
U=Q^{\mathsf T}P.
\tag{C50.2}
\]

Here the (i)-th row of (U) is (u_i=p_i-p_{i+3}). Assume that (Lambda) is
the connected positive-contact Dirichlet response on these six boundary vertices,
that (R=\Lambda^+), and that the force-hull affine response identity holds after
translation of the coordinates:

\[
\Lambda P=L_HP,
\qquad \mathbf 1^{\mathsf T}P=0.
\tag{C50.3}
\]

Assume also that (W_{ij}=R_{ii}+R_{jj}-2R_{ij}) obeys the circular-planar
Kalmanson inequalities. Then, with

\[
K=Q^{\mathsf T}RQ,
\qquad
\rho=\sum_{i=0}^2\beta_iW_{i,i+3}-2,
\tag{C50.4}
\]

one has

\[
\boxed{\rho\le 1.}
\tag{C50.5}
\]

Consequently, for the signed stress matrix

\[
\Omega=L_C(\alpha)-L_H(\beta)
\tag{C50.6}
\]

of the selected positive contact support, the C30 Schur reduction gives

\[
\boxed{\Omega\succeq0.}
\tag{C50.7}
\]

This applies to every strictly convex six-endpoint matching in the C30 three-edge
forest phase. No regularity, central symmetry, equal angular spacing, or special
contact graph is assumed.

## 2. Circular-planar inequality used in the proof

For a cyclic quadruple (i<j<k<\ell), define

\[
\begin{aligned}
\mathcal K_1(i,j,k,\ell)
  &=W_{ik}+W_{j\ell}-W_{ij}-W_{k\ell},\\
\mathcal K_2(i,j,k,\ell)
  &=W_{ik}+W_{j\ell}-W_{i\ell}-W_{jk}.
\end{aligned}
\tag{C50.8}
\]

The effective-resistance matrix of a connected circular-planar positive network
satisfies (mathcal K_1,mathcal K_2\ge0). This is the necessary Kalmanson property
used already in the regular-hexagon audit; see Stefan Forcey, *Circular planar
electrical networks, Split systems, and Phylogenetic networks*, Theorem 4.2,
[arXiv:2108.00550](https://arxiv.org/abs/2108.00550).

The only particular consequence needed here is

\[
\boxed{
K_{02}-K_{12}
=-\frac12\left(
\mathcal K_2(0,1,2,5)+\mathcal K_1(2,3,4,5)
\right)\le0.}
\tag{C50.9}
\]

Indeed, (q_0-q_1) and (q_2) have zero coordinate sum, so the standard identity

\[
x^{\mathsf T}Ry=-\frac12x^{\mathsf T}Wy
\qquad(\mathbf1^{\mathsf T}x=\mathbf1^{\mathsf T}y=0)
\tag{C50.10}
\]

gives

\[
\begin{aligned}
-2(K_{02}-K_{12})
  &=(W_{02}+W_{15}-W_{05}-W_{12})\\
  &\quad +(W_{24}+W_{35}-W_{23}-W_{45}),
\end{aligned}
\]

which is exactly the right-hand side of (C50.9).

## 3. Alternating-sign geometry of the matching

The rows (u_i=p_i-p_{i+3}) have an alternating linear dependence. More precisely,
for a counterclockwise cyclic order, set

\[
s_0=\det(u_1,u_2),
\qquad
s_1=\det(u_2,u_0),
\qquad
s_2=\det(u_0,u_1).
\tag{C50.11}
\]

Then

\[
s_0u_0+s_1u_1+s_2u_2=0,
\qquad
s_0>0,quad s_1<0,quad s_2>0.
\tag{C50.12}
\]

To check the signs, for (i<j) the four vertices occurring in the two chords
(p_i p_{i+3}) and (p_jp_{j+3}) form a strict convex quadrilateral. Its two
diagonals have positive oriented cross product when both are oriented from the
later endpoint to the earlier endpoint, so

\[
\det(u_0,u_1)>0,
\qquad
\det(u_1,u_2)>0,
\qquad
\det(u_0,u_2)>0.
\tag{C50.13}
\]

The determinant formula for the null vector of a (3\times2) matrix now gives
(C50.12). Strict convexity is used only to make these determinants nonzero.

## 4. Proof of the response inequality

From (C50.3), (R\Lambda) is the identity on centered boundary data. Therefore

\[
KBU
 =Q^{\mathsf T}RQBQ^{\mathsf T}P
 =Q^{\mathsf T}P
 =U.
\tag{C50.14}
\]

Let

\[
A=B^{1/2}U,
\qquad
T=B^{1/2}KB^{1/2}.
\tag{C50.15}
\]

The matrix (T) is symmetric and positive semidefinite, and (C50.14) says

\[
TA=A.
\tag{C50.16}
\]

Because the six boundary vertices are not collinear, (A) has rank two. Thus the
two-dimensional column space of (A) is a (1)-eigenspace of (T), and the only
remaining eigenvalue is

\[
\lambda=\operatorname{tr}T-2
 =\operatorname{tr}(KB)-2
 =\sum_{i=0}^2\beta_iW_{i,i+3}-2
 =\rho.
\tag{C50.17}
\]

The sign vector in (C50.12) gives a normal to (A):

\[
n=B^{-1/2}s,
\qquad n^{\mathsf T}A=s^{\mathsf T}U=0.
\tag{C50.18}
\]

Since (T) is symmetric and fixes (A), its spectral decomposition is

\[
T=I+(\rho-1)\frac{nn^{\mathsf T}}{n^{\mathsf T}n}.
\tag{C50.19}
\]

If `rho>1`, (C50.19) implies

\[
K=B^{-1}+c\,(B^{-1}s)(B^{-1}s)^{\mathsf T},
\qquad
c=\frac{\rho-1}{s^{\mathsf T}B^{-1}s}>0.
\tag{C50.20}
\]

The diagonal matrix (B^{-1}) has zero off-diagonal entries. Since
(s_0s_2>0) and (s_1s_2<0), (C50.20) gives

\[
K_{02}>0,
\qquad
K_{12}<0,
\qquad
K_{02}-K_{12}>0,
\tag{C50.21}
\]

contradicting the circular-planar inequality (C50.9). Hence `rho<=1`, proving
(C50.5). The semidefinite conclusion (C50.7) is exactly the C30 three-edge-forest
response-inertia alternative. \(square)

## 5. Equality boundary and exact implication

The proof also isolates the equality mode without overclaiming it. If `rho=1`,
then (C50.19) gives

\[
T=I,
\qquad K=B^{-1},
\qquad
W_{03}=\beta_0^{-1},\quad
W_{14}=\beta_1^{-1},\quad
W_{25}=\beta_2^{-1},
\tag{C50.22}
\]

and the two Kalmanson expressions in (C50.9) vanish. This is the exact extra scalar
kernel branch in C30. It is not removed by circular planarity or connectedness alone:
the six-terminal star response with terminal conductances (2\beta_i) on both
members of pair (i) realizes (C50.22), as in the regular-hexagon audit.

Therefore the theorem has the following precise C-I effect:

\[
\text{arbitrary six-endpoint matching}
\Longrightarrow
\text{no negative response mode};
\]

the remaining work is to rule out, classify geometrically, or integrate the equality
case for the actual triangle-free unit-contact source and the direction-dependent
KKT support. The theorem does not assert that every selected stress has the maximal
support, and it does not infer a finite release from semidefiniteness alone.

## 6. Equality classification from the Kalmanson split cone

The equality branch admits one additional exact response-level description. The
Kalmanson cone decomposition says that every Kalmanson matrix is a sum matrix plus a
nonnegative linear combination of interval cut matrices. This is Proposition 3.1 of
Polyakovskiy--Spieksma--Woeginger, *The three-dimensional matching problem in
Kalmanson matrices*,
[published open-access PDF](https://digital.library.adelaide.edu.au/server/api/core/bitstreams/9cc0da56-2dfb-4a98-bf0a-40f81869cbd2/content).

For an interval (A), put (z_A=Q^{\mathsf T}\mathbf1_A). A cut matrix contributes
(z_Az_A^{\mathsf T}) to (K=Q^{\mathsf T}RQ), while a sum matrix contributes zero.
After identifying (z) and (-z), the non-singleton interval vectors for six
cyclically ordered terminals are exactly

\[
 (1,1,0),\ (0,1,1),\ (1,0,-1),\
 (1,1,1),\ (1,-1,-1),\ (1,1,-1).
\tag{C50.23}
\]

Let their aggregate nonnegative coefficients be (a,b,c,d,e,f), in the displayed
order. If `rho=1`, then `K=B^{-1}`, so its three off-diagonal entries vanish.
The off-diagonal equations are

\[
 a+d-e+f=0,
\qquad
 -c+d-e-f=0,
\qquad
 b+d+e-f=0.
\tag{C50.24}
\]

The middle equation gives (d=c+e+f). Substitution into the first gives
(a+c+2f=0), so (a=c=f=0). The third then gives (b+2e=0), so
(b=d=e=0) as well. Thus only singleton interval cuts remain. Since the diagonal of
(W) is zero, the sum-matrix part vanishes on the diagonal and hence is identically
zero. Therefore there are numbers (r_0,ldots,r_5\ge0) such that

\[
\boxed{W_{ij}=r_i+r_j\quad(i\ne j).}
\tag{C50.25}
\]

In other words, equality forces the six-terminal response to be electrically
equivalent to a weighted star (with zero-length arms allowed as contracted limits),
not merely to have (K=B^{-1}). This is a boundary-response statement; it does not
assert that the original positive unit-contact graph is literally a star.

Strict convexity and the affine identity rule out a zero star arm: if \(r_i=0\),
the contracted hub is \(p_i\), while the two matching chords not incident to \(p_i\)
would both have to contain \(p_i\), impossible for a strict convex vertex. Thus all
star arms are nonzero. The star hub potential for the affine boundary data is
\(h=(\sum_j r_j^{-1}p_j)/(\sum_jr_j^{-1})\). The identity
\(\Lambda P=L_HP\) then forces

\[
h\in p_i p_{i+3}\quad(i=0,1,2),
\tag{C50.26}
\]

so the three diameter chord lines are concurrent at the electrical hub. This
concurrency still does not by itself produce a source vertex at \(h\), a unit
equilateral triangle, or a finite same-diameter release; those are the remaining
source-specific equality questions.

### Corollary C50.1 (the acyclic equality branch is triangle-forbidden)

Assume in addition that the positive contact graph carrying the response is a tree,
that the six terminals in (C50.1) are the only vertices with positive diameter
reaction, and that every contact edge has positive finite conductance. Then the
equality case \(\rho=1\) is impossible in a triangle-free unit-separated source.

Indeed, in a tree the effective resistance between two terminals is the sum of the
edge resistances on their unique path. By (C50.25), the resulting weighted tree
metric on the six terminals is \(r_i+r_j\). The minimal subtree connecting the
terminals therefore has one common branch vertex: if an edge of that subtree had
at least two terminals on each side, the two corresponding cross-pair sums would
differ by twice the positive length of the edge, contradicting the star metric.
After suppressing degree-two vertices, this is a six-arm star. Thus some original
contact vertex has at least six incident terminal paths.

The central branch vertex has at least six incident terminal paths (additional
terminal-free branches are irrelevant), so its contact degree is at least six.

Finally, a triangle-free unit-contact vertex has contact degree at most five. List its
incident unit directions cyclically. If a consecutive gap exceeded \(\pi\), one of the
other five gaps would be less than \(\pi/3\), contradicting unit separation. Thus all
gaps are at most \(\pi\), and unit separation makes each gap at least \(\pi/3\).
Equality would make the two neighboring contacts and the central vertex a unit
equilateral triangle. Triangle-freeness therefore makes all gaps strictly larger
than \(\pi/3\), which is impossible for six gaps summing to \(2\pi\).
This contradiction proves the corollary. \square

### Corollary C50.2 (all six-terminal equality realizations are triangle-forbidden)

The tree hypothesis in Corollary C50.1 is unnecessary. In the equality case of
Theorem C50, the positive circular-planar contact network itself cannot be a
triangle-free unit-contact graph.

We use the following elementary terminal-separator lemma.

**Lemma.** Let \(G\) be a finite connected graph and let \(A\subseteq V(G)\) have
\(|A|\ge4\). If \(G\) has no two vertex-disjoint \(A\)-paths (paths with distinct
ends in \(A\) and no internal vertex in \(A\)), then there is a vertex \(v\) such
that every component of \(G-v\) contains at most one vertex of \(A\).

**Proof.** Form the block-cut tree of \(G\), and attach a marked leaf for every
terminal (attach it to the terminal vertex when that vertex is a cut vertex, and
to its containing block otherwise). Restrict to the minimal subtree containing all
marked leaves. If an edge of this tree has at least two marked leaves on each
side, its corresponding cut vertex can be deleted; the two resulting sides each
contain two terminals and therefore supply disjoint \(A\)-paths, a contradiction.

Thus no edge has two marked leaves on both sides. The elementary center lemma for
trees then gives a node \(x\) whose incident branches each contain exactly one
marked leaf. If \(x\) is a cut-vertex node, that vertex is the required \(v\). If
\(x\) is a block node, it has at least four distinct terminal/branch attachment
vertices. A 2-connected block has two vertex-disjoint paths joining two pairs of
any four distinct vertices: apply Menger to the two sets of two vertices. Extending
these paths through their four disjoint branches, and trimming at consecutive
terminals if needed, gives two disjoint (A)-paths, again a contradiction. A bridge
block cannot be the latter center because it has only two attachment vertices. \(\square\)

Now assume equality and let \(G\) be the positive contact graph carrying the
response. By (C50.25), \(W_{ij}=r_i+r_j\) with all \(r_i>0\). The response matrix is
therefore the response of the six-arm star: for \(i\ne j\),

\[
\Lambda_{ij}=-\frac{g_i g_j}{\sum_k g_k},
\qquad g_i=r_i^{-1}.
\tag{C50.27}
\]

Every circular minor of order two is zero. The circular-planar response
characterization says that a circular minor is positive exactly when the associated
circular pair has a vertex-disjoint connection (Alman--Lian--Tran,
Theorem 2.2.6(b), [open PDF](https://joshalman.com/AlmanLianTran.pdf)). Hence \(G\)
has no two disjoint \(A\)-paths, where \(A\) is the six-terminal boundary set: any two disjoint
embedded terminal paths have a noncrossing endpoint pairing and hence form a
circular pair of size two. The lemma supplies a vertex \(v\) whose deletion leaves
at most one terminal in each component.

The separator cannot itself be a terminal. If \(v=i\in A\), choose two other
terminals \(j,k\) in distinct components of \(G-v\). The cut-vertex resistance
identity gives

\[
W_{jk}=W_{ji}+W_{ik}=(r_j+r_i)+(r_i+r_k),
\]

whereas the star metric gives \(W_{jk}=r_j+r_k\); this forces \(r_i=0\), a
contradiction. Therefore \(v\notin A\). The six terminal components of \(G-v\) are
distinct, and each has an edge to \(v\), so

\[
\deg_G(v)\ge6.
\tag{C50.28}
\]

All edges of \(G\) are unit contacts. The cyclic-neighbor argument in Corollary
C50.1 shows that a triangle-free unit-contact vertex has degree at most five.
Thus (C50.28) contradicts triangle-freeness. This proves the corollary. \(\square\)

## 7. Audit and regression check

| Claim | Classification | Audit |
| --- | --- | --- |
| Alternating-sign dependence (C50.12) | proved | Convex-quadrilateral diagonal orientation and the determinant null-vector formula. |
| Kalmanson contrast inequality (C50.9) | proved | Exact expansion into two nonnegative cyclic Kalmanson expressions. |
| `rho<=1` for the six-endpoint matching | proved | Spectral rank-two reduction plus the sign contradiction. |
| Omega>=0 in this selected three-edge phase | proved | C30 Schur congruence and (C50.5). |
| Strict `rho<1` in every triangle-free six-terminal realization | proved | Equality gives a star response, zero order-two circular minors, and then a degree-six terminal separator. |
| Acyclic equality branch is impossible in the triangle-free unit graph | proved | Star resistance metric forces degree six, while triangle-free unit-contact degree is at most five. |
| All six-terminal circular-planar equality realizations are impossible in the triangle-free unit graph | proved | The terminal-separator lemma removes the tree hypothesis from C50.1. |
| C-I globally closed | not proved | Support selection and the equality integration step remain. |

The C33 abstract sign-cone regression is not a counterexample: it violates the
circular-planar Kalmanson constraint used in (C50.9). The regular-hexagon C35 audit
is recovered as a special case, while no lattice, density, or global-optimality
assumption has been smuggled into the response proof.

## 8. Handoff

The former six-endpoint response question is now settled strictly for a triangle-free
unit-contact realization:

\[
\boxed{
H=\{03,14,25\},
\text{strict convex cyclic endpoints},
\Lambda P=L_HP,
\text{circular-planar response from a triangle-free unit graph}
\Longrightarrow
\sum_i\beta_iR_{\rm eff}(i,i+3)<3.}
\]

The six-endpoint equality theorem is now source-closed: a circular-planar realization
of (C50.22) would have a terminal separator of degree at least six, while a
triangle-free unit-contact graph has degree at most five. This removes the selected
three-edge matching equality loophole, but it does not supply maximal KKT support or
close C-I. Until those global steps are proved, Target C and Erdős Problem #99 remain
open.
