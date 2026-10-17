> Generated reading edition · [exact source](../../../docs/reports/target_c_switch_edge_antipodal_side_pairs_2026-09-30.md) · source SHA-256 `0ae0ec215d8696ffd2533e3e7b0988a645396a63c55d75a9c174192d2475a3fa`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E11FFD517FEA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — switch edges force paired antipodal hull sides

**Base main:** \`c00bb08090cf3a7a89fc195cbe3ab450983a5de0\`
**Status:** proof-only; C-II remains open.

Put
```math
a_D=\arcsin(1/(2D)),\qquad
A(\lambda)=\lambda+4\lambda\sqrt{1-\lambda^2},\qquad
\Delta(\lambda)=\pi/2-A(\lambda).
```

Current main gives exact diameter-star contiguity and, in the rooted wrapping branch,
```math
R_D=0,\qquad m_D=d_H,\qquad h=q-d_H.
```
It also gives the angular excess
```math
E_D=\pi-2a_Dq\le \Delta(\lambda)+o(1).
```

Call a diameter edge $`e=uv`$ a **switch edge** if its predecessor and successor in cyclic projective-direction order can be written
```math
e^-=ux,\qquad e=uv,\qquad e^+=vy.
```

## Theorem

1. An actual diameter edge $`uv`$ is a switch edge iff
```math
\deg_H(u)\ge2,\qquad \deg_H(v)\ge2.
```

2. Fix $`0<\eta<1`$. All but
```math
\left(\frac{2\Delta(\lambda)}{\eta}+o(1)\right)D
```
switch edges produce two loaded-hull sides $`xv`$ and $`uy`$ satisfying
```math
|x-v|,\ |u-y|\le1+\eta+o(1).
```
The side $`xv`$ has unique common diameter partner $`u`$, and $`uy`$ has unique common diameter partner $`v`$.

3. If $`n_{xv},n_{uy}`$ are their outward normals, their projective directions are each within
```math
a_D+\frac{\eta}{2D}
```
of the projective direction of $`uv`$. With oriented outward normals they are opposite up to $`O_\eta(D^{-1})`$, and
```math
0\le D-w_F(n_{xv})=O_\eta(D^{-1}),\qquad
0\le D-w_F(n_{uy})=O_\eta(D^{-1}).
```

Hence at the exact rooted endpoint $`\Delta(\lambda_1)=0`$, all but $`o(D)`$ switch edges force paired opposite short support sides.

## Proof

For a diameter vertex $`z`$, let $`I_z`$ be its positions in cyclic projective-direction order. Current main proves $`I_z`$ is one proper cyclic interval. For $`e=uv`$,
```math
I_u\cap I_v=\{e\}
```
because the diameter graph is simple. If both endpoint degrees are at least two, the two nontrivial intervals containing $`e`$ and otherwise disjoint must leave $`e`$ on opposite sides of the cyclic order. Thus one neighboring edge shares $`u`$, the other shares $`v`$. The converse is immediate. This proves (1).

For a switch $`ux,uv,vy`$, let the two adjacent projective gaps be $`\alpha,\beta`$. The diameter-neighbor cone has aperture at most $`\pi/3`$, so these are the ordinary angles $`\angle xuv,\angle uvy`$. Since both relevant triangles have equal sides $`D,D`$,
```math
|x-v|=2D\sin(\alpha/2),\qquad
|u-y|=2D\sin(\beta/2).
```

Call a shared gap bad if its excess above $`2a_D`$ is $`>\eta/D`$. Since the sum of all angular excess is $`E_D`$,
```math
N_{\rm bad}\frac{\eta}{D}\le E_D\le\Delta(\lambda)+o(1),
```
hence
```math
N_{\rm bad}\le\left(\frac{\Delta(\lambda)}{\eta}+o(1)\right)D.
```
A bad gap can flank at most two switch edges, proving the exceptional count in (2).

For a switch with both flanking gaps good,
```math
\alpha,\beta\le2a_D+\eta/D,
```
so
```math
|x-v|,\ |u-y|
\le2D\sin(a_D+\eta/(2D))
=1+\eta+o(1)<2-o(1).
```
The quantitative V-cover short-arc argument on current main now applies separately to $`x,v`$ and $`u,y`$: an intermediate loaded hull vertex would create at least two unit-separated hull sides in one $`o(1)`$ tangent cone, forcing the endpoint chord to have length at least $`2-o(1)`$. Thus both chords are hull sides.

If a side of length $`s=O_\eta(1)`$ had two distinct common diameter partners, the two intersections of its endpoint-centered radius-$`D`$ circles would be separated by
```math
2\sqrt{D^2-s^2/4}>D,
```
impossible. Hence each partner is unique.

The normal to chord $`xv`$ is the angle-bisector direction of the two radius-$`D`$ rays from $`u`$, so projectively it differs from $`uv`$ by exactly $`\alpha/2`$; similarly $`uy`$ differs by $`\beta/2`$. Their outward lifts point in opposite directions because $`u`$ and $`v`$ lie on the inward sides of the respective support lines.

Finally, for either side of length $`s`$, its common diameter partner lies at distance
```math
H=\sqrt{D^2-s^2/4}
```
from the supporting line. Therefore
```math
H\le w_F(n)\le D,
```
and
```math
0\le D-w_F(n)\le D-H
=\frac{s^2}{4(D+H)}
=O_\eta(D^{-1}).
```

This proves the theorem.

In the Woodall forest branch, switch edges are exactly diameter edges whose two endpoints are nonleaves. In the $`d_H=0`$ odd-unicyclic branch every odd-cycle edge is a switch and pendant edges are not.

The remaining bottleneck is now a train/fan-switch dichotomy: either there are linearly many switch edges, giving linearly many paired opposite short supports, or there are sublinearly many switches and almost all V-covered sides lie inside long single-center star fans. A closure must show that the two canonical inverse-phase train families cannot coexist with either alternative.

No computation or verifier is used.

## Salvage provenance and lifecycle

Copied from `proof/target-c-switch-edge-antipodal-side-pairs-clean-20260930` at tip
`ce2aeb36e544eae6026ab4f3f7b65da09ba74e86`. The later run2 ref
`proof/target-c-switch-edge-antipodal-side-pairs-run2-20260930` at tip
`eda91229cc7bad25f3ecaed2bb1ffc7070da1560` is a formatting-corrupted rewrite of this
same theorem and adds no mathematical content. This is proof-only structural work on
the current-main loaded diameter graph and rooted wrapping branch; it does not close
C-II or Level I, and remains unreviewed pending independent audit.
