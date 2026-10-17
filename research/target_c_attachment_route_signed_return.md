<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "0aa63784c4af137c1b8a783d912cfc84339812c1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_attachment_route_signed_return.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "09e68a681c525e682e9febfdd747539bb311a9efb2938a121b16bccc89aa1c6f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — attachment-route signed return

**Date:** 2026-09-12  
**Status:** proof-only research theorem; theorem-state authority unchanged  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The two-arc zero-host theorem spends the occurrence-counted outer walk in only two
routes.  For the all-regime problem there is a more source-specific decomposition:
cut the outer walk at **every consecutive attachment vertex** of one harmonic cell.
The displacement terms then add to the actual perimeter of the attachment polygon.
Every bounded nonquadrilateral face is still a closed zero-displacement route.

This gives the exact finite currency

\[
E_{\rm att}:=L+P_{\rm exc}-\operatorname{per}(P),
\]

and transports all strict-rhombus train return into that same physical route excess.
No train endpoint is discarded and no physical boundary occurrence is charged twice.

The result is

\[
\boxed{
E_{\rm att}
\ge \sum_{\tau\in\mathcal T}
\bigl(2-w_{Q_{\rm att}}(u_\tau)\bigr),
}
\tag{AR.1}
\]

and, after exact train-span transport,

\[
\boxed{
 d E_{\rm att}
\ge
\sum_{R\in\mathcal R}\operatorname{area}(R)
\left[
4-w_{Q_{\rm att}}(u_R)-w_{Q_{\rm att}}(v_R)
\right].
}
\tag{AR.2}
\]

Here `P` is the convex attachment polygon, `d=diam(P)`, `mathcal R` is the full
strict-rhombus complex in the harmonic component, `mathcal T` is its set of complete
local trains, and `u_R,v_R` are the two train directions crossing in `R`.

Using the exact face ledger, the left side is also

\[
\boxed{
E_{\rm att}
=4a-6-2s-2c+4f_{\rm exc}-\operatorname{per}(P).
}
\tag{AR.3}
\]

Thus the unresolved all-regime signed-return problem can be stated without a coarse
outer-walk baseline: the lower side of the desired comparison is an explicit weighted
return functional of the actual attachment-route host directions, and the upper side
is the actual route excess above the attachment polygon perimeter.

---

## 1. Setup

Fix one canonical harmonic component `I` with attachment set

\[
A=\{p_1,\ldots,p_a\}
\]

listed cyclically on

\[
P:=\operatorname{conv}(A).
\]

Let `H` be the induced positive-contact graph on `I\cup A`.  Retain the standard
local notation

- `L` = occurrence-counted outer-face walk length of `H`;
- `Q=\sum_f(\deg f-4)` over bounded faces;
- `s=e+t-2|I|-1>=0`;
- `c` = number of loaded-loaded contacts with both endpoints in `A`;
- `f_exc` = number of bounded nonquadrilateral faces;
- `P_exc=\sum_{f\,nonquad}\deg f`;
- `mathcal R` = all bounded strict-rhombus faces;
- `mathcal T` = all complete local train segments of `mathcal R`;
- `d=diam(P)`.

Canonical Section 82 gives

\[
L+Q=4a-6-2s-2c,
\tag{AR.4}
\]

and every physical boundary-edge occurrence of `mathcal R` faces either the old outer
face of `H` or one bounded nonquadrilateral face.  It also gives

\[
P_{exc}=4f_{exc}+Q.
\tag{AR.5}
\]

The consecutive-attachment outer routes are the same occurrence-counted routes used in
canonical Section 101.  Let `W_i` be the directed outer-walk route from `p_i` to
`p_{i+1}` (indices cyclic), with the bounded side on the left.  Write

\[
\ell_i=|W_i|,
\qquad
z_i=p_{i+1}-p_i,
\qquad
q_i={z_i\over |z_i|}.
\tag{AR.6}
\]

The attachment vertices are distinct, so `z_i!=0`.  The routes partition the
occurrence-counted outer walk and therefore

\[
\sum_i\ell_i=L,
\qquad
\sum_i|z_i|=\operatorname{per}(P).
\tag{AR.7}
\]

