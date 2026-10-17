<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e0c8c473f10c07eee02bdb74a475e27083315d5a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_universal_outer_supported_finite_manifold_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "bac6e0633ae90fd49840bf802594b7aacded07975d283f8c07b4be4219f6af53"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Erdos Problem #99 - universal finite integrability of outer-supported train modes

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** canonical strict convexity of bounded contact faces; audited stopped-train decomposition and no-bounded-return theorem; audited train-angle face-closure coordinates
**Claim class:** proof-only finite deformation theorem; theorem-state authority unchanged
**External literature:** none

## LEVEL I STATUS

`STILL OPEN`

The universal outer-supported kernel is not merely infinitesimal. Its private
outer-to-bounded blocks integrate to actual finite contact-preserving source families.
This holds for every bounded nonquadrilateral stopping face, with no residual or
pentagon hypothesis.

Let `O` be the complete stopped trains with both terminal occurrences on the actual
outer face and put `L_OO=|O|`. For each bounded nonquadrilateral contact face `F`, let
`J_F` be the complete stopped trains with one terminal occurrence on `F` and the other
on the actual outer face, and put `r_F=|J_F|`.

Then there is a smooth local family of full-source unit-separated realizations through
the given source whose train-angle parameter dimension is

\[
\boxed{d_{man}=L_{OO}+\sum_F(r_F-2)_+.}
\tag{UM.1}
\]

Its tangent train-coordinate space is exactly

\[
\boxed{\mathbb R^O\oplus\bigoplus_{F:r_F\ge3}\ker(C_F|_{J_F}),}
\tag{UM.2}
\]

where `C_F|_{J_F}` is the two-row first-order closure block of `F` on its private
outer-to-bounded columns. Every old unit contact remains exactly unit on the family,
and every old noncontact remains strictly longer than one after restricting to a
sufficiently small parameter neighborhood.

The exact outer occurrence ledger gives

\[
b=2L_{OO}+L_{OB},\qquad L_{OB}=\sum_F r_F,
\tag{UM.3}
\]

so

\[
\boxed{d_{man}\ge {b\over2}-f.}
\tag{UM.4}
\]

Modulo global Euclidean rotation, the genuinely non-Euclidean local dimension is at
least

\[
\boxed{d_{man}^{nonE}\ge {b\over2}-f-1.}
\tag{UM.5}
\]

Using `f<=Q` and `b+Q=2(q-k)` gives

\[
\boxed{d_{man}^{nonE}\ge {3b\over2}-2(q-k)-1.}
\tag{UM.6}
\]

Thus on a Type-II subsequence with

\[
{q-k\over D}\to t,\qquad {b-P_F\over D}\to\delta,
\qquad {P_F\over D}\to\pi,
\]

\[
\boxed{\liminf {d_{man}^{nonE}\over D}
\ge {3\pi\over2}-2t+{3\delta\over2}.}
\tag{UM.7}
\]

At the presently integrated hostile-audited `g=0.0021` Section-171 endpoint
`t=1.8212414379...`, the zero-detour coefficient is

\[
\boxed{1.0699061044\ldots .}
\tag{UM.8}
\]

The result does not claim diameter feasibility. It changes the remaining obstruction:
the actual diameter graph must make the maximum diameter function attain a local
minimum on an actual `Omega(D)`-dimensional contact-preserving manifold supported
entirely on trains touching the actual outer face.

---

## 1. Private outer-to-bounded train columns

Fix a bounded nonquadrilateral face `F`. Every train in `J_F` has exactly one bounded
nonquadrilateral terminal occurrence, namely its occurrence on `F`. Its other terminal
occurrence is on the actual outer face.

Choose one projective orientation `u_tau` for every complete train `tau`, and one fixed
occurrence sign `sigma_e in {+1,-1}` for each oriented physical contact edge `e`, so
at the original source

\[
p_y-p_x=\sigma_e u_{\tau(e)}.
\tag{UM.9}
\]

For `tau in J_F`, replace the train vector by

\[
u_\tau(\theta_\tau)=R_{\theta_\tau}u_\tau.
\tag{UM.10}
\]

Since these trains have no other bounded nonquadrilateral terminal, changing their
angles affects no other nonquadrilateral face-closure equation. Along every strict
rhombus, opposite sides belong to the same two trains and cancel identically for
arbitrary nearby train directions.

Hence the only finite closure equation involving the variables `theta_tau`,
`tau in J_F`, is

\[
\Phi_F(\theta):=\sum_{e\in\partial F}
\sigma_e u_{\tau(e)}(\theta_{\tau(e)})=0,
\tag{UM.11}
\]

with every nonselected train angle held fixed.

---

## 2. Every private block with at least three columns has rank two

Canonical C51 says every bounded contact face is a simple strictly convex unit-edge
polygon. Along the oriented boundary of a strictly convex polygon, the edge direction
turns strictly in one sense through a total angle `2pi`. Consequently a fixed
projective direction can occur on at most two boundary side occurrences: at most once
with either orientation.

The audited endpoint-fan/no-return package also says distinct terminal side
occurrences on one bounded stopping face belong to distinct complete trains. Therefore,
if `r_F>=3`, the selected boundary train vectors cannot all be projectively parallel.
At least two selected vectors are linearly independent.

Differentiating (UM.11) at the original source gives

\[
D\Phi_F(0)=C_F|_{J_F}
=(\pm Ju_{\tau_1}\ \cdots\ \pm Ju_{\tau_{r_F}}),
\tag{UM.12}
\]

and hence

\[
\boxed{\operatorname{rank}(C_F|_{J_F})=2\qquad(r_F\ge3).}
\tag{UM.13}
\]

