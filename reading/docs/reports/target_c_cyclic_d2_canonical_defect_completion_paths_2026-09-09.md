> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_canonical_defect_completion_paths_2026-09-09.md) · source SHA-256 `585129099b8ca6df9a1705ec85396498948f6c967a2dff36500fd5a4d2db6cf9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-16229A891214","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every cyclic `d_H=2` defect phase is two circular paths joined by two canonical short states

**Date:** 2026-09-09  
**Run type:** exact AD/MT completion unification  
**Target:** primitive cyclic `d_H=2`, all AD branches P2/PS/S2  
**Depends on:** AD defect split; D2 two-tree classification; MT maximal-thrackle completion structure; DG doubled gap for disjoint diameter edges; elementary rotating-calipers monotonicity  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The three AD branches

```text
P2: r_parallel=2, a_short=0
PS: r_parallel=1, a_short=1
S2: r_parallel=0, a_short=2
```

are not three unrelated diameter-graph geometries. After resolving each parallel Minkowski tie by one of its two one-endpoint-at-a-time support transitions, every branch has exactly the same refined antipodal skeleton:

- `q-2` actual radius-`D` diameter states, namely `E(H)`;
- exactly two strictly subdiametral antipodal states `g_1,g_2`;
- `q` unit Minkowski steps around one projective half-boundary.

Every such tie resolution gives a maximal `q`-edge convex thrackle

```math
\boxed{T=H\cup\{g_1,g_2\}.}
\tag{CP2.1}
```

MT forces both short states to join the two D2 diameter-tree components and to lie on the unique odd cycle of `T`.

The two short states cut the projective direction cycle into two arcs. Along either arc, every adjacent pair of actual diameter states is joined by a unit Minkowski step and both states have radius `D`. Hence their projective gap is exactly

```math
\delta:=2\arcsin\frac1{2D}.
```

DG says two disjoint diameter edges require gap at least `2delta`, so each adjacent pair on such an arc shares an endpoint. Therefore each D2 tree component admits an Euler ordering of all of its edges and must be a path.

### Main conclusion

For **every** primitive cyclic `d_H=2` survivor,

```math
\boxed{H=P_A\sqcup P_B}
\tag{CP2.2}
```

is the disjoint union of two nontrivial paths. Their path vertices lie on two circles of the same universal radius

```math
\boxed{
R_D=\frac{D}{2\cos(\delta/2)}
=\frac{D^2}{\sqrt{4D^2-1}}.
}
\tag{CP2.3}
```

The only phase dependence P2/PS/S2 is the local geometry of the two short cross-component completion states:

- a parallel-side defect contributes one short state of fixed length `sqrt(D^2-1)` but with two canonical endpoint-switch choices;
- an off-circle difference-body vertex contributes one fixed short antipodal state of its actual radius `<D`.

Thus after the separate P2 exclusion, the entire live `d_H=2` branch PS/S2 is two explicit equal-radius circular zigzag paths connected at their endpoints by two short antipodal defect chords.

---

## 1. Refine the difference-body half-boundary

Let

```math
K=F-F.
```

AD gives

```math
r_\parallel+a_{short}=2.
\tag{1.1}
```

Choose one projective half of the centrally symmetric K-boundary.

It contains

```math
q-r_\parallel
```

K-vertices, of which

- `q-2` are radius-`D` circular vertices and therefore actual oriented diameter states;
- `a_short` are strictly inside the radius-`D` circle and represent short vertex-vertex antipodal chords of `F`.

Each parallel side pair of `F` produces one length-two K-edge in this projective half. Such an edge is the merge of two codirected unit Minkowski contributions, one from `F` and one from `-F`.

Resolve that tie by ordering the two support changes one at a time. There are two choices. Either choice inserts one intermediate vertex-difference state between the two endpoints of the length-two K-edge and splits it into two unit steps.

If the tie comes from parallel unit shell sides `ab,cd` with opposite orientations, the two possible intermediate states are the two other rectangle chords. As in the P1/P2 rectangle calculation, their common length is

```math
\boxed{\sqrt{D^2-1}<D.}
\tag{1.2}
```

After choosing a resolution independently at every one of the `r_parallel` ties, the refined projective half-boundary therefore has

```math
(q-r_\parallel)+r_\parallel=q
```

states and exactly `q` unit steps.

Its short states are precisely

```math
a_{short}+r_\parallel=2.
```

Call the corresponding two unoriented antipodal chords

```math
g_1,g_2.
```

Every other refined state is one of the `q-2` actual diameter edges of `H`.

---

## 2. The refined antipodal state graph is a maximal convex thrackle

We include the crossing argument rather than treating the rotating-calipers language as a black box.

Every state in the refined sequence is a vertex-vertex antipodal pair of the strictly convex polygon `F`: it is obtained at a support normal for which both supporting points are vertices, after one of the two possible one-at-a-time choices at a parallel tie.

Take two distinct refined antipodal chords. Lift their support-normal parameters to one interval of length `<pi` and order them. As the normal rotates, the maximizing support vertex moves monotonically forward around `partial F`, and the minimizing support vertex does the same on the opposite side. Hence the two endpoint pairs alternate in convex boundary order unless they share an endpoint.

Therefore any two refined antipodal chords either share one endpoint or cross properly. They form a convex straight-line thrackle.

There are exactly `q` such chords on the `q` shell vertices. A convex thrackle has at most `q` edges, so the refined graph is maximal. Denote it

```math
T.
```

By construction

```math
\boxed{E(T)=E(H)\sqcup\{g_1,g_2\}.}
\tag{2.1}
```

This proves CP2.1.

Different tie resolutions can give different maximal completions in P2/PS. The theorem applies to every chosen resolution.

---

## 3. The two short states are exactly the two MT completion edges

MT classifies maximal convex-thrackle completions of the `d_H=2` diameter forest. For every such completion, the two added edges

1. are strictly subdiametral;
2. join the two diameter-tree components;
3. lie on the unique odd cycle of the maximal thrackle.

Our refined `T` is a maximal completion of `H` by exactly the two short edges `g_1,g_2`. Therefore MT applies directly:

```math
\boxed{
g_1,g_2\text{ both join }T_A\text{ to }T_B.}
\tag{3.1}
```

and

```math
\boxed{
g_1,g_2\text{ both lie on the unique odd cycle of }T.}
\tag{3.2}
```

In particular the two short states are not pendant artifacts of the rotating-calipers refinement. They are precisely the two cross-component cycle edges needed to close the D2 forest into a maximal antipodal thrackle.

---

## 4. Remove the two short states from direction order

Traverse the `q` refined antipodal states in their projective support order. Remove the two short states `g_1,g_2`.

The remaining states are exactly the `q-2` actual diameter edges of `H`. The two deleted positions cut the cyclic list into at most two nonempty linear arcs of actual diameter states.

Take two consecutive actual states `e,f` on one such arc. No parallel tie and no short K-vertex lies between them in the refined list. Their difference-body vectors are both on the radius-`D` circle and the K-boundary step between them has Euclidean length one.

Hence their projective angle is exactly

```math
\boxed{\angle_{proj}(e,f)=\delta.}
\tag{4.1}
```

DG gives for vertex-disjoint actual diameter edges

```math
\angle_{proj}(e,f)\ge2\delta.
```

Thus `e,f` must share an endpoint.

Edges in different D2 components share no endpoint. Therefore each connected arc of actual states belongs to one component.

Both components are nonempty, and all `q-2` H-edges occur. Hence the two arcs are exactly the complete edge sets of `T_A` and `T_B`, in some order.

So:

```math
\boxed{
\text{each diameter component occupies one contiguous block between }g_1,g_2.
}
\tag{4.2}
```

---

## 5. Each component is a path

Fix one component and list its edges in its projective block:

```math
e_1,e_2,\ldots,e_m.
```

Every consecutive pair shares an endpoint. Since each edge appears once, this is a trail traversing every edge of the tree exactly once: an Euler trail.

A nontrivial finite tree with a vertex of degree at least three has at least three leaves. Its leaves are odd-degree vertices, and parity then prevents an Euler trail with only zero or two odd vertices. Equivalently, a tree admits an Euler trail exactly when it is a path.

Therefore

```math
\boxed{T_A,T_B\text{ are paths}.}
\tag{5.1}
```

This proves CP2.2.

The result is stronger than D2's ordered-caterpillar conclusion and holds uniformly in PS/S2 as well as P2.

---

## 6. Every component path lies on the universal circle

Write one component path in edge order as

```math
a_0a_1,a_1a_2,\ldots,a_{m-1}a_m.
```

Every path edge is an actual diameter edge:

```math
|a_{k+1}-a_k|=D.
\tag{6.1}
```

Every consecutive pair in projective direction is separated by `delta` and shares the middle endpoint. Therefore the two nonshared endpoints satisfy

```math
|a_{k+2}-a_k|
=2D\sin\frac\delta2
=1.
\tag{6.2}
```

As in the P2-specific CP calculation, convex direction order chooses one consistent orientation sign and the path-edge vectors obey

```math
a_{k+1}-a_k
=D(-1)^k e^{i(\theta+k\delta)}.
\tag{6.3}
```

Summing the geometric progression gives a center `C` such that

```math
|a_k-C|
=\frac{D}{2\cos(\delta/2)}
=:R_D
```

for every path vertex.

Thus both components lie on circles of equal radius `R_D`, proving CP2.3.

Their two D2 bipartition classes are the even/odd path subsequences, and the two corresponding shell blocks are unit-chord arcs on the component circle.

---

## 7. Endpoint interpretation of PS and S2

After the P2 exclusion, the two live AD branches are:

### PS

One defect state comes from the unique parallel-side tie. It has fixed short length

```math
\sqrt{D^2-1}
```

and two canonical choices, corresponding to the two support-change orders across the `1 x sqrt(D^2-1)` rectangle.

The other defect state is the unique genuine off-circle vertex pair of `K` and has some radius

```math
\rho<D.
```

Both are cross-component edges joining the two endpoint regions of the circular paths.

### S2

There are no parallel ties. The two short states are the two off-circle antipodal vertex pairs of `K`, with lengths

```math
\rho_1,
ho_2<D.
```

The completion is canonical: it is the full vertex-vertex antipodal graph of `F`.

Thus every live `d_H=2` endpoint can now be represented as

```text
circular path A
   -- short cross-edge g1 --
