> Generated reading edition · [exact source](../../../docs/reports/target_c_near_lattice_loaded_hull_exclusion_2026-09-25.md) · source SHA-256 `815c4495fbfe12eaa7cbbc52aeb4a831118d0893615b1a45666fa9a7ebba160d`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6A191BDFBF7D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_near_lattice_loaded_hull_exclusion_2026-09-25.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=9212cf111587a425ebcc604be31560995936c765; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — a fixed-scale lattice-shadow obstruction for the loaded hull

**Phase 2 preservation provenance:** PR #579, branch swarm/gpt6/c2-source-detour, audited source head ed21248321fea8f8e99d257da60ca9e11417b814. Preserve as an unreviewed geometric candidate plus its explicit regression: linear lattice-shadow outliers alone do not pay the outer-walk detour; the canonical chart-cover premise remains missing.

- **Date:** 2026-09-25
- **Research-start commit:** `60e0d60801e1abfa2cfba65ba82ce89740c399f0` (fetch initially failed)
- **Verified current main:** `f5f68718da7d742128fb7b297854161550d2cce8` (fetched after the proof; state and route files unchanged)
- **State version:** `2026-09-14.audit.51`
- **Run type:** closing-proof attempt / exact geometric reduction
- **Target:** C-II full-core branch
- **Starting status:** canonical full-core near-disk theorem; aggregate detour and inactive-container branches open
- **Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
- **External literature search:** not used
- **Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting canonical endpoint and attempted chain

Canonical Section 80 makes the actual loaded force hull `F` approach a diameter-`D`
disk in relative Hausdorff distance. Section 63 gives `b+Q=2(q-k)`, where `q` is
the number of loaded hull vertices, `b>=per(F)`, `Q>=0`, and `k>=0`. Consequently
`q>=(pi/2-o(1))D`. Sections 122–123 force a positive aggregate harmonic-cell
detour but do not turn it into a strict same-cardinality sub-`D` source.

The line tested here was

```text
uniform common lattice shadow of the loaded hull
    -> quantitative convex near-lattice vertex bound
    -> contradiction with q >= (pi/2-o(1))D
    -> eliminate that full-core subbranch.
```

The geometric bound is proved below. The canonical stack does not give the first
arrow for every full-core survivor, so this is a subbranch exclusion only. A prior
unreviewed report, `target_c_affine_lattice_boundary_vertex_exclusion_2026-09-11.md`,
already excludes the exact-lattice case. The new statement allows a fixed positive
error and counts how many actual loaded vertices must miss every single lattice.

## 2. New result

**Classification:** proved candidate awaiting independent audit; noncanonical.

### Theorem NL.1 — convex near-lattice vertex bound

There is an absolute constant `C` with the following property. Let `P` be a convex
polygon of diameter `D`, with `q` distinct extreme vertices separated pairwise by
at least one. Suppose, after one translation, that

```math
B(0,r)\subseteq P\subseteq B(0,R),\qquad
0<r\le R,\qquad \eta:=1-r/R,
```

let `m` of the `q` vertices have distance greater than `epsilon` from one
translate of a lattice
```math
\Lambda=\mathbb Zu+\mathbb Zv,\qquad |u|=|v|=1,\qquad
\angle(u,v)\in[\pi/3,2\pi/3].
```

For `0<=epsilon<=1/100` and `0<=eta<=1/100`,

```math
\boxed{q-2m\le C D\bigl(\sqrt\epsilon+\eta^{1/6}\bigr).}
\tag{NL.1}
```

The constant is uniform in the lattice angle and the lattice translation. The
bound is asymptotic in no hidden parameter; enlarging `C` covers the small values
of `D` and the harmless integer rounding below.

### Proof

We give the counting details because the exact-lattice vertex theorem alone does
not control repeated lattice edge vectors after small vertex perturbations.

