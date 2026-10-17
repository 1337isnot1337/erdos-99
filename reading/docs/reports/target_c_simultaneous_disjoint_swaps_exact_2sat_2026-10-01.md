> Generated reading edition · [exact source](../../../docs/reports/target_c_simultaneous_disjoint_swaps_exact_2sat_2026-10-01.md) · source SHA-256 `a141c3c3808d83e9685d8db6e77382dce6dd03cd4503f0b0484636351ab6a83d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-899DF0979598","canonical":true,"claim_ids":["C-DISJOINT-SWAP-2SAT"],"claim_statuses":{"C-DISJOINT-SWAP-2SAT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C: simultaneous disjoint finite swaps form an exact 2-SAT system

**Date:** 2026-10-01

**Starting main:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`

**State:** `2026-09-14.audit.51`

**Mission:** finite source-preserving gap-cut competitors.

**Classification:** canonical in `2026-10-05.audit.60` as `C-DISJOINT-SWAP-2SAT` for Sections 1--4. The repeated two-phase TB1 specialization in Section 5 remains unreviewed. Level I OPEN; C-I CLOSED; C-II OPEN.

```text
disjoint actual-source swaps -> exact binary distance clauses -> satisfying
assignment with an old diameter shortened -> strict competitor or a violation
of canonical diameter-pair minimality after contact minimization.
```

## 1. Full-source hypotheses

Let `A` be a finite unit-separated source of diameter `D`. Retain all source
points, including contact-isolated points. Let `L_1,...,L_k` be pairwise
disjoint subsets of source points, with prescribed translation vectors
`Delta_1,...,Delta_k`. For a binary assignment `x`, put

$$
 P_x(p)=P(p)+x_i\Delta_i\quad(p\in L_i),
$$

and fix every point outside their union. Assume every original unit contact
stays exactly unit **for every binary assignment**. This hypothesis can be
checked on at most four endpoint states per contact. It is not inferred from
one-at-a-time contact preservation when the subsets are not disjoint.

The current nonadjacent TB1 strip swaps on one shore provide such subsets:
each selected physical middle slab has its two private boundary train
families, and its full translation exchanges their two unit directions.
No other selected swap changes those boundary contacts. This specialization
uses the full-source cutset hypotheses in the unpromoted
[block-transposition report](target_c_open_cell_block_transposition_2026-10-01.md).
The abstract theorem below requires no train, grid, KKT, or phase hypothesis.

## 2. Exact Boolean compilation

For a source pair `pq`, its new squared distance depends only on the binary
variables owning its two endpoints. These are at most two distinct variables;
both endpoints in one slab share one variable. Let `f_pq` denote that exact
squared distance in its local zero/one states.

Call an assignment **strict-inactive admissible** when

$$
 f_{pq}=1\quad\text{for every old contact},
$$
$$
 f_{pq}>1\quad\text{for every old noncontact},
$$
$$
 f_{pq}\le D^2\quad\text{for every old diameter},
$$
$$
 f_{pq}<D^2\quad\text{for every old nondiameter}.
$$

This strict policy keeps the exact old contact graph and permits no new
diameter pair. It is a sufficient competitor criterion. It deliberately
does not classify moves that create contacts while strictly decreasing the
diameter, or moves that trade old diameter pairs against new ones.

For each local state violating these inequalities, forbid its binary
pattern. A forbidden two-variable state `(x_i=a,x_j=b)` is the clause

$$
 (x_i\ne a)\lor(x_j\ne b),                           \tag{1}
$$

and a forbidden one-variable state is a unit clause. Fixed pairs require
no variables. The conjunction `F` of these clauses is a 2-CNF formula
with at most four clauses per source pair. The all-zero assignment satisfies
`F` because it is the original source.

**Theorem 1.** Models of `F` are exactly the strict-inactive admissible
assignments. There exists such an assignment shortening at least one old
diameter if and only if, for some old diameter and one of its at most four
strictly shortening local states, `F` is satisfiable after pinning that
state's at most two variables.

