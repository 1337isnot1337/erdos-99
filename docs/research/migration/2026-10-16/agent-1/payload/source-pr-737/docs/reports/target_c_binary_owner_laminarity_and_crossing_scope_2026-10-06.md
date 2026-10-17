<!-- theorem-state: {"artifact_id":"ART-E76E961E8727","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: acute independent binary owners cannot activate crossing trains

Date: 2026-10-06. Authority: main `583203ac`, audit.62.
Classification: **proved candidate synthesis awaiting independent audit**;
the rational packet below is a **scope regression**. Level I remains open.

## 1. The distinction needed before the crossing case

Use actual global stopped O--O cuts on the connected positive-contact core.
Assume every old contact stays exactly unit under **every independent binary
owner selection**, each nonzero translation has norm below one, distinct
nonzero translations are mutually acute, and all retained selected cut
increments are nonzero.

Then the active selected trains are pairwise noncrossing, even without a
projective window restriction.

**Proof.** Canonical `C-NEAR-UNIT-CONFLICT-GEOMETRY` classifies strict-rhombus
ownership under exactly these hypotheses: all vertices fixed, all four
in one moving owner, or two adjacent vertices in one owner and the other
two fixed. In the first two cases no train direction changes across the
rhombus. In the last case only the opposite moving/fixed contacts change,
and those two contacts belong to one complete train. Thus a strict rhombus
cannot activate both crossing trains. Two complete centerlines meet only
at strict-rhombus crossings, so no two active trains cross. QED.

The occurrence-disk dual is therefore a tree for this entire binary scope.
Its common-diameter hub proof and `K_own<=T_OO` do not require the narrow
direction window. Canonical good-to-good trains cross pairwise, so this
selected family has at most one fully good train. Hence the terminal and
owner-recurrence conclusions extend to this scope:

\[
 T_{OO}\le x_B+m_B+1,
 \qquad K_{own}+\rho_{own}\le x_B+m_B+1.
\]

The common-unit-neighbor binary-witness exclusion still requires the
narrow direction window: noncrossing trains can have widely separated
directions without crossing each other.

With the personally checked terminal O--O depletion candidate, every
acute independent-binary O--O owner system at `q/D->pi`, `u_B=o(D)`
has `K_own=o(D)`, regardless of selected direction width. This is a
composition of candidates, not a canonical promotion or full-core closure.

## 2. A crossing multishear is a different finite system

Train variables and disjoint owner variables are not interchangeable.
Consider the exact strict unit rhombus with

\[
 u=(1,0),\quad w=(5/13,12/13),\quad
 p_{00}=0,\ p_{10}=u,\ p_{01}=w,\ p_{11}=u+w.
\]

Its two noncontact diagonals have squared lengths `16/13` and `36/13`.
Let `R` be the rational rotation with

\[
 \cos\theta=999999/1000001,
 \qquad \sin\theta=2000/1000001.
\]

Put `delta_u=Ru-u`, `delta_w=Rw-w`. Choose either original or rotated
unit vector for each train independently, and set

\[
 p_{10}'=u(a),\quad p_{01}'=w(b),\quad
 p_{11}'=u(a)+w(b),\quad a,b\in\{0,1\}.
\]

All four old side contacts are exactly unit in all four train states,
and both diagonals stay strictly longer than one. Both trains are active
in state `11`. Moreover `delta_u dot delta_w>0`, and the cloud vectors
`delta_u`, `delta_w`, `delta_u+delta_w` are pairwise acute.

If those three nonzero region vectors are treated as three *independent
owner proposals*, selecting only the `u` vertex shortens the old unit
contact to the fixed `u+w` vertex below one. The latter vertex must be
selected consistently with the train variables. Therefore this packet
does not meet the independent binary contact-preservation hypothesis.

State `11` is a rigid rotation of the whole four-point rhombus and is
not a beneficial source competitor. The packet is not a canonical source;
it isolates the exact failure of applying the owner Horn theorem to
arbitrary crossing train variables.

## 3. The strengthened full-core problem

A genuine crossing multishear needs its own finite constraint compilation.
Its vertices have translations given by sums of several train increments.
Some constraints depend on more than two train variables. All-zero
validity alone does not imply Horn form for those higher-arity constraints.
For example `not x_1 or x_2 or x_3` is zero-valid but has two positive
literals; one forced variable can need a choice of repairs rather than
one least implication closure.

The next admissible endpoint must either construct a compatible independent
binary owner family within the proven laminar scope, or solve these
coupled train/face constraints directly and certify the resulting old
contacts, every old diameter, inactive uppers and lowers, unary rhombi,
and a strictly improved contact or diameter count. No such endpoint is
constructed by the rhombus packet.

Audit.53 return paths and audit.52 full face elimination remain available,
but neither identifies the owner binary variables with crossing train
variables. Pentagon capacity locks retain their actual-load/global-optimality
gap. The macroscopic inactive-container packet existence problem remains
separate.

## 4. Validation and scope

`research/verify_target_c_binary_crossing_scope_2026_10_06.py` checks the
four train states and all eight independent region-owner states by exact
rational pair distances. It verifies the acute cloud, strict source
rhombus, preserved train-state contacts, and the failed owner singleton.
It does not certify a canonical KKT source, active-diameter improvement,
asymptotic density or global optimality. Canonical rhombus ownership
patterns were additionally rerun through the existing near-unit verifier.

Dependencies: `C-NEAR-UNIT-CONFLICT-GEOMETRY`, `C-LINEAR-NONMATCH`, the
actual O--O shore hypotheses, and the separately documented terminal
O--O depletion candidate for the final terminal composition. Retain as
unreviewed research pending independent audit.
