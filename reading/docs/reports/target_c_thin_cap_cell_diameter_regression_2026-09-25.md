> Generated reading edition · [exact source](../../../docs/reports/target_c_thin_cap_cell_diameter_regression_2026-09-25.md) · source SHA-256 `d196592f0b9f27e1b4bb017ce5812923cce61af487fda34b0d4bb5f562aa68d0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7809076E5F73","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — thin cap cells separate diameter budget from rhombus area

**Date:** 2026-09-25
**Repository commit:** `15cd5d8a8346b42101b355afebd6da28ccd58886`
**State version:** `2026-09-14.audit.51`
**Run type:** exact geometric regression
**Target:** C-II, full-core aggregate detour
**Starting status:** canonical Sections 122–123 and the full-core train-coupled surplus floor
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** focused search found no theorem used below
**Computation:** not used

## LEVEL I STATUS

STILL OPEN.

## 1. Starting canonical endpoint and attempted chain

Section 122 retains the sharper finite inequality

$$
\sum_r E_r\ge(4-2\sqrt3)\sum_r\frac{A^0_{4,r}}{d_r},
\qquad E_r=L_r+P_{{\rm exc},r}-2d_r,
$$

but its published asymptotic consequence only uses `d_r<=D`. The promoted
train-coupled floor gives `liminf mu_D >= mu_TC = 1.637562...`, where
`mu_D=(e_BB+2s_C-3k)/D`. The attempted shortcut was

```text
linear total cell diameter budget above D
    -> strictly larger area-weighted reciprocal-diameter sum
    -> stronger aggregate detour demand
    -> contradiction with source boundary currency.
