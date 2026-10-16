<!-- theorem-state: {"artifact_id":"ART-629766A03C5F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — an auxiliary diameter-first normal form permits triangle-free contact gains

`canonical finite weak-row release -> diameter-first triangle-free optimal source
with full support -> finite diameter-pair reduction allowing safe new contacts ->
contradiction if such a source move is constructed -> Level I`

**Date:** 2026-10-02

**Starting shared HEAD:** `af823f5f8b998aadf652df9aed01b2dbc2882e75`

**Research base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`

**Predecessor:** `f12e91eb`

**State:** `2026-09-14.audit.51`; Level I and C-II OPEN.

**Classification:** proved candidate awaiting promotion; conditional finite-chart
application. This is an auxiliary source selection, not a change to the canonical
contact-first source or a promotion of its unreviewed train extraction.

## 1. Canonical finite-release input

The promoted C53/C63 restoration, Sections 4–7 of
`target_c_c53_orientation_and_ci_restoration_2026-09-09.md`, supplies:

- PSD for every normalized actual source KKT stress;
- a finite nearby same-cardinality feasible source that removes every weak
  active contact/diameter row and creates no new active pair;
- actual integration of critical velocities, with initially inactive pairs
  retaining strict slack.

The finite-release assertion precedes contact-count minimization in its proof.
That is the specific canonical input used below. We do not import a generic
second-order jet in place of this finite theorem.

## 2. Alternative normal-form theorem

Fix `n` for which a triangle-free global minimizer exists. Among all triangle-free
global minimizers choose `A` minimizing first the number `h(A)` of diameter pairs,
then the number `c(A)` of unit contacts within the first class. Such a source
exists: these are minima of nonempty sets of nonnegative integer counts. No
closedness or compactness claim for the triangle-free subset is needed.

Then

\[
\boxed{C=C_*,\qquad H=H_*.}
\tag{1}
\]

In particular a relative-interior normalized KKT stress is positive on every
actual contact and diameter pair.

### Proof

Apply the canonical finite weak-row release. Its new active sets are subsets
of the old sets, and every weak active row is absent. The new configuration
remains triangle-free, because its contact graph is a subgraph of the old
triangle-free graph. Its diameter is at most `D(n)` and hence, by global
optimality, equals `D(n)`.

If any diameter row was weak, the new source has fewer diameter pairs,
contradicting primary `h` minimization. If there is no weak diameter row
but some weak contact, either a diameter also disappears, contradicting
primary minimization, or the diameter count stays fixed and the contact
count falls, contradicting secondary minimization. These exhaust all
weak rows and prove (1). ∎

Every sufficiently nearby fixed-diameter feasible source likewise preserves
all old active lengths: inactive pairs stay strict, the diameter count cannot
fall, and then the contact count cannot fall. Consequently the canonical
common-kernel argument carries over to this auxiliary source. For a
relative-interior stress `s_bar`,

\[
\ker\Omega_{s_{\rm bar}}=\bigcap_s\ker\Omega_s,
\qquad
\ker R_{C\cup H}\subseteq\ker\Omega_{s_{\rm bar}}\otimes\mathbb R^2.
\tag{2}
\]

To check (2), integrate a critical velocity using the promoted finite theorem,
apply the local active-length preservation, and pair the exact squared-length
identities with any stress. PSD makes both displacement coordinate fields have
zero energy. Relative interior then gives the kernel intersection, just as in
the promoted proof. Isolated source coordinates remain free. No new claim of
ZR nullity, mixed rank, or complete-grid extraction is made here.

## 3. Stronger finite competitor contract

For this diameter-first source, any finite same-cardinality configuration `A'`
with

\[
\min_{x\ne y\in A'}|x-y|\ge1,\qquad
\operatorname{diam}A'\le D(n),\qquad
A'\text{ triangle-free},\qquad h(A')<h(A)
\tag{3}
\]

is impossible, **even if its number of unit contacts increases**.
If its diameter is smaller, global optimality is contradicted already; if it
equals `D(n)`, primary diameter-pair minimization is contradicted.

An old-contact-preserving motion therefore may create new contacts, provided
those contacts do not make a unit triangle and no new diameter replaces the
shortened old diameters. The canonical contact-first source does not have
this global comparison property. To apply (3), construct the move on the
auxiliary source and audit any extraction theorem that used absolute primary
contact minimization; do not transfer an existing source chart by assertion.

If every triangle-free global minimizer at large `n` yielded such a selected
source and a move satisfying (3), no triangle-free global minimizer could
exist. Thus the original `for every global minimizer` quantifier is retained.

## 4. Pure joint equality contacts are automatically triangle-free

Here is a precise useful contact-gain criterion. Let disjoint owners have
nonzero displacement vectors `Delta_i`, all with length at most `1/8`,
mutually positive dot products, and unit directions within Euclidean distance
`1/16` of one common unit vector `v`. Assume every old unit contact is
preserved for **every** binary owner pattern. The old source is triangle-free.

Take a pattern that is unit-separated. Suppose every new unit contact is a
pure joint equality between two selected distinct owners, whose old vector
`r` satisfies

\[
1<|r|\le5/4,\qquad |r\cdot v|\le1/8.
\tag{4}
\]

Also assume the relative displacement cloud has diameter at most `1/8`.
Then the new source is triangle-free.

### Proof

An old unit contact cannot join two different moving owners: the four
binary squared-length equations have mixed difference
`-2 Delta_i dot Delta_j`, which is nonzero.

Suppose a new triangle has exactly one new edge `xy`, with endpoint owners
`i,j`. A common old unit neighbor `z` cannot be in any moving owner: one
of the old edges would join distinct moving owners. Thus `z` is fixed.
For `a_i=|Delta_i|`, `v_i=Delta_i/a_i`, its old unit vector `c_i=x-z`
satisfies `c_i dot v_i=-a_i/2`. Its new vector `c_i'=c_i+Delta_i` is unit
and satisfies `c_i' dot v_i=a_i/2`. Hence

\[
|c_i'\cdot v|\le a_i/2+|v_i-v|\le1/8,
\]

and similarly for `j`. With `u` perpendicular to `v`, each unit vector
has `|c' dot u|>7/8`. If the two longitudinal signs agree, their
difference has longitudinal size at most `1/8` and transverse size at
most `1/4`, hence length strictly below one. If the signs differ, their
longitudinal difference exceeds `7/4`. Neither case is the unit edge
required by a triangle.

Every new edge in (4), after the pattern, is unit and has transverse
projection at most `1/8+1/8=1/4`. Two such unit edges at a common vertex
cannot be sides of a unit triangle: if their longitudinal signs agree,
the opposite side has length less than one; if signs differ, its length
exceeds `sqrt(15)/2>1`. This excludes triangles with at least two new
edges. A triangle with no new edge was already absent. ∎

Thus, on this auxiliary source, pure joint Horn states with final length
**exactly one** may be allowed under these explicit hypotheses. Final
length strictly below one remains forbidden. Unary rhombus equality
contacts create unit triangles and remain forbidden; arbitrary new
contacts do not receive this exemption.

The previous source path theorem is consistent with this argument: all
near-axial pure conflict pairs form disjoint paths on source vertices.
Their owner graph may still have cycles, and strict overlaps still block
finite motions. No positive multiplier is assigned to an inactive pair.

## 5. Exact contact-gain example and certificate

Let `a=1/1000`, `b=2/1000`, and put

\[
x=(1,b-a),\quad x^+=(1,1+b-a),\quad y=(0,0),\quad y^-=(0,-1).
\]

The old unit contacts are precisely `xx^+` and `yy^-`. Translate the
`x` owner by `(0,a)` and the `y` owner by `(0,b)`. The pair `xy` has
length greater than one in states `00,10,01` and equals one in `11`.
All old contacts remain unit for every state; all four patterns are
unit-separated. In state `11` the new contact graph is the path
`x^+—x—y—y^-`, so there is no triangle. Its squared diameter is five,
strictly less than the old `1+(2+b-a)^2`.

The existing exact source-face verifier now checks this rational packet.
It is not a global optimum or an unbounded disproof: it certifies that
benign pure joint contact creation and exact diameter shortening are
compatible, rather than treating every new contact as an overlap.

## 6. Remaining obligation

The reverse-order source theorem is proved directly from canonical finite
release. To use it for closure, audit the fixed-star/O–O extraction on
this source, then find a source-feasible diameter-pair-reducing pattern
or another finite motion. Strict outer-face overlaps, unsafe new unit
triangles, all TWO-SIGN alternatives, and the other global C-II branches
remain. No canonical source convention or Level I status changes.
