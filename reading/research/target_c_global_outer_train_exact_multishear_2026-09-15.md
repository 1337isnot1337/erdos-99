> Generated reading edition · [exact source](../../research/target_c_global_outer_train_exact_multishear_2026-09-15.md) · source SHA-256 `234ccd07283ae588eb612baa0c49384b2bdaa51f7682138686b1ab3bc5e80525`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target C-II — exact simultaneous finite shear for arbitrary outer-to-outer trains

**Date:** 2026-09-15
**Status:** proof-only exact finite structural theorem
**Scope:** any finite family of outer-to-outer complete stopped trains
**Dependencies:** audited finite stopped-train partition; audited O--O cutset/shear primitive, including the singleton-bridge case; positive relative-interior KKT stress for the weighted corollary
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The audited one-train shear theorem is stronger than previously exploited. Exact finite
shears do not merely superpose at first order. They superpose **exactly at finite
amplitude** for an arbitrary family of outer-to-outer trains, even when their midpoint
crosscuts intersect.

The reason is purely combinatorial: the shore cut of an O--O train separates exactly
the contact edges belonging to that train. Since the stopped-train decomposition
partitions contact edges, every other train's contact has both endpoints on the same
side of that cut.

Let

```math
\mathcal T=\{\tau_1,\ldots,\tau_m\}
```

be any finite family of distinct O--O complete trains. For each `i`, choose its audited
shore split

```math
V=S_i\sqcup T_i
```

and choose the unit train contact vector `u_i` so every contact edge of `tau_i`, when
oriented from `T_i` to `S_i`, has vector `u_i`. For a non-singleton this is the Jordan
shore split from the train midpoint crosscut; for an O--O singleton it is the audited
bridge shore split.

For arbitrary parameters `theta=(theta_1,...,theta_m)`, put

```math
\Delta_i(\theta_i)=R_{\theta_i}u_i-u_i
\tag{GM.1}
```

and define the full-source placement

```math
\boxed{
p_v(\theta)
=p_v+\sum_{i:\,v\in S_i}\Delta_i(\theta_i).
}
\tag{GM.2}
```

Then every old unit contact is preserved **exactly** for every `theta`. For all
sufficiently small `theta`, every strict old noncontact remains strictly longer than
one.

Thus every finite O--O family supplies an exact multi-parameter contact-preserving
finite deformation of the full source.

---

## 1. Exact contact preservation needs no laminarity

Take an old unit contact `xy` and let `tau_j` be its unique complete stopped train.

If `tau_j` is selected, the audited cutset statement for cut `j` says its endpoints lie
on opposite shores. Orient `xy` from `T_j` to `S_j`, so

```math
p_y-p_x=u_j.
```

For every selected `i\ne j`, the cutset statement for `tau_i` says that a contact edge
has opposite-shore endpoints only if it belongs to `tau_i`. Since stopped trains
partition contact edges, `xy` does not belong to `tau_i`, so its endpoints lie on the
same side of cut `i`. Hence all increments except `Delta_j` cancel and

```math
p_y(\theta)-p_x(\theta)
=u_j+\Delta_j
=R_{\theta_j}u_j.
\tag{GM.3}
```

Its length is exactly one.

If `tau_j` is not selected, the endpoints lie on the same side of every selected cut,
so every added translation cancels and the contact vector is unchanged.

No relation among the selected cuts was used. They may be nested, disjoint, or
mutually crossing.

Because the full source is finite, strict old noncontact lower-distance inequalities
persist in one neighborhood of `theta=0` by continuity. Contact-isolated source points
are included in (GM.2) using their geometric shore memberships exactly as in the
audited one-train finite shear.

### Theorem GM.1 — arbitrary O--O finite multishear

Equation (GM.2) is an exact `m`-parameter contact-preserving finite motion of the full
source for every finite family of O--O trains. It preserves unit separation for all
sufficiently small parameter vectors.

No diameter monotonicity is asserted.

---

## 2. Exact signed split support of every source pair

Fix an arbitrary orientation `h=xy` of any source pair and define

```math
\sigma_{hi}
:=\mathbf 1_{S_i}(y)-\mathbf 1_{S_i}(x)
\in\{-1,0,1\}.
\tag{GM.4}
```

Then subtracting (GM.2) gives the exact identity

```math
\boxed{
r_h(\theta)
:=p_y(\theta)-p_x(\theta)
=r_h+\sum_{i=1}^m\sigma_{hi}\Delta_i(\theta_i).
}
\tag{GM.5}
```

The support of row `h` is exactly the selected O--O cuts that separate its two
endpoints. This is the finite nonlinear version of the old split-matrix first-order
picture.

For a pairwise noncrossing selected family, rooting its complement dual tree makes the
nonzero support of a pair exactly the unique dual-tree path between its endpoint
regions. On one dual-path block, consistent pair orientation makes this a contiguous
unsigned interval, recovering the interval-shear theorem as a specialization.

---

## 3. Exact first and second variations

Along one scalar direction

```math
\theta_i=t c_i,
```

put

```math
A_h(c):=\sum_i\sigma_{hi}c_iJu_i,
\qquad
B_h(c):=\sum_i\sigma_{hi}c_i^2u_i.
\tag{GM.6}
```

