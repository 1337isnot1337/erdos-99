> Generated reading edition · [exact source](../../research/target_c_high_t_tb1_signed_local_window_row_unique_collapse_t18687_2026-09-17.md) · source SHA-256 `78a78a63451839f37223a707fe5024bdbefe1fb95af068a998ccd82f47b9b7fb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 8 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "845135426774ac061ad2459ee6a21040e049f16f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_tb1_signed_local_window_row_unique_collapse_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0de7ad16aefc6890369071cc552d4f2d36e5f838e3e5832e5f0b6c1c410c272e"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — ROW-UNIQUE SIGNED local windows collapse back to COMMON-CUT

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the SIGNED LOCAL-WINDOW cell reduction; no canonical promotion claimed  
**Scope:** SIGNED / LOCAL-WINDOW / ROW-UNIQUE side of the 15-spaced one-sign strong-TB1 Horn upper family through `t=(q-k)/D<=1.8687`  
**Dependencies:** SIGNED local-window cell reduction; injective Horn blocker ownership; exact path support; quarter-power SIGNED common-cut propagation  
**Certificate:** `research/verify_target_c_high_t_tb1_signed_local_window_row_unique_collapse_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The ROW-UNIQUE side of the new LOCAL-WINDOW reduction does not produce a genuinely new cell-local branch.

That reduction gives a pairwise-crossing SIGNED braid of size

```math
D^{1/4-o(1)}
```

whose exact closed path-region intervals

```math
J_A(e)=[p(e),q(e)]
```

all contain one fixed region rank `g_D`.

There are four formal interval types relative to `g_D`. The CELL-INTERNAL type

```math
p(e)=q(e)=g_D
```

can occur for at most **one** retained blocker: every Horn blocker has an injective owner coordinate which is one of its endpoint-region coordinates. If both endpoint regions equal `g_D`, its owner must equal `g_D`; two such blockers would repeat an owner.

After deleting that one possible exception, every remaining chord supports one of the two selected cuts adjacent to `R_{g_D}`:

- if `p(e)<g_D`, then `tau_{g_D}` belongs to its exact support;
- if `p(e)=g_D<q(e)`, then `tau_{g_D+1}` belongs to its exact support.

At a path endpoint only the existing adjacent cut is needed.

A two-way pigeonhole therefore leaves a `D^(1/4-o(1))` pairwise-crossing SIGNED sub-braid supporting one common selected cut. This is exactly the COMMON-CUT input already handled by the quarter-power robust-owner-grid theorem.

Hence:

```math
\boxed{
\text{SIGNED / LOCAL-WINDOW / ROW-UNIQUE}
\Longrightarrow
\text{SIGNED / COMMON-CUT at quarter-power scale}.
}
```

The only genuinely new SIGNED LOCAL-WINDOW remainder is COLUMN-UNIQUE, where the previous theorem traps the quarter-power braid in one fixed cell of the common linear train fence.

---

## 1. Internal path-cell blockers are owner-unique

Use the notation of the LOCAL-WINDOW cell theorem. Every retained blocker `e=xy` has endpoint path regions

```math
x\in R_p,
\qquad y\in R_q,
\qquad p\le q,
```

and one Horn owner coordinate

```math
o(e)\in\{p,q\}.
\tag{RC.1}
```

The ownership map is injective on the localized blocker family:

```math
e\ne f
\quad\Longrightarrow\quad
o(e)\ne o(f).
\tag{RC.2}
```

Suppose `e` is CELL-INTERNAL relative to the common Helly region `g_D`. Then

```math
p=q=g_D.
\tag{RC.3}
```

Equation (RC.1) forces

```math
o(e)=g_D.
\tag{RC.4}
```

By injectivity (RC.2), at most one retained blocker satisfies (RC.3). Thus

```math
\boxed{
N_{\rm path\text{-}internal}\le1.
}
\tag{RC.5}
```

This uses no metric estimate.

---

## 2. Every other Helly interval supports an adjacent common cut

The exact selected-cut support of a blocker with endpoint regions `p<q` is

```math
I(e)=\{p+1,\ldots,q\}.
\tag{RC.6}
```

All retained ROW-UNIQUE intervals contain `g_D`:

```math
p\le g_D\le q.
\tag{RC.7}
```

Delete the at most one internal blocker from (RC.5). Then `p<q`.

If

```math
p<g_D,
```

then

```math
p+1\le g_D\le q,
```

so

```math
\boxed{\tau_{g_D}\in I(e).}
\tag{RC.8}
```

If instead

```math
p=g_D<q,
```

then

```math
\boxed{\tau_{g_D+1}\in I(e).}
\tag{RC.9}
```

At `g_D=0`, only (RC.9) can occur; at the terminal region only (RC.8) can occur. Thus no nonexistent boundary cut is invoked.

The THROUGH type `p<g_D<q` satisfies both (RC.8) and (RC.9).

---

## 3. One common cut retains quarter-power size

The ROW-UNIQUE braid before this final step has size

```math
N_D=D^{1/4-o(1)}.
\tag{RC.10}
```

After deleting at most one chord, split it into

```math
\mathcal E^-:=\{e:p(e)<g_D\},
\qquad
\mathcal E^+:=\{e:p(e)=g_D<q(e)\}.
\tag{RC.11}
```

Equations (RC.8)--(RC.9) show that every chord in `E^-` supports `tau_{g_D}`, while every chord in `E^+` supports `tau_{g_D+1}`.

One class has cardinality at least

```math
{N_D-1\over2}=D^{1/4-o(1)}.
\tag{RC.12}
```

All geometric and Horn metadata survive because we only take a subset:

- vertex-disjointness;
- pairwise proper crossing;
- SIGNED fixed transverse projection;
- inverse-`D` near-diameter length;
- injective 15-spaced owners;
- exact path supports.

Therefore the winning class is a quarter-power SIGNED COMMON-CUT braid.

---

## 4. Feed directly into the existing common-cut theorem

The quarter-power common-cut propagation theorem now applies without any new averaging. It yields the already established robust-owner-grid fork:

```text
D^(1/4-o(1)) SIGNED chords supporting one common cut
-> D^(1/4-o(1)) far-owner crossing braid
   x D^(1/4-o(1)) robust co-phased owner rows
   x one fixed >0.0783D train family B_0
-> either
   ROW-UNIQUE one-sided logarithmic cables through polynomial row slabs,
   or
   COLUMN-UNIQUE quarter-power braid trapped in one exact B_0 fence cell/type.
```

Thus the ROW-UNIQUE half of LOCAL-WINDOW does not enlarge the frontier.

---

## 5. Updated SIGNED frontier

After the bounded-noncrossing-degree and local-window reductions, SIGNED has only the following genuinely distinct geometric outputs:

1. **COMMON-CUT normal form**, now always at quarter-power braid/owner-row scale, with its ROW-UNIQUE cable versus COLUMN-UNIQUE fixed `B_0` cell fork;
2. **LOCAL-WINDOW / COLUMN-UNIQUE**, a quarter-power pairwise-crossing braid whose exact intervals against the denser local common train fence all contain one fixed fence cell and, after a four-way split, have one common THROUGH / anchored / internal cell type.

The path-cell-anchored ROW-UNIQUE alternative has disappeared: owner injectivity forces it back onto a common selected cut.

The remaining LOCAL-WINDOW seam is therefore purely a train-fence-cell metric problem.

**Disposition:** eliminated ROW-UNIQUE as an independent SIGNED LOCAL-WINDOW escape and reduced it to the existing quarter-power COMMON-CUT theorem. C-II and Level I remain open.
