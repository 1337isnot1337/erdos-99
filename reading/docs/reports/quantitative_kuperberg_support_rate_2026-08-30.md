> Generated reading edition · [exact source](../../../docs/reports/quantitative_kuperberg_support_rate_2026-08-30.md) · source SHA-256 `d0c3ba237fe3bb8a94628cd470c467c5fd59d2925f103f556499a8b3ba48b947`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-A54588101FAD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — semialgebraic Kuperberg gain and stretched-exponential support bound

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`, through active v1.7.3 / Section 153
**Run type:** literature-to-theorem / quantitative finite witness
**Target:** A, quantitative gap-support route
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.3_FINAL_CONTINUATION_PROMPT.md`
**External web search:** used; exact imported statements are recorded below
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Section 150 isolates a precise quantitative hole in the Kuperberg gap-defect route. For the aligned triangular-lattice gap packing, the checked literature previously gave only

```math
W(d)<\infty\qquad(d>0),
```

with no asymptotic upper rate as `d downarrow 0`.

This report proves the first such rate from the actual Kuperberg--Kuperberg--Kuperberg block construction:

```math
\boxed{
W(d)\le C_1\exp\!\left(C_2d^{-q}\right)
\qquad(0<d<d_0)
}
\tag{QK.1}
```

for some constants `C_1,C_2,d_0>0` and some rational `q>0`.

The exponent is not numerically optimized. The point is the **functional class**: the support radius is at most stretched exponential in a reciprocal power of the gap. The proof has two inputs that were not exploited in Section 150:

1. the one-step five-block displacement problem is semialgebraic of fixed complexity, so its positive gain cannot be flatter than every power of `d`;
2. the paper's repeated smaller-block construction can be nested with a fixed geometric shrink ratio, so `k` widening stages require only exponentially large initial block size.

As a consequence, the free fixed-shape same-hull add-one theorem extends to a genuine vanishing accumulated strain regime:

```math
\boxed{
\alpha_L^{-q}=o(\log L)
\Longrightarrow
\alpha_1(H_{L,\alpha_L})\ge |P_L|+1
}
\tag{QK.2}
```

for all sufficiently large `L` in the notation of Section 150.

This does **not** yet handle exterior blockers of an embedded source/scaffold monomer domain, so it does not close Target A.

---

## 1. Normalizations

Kuperberg--Kuperberg--Kuperberg use unit **circles**, hence nearest-neighbor center distance `2`. Their aligned honeycomb lattice is

```math
\mathcal C=
\{(2i+j,\sqrt3j):i,j\in\mathbb Z\}.
```

For paper gap width `D_g>0`, the centers on or above the horizontal lattice line are shifted by `(0,D_g)`.

The canonical Section 150 normalization has minimum center separation `1`. Scaling all Kuperberg coordinates by `1/2` sends

```math
D_g=2d
```

to canonical gap width `d`. A support-radius bound of the form `exp(C D_g^{-q})` therefore gives the same form `exp(C' d^{-q})` after rescaling.

Throughout the proof below we work first in the paper normalization and rescale at the end.

---

## 2. Exact Kuperberg one-step mechanism

Section 2.1 of

> Greg Kuperberg, Krystyna Kuperberg, Włodzimierz Kuperberg, “Lattice Packings with Gap Defects Are Not Completely Saturated,” *Beiträge zur Algebra und Geometrie* 45 (2004), 267--273; arXiv:math/0303366

uses five rigid triangular blocks. For block parameter `n` these are two `Delta_n` blocks, two `nabla_n` blocks, and one middle `Delta_{n-1}` block forming a trapezoid. The three moves are:

1. move the two outer `Delta_n` blocks down by `d_1 <= D_g`;
2. move the two `nabla_n` blocks along directions at 60 degrees from vertical by `d_2`;
3. move the middle block vertically up by `d_3`.