Then

```math
r_h(t)=r_h+tA_h(c)-{t^2\over2}B_h(c)+O(t^3),
\tag{GM.7}
```

and for an active diameter row `|r_h|=D`,

```math
\boxed{
|r_h(t)|^2
=D^2+2t\,r_h\cdot A_h(c)
+t^2\bigl(|A_h(c)|^2-r_h\cdot B_h(c)\bigr)
+O(t^3).
}
\tag{GM.8}
```

The signs in `B_h` are essential for crossing cut families; they disappear only in the
consistently oriented laminar-path specialization.

---

## 4. KKT cut resultants give a global weighted curvature identity

Let `alpha_e>0` and `beta_h>0` be a relative-interior KKT stress. Put

```math
A_i:=\sum_{e\in E(\tau_i)}\alpha_e>0.
\tag{GM.9}
```

For a fixed selected cut `i`, if `h=xy` has the global orientation used in (GM.4),
then

```math
\sigma_{hi}r_h
```

is exactly the diameter vector oriented from `T_i` to `S_i` whenever the row crosses
that cut. Therefore audited Section 157 becomes

```math
\boxed{
A_i u_i
=\sum_h\beta_h\sigma_{hi}r_h.
}
\tag{GM.10}
```

Taking the dot product with `Ju_i` and summing against arbitrary coefficients gives

```math
\boxed{
\sum_h\beta_h r_h\cdot A_h(c)=0.
}
\tag{GM.11}
```

Similarly,

```math
\begin{aligned}
\sum_h\beta_h r_h\cdot B_h(c)
&=\sum_i c_i^2
  \left(\sum_h\beta_h\sigma_{hi}r_h\right)\cdot u_i\\
&=\sum_iA_i c_i^2.
\end{aligned}
\tag{GM.12}
```

Hence the exact weighted `t^2` coefficient is

```math
\boxed{
Q_{\mathcal T}(c)
=\sum_h\beta_h
 \left|\sum_i\sigma_{hi}c_iJu_i\right|^2
-\sum_iA_i c_i^2.
}
\tag{GM.13}
```

Equivalently,

```math
\boxed{
{1\over2}{d^2\over dt^2}
\sum_h\beta_h|r_h(t)|^2\Big|_{t=0}
=Q_{\mathcal T}(c).
}
\tag{GM.14}
```

This generalizes the interval-Gram formula and uses no rejected response theorem. No
sign of `Q_T` is claimed.

---

## 5. Split-Gram matrix form

Define the two-dimensional row vectors

```math
v_{hi}:=\sigma_{hi}Ju_i.
```

Then

```math
K_{ij}
=(u_i\cdot u_j)
 \sum_h\beta_h\sigma_{hi}\sigma_{hj}
\tag{GM.15}
```

satisfies

```math
\sum_h\beta_h
 \left|\sum_i\sigma_{hi}c_iJu_i\right|^2
=c^TKc.
```

The matrix `K` is positive semidefinite because it is a positive weighted Gram sum of
the signed split rows. Therefore

```math
\boxed{
Q_{\mathcal T}(c)
=c^T\bigl(K-\operatorname{diag}(A_i)\bigr)c.
}
\tag{GM.16}
```

The old rejected inequality `A_i>w_i` would make each coordinate diagonal negative,
but it is neither assumed nor needed for the identity.

---

## 6. Application to the new two-leaf frontier

The near-frontier theorem for `t<=1.8436` proves retained O--O pair weights

```math
P_U>0.103-o(1),
\qquad
P_V>0.103-o(1)
```

in the two distinct leaf phases of the dominant exact `pi/3` orbit. Since every
retained pair weight is at most one, the two phases contain more than

```math
0.103D-o(D)
```

distinct O--O trains each. The phase classes are disjoint, so their union contains

```math
\boxed{m>0.206D-o(D)}
\tag{GM.17}
```

distinct O--O trains.

Theorem GM.1 therefore places the live frontier inside an exact contact-preserving
finite deformation family with more than `0.206D-o(D)` explicit O--O shear
coordinates, simultaneously spanning **two exact projective directions separated by
`pi/3`**.

This is stronger than treating the two leaf O--O populations separately. Their cuts
may cross, but exact finite superposition remains valid; crossing appears only through
the signed split matrix `sigma` in the diameter constraints.

The natural closing object is now the active-diameter signed-split matrix on these two
large phase populations together with (GM.13), not a collection of unrelated one-cut
bracing statements.

---

## 7. Scope and non-conclusions

- The proof is finite and source-level; no limiting phase argument is needed for the
  multishear theorem itself.
- Intersecting train crosscuts are allowed. No complement-dual tree is needed for
  Theorem GM.1.
- The multi-shear preserves contacts and small-parameter unit separation, not the
  diameter bound.
- A negative KKT-weighted curvature is not by itself a diameter-decreasing direction;
  first-order max-function cusps remain possible.
- Equation (GM.17) uses the current proof-only two-leaf theorem and is therefore itself
  a proof-only frontier consequence, not canonical Level-I state.

**Disposition:** proved proof-only exact arbitrary-O--O finite multishear and signed
split-curvature reduction. C-II and Level I remain open.
