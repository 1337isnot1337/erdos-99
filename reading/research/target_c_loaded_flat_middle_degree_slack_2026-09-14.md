> Generated reading edition · [exact source](../../research/target_c_loaded_flat_middle_degree_slack_2026-09-14.md) · source SHA-256 `390aeda2e43af06c5efba68030164da436ed7d3da6298e3be870009eab01bede`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "719b4d23f44265133fb45dc2de663d50b72af6b1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_loaded_flat_middle_degree_slack_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7db7f41ebf1adea0d553ddc929c07328f8d8d3e5d48c814d6ec670474daa5509"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — loaded flat middles have contact degree two

**Date:** 2026-09-14  
**Target:** Target C-II, small-residual flat-pentagon branch  
**Claim class:** proof-only structural refinement; theorem-state authority unchanged  
**External input:** none

## LEVEL I STATUS

`STILL OPEN`

The flat-middle injectivity theorem reduces cheap pentagons to distinct almost-straight positive-core vertices. This note resolves the loaded side of its loaded/blocker fork exactly.

For a sufficiently flat pentagon, if its almost-flat middle vertex lies on the loaded force hull, then

```math
\boxed{\deg_C(m)=2.}
\tag{LF.1}
```

Both contacts are the two pentagon-chain edges; there is no third positive contact. Hence every loaded flat middle contributes one unit to the canonical loaded contact-degree slack

```math
s_B:=3q-e_{BI}-2e_{BB}
=\sum_{b\in B}(3-\deg_C b).
```

Therefore

```math
\boxed{L_{flat}\le s_B.}
\tag{LF.2}
```

Combined with flat-middle injectivity, on `R_F=o(D)`

```math
\boxed{
X+s_B+2E_{block}
\ge(f_*-o(1))D,
\qquad X:=Q-f,
}
\tag{LF.3}
```

with the AG58 face coefficient

```math
f_*=\sqrt{\Delta_2}-{\pi\over4}+0.00029
=0.167204643466509\ldots .
```

This inserts the flat-pentagon population into the exact ZI topology/stress ledger.

---

## 1. Loaded hull geometry leaves no room for a third contact

Let `m` be the almost-flat middle vertex of a bounded convex pentagonal contact face. Let the two incident pentagon boundary contacts be `ml,mr`, and write

```math
\alpha:=\angle lmr.
```

For the trapezoid-stability diagonal,

```math
\alpha\to\pi.
```

Fix a finite stage with

```math
\alpha>\pi-\varepsilon,
\qquad 0<\varepsilon<\pi/3.
\tag{1.1}
```

Assume `m` is loaded. Canonical force-hull geometry makes `m` an extreme convex-hull vertex of the positive-contact core. Therefore every positive-contact ray from `m` lies in one hull wedge of opening

```math
\theta_m<\pi.
\tag{1.2}
```

The pentagon sector between `ml` and `mr` has opening `alpha` and lies inside this wedge. The total angular room in the hull wedge outside that sector is less than

```math
\theta_m-\alpha
<\pi-(\pi-\varepsilon)
=\varepsilon
<\pi/3.
\tag{1.3}
```

Any third unit-contact ray from `m` would have to lie in this remaining wedge. But triangle-free unit separation says any two distinct contact rays at one vertex are separated by strictly more than `pi/3`. Such a ray cannot fit into (1.3).

Thus the only positive contacts at `m` are `ml,mr`, proving (LF.1).

Because `m` is incident with a positive diameter reaction, canonical C35 guarantees contact degree at least one; no additional assumption is used.

---

## 2. The two chain contacts are outer-face contacts

At a loaded convex-hull vertex, all contact edges lie in the hull wedge. Under (LF.1), the two pentagon edges are the only incident contact edges. The bounded pentagon occupies their interior sector of angle `<pi`; the complementary graph-face sector is therefore the outer face.

Hence each loaded flat middle is a degree-two occurrence of the outer contact walk, with the same two exact unit edges that bound the cheap pentagon.

Its outer-walk turn is

```math
\tau_m=\pi-\alpha=o(1).
\tag{2.1}
```

This is a geometric statement only; no lower bound on the corresponding KKT diameter weight is asserted.

---

## 3. Charge to loaded degree slack

Canonical C35 gives

```math
1\le\deg_C(b)\le3
\qquad(b\in B).
```

Therefore

```math
\begin{aligned}
s_B
&:=3q-e_{BI}-2e_{BB}\\
&=\sum_{b\in B}(3-\deg_C b).
\end{aligned}
\tag{3.1}
```

Every loaded flat middle has degree exactly two, and the flat-middle injectivity theorem makes these source vertices distinct. Thus each contributes exactly one summand to (3.1), proving

```math
L_{flat}\le s_B.
```

The existing loaded/blocker fork says

```math
X+L_{flat}+2E_{block}
\ge(f_*-o(1))D.
```

Substituting `L_flat<=s_B` gives (LF.3).

---

## 4. Insert the exact ZI identity

The post-ZF incidence ledger defines

```math
U:=\sum_r(t_r-\delta_r-3)\ge0
```

and proves exactly

```math
\boxed{
\sum_r\delta_r+U+s_B+3k
=6+e_{BB}+3s_C,
\qquad k=d_H+s_Z.
}
\tag{4.1}
```

Thus the loaded flat-middle population is no longer a free hull count: by (LF.2), any branch with many loaded flat middles must spend the right-hand topology/stress currency in (4.1), unless it simultaneously suppresses component diameter, attachment surplus, or `k`.

Combining (LF.3) and (4.1) gives the finite inequality

```math
\boxed{
X+2E_{block}
+6+e_{BB}+3s_C
-3k-\sum_r\delta_r-U
\ge(f_*-o(1))D.
}
\tag{4.2}
```

Dropping the two nonnegative subtraction terms gives the weaker but simpler necessary condition

```math
\boxed{
X+2E_{block}+e_{BB}+3s_C-3k
\ge(f_*-o(1))D.
}
\tag{4.3}
```

Equation (4.2), not (4.3), is the lossless form.

---

## 5. Low-`t` endpoint specialization

At the AG58 safe low-`t` endpoint, the pentagon-sea calculation gives

```math
{p_5\over D}\ge0.494493172369096\ldots .
```

On `R_F=o(D)`, all but `o(D)` of these pentagons are trapezoid-close and have distinct flat middles. Thus

```math
\boxed{
{s_B+2E_{block}\over D}
\ge0.494493172369096\ldots-o(1).
}
\tag{5.1}
```

In particular either

```math
{s_B\over D}\ge0.164831057456365\ldots-o(1)
```

or

```math
{E_{block}\over D}\ge0.164831057456365\ldots-o(1)
```

after branch selection.

The first alternative is now tied to the exact ZI identity (4.1); the second remains a genuine blocker-network problem.

---

## 6. Scope and next target

- The degree-two theorem uses only convex-hull extremality, convexity of the bounded pentagon, and the `>pi/3` triangle-free separation of unit-contact rays.
- It applies after the trapezoid-stability diagonal is below any fixed `epsilon<pi/3`.
- `s_B` is a contact-degree slack, not a stress weight.
- The local KKT regression shows that unloaded blocker edges can carry arbitrarily small positive stress, so no weight lower bound is inferred.
- Equation (4.2) is exact apart from the asymptotic flat-pentagon extraction count.
- No exact unit triangle or strict sub-`D` competitor follows yet.

The loaded alternative should now be attacked through (4.1) and the near-extremal diameter-thrackle topology; the unloaded alternative through the blocker train network.

**Disposition:** proof-only structural refinement. C-II remains open.
