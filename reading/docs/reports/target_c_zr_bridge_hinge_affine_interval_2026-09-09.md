> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_bridge_hinge_affine_interval_2026-09-09.md) · source SHA-256 `4503d6894b1e0a8a06df032e89b5de88639bd7712a56dd79c35a0665379df46e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-14F0E228B44F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZHAI: affine interval classes and the star-cutoff/nonstar-blocker dichotomy

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-bridge-hinge-interval`  
**Run type:** exact coefficient/rank refinement of ZHI  
**Target:** Target C bridge-hinge normal form  
**Depends on:** ZHI, C23 Helly hub  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZHI proves that the active diameter matrix restricted to a consecutive `H`-bridge hinge trunk has rank at least `H-1`, that every diameter row has consecutive-interval support, and that root-star rows have prefix support.

The coefficients have more structure than an arbitrary interval matrix.  On a fixed separating interval, a diameter row is an affine function of the physical bridge pivots `a_j`.  Therefore all rows with the same topological interval span a space of dimension at most three.  For diameter rows incident to a fixed root terminal `z`, all rows with the same prefix cutoff span a space of dimension at most two.

Combining this with ZHI gives the exact dichotomy

$$
\boxed{
H-1\le 2N_{\rm star}+m_{\rm ns},
}
$$

where `N_star` is the number of distinct trunk cutoff depths used by `z`-star diameter edges and `m_ns` is the number of nonstar diameter rows with nonzero hinge action.  Thus a macroscopic trunk cannot be blocked by a bounded number of star attachment depths plus a sublinear nonstar support.

C23 further says all nonempty topological trunk intervals pass through one common projected hub block.  The hinge matrix is therefore a common-hub affine interval system, not an arbitrary consecutive-ones matrix.

---

## 1. ZHI notation

Use the ZHI consecutive physical bridge trunk

$$
f_1,\ldots,f_H,
\qquad f_j=a_jb_j,
$$

with nested descendant shores

$$
S_1\supset\cdots\supset S_H.
$$

Let `phi_j` be the descendant rotation about `a_j`, and let

$$
G_{hj}=2(p_x-p_y)\cdot(\phi_j(x)-\phi_j(y))
\tag{1.1}
$$

for an active diameter edge `h=xy`.

ZF and ZHI give

$$
\operatorname{rank}G\ge H-1,
\tag{1.2}
$$

with equality improved to full rank `H` when the first root shore contains at least two vertices.

For every row there is a topological separating interval

$$
I_h=\{l_h+1,\ldots,r_h\}
\tag{1.3}
$$

such that `G_hj=0` outside `I_h`.  Entries inside `I_h` may vanish.

---

## 2. Exact affine coefficient formula on a separating interval

Fix one active diameter edge `h=xy`, and suppose throughout its separating interval that `x` is on the descendant shore and `y` on the root shore.  Put

$$
d_h=p_x-p_y.
$$

For `j in I_h`,

$$
\phi_j(x)=J(p_x-p_{a_j}),
\qquad
\phi_j(y)=0.
$$

Hence

$$
\begin{aligned}
G_{hj}
&=2d_h\cdot J(p_x-p_{a_j})\\
&=2d_h\cdot J(p_y-p_{a_j}),
\end{aligned}
\tag{ZHAI1}
$$

because `d_h dot Jd_h=0`.

Thus

$$
\boxed{
G_{hj}
=c_h-2d_h\cdot Jp_{a_j}
\qquad(j\in I_h),
}
\tag{ZHAI2}

where

