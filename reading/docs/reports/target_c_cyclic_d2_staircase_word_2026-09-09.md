> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_staircase_word_2026-09-09.md) · source SHA-256 `dc9f2709a3e7a24c61feb95baff8ed449a39cc0616fc235d65e8475c6c515d13`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-4185F5E81DD9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: each exact triangle-chain body is a monotone staircase word

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact combinatorial encoding downstream of D2S/D2R  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** D2 four-block normal form; D2S exact direction saturation; D2R exact exhaustion of internal block sides  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

D2R shows that every internal shell side in either color block is certified by exactly one pair of consecutive diameter directions sharing the opposite endpoint. This converts each of the two diameter trees into an exact monotone lattice staircase.

### Theorem SW — staircase-word normal form

Let `T` be one of the two diameter-tree components in the cyclic `d_H=2` phase. Let its bipartition classes be the two opposite shell blocks

```math
U=(u_1,\ldots,u_m),
\qquad
V=(v_1,\ldots,v_n),
```

listed in suitable boundary orientations. Then the `m+n-1` diameter edges of `T`, in their projective direction order, can be written uniquely as

```math
e_0,e_1,\ldots,e_{m+n-2},
\qquad
e_t=u_{i_t}v_{j_t},
```

so that, after possibly reversing either block order and reversing the whole direction list,

```math
\boxed{(i_0,j_0)=(1,1),\qquad(i_{m+n-2},j_{m+n-2})=(m,n),}
\tag{SW.1}
```

and every step is exactly one of

```math
\boxed{(i_{t+1},j_{t+1})-(i_t,j_t)\in\{(1,0),(0,1)\}.}
\tag{SW.2}
```

Thus `T` is encoded by a binary word

```math
w(T)\in\{U,V\}^{m+n-2}
```

with exactly `m-1` `U`-steps and `n-1` `V`-steps.

Geometrically:

- a `U`-step
  
  ```math
  u_i v_j\to u_{i+1}v_j
  ```

  certifies the unit shell side `u_i u_{i+1}` with common diameter center `v_j`;
- a `V`-step
  
  ```math
  u_i v_j\to u_i v_{j+1}
  ```

  certifies the unit shell side `v_j v_{j+1}` with common diameter center `u_i`.

Conversely the ordered edge set of `T` is exactly the set of lattice vertices visited by this staircase word.

This removes the remaining abstract caterpillar freedom: each D2R body is a discrete staircase of fixed `D,D,1` triangles.

---

## 1. Consecutive direction states change exactly one block coordinate

D2S says every consecutive pair of diameter directions inside `T` shares one endpoint. D2R says the two nonshared endpoints are consecutive shell vertices in one color block.

Hence if

```math
e_t=u_i v_j,
```

then

```math
e_{t+1}\in
\{u_{i-1}v_j,u_{i+1}v_j,u_i v_{j-1},u_i v_{j+1}\}
```

whenever the displayed indices exist.

Thus the projective direction list defines a walk in the Cartesian grid

```math
P_m\square P_n
```

whose vertices are endpoint pairs `(i,j)` and whose steps change exactly one coordinate by one.

---

## 2. Every coordinate gap is crossed exactly once

There are exactly

```math
(m-1)+(n-1)=m+n-2
```

internal shell sides in the two blocks `U,V`.

D2R proves that the `m+n-2` consecutive within-tree direction transitions certify these internal sides bijectively. Therefore:

- for every `1<=i<m`, the shell side `u_i u_{i+1}` occurs in exactly one transition;
- for every `1<=j<n`, the shell side `v_j v_{j+1}` occurs in exactly one transition.

Equivalently, in the coordinate walk:

```math
\boxed{
\text{each edge }\{i,i+1\}\text{ of }P_m\text{ is crossed exactly once by the }i\text{-coordinate,}
}
\tag{2.1}
```

and similarly every edge of `P_n` is crossed exactly once by the `j`-coordinate.

---

## 3. A walk on a path using every path edge once is monotone

Delete from the full direction sequence all steps on which `i_t` does not change. The remaining `i`-sequence is a walk on the path graph

```math
1-2-\cdots-m
```

which traverses every edge exactly once by (2.1).

A connected graph trail using every edge of a path exactly once is its unique Euler trail: it starts at one endpoint, ends at the other, and traverses the path monotonically. Hence, after perhaps reversing the labeling of `U`,

```math
1\to2\to\cdots\to m.
```

