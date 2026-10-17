> Generated reading edition · [exact source](../../research/target_c_interval_shear_kkt_curvature_identity_2026-09-15.md) · source SHA-256 `ccc253b9e72f87055060ce508896014eac24c1bbd92325925bf70916e2dd1de2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C-II — KKT-weighted curvature identity for laminar interval shears

**Date:** 2026-09-15
**Status:** proof-only exact finite structural theorem
**Scope:** the dual-path O--O interval-shear coordinates of `target_c_laminar_multitrain_interval_shear_2026-09-15.md`
**Dependencies:** exact interval-shear theorem; audited Section 157 cut resultants; positive relative-interior KKT stress
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The old global-train-shear report derived a useful weighted second-curvature formula for
one train, but its **sign** depended on the rejected response inequality
`A_tau>w_tau`.  The response-free Section 157 audit retained only the KKT cut resultant
and two-sided first-order bracing.

The new exact laminar interval-shear coordinates permit the weighted curvature algebra
to be recovered and generalized to an entire consecutive block **without** using the
rejected response theorem and without asserting any curvature sign.

Let `tau_1,...,tau_m` be a dual-path family as in the interval-shear theorem.  For each
selected cut `i`, let

$$
A_i:=\sum_{e\in E(\tau_i)}\alpha_e>0
$$

be its total positive KKT contact weight and let `u_i` be its contact vector oriented
from `T_i` to `S_i`.  For every actual diameter pair `h`, orient it from its lower
layer to its higher layer and let `I_h` be its contiguous interval of crossed selected
cuts.  Write

$$
r_h=p_{y_h}-p_{x_h},
\qquad |r_h|=D,
\qquad \beta_h>0.
$$

Then Section 157 gives, for every selected cut,

$$
\boxed{
A_i u_i=\sum_{h:\,i\in I_h}\beta_h r_h.
}
\tag{KC.1}
$$

For an arbitrary real shear direction `c=(c_1,...,c_m)`, put

$$
A_h(c):=\sum_{i\in I_h}c_iJu_i,
\qquad
B_h(c):=\sum_{i\in I_h}c_i^2u_i.
\tag{KC.2}
$$

Along the exact finite motion `theta_i=t c_i`, every active diameter row has

$$
|r_h(t)|^2
=D^2+2t\,r_h\cdot A_h(c)
+t^2\bigl(|A_h(c)|^2-r_h\cdot B_h(c)\bigr)
+O(t^3).
\tag{KC.3}
$$

The theorem is:

### Theorem KC.1 — weighted first variation vanishes identically

$$
\boxed{
\sum_h\beta_h\,r_h\cdot A_h(c)=0
\qquad\text{for every }c\in\mathbb R^m.
}
\tag{KC.4}
$$

### Theorem KC.2 — exact weighted quadratic coefficient

Define

$$
\boxed{
Q(c):=
\sum_h\beta_h|A_h(c)|^2
-\sum_{i=1}^m A_i c_i^2.
}
\tag{KC.5}
$$

Then

$$
\boxed{
\sum_h\beta_h|r_h(t)|^2
=D^2\sum_h\beta_h+t^2Q(c)+O(t^3).
}
\tag{KC.6}
$$

Equivalently,

$$
\boxed{
{1\over2}{d^2\over dt^2}
\sum_h\beta_h|r_h(t)|^2\Big|_{t=0}
=Q(c).
}
\tag{KC.7}
$$

No sign of `Q(c)` is asserted.

---

## 1. Orientation compatibility across all selected cuts

The interval-shear theorem chooses nested shores

$$
S_1\supseteq\cdots\supseteq S_m
$$

and defines a layer index `ell(v)`.  If `h=xy` is oriented so

$$
\ell(x)<\ell(y),
$$

then for every `i in I_h` one has `x in T_i` and `y in S_i`.  Thus the single vector

$$
r_h=p_y-p_x
$$

has exactly the orientation used in the Section 157 shore resultant for **every**
selected cut it crosses.  No extra signs are needed in (KC.1).

This compatibility is specific to a laminar path orientation and is one reason the
interval reduction is stronger than an arbitrary collection of O--O cuts.

---

## 2. Proof of the first-variation identity

Using (KC.2), interchange the finite sums:

$$
\begin{aligned}
\sum_h\beta_h r_h\cdot A_h(c)
&=\sum_h\beta_h
  \sum_{i\in I_h}c_i\,r_h\cdot Ju_i\\
&=\sum_i c_i
  \left(\sum_{h:\,i\in I_h}\beta_h r_h\right)\cdot Ju_i.
\end{aligned}
$$

Apply (KC.1):

$$
\sum_h\beta_h r_h\cdot A_h(c)
=\sum_i c_i A_i u_i\cdot Ju_i=0.
$$

This proves (KC.4).  It is precisely KKT stationarity restricted to the exact
multi-train contact-preserving motion, derived directly from the cut resultants.

---

## 3. Proof of the quadratic identity

Multiply the `t^2` coefficient in (KC.3) by `beta_h` and sum over all actual diameter
rows.  The positive part is already

$$
\sum_h\beta_h|A_h(c)|^2.
$$

For the longitudinal part,

$$
\begin{aligned}
\sum_h\beta_h r_h\cdot B_h(c)
&=\sum_h\beta_h
  \sum_{i\in I_h}c_i^2 r_h\cdot u_i\\
&=\sum_i c_i^2
  \left(\sum_{h:\,i\in I_h}\beta_h r_h\right)\cdot u_i\\
&=\sum_i A_i c_i^2,
\end{aligned}
$$

again by (KC.1).  Substitution gives (KC.5)--(KC.7).

The proof uses no response conductance, no lower bound on an individual KKT
coefficient, and no assumption that a diameter chord has positive longitudinal
projection by itself.

---

## 4. Interval-Gram matrix form

Define the diameter co-crossing weight kernel

$$
W_{ij}:=
\sum_{h:\,i,j\in I_h}\beta_h.
\tag{KC.8}
$$

Because every `I_h` is a contiguous interval, `W` is a sum of positive weighted
interval indicator outer products.  In particular it is positive semidefinite.

Expanding the first term of (KC.5),

$$
\sum_h\beta_h|A_h(c)|^2
=\sum_{i,j}c_ic_j\,(u_i\cdot u_j)W_{ij}.
\tag{KC.9}
$$

Hence

$$
\boxed{
Q(c)=c^T\left(K-\operatorname{diag}(A_1,\ldots,A_m)\right)c,
}
\tag{KC.10}
$$

where

$$
K_{ij}:=(u_i\cdot u_j)W_{ij}.
\tag{KC.11}
$$

The matrix `K` is positive semidefinite as well: it is the Gram sum

$$
K=\sum_h\beta_h V_h^TV_h,
$$

where the two rows of `V_h` are the Cartesian components of the vectors
`1_{i in I_h}Ju_i`.

At the single-coordinate vector `c=e_i`,

$$
Q(e_i)=w_i-A_i,
\qquad
w_i:=\sum_{h:\,i\in I_h}\beta_h.
\tag{KC.12}
$$

Thus the old rejected strict inequality `A_i>w_i` would exactly say that every
coordinate diagonal curvature is negative.  The present theorem does **not** assume or
recover that sign.

---

## 5. Near-common directions and the live rectangle

On the phase-collapsed small-leaf rectangle, after trimming, all selected leaf
contact directions lie in one projective window of width `O(D^{-1})`.  After choosing
consistent real orientations along the dual path,

$$
u_i\cdot u_j=1-O(D^{-2})
$$

uniformly on any fixed-density trimmed block.

Therefore `K` is an `O(D^{-2})` angular perturbation, entrywise relative to `W`, of the
pure interval kernel obtained when all leaf directions are equal.  The main remaining
unknown in (KC.10) is not phase disorder; it is the diagonal KKT contact-resultant
mass `A_i` versus the interval co-crossing kernel generated by the actual diameter
thrackle.

This cleanly isolates the next closing obligation:

1. prove that `K-diag(A)` has a negative direction using geometry/KKT normalization; or
2. show that positive semidefiniteness forced by local minimality is incompatible with
   the live rectangle's interval pattern and near-common `u_i`.

Either route would use the full simultaneous block rather than repeating one-train
bracing.

---

## 6. What the identity does and does not imply

A negative value `Q(c)<0` is **not by itself** a global-minimality contradiction.  The
active diameter max function may have a first-order cusp: individual diameter rows can
have first derivatives of both signs even though their KKT-weighted average vanishes.
This is exactly the one-coordinate regression emphasized in the old ZGS report.

To turn (KC.10) into a strict diameter decrease one still needs a direction that
controls all first-order active rows, or a second-order variational theorem on the
appropriate critical cone.

The contribution here is narrower and exact:

```text
exact laminar multi-shear
+ positive KKT cut resultants
= exact interval-Gram weighted curvature matrix K-diag(A)
```

with no rejected response input.

**Disposition:** proved proof-only exact KKT interval-curvature identity. C-II and
Level I remain open.
