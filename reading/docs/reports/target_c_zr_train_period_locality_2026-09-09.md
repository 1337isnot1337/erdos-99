> Generated reading edition · [exact source](../../../docs/reports/target_c_zr_train_period_locality_2026-09-09.md) · source SHA-256 `1a93466a41d0fcb8367cada708a3307eb671ed9d47e7c7de03ad861359416650`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-E1F0A4C5265C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — ZPL: hole periods only lock trains that terminate on holes

**Date:** 2026-09-09  
**Repository branch:** `sol/2026-09-09-weak-transverse-train`  
**Base:** stacked on PR #111  
**Run type:** exact train-period locality and finite shear modes  
**Target:** ZRC/ZTF macroscopic rhombic component  
**Depends on:** DT, ZRC, ZTF  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

ZTF counts train-angle infinitesimal modes after allowing arbitrary linear coupling through the hole-period equations. The period matrix is much sparser than that worst-case count: a train angle enters the period of a bounded hole only when that train has an endpoint edge on the boundary of that hole.

Consequently a train whose two stopped endpoints lie on the **outer boundary component of the rhombic sea** is completely absent from every hole-period equation. Its angle can be changed by itself, at finite amplitude, while all other train directions remain fixed. Every rhombus continues to close and every hole period remains exactly zero, so all contact edges of the rhombic component stay exactly unit.

Thus outer-to-outer component trains are explicit one-parameter shear mechanisms of the free rhombic sea. The only obstruction to using them against the full source is external locking by contacts/diameter geometry outside the component.

---

## 1. Boundary endpoints of component trains

Let `Q` be an edge-connected strict-rhombic component. DT/ZRC gives a stopped-train path decomposition of its contact edges.

Every train has exactly two endpoint contact edges, and every endpoint edge lies on the boundary of `Q`.

The planar complement of `Q` has

- one unbounded component, whose boundary edges will be called **outer component-boundary edges**;
- `g` bounded complementary components `H_1,...,H_g`, called holes.

For a train `tau`, classify its endpoints as

- outer/outer;
- outer/hole;
- hole/hole.

A train may have both endpoints on the same hole or on distinct holes.

---

## 2. A hole period contains exactly its endpoint trains

Orient one boundary walk `partial H_j` of a bounded hole. For train `tau`, let

```math
n_{j\tau}\in\mathbb Z
```

be the signed number of boundary edges of `partial H_j` that belong to `tau`, with sign determined by whether their oriented edge vector is `+u_tau` or `-u_tau`.

Because a stopped train is a path, it can meet a component boundary only at its endpoint edges. Therefore

```math
\boxed{
 n_{j\tau}\ne0
\Longrightarrow
\tau\text{ has an endpoint on }\partial H_j.
}
\tag{ZPL1}
```

The finite vector period of the hole is

```math
\boxed{
\sum_{\tau=1}^T n_{j\tau}u_\tau=0.
}
\tag{ZPL2}
```

This is simply the polygonal closure of the hole boundary, grouped by train directions.

Its infinitesimal derivative under train-angle velocities `t_tau` is

```math
\boxed{
\sum_\tau n_{j\tau}t_\tau Ju_\tau=0,
}
\tag{ZPL3}
```

which is the corresponding row pair of ZTF's period map.

By ZPL1, every column of the period map is supported only on holes at which that train terminates.

---

## 3. Outer-to-outer trains are absent from all hole periods

If `tau` has both endpoint edges on the outer component boundary, it has no endpoint on any bounded hole. Therefore

```math
 n_{j\tau}=0
\qquad(j=1,...,g).
```

Hence:

### Theorem ZPL.1 — free period column

For every outer-to-outer component train `tau`, the coordinate vector

```math
e_\tau\in\mathbb R^T
```

belongs to the ZTF infinitesimal period kernel.

Equivalently, varying only the angle of `tau` produces a nontrivial train-angle infinitesimal flex of the free rhombic component.

Different outer-to-outer trains give linearly independent coordinate flexes.

---

## 4. The one-train shear is finite, not merely infinitesimal

Fix an outer-to-outer train `tau_0`. For small real `theta`, replace its train vector by

```math
u_{\tau_0}(\theta)
:=R_\theta u_{\tau_0}
```

and leave every other train vector unchanged.

For every rhombus face, opposite sides belonging to the same train remain opposite parallel unit vectors. Therefore every rhombus boundary still closes exactly.

For every bounded hole `H_j`, ZPL1 gives

```math
n_{j,\tau_0}=0.
```

