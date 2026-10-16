<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c56bc686f9cc2623adbe7e207096647f666a6342", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_three_dominant_flower_through_pair_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0e5275a0e4d21eb3ac8b836054a5e74c3d6cddf02ca4c33b62c276cbd458c355"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — three-dominant full-flower through-pair normal form

**Date:** 2026-09-15\
**Audited source:** `research/target_c_three_dominant_flower_through_pair_2026-09-15.md`\
**Verdict:** **PASS at proof-only atomic/local scope.**\
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The theorem classifies a full pentagonal flower having at least three side directions
converging to one triangular projective orbit.  The audit targets the exact ray-sum
classification, the sole non-orbit escape, its connector geometry, and the conversion
to a three-complement occurrence cost.

## 1. Three-ray arithmetic is exhaustive

The exact six-ray verifier checks all `6^3=216` ordered triples.  The squared norms of
their sums are exactly

```text
0, 1, 3, 4, 7, 9.
```

Every norm-one triple contains an opposite ray pair.  Every norm-zero triple is one of
the two alternating triples `{0,2,4}` or `{1,3,5}`.  Every norm-four sum is twice a
six-ray unit vector.  Every norm-three sum is closed by an adjacent six-ray pair.

Since two remaining unit sides have resultant norm at most two, the norm-seven and
norm-nine cases are impossible.  No continuous closure case was omitted.

## 2. Norm-one, norm-three, and norm-four cases really become all-orbit

For norm one, cancelling the forced opposite ray pair leaves one orbit unit `u`.
Closure says `u+w_1+w_2=0`; three unit vectors summing zero are separated by `120`
degrees, so both remaining directions are orbit rays.

For norm three, the two remaining units have separation `60` degrees and a prescribed
resultant along a norm-`sqrt(3)` triangular vector.  The unordered pair is uniquely
the adjacent orbit-ray pair around that resultant.

For norm four, equality in the triangle inequality forces the two remaining units to
coincide at `-s/2`; the norm-four lattice solutions are exactly twice the six unit
rays.  This is allowed as a limiting direction even though finite faces are strictly
convex, so the proof does not smuggle in a false lower turn-angle bound.

## 3. The non-all-orbit case is uniquely the alternating return

If the selected three-ray sum is zero, those rays are an alternating triangular
triple and closure forces `w_2=-w_1`.  Conversely this configuration closes, so it
cannot be excluded algebraically.  It is therefore the correct unique escape rather
than an artifact of the proof.

If the common projective `w` direction is itself triangular, the escape collapses
back into the all-orbit case.  The genuinely new case has a non-triangular opposite
pair.

## 4. The complement connector calculation is correct

Normalize the alternating triple to angles `0,120,240` degrees.  After the permitted
rotation/reversal/exchange symmetries, take the complement direction `theta` in
`(0,60)` degrees.  Convex cyclic edge order is

```text
0, theta, 120, theta+180, 240.
```

The midpoint displacement from the `theta` side to its opposite side is exactly the
`120`-degree dominant ray.  The positive normal to the complement train has angle
`theta+90`, so the connector-normal difference is `|30-theta|<30` degrees and its
normal projection is at least `sqrt(3)/2`.

The connector is contained in the convex face and its interior contains no contact
graph.  Hence it is a genuine through connector, not only a vector identity.

At `theta=0` or `60` the complement direction is triangular and the configuration is
all-orbit, so loss of strictness at the endpoints causes no missing escape case.

## 5. The all-orbit local through pair does not need a new global theorem

A closed five-ray triangular pattern has phase multiplicities `3,1,1`; the repeated
phase contains both signs.  The standard midpoint calculation gives one connector at
`30` degrees from that phase normal.  Only this local fact is used.  The candidate
does not import the global supertrain deficit theorem from the separate
pentagon-splicing branch.

## 6. Uniformity over a linear flower population is valid

The theorem is asymptotic.  If the claimed `o(1)` direction mismatch or connector-cone
error were not uniform over all flowers with at least three selected dominant sides,
one could choose a worst offending flower for each `D` and pass to a compact
subsequence.  Its five unit side vectors would converge to one of the exact cases
above, contradicting the corresponding exact connector conclusion.

Thus a single error scale tending to zero can be used for the whole selected linear
population.

## 7. Three-complement occurrence counting is safe

Select one local through pair on every flower with at least three dominant-window side
terminals.  A flower left unselected has at most two dominant occurrences, hence at
least three complement terminal occurrences.  Therefore

\[
C_D\ge3(M_D-P_D)-o(D).
\]

The count is by terminal occurrence.  A complete train has exactly two terminals, so
turning it into a distinct-complement-train lower bound loses by at most a factor two,
with no endpoint-simplicity assumption between different flowers.

**Final verdict:** PASS at proof-only atomic/local scope.  The only remaining issue is
global simultaneous use of through pairs whose complement phases vary from flower to
flower; that is handled separately by the vertex-disjoint matching theorem.
