<!-- theorem-state: {"artifact_id":"ART-DD43E0F1EBBA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-a"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6f578189d0a465310f8e7015cd63dcfc4b17cefc", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_a_boundary_terminal_common_source_vpaths_2026-09-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f04211aa5b27f5eaf9778da6b3a801b14f8b698724bd9b10628b70dbcedfb091"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — Target A boundary-terminal common-source V-paths

**Date:** 2026-09-05  
**Run type:** exact zero-slack source/Schur boundary transport  
**Target:** Section 174 sink-surplus gate  
**Depends on:** zero-slack full response labels; Section 99 boundary terminality; planar two-shadow crossing theorem  
**LEVEL I STATUS:** STILL OPEN

## 1. Purpose

In the zero-slack branch there are two independent strict-conflict matchings into the same genuine triangle-free capacity source `A^0`:

1. a matching saturating `X^*`, hence its actual Schur source set `C^partial`;
2. a matching saturating `Y_in`, hence its exterior sink set `O`.

The two matchings must not be identified. Their source images can nevertheless be compared because both terminal shores lie in the width-one boundary zone of the smaller response hull `K^*`.

This note proves that the two source images have a forced boundary-order overlap, and that a constant fraction of the common source mediators can be chosen as pairwise disjoint geometric V-paths from actual Schur sources to actual exterior sinks.

## 2. Two-sided boundary-band packing

Let `K` be a convex body of perimeter `P`. For `w>0`, put

`T_w(partial K)={x: dist(x,partial K)<w}`.

### Lemma 1 — unit-separated points in a two-sided boundary band

If `A` is unit-separated, then

`|A cap T_w(partial K)|`

`<= [8(w+1/2)/pi] P +4(w+1/2)^2`.                    (2.1)

In particular, for `w=2`,

`|A cap T_2(partial K)| <=20P/pi+25`.                  (2.2)

### Proof

Put `r=w+1/2`. The open radius-`1/2` disks centered at the counted points are pairwise disjoint. Every such disk lies in the two-sided radius-`r` tube around `partial K`.

The outer part of this tube has area

`rP+pi r^2`

by Steiner's formula. The inner boundary layer has area at most

`rP`:

using the inner parallel bodies `K_t={x in K:dist(x,partial K)>=t}`, coarea gives

`area(K)-area(K_r)=integral_0^r per(K_t)dt <= rP`,

with `K_t` interpreted as empty after the inradius if necessary.

Thus the full two-sided tube has area at most

`2rP+pi r^2`.

Comparing with the disjoint disk area `pi/4` gives (2.1). `square`

For `K=K^*`, Cauchy's perimeter bound gives

`P<=pi d`,

so

### Corollary 2

Every unit-separated set has at most

`20d+25`                                                   (2.3)

points within distance below two of `partial K^*`.

## 3. Both zero-slack source images lie in that same band

Fix independently:

- a zero-slack matching `M_C` from `C^partial` into `A^0`, obtained by restricting the `X^*->A^0` matching;
- a zero-slack matching `M_O` from `O` into `A^0`, obtained by restricting the `Y_in->A^0` matching.

Write their source-image sets as

`S_C subset A^0`, `S_O subset A^0`.

Both matchings are injective, so

`|S_C|=|C^partial|`, `|S_O|=|O|`.                       (3.1)

Section 99 gives

`dist(c,partial K^*)<=1`

for every boundary Schur source `c in C^partial`. Since its matched source label satisfies `|c-a_c|<1`,

`dist(a_c,partial K^*)<2`.                               (3.2)

Likewise every `o in O` lies in the exterior unit band

`(K^*+B)\K^*`,

so `dist(o,partial K^*)<1`; its matched source label `b_o` satisfies

`dist(b_o,partial K^*)<2`.                               (3.3)

Thus

`S_C union S_O subset A^0 cap T_2(partial K^*)`.

Corollary 2 and inclusion-exclusion give:

### Theorem 3 — common source mediator floor

Let

`L=|S_C cap S_O|`.

Then

`L >= |C^partial|+|O|-(20d+25)`.                         (3.4)

The right side is understood as zero when negative.

Every common source point `a in S_C cap S_O` has unique partners

`c(a) in C^partial`, `o(a) in O`

in the two matchings and therefore gives a geometric V-path

`c(a) -- a -- o(a)`                                      (3.5)

whose two arms both have length strictly below one.

## 4. Constant-fraction pairwise disjoint V-paths

Within `M_C`, all straight matching segments `[c,a_c]` are pairwise disjoint by the short-matching planarity theorem. Within `M_O`, all `[o,b_o]` segments are likewise pairwise disjoint.

For distinct common mediators, an intersection can therefore occur only between a `C`-arm of one V-path and an `O`-arm of another.

The crossing-to-scaffold transport theorem of Section 163 applies verbatim to these two zero-slack matchings:

- one `C`-arm crosses at most four `O`-arms;
- one `O`-arm crosses at most five `C`-arms.

Form the interference graph whose vertices are the common mediators and whose edges join two V-paths when their closed polygonal arcs intersect away from their own mediator endpoints. Every vertex has degree at most

`4+5=9`.

A greedy independent set therefore has size at least `L/10`.

### Theorem 4 — disjoint boundary-terminal source gates

There is a family of pairwise disjoint polygonal V-paths

`c_i-a_i-o_i`,

with

`c_i in C^partial`, `a_i in A^0`, `o_i in O`,

all three endpoint sets pairwise distinct, and

`|c_i-a_i|<1`, `|a_i-o_i|<1`,

of cardinality at least

`boxed{
G_CO >= (1/10) max(0, |C^partial|+|O|-20d-25).
}`                                                        (4.1)

Each path starts at an actual Schur source in `K^*` and reaches an actual exterior sink in the width-one lattice collar.

## 5. Interface with the three-sector shield

Let `Sigma` be the stress-generated contact shield of Sections 173–174. A V-path whose `C^partial` endpoint and `O` endpoint are assigned to different shield sectors must intersect `|Sigma|` somewhere in its passage through `K^*` or at the sector boundary.

The source-label shield-crossing theorem already bounds crossings of the `C`-arm `[c,a]` by source labels near shield vertices. The V-path theorem here adds a disjointness resource: distinct selected gates cannot all reuse one geometric crossing point or one tiny local corridor.

This does not yet imply the sink-surplus inequality

`sum_i max(0,|O_i|-|C_i|)
 >= j_*+|W\O|-|O_iso|`.

A gate may leave `K^*` through the outer hull without changing its interior shield sector, and the `O`-arm may cross the shield after the source mediator. The next theorem must therefore classify a disjoint gate as either:

1. sector-preserving, contributing a common source label to one `C_i/O_i` sector pair; or
2. shield-crossing, consuming a quantitatively bounded shield/source-interface resource.

The new point is that this classification can now be imposed on a genuinely disjoint physical family of actual Schur-source/exterior-sink gates.

## 6. Regression checks

- The two zero-slack matchings remain independent; only intersection of their source-image sets is used.
- A common source mediator does not imply `|c-o|<1`; no such response edge is asserted.
- The disjoint V-path family does not imply Schur nullity or Schur rank by itself.
- Full conflict-graph planarity is not assumed. Only planarity of each strict-conflict matching and the audited constant cross-matching congestion are used.
- The `20d+25` source-band bound is independent of the cardinality of `A^0`.

## 7. Handoff

```text
LEVEL I STATUS: STILL OPEN.

For independent zero-slack matchings
  C^partial -> A^0
and
  O -> A^0,
both source-image sets lie in the two-sided width-2 band of partial K*.
That band contains at most 20d+25 source points.

Hence there are at least
  |C^partial|+|O|-20d-25
common source mediators, and at least one tenth of them can be selected as pairwise disjoint physical V-paths
  C^partial -- A^0 -- O.

Next: classify these disjoint gates relative to the three-channel contact shield and turn cross-sector gates into shield charge, leaving enough sector-preserving gates to force the exact sink-surplus inequality.
```
