> Generated reading edition · [exact source](../../../docs/reports/target_c_sharp_annular_source_terminal_2026-09-11.md) · source SHA-256 `25589dcbbe0b70d71a9279fa16f23a5a83632fa03acff3be6091416626f56dc8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-12EB94ED8ED4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp annular source and loaded-terminal ledger

**Date:** 2026-09-11

**Target:** Target C, C-II

**Status:** new proved report; unpromoted

**Dependencies:** the C-I representative, the force-hull notation, the strict translated-lattice comparison, and the finite simplicial-packing inequality of Graham–Witsenhausen–Zassenhaus, Theorem 4

## Statement

Let (A) be the contact-minimal, diameter-pair-minimal C-II representative, let

$$
K=\operatorname{conv}A,
\qquad F=\operatorname{conv}B,
\qquad q=|B|,
$$

where (B) is the loaded force-hull vertex set. Put

$$
Z=|A\setminus F|,
\qquad N=|A\cap F|,
\qquad a_0=\frac{\sqrt3}{2},
\qquad c_0=\frac{\sqrt3}{4}.
$$

When $F$ has nonempty interior, then

$$
\boxed{
a_0(Z+q)\le \operatorname{area}K-\operatorname{area}F
 +c_0(\operatorname{per}K+\operatorname{per}F)+a_0.}
\tag{SA.1}
$$

The additive $a_0$ is unnecessary when $F\subset\operatorname{int}K$.
If $F$ is degenerate, $\operatorname{area}F=0$, so the quadratic population
consequence below makes no assertion about that branch.

Combining (SA.1) with the strict global comparison

$$
a_0|A|>\frac{\pi D^2}{4}+a_0
\tag{SA.2}
$$

gives the source-level inequality

$$
\boxed{
a_0(N-q)>\operatorname{area}F+\delta_K
 -c_0(\operatorname{per}K+\operatorname{per}F),}
\tag{SA.3}
$$

where

$$
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K\ge0.
$$

Combining (SA.3) with Oler's inequality on (A\cap F) gives the following
correct equivalent consequence:

$$
\boxed{
\delta_K+a_0q<c_0(\operatorname{per}K+2\operatorname{per}F)+a_0.}
\tag{SA.4}
$$

If the full-source cell-slack theorem is also used, its exact rhombic-area
consequence sharpens (SA.4) to

$$
\boxed{
E+\delta_K+a_0q<c_0(\operatorname{per}K+2\operatorname{per}F)+a_0.}
\tag{SA.5}
$$

The useful population consequence is that (A\cap F\) contains a quadratic
population after the (O(D)) loaded boundary is removed whenever (F) has quadratic
area. This statement includes contact-isolated points and makes no hull-saturation
choice.

## Proof

Assume first that $F$ has nonempty interior. Consider the closed region

$$
U=K\setminus\operatorname{int}F.
$$

Its selected vertices are the points of $A\setminus F$, together with the $q$
loaded vertices of $F$. A source point lying on a common boundary is assigned to
$F$, so it is not counted twice. The extreme vertices of $K$ and $F$ are among
these selected vertices because they are vertices of the corresponding source or
force hull.

Triangulate the polygonal annulus bounded by $\partial K$ and $\partial F$,
using only its boundary vertices. Insert each remaining selected point of
$A\setminus F$ into the face that contains it, subdividing that face by straight
segments to its three vertices. This gives a finite straight plane simplicial
complex with support $U$ and with exactly the selected vertices (up to deleting
unused boundary vertices). If a selected point lies on an edge, subdivide that edge
and the incident face(s) instead. Every resulting edge joins two points of $A$,
so it has Euclidean length at least one. No artificial vertex is introduced; this
matters because the GWZ packing condition is imposed on vertices joined by edges.

The finite simplicial-packing inequality of Graham–Witsenhausen–Zassenhaus gives, in
the Euclidean norm,

$$
a_0|V(S)|\le \operatorname{area}(U)+c_0\operatorname{per}(U)+a_0\chi(U).
\tag{SA.GWZ}
$$

The selected vertices are a subset of V(S), and deleting unused triangulation
vertices only weakens the left side. The region (U) has at most one hole, so
$\chi(U)\le1$. Its geometric boundary is contained in the two hull boundaries,
with shared portions canceling, so

$$
\operatorname{area}(U)=\operatorname{area}K-\operatorname{area}F,
\qquad
\operatorname{per}(U)\le\operatorname{per}K+\operatorname{per}F.
$$

Substitution into (SA.GWZ) proves (SA.1). If $F$ is strictly inside $K$, $U$ is
a genuine annulus and $\chi(U)=0$, proving the stated improvement.

If $F$ is degenerate, its area is zero and the quadratic consequence below is
vacuous. If $F=K$ with nonempty interior, (SA.1) follows instead from Oler's
inequality on $F$ and $q\le\operatorname{per}F$, using $a_0=2c_0$. Thus the
full-dimensional zero-width case is also covered.

Now write $N+Z=|A|$. Subtract (SA.1) from (SA.2):

$$
\begin{aligned}
a_0(N-q)
&=a_0|A|-a_0(Z+q)\\
&>\frac{\pi D^2}{4}+a_0
 -\bigl(\operatorname{area}K-\operatorname{area}F
 +c_0(\operatorname{per}K+\operatorname{per}F)+a_0\bigr)\\
&=\operatorname{area}F+\delta_K
 -c_0(\operatorname{per}K+\operatorname{per}F).
\end{aligned}
$$

This is (SA.3).

Oler's finite inequality applied to the unit-separated subset $A\cap F\subset F$
gives

$$
a_0N\le\operatorname{area}F+c_0\operatorname{per}F+a_0.
\tag{SA.Oler}
$$

Combining (SA.3) with (SA.Oler) gives (SA.4) after substituting
$\operatorname{area}K=\pi D^2/4-\delta_K$.

For (SA.5), use the already audited full-source cell-slack consequence

$$
E+\delta_F<a_0Z+c_0\operatorname{per}F,
\qquad
\delta_F=\frac{\pi D^2}{4}-\operatorname{area}F.
\tag{SA.FS}
$$

The annular inequality gives

$$
a_0Z\le \delta_F-\delta_K+c_0(\operatorname{per}K+\operatorname{per}F)+a_0-a_0q.
$$

Substitution into (SA.FS), followed by cancellation of $\delta_F$, is exactly
(SA.5). This use of (SA.FS) is valid with arbitrary isolates because the full-source
cell-slack theorem counts them in its cell populations.
$\square$

## Exact new consequence

Suppose along a C-II sequence

$$
\frac{\operatorname{area}F}{D^2}\to a>0,
\qquad
\operatorname{per}K,\operatorname{per}F=O(D).
$$

Then (SA.3) gives

$$
N-q\ge \frac{a}{a_0}D^2-O(D).
\tag{SA.7}
$$

Thus a quadratic force hull cannot be populated only by its loaded boundary. The
remaining quadratic population consists of unloaded contact-core vertices and/or
contact-isolated source points. The estimate is source-specific, not a scaffold
count.

The same conclusion holds in the cyclic and forest diameter-topology branches and
when (s_Z>0), because no circuit identity was used.

If the report-level C67 force-hull floor is added as a hypothesis,
$$
\liminf\frac{\operatorname{area}F}{D^2}\ge
A_{\rm FS}:=\frac{2\rho+\sin(2\rho)}4
=0.6184708847\ldots,
\qquad \rho=\cos\rho,
$$
then (SA.7) specializes to
$$
\boxed{
N-q\ge
\frac{A_{\rm FS}}{a_0}D^2-O(D)
=0.7141486636\ldots D^2-O(D).
}
\tag{SA.8}
$$
This numerical specialization is conditional on C67 because that area floor is
not a promoted theorem module. The unconditional statement is (SA.7).

## Closure test

The new term a_0 q is exactly canceled by the sharp c_0 per(F) boundary credit
when one uses only q ≤ per(F), since a_0 = 2c_0. Therefore (SA.5) cannot by
itself contradict any of the three C-II
branches. It proves the scale of the inactive population but does not turn that
population into positive KKT contacts or a smaller-diameter competitor.

The remaining implication needed for Level I is still one of:

1. force-hull Oler saturation plus a quadratic inactive population implies a unit
   equilateral triangle;
2. the quadratic inactive population can be replaced by the same number of points in
   a container of diameter less than D; or
3. the contact/response ledgers provide a strict finite motion that reaches those
   source points without losing the global diameter certificate.

None of these implications follows from (SA.1)--(SA.7).

## Provenance and status

The only external input in this report is the finite simplicial-packing inequality
of R. L. Graham, H. S. Witsenhausen, and H. J. Zassenhaus, *On Tightest Packings in
the Minkowski Plane*, Pacific Journal of Mathematics 41 (1972), Theorem 4,
pp. 710--711. The primary-source PDF is
<https://msp.org/pjm/1972/41-3/pjm-v41-n3-p10-p.pdf>.

This is a report-level theorem. It does not alter the authoritative Target C route
map, whose C-II status remains open.
