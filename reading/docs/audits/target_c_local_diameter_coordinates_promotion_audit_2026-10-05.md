> Generated reading edition · [exact source](../../../docs/audits/target_c_local_diameter_coordinates_promotion_audit_2026-10-05.md) · source SHA-256 `738a0fb7348f4e5ad70ccc341bfbe05b2edf6713a40160c4bb955b341b614b01`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0CEAA832F690","canonical":true,"claim_ids":["C-CONTACT-DIAMETER-COORDINATES"],"claim_statuses":{"C-CONTACT-DIAMETER-COORDINATES":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — Target C local active-diameter coordinates

**Date:** 2026-10-05  
**Audit base:** \`6d4e4205b6c367d1011d03865b4388df1ec10bb7\`  
**Starting theorem state:** \`2026-10-05.audit.55\`  
**Target:** C-II / exact contact manifold and active-diameter cage  
**Verdict:** **PASS at the exact finite local scope registered below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes one theorem:

- \`C-CONTACT-DIAMETER-COORDINATES\`.

The theorem is a local normal form for the active diameter constraints on the exact unit-contact realization manifold. It is not a global diameter descent theorem and does not claim any uniform neighborhood radius along an asymptotic sequence.

## 1. Canonical manifold and notation

Audited source:
\`docs/reports/target_c_contact_manifold_local_diameter_coordinates_2026-10-05.md\`.

Work on the canonical nonisolated positive-contact core. Contact-isolated source points remain in the global source and are held fixed throughout this local core analysis.

Canonical \`C-CONTACT-FACE-REGULARITY\` gives a smooth exact unit-contact realization manifold near the source. Modulo Euclidean motions its dimension is

$$
m=q-k-1.
$$

Let $H$ be the set of active diameter edges, $h=|H|$, and define for every $e=ij\in H$

$$
\ell_e(p')
=
\frac{|p_i'-p_j'|^2-D^2}{2}.
$$

Thus $\ell_e=0$ at the original source, and $\ell_e>0$ means that old active diameter edge has become strictly longer than $D$.

Let
$$
g_e=d\ell_e|_{T_p\mathcal M}.
$$

Collect these covectors as the rows of a linear map
$$
G:T_p\mathcal M\to\mathbb R^H.
$$

## 2. The active-diameter differential has full rank

Suppose $u\in T_p\mathcal M$ lies in $\ker G$.

Because $u$ is tangent to the exact contact manifold, it kills every original contact row to first order. Since $Gu=0$, it also kills every active diameter row.

Canonical \`C-ZRF\` says that the mixed contact/active-diameter framework on the nonisolated core has only Euclidean infinitesimal motions. Modulo Euclidean motions, $u=0$.

Therefore

$$
\boxed{\operatorname{rank}G=m.}
$$

This is the exact linear statement needed below.

## 3. Positive KKT stationarity puts zero in the interior of the active-diameter covector hull

Choose a normalized relative-interior canonical KKT stress. Its active diameter coefficients satisfy

$$
\beta_e>0,
\qquad
\sum_{e\in H}\beta_e=1.
$$

Restricting KKT stationarity to the tangent space of the exact contact manifold gives

$$
\boxed{
\sum_{e\in H}\beta_e g_e=0.
}
$$

Because all coefficients are strictly positive and the $g_e$ span the full $m$-dimensional tangent dual, zero lies in the ordinary interior of
$$
\operatorname{conv}\{g_e:e\in H\}.
$$

Indeed, if zero lay on the boundary, there would be a nonzero tangent vector $u$ and a supporting halfspace with
$$
g_e(u)\ge0
$$
for every $e$. The positive weighted sum could vanish only if every $g_e(u)=0$, contradicting $\operatorname{rank}G=m$.

Hence there is a source-dependent constant $c>0$ such that for every tangent vector $u$,

$$
\max_{e\in H}g_e(u)\ge c\|u\|,
\qquad
\min_{e\in H}g_e(u)\le-c\|u\|.
$$

## 4. Exact local diameter cage

Take any smooth local coordinate chart
$$
\phi:U\subset\mathbb R^m\to\mathcal M,
\qquad
\phi(0)=p.
$$

Taylor expansion gives, uniformly over the finite active edge set,

$$
\ell_e(\phi(z))
=
g_e(D\phi_0z)+O(\|z\|^2).
$$

Since $D\phi_0$ is invertible onto $T_p\mathcal M$, the interior-hull estimate above gives one point-dependent $r>0$ such that every nonzero $z$ with $\|z\|<r$ has some old active diameter edge with

$$
\ell_e(\phi(z))>0.
$$

Therefore

$$
\boxed{
0<\operatorname{dist}_{\mathcal M}(p,p')<r
\quad\Longrightarrow\quad
\max_{e\in H}|p_i'-p_j'|>D
}
$$

for every noncongruent contact-preserving realization $p'$ in that neighborhood.

No uniform lower bound on $r$ is asserted.

This makes the current obstruction precise: the exact contact manifold has many dimensions, but the old active diameter cage is locally sharp in every non-Euclidean direction.

## 5. Exact local diameter coordinates and the residual cage

Choose a subset $B\subset H$ with
$$
|B|=m
$$
whose covectors form a basis of $T_p^*\mathcal M$. Put
$$
R=H\setminus B.
$$

The map
$$
p'\mapsto
y=
(\ell_b(p'))_{b\in B}
$$
has invertible derivative at $p$. By the inverse function theorem, $y$ is an exact local coordinate system on $\mathcal M$.

Write the residual active excesses as
$$
\rho(y)
=
(\ell_r(p'(y)))_{r\in R}.
$$

Now use
$$
d_H=q-h,
\qquad
k=d_H+s_Z.
$$
Since
$$
m=q-k-1,
$$
we obtain

$$
m=h-s_Z-1,
$$
hence

$$
\boxed{|R|=h-m=s_Z+1.}
$$

Thus every local diameter-coordinate basis leaves exactly $s_Z+1$ residual active diameter edges.

## 6. First-order residual obstruction

Let
$$
A=D\rho(0)
$$
denote the Jacobian of the residual excess map at the origin.

KKT stationarity in the $y$-coordinates becomes

$$
\boxed{
\beta_B+A^T\beta_R=0.
}
$$

Therefore for every nonzero componentwise $y\le0$,

$$
\beta_R^TAy
=
-\beta_B^Ty
>0.
$$

So if all basis active diameters are infinitesimally shortened or held fixed, some residual active diameter has positive first variation.

This is an exact finite first-order cage statement.

## 7. Exact nonlinear weighted identity

Canonical \`C-CONTACT-FACE-REGULARITY\` also supplies the exact stress-energy identity for every labelled contact-preserving core realization:

$$
\sum_{e\in H}\beta_e|p_i'-p_j'|^2
=
D^2-E_\Omega(p'),
\qquad
E_\Omega(p')\ge0.
$$

Substitute

$$
|p_i'-p_j'|^2=D^2+2\ell_e(p')
$$
and $\sum_H\beta_e=1$. In the $y,\rho(y)$ coordinates this gives exactly

$$
\boxed{
\beta_R^T\rho(y)
=
-\beta_B^Ty-\frac12E_\Omega(y).
}
$$

Because the displacement from $p$ is $O(\|y\|)$, the stress quadratic energy satisfies

$$
E_\Omega(y)=O(\|y\|^2).
$$

Hence for every sufficiently small nonzero componentwise $y\le0$,

$$
\boxed{
\beta_R^T\rho(y)>0.
}
$$

In particular at least one residual active diameter is strictly longer than $D$.

This is stronger than the first-order statement because it is an exact finite nonlinear obstruction in a point-dependent neighborhood.

It is still not a global obstruction: the chart neighborhood can shrink with the source, and a successful global replacement may leave this neighborhood or change the labelled active-diameter combinatorics.

## 8. The same residual edges parameterize every active-diameter covector dependence

Since
$$
\operatorname{rank}G=m,
$$
$$
\dim\ker G^T=h-m=s_Z+1.
$$

Order the rows with basis block $B$ first. If
$$
\lambda\in\ker G^T
$$
has $\lambda_R=0$, then
$$
G_B^T\lambda_B=0.
$$
Because $G_B$ is invertible,
$$
\lambda_B=0.
$$

Thus restriction to the residual coordinates is injective. Domain and codomain both have dimension $s_Z+1$, so it is an isomorphism:

$$
\boxed{
\ker G^T
\;\xrightarrow[\cong]{\lambda\mapsto\lambda_R}\;
\mathbb R^R.
}
$$

The same $s_Z+1$ residual diameter edges therefore parameterize all linear dependencies among the active-diameter covectors.

## 9. Hostile scope audit

The promoted theorem does **not** claim any of the following.

- It does not give a global strict-diameter competitor.
- It does not give a uniform chart radius.
- It does not imply that the $s_Z+1$ residual edges are geometrically localized.
- It does not identify residual active edges with the audit.53 loaded-return paths.
- It does not turn weighted stress-energy decrease into maximum-diameter decrease.
- It does not move or delete contact-isolated source points.
- It does not say that $s_Z=o(D)$ alone closes the branch.
- It does not say that $s_Z=\Omega(D)$ is itself contradictory; it is only linear mixed-rigidity currency.

The theorem changes the live problem from an undifferentiated active-diameter feasibility question into a finite residual-cage problem.

## 10. Canonical consequence for the current frontier

Audit.55 forces explicit linear physical/train currencies. Audit.54 supplies a strict source-replacement endpoint once certified wall-safe packing surplus pays a diameter vertex cover.

The present theorem adds an exact local dichotomy inside the contact manifold.

- A basis of
  $$
  m=q-k-1
  $$
  old active diameter excesses is a complete local coordinate system.
- The entire leftover local obstruction is carried by exactly
  $$
  s_Z+1
  $$
  residual active diameter edges.
- Attempting to make all basis coordinates nonpositive forces positive residual diameter excess, already at first order and in the exact nonlinear weighted identity.

Therefore a successful closing theorem must either:

1. control the $s_Z+1$ residual cage simultaneously with the wall/return currencies;
2. leave the local chart through a finite collective replacement;
3. change the active diameter graph by deleting a diameter cover and invoking the audit.54 refill theorem;
4. or force an exact unit equilateral triangle.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.56\` and register \`C-CONTACT-DIAMETER-COORDINATES\` as canonical.
