> Generated reading edition · [exact source](../../../../docs/targets/target-c/106-strong-phase-shore-quantitative-gap-audit.md) · source SHA-256 `73804e030dfdb95e0706d2800a62b0b1d10169f1d158b46f7951e61a28ddab2c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — stronger phase shores and a larger explicit carrier gap

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proved candidate, proof-only pending independent hostile audit/promotion.

Canonical Sections 101--103 and the independently audited proof-only Section 104 reduce the
near-endpoint full-core Type-II branch to a quantitative phase/corridor contradiction.  The
report-level Section-105 candidate sharpens the principal-corridor route-excess budget and
raises the explicit scalar window to `sigma=7e-7`.

This section keeps the Section-104 geometry and the sharper all-macroscopic-route excess
bound, but removes a much larger conservative loss in the Section-90 phase extraction.
Section 90 chose very small shores merely to leave an easy positive crossing margin.  With
the explicit carrier constants now canonical from Section 103, one can choose the phase
cutoff and bin width explicitly and retain much larger shores.

The result is an explicit scalar window

```math
\boxed{\sigma(\theta)\le 1.2\times10^{-5}},
\qquad
\sigma(\theta):=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
```

and hence an improved carrier coefficient

```math
\boxed{
\mu_{11}=0.9760410429297387484\ldots .
}
```

This is still a constant optimization, not a closure of C-II.

---

# 106. A larger explicit gap from stronger inverse-phase shores

## 106.1 Scalar window and inherited geometric stability

Let

```math
\sigma_*:=1.2\times10^{-5}.
\tag{106.1}
```

Let `theta_11` be the unique solution above the canonical Section-101 endpoint `theta_8`
of

```math
\sigma(\theta_{11})=\sigma_*.
\tag{106.2}
```

The scalar regression gives

```math
\boxed{
\theta_{11}
=2.7029105818462226988\ldots,
}
\tag{106.3}
```

```math
\boxed{
\mu_{11}:=\sin(\theta_{11}/2)
=0.9760410429297387484\ldots .
}
\tag{106.4}
```

Thus

```math
\boxed{
\mu_{11}-\mu_8
=2.77662686766\times10^{-7}>0.
}
\tag{106.5}
```

Assume for contradiction that all positive-area macroscopic harmonic-cell limits of a
full-core Type-II countersequence have normalized diameter at most `mu_11`.  Canonical
Section 103 gives a unique wrapping carrier with normalized area bounded below by the
cap deficit.  Since

```math
\sigma'(\theta)
=3-\tfrac12\cos(\theta/2)-2\cos\theta
\ge {15\over4},
```

we have

```math
0\le\theta-\theta_8
\le {4\over15}\sigma_*
<3.2\times10^{-6}.
\tag{106.6}
```

This lies far inside the canonical Section-103 neighborhood
`theta<=theta_8+0.03`, where the wrapping carrier has area greater than `0.1905D^2`
and admits the conservative local constants

```math
R_D\ge0.18D^2,
\qquad
T_D\le6D,
\qquad
\sum_R\delta_R<5.317D
\tag{106.7}
```

for all sufficiently large members of the sequence.

All Section-104 complement-gap stability arguments remain valid on (106.1): their only
fixed numerical barriers are the `delta=0.1` concavity barrier, the derivative lower
bound `h_theta'(delta)>0.30`, and `tau<phi`, all with orders of magnitude of spare
room.  Hence, retaining Section-104 notation,

```math
g_1=\theta-\delta,
\qquad
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
```

```math
0\le\delta\le {10\over3}\sigma,
\qquad
0\le x_2,x_3,\tau\le {13\over3}\sigma,
\tag{106.8}
```

and the principal corridor directions satisfy

```math
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>
{\theta_8\over2}-{\pi\over3}-{73\over6}\sigma
}
\tag{106.9}
```

for `i!=j`.  At `sigma=sigma_*`, the right side is

```math
\boxed{>0.3041104.}
\tag{106.10}
```

## 106.2 Reprove the sharp principal-route excess bound

We do not need Section 105 as a logical premise.

For every fixed finite family `J` of positive complement gaps, the exact Section-82
outer-walk identity plus the ordinary two-edge route floor gives, after division by
`D` and passage to the scale limit,

```math
\sum_{j\in J}\ell_j\le2\alpha.
\tag{106.11}
```

Take increasing finite families exhausting all positive complement components.  By
monotone nonnegativity,

