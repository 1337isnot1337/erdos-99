> Generated reading edition · [exact source](../../research/target_c_free_terminal_train_closure_hessian_2026-09-18.md) · source SHA-256 `4ef92bdba5de685b32443bc46bd773ad7614fe5a28c3147da425180019ccc0a5`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "6da236177c79542444e8364ac434420d27494af6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_free_terminal_train_closure_hessian_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "f3319275f77e1ae209917caf531eab683c4263ee14142f887cabce10174123ff"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the train-angle closure Hessian diagonalizes against every dual closure mode

**Date:** 2026-09-18  
**Status:** proof-only second-order structural reduction; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train angle closure system  
**Depends on:** exact nonlinear train-angle closure map; coherent train orientations; closure-corank identity `sigma_C=dim ker C_face^T`; exact finite contact-flex manifolds already constructed in train-angle coordinates  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current obstruction is nonlinear: the complete contact tangent can be much larger than the explicit exact finite contact-flex manifold. The first missing nonlinear condition can be written exactly.

Let

```math
\Psi:(\mathbb R/2\pi\mathbb Z)^T\to\mathbb R^{2f}
```

be the bounded-exceptional-face closure map and let

```math
C:=D\Psi(0)=C_{face}.
```

For every dual closure mode

```math
y=(y_F)_F\in\ker C^T
```

there is a canonical scalar coefficient `lambda_tau(y)` on every complete train such that the second-order obstruction is diagonal:

```math
\boxed{
 y^T D^2\Psi(0)[x,z]
 =-\sum_\tau \lambda_\tau(y)x_\tau z_\tau.
}
\tag{H.1}
```

The coefficients satisfy two exact rotation identities:

```math
\boxed{
\sum_\tau\lambda_\tau(y)=0,
}
\tag{H.2}
```

and

```math
\boxed{
\sum_\tau\lambda_\tau(y)x_\tau=0
\qquad(x\in\ker C).
}
\tag{H.3}
```

Thus every first-order train-angle flex that extends to a `C^2` exact closure path must satisfy

```math
\boxed{
\sum_\tau\lambda_\tau(y)x_\tau^2=0
\qquad
(y\in\ker C^T).
}
\tag{H.4}
```

More strongly, the tangent space of any smooth exact train-angle closure manifold is a common totally isotropic subspace for all of the diagonal bilinear forms in (H.1).

This gives a concrete second-order target. The nonlinear integration gap is not an unspecified singularity: at second order it is the simultaneous square-map condition

```math
x\in\ker C,
\qquad
x^{\odot2}\in\Lambda^\perp,
```

where `Lambda={lambda(y): y in ker C^T}`. No sufficiency claim is made.

---

## 1. Coherent occurrence notation

Fix a coherent unit direction `u_tau` for every complete stopped train `tau`. For every bounded exceptional face `F` incident to `tau`, let

```math
\epsilon_{F\tau}\in\{+1,-1\}
```

be the occurrence sign so that the oriented unit side vector contributed by that occurrence at the canonical placement is

```math
\epsilon_{F\tau}u_\tau.
```

The exact closure block is

```math
\Psi_F(\theta)
=\sum_{\tau\sim F}
\epsilon_{F\tau}R_{\theta_\tau}u_\tau.
\tag{1.1}
```

At the canonical placement, `Psi_F(0)=0` for every bounded exceptional face. A bounded--bounded train has two terminal occurrences with opposite occurrence signs; a bounded--outer train has one bounded exceptional occurrence; an outer--outer train has none.

Differentiating one train occurrence gives

```math
{d\over d\theta}R_\theta u\big|_{0}=Ju,
\qquad
{d^2\over d\theta^2}R_\theta u\big|_{0}=-u.
\tag{1.2}
```

Therefore the `tau` column of `C` has bounded-face blocks

```math
\epsilon_{F\tau}Ju_\tau.
\tag{1.3}
```

---

## 2. A dual mode assigns one scalar to every train

Fix

```math
y=(y_F)_F\in\ker C^T.
```

For each train define its signed terminal dual vector

```math
v_\tau(y):=
\sum_{F:\tau\sim F}\epsilon_{F\tau}y_F.
\tag{2.1}
```