```

The first implication is false for the geometric cell-budget hypotheses alone.
The construction below is a regression for that shortcut. It is not a canonical
source, a KKT stress, or a counterexample to the conjecture.

## 2. Thin-cap partition regression

**Classification:** regression, unreviewed.

### Statement

Fix any real `0<c<1`. There is a sequence of even integers `q->infinity`,
unit-separated convex `q`-gons `F_q` of diameter `D_q->infinity`, and partitions
of `F_q` into convex cells `P_{0,q},...,P_{N_q,q}` with vertices among the
vertices of `F_q`, such that:

1. `F_q` tends after division by `D_q` to a radius-`1/2` disk, and
   `area(F_q)=pi D_q^2/4-o(D_q^2)`;
2. the cells have disjoint interiors and tile `F_q` exactly; their vertices
   are unit-separated, and each outer vertex belongs to at most three cells;
3. `N_q=Theta(sqrt(D_q))`, hence `N_q=O(D_q^(2/3))`, and
   `sum_r sqrt(area(P_{r,q}))=O(D_q)`;
4. one cell has diameter exactly `D_q` and area
   `pi D_q^2/4-O(D_q)`, while all other cells together have area `O(D_q)`;
5. nevertheless
   $$
   \frac1{D_q}\sum_r\operatorname{diam}(P_{r,q})\longrightarrow1+c,
   \qquad
   \frac1{D_q}\sum_r
     \frac{\operatorname{area}(P_{r,q})}
          {\operatorname{diam}(P_{r,q})}
       \longrightarrow\frac\pi4.
   $$

The polygon-dissection deficit of Section 123 is zero for this partition:
`q-2-sum_r(a_r-2)=0`, where `a_r` is the number of vertices of `P_r`.
In particular one may take `c=mu_TC-1`, which lies in `(0,1)`: the geometric
total-diameter scale can equal the promoted numerical surplus floor without
increasing the area-over-diameter sum above its one-cell value.

### Complete proof

Let `q` range over even integers, put `x=pi/q`, and let `F_q` be the regular
`q`-gon of circumradius `R=1/(2 sin x)`. Every hull side has length one. Its
diameter is `D=2R=1/sin x`, and all pairs of vertices are unit-separated.
The regular-polygon area formula gives

$$
\operatorname{area}(F_q)=\frac{qD^2}{8}\sin(2\pi/q)
   =\frac\pi4D^2+O(1),
$$

and its normalized Hausdorff limit is the radius-`1/2` disk.

Set `M=floor(sqrt(D))` and `N=floor(cD/M)`. For large `q`, the first `NM`
boundary edges occupy less than one third of the perimeter, because
`NM/D->c<1<pi/3` and `q/D->pi`. Divide those edges into `N` consecutive blocks
of `M` edges. For each block, take the convex cap polygon spanned by its
`M+1` boundary vertices and closed by the chord joining its endpoints.
Cut these `N` cap polygons from `F_q`; call the remaining convex polygon `P_0`.
The caps have disjoint interiors and share only endpoints when adjacent; the
chords and retained boundary form the boundary of `P_0`. Every original hull
vertex is in one, two, or three cells. The elementary polygon dissection has
`a_0=q-N(M-1)` and `a_r=M+1` for `r>=1`, so

$$
q-2-\sum_{r=0}^{N}(a_r-2)=0.
$$

An antipodal pair of hull vertices lies outside the cut arc and remains in
`P_0`; hence `diam(P_0)=D`. Each cap is contained in an arc subtending angle
`2Mx<pi`, so its diameter is the endpoint chord

$$
d_{cap}=D\sin(Mx)=\frac{\sin(Mx)}{\sin x}=M(1+o(1)).
$$

Therefore `N d_cap/D->c` and `sum_r d_r/D->1+c`.

The exact area of one cap is

$$
\frac{D^2}{8}\bigl[M\sin(2x)-\sin(2Mx)\bigr].
$$

Its sagitta is `h=R(1-cos(Mx))`. Since `x=Theta(D^{-1})`
and `M=Theta(sqrt D)`, we have `h=O(M^2/D)=O(1)`. Its chord is at most `M`,
so the exact area is bounded by `Mh=O(M^3/D)=O(sqrt D)`. Consequently all caps
together have area `O(N sqrt D)=O(D)`. The central cell has the asserted area.
The square-root budget follows from

$$
\sum_r\sqrt{\operatorname{area}(P_r)}
 \le O(D)+N\,O(D^{1/4})=O(D).
$$

Finally the central term in `sum area(P_r)/d_r` is
`(pi/4)D+O(1)`, while the cap terms total at most
`O(D)/[M(1+o(1))]=O(sqrt D)=o(D)`. This proves both limits.

### Scope and dependencies

This uses only elementary regular-polygon geometry. It realizes the convex
attachment-cell tiling, near-disk area, square-root area budget, sublinear cell
count, unit-separated loaded vertices, at-most-three cell incidence, and zero
polygon-dissection deficit as **abstract geometry**. It does not realize the
unloaded positive-contact components, their rhombi, the KKT equilibrium,
`e_BB`, `s_C`, `k`, or global diameter minimality. Thus it does not refute a
stronger theorem using any of those source-derived inputs.

## 3. Exact frontier effect

No canonical theorem changes. The regression shows that the promoted lower bound
on `mu_D`, together with cell area saturation and the square-root budget, cannot
by itself improve the Section-122 estimate by replacing `d_r<=D` with a
purported strict area-weighted average. Linear excess cell diameter may be
stored in cells of vanishing total area.

## 4. Exact remaining lemma for this mechanism

A successful weighted-area route needs a **source-derived** nonconcentration
statement. One sufficient form is: there exist fixed `epsilon,eta>0` such that
every sufficiently large canonical full-core survivor satisfies

$$
\sum_{r:\,d_r\le(1-\epsilon)D} A^0_{4,r}\ge\eta D^2.
$$

This would improve Section 122's normalized lower bound by at least
`(4-2sqrt(3)) eta epsilon/(1-epsilon)`. It would still require an upper
detour/payment inequality strong enough to turn that improvement into a
contradiction. A different closing route is a source-preserving strict
sub-`D` deformation or an exact unit triangle.

## 5. Claim audit and regressions

| Claim | Classification | Reason |
| --- | --- | --- |
| Thin-cap partition and limits above | Regression, unreviewed | Complete elementary proof above; no source/KKT assertion |
| Cell diameter excess forces weighted-area excess | Rejected under geometric budgets alone | Thin caps hold linear diameter with `o(D^2)` area |
| The same partition is a triangle-free global minimizer | Not claimed | No contact network or global-optimality certificate |

The construction keeps boundary occurrences and convex cells distinct. It does
not delete source isolates, identify cells with the source, infer an Euler path,
or claim simultaneous source exchanges. The earlier abstract scalar
compatibility witness in the full-core diameter-budget report is consistent
with this geometric regression; this report adds a realizable near-disk convex
cell partition with the Section-123 dissection count exactly sharp.

## 6. Literature, computation, promotion, and handoff

No external theorem or computation is load-bearing. A focused literature search
found no applicable theorem needed for the construction.

**Promotion recommendation:** retain as an unreviewed regression. It narrows a
proposed proof mechanism but does not alter the canonical Target C or Level I
status. The next audit should check the polygon dissection and the scope line
against Sections 83, 122, and 123. The next mathematical step is to derive
nonconcentration or a detour payment from the actual positive-contact source,
not from the convex cell budgets alone.
