# Erdos Problem #99 - low-t outer/pentagon stopped-train gate

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** phase-star all-train gap `g=0.0009`; audited Section 171 ledgers; low-t pentagon degree-excess bookkeeping; empty-pentagon stability; triangle-free contact-degree bound
**Claim class:** proof-only structural closing reduction awaiting independent audit
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The low-`t` endpoint has almost no bounded endpoint mass on exceptional faces of degree
at least six.  Consequently almost every outer-face stopped-train terminal must either
pair with another outer terminal or terminate on an actual pentagon.  Keeping the
occurrence ledger exact gives a large fork that was not isolated in the earlier
pentagon-sea theorem.

Put

\[
\Delta_2={\pi\over2\sqrt3},\qquad s:=\sqrt{\Delta_2},\qquad
 g:=0.0009,\qquad C_g:=2s+g.
\]

On a Type-II subsequence write

\[
t_D={q-k\over D},\qquad
\delta_D={b-P_F\over D},\qquad
\kappa_D={k\over D},\qquad
X:=Q-f.
\]

For an upper endpoint `t_0` define

\[
A_g(t_0):={9t_0\over4}-\pi-{C_g\over2}.
\tag{OP.1}
\]

The new all-train atomic theorem and the audited Section-171 elimination give, on
`limsup t_D<=t_0`,

\[
\boxed{
{X\over D}\le
A_g(t_0)-\delta_D-{\kappa_D\over4}+o(1).
}
\tag{OP.2}
\]

Let

- `L_OO` be the number of complete stopped trains with both terminal occurrences on
  the outer face;
- `L_O5` be the number with one outer terminal and one terminal on a pentagonal
  exceptional face;
- `L_O6` be the number with one outer terminal and one terminal on an exceptional face
  of degree at least six.

Then

\[
\boxed{
2L_{OO}+L_{O5}
\ge
\left(W_g(t_0)-o(1)\right)D,
}
\tag{OP.3}
\]

where

\[
\boxed{
W_g(t_0):=\pi-6A_g(t_0)
=7\pi+3C_g-{27t_0\over2}.
}
\tag{OP.4}
\]

In particular, whenever `W_g(t_0)>0`,

\[
\boxed{
\max\{L_{OO},L_{O5}\}
\ge \left({W_g(t_0)\over3}-o(1)\right)D.
}
\tag{OP.5}
\]

At the safe phase-star/Section-171 endpoint

\[
t_9={4\over9}(\pi+s)+0.0014759
=1.8209894379\ldots,
\]

one has

\[
A_g(t_9)=0.002870775
\]

and therefore

\[
\boxed{
\max\{L_{OO},L_{O5}\}
\ge(1.0414560011\ldots-o(1))D.
}
\tag{OP.6}
\]

This already forces more than one outer-ending train per unit diameter in one of two
geometrically distinct classes.

On the additional small true-residual branch `R_F=o(D)`, the pentagonal side of the
fork can be localized to actual near-equilateral leaf teeth.  Fix a sufficiently small
flat-pentagon residual threshold `theta>0`.  Let `J_leaf` be the maximum number of
pairwise vertex-disjoint two-contact leaf teeth from `theta`-good pentagons such that
at least one of the two exact unit sides belongs to an `O5` train.  Then

\[
\boxed{
2L_{OO}+52J_{leaf}+{5R_F\over\theta}
\ge\left(R_g(t_0)-o(1)\right)D,
}
\tag{OP.7}
\]

where

\[
\boxed{
R_g(t_0):=2\pi-2t_0-5A_g(t_0)
=7\pi+{5C_g\over2}-{53t_0\over4}.
}
\tag{OP.8}
\]

Consequently, on `R_F=o(D)` at `t_0=t_9`, either

\[
\boxed{L_{OO}\ge(1.0414560011\ldots-o(1))D}
\tag{OP.9}
\]

or

\[
\boxed{J_{leaf}\ge(0.01046039\ldots-o(1))D.}
\tag{OP.10}
\]

Every tooth in the second alternative consists of three actual source vertices, has
two exact unit contacts, has its hidden side `1+o(1)` after the standard slow residual
diagonalization, and has one exact side on a complete train running from the pentagon
to the outer face.

## 1. High-degree faces absorb at most `6X` outer terminals

Let `n_d` be the number of bounded exceptional faces of degree `d>=5`.  The exact
degree-excess identity is

\[
X=Q-f=\sum_{d\ge6}(d-5)n_d.
\tag{OP.11}
\]

For every `d>=6`,

\[
d\le6(d-5).
\]

Hence the total number `B_{>=6}` of stopped-train terminal occurrences on
nonpentagonal bounded exceptional faces satisfies

\[
B_{\ge6}=\sum_{d\ge6}dn_d\le6X.
\tag{OP.12}
\]

Every train counted by `L_O6` consumes one distinct such occurrence, so

\[
\boxed{L_{O6}\le6X.}
\tag{OP.13}
\]