circular path B
   -- short cross-edge g2 --
```

in projective antipodal order.

---

## 8. What remains continuous

All ordinary mechanical geometry is now fixed by `D` and the two path lengths. The remaining continuous data are concentrated at the two short connectors:

1. their lengths `|g_1|,|g_2|<D`;
2. the two local support-change angles around them;
3. equivalently, the relative displacement and phase of the two equal-radius component circles.

The path interiors carry no further shape freedom.

This is the correct finite state space for PS/S2.

---

## 9. Regression audit

### Parallel ties

A tie is not itself a vertex of `K`. The report inserts exactly one intermediate vertex-vertex antipodal state after choosing one of the two support-change orders. That state is a short completion chord. It does not insert both alternatives simultaneously.

### Number of short states

The count is exact:

```math
r_\parallel+a_{short}=d_H=2.
```

Each tie contributes one chosen short state; each off-circle antipodal K-vertex pair contributes one fixed short state. Hence every refined completion has exactly two short edges.

### Crossing theorem

The maximal-thrackle claim uses monotone support indices for vertex-vertex antipodal pairs. It does not claim an arbitrary set of short chords is a thrackle.

### Euler-trail step

The two short states are the only separators where consecutive H-edges can change component without an ordinary radius-D/unit-step transition. Therefore each entire component really is one linear block before the Euler argument is applied.

### P2

Included by the theorem, but separately excluded by PX on PR #139 for `D>sqrt2`.

---

## 10. Next theorem

The live PS/S2 problem is now a two-circle/two-connector problem.

For each endpoint diameter edge, its component-circle center lies a fixed perpendicular distance

```math
h_D=\frac1{4\cos(\delta/2)}
```

from the edge midpoint. A short connector state between an A endpoint edge and a B endpoint edge is produced by two unit shell transitions in the refined support list.

The next target is to write the exact vector relation for

```math
C_B-C_A
```

through one arbitrary short state of length `rho<D`. Equating that relation for `g_1` and `g_2` should reduce PS/S2 to a finite pair of scalar equations. P2 is the special endpoint `rho=sqrt(D^2-1)` where those equations already contradict distinct parallel directions.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

AD: d_H=2 has r_parallel+a_short=2. Resolve each parallel length-2 K edge by one of
its two one-endpoint-at-a-time support changes. In one projective half this inserts one
short vertex-difference state per tie. Together with the a_short off-circle K states,
there are exactly two short states g1,g2 and q total unit Minkowski steps. The refined
q-state antipodal graph is a maximal convex thrackle T=H+{g1,g2}. MT forces both g_i
to join the two D2 tree components and lie on T's unique odd cycle.

Delete g1,g2 from projective state order. Between them, adjacent remaining states are
radius-D vertices joined by unit K edges, so their gap is delta=2asin(1/(2D)). DG says
disjoint diameter edges need >=2delta; therefore every such pair shares an endpoint and
belongs to one component. The two arcs are exactly the two components. Each component's
complete edge list is an Euler trail, hence each tree is a path.

For either path:
  |a_{k+1}-a_k|=D,
  |a_{k+2}-a_k|=1,
  a_{k+1}-a_k=D(-1)^k exp(i(theta+k delta)),
so all its vertices lie on a circle of radius
  R_D=D/[2cos(delta/2)]=D^2/sqrt(4D^2-1).

Thus all live d_H=2 geometry is two equal-radius circular zigzag paths joined by two
short cross-component antipodal states. PS has one tie-state of length sqrt(D^2-1) and
one genuine short K state; S2 has two genuine short K states. Next: derive the exact
component-center displacement through one general short state and equate the two defects.
```
