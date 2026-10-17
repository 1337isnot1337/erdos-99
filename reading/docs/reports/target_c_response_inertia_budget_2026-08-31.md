> Generated reading edition · [exact source](../../../docs/reports/target_c_response_inertia_budget_2026-08-31.md) · source SHA-256 `7747f3a42943ab5ae39c2386765622413739f00aea3466111512bf3234c6a7b5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-281DB326D429","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: response-matrix inertia budget

**Date:** 2026-08-31  
**Repository state:** `research/target-c-low-diameter-prestress-2026-08-31`  
**Run type:** proof / spectral reduction  
**Target:** Target C Gate C-I beyond the two-diameter theorem C25  
**Depends on:** Target C11 (contact-network Dirichlet/Kron response), C12 (positive contact support connected), and the signed stress-matrix notation of C20

## LEVEL I STATUS

`STILL OPEN`

Theorem C25 eliminates weak contacts whenever the maximal KKT diameter support has at
most two edges.  The next case is therefore three or more positive diameter edges.

This report gives an exact spectral reduction for that regime.  For any normalized KKT
stress `s`, let

```math
\Omega_s=L_C(\alpha)-L_H(\beta).
```

If the positive diameter graph has rank

```math
r_H:=\operatorname{rank}L_H,
```

then

```math
\boxed{
\nu_-(\Omega_s)\le r_H-2\le |H_s|-2,
}
```

where `nu_-` is the number of negative scalar eigenvalues, counted with multiplicity.

Thus:

- one or two positive diameter edges give no negative stress mode, recovering C20;
- three positive diameter edges give at most **one** negative scalar mode;
- more generally, every additional independent diameter edge beyond the two affine
  coordinate modes buys at most one negative mode.

For a three-edge diameter forest the reduction is sharper.  There is exactly one
non-affine generalized response eigenvalue

```math
\boxed{
\rho_s
=\sum_{h\in H_s}\beta_h R_{\rm eff}^{C_s}(h)-2,
}
```

where `R_eff^{C_s}(h)` is the electrical effective resistance between the endpoints of
`h` in the positive contact network with conductances `alpha`.  Then

```math
\boxed{
\Omega_s\succeq0\iff\rho_s\le1,
}
```

and `Omega_s` has exactly one negative eigenvalue iff `rho_s>1`.

This identifies the first possible failure of C20 as one scalar electrical crossing
mode.

---

## 1. Dirichlet response and Schur inertia

Fix a normalized KKT stress `s=(alpha,beta)`.  Let

```math
C_s=\{ij:\alpha_{ij}>0\},
\qquad
H_s=\{ij:\beta_{ij}>0\},
```

and let

```math
B=V(H_s),
\qquad
I=V(C_s)\setminus B.
```

C12 says `C_s` is connected.  Let `L_C` be its conductance Laplacian and let

```math
\Lambda
=L_C[B,B]-L_C[B,I]L_C[I,I]^{-1}L_C[I,B]
\tag{C26.1}
```

be the boundary response matrix.  The Dirichlet block `L_C[I,I]` is positive definite.
Let `L_H` denote the beta-weighted diameter Laplacian on `B` and put

```math
M=\Lambda-L_H.
\tag{C26.2}
```

As in C20, the full signed stress matrix is congruent to

```math
\boxed{
\Omega_s\sim_{\rm cong}M\oplus L_C[I,I].
}
\tag{C26.3}
```

Therefore

```math
\boxed{
\nu_-(\Omega_s)=\nu_-(M).
}
\tag{C26.4}
```

C11 gives

```math
M\mathbf1=0,
\qquad
MP_B=0.
\tag{C26.5}
```

Since `C_s` is connected,

```math
\Lambda\succeq0,
\qquad
\ker\Lambda=\operatorname{span}\{\mathbf1\}.
\tag{C26.6}
```

For completeness, (C26.6) follows from the Dirichlet principle: for boundary values
`z_B`,

```math
z_B^{\mathsf T}\Lambda z_B
=\min_{z_I}
\sum_{ij\in C_s}\alpha_{ij}(z_i-z_j)^2.
\tag{C26.7}
```

The minimum is zero exactly when every positive-contact edge has equal endpoint values,
and connectedness then forces all boundary values to be constant.

---

## 2. Generalized response operator

Work on the codimension-one space

```math
U=\mathbf1^\perp\subseteq\mathbb R^B.
```

By (C26.6), the restriction `Lambda_U` is positive definite.  Define the positive
semidefinite generalized diameter operator

```math
\boxed{
A_s
=\Lambda_U^{-1/2}L_H\Lambda_U^{-1/2}.
}
\tag{C26.8}
```

Then on `U`,

```math
M
\sim_{\rm cong}
I-A_s.
\tag{C26.9}
```

Hence

```math
\boxed{
\nu_-(M)
=\#\{\lambda(A_s)>1\}.
}
\tag{C26.10}
```

Also

```math
\operatorname{rank}A_s
=\operatorname{rank}L_H
=:r_H.
\tag{C26.11}
```

---

## 3. Two forced eigenvalues equal to one

Translate the origin so that the boundary coordinate columns `x,y` have zero mean and
therefore lie in `U`.  Because `B` contains the endpoints of at least two non-collinear
diameter edges whenever its affine span is two-dimensional, `x,y` are linearly
independent.

C11 gives

```math
\Lambda x=L_Hx,
\qquad
\Lambda y=L_Hy.
\tag{C26.12}
```

Put

```math
\widehat x=\Lambda_U^{1/2}x,
\qquad
\widehat y=\Lambda_U^{1/2}y.
```

Then

```math
\begin{aligned}
A_s\widehat x
&=\Lambda_U^{-1/2}L_Hx
=\Lambda_U^{-1/2}\Lambda x
=\widehat x,\\
A_s\widehat y
&=\widehat y.
\end{aligned}
\tag{C26.13}
```

Thus `A_s` has eigenvalue one with multiplicity at least two.

### Theorem C26 (response inertia budget)

Assume the force hull of the stress is two-dimensional.  Then

```math
\boxed{
\nu_-(\Omega_s)
\le r_H-2
\le |H_s|-2.
}
\tag{C26.14}
```

#### Proof

The PSD matrix `A_s` has exactly `r_H` positive eigenvalues by (C26.11), and at least
two of them equal one by (C26.13).  At most `r_H-2` remaining positive eigenvalues can
therefore exceed one.  Combine with (C26.4) and (C26.10).  Finally
`rank L_H<=|H_s|` for every weighted graph. `square`

### Scope

The two-dimensional hypothesis is essential only for obtaining the two independent
affine coordinate modes.  The one-dimensional force-hull phase is already excluded for
the contact-minimal Target C source by C19 and is classified separately by C20.1.

---

## 4. Recovery of the two-diameter theorem

If `|H_s|=2` and the force hull is two-dimensional, then

```math
r_H\le2.
```

C26.14 gives

```math
\nu_-(\Omega_s)=0.
```

Moreover `A_s` has rank exactly two and its two positive eigenvalues are both one.
Therefore `I-A_s` has no additional zero eigenvalue on `U`, so the scalar kernel of the
full stress matrix is exactly

```math
\operatorname{span}\{\mathbf1,x,y\}.
```

Thus C26 independently recovers the PSD/maximal-rank content of C20 for two positive
diameter edges without the four-terminal sign argument.

The C20 proof remains useful because it exposes the circular-planar boundary sign
structure directly.

---

## 5. Three positive diameter edges

Assume now

```math
|H_s|=3.
\tag{C26.15}
```

If the three positive diameter edges form a triangle, then `L_H` has rank two.  Hence
C26 gives

```math
\Omega_s\succeq0.
\tag{C26.16}
```

For sufficiently large global minimizers the diametral-triangle case is independently
excluded by C15.

The remaining case is a three-edge forest.  Then

```math
r_H=3.
\tag{C26.17}
```

So `A_s` has exactly three positive eigenvalues.  Two are the affine eigenvalues one.
Write the third as

```math
\rho_s>0.
\tag{C26.18}
```

Then

```math
\operatorname{spec}_{>0}(A_s)=\{1,1,\rho_s\}.
\tag{C26.19}
```

Consequently:

```math
\boxed{
\begin{array}{lll}
0<\rho_s<1 &\Longrightarrow& \Omega_s\succeq0
\text{ with scalar kernel exactly }\operatorname{span}\{1,x,y\},\\[1mm]
\rho_s=1 &\Longrightarrow& \Omega_s\succeq0
\text{ with one additional scalar kernel mode},\\[1mm]
\rho_s>1 &\Longrightarrow& \Omega_s
\text{ has exactly one negative scalar eigenvalue}.
\end{array}
}
\tag{C26.20}
```

Thus the first possible indefinite KKT stress matrix is rank-one on the negative side.

---

## 6. Effective-resistance formula for the third mode

Let `Lambda^+` be the Moore–Penrose inverse of the boundary response.  For boundary
vertices `i,j`, the effective resistance in the positive contact network is

```math
R_{\rm eff}^{C_s}(i,j)
=(e_i-e_j)^{\mathsf T}\Lambda^+(e_i-e_j).
\tag{C26.21}
```

This is the same effective resistance as in the full contact network because `Lambda`
is its Dirichlet response.

Since

```math
L_H
=\sum_{h=ij\in H_s}
\beta_h(e_i-e_j)(e_i-e_j)^{\mathsf T},
\tag{C26.22}
```

we have

```math
\begin{aligned}
\operatorname{tr}A_s
&=\operatorname{tr}(\Lambda^+L_H)\\
&=\sum_{h=ij\in H_s}
\beta_hR_{\rm eff}^{C_s}(i,j).
\end{aligned}
\tag{C26.23}
```

For a three-edge forest, (C26.19) therefore gives the exact identity

```math
\boxed{
\rho_s
=\sum_{h\in H_s}\beta_hR_{\rm eff}^{C_s}(h)-2.
}
\tag{C26.24}
```

Because `rho_s>0`, every three-edge forest stress automatically satisfies

```math
\boxed{
\sum_h\beta_hR_{\rm eff}^{C_s}(h)>2.
}
\tag{C26.25}
```

The PSD threshold is

```math
\boxed{
\Omega_s\succeq0
\iff
\sum_h\beta_hR_{\rm eff}^{C_s}(h)\le3.
}
\tag{C26.26}
```

The first genuine negative stress mode appears exactly when

```math
\boxed{
\sum_h\beta_hR_{\rm eff}^{C_s}(h)>3.
}
\tag{C26.27}
```

This is a single scalar electrical obstruction.

---

## 7. Edge-space interpretation

Orient the three diameter edges arbitrarily and let `B_H` be their boundary incidence
matrix.  Put `W=diag(beta_h)` and define

```math
K
=W^{1/2}B_H^{\mathsf T}\Lambda^+B_HW^{1/2}.
\tag{C26.28}
```

The nonzero eigenvalues of `K` equal those of `A_s`, so for a three-edge forest they
are

```math
1,1,\rho_s.
```

Let `R` be the `3 x 2` matrix whose `h`th row is the oriented diameter vector
`p_i-p_j`.  The response identity `Lambda P=L_HP` is equivalent to

```math
K(W^{1/2}R)=W^{1/2}R.
\tag{C26.29}
```

Hence the two columns of `W^{1/2}R` span the affine eigenvalue-one plane in diameter
edge space.

Let `q` span its orthogonal complement:

```math
\boxed{
\sum_{h\in H_s}q_h\sqrt{\beta_h}\,R_h=0.
}
\tag{C26.30}
```

Then `q` is an eigenvector of `K` with eigenvalue `rho_s`.

Define the scalar boundary load

```math
f=B_HW^{1/2}q.
\tag{C26.31}
```

It satisfies

```math
\boxed{
\mathbf1^{\mathsf T}f=0,
\qquad
P_B^{\mathsf T}f=0.
}
\tag{C26.32}
```

The second condition is exactly (C26.30): the load has zero total affine moment.
Moreover

```math
f^{\mathsf T}\Lambda^+f
=\rho_s\,q^{\mathsf T}q.
\tag{C26.33}
```

By contrast, routing the edge currents `sqrt(beta_h)q_h` directly through the three
abstract diameter edges has dissipated energy

```math
q^{\mathsf T}q.
\tag{C26.34}
```

Thus:

> `rho_s` is exactly the ratio between the minimum electrical energy required by the
> planar positive-contact network to carry the unique affine-balanced three-diameter
> boundary load and the energy of routing that same edge-current vector directly on the
> three diameter chords.

The possible negative KKT mode is therefore a planar **crossing-congestion mode**.

---

## 8. Consequence for the post-C25 frontier

C25 says a weak-contact source must have at least three strong diameter edges.  C26
now says that the first new spectral obstruction at three edges is only one-dimensional.

For a three-edge forest stress:

- if `rho_s<1`, the signed KKT stress is PSD with only the affine scalar kernel;
- if `rho_s=1`, exactly one additional zero mode appears;
- if `rho_s>1`, exactly one negative scalar mode appears.

Thus a proof excluding weak contacts in the `|H_*|=3` phase can be reduced to one of
the following sharper statements:

1. prove `rho_s<1` for every relevant three-diameter second-order KKT witness;
2. classify the equality mode `rho_s=1` and integrate it;
3. if `rho_s>1`, exploit the unique affine-balanced boundary load (C26.31) together
   with circular planarity of the contact response and the diameter geometry C17–C18.

The old open-ended request for a generic reverse angular Korn inequality is therefore
too broad in the three-edge phase.  There is only one non-affine electrical mode to
control.

---

## 9. Audit table

| Claim | Status | Reason |
| --- | --- | --- |
| Schur inertia reduction C26.3–C26.4 | **proved** | Positive Dirichlet block and block congruence. |
| Two forced generalized eigenvalues `1` | **proved** | C11 affine response identity. |
| Inertia budget `nu_-<=rank L_H-2` | **proved** | `A_s` PSD of rank `r_H` with two unit eigenvalues. |
| Three-edge forest spectrum `{1,1,rho}` | **proved** | `rank L_H=3`. |
| Effective-resistance identity for `rho` | **proved** | Trace `Lambda^+ L_H`. |
| Edge-space affine-balanced load interpretation | **proved** | Standard AB/BA nonzero spectrum and C11. |
| Universal bound `rho<=1` | **not proved** | This is now the exact three-edge PSD question. |
| Weak contacts excluded for all `|H_*|=3` | **not proved** | C25 currently closes only `|H_*|<=2`. |

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

C26 response inertia budget:
For any normalized KKT stress s with 2D force hull,

  nu_-(Omega_s) <= rank(L_H)-2 <= |H_s|-2,

where Omega_s=L_C(alpha)-L_H(beta).

Proof:
Schur-complement the positive contact Laplacian to B=diameter endpoints:
  Omega ~ (Lambda-L_H) + positive Dirichlet block.
On 1^perp, conjugate by Lambda^(1/2):
  Lambda-L_H ~ I-A,
  A=Lambda^(-1/2)L_H Lambda^(-1/2) >=0.
C11 gives Lambda x=L_H x and Lambda y=L_H y, so A has two independent eigenvectors
with eigenvalue 1. Since rank A=rank L_H, at most rank(L_H)-2 eigenvalues exceed 1.

For a three-edge diameter forest, rank L_H=3 and
  spec_+(A)={1,1,rho_s}.
Moreover
  rho_s = sum_h beta_h R_eff^{C_s}(h) - 2.
Hence
  Omega_s PSD iff sum beta_h R_eff(h) <= 3,
and Omega_s has exactly one negative scalar eigenvalue iff that weighted resistance
sum exceeds 3.

Edge-space form:
the third mode is the unique q satisfying
  sum_h q_h sqrt(beta_h) R_h = 0.
Its boundary load f=B_H sqrt(W) q has zero resultant and zero affine moment, and rho_s
is the ratio of contact-network Dirichlet energy for f to the direct three-diameter
routing energy. The first post-C25 obstruction is therefore one affine-balanced planar
crossing-congestion mode.

Next: prove/contradict rho<=1 using circular-planar response + C17/C18 geometry, or
classify the rho=1 equality mode.
```