The paper chooses `d_1,d_2,d_3` to maximize the last motion, observes that increasing the original gap relaxes the constraints, and obtains a positive gap increment `delta(D_g)` which is weakly nondecreasing in `D_g`. It then states that `n` is arbitrary and can be chosen large enough to repeat the same operation with smaller blocks until the gap reaches any prescribed fixed width. In the three-dimensional analogue the authors explicitly summarize the same feature as “as before, `delta` does not depend on `n`,” confirming that `n` is a support-size parameter rather than part of the local gain calculation.

The original proof does not give an asymptotic formula for `delta(D_g)`.

---

## 3. The one-step gain is semialgebraic

The missing rate is already constrained strongly by the finite geometry of the five-block move.

> **Lemma QK.1 (semialgebraic one-step gain).** There is `D_0>0` such that the maximal Kuperberg one-step gain
> 

```math
> \delta:(0,D_0)\to(0,\infty)
> 
```
> for the aligned five-block mechanism is a semialgebraic function.

### Proof

Fix a sufficiently large block parameter `n_0` for one instance of the five-block move. The old center coordinates in the gap packing are affine functions of the gap parameter `D_g`, with coefficients in the real algebraic field `Q(sqrt(3))`. After the prescribed rigid block translations, every moved center coordinate is affine in

```math
(D_g,d_1,d_2,d_3).
```

For any two centers whose block labels are fixed, the non-overlap condition is therefore a quadratic polynomial inequality

```math
|p_i(D_g,d_1,d_2,d_3)-p_j(D_g,d_1,d_2,d_3)|^2\ge4.
\tag{QK.3}
```

The same is true for a moved center versus an unmoved exterior center. Although the original packing is infinite, only finitely many exterior centers can matter for this fixed finite move, uniformly for small `D_g`. Indeed, the perfect center lattice has covering radius `2/sqrt(3)`. The gap packing has covering radius at most

```math
\frac2{\sqrt3}+D_g.
```

Choose

```math
0<D_0<2-\frac2{\sqrt3}.
```

Then this covering radius is strictly below `2`. If a final moved center were outside a bounded neighborhood of the old five-block support, a nearest old gap-packing center at distance below `2` would be an **unmoved** center, contradicting non-overlap. Hence every feasible translated block lies in one bounded region depending only on the fixed one-step support and `D_0`. Only finitely many unmoved lattice centers lie within distance `2` of that region, and all other inequalities are automatic.

Consequently the feasible parameter set

```math
\mathcal F\subset
(0,D_0)\times\mathbb R^3
```

is given by finitely many polynomial inequalities, together with `0<=d_1<=D_g` and the fixed direction conditions. If one insists that the three translations remain a packing throughout the sequential motion, the intermediate motion parameter can be universally quantified over a compact interval; Tarski--Seidenberg eliminates that quantifier and the resulting feasible set is still semialgebraic. Final-position feasibility alone is already enough for a finite packing rearrangement.

The local widened-gap condition beneath an interior segment of the vertically translated middle block is likewise a finite system of affine/quadratic inequalities. The Kuperberg proof establishes a feasible point with positive gain for every `D_g>0`.

Because the feasible motions are bounded, the maximum final vertical gain is attained. Its graph can be written by the first-order formula

```math
\begin{aligned}
(D_g,z)\in\operatorname{graph}\delta
\iff{}&
\exists(d_1,d_2,d_3)
\,[\mathcal F(D_g,d_1,d_2,d_3)\wedge z=d_3]\\
&\wedge\neg\exists(d'_1,d'_2,d'_3)
\,[\mathcal F(D_g,d'_1,d'_2,d'_3)\wedge d'_3>z].
\end{aligned}
\tag{QK.4}
```

Equivalently one may use the actual affine widened-gap functional if its notation is kept distinct from `d_3`; the argument is identical. Tarski--Seidenberg implies that (QK.4) is semialgebraic. This proves the lemma. $`\square`$

### Uniformity in the block parameter

