> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_single_free_outerwalk_currency_2026-09-18.md) · source SHA-256 `4acd9b73512450d2b92a8464419622d2344860258f43dd863c9f6a1969f6d0b8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "07c669b52f24bf7ed2b50a0d96fe01962ccea693", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_single_free_outerwalk_currency_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "1b9e4efd62a2b3978b6e8a36b64cc20afc20ce9e5075fd0f3deb135b26c1fd52"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — one FREE module already forces square-root outer-walk/external currency

**Date:** 2026-09-18  
**Status:** proved candidate awaiting promotion; proof-only corollary of two-sided FREE absorption plus the pocket-width routing theorem  
**Scope:** every all-inactive non-anchored FREE reflection module, before the fixed-pair `LINEAR-MATCHING/PAIR-REUSE` split  
**Dependencies:** two-sided gate absorption; two-sided outer-face localization; OP outer-pocket Oler absorption; outer-walk pocket capacity; pocket-width routing  
**Certificate:** `research/verify_target_c_tooth_reflection_pocket_width_outerwalk_coupling_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding pocket-width theorem used the two extreme `PAIR-REUSE` modules to gain the small directional-defect improvement from coefficient `1` to `nu_K>1`. The main outer-walk/external obstruction does not need pair reuse at all.

Fix one all-inactive FREE activation ancestry. Let

- `L` be its number of lower gates;
- `U` its number of upper gates;
- `Z_ext` the full source population outside the force hull `F`;
- `H_out` the OP outer-pocket area inside `F`;
- `x_B=b-q` the outer-walk excess;
- `u=b-P_F>=0` the chain-chord detour; and
- `t_D<h_*+D^{-1/3}`, with `h_*=sqrt(303)/52`.

Every ancestry vertex is an original contact- and diameter-inactive source point in the original outer contact face, and all ancestry vertices are distinct. The two-sided absorption theorem gives

$$
\boxed{L\ge D-O(\sqrt D).}
\tag{SF.1}
$$

## 1. One FREE ancestry pays almost one full diameter unit of OP currency

Let `Z_in` be the old outer-face isolate population inside `F`. Since the ancestry has `L+U+1` distinct vertices,

$$
Z_{\rm in}+Z_{\rm ext}\ge L+U+1.
\tag{SF.2}
$$

The exact OP inequality is

$$
Z_{\rm in}
\le\frac{2}{\sqrt3}H_{\rm out}-\frac{u}{2}.
\tag{SF.3}
$$

Therefore

$$
\boxed{
Z_{\rm ext}
+\frac{2}{\sqrt3}H_{\rm out}
-\frac u2
\ge D+U-O(\sqrt D).
}
\tag{SF.4}
$$

The outer-pocket area capacity

$$
H_{\rm out}\le\frac4\pi x_B^2
\tag{SF.5}
$$

and `u>=0` now give

$$
\boxed{
Z_{\rm ext}
+\frac8{\pi\sqrt3}x_B^2
\ge D+U-O(\sqrt D).
}
\tag{SF.6}
$$

Thus every FREE module, including the later `LINEAR-MATCHING` branch, already has a nonlinear canonical outer-currency cost. No common-edge reuse is needed.

Immediate consequences are

$$
x_B=o(\sqrt D)
\Longrightarrow
Z_{\rm ext}\ge D-O(\sqrt D),
\tag{SF.7}
$$

and

$$
Z_{\rm ext}=o(D)
\Longrightarrow
\frac{x_B}{\sqrt D}
\ge
\sqrt{\frac{\pi\sqrt3}{8}}-o(1).
\tag{SF.8}
$$

The constant is

$$
\boxed{
c_{\rm FREE}
:=\sqrt{\frac{\pi\sqrt3}{8}}
=0.824727083093451\ldots .}
\tag{SF.9}
$$

## 2. Combine with the directional pocket-width routing law

The pocket-width routing theorem for the same ancestry gives

$$
2x_B(U+1)+2(1+t_D)Z_{\rm ext}
\ge D-O(\sqrt D).
\tag{SF.10}
$$

Because every upper gate uses one distinct external source point,

$$
U\le Z_{\rm ext},
$$

so

$$
\boxed{
2x_B(Z_{\rm ext}+1)
+2(1+t_D)Z_{\rm ext}
\ge D-O(\sqrt D).
}
\tag{SF.11}
$$

