<!-- theorem-state: {"artifact_id":"ART-C3B40AF18E9A","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: hub-owner recurrence is paid, but the O--O supply can vanish

Date: 2026-10-06. Authority: main
`583203ac1dc1d7bc49f0ca0574d75e85f9de2ee1`, state `2026-10-05.audit.62`.
Research predecessor: `7c41287726f1c34a282f13c0da613bde15154ccb`.
Classification: **proved candidate synthesis awaiting independent audit**;
abstract obstruction packets are **regressions**, not source configurations.
C-II and Level I remain open. No literature import is used.

## 1. The exact composition

The predecessor bounds selected narrow-window O--O owners by `b/2`. The
canonical finite good-end theorem gives a much smaller bound:

\[
 T_{\rm OO}\le x_B+m_B+2\quad\hbox{for any selected O--O family},
 \tag{1}
\]
\[
 \boxed{T_{\rm OO}\le x_B+m_B+1}
 \quad\hbox{in a projective window of width }<\pi/3.
 \tag{2}
\]

In the disjoint-crosscut narrow-window system, let `K_own` count distinct
nonzero owner translations. Let `c_i` count connected components of dual
regions carrying owner `i`, and put

\[
 \rho_{\rm own}=\sum_{i=1}^{K_{\rm own}}(c_i-1).
\]

Then

\[
 \boxed{K_{\rm own}+\rho_{\rm own}\le x_B+m_B+1.}
 \tag{3}
\]

For a nonempty owner population this in particular gives the requested
canonical defect payment

\[
 \boxed{\rho_{\rm own}\le x_B+m_B.}
 \tag{4}
\]

The implication is

`good-end intersection theorem + exact bad terminal bank -> selected O--O
population and owner recurrence bounds -> no linear O--O owner family when
x_B=o(D)`.

This proves a supply limitation. It does not construct a beneficial family.
In the small-outer-defect case the *whole selected motion population*, not
only its obstructions, is sublinear. A comparison requiring linearly many
such owners cannot close that case without a new extraction theorem.

## 2. Complete proof of the terminal and recurrence bounds

Canonical `C-LINEAR-NONMATCH`, Section 61.5, proves that any two complete
trains with two good hull ends have alternating end pairs on the convex
hull and therefore cross. Section 61.2 proves that crossings require
projective direction separation greater than `pi/3`, and three complete
trains cannot cross pairwise. Thus at most two complete trains have two
good ends globally, and at most one in the present narrow window.

Every other selected O--O train has at least one bad outer terminal
occurrence. Choose one. Complete stopped trains partition physical contacts
and their terminal occurrences, so this choice is injective into the bad
occurrence bank. The canonical exact bank is

\[
 B_{\rm bad}=x_B+m_B,
\]

as rechecked in the audit.52 hull-depletion promotion and audit.55 singleton
promotion. This proves (1) and (2). Singleton bridges have two outer
occurrences; at least one is bad, so they are included.

The narrow-window crosscuts have a tree dual with `T_OO+1` regions. Choose
a reference region with zero translation. A component of regions carrying
each nonzero owner has at least one region. Different components have
different chosen regions, and none is the reference region. Therefore

\[
 \sum_i c_i=K_{\rm own}+\rho_{\rm own}\le T_{\rm OO}.
\]

Combining this with (2) proves (3) and (4). This permits repeated labels
and branching. It does not assume owners are connected.

An explicit injection for (4) is also available. Root the tree at the
reference region and charge a chosen region of each extra owner component
to its parent cut. These parent cuts are distinct. If the unique fully
good cut would be charged, choose its nonzero child component as that
owner's representative component instead. If its child is fixed it was
not charged in the first place. Every remaining charged cut has a chosen
distinct bad terminal occurrence. The argument uses genuine nonzero cuts;
a selected cut with zero increment can simply be omitted.

## 3. Audit of the predecessor hub and bandwidth arguments

In the assumed proper disjoint-crosscut occurrence disk, an actual diameter
edge has one dual-tree support path. Two disjoint actual diameter edges
have alternating extreme endpoints; a cut separating their two disjoint
support paths would separate those alternating endpoint pairs into
disjoint boundary intervals, impossible. Edges sharing an endpoint have
support paths meeting at its region. Tree Helly supplies a common region.

Every nonhub branch is one shore of its first crosscut, hence has one
cyclic loaded interval and no complete actual diameter pair. Audit.62
makes every loaded-loaded lower witness a hull side, giving at most two
such witnesses leaving a branch. This is a statement about physical
endpoint regions, not contracted owner labels.

The tube proof for fourteen non-singleton cuts also survives: a separating
non-singleton midpoint cut meets the straight witness segment in a strict
rhombus; distinct selected cuts use distinct rhombi in the narrow window.
Each rhombus has area greater than `sqrt(3)/2`, diameter below `sqrt(3)`,
and lies in the segment's `sqrt(3)` tube. The predecessor's area estimate
and rational constant calculation follow. Singleton cuts spend the bad
bank. Concatenated Horn clauses are still not bounded by one tube.

These personally checked statements remain candidates pending an
independent audit. No state promotion is made.

## 4. Overlap-aware root and implication accounting

Impose the predecessor's acute *binary* hypotheses: every old contact is
unit for every binary selection, distinct nonzero translations are acute,
and all retained train increments are nonzero. Across a contact between
moving owners `i,j`, the mixed squared-norm difference would be
`-2 Delta_i dot Delta_j=0`, impossible. Adjacent dual regions with equal
translations would have zero cut increment. Hence every selected cut
joins a zero region to exactly one nonzero owner. Assign the train to
that owner. This partitions the selected train set into disjoint banks
`T_i`, with

\[
 \sum_i T_i=T_{\rm OO}.
\]

Every outer run of owner `i` uses two boundary occurrences from its bank,
so its loaded run count satisfies `r_i<=T_i`. Every unary rhombus root of
`i` is supported by a train in *that same bank*. Consequently, for any
set `I` of loaded implication/outer-unary owners and set `J` of rhombus
root owners,

\[
 \boxed{\sum_{i\in I}r_i+|J\setminus I|\le T_{\rm OO}.}
 \tag{5}
\]

An owner in `I intersect J` is charged through its run count once. The
fact that it has both roles does not prove it consumes another train.
Equation (5), not addition of the two separate bank bounds, is the
overlap-aware statement justified by the hypotheses.

The more elementary union bound `|I union J|<=T_OO` follows when every
member of `I` has a loaded occurrence. Outer tails with unloaded moved
endpoints require separate endpoint currency. All these populations are
sublinear when `x_B=o(D)`; that still does not supply a useful pin.

## 5. Small exact obstruction search

The exact script
`research/verify_target_c_hub_owner_systems_2026_10_06.py` enumerates ordered
trees, zero/moving acute-binary incidence, repeated owner labels, physical
loaded-cycle witness roles, run/terminal budgets, and odd convex-thrackle
hub support. It independently rechecks Horn closure against truth tables.

It finds a binary-only zero-only packet first at four selected trains.
A hub star with leaf labels `A,B,A,B` and loaded word `0,A,B,A,B` supports
three different hull sides with roles

\[
 A\to B,\qquad B\to A,\qquad\neg(A\wedge B).
\]

Both owners have two loaded runs; `K_own+2=4=T_OO`. Take `m_B=x_B=3`.
The bad bank has six occurrences and pays the selected trains and owner
recurrence. The odd pentagram diameter graph has all paths through the
hub and no old diameter within a leaf branch. Each branch has at most
two loaded cycle edges leaving it; every lower witness has tree span two.
The inactive exception bank is empty. There is no excess demand.

A single owner with one explicit unary rhombus prohibition already blocks
its pin with one train, zero bad terminals and no inactive upper exception.
This is the smallest abstract unary obstruction.

These packets are **not** asserted to have source coordinates or KKT
equilibrium. In particular, the apparent beneficial pins have not been
realized. They refute the proposed inference from the encoded topology,
Horn and terminal constraints alone. They do not refute a theorem using
additional actual-source geometry.

## 6. Why audit.53 returns do not yet remove these packets

For a pentagon, the promoted face demand is

\[
 r_f=\max\{0,\lfloor(5-4)/2\rfloor-\ell_f\}=0.
\]

Even a linear pentagon bank creates no positive demand in this particular
quota theorem. The stronger full-boundary separator theorem can yield
returns *from that pentagon*, but does not require their endpoints to lie
outside its owner's branch. Nor does the joint bulk/face theorem identify
owner-component recurrence with selected face or bulk starts.

To use hub pruning with returns one must prove that a specified owner
obstruction supplies distinct starts whose *permitted target endpoints*
lie across a specified separator. Existence of unrestricted returns to
the entire loaded set is not this statement. It cannot be charged to a
hub separator until that missing localization is proved.

## 7. Exact remaining obligations

The immediate strengthened target is an actual-source extraction/repair
theorem: replace the lost linear O--O supply by compatible motions of
outer-to-bounded trains and their exceptional-face closure equations, or
prove a contradiction for the remaining small O--O population using
actual active-diameter truth tables and rhombus slack.

Audit.56 supplies a *local cage*, not arbitrary simultaneous shortening
signs. No model of the lower formula alone is a finite competitor. Every
candidate endpoint still needs all old diameter and inactive-upper tests,
every unary rhombus test, full-source lower tests, and actual shortening.

Large-defect spending, crossing multishears, and the macroscopic inactive
container remain unclosed. The one-strict-spare-site candidate from PR
#722 passes its finite deletion proof, but no surplus packet exists here.

## 8. Classification and validation

| Claim | Classification | Dependencies |
| --- | --- | --- |
| Selected O--O bounds (1)--(2) | Proved candidate synthesis | C-LINEAR-NONMATCH; exact audit.52/55 bad-occurrence bank |
| Owner recurrence (3)--(4) | Proved candidate | Personally checked disjoint-crosscut tree; (2) |
| Overlap-aware allocation (5) | Proved candidate | Binary acute contact preservation; train terminal partition |
| Encoded constraints force a useful Horn model | Rejected abstract inference | Exact packets in the certificate |
| Every large source has a useful O--O family | Unproved | Not supplied by the above canonical inputs |
| C-II or Level I closure | Unproved | Full-core and container obligations remain |

The verifier uses integer Boolean/tree arithmetic. Its finite search is
not a source realization, asymptotic existence theorem, or optimality
certificate. Output is preserved in
`research/target_c_hub_owner_systems_certificate_2026_10_06.json`.
Promotion recommendation: retain as unreviewed research pending independent
audit. The active state and prompts remain at audit.62.
