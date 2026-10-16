# Hostile audit — canonical `40888` three-cut kernel cusp

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_three_cut_kernel_cusp_40888_2026-09-15.md`
- `research/verify_target_c_three_cut_kernel_cusp_40888.py`
- parent three-cut kernel theorem and C65 correction
- current `z>2.217` retention / diameter-edge certificate

**Disposition:** **PASS.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate changes only the path-threshold and averaging constants in the exact
three-cut kernel theorem.  It also correctly incorporates the already-merged C65 scope
correction: at canonical Target C-II scope every actual diameter row has positive weight
in a relative-interior normalized KKT stress, so the exceptional kernel cusp must show
both derivative signs.

## 1. Fan/path substitution

The fixed choices

\[
\lambda=0.67765,
\qquad r=0.48565
\]

satisfy all parent path requirements.  Exact arithmetic gives

\[
g=0.013808745296\ldots>0,
\]

\[
d_{top}=0.13089595>0,
\qquad d_{low}=0.16140405>0,
\]

and

\[
p=0.00350125523288\ldots>0.
\]

Thus the same weighted thresholding, top-block double count, complement-dual path, and
lower-phase angular-defect charge apply without modification.

**Verdict:** PASS.

## 2. Diameter switch budget

Every actual diameter incidence row is one signed interval on the selected laminar
path, hence changes at at most two internal boundaries.  Therefore

\[
\sum_iN_i\le2h_H.
\]

Hopf--Pannwitz gives `h_H<=q`.  The current `z>2.217` theorem proves throughout the same
`t<=1.844` scope

\[
q/D<1.848545513+o(1),
\]

so

\[
\sum_iN_i<3.697091026D+o(D).
\]

This is a globally valid replacement for the parent `2 pi D` bound, not an assumption
about the particular selected path.

**Verdict:** PASS.

## 3. Exact combined constant

The normalized KKT interval budget remains `sum B_i<=2`.  The lower-phase reserve gives

\[
\sum_i(q_i+q_{i+1})
\le2C_{phase}/d_{low}+o(1).
\]

Hence the same nonnegative cost

\[
T_i=N_i+DB_i+D(q_i+q_{i+1})
\]

has exact outward average

\[
K={S_{switch}+2+2C_{phase}/d_{low}\over p}.
\]

The Fraction certificate independently rebuilds the `q/D` bound from the matched atomic
constant and `F(2.217)`, rather than importing a rounded decimal.  Its outward value is

\[
K=20443.5596261\ldots .
\]

Averaging `T_i+T_{i+1}` over consecutive triples doubles this constant.  The exact
certificate proves

\[
2K=40887.1192523\ldots<40888
\]

with margin greater than `0.8`.

**Verdict:** PASS.

## 4. Kernel propagation and C65 sign cusp

The parent kernel proof uses the triple averaging constant only to bound the union of
the two switching sets, its normalized KKT mass, and the total two-gap phase variation.
All later identities are exact.  Thus `42400` can be replaced by `40888` in those three
places.

The candidate also fixes the parent theorem's now-obsolete generic zero-KKT alternative.
Canonical C65 gives

\[
\beta_h>0
\]

for every actual diameter row.  Mixed infinitesimal rigidity guarantees at least one
exceptional derivative is nonzero, while exact stationarity gives

\[
\sum_{h\in H_{exc}}\beta_h\ell_h=0.
\]

Strict positivity then forces exceptional rows of both signs.  This is the correct
canonical conclusion.

**Verdict:** PASS.

## 5. Scope

The result remains quantitative.  It does not produce a finite descent and does not
supersede the adjacent-strip one/two-bar reaction theorem.  The two results address
different reductions: the present theorem localizes an exact three-shear kernel cusp;
the strip theorem sparsifies a two-dimensional layer reaction.

**Final verdict:** PASS at canonical full-core Type-II scope. C-II remains open.
