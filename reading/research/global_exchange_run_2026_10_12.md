> Generated reading edition · [exact source](../../research/global_exchange_run_2026_10_12.md) · source SHA-256 `001b81d3be7bd23a0c10976c873459bd7c0545563846f418ad1c92a8f98e609c`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Global exchange run, 2026-10-12

Classification: unreviewed research ledger. Level I remains open.

- Immutable base: `ab6dd3336f9f8d440f2bada76edb32153391cddc`.
- State version: `2026-10-10.audit.234`.
- Worktree: isolated source research worktree (local path withheld).
- Branch: `research/global-exchange-20261012`.
- Target: the whole-problem global minimizer quantifier, through simultaneous
  replacement of arbitrary subsets of the complete source.
- Endpoint: for every sufficiently large triangle-free global minimizer A,
  construct n unit-separated points of diameter strictly below diam(A).
- Dependencies: `docs/problem/statement.md`; elementary finite graph matching
  proved in the new report. No unpromoted mathematical report is a premise.

## Diverse mechanisms considered

1. **Many-label replacement and packing overlays.** Pursue an exact, integral
   optimization of the joint cost of deleting actual diameter pairs and removing
   every lower/upper cross-pair conflict. Comparison points may retain arbitrary
   original contact-isolated labels. The packet itself may have fewer than n points.
2. **Nonlinear or lifted source deformation.** Exploratory. An energy decrease,
   negative stress direction in three dimensions, or average contraction does not
   preserve planar feasibility and all maximum-distance constraints. No new bridge
   from these quantities to a strict planar competitor is available here.
3. **Density and thermodynamic/crystallization arguments.** Exploratory. Exact
   triangle-free packings can approach triangular density, and the canonical
   strict-D lattice competitor itself has a triangle-free deformation. A density
   estimate without a source-optimality mechanism cannot settle attainment.
4. **Contact pruning and isolated components.** Do not resume a narrower terminal
   lattice subcase. The current attempt must optimize the complete source and
   permit all source labels to participate in one simultaneous replacement.

## Current implication chain

For a unit-separated packet B with diam(B)<D, define a cross-pair conflict when
the squared distance is below 1 or at least D^2. Let H contain every actual
source diameter pair. For a vertex cover T of H, let nu_T be the maximum
matching size between B and A\T in the cross-conflict graph.

`m - |T| - nu_T >= 0`

`-> an independent mixed packet of at least n labels`

`-> every retained/inserted pair has distance in [1,D)`

`-> a same-cardinality strict-D competitor -> contradiction`.

The graph condition is an exact equivalence for mixtures from A and the supplied
B, not a proof that a successful B exists for arbitrary large minimizers.

## Binding checks

- Optimize |T|+nu_T jointly. Minimum-cardinality diameter covers alone can miss a
  genuine competitor; a three-label rational geometric regression is available.
- Include upper cross conflicts. Even a square global minimizer gives a false
  mixed competitor if only unit-distance blockers are counted.
- The lower cross-conflict graph is planar. The complete graph, with upper
  conflicts, need not be planar: a translated three-point packet and a square
  source produce K_(4,3).
- Exact pair checks, maximum matchings and exhaustive mixed-subset checks will be
  recorded in `research/verify_global_joint_exchange_2026_10_12.py`.

## Validated checkpoints

- `11b3195d`: exact joint cover/matching theorem, four rational full-source
  fixtures, and an independent exhaustive geometric enumeration; committed
  and pushed after the research verifier, artifact-index regeneration,
  theorem-state checks, PR-state check, and whitespace check passed.
- The minimum-cover-first obstruction now has an all-k rational construction
  with triangular leading population coefficient, exactly one unit contact,
  and n-2 contact isolates. Its cross graph is exactly a matching. A complete
  same-cardinality competitor has diameter D-1/8. At k=4,5 the exact verifiers
  certify 57/256 source labels and all 55/254 contact isolates. This is a
  nonglobal regression against the optimization shortcut, not a global
  counterexample or a KKT source theorem.

## Remaining global obligation

Prove that every sufficiently large triangle-free global minimizer admits a
unit-separated strict-D comparison packet B and a diameter vertex cover T with
`nu_T <= |B|-|T|`. This is a full-source existence theorem; proving the matching
identity for a supplied packet does not establish it.

## A different global mechanism: propagating a free region

Primary source checked: Achill Schurmann, *On packing spheres into containers*,
Documenta Mathematica 11 (2006), 393-406,
<https://ems.press/content/serial-article-files/25994>. Definition 1, Theorem 2,
and Propositions 2-4 were read in the original paper. The construction creates
a region with no unit contacts, propagates that condition through interior
labels, then moves boundary labels into the old hull. The theorem assumes a
smooth fixed container and a family with limited complexity: finitely many
local difference-vector accumulation points and a uniform positive lower
bound rho for contact affine spans that do not contain the source label.
Proposition 3 needs a seed radius at least 1/rho. Section 4 discusses diameter
minimization as another setting; a discussion is not a proof that arbitrary
triangle-free minimizers satisfy the hypotheses. The canonical literature
baseline already records the eventual nonlattice result, so it is not new.

The useful global endpoint here is an actual same-cardinality packing strictly
inside the old hull, or a spanning finite contact-release followed by a strict
homothety. No fixed grain, isolated point subset, or restricted lattice case
should be taken as the final target.

### Exact obstacle to dropping the uniform geometry hypothesis

Classification: regression, nonglobal. For rational 0<t<1, take a center 0 and
its three unit neighbors

    u=(1,0),
    v=(-(1-t^2)/(1+t^2), 2t/(1+t^2)),
    w=(0,-1).

The three neighbor-neighbor squared distances exceed 1, so this is a
triangle-free penny graph. With a=(1-t^2)/(1+t^2)>0 and b=2t/(1+t^2)>0,

    a*u + v + b*w = 0

is a strictly positive surrounding equilibrium. The affine line through u,v
misses the origin by t/sqrt(1+t^2), which tends to zero. Thus triangle-freeness
does not supply a uniform rho.

More concretely, for any prescribed R>0 take t<1/(4R), and let the potential
free ball have center q=(R*t,R) and radius R. Every one of these four source
labels is outside the closed ball: the origin has squared distance
R^2*(1+t^2)>R^2, the u,v distances exceed R^2 by R^2*t^2+1-2R*t>0,
and the w distance exceeds R^2 by R^2*t^2+1+2R>0. The surrounded origin is
only R*(sqrt(1+t^2)-1) beyond the free-ball boundary. This tends to zero while
its contacts still surround it. It refutes a uniform local propagation lemma
based solely on triangle-freeness and an adjacent free ball. It does not
refute a global source theorem: these four-label sources are nonglobal, and
no whole-source optimality or free-ball-in-hull extraction is asserted.

The next global bridge must either use full-source optimality to overcome
these weak surrounding cages, or construct a finite collective replacement
that bypasses them. Merely assuming a uniform angle/affine-span gap would
return to an unproved restricted branch.

## Publication and CI

- Draft research PR: <https://github.com/1337isnot1337/e-99/pull/957>.
- `74a36f31`: pushed all-k dense star regression and its exact verifier.
- Hosted workflow jobs had no executed steps at this source snapshot; no remote
  CI success is claimed for these changes.
- Both research verifiers and the local artifact/theorem-state/PR-state/
  whitespace checks passed at that commit. The branch contained unique unmerged research at this snapshot. Its recorded
  Level I continuation goal is historical; destination theorem-state remains
  authoritative.
