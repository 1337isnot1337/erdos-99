> Generated reading edition · [exact source](../../../docs/audits/target_c_centered_fan_blocker_closure_independent_audit_2026-10-08.md) · source SHA-256 `d0bcd14ea730e6ea5a6ace761b52af96ee6e056b2772fe431d9bd246d141d9e6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-37997D56E4BC","canonical":true,"claim_ids":["C-CENTERED-FAN-BLOCKER-DEPTH-PATH"],"claim_statuses":{"C-CENTERED-FAN-BLOCKER-DEPTH-PATH":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent Audit.152: centered-fan blocker paths reach macroscopic depth

**Date:** 2026-10-08  
**Audit base:** `d32a55f224e484609b1557bf5b8d531869b20558`, state `2026-10-08.audit.148`.  
**Frozen source:** `origin/research/target-c-fan-blocker-closure-20261005` at `ba8197f5c4ade5dbb55f3c5f138597e47a30191a`.  
**Source artifact:** `research/target_c_centered_fan_blocker_closure_2026-10-05.md`, blob `683e523a8aad8da73c04f75791521ccc566f1504`, SHA-256 `b4d3106a7ae373d05e48e10cbe02f2228f70fbbd2559e1e6c3d09c46b8288d31`.  
**Verdict:** PASS — promote the full-source blocker-path theorem below. CONDITIONAL ONLY — do not promote the face-localization and face-currency extension in source Section 7.  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Starting endpoint and exact implication

The canonical source is a contact-minimal, then actual-diameter-pair-minimal,
triangle-free global minimum-diameter source. Every source point is retained,
including contact-isolated points. The new implication is

```text
degree-two actual-diameter fan leaf
-> its full-source lower-blocker closure under the exact fan displacement
-> a near-unit source path to depth D/10, or a linearly long isolate prefix
-> a localized candidate obstruction, not yet a strict sub-D competitor
```

This does not force a large fan population. It also does not charge the paths
from different fan leaves disjointly.

## 2. Promoted statement

Let `A` be a finite triangle-free global minimum-diameter source with diameter
`D >= 10`, chosen contact-minimal and then actual-diameter-pair-minimal among
such global minimizers. Suppose `p` has exactly two unit-contact neighbors
`p_- , p_+`, and there is a source point `a` such that

```math
|p-a|=|p_--a|=|p_+-a|=D,
\qquad |p-p_-|=|p-p_+|=1.
```

Set `u=(p-a)/D`, `delta=1/D`, and define the support depth
```math
s(x)=u\cdot(p-x).
```
For distinct source points `x,y`, write `x -> y` if translating `x` by
`-delta u` would make an old strict pair no longer strict, or would shorten an
old contact below one:
```math
\begin{cases}
|x-\delta u-y|\le1,& |x-y|>1,\\
|x-\delta u-y|<1,& |x-y|=1.
\end{cases}
```

There is a path of distinct source points
```math
p=x_0\to x_1\to\cdots\to x_m
```
where `x_m` is the first vertex with `s(x_m) >= D/10`. For every edge,
```math
1\le |x_{j-1}-x_j|\le1+1/D,
\qquad s(x_j)-s(x_{j-1})>1/(2D),
```
and
```math
m\ge D/11,
\qquad
\sum_{j=1}^{m}(|x_{j-1}-x_j|-1)
<\frac1{10}+\frac1D+\frac1{D^2}.
```
The first edge is a strict old noncontact and satisfies
```math
1<|p-x_1|\le1+1/D,
\qquad
s(x_1)>\frac{\sqrt3}{2}-\frac1{4D}.
```

Consequently either the path reaches a nonisolated source vertex before its
first depth-`D/10` vertex, in which case the prefix to the first such vertex
has only contact-isolated internal vertices, or at least `D/11-1` distinct
contact-isolated vertices occur before depth `D/10`. In the latter case the
source contains `Omega(D)` distinct contact isolates on this path. The
assertion is per fan leaf; it gives no disjointness between paths chosen for
different leaves.

## 3. Independent proof reconstruction

### 3.1 The first blocker exists

Reflect `p` in the line through `p_- p_+`. The reflected point is
`p'=p-delta u`. For any fixed source point `y`, put `d=|p-y|`. The identity
```math
2(p-y)\cdot(p-a)=d^2+D^2-|y-a|^2\ge d^2
```
uses only that `a,y` are source points and `diam(A)=D`. Therefore
```math
|p'-y|^2-d^2
=-\frac{2(p-y)\cdot(p-a)}{D^2}+\frac1{D^2}
\le-\frac{d^2-1}{D^2}.
```
Every old strict pair incident to `p` strictly shortens. The two old contacts
at `p` remain unit contacts because each has distance `D` from `a`; there are
no other contacts at `p` by hypothesis. All other source pairs are fixed.

