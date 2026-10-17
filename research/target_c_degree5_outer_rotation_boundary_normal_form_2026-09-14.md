<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b634ff5a405c57708488456c410cd59afc1a30a6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_degree5_outer_rotation_boundary_normal_form_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e8cf526e1d791ca1831604d74dc870a0ec513a3c71b692f30bd5430f2bc64e37"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - degree-five flat-pentagon rotation boundary normal form

**Date:** 2026-09-14
**Target:** weighted hidden-rank minimax equality branch
**Dependencies:** audited train-angle closure coordinates; audited bounded-face endpoint fan; mixed infinitesimal rigidity; positive relative-interior KKT diameter weights
**Status:** proof-only structural theorem; C-II remains open

## 1. Statement

Let `P` be a bounded pentagonal contact face whose five boundary train variables are all private outer-to-flat trains. Label its cyclically oriented unit side vectors

\[
e_i=p_{i+1}-p_i,\qquad i\in\mathbb Z/5\mathbb Z.
\]

Every incident complete train `tau_i` has its other terminal occurrence on the actual outer face. The audited bounded-face endpoint-fan theorem says the five `tau_i` are pairwise noncrossing.

Set

\[
\omega_{\tau_i}=1\quad(i=1,\ldots,5),
\qquad
\omega_\tau=0\quad\text{for every other train}.
\tag{DR.1}
\]

Then (DR.1) is an actual contact-flex train-rate vector. Call the corresponding flex `v_P`, modulo translation.

Traverse the actual outer-face walk. Between consecutive outer terminal occurrences of the five selected trains, every traversed contact edge has train rate zero. Hence `v_P` is constant on every resulting outer sector. At the outer terminal of `tau_i`, the velocity jump is

\[
\boxed{-J e_i}
\tag{DR.2}
\]

with the sign fixed by the opposite boundary orientations at the two ends of one train. The five selected terminal occurrences may appear in an arbitrary cyclic permutation if other bounded holes intervene; no order-preservation assertion is needed.

Consequently, after subtracting one translation, every outer-sector velocity is of the form

\[
\boxed{V_S=-J\sum_{i\in S}e_i}
\tag{DR.3}
\]

for a subset `S` obtained as an initial segment of the five selected outer occurrences. In particular every difference of two outer-sector velocities is

\[
\boxed{V_T-V_S=-J w,
\qquad
w=\sum_{i\in I}e_i}
\tag{DR.4}
\]

for some subset `I subset {1,...,5}`.

If an active diameter edge `h=xy` has endpoints in sectors with velocity difference `-Jw`, its radial first-variation numerator is

\[
\boxed{
(p_y-p_x)\cdot(v_P(y)-v_P(x))
=-(p_y-p_x)\cdot Jw.
}
\tag{DR.5}
\]

Thus every diameter derivative of the degree-five hidden-null mode is an oriented-area determinant between the diameter vector and a subset sum of the five pentagon sides.

The mode is non-Euclidean in the asymptotic Type-II branch. Mixed rigidity makes its diameter derivative vector nonzero, while relative-interior KKT stationarity gives positive-weighted sum zero. Therefore

\[
\boxed{
\exists h_+,h_-\in H:\quad
\dot d_{h_+}(v_P)>0,
\qquad
\dot d_{h_-}(v_P)<0.
}
\tag{DR.6}
\]

This is the degree-five analogue of two-sided bracing for one outer-to-outer train shear.

## 2. Contact-flex proof

The five selected columns occur only in the two closure rows of `P`: their other endpoints are outer and contribute no bounded-face row. On `P`,

\[
\sum_{i=1}^5\omega_{\tau_i}Je_i
=J\sum_{i=1}^5e_i=0.
\]

Every other bounded-face row sees zero selected coordinates. Hence (DR.1) lies in `ker C_face`, and the audited train-angle/contact-flex isomorphism produces `v_P`.

For a sufficiently flat pentagon this is exactly the one-dimensional hidden-null direction from the four-row closure-plus-hidden-chord calculation: common angular rate is rigid rotation of the face boundary, so every internal pentagon chord has zero radial first variation.

## 3. Outer boundary trace without an order assumption

For one complete train, opposite strict-rhombus sides propagate one projective contact direction from one terminal occurrence to the other. If all bounded and outer face boundaries are oriented consistently, the two terminal boundary occurrences of a bounded-to-outer train have opposite oriented vectors. Therefore the outer terminal of `tau_i` contributes `-e_i` when the `P` occurrence contributes `e_i`.

Along an oriented contact edge `r`, train rate `omega` gives velocity increment `omega Jr`. Every outer edge except the five selected terminal occurrences has rate zero under (DR.1), while the selected occurrence of `tau_i` contributes `-Je_i`. This proves (DR.2)--(DR.4).

No claim is made that the outer cyclic order of the five terminals equals their order around `P`. Pairwise noncrossing spokes in a multiply holed carrier need not justify that stronger statement. Repeated outer-face vertices likewise cause no problem: a physical vertex has one velocity, so repetitions only identify some of the step values.

## 4. Diameter derivative and two-sided bracing

Actual diameter endpoints are loaded extreme vertices of the positive core and lie on its outer face. If `x,y` have outer-sector velocity difference `-Jw`, differentiating squared distance gives

\[
{1\over2}{d\over dt}|p_y-p_x|^2
=(p_y-p_x)\cdot(-Jw),
\]

which is (DR.5).

The train-rate vector (DR.1) is not the all-trains rotation vector once the complete train system has more than these five trains; in the asymptotic Type-II branch `T=Theta(D)`. Thus `v_P` is non-Euclidean modulo translations and rotation. Canonical mixed rigidity implies that some active diameter derivative is nonzero.

For a relative-interior KKT stress every actual diameter multiplier satisfies `beta_h>0`, and stationarity gives

\[
\sum_{h\in H}\beta_h\dot d_h(v_P)=0.
\]

A nonzero vector with strictly positive weighted sum zero contains both signs, proving (DR.6).

## 5. Flat endpoint finite direction alphabet

At the flat trapezoid limit take

\[
e_1=e_2=(1,0),
\quad e_3=(-1/2,\sqrt3/2),
\quad e_4=(-1,0),
\quad e_5=(-1/2,-\sqrt3/2).
\]

Every subset sum `w=sum_{i in I}e_i` has vertical coordinate in `{-sqrt3/2,0,sqrt3/2}` and half-integral horizontal coordinate. Direct finite inspection gives, for every nonzero subset sum, projective direction in

\[
\boxed{\{0,\ \pm\pi/6,\ \pm\pi/3\}.}
\tag{DR.7}
\]

For sufficiently flat actual pentagons the corresponding nonzero directions lie in an `o(1)` neighborhood of this five-direction alphabet. Therefore each degree-five blocking column has a finite limiting sign geometry even without controlling the order of its five outer terminals.

## 6. Frontier

Near equality in the weighted hidden-rank minimax theorem forces a linear population of degree-five receiving pentagons, one common-rotation mode per such face. The present normal form says these are not arbitrary hidden-null columns: each is a five-step outer-boundary motion, and every diameter row evaluates it through one of finitely many limiting subset-sum directions.

What remains is global. A single diameter edge can brace many face-rotation modes, so two-sided bracing alone does not yield a row count. The next useful theorem must exploit the straight-line-thrackle order of `H` together with the five-step/subset-sum structure to force either a rank defect or a nonzero combination with all diameter derivatives nonpositive.

**Disposition:** hardened proof-only normal form and two-sided bracing. No C-II closure claim.