> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_close_normal_shared_skeleton_2026-09-18.md) · source SHA-256 `921c9fb61f8718af4178d59cbd7f74abac08c32f8eac219b5d1bd8a6a44e59e7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 6 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f5219143e8f5a7af753027efaeb75a3e008550d7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_close_normal_shared_skeleton_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5220201604f94674b3b937eda6c38d857d01f6e1e4bd93a68047188b94fd09b3"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — heavy FREE reuse also forces a close-normal shared skeleton

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; complementary metric refinement of heavy corridor reuse  
**Scope:** `HEAVY-REUSE` and its small-external common-run descendants  
**Dependencies:** multi-module FREE corridor reuse; degree-six inverse-`D` graph bound; two-sided activation-time telescope; ordered common-run extraction  
**Certificate:** `research/verify_target_c_tooth_reflection_close_normal_shared_skeleton_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The existing heavy-reuse theorem assigns each heavily reused edge to its first and last participating modules. That is the right choice when one wants a lower bound on normal separation. The same incidence set also gives a complementary assignment: every edge reused by many modules belongs to two modules whose normals are close. This yields a shared skeleton with an upper, rather than lower, angular bound.

Fix `K>h_*` and

```math
\alpha_K=1-h_*/K.
```

Suppose `m` ordered FREE modules are in the `HEAVY-REUSE` branch at threshold `R`, so at least

```math
\left(\frac{\alpha_K}{2}-o(1)\right)D
```

distinct original inverse-`D` edges occur in at least `R+1` module ancestries.

For one such heavy edge, take the `R+1` participating module normals as points on the unit circle. The cyclic angular gaps sum to `2pi`, so two participating normals have smaller angular separation at most

```math
\frac{2\pi}{R+1}.
\tag{CN.1}
```

Assign the heavy edge to one such close pair. There are at most `binom(m,2)` module pairs, hence one fixed pair `i,j` receives at least

```math
\boxed{
(\alpha_K-o(1)){D\over m^2}
}
\tag{CN.2}
```

assigned original edges. Every assigned edge is a lower gate in both module ancestries and satisfies

```math
1<|e|\le1+K/D.
\tag{CN.3}
```

If the modules come from the ordered slow-scale family with consecutive normal gap at least `gamma_D`, then this fixed pair obeys

```math
\boxed{
\gamma_D
\le
\theta_{ij}:=\angle(N_i,N_j)
\le
{2\pi\over R+1}.
}
\tag{CN.4}
```

Taking

```math
R=\lfloor\sqrt m\rfloor
```

gives

```math
\boxed{
\theta_{ij}=O(m^{-1/2})=o(1)
}
\tag{CN.5}
```

while preserving the same `Omega(D/m^2)` common-edge population as the far-pair extraction.

The degree-six matching extraction, activation-time thinning, orientation thinning, and Erdos-Szekeres ordering argument do not use a positive lower angular bound. They therefore apply verbatim to this close pair. In particular, after the same losses there is an order-coherent shared matching of size

```math
\Omega(\sqrt D/m)
```

whose selected edges have activation increments `O(m^2/D)` in both repairs.

In the small-external branch, the same lower-run-pair pigeonhole gives two fixed all-lower paths sharing

```math
q=\Omega\left({\kappa_DD^{1/4}\over Z_D+1}\right)
\tag{CN.6}
```

ordered selected gates, now with the extra angular information (CN.5).

---

## Opposite/reverse common trunks become asymptotically straight

Assume this close-normal pair reaches the parity-compatible `OPPOSITE + REVERSE-ORDER` common-trunk branch. Orient a common trunk edge vector `r` according to module `i`, and write `L=|r|`. The two-normal cone theorem gives

```math
0<r\cdot N_i<L\sin\theta_{ij}.
\tag{CN.7}
```

If `Delta_i(e)` is the lower-gate activation increment for that edge, then

```math
|r-\Delta_iN_i|=1,
```

so

```math
L^2-1
=2\Delta_i(r\cdot N_i)-\Delta_i^2
<2L\sin\theta_{ij}\,\Delta_i.
```

Therefore

```math
L-1<2\sin\theta_{ij}\,\Delta_i.
\tag{CN.8}
```

Summing over the entire common trunk and using the full ancestry activation telescope,

```math
\sum_e\Delta_i(e)\le h_*+o(1),
```

gives

```math
\boxed{
\sum_{e\subset C}(|e|-1)
\le
(2h_*+o(1))\sin\theta_{ij}
=o(1).
}
\tag{CN.9}
```

Thus the total original excess above unit length on the whole common trunk tends to zero, not merely the excess on the selected inverse-`D` matching.

Let

```math
T={N_i-N_j\over|N_i-N_j|}.
```

The opposite-traversal cone estimate gives, edge by edge,

```math
r\cdot T>|r|\cos(\theta_{ij}/2).
```

If `S_C` is the polygonal length of the trunk and `X_C` its endpoint displacement, then

```math
\boxed{
X_C\cdot T
\ge
S_C\cos(\theta_{ij}/2),
}
\tag{CN.10}
```

so

```math
\boxed{
1\le {S_C\over|X_C|}
\le \sec(\theta_{ij}/2)
=1+O(m^{-1}).
}
\tag{CN.11}
```

The common trunk is therefore an asymptotically geodesic chain. If it contains `s->infinity` selected vertex-disjoint gates, then it has at least `2s-1` edges, (CN.9) says its total edge-length slack is `o(1)`, and (CN.11) says its endpoint distance is `(1-o(1))` times its full polygonal length.

For `Z_D=o(sqrt(D))`, the existing common-run theorem has `q->infinity`, so the balanced trunk alternative has `s=sqrt(q)->infinity`. Hence an opposite/reverse survivor for the close-normal pair contains a diverging old fully inactive outer-face chain which is simultaneously:

- composed of edges longer than one;
- of total excess above unit length `o(1)`;
- confined to an `o(1)` angular cone;
- and `(1+o(1))`-geodesic between its endpoints.

This is a stricter residual geometry than the generic compatible-trunk statement. It is a nearly straight, nearly unit-spaced inactive source chain produced by two distinct reflection repairs.

The `SAME + SAME-ORDER` close-normal case is not closed by this argument: close normals make the common positive half-plane cone wide. It should continue to be attacked using the separated-pair extraction, where a lower angular bound is useful.

C-II remains open. No theorem-state authority is changed.

**Disposition:** supplemented the far-pair heavy-reuse extraction with a close-pair assignment and showed that any opposite/reverse common trunk for that pair has vanishing total slack and asymptotically unit stretch.
