# Target C hidden-tetrahedron support audit — 2026-09-23

## Purpose

This note audits the scope of the hidden-tetrahedron support computation before using it in a closure argument.

## Finite statement checked

The checked configuration is the four-support pattern

```
(1234), (1235), (1456), (2457)
```

with hidden tetrahedron `(1245)`.

The associated triangle rows over edge variables have rank 10 and nullity 5 for the 15 touched triangles. The singleton-complement nullity census is:

- nullity 2: 350 cases
- nullity 3: 103 cases
- nullity 4: 2 cases

The support stabilizer has order 4, giving support orbit size 1260. The enumerated cycle states give 24 orbits for the 2222 profile and 84 orbits for the 3221 profile.

These are finite enumeration facts about this support pattern.

## Logical boundary

The computation does not prove that every possible Target C obstruction reduces to this support orbit. The missing bridge is a reduction from arbitrary surviving full-core configurations to this four-support incidence type, or a proof that all alternative support types have equivalent rank obstructions.

The next high-value target is a support-classification lemma:

> Every remaining p=3,m=4 candidate with the relevant hidden tetrahedron behavior is contained in the enumerated support orbit family, up to relabeling.

A weaker intermediate target is a complete census of non-isomorphic four-support patterns with touched-triangle rank/nullity signatures, to determine whether the current obstruction is universal or only exceptional.

## Next computational target

Generate the complete labeled four-support incidence catalog:

1. Enumerate all choices of four 4-vertex supports on seven vertices.
2. Quotient by S_7 relabeling.
3. Record touched triangle rank, nullity, support stabilizer, and cycle-state obstruction profiles.
4. Compare surviving classes against the hidden-tetrahedron class.

The output should separate a universal obstruction from a single exceptional orbit.