```math
\sum_{j\ge1}\ell_j\le2\alpha.
\tag{106.12}
```

Every macroscopic route dominates its endpoint chord,

```math
\ell_j\ge f(g_j),
\qquad f(x)=\sin(x/2),
```

and canonical Section 101 gives

```math
C:=\sum_j f(g_j)\le2\alpha,
\qquad
2\alpha-C\le\sigma.
```

Therefore

```math
\boxed{
\sum_{j\ge1}\bigl(\ell_j-f(g_j)\bigr)
\le2\alpha-C\le\sigma.
}
\tag{106.13}
```

In particular the three principal corridors satisfy

```math
\boxed{
\sum_{i=1}^3\bigl(\ell_i-f(g_i)\bigr)\le\sigma.
}
\tag{106.14}
```

The larger Section-104 bound `(19/6)sigma` is still retained where the total *length*
of nonprincipal macroscopic routes is needed.

## 106.3 Strengthen the Section-90 phase-family extraction

The key new step is purely combinatorial/phase-theoretic.

Start with the carrier constants (106.7).  Canonical Section 90 first performs the
phase-circle cut, deleting only `O(D)` crossing rhombi.  Hence, for all sufficiently
large `D`, at least

```math
0.179D^2
\tag{106.15}
```

carrier crossings remain.

Call a retained crossing **good** when its angular defect is at most

```math
{K\over D},
\qquad K:=1000.
\tag{106.16}
```

The defect sum in (106.7) bounds the number of nongood crossings by

```math
{5.317D\over K/D}
=0.005317D^2.
\tag{106.17}
```

Thus at least

```math
(0.179-0.005317)D^2
=0.173683D^2
\tag{106.18}
```

good crossings remain.  There are only three unordered pairs of phase labels, so one
fixed label pair supports at least

```math
{0.173683\over3}D^2
=0.057894333\ldots D^2
\tag{106.19}
```

good crossings.

For this label pair, write the real reduced phases as in canonical Section 90.  Every
good crossing joins phases at distance at most `K/D`.  Randomly shift bins of width

```math
W:={20K\over D}={20000\over D}.
\tag{106.20}
```

For one good crossing, a bin boundary separates its two endpoint phases with
probability at most `1/20`.  Hence some shift retains at least `19/20` of the crossings
inside common bins.  The total internal-bin crossing count is therefore at least

```math
{19\over20}{0.173683\over3}D^2
=0.0549996166\ldots D^2.
\tag{106.21}
```

Let `a_j,b_j` be the two shore sizes in bin `j`.  Since both shores are subsets of the
full local train set,

```math
\sum_j a_j\le6D,
\qquad
\sum_j b_j\le6D.
\tag{106.22}
```

Set

```math
A_0:=0.0045.
\tag{106.23}
```

If every occupied bin had `a_j<A_0D` or `b_j<A_0D`, then bins small on the first shore
would carry at most

```math
A_0D\sum_jb_j\le0.027D^2
```

crossings, and among the remaining bins those small on the second shore would carry
at most another `0.027D^2`.  Thus all internal-bin crossings would total at most

```math
0.054D^2,
```

contradicting (106.21).

Therefore one common reduced-phase bin contains two fixed, distinct label families
`A_D,B_D` with

```math
\boxed{
|A_D|,|B_D|\ge0.0045D.
}
\tag{106.24}
```

The bin width is `20000/D=o(1)`, so each family has one limiting projective direction,
`u_A,u_B`, and the distinct phase labels give

```math
\boxed{
\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
}
\tag{106.25}
```

Every full local train segment has two distinct physical boundary-end occurrences,
and a physical boundary edge terminates only the train using its edge direction.
Hence each selected family supplies at least

```math
\boxed{E_0D,\qquad E_0:=0.009}
\tag{106.26}
```

physical train endpoints.

This improves the `E_0=0.001875` endpoint supply used in Sections 104--105 by a factor
of `4.8` without changing the carrier geometry.

## 106.4 Reuse the Section-104 leakage bound with an optimized tooth cutoff

The Section-104 technical companion proves that, for any excess-base cutoff `h>0`, one
selected inverse-phase family can place at most

```math
L(\sigma,h)D+o(D)
\tag{106.27}
```

