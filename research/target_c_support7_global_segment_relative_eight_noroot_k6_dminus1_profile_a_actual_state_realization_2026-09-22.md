<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3267eee6ac58dec221d892e1882b6a028fdaeec3", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_actual_state_realization_2026-09-22.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "91958b3825e850c61131fdc617b02719ce332af2c8079f52d09c174b4150db93"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C: actual-state realization filter for the remaining `k=6, D=-1` Profile A

Date: 2026-09-22

Status: rigorous strengthening of the Profile A finite reduction, retained as an independent crosscheck. The later structural closure in `research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_kernel_incidence_closure_2026-09-22.md` eliminates Profile A without requiring this full cover to execute.

Companion verifier:

`research/verify_target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_actual_state_realization_2026_09_22.py`

This note corrects one remaining overapproximation in the earlier global fixed-basis audit. The earlier audit required one fixed set of seven singleton replacement classes plus one pair replacement class to form the required functional basis through the selected `8 -> 7 -> 6 -> 5` puncture fan, but it did not require those same eight root-block states to generate the prescribed rank-two coefficient plane at the eight-row source.

## 1. Coefficient realization is an independent necessary condition

Let `P <= Q^8` be the rank-two coefficient-constraint plane of an eight-row Profile A candidate. Let `E <= P` be the span of the local coefficient constraints from the virtual-empty root blocks.

For a singleton-compatible virtual-complete block `b`, write

```text
L_b <= P
```

for its local coefficient-constraint line and `f_b` for its replacement-functional class.

For the fixed pair replacement block `p`, write `g_p` for its replacement-functional class. A pair state uses two local root rows. Those two rows span the local two-dimensional block space, so every pair state has empty coefficient constraint:

```text
L_p = 0.
```

Therefore a genuine Profile A realization with singleton block set `B`, `|B|=7`, must satisfy both

```text
rank({g_p} union {f_b : b in B}) = 8
```

and

```text
E + sum_{b in B} L_b = P.
```

The first condition is the fixed functional-basis condition already imposed by the previous verifier. The second condition was not previously enforced.

## 2. Mixed coefficient-functional seed lemma

There is a cheap exact characterization of the new source condition.

Fix the pair block/state `p`. Let `U` be the set of singleton-compatible virtual-complete blocks distinct from `p`.

Assume the mixed functional ground set has full rank:

```text
rank({g_p} union {f_b : b in U}) = 8.
```

Then there exists a seven-singleton-plus-pair functional basis whose singleton constraints generate `P` together with `E` if and only if there is a subset

```text
S <= U,
|S| <= 2,
```

such that

```text
E + sum_{b in S} L_b = P
```

and

```text
rank({g_p} union {f_b : b in S}) = 1 + |S|.
```

Proof. Suppose an actual eight-class basis exists. Its seven singleton constraints generate `P` together with `E`. Choose a minimal subset of those singleton constraints that still completes `E` to `P`. Because `dim(P/E) <= 2`, this minimal subset has size at most two. It is a subset of an eight-element functional basis, so adjoining the pair functional remains independent. This gives the required seed.

Conversely, suppose such a seed exists and the full mixed ground set has rank eight. The pair functional together with the seed is an independent set in the functional matroid. By the basis-extension theorem it extends to an eight-element basis using elements from the same ground set. The pair is fixed and every other ground element is a singleton block, so the extension consists of the pair plus exactly seven singleton blocks. Its singleton constraints already contain the seed, hence generate `P` together with `E`.

This is an exact source-level equivalence, not merely a heuristic pruning rule.

## 3. Fixed six-class source extension

The global audit has more information than the source-level lemma alone. It starts from a synchronized six-row Profile A seed with five fixed singleton replacement classes and the fixed pair class. Those six classes form a basis of the six-dimensional six-row quotient.

Under the two-row restoration back to the eight-row source, puncture functoriality sends the corresponding six source classes onto that six-row basis. Therefore the pair plus the five fixed singleton classes must already be functionally independent at the source:

```text
rank({g_p} union {f_b : b in B_5}) = 6.
```

The global profile has exactly two further singleton blocks, say `x,y`. Thus a genuine source extending this particular six-row seed must satisfy

```text
rank({g_p} union {f_b : b in B_5} union {f_x,f_y}) = 8
```

and, because the pair imposes no coefficient constraint,

```text
E + sum_{b in B_5} L_b + L_x + L_y = P.
```

The strengthened verifier enumerates every compatible choice of `x,y` and requires both conditions before entering the more expensive full puncture-fan test. This is stronger than the generic mixed seed lemma because it preserves the identity of the six classes fixed by the actual six-row seed.

Necessity is immediate from a genuine global Profile A realization. Conversely, for source-level existence relative to the fixed six classes, the displayed conditions are sufficient: the six fixed classes plus `x,y` are already the required eight-class functional basis and their singleton constraints generate the prescribed plane.

## 4. Exact actual-state reconstruction

For every particular seven-singleton-plus-pair set that reaches the eight-row rank test, the wrapper reconstructs the actual block-state tuple:

- virtual-empty blocks remain empty;
- unchosen virtual-complete blocks remain complete;
- the seven chosen singleton blocks use their unique compatible singleton states;
- the fixed pair block uses its inherited pair state.

It computes the exact coefficient space generated by those actual block states and requires

```text
generated coefficient space = P.
```

A candidate with the correct abstract functional ranks but the wrong generated coefficient plane is rejected.

For any chosen set that reaches functional rank eight, the verifier also rebuilds the actual relation matrix over `Q` and independently requires

```text
p = 9
```

and

```text
D = |A| - 3 rank(A) = -1.
```

Thus a reported survivor is an actual locally realizable Profile A source state, not merely a compatible functional-basis shadow.

## 5. Validation

The verifier, including the fixed-six source-extension test, was syntax-compiled locally before commit.

The mixed seed lemma was also tested independently on 5,000 randomly generated small finite-field linear-matroid instances. In each test the seed criterion agreed with brute-force enumeration of all pair-plus-singleton bases satisfying the coefficient-generation condition. This randomized check is not part of the proof; the proof is the rank-two basis-extension argument above.

## 6. Consequence for the finite target

The previous global fixed-basis cover remains exhaustive, but it searched a superset because a candidate coefficient plane could have been generated by local constraints unrelated to the chosen global Profile A replacement set.

The strengthened cover now requires, simultaneously:

1. the coverage-correct six-row Profile A seed;
2. a realizable clean seven-row lift;
3. a realizable eight-row rank-two lift;
4. the generic mixed source coefficient-functional seed criterion;
5. the fixed six source classes to remain independent and admit two additional singleton classes that both complete functional rank eight and generate the prescribed coefficient plane;
6. one fixed seven-singleton-plus-pair functional basis through the full selected puncture fan;
7. exact generation of the prescribed eight-row coefficient plane by the chosen actual block states; and
8. direct exact rational defect `-1` for the reconstructed source state.

A zero result for the complete 20,451-orbit cover would exclude Profile A under strictly stronger necessary conditions than the previous global fixed-basis audit.

That execution is no longer the closure bottleneck. The kernel-incidence argument in `research/target_c_support7_global_segment_relative_eight_noroot_k6_dminus1_profile_a_kernel_incidence_closure_2026-09-22.md` rules out Profile A structurally from the already-proved all-shadow conditions. This verifier remains useful only as an independent finite crosscheck. The remaining eight-no-root `k=6,D=-1,p=9` target is Profile B. Target C-II remains open.
