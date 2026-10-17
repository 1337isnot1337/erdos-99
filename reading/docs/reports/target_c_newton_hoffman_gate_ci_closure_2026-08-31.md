> Generated reading edition · [exact source](../../../docs/reports/target_c_newton_hoffman_gate_ci_closure_2026-08-31.md) · source SHA-256 `6a8b820bab247a0fb3ab85a4cf4052c82cb242ed3bf161aff04054d5d4746c3e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-18B993FE7458","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: Newton–Hoffman closure of Gate C-I

**Date:** 2026-08-31  
**Repository base:** `f173aa9b` (main after second-order support duality C62 / PR #64)  
**Run type:** exact nonlinear integration / quadratic Farkas iteration  
**Target:** Target C Gate C-I  
**Depends on:** C6 strong/weak critical rows, C54 universal PSD for every normalized KKT stress, C62 second-order support duality

## LEVEL I STATUS

**STILL OPEN, BUT GATE C-I IS CLOSED.**

C62 proves that the fixed-direction second-order acceleration system is feasible and identifies its exactly frozen support. The remaining issue there was jet stitching. This report removes that issue completely.

The active distance constraints are exact quadratic functions of the displacement. At any current displacement `x`, Farkas duality and C54 universal PSD imply that the fixed base rigidity matrix can linearly correct the entire current strong-row error. A Hoffman error bound chooses that correction with norm proportional to the present violation. The only new error after the correction is the change in the quadratic term, which is smaller by an extra factor `O(|x|)`. Starting at `x_0=t v`, the violation is `O(t^2)` and the correction series converges geometrically with total norm `O(t^2)`.

Thus every fixed-diameter critical velocity is tangent to actual nearby configurations satisfying every strong active inequality. For a relative-interior weak-release velocity, weak rows retain their strict `Theta(t)` slack. Consequently weak unit contacts can be removed at the same globally minimal diameter, contradicting contact minimality.

Hence

```math
\boxed{C=C_*}.
```

Gate C-I is closed. Only the fully force-visible Gate C-II remains.

## 1. Exact signed quadratic system

Let the base configuration be `A={p_1,...,p_n}` with globally minimal diameter `D`. For a displacement

```math
x=(x_1,\ldots,x_n)\in(\mathbb R^2)^n
```

define, for an active unit contact `e=ij`,

```math
g_e(x)=|p_i-p_j+x_i-x_j|^2-1,
\tag{C63.1}
```

and, for an active diameter pair `h=ij`,

```math
g_h(x)=D^2-|p_i-p_j+x_i-x_j|^2.
\tag{C63.2}
```

Feasibility is `g>=0`. Writing `r_ij=p_i-p_j` and `d_ij(x)=x_i-x_j`, we have the exact identity

```math
\boxed{g(x)=\mathcal A x+Q(x),}
\tag{C63.3}
```

with

```math
(\mathcal A x)_{ij}=
\begin{cases}
2r_{ij}\cdot d_{ij}(x),&ij\in C,\\
-2r_{ij}\cdot d_{ij}(x),&ij\in H,
\end{cases}
\tag{C63.4}
```

and

```math
Q_{ij}(x)=
\begin{cases}
|d_{ij}(x)|^2,&ij\in C,\\
-|d_{ij}(x)|^2,&ij\in H.
\end{cases}
\tag{C63.5}
```

There is no Taylor remainder.

Let `E_*=C_* union H_*` be the maximal normalized KKT support, and restrict the row map and quadratic map to it, writing `A_*` and `Q_*`. By C6,

```math
\mathcal A_*v=0
\tag{C63.6}
```

for every fixed-diameter critical velocity `v`.

## 2. Every nonnegative left multiplier has nonnegative quadratic pairing

Let

```math
\mathcal M=\{\lambda\ge0:\lambda^{\mathsf T}\mathcal A_*=0\}.
\tag{C63.7}
```

A nonzero `lambda in M` has positive total diameter coefficient. If its diameter coefficients were all zero, it would be a nonnegative equilibrium stress using only unit contacts. At each vertex,

```math
\sum_j\alpha_{ij}(p_i-p_j)=0.
```

Dot with `p_i`, sum over all vertices, and combine the two endpoint contributions of each contact edge. Since every such edge has length one,

```math
0=\sum_{ij}\alpha_{ij}|p_i-p_j|^2=\sum_{ij}\alpha_{ij},
```

forcing `lambda=0`.

Hence every nonzero `lambda in M` can be divided by its positive total diameter coefficient to obtain a normalized KKT stress `s`. By C54,

```math
\Omega_s=L_C(\alpha)-L_H(\beta)\succeq0.
\tag{C63.8}
```

For every displacement `x`, the multiplier pairing with the exact quadratic part is, up to that positive normalization factor,

```math
\lambda^{\mathsf T}Q_*(x)
=
\sum_C\alpha_e|d_e(x)|^2-
\sum_H\beta_h|d_h(x)|^2.
```

Therefore

```math
\boxed{
\lambda^{\mathsf T}Q_*(x)\ge0
\qquad(\lambda\in\mathcal M,\ x\in(\mathbb R^2)^n).
}
\tag{C63.9}
```

The important point is that C63.9 is global in the correction field `x`; it is not restricted to critical velocities.

## 3. Farkas correction at an arbitrary iterate

Fix any displacement `x`. Consider

```math
\boxed{
\mathcal A_*y\ge-g_*(x).
}
\tag{C63.10}
```

The Farkas alternative says this system is feasible iff, for every `lambda>=0` with `lambda^T A_*=0`,

```math
\lambda^{\mathsf T}[-g_*(x)]\le0.
```

But

```math
\lambda^{\mathsf T}g_*(x)
=
\lambda^{\mathsf T}\mathcal A_*x+
\lambda^{\mathsf T}Q_*(x)
=
\lambda^{\mathsf T}Q_*(x)
\ge0
\tag{C63.11}
```

by C63.9. Thus:

### Lemma C63.1

For every displacement `x`, the linear correction system C63.10 is feasible.

This is the nonlinear strengthening of C62.1: after every correction, not only at the original second-order jet, the residual admits another base-linear repair.

## 4. Uniform Hoffman correction bound

For the fixed matrix `A_*`, Hoffman's linear error bound gives a constant

```math
H=H(\mathcal A_*)<\infty
\tag{C63.12}
```

such that for every feasible right-hand side `b` and every test point `u`,

```math
\operatorname{dist}(u,\{y:\mathcal A_*y\ge b\})
\le H\,|[b-\mathcal A_*u]_+|.
\tag{C63.13}
```

Apply this with `u=0` and `b=-g_*(x)`. Lemma C63.1 gives feasibility, so there is a correction satisfying C63.10 and

```math
\boxed{
|y|\le H\,|[g_*(x)]_-|.
}
\tag{C63.14}
```

This exact fixed-matrix/right-hand-side form is the classical Hoffman theorem. One modern reference is J. F. Peña, J. Vera, and L. F. Zuluaga, *New characterizations of Hoffman constants for systems of linear constraints*, Proposition 1, arXiv:1905.02894 (2019): for fixed `A`, the same Hoffman constant works for every feasible right-hand side.

## 5. Quadratic contraction estimate

Fix norms on the finite-dimensional displacement and row spaces. Since `Q_*` is a fixed finite family of squared edge-difference forms, some constant `L` satisfies

```math
\boxed{
|Q_*(x+y)-Q_*(x)|
\le L(|x|\,|y|+|y|^2).
}
\tag{C63.15}
```

Let

```math
\varepsilon(x)=|[g_*(x)]_-|.
```

Choose a Hoffman correction `y` and put `x'=x+y`. Since

