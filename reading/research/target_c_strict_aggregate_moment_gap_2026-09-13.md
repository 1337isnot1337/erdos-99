> Generated reading edition · [exact source](../../research/target_c_strict_aggregate_moment_gap_2026-09-13.md) · source SHA-256 `79ee5f71aba6e68ed377773c7132b4e70ea465a65c1e696e7e544a4e4021ac09`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1ef3c91d2941074e9c46c0af9a870df08073f731", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_strict_aggregate_moment_gap_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a2c478743fae93ecd4409882fa6b2255b280377cf1c3abfb3d12413d9f564502"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — strict gap above the aggregate harmonic-cell diameter moment

**Date:** 2026-09-13
**Status:** proof-only Type-II candidate; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note retains the positive aggregate detour payment from the canonical
two-arc audit.  Combining it with the exact outer-walk decomposition gives a
strict linear gap above the summed harmonic-cell diameter moment.  The result is
source-level and does not identify local defects with the global defect ledger.

## 1. Quantities and exact identities

For every unloaded harmonic component `r`, let `L_r` be its
occurrence-counted outer-face walk length, `d_r=diam(conv(A_r))`,
and let `f_r` and `Q_r` be its bounded nonquadrilateral-face count and degree
excess.  Set

```math
S_D:=\sum_r d_r,\qquad S_{\rm out}:=\sum_r(L_r-2d_r),
\qquad F_{\rm loc}:=\sum_r f_r,\qquad Q_{\rm loc}:=\sum_r Q_r,
```

and `X:=q-k-S_D`.  The component outer-walk inequality and the exact
aggregate decomposition are

```math
S_{\rm out}\ge0,
\tag{SMG.1a}
```

```math
S_{\rm out}
 =2\sum_r(a_r-d_r)+2(e_{BB}-k)-2d_{\rm tile}
   -2C_{\rm loc}-Q_{\rm loc}.
\tag{SMG.1b}
```

The audited Type-II completion-side payment `e_BB-C_loc<=2d_tile`, together
with `a=q-2+2c_I-d_tile`, therefore gives

```math
0\le S_{\rm out}
 \le 2X+4c_I-4-Q_{\rm loc}.
\tag{SMG.2}
```

In particular,

```math
Q_{\rm loc}\le 2X+4c_I-4.
\tag{SMG.3}
```

The canonical aggregate two-arc payment is

```math
E_{\rm agg}:=\sum_r(L_r+4f_r+Q_r-2d_r)
             =S_{\rm out}+4F_{\rm loc}+Q_{\rm loc},
\tag{SMG.4}
```

with

```math
\liminf_{D\to\infty}E_{\rm agg}/D
\ge c_{\rm det}:=\frac\pi2(2-\sqrt3).
\tag{SMG.5}
```

Every bounded nonquadrilateral face has degree at least five, so
`F_loc<=Q_loc`.  Substituting (SMG.2)--(SMG.3) into
(SMG.4) gives the finite estimate

```math
E_{\rm agg}
 \le 10X+20c_I-20.
\tag{SMG.6}
```

## 2. Strict aggregate moment gap

The canonical component-count estimate `c_I=O(D^(2/3))` makes
`c_I/D->0`.  Dividing (SMG.6) by `D` and using (SMG.5) yields

```math
\boxed{\displaystyle
\liminf_{D\to\infty}\frac{(q-k)-\sum_r d_r}{D}
\ge \frac{c_{\rm det}}{10}
=\frac\pi{20}(2-\sqrt3)
=0.0420893607\ldots .}
\tag{SMG.7}
```

Thus the detour payment cannot be made asymptotically compatible with
`q-k=\sum_r d_r+o(D)`.  More precisely, on any subsequence with
`X/D\to0`, (SMG.3) forces `Q_{\rm loc}=o(D)`, and then
`F_{\rm loc}=o(D)`, while (SMG.5) still requires a positive
`E_{\rm agg}/D`.  The payment must
therefore appear in the outer-walk surplus or in the (q-k) excess itself.

## 3. Scoped Section-118 endpoint consequence

On the proof-only Section-118 common-cap moment profile, the independently
audited complement-gap argument supplies

```math
\liminf_{D\to\infty}\frac{\sum_r d_r}{D}
\ge S_{118}:=2.798596312209462\ldots .
\tag{SMG.8}
```

Combining (SMG.7) and (SMG.8) gives the scoped endpoint floor

```math
\boxed{\displaystyle
\liminf_{D\to\infty}\frac{q-k}{D}
\ge 2.8406856729\ldots >2.8406.}
\tag{SMG.9}
```

The decimal is certified conservatively by the accompanying exact-rational
arithmetic script.  This specialization is only for the named Section-118
common-cap profile; (SMG.7) is the general Type-II consequence of the cited
aggregate payment.

## 4. Scope and non-implications

The argument uses only the active aggregate outer-walk identities, the audited
completion-side inequality, the canonical `c_I=o(D)` estimate, and the
canonical Type-II detour floor.  `Q_loc` and `F_loc` are not replaced by the
global `Q` and `f`, and no boundary-order injectivity is
assumed.  The result does not determine the loaded diameter graph, produce a
finite source-preserving motion, or prove a unit equilateral triangle in every
global minimizer.  It is therefore a proof-only narrowing of C-II, not a
Level-I result or theorem-state promotion.

**Classification:** proved candidate awaiting hostile audit; scoped as stated;
C-II remains open.