The gain is a local interface quantity. Once `n` exceeds the fixed number of rows required to realize all corner/interface types, enlarging `n` only repeats straight lattice-edge neighborhoods. The possible relative lattice vectors that can become shorter than `2` under the bounded translations form a fixed finite set. Hence the same feasible displacement inequalities and the same maximal gain apply for every sufficiently large block parameter. This is the finite-constraint content behind the paper's statement that the parameter `n` is arbitrary and is used only to permit repetition; the later 3D discussion explicitly says that, “as before,” the gain does not depend on `n`.

---

## 4. Semialgebraicity forces a power-law one-step gain

We use two standard facts from semialgebraic geometry.

1. **Tarski--Seidenberg / semialgebraic choice.** Projections of semialgebraic sets are semialgebraic, and a nonempty semialgebraic fiber relation admits a semialgebraic selection. A convenient explicit statement is Yehuda John Levy, “Uniformly Supported Approximate Equilibria in Families of Games,” *Journal of Mathematical Economics* 98 (2022), Theorem 2.3.
2. **Growth dichotomy.** If `f:(0,epsilon)->R` is semialgebraic and nowhere zero, then
   ```math
   f(t)=a t^q+o(t^q)
   
   ```
   for some `a != 0` and rational `q`. One explicit statement is Jae Hyoung Lee and Tien-Son Pham, “Openness, Hölder Metric Regularity and Hölder Continuity Properties of Semialgebraic Set-Valued Maps,” Lemma 2.2.

> **Theorem QK.2 (power-law Kuperberg gain).** There are constants
> 

```math
> c_*>0,
> \qquad
> q\in\mathbb Q_{>0},
> \qquad
> D_*\in(0,D_0)
> 
```
> such that
> 

```math
> \boxed{
> \delta(D_g)\ge c_*D_g^q
> \qquad(0<D_g<D_*).
> }
> \tag{QK.5}
```

### Proof

By Lemma QK.1, `delta` is semialgebraic. The Kuperberg construction gives

```math
\delta(D_g)>0
\qquad(D_g>0).
```

The feasible translations are uniformly bounded on `(0,D_0)`, so `delta` is bounded there. Growth dichotomy gives

```math
\delta(D_g)
=aD_g^q+o(D_g^q)
```

with `a>0` and `q in Q_{>=0}`. Shrink `D_*` so that

```math
\delta(D_g)\ge\frac a2D_g^q.
```

This proves (QK.5) with `c_*=a/2`.

In fact `q` cannot be zero. If `q=0`, the one-step gain would stay bounded below by a positive constant as `D_g downarrow 0`; the nesting argument in the next section would then give positive-gain witnesses with uniformly bounded support as the gap closes. After scaling, this contradicts canonical Theorem 146.1, which proves that the number of deleted old centers in every positive-gain witness diverges as `d downarrow 0`. Thus `q>0`. $`\square`$

The theorem is qualitative in its exponent but quantitatively nontrivial: it rules out gains such as `exp(-1/D_g)` or any other super-polynomially flat behavior.

---

## 5. Quantifying the repeated smaller-block construction

The paper says to choose `n` large enough to repeat the five-block move with smaller blocks. The needed support growth can be bounded without determining the optimal nesting.

Represent an upward triangular lattice block of size `N` in lattice coordinates as

```math
T_N=
\{ie_1+je_2:
 i,j\ge0,\ i+j\le N-1\},
```

with `|e_1|=|e_2|=2` in the paper normalization. A five-block template of parameter `m` is a union of five triangular patches whose lattice-coordinate extents are affine-linear in `m`. Therefore its total horizontal and vertical lattice-coordinate spans are at most

```math
A_0m+B_0
```

for fixed constants `A_0,B_0`, independent of `m` and of the gap width. All actual rigid translations used while the target gap remains at most `2` are bounded by another fixed constant and can be absorbed into `B_0`.

The middle upward block produced by one stage is still a rigid translate of a perfect triangular block of size `N-1`, and the widened gap lies along its base. A basal subtriangle of `T_{N-1}` whose distance from the two sloping sides is a fixed positive fraction of `N` has both width and height `Theta(N)`. Hence:

