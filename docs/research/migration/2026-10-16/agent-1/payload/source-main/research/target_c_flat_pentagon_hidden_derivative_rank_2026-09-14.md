# Erdos Problem #99 - flat-pentagon hidden-derivative rank

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** train-angle face-closure normal form; bounded-face train-loop exclusion; bounded-face endpoint simplicity; empty-pentagon trapezoid stability; low-t pentagon sea
**Claim class:** proof-only structural refinement awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The low-`t`, small-residual branch contains a linear sea of isolate-free pentagons
close to the flat unit trapezoid.  Existing work uses their hidden diagonals only as a
large family of near-contacts.  The same geometry has a stronger linear-algebraic
consequence: after the ordinary contact face-closure equations are imposed, the two
hidden leaf diagonals still provide linearly many independent first-order radial
coordinates.

Let `P` be any family of sufficiently flat isolate-free pentagonal bounded contact
faces and put `p=|P|`.  Let `C_face` be the full stopped-train face-closure matrix,
with

\[
\operatorname{rank}C_{face}=2f-\sigma_C,
\qquad 0\le\sigma_C\le s_Z.
\tag{HR.1}
\]

For each `F in P`, cyclically label its boundary

\[
l,m,r,a,b
\]

as in the flat-trapezoid endpoint and let `H_F` be the two rows giving the first radial
variations of the hidden chords `ma` and `mb` in train-angle coordinates.  Stack all
these rows into `H_P`.

Then, after fixing one sufficiently small flatness neighborhood,