Orient every bounded nonquadrilateral face boundary clockwise.  Each such route is
closed and receives host `0`.

Define the finite host set

\[
Q_{att}:=\{q_1,\ldots,q_a,0\}\subset\overline{B_1(0)}
\tag{AR.8}
\]

and, for a unit direction `u`,

\[
w_{Q_{att}}(u)
:=\max_{q\in Q_{att}}q\cdot u
 -\min_{q\in Q_{att}}q\cdot u.
\tag{AR.9}
\]

Since every host has norm at most one,

\[
0\le w_{Q_{att}}(u)\le2.
\tag{AR.10}
\]

---

## 2. Exact route excess

For any directed unit-edge walk `W` with displacement `z`, assign

\[
q(W)=z/|z|\quad(z\ne0),
\qquad
q(W)=0\quad(z=0).
\]

Then

\[
|W|-|z|
=\sum_{e\in W}(1-q(W)\cdot v_e),
\tag{AR.11}
\]

where `v_e` is the directed unit step of the occurrence.  Every summand is
nonnegative.

Apply (AR.11) to all attachment routes and all bounded defect-face cycles.  The outer
routes contribute

\[
\sum_i(\ell_i-|z_i|)
=L-\operatorname{per}(P),
\]

while the closed defect cycles contribute their entire lengths, totaling `P_exc`.
Therefore their total exact excess is

\[
\boxed{
E_{att}
=L+P_{exc}-\operatorname{per}(P).
}
\tag{AR.12}
\]

This quantity is nonnegative before any asymptotics.

Using (AR.4)--(AR.5), the degree-excess variable cancels:

\[
\begin{aligned}
L+P_{exc}
&=(L+Q)+4f_{exc}\\
&=4a-6-2s-2c+4f_{exc}.
\end{aligned}
\]

Hence (AR.3) follows exactly.

---

## 3. Every physical train end has one route occurrence

Orient physical strict-rhombus boundary edges with the incident retained rhombus on
the left.

If a physical boundary occurrence faces a bounded nonquadrilateral face, the clockwise
orientation of that face has the same edge orientation.  Assign the train end to that
face-cycle occurrence.

If it faces the old outer face, the outer walk oriented with its bounded side on the
left has the same orientation.  That occurrence belongs to exactly one of the
consecutive-attachment routes `W_i`; assign the train end there.

Thus every physical end of every complete local train is assigned.  The assignment is
injective on physical occurrences: a physical boundary edge is terminal for exactly
one train, namely the train using that edge direction.  An outer-face bridge may occur
more than once in the outer walk; the occurrence adjacent to the retained rhombus is
the assigned occurrence and any other traversal remains unassigned.  This can only
increase the available route excess.

Hole boundaries require no separate convention: they face bounded
nonquadrilateral faces and are already assigned through those clockwise cycles.
Disconnected strict-rhombus components are also harmless because the train statement
is applied componentwise and all their physical ends enter the same occurrence
ledger.

No source point is removed or replaced in this construction.

---

## 4. Exact signed return on attachment routes

Take one complete train `tau`.  Its two terminal physical boundary orientations are
`u_tau` and `-u_tau`.  Suppose their assigned routes have hosts `q_i,q_j` in
`Q_att`.  Their two assigned summands in (AR.11) are

\[
(1-q_i\cdot u_\tau)
 +(1-q_j\cdot(-u_\tau))
=2-(q_i-q_j)\cdot u_\tau.
\tag{AR.13}
\]

By definition of width,

\[
(q_i-q_j)\cdot u_\tau
\le w_{Q_{att}}(u_\tau).
\]

Hence the two ends cost at least

\[
\delta_\tau
:=2-w_{Q_{att}}(u_\tau)
\ge0.
\tag{AR.14}
\]

The assigned endpoint occurrences are pairwise distinct.  Every unassigned route
occurrence contributes a nonnegative term to (AR.11).  Summing (AR.14) over all
complete trains therefore proves

\[
\boxed{
E_{att}\ge\sum_{\tau\in\mathcal T}\delta_\tau.
}
\]

This is (AR.1).

