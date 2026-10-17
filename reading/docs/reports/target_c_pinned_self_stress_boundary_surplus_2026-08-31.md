> Generated reading edition · [exact source](../../../docs/reports/target_c_pinned_self_stress_boundary_surplus_2026-08-31.md) · source SHA-256 `e32adca28d3b81244dc5f6e2ce08ac45f6ce798097128254766a32f9c920d961`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-0A6E1BF15A6B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C33: pinned positive self-stress sharpens the loaded-boundary count

**Date:** 2026-08-31  
**Repository base:** `cff961a6162dce12c75084aa963926a4bb6b0eea`  
**Target:** C-II  
**Depends on:** C26, canonical C30 force-visible boundary count, positive KKT equilibrium, Eppstein's triangle-free penny-graph bound  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Canonical C30 gives the global force-visible boundary estimate

```math
2q\ge \delta+2,\qquad q:=|B_+|,
```

where `delta` is the graph diameter of the connected fully force-visible contact core. The strictly positive KKT contact stress gives extra row dependencies after `B_+` is pinned.

Let

- `I=V(C)\setminus B_+`;
- `c_I` be the number of connected components of `C[I]`; and
- `e_{BB}` be the number of unit contacts with both endpoints in `B_+`.

Then

```math
\boxed{e-e_{BB}\ge2(m-q)+c_I,}
```

and therefore

```math
\boxed{2q\ge\delta+c_I+e_{BB}+2.}
```

Since `delta>=ceil(D)`, every fully force-visible survivor satisfies

```math
\boxed{q\ge\frac{\lceil D\rceil+c_I+e_{BB}+2}{2}.}
```

Thus if the loaded boundary is close to the C30 minimum, the unpinned core has few connected components and few direct loaded-loaded unit contacts.

---

## 1. Pinned decomposition

Work in the contact-minimal fully force-visible branch `C=C_*` and choose a relative-interior normalized KKT stress, so

```math
\alpha_e>0\qquad(e\in C).
\tag{C33.1}
```

Let `m=|V(C)|`, `q=|B_+|`, and pin every vertex of `B_+`. C26 identifies `B_+` with all source diameter endpoints lying in the contact core, so the canonical straight-motion contact-minimal argument gives zero pinned expansive cone and full pinned contact rank on the `2(m-q)` unpinned coordinate columns.

Let

```math
I_1,\ldots,I_{c_I}
\tag{C33.2}
```

be the connected components of the induced contact graph `C[I]`. For one component `I_r`, let `E_r` consist of all contacts internal to `I_r` together with all contacts joining `I_r` to `B_+`. The sets `E_r` are pairwise disjoint and

```math
e-e_{BB}=\sum_r|E_r|.
\tag{C33.3}
```

The pinned rigidity matrix is block diagonal across the `I_r`, so each component matrix has full column rank `2|I_r|`.

---

## 2. One independent positive left-kernel vector per unpinned component

At every `i in I`, C26 gives zero positive diameter reaction. KKT equilibrium is therefore

```math
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)=0.
\tag{C33.4}
```

Restricted to `I_r`, this is exactly a left-kernel relation for the pinned rigidity matrix on rows `E_r`, with coefficient vector given by the strictly positive contact stresses on those rows. The relation is nonzero because `I_r` is connected to the pinned set or contains an internal edge, and every participating `alpha` is positive.

Hence the left nullity of the component matrix is at least one. Full column rank then gives

```math
|E_r|\ge2|I_r|+1.
\tag{C33.5}
```

Summing over `r` proves:

### Theorem C33.1 — pinned positive-stress row surplus

```math
\boxed{e-e_{BB}\ge2(m-q)+c_I.}
\tag{C33.6}
```

The `c_I` surplus is not a generic Maxwell count; it is supplied by the actual strictly positive KKT stress, one independent dependency on each unpinned component.

---

## 3. Boundary surplus

The connected triangle-free penny contact core satisfies Eppstein's bound

```math
e\le2m-\delta-2.
\tag{C33.7}
```

Combining with C33.6 gives

```math
2m-2q+c_I+e_{BB}
\le2m-\delta-2.
```

Therefore:

### Theorem C33 — pinned self-stress boundary surplus

```math
\boxed{2|B_+|\ge\delta+c_I+e_{BB}+2.}
\tag{C33.8}
```

Since `delta>=ceil(D)`, also

```math
\boxed{|B_+|\ge\frac{\lceil D\rceil+c_I+e_{BB}+2}{2}.}
\tag{C33.9}
```

Define

```math
\sigma_B:=2q-\delta-2\ge0.
\tag{C33.10}
```

Then

```math
\boxed{c_I+e_{BB}\le\sigma_B.}
\tag{C33.11}
```

Thus a near-minimal loaded boundary, `sigma_B=o(D)`, forces

```math
c_I=o(D),\qquad e_{BB}=o(D).
\tag{C33.12}
```

---

## 4. Cyclomatic consequence

The core is connected, so its cyclomatic number is `kappa=e-m+1`. From C33.6,

```math
\boxed{\kappa\ge m-2q+c_I+e_{BB}+1.}
\tag{C33.13}
```

Hence whenever the positive contact core contains many more vertices than its `Theta(D)` loaded boundary, it necessarily contains a correspondingly large contact-cycle space. This is compatible with a two-edge-connected rhombic bulk and is not itself a contradiction.

---

## 5. Regression audit

- **Unit square:** `I=empty`, `c_I=0`, `e_BB=4`, `q=4`, `delta=2`; C33.8 is equality.
- **One large interior component:** costs exactly one self-stress surplus term, as expected.
- **Many interior islands:** each costs one additional row dependency and therefore one unit of boundary surplus.
- **C-I weak-contact branch:** not covered; strict positivity on the full contact graph is essential.

---

## Compact handoff

```text
C33:
Pin B_+ in the fully force-visible contact core.  If C[I] has c_I connected components
and e_BB loaded-loaded contact edges, the positive KKT stress gives one independent
left-kernel dependency on each unpinned component.  Full pinned rank implies
    e-e_BB >= 2(m-q)+c_I.
Eppstein e<=2m-delta-2 then gives
    2q >= delta+c_I+e_BB+2.
Therefore boundary surplus sigma_B=2q-delta-2 pays for both unpinned fragmentation and
loaded-loaded contacts:
    c_I+e_BB <= sigma_B.
```