**Proof.** Each pair constraint is enforced by excluding exactly its bad
local states; no variable belonging to another slab affects its length.
This proves the first statement. If a model shortens an old diameter, its
local state is one of the enumerated shortening states and supplies a
satisfiable pinned formula. Conversely any model of a pinned formula
is admissible and shortens the pinned diameter. QED.

Construction uses `O(|A|^2)` exact distance evaluations. A 2-SAT instance
is solved by its implication graph: a two-literal clause gives its two
contrapositive implications, and it is unsatisfiable exactly when a literal
and its negation lie in one strongly connected component. Here is a proof
of that criterion. Such a component forces either truth choice to imply
its negation. Conversely, when no opposite literals share a component,
topologically order the component DAG, and set each variable according to
which of its opposite components comes later; an implication from a true
literal to a false literal would contradict this order and its
contrapositive implication. This gives a model.

Thus at most `4|H|` pinned solves decide the strict-inactive escape problem
in polynomial time. Each failed pinned solve can be certified by the two
directed paths connecting an opposite-literal pair in the augmented
implication graph. Numerical angle approximation is unnecessary when the
source and prescribed moves have exact coordinates.

## 3. Exact canonical consequence

Suppose the source is the canonical contact-minimal, then
diameter-pair-minimal global representative. An admissible assignment with
an old diameter shortened preserves cardinality, all old contacts, and all
old noncontact strictness. Every new diameter pair is an unchanged-length
old diameter pair. Consequently either:

- all old diameters shorten, giving global diameter `<D`; or
- diameter stays `D`, contact count stays the same, and diameter-pair count
  strictly decreases.

Both contradict the canonical normalization. This is an actual finite
source argument. It does not identify an infinitesimal flex with a finite
move or assume that independently feasible exchanges are compatible.

Accordingly every pinned shortening instance is unsatisfiable for a
canonical survivor. This gives a concrete augmented-system obstruction:
its actual source pair inequalities must yield implication-path
contradictions for **every** candidate shortening state. The missing
closing theorem is that the source geometry forbids that collection of
contradictions for a sufficiently large retained TB1 family.

## 4. The inactive clauses remain at inverse-diameter scale

Suppose `|Delta_i|<=s`. Changing a local binary state changes a pair
distance by at most `2s`. Therefore an old noncontact that contributes
a forbidden lower-bound state has old length at most `1+2s`, and an old
nondiameter that contributes a forbidden upper-bound state has old length
at least `D-2s`. Both statements include moves of both endpoints.

For current TB1 swaps, `s<=4K/D`; every inactive blocking clause comes
from an actual source pair satisfying

$$
 1<|pq|\le1+8K/D
 \quad\text{or}\quad D-8K/D\le|pq|<D.              \tag{2}
$$

Old diameter clauses represent finite compensation requirements between
moving endpoint slabs, including the TWO-SIGN case. Formula `F` therefore
retains both active diameter compensation and nonlocal near-active source
pairs in one exact system. Counting such pairs is not its conclusion.

For nonadjacent swaps on one retained shore, complete-grid rhombus
immunity also persists jointly: each boundary row exchanges its unit
direction with its paired row, while transverse row directions stay
unchanged. Each affected rhombus is congruent to an old retained rhombus.
No chosen train belongs to two swaps, so another swap cannot alter its
boundary contact family. Thus their diagonals do not supply inactive
clauses. This is conditional on the actual grid/slab embedding of the
unpromoted block theorem, not a general statement about arbitrary slabs.

## 5. Identical two-phase swaps force directed returns to the fixed source

There is a stronger exact specialization when every selected slab exchanges
the same ordered pair of distinct unit directions `u,v`. Then every
translation is the identical nonzero vector `Delta=v-u`. This is a stated
two-phase hypothesis; a general nonconstant shore need not contain such a
large repeated family.

For two moving slabs, the `00` and `11` states give the same relative vector.
They are both feasible. Hence every forbidden state is `10` or `01`, giving
an implication `x_i=>x_j` or `x_j=>x_i`. A forbidden `1` state against a
fixed point gives `x_i=>x_0`, where `x_0` is the fixed false node. The
entire strict-inactive formula is therefore a directed closure system.

Let `R` be the moving nodes from which `x_0` is reachable. The assignment