> **Lemma QK.3 (uniform nesting).** There are integers
> 

```math
> A\ge2,
> \qquad B\ge0,
> 
```
> such that whenever
> 

```math
> N\ge Am+B,
> \tag{QK.6}
> 
```
> the widened middle `Delta_{N-1}` block contains, along an interior portion of its base and with all relevant exterior-neighbor rows present, a translated copy of the complete five-block template of parameter `m` for the next widening stage.

### Proof

The five child blocks and the fixed number of neighboring lattice rows needed to certify non-overlap have lattice-coordinate diameter at most `A_0m+B_0`. The parent triangle `T_{N-1}` contains along its base a trapezoidal lattice region of width and height proportional to `N`; for example, after discarding fixed-fraction neighborhoods of the two sloping sides, the remaining basal region has both dimensions at least `cN-O(1)` for an absolute `c>0`. Choose `A>A_0/c` and then `B` large enough to absorb the fixed margins and the bounded rigid translations. The child template then fits by a lattice translation.

Because it is kept beyond the fixed interaction margin from the parent side boundaries, every unmoved neighboring circle relevant to the child move is exactly the same as in the infinite aligned gap packing. The parent middle block is a rigid translate, so its internal triangular-lattice coordinates are unchanged. Thus the next five-block move has precisely the same local constraints and gain function. $`\square`$

Iterating (QK.6) backward, `k` widening stages fit inside an initial block parameter

```math
N_0\le C_AA^k
\tag{QK.7}
```

for a constant `C_A`. The Euclidean support radius of the complete nested rearrangement is therefore

```math
R_k\le C_RA^k.
\tag{QK.8}
```

This is intentionally conservative. The proof needs only a fixed shrink ratio, not an optimal one.

---

## 6. Number of widening stages

Let the initial paper-normalized gap be `D_g<D_*`, and define the successive widths

```math
D_{j+1}=D_j+\delta(D_j).
```

As long as `D_j<D_*`, Theorem QK.2 and `D_j>=D_g` give

```math
D_{j+1}-D_j
\ge c_*D_j^q
\ge c_*D_g^q.
```

Hence the number of stages required to reach `D_*` is at most

```math
k_1(D_g)
\le
1+\frac{D_*}{c_*D_g^q}
=O(D_g^{-q}).
\tag{QK.9}
```

The original Kuperberg proof observes that the maximal gain is weakly nondecreasing in the gap width. Once the gap is at least the fixed positive number `D_*`, every further stage gains at least the fixed amount `delta(D_*)>0`. Therefore only a fixed additional number `k_2=O(1)` of stages is needed to reach gap width `2`, at which point one additional unit circle fits.

Thus

```math
\boxed{k(D_g)=O(D_g^{-q}).}
\tag{QK.10}
```

---

## 7. Stretched-exponential support radius

Combine (QK.8) and (QK.10):

```math
R(D_g)
\le
C_RA^{C D_g^{-q}}
\le
C_1\exp(C_2D_g^{-q}).
\tag{QK.11}
```

At the final stage the local gap has width at least `2`, so the Kuperberg construction inserts one additional unit circle. No old circles were deleted merely to perform the two-dimensional widening stages; they were partitioned into and translated as rigid finite blocks. Thus the operation gives a finite positive-gain witness supported in the same radius bound.

Rescale center distances by `1/2`. Canonical gap width `d` corresponds to `D_g=2d`, and support radii scale by `1/2`. Absorbing fixed factors into the constants gives:

> **Theorem QK.4 (stretched-exponential aligned support bound).** For the aligned unit-triangular-lattice gap packing used in Sections 148 and 150, there exist constants
> 

```math
> C_1,C_2,d_0>0,
> \qquad q\in\mathbb Q_{>0},
> 
```
> such that
> 

