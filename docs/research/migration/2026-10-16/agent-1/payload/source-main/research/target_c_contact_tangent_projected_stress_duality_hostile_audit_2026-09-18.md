# Hostile audit — contact-tangent/projected-stress duality

**Date:** 2026-09-18  
**Audited source:** `research/target_c_contact_tangent_projected_stress_duality_2026-09-18.md`  
**Verdict:** `PASS at proof-only scope`  
**Theorem-state authority:** unchanged  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

## 1. Quotient and injectivity

The contact-flex quotient

\[
V_C=\ker R_C/\mathcal E
\]

is legitimate because Euclidean infinitesimal motions are killed by every distance
row, including all actual diameter rows.  Hence `R_H` descends to a linear map

\[
G:V_C\to\mathbb R^h.
\]

If `G[u]=0`, a representative `u` lies in both `ker R_C` and `ker R_H`.  Canonical
mixed rigidity has rank `2v-3`, so the joint kernel consists exactly of Euclidean
motions.  Therefore `[u]=0` and `G` is injective.

No nonlinear rigidity or second-order claim is used.

**Disposition:** PASS.

## 2. Equality of the projected signed stress space and the row-nullity

For a mixed signed stress `(alpha,beta)`, equilibrium is

\[
R_C^T\alpha+R_H^T\beta=0.
\]

Pairing with every `u in ker R_C` shows that `beta` annihilates `R_H(ker R_C)`, hence
belongs to the left nullspace of the diameter derivative map on `V_C`.

Conversely, if `beta` annihilates `R_H(ker R_C)`, then `R_H^T beta` annihilates
`ker R_C`.  In finite dimensions

\[
(\ker R_C)^\perp=\operatorname{im}R_C^T,
\]

so some `alpha` satisfies

\[
R_C^T\alpha=-R_H^T\beta.
\]

Thus the projection of the full signed mixed-stress space is exactly the left kernel of
`G`.  The quotient by Euclidean motions introduces no extra condition because distance
rows already vanish on those motions.

**Disposition:** PASS.

## 3. Dimension count

The hostile-audited projected-stress theorem gives

\[
\dim\pi_H(\mathcal L)=s_Z+1-\sigma_C=p_D+1.
\]

Injectivity of `G` gives `rank G=d_C`, so its left nullity is `h-d_C`.  Therefore

\[
h-d_C=p_D+1,
\qquad
d_C=h-p_D-1.
\]

Using `d_H=q-h` gives

\[
d_H+p_D=q-d_C-1.
\]

The same formula follows independently from

\[
d_C=T-2f-1+\sigma_C=(q-k)-1+\sigma_C
\]

and `k=d_H+p_D+sigma_C`.  The two derivations agree.

**Disposition:** PASS.

## 4. The `p_D=0` positive-circuit statement

When `p_D=0`, the left kernel of `G` is one-dimensional.  The relative-interior KKT
stress projects to a diameter vector `beta` with every actual-diameter coordinate
strictly positive.  Hence that vector spans the unique row dependence.

If any `h-1` diameter derivative rows were dependent, the corresponding dependence
extended by zero on the omitted row would be a second left-kernel vector with a zero
coordinate.  It cannot be proportional to the full-support positive `beta`.  Thus every
`h-1` rows are independent and the `h` rows form a positive circuit.

This conclusion uses only positivity of the known KKT diameter coefficients, not
positivity of every signed stress in the linear kernel.

**Disposition:** PASS.

## 5. Relation to the normalized projected stress polytope

The proof does **not** claim that every nonnegative vector in `ker G^T` lifts to a
nonnegative contact stress.  That would be stronger and is not established.  The only
polytope fact used for the dimension identity is the already audited equality

\[
\dim\pi_H(\mathcal L)=p_D+1,
\]

which follows because the full-support relative-interior KKT point makes the normalized
projected polytope have the full normalized affine hull.

This distinction is important.  The theorem identifies the signed row-nullity exactly;
it does not replace the KKT polytope by an arbitrary orthant section.

**Disposition:** PASS.

## 6. Live tangent-space reformulation

The exact identity

\[
d_H+p_D=q-d_C-1
\]

and `q/D->pi` convert the latest three-line frontier for `d_H+p_D` directly into the
stated cap on `d_C/D`.  This is a change of variables, not an additional numerical
estimate.

`m_D` and `d_C` remain distinct:

- `m_D` is the dimension of an explicitly integrated finite contact-preserving
  manifold;
- `d_C` is the complete infinitesimal contact-flex dimension.

The audit found no step that silently integrates all of `V_C`.  The source note
explicitly leaves that nonlinear gap open.

**Disposition:** PASS.

## 7. Scope regression

- Contact-isolated source points remain outside all rigidity matrices.
- The identity is exact on the canonical nonisolated positive-contact core.
- The positive-circuit corollary applies only when `p_D=0`.
- No claim is made that a positive circuit of diameter derivative rows is itself
  impossible.
- No theorem-state file is changed and C-II is not declared closed.

**Final verdict:** PASS at proof-only scope.  The main gain is an exact primal meaning
for `p_D` and `d_H+p_D`, which turns the remaining projected-stress/topology defect into
a statement about the full contact tangent.