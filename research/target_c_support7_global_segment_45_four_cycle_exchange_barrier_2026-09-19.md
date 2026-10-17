<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "25ae5cbb256ac7dd6cb7022787f3d279a4c05a41", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_45_four_cycle_exchange_barrier_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "79c5f33d433f1c935fb53d1eabf525277b82e772bc296b021666e3cb13d4280f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C support-seven: a four-exchange barrier for the 45-cycle metric test

Date: 2026-09-19

Status: exact structural refinement of the generic reciprocal metric layer. The theorem-state authority is unchanged. C-II remains open.

## Result

The current complete generic metric test uses the 45 simple `K8` four-cycles

\[
F=\{C^{(1)}_{ij},C^{(2)}_{ij},C^{(3)}_{ij}:2\le i<j\le7\},
\]

three for each of the fifteen pairs `ij`. Together with the 56 automatic triangle-side cycles, these imply the fifteen ground-root star equations.

There are 210 undirected simple four-cycles in `K8`. An obvious next question is whether some 44 of them can replace the present 45-cycle test. The following exact obstruction sharply restricts such a search:

\[
\boxed{\text{Any sufficient 44-cycle family must use at least five cycles outside }F.}
\]

Equivalently, no sufficient 44-cycle family can be obtained by introducing only zero, one, two, three, or four external simple four-cycles. Such a 44-family, if it exists at all, must omit at least six of the present 45 cycles and introduce at least five external cycles.

This is not a proof that 45 is globally minimal. It rules out all replacements through four external cycles and identifies the first unresolved exchange depth as five.

Certificate:

`research/verify_target_c_support7_global_segment_45_four_cycle_exchange_barrier_2026_09_19.py`

The verifier uses only exact `fractions.Fraction` arithmetic and integer determinants. It uses no floating-point arithmetic or optimization.

## Coordinate structure

Let `SIDE` be the span of the 56 automatic triangle-side cycles in the 168-edge cycle space of `L(K8)`. Let

\[
W=\operatorname{span}_{\mathbb Q}(\mathrm{SIDE}\cup F).
\]

The 101 rows `SIDE + F` are independent, so `F` is a 45-element basis of `W/SIDE`.

For each pair `2 <= i < j <= 7`, the previously proved local `K4` identity is

\[
2S_{ij}
=-T_{01i}+T_{01j}-T_{0ij}-T_{1ij}
+C^{(1)}_{ij}-C^{(2)}_{ij}-C^{(3)}_{ij}.
\]

Modulo `SIDE`, therefore,

\[
S_{ij}=\tfrac12\bigl(C^{(1)}_{ij}-C^{(2)}_{ij}-C^{(3)}_{ij}\bigr).
\]

In the `F` basis, the fifteen ground-root cycles consequently occupy fifteen disjoint three-coordinate blocks. Each block has coordinate vector

\[
\tfrac12(1,-1,-1).
\]

If a subset `R` of the selected cycles is removed, the dimension of the missing ground information is exactly the number `t(R)` of these three-coordinate blocks touched by `R`.

## External cycles and the quotient by W

Enumerating all 210 undirected simple `K8` four-cycles gives 45 selected cycles and 165 external cycles. Every one of the 165 has nonzero image in the quotient by `W`.

For a set `E` of `r` external cycles, let `d(E)` be the exact rank of their images modulo `W`. Then

\[
\dim\bigl(\operatorname{span}(E)\cap W\bigr)=r-d(E).
\]

A 44-cycle replacement with `r` external cycles contains `44-r` members of `F`, hence removes

\[
|R|=45-(44-r)=r+1
\]

selected cycles. A necessary condition for it to recover all fifteen ground equations is

\[
t(R)\le r-d(E).
\tag{1}
\]

The verifier applies this condition exactly.

## Zero and one external cycle

For `r=0`, one selected cycle is removed, so `t(R)>=1`, while no replacement direction in `W` is available.

For `r=1`, the external cycle has nonzero quotient image, so `d(E)=1` and again `r-d(E)=0`. Two selected cycles are removed, so `t(R)>=1`. Both cases fail immediately.

## Two external cycles

The exact quotient images of the 165 external cycles form

```text
105 projective classes
 45 singleton classes
 60 two-element classes
```

Thus two external cycles can contribute a nonzero `W`-valued combination only for one of the 60 dependent pairs. Otherwise `d(E)=2` and (1) fails.

For a dependent pair, `r-d(E)=1`. Three selected cycles are removed. If those three touch two or more ground blocks, (1) fails. The only remaining possibility is to remove exactly one whole three-cycle block.

The verifier constructs the unique `W`-valued combination of each of the 60 dependent external pairs in exact rational coordinates and checks it against all fifteen ground blocks. None is proportional to the missing block vector `(1,-1,-1)`.

Thus all

\[
60\cdot15=900
\]

two-external/full-block possibilities fail exactly.

## Three external cycles

Every exact external projective class has size at most two. Therefore three external cycles have quotient rank at least two:

\[
d(E)\ge2,
\qquad
r-d(E)\le1.
\]

But removing four selected cycles necessarily touches at least

\[
\left\lceil\frac4{3}\right\rceil=2
\]

ground blocks. Hence (1) fails for every three-external replacement.

## Four external cycles

Removing five selected cycles touches at least two ground blocks. Hence a possible four-external replacement must satisfy

\[
4-d(E)\ge2,
\]

so `d(E)<=2`.

The verifier constructs the exact projective quotient configuration of all 165 external cycles and enumerates every four-set of quotient rank at most two. There are exactly

\[
\boxed{2010}
\]

such four-sets, and every one has exact quotient rank two. Thus each contributes exactly two `W`-valued directions.

With only two replacement directions, the five removed selected cycles must touch exactly two ground blocks. Because a block has only three coordinates, the removal pattern must be `3+2`: one complete block and two coordinates of another. There are

\[
15\cdot14\cdot\binom32=\boxed{630}
\]

such removed-five patterns.

For each of the 2,010 external four-sets, the verifier computes an exact rational basis for `span(E) intersect W`, restricts those two directions to each of the 630 possible removed-coordinate sets, and tests exact row-space containment of the two missing ground directions. None works.

The final finite audit therefore contains

\[
2010\cdot630=\boxed{1,266,300}
\]

exact four-external compensation checks.

## Consequence

A 44-cycle complete metric test, if one exists among the 210 simple `K8` four-cycles, must begin at exchange depth five:

\[
|E|\ge5,
\qquad
|R|=|E|+1\ge6.
\]

This makes the remaining minimization problem smaller and more structured. The next search should classify quotient-rank-at-most-three five-external sets. For five external cycles, six selected cycles are removed. The first possible cases are:

- quotient rank three, leaving a two-dimensional `W` kernel and therefore forcing the six removals to be exactly two whole ground blocks;
- quotient rank two, leaving a three-dimensional `W` kernel and allowing removals across at most three ground blocks.

That is the first unresolved exchange layer. A failure there would push any 44-cycle certificate to at least six external cycles; a success would produce an explicit 44-cycle replacement to test with the rational sine-interval engine.

## Scope

This result concerns only the size and structure of a simple-four-cycle metric completion test. It does not by itself exclude additional generic-H6 cells, does not prove that 45 four-cycles are globally minimal, and does not change C-II theorem state. The current explicit reflection-closed generic-H6 endpoint is 4,464 cells; these metric identities are intended for the next state-by-state exact magnitude exclusions on that endpoint.
