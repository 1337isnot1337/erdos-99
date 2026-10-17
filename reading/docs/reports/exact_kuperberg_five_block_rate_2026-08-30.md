> Generated reading edition · [exact source](../../../docs/reports/exact_kuperberg_five_block_rate_2026-08-30.md) · source SHA-256 `27560100129be1bcfc4a9a19360f10f086b4393af5a313dc284a1fb8f5cc1147`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AF559C180C0F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — exact Kuperberg five-block gain and explicit support rate

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`, through active v1.7.3 / Section 153
**Run type:** exact literature reconstruction / quantitative finite witness
**Target:** A, quantitative gap-support route
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.3_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used only to inspect the original Kuperberg--Kuperberg--Kuperberg paper
**Computation:** symbolic/numerical scratch was used to discover the active constraints; the proof below is exact and does not depend on computation

## LEVEL I STATUS

`STILL OPEN`

The preceding quantitative reports obtained an asymptotic support rate from semialgebraicity but left the one-step Puiseux exponent unspecified. This report removes that ambiguity for the actual five-block mechanism in Kuperberg--Kuperberg--Kuperberg §2.1.

In the paper normalization, where circles have radius one and nearest-neighbor center distance two, the explicit three-move construction has gap gain

$$
\boxed{
\delta(d)
=\frac{\sqrt3}{72}d^4-rac1{72}d^5+O(d^6).
}
\tag{E.1}
$$

Thus the leading exponent is exactly four for the published mechanism.

Moreover the repeated-smaller-block step can be quantified directly: a five-block template of parameter `m` fits along the base of the moved middle `Delta_{n-1}` block whenever

$$
\boxed{n-2\ge3m.}
\tag{E.2}
$$

Consequently `k` widening stages require initial block size only `O(3^k)`. Since the quartic recurrence reaches fixed positive width in `O(d^{-3})` stages, the canonical support radius satisfies

$$
\boxed{
W(d)\le C_1\exp(C_2d^{-3})
\qquad(d\downarrow0).
}
\tag{E.3}
$$

This supersedes the unknown-exponent semialgebraic upper bound in the two preceding reports. It also sharpens the fixed-shape vanishing-strain consequence to

$$
\boxed{
\alpha_L^{-3}=o(\log L)
\Longrightarrow
\alpha_1(H_{L,\alpha_L})\ge |P_L|+1
}
\tag{E.4}
$$

for all sufficiently large `L` in the notation of canonical Section 150.

The theorem remains a **free aligned-gap** result. Exterior blockers in a genuinely embedded Target A monomer domain are not removed.

---

## 1. Paper normalization and an exact coordinate model of Figures 3--4

The paper uses the triangular center lattice

$$
\Lambda_2
=
\{(2i+j,\sqrt3j):i,j\in\mathbb Z\},
\tag{E.5}
$$

whose minimum distance is two. The gap packing moves every center with `j>=0` by

$$
(0,d),
\qquad d>0.
\tag{E.6}
$$

Fix `n>=3` and put

$$
a=n-1.
$$

A coordinate realization of the five triangular blocks in Figures 3--4 is the following partition of a trapezoidal patch of the upper half-lattice. We specify centers by their lattice indices `(i,j)` in (E.5):

$$
\begin{aligned}
B_1&=
\{(i,j):0\le j\le a,\ 0\le i\le a-j\},\\
B_2&=
\{(i,j):0\le j\le a,\ a+1-j\le i\le a+1\},\\
B_3&=
\{(i,j):0\le j\le a-1,\ a+2\le i\le2a+1-j\},\\
B_4&=
\{(i,j):0\le j\le a,\ 2a+2-j\le i\le2a+2\},\\
B_5&=
\{(i,j):0\le j\le a,\ 2a+3\le i\le3a+3-j\}.
\end{aligned}
\tag{E.7}

Then `B_1,B_5` are upward `Delta_n` blocks, `B_2,B_4` are downward `nabla_n` blocks, and `B_3` is an upward `Delta_{n-1}` block. Their sizes are respectively

\[
\frac{n(n+1)}2,
\quad
\frac{n(n+1)}2,
\quad
\frac{n(n-1)}2,
\quad
\frac{n(n+1)}2,
\quad
\frac{n(n+1)}2.
$$

For `0<=j<=a-1`, their union is the consecutive row

$$
0\le i\le3a+3-j,
$$

and the top row `j=a` is again consecutive. Thus the five blocks form exactly the finite trapezoid described in the paper.

Use the paper's three moves, with symmetric directions made explicit:

$$
\begin{aligned}
B_1,B_5 &: (0,-x),\\
B_2 &: \left(-\frac{\sqrt3}{2}u,-\frac12u\right),\\
B_4 &: \left(+\frac{\sqrt3}{2}u,-\frac12u\right),\\
B_3 &: (0,v).
\end{aligned}
\tag{E.8}

The `B_2,B_4` directions make 60-degree angles with downward vertical, exactly as in §2.1. The paper performs these moves successively: first increase `x`, then `u`, then `v`.

---

## 2. First move: the exact optimum is `x=d`

The bottom centers of each outer `Delta_n` block initially lie at height `d` above the unshifted lower half-lattice. Moving the outer blocks downward by `x` leaves a packing for

\[
0\le x\le d,
$$

and at `x=d` the bottom boundary restores exact triangular-lattice contacts with the lower half-plane. Thus the maximal first motion is

$$
\boxed{x=d.}
\tag{E.9}

All later gains are increasing for sufficiently small positive first-stage clearance, so the paper's maximizing choice uses (E.9).

---

## 3. Exact nearest-neighbor constraint enumeration

Rigid translation preserves every within-block distance. At `d=0`, all other center pairs in the triangular lattice have distance either two or at least `2sqrt(3)`. For sufficiently small `d`, all four block-translation magnitudes below are `<d`; therefore any originally non-neighboring pair remains farther than

\[
2\sqrt3-2d>2
$$

once, for example, `d<sqrt(3)-1`. It is therefore enough to check the lattice-neighbor pairs.

A direct row-boundary enumeration from (E.7) gives, after the outer move `x=d`, exactly the following nonconstant squared-distance margins `|p-q|^2-4`, up to left-right symmetry and repeated copies:

$$
\begin{array}{c|l}
\text{interface type} & |p-q|^2-4 \\ \hline
\text{outer / fixed upper} & d^2,
\quad d(d+2\sqrt3)\\[1mm]
\text{outer / lower half-plane} & 0\\[1mm]
\text{outer / inner} &
F_d(u),
\quad F_d(u)+2\sqrt3d\\[1mm]
\text{inner / lower half-plane} &
d^2-du+u^2+2\sqrt3d\\[1mm]
\text{inner / fixed upper} &
u^2,
\quad u(u+2\sqrt3)\\[1mm]
\text{left inner / right inner at the top seam} &
u(3u+4\sqrt3)\\[1mm]
\text{inner / middle} &
G_u(v),
\quad u^2+uv+v^2+2\sqrt3u\\[1mm]
\text{middle / lower half-plane} &
(d+v)(d+v+2\sqrt3),
\end{array}
\tag{E.10}
$$

where

$$
\boxed{
F_d(u)
=u^2-(2\sqrt3+d)u+d^2,
}
\tag{E.11}
$$

and

$$
\boxed{
G_u(v)
=v^2-(2\sqrt3-u)v+u^2.
}
\tag{E.12}

For audit, the two controlling formulas can also be read off from one representative contact each.

### Outer-to-inner contact

Take a horizontal nearest-neighbor pair with initial difference `(2,0)`, the left point in `B_1` and the right point in `B_2`. After the moves it has difference

\[
\left(
2-\frac{\sqrt3}{2}u,
\ d-\frac12u
\right).
$$

Subtracting four from its squared length gives exactly

$$
F_d(u)
=d^2-du+u^2-2\sqrt3u.
$$

### Inner-to-middle contact

Take the diagonal nearest-neighbor pair whose initial difference from the middle point to the left-inner point is

$$
(-1,\sqrt3).
$$

After moving the inner block and middle block the difference is

$$
\left(
-1-\frac{\sqrt3}{2}u,
\sqrt3-\frac12u-v
\right).
$$

Its squared-distance margin is

$$
u^2+uv+v^2-2\sqrt3v=G_u(v).
$$

Every expression in (E.10) other than `F_d` and `G_u` is manifestly nonnegative whenever `d,u,v>=0`, once `F_d(u)>=0` is imposed where appropriate.

---

## 4. Exact second move

At `u=0`,

$$
F_d(0)=d^2>0.
$$

The two roots of `F_d` are

$$
\frac{2\sqrt3+d
\pm
\sqrt{(2\sqrt3+d)^2-4d^2}}{2}.
$$

The continuous motion from zero encounters the smaller root first. Define

$$
\boxed{
\phi(d)
:=
\frac{2\sqrt3+d-
\sqrt{(2\sqrt3+d)^2-4d^2}}{2}.
}
\tag{E.13}

Then `F_d(u)>=0` for

\[
0\le u\le\phi(d),
$$

all other second-stage margins in (E.10) remain nonnegative, and the horizontal outer-inner contacts become exact at `u=phi(d)`. Hence the maximal second movement in the prescribed continuous move is

$$
\boxed{u=\phi(d).}
\tag{E.14}

Expansion at zero gives

\[
\boxed{
\phi(d)
=
\frac{d^2}{2\sqrt3}
-\frac{d^3}{12}
+\frac{\sqrt3}{36}d^4
+O(d^5).
}
\tag{E.15}

The first amplification stage is therefore actually a **quadratic bottleneck**: the distance gained by moving the outer blocks tangentially to their horizontal inter-block contacts is second order.

---

## 5. Exact third move and quartic gap gain

With `u=phi(d)>0`,

\[
G_u(0)=u^2>0.
$$

The roots of `G_u` are

$$
\frac{2\sqrt3-u
\pm
\sqrt{(2\sqrt3-u)^2-4u^2}}{2}.
$$

Define the smaller root

$$
\boxed{
\psi(u)
:=
\frac{2\sqrt3-u-
\sqrt{(2\sqrt3-u)^2-4u^2}}{2}.
}
\tag{E.16}

Then `G_u(v)>=0` for

\[
0\le v\le\psi(u),
$$

and every other third-stage margin in (E.10) stays nonnegative. Thus the middle block may be moved upward by

$$
\boxed{v=\psi(\phi(d)).}
\tag{E.17}

Along the interior of the middle block's base, the upper-half center row has moved from height `d` to height

\[
d+v,
$$

while the lower half-packing is unchanged. This creates an aligned local gap of width

$$
\boxed{d'=d+\delta(d),
\qquad
\delta(d)=\psi(\phi(d)).}
\tag{E.18}

Expanding (E.16) and substituting (E.15) gives

\[
\boxed{
\delta(d)
=
\frac{\sqrt3}{72}d^4
-\frac1{72}d^5
+\frac{\sqrt3}{144}d^6
+O(d^7).
}
\tag{E.19}

In particular

\[
\boxed{
\delta(d)\sim\frac{\sqrt3}{72}d^4.
}
\tag{E.20}

This explains a point left quantitative only in prose in the original paper. The sentence that the gap is to be widened “by a factor bounded away from 1” cannot be used as a uniform small-`d` multiplicative estimate for this explicit mechanism: (E.20) gives

\[
\frac{d'}d
=1+\frac{\sqrt3}{72}d^3+O(d^4)
\longrightarrow1.
$$

The proof itself only needs positive monotone gain and repeated smaller blocks, so there is no conflict with the qualitative theorem.

---

## 6. Exact nesting ratio: factor three in block size

The paper says that `n` can be taken large enough to repeat the operation with smaller blocks. The coordinate model makes this quantitative.

A size-`m` five-block template of the form (E.7), with `b=m-1`, occupies in lattice indices the rows

$$
0\le j\le b,
$$

and for `0<=j<=b-1` the complete interval

$$
0\le i\le3m-j.
\tag{E.21}

Its top row also satisfies the same containing inequality.

After one widening stage, the moved middle block is a rigid translate of `Delta_{n-1}`. Before translation, that block is a triangular lattice set with parameter `n-1`, hence after shifting its base coordinate to zero it has rows

\[
0\le j\le n-2,
\qquad
0\le i\le n-2-j.
\tag{E.22}

A translated copy of (E.21) fits along the base of (E.22) provided

\[
3m-j\le n-2-j
$$

for every relevant row, i.e. exactly when

$$
\boxed{3m\le n-2.}
\tag{E.23}

If desired one may impose a fixed extra lattice-row safety margin; this only replaces the `2` in (E.23) by another absolute constant and does not alter the factor three.

Because the parent middle block moved rigidly, its internal triangular-lattice geometry is unchanged. Its base is precisely the newly widened local gap segment. Therefore a child five-block template satisfying (E.23) sees the same local aligned-gap geometry and the same three-move constraint calculation.

Iterating backward, `k` widening stages can be supported by an initial block parameter

\[
\boxed{n_0=O(3^k).}
\tag{E.24}

The five-block trapezoid has Euclidean diameter `O(n_0)`, so the same bound holds for the support radius.

---

## 7. Stage count for the quartic recurrence

From (E.20), choose `d_0,c_*>0` such that

\[
\delta(x)\ge c_*x^4
\qquad(0<x<d_0).
\tag{E.25}

Let

\[
x_{j+1}=x_j+\delta(x_j),
\qquad x_0=d.
$$

While `x_j<d_0`, comparison with the differential equation

$$
\frac{dx}{dj}=c_*x^4
$$

or the elementary integral estimate

$$
1
\le C
\int_{x_j}^{x_{j+1}}t^{-4}\,dt
$$

for small enough `x_j` gives

$$
\boxed{k_0(d)=O(d^{-3})}
\tag{E.26}

stages to reach the fixed width `d_0`.

The Kuperberg gain is weakly nondecreasing in the current gap. Once the width is at least `d_0`, every further stage gains at least the fixed positive number `delta(d_0)`. Hence only `O(1)` more stages reach paper gap width two, at which point one additional radius-one circle can be inserted.

Thus

\[
\boxed{k(d)=O(d^{-3}).}
\tag{E.27}

---

## 8. Explicit aligned support-radius upper class

Combine (E.24) and (E.27): in the paper normalization,

\[
R(d)
\le C3^{C'd^{-3}}
\le C_1\exp(C_2d^{-3}).
\tag{E.28}

The canonical repository normalization has nearest-neighbor center distance one, so paper gap `d_p` corresponds to canonical gap

\[
d_c=\frac{d_p}{2}
$$

and all support radii are divided by two. Absorbing the fixed factors into constants gives:

> **Theorem E.1 (explicit Kuperberg support exponent).** For the aligned triangular-lattice gap packing in canonical Section 150, there exist constants
> 

$$

> C_1,C_2,d_*>0
> 
$$


> such that
> 

$$

> \boxed{
> W(d)\le C_1\exp(C_2d^{-3})
> \qquad(0<d<d_*).
> }
> \tag{E.29}

For reference, the explicit canonical one-step gain obtained by scaling (E.19) is

\[
\boxed{
\delta_{\rm can}(d)
=\frac12\delta(2d)
=\frac{\sqrt3}{9}d^4+O(d^5).
}
\tag{E.30}

No claim is made that (E.29) is optimal among all finite rearrangements. It is an upper bound obtained from the published five-block architecture.

---

## 9. Fixed-shape vanishing-strain consequence

Canonical Section 150 takes a fixed full-dimensional triangular-lattice polygon `K`, with

\[
r\mathbb B\subset K,
$$

and an accumulated homothetic strain `alpha_L>0`. The row split produces canonical aligned gap width

$$
d_L=r\alpha_L.
$$

Canonical (150.4) says that the desired same-hull add-one conclusion follows if

$$
W(r\alpha_L)=o(L).
$$

Theorem E.1 gives

$$
\log W(r\alpha_L)
\le O(1)+C r^{-3}\alpha_L^{-3}.
$$

Therefore:

> **Corollary E.2 (explicit vanishing accumulated-strain regime).** If
> 

$$

> \boxed{
> \alpha_L^{-3}=o(\log L),
> }
> \tag{E.31}
> 
$$


> then
> 

$$

> \boxed{
> \alpha_1(H_{L,\alpha_L})
> \ge |P_L|+1
> }
> \tag{E.32}
> 
$$


> for all sufficiently large `L`.

This strictly extends canonical Theorem 148.1 from fixed positive accumulated strain to a concrete vanishing-strain class.

It does **not** reach power-law accumulated strain `alpha_L=L^{-beta}` for any fixed `beta>0`, because (E.29) is still stretched exponential.

---

## 10. Audit against canonical warnings

### Witness-cardinality divergence

There is no conflict with Section 146:

$$
\kappa_*(d)\to\infty.
$$

The support bound (E.29) also diverges rapidly as `d downarrow0`. The exact five-block mechanism indeed requires an increasing number of nested stages.

### No unsupported literature rate

The original paper does not state (E.19), (E.23), or (E.29). They are new deductions from its explicitly stated lattice, block sizes, movement directions, and repeat-with-smaller-block architecture. The proof above gives the missing arithmetic rather than attributing the rate to the paper.

### Exterior compatibility remains open

The rearrangement uses a free triangular-lattice block cut from an aligned gap packing. A genuine Target A monomer domain may have source/scaffold points immediately outside the selected block. The proof above does not show those exterior blockers stay clear during the three moves.

Thus this theorem advances the **quantitative support** route but does not solve the higher-priority exterior-compatible gap-concentration theorem.

### Activation regressions

Sections 152 and 153 are orthogonal. No activation-rank-to-Schur or positive-KKT-load implication is used.

---

## 11. Relation to the two preceding quantitative reports

This report supersedes their unknown-exponent conclusions for the actual published five-block mechanism.

- `quantitative_kuperberg_support_rate_2026-08-30.md` proved that finite algebraicity would force some asymptotic upper class but left a rational exponent `q` unspecified.
- `quantitative_kuperberg_rate_refinement_2026-08-30.md` split the resulting support rate according to whether `q<1`, `q=1`, or `q>1`.
- The exact coordinate calculation here gives
  $$
  \boxed{q=4}
  $$
  for the specific three-move Kuperberg mechanism and therefore the concrete support exponent `d^{-3}` in (E.29).

The semialgebraic reports remain useful as an audit trail and as a method that would apply to variants of the block mechanism, but they are no longer the strongest rate statement.

---

## 12. Highest-value next lemma

The remaining gap is now geometric rather than quantitative in the free model.

> **Exterior-compatible Kuperberg embedding lemma.** Let a genuinely derived Target A monomer region contain an aligned gap corridor of width `d`. Prove that it contains a radius
> 

$$

> R\ge C_1\exp(C_2d^{-3})
> 
$$


> subregion on which the nested five-block moves above can be executed while every exterior source/scaffold point remains at distance at least one throughout; or replace this support requirement by a stronger protected finite rearrangement.

A proof of this statement at an actual canonical gap scale with `R=o(D)` would feed directly into the strict smaller-diameter replacement route.

A separate route is to improve the block architecture itself. The quartic bottleneck is now explicit:

$$
\text{outer vertical move}
\Rightarrow u=\Theta(d^2)
\Rightarrow v=\Theta(u^2)=\Theta(d^4).
$$

Any alternative finite block mechanism that creates a **linear** or **quadratic** final gap gain would dramatically reduce the support cost. This is now a concrete finite geometric design problem.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact new Kuperberg calculation (paper normalization, center distance 2):

Use a coordinate realization of the five blocks from Figures 3--4. After moving the
outer Delta_n blocks down by the full gap d, the only controlling second-stage
nearest-neighbor margin is

    F_d(u)=u^2-(2sqrt(3)+d)u+d^2.

Hence the maximal continuous diagonal move is the small root

    phi(d)=[2sqrt(3)+d-sqrt((2sqrt(3)+d)^2-4d^2)]/2
          = d^2/(2sqrt(3)) - d^3/12 + O(d^4).

After that, the controlling middle-block margin is

    G_u(v)=v^2-(2sqrt(3)-u)v+u^2,

so the maximal upward move is the small root

    psi(u)=[2sqrt(3)-u-sqrt((2sqrt(3)-u)^2-4u^2)]/2.

Thus the explicit local gap gain is

    delta(d)=psi(phi(d))
            = (sqrt(3)/72)d^4 -(1/72)d^5 + O(d^6).

So the published mechanism has exact Puiseux exponent q=4.

Exact nesting:
a size-m five-block trapezoid fits along the base of the moved middle Delta_{n-1}
block whenever 3m <= n-2. Therefore k stages need block size O(3^k).

Quartic recurrence needs O(d^-3) stages to reach fixed gap width. Hence in the
canonical center-distance-1 normalization

    W(d) <= C1 exp(C2 d^-3).

Fixed-shape consequence:

    alpha_L^-3 = o(log L)

is sufficient for the Section-150 same-hull add-one conclusion.

Still missing:
protect the nested finite rearrangement against exterior blockers in a genuine Target A
monomer domain, or invent a finite block mechanism with a lower-order gap bottleneck.
```