**Step 1: a short normal-arc bound.** Put
```math
\alpha:=\arccos(r/R)\le C_1\sqrt\eta.
```
At any point `x` of an edge of `P`, its outward supporting normal `n` satisfies
`n dot x=h_P(n)>=r` and `|x|<=R`. Thus the radial direction of `x` differs from
`n` by at most `alpha`. Consider all edges whose oriented tangent directions lie
in one angular interval `J` of width `w<=1/4`. Convexity puts these edges in one
contiguous boundary chain (allowing empty edges between them). Every point of that
chain lies in an annular sector of radial angular width at most `w+2alpha` and
radii between `r` and `R`. Two points in this sector are at distance at most
```math
R(w+2\alpha)+(R-r).
```
Closing the convex chain by the chord between its endpoints makes a convex polygon.
The perimeter-diameter inequality for that polygon bounds the chain length by
```math
\boxed{\operatorname{length}(J)
\le \pi\{R(w+2\alpha)+(R-r)\}
\le C_2D(w+\sqrt\eta).}
\tag{NL.2}
```
Here `R<=D/2+o(D)` is not needed: the diameter of `P` lies between `2r` and
`2R`, so `R<=D/[2(1-eta)]`, and `R-r=R eta` is absorbed by `R sqrt(eta)`.
The same bound, with a larger absolute constant, holds for wider angular
intervals: once `w>=1/4`, the whole perimeter `<=pi D` is already `O(Dw)`.

**Step 2: assign lattice edge vectors.** Call a vertex good when it is within
`epsilon` of the lattice. At most `2m` polygon edges touch a bad vertex, so at
least `q-2m` edges have two good endpoints. Assign one lattice point `z_i`
within `epsilon` of each good vertex `p_i`. Since `2epsilon<1` and the actual
vertices are unit separated, assigned lattice points at distinct good vertices
are distinct. For each good-good edge set
```math
v_i=z_{i+1}-z_i,\qquad e_i=p_{i+1}-p_i.
```
The lattice minimum distance is one: vectors with both integer coefficients in
`{-1,0,1}` are checked directly, while every other nonzero vector has squared
length at least `(a^2+b^2)/2>=2`. Then `v_i` is a nonzero lattice vector and
`|e_i-v_i|<=2epsilon`. The angle between
`e_i` and `v_i` is at most `C_3 epsilon/|v_i|`; in particular, for a fixed lattice
vector `v`, all edges with `v_i=v` have tangents in an interval of width at most
`C_4 epsilon/|v|<=1/4`. Their total number is at most their total length because
each actual edge has length at least one. By (NL.2), that number is at most
```math
C_5D(\epsilon/|v|+\sqrt\eta).
\tag{NL.3}
```

**Step 3: sum short vectors and pay long edges by length.** Uniformly over the
angle range,
```math
|au+bv|^2=a^2+b^2+2ab\cos\theta
\ge (a^2+b^2)/2.
```
Consequently the number of lattice vectors of length at most `M` is `O(M^2)`,
and the sum of their reciprocal lengths is `O(M)`, with absolute constants. Sum
(NL.3) over all nonzero vectors of length at most `M`:
```math
q_{\le M}^{\rm good}\le C_6D(\epsilon M+M^2\sqrt\eta).
\tag{NL.4}
```
An edge assigned a vector longer than `M` has actual length at least
`M-2epsilon`. Since `per(P)<=pi D`,
```math
q_{>M}^{\rm good}\le {\pi D\over M-2\epsilon}.
\tag{NL.5}
```
For `M>=2`, (NL.4)–(NL.5) give
```math
q-2m\le C_7D(\epsilon M+M^2\sqrt\eta+M^{-1}).
\tag{NL.6}
```
Choose `M` comparable to
`min(epsilon^(-1/2), eta^(-1/6))`, interpreting a zero
parameter as infinity. This makes the three terms in (NL.6) at most constant
multiples of `sqrt(epsilon)+eta^(1/6)`. If both parameters vanish, let `M` tend
to infinity in (NL.6); no finite polygon with the stated disk sandwich exists.
This proves (NL.1). Taking `m=0` gives the all-vertex shadow bound. `square`

