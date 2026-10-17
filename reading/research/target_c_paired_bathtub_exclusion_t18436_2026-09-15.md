> Generated reading edition · [exact source](../../research/target_c_paired_bathtub_exclusion_t18436_2026-09-15.md) · source SHA-256 `ce4bee716f710761d689713a1775db0ddc17e6fcb273237d0139a89d372a91c2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e4a70a46b0afce98852082ebcd7956651663f2c3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_paired_bathtub_exclusion_t18436_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a26061233f15cb0525b056f15e73a6ba009cfa9a03bb94a9d435569e59b640c9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — paired O--O bathtub energy excludes the full `t<=1.8436` band

**Date:** 2026-09-15  
**Status:** proof-only full-core Type-II strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.8436`  
**Dependencies:** phase-resolved retained outer-mass theorem; two-leaf common-center terminal-energy theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The phase-resolved outer-energy theorem and the two-leaf O--O theorem were previously
used separately.  They are incompatible in the entire current `t<=1.8436` band.

The first theorem gives three retained exact-phase outer-occurrence measures with total
mass

```math
z_C+z_U+z_V>2.2069-o(1)
\tag{PB.1}
```

and total directional-energy ceiling

```math
\delta<0.051295+o(1).
\tag{PB.2}
```

The second theorem gives, in each leaf phase, more than `0.06895D-o(D)` retained
outer-to-outer pair weight in a good family, and proves that the two good families are
cross-phase noncrossing with terminal-energy payment

```math
E_U^{good}+E_V^{good}>0.01847-o(1).
\tag{PB.3}
```

The missing composition is that the energy in (PB.3) must be carried by **paired
terminal submeasures of fixed mass** inside the same phase measures that appear in the
bathtub bound.  Removing those paired submeasures leaves less mass available near each
phase-energy well.  A second one-well bathtub bound on the remainder raises the total
minimum energy above the global ceiling:

```math
\boxed{
\delta
>3f(0.6437)+0.01847-o(1)
>0.0516369-o(1),
}
\tag{PB.4}
```

where

```math
f(s)=s-2\sin(s/2).
```

This contradicts (PB.2) by more than `3.4e-4`.  Therefore no full-core Type-II
survivor sequence can have limiting

```math
t\le1.8436.
```

The gain is not another atomic-gap decimal optimization.  It uses where the already
forced leaf energy must live inside the retained outer measure.

---

## 1. Phase-resolved retained measures

Freeze the dominant exact `pi/3` orbit with phase labels `C,U,V` as in the parent
phase-resolved theorem.  Let

```math
\nu_C,\nu_U,\nu_V
```

be the limiting retained outer-occurrence measures on the projective loaded-hull
direction circle.  Write

```math
z_i=\nu_i(\mathbb R/\pi\mathbb Z).
```

Joint routewise retention gives

```math
0\le\nu_i\le d\theta
\tag{PB.5}
```

for each phase.  Relative to its exact phase direction, an occurrence at projective
angular distance `r` pays directional energy at least

```math
c(r)=1-\cos r.
\tag{PB.6}
```

For any measure `mu<=dtheta` of total mass `s<pi`, the one-well bathtub principle gives

```math
\int c\,d\mu
\ge
f(s):=s-2\sin(s/2).
\tag{PB.7}
```

The function `f` is increasing and convex on `[0,pi]` because

```math
f'(s)=1-\cos(s/2)\ge0,
\qquad
f''(s)={1\over2}\sin(s/2)\ge0.
\tag{PB.8}
```

The already-certified `t<=1.844` bootstrap remains valid on the smaller present band
and gives (PB.1), while the same theorem gives (PB.2).

---

## 2. Trim both good O--O families to the same limiting weight

The two-leaf common-center theorem produces good retained O--O pair weights

```math
G_U,G_V>0.06895-o(1).
\tag{PB.9}
```

For a good O--O train `tau`, let its two retained terminal weights be
`a_tau,b_tau` and its pair weight

```math
w_\tau=\min(a_\tau,b_\tau).
```

Pass to a subsequence and trim the good weights, if necessary, so that the selected
pair weight in each leaf tends to

```math
g_0:=0.06895.
\tag{PB.10}
```

This trimming is legitimate because retained weights are real numbers in `[0,1]`; the
last selected train may be fractionally trimmed.  For each selected train assign its
trimmed pair weight to **both** terminal occurrences.  This defines paired terminal
submeasures

```math
\mu_U\le\nu_U,
\qquad
\mu_V\le\nu_V
\tag{PB.11}
```

with limiting masses

```math
\boxed{
\mu_U(\mathbb R/\pi\mathbb Z)
=\mu_V(\mathbb R/\pi\mathbb Z)
=m_0:=2g_0=0.1379.
}
\tag{PB.12}
```

The domination in (PB.11) is pointwise in occurrence weight: the trimmed pair weight
never exceeds either retained terminal weight.

---

## 3. The trimmed pair energy still costs `>0.01847`

Every good `U`-train and every good `V`-train share a center neighbor.  The train
crossing graph is triangle-free, so every such cross-leaf pair is noncrossing.  The
audited endpoint theorem for exact phases separated by `pi/3` then gives

```math
e_\tau+e_\sigma\ge2-\sqrt3-o(1)
\tag{PB.13}
```

uniformly over the two good families.

Multiply by the trimmed pair weights and sum over the complete product.  Because both
trimmed total weights tend to the same value `g_0`, division by the opposite-family
weight gives

