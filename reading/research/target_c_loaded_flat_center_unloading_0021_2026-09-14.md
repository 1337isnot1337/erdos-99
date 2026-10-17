> Generated reading edition · [exact source](../../research/target_c_loaded_flat_center_unloading_0021_2026-09-14.md) · source SHA-256 `3e1ec9d94f5fefaefcd4abc2f2cd1aaa98dc9c12507e65439308ec94a76912d0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0d0730ee37f7f87b6e793d28d51c4e1a1425f776", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_loaded_flat_center_unloading_0021_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ad74c1681033cf601f732f6cb5d87d208711d329b572010a3c2b8c67259dcc55"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - loaded flat-center unloading at atomic gap 0.0021

**Date:** 2026-09-14
**Target:** C-II, canonical contact-minimal full-core Type-II branch
**Dependencies:** minimax phase-star atomic gap `g=0.0021`; low-t flat-center multiplicity one; loaded flat-center singleton gate; flat-center degree-three/four structure; edge-level flat-center trichotomy
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The loaded-flat-center singleton theorem already shows that a loaded flat center costs
two distinct singleton stopped trains. Its numerical unloading bound used the older
`0.00042` all-train constant and only the older independently audited rhombic floor.
The new minimax phase-star theorem supplies the same stronger constant

$$
g:=0.0021
$$

simultaneously in the all-train face floor and the rhombic train floor. Keeping both
copies yields a strictly larger unloaded-center population and a wider low-`t` window.
Combining that population with the newer edge-level flat-center theorem also removes
the old `1/9` matching loss in the degree-four branch.

Put

$$
\Delta_2={\pi\over2\sqrt3},\qquad s:=\sqrt{\Delta_2},\qquad C_g:=2s+g.
$$

On a convergent Type-II subsequence write

$$
t:=\lim {q-k\over D},\qquad
\delta:=\lim {b-P_F\over D},\qquad
\kappa:=\lim {k\over D},
$$

and assume the true force-hull residual satisfies

$$
R_F=o(D).
\tag{U21.1}
$$

Let `V_flat` be the distinct good flat centers, `L` the loaded ones, and
`U=U_3\sqcup U_4` the unloaded degree-three/four centers. Then

$$
\boxed{
\liminf {V_{flat}\over D}
\ge
P_g(t,\delta,\kappa)
:=\pi+2s+g-{5t\over2}+\delta+{\kappa\over2}.
}
\tag{U21.2}
$$

The exact singleton payment and the `g=0.0021` rhombic train floor imply

$$
\boxed{
\liminf {|U|\over D}
\ge
U_g(t,\delta,\kappa)
:=2\pi+3s+{3g\over2}-5t+2\delta+{\kappa\over2}.
}
\tag{U21.3}
$$

Whenever `U_g>0`, at least one of two actual source-level degeneracies is forced:

### (A) Dense degree-four activation branch

There is a set `P_4` of **distinct** inactive source pairs such that

$$
\boxed{
\liminf {|P_4|\over D}
\ge {3\over4}U_g(t,\delta,\kappa),
}
\tag{U21.4}
$$

and, on the same diagonal flatness scale,

$$
\boxed{
\sum_{xy\in P_4}(|x-y|-1)=o(D),
\qquad 1<|x-y|=1+o(1).
}
\tag{U21.5}
$$

### (B) Dense weak-contact branch

There is a set `E_3` of distinct positive contact edges such that

$$
\boxed{
\liminf {|E_3|\over D}
\ge {1\over4}U_g(t,\delta,\kappa),
}
\tag{U21.6}
$$

and, for the canonical relative-interior normalized KKT stress,

$$
\boxed{
\sum_{e\in E_3}\alpha_e=o(D^2).
}
\tag{U21.7}
$$

Thus the loaded class cannot absorb the flat-center sea throughout the window where
`U_g>0`.

## 1. Updated flat-center supply

The minimax phase-star theorem gives

$$
\liminf {T-q/2\over D}\ge2s+g.
$$

The same audited low-`t` face ledger used in the flat-center theorem therefore gives

$$
{f\over D}\ge {2s+g\over2}-{t\over4}+{\kappa\over4}-o(1).
$$

Combining this with the exact degree-excess relation and the pentagon estimate gives

$$
{p_5\over D}
\ge \pi+(2s+g)-{5t\over2}+\delta+{\kappa\over2}-o(1).
\tag{U21.8}
$$

On `R_F=o(D)`, all but `o(D)` of these pentagons are in the fixed flat-trapezoid
stability neighborhood. The flat-center multiplicity-one theorem loses no further
factor, proving (U21.2).

## 2. Updated singleton capacity

Every loaded flat center has contact degree exactly two and contributes two distinct
singleton stopped trains. Hence

$$
2|L|\le S,
\tag{U21.9}
$$

where `S` is the total singleton train population.

Write the exact train split

$$
T=T_R+S.
\tag{U21.10}
$$

The terminal occurrence ledger and `f<=Q` give the same upper bound as before,

$$
\limsup {T\over D}\le5t-2\pi-2\delta.
\tag{U21.11}
$$

The minimax theorem restricted to the rhombic train graph gives

$$
\liminf {T_R\over D}\ge2s+g.
\tag{U21.12}
$$

Therefore

$$
\limsup {S\over D}
\le5t-2\pi-2\delta-2s-g,
\tag{U21.13}
$$

and (U21.9) yields

$$
\limsup {|L|\over D}
\le {5t\over2}-\pi-\delta-s-{g\over2}.
\tag{U21.14}
$$

Subtracting (U21.14) from the flat-center floor (U21.2) gives exactly

$$
\begin{aligned}
\liminf {|U|\over D}
&\ge
\pi+2s+g-{5t\over2}+\delta+{\kappa\over2}
-\left({5t\over2}-\pi-\delta-s-{g\over2}\right)\\
&=
2\pi+3s+{3g\over2}-5t+2\delta+{\kappa\over2},
\end{aligned}
$$

proving (U21.3).

## 3. Replace the old matching loss by physical pair multiplicity

The unloaded centers partition as

$$
U=U_3\sqcup U_4.
$$

If `|U_4|>=|U|/2`, each degree-four center creates three inactive consecutive
neighbor pairs with total gap at most its flatness defect. A fixed unordered source
pair has at most two unit common neighbors, because two unit circles intersect in at
most two points. Thus the edge-level flat-center theorem gives

$$
|P_4|\ge {3|U_4|\over2}\ge {3|U|\over4},
$$

and the occurrence-counted total gap is `o(D)`. This proves (U21.4)--(U21.5).

If instead `|U_3|>=|U|/2`, designate the unique exterior contact at every degree-three
flat center. Any actual contact edge can be designated by at most its two endpoints,
so after deduplication

$$
|E_3|\ge {|U_3|\over2}\ge {|U|\over4}.
$$

The local degree-three KKT balance gives an exterior-to-face weight ratio tending
uniformly to zero. Summing over the distinct flat centers and using
`sum_{e in C} alpha_e=D^2` gives the parent theorem's aggregate estimate

$$
\sum_{e\in E_3}\alpha_e=o(D^2).
$$

This proves (U21.6)--(U21.7).

## 4. Current endpoint constants and widened window

The minimax theorem's safe Section-171 endpoint is

$$
t_0=C_{146}+0.0017279,
\qquad
C_{146}={4\over9}(\pi+s),
$$

with

$$
t_0=1.8212414379\ldots .
$$

At the most permissive `delta=kappa=0`, (U21.2) gives

$$
\boxed{
{V_{flat}\over D}
\ge0.495214672369096\ldots-o(1),
}
\tag{U21.15}
$$

and (U21.3) gives

$$
\boxed{
{|U|\over D}
\ge0.0370665378742349\ldots-o(1).
}
\tag{U21.16}
$$

Hence every endpoint survivor has either

$$
\boxed{
{|P_4|\over D}
\ge0.0277999034056761\ldots-o(1),
}
\tag{U21.17}
$$

with total activation gap `o(D)`, or

$$
\boxed{
{|E_3|\over D}
\ge0.0092666344685587\ldots-o(1),
}
\tag{U21.18}
$$

with total normalized KKT weight `o(D^2)`.

Even after dropping the nonnegative `delta,kappa` bonuses, the unloaded floor stays
positive throughout

$$
\boxed{
t< {2\pi+3s+3g/2\over5}
=1.8286547455\ldots .}
\tag{U21.19}
$$

Thus excluding the two degeneracies (U21.4) and (U21.6) would immediately raise the
proof-only Type-II `q-k` floor from `1.8212414...` to at least `1.8286547...` before
using detour or topology bonuses.

## 5. Frontier effect

The low-`t`, small-residual branch is now reduced, after paying every loaded flat
center from the singleton-train budget, to one of two physical objects:

```text
at least 0.0277999 D distinct inactive 1+o(1) source pairs
with only o(D) total activation gap,

