<!-- theorem-state: {"artifact_id":"ART-7383567A6F48","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- finite subset reflections and the signed gap obstruction

`subset reflection -> exact full-source contact preservation and finite diameter
signs -> active TWO-SIGN or inactive slack barrier -> strict competitor only after
the surviving source constraints are eliminated`

Date: 2026-10-02. Starting commit:
`fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`.
State version: `2026-09-14.audit.51`.
Branch: `swarm/root/c2-finite-release-20261002`.
Mission: test finite moves beyond phase permutations in the nonconstant-phase
open-cell shore, then attack their active-diameter obstruction.

Classification: **proved candidate awaiting independent audit** for Sections 2--6;
**conditional** for their application to the unpromoted train extraction;
**regression** for Section 7. Artifact lifecycle is unreviewed. No canonical
promotion is requested. **Level I and C-II remain open.**

## 1. Authority, dependencies, and the exact implication chain

The canonical source is contact-minimal, then diameter-pair-minimal, with positive
relative-interior multipliers on every actual contact and diameter. Every source
point is retained, including contact isolates. The authority is
[C-I normalization](../targets/target-c/56-ci-restored-frontier.md) and the
[current C-II ledger](../targets/target-c/CURRENT.md). No full-source extension
of the core-only [ZR/ZF theorem](../targets/target-c/57-zr-zf-rigidity-audit.md)
is used.

The geometric coordinate inputs remain unpromoted:

- [laminar exact train shear](../../research/target_c_laminar_multitrain_interval_shear_2026-09-15.md),
  including actual contact cutsets and layers;
- [exact multishear hostile audit](../../research/target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md),
  especially its signed KKT cut resultant;
- [open witness-cell extraction](target_c_local_witness_cell_2026-10-01.md);
- [arbitrary block transposition](target_c_open_cell_block_transposition_2026-10-01.md).

The new proofs below require only the expressly stated cutset and force identities.
They neither promote nor re-audit the extraction ancestry. PR
[608](https://github.com/1337isnot1337/e-99/pull/608) contains a distinct cyclic
permutation move; no result from it is a premise here.

The intended chain is

```
nonconstant phases on actual ordered O-O cuts
 -> reflect a selected subset about its resultant direction
 -> preserve every old contact and fix both exterior layers exactly
 -> obtain a strictly shortening old diameter from positive KKT work
 -> either another old diameter lengthens or an inactive source pair blocks
 -> Level I only if these obstacles and every other C-II branch are excluded.
```

The proposed immediate closure, that changing phases beyond permutations removes
TWO-SIGN using diameter geometry and cut balances alone, fails by Section 7.
This is a failure of that scoped implication, not a counterexample to a source
theorem with the missing contact/KKT/global hypotheses supplied.

## 2. An exact finite move beyond permutations

Let the cuts be indexed `1,...,m`, and the physical layers `0,...,m`.
Contact edges crossing cut `i`, oriented from layer `i-1` toward layer `i`,
have the same unit vector `u_i`. No other contact crosses that cut. Thus an old
contact is either internal to a layer or crosses exactly one selected cut.

All coherently lifted directions lie in an open actual-diameter-direction cell
`J`. Their real angular span is less than `pi/2`.

Choose a subset `I` of `k>=2` cuts whose directions are not all equal. Put

\[
U=\sum_{i\in I}u_i,\qquad e=U/|U|,\qquad w=Je,
\qquad a_i=u_i\cdot w.
\tag{1}
\]

The narrow span ensures `U!=0`; its direction is strictly between the smallest
and largest selected angles. Reflect the selected contact vectors across the
line in direction `e`:

\[
u'_i=u_i-2a_iw\quad(i\in I),\qquad u'_i=u_i\quad(i\notin I).
\tag{2}
\]

Assign the scalar prefix translations

\[
x_j=-2\sum_{i\in I,\ i\le j}a_i,\qquad X_j=x_jw,
\qquad j=0,\ldots,m.
\tag{3}
\]

Translate **every** source point in layer `j` by `X_j`. Since
`sum_{i in I}a_i=U dot w=0`,

\[
X_0=X_m=0.
\tag{4}
\]

### Theorem 1: exact contacts, fixed exterior, and displacement bound

The finite placement (3) preserves every old unit contact exactly and fixes both
exterior layers. If `W<pi/2` is the angular span of the selected directions, every
point displacement and every pair-relative displacement is at most

\[
\boxed{\eta_I:=\sum_{i\in I}|a_i|\le k\sin W.}
\tag{5}
\]

**Proof.** A selected cut contact becomes
`u_i+(X_i-X_{i-1})=u_i-2a_iw=u'_i`, which has norm one. Every other old contact
is unchanged. Equation (4) proves the exterior assertion.

Write `T=sum_{a_i>0}a_i=-sum_{a_i<0}a_i`. The sum of any subset of the `a_i`
lies between `-T` and `T`. Every prefix or interval in (3) is such a subset.
Consequently its displacement has norm at most `2T=sum |a_i|`. The mean angle
lies between the selected extreme angles, so `|a_i|<=sin W`. This proves (5).
The full finite endpoint need not be unit-separated: inactive pairs have not
yet been checked. QED.

For `k=2`, reflecting across the vector sum exchanges the two unit directions,
so Theorem 1 recovers the block transposition. For `k>=3`, the new vectors need
not be a permutation of the old vectors. Section 8 gives an exact three-cut
example. It would therefore be incorrect to dismiss every move (3) as a
permutation of the phase word.

## 3. Exact non-grazing with a linear, rather than quadratic, size threshold

Let `mu=arg e`, and let the selected extreme angles be `alpha<beta`. Put

\[
g=\min(\mu-\alpha,\beta-\mu)>0.
\tag{6}
\]

Both selected extremes lie strictly inside the empty cell `J`. Every old actual
diameter vector `r`, with `|r|=D`, therefore satisfies

\[
\boxed{|r\cdot w|>D\sin g.}
\tag{7}
\]

This follows from projective angular distance: no actual diameter direction
lies between `alpha` and `beta`, and the nearest direction outside `J` is
strictly farther from `mu` than `g`.

### Lemma 2: the balanced-prefix bound

\[
\boxed{\eta_I\le 2(k-1)\sin g.}
\tag{8}
\]

**Proof.** If `g=mu-alpha`, every negative `a_i` has magnitude at most `sin g`.
There are at most `k-1` negative terms, because a nonconstant selected family has
at least one positive term. Thus `T<= (k-1)sin g`. If `g=beta-mu`, apply the
same argument to the positive terms. In either case `eta_I=2T`, proving (8).
QED.

### Theorem 3: every moved actual diameter has its full finite work sign

Assume

\[
\boxed{D\ge k-1.}
\tag{9}
\]

For a diameter whose endpoints have layers `a,b`, its relative displacement
is `Delta=(x_b-x_a)w=lambda w`. If `lambda!=0`, then

\[
\boxed{
\operatorname{sgn}(|r+\Delta|^2-D^2)
=\operatorname{sgn}(r\cdot\Delta)\ne0.
}
\tag{10}
\]

**Proof.** Equations (7)--(9) give

\[
2|r\cdot w|>2D\sin g\ge2(k-1)\sin g\ge|\lambda|.
\]

Hence `2r dot Delta+|Delta|^2=lambda(2r dot w+lambda)` has the sign of
`lambda(r dot w)`. Both factors determining that sign are nonzero. If
`lambda=0`, the diameter is exactly unchanged. QED.

The reflected directions are allowed to leave the original phase range or the
witness cell. Only the **old** selected extremes and old actual diameters enter
(7). Neither a new-direction gap nor an interpolating feasible motion was used.

For fixed `k`, Section-90 width `W<=4K/D` makes (5) inverse-diameter. Theorem 3
also permits a reflected subset with as many as `floor(D)+1` cuts. Its displacement
bound may then be order one, so it must not be called an inverse-diameter move.

## 4. KKT and the source-level finite fork

Let `A_i>0` be the actual positive contact mass on cut `i`. With arbitrary global
diameter orientations and signed cut incidences `sigma_hi`, the audited identity is

\[
A_i u_i=\sum_h\beta_h\sigma_{hi}r_h,\qquad\beta_h>0.
\tag{11}
\]

The relative displacement is `Delta_h=sum_i sigma_hi(u'_i-u_i)`. Therefore

\[
\boxed{
\sum_h\beta_h r_h\cdot\Delta_h
=-2\sum_{i\in I}A_i a_i^2<0.
}
\tag{12}
\]

The inequality is strict because some selected direction differs from `e` and
every `A_i` is positive. By Theorem 3, at least one old actual diameter strictly
shortens at the full reflected endpoint.

Either a different old actual diameter strictly lengthens, or every moved old
diameter strictly shortens. In the latter case, suppose all previously strict
pairs remained strictly between `1` and `D`. All old contacts are still unit,
and no new contact or diameter is created. If an unchanged diameter remains,
the placement is a diameter-`D` global minimizer with unchanged contact count
and fewer diameter pairs. If none remains, its diameter is below `D`. Both
contradict the canonical choice.

Thus the second alternative forces a previously strict pair with

\[
\boxed{1<|xy|\le1+\eta_I\quad\hbox{or}\quad D-\eta_I\le|xy|<D.}
\tag{13}
\]

Only the triangle inequality and (5) enter the slack conclusion. This is an
endpoint comparison; contact-preserving interpolation and endpoint feasibility
are not asserted. A newly unit pair is included in the lower witness even when
the endpoint remains unit-separated, because it would change contact count.

## 5. Complete classification of finite motions along one axis

### Theorem 4

Fix a unit axis `w`, and translate each layer by `x_j w`, with `x_0=x_m=0`.
If every old contact is preserved exactly, the motion is a subset reflection
of the form (1)--(3), unless it is the zero motion.

**Proof.** Put `d_i=x_i-x_{i-1}`. On a cut contact,

\[
|u_i+d_iw|^2=1
\quad\Longleftrightarrow\quad d_i(d_i+2u_i\cdot w)=0.
\tag{14}
\]

Consequently each cut either has `d_i=0` or is reflected, with
`d_i=-2u_i dot w`. Let `I` consist of the genuinely changed cuts. The exterior
condition gives `sum_{i in I}u_i dot w=0`. Their nonzero sum `U` is perpendicular
to `w`, so their reflection axis is exactly the direction of `U`; changing the
sign of `w` leaves the placement unchanged. Taking prefixes proves (3).
If all selected directions are equal, the balance forces every increment zero.
This is why a nonzero motion requires at least two distinct phases. QED.

Theorem 4 classifies contact-preserving **layer translations along one axis**,
with fixed exterior. It does not classify all finite source motions, rotations
of layers, two-axis motions, or changes that open or replace old contacts.

## 6. The directed gap graph can force TWO-SIGN for the entire class

For the axis `w=Je` of a reflection, orient each old diameter from its lower layer
`a` to its higher layer `b`. If `a=b`, discard it. The empty cell makes
`r_h dot w` nonzero. Define a directed graph `G_J` on layers `0,...,m`:

- use `a -> b` if `r_h dot w>0`;
- use `b -> a` if `r_h dot w<0`.

The direction is independent of the choice of `e` inside `J`, because no old
diameter can cross a transverse zero there. Parallel graph edges are retained.

For a scalar layer potential `x`, absence of positive work is exactly

\[
x_{\rm head}\le x_{\rm tail}\quad\text{on every directed edge.}
\tag{15}
\]

### Theorem 5: strong connectivity prevents every nonzero admissible reflection

If `G_J` is strongly connected and `D>=k-1`, every nonzero `k`-cut reflection
has at least one strictly shortening and at least one strictly lengthening old
actual diameter. In particular no inactive blocker need be invoked.

**Proof.** If no diameter has positive work, (15) along directed paths makes
`x` constant on a strongly connected graph. Since `x_0=0`, it is zero, contrary
to a nonzero reflection. Thus some diameter has positive work. Applying the
same argument to `-x` gives negative work as well. Theorem 3 converts both
work signs to strict finite signs. This argument does not require KKT weights.
QED.

### Corollary 5.1: opening contacts does not rescue a motion along one axis

If `G_J` is strongly connected, the only layer translation `X_j=x_j w` that
does not lengthen any old actual diameter is a common translation. This holds
at every finite amplitude, without preserving old contacts, without a phase
reflection, and without the condition `D>=k-1`.

**Proof.** On a diameter edge with relative displacement `lambda w`,
nonlengthening gives `2lambda(r_h dot w)+lambda^2<=0`, hence
`lambda(r_h dot w)<=0`. These are exactly (15). Strong connectivity makes
`x` constant. If either exterior layer is fixed, that constant is zero. QED.

This exhausts a broader closing mechanism than reflections: a nonzero motion
along this axis cannot be repaired merely by allowing some old contacts to open.
Two-axis motions or a changed action on the individual points of one layer
remain outside the corollary.

More generally, (15) makes `x` constant on each strongly connected component,
with nonincreasing values along the condensation graph. An ONE-SIGN move must
therefore move whole such components compatibly. This is a precise restriction,
not a proof that such a reflected subset exists.

In an exact-phase cell, positive KKT transverse balance and gap connectivity
give strong connectivity: the signed edge flows form a positive circulation,
every edge belongs to a directed cycle, and the underlying graph is connected.
The nonconstant-phase analogue is not assumed. Section 7 instead constructs
an exact nonconstant geometric/aggregate-force example where strong connectivity
still holds.

There is also a useful limit on two-shore rescue. A reflected motion fixes layers
`0,m` on its shore. An actual diameter with both endpoints internal on shore A
has endpoints on the two extreme B rails under the current four-host hypothesis;
it is therefore unchanged by every fixed-exterior B reflection. Any strict A
lengthening on such a bar survives adding the B reflection. This follows from
the two endpoint displacements, without a simultaneous feasibility assumption.
It does not cover bars meeting an extreme A layer, and it does not close either
shore. The four-host theorem is an additional unpromoted hypothesis for this
last observation.

## 7. Exact nonconstant regression to a geometry/aggregate-force closure

For `m>=2`, set `D=100m` and

\[
t_j=\frac{m-j+1}{10m},\qquad
c_j=\frac{1-t_j^2}{1+t_j^2},\qquad
s_j=\frac{2t_j}{1+t_j^2}.
\]

The source consists of

\[
v=(0,0),\qquad p_j=D(c_j,s_j),\qquad n_j=D(c_j,-s_j),
\quad j=1,\ldots,m.
\tag{16}
\]

Its actual diameters are exactly `vp_j,vn_j`. All other pairs have length
strictly between `1` and `D`. Indeed `0<t_j<=1/10` makes the neighbor arc
aperture less than `pi/3`, so its chords are below `D`; same-sign distances are
at least `20/1.01>1`, and opposite-sign distances are at least
`4D t_m/(1+t_m^2)>39`. The source has no unit contacts.

Give `v` layer zero and `p_j,n_j` layer `j`. The convex cyclic order is
`v,n_1,...,n_m,p_m,...,p_1`; disjoint proper crosscuts can realize the nested
layer shores. The two innermost star rays have full support and bound the empty
direction cell around the positive horizontal axis.

Assign distinct rational unit directions

\[
z_i=\frac{i}{10^6m^3},\qquad
u_i=\left(\frac{1-z_i^2}{1+z_i^2},\frac{2z_i}{1+z_i^2}\right),
\qquad F_i=(m-i+1)u_i,
\quad F_{m+1}=0.
\tag{17}
\]

All these directions lie strictly inside that same empty diameter cell. Put
`V_j=F_j-F_{j+1}` and assign positive diameter weights

\[
\gamma_j^\pm=\frac12\left(\frac{V_{j,x}}{Dc_j}
\ \pm\frac{V_{j,y}}{Ds_j}\right).
\tag{18}
\]

These weights are strictly positive. To check this uniformly, `z_i<=1/(10^6m^2)`
gives `|V_{j,x}-1|<=4/(10^{12}m^3)` and
`|V_{j,y}|<=4/(10^6m)`; also `c_j>=99/101` and
`s_j>=1/(6m)`. Hence `|V_{j,y}|/s_j<24/10^6`, whereas
`V_{j,x}/c_j>0.99`. This proves positivity without a numerical sign test.

For every cut `i`, the exact telescope gives

\[
\sum_{j\ge i}(\gamma_j^+p_j+\gamma_j^-n_j)
=\sum_{j\ge i}V_j=F_i=(m-i+1)u_i.
\tag{19}
\]

Thus the complete cut-resultant identity has positive cut masses and positive
diameter coefficients. Normalizing all weights by their diameter-weight sum
preserves (19).

The nonconstant diameter derivative matrix has rank `m`: choose the positive
star row with support `[1,j]` for each `j`. Its `j`th entry
`p_j dot Ju_j` is nonzero, and the resulting `m`-by-`m` interval matrix is
triangular with nonzero diagonal. The positive weights in (18) annihilate its
transverse virtual work by (19).

The signed gap graph has both `0 -> j` and `j -> 0` for every `j`, so it is
strongly connected. Every nonzero subset reflection has TWO-SIGN. Its selected
cut count is at most `m`, whereas `D=100m`, so Theorem 3 applies to all subsets.
The exact verifier checks every subset for `m<=8` and selected subsets in the
larger packets.

Even the restricted scalar stress test survives. With
`B_j=gamma_j^++gamma_j^-=V_{j,x}/(Dc_j)<2/D`, the formal cut quadratic form is

\[
Q=\operatorname{diag}(m,m-1,\ldots,1)
-\sum_jB_j1_{[1,j]}1_{[1,j]}^T\succ0.
\tag{20}
\]

Indeed Cauchy--Schwarz bounds each squared prefix by `j` times its coordinate
square sum. At coordinate `i`, the subtracted coefficient is at most
`sum_{j>=i}2j/D<= (2m/D)(m-i+1)`, only `1/50` of its diagonal. The normalized
form has the same sign.

**Encoded and omitted hypotheses.** This regression supplies actual Euclidean
diameters and their thrackle geometry, unit separation, physical ordered layer
shores, a common witness star, an empty diameter-direction cell, distinct phases,
positive aggregate cut balance, full derivative rank, and the restricted
positive quadratic form. It does **not** supply actual unit-contact cutsets,
vertex KKT equilibrium, a full scalar source stress, complete transverse trains,
quadratic population, near-disk geometry, or global optimality. Its star degree
also fails the large-source star bound when `m` is linear in `D`.

The missing contact hypotheses are decisive: the source has no contacts at all,
so (19) is only an assigned cut balance, not a source KKT stress. A unit-spaced
line on `2m+1` points has diameter `2m<D`, proving that (16) is not globally
optimal. The example is neither a Level I disproof nor a counterexample to a
fully hypothesized canonical source theorem.

### 7.1 Positive cut balance and full rank do not force strong connectivity

There is a complementary exact five-point example. Take (16) at `m=2`, but
give `n_1` layer two instead of layer one. The cyclic layer labels are now
`0,2,2,2,1`, so the nested shores are still proper boundary intervals. Write

\[
u_1=\operatorname{circle}(10^{-6}),\quad u_2=(1,0),\qquad
f=u_{1,x}-u_{1,y}c_1/s_1>0.
\tag{21}
\]

Here `circle(z)=((1-z^2)/(1+z^2),2z/(1+z^2))`. Give `vp_1` the positive weight

\[
b_1=u_{1,y}/(Ds_1).
\]

It has only the first cut in its support. All other diameters have full support.
Choose `d=f/(100D)>0` as the weight of `vn_1`, and put `T=f(1,0)-d n_1`.
Give `vp_2,vn_2` the respective weights

\[
b_2^\pm=\frac12(T_x/(Dc_2)\pm T_y/(Ds_2)).
\tag{22}
\]

Both are positive: `s_1/s_2<2`, `c_2>0.99`, and `c_1<1` give
`T_x/(Dc_2)>0.99f/D`, whereas `T_y/(Ds_2)<f/(50D)`.

The cut resultants are exactly

\[
R_2=d n_1+b_2^+p_2+b_2^-n_2=f u_2,
\qquad R_1=R_2+b_1p_1=u_1.
\tag{23}
\]

Thus both cut masses and all actual-diameter weights are positive; both unit
directions lie in the empty star cell; and the derivative matrix has rank two
by its singleton `vp_1` row and a full-support row. Nevertheless the signed
gap graph has `0 -> 1`, `0 -> 2`, and `2 -> 0`, with no edge leaving vertex one.
It is connected but not strongly connected. The exact-phase positive-circulation
argument cannot be imported into nonconstant phase.

The two-cut reflection translates only layer one by `u_2-u_1`. Its only moving
old diameter, `vp_1`, strictly shortens. The exact verifier checks that every
old inactive pair remains strictly between `1` and `D`; the other three old
diameters remain at `D`. The five-point source really has an ONE-SIGN endpoint
with fewer diameter pairs. Again it has no contacts or vertex KKT and is beaten
by a diameter-four unit line. It violates global/secondary optimality, not the
source-level fork. Its restricted cut quadratic form is also positive, as
checked by the coefficientwise Cauchy bound in the verifier.

The two regression families identify distinct surviving alternatives. Strong
connectivity cannot be assumed from nonconstant cut balance and rank; absence
of strong connectivity cannot be discarded using the geometric hypotheses alone.

## 8. Computation and the next attack

The analytic proofs do not depend on computation. The exact verifier
[verify_target_c_subset_reflections_2026_10_02.py](../../research/verify_target_c_subset_reflections_2026_10_02.py)
uses rational arithmetic. It checks every source pair in the regression,
positivity and every coordinate of (19), matrix rank, exact reflection/contact
identities, fixed exterior, both strict diameter signs, and a rational three-cut
reflection whose new unit directions are not a permutation of the original
directions. Its encoded and omitted hypotheses are also recorded in
[research/README.md](../../research/README.md).

The new finite class is broader than swaps and cyclic permutations, but does
not bypass the active diameter obstruction. The concrete next attack is to
use the **actual contact co-embedding and the transverse complete shore** to
exclude or release a strongly connected signed gap block, or to permit
two-axis/contact-opening motions. An internal-to-internal diameter cannot be
rescued by a fixed-exterior opposite-shore reflection, as Section 6 shows.

The bounded contact graph, full vertex equilibrium, and simultaneous strict
pair constraints must enter that argument. Repeating a scalar potential move
on a strongly connected block cannot succeed. The open nonconstant, exact-phase,
split-star O-O, inactive-interface, macroscopic inactive-container/exterior-cap,
and higher-defect full-core branches remain explicit. No finite witness,
numerical search, or formal stress assignment proves any global minimizer exists.