### Corollary NL.2 — linear loaded-hull outlier population

There are universal constants `epsilon_*>0` and `c_*>0` such that, for every
sufficiently large canonical C-II full-core Type-II survivor and every translate
of every unit oblique lattice whose angle is in `[pi/3,2pi/3]`, at least `c_*D`
loaded force-hull vertices have distance greater than `epsilon_*` from that
lattice. In particular no sequence of these loaded hulls has a common-lattice
vertex shadow with maximum error `o(1)`.

**Proof.** Section 80 supplies a disk center with `r/D,R/D->1/2`, so `eta->0`.
Section 63 supplies
```math
q\ge q-k={b+Q\over2}\ge{\operatorname{per}(F)\over2}
 =(\pi/2-o(1))D.
```
The loaded vertices are actual source points and are unit separated. Apply NL.1.
Choose a fixed `epsilon_*` so small that `C sqrt(epsilon_*)<pi/8`. Since
`eta->0`, NL.1 then gives, for all sufficiently large `D`,
`q-2m<=(pi/4)D`. The lower bound on `q` yields
`m>=(pi/8-o(1))D`; some fixed `c_*<pi/8` works. `square`

### Corollary NL.3 — a near-exact finite atlas needs linear hull transitions

Let the vertices of a polygon satisfying NL.1 be labelled by `t` translates of
unit oblique lattices in the same angle range. Suppose each vertex lies within
`epsilon` of the lattice bearing its label. Let `T` count polygon sides whose
endpoint labels differ. Then
```math
\boxed{q-T\le CtD(\sqrt\epsilon+\eta^{1/6}).}
\tag{NL.7}
```

Indeed, there are exactly `q-T` same-label sides. For each fixed label, Steps
1–3 of NL.1 count its same-label sides by the displayed bound; the proof never
uses sides of other labels. Sum over the `t` labels. In a canonical full-core
Type-II sequence, if `t` is bounded and `epsilon=o(1)`, then
```math
\liminf_{D\to\infty}{T\over D}\ge {\pi\over2}.
\tag{NL.8}
```
More generally this holds when
`t(sqrt(epsilon)+eta^(1/6))->0`. Thus a fixed number of
near-exact affine grains can cover the loaded hull only if their labels
alternate along a linear number of actual hull sides. This counts hull label
changes, not contact edges or harmonic-cell interface length.

### Theorem NL.4 — near-lattice subsets of the curved hull

The transition conclusion can be strengthened. Under the disk-sandwich and
unit-separation hypotheses of NL.1, let `S` be **any subset** of the extreme
vertices of `P` whose members lie within `epsilon` of one translate of one
unit oblique lattice. The vertices of `S` need not be adjacent on `partial P`.
For `D` sufficiently large, `epsilon<=1/100`, and `eta<=1/100`, an absolute
constant `C'` satisfies
```math
\boxed{|S|\le C'D\bigl(\sqrt\epsilon+\eta^{1/6}+D^{-1/4}\bigr).}
\tag{NL.9}
```

**Proof.** List `S` in the cyclic order inherited from `partial P`, and join
successive members to form the convex polygon `P_S`. Every member remains an
extreme vertex of `P_S`. Its perimeter is at most `pi D`, and its sides have
length at least one. At most one cyclic side of `P_S` skips a parent-boundary
arc of radial angular width greater than `pi`; discard that side from the
count. The other sides correspond to pairwise interior-disjoint arcs of
`partial P` in the same cyclic order.
The assertion is immediate for `|S|<=2`, so assume `|S|>=3` below.

