# Target C: open-cell strong staircase couples to the transverse shore

Date: 2026-10-04
Base: dd0ce94b395605886e2a4b1cd43d51f532cc34bd
Status: proof-only Target C-II candidate; theorem-state authority unchanged.
LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.

This note continues the nonconstant open-witness-cell strong-SCC branch. The two
immediate predecessor notes prove that, after excluding the inverse-D inactive
near-activity alternative, the signed gap support is one bidirected maximal
staircase. The result below couples that staircase to the opposite complete O--O
shore. It uses the two full-support open-cell guard diameters, convex
diameter-thrackle geometry, the current four-host decomposition, exact laminar
support, and the complete-grid rank theorem. It does not use exact-phase bundle
balance.

## 1. Setup

Let the selected A-shore have cuts tau_1,...,tau_m, layers 0,...,m, and common
open diameter-direction cell J. The sign-nesting theorem supplies two
full-support actual diameters

    h_- = v x_-,    h_+ = v x_+,

with common endpoint v in A-layer 0, far endpoints x_-,x_+ in A-layer m, and
opposite strict transverse signs throughout J.

The strong-SCC theorem gives one maximal staircase of simple A-support edges

    C_1,...,C_m,    C_1 = (0,m),

where every step has the form

    (a,b) -> (a+1,b)    or    (a,b) -> (a,b-1),          (1)

and every simple support edge occurs with at least one positive and at least one
negative physical diameter row.

Let the retained opposite shore have cuts sigma_1,...,sigma_n. Use the current
four-host cyclic order

    I_A^+, I_B^+, I_A^-, I_B^-.                           (2)

On the two A-host intervals the B-layer is constant at the two opposite extreme
values 0,n. On the two B-host intervals the A-layer is constant at the two
opposite extreme values 0,m.

## 2. Internal A-support forces full B-support

Call a simple staircase edge (a,b) internal when

    0 < a < b < m.                                        (3)

Take any physical actual-diameter row g=yz with this A-support. Both endpoints
of g have internal A-layer, so g is vertex-disjoint from both guards h_-,h_+.

The boundary-layer order from the sign-nesting theorem is

    0,1^+,...,(m-1)^+,m,(m-1)^-,...,1^-.                  (4)

Accordingly the convex-hull boundary is split by v,x_-,x_+ into the two side
arcs from v to x_- and from x_+ to v, plus the far A-layer-m arc between
x_- and x_+.

Because actual diameter edges form a convex thrackle, g must cross both
vertex-disjoint guard edges v x_- and v x_+. A chord crossing both chords that
share v has one endpoint on each of the two side arcs adjacent to v. This is the
ordinary alternating-endpoint criterion: an endpoint on the far arc would make
simultaneous crossing of both guard chords impossible.

Thus the two internal endpoints of g lie on opposite A-side arcs. By the
four-host order, internal A-layer points on those two arcs lie on the two
opposite A-host intervals I_A^+ and I_A^-. Their B-layers are therefore 0 and n.
Exact laminar B-support gives

    0 < a < b < m  =>  g is full-support on the B-shore.  (5)

This statement holds for every physical row over an internal staircase edge,
not only for a selected representative.

Let I be the number of internal simple staircase edges. Each such support type
has at least one row of each strict transverse sign, hence at least two distinct
physical rows. Therefore

    N_full^B >= 2I.                                       (6)

The complete-grid rank theorem independently gives at least

    N_prop^B >= n-2                                       (7)

distinct nonempty proper-support diameter rows on B. Full-support and
proper-support rows are disjoint, so if h is the total number of actual diameter
edges,

    h >= n + 2I - 2.                                      (8)

If B is exact phase, the existing N_prop^B >= n-1 form sharpens this to

    h >= n + 2I - 1.

## 3. The complementary support is one boundary star run

Put

    s := m-I.                                             (9)

Because the staircase starts at (0,m) and each step changes exactly one endpoint,
its noninternal edges form one initial run. If the first proper step changes b,
every proper noninternal edge is of the form (0,b). If the first proper step
changes a, every proper noninternal edge is of the form (a,m). Once both
endpoints become internal they remain internal.

Hence the s noninternal support classes form one initial one-sided boundary-star
run.                                                        (10)

If I=0, the whole simple staircase tree is an endpoint star.

Every support class in this run has at least two physical representatives, one
of each strict transverse sign. Each representative has one endpoint in the
common extreme A-layer. Thus the centered A-extreme layer carries at least

    2s                                                     (11)

selected actual-diameter endpoint incidences.

Since I+s=m, exactly one of the following alternatives holds:

    I >= m/2,                                              (12a)

or

    s > m/2.                                               (12b)

In the first case, (6) and (8) give

    N_full^B >= m,
    h >= n + m - 2.                                       (13)

In the second case, more than half of the simple staircase support classes belong
to one ordered endpoint-star run, and the common extreme A-layer carries more
than m selected diameter endpoint incidences.

At the current open-cell extraction m=Omega(D), so both branches are linear.

## 4. Counterexample pressure and scope

The earlier strong-SCC packet fork gave only a linear opposite-full-support packet
or a square-root extreme-layer carrier packet. Equations (5)--(13) identify the
source of those alternatives exactly: a terminal internal suffix of the maximal
staircase versus one initial one-sided boundary-star run.

The boundary-star branch cannot be rejected from diameter support alone. The
nonconstant star regression already on main realizes a bidirected endpoint-star
gap graph after dropping the actual contact, full-KKT, and global-optimality
hypotheses. Likewise, the threshold audits show that a large transverse
full-span diameter family is not by itself a convex-thrackle contradiction.

Therefore this note does not claim C-II closure. It narrows the surviving
strong-SCC branch to two explicit source geometries.

## 5. Target-C frontier

After composing with the two predecessor open-cell notes, the nonconstant
open-witness-cell route is reduced to:

1. inverse-D inactive near-unit or near-diameter activity; or
2. an internal-heavy paired staircase with at least m B-full-span diameter rows
   and h >= n+m-2; or
3. a boundary-heavy paired staircase with more than m/2 simple support classes
   in one ordered endpoint-star run and more than m selected diameter incidences
   at its center layer.

The exact next obligations are correspondingly narrow:

- internal-heavy: couple the linear B-full-span family and edge lower bound to
  opposite-shore contact equilibrium or source currency;
- boundary-heavy: use the ordered paired-sign endpoint-star run together with the
  actual contact/KKT co-embedding to force release or a strict competitor;
- inactive-near-activity: convert the inverse-D inactive pair into source currency
  or a strict competitor.

No computation, verifier, numerical experiment, or CI result is used as a proof
premise.
