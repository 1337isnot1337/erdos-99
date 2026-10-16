<!-- theorem-state: {"artifact_id":"ART-CEC8A7C80E23","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: terminal-twist / full-span-prefix contradiction

**Date:** 2026-09-04  
**Repository base:** `89c17412` plus branch commits `c6cc7744`, `55efe3e9`  
**Run type:** candidate exact branch closure  
**Target:** canonical pure-rhombic C80-C88 chain-face survivor  
**Status:** proof candidate; requires promotion audit before canonical use  
**LEVEL I STATUS:** STILL OPEN globally

This report combines three exact facts:

1. the C80 diameter chain has the forced terminal twist proved on this branch;
2. C88 equality forces the full-span simple prefix edge `{0,D}`;
3. C87.4 requires every simple prefix edge in both physical hull-arc orientations.

The terminal twist makes one of those two full-span orientations equal to the original
chain diameter `za`, which has zero transverse coefficient and therefore cannot be the
required non-chain orientation. This is a contradiction.

If the boundary-arc identification in Section 3 survives audit, the entire **pure
simply connected strict-rhombic C80 chain-face survivor is empty**. This is a closure of
that canonical branch, not yet a Level I proof of Erdős #99 unless the upstream route
has already reduced every C-II survivor to this exact branch.

---

## 1. Inputs

Use the exact C80 chain

`z=x_0,x_1,...,x_D=a`,

with ordered chain trains

`P={tau_1,...,tau_D}`,

where `x_(j-1)x_j` belongs to `tau_j` and the `tau_j` are exactly the tracks
separating `z` from `a`.

C83 assigns every source vertex a prefix level

`k(v) in {0,...,D}`,

with `k(z)=0`, `k(a)=D`.

C87 splits the convex-hull boundary at `z,a` into two arcs `L,U`, each ordered from
`z` to `a`. Along each arc, `k` is nondecreasing.

For a non-chain active diameter with interval `(a,b]`:

- positive transverse orientation is physically `L_a U_b`;
- negative transverse orientation is physically `U_a L_b`.

C87.4 says every simple prefix edge `{a,b}` occurs in both orientations, with positive
relative-interior KKT flow in each.

C88 Section 1 gives `a_1=0`, `M_1=D`, and row 1 complete. Therefore

`{0,D} in E(G_P)`.

So C87.4 requires both

`L_0 U_D`

and

`U_0 L_D`

as actual **non-chain** active diameter pairs.

## 2. Forced terminal twist

The branch report `target_c_chain_monotone_rows_2026-09-04.md` proves that the first
and last chain edges are outer-boundary edges on opposite sides of the chain.

Reflect across the chain line if necessary. Then:

- `e_1=x_0x_1` has the outer face above the chain;
- `e_D=x_(D-1)x_D` has the outer face below the chain.

In particular both are terminal edges of their corresponding chain tracks:

- `e_1` is one terminal edge of `tau_1`;
- `e_D` is one terminal edge of `tau_D`.

The other side of each terminal edge is a rhombus, so the train enters the disk from
that edge.

## 3. The terminal edges lie on opposite `z`-to-`a` outer-boundary arcs

The pure rhombic disk has a simple outer boundary. Delete `z,a`; its boundary consists
of two simple boundary paths from `z` to `a`.

The two terminal chain edges cannot lie on the same one of these paths.

Indeed, traverse any fixed boundary path from `z` toward `a`. Its orientation is the
restriction of one orientation of the simple boundary cycle, so the disk interior is
locally on the same side (left or right) of every oriented edge of that path.

Both terminal chain edges are geometrically directed by this `z`-to-`a` traversal as
`+u`:

- if the path contains `e_1`, it traverses `z=x_0` to `x_1`;
- if it contains `e_D`, it traverses `x_(D-1)` to `a=x_D`.

But the forced terminal twist puts the disk interior below `e_1` and above `e_D`.
Thus a single consistently oriented boundary path cannot contain both.

Call the boundary path containing `e_1` the `U` path and the path containing `e_D`
the `L` path. The names may be swapped relative to an earlier convention; only their
roles matter. The convex-hull vertices are vertices of this simple outer boundary and
occur in the same cyclic order as on `conv A`. Therefore these two outer-boundary
paths induce exactly the two C87 convex-hull arcs, after the same possible `L/U`
renaming.

## 4. The `U` hull arc has no level-0 hull vertex except `z`

The train `tau_1` is a properly embedded crosscut of the rhombic disk. It separates
`z` from `a`.

Its terminal edge on the `U` boundary path is

`e_1=zx_1`.

The train itself exits the disk through the midpoint of this edge. Thus, when the
`U` boundary path is traversed from `z` to `a`, it crosses the crosscut `tau_1`
inside the very first boundary edge, between `z` and `x_1`.

A simple crosscut has only two boundary terminals. Since it separates `z,a`, its two
terminals lie on opposite `z`-to-`a` boundary paths. Therefore the `U` path does not
meet `tau_1` again.

Consequently every source vertex of the `U` path after `z` lies on the `a` side of
`tau_1`. By the C83 prefix convention it has

`k(v)>=1`.

Hence, among convex-hull vertices on this arc,

`U_0={z}`.

This statement does **not** identify a generic prefix level with a unique source
vertex. It uses the special fact that the first separator terminates in the first
boundary edge adjacent to `z` on this particular arc.

## 5. The `L` hull arc has no level-D hull vertex except `a`

Apply the same argument at the other end.

The last chain train `tau_D` terminates on the `L` path in

`e_D=x_(D-1)a`.

When the `L` path is traversed from `z` to `a`, this crosscut is met inside the final
boundary edge, between `x_(D-1)` and `a`. Since the other terminal of `tau_D` lies on
the opposite boundary path, the `L` path does not meet it earlier.

Every source vertex on the `L` path before `a` therefore lies on the `z` side of
`tau_D`, so

`k(v)<=D-1`.

Thus

`L_D={a}`.

Again this is endpoint localization from a terminal separator, not a general
one-vertex-per-prefix-level assumption.

## 6. C87.4 now forces the chain diameter to have nonzero transverse sign

C88 forces the simple full-span edge `{0,D}`.

C87.4 requires one actual non-chain diameter in the orientation

`U_0 L_D`.

Sections 4-5 give

`U_0={z}`,

`L_D={a}`.

Therefore that required active diameter pair is exactly

`za=h_0`.

But the C80 chain bar has

`r_(h_0)=D u`

and hence

`eta_(h_0)=r_(h_0) dot Ju=0`.

It is not a non-chain interval bar and cannot carry the strictly negative transverse
orientation required by C87.4. C83 explicitly proves `eta_h!=0` for every non-chain
active diameter meeting `P`.

This is a contradiction.

### Candidate theorem C97 — pure chain-face branch contradiction

There is no triangle-free lexicographically normalized global minimizer satisfying the
canonical pure simply connected strict-rhombic C80-C88 chain-face hypotheses.

Equivalently, the C87 paired staircase tree cannot coexist with the exact boundary
geometry forced by the C80 chain and C65 full contact visibility.

## 7. Why this does not repeat the rejected two-sheeted-lift shortcut

The rejected shortcut in the earlier branch audit falsely treated every prefix level
as one physical source vertex. The present proof does not do that.

Only two endpoint fibers are made singleton, and each singleton follows from an actual
terminal separator in the first/final boundary edge:

`U_0={z}` and `L_D={a}`.

All intermediate levels may still contain arbitrary multiplicity on either hull arc.
The contradiction uses only the forced C88 edge `{0,D}` and the C87 requirement that
this one edge occur in both orientations.

## 8. Adversarial checks still required before promotion

1. **Boundary-path / hull-arc order.** Verify in the exact pure-disk definition that
   every convex-hull vertex belongs to the simple contact outer boundary and that its
   cyclic order agrees with the hull order. This is standard for a straight-line plane
   disk containing all source vertices, but it should be cited canonically.
2. **Terminal midpoint separation.** Verify the C83 train curve convention treats a
   terminal contact edge as crossed at its midpoint, so the two endpoints of `e_1`
   have levels `0,1` and those of `e_D` have levels `D-1,D`. This is exactly how train
   coordinates are defined in C77/C80, but it should be checked against notation.
3. **Opposite-boundary-path claim.** The proof uses consistent boundary orientation,
   not a visual “upper/lower” assumption. A counterexample would require a single
   `z`-to-`a` boundary path to traverse two collinear `+u` edges with the disk interior
   on opposite sides, impossible for a simple oriented boundary.
4. **C88 full-span edge.** C88 row completeness with `a_1=0,M_1=D` must indeed put
   `{0,D}` in the simple graph, not only in a multiplicity count. Its displayed
   `B_1={m_1,...,D}` does so.
5. **C87 orientation quantifier.** C87.4 must require an actual non-chain physical
   diameter of each sign for `{0,D}`, not merely signed flow after combining bars.
   C87.4 states exactly that every simple edge is represented by at least two actual
   active diameter pairs, one with each sign of `eta`.

Until those checks are completed, this report remains a proof candidate and is not
promoted into the canonical route map.