The `tau` component of `C^Ty=0` says

```math
v_\tau(y)\cdot Ju_\tau=0.
\tag{2.2}
```

Hence `v_tau(y)` is parallel to `u_tau`. There is a unique scalar `lambda_tau(y)` such that

```math
\boxed{
v_\tau(y)=\lambda_\tau(y)u_\tau.
}
\tag{2.3}
```

For an outer--outer train the sum in (2.1) is empty, so `lambda_tau(y)=0`.

This definition is independent of the arbitrary coherent orientation convention. Replacing `u_tau` by `-u_tau` also replaces every occurrence sign `epsilon_{F tau}` by its negative; both sides of (2.3) reverse, leaving `lambda_tau(y)` unchanged.

In the common normalization for a bounded--bounded train `tau=FG` with occurrence signs `+1,-1`, equation (2.3) is exactly

```math
y_F-y_G=\lambda_\tau(y)u_\tau.
```

For a bounded--outer train it is the analogous one-face relation.

---

## 3. Exact diagonal Hessian formula

Let `x,z in R^T`. Since a train angle occurs only through its own rotation, there are no mixed second derivatives between distinct train variables. By (1.2),

```math
D^2\Psi_F(0)[x,z]
=-\sum_{\tau\sim F}
\epsilon_{F\tau}u_\tau x_\tau z_\tau.
```

Contract with `y` and regroup by trains:

```math
\begin{aligned}
y^TD^2\Psi(0)[x,z]
&=-\sum_\tau
\left(
\sum_{F:\tau\sim F}\epsilon_{F\tau}y_F
\right)\cdot u_\tau\,x_\tau z_\tau\\
&=-\sum_\tau\lambda_\tau(y)x_\tau z_\tau.
\end{aligned}
```

This proves (H.1).

The reduction is exact and finite. It does not use the terminal asymptotics or the one-anchor normal form.

---

## 4. Global rotation forces two orthogonality identities

Let `mathbf 1` be the all-ones train-angle vector. Rotating every train by the same angle rotates every face-closure vector, so for all sufficiently small `c`,

```math
\boxed{
\Psi(\theta+c\mathbf1)=R_c\Psi(\theta),
}
\tag{4.1}
```

where `R_c` acts blockwise on the `f` closure vectors.

Set `theta=0`. Since `Psi(0)=0`, the path `c -> c mathbf1` lies in the exact zero set. Contracting its second derivative with `y` and using (H.1) gives

```math
0
=y^TD^2\Psi(0)[\mathbf1,\mathbf1]
=-\sum_\tau\lambda_\tau(y),
```

which proves (H.2).

Now differentiate (4.1) first in `c` and then in an arbitrary direction `x` at `(theta,c)=(0,0)`. This gives

```math
D^2\Psi(0)[x,\mathbf1]=J\,Cx,
\tag{4.2}
```

with `J` acting blockwise. If `x in ker C`, the right side vanishes. Contracting with `y` and using (H.1) gives

```math
\sum_\tau\lambda_\tau(y)x_\tau=0.
```

This is (H.3).

Equivalently,

```math
\lambda(y)\in(\ker C)^\perp=\operatorname{row}C.
\tag{4.3}
```

The last statement is a consistency check: the scalar train stress extracted from a left closure mode lies in the row space of the first-order closure matrix.

---

## 5. Necessary second-order compatibility

Suppose a first-order angle vector `x in ker C` is the initial velocity of a `C^2` exact closure path

```math
\theta(t)=tx+{t^2\over2}w+o(t^2),
\qquad
\Psi(\theta(t))=0.
```

The second derivative of the closure equation is

```math
Cw+D^2\Psi(0)[x,x]=0.
```

Contract with any `y in ker C^T`. The acceleration term disappears and (H.1) gives

```math
\boxed{
\sum_\tau\lambda_\tau(y)x_\tau^2=0.
}
\tag{5.1}
```

This proves (H.4).

