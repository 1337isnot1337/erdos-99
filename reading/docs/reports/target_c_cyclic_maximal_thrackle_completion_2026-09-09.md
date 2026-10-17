> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_maximal_thrackle_completion_2026-09-09.md) · source SHA-256 `14f70efe3664183aa0a08f6f7fd173b005eb37195654965a6ef2f53beffd98f6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-DE4491489475","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every cyclic diameter graph is a maximal convex thrackle with at most two short cycle chords

**Date:** 2026-09-09  
**Repository branch:** PR #118 after DC/D2/EU/SL  
**Run type:** exact convex-thrackle completion / unified cyclic normal form  
**Target:** complete cyclic primitive endpoint, `d_H=0,1,2`  
**Depends on:** DC component classification, D2 four-block theorem, classical maximal-convex-thrackle structure  
**External literature:** standard theorem that every edge-maximal convex thrackle on `q` convex vertices consists of one odd cycle plus degree-one vertices attached to that cycle, and has exactly `q` edges  
**Computation:** small exact convex-thrackle enumeration was used only to reject uniqueness; it is not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

The cyclic endpoint has

```math
|E(H)|=h=q-d_H,
\qquad d_H\in\{0,1,2\}.
```

Thus its full actual diameter graph is within at most two edges of the extremal size of a convex thrackle. Extending the edge set greedily on the same cyclic vertex set gives a much sharper unified normal form.

### Theorem MT — two-defect maximal-thrackle completion

There exists a maximal convex thrackle `T` on the same `q` shell vertices such that

```math
H\subseteq T,
\qquad
|E(T)\setminus E(H)|=d_H.
\tag{MT.1}
```

The maximal graph `T` consists of one odd cycle `C_T` with every remaining vertex a degree-one leaf attached directly to a cycle vertex. Moreover every added edge

```math
g\in E(T)\setminus E(H)
```

lies on `C_T`. Consequently:

- every pendant edge of `T` is an actual diameter edge of length exactly `D`;
- every cycle edge already in `H` has length exactly `D`;
- the only edges of `T` whose lengths are below `D` are the `d_H` added cycle edges.

Hence the complete cyclic endpoint admits a single description:

```math
\boxed{
\text{odd-cycle-plus-leaves maximal convex thrackle with exactly }d_H\le2
\text{ short cycle chords}.}
\tag{MT.2}
```

The three phases are:

```math
\begin{array}{c|c|c}
 d_H & H & T\setminus H\\ \hline
