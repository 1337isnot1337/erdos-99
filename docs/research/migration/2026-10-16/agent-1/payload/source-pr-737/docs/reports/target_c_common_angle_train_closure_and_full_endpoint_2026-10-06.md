<!-- theorem-state: {"artifact_id":"ART-1F4E76DE5401","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: exact common-angle train closure and full-source endpoint checks

Date: 2026-10-06. Authority: `583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`,
state `2026-10-05.audit.62`. Classification: **proved candidate awaiting
independent audit** for the reduction; **regression** for the finite scope
packets. C-II and Level I remain open. No claims are promoted here.

The next implication being audited is

`closed coupled train selection -> explicitly reconstructed source ->
all finite lower/upper checks -> fewer old diameter pairs or sub-D
diameter -> contradiction`.

The owner Horn theorem remains valid in its acute independent-owner scope.
It is not a theorem about arbitrary independent stopped-train bits.

## 1. Linear Boolean closure for a common angle

On the actual connected nonisolated contact core, choose one bit `x_tau`
for every complete stopped train. Selected contacts rotate by a common
angle `theta`; unselected contacts retain their original vectors. For an
oriented original unit edge `e`, write its vector as `w_e`.

Opposite sides of an old rhombus belong to the same train, so their
rotated vectors cancel identically. At a physical exceptional face `F`,
the exact closure equation is

\[
 \sum_{e\in\partial F}\operatorname{Rot}(x_{\tau(e)}\theta)w_e
 = (\operatorname{Rot}(\theta)-I)
       \sum_{e\in\partial F}x_{\tau(e)}w_e=0.
\tag{1}
\]

For `theta` not a multiple of `2pi`, `Rot(theta)-I` is invertible. Thus
the face requirement is precisely

\[
 \sum_{e\in\partial F}x_{\tau(e)}w_e=0.
\tag{2}
\]

All bounded face cycles generate the cycle space of the actual plane
contact graph; bridges impose no additional cycle equation. Consequently
(2) for every exceptional face permits a well-defined vertex potential
`y`, up to translation, with

\[
 y_j-y_i=x_{\tau(ij)}(p_j-p_i).
\tag{3}
\]

Choose one base coordinate and integrate along contact paths. The exact
endpoint is then

\[
 p'_i=p_i+(\operatorname{Rot}(\theta)-I)y_i.
\tag{4}
\]

Its original contact vectors are the assigned rotated unit vectors, so
all original contacts are preserved. Assign `y_z=0` to every retained
contact isolate and keep its original position. No isolate is treated as
part of the affine-kernel core. Equations (1)--(4) do not establish the
other source inequalities; those are checked next.

## 2. Every finite pair inequality is quadratic in one parameter

For any full-source labelled pair, including pairs involving isolates, put

\[
 r=p_i-p_j,\quad s=y_i-y_j,\quad
 A=(r-s)\cdot s,\quad B=r\cdot Js,
 \qquad t=\tan(\theta/2).
\]

Direct expansion of `r'=(r-s)+Rot(theta)s` gives

\[
 |r'|^2-|r|^2={4t\over1+t^2}(B-tA).
\tag{5}
\]

For inactive lower pairs, with `ell=|r|^2-1>0`, require

\[
 \ell(1+t^2)+4tB-4t^2A>0.
\tag{6}
\]

For inactive upper pairs, with `u=D^2-|r|^2>0`, require

\[
 u(1+t^2)-4tB+4t^2A>0.
\tag{7}
\]

For **every actual old diameter pair**, require

\[
 t(B-tA)\le0,
\tag{8}
\]

and require strict inequality for at least one of them. Selected and
unselected old contacts already have `A=B=0` by (3); their exact unit
lengths are maintained. With (6)--(8), cardinality is unchanged, the
source remains triangle-free, every inactive upper pair is below `D`,
and the new actual diameter graph is a proper subset of the old one,
unless the whole diameter strictly decreases. Both outcomes contradict
the stated canonical lexicographic normalization.

For angle `pi`, check the separate endpoint `Rot=-I`: the pair change is
`-4A`. Its corresponding conditions are `ell-4A>0`, `u+4A>0` and `A>=0`
on old diameters, with at least one strict positive `A`.

For a given bit pattern and algebraic source coordinates, the complete
test is exact: isolate the real roots of these finitely many quadratics,
partition the real parameter line, and check the required signs on each
open interval and each allowed endpoint. Include the `pi` endpoint.
There is no uniform chart radius and no conversion of weighted energy
into maximum diameter. This is a decision procedure for this restricted
motion family, not a proof that every canonical source supplies a
beneficial pattern or parameter.

### 2.1 The active diameters impose a nonuniform amplitude gap

Choose a relative-interior normalized actual-row KKT stress, so every
actual diameter has positive coefficient `beta_h`. Equilibrium and (3)
give

\[
 \sum_h\beta_h B_h
 =\sum_e\alpha_e (p_i-p_j)\cdot J(y_i-y_j)=0.
\tag{8a}
\]

If every `B_h` vanished, the contact flex `u_i=Jy_i` would also preserve
all actual diameters to first order. Canonical Section 57 mixed rigidity
on the nonisolated core makes it Euclidean: `y_i=b+omega p_i`.
Comparing an actual contact difference with (3) gives `x_tau=omega` on
every train. Thus every bit is zero or every bit is one. For every
nonconstant closed pattern, the `B_h` are nonzero somewhere, and (8a)
forces both a positive and a negative `B_h`.

On the positive half-angle line `t>0`, each positive `B_h` makes (8)
impossible if `A_h<=0`. Otherwise it requires

\[
 t\ge\tau_+:=\max_{B_h>0}{B_h\over A_h}>0.
\tag{8b}
\]

On `t<0`, each negative `B_h` likewise requires `A_h>0` and

\[
 |t|\ge\tau_-:=\max_{B_h<0}{-B_h\over A_h}>0.
\tag{8c}
\]

These are necessary conditions; all the other old diameter, inactive
upper, and inactive lower quadratics must still hold. At angle `pi`,
the separate `A_h>=0` test above applies. There is no uniform lower
bound on either threshold as the source changes. This exact calculation
does not turn local active-diameter coordinates into prescribed feasible
shortening signs. A beneficial common-angle endpoint, if one exists,
must clear this finite source-dependent amplitude gap.

For the alternating six-point hexagon pattern in Section 5, every
`B_h=0`. Its scalar stress is PSD with affine kernel and rank three,
but its mixed contact/diameter matrix has rank eight rather than nine.
The new cyclotomic
[verifier](../../research/verify_target_c_collective_wall_guard_scope_2026_10_06.py)
checks these exact ranks. Thus the scalar affine kernel alone does not
supply the mixed-rigidity step in this argument.

## 3. Pentagons couple five train bits

A strictly convex triangle-free physical unit pentagon has no pair of
parallel side directions, as checked in canonical
`C-CONTACT-FACE-REGULARITY`. It has no proper nonempty balanced subset of
its side vectors: subsets of size one or four cannot balance; a balanced
two-element subset would be an opposite unit pair; a balanced three-element
subset would leave a balanced two-element complement. Hence (2) requires
all five of its terminal train bits to be equal.

These equalities propagate through every connected component of the
physical exceptional-face/train incidence graph. They need not leave a
linear number of independently selectable train groups. If a connected
pentagon component has `f_0` faces and `E_0` internal trains, canonical
reciprocal sparsity gives `E_0<=2f_0-3` for `f_0>=2`. Its number of
outside terminal incidences is

\[
 5f_0-2E_0\ge f_0+6.
\tag{9}
\]

Nevertheless one such component can use linearly many faces and outside
terminals while carrying only one common-angle Boolean bit. An incident
forbidden bit may propagate through that whole component. Counting its
first face/train incidence does not bound the number of suppressed train
proposals. The continuous canonical face chart still has many dimensions;
this common-angle binary restriction does not parameterize that chart.

## 4. A physical six-edge closure relation is not Horn

Use the six unit vectors of a regular hexagon, cyclically numbered
`0,...,5`. Each opposite pair balances, and each alternating triple
balances. Exactly ten of the 64 side-bit patterns satisfy (2).

The two valid patterns

\[
 a=(1,0,0,1,0,0),\qquad b=(1,0,1,0,1,0)
\]

have coordinatewise intersection

\[
 a\wedge b=(1,0,0,0,0,0),
\]

which fails closure. Every Horn model family is closed under this
intersection operation: if an implication or all-negative clause holds
in both assignments, it also holds in their intersection. The same is
true after existentially eliminating Horn auxiliary variables, by
intersecting witnesses. Thus no exact Horn encoding, even with auxiliary
variables, represents this full six-edge physical closure relation.

All ten patterns produce full unit-separated six-point contact
realizations at the small rational rotations checked by the verifier.
This is a physical-face regression, not an actual canonical source.
The regular hexagon as a whole lacks the canonical mixed-rigidity
premise. Its balanced alternating triple is a vector circuit; it is
not an equilateral triangle of source points. No C-I result is reopened.

Consequently zero-state validity of a coupled train system does not
justify importing the two-owner Horn normal form. A non-Horn closure
already occurs at a hexagon, spending one unit of `Q-f`. Even if such
faces are sublinear, their train equalities can connect to large pentagon
components; no bounded suppression multiplicity follows without proof.

## 5. A retained isolate changes the actual upper check

Integrate the regular-hexagon edge vectors from `p_0=(0,0)`. The source
positions include `p_2=(3/2,sqrt(3)/2)`, and its three core actual
diameters have squared length four. Select the alternating pattern `b`
above and take `t=1/10`. Equations (4)--(8) certify all 15 six-point
pairs: every old contact remains unit, all other lower pairs remain
strict, and every pair is strictly shorter than two. This is a finite
strict competitor for that feasible nonglobal hexagon.

Now retain the contact isolate `z=(-4,0)`, with `y_z=0`. The seven-point
source's unique actual diameter pair is `p_2,z`, of squared length 31.
The same train state increases it by

\[
 {20\sqrt3-18\over101}>0.
\tag{10}
\]

Thus the core-only finite endpoint fails the full-source upper requirement.
No contact isolate is deleted from the certificate. The seven-point
packet is also only feasible geometry, with no canonical KKT or global
optimality assertion. Its actual diameter endpoint is a contact isolate,
which also violates the canonical Section-57 requirement that actual
diameter endpoints lie in the positive-contact core. It demonstrates
why a general finite core endpoint must use the actual full-source pair
list in (7)--(8).

## 6. Verification and exact remaining task

[The verifier](../../research/verify_target_c_common_angle_train_endpoint_2026_10_06.py)
uses `Q(sqrt(3))`. It checks all 64 bit patterns, the ten closed patterns,
300 old-contact/inactive-lower checks, 420 exact quadratic pair identities
including the retained isolate, all 15 strict-competitor upper checks,
and the exact isolate diameter increase (10).

This supplies a correct finite test once an actual common-angle proposal
is given. It does not establish that the proposal population is large,
that the all-pentagon groups are independently useful, or that root
intervals survive the old-diameter cage. The next obligation is a
source-specific beneficial pattern with a nonempty certified parameter
interval, or a heterogeneous coupled train endpoint satisfying all source
pairs. The inactive-container branch separately needs a protected packet;
the one-vertex convex shield changes that packet region but does not
prove its universal capacity.
