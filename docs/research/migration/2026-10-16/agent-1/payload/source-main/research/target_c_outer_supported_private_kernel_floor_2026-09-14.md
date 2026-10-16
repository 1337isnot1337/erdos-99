# Erdos Problem #99 - universal outer-supported private-kernel floor

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** audited complete stopped-train endpoint ledger; audited train-angle face-closure coordinates; canonical outer/exceptional identity
**Claim class:** proof-only finite structural refinement; theorem-state authority unchanged
**External literature:** none

## LEVEL I STATUS

`STILL OPEN`

The actual outer face alone forces a large, support-localized subspace of contact
flexes. No small-residual hypothesis and no flat-pentagon stability theorem are
needed.

Let

- `L_OO` be the number of complete stopped trains whose two terminal occurrences are
  on the actual outer face;
- `L_OB` be the number with one actual-outer terminal and one bounded
  nonquadrilateral-face terminal;
- `f` be the number of bounded nonquadrilateral contact faces; and
- for each such face `F`, let `r_F` be the number of outer-to-bounded complete trains
  terminating at `F`.

Then the train-angle closure matrix has an outer-supported kernel subspace `W_out`
with

\[
\boxed{
\dim W_{out}
\ge L_{OO}+\sum_F(r_F-2)_+.
}
\tag{OK.1}
\]

The actual-outer occurrence ledger is exact:

\[
\boxed{b=2L_{OO}+L_{OB},\qquad \sum_F r_F=L_{OB}.}
\tag{OK.2}
\]

Consequently

\[
\boxed{
\dim W_{out}\ge {b\over2}-f.
}
\tag{OK.3}
\]

After quotienting the one-dimensional global rotation, the corresponding genuinely
non-Euclidean contact-flex subspace has dimension

\[
\boxed{
 d_{out}^{loc}\ge {b\over2}-f-1.
}
\tag{OK.4}
\]

Using only `f<=Q` and the exact canonical endpoint identity

\[
b+Q=2(q-k),
\tag{OK.5}
\]

we obtain the completely finite weaker form

\[
\boxed{
 d_{out}^{loc}
\ge {3b\over2}-2(q-k)-1.
}
\tag{OK.6}
\]

Thus on any Type-II subsequence on which

\[
t={q-k\over D}\to t,
\qquad
\delta={b-P_F\over D}\to\delta,
\qquad {P_F\over D}\to\pi,
\]

we have

\[
\boxed{
\liminf {d_{out}^{loc}\over D}
\ge {3\pi\over2}-2t+{3\delta\over2}.
}
\tag{OK.7}
\]

At the current proof-only low-`t` endpoint

\[
t_0={4\over9}\left(\pi+\sqrt{\pi/(2\sqrt3)}\right)+0.0017279
=1.8212414379\ldots,
\]

and with the conservative choice `delta=0`,

\[
\boxed{
\liminf {d_{out}^{loc}\over D}
>1.06990.
}
\tag{OK.8}
\]

More robustly, throughout the entire working low-`t` band `t<=1.8585`,

\[
\boxed{
\liminf {d_{out}^{loc}\over D}
>0.99538
}
\tag{OK.9}
\]

before using any positive outer-detour bonus. The zero-bonus coefficient stays
positive all the way to

\[
t<{3\pi\over4}=2.35619\ldots .
\tag{OK.10}
\]

This is not a stronger lower bound on the total contact-flex dimension, which is
already large from the global closure-rank ledger. Its content is localization: a
linear-dimensional subspace can be chosen using only train coordinates that touch the
actual outer face.

---

## 1. Outer-to-outer train columns are identically zero

The audited face-closure matrix

\[
C_{face}:\mathbb R^T\to\mathbb R^{2f}
\]

has one train-angle column for every complete stopped train and two scalar closure rows
for every bounded nonquadrilateral face. Strict rhombi impose no additional rows
because angular rate is constant along a complete train.

An outer-to-outer train has no bounded nonquadrilateral terminal occurrence. A stopped
train can meet a nonrhombic face only at a terminal occurrence. Therefore its column
in `C_face` is identically zero.

Every outer-to-outer coordinate vector is consequently in `ker C_face`, and the
`L_OO` such coordinate vectors are independent.

---

## 2. Every bounded landing face contributes all private-column nullity

Fix a bounded nonquadrilateral face `F`. Suppose `r=r_F` complete trains have one
terminal occurrence on `F` and their other terminal occurrence on the actual outer
face.

Each of these `r` train columns is private to `F`: it occurs in no other bounded-face
closure row. Restrict `C_face` to these columns. Its only possibly nonzero block is a
real `2 x r` matrix

\[
B_F=(\pm Jr_1\ \cdots\ \pm Jr_r).
\tag{OK.11}
\]

Hence

\[
\dim\ker B_F\ge(r-2)_+.
\tag{OK.12}
\]

Extending a local kernel vector by zero on all other train coordinates gives a vector
in the global `ker C_face`.

Outer-to-bounded train sets belonging to distinct bounded faces are disjoint: such a
train has only one bounded terminal occurrence. They are also disjoint from the
outer-to-outer trains. Thus all local kernels and all outer-to-outer coordinate spaces
form a direct sum. This proves (OK.1).

