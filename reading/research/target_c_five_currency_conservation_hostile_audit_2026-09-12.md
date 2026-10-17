> Generated reading edition · [exact source](../../research/target_c_five_currency_conservation_hostile_audit_2026-09-12.md) · source SHA-256 `78721ae1f5685b0f3c07d4dcddcc6e2286231527c71d90216656be06add032fe`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "e75de498f5620a2e4d1d2c2dcaca72ce5b98fd93", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_five_currency_conservation_hostile_audit_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5e8efe88423cde37479120a3e1a85379f1a5571706121450e78d706af67e6e56"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Type-II five-currency conservation

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_five_currency_conservation_2026-09-12.md`  
**Disposition:** **PASS at proof-only scope, with the sign warning on `chi_D` binding.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact ledger check

The source uses two independently audited finite identities.

First, Type-II loaded-contact localization gives

$$
e_{BB}=q-m=Q+2k+u_B.
$$

Therefore

$$
Q+u_B=q-m-2k.
\tag{1.1}
$$

Second, audited §160 defines

$$
G_D=2+q+m-k-\sum_r d_r.
\tag{1.2}
$$

Adding `(1.1)`, `k`, and `sum d_r+G_D` gives exactly

$$
\sum_r d_r+G_D+Q+u_B+k
=2+2q-2k.
$$

Hence

$$
2(q-k)+2=\sum_r d_r+G_D+Q+u_B+k.
$$

There is no asymptotic replacement and no hidden sign change.  **PASS.**

## 2. Outer-detour identity

The loaded outer-walk ledger has

$$
b=q+x_B,
\qquad x_B=m+u_B,
$$

so `b=q+m+u_B`.  Equation (1.2) gives

$$
q+m=\sum_r d_r+G_D+k-2.
$$

Thus

$$
b-P_F
=\sum_r d_r+G_D+k+u_B-P_F-2.
$$

This is exact.  **PASS.**

For

$$
\chi_D=q+m-P_F,
$$

write the `q-m` unit hull-side lengths as one and the `m` nonunit hull-side lengths as
`s_i>1`.  Then

$$
P_F=q-m+\sum_i s_i,
$$

so

$$
\chi_D=\sum_i(2-s_i).
$$

A nonunit hull side can be longer than two if its old outer interval has at least three
unit edges.  Therefore `chi_D` is **not** nonnegative.  The source explicitly retains
this.  Since

$$
b-P_F=u_B+\chi_D\ge0,
$$

negative `chi_D` implies only `u_B>=-chi_D`; it does not by itself contradict Type II.
**PASS with this warning binding.**

## 3. Phase-elimination algebra

The exact train ledger is

$$
T=q+2f-k.
$$

Since every bounded nonquadrilateral face has degree at least five, `f<=Q`. Hence

$$
T-q/2=q/2+2f-k
\le q/2+2(Q+u_B)-k.
\tag{3.1}
$$

Using

$$
Q+u_B=q-m-2k
$$

and

$$
m=P_F-q+\chi_D,
$$

we get

$$
Q+u_B=2(q-k)-P_F-\chi_D.
\tag{3.2}
$$

Substituting (3.2) in (3.1),

$$
T-q/2
\le {9\over2}(q-k)-{1\over2}k-2P_F-2\chi_D.
$$

Therefore

$$
q-k
\ge
{2\over9}(T-q/2)+{1\over9}k+{4\over9}(P_F+\chi_D).
$$

All coefficients in the candidate are correct.  **PASS.**

## 4. Atomic-gap substitution

The merged proof-only finite-diagonal theorem gives one absolute `eta_grid>0` such that

$$
{T-q/2\over D}
\ge2\sqrt{\Delta_2}+\eta_{grid}-o(1),
\qquad
\Delta_2={\pi\over2\sqrt3}.
$$

Multiplying by `2/9` contributes

$$
{4\over9}\sqrt{\Delta_2}+{2\over9}\eta_{grid}.
$$

Type-II perimeter convergence contributes `4pi/9`.  Their sum is

$$
C_{146}+{2\over9}\eta_{grid},
\qquad
C_{146}={4\over9}(\pi+\sqrt{\Delta_2}).
$$

Thus the safe combined form is

$$
{q-k\over D}-{k\over9D}-{4\chi_D\over9D}
\ge C_{146}+{2\over9}\eta_{grid}-o(1).
$$

The source's separated-liminf formulation is valid only along a common subsequence; the
pointwise/asymptotic form above is the preferred statement.  **PASS.**

## 5. Source-point and authority audit

- Contact-isolated source points are not deleted.
- No isolate coordinate is inserted into the Section-57 affine-kernel theorem.
- The result uses the audited Type-II `c_B=0` localization and proof-only §160 plus the
  merged proof-only finite-diagonal atomic gap; it does not promote theorem authority.
- No claim is made that `chi_D>=0` or that the negative-`chi_D` branch is closed.
- The inactive-container branch is untouched.

## Final verdict

**PASS at proof-only scope.**  The new content is the exact conservation law and the
correlated hull-side correction to the stopped-train phase floor.  The surviving
full-core obstruction is now sharper: a sequence can evade the favorable `chi_D`
correction only by carrying linear long-hull-side excess, which necessarily appears in
outer-walk occurrence surplus through `b-P_F=u_B+chi_D`.
