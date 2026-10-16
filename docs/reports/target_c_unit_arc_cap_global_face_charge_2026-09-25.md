<!-- theorem-state: {"artifact_id":"ART-A6F191712D3B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — global face charge for unit-arc harmonic caps

**Date:** 2026-09-25  
**Repository commit:** `404e8d49ddb1ee14cd0f69a83e7f120e77b3ab33`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing-proof attempt and exact source-graph reduction  
**Target:** C-II full-core branch  
**Starting status:** canonical Sections 60, 62, 63, 83, 122--123 and the promoted full-core loaded-chord theorem  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** no theorem imported  
**Computation:** not used

## LEVEL I STATUS

STILL OPEN.

## 1. Exact endpoint and implication chain

The current full-core source obstruction is the aggregate detour of actual
harmonic-cell outer walks, coupled to the loaded-hull/diameter currency.
Open PR #585 charges a long unit-arc cap's *augmented* closing-chord face
to `e_BB-k`. The candidate chain here is stronger:

```text
actual unit-arc harmonic cap with long nonunit closing chord
    -> graph-free chord and an actual contact route facing it
    -> bounded-face degree Q or global outer-walk excess x_B
    -> q-2k = Q+x_B source-topology capacity
    -> hoped-for exclusion of a macroscopic cap-diameter tail.
```

The first three arrows are proved below. The final exclusion does not
follow: the live high-surplus branch permits `q-2k` to be linear.

## 2. Scope and notation

Let `A` be a canonical contact-minimal, then diameter-pair-minimal,
triangle-free global-minimizer representative in the sufficiently large
full-core near-disk Type-II branch. C-I gives `C=C_*`, so every unit
contact of the source belongs to the positive-contact graph `G`. Let
`F=conv(B)` be the loaded force hull; its loaded vertices `B` are in
strictly convex position.

A **unit-arc cap cell** is an actual harmonic attachment cell
`P_r=conv(A_r)` such that its attachment vertices are a consecutive
interval `a=p_0,p_1,...,p_M=b` on `partial F`, all `M` hull sides
`p_{i-1}p_i` are unit contacts, and the closing side `ab` has length
`ell_r>4`. The cell `P_r` is the convex hull of that interval and lies
on one side of line `ab`. Its unloaded component `I_r` is connected and
attached to every vertex of `A_r`. The promoted loaded-chord theorem says
that every loaded-loaded unit contact is a side of `F` in this branch.

Write `q=|B|`, `b` for the occurrence-counted outer-face walk length of
`G`, `x_B=b-q`, `Q=sum_{bounded nonquadrilateral faces}(degree-4)`, and
`k=d_H+s_Z`. Canonical Section 63 gives

\[
\boxed{q-2k=Q+x_B.}
\tag{GF.1}
\]

The cap family below may be any finite collection `S` of distinct cells
with these properties. Their interiors are disjoint by canonical
Section 83. Contact-isolated source points are retained; they carry no
contact edge and do not affect the plane graph argument.

## 3. Strict interior and graph-free chord lemmas

### Lemma GF.2 — no unloaded component vertex lies on its attachment polygon

Every vertex of `I_r` lies in `int(P_r)`.

**Proof.** Canonical Section 62 gives `I_r subset P_r`, at least three
distinct attachments, and positive harmonic equilibrium at every
unloaded component vertex. If `u in I_r` lies on a supporting line of
`P_r`, all its contact neighbors lie in `P_r`. A strictly positive
weighted average of their positions equals `u`; hence every neighbor
lies on the same supporting line. Unit separation allows at most one
unit-contact neighbor on each side of `u` along that line, and positive
equilibrium requires both. Thus `u` has exactly two collinear contact
neighbors and no contact edge leaving the polygon side. Repeating this
argument along the connected unloaded component keeps every vertex of
`I_r` on the same side. The resulting unit path can attach only to the
two loaded vertices at that side's endpoints, contradicting
`|A_r|>=3`. Therefore no such `u` exists. `square`

### Lemma GF.3 — the open closing chord meets no contact graph

The relative interior of `ab` contains no vertex or edge of `G`, and
no edge of `G` crosses it.

**Proof.** Lemma GF.2 excludes vertices and internal/attachment edges
of `I_r` on the side `ab`. Any other unloaded component `I_s` and all
its attachment edges lie in `P_s`; Section 83 gives
`int(P_s) cap int(P_r)=empty`. A segment of `P_s` crossing the open
side `ab` into `int(P_r)` would make the interiors of the two
two-dimensional convex cells intersect near the crossing. A segment
lying along `ab` would require an unloaded vertex on `partial P_s`,
contrary to Lemma GF.2, or a loaded-loaded unit chord `ab`, impossible
because `ell_r>4`. Finally all other loaded-loaded unit contacts are
hull sides by the promoted loaded-chord theorem and cannot cross an
internal chord of the convex hull. C-I says these cases exhaust the
source contact edges. `square`

## 4. One cap: bounded-face or outer-walk payment

### Theorem GF.4 — exact face dichotomy

For each unit-arc cap cell, the open chord `ab` lies in one face
`F_r` of the actual positive-contact graph. There is an
occurrence-counted `a`-to-`b` subwalk `W_r` on the boundary of `F_r`
whose internal vertex occurrences are all unloaded vertices of `I_r`,
and

\[
|W_r|\ge\lceil\ell_r\rceil.
\tag{GF.2}
\]

Consequently exactly one of the following applies:

1. `F_r` is bounded and has degree at least `2 ceil(ell_r)`, so its
   contribution to `Q` is at least `2 ceil(ell_r)-4`;
2. `F_r` is the outer face and `x_B>=ceil(ell_r)-1`.

**Proof.** The unit hull-side arc `Gamma_r` from `a` to `b` is in `G`.
Connectivity of `I_r` supplies a simple contact path `Pi_r` from `a`
to `b` with all internal vertices in `I_r`. Lemma GF.2 puts its
interior strictly inside `P_r`, so `Gamma_r union Pi_r` is a Jordan
cycle. The open chord lies on the side of `Pi_r` opposite
`Gamma_r`. The component of `int(P_r)\setminus G` touching the chord
has an occurrence-counted boundary route from `a` to `b` through
`I_r`: the Jordan cycle keeps that boundary away from the hull arc,
and there is no other component graph inside `P_r`. Call the route
`W_r`. Lemma GF.3 makes it a subwalk of the boundary of the *global*
face containing the chord; outside graph edges cannot enter the region
between `W_r` and the chord. Every edge of `W_r` is a unit contact,
so the triangle inequality proves (GF.2).

If that face is bounded, its occurrence-counted boundary has another
`b`-to-`a` subwalk in addition to `W_r`. Its unit edges also require
at least `ceil(ell_r)` occurrences. Thus the face degree is at least
`2 ceil(ell_r)>4`, and its degree-above-four defect belongs to `Q`.
If the face is outer, `W_r` appears in the outer boundary walk. Every
loaded vertex is also on that walk at least once, because it is an
extreme vertex of `F` and the entire contact graph lies in `F`.
The `|W_r|-1` internal unloaded vertex occurrences are additional to
these `q` loaded occurrences. Hence `b>=q+|W_r|-1`, giving the
outer-face alternative. `square`

The proof never assumes the full outer walk is a simple cycle or that
diameter edges form an Euler path. Bridges and repeated occurrences are
retained in the walk lengths.

## 5. A family of caps: one actual global currency

### Theorem GF.5 — additive cap-face charge

For any family `S` of distinct unit-arc cap cells,

\[
\boxed{\quad
q-2k=Q+x_B
\ge\sum_{r\in S}\bigl(\lceil\ell_r\rceil-4\bigr).
\quad}
\tag{GF.3}
\]

Every side of `F` has length at least one, so `q<=per(F)<=pi D`.
Thus (GF.3) also gives the finite source inequality

\[
\boxed{\quad
2k+\sum_{r\in S}\lceil\ell_r\rceil
\le\pi D+4|S|.
\quad}
\tag{GF.3a}
\]

**Proof.** Partition `S` according to whether `F_r` is bounded or
outer. The routes `W_r` use pairwise disjoint physical contact edges:
their internal vertices belong to distinct unloaded components, and
their endpoint attachment edges are distinct. If several bounded
routes belong to the same face, their edge occurrences occupy disjoint
parts of that face's boundary walk. For each bounded face used by the
family, its degree is at least the sum of `|W_r|` assigned to it;
subtracting four for that face costs at most four per assigned cap.
Therefore

\[
Q\ge\sum_{r:F_r\text{ bounded}}(|W_r|-4).
\]

For outer routes, their internal unloaded vertex occurrences are
distinct (including multiplicity within each walk) and are additional
to the `q` loaded vertex occurrences. Thus

\[
x_B\ge\sum_{r:F_r\text{ outer}}(|W_r|-1).
\]

Combine these inequalities, use (GF.2), and weaken the outer subtraction
from one to four. Equation (GF.1) gives (GF.3). `square`

If `|S|=o(D)` and
`sum_{r in S} ell_r >= cD` along a survivor sequence, (GF.3) forces

\[
\limsup {k\over D}\le{\pi-c\over2}.
\tag{GF.4}
\]

This is a source-level restriction on the Woodall/mixed-stress defect,
not a contradiction: the canonical stack has no matching positive
lower bound on `k/D` in the high-surplus full-core regime.

### Corollary GF.6 — a cap-tail floor for the full-core surplus

Let `m_B` be the number of nonunit sides of the loaded force hull and
`c_I` the number of unloaded positive-contact components. The promoted
loaded-chord theorem gives `e_BB=q-m_B`; the canonical pinned ledger
`c_I+e_BB+s_C=q-2+k` therefore yields

\[
\mu_DD:=e_{BB}+2s_C-3k
=q+m_B-k-2c_I-4.
\tag{GF.6a}
\]

Substituting (GF.3) into (GF.6a) gives the **finite** inequality

\[
\boxed{\quad
\mu_DD\ge
{q+\sum_{r\in S}\lceil\ell_r\rceil\over2}
+m_B-2c_I-2|S|-4.
\quad}
\tag{GF.6}
\]

In particular, along a canonical full-core sequence with `q/D->pi`,
`|S|=o(D)`, and `liminf D^{-1}sum_{r in S}ell_r>=c`, canonical
Section 75 gives `c_I=o(D)` and hence

\[
\boxed{\liminf\mu_D\ge(\pi+c)/2.}
\tag{GF.7}
\]

If `c>pi/5`, the right side exceeds `3pi/5`. Therefore a cap family
of this size cannot be used to realize the below-`3pi/5` low-surplus
window in an asymptotically all-unit, near-circular loaded hull.
The regular-polygon thin-cap regression of PR #583 uses all unit hull
sides and permits `c=mu_TC-1=0.637562...>pi/5`; if those geometric
caps were actual source cells, (GF.7) would force
`liminf mu_D>=1.88957...`, above the `3pi/5=1.88495...` split.
This conditional statement does not identify that geometric partition
with a canonical source and does not bound `mu_D` from above.

The same finite inequality has a useful **global outer-walk escape**
form without assuming `q/D->pi`. Section 63 gives
`u_B=x_B-m_B=b-q-m_B` and `b>=P_F:=per(F)`. Rearranging (GF.6),

\[
\boxed{\quad
u_B-m_B\ge
P_F-2\mu_DD+\sum_{r\in S}\lceil\ell_r\rceil
-4c_I-4|S|-8.
\quad}
\tag{GF.8}
\]

In the near-disk branch `P_F/D->pi`. Thus if `|S|=o(D)`, its cap
chords total at least `cD`, and `limsup mu_D<=mu_0`, then

\[
\liminf {u_B-m_B\over D}\ge\pi-2\mu_0+c.
\tag{GF.9}
\]

Whenever `c>2mu_0-pi`, a low-surplus cap tail forces a **linear
extra global outer-walk surplus**, even if `q/D` is smaller than `pi`.
This is the precise remaining source-level escape in that window;
neither Section 63 nor (GF.8) turns it into a strict sub-`D`
configuration.

There is a sharper finite exclusion when the bounded chord faces are
pairwise distinct and none is outer. Then the two routes of GF.4 can be
charged independently in `Q`, giving

\[
\boxed{\quad
2k+2\sum_{r\in S}\lceil\ell_r\rceil
\le q+4|S|\le\pi D+4|S|.
\quad}
\tag{GF.5}
\]

In particular, no canonical sequence can have such a family with
`|S|=o(D)` and `liminf D^{-1} sum_r ell_r>pi/2`. If a family has more
than `(pi/2+o(1))D` total chord length, its chord faces must therefore
share a bounded face or include an outer-face chord. The shared-face
case is precisely why the single-cap factor two cannot be summed in
GF.3 without an extra hypothesis.

## 6. Regressions and failed closure steps

The regular odd unit shell is a binding regression. It has `k=2`,
`q/D->pi`, and large actual bounded-face defect, so it shows that
`q-2k` can have coefficient `pi`. It has no harmonic cap cell and is
not a global-minimizer certificate, but it prevents replacing the
right side of (GF.3) by `o(D)` from source geometry or KKT rank alone.

The abstract shallow caps in PR #583 have no positive-contact component;
they cannot be inserted into Theorem GF.5 as actual cells. Rescaling
their width does not manufacture an attached contact network. Open
PR #585 gives a local augmented-graph charge; the present theorem
charges the **actual** bounded-face or outer-walk currency and includes
all repeated boundary occurrences. Neither report identifies a
strict source-preserving sub-`D` motion.

The attempted final step was to combine (GF.4) with a universal
`k/D>=kappa>0` large enough to contradict a linear cap tail. No such
lower bound is canonical; `k` may remain sublinear in the Woodall cyclic
branch. Thus this route currently narrows the cap-diameter mechanism
and eliminates the distinct-bounded-face subbranch beyond `pi D/2`.
It also rules out a `c>pi/5` cap tail as an explanation of the
below-`3pi/5` surplus window when `q/D->pi`,
and (GF.9) forces linear global outer-walk surplus if that hull-vertex
density is lost,
but does not eliminate all of Type II, the inactive-container branch,
or Level I.

## 7. Exact remaining lemma and promotion recommendation

A sufficient cap-specific next theorem would be: for some fixed
`c>0`, every canonical Type-II survivor with a sublinear family of
unit-arc caps of total closing-chord length at least `cD` has

\[
\liminf k/D>(\pi-c)/2.
\]

Together with (GF.4), this would exclude that entire cap family.
The statement is deliberately source-specific; the odd-shell
regression shows why the lower bound cannot come from near-disk hull
geometry and positive KKT equilibrium alone. Other full-core cell
shapes and the macroscopic inactive-container branch would still need
separate closure.

**Classification:** GF.2--GF.5 are proved candidates awaiting an
independent planar-topology audit. No canonical theorem-state, route,
or prompt file is changed. An audit should scrutinize the chord-side
face-boundary route in GF.4, the no-crossing use of Section 83, and the
occurrence injection when several caps share one bounded face.
