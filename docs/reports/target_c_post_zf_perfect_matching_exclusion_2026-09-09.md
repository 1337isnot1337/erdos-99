<!-- theorem-state: {"artifact_id":"ART-2F84A6528AE3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF perfect-matching diameter branch is impossible

**Date:** 2026-09-09  
**Repository base:** `faa60082283fb0c3c64b59c9817219083d46962e`  
**Run type:** exact branch closure  
**Target:** Target C C-II after ZF  
**Depends on:** MB matching-branch collapse, C77 train-track pseudolines, ZS `h>=ceil(D)`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The perfect-matching branch of the full actual diameter graph is impossible once the post-ZF terminal ledger is combined with the existing C77 rhombic train-track theorem.

### Theorem MC — perfect matching excluded

Let a post-ZF C-II survivor have full actual diameter graph `H` on loaded terminal set `B_+`, and suppose `H` is a perfect matching. Then

\[
D\le2.
\]

Consequently no sufficiently large triangle-free global minimizer in the audited post-ZF branch can have a perfect-matching diameter graph.

The conclusion is independent of the contact-isolated external population. The external rattlers left alive by MB do not rescue the branch.

---

## 1. MB collapses the positive core to a convex pure rhombic disk

Let

- `q=|B_+|`;
- `h=|E(H)|`;
- `T` be the number of rhombic train tracks in the positive contact core.

If `H` is a perfect matching, MB proves

\[
h=\frac q2,
\qquad
x_B=f=g_F=s_Z=0.
\tag{MC.1}
\]

Hence

\[
b=q,
\qquad Q=0,
\tag{MC.2}
\]

and the outer contact-face boundary walk is exactly the convex force-hull cycle. Every hull side is a unit contact edge, every bounded contact face is a strict unit rhombus, and the positive contact core is a simply connected strict-rhombic disk.

DT then gives

\[
T=\frac{b+Q}{2}+2f=\frac q2.
\tag{MC.3}
\]

Therefore

\[
\boxed{T=h=q/2.}
\tag{MC.4}
\]

All statements in this section concern only the fixed positive core. Contact-isolated source points outside the force hull may still exist, but they do not alter its rhombic disk or train tracks.

---

## 2. The two ends of one train are an opposite parallel pair of boundary edges

C77 defines a train track by continuing through opposite edges of successive strict rhombi. In a pure rhombic disk every maximal track is a finite simple path with exactly two ends, both on the outer boundary.

All entry and exit edges of one train are parallel, so its two boundary-end edges have one common unoriented direction

\[
[u_T]\in\mathbb{RP}^1.
\tag{MC.5}
\]

Because the outer boundary is a strict convex polygon, an oriented boundary-edge direction occurs at most once while traversing the boundary counterclockwise. Therefore an unoriented direction can occur on at most two boundary edges: once in orientation `u` and once in orientation `-u`.

Each train already consumes two parallel boundary edges. Hence:

1. no two distinct train tracks can have the same unoriented direction;
2. each train's two ends are the unique two boundary edges in that parallel class;
3. those two boundary edges occur with opposite orientations.

Since every boundary edge of a pure rhombic disk is the end of exactly one train, the `2T` boundary edges split into exactly `T` distinct opposite parallel pairs.

---

## 3. Convex cyclic order makes every pair of trains alternate

Write the oriented edge vectors of the convex outer polygon in increasing direction order. After rotating the angular origin, the `T` distinct unoriented train directions can be represented by

\[
0\le\theta_1<\theta_2<\cdots<\theta_T<\pi.
\]

The full oriented boundary edge directions are then necessarily

\[
\theta_1,\ldots,\theta_T,
\theta_1+\pi,\ldots,\theta_T+\pi.
\tag{MC.6}
\]

Thus the two boundary ends of train `i` occur at cyclic edge positions

\[
i,\qquad T+i.
\tag{MC.7}
\]

For two trains `i<j`, their four boundary ends occur in the order

\[
i<j<T+i<T+j.
\tag{MC.8}
\]

So the endpoint pairs alternate around the boundary circle.

This also incidentally proves that the convex outer polygon is centrally symmetric, but central symmetry is not needed for the contradiction.

---

## 4. Alternating train ends force a crossing

Represent each C77 train by the standard embedded dual arc through the midpoints of the successive opposite edges/rhombi, joining the midpoints of its two terminal boundary edges.

C77 proves each train arc is simple and two distinct train arcs cross at most once.

Take two trains. Their endpoint pairs alternate on the boundary by (MC.8). Two disjoint simple arcs in a topological disk cannot connect alternating pairs of boundary points: adjoining one arc to either boundary interval between its endpoints gives a Jordan curve separating the other pair. Therefore the second arc must cross the first.

Hence **every pair of distinct trains crosses**.

A crossing of two rhombic train tracks occurs in exactly one common rhombus by C77. Thus the train-intersection graph `Gamma_R` satisfies

\[
\boxed{\Gamma_R=K_T.}
\tag{MC.9}
\]

---

## 5. C77 triangle-freeness gives the contradiction

C77 proves that the train-intersection graph of a triangle-free unit-contact rhombic complex is triangle-free. At any train crossing the acute projective angle is strictly greater than `pi/3`; three projective directions cannot be pairwise separated by more than `pi/3`.

But (MC.9) says the graph is complete. Therefore

\[
\boxed{T\le2.}
\tag{MC.10}
\]

On the other hand ZS gives for every post-ZF survivor

\[
h\ge\delta\ge\lceil D\rceil.
\tag{MC.11}
\]

Using `T=h` from MC.4,

\[
T\ge\lceil D\rceil.
\]

Together with MC.10,

\[
\boxed{D\le2.}
\]

This proves Theorem MC. `square`

---

## 6. Why external rattlers do not matter

MB originally reduced the perfect-matching branch to a pure rhombic positive core plus a required macroscopic external rattler shell. That population issue is now irrelevant for this branch.

The contradiction uses only:

1. the positive core topology forced by the exact post-ZF ledger;
2. convexity of its outer force-hull cycle;
3. C77 train pseudolines and triangle-freeness;
4. the actual diameter-edge count `h>=ceil(D)`.

No statement about the location, density, KKT visibility, or removability of the external rattlers is used.

Thus MC strictly supersedes MB's matching-shell endpoint: the shell never arises in a sufficiently large survivor because its required core is itself impossible.

---

## 7. Relation to the earlier matching regression

MB records an exact one-parameter family of convex equilateral hexagons whose diameter graph is a perfect matching but which are not centrally symmetric.

There is no contradiction with MC. Those polygons were deliberately only regressions against the implication

```text
perfect-matching diameter graph -> centrally symmetric convex polygon.
```

MC uses the much stronger post-ZF conclusion that the contact core is a **pure rhombic disk**. The train decomposition then pairs all outer boundary edges by rhombic opposite-edge classes. It is this extra contact topology, not the diameter matching alone, that forces the alternating boundary pairing and complete train-intersection graph.

The regression therefore remains useful and should be retained.

---

## 8. Exact frontier change

The post-ZF diameter graph has no isolated terminal vertices. Therefore

\[
\sum_{b\in B_+}(\deg_H(b)-1)=2h-q\ge0.
\]

DB/ZT identify this exactly as

\[
2h-q=x_B+Q+2s_Z.
\tag{MC.12}
\]

Equality `2h-q=0` is equivalent to every diameter-terminal degree being exactly one, hence to `H` being a perfect matching.

MC excludes equality for every sufficiently large survivor. Thus

\[
\boxed{
2h-q=x_B+Q+2s_Z\ge1
}
\tag{MC.13}
\]

for every sufficiently large post-ZF survivor.

This is only a one-unit strictness result by itself. The next quantitative target is stability: prove that `2h-q=o(D)` is impossible, or force a definite linear lower bound on the branching currency.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| MB pure-rhombic core under perfect matching | report-level proved input | exact post-ZF terminal partition |
| each train has two parallel boundary ends | canonical C77 input | fixed opposite-edge direction |
| distinct trains have distinct directions | proved here | strict convex boundary cannot repeat an oriented edge direction |
| train endpoints occur antipodally in edge order | proved here | convex sorting of paired `u,-u` directions |
| every two trains cross | proved here | alternating-boundary-endpoint Jordan argument |
| train graph is `K_T` | proved here | C77 crossing uniqueness |
| `T<=2` | proved here | C77 triangle-free intersection graph |
| perfect-matching post-ZF branch excluded for `D>2` | proved here | `T=h>=ceil(D)` |
| near-perfect matching excluded | not proved | quantitative stability remains open |
| Level I | still open | nonmatching diameter graphs remain |

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

If MB/ZE/ZT/ZF are promoted, MC should replace the perfect-matching external-shell subcase entirely. The matching shell is no longer a live branch.

---

## 11. Next theorem

The natural stability problem is now exact:

> **Near-matching train stability.** Show that a post-ZF survivor with
> \[
> 2h-q=x_B+Q+2s_Z=o(D)
> \]
> inherits enough of the alternating train-end structure of MC to force either a train triangle or a linear number of contact/face defects.

Since the left side is literally the total diameter degree excess above one, this is equivalent to saying that all but `o(D)` loaded terminals are diameter leaves.

A successful stability theorem would close the low-branching side of DB's exact split and leave only a linear contact/topology-defect branch.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

MC closes the exact perfect-matching diameter branch.

MB gives under H perfect matching:
    x_B=f=g_F=s_Z=0,
    b=q,
    positive core = simply connected strict-rhombic disk,
    T=h=q/2.

In that disk every train has exactly two parallel boundary-edge ends.
The outer boundary is strict convex, so each train direction occurs in exactly
one opposite pair. Ordering boundary edge directions gives endpoints
    i and T+i.
Thus every two train endpoint pairs alternate around the boundary.
C77 train arcs are simple pseudolines, so alternating pairs must cross.
Hence the train-intersection graph is K_T.
C77 says that graph is triangle-free, so T<=2.
But ZS gives T=h>=ceil(D).
Therefore D<=2: no sufficiently large post-ZF survivor has H a perfect matching.

Consequently for large survivors
    2h-q = x_B+Q+2s_Z >=1.
Next: upgrade this one-unit strictness to Omega(D) via near-matching train stability.
```
