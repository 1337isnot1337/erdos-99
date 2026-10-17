> Generated reading edition · [exact source](../../research/target_c_support7_h7b_triangle_simplex_reduction_2026-09-19.md) · source SHA-256 `ef01652c2d20328d250c91fae17d896ccb8d219ba211af1e9eeaa6a21fa0507c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f7b779d41c1c7c113050191bb968f88f2d05aa5b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_h7b_triangle_simplex_reduction_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "18494e557d0ae7018f268d581415cbe20a6959ba2d3f8bdb7839234b1589292a"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — generic interior-ground H7b reduces from 176 to 77 by exact triangle/simplex certificates

**Date:** 2026-09-19  
**Claim class:** exact finite exclusion within the generic interior-ground support-seven branch  
**Scope:** `H7b`: `y_0=0` strictly inside a strict convex heptagon `y_1,...,y_7`, with no reciprocal collinear triple  
**Depends on:** the 184-orbit generic `H7b` order/sign census and its eight signed-trace exclusions; the audited raw-angle/force-turn conversion; the audited physical-pentagon turn simplex  
**Certificate:** `research/verify_target_c_support7_h7b_triangle_simplex_reduction_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding generic `H7b` reduction left 176 order/sign orbits after eight exact signed-distance exclusions. Adding the reciprocal triangle-angle equations among non-ground hull vertices and the full affine content of the physical equilateral-pentagon turn theorem gives

$$
\boxed{176\longrightarrow77.}
$$

The final split is

$$
\boxed{47\ C_7+30\ (C_3\sqcup C_4).}
$$

This is a generic-branch reduction, not a support-seven exclusion. The classified reciprocal-collinearity walls, `H7a`, `H6`, and the surviving `H8` cases remain separate.

## 1. The angular system does not need a ground force-ray order

For a generic interior-ground state, every non-ground reciprocal point `y_i` is a hull vertex. Its six hull rays occur in the fixed convex-heptagon order, and the ray to `y_0` occupies one of the five already-enumerated interior slots. Deleting the two missing non-ground neighbors leaves the five present reciprocal rays of the physical equilateral force pentagon.

Let

$$
x_{i,k}=\delta_{i,k}/\pi,
\qquad i=1,\ldots,7,
$$

be the consecutive force-direction gaps in the signed force cycle at `i`. The exact raw-angle conversion already used in the support-six/H8 certificates expresses every reciprocal angle at a non-ground vertex as an affine form in these variables. For a counterclockwise force arc `R` between two incident edges, the raw angle is one of

$$
R,\quad 2-R,\quad R-1,\quad 1-R,
$$

according to the two edge signs and raw orientation sign.

Only triangles `abc` with `a,b,c\in\{1,\ldots,7\}` and all three relation edges present are used. Hence no cyclic order of the seven signed force rays at the interior ground point is assumed. Because this branch excludes reciprocal collinear triples, each such triangle is ordinary and its three affine angles satisfy

$$
T_{abc}=1.
\tag{1}
$$

Together with the seven face equations

$$
F_i:=\sum_{k=0}^4x_{i,k}=2,
\tag{2}
$$

these are exact rational-affine equalities.

## 2. Use all affine information carried by a physical equilateral pentagon

The audited turn-simplex theorem says that every strict physical equilateral force pentagon satisfies

$$
q_{i,k}:=x_{i,k}+x_{i,k+1}-x_{i,k+3}>\frac13.
\tag{3}
$$

Moreover those five inequalities, with (2), describe the closed convex hull of all physical pentagon turn vectors. Thus this test uses the complete affine-linear information available separately at each non-ground face.

## 3. Exact Farkas contradictions exclude 106 of the 184 generic orbits

For each generic order/sign orbit, form (1)-(2) and the 35 strict inequalities (3). A numerical LP was used only to discover sparse dual supports. The committed verifier does not call an optimizer and does not use floating point.

For 106 of the 184 orbits, the verifier reconstructs an exact rational certificate

$$
\sum_{j\in J}\alpha_j\left(q_j-\frac13\right)=\kappa
\qquad\text{on the affine space }(1)-(2),
\tag{4}
$$

with

$$
\alpha_j>0,\qquad \sum_j\alpha_j=1,\qquad \kappa\le0.
\tag{5}
$$

The left side is strictly positive by (3), while the right side is nonpositive. Hence every such orbit is impossible.

All dual coefficients are solved again from their sparse supports by exact `fractions.Fraction` Gaussian elimination. The verifier checks exact cancellation in all 35 turn variables, positivity of every active coefficient, normalization, and `kappa<=0`.

The 106 exclusions split as

$$
\boxed{72\ C_7+34\ (C_3\sqcup C_4).}
\tag{6}
$$

Of them, 54 have `kappa=0`; the other 52 have `kappa<0`, with exact census

$$
\begin{array}{c|r}
\kappa&\#\\ \hline
-1/30&35\\
-1/66&7\\
-1/102&3\\
-1/24&2\\
-1/120&2\\
-7/156&1\\
-5/114&1\\
-1/57&1
\end{array}.
\tag{7}
$$

Before using the older signed-distance information, the angular/simplex layer leaves

$$
\boxed{78=48\ C_7+30\ (C_3\sqcup C_4)}.
\tag{8}
$$

## 4. Union with the signed-distance trace certificates leaves 77

The preceding generic `H7b` note excluded eight `C7` orbits by exact signed-distance identities. The missing companion verifier referenced by that note is restored as `research/verify_target_c_support7_h7b_generic_order_sign_reduction_2026_09_19.py`; it reproduces the 57-slot and 184-orbit census and coefficient-checks all eight signed-distance certificates over `Fraction`.

Exactly seven of those eight trace-excluded orbits are already among the 106 angular/simplex exclusions. One trace exclusion is independent. Therefore the union removes

$$
106+8-7=107
$$

of the original 184 generic orbits and leaves

$$
\boxed{184-107=77=47\ C_7+30\ (C_3\sqcup C_4).}
\tag{9}
$$

Equivalently, relative to the previously committed trace-reduced state,

$$
\boxed{176\longrightarrow77,}
$$

so this removes 99 additional generic `H7b` orbits by exact angular certificates.

## 5. What remains

The 77 survivors satisfy every equality and strict affine pentagon constraint used here with positive linear feasibility margin. Another affine inequality in one pentagon cannot finish them because of the turn-simplex theorem.

The next layer is nonlinear. Each of the seven physical force pentagons must satisfy its actual equilateral closure, not merely lie in the convex hull of possible turn vectors. Reciprocal distances/radii must also integrate consistently across the relation graph. The next target is to combine nonlinear equilateral-pentagon closure with reciprocal law-of-sines cycle constraints, or derive a monotone consequence that can be interval-certified over the 77 finite order/sign cells.

The collinearity walls remain separate because (1) can degenerate there and the five-slot ground-ray census changes on a coincident ray.

No theorem-state file is changed.

**Disposition:** generic interior-ground support seven is reduced to 77 exact order/sign orbits. C-II remains open.
