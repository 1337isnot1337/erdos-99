> Generated reading edition · [exact source](../../research/target_c_contact_chain_safe_area_capacity.md) · source SHA-256 `e7f504be12601518f4aae9cf845d04e87e88decfc433f45f9d9e7c40f2172cbe`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f60f9a3639e14091ca689094e6cb525c4938f648", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_contact_chain_safe_area_capacity.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a3db19dbaab4c354badd87ab0a572d88f7cef83fb304f3db3e925742ff358b85"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — exact contact-chain safe-area and lattice-capacity bound

**Date:** 2026-09-12  
**Status:** proof-only research theorem; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

The contact-wall and mixed-wall repacking theorems reduce Type-I capacity to the area
of a region protected by boundary source vertices rather than by a full unit collar.
This note proves an exact universal area bound for that protected region.

The key constant is

```math
 c_*:={\pi\over6}+{\sqrt3\over4},
 \qquad
 g_*:=1-c_*>0.
\tag{0.1}
```

Numerically `c_*=0.9566...` and `g_*=0.04338...`. No numerical value is used in the
proof.

For every unit contact edge in a convex boundary chain, the next boundary-vertex unit
disk contributes at most `c_*` new one-sided forbidden area. The estimate is exact for
a straight infinite unit chain and requires no turning, inradius, or near-disk
hypothesis.

Combined with triangular-lattice translation averaging, this converts the Oler
residual of a Type-I inactive chamber into a constructive lower bound on actual
same-container packing slots.

---

## 1. One-edge incremental disk area

Let

```math
 p=(0,0),\qquad q=(1,0),\qquad H=\{(x,y):y\ge0\}.
```

Let `B_p,B_q` be the closed unit disks centered at `p,q`.

### Lemma 1.1

```math
 \boxed{
 \operatorname{area}\bigl((B_q\cap H)\setminus B_p\bigr)
 =c_*={\pi\over6}+{\sqrt3\over4}.
 }
\tag{1.1}
```

#### Proof

The half-disk `B_q cap H` has area `pi/2`. The overlap of two unit disks whose centers
are one unit apart has full area

```math
 2\cos^{-1}(1/2)-{1\over2}\sqrt{4-1}
 ={2\pi\over3}-{\sqrt3\over2}.
```

The overlap is symmetric across the line `pq`, so its part in `H` has area

```math
 {\pi\over3}-{\sqrt3\over4}.
```

Subtracting from `pi/2` gives (1.1). `square`

Put also

```math
 h_*:={\pi\over2}-c_*
 ={\pi\over3}-{\sqrt3\over4}.
\tag{1.2}
```

---

## 2. Any convex unit-contact path has a linear forbidden-area bound

Let `C` be a convex polygon and suppose one boundary arc is the unit-contact path

```math
 W=(p_0,p_1,\ldots,p_\ell),
 \qquad |p_i-p_{i-1}|=1.
```

Let

```math
 U_W:=C\cap\bigcup_{i=0}^{\ell}\overline B(p_i,1).
```

### Theorem 2.1 — contact-chain disk-union bound

```math
 \boxed{
 \operatorname{area}(U_W)
 \le {\pi\over2}+\ell c_*.
 }
\tag{2.1}
```

#### Proof

The first disk satisfies

```math
 C\cap B(p_0,1)
 \subseteq B(p_0,1)\cap H_0,
```

where `H_0` is the interior half-plane of the first boundary edge
`[p_0,p_1]`. Therefore its area is at most `pi/2`.

For `i>=1`, let `H_i` be the interior half-plane bounded by the preceding contact edge
`[p_{i-1},p_i]`. Convexity gives `C subset H_i`. The part of the `i`th disk not already
covered by the earlier disks is contained in

```math
 \bigl(B(p_i,1)\cap H_i\bigr)\setminus B(p_{i-1},1).
```

Rigidly moving the unit edge to the model of Lemma 1.1 shows that this set has area
exactly `c_*`. Summing the first contribution and the `ell` increments proves (2.1).
`square`

No relation between nonconsecutive boundary vertices is used.

---

## 3. Internal exceptional face: safe-area lower bound

Let `C` be a convex internal contact face with `m` unit boundary edges and vertices
`p_0,...,p_{m-1}`. Define the fixed-boundary safe region

```math
 S_\partial(C)
 :=\{y\in\operatorname{int}C:|y-p_i|\ge1\ \forall i\}.
\tag{3.1}
```

Apply Theorem 2.1 to the boundary path
`p_0,p_1,...,p_{m-1}`, using only `m-1` of the `m` unit edges. The forbidden union of
all boundary-vertex disks has area at most

```math
 {\pi\over2}+(m-1)c_*=mc_*+h_*.
\tag{3.2}
```

Therefore

```math
 \boxed{
 \operatorname{area}S_\partial(C)
 \ge A_C-mc_*-h_*.
 }
\tag{3.3}
```

Since `c_*=1-g_*`, this may also be written

```math
 \operatorname{area}S_\partial(C)
 \ge A_C-m+g_*m-h_*.
\tag{3.4}
```

Thus replacing full distance-one edge erosion by endpoint guards recovers a universal
linear area coefficient `g_*` before any packing argument.

---

## 4. Exterior cap: closing chord plus contact path

Let `C` be a convex exterior cap with closing chord `[u,v]` of length

```math
 s=|u-v|
```

and complementary unit-contact path

```math
 u=p_0,p_1,\ldots,p_\ell=v.
```

