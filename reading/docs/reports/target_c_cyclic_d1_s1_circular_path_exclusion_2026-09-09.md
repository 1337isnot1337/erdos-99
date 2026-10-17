> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_s1_circular_path_exclusion_2026-09-09.md) · source SHA-256 `330f2f2aff96d0027c0d378261742118dd3e6f0fa679f6a313e93f84d644dae7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E38D9638857A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=1` S1: correct ordinary-gap saturation and two-defect shell normal form

**Date:** 2026-09-09  
**Repository branch:** `research/cyclic-d1-s1-path-exclusion-2026-09-09`  
**Run type:** hostile correction + exact structural refinement  
**Target:** primitive cyclic `d_H=1, s_Z=1`, AD/S1 branch  
**Depends on:** AC canonical antipodal completion on PR #118; DG doubled gap on PR #119; cyclic `d_H=1` classification  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

## Correction

The first version of this report made the invalid inference

```text
consecutive direction-list edges share an endpoint
=> the direction list is an Euler trail
=> the diameter tree is a path.
```

This is false. A three-edge star `za,zb,zc` is the binding counterexample: both consecutive pairs share `z`, but the three edges cannot be traversed as a trail in that order. The same inference appears in the current CP2 report on PR #141 and must not be used without an additional argument excluding star runs.

The claimed S1 phase exclusion is therefore withdrawn.

The ordinary-gap information still gives a sharp exact theorem.

### Theorem S1S — complete ordinary-gap saturation

Let `F` be a cyclic S1 survivor. Write the `q-1` actual diameter edges in the linear projective order obtained by deleting the unique short antipodal state `g` from AC's maximal antipodal graph:

$$
e_0,e_1,\ldots,e_{q-2}.
$$

Then, for all sufficiently large `D`:

1. every consecutive pair `e_j,e_{j+1}` shares exactly one terminal;
2. for every terminal `v`, all diameter edges incident to `v` occur in one contiguous run in this projective order;
3. every one of the `q-2` ordinary H-H transitions certifies a distinct unit shell side joining the two nonshared diameter endpoints;
4. these `q-2` certified sides are exactly all shell sides except the two sides adjacent, in the strict Minkowski merge, to the unique short antipodal state;
5. AC's maximal antipodal graph remains one odd cycle plus direct leaves, and `H=A(F)-g` is the corresponding opened-cycle caterpillar; the only metric departure from local Reinhardt side/antipode equality is concentrated at the two defect-adjacent shell sides.

Thus S1 is not yet excluded, but it is an exact **two-shell-side defect** of the Reinhardt side/antipode pattern.

---

## 1. One projective block of actual diameter states

AC gives

$$
A(F)=H\cup\{g\},
$$

where `A(F)` is the complete vertex-vertex antipodal graph, `H` is the connected spanning diameter tree with

$$
|E(H)|=q-1,
$$

and `g` is the unique short antipodal edge.

S1 has no parallel shell sides. In one projective half-boundary of `K=F-F`, deleting the unique short K-vertex state leaves all actual diameter states in one linear block

$$
e_0,e_1,\ldots,e_{q-2}.
\tag{1.1}

Every K-edge between two consecutive states in this block has length one and both endpoints lie on the radius-`D` circle. Hence

