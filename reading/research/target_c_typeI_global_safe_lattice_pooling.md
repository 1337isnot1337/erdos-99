> Generated reading edition · [exact source](../../research/target_c_typeI_global_safe_lattice_pooling.md) · source SHA-256 `2c1ff39f5139fb2c26701d60d2333c7f60a8b7ca7a273f908e319f514624bf60`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "74576836d6a8eb74a49322433ca86353fcdc64ac", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_typeI_global_safe_lattice_pooling.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1b927436164a6cb3c41abbfd7989c7c30d0cb93f14b6f37962f39c49c89db148"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — global safe-lattice pooling for both Type-I container geometries

**Date:** 2026-09-12  
**Status:** proof-only research theorem; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

Audited-working Section 165 proves that either Type-I macroscopic inactive container
closes if its own depth-one packing capacity can absorb a vertex cover of the complete
actual diameter graph. The internal force-hull chamber system admits a stronger safe
region: contact-wall and hull-outer-pocket shields recover boundary area that a full
collar would discard.

These two sources of capacity can be pooled. In the genuine exterior-cap branch, keep
Section 165's full depth-one collar for the exterior cap, but combine it with every safe
inactive chamber inside the force hull and use one common translated triangular
lattice. The same construction also contains the purely internal branch as the case
with no exterior cap.

No mixed-wall assertion is made about the Section-80/162 exterior cap.

---

## 1. Two disjoint inactive regions

Let `F` be the force hull and `K=conv(A)` the full source hull.

Inside `F`, let

```math
 S_F=\bigcup_j S_j
```

be the union of the safe regions from the aggregate inactive-chamber theorem, and let

```math
 Z_F:=Z_{ch}=N_F-m
```

be all contact-isolated source points assigned to those chambers.

If the Type-I alternative is the genuine exterior-cap branch of Sections 80/162, let
`C_E subset K\setminus int F` be the selected convex exterior cap and let `Z_E` be its
assigned contact-isolated source set, of cardinality `z_E`. Audited-working Section 165
defines

```math
 C_{E,-1}:=\{x\in C_E:dist(x,partial C_E)>1\}.
\tag{1.1}
```

Put

```math
 S_E:=C_{E,-1}.
```

If there is no selected exterior cap, set `S_E=emptyset` and `z_E=0`.

The interiors of `S_F` and `S_E` are disjoint: `S_F subset int F`, while the interior
of a Section-80/162 exterior cap lies on the exterior side of its force-hull chord.
Their boundaries are irrelevant for area and lattice counting.

Define the pooled safe region

```math
 S_{all}:=S_F\cup S_E.
\tag{1.2}
```

---

## 2. One lattice translate protects cross-region separation

Let `Lambda` be the unit triangular lattice, of covolume

```math
 a_0={\sqrt3\over2}.
```

For every translate `Lambda+t`, every two distinct points of
`(Lambda+t) cap S_all` have distance at least one, even if they lie in different
inactive regions.

Translation averaging gives

```math
 \boxed{
 \max_t |(\Lambda+t)\cap S_{all}|
 \ge\left\lfloor{area(S_{all})\over a_0}\right\rfloor.
 }
\tag{2.1}
```

The advantage is structural: the internal chamber system and the exterior cap share
one lattice phase and one integer floor.

---

## 3. Pooled diameter-cover repacking

Let `H` be the complete actual diameter graph and `U` a minimum vertex cover, so
`|U|=tau(H)`.

The sets `Z_F`, `Z_E`, and `U` are pairwise disjoint. The first two consist of assigned
contact-isolated inactive source points. The cover consists of loaded actual-diameter
endpoints. The internal and exterior assigned populations lie in disjoint container
regions.

### Theorem 3.1 — global Type-I safe-lattice pooling

If

```math
 \boxed{
 \left\lfloor{area(S_{all})\over a_0}\right\rfloor
 \ge Z_F+z_E+\tau(H),
 }
\tag{3.1}
```

then the source is not a global diameter minimizer.

#### Proof

Choose one lattice translate with at least the right-hand side of (3.1) points in
`S_all`, retain exactly that many, and call the resulting set `Y`. Define