We first record the short-chord transfer. Let `a,b` be the endpoints of one
remaining side of `P_S`, and suppose `|a-b|<=2M` with `M/D` small. Because
`|a|,|b|>=r`, the radial angular separation `Delta` of the short parent arc
satisfies
```math
2r\sin(\Delta/2)\le |a-b|\le2M,
\qquad \Delta\le C_8M/D.
\tag{NL.10}
```
The first inequality follows by expanding `|a-b|^2` and using both radii at
least `r`. Since the origin lies inside `P`, radial angle increases in the
boundary order. Every point of this parent arc has radial direction between
those of `a` and `b`. Each of its supporting normals differs from that radial
direction by at most `alpha=arccos(r/R)<=C_1 sqrt(eta)`, as in NL.1. Thus
the tangent directions of all parent edges on the arc lie in one cone of width
at most `Delta+2alpha`. The vector `b-a` is the sum of these parent-edge
vectors. Because this cone has width less than `pi`, the chord direction also
lies in it. Hence every parent-edge tangent on the arc differs from the chord
direction by at most `C_9(M/D+sqrt(eta))`.

Assign distinct lattice points to the members of `S` as in NL.1. If a side
`ab` of `P_S` has assigned lattice vector `v` with `|v|<=M`, then
`|a-b|<=M+2epsilon<=2M`; its chord direction differs from that of `v` by at
most `C_3 epsilon/|v|`. By the short-chord transfer, its associated parent
arc consists only of parent edges with tangents in a cone around `v` of
width
```math
C_{10}(\epsilon/|v|+M/D+\sqrt\eta).
\tag{NL.11}
```
The parent arcs associated to successive `P_S` sides are disjoint except at
endpoints. Each has length at least `|a-b|>=1`. Applying the parent normal-arc
bound (NL.2) to the cone in (NL.11), the number of `P_S` sides assigned the
same short vector `v` is at most
```math
C_{11}D(\epsilon/|v|+M/D+\sqrt\eta).
\tag{NL.12}
```
The discarded wrap side, if any, costs one side and needs no assignment.

There are `O(M^2)` vectors with `|v|<=M`, and their reciprocal lengths sum to
`O(M)`, uniformly over the allowed lattice angles. Thus all short assigned
sides number at most
```math
C_{12}(D\epsilon M+M^3+DM^2\sqrt\eta).
\tag{NL.13}
```
Every remaining side assigned `|v|>M` has length at least `M-2epsilon`.
Since `per(P_S)<=pi D`, there are at most `pi D/(M-2epsilon)` such sides.
Including the one discarded side,
```math
|S|\le1+C_{13}D
\bigl(\epsilon M+M^3/D+M^2\sqrt\eta+M^{-1}\bigr).
\tag{NL.14}
```
Take `M` comparable to
`min(epsilon^(-1/2),eta^(-1/6),D^(1/4))`, with a zero
parameter interpreted as infinity. Each term in (NL.14) is bounded by a
constant multiple of `sqrt(epsilon)+eta^(1/6)+D^(-1/4)`. The added one is
absorbed for large `D`. This proves (NL.9). `square`

### Corollary NL.5 — fixed finite near-lattice atlases miss linear population

Fix any integer `t>=1`. There are constants `epsilon_t,c_t>0` such that every
sufficiently large canonical full-core Type-II loaded hull has at least
`c_tD` vertices farther than `epsilon_t` from the union of **any** `t`
translates of unit oblique lattices in the allowed angle range. The lattices
may have different angles and translations. Indeed, if `S_i` is the subset
within `epsilon_t` of the `i`th lattice, NL.4 bounds each `|S_i|` by
`C'D(sqrt(epsilon_t)+o(1))`. Choose `epsilon_t` so that
`tC'sqrt(epsilon_t)<pi/4`, then combine the union bound with
`q>=(pi/2-o(1))D`. No disjointness or connected-grain premise is needed.

### Regression NL.R1 — lattice outliers do not by themselves pay outer-walk detour

