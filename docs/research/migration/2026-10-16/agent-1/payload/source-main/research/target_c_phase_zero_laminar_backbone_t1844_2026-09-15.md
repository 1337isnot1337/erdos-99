# Target C-II — phase-zero localization forces a `>0.0295D` laminar O--O backbone

**Date:** 2026-09-15  
**Status:** proof-only source-level structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited `0.7404D` weighted smallest-leaf center fan; retained pair-weight floor `P_V>0.0848`; audited Section 157 outer-train bracing and its normal-arc hostile audit; routewise round-hull endpoint-capacity domination; exact laminar multi-train shear; mixed infinitesimal rigidity  
**Certificate:** `research/verify_target_c_phase_zero_laminar_backbone_t1844.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current live-backbone theorem obtains a path of more than `0.017104D` smallest-leaf
outer-to-outer trains by thresholding center degree and then extracting one center-train
path from the complement dual tree.  The retained boundary geometry gives a different
route: almost all of the **non-singleton retained pair mass itself** lies on at most two
nested chains.

The gain comes from two facts already present in the proof stack.

1. Singleton stopped trains have no strict-rhombus train crossings.  Therefore the
   audited weighted center-fan average forces a definite amount of retained pair mass
   onto non-singleton O--O trains.
2. Section 157 puts one zero of the train's transverse diameter-bracing function inside
   the smaller outer normal arc.  All trains in one shrinking exact-phase window have
   those zeros near the same antipodal pair.  Except for `o(D)` retained pair weight,
   every smaller terminal arc therefore contains one of two fixed antipodal markers.
   Same-phase O--O trains are pairwise noncrossing, so the arcs containing either fixed
   marker form one nested chain.

This yields the following structural strengthening.

## Theorem PZL — phase-zero laminar backbone

For every full-core Type-II survivor sequence with

\[
 t={q-k\over D}\le1.844,
\]
there is a family

\[
\mathcal L_D=\{\tau_1,\ldots,\tau_m\}
\]
of distinct **non-singleton** smallest-leaf O--O complete stopped trains such that

\[
\boxed{
 m>{59\over2000}D-o(D)=0.0295D-o(D),
}
\tag{PZL.1}
\]

and their proper train midpoint crosscuts are linearly nested.  Equivalently, after
coherent shore orientation, their shores satisfy

\[
S_1\supset S_2\supset\cdots\supset S_m,
\tag{PZL.2}
\]

and the selected crosscuts are the consecutive edges of one simple complement-dual
path.

The stronger load-bearing weight bound before safe rounding is

\[
\boxed{
{1\over D}\sum_{\tau\in\mathcal L_D}w_\tau
>{98103\over3321875}-o(1)
=0.02953241768\ldots-o(1).
}
\tag{PZL.3}
\]

Consequently the exact laminar shear/rank argument applies to a substantially longer
backbone than previously known.  In particular:

\[
\boxed{N_{prop}>0.0295D-o(D),}
\tag{PZL.4}
\]

where `N_prop` is the number of actual diameter edges having a nonempty proper
incidence interval on this backbone;

\[
\boxed{|S_{switch}|>0.01475D-o(D),}
\tag{PZL.5}
\]

where `S_switch` is the set of internal backbone boundaries at which some diameter
incidence starts or stops; and there are the same number of distinct loaded actual
diameter endpoints localized at distinct backbone layers.

Moreover, using the standard KKT interval-row total-variation bounds, some adjacent
pair on this backbone satisfies

\[
\boxed{
N_i+D B_i<281+o(1),
}
\tag{PZL.6}
\]

where `N_i` is the number of switching actual diameter rows and

\[
B_i=\sum_h\beta_h|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
\]
Hence the same pair has

\[
N_i<281+o(1),
\qquad
B_i<{281\over D}+o(D^{-1}).
\tag{PZL.7}
\]

This last pair is not asserted to have the inverse-`D` phase mismatch of the separate
Pareto finite-cusp theorem.  Its two train directions are only `o(1)` apart from the
common exact leaf atom.  Thus (PZL.6) is a stronger switching-support reduction but not
a replacement for the current `<1800` three-way cusp theorem.

---

## 1. The weighted fan forces non-singleton pair mass

Let `Q_V` be the retained weighted O--O family in the smallest leaf phase.  Write

\[
W=\sum_{\tau\in Q_V}w_\tau.
\]

The phase-resolved pair theorem gives

\[
\boxed{W>PD-o(D),\qquad P={53\over625}=0.0848.}
\tag{PZL.8}
\]

Let `d_\tau D` be the number of center-phase complete trains that cross `tau` in strict
rhombi.  The hostile-audited fan theorem gives

\[
\boxed{
{\sum_\tau w_\tau d_\tau D\over W}
>AD-o(D),
\qquad
A={1851\over2500}=0.7404.
}
\tag{PZL.9}
\]

The total center phase contains fewer than

\[
ND+o(D),
\qquad
N={1063\over1000}=1.063,
\tag{PZL.10}
\]
complete trains.

A singleton stopped train contains no strict rhombus.  Hence it has

\[
d_\tau=0.
\]
Let `W_ns` be the total retained pair weight carried by non-singleton members of
`Q_V`.  Every one of them has `d_tau<=N+o(1)`, so (PZL.9) gives

\[
(ND+o(D))W_{ns}
\ge\sum_\tau w_\tau d_\tau D
>(AD-o(D))W.
\]
Using (PZL.8),

\[
\boxed{
W_{ns}>{AP\over N}D-o(D)
={196206\over3321875}D-o(D)
=0.05906483537\ldots D-o(D).
}
\tag{PZL.11}
\]

This is the first point where singleton trains matter.  No deletion of singletons from
an all-train Mantel graph is being made; their zero crossing degree removes them only
from this boundary pair population.

---

## 2. Section 157 puts every train near one of two fixed phase zeros

Pass to the standard shrinking smallest-leaf phase window.  Let `phi_*` be the limiting
projective leaf phase and choose full-circle normal-angle lifts

\[
\phi_*,\qquad \phi_*+\pi.
\]

For each non-singleton O--O train `tau`, use the audited convex-pocket retraction of its
two terminal occurrences to the loaded-hull boundary.  Let `J_tau` be the boundary
normal-angle arc of the **smaller** Jordan shore, so

\[
|J_\tau|\le\pi.
\]

Section 157 gives actual diameter edges crossing the train cut with both transverse
signs.  The hostile audit of the outer-train bracing-energy theorem converts this into
the following uniform near-disk statement: one zero of

\[
n\mapsto n\cdot Ju_\tau
\]
lies in `J_tau` up to `o(1)` normal angle.  Those two zeros are exactly the two
full-circle representatives of the projective train phase.

Because the selected train phases lie in a shrinking window around `phi_*`, there is a
sequence

\[
\eta_D\longrightarrow0
\]
such that every `J_tau` comes within angular distance `eta_D` of at least one of

\[
\phi_*,\qquad\phi_*+\pi.
\tag{PZL.12}
\]

Classify `tau` by one such nearest marker, breaking the measure-zero/tie case
arbitrarily.

---

## 3. Only `o(D)` retained pair weight misses its class marker

Fix one marker `z` from the antipodal pair.  Delete every train assigned to `z` for
which either

1. `z` is not contained in `J_tau`; or
2. an endpoint of `J_tau` lies within angular distance `2 eta_D` of `z`.

In the first case, (PZL.12) already puts an endpoint of `J_tau` within `eta_D` of `z`.
Thus every deleted train has a terminal occurrence whose retracted normal angle lies
within `2 eta_D` of its class marker.

The retained pair weight is

\[
w_\tau=\min(a_\tau,b_\tau),
\]
so it is no larger than the retained weight of either terminal occurrence.  Charge each
deleted train to such a near-marker endpoint occurrence.

The routewise retention used by the dominant-orbit argument is dominated by loaded-hull
side-length measure.  In the Type-II round limit, normalized full-circle normal-angle
endpoint measure is dominated by

\[
{1\over2}\,d\theta+o(1)
\]
uniformly on intervals.  Equivalently, the projective occurrence measure is dominated
by `d theta`, exactly the measure domination used in the phasewise bathtub theorem.
Therefore the total retained endpoint weight in the `eta_D`-neighborhood of one marker
is at most

\[
\eta_DD+o(D)=o(D).
\]
The two marker neighborhoods together still carry only `o(D)` retained weight.

Finite loaded-hull side ties do not change this conclusion: the canonical interface
collapse has maximal normalized side length `o(1)`, and the audited pocket retraction
uses the original occurrence order as a tie-breaker.

Hence after deleting total retained pair weight `o(D)`, every remaining train assigned
to `z` satisfies

\[
\boxed{z\in \operatorname{int}J_\tau,}
\tag{PZL.13}
\]

and each endpoint of `J_tau` is separated from `z` by at least `2 eta_D`.  This extra
margin removes the only possible ambiguity caused by several terminal occurrences
retracting to the same loaded-hull side at the marker.

---

## 4. Each marker class is one nested chain

All trains under discussion lie in one shrinking exact leaf-phase window.  Two such
complete trains cannot cross: a strict-rhombus train crossing requires projective
separation strictly larger than `pi/3`.

The audited convex-pocket retraction preserves cyclic endpoint order.  Thus the
retracted endpoint chords of these non-singleton trains form a noncrossing chord
family.  For a noncrossing chord family, the shorter boundary arcs are laminar: two
partially overlapping but non-nested shorter arcs would have alternating endpoints and
the chords would cross.  This is exactly the laminar step already hostile-audited in
the outer-train bracing-energy theorem.

Within one marker class, (PZL.13) says every shorter arc contains the same point `z`
in its interior, with a shrinking but positive endpoint margin.  No two such arcs can
therefore be disjoint, even before collapsing same-side occurrence ties.  Laminarity
collapses to total inclusion:

\[
J_{\tau_1}\supseteq J_{\tau_2}\supseteq\cdots
\]
after reindexing.

For pairwise disjoint proper crosscuts of a disk, nested chosen boundary arcs give
nested geometric shores.  Indeed the crosscut for the smaller boundary arc has both
endpoints in the boundary arc of the larger cap and, being disjoint from the larger
crosscut, must lie in that cap.  Inductively the corresponding shore sets are nested.
Thus every marker class is one simple complement-dual path.

There are only two marker classes.  By (PZL.11), after the `o(D)` deletion one of them
has retained pair weight greater than

\[
{1\over2}{AP\over N}D-o(D)
={98103\over3321875}D-o(D).
\tag{PZL.14}
\]

Every retained pair weight is at most one.  Therefore that class contains at least as
many distinct trains as its total weight, proving (PZL.1)--(PZL.3).

All selected trains are non-singleton by construction, so the exact laminar
multi-train interval theorem applies directly.

---

## 5. Full shear rank on the longer chain

For the nested chain orient the exact laminar shores coherently and let

\[
M_{hi}=\varepsilon_{hi}(r_h\cdot Ju_i)
\]
be the actual-diameter first-variation matrix in the selected train-angle coordinates.

The previous live-backbone rank proof used a center train crossing the whole extracted
path to kill the Euclidean rotation mode.  Full crossing is unnecessary here.  The
dominant exact orbit has positive center-phase mass (`C>0.8538` in the upstream
`t<=1.844` theorem), so there is at least one center-phase complete train outside the
selected smallest-leaf family.  Every selected O--O shear leaves every contact edge of
that unselected train unchanged, because only contacts belonging to the selected train
cross its shore cut.  Its train angular rate is therefore zero.

If `M theta=0`, the exact train shears give an infinitesimal flex of all positive
contacts and all actual diameter constraints.  Canonical mixed infinitesimal rigidity
makes the flex Euclidean.  A translation has zero train rates; a rotation has one
common train rate.  The unselected center train has rate zero, so the rotation rate is
zero.  Hence every selected rate `theta_i` is zero and

\[
\boxed{\operatorname{rank}M=m.}
\tag{PZL.15}
\]

This removes the only apparent dependence of the old rank lemma on a common crossing
center train.

---

## 6. Proper intervals, switching layers, and loaded endpoints

The exact laminar interval theorem says every actual diameter row has one signed
contiguous incidence interval on the chain.

All full-span rows lie in the two-dimensional span of the coordinate sequences of the
near-leaf directions `Ju_i`.  Every proper interval row adds at most one row dimension.
Thus, exactly as in the live-backbone theorem,

\[
N_{prop}\ge m-2.
\]
Equation (PZL.1) gives (PZL.4).

If `s` internal boundaries carry any support change, they partition the columns into
`s+1` constant-incidence blocks.  On each block all rows lie in a two-dimensional
coordinate span.  Therefore

\[
m=\operatorname{rank}M\le2(s+1),
\]
so

\[
s\ge\left\lceil{m\over2}\right\rceil-1
>0.01475D-o(D),
\]
proving (PZL.5).

At a switching boundary the endpoint-region path of some proper diameter interval
enters or leaves the backbone.  Hence at least one endpoint of that actual diameter
edge projects to the corresponding internal dual vertex.  Distinct boundary indices
have distinct projection vertices, and one physical endpoint has one projection.
Thus the same lower bound gives distinct loaded diameter endpoints at distinct chain
positions.

---

## 7. A `<281` switching pair without an inverse-`D` phase claim

For each internal boundary put

\[
N_i=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\}
\]
and

\[
B_i=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
\]

Every diameter incidence is one signed interval.  It can start and stop at most once,
so

\[
\sum_iN_i\le2|H|\le2\pi D.
\tag{PZL.16}
\]

The relative-interior KKT normalization has

\[
\sum_h\beta_h=1,
\]
and each row again switches at most twice, giving

\[
\sum_iB_i\le2.
\tag{PZL.17}

For `m>(59/2000)D-o(D)`, average the nonnegative quantities

\[
N_i+D B_i.
\]
Using `pi<355/113`, the exact certificate gives

\[
{2\pi+2\over59/2000}<281.
\]
Therefore some internal boundary satisfies (PZL.6)--(PZL.7).

The associated KKT cut-resultant difference is

\[
F_{i+1}-F_i
=\sum_h\beta_h
(\varepsilon_{h,i+1}-\varepsilon_{hi})r_h,
\]
so

\[
\|F_{i+1}-F_i\|\le D B_i<281+o(1).
\tag{PZL.18}
\]

Separately, averaging only (PZL.17) gives an adjacent pair with

\[
D B_i<68+o(1),
\qquad
\|F_{i+1}-F_i\|<68+o(1).
\tag{PZL.19}
\]

The selected leaf directions all belong to a shrinking phase window, so their adjacent
projective mismatch is `o(1)`.  Nothing in this argument upgrades it to `O(D^{-1})`.
That distinction is essential: the existing Pareto adjacent-cusp theorem remains the
correct input when a uniform finite first-derivative bound on every spanning diameter
row is required.

---

## 8. Frontier effect

The live `t<=1.844` structure can now be strengthened from

```text
>0.017104D center-extracted O-O backbone
```

to

```text
>0.0295D non-singleton phase-zero laminar O-O backbone
+ >0.0295D proper-interval diameter edges
+ >0.01475D switching strip positions
+ >0.01475D distinct loaded endpoints at distinct strip positions
+ an adjacent pair with <281 switching rows and beta switch mass <281/D
+ an adjacent pair with cut-resultant jump <68
```

The new backbone is obtained before choosing a common center train.  Its topology comes
from Section-157 phase-zero localization and boundary order, rather than from a path in
a branching good-leaf dual tree.

This does not close C-II.  Its main use is to remove a large amount of dual-tree
branching from the source-level obstruction.  The next useful attack is to combine the
longer nested backbone with the straight-thrackle/caterpillar structure of switching
layer cuts, or to re-run the high-phase-center selection inside this already laminar
family and seek a better simultaneous phase/switching Pareto pair.

**Disposition:** proved proof-only phase-zero laminar-backbone strengthening. C-II and
Level I remain open.