Let `S_mix(C)` be the mixed-wall region: distance at least one from `[u,v]` and from
every `p_i`.

The one-sided unit neighborhood of a boundary segment of length `s` has area

```math
 s+{\pi\over2}.
\tag{4.1}
```

It already contains the full unit disks centered at the chord endpoints `p_0,p_ell`.
Starting with this chord neighborhood and adding only the internal path-vertex disks
`p_1,...,p_{ell-1}`, Theorem 1.1 bounds every new contribution by `c_*`. Hence

```math
 \operatorname{area}\left(
 C\cap\left[N_1([u,v])\cup\bigcup_{i=0}^{\ell}B(p_i,1)\right]
 \right)
 \le s+{\pi\over2}+(\ell-1)c_*.
\tag{4.2}
```

Consequently

```math
 \boxed{
 \operatorname{area}S_{mix}(C)
 \ge A_C-s-\ell c_*-h_*.
 }
\tag{4.3}
```

Since `per(C)=s+ell`, this is

```math
 \boxed{
 \operatorname{area}S_{mix}(C)
 \ge A_C-\operatorname{per}(C)+g_*\ell-h_*.
 }
\tag{4.4}
```

The gain `g_* ell` is the precise linear benefit of using the unit-contact wall
instead of eroding that boundary arc geometrically.

---

## 5. Triangular-lattice realization

Let `Lambda` be the unit triangular lattice of covolume

```math
 a_0={\sqrt3\over2}.
```

Translation averaging gives, for every bounded measurable safe region `S`,

```math
 \max_t |(\Lambda+t)\cap S|
 \ge \left\lfloor{\operatorname{area}S\over a_0}\right\rfloor.
\tag{5.1}
```

All selected points are pairwise unit-separated. The contact-wall and mixed-wall
shield theorems then guarantee separation from all retained old source points.

### 5.1 Internal-face capacity in residual variables

Let

```math
 r_\partial
 ={A_C\over a_0}-{m\over2}+1-z_C
```

be the exact internal-face Oler residual from the contact-wall theorem. Then

```math
 {A_C\over a_0}=z_C+r_\partial+{m\over2}-1.
\tag{5.2}
```

Define

```math
 \kappa_*:={\pi\over3\sqrt3},
 \qquad
 C_*:={1\over2}+{2\pi\over3\sqrt3}.
\tag{5.3}
```

Because

```math
 {c_*\over a_0}={1\over2}+\kappa_*,
 \qquad
 {h_*\over a_0}=2\kappa_*-{1\over2},
\tag{5.4}
```

(3.3), (5.1), and (5.2) give

```math
 \boxed{
 M_\partial(C)-z_C
 \ge
 \left\lfloor
 r_\partial-\kappa_*m-C_*
 \right\rfloor.
 }
\tag{5.5}
```

Therefore the internal Type-I branch is eliminated whenever

```math
 \boxed{
 r_\partial
 \ge \tau(H)+\kappa_*m+C_*.
 }
\tag{5.6}
```

This is a genuine lower realization theorem: it uses lattice averaging, not a reverse
Oler inference.

### 5.2 Exterior-cap capacity in residual variables

For an exterior cap, let `k_C=ell+1` be its augmented graph-boundary vertex count and
let

```math
 \sigma_C={A_C\over a_0}+{s+\ell\over2}+1-z_C,
 \qquad
 r_C:=\sigma_C-k_C.
\tag{5.7}
```

Thus

```math
 {A_C\over a_0}=z_C+r_C+{\ell\over2}-{s\over2}.
\tag{5.8}
```

Put

```math
 \lambda_*:={2\over\sqrt3}+{1\over2}.
\tag{5.9}
```

Equations (4.3), (5.1), and (5.8) give

```math
 \boxed{
 M_{mix}(C)-z_C
 \ge
 \left\lfloor
 r_C-\kappa_*\ell-\lambda_*s-{h_*\over a_0}
 \right\rfloor.
 }
\tag{5.10}
```

Hence the exterior Type-I branch is eliminated whenever

```math
 \boxed{
 r_C
 \ge
 \tau(H)+\kappa_*\ell+\lambda_*s+{h_*\over a_0}.
 }
\tag{5.11}
```

The closing chord is more expensive than a unit-contact side because it lacks a
unit-edge crossing shield.

---

## 6. Interaction with residual conservation

The companion residual-conservation theorem proves

```math
 \sum_j r_j=R_F,
```

where `R_F` is the single punctured force-hull Oler residual.

Equations (5.6) and (5.11) now give explicit **realization thresholds** for the
individual chamber residuals. A Type-I survivor must keep the selected macroscopic
container below the appropriate threshold; otherwise the triangular-lattice translate
plus diameter-cover replacement gives a strict same-cardinality diameter decrease.

This does not yet force one chamber above threshold. It does, however, replace the
previous qualitative question "does Oler slack correspond to spare capacity?" by an
explicit theorem with sharp local chain constant `c_*` and a precise remaining
residual deficit.

---

## 7. Scope

- The internal theorem uses only convexity and a unit-contact boundary cycle.
- The exterior theorem uses exactly one artificial closing chord plus a complementary
  unit-contact path, as supplied by the canonical cap geometry.
- No lower bound on contact weights or KKT response is used.
- Contact-isolated points remain part of the full source and never enter the Section-57
  affine-kernel theorem.
- The replacement competitor need not be triangle-free.
- Floors are kept explicitly; all closure thresholds are finite, not merely
  asymptotic.