For every even `N>=6`, put `t=pi/N`, `R=1/sin(t)`, and
```math
A_j=R(\cos(2jt),\sin(2jt)),\qquad
M_j={A_j+A_{j+1}\over2},\qquad j\in\mathbb Z/N\mathbb Z.
```
The source `X_N={A_j,M_j:j in Z/NZ}` is unit separated and triangle-free.
Its only unit contacts are the cycle edges `A_jM_j` and `M_jA_{j+1}`.
Its force hull for those positive contacts is the regular `N`-gon
`F_N=conv{A_j}`. Its diameter is `D=2R`, its inradius is `r=R cos(t)`, and
```math
{N\over D}={N\sin t\over2}\longrightarrow{\pi\over2},
\qquad 1-r/R=1-\cos t\longrightarrow0.
```
Therefore NL.5 applies to `F_N`: any fixed finite collection of unit oblique
lattices misses `cD` of its actual hull vertices at a fixed positive distance.
Nevertheless each hull side has length two and is exactly the straight
two-contact path `A_j,M_j,A_{j+1}`. The outer contact-face walk has length
`b=2N=per(F_N)`, so its **metric** detour `b-per(F_N)` is exactly zero.

Here is a direct check of source feasibility and stress. The `2N` points have
equally spaced radial arguments `jt`, with alternating radii `R` and
`R cos t`. Two outer vertices are at distance at least two. Two midpoints are
at distance at least `2 cos t>1`. A mixed pair at angular distance `t` is a
listed contact of length one; every other mixed pair has larger angular
distance up to `pi` and hence distance greater than one. Thus the displayed
cycle is the entire unit-contact graph. In particular it has no triangle.

Give every cycle contact multiplier one. At a midpoint the contact-force sum
vanishes. At an outer vertex, writing `e_j=A_j/R`,
```math
(A_j-M_{j-1})+(A_j-M_j)=2\sin t\,e_j.
```
The only active diameter pair at `A_j` is `A_jA_{j+N/2}`, whose vector is
`D e_j`. Giving each opposite diameter pair the positive multiplier
`2 sin(t)/D` balances the displayed contact force at every outer vertex.
Thus even positive first-order contact/diameter equilibrium does not make the
outlier population pay positive `b-per(F)`.

The example can be made dense while retaining every source point. Choose a
triangular lattice of spacing `1+1/R`, and add every lattice point in
`B(0,r-2)` to `X_N`. Such points are contact-isolated: they have mutual
distances greater than one and their distance from the contact ring is at
least two. Their pair distances are strictly below `D`, so the active diameter
pairs and the positive equilibrium above remain unchanged. Elementary
fundamental-cell counting gives, for the enlarged source,
```math
|X_N|={\pi\over2\sqrt3}D^2+O(D).
```
This is the leading triangular-packing density, yet the source is still
triangle-free and has zero hull metric detour. The construction is **not**
claimed to be a global diameter minimizer or a canonical full-core source;
the added points are contact-isolated and the ring core does not satisfy the
canonical post-ZF rank conclusion: on its `v=2N` nonisolated vertices it has
only `e+h=2N+N/2<2v-2` contact-plus-diameter rows. It rules out any payment argument using
only near-disk hull geometry, leading-order density, positive first-order
equilibrium, and the NL.5 outlier count.

### Scope and dependencies

NL.1 concerns arbitrary unit-separated convex polygons with the displayed disk
sandwich and a partial lattice-vertex shadow. It does not assume a contact graph, stress,
or global minimality. NL.4 concerns any lattice-near subset of the **actual
parent hull vertices**, so its convexity and disk sandwich remain those of the
parent hull. NL.2 and NL.5 concern the actual loaded vertices of the canonical
full-core Type-II source. Other source points, including contact-isolated ones,
remain present and are not assigned lattice points. Their only canonical inputs
are Section 63's outer-walk identity and Section 80's full-core near-disk
conclusion. The exact-lattice report cited above is prior art, not a dependency.

## 3. Frontier effect

This proves a fixed-scale, linear-population obstruction: every single unit
oblique lattice misses a linear number of actual loaded hull vertices. NL.4
upgrades this to **any fixed finite collection** of near-exact lattice charts,
without a condition on chart transitions. Neither count is yet a canonical
detour payment. NL.R1 shows that no payment into the hull metric detour can
follow from these geometric counts plus leading density and positive
first-order equilibrium alone.
The canonical theorem state remains unchanged. A general full-core survivor can
use multiple grains or a nonlattice contact mesh; NL.2 does not bound its aggregate
outer-walk detour or produce a strict sub-`D` competitor. The macroscopic
inactive-container branch is untouched.