```math
\boxed{
E_U^{trim}+E_V^{trim}
\ge(2-\sqrt3)g_0-o(1).
}
\tag{PB.14}
```

Using

```math
\sqrt3<1.7321
```

and `g_0=0.06895`,

```math
(2-\sqrt3)g_0
>0.2679(0.06895)
=0.018471705
>0.01847.
\tag{PB.15}
```

Thus the trimmed pair energy itself satisfies

```math
E_U^{trim}+E_V^{trim}>0.01847-o(1).
\tag{PB.16}
```

This is the same outer directional-energy currency as the phase bathtub theorem, not an
additional energy budget.

---

## 4. Remove the paired terminal submeasures and reapply the bathtub principle

Because `mu_U<=nu_U`, the remainder

```math
\eta_U:=\nu_U-\mu_U
```

is a nonnegative measure dominated by `dtheta`, with mass

```math
\eta_U(\mathbb R/\pi\mathbb Z)=z_U-m_0.
```

Likewise

```math
\eta_V:=\nu_V-\mu_V
```

has mass `z_V-m_0` and is dominated by `dtheta`.

The actual retained directional energy in leaf `U` decomposes into the energy carried
by the trimmed paired terminal weights plus the remainder.  The latter is at least its
one-well bathtub cost.  Therefore

```math
D_U
\ge E_U^{trim}+f(z_U-m_0)-o(1),
\tag{PB.17}
```

```math
D_V
\ge E_V^{trim}+f(z_V-m_0)-o(1).
\tag{PB.18}
```

For the center phase, no subtraction is needed:

```math
D_C\ge f(z_C)-o(1).
\tag{PB.19}
```

The three selected phase energies have disjoint occurrence support and are all paid by
the global outer directional-energy budget.  Combining (PB.16)--(PB.19),

```math
\boxed{
\delta
\ge
f(z_C)+f(z_U-m_0)+f(z_V-m_0)+0.01847-o(1).
}
\tag{PB.20}
```

No energy term has been counted twice: the paired weights are explicitly removed before
the remainder bathtub is applied.

---

## 5. Jensen collapses the constrained bathtub to one number

By (PB.1),

```math
z_C+(z_U-m_0)+(z_V-m_0)
>2.2069-2(0.1379)-o(1)
=1.9311-o(1).
\tag{PB.21}
```

Each argument lies in `[0,pi]`; in particular the parent phase theorem gives
`z_U,z_V>0.616-o(1)`, so the two leaf remainders remain positive.

Convexity and monotonicity of `f` give

```math
\begin{aligned}
f(z_C)+f(z_U-m_0)+f(z_V-m_0)
&\ge
3f\left({1.9311\over3}\right)-o(1)\\
&=3f(0.6437)-o(1).
\end{aligned}
\tag{PB.22}
```

Hence

```math
\boxed{
\delta
>3f(0.6437)+0.01847-o(1).
}
\tag{PB.23}
```

This is precisely the continuous dual of the paired-submeasure bathtub problem; no
discretized LP is needed in the proof.

---

## 6. Exact rational certificate

Run

`research/verify_target_c_paired_bathtub_excludes_t18436.py`.

The certificate uses only `Fraction` arithmetic.  Set

```math
s={6437\over10000},
\qquad x={s\over2}.
```

Since the sine series is alternating with decreasing terms at this `x`,

```math
\sin x
< x-{x^3\over6}+{x^5\over120}.
\tag{PB.24}
```

Therefore

```math
f(s)
=s-2\sin(s/2)
>
0.0110556445694\ldots .
\tag{PB.25}
```

The exact rational computation gives

```math
\boxed{
3f(0.6437)+0.01847
>0.0516369337082\ldots
}
\tag{PB.26}
```

while the parent outer-energy theorem gives

```math
\delta<0.051295+o(1).
\tag{PB.27}
```

The certified contradiction gap is larger than

```math
\boxed{0.00034.}
\tag{PB.28}
```

This margin is two orders of magnitude larger than the recent sixth-decimal scalar
endpoint gains.

---

## 7. Consequence and frontier

Assume a full-core Type-II survivor subsequence has limiting

```math
t\le1.8436.
```

All parent hypotheses above hold on that subsequence, so (PB.26)--(PB.27) contradict
one another.  Therefore

```math
\boxed{
\text{no full-core Type-II survivor has limiting }t\le1.8436.
}
\tag{PB.29}
```

Equivalently, at the present proof-only full-core Type-II scope the low-`t` floor may be
promoted from `1.843579` to

```math
\boxed{
\liminf {q-k\over D}\ge1.8436.
}
\tag{PB.30}
```

The argument does **not** close C-II.  It eliminates the entire band covered by the
current two-leaf common-center theorem.  The next quantitative target is to extend the
two-leaf O--O/common-center structure above `1.8436`; every such extension can now be
fed directly into the paired-bathtub inequality rather than into another atomic-gap
decimal optimization.

A second target is structural rather than scalar: use the complete ordered
leaf/center rectangle together with the fact that both leaf phases now carry
macroscopic O--O populations, seeking a two-braced-shore rectangle or a bounded
reuse theorem for Section-157 diameter braces.

**Disposition:** proved proof-only paired-submeasure bathtub exclusion of the complete
`t<=1.8436` full-core Type-II band. C-II and Level I remain open.
