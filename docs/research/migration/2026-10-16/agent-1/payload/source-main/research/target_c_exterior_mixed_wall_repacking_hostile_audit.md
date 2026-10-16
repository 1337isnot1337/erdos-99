# Hostile audit — exterior mixed-wall repacking

**Date:** 2026-09-12  
**Audited source:** `research/target_c_exterior_mixed_wall_repacking.md`  
**Verdict:** PASS at the stated proof-only exterior-cap scope.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Canonical geometry check

Canonical Sections 67/80 and the explicit Section-84 outer-pocket statement give a
convex cap/pocket whose boundary is one force-hull closing side `[u,v]` plus a
complementary old unit-contact path `W`. Audited-working Section 162 supplies the
Type-I source partition and contact isolation of assigned exterior points.

The proof uses no stronger statement about the cap boundary.

## 2. Exit-case audit

Let `y` be in the mixed safe region and `x` an old source outside the cap interior.
If `|x-y|<1`, the first exit point of the segment `yx` from the convex cap is on its
boundary.

- If it is in the relative interior of the artificial chord, then the distance from
  `y` to that chord is `<1`, immediately contradicting the chord guard.
- If it is a boundary source vertex, either `x` is that vertex and the vertex guard
  applies directly, or the vertex lies strictly between `x,y` and the two unit lower
  bounds add to at least two.
- If it is in the relative interior of a unit contact edge, `y` is strictly on the
  interior side of the supporting line, so the crossing is proper. Unless `x` is an
  endpoint, source unit separation puts `x` at distance at least one from both edge
  endpoints, and the exact two-endpoint crossing inequality forces `y` within unit
  distance of both, contradicting the guards.

A source point lying in the relative interior of the artificial closing chord is
protected directly by distance from the chord. No assignment convention beyond
`x notin int C` is needed for this case.

The three cases exhaust the polygon boundary.

**Verdict:** the mixed-wall shield is valid.

## 3. Relation to the full collar

Every point of `C_{-1}` is at distance at least one from the entire boundary. It is
therefore at distance at least one from the closing chord and from every contact-path
vertex. Thus

\[
 C_{-1}\subseteq S_{mix}(C)
\]

literally. No claim of strict inclusion is required.

The theorem does not replace contact-edge distance by endpoint distance for arbitrary
external points. It uses the unit-edge crossing lemma specifically when a subunit
inside-to-outside segment crosses that edge.

## 4. Cardinality and diameter audit

Assigned exterior points lie in `int C subset int K`; hence none is an actual diameter
endpoint. The assigned isolate set and any vertex cover of the complete diameter graph
are disjoint, so deleting both and inserting their combined cardinality preserves
`n`.

The cover removes every old-old pair at distance `D`. New points lie in `int K`, so
every distance involving a new point is strictly below `D`. New-old unit separation
comes from the mixed-wall shield and new-new separation is imposed.

The competitor need not remain triangle-free because it is compared directly with the
definition of `D(n)`.

**Verdict:** the strict-diameter competitor is valid.

## 5. Lattice averaging audit

For the unit triangular lattice `Lambda`, covolume is `a0=sqrt(3)/2`. For any bounded
measurable `S`, translation averaging over one fundamental cell gives

\[
 \mathbb E_t |(\Lambda+t)\cap S|={\operatorname{area}(S)\over a_0}.
\]

The counting function is integer-valued, so some translate contains at least

\[
 \left\lfloor {\operatorname{area}(S)\over a_0}\right\rfloor
\]

points. Distinct lattice points are separated by at least one. Taking
`S=S_mix(C)` therefore supplies a constructive lower bound on `M_mix`.

The use of `floor` is deliberately conservative and avoids any issue at equality or
with measure-zero safe-region boundaries. All selected points belong to `int C` by
definition of `S_mix`, so the strict-diameter argument is unaffected.

This is a lower bound and is logically different from the Oler upper bounds in the
inactive-chamber residual theorem.

**Verdict:** the lattice capacity criterion is valid.

## 6. Quantitative limitation

The proof defines

\[
 G_{wall}=area(S_{mix})-area(C_{-1})\ge0
\]

but does not prove `G_wall=Omega(D)`.

A single isolated straight unit contact edge has a positive local crescent between
full edge erosion and endpoint-disk erosion. That local picture cannot simply be
summed: adjacent vertices, high boundary turning, or another nearby boundary arc can
cut the crescent. Type-I linear inradius strongly restricts such overlap, but the
required global estimate still needs proof.

No positive wall-area coefficient is imported from this local model.

**Final verdict:** PASS. The theorem removes unnecessary contact-side erosion and
reduces exterior-cap closure to a quantitative safe-area/capacity estimate. It does
not yet eliminate Type I or C-II.