```math
 A':=(A\setminus(Z_F\cup Z_E\cup U))\cup Y.
\tag{3.2}
```

Pairwise disjointness of the deleted sets gives `|A'|=|A|`.

New-new distances are at least one because all new points come from one unit-lattice
translate.

Let `y in Y cap S_F`. It lies in one force-hull chamber safe region. Every retained old
source point lies outside that chamber interior, so the corresponding contact-wall or
hull-outer-pocket shield gives distance at least one from `y` to every retained old
source.

Let `y in Y cap S_E`. Section 165's protected-depth argument applies: every retained
old source point outside `int C_E` is at distance strictly greater than one from
`C_{E,-1}`. All old points assigned to `C_E` were removed. Thus new-old separation
holds also for exterior-cap lattice points.

The cover `U` removes every old-old pair at distance exactly `D`. Every new point lies
in `int K`: the internal safe regions lie in `int F subset int K`, and Section 165
proves `C_{E,-1} subset int K`. For `x in K` and `y in int K`, `|x-y|<D`.
Consequently every pair involving a new point is strictly subdiametral.

The finite set `A'` is therefore a same-cardinality unit-separated configuration of
diameter strictly below `D=D(n)`, contradiction. `square`

The competitor need not remain triangle-free.

---

## 4. Scalar criterion using the internal residual theorem

The aggregate internal-chamber theorem proves

```math
 {area(S_F)\over a_0}-Z_F\ge\Xi,
\tag{4.1}
```

with

```math
 \Xi=R_F
 -\kappa_*L_c
 -\lambda_*L_{add}
 -C_*f
 -\eta_*a.
\tag{4.2}
```

For the selected genuine exterior cap define its **real protected lattice spare**

```math
 \Psi_E:={area(C_{E,-1})\over a_0}-z_E.
\tag{4.3}
```

Set `Psi_E=0` when no exterior cap is selected.

Because `Z_F+z_E` is an integer,

```math
\begin{aligned}
 \left\lfloor{area(S_{all})\over a_0}\right\rfloor-(Z_F+z_E)
 &=\left\lfloor
 {area(S_F)\over a_0}-Z_F
 +{area(C_{E,-1})\over a_0}-z_E
 \right\rfloor\\
 &\ge\lfloor\Xi+\Psi_E\rfloor.
\end{aligned}
\tag{4.4}
```

Hence the finite closing criterion is

```math
 \boxed{
 \Xi+\Psi_E\ge\tau(H)
 \quad\Longrightarrow\quad
 \text{strict global diameter contradiction}.
 }
\tag{4.5}
```

Every surviving Type-I configuration therefore satisfies

```math
 \boxed{
 \Xi+\Psi_E<\tau(H)
 \le\left\lceil{q\over2}\right\rceil.
 }
\tag{4.6}
```

The second inequality is audited-working Section 165's Woodall cover bound.

In the purely internal branch `Psi_E=0`, recovering the aggregate chamber criterion.
In the exterior-cap branch, (4.6) is strictly stronger than asking the exterior cap to
pay the entire cover alone whenever the internal safe system has positive realized
spare.

---

## 5. Comparison with Section 165

Section 165's lattice baseline for the exterior cap uses only

```math
 area(C_{E,-1})/a_0.
```

The pooled theorem adds all usable force-hull chamber area before lattice translation.
It does not require separate integer packings in the two regions and therefore loses
no independent rounding term.

This is not a new geometric claim about the exterior-cap boundary. The cap protection
is exactly Section 165's full depth-one collar. The improvement is the source-level
pooling of otherwise disjoint inactive capacity.

---

## 6. Remaining obstruction

The full Type-I branch would close if canonical container geometry forced

```math
 \Xi+\Psi_E\ge\tau(H)
```

in the exterior-cap case and `Xi>=tau(H)` in the internal case.

The present theorem does not establish those lower bounds. It reduces both Type-I
alternatives to one common source-level capacity currency while preserving every source
point and the complete diameter-graph quantifier.

Contact-isolated points never enter the Section-57 affine-kernel theorem.