\[
c_h:=2d_h\cdot Jp_y.
$$

If `y` rather than `x` is descendant, the same formula holds after changing the row parameters by an overall sign and exchanging the endpoint used in the constant term.  In either orientation, the dependence on `j` is affine in the two coordinates of the pivot `p_{a_j}`.

No approximation or near-radial hypothesis is used.

---

## 3. At most three dimensions per topological interval class

Fix one interval

$$
I=\{l+1,\ldots,r\}.
$$

Define three vectors in `R^H`, supported on `I`, by

$$
\mathbf 1_I,
\qquad
A_I^{(x)}=(a_{j,x})_{j\in I},
\qquad
A_I^{(y)}=(a_{j,y})_{j\in I},
\tag{3.1}
$$

and zero outside `I`.

Equation ZHAI2 shows that every diameter row whose topological separating interval is exactly `I` belongs to

$$
\operatorname{span}\{\mathbf1_I,A_I^{(x)},A_I^{(y)}\}.
$$

Therefore:

### Theorem ZHAI.1 — three-dimensional interval-class bound

For every fixed topological trunk interval `I`,

$$
\boxed{
\dim\operatorname{span}\{G_{h,*}:I_h=I\}\le3.
}
\tag{ZHAI3}

Let `N_int` be the number of distinct nonempty topological intervals represented by active diameter rows.  Then

\[
\operatorname{rank}G\le3N_{int}.
$$

Combining with ZHI gives

$$
\boxed{
N_{int}\ge\frac{H-1}{3}.
}
\tag{ZHAI4}

Thus a linear bridge trunk forces linearly many distinct diameter routing intervals unless the first-shore Euclidean exception changes only the harmless additive constant.

---

## 4. Root-star rows have only two dimensions per cutoff

Now fix a terminal `z` in the root block `X_0` of the trunk and translate coordinates so

\[
p_z=0.
$$

Take an active diameter edge

$$
h=zy,
\qquad |p_y|=D.
$$

If its partner `y` lies beyond trunk cutoff `r_y`, then its topological interval is the prefix

$$
I_h=\{1,\ldots,r_y\}.
$$

For every `j<=r_y`, ZHAI1 becomes

$$
\boxed{
G_{zy,j}
=-2p_y\cdot Jp_{a_j}.
}
\tag{ZHAI5}

There is no independent constant term.  For one fixed cutoff `r`, all such rows lie in the two-dimensional space spanned by the truncated pivot-coordinate sequences

\[
(a_{j,x})_{1\le j\le r},
\qquad
(a_{j,y})_{1\le j\le r}.
$$

### Theorem ZHAI.2 — two-dimensional star-cutoff bound

Let `N_star` be the number of distinct positive cutoff indices represented by active diameter edges incident to `z`.  Then the complete `z`-star submatrix satisfies

$$
\boxed{
\operatorname{rank}G_{star}\le2N_{star}.
}
\tag{ZHAI6}

Rows with the same cutoff can be numerous, but they contribute at most two new hinge-rank dimensions in total.

---

## 5. Exact star-cutoff versus nonstar-blocker dichotomy

Let `m_ns` be the number of active diameter edges not incident to `z` whose ZHI row is nonzero.  Each such row can increase rank by at most one, so

\[
\operatorname{rank}G
\le
\operatorname{rank}G_{star}+m_{ns}
\le
2N_{star}+m_{ns}.
\tag{5.1}
$$

Use ZHI5:

### Theorem ZHAI.3 — finite blocking dichotomy

$$
\boxed{
H-1\le2N_{star}+m_{ns}.
}
\tag{ZHAI7}

If the first root shore contains at least two vertices, then

\[
\boxed{
H\le2N_{star}+m_{ns}.
}
\tag{ZHAI8}

Consequently at least one of the following holds:

\[
\boxed{
N_{star}\ge\frac{H-1}{4}
\quad\text{or}\quad
m_{ns}\ge\frac{H-1}{2}.
}
\tag{ZHAI9}

The constants are deliberately nonoptimized; ZHAI7 is the exact useful statement.

For the ZHT trunk, `H=Omega_eta(D)`.  Therefore the source must have either

1. `Omega_eta(D)` distinct star-partner cutoff depths along the same trunk, or
2. `Omega_eta(D)` nonstar diameter rows with genuinely nonzero rotational action on the trunk.

This is a support theorem, not a weight theorem.  C66 permits the second family to have total beta mass `o(1)`.

---

## 6. C23 projects every diameter route through one trunk hub

Let `T_br` be the full contact bridge-block tree, and let `X_*` be the C23 Helly hub contained in the bridge-tree path of every active diameter edge.

Let the trunk blocks be

\[
X_0,X_1,\ldots,X_H,
$$

where `f_j` joins `X_{j-1}` to `X_j`.  Let `X_k` be the unique projection of `X_*` to this trunk path: the path from `X_*` to the trunk first meets it at `X_k`.

Fix any active diameter edge `h`.  Its block-tree path `P_h` contains `X_*`.  If `P_h` intersects the trunk at a block `Y`, then the unique tree path from `X_*` to `Y` lies inside `P_h` and passes through `X_k`.  Therefore `X_k in P_h`.

The intersection of two tree paths is connected, so `P_h` intersects the trunk in a connected subpath containing `X_k` whenever that intersection is nonempty.

### Theorem ZHAI.4 — common-hub interval geometry

Every nonempty topological separating interval has closed block span containing the same trunk block `X_k`.

Equivalently, if the endpoint projections of a diameter path onto the trunk are `X_l,X_r` with `l<=r`, then

\[
\boxed{l\le k\le r.}
\tag{ZHAI10}

Thus the interval family underlying `G` is a common-hub family.

If `z in X_0`, then every active star edge `zy` whose row meets the trunk has cutoff

\[
\boxed{r_y\ge k.}
\tag{ZHAI11}

So all star-prefix rows reach at least the projected Helly hub before they are allowed to terminate.

---

## 7. Interaction with the PR #111 low-reset branch

In ZEG-A/ZSP, the captured diameter path runs through the complete ZHT trunk and is `D+o(D)` long.  Central trunk pivots lie in an `o(D)` tube around that diameter segment.  ZHAI5 then says that a star row on a central portion is controlled by the signed transverse moment of its diameter direction against a nearly axial pivot.

The exact rank dichotomy ZHAI7 prevents the following overly simple regression:

```text
boundedly many star partner depths
+ sublinear nonstar diameter support
+ a linear physical bridge trunk.
```

That regression cannot satisfy ZF.

The remaining regressions are sharper:

- linearly many star endpoints may peel off at distinct trunk depths;
- or linearly many nonstar diameter rows of vanishing total beta mass may supply the missing exact rank;
- tiny transverse deviations of the ZSP pivots can support exact rank even when the limiting affine coefficient system is low-dimensional.

Those are now the two support-level branches to attack.

---

## 8. Why this does not yet close Level I

Neither branch of ZHAI9 is presently impossible.

A geometric diameter graph can contain linearly many star partners at distinct bridge depths.  Conversely, ZS and ZRI already warn that a linear or quadratic mechanically tiny support can remain geometrically indispensable.  Exact rank does not lower-bound beta mass or singular values.

Therefore one must not infer a quantitative response defect from ZHAI7 alone.

The most promising next step is to combine:

- the explicit moment formula ZHAI5;
- ZHT/ZSP near-axial pivot positions;
- C18's sub-`60 degree` common star cone;
- C66's `o(1)` total nonstar beta mass; and
- the two-sided column sign law ZHI13.

A successful theorem would show that either the star cutoff family itself supplies a forbidden ordered geometry, or the nonstar rows must carry nonvanishing beta mass rather than merely nonzero support.

---

## 9. Classification

**Status:** proved report-level refinement of ZHI.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

ZHAI:
On the separating interval of diameter h=xy, orient x descendant, y root. Then
    G_hj = 2(x-y) dot J(x-a_j)
          = 2(x-y) dot J(y-a_j).
Thus for a fixed topological interval I, all rows lie in the span of
    1_I, (a_j,x)_I, (a_j,y)_I,
so one interval class has rank <=3. Hence rank G>=H-1 forces at least (H-1)/3
distinct topological routing intervals.

For a root-star edge zy, translate z=0. On its prefix j<=r_y,
    G_zy,j = -2 y dot J a_j.
Rows with the same cutoff r_y span dimension <=2. If N_star is the number of distinct
star cutoffs and m_ns is the number of nonstar nonzero rows,
    H-1 <= rank G <= 2 N_star + m_ns.
So either N_star=Omega(H) or m_ns=Omega(H).

C23 adds a common-hub constraint: project the universal diameter-path hub X_* to trunk
block X_k. Every nonempty diameter/trunk interval has closed block span containing X_k;
all z-star prefixes terminate at depth >=k.

Next target: combine the explicit star moment formula with ZHT/ZSP near-axial pivots,
C18 star-angle control, C66 nonstar beta mass o(1), and ZHI's two-sided blocker signs.
```