\[
\boxed{
\operatorname{rank}\left(H_P\big|_{\ker C_{face}}\right)
\ge {7\over3}p-2f+\sigma_C.
}
\tag{HR.2}

The left side is an integer, so a negative right side is merely vacuous.  Equation
(HR.2) is finite and does not assume that the pentagon network is connected.

On a Type-II subsequence with `R_F=o(D)`, put

\[
t={q-k\over D},\qquad
\delta={b-P_F\over D},\qquad
\kappa={k\over D},
\]

\[
C_0:=2\sqrt{\Delta_2}+0.00042,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\]

The low-`t` pentagon theorem supplies a diagonal family `P` with

\[
{p\over D}
\ge \pi+C_0-{5t\over2}+\delta+{\kappa\over2}-o(1),
\tag{HR.3}
\]

while `f<=Q` and

\[
{Q\over D}=2t-\pi-\delta.
\tag{HR.4}
\]

Therefore

\[
\boxed{
\liminf {1\over D}
\operatorname{rank}\left(H_P\big|_{\ker C_{face}}\right)
\ge
R_H(t)+{13\over3}\delta+{7\over6}\kappa,
}
\tag{HR.5}
\]

where the conservative scalar floor is

\[
\boxed{
R_H(t):={13\pi\over3}+{7C_0\over3}-{59t\over6}.
}
\tag{HR.6}

At the current proof-only endpoint

\[
t_{42}={4\over9}(\pi+\sqrt{\Delta_2})+0.0013751,
\]

\[
\boxed{R_H(t_{42})=0.1532696574\ldots .}
\tag{HR.7}

Thus at least `0.15326D-o(D)` linearly independent hidden radial variations survive
after **all** ordinary bounded-face closure equations have been imposed.  The
conservative floor stays positive for

\[
\boxed{
t<{26\pi+14C_0\over59}=1.836\ldots .}
\tag{HR.8}

This is a rank statement on actual contact-framework infinitesimal flexes.  It does
not assert that the corresponding hidden chords can all be shortened with one sign,
or that any such flex is diameter-nonincreasing.

---

## 1. Local four-row rank at the flat trapezoid

Orient the five pentagon boundary vectors cyclically as

\[
e_1=l m,\quad e_2=m r,\quad e_3=r a,\quad e_4=a b,\quad e_5=b l.
\]

At the flat equality trapezoid take

\[
e_1=e_2=(1,0),
\]

\[
e_3=\left(-{1\over2},{\sqrt3\over2}\right),
\quad
e_4=(-1,0),
\quad
e_5=\left(-{1\over2},-{\sqrt3\over2}\right).
\tag{HR.9}
\]

Let `omega_i` be the angular rate of the complete stopped train containing side `e_i`.
Differentiated face closure is

\[
\sum_{i=1}^5\omega_i e_i=0,
\tag{HR.10}
\]

after applying the common invertible quarter-turn to the usual vector equation.
Writing `a=sqrt(3)/2`, the two scalar closure rows are

\[
C_x=(1,1,-1/2,-1,-1/2),
\]

\[
C_y=(0,0,a,0,-a).
\tag{HR.11}
\]

The hidden chord `ma=e_2+e_3` has unit direction `(1/2,a)`.  Its radial first variation
is

\[
\boxed{\dot d_{ma}=a(\omega_2-\omega_3).}
\tag{HR.12}
\]

Likewise `mb=-e_1-e_5` has unit direction `(-1/2,a)` and

\[
\boxed{\dot d_{mb}=a(\omega_5-\omega_1).}
\tag{HR.13}
\]

Thus the two hidden rows at equality are

\[
H_a=(0,a,-a,0,0),
\qquad
H_b=(-a,0,0,0,a).
\tag{HR.14}
\]

The `4 x 4` minor of `(C_x,C_y,H_a,H_b)` on columns `1,2,3,4` has determinant

\[
\boxed{a^3={3\sqrt3\over8}>0.}
\tag{HR.15}

Hence the four rows have rank four.  All four rows annihilate the all-ones rate vector:
face closure does so because the polygon closes, and a common angular rate is rigid
rotation, which changes no chord length to first order.  Therefore the local common
kernel is exactly

\[
\boxed{\operatorname{span}\{(1,1,1,1,1)\}.}
\tag{HR.16}

The row entries depend continuously on the five realized boundary vectors and the two
hidden chord directions.  Shrink the fixed flat-pentagon neighborhood once.  The same
minor remains nonzero on every retained actual pentagon.  Thus (HR.16) is a finite
statement throughout that neighborhood: if a contact flex satisfies the pentagon
closure equations and has zero first variation on both hidden leaf chords, all five
incident train rates are equal.

---

## 2. The pentagon/train incidence network

Audited stopped-train topology gives two facts for bounded exceptional faces:

1. a complete train cannot return nontrivially to the same bounded face, and a
   singleton bounded loop is also excluded;
2. two distinct complete trains cannot have the same pair of bounded stopping faces.

Consequently the five boundary sides of every pentagon in `P` belong to five distinct
complete trains, and after suppressing the train nodes that join two faces of `P`, the
internal face-to-face graph is simple.

Consider one connected component containing `s` pentagons.  Let `e` be the number of
trains joining two pentagons inside this component.  Every face contributes five train
terminal incidences.  An internal train uses two of them and every other incident train
uses one.  Hence the number `n` of distinct train variables occurring in the component
is exactly

\[
\boxed{n=5s-e.}
\tag{HR.17}

The local kernel statement (HR.16) says that annihilating both closure and hidden rows
on one pentagon makes its five incident train rates equal.  Connectivity propagates
that equality through every internal train.  Therefore the combined closure-plus-hidden
matrix on this component has one-dimensional kernel and rank

\[
\boxed{n-1=5s-e-1.}
\tag{HR.18}

Because the internal face graph is simple and every face has only five train
incidences,

\[
e\le\min\left\{{s\choose2},\left\lfloor{5s\over2}\right\rfloor\right\}.
\tag{HR.19}

For `1<=s<=5`, direct substitution gives respectively the lower bounds

\[
4,8,11,13,14
\]

for `n-1`, each at least `7s/3`.  For `s>=6`, (HR.19) gives

\[
n-1\ge {5s\over2}-1\ge {7s\over3}.
\]

Thus every component satisfies

\[
\boxed{n-1\ge {7s\over3}.}
\tag{HR.20}

Summing over components gives

\[
\boxed{
\operatorname{rank}
\begin{bmatrix}C_P\\H_P\end{bmatrix}
\ge {7p\over3}.
}
\tag{HR.21}

External trains ending on the outer face or on faces outside `P` are simply degree-one
train nodes of the restricted incidence network and are already counted in (HR.17).

---

## 3. Remove the ordinary contact-closure rank

For any two linear maps `C,H` with the same domain,

\[
\operatorname{rank}(H|_{\ker C})
=
\operatorname{rank}\begin{bmatrix}C\\H\end{bmatrix}
-\operatorname{rank}C.
\tag{HR.22}

Apply this with the full `C_face` and `H_P`.  Adding all non-`P` closure rows can only
increase the stacked rank, so by (HR.21),

\[
\operatorname{rank}(H_P|_{\ker C_{face}})
\ge {7p\over3}-\operatorname{rank}C_{face}.
\]

Use the exact closure-corank identity (HR.1) to obtain (HR.2).

Under the train-angle/contact-flex isomorphism,

\[
\ker R_C/\mathrm{Trans}\cong\ker C_{face},
\]

so the left side of (HR.2) is literally the rank of the two hidden radial derivatives
on contact-preserving infinitesimal source motions modulo translations.  Global
rotation lies in its kernel automatically.

---

## 4. Low-t numerical insertion

On `R_F=o(D)`, diagonalize the flatness threshold slowly enough that deleting
non-flat pentagons costs `o(D)`.  The low-`t` pentagon theorem gives (HR.3).

Every bounded exceptional face has degree at least five, so `f<=Q`.  With (HR.4),

\[
{2f\over D}\le4t-2\pi-2\delta.
\tag{HR.23}

Insert (HR.3) and (HR.23) into (HR.2), discard the nonnegative `sigma_C/D`, and obtain

\[
\begin{aligned}
{1\over D}\operatorname{rank}(H_P|_{\ker C_{face}})
&\ge {7\over3}
\left(\pi+C_0-{5t\over2}+\delta+{\kappa\over2}\right)
 -4t+2\pi+2\delta-o(1)\\
&=R_H(t)+{13\over3}\delta+{7\over6}\kappa-o(1).
\end{aligned}
\]

This proves (HR.5).  The endpoint and positivity constants in (HR.7)--(HR.8) are
checked outward by the companion Decimal regression.

---

## 5. Frontier effect

The small-residual low-`t` endpoint no longer merely contains many hidden near-contacts.
It contains a linear-rank block of them:

```text
~0.494 D flat pentagons
  -> two hidden leaf-chord rows per pentagon
  -> after every contact face-closure equation is imposed,
     at least 0.153 D independent hidden radial coordinates remain.
```

This rules out an explanation in which the entire hidden-contact sea is first-order
redundant with ordinary contact closure.  A closing theorem can now target the map from
these `Omega(D)` independent activation coordinates to the near-square actual diameter
locking system.  The remaining obstruction is genuinely the diameter inequalities,
not a deficiency of contact-flex rank.

No sign control on the hidden derivatives is asserted, no inverse-condition-number
bound is claimed, and no infinitesimal contact flex is claimed to be diameter-feasible.

---

## 6. Scope audit

- The hidden rows are derivatives of actual inactive source-pair distances; they are
  not assigned KKT multipliers.
- Same-face train returns and repeated bounded face pairs are excluded only by the
  existing audited-working train topology theorems.
- The component estimate uses a simple graph only after those exclusions.
- Near-flat local rank uses continuity of a nonzero explicit minor; no asymptotic row
  identification is substituted for a finite statement.
- The global rank subtraction uses the full `C_face`, including bridges,
  articulations, occurrence signs, and all nonpentagonal bounded faces.
- Contact-isolated source points remain in the full source and are not inserted into
  the core train-angle matrix.
- C-II and Level I remain open.

**Disposition:** proof-only activation-rank theorem; theorem-state authority unchanged.