```math
g_*(x)+\mathcal A_*y\ge0,
```

all possible new negative slack comes from changing the quadratic part. Hence

```math
\begin{aligned}
\varepsilon(x')
&\le |Q_*(x+y)-Q_*(x)|\\
&\le L\bigl(H|x|\varepsilon(x)+H^2\varepsilon(x)^2\bigr).
\end{aligned}
\tag{C63.16}
```

Thus, inside an `O(t)` neighborhood of the origin, one correction multiplies the current violation by `O(t)`.

## 6. Newton–Hoffman convergence

### Theorem C63 (critical-cone integrability)

Let `v` be any fixed-diameter critical velocity. For every sufficiently small `t>0` there exists a displacement `x(t)` such that

```math
\boxed{x(t)=tv+O(t^2)}
\tag{C63.17}
```

and

```math
\boxed{g_e(x(t))\ge0\qquad(e\in E_*).}
\tag{C63.18}
```

#### Proof

Start with

```math
x_0=tv.
```

By C63.6,

```math
g_*(x_0)=Q_*(tv)=O(t^2),
\qquad
\varepsilon_0=O(t^2).
\tag{C63.19}
```

Given `x_k`, choose `y_k` by Lemma C63.1 and C63.14, and set

```math
x_{k+1}=x_k+y_k.
```

Then

```math
|y_k|\le H\varepsilon_k.
\tag{C63.20}
```

Choose constants `C_0,C_1` so that initially

```math
|x_0|\le C_0t,
\qquad
\varepsilon_0\le C_1t^2.
```

Suppose inductively that

```math
|x_k|\le2C_0t
```

and `t` is small enough that

```math
2LHC_0t+LH^2C_1t^2\le\frac12.
\tag{C63.21}
```

Then C63.16 gives

