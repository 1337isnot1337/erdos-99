<!-- migration-source: path=docs/reports/target_c_hex_window_shear_endpoint_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=7c45761ed32dc530ab486de54c643a8c3268b0ea; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — exact endpoint for centrally symmetric oblique-hexagon shear

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / computation / regression
**Target:** C-II / Level I
**Starting status:** canonical Sections 122–123; full-core and macroscopic-container branches open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for status only; no theorem imported
**Computation:** used: `research/verify_target_c_hex_window_shear_endpoint.py`

## LEVEL I STATUS

STILL OPEN.

This report gives an exact same-cardinality global comparison for one candidate
triangle-free family. It does not assert that arbitrary triangle-free sources have
the tested affine-window form, so it does not close C-II or Level I.

## 1. Exact restricted theorem

For an integer \(R\ge1\), define the axial hexagonal index window

\[
 H_R=\{(i,j)\in\mathbb Z^2:\max(|i|,|j|,|i+j|)\le R\}.
\]

Let \(u,v\) be unit vectors with \(u\cdot v=c\), where \(0\le c<1/2\), and map
\((i,j)\mapsto iu+jv\). Then:

1. the image is unit-separated;
2. its unit-contact graph has exactly the four differences
   \(\pm u,\pm v\), hence is bipartite and triangle-free;
3. \(|H_R|=1+3R(R+1)\);
4. its exact squared diameter is
   \[
   D_{\rm shear}^2=8R^2(1-c)>4R^2;
   \]
5. the equilateral choice \(c=1/2\), with the same index set and cardinality, is
   unit-separated and has diameter \(D_{\rm tri}=2R\), and its contact graph contains
   unit equilateral triangles.

Consequently, every non-equilateral member of this restricted affine hex-window
family is not a global diameter minimizer for its cardinality: the equilateral
hex-window competitor has strictly smaller diameter.

### Proof

Write

\[
 q_c(i,j)=|iu+jv|^2=i^2+j^2+2cij.
\]

If \(ij\ge0\), a nonzero integer pair has \(q_c(i,j)\ge i^2+j^2\ge1\).
If \(ij<0\), put \(a=|i|\), \(b=|j|\). Then

\[
 q_c(i,j)=(a-b)^2+2ab(1-c).
\]

For \(a=b=1\), this is \(2(1-c)>1\). For \(a\ne b\), the first term is at
least \(1\) and the second term is positive. Thus all distinct image points are
at distance at least one. Equality is possible only for
\((i,j)=\pm(1,0),\pm(0,1)\).

The contact graph is therefore a subgraph of the square grid on the two index
directions. Coloring \((i,j)\) by \(i+j\bmod2\) proves bipartiteness and
triangle-freeness.

The cardinality identity is the standard count of the six axial sides:

\[
 |H_R|=1+6(1+\cdots+R)=1+3R(R+1).
\]

For the diameter, the difference set is contained in the continuous hexagon

\[
 H_{2R}^{\mathbb R}=\{(x,y):|x|\le2R,\ |y|\le2R,\ |x+y|\le2R\}.
\]

The quadratic form \(q_c\) is convex. Its maximum on this hexagon is attained
at a vertex. At the six vertices the values are \(4R^2\) at
\((\pm2R,0),(0,\pm2R)\) and \(8R^2(1-c)\) at
\((\pm2R,\mp2R)\). Since \(c<1/2\), the latter is larger. The difference
\((2R,-2R)\) is attained by the two window points \((R,-R)\) and
\((-R,R)\), so

\[
 \operatorname{diam}^2=8R^2(1-c).
\]

At \(c=1/2\), the same calculation gives \(D_{\rm tri}^2=4R^2\). The
three image points (0,u,v) form a unit equilateral triangle, and the strict
inequality (8R^2(1-c)>4R^2) proves the same-cardinality comparison.
\(□\)

## 2. Certified finite check

The proof is independently checked by

```text
python3 research/verify_target_c_hex_window_shear_endpoint.py
```

The script uses only integer enumeration and rational arithmetic. For
(c=499/1000), it verifies unit separation, the exact unit-difference set, the
cardinality formula, and the strict diameter comparison for several radii.

It does not use floating-point coordinates or a numerical optimizer.

## 3. What this eliminates

The result eliminates the following proposed disproof mechanism at the level of
this natural finite family:

```text
take the symmetric triangular-lattice hexagon,
shear the two unit directions past 60 degrees,
retain the same axial window,
and obtain a triangle-free global minimizer.
```

The sheared object is feasible and triangle-free, but the unsheared object has the
same cardinality and strictly smaller diameter. Thus local triangle-freeness and
near-equilateral rhombic geometry are not enough to certify global optimality.

This is stronger than a density-only regression because the comparison is finite,
source-cardinality exact, and globally valid for the restricted candidate.

## 4. Exact remaining obstruction

