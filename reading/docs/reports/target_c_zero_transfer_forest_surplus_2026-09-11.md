> Generated reading edition · [exact source](../../../docs/reports/target_c_zero_transfer_forest_surplus_2026-09-11.md) · source SHA-256 `3aef7170fa2eca2a88359125c6f0c19d82c31cf742cf235fcdee2c3c2c38a122`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2A452F7392D9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 - zero-transfer forest alternative and surplus cost

**Date:** 2026-09-11  
**Target:** Target C, post-C-I common-block phase  
**Status:** STILL OPEN; local structural report superseded for canonical C-II zero-transfer stresses by `target_c_zero_transfer_additive_cii_exclusion_2026-09-11.md`  
**Depends on:** promoted C53/C63, circular-planar response/Kalmanson theory,
SEPq, Woodall, and the report-level ZF/E597 stack  
**Computation:** none

## 1. Result

Let $`H`$ be the actual diameter graph of the contact/diameter-lexicographically
normalized C-II source, and let $`K=Q^{\mathsf T}\Lambda^+Q`$ be the C53 transfer
kernel in the single legal projective orientation. Suppose

```math
\min_{e\ne f}K_{ef}=0.
\tag{ZT.1}
```

Then:

1. $`K_{ef}=0`$ for every $`e\ne f`$, and $`K=\operatorname{diag}(\beta_e^{-1})`$;
2. every connected component of $`H`$ is a star;
3. every such star has at most four edges in fully force-visible C-II;
4. if the report-level ZF conclusions are also invoked, then
   ```math
   d_H\ge h/4\ge D/4;
   \tag{ZT.2}
   
   ```
5. in the report-level $`s_Z=0`$ E597 branch,
   ```math
   \frac{e_{BB}+2s_C}{D}
   >0.597+\varepsilon_{597}+\frac35
   =1.347+\varepsilon_{597}.
   \tag{ZT.3}
   
   ```

The same conclusion with $`>1.347`$ follows in the report-level arbitrary-$`s_Z`$
extension from
$`\nu_D=(e_{BB}+2s_C-3d_H)/D>0.597+o(1)`$.

For the canonical fully force-visible C-II relative-interior stress with (D\ge9),
the later all-terminal split argument and SEPq exclude the zero-transfer hypothesis
itself. The structural conclusions below remain useful as a conditional local
analysis and as regressions for any attempted proof that does not have full C-II
support. The global problem is still open because the strictly negative-transfer
branch remains, as does the source-population/surplus obstruction.

## 2. Zero minimum forces complete transfer orthogonality

Orient the positive diameter edges in the legal C53 half-plane. Write

```math
u_e=a_e(1,t_e),\qquad a_e>0,
```

with the $`t_e`$ pairwise distinct and increasing. Put

```math
\gamma_e=a_e\beta_e>0,
\qquad
M=\Gamma(\Beta^{-1}-K)\Gamma,
\qquad
\Gamma=\operatorname{diag}(\gamma_e).
```

C53 gives

```math
M\succeq0,\qquad M\mathbf 1=0,\qquad Mt=0.
\tag{ZT.4}
```

Under (ZT.1), all off-diagonal entries of $`K`$ are nonnegative. Therefore the
off-diagonal entries of $`M`$ are nonpositive:

```math
M_{ef}=-\gamma_e\gamma_fK_{ef}\le0\qquad(e\ne f).
```

Together with $`M\mathbf1=0`$, this makes $`M`$ the weighted graph Laplacian with
edge weights $`w_{ef}=\gamma_e\gamma_fK_{ef}\ge0`$. Hence

```math
0=t^{\mathsf T}Mt
=\sum_{e<f}w_{ef}(t_e-t_f)^2.
```

The slopes are pairwise distinct, so every $`w_{ef}=0`$. Thus every off-diagonal
entry of $`K`$ vanishes. The row-sum identity in (ZT.4) then gives $`M=0`$, and
therefore

```math
\boxed{K=\Beta^{-1}.}
\tag{ZT.5}
```

This is an equality alternative inside the promoted C53 theorem. It uses neither the
withdrawn incompatible-orientation regression nor the unpromoted C56 equality chain.
In the canonical C-II branch it is subsequently ruled out by the all-terminal
additive-response theorem and SEPq; this report records the weaker structural
consequences before that final source-network contradiction.

## 3. The diameter components are stars