Suppose a subsequence has finite square-root limits

$$
\frac{x_B}{\sqrt D}\to\xi,
\qquad
\frac{Z_{\rm ext}}{\sqrt D}\to\zeta.
$$

Then (SF.6) and (SF.11) give

$$
\boxed{
\frac8{\pi\sqrt3}\xi^2\ge1,
\qquad
2\xi\zeta\ge1.
}
\tag{SF.12}
$$

Hence

$$
\xi\ge c_{\rm FREE},
\qquad
\zeta\ge\frac1{2\xi}.
\tag{SF.13}
$$

Since `c_FREE>1/sqrt(2)`, minimizing `xi+1/(2xi)` on this range gives

$$
\boxed{
\liminf
\frac{x_B+Z_{\rm ext}}{\sqrt D}
\ge
c_{\rm FREE}+\frac1{2c_{\rm FREE}}
=1.430988245421916\ldots .
}
\tag{SF.14}
$$

This statement is unconditional on the FREE side: if either normalized currency diverges, the bound is automatic; if both remain bounded, (SF.12) applies.

At the scalar minimum,

$$
\frac{x_B}{\sqrt D}\to0.824727083093451\ldots,
\qquad
\frac{Z_{\rm ext}}{\sqrt D}\to0.606261162328465\ldots .
\tag{SF.15}
$$

The fixed-pair `PAIR-REUSE` directional-defect theorem improves these constants slightly to `0.825157...`, `0.605945...`, and `1.431102...`, but the basic obstruction is already present in one FREE module.

## 3. The square-root endpoint also forces outer chain-chord detour

From (SF.4), if `Z_ext=O(sqrt(D))`, then

$$
H_{\rm out}\ge\left(\frac{\sqrt3}{2}-o(1)\right)D.
\tag{SF.16}
$$

The canonical outer-pocket detour-area theorem gives

$$
H_{\rm out}\le\frac\pi2x_B^{3/2}\sqrt u.
\tag{SF.17}
$$

Thus, for finite normalized limits

$$
\frac{x_B}{\sqrt D}\to\xi,
\qquad
\frac{u}{\sqrt D}\to\eta,
$$

one has

$$
\boxed{
\xi^3\eta\ge\frac3{\pi^2}
=0.303963550927013\ldots .
}
\tag{SF.18}
$$

At the minimum `xi=c_FREE`, this gives

$$
\boxed{
\eta\ge0.541864550399676\ldots .
}
\tag{SF.19}
$$

The finiteness assumption on `eta` is automatic at the combined-currency endpoint. Since every force-hull side joins distinct source points, `P_F>=q`; hence

$$
0\le u=b-P_F=q+x_B-P_F\le x_B.
\tag{SF.20}
$$

Therefore a FREE sequence approaching the scalar minimum (SF.14) must simultaneously satisfy the positive square-root detour floor (SF.19).

## 4. Frontier effect

The all-inactive FREE branch now has a source-wide canonical outer-boundary cost before any reuse or forest analysis:

```text
one FREE module
  => Z_ext + (8/(pi sqrt(3))) x_B^2 >= D - O(sqrt(D))
  => 2 x_B (Z_ext+1) + 2(1+h_*+o(1)) Z_ext >= D-O(sqrt(D))
  => (x_B+Z_ext)/sqrt(D) >= 1.4309882454...-o(1).
```

The later extreme-pair argument improves the coefficient only slightly, to `1.4311023381...`, while adding the much stronger common-edge/forest information. This separates the roles cleanly:

- one FREE ancestry already forces outer-walk/external capacity;
- pair reuse is needed for the directional-defect gain and common lower-network structure.

C-II remains open. The next obstruction is no longer a FREE branch with negligible outer boundary currency. A hard survivor must either carry at least one linear external source population when `x_B=o(sqrt(D))`, or carry explicit square-root outer-walk excess and, at the critical boundary, square-root chain-chord detour. A closing theorem must convert that boundary currency into the canonical Sections 122--123 aggregate attachment-cell detour/payment, or use the linear external population to build a strict source-preserving diameter decrease.

**Disposition:** generalized the pocket-width/outerwalk obstruction from `PAIR-REUSE` to every all-inactive FREE module and identified the exact one-module square-root endpoint.