$$
 x_i=0\ (i\in R),\qquad x_i=1\ (i\notin R)          \tag{3}
$$

is admissible: its true-node set has no outgoing implication to a false
node. It is the largest admissible true set. This follows directly from
the graph, not a numerical motion search.

Now assume the **actual full-source** positive KKT equilibrium. For each
slab, suppose its only boundary contacts are the two private families,
oriented inward as `u` and `-v`, with positive total contact mass. No old
contact joins two different moving slabs. These are the actual nonadjacent
TB1 slab hypotheses, not properties of arbitrary disconnected source cuts.

**Theorem 2.** For a canonical global source with these hypotheses,
every selected moving node lies in `R`: each has a directed source-pair
implication path to the fixed source.

**Proof.** If `S` is the nonempty set of nodes outside `R`, (3) translates
their union by `Delta` and is admissible. Put `q=|Delta|>0`. The two inward
contact vectors satisfy

$$
 u\cdot\Delta=(-v)\cdot\Delta=-q^2/2<0.
$$

Sum full-source KKT virtual work for the velocity that is `Delta` on
this union and zero elsewhere. Internal forces cancel. Its boundary
contact contribution is strictly negative, since at least one private
boundary family has positive mass. Thus its weighted diameter contribution
is nonzero, and at least one old diameter crosses the union boundary.

Such a diameter's relative vector changes by `Delta` or `-Delta`. The
open-cell non-grazing bound for the same pair `u,v` is
`|r dot Delta|>Dq^2/2`, from the unpromoted block-swap theorem. If its
crossing relative vector changes by `Delta`, its squared change is
`2r dot Delta+q^2`; the reverse case has the other sign. For `D>1`,
neither can vanish. Admissibility excludes a positive change, so the
crossing diameter strictly shortens. Section 3 then contradicts canonical
global/lexicographic minimality. Therefore `S` is empty. QED.

Every inactive edge on these implication paths comes from a source pair
within `q`, rather than `2q`, of unit or diameter activity: identical
translations cancel in the `11` state, while a split state changes only
one relative endpoint by `Delta`. Thus repeated two-phase TB1 swaps force
actual directed returns through diameter edges and `4K/D`-near-active
source pairs. The result is a global simultaneous-move obstruction,
not a count of one-at-a-time witnesses.

What remains unproved is that the actual hull/train geometry excludes
these return paths. ONE-SIGN near-active clauses or TWO-SIGN diameter
clauses can still provide them. Nor is the repeated ordered two-phase
hypothesis established for arbitrary nonconstant-phase survivors.

## 6. Verifier, regressions, and scope

`python3 research/verify_binary_contact_swap_2sat.py` runs five exact
source examples and compares each solver answer with exhaustive binary
assignments. They include an actual two-contact swap giving a strict
competitor, compatible simultaneous moves, a diameter compensation
implication, all nonzero moves blocked, and a move excluded because it
creates new contacts under the stated strict policy. A move failing contact
preservation is rejected. All 176 two-variable clause systems with up to
three distinct clauses from the ten possible unit/binary clauses are also
checked against exhaustive assignments.

With `--source path.json`, the tool reads rational source points and
disjoint moves, checks contact preservation, compiles every source pair,
and either prints a fully rechecked escape assignment or reports none in
that finite family. For identical translations it also prints implication
return paths to the fixed node and the largest admissible closed moving set.
The JSON schema is in the script docstring. Negative
output does not prove global optimality or eliminate the branch.

Canonical dependencies: source normalization and retained-isolate scope
from [CURRENT](../targets/target-c/CURRENT.md). Unpromoted dependencies
for the TB1 specialization: full-source strip cutsets, finite swaps, and
complete-grid immunity. The general compilation theorem is self-contained.
The abstract Sections 1--4 theorem is independently audited and canonical in audit.60; the TB1 specialization retains its stated unreviewed scope.

Exact remaining obligation: extract a satisfying pinned shortening state
for a large **actual** TB1 source family, or rule out every possible
opposite-literal contradiction using actual diameter hull order and the
near-active pair geometry in (2). Exact-phase, split-star,
inactive-interface, and macroscopic-container branches remain separate.
