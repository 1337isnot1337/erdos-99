# Target C-II — truncation-free outer currency and full endpoint activation from FREE pair reuse

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; strengthens the proof-only half-plus outer-currency/contact-activation note  
**Scope:** `PAIR-REUSE` for the two extreme all-inactive FREE modules  
**Dependencies:** two-normal lower directional defect; two-sided outer-face localization; OP outer-pocket Oler absorption  
**Certificate:** `research/verify_target_c_halfplus_outer_charge_full_activation_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding half-plus note spends a near-unit parity matching against outer-pocket
capacity and activates a sixth of one chosen endpoint set by a planar-coloring
argument. Both losses are avoidable for different reasons.

First, the outer-pocket charge does not need parity thinning or the `J/D` lower-edge
truncation at all. The directional-defect theorem already forces one activation
ancestry to contain more than `D` lower gates, and activation times make all vertices
of that ancestry distinct old source points. Two-sided localization puts every one of
those vertices in the original outer contact face.

Second, once a vertex-disjoint fully inactive near-unit matching is available, one can
activate **every matching endpoint** by sequential first-contact motions. No auxiliary
short-edge graph, planarity theorem, or coloring loss is needed. A first-hit target is
frozen as soon as it becomes contact-active; this prevents later moves from destroying
created contacts. The construction creates at least one new persistent unit contact
per original matching edge and moves every source point by at most the original
matching excess.

Put

\[
h_*:=\frac{\sqrt{303}}{52},\qquad
c_*:=0.129220199818177\ldots,
\]

\[
\delta_*:=2\left(1-\cos\frac{c_*}{2}\right)
=0.00417301303247308\ldots,
\]

and, for fixed `K>h_*`,

\[
\alpha_K:=1-\frac{h_*}{K},\qquad
\nu_K:=1+\frac{\delta_*\alpha_K}{4}.
\tag{FA.1}
\]

The fixed-pair directional-defect theorem gives one of the two extreme FREE
ancestries, say ancestry `i`, whose number `L_i` of lower gates satisfies

\[
\boxed{L_i\ge (\nu_K-o(1))D.}
\tag{FA.2}
\]

For the same fixed-pair branch, after a second fixed cutoff `J>h_*`, it also gives a
vertex-disjoint matching `M` of old fully inactive outer-face source pairs with

\[
\boxed{
|M|\ge\left(\frac{\mu_{K,J}}2-o(1)\right)D,
\qquad
\mu_{K,J}:=\nu_K-\frac{h_*}{J},
}
\tag{FA.3}
\]

and

\[
\boxed{1<|x-y|\le1+\frac JD\qquad(xy\in M).}
\tag{FA.4}
\]

## 1. The ancestry itself gives a truncation-free OP charge

Let `U_i` be the number of upper gates on ancestry `i`, and write its successive
source vertices as

\[
z_0,z_1,\ldots,z_{L_i+U_i}.
\]

The activation-time increments on every ancestry edge are strictly positive. Hence a
source vertex cannot recur on one ancestry: its activation time is unique and the
successive activation times strictly increase. Therefore the ancestry contains exactly

\[
L_i+U_i+1
\]

distinct old source points.

The two-sided outer-face localization theorem says every one of these vertices is an
old fully contact- and diameter-inactive source point in the original unbounded
contact face. Let `Z_in` count such contact-isolated outer-face points lying in the
force hull `F`, and let `Z_ext` count source points outside `F`. Then

\[
\boxed{Z_{in}+Z_{ext}\ge L_i+U_i+1\ge L_i+1.}
\tag{FA.5}
\]

The exact OP bound is

\[
Z_{in}\le\frac{2}{\sqrt3}H_{out}-\frac{b-P_F}{2},
\tag{FA.6}
\]

where `H_out` is total OP outer-pocket area, `b` is the unit-contact outer-walk
length, and `P_F=per(F)`. Combining FA.2, FA.5, and FA.6 gives

### Theorem FA-OP — truncation-free pair-reuse outer currency

\[
\boxed{
Z_{ext}
+\frac{2}{\sqrt3}H_{out}
-\frac{b-P_F}{2}
\ge
(\nu_K-o(1))D.
}
\tag{FA.7}
\]

Equivalently,

\[
\boxed{
Z_{ext}
+\frac{2}{\sqrt3}H_{out}
\ge
(\nu_K-o(1))D+\frac{b-P_F}{2}.
}
\tag{FA.8}
\]

This strictly strengthens the finite-cutoff coefficient in the preceding half-plus
outer-currency theorem: the old coefficient was

\[
\mu_{K,J}=\nu_K-h_*/J,
\]

because it first discarded all lower edges longer than `1+J/D` and then parity
thinned. Neither operation is relevant to population accounting.

For the moderate fixed choice `K=1`,

\[
\boxed{\nu_1=1.000694026332810\ldots.}
\tag{FA.9}
\]

For `K=400`,

\[
\boxed{\nu_{400}=1.001042380190805\ldots.}
\tag{FA.10}
\]

Thus one does not need a large second cutoff `J` to obtain essentially the full
fixed-cutoff envelope. Letting `K` tend through fixed constants after the asymptotic
argument gives

\[
\boxed{
\nu_\infty=1+\frac{\delta_*}{4}
=1.001043253258118\ldots.
}
\tag{FA.11}
\]

In particular, if `Z_ext=o(D)`, then

\[
\boxed{
H_{out}\ge
\left(\frac{\sqrt3}{2}\nu_K-o(1)\right)D
+\frac{\sqrt3}{4}(b-P_F).
}
\tag{FA.12}
\]

For `K=400` the linear area coefficient is

\[
\boxed{0.866928131510077\ldots,}
\tag{FA.13}
\]

already within `7.6e-7` of the envelope
`0.866928887608550...`.

There is also an exact gate-count refinement. Summing the directional-defect estimate
before choosing the heavier ancestry and then adding the upper-gate counts gives

\[
\max_{r\in\{1,2\}}(L_r+U_r)
\ge
D+\frac{\delta_*}{2}E
+\frac{U_1+U_2}{2}-O(\sqrt D)-o(D),
\tag{FA.14}
\]

where `E` is the common lower-edge population. Since
`E>=(alpha_K/2-o(1))D`, the right side contains FA.2 plus the additional
nonnegative term `(U_1+U_2)/2`. Consequently FA.7 can be sharpened, without changing
notation, to

\[
\boxed{
Z_{ext}+\frac{2}{\sqrt3}H_{out}-\frac{b-P_F}{2}
\ge
\nu_KD+\frac{U_1+U_2}{2}-o(D).
}
\tag{FA.15}
\]

The useful point is not another decimal. Linear upper-gate population must be paid in
this same canonical outer currency on top of the directional-defect surplus.

## 2. General matching endpoint-saturation lemma

The contact-activation loss can be removed completely by a source-level lemma that
does not use the FREE construction.

### Lemma FA-SAT — fully inactive near-unit matching saturation

Let `A` be any finite unit-separated planar source of diameter `D`, let
`K=conv(A)`, and let `M` be a matching of `m` original source pairs. Assume every
endpoint of `M` is both contact-inactive and diameter-inactive in `A`, and

\[
1<|x-y|\le1+\varepsilon
\qquad(xy\in M).
\tag{FA.16}
\]

Then there is another source `A'` with the same cardinality and diameter exactly `D`
such that:

1. every original contact remains a unit contact;
2. every original diameter endpoint remains fixed, so every original diameter pair
   remains at distance `D`;
3. every endpoint of `M` is incident to at least one new persistent unit contact;
4. at least `m` distinct new unit contacts are present;
5. every point moves by at most `epsilon`, and each matching endpoint moves at most
   once;
6. every moved point stays in the original convex hull `K`.

### Proof

Call a matching endpoint **unresolved** until it has acquired a new contact and is
then frozen forever. Initially all `2m` endpoints are unresolved, because all were
contact-inactive in the original source. All nonmatching source points are fixed
forever.

While an unresolved endpoint remains, choose one, call it `v`, and let `p(v)` be its
original matching partner. An unresolved endpoint has never moved and has never been
hit by an earlier new contact. Its partner is in one of three states:

- unresolved and still at its original position;
- already resolved as a target and still at its original position; or
- already resolved as a mover, in which case its only possible earlier motion was
  straight toward `v`, its unique matching partner.

Hence the current pair distance satisfies

\[
1<|v-p(v)|_{current}\le |v-p(v)|_{original}\le1+\varepsilon.
\tag{FA.17}
\]

Move `v` straight toward the **current** position of `p(v)` and stop at the first
unit-distance event with any current source point. Such an event occurs no later than
the moment `v` reaches distance one from `p(v)`, so the displacement is at most
`epsilon`. Before the first event all lower metric inequalities remain strict.

Freeze `v`. If the first event is simultaneous with one or more other unresolved
matching endpoints, freeze all of those endpoints as well. Every new contact created
at this event persists: the mover is frozen, every unresolved matching endpoint hit at
the event is frozen, already resolved matching endpoints are already frozen, and
nonmatching points never move.

