<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9d85418ca59390e00666885c2fdad22996a4e8a5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_inactive_blocker_multiplicity_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "19a4a737ef7c489b83a868c86f97911a5ae952036d8a85bb9bddeb33f3a2c833"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — bounded multiplicity of deep isolate blockers

**Date:** 2026-09-12  
**Audited source:** `research/target_c_inactive_blocker_multiplicity.md`  
**Verdict:** **PASS at proof-only scope.**  
**Theorem-state authority:** unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Dependency scope

The source uses only canonical Section 87 after fixing one depth `w>1`:

- at least `c_w D` vertex-disjoint contact-isolate pairs;
- pair gaps in `(1,1+K_w/D]`;
- both endpoints at depth at least `w`;
- the straight motion of one endpoint toward its mate is protected from the positive
  core, the exterior source, and the global diameter constraint until the mate or
  another chamber isolate first reaches distance one.

No KKT statement is extended to isolate coordinates.

**Disposition:** PASS.

## 2. Six-blocker bound

If one fixed isolate `z` first-blocks motions indexed by `I`, every auxiliary blocked
position `x_i'` satisfies

\[
|x_i'-z|=1,
\qquad
|x_i-x_i'|<K_w/D.
\]

For distinct matching pairs, the original moving endpoints are distinct contact
isolates and therefore satisfy

\[
|x_i-x_j|>1.
\]

Consequently

\[
|x_i'-x_j'|>1-2K_w/D.
\]

Seven points on a unit circle contain a pair with angular separation at most `2pi/7`,
so their chord is at most

\[
2\sin(\pi/7)=0.867767\ldots .
\]

For fixed `K_w`, eventually

\[
1-2K_w/D>2\sin(\pi/7).
\]

Thus seven blocked positions around one `z` are impossible and the multiplicity is at
most six.

Potential aliasing was checked: the blocker `z` may be an endpoint of a different
matching pair, but it is not the moving or mate endpoint of any motion that it blocks.
The pairwise estimate among the blocked motions is unaffected.

**Disposition:** PASS.

## 3. Blocked-angle calculation

At the blocked position set `x'=0`, put the mate at `y=re`, `r>1`, and blocker at a
unit vector `z`, with the original moving endpoint `x=-te`, `t>0`.

Original isolation gives

\[
|z-x|^2=1+t^2+2t(z\cdot e)>1,
\]

hence

\[
z\cdot e>-t/2.
\]

Likewise

\[
|z-y|^2=1+r^2-2r(z\cdot e)>1
\]

implies

\[
z\cdot e<r/2.
\]

Since `t=O(1/D)` and `r=1+O(1/D)`, the angle lies between
`pi/3-O(1/D)` and `pi/2+O(1/D)` after reflection.

The inequalities are strict because both relevant distances are strict in the original
contact-isolate source.

**Disposition:** PASS.

## 4. Disjoint-gadget extraction

For blocked pairs form hyperedges `{x_i,y_i,z_i}`.

- matching endpoint incidence contributes degree at most one to any source point;
- blocker incidence contributes degree at most six by the theorem.

Thus maximum hypergraph degree is at most seven. A chosen 3-edge intersects at most
`3*7=21` hyperedges, a safe overcount. Greedy matching therefore retains at least
`1/21` of all blocked gadgets.

If fewer than half of the original `m>=c_wD` pairs are blocked, at least half are
direct. Otherwise at least `m/2` are blocked and at least `m/42` vertex-disjoint
blocked triples remain. The advertised universal choice `c'_w=c_w/42` is valid in both
cases.

**Disposition:** PASS.

## 5. Regression check

The theorem does not contradict the scaled triangular-lattice zero-reserve regression.
Such a packing can have a linear population of local near-contact/blocking gadgets with
bounded blocker multiplicity. The theorem therefore cannot be promoted into a packing
reserve statement without a new collective argument.

It also does not claim:

- simultaneous feasibility of all individual pair motions;
- a unit triangle in the original source;
- force transfer into the positive core; or
- a same-cardinality diameter competitor.

These limitations are stated correctly.

## 6. Final verdict

The finite blocker concentration regression is eliminated: canonical §87 deep
pair-closing motions cannot all be stopped by `o(D)` repeatedly reused blockers.
A linear disjoint family of direct pairs or blocked triples is forced.

**Final verdict:** PASS at proof-only scope. C-II remains open.