The theorem does not apply to arbitrary finite subsets of an oblique lattice with a
non-hexagonal index window, non-affine triangle-free near-triangular packings, the
canonical source/core decomposition with inactive chambers or exterior caps, a shear
whose shape is simultaneously changed to a different index window, or an arbitrary
global minimizer not known to lie in an affine-lattice family.

In particular, choosing `c=1/2-epsilon_D` with `epsilon_D down to 0` makes the
restricted diameter excess only
`2R^2 epsilon_D+O(R^2 epsilon_D^2)`. The theorem supplies no uniform
positive gap when the shear tends to the equilateral endpoint. The missing C-II
statement remains a source-level second-order comparison for all non-hexagonal
windows and all non-lattice full-core sources.

## 5. Proof-obligation ledger

| Item | Status | Scope / reason |
|---|---|---|
| Canonical Sections 122–123 | trusted canonical input | Exact hypotheses and full-source conventions retained |
| Oblique hex-window theorem above | new proved lemma | Finite affine family; exact source cardinality |
| Script certificate | exact regression | Rational quadratic forms; no numerical optimizer |
| Arbitrary affine-window global optimality | unresolved | Index-window shape can change |
| Type-II aggregate detour closure | unresolved | Residual and source-preserving deformation remain open |
| Macroscopic-container branch | unresolved | No protected finite exchange constructed |
| Level I | open | Original quantifiers remain |

No canonical manifest, route map, or theorem-state entry was promoted by this report.

## 6. Claim audit table

| Claim | Status | Dependencies | Reason |
|---|---|---|---|
| Oblique hex-window unit separation | new proved lemma | elementary quadratic-form calculation | The four unit differences are exact |
| Oblique hex-window diameter formula | new proved lemma | convexity on the continuous difference hexagon | The extremal difference is attained by actual window points |
| Same-cardinality equilateral competitor | new proved lemma | same index window at (c=1/2) | It has strictly smaller diameter and a unit triangle |
| Arbitrary affine-window global optimality | unresolved | none | The index-window shape can change |
| Type-II aggregate detour closure | unresolved | canonical §§122–123 | The source-level residual remains uncontrolled |
| Macroscopic-container branch | unresolved | canonical C-II dichotomy | No protected finite exchange is constructed |
| Level I | open | all original quantifiers | No uniform (n_0) is proved |

## 7. Regression checks

| Regression/correction | Result | Exact hypothesis or failure |
|---|---|---|
| Vanishing-shear near-density family | pass | The present theorem tests the symmetric hex-window subfamily only |
| Near-equilateral triangle-free configurations | pass | (c<1/2) gives a bipartite contact graph with angle tending to (60^circ) |
| Local structure versus global optimality | pass | The sheared window is feasible but is beaten by an exact same-cardinality source |
| Source/scaffold identification | pass | The certificate compares two actual finite sources |
| Contact-isolated source points | not applicable | No inactive points are deleted or introduced in the restricted comparison |
| Non-hexagonal windows | unresolved | Explicitly outside the theorem |

An exact warning against overextending the comparison is the index set
(I=\{(-2,-2),(-2,0),(0,-1)\}) at (c=49/100). Its sheared squared diameter is
(174/25), while replacing the same two basis vectors by either equilateral
orientation gives squared diameter (7). Thus a general “equilateralize every
affine window at fixed indices” lemma is false; the hex-window support geometry is
essential.

## 8. Literature imports

No external theorem is used. The internet search was only a status check; the proof
and certificate are self-contained and use no literature-dependent premise.

## 9. Computation

The command

```text
python3 research/verify_target_c_hex_window_shear_endpoint.py
```

checks the exact cardinality, minimum squared distance, unit-difference set, and
diameter formula for (R=1,2,3,5,9,17) at the rational value (c=499/1000).
All quadratic forms are evaluated with Python `Fraction`; there is no floating-point
rounding and no optimizer. The certificate proves only the restricted finite family
comparison, not global optimality of arbitrary configurations.

## 10. Corrections / supersessions

This report does not supersede a canonical theorem. It narrows the vanishing-shear
regression by adding a source-cardinality-exact global comparison for one natural
window. The prior finite near-density shear regressions remain valid outside this
restricted comparison and still block any density-only closure.

## 11. Promotion recommendation and handoff

**Regression/rejection only — do not promote.**

The strongest new result is the exact same-cardinality comparison for symmetric
oblique hexagonal windows. Its canonical dependency chain is empty beyond elementary
Euclidean geometry; canonical §§122–123 are only the C-II endpoint that remains open.

The next exact lemma needed for this route is a source-level comparison for
non-hexagonal affine windows (or a proof that a near-disk full-core global minimizer
must have a window to which the same comparison applies). That lemma must then be
connected to the aggregate outer-walk detour and the source-preserving deformation
obligation. The binding dead route is any inference from near-density or local
rhombic shear alone to global optimality.

Next files to read: `docs/targets/target-c/CURRENT.md`, canonical §§122–123, and
`docs/targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md`.
