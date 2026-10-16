# Target C-II — phase-zero O--O path and one-sided finite strip extend through `t<=1.865`

**Date:** 2026-09-15
**Status:** proof-only high-`t` structural extension
**Scope:** full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.865`
**Dependencies:** hostile-audited retained dominant O--O pair-weight extension through `1.865`; hostile-audited phase-zero path extraction; diameter-path Helly hub; exact laminar interval support; normalized positive KKT stress
**Certificate:** `research/verify_target_c_phase_zero_path_t1865_interface.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Main has retracted the former low-energy path claims beyond `t<=1.8593` because their
oriented terminal-branch step was incomplete.  The currently valid main replacement
uses an explicit same-branch exclusion through `t<=1.8593`.  The independently
hostile-audited retained-pair bootstrap remains positive farther, through `t<=1.865`:

\[
{P_{OO}^{dom}\over D}>0.0027-o(1).
\]

One of the at most three dominant projective phase classes therefore carries retained
pair weight

\[
>0.0009D-o(D).
\]

The phase-zero marker theorem converts **retained pair weight itself** into a dual path;
it does not require a fixed low-energy threshold.  Applying its same deletion argument
at the new endpoint gives a live path and one-sided finite-strip normal form through
`1.865`.

### Theorem E65-PATH

Every sufficiently large full-core Type-II survivor with

\[
\boxed{1.844<t\le1.865}
\tag{P65.1}
\]

contains one shrinking dominant phase window with a pairwise-noncrossing O--O family

\[
\mathcal L_D=\{\tau_1,\ldots,\tau_m\}
\]

such that, after deleting only `o(D)` retained pair weight near two shrinking phase-zero
marker neighborhoods,

\[
\boxed{m>0.0009D-o(D),}
\tag{P65.2}
\]

and the complement dual of the selected proper O--O crosscuts is a simple path.
Every actual diameter endpoint-region path on this dual contains one common hub region.

After discarding the single potentially mixed hub boundary, one nonhub adjacent strip
has every switching diameter row directed topologically toward the hub side and

\[
\boxed{N_i\le6981}
\tag{P65.3}
\]

if switching count alone is optimized.

Alternatively, one nonhub strip may be chosen with all three finite-interface
quantities simultaneously controlled:

\[
\boxed{
N_i\le12694,
\qquad
L_i\le12694,
\qquad
B_i<{12695\over D}+o(D^{-1}).
}
\tag{P65.4}
\]

Here

- `N_i` is actual switching-diameter edge count;
- `L_i` is the number of actual diameter endpoints in the middle region; and
- `B_i` is total normalized KKT multiplier on the switching diameter rows.

The two adjacent train directions lie in one shrinking phase window, so their
projective gap is `o(1)`.

Thus the exact path / common-hub / one-sided finite-interface machinery extends beyond
main's currently valid `1.8593` opposite-branch endpoint to

\[
\boxed{t\le1.865}
\]

without a fixed low-energy terminal threshold.  The load-bearing oriented-branch step
is supplied instead by the separately hostile-audited two-shore phase-zero argument.

---

## 1. One phase retains linear pair weight at `T=1.865`

The hostile-audited retained-pair theorem gives

\[
P_{OO}^{dom}>0.0027D-o(D).
\tag{P65.5}
\]

The limiting dominant train orbit has at most three projective phase classes.  Freeze
disjoint shrinking windows around those atoms.  Pigeonhole gives one window with
retained O--O pair weight

\[
\boxed{P_i>0.0009D-o(D).}
\tag{P65.6}
\]

For one train in this window, write its selected outer-terminal weights as
`a_tau,b_tau` and pair weight as

\[
w_\tau=\min(a_\tau,b_\tau)\le1.
\]

Hence the number of positive-weight trains in the chosen window is at least its total
pair weight:

\[
\#\{\tau:w_\tau>0\}>0.0009D-o(D).
\tag{P65.7}
\]

Because the phase-window radius tends to zero, distinct trains in this window are
pairwise noncrossing for all sufficiently large sources: strict-rhombus train crossing
requires projective phase separation strictly greater than `pi/3`.

---

## 2. Reuse the hostile-audited phase-zero deletion

The phase-zero path theorem is quantitative in only one input: a positive linear
retained pair-weight density in one shrinking phase window.  Its proof then uses
Section 157 two-shore bracing and near-disk normal convergence to produce one fixed
antipodal pair of limiting phase-zero markers.

Let the phase-window error be `epsilon_D->0` and the near-disk directional replacement
error be `eta_D->0`.  Choose

\[
\rho_D\downarrow0,
\qquad
\epsilon_D+\eta_D=o(\rho_D).
\tag{P65.8}
\]

Delete every selected train having either retained endpoint in the two oriented normal
neighborhoods of radius `rho_D` around the antipodal markers.

The hostile audit proves that each pair-endpoint measure is dominated by retained
loaded-hull side-length measure.  Type-II near-disk perimeter convergence therefore
makes those shrinking neighborhoods carry only `o(D)` retained pair weight.  Hence the
surviving family still has

\[
\boxed{
\sum_{\tau\in\mathcal L_D}w_\tau
>0.0009D-o(D),
\qquad
m>0.0009D-o(D).
}
\tag{P65.9}
\]

Every surviving proper crosscut separates the same two fixed boundary markers.  The
hostile-audited two-marker crosscut lemma then totally orders the marker-side shores by
inclusion.  Therefore the complement dual is a path