The same argument applies independently to the `j`-coordinate. After perhaps reversing the labeling of `V`, its changing subsequence is

```math
1\to2\to\cdots\to n.
```

Consequently every full step is either `(1,0)` or `(0,1)`, the first state is `(1,1)`, and the last is `(m,n)`. This proves SW.1-SW.2.

No separate monotonicity theorem is needed at this stage; D2R's exact side exhaustion alone forces it.

---

## 4. Edge count and tree reconstruction

A staircase from `(1,1)` to `(m,n)` has

```math
(m-1)+(n-1)=m+n-2
```

steps and therefore visits exactly

```math
m+n-1
```

lattice states.

Those states are exactly the projectively ordered diameter edges of `T`, whose tree edge count is also

```math
|E(T)|=m+n-1.
```

Thus no extra diameter edge is omitted from the staircase and no lattice state is repeated.

The graph `T` can be reconstructed directly from the word: every visited lattice state `(i,j)` represents the diameter edge `u_i v_j`.

Consecutive equal letters in the word are star runs about one endpoint; a change of letter is exactly a center switch and therefore carries D2R's rigid isosceles-trapezoid metric.

---

## 5. Fixed metric recursion

Every staircase step glues one exact `D,D,1` triangle.

For a `U`-step

```math
(i,j)\to(i+1,j),
```

we have

```math
|u_i-v_j|=|u_{i+1}-v_j|=D,
\qquad
|u_i-u_{i+1}|=1.
```

For a `V`-step the analogous statement holds with `U,V` exchanged.

If two consecutive staircase letters differ, the corresponding four vertices form the exact D2R center-switch trapezoid with bases

```math
D,
\qquad D-1/D,
```

and unit legs.

Therefore, once the first diameter edge and the side of the shell on which each new unit vertex lies are fixed, the entire Euclidean body is recursively determined by the binary word.

The global convexity/diameter condition removes the wrong reflection at every center switch exactly as in D2R.

---

## 6. Endpoint/corner meaning

The first staircase state `u_1v_1` and last state `u_mv_n` are the two extreme projective diameter directions of this tree component.

Because D2S gives exactly two cross-tree direction switches globally, the two omitted completion states of the full `d_H=2` shell sit between the extreme states of the A- and B-staircases.

Thus the complete D2 geometry is now:

```text
A staircase word w_A between opposite blocks A0,A1;
B staircase word w_B between opposite blocks B0,B1;
four unit shell transition sides joining the four block corners;
two cross-tree projective direction gaps carrying all diameter defect.
```

Every internal shell side and every selected diameter edge is fixed by the two staircase words. The only non-Reinhardt metric information is concentrated at the four corners/two cross-tree gaps.

---

## 7. Binding regression

SSR shows that this selected staircase/four-transition architecture cannot itself be contradictory: a regular exact Reinhardt shell at a vertex of its KKT stress polygon realizes the special staircase pair

```math
K_2\sqcup P_{q-2}
```

with positive selected KKT stress and maximal-rank PSD matrix, while the two omitted rows remain actual diameter equalities.

Therefore SW is useful precisely because it gives finite coordinates in which to measure the distinction between

- the SSR boundary point, where the two omitted completion chords have length exactly `D`, and
- a true D2 source, where those completion states are genuinely missing from the diameter graph.

---

## 8. Next theorem

For each pair of staircase words `w_A,w_B`, derive the two omitted completion chord lengths as functions of the four corner transition geometry.

The desired metric statement is:

> In any convex unit shell obtained by joining two exact D2 staircases with four unit transition sides, at least one of the two canonical completion chords has length at least `D`, with equality only on the `d_H=0` Reinhardt boundary.

If true, this closes the complete cyclic `d_H=2` phase without using stress coefficients or the quadratic rattler population.

The theorem is sharp against SSR: equality must be allowed there because both omitted selected rows are actual diameter chords.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| direction edge sequence is a nearest-neighbor grid walk | proved | D2S shared endpoints + D2R shell adjacency |
| every U/V coordinate gap used exactly once | proved | D2R bijection with all internal block shell sides |
| coordinate motion is monotone | proved | Euler trail of a path graph |
| exact binary staircase word | proved | sections 1-3 |
| word reconstructs all selected diameter edges | proved | exact tree edge count |
| every step is a `D,D,1` triangle | proved | D2R |
| center switch has fixed trapezoid metric | proved | D2R |
| completion-chord inequality | open | next metric target |
| Level I | still open | true D2 corner compatibility not yet excluded |
