# Hostile audit — bridge-deduplicated long-side contacts

**Date:** 2026-09-14  
**Reviewed:** `research/target_c_bridge_deduplicated_longside_contacts_2026-09-14.md`  
**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks the two places where the improved long-side count could silently
fail: outer-face occurrence multiplicity and the use of full-core area saturation to
control bridges.

## 1. Outer-face multiplicity is exactly a bridge issue

For a connected plane graph, an edge is a graph bridge if and only if its two edge
sides are incident to the same face.  Hence an edge on the occurrence-counted boundary
walk of the unbounded face behaves as follows:

- if it is not a bridge, exactly one edge side is incident to the outer face, so the
  physical edge contributes exactly one outer-face occurrence;
- if it is an outer bridge, both edge sides are incident to the outer face, so it
  contributes exactly two outer-face occurrences.

This remains true with articulation vertices and repeated boundary vertices.  The
multiplicity is an edge-side statement, not a vertex-simple-walk statement.

Therefore for any selected subset of `G` outer-face occurrences, if `E` distinct
physical edges occur in that subset and the whole graph has `B_o` outer bridges, then

\[
G\le E+B_o,
\]

so

\[
E\ge G-B_o.
\]

The bridge deduction in (BD.3) is occurrence-safe.  It is stronger than dividing by
two because nonbridges cannot be duplicated at all.

**Verdict:** PASS.

## 2. The bridge-isoperimetry theorem applies to the full positive core

The hostile-audited bridge-subtracted theorem gives for the full bounded-face union
`U`

\[
B_o\le {b-2\sqrt{\pi\operatorname{area}(U)}\over2}.
\]

In the canonical no-container full-core Type-II branch, the same hostile audit already
verified the area sandwich

\[
A_4\le\operatorname{area}(U)\le\operatorname{area}(F),
\]

with both endpoints equal to

\[
{\pi\over4}D^2-o(D^2).
\]

Thus

\[
2\sqrt{\pi\operatorname{area}(U)}
=\pi D-o(D).
\]

The distinguished outer-route partition uses the actual full-core outer-face walk, so

\[
b=\operatorname{per}(F)+d_{out}
=\pi D+d_{out}+o(D).
\]

Substitution gives exactly

\[
B_o\le {d_{out}\over2}+o(D).
\]

No selected-cell area saturation is being assumed.  The scope is the full positive
core, exactly where the bridge theorem's area premise is available.

**Verdict:** PASS.

## 3. Directional occurrence count composes without changing scope

The main directional-energy identity is finite on the same distinguished outer-route
partition:

\[
d_{out}=\sum_{i,j}(1-\cos\theta_{i,j}).
\]

Hence the number of bad occurrences at angular threshold `beta` is at most

\[
{d_{out}\over1-\cos\beta}.
\]

Long-side routes carry at least `L_{>2}` total occurrences, so after removing bad
occurrences there are at least

\[
G_\beta
\ge L_{>2}-{d_{out}\over1-\cos\beta}
\]

good occurrences.  Applying the physical bridge multiplicity bound to this same
subset gives

\[
E_{tan}(\beta)
\ge
L_{>2}
-\left({1\over1-\cos\beta}+{1\over2}\right)d_{out}
-o(D).
\]

There is no mismatch between an all-outer-face bridge count and a selected long-side
occurrence subset: using the total `B_o` only weakens the selected-subset estimate.

**Verdict:** PASS.

## 4. A stronger nonbridge corollary

For later phase/interface work it is useful to discard every outer bridge entirely.
At most `2B_o` selected occurrences lie on outer bridges, because each outer bridge has
exactly two outer-face occurrences.  Every remaining occurrence belongs to a
nonbridge, and distinct remaining occurrences correspond to distinct physical edges.
Therefore

\[
\boxed{
E_{tan}^{nb}(\beta)
\ge
L_{>2}-{d_{out}\over1-\cos\beta}-2B_o.
}
\tag{BA.1}
\]

Using `2B_o<=d_out+o(D)`,

\[
\boxed{
E_{tan}^{nb}(\beta)
\ge
L_{>2}
-\left({1\over1-\cos\beta}+1\right)d_{out}
-o(D).
}
\tag{BA.2}
\]

At `beta=pi/8`, the current low-`t` constants imply conservatively

\[
\boxed{
E_{tan}^{nb}(\pi/8)>0.3956D-o(D).
}
\tag{BA.3}
\]

Every edge in this cohort has the outer face on one side and a genuine bounded face on
the other.  Thus it is automatically one of:

1. a boundary edge of a strict unit rhombus, hence a terminal edge of a non-singleton
   stopped rhombus train; or
2. an edge incident to a bounded nonquadrilateral face, hence an exceptional-face
   boundary incidence.

This is a physical partition; bridges have already been removed.

The exact threshold needed merely to keep the nonbridge long-side count at least the
companion tooth count `N_2-15 d_out` is

\[
{1\over1-\cos\beta}+1\le15,
\]

or equivalently

\[
\boxed{\cos\beta\le {13\over14}.}
\tag{BA.4}
\]

The convenient choice `beta=pi/8` satisfies this with room.

**Verdict:** PASS.

## 5. Interaction with the new straight-event theorem

Main now also contains a long-side near-straight-event theorem.  That theorem counts
internal outer-route occurrences and derives a degree-two-loaded versus transverse
branching tradeoff.  It does not make the bridge correction above redundant:

- its initial straight-event population is occurrence-counted;
- a physical bridge may still be traversed twice in opposite directions in the outer
  walk;
- (BA.2) instead extracts a large population of distinct **nonbridge** outer contacts
  before any local vertex classification.

The two reductions are complementary.  A future composition can apply straight-event
analysis specifically to the nonbridge/rhombic-terminal cohort or charge the
exceptional-face subcohort separately.

## 6. Scope and non-conclusions

- The bridge estimate uses full-core Type-II bounded-face area saturation; it is not an
  arbitrary harmonic-cell statement.
- No KKT coefficient floor is obtained for the near-tangent contacts.
- A nonbridge edge having a bounded face on its other side does not imply that face is
  a rhombus; the exceptional-face alternative is retained explicitly.
- The large contact cohort alone gives no strict same-cardinality diameter descent.

**Final verdict:** PASS at proof-only full-core Type-II scope.  The bridge correction
is a real factor-two-scale improvement in the long-side physical population, but C-II
remains open.