The ordinary implicit-function theorem now gives a smooth local solution manifold of
train angles of dimension exactly `r_F-2`, tangent to
`ker(C_F|_{J_F})`.

For `r_F<=2` we freeze those outer-to-bounded train angles in this construction and
claim no local parameter from `F`.

---

## 3. Outer-to-outer trains are exact free angular parameters

A train in `O` has no bounded nonquadrilateral terminal occurrence. Its vector
therefore appears in no equation (UM.11). It may be rotated independently through a
small angle.

Every strict-rhombus boundary still closes identically because the two occurrences of
each train vector cancel with opposite signs. Thus each outer-to-outer train supplies
one exact finite angular parameter, not merely one infinitesimal zero column.

---

## 4. The nonlinear closure system is a direct product

If `F` and `F'` are distinct bounded nonquadrilateral faces, then

\[
J_F\cap J_{F'}=\varnothing.
\tag{UM.14}
\]

Indeed an outer-to-bounded train has exactly one bounded terminal occurrence. Hence the
variables occurring in `Phi_F` and `Phi_F'` are disjoint.

The simultaneous finite closure system on all selected outer-supported variables is
therefore the direct product of one unconstrained angular coordinate for every train in
`O` and one two-component equation `Phi_F=0` for every face with `r_F>=3`.
Applying the implicit-function theorem block by block proves the parameter count
(UM.1) and tangent decomposition (UM.2).

---

## 5. Integrate train vectors to source coordinates

For every physical oriented contact edge define its deformed edge vector by

\[
r_e(\theta)=\sigma_e u_{\tau(e)}(\theta_{\tau(e)}).
\tag{UM.15}
\]

All bounded face boundaries have zero vector sum:

- strict rhombi close identically for arbitrary nearby train directions;
- a selected nonquadrilateral face closes by its equation `Phi_F=0`;
- an unselected nonquadrilateral face uses only fixed train directions and retains its
  original closure.

The oriented bounded-face cycles span the real cycle space of a connected plane graph,
including in the presence of bridges and articulation vertices. Therefore the edge
one-form (UM.15) has zero sum around every contact cycle.

Fix one positive-contact-core root vertex. Define every other core vertex by summing
the deformed contact-edge vectors along an arbitrary contact path from the root. Cycle
closure makes the result path-independent. Every old contact is realized by a unit
vector, so its length remains exactly one.

Contact-isolated source points are retained and held fixed. Because the full source is
finite and every old noncontact has strictly positive separation slack above one, all
old noncontacts remain strictly longer than one after shrinking the parameter
neighborhood. Thus the construction gives legitimate full-source unit-separated
configurations with the same contact graph.

No diameter estimate is used in this construction.

---

## 6. Dimension lower bound from outer occurrences

For every integer `r>=0`,

\[
(r-2)_+\ge r-2,
\]

and the left side is nonnegative. Therefore

\[
\boxed{
\sum_F(r_F-2)_+\ge (L_{OB}-2f)_+.
}
\tag{UM.16}
\]

Combining (UM.1) with the exact outer occurrence ledger gives

\[
d_{man}
\ge L_{OO}+(L_{OB}-2f)_+.
\tag{UM.17}
\]

For nonnegative `L_OB`,

\[
(L_{OB}-2f)_+\ge {L_{OB}\over2}-f.
\tag{UM.18}
\]

Indeed, if `L_OB<=2f`, the right side is nonpositive; if `L_OB>=2f`,
the difference between the two sides is `L_OB/2-f>=0`. Hence

\[
\boxed{
d_{man}\ge L_{OO}+{L_{OB}\over2}-f={b\over2}-f.
}
\tag{UM.19}
\]

Global rotation is one tangent direction whenever it lies in the selected support.
Quotienting it costs at most one dimension, proving (UM.5).

Finally `f<=Q` and `b+Q=2(q-k)` give (UM.6), and division by `D` gives (UM.7).

---

## 7. Frontier effect

The universal outer-supported theorem gave more than `1.0699D-o(D)` non-Euclidean
**infinitesimal** outer-supported contact flexes at the current low-`t` endpoint. The
present theorem upgrades the same support class to an actual finite contact manifold.
The obstruction is therefore not singular first-order flexibility.

For every finite canonical minimizer, the diameter function

\[
\mathcal D(\theta)=\max_{x,y}|p_x(\theta)-p_y(\theta)|
\]

has a local minimum at the original parameter on this manifold. Canonical mixed
rigidity says the active-diameter derivative map is injective after quotienting the
Euclidean rotation direction, while positive KKT stationarity gives a positive left
kernel. Pure row count is still insufficient.

The remaining closing theorem is explicitly geometric: use the circular order and
crossing structure of the near-extremal Woodall diameter graph to show that its length
functions cannot simultaneously support a local minimum on this large outer-supported
manifold. Equivalently, one needs a support-sensitive diameter-locking or finite descent
theorem, not another contact-flex count.

---

## 8. Scope audit

- The finite theorem uses every bounded nonquadrilateral stopping face, not only good
  pentagons.
- Strict convexity is canonical C51; it forces rank two for any private block with at
  least three selected sides.
- Distinct terminal side occurrences on one bounded face belong to distinct complete
  trains by the audited endpoint-fan/no-return package.
- Outer-to-bounded columns are private because their other terminal occurrence is on
  the actual outer face.
- Outer-to-outer train angles are exact finite parameters because they enter no bounded
  nonquadrilateral closure equation.
- The finite parameter radius can depend on the source and may shrink along an
  asymptotic sequence.
- Contact-isolated source points remain in the full source and are held fixed.
- Diameter feasibility is not claimed. No exact unit triangle or strict sub-`D`
  competitor is produced.
- C-II and Level I remain open.
