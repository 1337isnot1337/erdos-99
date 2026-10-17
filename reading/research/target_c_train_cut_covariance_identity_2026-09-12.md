> Generated reading edition · [exact source](../../research/target_c_train_cut_covariance_identity_2026-09-12.md) · source SHA-256 `e1afa5e7360315d43e8c7041ea484270a53b310ea329150dbc9df1ee52120550`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "9ac5c4cba11f020d94f7c55d969eeece54ff1563", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_train_cut_covariance_identity_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "6f6cce0c48fde050be5c6cc60d6ba5939ea105dd515c3b7d4ffc0c9db034486f"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact train-cut covariance identity

**Date:** 2026-09-12  
**Base state:** `2026-09-12.audit.46`, canonical through Section 123  
**Classification:** proved candidate awaiting independent audit; theorem-state authority unchanged  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note records the matrix consequence of the exact pure-tooth train-cut
coordinates and the shore KKT resultants.  It is a metric strengthening of the
support-only Section-158 regression, but it still does not close the endpoint.

The implication chain is

```text
binary train-cut coordinates + shore KKT resultants
 -> exact weighted train/diameter covariance
 -> spectral nullity and angular-slack identities
 -> a possible metric incompatibility with the odd-unicyclic diameter thrackle
```

The final incompatibility is not proved here.

## 1. Exact matrices

Use the exact pure-tooth normal form of proof-only Section 126.  There are `q`
outer-to-outer trains and `q` actual diameter edges.  For each train `tau`, choose
the shore orientation and its unit cut vector `u_tau`.  For each diameter edge
`h`, choose an orientation and write

```math
r_h=p_{y_h}-p_{x_h},\qquad |r_h|=D.
```

Define the signed shore-separation matrix

```math
E_{h\tau}=\varepsilon_{h\tau}
 :=\chi_\tau(y_h)-\chi_\tau(x_h)\in\{-1,0,1\}.
```

The exact Section-159 displacement identity, written row-wise, is

```math
\boxed{R=EU},
\tag{TC.1}
```

where `U` is the `q x 2` matrix whose `tau`-row is `u_tau`, and `R` is the
`q x 2` matrix whose `h`-row is `r_h`.

For the relative-interior KKT stress, put `B_beta=diag(beta_h)` and

```math
a_\tau:=\sum_{e\in\tau}\alpha_e>0,
\qquad A_\alpha:=\operatorname{diag}(a_\tau).
```

The exact shore sum from Section 127 is, with the same sign convention,

```math
a_\tau u_\tau
 =\sum_h\beta_h\varepsilon_{h\tau}r_h.
\tag{TC.2}
```

In matrix form this is

```math
\boxed{A_\alpha U=E^{\mathsf T}B_\beta R
       =E^{\mathsf T}B_\beta E U.}
\tag{TC.3}
```

No diameter coefficient lower bound is used.  The identity only uses the actual
positive relative-interior stress and the fact that every train is a global cut.

## 2. Weighted covariance identity

Left-multiply (TC.3) by `U^T`.  Since `R=EU`, this gives the exact symmetric
two-dimensional covariance equality

```math
\boxed{
U^{\mathsf T}A_\alpha U
 =R^{\mathsf T}B_\beta R.
}
\tag{TC.4}
```

Equivalently, for every `z\in\mathbb R^2`,

```math
\boxed{
\sum_\tau a_\tau(z\cdot u_\tau)^2
 =\sum_h\beta_h(z\cdot r_h)^2.
}
\tag{TC.5}
```

Taking traces and using `|u_tau|=1`, `|r_h|=D`, `sum_h beta_h=1`, and the
normalized KKT virial `sum_tau a_tau=sum_e alpha_e=D^2`, gives

```math
\operatorname{tr}(U^{\mathsf T}A_\alpha U)
 =\operatorname{tr}(R^{\mathsf T}B_\beta R)=D^2.
\tag{TC.6}
```

Thus the train-cut system does not merely reproduce the scalar shore resultant:
its entire second moment in the two physical directions agrees with the actual
diameter second moment.

## 3. Spectral nullity forced by the geometry

Set

```math
W:=E^{\mathsf T}B_\beta E.
```

Then `W` is positive semidefinite and (TC.3) says

```math
\boxed{(W-A_\alpha)U=0.}
\tag{TC.7}
```

The train directions span the plane because the pure endpoint contains strict
rhombi with two nonparallel train directions.  Hence the two coordinate columns of
`U` are linearly independent, and

```math
\boxed{\dim\ker(W-A_\alpha)\ge2.}
\tag{TC.8}
```

Since `A_alpha` is positive diagonal, this is a genuine spectral condition on the
signed circular-split matrix `E`; it is stronger than the row/column support and
positive-left-kernel data rejected by Section 158.

