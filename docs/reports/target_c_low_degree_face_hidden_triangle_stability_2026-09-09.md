<!-- migration-source: path=docs/reports/target_c_low_degree_face_hidden_triangle_stability_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e01c372ff95d19fba9ffb8de7a03b489bcbb835e; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — low-degree defect faces: cheap area forces a hidden near-triangle

**Date:** 2026-09-09  
**Repository base:** PR #119 after UF/CV  
**Run type:** finite packing equality/stability  
**Target:** pentagon/hexagon regression in the near-circle face-defect branch  
**External theorem:** G. Wegner's finite congruent-disk inequality, with equality iff the packing is a Wegner packing; checked through K. J. Böröczky and I. Z. Ruzsa, *Note on an Inequality of Wegner*, Discrete Comput. Geom. 37 (2007), 245–249, DOI 10.1007/s00454-006-1277-4  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The DP regression shows that strict convex unit pentagons can have Oler area slack tending to zero. Its explicit family degenerates to a triangular-lattice cluster and creates hidden unit diagonals in the limit.

This report proves that this feature is not an artifact of DP's coordinates. For both five- and six-sided convex equilateral unit-separated faces, asymptotic equality in the Oler face bound forces convergence to a finite triangular/Groemer packing. In particular, some nonboundary pair has distance tending to one.

Thus the low-degree cheap-face obstruction has the exact form

```text
small Oler face slack
    -> hidden nonedge distance 1+o(1)
    -> limiting unit triangle / Groemer cell.
```

The theorem is finite and quantitative by compactness: for every fixed separation margin `eta>0`, there is a positive face-area gap.

---

## 1. Scaled Wegner inequality

Wegner's theorem states that if `N` nonoverlapping unit-radius disks have convex-hull region `D_N`, then

\[
\operatorname{area}(D_N)
\ge
2\sqrt3(N-1)
+(2-\sqrt3)
\left\lceil\sqrt{12N-3}-3\right\rceil
+\pi,
\tag{1.1}
\]

with equality if and only if the packing is a Wegner packing. A Wegner packing is Groemer: its centers can be triangulated into equilateral triangles of side two.

Scale by `1/2`. For `N` unit-separated centers with convex hull `K`, the radius-`1/2` disks are nonoverlapping and their convex hull is

\[
K+\frac12\mathbb B.
\]

Steiner's formula gives

\[
\operatorname{area}\left(K+\frac12\mathbb B\right)
=
\operatorname{area}(K)+\frac12\operatorname{per}(K)+\frac\pi4.
\tag{1.2}
\]

Therefore the scaled Wegner theorem is

\[
\boxed{
\operatorname{area}(K)+\frac12\operatorname{per}(K)
\ge
\frac{\sqrt3}{2}(N-1)
+\frac{2-\sqrt3}{4}
W_N,
}
\tag{1.3}
\]

where

\[
W_N:=\left\lceil\sqrt{12N-3}-3\right\rceil.
\tag{1.4}
\]

Equality holds exactly when the unit-separated center set is the `1/2`-scaled center set of a Wegner packing, hence a Groemer packing triangulatable by unit equilateral triangles.

---

## 2. For `N=5,6`, Wegner equals the Oler face bound exactly

For `N=5`,

\[
W_5=5.
\]

If `K` is an equilateral convex pentagon, `per(K)=5`, so (1.3) gives

\[
\operatorname{area}(K)
\ge
4\frac{\sqrt3}{2}
+5\frac{2-\sqrt3}{4}
-\frac52
=
\boxed{\frac{3\sqrt3}{4}}.
\tag{2.1}
\]

This is exactly Oler's face lower bound

\[
c_0(5-2)=3\sqrt3/4.
\]

For `N=6`,

\[
W_6=6.
\]

An equilateral convex hexagon has perimeter six, and (1.3) gives

\[
\operatorname{area}(K)
\ge
5\frac{\sqrt3}{2}
+6\frac{2-\sqrt3}{4}
-3
=
\boxed{\sqrt3},
\tag{2.2}
\]

again exactly Oler's face bound

\[
c_0(6-2)=\sqrt3.
\]

Thus equality in the pentagon/hexagon Oler face inequality is governed by Wegner's exact equality classification.

---

## 3. Compactness of unit equilateral low-degree faces

Fix `m in {5,6}`. Consider convex equilateral `m`-gons

\[
P=(p_1,\ldots,p_m)
\]

in cyclic order with

\[
|p_i-p_{i+1}|=1
\]

and all distinct vertex distances at least one.

Modulo rigid motions this family has compact closure. Fix

\[
p_1=(0,0),
\qquad
p_2=(1,0).
\]

All remaining vertices lie in the radius-`m` disk about `p_1` because the boundary path has total length `m`. Closed convexity and all distance inequalities survive limits; strict convexity may degenerate to collinearity, which is exactly what occurs in DP.

Area and convex-hull perimeter are continuous under this convergence.

---

## 4. Zero-slack limits are Groemer and contain an extra unit edge

Let `P_j` be a sequence of strict convex unit-separated equilateral `m`-gons, `m=5` or `6`, whose Oler face slack tends to zero:

\[
\operatorname{area}(P_j)-c_0(m-2)\to0.
\tag{4.1}
\]

After rigid motions and a subsequence, let the vertex sets converge to `X` and their convex hulls to `K`.

