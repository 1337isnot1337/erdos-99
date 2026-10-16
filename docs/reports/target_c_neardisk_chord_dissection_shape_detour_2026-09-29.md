<!-- theorem-state: {"artifact_id":"ART-68135CFE7C0C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_neardisk_chord_dissection_shape_detour_2026-09-29.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=aa17984fda7e8a1fc5accf8744f0976fa68c98fb; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II — near-disk chord-dissection shape-detour theorem

**Date:** 2026-09-29  
**Base main:** 77d418e49da08328f126fcd5bbab21cccb15b639  
**Status:** proof-only current-main theorem; theorem-state authority unchanged  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Result

Work in the canonical full-core Type-II branch. Let

\[
P_r=\operatorname{conv}(A_r),\qquad
d_r=\operatorname{diam}(P_r),\qquad
p_r=\operatorname{per}(P_r)
\]

be the harmonic attachment cells. Then

\[
\boxed{\sum_r(p_r-2d_r)\ge(\pi-2-o(1))D.}
\tag{1.1}
\]

Since the occurrence-counted harmonic outer walk satisfies \(L_r\ge p_r\),

\[
\boxed{
S_{\rm out}:=\sum_r(L_r-2d_r)\ge(\pi-2-o(1))D.
}
\tag{1.2}
\]

Current main proves, with

\[
S_D:=\sum_rd_r,\qquad
X_D:=q-k-S_D,\qquad
Q_{\rm loc}:=\sum_rQ_r,
\]

the finite upper bound

\[
0\le S_{\rm out}\le2X_D+4c_I-4-Q_{\rm loc}.
\tag{1.3}
\]

Canonical component deatomization has \(c_I=o(D)\). Combining (1.2)--(1.3)
therefore gives

\[
\boxed{
\liminf_{D\to\infty}{q-k-\sum_rd_r\over D}
\ge{\pi\over2}-1
=0.5707963267\ldots .
}
\tag{1.4}
\]

This replaces the current-main convex-width value
\(0.0905130297\ldots\) by a geometric dissection constant more than six times
as large.

The load-bearing new theorem is not a scalar optimization. It says that an
asymptotically disk-filling family of noncrossing boundary-supported convex
cells must collectively pay essentially the disk perimeter-minus-diameter
amount \((\pi-2)D\) in the same cell-shape detour appearing inside the
aggregate outer-walk currency.

No numerical computation is used.

## 2. Exact circle model

### Lemma 2.1 — triangle detour on a circle

Let a nondegenerate triangle of circumradius \(R\) have perimeter \(p\),
diameter \(d\), and area \(A\). Then

\[
\boxed{p-2d\le {4A\over3R}.}
\tag{2.1}
\]

Equality holds for an equilateral triangle.

Let \(C\) be the largest angle and \(A_1,B_1\) the other two angles. The side
opposite \(C\) is \(d\). By the extended sine law, (2.1) is equivalent to

\[
\sin A_1+\sin B_1-\sin C
\le {4\over3}\sin A_1\sin B_1\sin C.
\tag{2.2}
\]

Put

\[
x={A_1+B_1\over2}={\pi-C\over2},
\qquad
y={A_1-B_1\over2}.
\]

Since \(C\) is largest,

\[
0<x\le{\pi\over3},
\qquad
|y|\le\min\{x,\pi-3x\}.
\tag{2.3}
\]

Product-to-sum identities reduce (2.2), by continuity at a degenerate
cancellation endpoint, to

\[
3\le4\cos x(\cos y+\cos x).
\tag{2.4}
\]

If \(x\le\pi/4\), then \(\cos y\ge\cos x\), so the right side is at least
\(8\cos^2x\ge4\).

If \(x\in[\pi/4,\pi/3]\), then
\(\cos y\ge\cos(\pi-3x)=-\cos3x\). Hence

\[
4\cos x(\cos y+\cos x)
\ge4\cos x(\cos x-\cos3x)
=4\sin^2(2x)
\ge3.
\]

Equality occurs at \(x=\pi/3,y=0\). This proves the lemma.

### Lemma 2.2 — cyclic polygon detour

Let \(Q\) be a convex polygon whose vertices lie on one circle of radius \(R\).
If \(p(Q),d(Q),A(Q)\) are its perimeter, diameter, and area, then

\[
\boxed{
0\le p(Q)-2d(Q)\le {4A(Q)\over3R}.
}
\tag{2.5}
\]

The lower bound is the two-boundary-arc inequality \(p(Q)\ge2d(Q)\).

Triangulate \(Q\), and let \(I\) be the total length of the triangulation
diagonals. For any diagonal \(e\), the child polygon supported on the minor
circle arc between its endpoints has diameter exactly \(|e|\); the other child
has diameter at most the diameter of its parent. Induction therefore gives

\[
\sum_Td(T)\le d(Q)+I.
\tag{2.6}
\]

Also

\[
\sum_Tp(T)=p(Q)+2I.
\]

Thus

\[
p(Q)-2d(Q)
\le\sum_T\bigl(p(T)-2d(T)\bigr).
\]

Apply Lemma 2.1 to every triangle and sum their areas. The coefficient \(4/3\)
is sharp by the equilateral triangle.

## 3. Annulus stability for a short polar arc

Let a convex body \(F\) satisfy

\[
B(0,r)\subset F\subset B(0,R),
\qquad 0<r\le R,
\tag{3.1}
\]

and put \(\lambda=R/r\). Write its boundary as the radial graph

\[
p(\phi)=\rho(\phi)e_\phi.
\]

The radial function is locally absolutely continuous. At almost every
differentiability point, with \(n\) the outward unit normal,

\[
n\cdot p=h_F(n)\ge r.
\]

For a polar graph,

\[
n\cdot e_\phi
={\rho\over\sqrt{\rho^2+(\rho')^2}}.
\]

Hence

\[
|\rho'|
\le
\rho\sqrt{\rho^2/r^2-1}
\le
M,
\qquad
M:=R\sqrt{\lambda^2-1}.
\tag{3.2}
\]

Consider boundary vertices \(x,y\) whose shorter polar angular separation is
\(\theta\le\pi\), and put \(e=|x-y|\). Every pair \(z,w\) on that shorter
boundary arc, with angular separation \(\phi\le\theta\), satisfies

\[
|z-w|
\le M\phi+2R\sin(\phi/2)
\le M\theta+2R\sin(\theta/2).
\tag{3.3}
\]

Meanwhile

\[
e\ge2r\sin(\theta/2).
\tag{3.4}
\]

Since

\[
{\theta\over2\sin(\theta/2)}\le{\pi\over2},
\]

we obtain

\[
\boxed{
\operatorname{diam}
\{\hbox{any boundary vertices on the short arc }xy\}
\le C(\lambda)|e|,
}
\tag{3.5}
\]

where

\[
\boxed{
C(\lambda)
:=
\lambda+{\pi\over2}\lambda\sqrt{\lambda^2-1}.
}
\tag{3.6}
\]

Thus \(C(\lambda)\to1\) as \(\lambda\downarrow1\).

## 4. Diameter telescoping in a chord dissection

Let \(F\) be a convex polygon and add a finite noncrossing family of diagonals.
The resulting bounded faces form a polygonal dissection. Let \(d_f\) be the
diameter of face \(f\), and let \(I\) be the total Euclidean length of the
distinct internal diagonals. Under (3.1),

\[
\boxed{
\sum_fd_f\le D+C(\lambda)I,
\qquad D:=\operatorname{diam}F.
}
\tag{4.1}
\]

Indeed, split a parent polygon by a diagonal \(e=xy\). The two child vertex
sets lie on the two corresponding cyclic boundary arcs of the original
\(F\). One child is supported on the shorter polar arc, so (3.5) bounds its
diameter by \(C(\lambda)|e|\). The other child diameter is at most the parent
diameter. Hence

\[
d_1+d_2\le d_{\rm parent}+C(\lambda)|e|.
\]

Induction through the noncrossing dissection proves (4.1).

Face-perimeter incidence gives

\[
\sum_fp_f=P_F+2I,
\tag{4.2}
\]

so

\[
\boxed{
\sum_f(p_f-2d_f)
\ge
P_F-2D-2(C(\lambda)-1)I.
}
\tag{4.3}
\]

## 5. The harmonic cells generate an O(D)-edge-length dissection

Return to the canonical Type-II harmonic cells. Section 83 proves that their
interiors are pairwise disjoint and their boundaries do not cross properly.
Form the straight-line graph consisting of the loaded force-hull boundary and
every distinct side of every attachment polygon.

Every graph vertex is a loaded extreme vertex of \(F\). No edge of another
cell can enter the interior of \(P_r\), because that would create either a
proper crossing or intersect cell interiors. Hence every \(P_r\) is a face of
this chord dissection. Call all remaining bounded faces gaps.

Let \(I_D\) be the total length of the distinct internal chord edges. Every
such edge belongs to the boundary of at least one attachment cell, so

\[
I_D\le\sum_rp_r.
\tag{5.1}
\]

Canonical Section 83 gives

\[
\sum_rp_r=O(D),
\tag{5.2}
\]

hence \(I_D=O(D)\).

The same incidence identity gives

\[
\sum_{G\ {\rm gap}}p(G)
=
P_F+2I_D-\sum_rp_r
=O(D),
\tag{5.3}
\]

and therefore, because \(p(G)\ge2d(G)\),

\[
\sum_{G\ {\rm gap}}d(G)=O(D).
\tag{5.4}
\]

Canonical full-core area tiling gives

\[
\boxed{
A_{\rm gap}
:=
\sum_{G\ {\rm gap}}\operatorname{area}(G)
=
\operatorname{area}(F)-\sum_r\operatorname{area}(P_r)
=o(D^2).
}
\tag{5.5}
\]

## 6. Complementary gaps have only o(D) total detour

Canonical Type-II near-disk convergence implies, after translation, that there
exist \(r_D,R_D\) such that

\[
B(0,r_D)\subset F_D\subset B(0,R_D),
\qquad
{r_D\over D},{R_D\over D}\to{1\over2},
\qquad
\lambda_D:={R_D\over r_D}\to1.
\tag{6.1}
\]

We prove

\[
\boxed{
\sum_{G\ {\rm gap}}\bigl(p(G)-2d(G)\bigr)=o(D).
}
\tag{6.2}
\]

### 6.1 Macroscopic gaps

Fix \(\delta>0\). By (5.4), the number of gaps with
\(d(G)\ge\delta D\) is \(O_\delta(1)\).

If their total detour were not \(o(D)\), after taking a subsequence one such
gap would have normalized detour bounded below. Scale by \(D\). Blaschke
compactness gives a Hausdorff-convergent subsequence.

Every gap vertex lies on \(\partial F_D\), and (6.1) puts every normalized
vertex asymptotically on the radius-\(1/2\) circle. But (5.5) implies that the
normalized area of every individual gap tends to zero. The limiting convex
body is therefore a nontrivial line segment.

Planar convex perimeter is continuous under Hausdorff convergence, including
degeneration to a segment, directly from Cauchy's width formula. The perimeter
of a segment is twice its length. Hence

\[
{p(G)-2d(G)\over D}\to0,
\]

a contradiction. Therefore, for every fixed \(\delta>0\),

\[
\sum_{\substack{G\ {\rm gap}\\d(G)\ge\delta D}}
(p(G)-2d(G))
=o_\delta(D).
\tag{6.3}
\]

### 6.2 Small gaps are cap type

Call a gap cap type if its radial directions are contained in a closed angular
interval of length at most \(\pi\).

If a vertex set is not cap type, the origin belongs to the convex hull of its
radial directions. By Caratheodory choose three such directions around the
origin. Their cyclic gaps are at most \(\pi\) and sum to \(2\pi\), so one is
at least \(2\pi/3\). The corresponding actual boundary vertices have distance
at least

\[
2r_D\sin(\pi/3)=\sqrt3\,r_D.
\tag{6.4}
\]

Thus every non-cap gap is macroscopic. For any fixed sufficiently small
\(\delta\), all large-\(D\) gaps with \(d(G)<\delta D\) are cap type.

### 6.3 Quantitative cap-gap detour

Let a cap gap \(G\) have minimal polar support interval of angular length
\(0<\theta\le\pi\), with endpoint vertices \(x,y\), and put \(e=|x-y|\).

The polygon boundary is the chord \(xy\) plus the chordal chain through the
remaining selected force-hull vertices in that angular interval. The chordal
chain is no longer than the corresponding force-hull boundary arc. Canonical
Section 88's polar-arc estimate gives

\[
\ell_{\rm arc}\le{R_D^2\over r_D}\theta.
\tag{6.5}
\]

Since \(d(G)\ge e\),

\[
p(G)-2d(G)\le \ell_{\rm arc}-e.
\tag{6.6}
\]

Also

\[
e\ge2r_D\sin(\theta/2).
\]

Hence

\[
p(G)-2d(G)
\le
\left({R_D^2\over r_D}-r_D\right)\theta
+r_D\left(\theta-2\sin{\theta\over2}\right).
\tag{6.7}
\]

For \(0\le\theta\le\pi\),

\[
\sin(\theta/2)\ge{\theta\over\pi},
\qquad
\theta-2\sin(\theta/2)\le{\theta^3\over24}.
\]

Using \(d(G)\ge e\ge2r_D\theta/\pi\), we get

\[
\boxed{
p(G)-2d(G)
\le
{\pi\over2}(\lambda_D^2-1)d(G)
+
{\pi^3\over192}{d(G)^3\over r_D^2}.
}
\tag{6.8}
\]

Sum (6.8) over cap gaps with \(d(G)<\delta D\). From (5.4),

\[
\sum_Gd(G)=O(D),
\]

and

\[
\sum_{d(G)<\delta D}d(G)^3
\le
\delta^2D^2\sum_Gd(G)
=O(\delta^2D^3).
\]

Since \(r_D/D\to1/2\) and \(\lambda_D\to1\),

\[
\limsup_{D\to\infty}
{1\over D}
\sum_{\substack{G\ {\rm gap}\\d(G)<\delta D}}
(p(G)-2d(G))
=O(\delta^2).
\tag{6.9}
\]

First let \(D\to\infty\), then let \(\delta\downarrow0\). Together with
(6.3), this proves (6.2).

## 7. Global cell-shape detour

Apply (4.3) to the complete cell-plus-gap chord dissection. Equations
(5.1)--(5.2), (6.1), and \(C(\lambda_D)\to1\) give

\[
2(C(\lambda_D)-1)I_D=o(D).
\]

Near-disk convergence gives \(P_F/D\to\pi\). Therefore

\[
\sum_{\rm all\ faces}(p_f-2d_f)
\ge(\pi-2-o(1))D.
\tag{7.1}
\]

Subtract the \(o(D)\) total gap detour from (6.2). The remaining faces are
exactly the harmonic cells, proving (1.1).

Every attachment vertex is on the outer face of its induced harmonic graph,
and the convex hull of that outer-walk image is \(P_r\). A closed polygonal
walk has length at least the perimeter of its convex hull. Hence \(L_r\ge p_r\)
and (1.2) follows.

Finally current main's aggregate outer-detour upper bound (1.3), together with
\(c_I=o(D)\) and \(Q_{\rm loc}\ge0\), gives

\[
(\pi-2-o(1))D\le2X_D+o(D).
\]

Thus

\[
\boxed{
\liminf {X_D\over D}
\ge{\pi-2\over2}
={\pi\over2}-1.
}
\]

This proves (1.4).

## 8. Immediate consequences

Since \(q-k\le q\le P_F=\pi D-o(D)\), (1.4) gives

\[
\boxed{
\limsup {1\over D}\sum_rd_r
\le
{\pi\over2}+1
=2.5707963267\ldots .
}
\tag{8.1}
\]

At the audited-working component-remainder scope, the exact identity

\[
G_D=m+2+X_D
\]

would similarly imply

\[
\liminf {G_D-m\over D}\ge{\pi\over2}-1.
\tag{8.2}
\]

Equation (1.4) is stronger than merely recovering the canonical
\((q-k)/D\ge\pi/2\) hull floor because it retains the full harmonic diameter
moment \(S_D\).

## 9. Remaining obstruction

This theorem does not by itself close full-core Type II. It changes the live
gap from

\[
q-k-\sum_rd_r\ge0.090513D-o(D)
\]

to

\[
\boxed{
q-k-\sum_rd_r
\ge
\left({\pi\over2}-1-o(1)\right)D.
}
\tag{9.1}
\]

A closing continuation can now target one of:

1. an upper bound on the same gap below \((\pi/2-1)D\);
2. exclusion of the one-cell/two-cell near-disk decompositions compatible with
   the new diameter-moment cap (8.1);
3. a source-preserving strict diameter decrease forced by the disk-scale cell
   shape detour;
4. coupling (9.1) to the actual Woodall diameter graph or train/interface
   ledgers strongly enough to force an exact unit equilateral triangle.

The macroscopic inactive-container branch remains separate.

## 10. Scope audit

- The only near-disk input is canonical C-FULLCORE-NEAR-DISK; no convergence
  rate is assumed.
- The O(D) internal-edge budget is canonical Section 83's total
  attachment-cell perimeter bound.
- Gap area o(D^2) is exactly canonical Section 83's area-tiling theorem.
- The proof does not identify local exceptional-face counts with global ones.
- Repeated outer-walk occurrences are retained when passing from cell perimeter
  to \(L_r\).
- Contact-isolated source points are untouched.
- No full-source extension of the Section-57 affine-kernel theorem is used.
- No rejected Reuleaux-cap, Euler-path, FB4, or Section-121 scaling inference
  is used.
- No computation or unexecuted verifier is load-bearing.
- The theorem-state manifest is unchanged.

**Disposition:** proof-only current-main theorem; C-II and Level I remain open.