\[
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m.
\tag{P65.10}
\]

No low-energy threshold or fixed positive terminal-arc separation is used.

---

## 3. Every actual diameter support is an interval with one common hub

For an actual diameter edge with endpoint regions `R_a,R_b`, exact laminarity gives
selected-cut support equal to the path interval between `a` and `b`.

Any two actual diameter segments meet or share an endpoint, so their endpoint-region
paths intersect in the complement dual.  Pairwise intersecting subpaths of a tree have
a common vertex.  Thus there is one hub index `k` with

\[
\boxed{a_h\le k\le b_h\qquad(h\in H).}
\tag{P65.11}
\]

This Helly statement is purely topological and applies directly to the finite shrinking-
phase path.

At an internal region `R_i`:

- if `i<k`, every switching diameter interval starts at `i` and runs toward the hub;
- if `i>k`, every switching interval ends at `i` and comes from the hub side.

Only the hub region itself can support both switch orientations.  Hence every nonhub
switching set is one-sided toward the common hub.

---

## 4. Count and KKT entry/exit budgets

Let

\[
N_i:=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\},
\tag{P65.12}
\]

\[
B_i:=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|,
\tag{P65.13}
\]

and

\[
L_i:=|B_+\cap R_i|.
\tag{P65.14}
\]

One interval enters/exits at most twice, so

\[
\sum_iN_i\le2|H|.
\]

The actual diameter graph is a straight-line thrackle, hence

\[
|H|\le|B_+|.
\]

Actual diameter endpoints are distinct unit-separated extreme vertices of the force
hull, whose perimeter is at most `pi D`.  Therefore

\[
\boxed{\sum_iN_i\le2\pi D.}
\tag{P65.15}
\]

Under the normalized KKT stress

\[
\sum_h\beta_h=1,
\]

each diameter interval changes at most twice, so

\[
\boxed{\sum_iB_i\le2.}
\tag{P65.16}
\]

The middle regions are disjoint and their loaded diameter endpoints are subsets of
`B_+`, so

\[
\boxed{\sum_iL_i\le\pi D.}
\tag{P65.17}
\]

Discard the single hub index if internal.  The remaining number of boundaries is still

\[
>0.0009D-o(D).
\tag{P65.18}
\]

All preceding sums only decrease.

---

## 5. Exact finite-interface constants

For count only, average (P65.15) over the nonhub boundaries.  Using

\[
\pi<{355\over113},
\]

the exact certificate proves

\[
{2(355/113)\over0.0009}
={7100000\over1017}
=6981.3176\ldots<6982.
\tag{P65.19}
\]

Since `N_i` is integral, some nonhub boundary has

\[
N_i\le6981.
\]

For simultaneous control, define

\[
C_i:=N_i+D B_i+L_i.
\]

Equations (P65.15)--(P65.17) give

\[
\sum_iC_i\le(3\pi+2)D.
\tag{P65.20}
\]

The exact verifier gives

\[
{3(355/113)+2\over0.0009}
={12910000\over1017}
=12694.1986\ldots<12695.
\tag{P65.21}
\]

Thus one nonhub boundary has

\[
C_i<12695+o(1).
\]

All terms are nonnegative.  Eventually integrality yields

\[
N_i,L_i\le12694,
\]

and

\[
B_i<{12695\over D}+o(D^{-1}).
\]

This proves (P65.4).

---

## 6. Relation to the repaired main path frontier

Main's currently valid high-`t` path is
`target_c_opposite_branch_dual_path_t18593_2026-09-15.md`.  It uses threshold
`lambda=0.5025` together with an explicit Section-157 same-branch exclusion and is
proved through `t<=1.8593`.  Former path claims through `1.860` and `1.8623` were
correctly retracted because their projective endpoint-energy bounds did not establish
opposite oriented terminal branches.

The present theorem uses a different localization mechanism:

```text
retained pair weight
+ two-sided diameter bracing
+ near-disk phase-zero markers
+ delete only shrinking marker neighborhoods
-> path.
```

Because shrinking neighborhoods have `o(D)` retained endpoint mass, no fixed energy
threshold is paid.  This is why the path survives to the later retained-pair endpoint
`1.865`.

The price is that the two terminal arcs are separated only at a shrinking scale; no
fixed positive gap and no `O(D^-1)` adjacent phase bound is claimed.

---

## 7. Updated high-`t` frontier

The proof-only full-core state now has the following overlap:

```text
t <= 1.844:
    excluded by the hostile-audited paired-remainder theorem.

1.844 < t <= 1.8593:
    repaired main opposite-branch path;
    phase-zero marker path also applies.

1.8593 < t <= 1.865:
    phase-zero marker path with >0.0009D-o(D) cuts,
    common diameter-routing hub,
    one-sided switching at every nonhub boundary,
    a finite nonhub strip with <=6981 movers,
    or simultaneous <=12694 middle/moving vertices/edges and O(1/D) switch beta mass.
```

The retained-pair bootstrap itself numerically dies near `1.865196`, so extending this
particular path mechanism materially farther requires a new retained-mass inequality.
For the now-covered band, the next target is source-level classification/repacking of
the finite one-sided middle layer, not another path-count improvement.

**Disposition:** proved proof-only extension of the path/hub/one-sided finite-interface
normal form through `t<=1.865`. C-II and Level I remain open.
