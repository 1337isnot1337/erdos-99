# Target C — arbitrary matching response frontier

**LEVEL I STATUS: STILL OPEN.**

This module records C52, the arbitrary-cardinality extension of the C50-C51 selected-response contraction.

Full proof: [target_c_arbitrary_matching_response_contraction_2026-08-31.md](../../reports/target_c_arbitrary_matching_response_contraction_2026-08-31.md).

## C52 — every selected diameter matching has nonnegative Schur defect

Let `2q` force-hull terminals occur in strict convex cyclic order and let the selected positive diameter support be a matching. The planar diameter-thrackle property forces, after cyclic relabeling,

`H={i(i+q):0<=i<q}`.

For positive weights `B=diag(beta_i)`, pair-incidence matrix `Q`, connected circular-planar contact response `Lambda`, `R=Lambda^+`, and

`K=Q^T R Q`,

the C11 affine identity `Lambda P=L_H P` implies

`K B U = U`,

where the rows of `U=Q^T P` are the directed opposite chords.

Strict convexity orders those chord directions. There are positive scales `a_i` and strictly increasing slopes

`t_0<...<t_(q-1)`

with `u_i=a_i(1,t_i)`.

The C50 Kalmanson split-cone representation gives, for every `i<j<k`,

`K_ik <= min(K_ij,K_jk)`.

Thus `K` is a Robinson similarity in the chord-slope order.

Put

`N=B-B K B`, `E=diag(a_i)`, `M=E N E`, and `gamma_i=a_i beta_i`.

Then

`M 1=0`, `M t=0`,

and, for `i!=j`,

`M_ij=-gamma_i gamma_j K_ij`.

C52.R proves that a weighted Laplacian built from a Robinson similarity cannot have a negative eigenvalue when it annihilates both the constant vector and a strictly increasing vector. The proof uses a weighted first-difference Fiedler transform and Perron-Frobenius; a negative mode would yield a nonconstant monotone eigenvector weighted-orthogonal to both `1` and `t`, contradicting the strict weighted covariance identity.

Therefore

`M>=0`, `N>=0`, and

`B^(-1)-K>=0`.

Equivalently,

`Lambda-L_H>=0`

on the centered boundary space, and the selected full Schur defect satisfies

`L_C(alpha)-L_H(beta)>=0`.

## Exact route effect

C52 subsumes the matching part of C50 and C51 and removes the cardinality parameter entirely:

`selected positive diameter support is a matching -> no negative response mode`.

Therefore every response topology still capable of producing a negative selected Schur mode must contain a positive-diameter vertex of degree at least two.

This does not close C-I. The direction-dependent second-order multiplier need not have matching support or maximal support, and semidefiniteness alone is not the common-angular-rate finite-integration theorem.

## Next exact target

The response problem has now localized to shared-endpoint diameter supports.

A useful next lemma would show that for a convex diameter thrackle satisfying the same affine response identity, either the full Schur defect is positive semidefinite or a negative mode localizes at a vertex incident to at least two positive diameter edges in a form incompatible with the shared-endpoint angle bound or the C9 shear separator.

Do not split the support into matching color classes and apply C52 blockwise: the affine identity belongs to the total `L_H` and is not inherited by an arbitrary color class.