Every `P_j` has perimeter exactly `m`. Convex-hull perimeter is continuous, so

\[
\operatorname{per}(K)=m.
\tag{4.2}
\]

Also

\[
\operatorname{area}(K)=c_0(m-2).
\tag{4.3}
\]

By Sections 1-2, equations (4.2)-(4.3) give equality in the scaled Wegner inequality. Hence `X` is a scaled Wegner packing and in particular a Groemer packing: its centers admit a triangulation by unit equilateral triangles.

The original cyclic boundary graph contributes only the `m` unit side pairs

\[
p_ip_{i+1}.
\]

A Groemer packing on five or six points contains a unit equilateral triangle. The cycle `C_m` itself contains no triangle. Therefore at least one edge of the Groemer unit triangulation joins a pair that is **not** consecutive in the original cyclic order.

Thus:

### Theorem LH.1 — hidden unit diagonal in every zero-slack limit

For `m=5` or `m=6`, any zero-Oler-slack limit of strict convex unit-separated equilateral `m`-gons satisfies

\[
\boxed{
\min_{\substack{i,j\\j\not\equiv i\pm1\pmod m}}
|p_i-p_j|=1.
}
\tag{LH.1}
\]

In fact the limiting five- or six-point set contains a unit equilateral triangle.

For DP this recovers the visible degeneration: the near-flat bottom vertex acquires unit diagonals to the upper vertices and the limit is a triangular-lattice cluster.

---

## 5. Uniform stability away from hidden diagonals

The compactness argument immediately makes LH.1 quantitative without needing an explicit modulus.

Fix `eta>0`. Let `F_{m,eta}` be the compact family of convex equilateral `m`-gons, `m=5` or `6`, satisfying

\[
|p_i-p_j|\ge1+\eta
\]

for every nonconsecutive pair.

No member of `F_{m,eta}` can attain the Oler equality value by LH.1. Area is continuous on this compact set. Therefore its minimum is strictly larger than the Oler bound.

### Theorem LH.2 — positive low-degree face gap at fixed hidden-diagonal margin

For every `eta>0` and `m in {5,6}`, there exists

\[
\sigma_m(\eta)>0
\]

such that every convex equilateral unit-separated `m`-gon whose nonconsecutive vertex pairs all satisfy

\[
|p_i-p_j|\ge1+\eta
\]

obeys

\[
\boxed{
\operatorname{area}(P)
\ge
c_0(m-2)+\sigma_m(\eta).
}
\tag{LH.2}
\]

Equivalently, if a sequence of pentagonal or hexagonal defect faces has face slack tending to zero, then

\[
\boxed{
\min_{\text{nonedge }ij}(|p_i-p_j|-1)\to0.
}
\tag{LH.3}
\]

---

## 6. Consequence for triangle-free C65 defect faces

An actual bounded C65 contact face is strictly convex and its boundary is exactly a contact cycle. Triangle-freeness forbids any nonconsecutive pair in a pentagon or hexagon from being at distance exactly one if that pair together with boundary unit edges would create a unit triangle; more generally, every nonboundary unit pair would be an additional contact chord and would split the face, contradicting that the displayed cycle is a face boundary.

Hence every nonconsecutive pair in the face is strictly longer than one.

LH says that low-degree face slack can still tend to zero, but only by pushing one or more forbidden contact chords arbitrarily close to activation.

Thus the DP obstruction is now classified invariantly:

```text
cheap 5/6-face
    -> near-Groemer geometry
    -> hidden nonedge length 1+o(1)
    -> limiting unit triangle / face subdivision.
```

This is the correct local object for any simultaneous KKT/global-optimality stability theorem.

---

## 7. What the theorem does not prove

LH does **not** infer that `1+o(1)` equals one at finite `D`. Arbitrarily close hidden diagonals are compatible with triangle-freeness.

It also does not by itself supply a uniform face charge, because the margin `eta` may tend to zero with `D`. DP remains a valid regression.

The missing next step is source-specific: show that a linear population of near-Groemer defect faces with hidden diagonals approaching unit length cannot all remain unactivated in a lexicographically normalized global minimizer. Potential mechanisms are:

1. external bracing/contact incidence required at the degenerating nearly-flat vertex;
2. simultaneous activation of a matching of hidden diagonals;
3. a second-order diameter-decreasing motion using the near-triangle slack;
4. conversion of the hidden-diagonal population into response conductance or pinned-stress surplus.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Scaled Wegner:
  area(K)+per(K)/2
    >= (sqrt3/2)(N-1)
       +(2-sqrt3)/4 * ceil(sqrt(12N-3)-3),
with equality iff the center set is a scaled Wegner/Groemer packing.

For equilateral convex faces:
  N=5, per=5 -> area>=3sqrt3/4 exactly Oler;
  N=6, per=6 -> area>=sqrt3 exactly Oler.

Therefore any sequence of strict convex unit-separated 5- or 6-faces whose Oler
slack tends to zero converges, after a subsequence, to a Groemer packing and acquires
at least one nonboundary unit edge; the limit contains a unit equilateral triangle.

Quantitative compactness:
For every eta>0, if all nonconsecutive distances are >=1+eta, then
  area >= Oler_min + sigma_m(eta)
for some sigma_m(eta)>0.
```
