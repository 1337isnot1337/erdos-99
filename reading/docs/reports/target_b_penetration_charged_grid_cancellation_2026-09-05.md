> Generated reading edition · [exact source](../../../docs/reports/target_b_penetration_charged_grid_cancellation_2026-09-05.md) · source SHA-256 `a1ecda90c62bbe13b93a1c4091fb0ec333255a27014c6536a2b03d588608e5fb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6B2E6BA35F58","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdos Problem #99 - Target B penetration-charged grid cancellation

**Date:** 2026-09-05  
**Run type:** exact train-coordinate / crossing-budget inequality plus coherent-component refinement  
**Target:** positive-density complete-grid promotion without negligible external trains  
**Depends on:** trimmed-grid penetration lemma TG1; train coordinates; Section-50 three-phase potential; pure simply connected rhombic disk  
**LEVEL I STATUS:** STILL OPEN

## 1. Setup

Let `A` and `B` be two internally pairwise noncrossing train families in a pure simply connected strict-rhombic disk, with

`|A|=M`, `|B|=b`,

such that every `A` train crosses every `B` train exactly once.

Thus the physical rhombic disk already contains exactly

`M b`

rhombi at the `A-B` crossings.

Choose trim depths

`k<M/2`, `l<b/2`

and retain the central subfamilies

`A'`, `B'`

with

`M'=M-2k`, `b'=b-2l`.

As in TG1, choose opposite inward source corners `p_00,p_11` of the central grid rectangle. Orient the retained train vectors consistently and put

`U=sum_(alpha in A') u_alpha`,

`V=sum_(beta in B') u_beta`.

Train coordinates give the exact diagonal decomposition

`p_11-p_00=U+V+E`,                                      (1.1)

where `E` is the signed sum of train vectors from trains outside `A union B` that separate the two selected corners. The trimmed-away outer `A` and `B` tracks do not separate these inward corners.

Put

`d=min(k,l)-2`.

Assume `d>0`.

## 2. Every unit of external cancellation spends grid crossings

Let `S_ext` be the set of external trains that separate `p_00,p_11` and let

`s=|S_ext|`.

TG1 says every `gamma in S_ext` crosses at least `d` tracks of `A union B`. Therefore the number `X` of physical rhombi at crossings between `S_ext` and the complete grid families satisfies

`X>=d s`.                                                (2.1)

Every train vector has norm one, so from the signed train-coordinate sum

`|E|<=s<=X/d`.                                          (2.2)

By (1.1) and the reverse triangle inequality,

`D>=|p_11-p_00|>=|U+V|-|E|`.

Hence

`X>=d(|U+V|-D)_+`.                                     (2.3)

The `X` external-grid rhombi are distinct from the `M b` internal grid rhombi. If `R` is the total number of rhombi in the pure disk, then

### Theorem PC1 - penetration-charged cancellation inequality

`boxed{
R >= M b + d(|U+V|-D)_+.
}`                                                       (2.4)

This is exact and finite.

It makes no assumption that the external train population is `o(D)`, that its crossing mass is negligible, or that it belongs to one coherent third phase. Arbitrary cancellation is allowed, but every external train used for cancellation must pay TG1 penetration crossings.

## 3. Coherent 60-degree form

Suppose the `A` directions are uniformly `epsilon`-close to a unit vector `u`, the `B` directions are uniformly `epsilon`-close to a unit vector `v`, and

`angle(u,v)=pi/3`.

Then

`|U-M'u|<=epsilon M'`,

`|V-b'v|<=epsilon b'`,

so

`|U+V|`

`>=sqrt(M'^2+b'^2+M'b')-epsilon(M'+b')`.               (3.1)

Therefore

`R >= M b`

` + d[ sqrt(M'^2+b'^2+M'b') - D - epsilon(M'+b') ]_+`. (3.2)

In the Section-50 coherent regime, `epsilon=o(1)`, so on the `D^2` scale the angular error is negligible.

## 4. Asymptotic normalized obstruction

Assume

`R/D^2 -> Delta_2=pi/(2sqrt(3))`,

and write

`M/D -> x`, `b/D -> y`.

Choose equal asymptotic trim depth

`k/D,l/D -> delta`,

with

`0<delta<min(x,y)/2`.

Then PC1 gives the necessary inequality

`Delta_2`

`>= x y`

` + delta[ sqrt((x-2delta)^2+(y-2delta)^2+(x-2delta)(y-2delta)) - 1 ]_+`.  (4.1)

Thus define

`Phi(x,y)=sup_(0<delta<min(x,y)/2)`

`{xy + delta[ sqrt((x-2delta)^2+(y-2delta)^2+(x-2delta)(y-2delta))-1 ]_+}`.

Every asymptotic coherent complete grid in a global-minimizer pure disk must satisfy

`Phi(x,y)<=Delta_2`.                                   (4.2)

This is a complete-grid exclusion region that already incorporates arbitrary external cancellation.

## 5. Symmetric threshold

Take `x=y=t`. Then

`sqrt((t-2delta)^2+(t-2delta)^2+(t-2delta)^2)`

`=sqrt(3)(t-2delta)`.

For `t>1/sqrt(3)`, the positive part is active for small positive `delta`, and the quantity to maximize is

`t^2 + delta[sqrt(3)t-1-2sqrt(3)delta]`.

Its maximizing trim is

`delta_*=(sqrt(3)t-1)/(4sqrt(3))`,                     (5.1)

which lies inside the allowed interval. At this trim,

`Phi(t,t)>=t^2+(sqrt(3)t-1)^2/(8sqrt(3))`.             (5.2)

Let `t_*` be the positive root of

`t^2+(sqrt(3)t-1)^2/(8sqrt(3))=Delta_2`.

Numerically,

`boxed{t_*=0.9374561097...}`.                           (5.3)

Therefore:

### Corollary PC2 - symmetric complete-grid threshold

A coherent complete `tD x tD` grid with triangular phase angle is impossible in a global-minimizer pure rhombic disk whenever

`t>0.9374561097...+o(1)`,

even if there are `Theta(D)` arbitrary external trains available for cancellation.

The previous trimmed-grid theorem obtained contradiction by proving the external contribution was `o(D)` after an almost-full extraction. PC1 replaces that hypothesis by a physical crossing charge.

## 6. A sharper cancellation functional inside one Section-50 phase component

PC1 treats every external train as an arbitrary unit vector. Inside one retained Section-50 component, the three-phase potential gives more information.

Let `H` be one retained coherent component. Assume the complete grid families `A,B` lie in two of its phase classes. After choosing oriented triangular representatives, take

`u=(1,0)`,

`v=(1/2,sqrt(3)/2)`,

`w=(-1/2,sqrt(3)/2)`.

The third projective class can equally be represented by `-w`; signs in train coordinates are allowed separately.

Define the linear functional

`L(x,y)=x+y/sqrt(3)`.

Then exactly

`L(u)=L(v)=1`,

`L(w)=0`,

and its Euclidean operator norm is

`||L||=2/sqrt(3)`.                                      (6.1)

For an `epsilon`-coherent finite component, these identities hold with `O(epsilon)` errors on its three train classes.

Split the external separator trains in (1.1) into

- `S_in`: trains of `H\(A union B)`;
- `S_out`: trains outside `H`.

Write their cardinalities as `s_in,s_out`, and let `X_in,X_out` be their numbers of physical crossings with `A union B`. TG1 gives

`X_in>=d s_in`,

`X_out>=d s_out`.                                      (6.2)

Because every train in `H` is `epsilon`-close to one of the three phase directions, one such separator can reduce `L(U+V)` by at most `1+O(epsilon)`. An arbitrary outside train can reduce it by at most `2/sqrt(3)`.

On the other hand, the final source-point difference has Euclidean norm at most `D`, so its `L`-value has absolute value at most `2D/sqrt(3)`.

Consequently

`s_in + (2/sqrt(3))s_out`

`>= M'+b' - 2D/sqrt(3) - O(epsilon(M+b+s_in))`.         (6.3)

For the asymptotic Section-50 regime `epsilon=o(1)` and all train populations `O(D)`, this becomes

`s_in + (2/sqrt(3))s_out`

`>= M'+b' - 2D/sqrt(3) - o(D)`.                        (6.4)

Now every crossing between a train of `H` and a train outside `H` was deleted before the final retained-component graph was formed: otherwise the two trains would lie in the same retained component. Let `E_del(H)` denote the number of such deleted physical crossing edges incident with `H`. Then

`X_out<=E_del(H)`.                                     (6.5)

Eliminate `s_in,s_out` from (6.2)-(6.5). Put `c_3=2/sqrt(3)`. If

`C=M'+b'-c_3D-o(D)`,

then

`X_in+X_out`

`>= d C - (c_3-1)X_out`

`>= d C - (c_3-1)E_del(H)`,                            (6.6)

whenever the right side is positive.

Thus:

### Theorem PC3 - three-phase penetration/interface inequality

For a coherent complete grid contained in one retained Section-50 component,

`boxed{
R >= M b
  + [ d(M'+b'-2D/sqrt(3)-o(D))
      -(2/sqrt(3)-1)E_del(H) ]_+.
}`                                                       (6.7)

The `o(D)` term is only the phase-coherence error. In a fixed finite coherence window it can be replaced by an explicit `O(epsilon D)` term.

PC3 has two improvements over PC1:

1. in-component third-phase trains have cancellation coefficient at most one under `L`, rather than the arbitrary Euclidean coefficient;
2. the only trains receiving the weaker coefficient `2/sqrt(3)` are outside the coherent component, and their physical crossings are already part of the Section-50 deletion/interface budget.

The subtraction coefficient is small and explicit:

`2/sqrt(3)-1=0.1547...`.

No near-star or local saturation hypothesis is used.

## 7. What PC3 does and does not solve

For a grid with `M'+b'<=2D/sqrt(3)+o(D)`, the phase functional does not force any cancellation, so PC3 reduces to the already-used internal grid count. Thus a single small coherent component can still survive.

For a macroscopic grid whose two retained dimensions sum above `2D/sqrt(3)`, PC3 is stronger than the arbitrary-direction PC1 unless the deleted-interface budget incident with that component is itself quadratic.

This isolates a useful global dichotomy:

- a large complete phase grid must pay a quadratic penetration cost; or
- a quadratic fraction of the Section-50 deleted/interface edges must be incident with that component.

The latter is precisely the interface branch already isolated by the virtual-area certificate. PC3 therefore couples the grid/diameter route to the current virtual-area/interface route in the same currency: deleted physical train crossings.

## 8. Interaction with positive-density grid extraction

The positive-density dual-tree theorem PDG proves that every phase pair of fixed positive crossing density contains a complete grid with both dimensions linear in the parent phase sizes.

PC1 and PC3 show exactly what is needed after that extraction. It is no longer necessary to make every discarded train negligible. It is enough to make the extracted grid large enough that the grid rhombi plus the penetration cost of required cancellation exceed the global rhombus budget, unless the relevant retained component itself consumes a quadratic deleted-interface budget.

The present conservative PDG constants are not by themselves large enough to force (4.2) or (6.7) to fail in every Section-50 component. Thus this is not yet a Level-I closure.

The next quantitative targets are:

1. apply PC3 simultaneously to several dense retained components and charge `E_del(H)` with bounded multiplicity;
2. strengthen dual-tree extraction using the three-phase cyclic-order structure, rather than density alone;
3. combine PC3 directly with the local virtual-area/interface certificate, which already gives a lower bound on support depth when many trains are pruned.

## Handoff

```text
PC1, arbitrary external trains:
For any complete M x b train grid, trim by k,l and let d=min(k,l)-2. For the deep diagonal,

  p_11-p_00 = U+V+E,

and every external separator spends at least d physical grid crossings. Hence

  R >= M b + d(|U+V|-D)_+.

PC3, grid inside one Section-50 coherent component H:
Use L with L(u)=L(v)=1, L(w)=0, ||L||=2/sqrt(3). In-component external trains cancel at rate <=1; outside-component trains at rate <=2/sqrt(3), but all of their grid crossings lie in the deleted/interface edge set. Therefore

  R >= M b
    + [d(M'+b'-2D/sqrt(3)-o(D))
       -(2/sqrt(3)-1)E_del(H)]_+.

Thus a large grid either pays a quadratic diameter-cancellation cost or forces quadratic deleted interface at that component.
```