Nothing in this argument uses the degree, metric residual, or near-trapezoid geometry
of `F`. This is why all bounded exceptional faces can be retained instead of paying
nonpentagons and metrically bad pentagons as losses.

---

## 3. Optimize the exact outer occurrence budget

The outer-face occurrence ledger counts two occurrences from each outer-to-outer train
and one from each outer-to-bounded train:

\[
b=2L_{OO}+L_{OB}.
\]

Also

\[
\sum_F r_F=L_{OB}.
\]

For nonnegative numbers `r_F`,

\[
\sum_F(r_F-2)_+
\ge (L_{OB}-2f)_+.
\tag{OK.13}
\]

Therefore (OK.1) gives

\[
\dim W_{out}
\ge L_{OO}+(L_{OB}-2f)_+.
\tag{OK.14}
\]

For `x=L_OO` and `y=L_OB`,

\[
x+(y-2f)_+\ge x+{y\over2}-f={b\over2}-f.
\tag{OK.15}
\]

Indeed, if `y<=2f`, then the left side is `x` and
`x-(x+y/2-f)=f-y/2>=0`; if `y>=2f`, the difference is `y/2-f>=0`.
This proves (OK.3).

The all-ones train-angle vector represents global infinitesimal rotation. Passing from
`W_out subset ker C_face` to the contact-flex quotient modulo Euclidean motions can
remove at most one dimension, proving (OK.4). No support-gap argument is needed.

---

## 4. Eliminate face count using the endpoint identity

Every bounded nonquadrilateral face has degree at least five, so its contribution to

\[
Q=\sum_F(\deg F-4)
\]

is at least one. Hence

\[
f\le Q.
\tag{OK.16}
\]

The canonical outer/exceptional identity is

\[
b+Q=2(q-k).
\]

Substitute (OK.16) into (OK.4):

\[
\begin{aligned}
d_{out}^{loc}
&\ge {b\over2}-Q-1\\
&={b\over2}-\bigl(2(q-k)-b\bigr)-1\\
&={3b\over2}-2(q-k)-1.
\end{aligned}
\]

This proves (OK.6).

On a Type-II subsequence, `P_F/D->pi` and by definition

\[
{b\over D}={P_F\over D}+{b-P_F\over D}\to\pi+\delta.
\]

Divide (OK.6) by `D` to obtain (OK.7).

---

## 5. Relation to the previous outer-flat extraction

The previous outer-flat theorem used only metrically good pentagons and retained one
local kernel direction from each face with at least three outer-to-flat train columns.
It therefore produced a floor proportional to an `N_3` face count.

The first version of the present note improved that to all `r-2` private dimensions on
one good pentagon and kept the weighted `2L_OO+L_OF` gate. That gave a localized floor
above `0.56D` at the then-current endpoint.

Equation (OK.3) supersedes both steps. The good-face restriction is unnecessary for
closure support, and the exact outer occurrence identity already contains every
outer-to-bounded train. The resulting current-endpoint coefficient exceeds `1.0699`.

A concurrent weighted-good-pentagon calculation gives about `1.06139D`; (OK.3) is
strictly stronger and removes its `R_F=o(D)` hypothesis.

---

## 6. Frontier effect

The low-`t` C-II survivor now carries an almost-one-dimensional-per-diameter-scale
family of **outer-supported** non-Euclidean contact flexes:

```text
all free outer-to-outer train shears,
plus
all private closure-kernel modes from outer-to-bounded terminal columns.
```

Canonical mixed rigidity makes the active-diameter derivative map injective on this
localized quotient subspace. Relative-interior KKT stationarity also implies that every
nonzero localized flex has active-diameter first variations of both signs.

The remaining obstruction is sharply support-sensitive. A closing theorem can focus
only on the action of the near-extremal planar diameter graph on outer-supported train
modes. In particular, any rank-capacity theorem showing that fewer than

\[
\left({3\pi\over2}-2t+{3\delta\over2}\right)D-o(D)
\]

independent diameter rows can act on these modes would close the corresponding Type-II
subsequence.

No such locking-capacity theorem is proved here. No exact hidden contact, unit
triangle, or same-cardinality strict sub-`D` competitor is claimed.

---

## 7. Scope audit

- The finite inequalities (OK.1)--(OK.6) use no asymptotics, residual estimate, atomic
  direction theorem, or pentagon stability theorem.
- The only geometric input is the audited stopped-train decomposition and the audited
  train-angle closure parametrization.
- Outer-to-bounded columns are private because a complete stopped train terminates at
  its first nonrhombic face and has exactly one bounded terminal in this class.
- Singleton trains are included automatically.
- Repeated outer-face vertices and articulation points cause no ambiguity because `b`
  is occurrence-counted.
- The `-1` in (OK.4) safely quotients global rotation.
- Contact-isolated source points remain in the full source and do not enter the
  positive-contact closure matrix.
- The numerical endpoint uses the current hostile-audited `g=0.0021` Section-171 floor
  only to instantiate `t`; it is not needed for the finite theorem.
- C-II and Level I remain open.