```math
\varepsilon_{k+1}\le\frac12\varepsilon_k.
\tag{C63.22}
```

Consequently

```math
\sum_{k\ge0}|y_k|
\le H\sum_{k\ge0}\varepsilon_k
\le2H\varepsilon_0
=O(t^2).
\tag{C63.23}
```

After decreasing `t` once more, this total correction is at most `C_0t`, so the inductive bound on `|x_k|` is self-consistent. Hence `x_k` converges to a limit

```math
x(t)=tv+O(t^2).
```

Also `\varepsilon_k\to0`; continuity of `g_*` yields C63.18. `\square`

This constructs actual feasible points. No formal power series or smooth-path theorem is used.

## 7. Weak and inactive rows

Take now

```math
v\in\operatorname{ri}\mathcal K_D(A).
```

C6 says every active row outside `E_*` has strict signed first variation. For such a weak row `w`, C63.17 gives

```math
g_w(x(t))
=t(\mathcal Av)_w+O(t^2)>0
\tag{C63.24}
```

for all sufficiently small positive `t`.

Every initially inactive pair has fixed strict slack: its distance lies strictly between the active boundaries relevant to unit separation and diameter. Since there are finitely many pairs and `x(t)=O(t)`, all inactive inequalities remain strict for small `t`.

Thus the perturbed configuration is unit-separated and has diameter at most `D`.
Because `D=D(n)` is the globally minimal diameter for `n` unit-separated points, its diameter is also at least `D`. Therefore

```math
\boxed{\operatorname{diam}A(t)=D.}
\tag{C63.25}
```

exactly.

## 8. Gate C-I

Assume the contact-minimal triangle-free global minimizer has a weak unit contact. Choose the relative-interior critical velocity supplied by C6. Every weak active row has strict first variation.

Apply Theorem C63. Strong rows are feasible, weak unit contacts become strict, and inactive rows retain strict slack. Hence no new unit contact appears, while every weak unit contact disappears. The perturbed set is still triangle-free, unit-separated, and has the same globally minimal diameter `D`, but it has fewer unit contacts than the contact-minimal source. Contradiction.

### Corollary C63.2 (Gate C-I closed)

```math
\boxed{C=C_*.}
\tag{C63.26}
```

Every unit contact of the contact-minimal triangle-free global minimizer is KKT-supported.

## 9. Relation to C62

C62 proves one common acceleration with strict second-order slack outside the velocity-specific zero-energy face, but correctly leaves an exact jet-stitching problem on the frozen support.

C63 does not choose one acceleration and try to integrate it. Instead it repeatedly re-solves the full strong-row correction system after the exact quadratic residual is known. Universal PSD makes every one of those linear correction systems feasible, and Hoffman bounds their size. This iterative repair is precisely what removes the C62 stitching obstruction.

The body-hinge chain C57-C61 remains valid and useful structural information, but Gate C-I no longer depends on its support-coverage hypotheses.

## 10. Audit points

- No fixed stress is assumed: Farkas tests the entire nonnegative equilibrium multiplier cone at every iterate.
- No MFCQ/Slater hypothesis is assumed.
- A pure positive contact equilibrium cannot occur, so every nonzero Farkas multiplier normalizes to an actual KKT stress.
- C54 PSD is used on arbitrary displacement fields, which is exactly what C63.9 requires.
- The Hoffman constant is uniform in the changing feasible right-hand side because the matrix is fixed.
- Weak `Theta(t)` slack dominates the total `O(t^2)` correction.
- The argument constructs actual feasible configurations, not merely second-order jets.
- Exact diameter follows from global minimality once unit separation and `diameter<=D` are established.

## 11. Remaining Target C task

The proof now enters the fully force-visible phase

```math
C=C_*.
```

Gate C-II must rule out a triangle-free global minimizer in which every unit contact is supported by normalized KKT stresses. All previous C-II degree, bridge, response, force-hull, and separator theorems can now be used without the weak-contact alternative.

## 12. Compact handoff

**LEVEL I STATUS:** still open. **GATE C-I: CLOSED.**

**C63:** for the exact quadratic strong active system `g_*(x)=A_*x+Q_*(x)`, universal PSD implies that every current residual has a Farkas-feasible base-linear correction. A fixed Hoffman bound makes that correction proportional to the violation; the quadratic remainder contracts the violation by `O(t)`. Starting from `tv`, the convergent correction series has total size `O(t^2)` and yields actual feasible points `tv+O(t^2)`.

For a relative-interior critical velocity, all weak rows remain strictly feasible. A weak unit contact would therefore be removable at exact minimal diameter, contradicting contact minimality.

**Conclusion:** `C=C_*`. Gate C-I is complete.

**Next:** finish fully force-visible Gate C-II.