\[
\boxed{
\angle_{proj}(e_j,e_{j+1})
=\delta:=2\arcsin\frac1{2D}.
}
\tag{1.2}

---

## 2. DG forces every ordinary transition to share a terminal

DG proves that two vertex-disjoint actual diameter edges satisfy

\[
\angle_{proj}(e,f)\ge2\delta.
$$

Equation (1.2) is smaller. Therefore

$$
\boxed{e_j\cap e_{j+1}\ne\varnothing}
\tag{2.1}

for every `0<=j<=q-3`.

The two edges are distinct in a simple graph and therefore share exactly one endpoint.

There are exactly

\[
q-2
\tag{2.2}

such ordinary transitions.

This is the point at which the withdrawn proof incorrectly called the list an Euler trail. No such claim is needed below.

---

## 3. Exact adjacency-capacity count forces one direction run at every terminal

For a terminal `v` of diameter degree `d_v`, its `d_v` incident edges can account for at most

\[
d_v-1
\tag{3.1}

consecutive pairs in a linear list of distinct edges. Equality holds if and only if all `d_v` incident edges occur as one contiguous block in that list.

Because `H` is spanning, every terminal has `d_v>=1`. Since `H` is a tree on `q` vertices,

\[
\sum_v d_v=2(q-1).
$$

Therefore

$$
\boxed{
\sum_v(d_v-1)=2(q-1)-q=q-2.
}
\tag{3.2}

Every one of the `q-2` consecutive pairs in (1.1) has a unique shared terminal by Section 2. Thus the total number of realized shared-terminal adjacencies is exactly `q-2`, equal to the sum of all upper capacities (3.2).

Consequently equality holds termwise in the capacity accounting: every terminal realizes all `d_v-1` possible internal adjacencies. Hence

\[
\boxed{
\text{the diameter edges incident to every terminal form one contiguous projective run.}
}
\tag{3.3}

This permits arbitrary star runs. It is exactly the correction missing from the false path argument.

---

## 4. Every ordinary transition certifies a unit shell side

Take two consecutive actual diameter states that share terminal `z`:

\[
zy,
\qquad
zw.
$$

The corresponding two difference-body vertices are oriented diameter vectors with one support endpoint fixed at `z`. The K-boundary step between them changes only the opposite support vertex and is one of the strict unit Minkowski edges of S1. Thus that step is, up to sign,

$$
y-w.
$$

Its K-edge length is one, so

$$
\boxed{|y-w|=1.}
\tag{4.1}

Because this support change is one step in the strict merge of the side directions of `F` and `-F`, `yw` is an actual shell side of `F`.

Distinct H-H transitions are distinct K-boundary edges and therefore certify distinct primal shell sides.

There are exactly `q-2` such transitions. Hence they certify exactly `q-2` distinct shell sides.

---

## 5. Only two shell sides remain uncertified

The shell has exactly `q` unit sides. S1's projective half-boundary of `K` has exactly `q` unit Minkowski edges.

The `q-2` H-H edges of that half-boundary are the certified sides from Section 4. The only two remaining K-edges are the edges immediately before and after the unique short antipodal vertex `g`.

AC's endpoint-switch theorem writes the local antipodal states, after orientation, as

\[
(u_-,v),\quad (u,v)=g,\quad (u,v_+),
\tag{5.1}

so the two defect-adjacent shell sides are

\[
u_-u,
\qquad
vv_+.
\tag{5.2}

Every other shell side `ab` has a unique opposite diameter center `z` satisfying

\[
\boxed{|z-a|=|z-b|=D.}
\tag{5.3}

Thus the S1 shell is a local side/antipode equality polygon at all but two shell sides.

---

## 6. Exact maximal-thrackle structure remains

AC proves that `A(F)` is a maximal convex thrackle: one odd cycle with every other vertex a direct leaf. The short edge `g` lies on the unique odd cycle. Removing it opens that cycle into a path but retains all direct leaves.

Therefore `H` is an opened-cycle caterpillar, not necessarily a path.

Section 3 adds a transverse ordering property absent from the earlier AC statement: every star of this caterpillar occupies one contiguous interval in projective diameter-direction order. Section 4 identifies the unit shell path induced by each such star run.

A run

\[
zy_0,zy_1,\ldots,zy_r
$$

forces

$$
|y_j-y_{j+1}|=1,
\qquad
|z-y_j|=D.
$$

Hence its opposite shell vertices lie on one radius-`D` circle about `z` with exact angular step `delta`.

A change of shared center between two adjacent runs has the same exact `D,D,1` center-switch trapezoid geometry derived in D2R.

So the S1 shell is a finite concatenation of exact star-run circular arcs and exact center-switch trapezoids, with only two shell sides adjacent to `g` outside this pattern.

---

## 7. Why this is still useful

The corrected theorem reduces S1 to the same discrete objects that made the D2 staircase route effective:

```text
one opened odd-cycle caterpillar H;
all H-stars contiguous in projective direction order;
q-2 exact ordinary direction transitions;
q-2 certified unit shell sides;
only two defect-adjacent shell sides;
one canonical short antipodal cycle edge g;
all metric non-Reinhardt behavior localized at g and those two sides.
```

This is stronger than the raw sign-code description but does not falsely remove leaves.

The correct next target is a **star-run word** rather than a path theorem: encode successive projective transitions by the shared terminal. Every repeated label is a star run; every label switch is the exact D2R trapezoid. AC's opened odd-cycle-plus-leaves topology should sharply constrain which such words are compatible with the two defect-adjacent sides.

---

## 8. Audit impact on PR #141

The same logical issue occurs in the CP2 proof currently on PR #141:

```text
Every consecutive pair shares an endpoint. Since each edge appears once, this is a trail traversing every edge of the tree exactly once.
```

That implication is false in the presence of a star run. D2R explicitly retains star runs and center switches, so they cannot be excluded silently.

The downstream PS/S2 exclusions on #141 use the claimed circular-path geometry and therefore require re-audit. The independent P2 exclusion on #139 may remain valid if its separate CP path proof has an additional no-star argument; it must be checked rather than inherited automatically.

This report does not claim #141 is entirely false. It identifies the exact unsupported step and supplies the valid replacement conclusion.

---

## 9. Regression test

Take a three-edge star with direction order

$$
za,zb,zc.
$$

Both consecutive pairs share endpoint `z`, and all three edges form one contiguous star run. But there is no graph trail traversing the three edges in that order: after traversing `za` and `zb`, one is at `b`, not at `z` to traverse `zc`.

This example satisfies the combinatorial premise of the rejected inference and is the minimal regression that future proofs must pass.

---

## 10. Current status

What is proved:

$$
\boxed{
\begin{array}{l}
\text{all S1 ordinary diameter gaps equal }\delta;\\
\text{every ordinary adjacent pair shares one terminal;}\\
\text{every H-star is one contiguous direction run;}\\
\text{all but two shell sides have an exact common diameter center.}
\end{array}}
$$

What is not proved:

$$
\boxed{
H\text{ is a path, the shell is concyclic, or S1 is excluded.}
}
$$

The shortest next theorem is to classify the allowed sequence of star runs in the opened odd-cycle caterpillar. A valid proof must either show star runs collapse for a geometric reason or propagate their exact circular-arc/trapezoid geometry through the two defect sides.
