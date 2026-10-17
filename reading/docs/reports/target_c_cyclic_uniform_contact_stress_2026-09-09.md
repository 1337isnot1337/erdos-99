> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_uniform_contact_stress_2026-09-09.md) · source SHA-256 `6f8c22ae589ef273f7a00f276e8b36064bdf2887811fe004141ea577309222a6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 3 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-F814C5D87563","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — every `d_H=0` KKT stress has asymptotically uniform shell-contact weights

**Date:** 2026-09-09  
**Run type:** exact finite stress-cone estimate with asymptotic consequence  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** KL/EZ/PP in this PR; PS path-stress reduction; PR #125 AE bound `phi_max=O(D^-1/3)`  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The normalized KKT polytope is two-dimensional, but its shell-contact coefficients become asymptotically rigid.

Let

```math
\theta=\frac\pi q,
\qquad
\phi_i=\ell_i\theta,
\qquad
\phi_{max}=\max_i\phi_i.
```

PR #125 AE gives

```math
\phi_{max}=O(D^{-1/3}).
\tag{UC.1}
```

For **every** normalized KKT stress, including every PP extreme, every shell contact coefficient satisfies

```math
\boxed{
\alpha_e
=\frac{D^2}{q}\left(1+O(D^{-1})\right).
}
\tag{UC.2}
```

Since

```math
\frac{D^2}{q}=\frac D\pi+O(D^{-1}),
```

this is equivalently

```math
\boxed{
\alpha_e=\frac D\pi+O(1)
}
\tag{UC.3}
```

uniformly over the complete KKT polygon and over all shell contacts.

The relative spread of **all** contact coefficients in **all** normalized stresses is therefore only `O(1/D)`.

For the PS path variables,

```math
\boxed{
\max_i\sigma_i/\min_i\sigma_i=1+O(D^{-1}).
}
\tag{UC.4}
```

Consequently every walking four-bar KKT circuit from WF has four transition-contact weights with pairwise ratio `1+O(1/D)`.

---

## 1. Signed cycle directions have bounded partial sums

Use the EZ cycle notation. Let

```math
r_i:=\chi_i\nu_i,
\qquad
\chi_i=(-1)^i,
```

where `nu_i` are the projective unit directions of consecutive unique-cycle diameter edges. The angular gap from `nu_i` to `nu_{i+1}` is

```math
\phi_i=\ell_i\theta.
```

Therefore

```math
\boxed{
 r_{i+1}=-R_{\phi_i}r_i.
}
\tag{1.1}
```

Pair consecutive signed directions:

```math
|r_i+r_{i+1}|
=|r_i-R_{\phi_i}r_i|
=2\sin\frac{\phi_i}{2}
\le\phi_i.
\tag{1.2}
```

Since

```math
\sum_i\phi_i=\pi,
\tag{1.3}
```

any partial sum beginning at the fixed EZ origin has norm at most one unpaired unit vector plus the sum of some pair bounds. Hence

```math
\boxed{
|R_t|\le1+\pi
}
\tag{1.4}
```

for every partial cycle sum `R_t` appearing in KL/EZ.

This bound is absolute and does not grow with `r` or `q`.

---

## 2. The beta-functional polygon is an `O(1)` perturbation of a radius-`D` direction polygon

EZ writes the cycle beta-functional vertices as

```math
K_i
=D r_i+\lambda J M_i,
\qquad
\lambda=\sec\frac\theta2,
\tag{2.1}
```

where

```math
M_i=\frac{R_{i-1}+R_i}{2}.
```

By (1.4),

```math
|M_i|\le1+\pi.
```

Put

```math
\boxed{
C_D:=\lambda(1+\pi).
}
\tag{2.2}
```

Then

```math
\boxed{
|K_i-D r_i|\le C_D.
}
\tag{2.3}
```

Since `theta->0`,

```math
C_D=1+\pi+o(1)=O(1).
```

---

## 3. The signed direction polygon has inradius `cos(phi_max)`

Because the odd cycle length `r` is odd, addition by two visits every cycle index. Equation (1.1) gives

```math
r_{i+2}
=R_{\phi_i+\phi_{i+1}}r_i.
\tag{3.1}
```

Thus the convex order of the signed unit directions is the step-two order, with successive angular gaps

```math
g_i=\phi_i+\phi_{i+1}
\le2\phi_{max}.
\tag{3.2}
```

A polygon whose vertices lie on the unit circle and whose maximum central gap is at most `2 phi_max` contains the centered disk of radius

```math
\cos\phi_{max}.
```

Therefore

```math
\boxed{
 h_{\operatorname{conv}\{Dr_i\}}(u)
\ge
D\cos\phi_{max}|u|
}
\tag{3.3}
```

for every vector `u`.

The perturbation bound (2.3) gives the support estimate for the actual beta-functional polygon

```math
K:=\operatorname{conv}\{K_i\}:
```

```math
\boxed{
 h_K(u)
\ge
\rho_D|u|,
\qquad
\rho_D:=D\cos\phi_{max}-C_D.
}
\tag{3.4}
```

By UC.1,

```math
\boxed{
\rho_D=D-O(D^{1/3}).
}
\tag{3.5}
```

In particular `rho_D>0` for all sufficiently large sources.

---

## 4. KKT nonuniformity parameter is `O(A/D)`

KL/EZ parametrize every signed equilibrium stress by

```math
(A,c),
\qquad c\in\mathbb R^2,
```

with cycle coefficients

```math
D^2\beta_i=A-c\cdot K_i.
\tag{4.1}
```

PP proves that the complete KKT cone is exactly the cycle-halfspace cone. Hence every nonnegative KKT stress satisfies

```math
A\ge c\cdot K_i
\qquad\text{for all }i.
```

Taking the support function and using (3.4):

```math
A\ge h_K(c)
\ge\rho_D|c|.
```

Thus

```math
\boxed{
|c|\le\frac A{\rho_D}.
}
\tag{4.2}
```

The integrated KL contact formula is

```math
a_t=A-\lambda c\cdot J R_t.
\tag{4.3}
```

Using (1.4):

```math
|a_t-A|
\le C_D|c|
\le\frac{C_D}{\rho_D}A.
```

Define

```math
\boxed{
\varepsilon_D:=\frac{C_D}{\rho_D}
=O(D^{-1}).
}
\tag{4.4}
```

Then every contact coefficient obeys the finite two-sided bound

```math
\boxed{
(1-\varepsilon_D)A
\le a_t\le
(1+\varepsilon_D)A.
}
\tag{4.5}
```

This holds uniformly over the entire KKT cone after choosing any nonzero nonnegative stress.

---

## 5. Normalization pins `A` to `D^2/q`

Normalize by

```math
\sum_h\beta_h=1.
```

The virial identity gives

```math
\sum_{e\in C_q}\alpha_e=D^2.
```

There are exactly `q` shell contacts, and every `a_t` satisfies (4.5). Therefore

```math
q(1-\varepsilon_D)A
\le D^2\le
q(1+\varepsilon_D)A.
```

Hence

```math
\boxed{
\frac{D^2}{q(1+\varepsilon_D)}
\le A\le
\frac{D^2}{q(1-\varepsilon_D)}.
}
\tag{5.1}
```

Combining (4.5) and (5.1), every contact coefficient satisfies

```math
\boxed{
\frac{1-\varepsilon_D}{1+\varepsilon_D}
\frac{D^2}{q}
\le
\alpha_e
\le
\frac{1+\varepsilon_D}{1-\varepsilon_D}
\frac{D^2}{q}.
}
\tag{5.2}
```

Since `epsilon_D=O(1/D)`, UC.2 follows.

The same inequality applies to every PS path stress `sigma_i`, proving UC.4.

---

## 6. Pendant diameter coefficients are also asymptotically uniform

PS gives every pendant diameter coefficient on path `i` exactly as

```math
\beta_h=\frac{\sigma_i}{D^2}.
```

Therefore (5.2) gives

```math
\boxed{
\beta_h
=\frac1q\left(1+O(D^{-1})\right)
}
\tag{6.1}
```

uniformly over every pendant diameter edge and every normalized KKT stress.

This is stronger than universal leaf positivity: pendant beta weights cannot approach zero even when the KKT stress moves to a polygon vertex.

Since `q~pi D`,

```math
\beta_h=\frac1{\pi D}+O(D^{-2}).
```

Cycle beta coefficients remain different: PP extremes force two of them to vanish, so no analogous pointwise estimate is possible on the unique cycle.

---

## 7. Four-bar extreme stresses are almost equal-weight

WF identifies every PP extreme with two isostatic bodies joined by exactly four shell-contact bars. Each of those four contact coefficients is one of the shell values controlled by (5.2).

If their coefficients are

```math
\alpha_0,\alpha_1,\alpha_2,\alpha_3,
```

then

```math
\boxed{
\max_j\alpha_j/\min_j\alpha_j
\le
\left(\frac{1+\varepsilon_D}{1-\varepsilon_D}\right)^2
=1+O(D^{-1}).
}
\tag{7.1}
```

Thus the exact alternating force/moment balance of every walking four-bar circuit is an asymptotically equal-weight balance.

This conclusion is uniform in the extreme index and therefore holds simultaneously around the entire `r`-vertex KKT polygon.

---

## 8. Approximate unweighted four-force balance

Orient the four transition contact unit vectors consistently from the short body to its complement, so their exact KKT force balance is

```math
\alpha_0u_0-\alpha_1u_1+\alpha_2u_2-\alpha_3u_3=0
\tag{8.1}
```

for a suitable cyclic alternating convention.

Put

```math
\bar\alpha=\frac{D^2}{q}.
```

By UC.2,

```math
\alpha_j=\bar\alpha(1+O(D^{-1})).
```

Divide (8.1) by `bar alpha` to obtain

```math
\boxed{
 u_0-u_1+u_2-u_3
=O(D^{-1})
}
\tag{8.2}
```

uniformly over all KKT extremes.

Thus the four body-cut contact directions form an approximate unweighted parallelogram at angular error scale `O(1/D)` in force-vector space.

This is a mechanical consequence of the *whole stress-polytope geometry*, not an assumption of shell regularity.

---

## 9. Why no contradiction is claimed yet

For a walking short body of size

```math
m_i=\ell_{i+1}+\ell_{i+2},
```

its two shell intervals each have total turning `m_i theta` by the curvature-degree bookkeeping. When `m_i` is large, the four transition directions naturally come in two nearly antipodal pairs, so an approximate equal-weight four-force balance is geometrically plausible.

Therefore UC.8.2 is not itself a contradiction.

The next useful step is to combine **force and moment** at this precision and express the four transition lines in terms of the adjacent Reuleaux composition. A mismatch between the two interval lengths may then produce a first noncancelling moment term.

---

## 10. Regression audit

- The inradius estimate uses the step-two order of the signed cycle directions, not the ordinary projective order. The gap is `phi_i+phi_{i+1}`.
- The `O(1)` partial-sum bound uses alternating signed cycle directions. Unsigned projective direction sums would be `Theta(r)` and would not prove UC.
- The result concerns contact and pendant-diameter coefficients. Cycle beta coefficients can vanish at KKT extremes.
- The normalization `sum beta=1` is essential for the scale `D^2/q`; without normalization UC is a relative statement.
- No claim is made that all four transition weights are exactly equal in a nonuniform stress.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Signed cycle vectors satisfy
  r_{i+1}=-R_{phi_i}r_i,
so pair cancellation gives every KL partial sum
  |R_t|<=1+pi.
EZ beta-functional vertices are
  K_i=D r_i + sec(theta/2) J M_i,
thus |K_i-D r_i|<=C_D=sec(theta/2)(1+pi)=O(1).

In step-two convex order,
  r_{i+2}=R_{phi_i+phi_{i+1}}r_i.
AE gives phi_max=O(D^-1/3), so conv{Dr_i} contains a centered disk of radius
  D cos(phi_max)=D-O(D^(1/3)).
Hence the actual K polygon contains radius
  rho_D=D cos(phi_max)-C_D.

PP cone inequalities A-c.K_i>=0 imply
  |c|<=A/rho_D.
KL contact formula a_t=A-sec(theta/2)c.JR_t therefore gives
  |a_t-A|<=epsilon_D A,
  epsilon_D=C_D/rho_D=O(1/D).
Normalize sum beta=1; virial gives sum contacts=D^2. Therefore
  alpha_e=D^2/q(1+O(1/D))=D/pi+O(1)
uniformly for EVERY contact in EVERY normalized KKT stress, including extremes.
Pendant beta=sigma_i/D^2=1/q(1+O(1/D)).

Every WF four-bar extreme consequently has transition weights with ratio 1+O(1/D),
and its alternating unweighted unit-vector balance is O(1/D).

Next: add moment balance at the same precision and express the first noncancelling term
through adjacent composition lengths.
```
