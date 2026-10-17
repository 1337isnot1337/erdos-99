> Generated reading edition · [exact source](../../research/target_c_paired_remainder_bathtub_2026-09-15.md) · source SHA-256 `2e249c56cfc0da704ceb7cee12cac75aa5fd3a501c248e1d57e335eb824865dd`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9267a24f1512bb52ce0792f91ff02ec59a2199ba", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_paired_remainder_bathtub_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5edb004bb05db0c2290cfeedb8502e66e12a6f22e00f09783a74197b34ac1456"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — paired O--O terminal submeasures leave a second leaf bathtub

**Date:** 2026-09-15  
**Status:** proof-only structural strengthening  
**Scope:** dominant exact three-phase orbit in the full-core Type-II branch  
**Dependencies:** phasewise retained-outer measure domination; O--O pair weights; hostile-audited cross-phase endpoint-energy theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current two-leaf outer-energy argument uses the pair-weighted terminal energy of a good O--O family and then discards every other selected outer occurrence in those two leaf phases. That is a genuine loss.

The paired terminal weights form a **submeasure** of the retained outer-occurrence measure. After that submeasure is removed, the remaining selected leaf occurrence measure is still nonnegative, still has density at most one with respect to projective boundary angle, and therefore still pays the ordinary one-well bathtub energy.

This gives the following reusable strengthening.

Let two exact phase classes `U,V` be separated projectively by `pi/3`. For phase `i`, let

```math
\nu_i
```

be its retained outer-occurrence measure, with

```math
0\le \nu_i\le d\theta,
\qquad
z_i:=\nu_i(\mathbb R/\pi\mathbb Z).
```

Let `F_i` be a weighted O--O train family in phase `i`. For train `tau`, let its two retained terminal weights be `a_tau,b_tau` and put

```math
w_\tau=\min(a_\tau,b_\tau).
```

Assume every train in `F_U` is noncrossing with every train in `F_V`. Write

```math
G_i={1\over D}\sum_{\tau\in F_i}w_\tau.
```

For every

```math
0<g\le\min(G_U,G_V)
```

one has

```math
\boxed{
D_U+D_V
\ge
(2-\sqrt3)g
+f(z_U-2g)+f(z_V-2g)-o(1),
}
\tag{PR.1}
```

where `D_i` is the normalized selected outer directional energy in phase `i` and

```math
f(s)=s-2\sin(s/2).
```

In particular, if

```math
z_U,z_V\ge A-o(1),
\qquad
G_U,G_V\ge G-o(1),
```

then, after taking the source limit and then `g\uparrow G`,

```math
\boxed{
D_U+D_V
\ge
(2-\sqrt3)G+2f(A-2G)-o(1).
}
\tag{PR.2}
```

If a third, disjoint center phase has retained mass `z_C>=A-o(1)`, then

```math
\boxed{
D_C+D_U+D_V
\ge
f(A)+(2-\sqrt3)G+2f(A-2G)-o(1).
}
\tag{PR.3}
```

The extra term `2f(A-2G)` is absent from the previous two-leaf ledger.

---

## 1. Trim both good weighted families to equal mass

Fix

```math
g<\min(G_U,G_V).
```

Because every pair weight lies in `[0,1]`, choose coefficients

```math
0\le\lambda_\tau\le1
```

inside each family so that the trimmed weights

```math
\widetilde w_\tau=\lambda_\tau w_\tau
```

have total normalized weight exactly `g` in each phase:

```math
{1\over D}\sum_{\tau\in F_U}\widetilde w_\tau
={1\over D}\sum_{\sigma\in F_V}\widetilde w_\sigma
=g.
\tag{PR.4}
```

This is only a weighting operation. It does not change any train, crossing relation, center neighborhood, endpoint cyclic order, or terminal directional energy.

---

## 2. The trimmed terminal weights are dominated by the retained occurrence measure

For one O--O train `tau`, put trimmed mass `widetilde w_tau` on each of its two selected outer terminal occurrences. Denote the resulting phase-`i` measure by

