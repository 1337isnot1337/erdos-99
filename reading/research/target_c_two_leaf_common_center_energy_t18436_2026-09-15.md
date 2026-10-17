> Generated reading edition · [exact source](../../research/target_c_two_leaf_common_center_energy_t18436_2026-09-15.md) · source SHA-256 `af972dba71f8e5b1e114558d6043f31655218062e858c31a0ad16d034b5c006c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "df808fbebfd11bdf51ecd60633d5eae357bcefda", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_leaf_common_center_energy_t18436_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "16123cdf4215c493bc2ffedb8a43cd7da4ebe2a5364ede80ed6c8e34c0036c5c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — two macroscopic leaf O--O families force `>0.01847D` terminal energy

**Date:** 2026-09-15  
**Status:** proof-only near-frontier structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.8436`  
**Dependencies:** two-leaf O--O weight theorem; dominant-orbit triangle-free correlation; low-energy cross-phase O--O endpoint theorem  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The near-frontier phase-localization theorem gives two retained outer-to-outer train
populations in the two leaf phases of the dominant exact `pi/3` orbit:

$$
P_U>0.103-o(1),
\qquad
P_V>0.103-o(1).
\tag{CE.1}
$$

This note couples those populations through the center phase.  After discarding less
than `0.03405D` retained pair weight in total, every remaining train in both leaf
families crosses more than half of the center-phase trains.  Hence every surviving
`U`-train and every surviving `V`-train share a center neighbor.  Triangle-freeness
then forces the two leaf trains not to cross.  Since the two leaf phases differ by
exactly `pi/3`, the outer-endpoint alternation theorem converts that noncrossing into a
terminal directional-energy payment.

The result is

$$
\boxed{
E_U+E_V>0.01847-o(1),
}
\tag{CE.2}
$$

where `E_U D` and `E_V D` are the retained-pair-weighted sums of the exact two-terminal
directional energies in the two leaf phases.

This energy is not a new currency: it is a subset of the already existing dominant
outer directional-energy budget.

---

## 1. Near-frontier phase box

Write the dominant orbit phase masses as

$$
C\ge U\ge V.
$$

The `t<=1.8436` two-leaf theorem supplies the safe bounds

$$
W:=C+U+V<1.912456+o(1),
\tag{CE.3}
$$

$$
E_{dom}>0.90689967-o(1),
\tag{CE.4}
$$

and

$$
U,V<0.513-o(1).
\tag{CE.5}
$$

Let

$$
x=CU-e(C,U),
\qquad
y=CV-e(C,V)
$$

be the missing center/leaf crossing masses, and put

$$
h=C(U+V)-E_{dom}.
$$

The hostile-audited center/leaf correlation is

$$
\left(1-{V\over C}\right)x
+
\left(1-{U\over C}\right)y
\le h.
\tag{CE.6}
$$

Since `U>=V`, the smaller coefficient is `1-U/C`.  Thus

$$
\left(1-{U\over C}\right)(x+y)
\le h.
$$

Using (CE.3)--(CE.5),

$$
\boxed{
 x+y
\le
{C[C(1.912456-C)-0.90689967]\over C-0.513}
+o(1).
}
\tag{CE.7}

Generic center capacity also forces `C>0.513`: otherwise, because the right side
`C(W-C)` is increasing for `C<W/2`,