physical endpoints away from the three principal corridors, where

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\tag{106.28}
```

```math
w(h):={\pi\over3}-\arccos((1+h)/2).
\tag{106.29}
```

The coefficient `169/6` includes nonquadrilateral boundary, nonprincipal macroscopic
corridors, exceptional micro routes, the two tiny support spans, and the tail-chord
contribution.  The `sigma/h` term is the bad-base Markov loss; `w(h)` is the two-window
good-base directional capacity.

Choose

```math
\boxed{h:=0.00455.}
\tag{106.30}
```

At `sigma=sigma_*`,

```math
w(h)=0.0026289418825\ldots,
\tag{106.31}
```

and

```math
\boxed{
L(\sigma_*,h)
=0.0056043045199\ldots .
}
\tag{106.32}
```

Subtracting from (106.26), more than

```math
0.00339569D
```

endpoints of each phase family remain on the three principal corridors.  One principal
corridor therefore carries more than

```math
0.00113189D
```

endpoints from that family.  Fix the slightly smaller explicit constant

```math
\boxed{\rho:=0.00113.}
\tag{106.33}
```

## 106.5 Exact projection alignment closes the larger window

Suppose one principal corridor carries at least `rho D` endpoints of one selected
phase family.  Let `u` be the limiting projective direction of the family, `q` the
corridor chord direction, and

```math
\Delta:=\operatorname{dist}_{RP^1}(u,q).
```

Orient the corridor route along its chord.  Every selected endpoint edge contributes
asymptotic projection loss at least `1-cos Delta`.  By (106.14), the total normalized
excess of all three principal routes is at most `sigma`.  Therefore

```math
\boxed{
\rho(1-\cos\Delta)\le\sigma.
}
\tag{106.34}
```

At `sigma=sigma_*` and `rho=0.00113`, the exact inverse cosine gives

```math
\boxed{
\Delta
\le\arccos\left(1-{1.2\times10^{-5}\over0.00113}\right)
<0.145866.
}
\tag{106.35}
```

Apply this to both selected phase families.  They cannot use the same principal
corridor, because then

```math
\operatorname{dist}_{RP^1}(u_A,u_B)
<2(0.145866)<\pi/3,
```

contradicting (106.25).  Hence they use two distinct principal corridors.

For those corridors, the projective triangle inequality gives

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
<2(0.145866)
<0.291732.
\tag{106.36}
```

But (106.10) gives

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>0.3041104.
```

The contradiction margin is greater than

```math
\boxed{0.01237\text{ radians}.}
\tag{106.37}
```

Thus no full-core Type-II countersequence can have all positive-area macroscopic
harmonic-cell limits of normalized diameter at most `mu_11`.

## 106.6 Carrier consequence

The canonical Section-83 finite-macroscopic-cell reduction gives an actual carrier
conclusion exactly as in Sections 104--105.  There is an absolute `c_11>0` such that
every sufficiently large Type-II survivor contains a locally rhombus-saturated harmonic
cell `P_*` with

```math
\boxed{
\operatorname{area}(P_*)\ge c_{11}D^2,
\qquad
\operatorname{diam}(P_*)
\ge(\mu_{11}-o(1))D,
}
\tag{106.38}
```

where

```math
\boxed{
\mu_{11}=0.9760410429297387484\ldots .
}
\tag{106.39}
```

## 106.7 Dependencies and audit scope

- **Canonical Section 101 / `C-WRAP-COMPLEMENT-CHORD`:** scalar chain and the endpoint
  `theta_8,mu_8`.
- **Canonical Section 103:** unique wrapping carrier, area concentration, and the
  explicit near-endpoint constants `R_D>=0.18D^2`, `T_D<=6D`,
  `sum delta_R<5.317D`.
- **Independently audited proof-only Section 104 plus its technical companion:**
  complement-gap stability and leakage decomposition.
- **Section-105 candidate:** not a required premise.  Section 106 rederives the only
  new Section-105 fact it uses, namely the all-macroscopic-route excess bound
  `sum(ell_j-f(g_j))<=sigma`.
- **Canonical Sections 68, 69, 82, 89, and 90:** phase potential/defect, physical train
  endpoints, outer-face ledger, local train count, and inverse-phase binning.
- **New input:** only the explicit stronger shore extraction in §106.3 and the resulting
  re-optimization of the already-audited leakage inequality.
- **Bridges and contact-isolated source points:** untouched; all train-end counting is
  on physical strict-rhombus boundary edges, with the outer walk counted with its
  canonical multiplicity.
- **No theorem-state mutation.** C-II remains open.