If no strict old pair becomes distance at most one, this is a same-cardinality
unit-separated triangle-free source with no new contacts, diameter at most
`D`, and the old diameter pair `pa` strictly shortened. A diameter below `D`
contradicts global minimality. At diameter `D`, either a contact was lost,
contradicting contact-minimality, or the contact count is unchanged and the
actual diameter-pair count is smaller, contradicting the secondary
normalization. Thus a strict-pair blocker exists and is exactly an outgoing
arrow from `p`.

This proof does not require a local motion radius, a KKT stress, or a
midpoint-concentration hypothesis. It is a finite full-source reflection.

### 3.2 Every arrow advances inward

For `r=x-y` and `d=|r|`, the arrow definition gives `d<=1+delta` by the
triangle inequality. If `d>1`, then
```math
0<d^2-1\le d^2-|r-\delta u|^2
=2\delta\,u\cdot r-\delta^2.
```
If `d=1`, the strict arrow condition gives the same final strict inequality.
Since `s(y)-s(x)=u\cdot r`, each arrow has
`s(y)-s(x)>delta/2`. The directed relation is acyclic, so each closure chain
has distinct vertices.

On every arrow,
```math
d^2-1\le2\delta(s(y)-s(x))-\delta^2.
```
Divide by `d+1 >= 2` and sum along a path to obtain
```math
\sum_j(d_j-1)\le\delta s(x_m)-m\delta^2/2.
```

### 3.3 A shallow closed blocker set is a finite competitor

Let `R` be closed under every arrow from a member of `R` to a point outside
`R`, and suppose `s(x)<H=D/10` for every `x in R`. Translate all points in
`R` by `-delta u` and fix the rest.

For a crossing pair, the closure condition prevents an old strict pair from
becoming distance `<=1` and prevents an old contact from becoming `<1`.
Pairs internal to `R` or its complement do not change. Thus the new source is
unit-separated, creates no new contact, and is still triangle-free. It may
lose old contacts, which only strengthens the contact-minimality contradiction.

To check the full-source upper bound, take a crossing pair `(x,y)` whose
distance increases. The increase implies
```math
s(y)-s(x)<\delta/2.
```
Hence `s(y)<H+delta/2` and the translated point `x'=x-delta u` has
`s(x')<H+delta`. Also `|x'-a|<|x-a|<=D`: indeed
```math
|x'-a|^2=|x-a|^2-2\delta(D-s(x))+\delta^2,
```
and `s(x)<D/10`, `D>=10` make the last two terms strictly negative.
Both `x'` and `y` lie in the cap
```math
\{z:|z-a|\le D,\ s(z)\le h\},\qquad h=H+\delta.
```
For any two points in this cap, their coordinates parallel to `u` differ by
at most `h`, and each perpendicular coordinate has magnitude at most
`sqrt(2Dh-h^2)`. Thus its squared diameter is at most
```math
8Dh-3h^2=D^2(8q-3q^2),\qquad q=h/D\le 11/100.
```
The function `8q-3q^2` is increasing on this interval and its endpoint is
`8437/10000 < 1`; the new crossing distance is strictly below `D`. A
nonincreasing crossing distance stays at most its old value. Therefore no
new actual diameter pair is created.

The carrier `a` is outside `R`, because `s(a)=D`. The old diameter pair `pa`
crosses the cut and shortens to `D-delta`. The translated source has the same
cardinality, diameter at most `D`, no more contacts, no new diameter pairs,
and has lost `pa`. This contradicts the canonical lexicographic choice:
diameter below `D` violates global minimality; at diameter `D`, a lost contact
violates contact-minimality; with the contact count unchanged, the lost `pa`
and absence of new diameter pairs violate diameter-pair-minimality.

So no all-shallow arrow-closed set containing `p` exists. Starting from `{p}`
and adding an arrow target while one exists must reach depth `H` in the finite
source. Its parent edges give the asserted path. The two fan contacts remain
exactly unit under the initial reflection, so the first arrow is a strict
old noncontact.