0 & T & \varnothing\\
1 & T-g\text{ is a spanning tree} & \{g\},\\
2 & T-\{g_1,g_2\}\text{ is two trees} & \{g_1,g_2\}.
\end{array}
\tag{MT.3}
```

For `d_H=2`, both added chords join the two D2 tree components and are opposite-corner chords of the four-block partition.

For `d_H=1`, at every KKT endpoint zeroed nonleaf edge `e`, every maximal-completion edge `g` crosses the two components of `H-e`; both `e` and `g` are opposite-corner chords for the EU four-block cut.

This turns the tree phases into one- and two-edge defects of the exact Reinhardt diameter-skeleton topology.

---

## 1. Greedy completion has exactly `d_H` new edges

Fix the `q` force-hull vertices in their cyclic convex order. A convex thrackle is an edge set in which every two edges meet, either at a common endpoint or by a proper crossing.

The full diameter graph `H` is a convex thrackle. Because there are finitely many chords on the fixed vertex set, repeatedly add any chord meeting every current edge until no further chord can be added. This produces an edge-maximal convex thrackle `T` with

```math
H\subseteq T.
```

The standard classification of maximal convex thrackles says that `T` consists of one odd cycle plus leaves attached directly to cycle vertices. In particular

```math
|E(T)|=q.
\tag{1.1}
```

Since

```math
|E(H)|=q-d_H,
```

we obtain

```math
|E(T)\setminus E(H)|=d_H,
```

which proves MT.1. `square`

The completion need not be unique. Small exact enumeration finds spanning convex-thrackle trees with two distinct maximal completion chords and two-component forests with multiple completion pairs. No uniqueness is used below.

---

## 2. `d_H=1`: the added chord is necessarily a cycle edge

DC says `H` is a connected spanning tree when `d_H=1`.

Let

```math
E(T)\setminus E(H)=\{g\}.
```

If `g` were a pendant edge of the maximal odd-cycle-plus-leaves graph `T`, then deleting `g` would isolate its leaf endpoint. But

```math
H=T-g
```

is connected and spanning. Contradiction.

Therefore `g` lies on the unique odd cycle `C_T`.

Deleting one cycle edge from a connected unicyclic graph gives a spanning tree, exactly as required. Every pendant edge of `T` is already in `H` and hence is an actual diameter edge.

Thus the `d_H=1` full diameter graph is **exactly one cycle chord short** of a maximal odd-cycle-plus-leaves thrackle.

---

## 3. `d_H=2`: both added chords connect the two tree components

DC/D2 give

```math
H=T_A\sqcup T_B,
```

where `T_A,T_B` are two nontrivial trees covering all shell vertices.

Let

```math
E(T)\setminus E(H)=\{g_1,g_2\}.
```

Because `T` is connected, at least one added edge joins `T_A` to `T_B`.

Suppose only one added edge, say `g_1`, joins the two components. Then `g_2` lies inside one component, say `T_A`. Adding `g_2` to the tree `T_A` creates a cycle entirely in `A`. Since `g_1` is then the only connection to the nontrivial tree `T_B`, it is a bridge and the unique cycle of the final unicyclic graph `T` lies wholly in `A`.

But the maximal-convex-thrackle classification says every vertex outside the unique odd cycle is a degree-one leaf attached **directly** to a cycle vertex. The retained nontrivial B-tree contains at least one edge with both endpoints outside the A-cycle, impossible.

Therefore both `g_1` and `g_2` join `T_A` to `T_B`.

Their union with one path in `T_A` and one path in `T_B` forms the unique odd cycle of `T`; hence both added edges lie on that cycle. Every edge outside that cycle is a retained pendant diameter edge from `H`.

This proves the added-edge assertion for `d_H=2`. `square`

---

## 4. Four-block localization of the two `d_H=2` defect chords

D2 writes the two tree bipartitions as four nonempty cyclic blocks

```math
A_0\mid B_0\mid A_1\mid B_1.
\tag{4.1}
```

Take any chord

```math
g=uv,
\qquad u\in A_s,\quad v\in B_t,
```

which can be added to `H` while preserving the convex-thrackle property.

It must meet every A-edge and every B-edge. The same corner argument used in EU now applies without any KKT hypothesis. For example, if

```math
u\in A_0,\qquad v\in B_0,
```

then every A0 vertex other than `u` is incident to an A0--A1 tree edge that must cross `uv`; the cyclic endpoint criterion forces all such A0 vertices to lie on one side of `u` inside their block. Hence `u` is the A0 block endpoint at the opposite transition. The symmetric B argument makes `v` the corresponding B0 corner.

Thus each addable cross-component chord is one of the finitely many opposite-corner chords determined by the four blocks.

In particular both `g_1,g_2` in a maximal completion are opposite-corner chords. They must also meet one another because `T` is a thrackle.

So the `d_H=2` phase is not merely two arbitrary diameter trees: it is obtained from a maximal odd-cycle-plus-leaves convex thrackle by shortening/removing a pair of compatible four-block corner chords.

---

## 5. Relation to a `d_H=1` KKT endpoint

Let `H` be the spanning tree and let

```math
e\in E(H)
```

be a zeroed nonleaf full-tree edge at a KKT endpoint. EU gives

```math
H-e=T_A\sqcup T_B
```

with four alternating bipartition blocks, and proves that `e` is an opposite-corner chord.

Fix any maximal completion

```math
T=H+g.
```

Section 2 shows `g` lies on the unique odd cycle of `T`.

We claim `g` must cross the `A|B` cut of `H-e`. If it were internal to, say, `A`, then `T_A+g` would contain the unique cycle of `T`, while the nontrivial B-tree would attach to it only through the retained full-tree edge `e`. This again leaves adjacent off-cycle vertices, impossible in a maximal odd-cycle-plus-leaves thrackle.

Hence `g` joins `A` to `B`. The four-block corner argument from Section 4 applies, so `g` is also an opposite-corner chord for the EU cut.

Therefore every zeroed nonleaf endpoint edge `e` sits in a four-block presentation with:

- one actual length-`D` corner chord `e` whose KKT coefficient is zero at the selected endpoint;
- one subdiameter maximal-completion corner chord `g` with
  
  ```math
  |g|<D.
  ```


The two chords together lie on the odd cycle of the maximal completion.

---

## 6. Every completion defect is genuinely subdiametral

By definition `H` is the **full actual diameter graph** on the cyclic source. Thus if

```math
g\notin H,
```

then

```math
\boxed{|g|<D.}
\tag{6.1}
```

No quantitative gap is claimed yet. The added chords may be arbitrarily close to diameter.

This is precisely the remaining geometric defect relative to the exact `d_H=0` Reinhardt phase.

---

## 7. Unified defective-Reinhardt picture

Let `C_T` have odd length `nu`. Every cyclic phase admits a maximal completion whose geometry is:

1. `nu-d_H` cycle edges have length exactly `D`;
2. `d_H` cycle edges have length strictly below `D`;
3. all `q-nu` pendant edges have length exactly `D`;
4. the shell itself is equilateral with side length one;
5. RP gives
   
   ```math
   q=\pi D-\frac\pi{24D}+O(D^{-2});
   ```

6. UFB gives
   
   ```math
   F=\operatorname{conv}A;
   ```

7. SL says `F` is a local diameter minimum among convex equilateral `q`-gons.

For `d_H=0`, RE upgrades the zero-defect case to exact Reinhardt equality.

The remaining tree phases are therefore literal one- and two-chord defects from the same maximal-thrackle combinatorics.

---

## 8. Literature regression: power-of-two shells fit the one-defect philosophy

This normal form is consistent with, rather than contradicted by, the small-polygon literature.

Mossinghoff's and later Bingane--Audet power-of-two constructions show that convex equilateral small polygons can approach the formal Reinhardt perimeter bound extremely closely while carrying connected or highly structured diameter skeletons. In particular shell-only near-equality is not enough to force the zero-defect Reinhardt phase.

The useful Target C distinction is now exact: there are at most two missing edges from a **maximal convex thrackle**, not merely an asymptotically small perimeter defect.

Any closing theorem should quantify the Euclidean shortening of those one or two missing cycle chords, or show that local/global source optimality cannot coexist with such a defective maximal-thrackle completion.

---

## 9. Regression audit

### Completion uniqueness

False and not used. Small convex-thrackle enumeration gives trees with two completion chords and two-component forests with several completion pairs.

### Added pendant edge in `d_H=1`

Impossible because deleting it would disconnect the spanning tree.

### One internal plus one cross edge in `d_H=2`

Impossible because the nontrivial other component would remain as a multi-vertex off-cycle branch, forbidden by maximal-thrackle structure.

### Power-of-two near-extremal shell

Allowed. MT does not claim one short cycle chord produces a large perimeter loss.

### `d_H=0`

No added edge exists; MT reduces to the exact maximal-thrackle topology already used by RE.

---

## 10. Next theorem

The most direct unified geometric target is now:

### MT-gap

For a convex equilateral cyclic shell with a maximal-thrackle completion `T`, prove that if exactly `k<=2` cycle edges of `T` are subdiametral, then either

```math
\max_{g\in T\setminus H}(D-|g|)
```

has a quantitative lower bound incompatible with RP/local optimality, or the shell is forced into a finite near-Reinhardt normal form that can be checked against C56-G and the dense interior population.

A second route is to reconstruct Reinhardt's semicircle proof with the `d_H` short cycle chords retained as explicit defect terms. Since there are only one or two, the global perimeter deficit may become an exact function of their chord deficits rather than an uncontrolled stability remainder.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

The greedy extension is elementary. The only external combinatorial input is the standard classification of edge-maximal convex thrackles.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Full cyclic diameter graph H is a convex thrackle with
  |H|=q-d_H, d_H in {0,1,2}.
Greedily extend H on the same q convex vertices to an edge-maximal convex thrackle T.
Standard structure: T is one odd cycle plus direct degree-1 leaves and has q edges.
Hence exactly d_H chords are added.

Added chords all lie on the odd cycle:
- d_H=1: H is connected spanning tree, so the one added edge cannot be pendant.
- d_H=2: H is two nontrivial trees. If only one added edge crossed components and the
  other created a cycle internally, the other nontrivial tree would be a multi-vertex
  off-cycle branch, impossible in maximal-thrackle structure. Thus both added edges
  cross the two components and both lie on the unique odd cycle.

Therefore every pendant edge and every retained cycle edge is an actual length-D chord;
only the d_H added cycle edges are strictly shorter than D.
D2/EU further localize added cross-component chords to opposite four-block corners.

Unified endpoint: maximal odd-cycle-plus-leaves thrackle with 0,1,or2 shortened cycle
chords. d_H=0 is exact Reinhardt (RE). Next: redo Reinhardt's semicircle proof with the
one/two short cycle chords retained as explicit defect terms.
```