Let $`T`$ be a connected component of $`H`$. In the forest branch $`T`$ is a tree.
For vertices $`x,y\in V(T)`$, write the incidence identity

```math
e_x-e_y=Qz,
```

where $`z`$ has entries $`+1`$ or $`-1`$ on the unique $`T`$-path from $`x`$ to $`y`$
and is zero elsewhere. Using (ZT.5),

```math
W_{xy}:=(e_x-e_y)^{\mathsf T}\Lambda^+(e_x-e_y)
=z^{\mathsf T}Kz
=\sum_{e\in P_T(x,y)}\beta_e^{-1}.
\tag{ZT.6}
```

Thus the effective-resistance metric restricted to $`V(T)`$ is the positive weighted
tree metric of $`T`$. The actual contact network is circular-planar, so this metric is
Kalmanson in the inherited cyclic order.

Every edge split of a positive weighted Kalmanson tree metric is circular. Indeed, if
an edge split separates $`a,c`$ from $`b,d`$ in cyclic order $`a,b,c,d`$, the tree
four-point relation gives

```math
d(a,c)+d(b,d)<d(a,b)+d(c,d),
```

whereas the Kalmanson inequality gives the reverse inequality.

If $`T`$ contained two vertex-disjoint edges, choose an edge on the tree path between
them. Its circular split would place the two endpoints of one edge in one cyclic
interval and both endpoints of the other edge in the complementary interval. The two
straight diameter chords would then be noncrossing, contradicting the diameter-thrackle
property. Hence $`T`$ has no two disjoint edges. A tree with that property is a star.

The cyclic case is impossible in (ZT.5) by rank: $`Q`$ would have $`h=q`$ columns in
the $`(q-1)`$-dimensional centered terminal space. Thus the equality alternative is
automatically a forest alternative.

## 4. Each star has at most four diameter edges

Let one star component have $`k`$ edges and $`k+1`$ terminals. Formula (ZT.6) is
additive on those terminals: if $`o`$ is the center and $`v_i`$ a leaf, then

```math
W_{v_iv_j}=\beta_{ov_i}^{-1}+\beta_{ov_j}^{-1},
\qquad
W_{ov_i}=\beta_{ov_i}^{-1}.
```

Apply the source-preserving additive-response separator theorem SEPq to the actual
positive contact network, taking only these $`k+1`$ vertices as terminals. If $`k\ge3`$,
SEPq supplies a source vertex $`z`$ whose deletion leaves at most one of these
terminals in each component. Therefore

```math
\deg_C(z)\ge k
```

if $`z`$ is one of the terminals, and $`\deg_C(z)\ge k+1`$ otherwise.

In the fully force-visible C-II branch, loaded terminals have contact degree at most
three and every other contact-core vertex has degree at most five. If the separator is
one of the selected terminals, $`k\le3`$. If it is outside the selected terminal set,
it has degree at least $`k+1`$, so $`k\le4`$. The cases $`k=1,2`$ satisfy the same
bound. Consequently every component of $`H`$ has at most five vertices and at most
four edges.

## 5. ZF and surplus consequences

Woodall gives $`d_H=q-h`$ as the number of tree components of $`H`$. Since each has
at most four edges,

```math
 h\le4d_H.
\tag{ZT.7}
```

On the report-level ZF route, ZS gives $`h\ge\delta\ge\lceil D\rceil`$. Hence

```math
 d_H\ge h/4\ge\lceil D\rceil/4.
```

In the report-level $`s_Z=0`$ circuit phase, E597 gives

```math
\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.597+\varepsilon_{597}
```

for all sufficiently large survivors. Combining with (ZT.2) proves (ZT.3).

In the report-level arbitrary-$`s_Z`$ extension, the same algebra uses the proved
conditional inequality $`\nu_D>0.597+o(1)`$ and gives

```math
\frac{e_{BB}+2s_C}{D}
=\nu_D+3\frac{d_H}{D}
>1.347+o(1).
```

## 6. What this does and does not close

This rules out the zero-transfer equality as a low-component or near-tree diameter
phase. It also gives a finite four-edge cap on every diameter component in that branch.
The result does not rule out a forest made of many bounded stars, including a matching.
It does not control a strictly negative transfer entry, which the weighted four-cycle
regression shows can occur in a general 2-edge-connected block. Finally, the surplus
lower bound (ZT.3) has no opposing global upper bound in the promoted theorem stack.

Therefore the report remains STILL OPEN and should not be promoted as a C-II closure.