## 2. Exact outer occurrence ledger

Every complete stopped train has exactly two terminal occurrences.  Counting only
outer-face occurrences gives the exact partition

\[
\boxed{b=2L_{OO}+L_{O5}+L_{O6}.}
\tag{OP.14}
\]

Together with (OP.13),

\[
2L_{OO}+L_{O5}\ge b-6X.
\tag{OP.15}
\]

Canonical Type II has

\[
{b\over D}=\pi+\delta_D+o(1).
\]

Insert (OP.2):

\[
{b-6X\over D}
\ge
\pi-6A_g(t_0)+7\delta_D+{3\over2}\kappa_D-o(1).
\tag{OP.16}
\]

Dropping the nonnegative bonuses proves (OP.3).  Since
`2a+b<=3 max{a,b}`, (OP.5) follows.

## 3. Flat leaf-side localization

Fix `theta>0` below the Wegner first jump and inside the empty-pentagon trapezoid
stability neighborhood.  Call a pentagon `theta`-good when its residual is below
`theta`.  Exact residual conservation shows that at most

\[
{R_F\over\theta}
\tag{OP.17}
\]

pentagons are not good.

For a good pentagon use the canonical cyclic labeling

\[
l,m,r,a,b.
\]

Its two leaf teeth are `(m,l,b)` and `(m,r,a)`.  Their four exact boundary sides are

\[
lm,\quad lb,\quad mr,\quad ra,
\]

and `ab` is the unique boundary side not contained in a leaf tooth.

Let `A_leaf` be the number of good pentagons having at least one leaf side whose
complete train is of type `O5`.  The high-residual pentagons absorb at most
`5R_F/theta` `O5` occurrences.  Among the remaining good pentagons, the one non-leaf
side `ab` contributes at most one occurrence per pentagon, while every further `O5`
occurrence must lie on a leaf side.  Therefore

\[
L_{O5}\le {5R_F\over\theta}+p_5+4A_{leaf}.
\tag{OP.18}
\]

Since `p_5<=f`, equations (OP.13), (OP.14), and (OP.18) give

\[
2L_{OO}+4A_{leaf}+{5R_F\over\theta}
\ge b-f-6X.
\tag{OP.19}
\]

Use `f=Q-X` to rewrite the right side as

\[
b-Q-5X.
\tag{OP.20}
\]

The exact low-`t` outer ledger is

\[
{Q\over D}=2t_D-\pi-\delta_D+o(1).
\tag{OP.21}
\]

Using `t_D<=t_0+o(1)` and (OP.2),

\[
{b-Q-5X\over D}
\ge
R_g(t_0)+7\delta_D+{5\over4}\kappa_D-o(1),
\tag{OP.22}
\]

which yields the source-level inequality before the conflict extraction.

## 4. Vertex-disjoint leaf-tooth extraction

Choose one qualifying leaf tooth from every pentagon counted by `A_leaf`.  There is at
most one chosen tooth per face.  A source vertex belongs to at most five bounded face
sectors in a triangle-free unit-contact graph.  Hence a chosen three-vertex tooth
conflicts with at most

\[
3(5-1)=12
\]

others.  A greedy independent set keeps at least `A_leaf/13` teeth.  By definition of
`J_leaf`,

\[
A_{leaf}\le13J_{leaf}.
\tag{OP.23}
\]

Insert this in (OP.19)--(OP.22) to obtain (OP.7).

## 5. The current-floor two-stage fork

At `t_0=t_9`, the exact arithmetic gives

\[
W_g(t_9)=3.1243680035\ldots,
\qquad
R_g(t_9)=2.6268525563\ldots .
\tag{OP.24}
\]

If (OP.9) fails, (OP.3) forces the pentagonal outer-train side.  More directly, combine
(OP.7) with `L_OO<W_g(t_9)D/3+o(D)` and `R_F=o(D)`:

\[
52J_{leaf}
\ge
\left(R_g(t_9)-{2W_g(t_9)\over3}-o(1)\right)D.
\tag{OP.25}
\]

The bracket is positive.  Dividing by 52 gives (OP.10).

## 6. Frontier effect and scope

The hard low-`t`, small-residual branch is now forced into one of two global source
objects:

```text
>1.04145 D outer-to-outer train cuts,
all individually two-sidedly braced by actual diameter edges;

or

>0.01046 D vertex-disjoint near-equilateral leaf teeth,
each with one exact unit side carried by a train from the pentagon to the outer face.
```

The first branch is ready for a multi-train cut-order versus Woodall-thrackle theorem.
The second branch supplies the missing localization between the pentagon metric defect
and the outer train system; unlike a generic near-contact matching, every tooth is
attached to an actual outer-ending complete train.

This theorem does not assert that an outer-to-pentagon train is a bridge or that it
admits the outer-to-outer shear from audited Section 157.  It assigns no KKT multiplier
to the hidden tooth side.  No exact unit triangle or same-cardinality strict sub-`D`
competitor is produced.

C-II and Level I remain open.