The case in which both ends lie on the same designated route causes no loss: then the
exact two-end contribution in (AR.13) is `2`, while `delta_tau<=2`.

---

## 5. Whole-area transport

For a train `tau`, let

\[
A(\tau):=\sum_{R\in\tau}\operatorname{area}(R).
\tag{AR.15}
\]

The canonical train-span identity says that `A(tau)` is exactly the transverse
displacement between its two terminal edge midpoints.  Both midpoints lie in the
convex attachment cell `P`, so

\[
\boxed{A(\tau)\le d.}
\tag{AR.16}
\]

Multiply `delta_tau` by `A(tau)` and sum over all trains.  Each strict rhombus lies on
exactly two trains, with its two train directions denoted `u_R,v_R`.  Therefore

\[
\begin{aligned}
&\sum_{R\in\mathcal R}\operatorname{area}(R)
\bigl(\delta_{\tau_u(R)}+\delta_{\tau_v(R)}\bigr)\\
&\qquad=\sum_{\tau\in\mathcal T}\delta_\tau A(\tau)\\
&\qquad\le d\sum_{\tau\in\mathcal T}\delta_\tau\\
&\qquad\le dE_{att}.
\end{aligned}
\tag{AR.17}
\]

Substitute

\[
\delta_{\tau_u(R)}+\delta_{\tau_v(R)}
=4-w_{Q_{att}}(u_R)-w_{Q_{att}}(v_R)
\]

to obtain (AR.2).

Because every summand in (AR.2) is nonnegative, the right side may be restricted to
any selected collection of rhombi.  In particular it can be restricted to the actual
linear-by-linear ordered complete grid from canonical Section 91 without charging any
physical route occurrence twice.

---

## 6. Hostile scope audit

The theorem uses no full-source affine-kernel statement.  Contact-isolated source
points remain part of the source and are untouched.  The theorem is a geometric
inequality on one positive-contact harmonic carrier; it is not promoted to a global
contradiction by deleting the rest of the source.

The following possible multiplicity failures are explicitly excluded.

1. **Repeated outer vertices.** Routes are occurrence-counted; cuts are at the
   canonical consecutive-attachment occurrences used by Section 101.
2. **Outer bridges.** Only the physical occurrence incident to a retained rhombus is
   assigned. Other walk occurrences remain as nonnegative excess.
3. **Defect-face endpoints.** Each bounded nonquadrilateral face is used once as its
   full clockwise cycle. Shared contact edges are separate face occurrences, while a
   physical train end has only one incident nonrhombic side.
4. **Train reuse.** Each physical boundary edge terminates one train only. The area
   regrouping counts each rhombus exactly twice, once for each crossing train.
5. **Loaded boundary vertices.** No assumption is made that route interiors are
   unloaded. Only the route endpoints and exact displacement are used.
6. **Nonquadrilateral holes.** They are included through their full closed cycles and
   hence through the single common zero host.
7. **Same-route train ends.** Equation (AR.13) remains valid and is stronger than the
   width lower bound.
8. **Source cardinality.** No point is moved, removed, or duplicated.

Thus (AR.1)--(AR.3) are finite source-level statements with the same endpoint-retention
requirements as the canonical Target C stack.

---

## 7. What this changes

The two-arc theorem gives a universal local return constant but spends only the
diameter-pair displacement `2d`.  The present theorem spends **all actual attachment
chords** and therefore replaces its raw outer-walk term by

\[
L+P_{exc}-\operatorname{per}(P).
\]

The price is that the host set now contains every attachment-chord direction, so there
is no universal positive lower bound for

\[
4-w_{Q_{att}}(u)-w_{Q_{att}}(v)
\]

over all two-direction rhombi.

This identifies the precise all-regime obstruction.  To close the full-core branch it
is enough to prove, on the same actual harmonic cell, that the ordered inverse-phase
train system forces the weighted return functional in (AR.2) to exceed

\[
d\left(4a-6-2s-2c+4f_{exc}-\operatorname{per}(P)\right).
\]

Any such theorem must use the distribution and capacity of the physical
attachment-route host directions; a uniform three-host constant cannot supply it.

**Theorem state:** unchanged. This file is proof-only pending independent hostile
audit and any lifecycle promotion.