## 4. Exact remaining lemma

The exact next bridge for this mechanism is a payment theorem for either the
`c_tD` loaded vertices outside every fixed finite near-lattice atlas: under
the canonical full-core hypotheses, show that the forced quantity
either gives an exact unit triangle, a same-cardinality feasible source of
diameter strictly below `D`, or an aggregate Section-122/123 detour charge that
exceeds the loaded-hull budget. None of these payments is currently proved;
NL.R1 shows that the payment must use more than a near-disk hull, leading
density, and positive first-order equilibrium. In particular it must use the
canonical post-ZF rank/full-core structure or an equally strong source-level
hypothesis. The regression's zero `b-per(F)` does not directly test the
Section-122 attachment-cell detour, which is defined only in the canonical
full-core analysis.
multiple grains and phase drift may account for the outliers and transitions.
C-II would still need the separate macroscopic-container branch closed.

## 5. Claim audit

| Claim | Status | Dependency | Reason |
| --- | --- | --- | --- |
| NL.1 quantitative near-lattice vertex bound | proved candidate awaiting promotion | elementary convex geometry | Complete proof above; independent audit still required |
| NL.2 linear loaded-hull outlier count | proved candidate awaiting promotion | NL.1; canonical §§63, 80 | Applies to actual loaded vertices in full-core branch |
| NL.3 finite-atlas hull transition bound | proved candidate awaiting promotion | NL.1 proof; canonical §§63, 80 for asymptotic conclusion | Counts actual loaded-hull sides, not contact interface |
| NL.4 arbitrary near-lattice subset bound | proved candidate awaiting promotion | NL.1 normal-arc bound; elementary chord geometry | Does not assume adjacent labelled vertices |
| NL.5 finite-atlas linear outlier count | proved candidate awaiting promotion | NL.4; canonical §§63, 80 | Applies to actual loaded vertices; fixed atlas size |
| NL.R1 regular contact-ring counterexample | regression | elementary exact construction | Rules out an outlier-to-hull-metric-detour implication under weak source hypotheses |
| Outlier-to-detour or strict-competitor payment | unreviewed missing premise | none | Not supplied by harmonic-cell theory |
| Full C-II or Level I closure | not claimed | would require the payment and container closure | Global quantifiers remain open |

## 6. Regressions checked

- Exact affine-lattice exclusion is already in the September 11 unreviewed
  boundary-vertex report. NL.1 strengthens its hypothesis to a positive error;
  it does not re-label that prior report canonical.
- The disk sandwich matters. A nearly straight convex chain can contain many
  near-collinear unit-spaced points after tiny outward perturbations; NL.2 does
  not apply to a flat or highly anisotropic hull.
- The lower lattice singular-value bound matters. The count of short lattice
  vectors would not be uniform for a degenerating lattice.
- The proof counts actual convex-hull vertices, not repeated outer-walk
  occurrences, harmonic-cell attachments, or contact-isolated source points.
- No numerical approximation or local optimality is used to claim global
  diameter minimality.

## 7. Literature and computation

No external theorem is imported. The perimeter-diameter inequality is the
elementary convex Cauchy bound already used in the canonical route. No script is
load-bearing.

## 8. Promotion recommendation and handoff

Keep this report **unreviewed** pending independent geometric audit. It does not
change the current prompt or canonical state. An auditor should check the normal
arc estimate (NL.2), including degenerate short chains, and the uniform lattice
vector count and the short-chord transfer (NL.10)–(NL.12). The next research
step is the exact payment in §4, with particular
attention to multi-grain and phase-drift configurations. Read canonical §§63,
80, 122–123 and the current Target C route map before attempting that step.
