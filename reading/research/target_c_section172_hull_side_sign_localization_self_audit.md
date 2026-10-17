> Generated reading edition · [exact source](../../research/target_c_section172_hull_side_sign_localization_self_audit.md) · source SHA-256 `3e3ee11c9bb18f49b332147ff18f0e9798ac3a8ae8e922c0f32e537ae2f24eb9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "c774e043f4cdd71ff31ae0d341037030e9992037", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_section172_hull_side_sign_localization_self_audit.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "30030598e61c8a03649fed61d3947e1895c1da5b4a2f43958cfe5f2516ba27db"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Self-audit — Target C Section 172 hull-side sign localization

**Date:** 2026-09-12
**Disposition:** PASS at proof-only scope; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact algebra

Audited §160 defines

$$
G_D=2+q+m-k-\sum_r d_r.
$$

Therefore `q+m=sum d_r+G_D+k-2`, and subtracting `per(F)` gives (172.1). This is
finite and does not assume a sign for `chi_D`.

The audited Type-II outer ledger is `b=q+m+u_B`. Hence

$$
b-\operatorname{per}(F)=u_B+\chi_D.
$$

The occurrence-counted outer walk is a concatenation of unit-edge paths joining the
consecutive loaded-hull vertices, so each path is at least its chord length. Thus the
left side is nonnegative, and `chi_D\le-\varepsilon D` forces `u_B\ge\varepsilon D`.

**Result:** PASS.

## 2. Same-carrier remainder bound

Audited §160 proves, for a carrier with internal strict-rhombus area `A D^2+o(D^2)`
and diameter `lambda D+o(D)`,

$$
G_D/D\ge[\sqrt{\pi A}-\lambda]_+-o(1).
$$

Substitution into (172.2), together with `sum d_r/D>=S-o(1)` and `k/D->kappa`, gives
(172.8). The same-carrier requirement is stated explicitly, so no independent
optimization of incompatible profiles occurs.

**Result:** PASS, conditional on the audited §160 hypotheses.

## 3. Endpoint arithmetic

Using the displayed proof-only endpoint values gives

$$
\sqrt{\pi(0.4703752868004241)}-0.9762439137425688
=0.239374260456223\ldots,
$$

and

$$
2.798596312209462+0.239374260456223-\pi
=-0.103622080924108\ldots.
$$

The decimals are diagnostic evaluations of exact expressions/previously audited
profiles, not new canonical premises.

**Result:** PASS.

## 4. Scope and regressions

- The theorem is Type II only and does not address the inactive-container branch.
- It does not assert `chi_D>=0`; long hull sides remain possible.
- It does not turn a linear `u_B` into a diameter decrease or triangle.
- Contact-isolated points are retained and are not inserted into the §57 affine kernel.
- The endpoint bound is conditional and does not claim that the endpoint sequence exists.

**Final verdict:** Section 172 is a valid proof-only sign/localization reduction. C-II
remains open.
