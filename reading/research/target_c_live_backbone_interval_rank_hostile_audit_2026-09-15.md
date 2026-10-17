> Generated reading edition · [exact source](../../research/target_c_live_backbone_interval_rank_hostile_audit_2026-09-15.md) · source SHA-256 `f1b2cd8783dec036856fa1b0a5179c6b0fd8bc20431e04112052bf80193e68e4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b292de65d8fe315eeb4a6179e7567b584c552ccf", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_live_backbone_interval_rank_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0a271a3674b171ee3c58931bd3c75d38eff64e7b169bac41f390b599f0b5fae2"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — live `0.017104D` O--O backbone and diameter-interval rank

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_live_backbone_interval_rank_t1844_2026-09-15.md`  
**Base:** `c0e3cfd451bbc80b796a5a984940dd70977fb8ac`  
**Disposition:** **PASS at proof-only `t<=1.844` full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate avoids the final consecutive-block extraction in the current rectangle proof and instead uses the longer good-leaf dual-tree path already crossed by one center train.  It then combines exact tree shore coordinates with simultaneous train-shear mixed rigidity.

The claimed conclusions are:

- a live smallest-leaf O--O backbone of length `>0.017104D-o(D)`;
- at least `m-2` actual diameter edges with proper nonempty crossing intervals on an `m`-cut backbone;
- actual diameter incidence changes at at least `ceil(m/2)-1` distinct internal strip boundaries;
- exact KKT-resultant total variation at most `2D`; and
- an adjacent live cut pair with resultant difference `<117+o(1)`.

All claims pass.  The proof does not inherit the now-excluded `t<=1.8436` two-leaf branch; it uses only the uniform `t<=1.844` smallest-leaf fan/rectangle inputs and is therefore nonvacuous on the surviving band `1.8436<t<=1.844`.

---

## 1. The `0.017104D` backbone arithmetic is a direct parent-theorem specialization

The audited `0.7404D` fan profile gives, for a good-leaf threshold `lambda`,

```math
g(\lambda)
={ (0.7404-\lambda)(0.0848)\over1.063-\lambda}
```

retained good-leaf weight per `D`.  Since every retained pair weight is at most one, the distinct good-leaf train count is at least `g(lambda)D-o(D)`.

Every good leaf has more than `lambda D` center neighbors, while the total center count is below `1.063D+o(D)`.  Averaging therefore produces one center train whose crossing set in the good-leaf complement dual has path length

```math
s(\lambda)D-o(D),
\qquad
s(\lambda)={\lambda g(\lambda)\over1.063}.
```

At the candidate's exact choice `lambda=477/1000`,

```math
g={69801\over1831250}
=0.0381165870\ldots,
```

```math
s={33295077\over1946618750}
=0.01710405645\ldots>0.017104.
```

The center train's crossing set is a simple dual-tree path by the already-audited rectangle topology.  No complete-neighborhood block estimate is needed.

**Verdict:** PASS.

---

## 2. One diameter edge has one signed interval on the rooted path

For a rooted tree path, a cut edge separates two endpoint regions exactly when it belongs to their unique tree path.  Intersection of two tree paths is connected.  Therefore the nonzero shore incidences of one diameter edge form one interval.

The sign cannot flip inside that interval: throughout it the same endpoint lies on the root side and the other on the far side.  Extending by zero at both ends gives incidence total variation at most two.

This is an exact graph/tree fact and does not use near-parallel train directions.

**Verdict:** PASS.

---

## 3. The KKT resultant orientation is coherent

Section 157 permits swapping the two Jordan shores and reversing the train contact vector.  Thus each selected train can be oriented according to the rooted tree indicator without changing the positive cut stress

```math
A_i=\sum_{e\in E(\tau_i)}\alpha_e.
```

With fixed diameter-edge orientations,

```math
F_i=A_i u_i=\sum_h\beta_h\varepsilon_{hi}r_h.
```

The usual normalization `sum beta_h=1`, diameter length `D`, and interval variation at most two give

```math
\sum_i\|F_{i+1}-F_i\|\le2D.
```

No diameter edge is counted with an unsigned incidence inside the vector identity; the signs are exactly the rooted shore signs.

**Verdict:** PASS.

---

## 4. Selected train shears have full column rank

