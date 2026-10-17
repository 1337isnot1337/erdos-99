> Generated reading edition · [exact source](../../../docs/reports/quantitative_kuperberg_rate_refinement_2026-08-30.md) · source SHA-256 `54c28ac8710295156a0f189e79b177b381a122dcb1ee7b336247e72a499aecee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6865F655759A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — refinement of the semialgebraic Kuperberg support rate

**Date:** 2026-08-30
**Repository state:** `research/bhs-scale-activation-regression-2026-08-30`
**Run type:** audit / quantitative refinement
**Target:** A, quantitative gap-support route
**Depends on:** `quantitative_kuperberg_support_rate_2026-08-30.md`

## LEVEL I STATUS

`STILL OPEN`

This note corrects one overly coarse estimate in the preceding quantitative Kuperberg report and records the sharper rate that follows from the same proved inputs.

The preceding report proves that the one-step aligned-gap gain is semialgebraic and hence, for some

$$
a>0,
\qquad q\in\mathbb Q_{>0},
$$

has

$$
\delta(d)=a d^q+o(d^q)
\qquad(d\downarrow0).
\tag{R.1}
$$

It then used the crude bound `k(d)=O(d^{-q})` on the number of widening stages. That bound is valid but loses a full power, or much more, because the current gap itself grows after every stage.

The correct stage count has three regimes.

---

## 1. Refined iteration theorem

Fix small `d_* > 0` and shrink it if needed so that

$$
\delta(x)\ge c x^q
\qquad(0<x<d_*)
\tag{R.2}
$$

for some `c>0`. Define the widening recurrence

$$
x_0=d,
\qquad
x_{j+1}\ge x_j+c x_j^q
\tag{R.3}
$$

until `x_j >= d_*`. Once `d_*` is reached, Kuperberg monotonicity gives only `O(1)` additional stages to reach insertion width.

> **Theorem R.1 (three-regime stage count).** As `d downarrow 0`, the number `k(d)` of Kuperberg widening stages needed to reach a fixed positive gap satisfies
> 

$$

> \boxed{
> k(d)=
> \begin{cases}
> O(\log\log(1/d)), & 0<q<1,\\[1mm]
> O(\log(1/d)), & q=1,\\[1mm]
> O(d^{-(q-1)}), & q>1.
> \end{cases}
> }
> \tag{R.4}

### Case `0<q<1`

For sufficiently small `x`,

\[
c x^{q-1}\ge1.
$$

Hence (R.3) gives

$$
x_{j+1}\ge c x_j^q.
\tag{R.5}
$$

Put

$$
z_j=\log\frac1{x_j}.
$$

Then

$$
z_{j+1}
\le qz_j+\log\frac1c.
\tag{R.6}
$$

Iterating,

$$
z_j
\le
q^jz_0+
\frac{\log(1/c)}{1-q}
\tag{R.7}
$$

with the obvious harmless modification if `c>=1`. Choose `j` so that `q^j z_0=O(1)`. Since

$$
j=
O(\log z_0)
=O(\log\log(1/d)),
$$

the gap reaches a fixed positive threshold in that many stages.

### Case `q=1`

Equation (R.3) gives

$$
x_{j+1}\ge(1+c)x_j,
$$

so

$$
x_j\ge(1+c)^jd.
$$

Thus `j=O(log(1/d))` reaches `d_*`.

### Case `q>1`

While

$$
c x_j^{q-1}\le1,
$$

we have

$$
x_{j+1}\le 2x_j
$$

for the comparison sequence with equality increment `c x_j^q`; any larger actual Kuperberg gain only reduces the number of stages. For such a step, every `t in [x_j,x_{j+1}]` satisfies `t<=2x_j`, hence

$$
x_j^{-q}
\le
2^q t^{-q}.
$$

Using

$$
1
\le
\frac{x_{j+1}-x_j}{c x_j^q},
$$

we get

$$
1
\le
\frac{2^q}{c}
\int_{x_j}^{x_{j+1}}t^{-q}\,dt.
\tag{R.8}
$$

Summing until a fixed positive threshold gives

$$
k(d)
\le
O(1)+
\frac{2^q}{c}
\int_d^{d_*}t^{-q}\,dt
=O(d^{1-q}).
\tag{R.9}
$$

This is `O(d^{-(q-1)})`, proving (R.4). $\square$

---

## 2. Refined support-radius classes

The preceding report's conservative nesting lemma gives a fixed `A>1` and `C>0` such that `k` widening stages can be realized in support radius

$$
R_k\le C A^k.
\tag{R.10}
$$

Substituting Theorem R.1 yields:

> **Corollary R.2 (support rate by semialgebraic exponent).** For sufficiently small aligned unit-separation gap width `d`,
> 

$$

> \boxed{
> W(d)\le
> \begin{cases}
> C_1\,[\log(1/d)]^{C_2}, & 0<q<1,\\[1mm]
> C_1 d^{-C_2}, & q=1,\\[1mm]
> C_1\exp\!\bigl(C_2d^{-(q-1)}\bigr), & q>1.
> \end{cases}
> }
> \tag{R.11}

The constants can change from line to line and absorb the paper-to-canonical factor-two scaling.

This strictly strengthens the uniform coarse bound

\[
W(d)\le C_1\exp(C_2d^{-q})
$$

from the preceding report.

### Audit correction: `q<1` is not excluded by witness-complexity divergence

An intermediate scratch argument incorrectly suggested that `q<1` would make the number of widening stages uniformly bounded. Equation (R.7) shows the correct behavior:

$$
k(d)=O(\log\log(1/d))\to\infty.
$$

Therefore the canonical theorem

$$
\kappa_*(d)\to\infty
$$

does **not** rule out `q<1`. The support bound in that regime is polylogarithmic but still diverges, so there is no conflict with Section 146.

No lower bound such as `q>=1` is claimed.

---

## 3. Refined fixed-shape vanishing-strain regimes

Canonical (150.4) only needs

$$
W(r\alpha_L)=o(L).
$$

Corollary R.2 therefore gives different sufficient conditions according to the unknown rational gain exponent.

### If `0<q<1`

It suffices that

$$
\boxed{
[\log(1/\alpha_L)]^{C_2}=o(L).
}
\tag{R.12}

Thus the free fixed-shape theorem tolerates strains much smaller than any inverse power of `log L`; the exact allowable rate depends on the support exponent `C_2` coming from the nesting constant.

### If `q=1`

It suffices that

\[
\boxed{
\alpha_L^{-C_2}=o(L).
}
\tag{R.13}

Hence a nontrivial range of power-law accumulated strains

\[
\alpha_L=L^{-\beta}
$$

is covered whenever

$$
\beta C_2<1.
$$

### If `q>1`

It suffices that

$$
\boxed{
\alpha_L^{-(q-1)}=o(\log L).
}
\tag{R.14}

This improves the exponent `q` in the preceding report's sufficient logarithmic condition to `q-1`.

These are free fixed-shape consequences only. None protects an embedded witness from exterior blockers.

---

## 4. Highest-value quantitative subproblem

The semialgebraic argument reduces the remaining rate ambiguity to a finite local quantity:

\[
\boxed{
q=\operatorname{ord}_{d=0}\delta(d)
}
$$

in the Puiseux expansion of the five-block one-step gain.

Determining whether

$$
q<1,
\qquad q=1,
\qquad\text{or}\qquad q>1
$$

would immediately decide whether the Kuperberg support produced by this construction is respectively polylogarithmic, polynomial, or stretched exponential.

This is now a finite algebraic-geometry calculation rather than an infinite-packing question: enumerate the finitely many active circle-pair constraints in the three rigid block translations, eliminate `d_1,d_2,d_3`, and compute the leading Puiseux exponent of the maximal feasible `d_3` (or the exact local gap-gain functional).

That is the next quantitative task.

---

## 5. Compact handoff

```text
Correction/refinement to quantitative Kuperberg report:

If the semialgebraic one-step gain is

    delta(d) ~ a d^q,  q>0 rational,

then the widening-stage count is not merely O(d^-q). It is

    O(log log(1/d))   if 0<q<1,
    O(log(1/d))       if q=1,
    O(d^{-(q-1)})     if q>1.

With conservative nested-block support R_k <= C A^k, this gives

    W(d) <= polylog(1/d)                  if q<1,
    W(d) <= d^{-C}                        if q=1,
    W(d) <= exp(C d^{-(q-1)})             if q>1.

Do NOT claim q>=1: Section 146 does not exclude q<1 because log-log many stages still
give diverging witness support/cardinality.

Highest-value next calculation:
Determine the Puiseux order q of the finite five-block displacement optimization.
```