This invariant also shows that every still-unresolved endpoint remains contact-inactive
until its own resolving event. Therefore the procedure can continue until no
unresolved matching endpoint remains.

No old contact can be destroyed, because an endpoint of `M` had no old contact and
all nonmatching points are fixed. For upper safety, use induction. Every current point
lies in the original convex hull `K`. At one step both `v` and its current partner lie
in `K`, so the entire motion segment lies in `K` by convexity. Since `diam(K)=D`, no
current distance can exceed `D`. Every original exact-diameter endpoint is outside the
matching and therefore never moves, so at least one original diameter pair stays at
exact distance `D`. The diameter is exactly `D` throughout.

It remains to count contacts. Suppose one iteration newly resolves `s>=1` matching
endpoints. If `s=1`, the mover has at least one new contact with a fixed or previously
resolved point. If `s>=2`, the mover has a distinct new contact with each of the other
`s-1` newly resolved endpoints. Thus the iteration creates at least

\[
\max\{1,s-1\}\ge\frac{s}{2}
\]

distinct persistent new contacts. The newly resolved sets partition all `2m`
matching endpoints. Summing over iterations gives at least

\[
\frac12(2m)=m
\]

new contacts. Every matching endpoint is resolved at termination, proving the lemma.
`\square`

The lemma deliberately does **not** assert that the new representative is
triangle-free. A first-hit event can create a unit triangle. Therefore FA-SAT by
itself is not a contradiction to the contact-minimal normalization, which minimizes
contacts only among triangle-free global minimizers.

## 3. Apply FA-SAT to the half-plus FREE matching

Apply FA-SAT to `M` from FA.3 with

\[
\varepsilon=J/D.
\]

The terminal source is another same-cardinality global minimizer because its diameter
is still exactly the globally minimal value `D`. The original positive-force core and
force hull are fixed pointwise. Any old equilibrium certificate remains valid after
assigning multiplier zero to the new contacts.

The quantitative conclusion is now:

\[
\boxed{
\text{new persistent contacts}
\ge
\left(\frac{\mu_{K,J}}2-o(1)\right)D,
}
\tag{FA.18}
\]

and

\[
\boxed{
\text{formerly isolated matching endpoints made contact-active}
\ge
(\mu_{K,J}-o(1))D.
}
\tag{FA.19}
\]

Every source point moves by at most `J/D`.

For the explicit fixed choice `K=J=400`,

\[
\boxed{
\mu_{400,400}=1.000205510229962\ldots,
}
\]

so the construction creates at least

\[
\boxed{(0.500102755114981\ldots-o(1))D}
\tag{FA.20}
\]

persistent new unit contacts and makes at least

\[
\boxed{(1.000205510229962\ldots-o(1))D}
\tag{FA.21}
\]

old isolated endpoints contact-active, with pointwise displacement at most `400/D`.

The preceding coloring construction guaranteed only

\[
(0.0833504591858302\ldots-o(1))D
\]

new contacts for the same cutoffs. FA-SAT improves that guaranteed contact count by an
exact factor of six and, more importantly, removes all dependence on short-edge
planarity from the activation step.

Letting `K,J` tend through fixed constants after the asymptotic argument gives the
envelope

\[
\boxed{
\text{new contacts}
\ge(0.500521626629059\ldots-o(1))D,
}
\tag{FA.22}
\]

\[
\boxed{
\text{activated old isolates}
\ge(1.001043253258118\ldots-o(1))D.
}
\tag{FA.23}
\]

## 4. Exact remaining seam

These improvements do not close C-II.

The OP consequence is now limited by genuine geometry, not by the `J/D` truncation:
`PAIR-REUSE` must pay more than `D` units of combined external-population / outer-pocket
currency, plus the exact detour correction and any linear upper-gate population.

The representative-transfer consequence is also saturated at the natural matching
scale: every endpoint of the half-plus matching can be made contact-active by
`O(D^{-1})` displacement and at least one new contact per matching edge can be made
persistent while the old diameter/force carrier is fixed. But the resulting minimizer
need not be triangle-free and it has **more**, not fewer, contacts. Contact minimality
therefore supplies no contradiction yet.

A closing use of FA-SAT must be representative-invariant: either transfer a canonical
outer-walk/force-hull obstruction to this contact-rich representative, or use the
vanishing displacement and fixed old diameter carrier to build a second deformation
that removes old contacts or strictly decreases the diameter. Further coloring or
matching extraction cannot improve the activation endpoint count, because all `2|M|`
matching endpoints are already activated.

**Disposition:** removed the lower-edge truncation from the OP population charge and
removed the factor-six coloring loss from the half-plus contact activation. C-II
remains open.
