> Generated reading edition · [exact source](../../../docs/reports/target_b_trimmed_grid_phase_star_exclusion_2026-09-05.md) · source SHA-256 `4013536ad4ca97b13f9c0c7d39ca6911cec3f1fc8f1897cf406b5ae3eba3ab86`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-6FBFFF44EE97","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Erdős Problem #99 — Target B trimmed-grid phase-star exclusion

**Date:** 2026-09-05  
**Run type:** exact topological reduction plus asymptotic diameter comparison  
**Target:** dense coherent three-phase / biclique-to-additive promotion gap  
**LEVEL I STATUS:** STILL OPEN

## 1. Result

A complete positive-density crossing grid between two coherent train families already forces a diameter larger than the global-minimizer scale, even when other trains shift the train-coordinate base and a third coherent phase contributes its worst possible linear cancellation.

Thus the old additive-block/base-alignment hypothesis is unnecessary for a complete coherent phase star.

## 2. Topological grid-depth lemma

Let

`A={alpha_1,...,alpha_M}` and `B={beta_1,...,beta_b}`

be two families of train tracks in a simply connected rhombic disk such that

1. tracks inside each family are pairwise noncrossing;
2. every `alpha_i` crosses every `beta_j` exactly once.

The tracks have natural linear orders. Their union is a topological `M x b` pseudoline grid.

Fix integers `k<M/2`, `l<b/2` and retain

`A'={alpha_(k+1),...,alpha_(M-k)}`,

`B'={beta_(l+1),...,beta_(b-l)}`.

The four extremal crossings bound a central grid rectangle. Choose source vertices `p_00,p_10,p_01,p_11` at inward corners of those four extremal crossing rhombi.

### Lemma TG1 — penetration depth

If a train `gamma` outside `A union B` separates either diagonal pair

`p_00,p_11` or `p_10,p_01`,

then `gamma` crosses at least

`min(k,l)-2`

tracks of `A union B`.

### Proof

A train separating a diagonal pair meets every path between those vertices, hence enters the closed central grid rectangle.

Complement regions of the complete `A`–`B` grid have integer coordinates `(i,j)`, counting crossed `A` and `B` tracks from fixed outer sides. Every point of the central rectangle has

`k-O(1)<=i<=M-k+O(1)`,

`l-O(1)<=j<=b-l+O(1)`.

For two complete noncrossing train families, their boundary endpoints occur in four alternating blocks. Every disk-boundary region therefore has at least one coordinate equal to `0` or its maximum.

Follow either branch of `gamma` from the central rectangle to its boundary endpoint. Each crossing with `A union B` changes one coordinate by one. Reaching a boundary region therefore requires at least `min(k,l)-2` such crossings. QED.

## 3. External-train error after trimming

Use train coordinates

`p_v=p_0+sum_tau epsilon_tau(v)u_tau`, `|u_tau|=1`.

Orient retained grid tracks consistently and put

`U=sum_(alpha in A')u_alpha`,

`V=sum_(beta in B')u_beta`.

For one selected diagonal,

`p_11-p_00=U+V+E`,

where `E` is the signed sum of trains outside `A union B` separating the two corners.

Suppose the full coherent three-phase system has center class `A` and leaf classes `B,C`. Split

`E=E_C+E_ext`.

Let `E_bad` be the number of rhombus crossings with at least one train outside `A union B union C`. If

`E_bad=o(M^2)`, `b/M>=tau>0`,

and

`k=floor(epsilon M)`, `l=floor(epsilon b)`

for fixed `epsilon>0`, then TG1 gives

`#supp(E_ext)=o(M)`.

Hence

`|E_ext|=o(M)`.

The possibly linear contribution from `C` remains and is treated exactly below.

## 4. Worst coherent cancellation by the third phase

Assume a complete coherent phase star:

- `|A|=M`, `|B|=b`, `|C|=a`, with `0<=a<=b<=M`;
- every `A` train crosses every train in `B union C`;
- non-star crossings are `o(M^2)`;
- the three projective direction classes are `o(1)`-coherent around the triangular phases.

After isometry/projective choices, use

`u=(1,0)`,

`v=(1/2,sqrt(3)/2)`,

`w=(1/2,-sqrt(3)/2)`.

After trimming,

`U=M'u+o(M)`,

`V=b'v+o(M)`,

with

`M'=(1-2epsilon)M+O(1)`, `b'=(1-2epsilon)b+O(1)`.

Every `C`-train contribution to the chosen diagonal is `0`, `+u_gamma`, or `-u_gamma`; coherence gives

`E_C=xw+o(M)`

for some real `x` with

`|x|<=a+o(M)`.

Therefore

`p_11-p_00=M'u+b'v+xw+o(M)`.

Because this is a source-point difference,

`D^2>=min_(|x|<=a+o(M)) |M'u+b'v+xw|^2-o(M^2)`.

Let `epsilon->0` after the asymptotic limit and normalize

`t=b/M`, `s=a/M`, `0<=s<=t<=1`.

Define

`f_t(x)=|u+t v+x w|^2`

`=1+t+t^2+(1-t)x+x^2`.

The unconstrained minimizer is

`x_*=-(1-t)/2`.

Thus the exact constrained minimum is

`F(s,t)=1+t+t^2-s(1-t)+s^2`

when `s<(1-t)/2`, and

`F(s,t)=3(1+t)^2/4`

when `s>=(1-t)/2`.

### Theorem TG2 — complete phase-star diameter cost

Every complete coherent phase star above obeys

`D^2 >= (F(s,t)-o(1))M^2`.

No exact additive block or coordinate-base alignment is assumed.

## 5. The diameter cost exceeds the global-minimizer scale

Put

`c=2sqrt(3)/pi=1.1026577908...`.

If the phase star carries the quadratic rhombus core,

`R=M(a+b)+o(M^2)`,

and `T=O(M)`, then the pure-disk Euler count gives

`n=(s+t)M^2+o(M^2)`.

The strict translated-lattice comparison gives

`D(n)^2 < (c(s+t)+o(1))M^2`.

We prove

`F(s,t)>c(s+t)`

for every `0<=s<=t<=1`.

### Case 1: `s>=(1-t)/2`

Since `s<=t`,

`c(s+t)<=2ct`.

It suffices to prove

`3(1+t)^2/4>2ct`.

The difference is a quadratic with leading coefficient `3/4` and discriminant

`(3/2-2c)^2-9/4=2c(2c-3)<0`,

because `0<c<3/2`. Hence it is positive for all real `t`.

### Case 2: `s<(1-t)/2`

Set

`H(s,t)=1+t+t^2-s(1-t)+s^2-c(s+t)`.

For fixed `t`,

`dH/ds=2s-(1-t+c)<0`

throughout `0<=s<=(1-t)/2`. The minimum is at the upper endpoint, where

`H((1-t)/2,t)`

`=3(1+t)^2/4-c(1+t)/2`

`=(1+t)(3(1+t)/4-c/2)>0`,

because already `3/4-c/2>0`.

Therefore `F(s,t)>c(s+t)` in both cases, with a uniform positive gap on every positive-density range `t>=tau>0`.

### Corollary TG3 — complete coherent phase stars are impossible

No sufficiently large global minimizer can have a complete coherent phase star with

`0<=a<=b<=M`, `b/M>=tau>0`,

`R=M(a+b)+o(M^2)`,

and only `o(M^2)` non-star crossing mass.

## 6. Remaining promotion problem

The remaining issue is ordered star stability: show that a near-saturated coherent three-phase core contains a positive-density complete center-to-leaf train grid after negligible loss, or obtain the same diagonal estimate directly from its ordered missing-crossing pattern.