The diagonal entries of `W` are

```math
W_{\tau\tau}=\sum_{h\pitchfork\tau}\beta_h,
\tag{TC.9}
```

and (TC.7) also recovers the finite train resultant and angular-slack formula

```math
a_\tau u_\tau
 =\sum_{h\pitchfork\tau}\beta_h\varepsilon_{h\tau}r_h,
\qquad
a_\tau\le D W_{\tau\tau}.
\tag{TC.10}
```

Summing (TC.10) over trains gives

```math
\boxed{
\sum_h\beta_h(t_h-D)
 ={1\over D}\sum_\tau\sum_{h\pitchfork\tau}
 \beta_h\left(D-u_\tau\cdot(\varepsilon_{h\tau}r_h)\right),
}
\tag{TC.11}
```

where `t_h` is the number of trains separating the endpoints of `h`.  Every term
on the right is nonnegative, and Section 159 gives `t_h\ge D` pointwise.

## 4. What this does and does not close

The new exact content is (TC.4)--(TC.8): the metric endpoint supplies a
two-dimensional nullspace of a concrete PSD-minus-positive-diagonal matrix built
from the actual train cuts and the positive diameter stress.  This is a valid target
for a future circular-split/odd-thrackle theorem.

It does **not** imply `W=A_alpha`, a uniform lower bound on any `beta_h`, or a
contradiction from planarity.  The trace identity (TC.6) is the already-known
virial equality in train coordinates, and the pointwise incidence floor alone still
allows cancellation among the unit vectors.  In particular, no Schur kernel or
finite source motion is inferred from (TC.8).

The correct next lemma would have to prove one of:

1. the circular interval structure of `E` forces `W-A_alpha` to have fewer than two
   zero directions under the odd-unicyclic convex-thrackle geometry;
2. the train-direction crossing gaps force a strict covariance inequality in some
   direction `z`; or
3. (TC.11) is quantitatively positive and can be charged to the remaining
   aggregate detour/source-preserving descent branch.

The support-only Section-158 family is not a counterexample to this note because it
does not provide realized unit vectors, the displacement identity, and (TC.3)
simultaneously. Conversely, this note is not a closure theorem: it leaves the
metric circular-split compatibility problem explicit.

## 5. Circulant algebraic regression

The covariance condition itself cannot be upgraded to a contradiction.  There is a
finite family satisfying the exact metric cut identity and the positive shore
resultants at the odd-shell scale.

Let `q` be odd, let `r=(q-1)/2`, and choose an integer `2<=ell<q/2`.  Index loaded
vertices and trains by `Z/qZ`.  For train `s`, let its cut shore be the cyclic
interval

```math
S_s=\{s,s+1,\ldots,s+\ell-1\}.
```

Take

```math
u_s=(\cos(2\pi s/q),\sin(2\pi s/q))
```

and define loaded points by the exact binary cut coordinates

```math
p_i=\sum_s\chi_{S_s}(i)u_s.
\tag{TC.12}
```

The points `p_i` form a regular `q`-gon.  Its `r`-step edges are the diameter
edges of length `D`; the corresponding signed cut matrix is

```math
E_{is}=\chi_{S_s}(i+r)-\chi_{S_s}(i),
```

and its displacement rows satisfy `r_i=p_(i+r)-p_i=(EU)_i` exactly.  With uniform
diameter weights `beta_i=1/q`, the circulant matrix `E^T B_beta E` has the first
Fourier sine/cosine pair as an eigenspace.  The two-dimensional unit-direction
matrix `U` therefore satisfies

```math
E^{\mathsf T}B_\beta E U={D^2\over q}U.
\tag{TC.13}
```

Setting `a_tau=D^2/q` gives the exact shore resultant (TC.3), positive contact
train weights, `sum_tau a_tau=D^2`, and the covariance identity (TC.4).  For
`ell/q` near `1/3`,

```math
{D\over q}\longrightarrow {2\over\pi}\sin(\pi/3)={\sqrt3\over\pi},
\qquad
{q\over D}\longrightarrow {\pi\over\sqrt3}=1.813799\ldots,
\tag{TC.14}
```

which is on the current Type-II scale.

This is deliberately only an algebraic/metric regression.  The regularly spaced
train directions do not supply the strict-rhombus crossing graph with its
projective angle greater than `pi/3`; no full contact complex or global minimizer is
claimed.  Its exact implication is narrower:

```math
\boxed{
\text{covariance + binary circular cuts + odd-shell diameter support}
\not\Longrightarrow\text{C-II closure}.
}
```

The missing closing input must therefore use the actual triangle-free train
crossing graph, its angular defect/phase budget, or a finite source-preserving
diameter descent.

**Disposition:** proved candidate awaiting independent audit. No promotion or
theorem-state mutation is made; C-II remains open.
