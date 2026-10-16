<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "bd95c0a79d8956ec0b0310518a6f38371916cbeb", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_projected_stress_transversal_dimension_hostile_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a0b0b778bcc80f56efb5457c235acb2a2b625629a37fa4a66ceb0f0b9d20f629"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — projected stress dimension and reduced reinsertion burden

**Date:** 2026-09-12  
**Audited source:** `research/target_c_projected_stress_transversal_dimension.md`  
**Verdict:** **PASS at proof-only scope.**  
**Theorem-state authority:** unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Linear image dimension

Let

\[
\mathcal L=\ker R_{C\cup H}^T.
\]

Canonical mixed rank gives

\[
\dim\mathcal L=s_Z+1.
\]

Projection to the diameter coordinates has kernel exactly

\[
\{(\alpha,0):R_C^T\alpha=0\},
\]

whose dimension is `sigma_C`. There is no additional kernel: zero diameter part is
literally the pure-contact self-stress condition.

Thus rank-nullity gives

\[
\dim\pi_H(\mathcal L)=s_Z+1-\sigma_C.
\]

**Disposition:** PASS.

## 2. Affine dimension of the normalized projected polytope

The normalization functional `sum beta` is nonzero on the image because the canonical
relative-interior KKT stress has `sum beta=1`.

The only delicate point is whether nonnegativity could make the normalized stress
polytope lie in a smaller affine subspace. It cannot: the canonical full-support stress
has every actual contact and diameter coordinate strictly positive. Therefore every
direction in the normalized affine stress space can be followed a sufficiently small
positive and negative amount while retaining coordinate nonnegativity. Hence the
normalized polytope has the full normalized affine stress space as its affine hull.

Projection commutes with affine hull, so the projected polytope has affine hull

\[
\pi_H(\mathcal L)\cap\{\sum\beta=1\}
\]

and dimension

\[
s_Z-\sigma_C.
\]

No multiplier lower bound uniform in `D` is needed; the argument is source-by-source.

**Disposition:** PASS.

## 3. Coordinate-face transversal

The nested proper-face argument applies to the compact projected polytope exactly as it
does to the full stress polytope. In affine dimension `d`, at most `d+1` selected
nonnegative diameter coordinates suffice to make their simultaneous zero face empty.
Thus

\[
|J|\le s_Z-\sigma_C+1.
\]

Deleting one endpoint of every selected diameter edge removes those rows. Any
normalized stress on the retained source extends to the original core by putting zero
on every removed row. At a deleted vertex all extended incident rows have zero weight,
so equilibrium there is zero; at retained vertices the original retained equilibrium
is unchanged. The extended diameter vector vanishes on all selected coordinates,
contradicting the chosen empty projected face.

Repetition among chosen endpoints only decreases the number of deleted vertices.

**Disposition:** PASS.

## 4. Outer-train bound

Audited-working §156 gives

\[
\sigma_C=2f-\operatorname{rank}C_{face},
\qquad
\operatorname{rank}C_{face}\le T-L_{OO},
\]

and

\[
T=h-s_Z+2f.
\]

Therefore

\[
\begin{aligned}
s_Z-\sigma_C
&=s_Z-2f+\operatorname{rank}C_{face}\\
&\le s_Z-2f+T-L_{OO}\\
&=h-L_{OO}.
\end{aligned}
\]

The signs and ledger substitution are correct.

**Disposition:** PASS.

## 5. Interaction with protected reinsertion

The stress-transversal reinsertion theorem needs a protected replacement set whose
cardinality equals the number of deleted core vertices plus any repacked isolates.
Replacing the old bound `s_Z+1` by the actual deleted-set bound
`s_Z-sigma_C+1` is legitimate. The theorem does **not** assert that such reserve exists;
it only lowers the sufficient reserve threshold.

Special cases are correct:

- `sigma_C=s_Z` -> projected affine dimension zero -> one diameter coordinate/endpoint
  suffices;
- `sigma_C=0` -> old `s_Z+1` bound;
- `L_OO=h` -> the outer-train inequality forces projected dimension zero.

## 6. Scope regression

The result never places contact isolates in `R_C`. It is a core linear-algebra theorem
used only to reduce how many core points must later be restored. The same-cardinality
obligation remains binding.

No claim is made that the inactive branch has large `sigma_C`, large `L_OO`, or enough
packing reserve. Those are downstream geometric questions.

**Final verdict:** PASS at proof-only scope.