Thus its finite period remains

```math
\sum_{\tau\ne\tau_0}n_{j\tau}u_\tau
+n_{j,\tau_0}R_\theta u_{\tau_0}
=0.
```

All hole periods remain exactly closed.

It follows that the modified unit edge-vector assignment is globally integrable on `Q`: fix one vertex position and integrate edge vectors along paths. Face and hole closure make the result path-independent.

Hence:

### Theorem ZPL.2 — exact one-train shear

Every outer-to-outer train of a finite edge-connected rhombic component generates a one-parameter family of exact unit-edge realizations of that component, obtained by rotating only that train direction.

For sufficiently small `theta`, all rhombi remain nondegenerate and retain angles in `(60,120)` degrees. Since the component is finite, all noncontact vertex pairs that have strict distance slack remain strictly separated for sufficiently small `theta`.

Thus this is a genuine local bar-preserving deformation of the isolated rhombic component, not only an infinitesimal formal mode.

---

## 5. Geometric form of the shear

Remove the train edges of `tau_0` from the rhombic component's edge graph. The train is a simple pseudoline path from one outer component-boundary edge to another. In the planar component it separates the rhombic faces locally into two shores; across each train edge the modified edge vector changes by

```math
(R_\theta-I)u_{\tau_0}.
```

Accordingly, after choosing one shore as reference, the other shore undergoes the same relative translation increment each time a path crosses the train. In a simply connected disk this is the familiar train shear. With holes, ZPL2 shows that the outer-to-outer hypothesis is exactly what prevents any nonzero period obstruction.

No claim is made that the complete source outside `Q` follows this shear rigidly.

---

## 6. Endpoint-type split for the weak-rich train family

Apply ZPL to the ZRC macroscopic component `Q_*`, which contains `Omega_eta(D)` weak-rich trains.

Let

```math
N_{oo},N_{oh},N_{hh}
```

be the numbers of weak-rich trains of the three endpoint types. Then

```math
N_{oo}+N_{oh}+N_{hh}=\Omega_\eta(D).
\tag{6.1}
```

There are two structural alternatives.

### ZPL-A — many outer-to-outer weak trains

If

```math
N_{oo}=\Omega_\eta(D),
```

then the free rhombic sea contains `Omega_eta(D)` linearly independent **exact one-train shear mechanisms**, each attached to a train that is weak on `Omega_eta(D)` rhombi.

The full globally rigid source must lock these modes entirely through the external contact/diameter constraints incident to the component boundary.

### ZPL-B — many hole-ending weak trains

Otherwise

```math
N_{oh}+N_{hh}=\Omega_\eta(D).
```

Each such train consumes at least one hole-boundary endpoint incidence. Therefore the bounded-hole boundary of `Q_*` itself has linear length:

```math
\boxed{
B_{hole}=\Omega_\eta(D).
}
\tag{ZPL4}
```

So the weak-train degeneration is then tied to a linearly large internal defect boundary rather than the outer component boundary.

Both alternatives are substantially more specific than the raw `O(D)` total boundary statement.

---

## 7. Relation to the full source

ZPL2 preserves every contact edge belonging to the rhombic component. It does **not** automatically preserve

- contact edges incident to component vertices but lying outside `Q_*`;
- diameter constraints involving component vertices;
- unit separation from source points outside the component.

Those are precisely the locking constraints that must prevent the one-train shear in the actual global minimizer.

The next theorem should quantify that locking. In ZPL-A, the source must independently block `Omega(D)` explicit shears using only an `O(D)` boundary/diameter system. In ZPL-B, a positive fraction of the component's linear boundary is internal hole boundary and should be coupled to the PI/PC/GU exceptional-pocket currencies.

---

## 8. Exact next target

The two shortest routes are now:

1. **Outer-shear locking theorem:** show that the ZSP/ZHA loaded-boundary geometry cannot lock `Omega(D)` independent outer-to-outer weak train shears without producing an `Omega(1/D)` response defect or a strict sub-`D` motion.
2. **Hole-boundary charge theorem:** show that `Omega(D)` weak-rich trains ending on bounded holes force enough exceptional-face perimeter/area loss to enter the already constrained PI/GU high-gap branch.

The oblique-grid regression corresponds to ZPL-A with its outer boundary artificially clamped. The missing source-specific fact is that the actual clamp is itself part of the diameter-minimizing point configuration.

---

## 9. Classification

**Status:** proved report-level exact deformation/locality theorem.  
**Level I:** still open.  
**External literature:** none.  
**Computation:** none.