A useful immediate corollary is that any first-order closure flex whose train-angle coordinates all have the same absolute value automatically passes every second-order dual test. Indeed, if `x_tau^2=c^2` for all trains, then (H.2) makes (5.1) vanish. This is only a second-order statement; existence of a non-Euclidean equal-magnitude vector in `ker C` is a separate combinatorial problem.

---

## 6. Exact manifolds are common totally isotropic subspaces

Let `M` be any smooth exact train-angle closure manifold through the canonical point and let

```math
L=T_0M\subseteq\ker C
```

be its tangent space. Take arbitrary `x,z in L`. Choose a smooth two-parameter chart `theta(s,t) in M` with

```math
\partial_s\theta(0,0)=x,
\qquad
\partial_t\theta(0,0)=z.
```

Differentiate `Psi(theta(s,t))=0` once in each parameter:

```math
C\,\partial_{st}\theta(0,0)
+D^2\Psi(0)[x,z]=0.
```

Contract with `y in ker C^T`. The first term vanishes, so (H.1) yields

```math
\boxed{
\sum_\tau\lambda_\tau(y)x_\tau z_\tau=0
\qquad
(x,z\in L,\ y\in\ker C^T).
}
\tag{6.1}
```

Thus every already constructed exact finite contact-flex manifold supplies a common totally isotropic subspace for the full family of diagonal dual Hessians.

This gives an additional audit tool for proposed exact-flex constructions: their tangent spaces must satisfy (6.1), not merely the first-order closure equations.

---

## 7. Full-row-rank branch integrates without an activation order

If

```math
\sigma_C=\dim\ker C^T=0,
```

then `C` has full row rank `2f`. The implicit-function theorem applied directly to the full closure map `Psi` gives a smooth local zero manifold of train-angle dimension

```math
T-2f.
```

As in the audited two-anchor integration theorem, strict rhombi close identically in train-angle coordinates, exact closure of all bounded exceptional faces closes every contact-graph cycle, and fixing one core vertex integrates the resulting unit edge vectors to actual vertex positions. Finite strict noncontact slack persists in a sufficiently small neighborhood. Thus this zero manifold is an exact finite contact-preserving realization manifold, not merely a formal angle-space solution.

After quotienting the one-dimensional global-rotation direction, the non-Euclidean exact finite contact-flex dimension is

```math
\boxed{
 m_{full}=T-2f-1=(q-k)-1.
}
\tag{7.1}
```

No two-anchor activation order is needed for this implication; complete activation is one sufficient combinatorial certificate for `sigma_C=0`, not a necessary hypothesis for nonlinear integration.

This exact branch observation does not close C-II. A survivor with positive but small closure corank can still be singular, and real analytic equations can lose many local dimensions at a singular point. The point is to isolate the nonlinear problem precisely to `sigma_C>0`.

---

## 8. Frontier effect

The contact-tangent/projected-stress duality identifies the remaining gap as a nonlinear integration problem. Equations (H.1)--(H.4) now give its complete second-order dual form in train coordinates.

For every live terminal survivor:

- if `sigma_C=0`, the complete train-angle contact tangent integrates locally and has exact finite non-Euclidean dimension `(q-k)-1`;
- if `sigma_C>0`, every candidate additional first-order train-angle mode must satisfy the explicit diagonal square constraints (H.4) before any higher-order obstruction is relevant;
- the tangent spaces of the already proved pair-shield / sealed-component manifolds are common totally isotropic spaces for these same forms.

The next concrete target is therefore finite-dimensional: understand the simultaneous quadratic system

```math
 x\in\ker C,
 \qquad
 \Lambda(x^{\odot2})=0,
```

on the near-pure pentagonal one-anchor core. A theorem producing many non-Euclidean solutions would enlarge exact flex beyond the current pair-shield manifold; a theorem showing that all such solutions lie in the known manifold would identify the precise second-order rigidity mechanism that must be reconciled with diameter locking.

No theorem-state file is changed.

**Disposition:** diagonalized every dual second-order face-closure obstruction in train-angle coordinates, proved the rotation orthogonality identities, showed exact-manifold tangent spaces are common totally isotropic subspaces, and removed the full-row-rank `sigma_C=0` branch from the nonlinear-integration bottleneck. C-II remains open.