\[
E_{dom}
\le0.513(1.912456-0.513)
<0.718
$$

would contradict (CE.4).

---

## 2. Low-center-degree O--O weight is less than `0.03405D`

For a retained O--O train `tau` in either leaf phase, let `w_tau in(0,1]` be its
retained pair weight.  Let `N_C` be the actual number of frozen-window center-phase
trains; then

$$
{N_C\over D}\to C.
$$

Call a leaf O--O train **bad** if its center crossing degree is at most `N_C/2`.
Such a train misses at least `N_C/2` center trains.  Therefore the total normalized
retained weight of bad `U`-trains is at most

$$
{2x\over C}+o(1),
$$

and similarly the bad `V`-weight is at most

$$
{2y\over C}+o(1).
$$

Hence the total bad retained weight is at most

$$
B_{bad}
\le {2(x+y)\over C}+o(1)
\le
{2[C(1.912456-C)-0.90689967]
\over C-0.513}+o(1).
\tag{CE.8}
$$

The right side is uniformly below `0.03405`.  Indeed, with

$$
W_0={239057\over125000},
\quad
E_0={90689967\over10^8},
\quad
u={513\over1000},
\quad
b={681\over20000},
$$

the desired inequality is equivalent to positivity of

$$
q(C)=b(C-\nu)-2[C(W_0-C)-E_0].
$$

This quadratic has leading coefficient `2`, and its exact discriminant is

$$
\boxed{
\operatorname{disc}(q)<-1.88\times10^{-5}<0.
}
\tag{CE.9}

Therefore

\[
\boxed{B_{bad}<0.03405-o(1).}
\tag{CE.10}

By (CE.1), even if all bad weight is concentrated in one leaf phase, each leaf retains
good O--O weight

\[
\boxed{
G_U,G_V>0.103-0.03405-o(1)
=0.06895-o(1).
}
\tag{CE.11}

---

## 3. Every good cross-leaf pair shares a center neighbor

Take a good `U`-phase O--O train `tau` and a good `V`-phase O--O train `sigma`.
Each crosses strictly more than half of the same finite center family.  Hence

\[
N_C(\tau)\cap N_C(\sigma)\ne\varnothing.
\tag{CE.12}

Choose a center train `gamma` in the intersection.  Then `gamma` crosses both `tau` and
`sigma` in strict rhombi.

The complete stopped-train crossing graph is triangle-free.  Therefore `tau` and
`sigma` cannot cross each other.

Both are proper O--O crosscuts in the audited convex-pocket augmentation.  If their
outer endpoints alternated cyclically, the two crosscuts would have to intersect.
Thus their endpoints are nonalternating.

The two leaf phases belong to the same exact three-phase orbit, so their projective
phase separation is exactly `pi/3` in the limiting frozen-window sense.  The existing
cross-phase endpoint theorem therefore gives, uniformly over the good families,

\[
\boxed{
e_\tau+e_\sigma
\ge2-\sqrt3-o(1),}
\tag{CE.13}

where `e_tau,e_sigma` are the exact sums of the two terminal directional-energy
contributions of the corresponding O--O trains.

---

## 4. Sum the complete weighted product

Let

\[
E_U^{good}
={1\over D}\sum_{\tau\in U_{good}}w_\tau e_\tau,
\qquad
E_V^{good}
={1\over D}\sum_{\sigma\in V_{good}}w_\sigma e_\sigma.
$$

Multiply (CE.13) by `w_tau w_sigma` and sum over the complete product of the two good
families.  After dividing by `D^2`,

$$
G_VE_U^{good}+G_UE_V^{good}
\ge(2-\sqrt3)G_UG_V-o(1).
\tag{CE.14}

If `G_U<=G_V`, then the left side is at most

\[
G_V(E_U^{good}+E_V^{good}),
$$

so

$$
E_U^{good}+E_V^{good}
\ge(2-\sqrt3)G_U-o(1).
$$

The symmetric case is identical.  Hence

$$
E_U+E_V
\ge E_U^{good}+E_V^{good}
\ge(2-\sqrt3)\min(G_U,G_V)-o(1).
\tag{CE.15}

Using (CE.11),

\[
E_U+E_V
>(2-\sqrt3)(0.06895)-o(1).
$$

The exact certificate uses the rational bound

$$
\sqrt3<1.7321
$$

and obtains

$$
(2-\sqrt3)(0.06895)>0.0184717.
$$

Therefore

$$
\boxed{E_U+E_V>0.01847-o(1).}
$$

---

## 5. Frontier effect

Near the current low-`t` floor, the two leaf O--O populations can no longer be treated
as independent boundary decoration.  A linear subfamily in each leaf is forced to
share center neighbors across the complete product.  Triangle-freeness then turns the
entire product into a noncrossing cross-phase relation, which has a fixed endpoint
energy cost.

The resulting live object at `t<=1.8436` is now

```text
U leaf: >0.06895D high-center-degree O-O weight
V leaf: >0.06895D high-center-degree O-O weight
cross-product: every pair shares a center neighbor, hence is noncrossing
terminal-energy consequence: E_U+E_V >0.01847D
```

This should be combined next with the phase-resolved outer bathtub problem.  The global
three-well bound already nearly saturates the total outer-energy budget at the scalar
frontier; the remaining question is whether a bathtub minimizer can place this much
energy specifically on the paired O--O occurrence submeasures in both leaf phases.

No C-II or Level-I closure is claimed.