```math
> \boxed{
> W(d)\le C_1\exp(C_2d^{-q})
> \qquad(0<d<d_0).
> }
> \tag{QK.12}
```

This is the first audited asymptotic upper class for `W(d)` obtained from the Kuperberg proof. It is compatible with the canonical lower-complexity theorem `kappa_*(d)->infinity`.

### Scope

The theorem is for the **lattice-line aligned gap** used by the row-split construction in Section 148. This is exactly the direction needed for canonical (150.3)--(150.4). The arbitrary-line reduction of Kuperberg Section 2.2 is not needed here and no rate for that preliminary reduction is claimed.

---

## 8. New vanishing-strain same-hull theorem

Return to Section 150. Let `K` be a fixed full-dimensional convex triangular-lattice polygon with

```math
r\mathbb B\subset K,
```

and let accumulated homothetic strain `alpha_L>0` tend to zero. The row split creates an aligned gap

```math
d_L=r\alpha_L.
```

Canonical (150.4) says that it is enough to have

```math
W(r\alpha_L)=o(L).
```

Theorem QK.4 gives

```math
\log W(r\alpha_L)
\le
O(1)+C_2r^{-q}\alpha_L^{-q}.
```

Therefore if

```math
\boxed{
\alpha_L^{-q}=o(\log L),
}
\tag{QK.13}
```

then

```math
W(r\alpha_L)
=\exp(o(\log L))
=L^{o(1)}
=o(L).
```

Hence:

> **Corollary QK.5 (vanishing accumulated strain closure for fixed shape).** There exists a rational `q>0`, depending only on the fixed Kuperberg local mechanism, such that for every fixed full-dimensional convex triangular-lattice polygon `K` and every positive sequence `alpha_L` satisfying
> 

```math
> \alpha_L^{-q}=o(\log L),
> 
```
> the hull of
> 

```math
> \left(1+\frac{\alpha_L}{L}\right)(\Lambda\cap LK)
> 
```
> contains a unit-separated set with one additional point for all sufficiently large `L`.

This strictly extends Theorem 148.1, which handled fixed positive accumulated strain. It does **not** assert anything for strains decaying as a power of `L`, and it still does not protect the rearrangement from exterior blockers in an embedded source/scaffold monomer domain.

---

## 9. Regression and hypothesis audit

| Regression / issue | Result | Exact reason |
| --- | --- | --- |
| Canonical `kappa_*(d)->infinity` | passed | The new upper bound diverges as `d downarrow 0`; it does not predict bounded witnesses. It also forces the semialgebraic gain exponent `q` to be positive. |
| No invented explicit Kuperberg formula | passed | No formula for `d_1,d_2,d_3` is assumed. The only new input is semialgebraicity of the finite quadratic feasibility problem. |
| Block-size parameter absent from local gain | passed | This is exactly the role assigned to `n` in Kuperberg §2.1; the later 3D analogue explicitly says that, “as before,” the gain is independent of `n`. |
| Distributed strain with exterior locking | not solved | QK.4 concerns the free aligned gap packing. An embedded domain can still be blocked by exterior source/scaffold points. |
| Fixed-shape same-hull regression | strengthened | Corollary QK.5 now covers a nontrivial vanishing accumulated strain regime. |
| Section 152 activation/monomer regression | irrelevant | No activation-rank-to-nullity implication is used. |
| Section 153 zero-KKT-load theorem | irrelevant | No KKT stress weight on activation edges is used. |
| Arbitrary gap direction | not claimed | The canonical row split is aligned; §2.2 arbitrary-line quantitative reduction is unnecessary for this theorem. |

---

## 10. Literature imported

### Kuperberg--Kuperberg--Kuperberg 2004

- Source: arXiv:math/0303366; *Beiträge zur Algebra und Geometrie* 45 (2004), 267--273.
- Exact part used: §2.1.
- Hypotheses: honeycomb/triangular circle packing, positive linear gap along a lattice line.
- Construction: five triangular blocks; three scalar rigid translations; positive gap widening; gain weakly nondecreasing in the original gap; block size arbitrary and large enough for repeated smaller-block widening.
- Exact use here: identifies a fixed finite algebraic displacement mechanism and the nested self-similar support architecture.

