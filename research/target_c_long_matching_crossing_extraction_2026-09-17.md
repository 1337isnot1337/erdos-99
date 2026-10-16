<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "220db7bea3809920f02e7cef0f3fee2e533ec1db", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_long_matching_crossing_extraction_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7084980ad88764b2471c43adb612bf20fd612f0bfc7bf7226f8af312930cd260"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — long inactive matchings have bounded noncrossing degree

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; general source-level geometric lemma  
**Scope:** any unit-separated planar source of diameter at most `D`; applied below to FREE upper gates  
**Dependencies:** unit separation and the diameter bound only  
**Certificate:** `research/verify_target_c_long_matching_crossing_extraction_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The sharp superdiameter-thrackle lemma handles edges longer than `sqrt(D^2-1)`. For the current FREE ancestry, upper-gate deficits need not be that small. The correct replacement is a bounded-conflict statement: if a matching consists of edges of length at least `L`, then any edge can fail to cross only those matching edges with an endpoint inside a fixed-radius disk around one of its own endpoints.

This gives a quantitative extraction theorem for every long matching, including the regime

\[
L=D-O(D^{-\alpha}).
\]

The proof is elementary and uses no KKT or Target C structure.

---

## 1. Short-connector lemma

Let `S` be unit-separated with diameter at most `D`. Let

\[
e=AB,\qquad f=CD
\]

be vertex-disjoint source segments with

\[
|AB|,|CD|\ge L.
\]

Put

\[
\boxed{R(D,L):=\sqrt{D^2-L^2}.}
\tag{LC.1}
\]

### Lemma LC.1

If `AB` and `CD` do not cross properly, then at least one cross-endpoint distance satisfies

\[
\boxed{
\min\{|AC|,|AD|,|BC|,|BD|\}\le R(D,L).
}
\tag{LC.2}
\]

### Proof: convex four-point case

Assume first that the four points are in strictly convex position. Since the matching edges are vertex-disjoint and do not cross, they are opposite sides of the induced convex quadrilateral. Relabel cyclically as

\[
A,B,C,D,
\]

with selected long sides `AB` and `CD`. Put

\[
x=B-A,
\quad y=C-B,
\quad z=D-C,
\quad w=A-D.
\]

Suppose for contradiction that every cross-endpoint distance is larger than `R`. In particular

\[
|y|=|BC|>R,
\qquad
|w|=|DA|>R.
\]

The diagonals are source distances, hence

\[
|x+y|=|AC|\le D,
\qquad
|y+z|=|BD|\le D,
\]

and similarly `|z+w|<=D`, `|w+x|<=D`.

Therefore

\[
2x\cdot y
=|x+y|^2-|x|^2-|y|^2
<D^2-L^2-R^2=0.
\]

The same calculation at the other three vertices gives

\[
x\cdot y<0,
\quad y\cdot z<0,
\quad z\cdot w<0,
\quad w\cdot x<0.
\]

Every exterior turn of the convex quadrilateral is therefore strictly larger than `pi/2`. Their sum would exceed `2pi`, impossible. Hence one cross-endpoint distance is at most `R`.

### Proof: nonconvex or degenerate four-point case

If the four points are not in strictly convex position, some endpoint lies in the convex hull of the other three. Suppose for example that

\[
A\in\operatorname{conv}\{B,C,D\}.
\]

Use the long edge `AB` and put

\[
u={A-B\over|A-B|}.
\]

Because `A` is a convex combination of `B,C,D`, while

\[
u\cdot(B-A)=-|AB|<0,
\]

at least one `Z in {C,D}` satisfies

\[
u\cdot(Z-A)\ge0.
\]

Then

\[
\begin{aligned}
|Z-B|^2
&=|(A-B)+(Z-A)|^2\\
&=|AB|^2+|Z-A|^2+2|AB|\,u\cdot(Z-A)\\
&\ge L^2+|Z-A|^2.
\end{aligned}
\]

Since `|Z-B|<=D`,

\[
|Z-A|^2\le D^2-L^2=R^2.
\]

This is one of the four cross-endpoint distances. The same argument applies if the interior/degenerate endpoint is `B`, `C`, or `D`.

This proves LC.1. `square`

The rectangle with sides `L` and `R(D,L)` has diagonals exactly `D`, and its two long opposite sides do not cross. Thus the radius in LC.1 is sharp.

For

\[
L>\sqrt{D^2-1},
\]

we have `R<1`, contradicting unit separation. LC.1 therefore recovers the existing sharp superdiameter-thrackle lemma as the special case `R<1`.

---

## 2. A long matching has bounded noncrossing degree

Let `E` be a matching of source pairs, every edge having length at least `L`. Define the **conflict graph** `Gamma(E)` on vertex set `E` by joining two matching edges when their straight segments do **not** cross properly.

Fix `e=AB in E`. By LC.1, every conflict neighbor `f` has at least one endpoint in

\[
B(A,R)\cup B(B,R).
\tag{LC.3}
\]

A unit-separated set has at most

\[
\boxed{(2R+1)^2}
\tag{LC.4}
\]

points in a disk of radius `R`: the open radius-`1/2` disks around those source points are pairwise disjoint and fit inside the concentric disk of radius `R+1/2`.

Because `E` is a matching, distinct conflict neighbors use disjoint source endpoints. Assign one witnessing endpoint from (LC.3) to each conflict neighbor. This is injective. Hence

\[
\boxed{
\Delta(\Gamma(E))
\le
2(2R+1)^2.
}
\tag{LC.5}
\]

A graph of maximum degree `Delta` has an independent set of size at least `|E|/(Delta+1)`. An independent set in `Gamma(E)` is exactly a submatching whose segments cross properly pairwise. Therefore:

> **Theorem LC.2 — crossing extraction from a long matching.**  
> If `S` is unit-separated of diameter at most `D` and `E` is a matching with every edge length at least `L`, then `E` contains a pairwise-properly-crossing submatching of size at least
> \[
> \boxed{
> { |E| \over 2(2\sqrt{D^2-L^2}+1)^2+1 }.
> }
> \tag{LC.6}
> \]

No convex-hull hypothesis is required.

---

## 3. Inverse-`D` and variable-slack forms

If

\[
L=D-{A\over D},
\]

then

\[
R^2
=D^2-\left(D-{A\over D}\right)^2
=2A-{A^2\over D^2}.
\tag{LC.7}
\]

For fixed `A`, the conflict degree is `O_A(1)`. Thus every matching of `Theta(D)` pairs of length at least `D-A/D` contains a `Theta(D)` pairwise-crossing submatching.

More generally, if

\[
L=D-\delta,
\qquad \delta=o(D),
\]

then

\[
R^2=2D\delta-\delta^2.
\tag{LC.8}
\]

The extraction loss is therefore only

\[
O(1+D\delta).
\]

In particular, a matching of `m` edges with common deficit bound `delta` contains a crossing submatching of order

\[
\boxed{
\Omega\!\left({m\over 1+D\delta}\right).
}
\tag{LC.9}
\]

This is the scale needed by the FREE upper-gate ledger.

---

## 4. Hostile checks

- LC.1 does not assume that the long-edge endpoints are hull vertices. The nonconvex case is handled separately.
- The matching hypothesis is used only in the degree count. Without it, many conflict edges could reuse one nearby endpoint.
- The conflict graph treats every failure of proper crossing as a conflict, including collinear degeneracies.
- The rectangle example shows the short-connector radius is exact.
- The result is source-level. No deformed activation configuration is used.

**Disposition:** proved a general bounded-noncrossing-degree theorem for long source matchings, extending the sharp superdiameter-thrackle threshold to the entire `D-delta` regime. The immediate Target C application is the FREE upper-gate branch.