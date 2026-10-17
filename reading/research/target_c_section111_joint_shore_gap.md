> Generated reading edition · [exact source](../../research/target_c_section111_joint_shore_gap.md) · source SHA-256 `0e01dd96da311251153293d2c474673c66cd51c01ecd1d3ad9901ed1150b3185`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — Section 111: joint shore capacity doubles the phase-shore coefficient

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only stacked research candidate; depends on Section 110.

Section 109 correctly proves the lower-bound shore theorem

```math
a<{r\over6C_T},
```

but its statement that `r/(6C_T)` is the asymptotic limit of the bin-counting method
is false.  The two selected phase-label shores are disjoint subsets of the same local
train set, so their **joint** population is at most `T_D`.  Using that fact removes a
factor two from the small-shore crossing capacity and improves the true threshold to

```math
\boxed{a<{r\over3C_T}.}
```

Combining this corrected shore lemma with proof-only Section 110's
`C_T=1.83` and Section 107's `r=0.472` yields shores of size `0.08D`, endpoint supply
`0.16D`, and an explicit scalar window

```math
\boxed{\sigma(\theta)\le4\times10^{-4}.}
```

The resulting carrier coefficient is

```math
\boxed{0.9760500197446322\ldots .}
```

---

## 111.1 Correction to Section 109's sharpness claim

Use the notation of the Section-109 bin argument.  For bin `j`, let `a_j,b_j` be the
two distinct phase-label shore sizes and `e_j` the number of simple crossing edges
inside the bin.  Suppose every occupied bin has

```math
a_j<aD\quad\hbox{or}\quad b_j<aD.
```

Partition the occupied bins into

```math
X:=\{j:a_j<aD\}
```

and

```math
Y:=\{j:a_j\ge aD,\ b_j<aD\}.
```

Since `e_j<=a_jb_j`,

```math
\sum_{j\in X}e_j
\le aD\sum_{j\in X}b_j,
\qquad
\sum_{j\in Y}e_j
\le aD\sum_{j\in Y}a_j.
\tag{111.1}
```

The two phase labels are distinct, hence the selected shore vertices are disjoint local
train segments.  Therefore

```math
\sum_j a_j+\sum_j b_j\le T_D\le C_TD.
\tag{111.2}
```

Combining (111.1)--(111.2),

```math
\boxed{
\sum_j e_j\le aC_TD^2.
}
\tag{111.3}
```

Section 109 instead bounded the two terms separately by `aC_TD^2`, giving the valid
but nonsharp ceiling `2aC_TD^2`.

If the phase-cut/bin procedure retains asymptotically `rD^2/3` crossings for one label
pair, (111.3) is contradicted whenever

```math
\boxed{a<{r\over3C_T}.}
\tag{111.4}
```

Thus the Section-109 theorem remains valid, but the sentence claiming `r/(6C_T)` is
the limit of the method must be superseded by (111.4).

## 111.2 Apply the corrected lemma with the Section-110 train budget

Proof-only Section 107 gives, throughout `sigma<=10^-3`, the conservative rhombus
count

```math
R_D\ge0.472D^2.
\tag{111.5}
```

Proof-only Section 110 derives from the exact Section-82/89 boundary ledger that,
throughout the present window,

```math
T_D\le1.83D.
\tag{111.6}
```

Therefore the corrected shore threshold is

```math
{0.472\over3(1.83)}
=0.0859744990\ldots .
\tag{111.7}
```

Fix

```math
\boxed{a:=0.08.}
\tag{111.8}
```

The Section-90 extraction then produces two distinct-label inverse-phase families of
at least `0.08D` full local train segments each, with limiting projective terminal-edge
directions separated by exactly `pi/3`.

Each full local train has two distinct physical boundary-end occurrences, so each
family supplies

```math
\boxed{E_0D,\qquad E_0:=0.16}
\tag{111.9}
```

terminal edges.

For a completely finite regression, retain `0.471D^2` crossings after the phase cut,
use defect threshold `K=5000`, and bins of width `100K/D`.  Then the internal-bin
crossing density is

```math
{99\over100}{0.471-5.317/5000\over3}
=0.155079078\ldots .
\tag{111.10}
```

If every bin had one shore below `0.08D`, the corrected joint-shore capacity (111.3)
would be at most

```math
0.08(1.83)=0.1464,
\tag{111.11}
```

strictly smaller than (111.10).

## 111.3 Scalar window and leakage

Let

```math
\sigma(\theta)
=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
```

Let `theta_15` solve

```math
\boxed{\sigma(\theta_{15})=4\times10^{-4}.}
\tag{111.12}
```

The regression certificate gives

```math
\boxed{
\theta_{15}=2.7029931020938935\ldots,
\qquad
\mu_{15}=\sin(\theta_{15}/2)
=0.9760500197446322\ldots .
}
\tag{111.13}
```

This lies inside Section 107's `sigma<=10^-3` stability regime.  Section 110's exact
train estimate remains stronger than `1.83D` because

```math
U(\theta_{15})+2\sigma
=1.8265939991\ldots<1.83.
\tag{111.14}
```

The Section-104 technical leakage bound is

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\qquad
w(h)={\pi\over3}-\arccos((1+h)/2).
\tag{111.15}
```

Take

```math
\boxed{h:=0.0262.}
\tag{111.16}
```

At maximal slack,

```math
\boxed{
L=0.0417276437063\ldots .
}
\tag{111.17}
```

Thus each phase family leaves more than

```math
0.16-L
=0.1182723562\ldots
```

endpoints per `D` on the union of the three principal corridors.  One principal
corridor carries more than `0.0394241D`.  Fix

```math
\boxed{\rho:=0.039.}
\tag{111.18}
```

## 111.4 Exact projection contradiction

The full complement-route ledger gives the principal-route excess bound

```math
\sum_i(\ell_i-\sin(g_i/2))\le\sigma.
\tag{111.19}
```

If a principal corridor carries at least `rho D` terminal edges from one selected phase
family and `Delta` is the projective angle between the family direction and the
corridor chord, the exact route projection identity gives

```math
\rho(1-\cos\Delta)\le\sigma.
\tag{111.20}
```

At maximal slack,

```math
\Delta
\le
\arccos\left(1-{4\times10^{-4}\over0.039}\right)
=0.14334567096\ldots .
\tag{111.21}
```

Hence two distinct principal corridors selected by the two `pi/3`-separated phase
families would satisfy

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
<2\Delta
=0.28669134193\ldots .
\tag{111.22}
```

But Section 107's gap stability gives

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma
=0.29938979696\ldots .
\tag{111.23}
```

The contradiction margin is

```math
\boxed{0.0126984550\ldots\text{ radians}.}
\tag{111.24}
```

## 111.5 Carrier consequence and audit disposition

No full-core Type-II countersequence can have every positive-area macroscopic harmonic
cell of normalized diameter at most `mu_15`.  The standard macroscopic-cell transfer
therefore gives a locally rhombus-saturated carrier of quadratic area satisfying

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760500197446322\ldots-o(1))D.
}
\tag{111.25}
```

The Section-109 lower-bound theorem is not invalidated.  Only its asserted sharpness is
superseded:

```text
old claimed method limit: a < r/(6 C_T)
correct joint-shore limit: a < r/(3 C_T).
```

Dependencies: canonical Sections 82, 89, 100, 101, 103; proof-only Sections 107 and
110; the Section-104 technical leakage theorem; and the elementary Section-90
phase-bin construction.  No source point is deleted, and boundary-hole occurrences are
counted by the same physical train decomposition as before.

**Theorem state:** unchanged. Independent hostile audit is required.