### Semialgebraic selection / Tarski--Seidenberg

- Convenient statement: Yehuda John Levy, “Uniformly Supported Approximate Equilibria in Families of Games,” *Journal of Mathematical Economics* 98 (2022), Theorem 2.3.
- Exact statement used: projection of a semialgebraic set is semialgebraic; semialgebraic fiber relations admit semialgebraic selections.
- Use here: the optimizer/positive-gain branch of the finite Kuperberg displacement problem is semialgebraic.

### Growth dichotomy

- Convenient statement: Jae Hyoung Lee and Tien-Son Pham, “Openness, Hölder Metric Regularity and Hölder Continuity Properties of Semialgebraic Set-Valued Maps,” Lemma 2.2.
- Exact statement used: a nowhere-zero one-variable semialgebraic function has asymptotic form `a t^q + o(t^q)` for rational `q`.
- Use here: converts positivity of the Kuperberg gain into the power-law lower bound (QK.5).

These are general semialgebraic facts, not subject-specific packing assumptions.

---

## 11. Exact Target A consequence

The quantitative gap-support item in the active v1.7.3 prompt is no longer wholly open for the aligned gap:

old status:

```math
W(d)<\infty\quad(d>0),
\qquad
\text{no asymptotic upper rate};
```

new status:

```math
\boxed{
W(d)\le C_1\exp(C_2d^{-q})
}
```

for some rational `q>0`.

This does **not** close the actual embedded monomer branch. The exact remaining geometric lemma is now sharper:

> **Exterior-compatible support lemma.** Show that a monomer region produced by the genuine source/scaffold geometry contains, after deleting/protecting only the exact boundary-order obstruction set, an aligned gap corridor of width `d` and radius at least
> 

```math
> C_1\exp(C_2d^{-q}),
> 
```
> or prove a stronger finite replacement directly.

The stretched-exponential scale is large, so this may still be too expensive for the actual vanishing gap generated by Target A. But the previous undefined function `W(d)` has been replaced by a concrete asymptotic class.

---

## 12. Promotion recommendation

**Promote after independent audit.**

If the semialgebraic and nesting arguments survive review, the natural canonical edit is a new post-Section-153 Target A addendum that:

1. replaces the “no upper rate for `W(d)`” sentence in Sections 150--151 by Theorem QK.4;
2. adds Corollary QK.5 as the exact fixed-shape vanishing-strain consequence;
3. updates the active continuation prompt so quantitative-gap work targets exterior compatibility or a rate better than stretched exponential, rather than asking merely for any rate.

No change to the exact Schur endpoint is warranted.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New quantitative theorem:
The Kuperberg aligned five-block widening problem is a fixed finite quadratic
semialgebraic optimization in the gap width d. Its positive one-step gain delta(d) is
therefore semialgebraic. Growth dichotomy gives

    delta(d) >= c d^q

for some rational q>0 and small d.

The paper's repeated-smaller-block architecture has a fixed geometric nesting ratio:
a parent triangular block of size N contains the next five-block template of size m
whenever N >= A m + B. Thus k widening stages require support radius O(A^k).
Since O(d^-q) stages reach a fixed gap and only O(1) more reach insertion width,

    W(d) <= C1 exp(C2 d^-q).

This is the first asymptotic upper class for the canonical aligned support radius W(d).

Fixed-shape consequence:
If accumulated homothetic strain alpha_L -> 0 but

    alpha_L^-q = o(log L),

then W(r alpha_L)=o(L), so canonical (150.4) gives a same-hull add-one packing for
all sufficiently large L.

Still missing:
The actual Target A monomer domain has exterior blockers. Need an exterior-compatible
gap corridor/support theorem, or a stronger rate/finite replacement. The exact Schur
endpoint remains open.
```