or

at least 0.00926663 D distinct exact positive contacts
carrying only o(D^2) total normalized KKT weight.
```

The first branch is a dense core-contact activation problem, not the old protected
isolate problem: its endpoints already lie in the positive core, so the protected
simultaneous-isolate motion theorem does not apply. The second branch is a genuine
stress-degeneration problem. A closing argument must either find a contact-preserving
multi-center motion for the first family or turn the linear weak-contact family into a
mixed-rigidity / diameter-descent contradiction.

No exact unit triangle, exact new contact, or strict same-cardinality sub-`D` source is
claimed here.

## 6. Scope audit

- The `g=0.0021` input is the minimax phase-star theorem and inherits its proof-only
  lifecycle until independent audit/promotion.
- The loaded-center singleton payment `2|L|<=S` is finite and unchanged.
- The new rhombic train floor uses the same minimax theorem restricted to the
  non-singleton rhombic crossing graph.
- Flat centers are distinct actual source vertices; contact-isolated source points
  remain in the full source.
- `P_4` is not claimed endpoint-disjoint; the `3/2` multiplicity is obtained from the
  exact two-circle common-neighbor bound.
- The aggregate weak-contact stress statement uses the existing full-support virial
  normalization and degree-three local KKT estimate.

C-II and Level I remain open.
