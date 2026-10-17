> Generated reading edition · [exact source](../../../../docs/targets/target-c/105-optimized-quantitative-phase-gap-audit.md) · source SHA-256 `94d1315e481a795b0417c3118d33935eab32a46b2f110a8c1f38cd6914145e45`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DE228C892A14","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — optimized quantitative phase/corridor gap

**Date:** 2026-09-12
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**
**Status:** proved candidate, proof-only pending independent hostile audit/promotion.

Proof-only Section 104 makes the qualitative Section-102 carrier gap explicit by
transporting the Section-101 scalar slack

```math
\sigma(\theta)
:=3\theta-2\pi-\sin(\theta/2)-2\sin\theta
```

through complement-gap stability, the exact outer-walk ledger, attachment-base
packing, and the canonical Section-90 two-phase train core.  Its published constants
stop at `sigma=10^{-7}`.

Two deliberately conservative losses in Section 104 are unnecessary:

1. the **principal** route-excess budget is at most `sigma`, not
   `(19/6)sigma`; the larger factor is needed only for total nonprincipal route length;
2. the good/bad tooth cutoff can be chosen near the minimum of the explicit leakage
   expression instead of fixed at `h=0.0005`.

Keeping every other Section-104 estimate unchanged and taking

```math
\boxed{
\sigma_*:=7\times10^{-7},
\qquad
h_*:=0.0011
}
```

still leaves a comfortable phase/corridor angular contradiction.

Let `theta_10` be the unique solution above the canonical Section-101 endpoint of

```math
\boxed{
\sigma(\theta_{10})=7\times10^{-7}.
}
```

Numerically,

```math
\boxed{
\theta_{10}=2.7029081785266174\ldots,
}
```

```math
\boxed{
\mu_{10}:=\sin(\theta_{10}/2)
=0.9760407814640902\ldots .
}
```

Thus

```math
\boxed{
\mu_{10}-\mu_8
=1.6197038\times10^{-8}>0,
}
```

about seven times the explicit gain in Section 104.

---

# 105. The explicit carrier coefficient can be raised to 0.9760407814

## 105.1 Section-104 stability lemmas remain valid on the larger window

Retain all notation from proof-only Section 104.  In particular

```math
M\le C\le2\alpha\le|S|\le U,
\qquad
U-M=\sigma(\theta),
```

and the complement gaps are written

```math
g_1=\theta-\delta,
\qquad
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau=\sum_{j\ge4}g_j.
```

Assume

```math
0\le\sigma:=\sigma(\theta)\le7\times10^{-7}.
\tag{105.1}
```

The scalar derivative bound used in Section 104 is unchanged:

```math
\sigma'(\theta)
=3-\tfrac12\cos(\theta/2)-2\cos\theta
\ge{15\over4}.
```

Hence

```math
0\le\theta-\theta_8
\le{4\over15}\sigma
<1.87\times10^{-7}.
\tag{105.2}
```

The only hard-coded `10^{-7}` comparisons in the proof of the Section-104 gap-stability
lemmas had enormous room:

- the coarse `delta=0.1` majorization barrier is greater than `0.0326`;
- the derivative of the transfer function `h_theta(delta)` is greater than `0.30`
  on `0<=delta<=0.1`;
- the tail bound needed only `tau<phi`, while `phi` is about `0.877`.

All therefore remain valid under (105.1).  We retain

```math
\boxed{
0\le\delta\le{10\over3}\sigma,
}
\tag{105.3}
```

```math
\boxed{
0\le x_2,x_3,\tau\le{13\over3}\sigma,
}
\tag{105.4}
```

and the two support spans adjacent to the largest principal gap are each at most
`delta`.

The principal-corridor direction estimates also remain unchanged.  Every pair of
principal corridor directions satisfies

```math
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>m_*(\sigma),
}
\tag{105.5}
```

where it is enough to take the worst Section-104 perturbation

```math
m_*(\sigma)
:={\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
\tag{105.6}
```

At `sigma=7e-7`,

```math
\boxed{m_*>0.3042479.}
\tag{105.7}
```

## 105.2 Sharpen the principal route-excess budget

Section 104 uses the safe estimate

```math
\sum_{i=1}^3(\ell_i-f(g_i))
\le {19\over6}\sigma.
```

The exact outer-walk budget gives more.  For every fixed finite family `J` of positive
complement gaps, the Section-82 identity and the ordinary two-edge floor imply

```math
\sum_{j\in J}\ell_j\le2\alpha+o(1).
```

Pass first to the scale limit and then exhaust all positive complement components.
Monotone nonnegativity gives

```math
\sum_{j\ge1}\ell_j\le2\alpha.
\tag{105.8}
```

Every route dominates its endpoint chord:

```math
\ell_j\ge f(g_j).
```

Therefore

```math
\begin{aligned}
\sum_{i=1}^3(\ell_i-f(g_i))
&\le
\sum_{j\ge1}(\ell_j-f(g_j))\\
&\le2\alpha-C\\
&\le\sigma.
\end{aligned}
```

Thus

```math
\boxed{
\sum_{i=1}^3(\ell_i-f(g_i))\le\sigma.
}
\tag{105.9}
```