The first depth crossing overshoots by at most `1+delta`, since each depth
increment is at most its edge length. Thus
`s(x_m)<D/10+1+1/D` and `m(1+1/D)>=D/10`, which yields `m>=D/11` for
`D>=10`. Substitution into the accumulated-gap bound gives the stated
`O(1)` total gap-excess estimate. The first-edge depth estimate was checked
independently from the two fan-neighbor separation inequalities: if
`x_1=p-su+vt`, then
```math
4s^2+2\delta(1-\delta^2)s-3-\delta^2+\delta^4>0,
```
so
```math
s>\frac{-\delta(1-\delta^2)+
\sqrt{12+5\delta^2-6\delta^4+\delta^6}}4
\ge\frac{\sqrt3}{2}-\frac\delta4.
```

The path edges have length at most `1+1/D <= 1.1 < sqrt(2)`. The straight
segments for pairs of unit-separated source points of length `<sqrt(2)` cannot
cross properly: a crossing would make the two segments diagonals of a convex
quadrilateral, and a quadrilateral angle at least `pi/2` forces the opposite
diagonal to have length at least `sqrt(2)`. An endpoint cannot lie in the
interior of such a segment because its distance to one endpoint would be
less than one. Hence the path is an embedded near-unit path.

## 4. Scope and hostile checks

- **Full source and isolates:** the closure translates a subset but retains
  every label. The upper-cap argument checks every crossing pair against the
  actual diameter `D`; no contact isolate is dropped or silently fixed.
- **Finite motion:** the move is a common finite translation of the entire
  closure. No first-order velocity is used.
- **Globality:** the contradiction uses global diameter minimality and the
  canonical two-stage contact/diameter-pair tie-break. It is not a local or
  jammed-source argument.
- **No simultaneous-exchange inference:** one closed set is proved feasible
  all at once from its arrow closure and support-cap bound. The theorem does
  not combine separately feasible sets or assert distinct paths for several
  fan leaves.
- **No diameter-trail inference:** no path or Euler-trail conclusion is drawn
  from incident diameter edges. The path edges are the explicitly defined
  lower-blocker arrows.
- **Computed inputs:** no unreviewed computation or literature statement is
  used. There is no verifier dedicated to this new path theorem; its decisive
  estimates are derived above with exact inequalities.

### Source Section 7 is not promoted

The source claims a bounded-face localization and then charges a macroscopic
face to `Q-f` and to loaded-return currency. The proof-only dependency
`target_c_degree2_fan_exceptional_face_payment_2026-10-02.md` is not in the
canonical theorem stack, and this audit did not independently verify its
bridge-adjacent fan payment or the face-excess accounting. In addition, the
sentence that *every* propagation edge lies in `overline{G(p)}` exceeds the
argument: after a path first reaches a nonisolated boundary vertex, a later
edge may leave through that shared vertex without crossing a contact edge.
The argument establishes localization only for the prefix up to the first
nonisolated vertex. That prefix suffices for a conditional face fork, but the
fork and the `Q-f`/return conclusions are withheld. The source report remains
unreviewed outside the exact promoted path theorem.

## 5. Disposition and frontier effect

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Full-source blocker closure reaches support depth `D/10`; path, edge, and gap bounds in Section 2 | PASS | Promote as `C-CENTERED-FAN-BLOCKER-DEPTH-PATH`. |
| Core-hit versus `Omega(D)` isolate-prefix dichotomy | PASS | Include in the exact theorem scope and conclusion. |
| Section 7 bounded-face localization and face/return currency | CONDITIONAL ONLY | No canonical theorem entry; noncanonical face/payment dependency and an overbroad localization sentence remain. |
| Source report's implication that this settles C-II | Not claimed | C-II and Level I remain open. |

This theorem sharpens the per-leaf blocker consequence of
`C-CENTERED-FAN-REFLECTIONS`, but it does not bound the number of fan leaves,
make paths from different leaves disjoint, or produce a refill/source
competitor. The exact C-II finite-move/payment obligation is unchanged. Do not
refresh the active prompt.

## 6. Validation

No new computational certificate is registered. The exact source report and
tip above are frozen; the independent proof does not use its proposed
face-localization conclusion. Local validation passed: artifact-index
generation wrote 1,314 records and updated this audit header; generated views,
`check_theorem_state.py`, and `check_active_route_summaries.py` passed; the full
certificate runner passed all 78 unique registered certificates; and
`git diff --check` passed. These are promotion gates, not evidence for the new
analytic path theorem.

## 7. Exact next obligation

Use a specified per-leaf path family or a source-realized face fork to derive
either a canonical face/outer-walk charge with proved scope, or a full-source
finite replacement that passes every lower and actual-diameter upper pair.
The missing population/disjointness step remains explicit; the theorem gives
only one path per supplied fan leaf.
