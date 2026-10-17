> Generated reading edition · [exact source](../../../docs/reports/target_c_harmonic_component_diameter_cost_2026-08-31.md) · source SHA-256 `5488ff6f7ff1012459e3e4e0575dfd9269428b89615eff1af754d692f6801cfe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2C520474A318","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_harmonic_component_diameter_cost_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=919863c58ec59be9fafebfb4eb5fc4aff168787f; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C40: each harmonic interior diameter costs loaded-boundary contacts

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C33, C35-C38, positive KKT self-stress, Eppstein 2018  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let `I_r` be one connected component of the unpinned contact graph `C[V(C)\setminus B_+]`. Write

- `n_r=|I_r|`;
- `e_r` for its internal unit contacts;
- `t_r` for the number of unit contacts from `I_r` to `B_+`; and
- `delta_r` for the graph diameter of `C[I_r]`, with `delta_r=0` for a singleton.

After pinning `B_+`, the component rigidity matrix has full rank `2n_r`. The strictly positive KKT contact stress supplies a nonzero left-kernel dependency. Hence

```math
e_r+t_r\ge2n_r+1.
```

Eppstein gives

```math
e_r\le2n_r-\delta_r-2.
```

Therefore

```math
\boxed{t_r\ge\delta_r+3.}
```

This strengthens C35's `t_r>=3` by charging every unit of internal graph diameter to an additional loaded-boundary contact.

Since every loaded vertex has full contact degree at most three,

```math
\boxed{\delta_r\le3|A_r|-3,}
```

where `A_r` is the distinct loaded attachment set from C36.

Summing over all unpinned components gives

```math
\boxed{
\sum_r\delta_r+3c_I
\le e_{BI}
\le3q-2e_{BB},}
```

hence

```math
\boxed{
\sum_r\delta_r
\le3q-2e_{BB}-3c_I.}
```

Thus the harmonic interior components also share an `O(D)` total graph-diameter budget.

---

## 1. Pinned component rank with positive self-stress

Pin every loaded vertex `B_+`. The global pinned rigidity matrix is block diagonal by the connected components `I_r` of the unpinned graph. Contact minimality gives zero pinned expansive cone, so the block for `I_r` has full column rank

```math
2n_r.
\tag{C40.1}
```

Its rows are exactly the `e_r` internal contacts and the `t_r` contacts from `I_r` to `B_+`.

At every unpinned vertex, positive diameter reaction is zero. Restricting the strictly positive KKT contact stress to these `e_r+t_r` rows gives a nonzero left-kernel vector. Hence left nullity is at least one and

```math
\boxed{e_r+t_r\ge2n_r+1.}
\tag{C40.2}
```

This is the componentwise source of the global C33 surplus.

---

## 2. Eppstein converts row surplus into boundary-contact cost

The induced graph `C[I_r]` is a connected triangle-free penny graph. Eppstein's bound applies:

```math
\boxed{e_r\le2n_r-\delta_r-2.}
\tag{C40.3}
```

For `n_r=1`, this reads `0<=0` with `delta_r=0`.

Combine C40.2 and C40.3:

```math
2n_r+1
\le e_r+t_r
\le2n_r-\delta_r-2+t_r.
```

Therefore:

### Theorem C40.1 — harmonic component diameter cost

```math
\boxed{t_r\ge\delta_r+3.}
\tag{C40.4}
```

C35 is the `delta_r>=0` corollary.

---

## 3. Distinct attachment-set consequence

Let `A_r` be the distinct loaded vertices adjacent to `I_r`. Every boundary contact counted by `t_r` has its loaded endpoint in `A_r`. C35 gives

```math
\deg_C(b)\le3
\qquad(b\in B_+).
```

Therefore each `b in A_r` contributes at most three of the `t_r` contact edges, so

```math
t_r\le3|A_r|.
\tag{C40.5}
```

Together with C40.4:

### Corollary C40.2

```math
\boxed{
\delta_r\le3|A_r|-3.}
\tag{C40.6}
```

Thus a harmonic component spanning large contact-graph distance requires a proportionally large distinct loaded attachment set.

This is compatible with C36's localization `I_r subset conv(A_r)` and turns that qualitative hull statement into a graph-distance charge.

---

## 4. Global interior-diameter budget

Sum C40.4 over all `c_I` components:

```math
\sum_r\delta_r+3c_I
\le\sum_rt_r
=e_{BI}.
\tag{C40.7}
```

C35's loaded degree budget is

```math
e_{BI}+2e_{BB}\le3q.
\tag{C40.8}
```

Hence:

### Theorem C40.3 — global harmonic interior diameter budget

```math
\boxed{
\sum_r\delta_r+3c_I+2e_{BB}\le3q,}
\tag{C40.9}
```

and in particular

```math
\boxed{
\sum_r\delta_r\le3q-2e_{BB}-3c_I.}
\tag{C40.10}
```

Canonical C30 gives `q=O(D)` from convex perimeter, so the total internal graph diameter of all harmonic response components is `O(D)`.

---

## 5. Population consequence

Choose one vertex in `I_r`. Every vertex of the component lies within Euclidean distance at most `delta_r` of it. Disjoint radius-`1/2` disks around the unit-separated vertices lie inside a disk of radius `delta_r+1/2`. Thus

```math
\boxed{n_r\le(2\delta_r+1)^2.}
\tag{C40.11}
```

Combined with C40.6,

```math
\boxed{n_r\le(6|A_r|-5)^2.}
\tag{C40.12}
```

This is crude but exact: a component with `Theta(D^2)` vertices must have `Theta(D)` distinct loaded attachment vertices.

---

## 6. Near-minimal response effect

In the C33 near-minimal phase `sigma_B=o(D)`, C38 says all but `o(D)` loaded vertices belong to exactly one of `o(D)` noncrossing attachment sets. C40 adds:

- every component's internal graph diameter is at most three times its attachment-set size minus three;
- all interior component diameters together are `O(D)`;
- a macroscopically populated interior component must consume a macroscopic fraction of the loaded boundary.

Thus a response closing theorem can split further between:

1. one or a few components with `Omega(D)` attachment sets and potentially `Theta(D^2)` population; or
2. only submacroscopic components, whose individual diameter/population is controlled by correspondingly smaller attachment sets.

---

## 7. Regression audit

- A single interior vertex has `delta=0` and requires `t>=3`, sharp.
- A long reaction-free chain with two pins would violate `t>=delta+3`; it was already excluded by C26, and C40 quantifies the failure.
- Multiple contacts from one loaded pin to a component are allowed; this is why C40.6 has coefficient three rather than one.

```text
C40:
For unpinned component I_r, pinned full rank plus one positive KKT left-kernel relation
gives e_r+t_r>=2n_r+1.  Eppstein gives e_r<=2n_r-delta_r-2.  Therefore
    t_r>=delta_r+3.
Since each loaded pin has contact degree <=3,
    delta_r<=3|A_r|-3.
Globally
    sum delta_r+3c_I+2e_BB<=3|B_+|.
Thus all harmonic response components share an O(D) total internal graph-diameter
budget, and any macroscopic component needs a macroscopic loaded attachment set.
```