No other Section-104 leakage estimate changes.  In particular the total route length
of nonprincipal macroscopic gaps is still bounded by `(19/6)sigma`, and the
micro-route, nonquadrilateral-face, and tiny-support-span estimates remain exactly as
before.

## 105.3 Re-optimize the tooth cutoff

Let `h>0` be the excess-base cutoff for regular two-edge unloaded-apex teeth.  The
technical companion to Section 104 proves the two required finite geometric estimates:

- total micro-base excess is at most `(sigma/2)D+o(D)`;
- for good bases `1<=b<=1+h`, one inverse-phase family can use good tooth legs only
  over two base-direction windows whose combined endpoint-density contribution is at
  most
  ```math
  w(h)+{13\over3}\sigma,
  
  ```
  where
  ```math
  w(h):={\pi\over3}-\arccos((1+h)/2).
  
  ```

Bad-base teeth cost at most `(sigma/h)D` phase endpoint occurrences.  The remaining
Section-104 leakage coefficients are

```math
5+{19\over6}+9+{20\over3}+{13\over3}
={169\over6}.
```

Hence one selected phase family has at most

```math
\boxed{
L(\sigma,h)D+o(D),
\qquad
L(\sigma,h)
:=w(h)+\left({1\over h}+{169\over6}\right)\sigma
}
\tag{105.10}
```

physical train endpoints away from the three principal corridors.

Take

```math
\boxed{h=h_*:=0.0011.}
\tag{105.11}
```

Then

```math
w(h_*)
=0.0006352018\ldots .
\tag{105.12}
```

At `sigma=7e-7`,

```math
\boxed{
L(7e-7,h_*)
=0.0012912822\ldots<0.001292.
}
\tag{105.13}
```

The canonical Section-90 phase extraction, with the Section-103 area concentration,
still supplies at least

```math
E_0D,
\qquad E_0=0.001875,
```

physical endpoints in each of the two selected phase families.  Therefore more than

```math
0.001875-0.001292
>0.000583
```

endpoints per `D` remain on the union of the three principal corridors.  One corridor
therefore carries more than

```math
0.000194D
```

of those endpoints.  We may safely fix

```math
\boxed{\rho:=0.00019.}
\tag{105.14}
```

## 105.4 Improved projection alignment

Suppose a principal corridor carries at least `rho D` physical endpoints from one
selected phase family, whose limiting projective direction is `u`.  Let `q` be the
corridor chord direction and put

```math
\Delta:=\operatorname{dist}_{RP^1}(u,q).
```

Every such route-edge occurrence contributes asymptotic projection loss at least
`1-cos Delta`.  The sharpened principal route-excess budget (105.9) gives

```math
\rho(1-\cos\Delta)\le\sigma.
\tag{105.15}
```

Using

```math
1-\cos x\ge{2x^2\over\pi^2},
```

we get

```math
\boxed{
\Delta
\le\pi\sqrt{\sigma\over2\rho}.
}
\tag{105.16}
```

At `sigma=7e-7` and `rho=0.00019`,

```math
\boxed{\Delta<0.13484.}
\tag{105.17}
```

Canonical Section 90 supplies two selected phase families whose projective directions
are exactly `pi/3` apart.  They cannot use the same principal corridor, because then
their separation would be below `2Delta<0.26968<pi/3`.  Hence they use two distinct
principal corridors.

The triangle inequality would then force that corridor pair to satisfy

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|<2\Delta<0.26968.
\tag{105.18}
```

But (105.7) gives the incompatible lower bound

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>0.3042479.
```

The contradiction margin is more than `0.0345` radians.

## 105.5 Explicit optimized carrier coefficient

We have shown that the Section-104 contradiction works throughout

```math
0\le\sigma(\theta)\le7\times10^{-7}.
```

Since `sigma` is strictly increasing on the live interval, no full-core Type-II
countersequence can have all positive-area macroscopic harmonic cells of normalized
diameter at most

```math
\mu_{10}=\sin(\theta_{10}/2),
```

where `sigma(theta_10)=7e-7`.

The same finite-macroscopic-cell compactness transfer as Section 104 therefore yields
an actual locally rhombus-saturated carrier `P_*` with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760407814640902\ldots-o(1))D
}
\tag{105.19}
```

and quadratic area.

This is a constant optimization, not a new qualitative mechanism.  It is separated
from Section 104 so the conservative `sigma=1e-7` theorem can be independently audited
without moving its target.

## 105.6 Dependencies and scope

- **Canonical Sections 101 and 102:** the current explicit endpoint and the qualitative
  phase/corridor exclusion.
- **Proof-only, independently audited Section 103:** unique wrapping carrier and full
  cap-deficit area concentration.
- **Proof-only Section 104 plus its non-numbered technical companion:** quantitative
  complement-gap stability, micro-route/base leakage, convex direction-window bound,
  and explicit Section-90 endpoint count.
- **New input in Section 105:** only the exact all-macro-route excess deduction
  (105.8)--(105.9) and the re-optimized base cutoff.
- **No theorem-state mutation.**  C-II remains open.