The exact one-train shear rotates only the contact edges of its own train cut to first order.  Any other contact edge has both endpoints on the same shore and is translated equally.  Hence superposing the selected O--O shears gives a valid contact infinitesimal flex with train angular rates equal to the selected coefficient vector and zero elsewhere.

The diameter derivative matrix is, up to a common factor two,

```math
M_{hi}=\varepsilon_{hi}(r_h\cdot Ju_i).
```

If `M theta=0`, canonical mixed rigidity makes the superposed flex Euclidean.  The center train used to construct the backbone is outside the selected smallest-leaf family and has angular rate zero.  A Euclidean rotation would have the same nonzero angular rate on every complete train, so the rotation rate must vanish.  Translation also has zero train rates.  Therefore every selected coefficient is zero and

```math
\operatorname{rank}M=m.
```

This closes the only potential Euclidean-kernel loophole.

**Verdict:** PASS.

---

## 5. Full-span diameter braces have only two row dimensions

For a diameter edge crossing every selected cut, its signed incidence is one fixed sign.  Its row is

```math
s_h(r_h\cdot Ju_1,\ldots,r_h\cdot Ju_m).
```

As the planar vector `r_h` varies, these rows lie in the two-dimensional span of the two coordinate sequences of `Ju_i`.  Thus all full-span braces together contribute row rank at most two.

Every proper-interval diameter edge contributes at most one additional row dimension.  Since total rank is `m`, at least `m-2` distinct proper-interval diameter edges are required.

This does not assume that proper rows are independent; counting each as adding a full dimension only weakens the conclusion.

**Verdict:** PASS.

---

## 6. `s` switching boundaries allow row rank at most `2(s+1)`

If actual diameter incidence changes only at `s` internal boundaries, the `m` cut columns split into `s+1` consecutive blocks.  Every signed incidence sequence is constant on each block.

On one block, every diameter row is a linear combination of the two masked coordinate sequences of `Ju_i`.  Across all blocks the complete row space therefore has dimension at most `2(s+1)`.  Full column rank gives

```math
m\le2(s+1),
\qquad
s\ge\lceil m/2\rceil-1.
```

The argument remains exact when the leaf train directions vary; inverse-`D` phase collapse is not needed for this rank statement.

**Verdict:** PASS.

---

## 7. Switching boundaries correspond to distinct endpoint projection positions

If a diameter path in the complement dual contains `tau_i` but not adjacent `tau_{i+1}` (or vice versa), it enters or leaves the selected backbone at their common dual vertex.  Therefore one endpoint region projects to that vertex.

A fixed region in a tree has a unique projection to a fixed path, so one physical diameter endpoint cannot account for two distinct internal projection vertices.  Distinct switching boundaries therefore localize distinct actual diameter endpoints.

C65 places every actual diameter endpoint in the loaded positive core.  The theorem correctly stops at dual-tree localization; it does not claim Euclidean proximity to the center-train crossing point.

**Verdict:** PASS.

---

## 8. Live numerical consequences are conservative

From

```math
m>0.017104D-o(D),
```

one gets

```math
m/2>0.008552D-o(D).
```

The exact backbone density is `0.01710405645...`, so the rounded constants lose positive room.

For switching multiplier masses

```math
q_i=\sum_h\beta_h|\varepsilon_{h,i+1}-\varepsilon_{hi}|,
```

the internal sum is at most two.  Thus some adjacent pair has

```math
\|F_{i+1}-F_i\|
\le {2D\over m-1}.
```

The candidate uses

```math
{2\over0.017104}=116.9317\ldots<117,
```

so `<117+o(1)` is safe.

**Verdict:** PASS.

---

## 9. Scope after the new `t<=1.8436` exclusion

Current main now excludes `t<=1.8436`, but all inputs to this candidate were proved uniformly for `t<=1.844`.  Therefore the theorem remains live on

```math
1.8436<t\le1.844.
```

It does not use the two-leaf mass bounds that became vacuous after the exclusion.

The remaining gap is correctly identified: rank and dual localization do not give a lower bound on the KKT multiplier of the switching diameter edges or a metric chart for their loaded endpoints.

**Final verdict:** PASS at proof-only `t<=1.844` full-core Type-II scope. C-II and Level I remain open.
