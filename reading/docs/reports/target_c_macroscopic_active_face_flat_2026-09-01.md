> Generated reading edition · [exact source](../../../docs/reports/target_c_macroscopic_active_face_flat_2026-09-01.md) · source SHA-256 `e4da27b42de8ce1a5b07c7588b01a6bec32e4d464e96581b3b168a17d240e6a9`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-C6B729314F23","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_macroscopic_active_face_flat_2026-09-01.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=d5f63685138795b61e2d944e53b8a47c4b14c005; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C C94: macroscopic exact active-face flat

**Date:** 2026-09-01  
**Repository base:** `591a395a` (main after C93 / PR #98)  
**Status:** LEVEL I STILL OPEN

C86 proves that every fixed-diameter critical velocity of the C65 lexicographically
normalized source integrates to an actual nearby realization preserving **every**
original unit contact and **every** original diameter pair exactly. C94 combines this
with the macroscopic train-neutral-space theorem from Target B Section 40 and C82's
chain-atom shell inequality.

The result is an exact geometric dichotomy. In the canonical pure-rhombic C80 chain
face, either

`T >= (3-o(1))D`,

or the local exact `(C,H)` realization face has a tangent cone containing a linear
subspace of dimension at least

`(2 Delta_2-1-o(1))D = (0.8137993642...-o(1))D`.

After fixing global rotation, every vector in this subspace is supported entirely on
**non-chain train angles**: the D exact C80 chain trains do not move relative to one
another.

Thus the remaining low-train-count chain branch is not a nearly rigid shell. It has a
macroscopic exact active-framework flat involving only the secondary train system.

---

## 1. Full train-neutral space

Work in the pure simply connected strict-rhombic train-angle quotient

`V = R^T / <1>`,

so `dim V=T-1`. For each active diameter pair `h in H`, let `g_h` be its train-angle
first-variation row, and define

`L = intersection_(h in H) ker g_h`.

Every train-angle first variation preserves all unit-contact lengths exactly to first
order. Hence `L` is precisely the train-angle subspace of fixed-diameter critical
velocities.

Target B Section 40 uses the positive KKT dependence among the rows and the diameter
edge bound `|H|<=q` to prove

`dim L >= T-|H| >= T-q`.

This is an exact finite-dimensional inequality.

## 2. C86 turns every vector of L into an exact active-face tangent

C65 chooses the hypothetical counterexample lexicographically: first minimize the
number of unit contacts, then among those minimizers minimize the number of diameter
pairs. C63/C65 imply all active contact and diameter rows are strong. C86 then proves
that for every critical velocity `v` there is a nearby realization

`p(t)=p+t v+O(t^2)`

such that, for all sufficiently small `t`,

`|p_i(t)-p_j(t)|=1` for every `ij in C`,

`|p_i(t)-p_j(t)|=D` for every `ij in H`,

and every inactive pair remains strict.

Therefore every `v in L` belongs to the tangent cone of the local exact active
equality realization set.

No smooth-manifold assertion is needed: C94 uses only the linear subspace `L` already
contained in that tangent cone.

## 3. The chain coordinates vanish after fixing rotation

C80 gives the exact straight contact chain

`z=x_0,x_1,...,x_D=a`

and D distinct parallel train tracks

`P={tau_1,...,tau_D}`,

one through each chain edge.

C86 applies equality in the Euclidean triangle inequality along every exact active-face
realization and proves that every critical train-angle velocity satisfies

`v_(tau_1)=...=v_(tau_D)`.

In the quotient `V=R^T/<1>`, subtract this common value. This gives a unique
representative of every `v in L` with

`v_tau=0` for all `tau in P`.

Consequently the natural restriction to the `T-D` non-chain train coordinates is
injective on `L`:

`L embeds in R^(T-D)`.

Thus the large active-face tangent flat furnished below is carried entirely by the
secondary train system; none of its dimension comes from bending the exact chain.

## 4. C82 converts shell counts into a sharper dimension bound

Put

`x=T/D`, `y=q/T`,

and

`A=1+Delta_2`, `Delta_2=pi/(2sqrt(3))`.

C82 proves

`x >= A/(1-y/2)+o(1)`.

For every bounded subsequential value of `x`, rearrangement gives

`x(1-y/2) >= A-o(1)`,

hence

`xy=q/D <= 2x-2A+o(1)`.

Combining with `dim L >= T-q` yields

`dim L / D >= x-xy`

`>= 2A-x-o(1)`.

Equivalently,

### Theorem C94.1 — quantitative exact-flat dimension

Along every canonical pure-rhombic chain-face sequence with bounded `T/D`,

`dim L >= [2(1+Delta_2)-T/D-o(1)] D`.

Every vector in this linear tangent subspace integrates, direction by direction, to a
nearby realization preserving the complete active equality framework `(C,H)`.

## 5. The 3D train-count dichotomy

If

`liminf T/D >=3`,

we are already in a very large train-surplus phase.

Otherwise pass to a subsequence with `T/D<3+o(1)`. Theorem C94.1 gives

`dim L / D >= 2(1+Delta_2)-3-o(1)`

`= 2Delta_2-1-o(1)`.

Numerically,

`2Delta_2-1 = pi/sqrt(3)-1 = 0.8137993642...`.

Therefore:

### Theorem C94 — macroscopic exact active-face flat

Every asymptotic canonical pure-rhombic C80 chain-face survivor satisfies at least one
of the following:

1. **high-train phase**

   `T >= (3-o(1))D`;

2. **macroscopic exact-flat phase**

   the tangent cone of the local exact `(C,H)` realization set contains a linear
   subspace of dimension at least

   `(pi/sqrt(3)-1-o(1))D`

   `= (0.8137993642...-o(1))D`,

   and after fixing global rotation this entire subspace is supported on non-chain
   train-angle coordinates.

C92 sharpens the lower end of the second phase: there

`T/D >= 2+Delta_2+10^(-4)`.

Thus throughout the low-train phase the exact active-face tangent dimension is between
roughly `0.8138D` and `0.9068D` at the coefficient level.

## 6. What C94 does not claim

C94 does **not** claim that the exact active equality set is a smooth manifold of this
dimension. Independent analytic arcs need not furnish one coordinate chart. The
proved statement is the one needed downstream: its tangent cone contains the explicit
linear space `L`, and C86 integrates every vector of `L` inside the exact active face.

C94 also does not say such a flex remains triangle-free until a macroscopic parameter
value. C86 is local; a finite continuation can hit a new unit contact, a new diameter
pair, or a 60-degree rhombus wall.

Therefore a dimension count alone is not a Level I contradiction.

## 7. Frontier effect

Before C94, the pure chain branch was described mainly by the ordered diameter objects
C87-C93. C94 adds a complementary kinematic invariant:

- C87-C93 force a paired staircase tree and quadratic secondary-train separation;
- C92 forces explicit train surplus;
- C94 says that unless `T/D` reaches 3, at least `0.813799D-o(D)` independent
  secondary-train angular directions are tangent to exact local realizations
  preserving all original contacts and all original diameter pairs.

The next target is an **activation-boundary theorem** for this macroscopic exact flat:
show that a linear-dimensional family of secondary-train motions cannot all terminate
only at harmless new-contact/new-diameter events. A valid theorem may instead force a
60-degree rhombus (hence a unit triangle), a strict sub-D competitor, or a shell area
loss proportional to the flat dimension.