```math
\mu_i.
```

The complete-train decomposition assigns each terminal occurrence to its train in that phase, and

```math
\widetilde w_\tau
\le w_\tau
\le a_\tau,b_\tau.
```

Hence, as measures,

```math
\boxed{0\le\mu_i\le\nu_i.}
\tag{PR.5}
```

Each train contributes the trimmed weight at two terminals, so

```math
\boxed{\mu_i(\mathbb R/\pi\mathbb Z)=2g.}
\tag{PR.6}
```

Therefore the remainder

```math
\rho_i:=\nu_i-\mu_i
```

is a genuine nonnegative retained-occurrence measure with

```math
0\le\rho_i\le d\theta,
\qquad
\rho_i(\mathbb R/\pi\mathbb Z)=z_i-2g.
\tag{PR.7}
```

There is no count-to-weight conversion here. The subtraction is performed directly at the retained occurrence-weight level.

---

## 3. The remainder pays an independent one-well bathtub cost

Let the exact phase direction be `phi_i`. Every selected outer occurrence at projective angle `theta` pays directional energy at least

```math
1-\cos d(\theta,\phi_i).
```

The usual one-well bathtub theorem says that among measures `0<=rho<=dtheta` of total mass `s`, this energy is minimized by filling the centered interval of length `s`, giving

```math
\int (1-\cos d(\theta,\phi_i))\,d\rho
\ge
f(s),
\qquad
f(s)=s-2\sin(s/2).
\tag{PR.8}
```

Apply this to `rho_i`. If `E_i^g` denotes the actual trimmed pair-weighted terminal energy, linearity of the selected edge-energy sum and (PR.5) give

```math
\boxed{
D_i\ge E_i^g+f(z_i-2g)-o(1).
}
\tag{PR.9}
```

This is the key point: the pair terminal energy and the remainder bathtub are paid by disjoint portions of the same selected occurrence weights. They may therefore be added without double counting.

---

## 4. The cross-leaf noncrossing product pays `(2-sqrt(3))g`

The hostile-audited endpoint theorem gives, for every cross pair `tau in F_U`, `sigma in F_V`,

```math
e_\tau+e_\sigma
\ge
2-\sqrt3-o(1),
\tag{PR.10}
```

because the two exact phases are separated by `pi/3` and the two O--O trains are noncrossing.

Multiply (PR.10) by

```math
\widetilde w_\tau\widetilde w_\sigma
```

and sum over the complete product. The left side factors using (PR.4):

```math
gE_U^g+gE_V^g
\ge
(2-\sqrt3)g^2-o(1).
```

Thus

```math
\boxed{
E_U^g+E_V^g
\ge
(2-\sqrt3)g-o(1).
}
\tag{PR.11}
```

Combining (PR.9) in the two leaves with (PR.11) proves (PR.1).

If `z_U,z_V>=A-o(1)`, monotonicity of `f` gives

```math
D_U+D_V
\ge
(2-\sqrt3)g+2f(A-2g)-o(1).
```

For every fixed `g<G` this is valid. Let `g\uparrow G`; continuity of `f` proves (PR.2). Adding the disjoint center-phase bathtub `f(A)` proves (PR.3).

---

## 5. Why this matters at the current frontier

The earlier common-center theorem explicitly left open whether the phasewise bathtub could coexist with the required paired O--O terminal energy. Equation (PR.3) resolves that question at the correct measure level.

At the current `t<=1.84365` endpoint, the old proof uses only

```math
f(A)+(2-\sqrt3)G.
```

It discards retained leaf mass of size approximately

```math
A-2G
```

in **each** leaf. Equation (PR.3) restores the two corresponding bathtub costs. Numerically this is a first-order gain at the present constants, not a sixth-decimal correction.

The next downstream task is to propagate (PR.3) through the residual/phase-localization package and determine the new safe endpoint. A preliminary exact-arithmetic target is `t<=1.84370`; no endpoint claim is made in this structural note itself.

**Disposition:** proved structural energy strengthening. C-II and Level I remain open.
