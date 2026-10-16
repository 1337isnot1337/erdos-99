# Erdős Problem #99 — Wegner quantization of the exceptional-face residual

**Date:** 2026-09-14  
**Target:** C-II, canonical full-core Type-II branch  
**Base:** all-degree Groemer face stability plus exact force-hull residual conservation  
**Claim class:** proof-only research consequence awaiting independent audit  
**External theorem:** G. Wegner's finite disk-packing inequality, as restated in K. J. Böröczky and I. Z. Ruzsa, *Note on an Inequality of Wegner*, Discrete Comput. Geom. 37 (2007), 245–249, DOI `10.1007/s00454-006-1277-4`

## LEVEL I STATUS

`STILL OPEN`

The all-degree Groemer compactness theorem says that small fixed-boundary Oler residual forces an exceptional face toward a finite Groemer packing. Wegner's stronger finite packing inequality gives an additional **discrete** restriction on that limit regime.

For a bounded exceptional contact face of degree `d` with `z` assigned interior contact-isolated source points, write

\[
N=d+z
\]

for the number of source points in the face including its boundary, and let

\[
r(P)={A(P)\over a_0}-{d\over2}+1-z,
\qquad a_0={\sqrt3\over2},
\tag{WQ.1}
\]

be the exact canonical fixed-boundary residual. The main finite conclusion is

\[
\boxed{
r(P)\ge \kappa\left(\left\lceil\sqrt{12N-3}-3\right\rceil-d\right),
\qquad
\kappa={1\over\sqrt3}-{1\over2}.
}
\tag{WQ.2}
\]

Together with `r(P)>=0`, this is an explicit quantization of the local residual.

## 1. Scaling Wegner's theorem to the source normalization

Böröczky–Ruzsa restate Wegner's theorem as follows. If `D` is the convex hull of `N` pairwise nonoverlapping unit disks, then

\[
A(D)
\ge
2\sqrt3(N-1)
+(2-\sqrt3)L_N
+\pi,
\tag{WQ.3}
\]

where

\[
L_N:=\left\lceil\sqrt{12N-3}-3\right\rceil.
\tag{WQ.4}
\]

Equality holds exactly for a Wegner packing.

Let `X` be any unit-separated `N`-point set with convex hull `C`. Scale its centers by two. The doubled centers are pairwise distance at least two, so unit disks centered there are nonoverlapping. Their convex hull is

\[
2C+B_2.
\]

Steiner's formula gives

\[
A(2C+B_2)=4A(C)+2P(C)+\pi.
\tag{WQ.5}
\]

Applying (WQ.3) and cancelling `pi`,

\[
4A(C)+2P(C)
\ge
2\sqrt3(N-1)+(2-\sqrt3)L_N.
\]

Equivalently,

\[
A(C)
\ge
a_0(N-1)+{2-\sqrt3\over4}L_N-{P(C)\over2}.
\tag{WQ.6}
\]

The ordinary Oler slack of `X` is

\[
r_X={A(C)\over a_0}+{P(C)\over2}+1-N.
\tag{WQ.7}
\]

Since

\[
{2-\sqrt3\over4a_0}
={1\over\sqrt3}-{1\over2}
=\kappa
\]

and

\[
{1\over2}-{1\over2a_0}=-\kappa,
\]

(WQ.6) yields the general finite inequality

\[
\boxed{
r_X\ge\kappa(L_N-P(C)).}
\tag{WQ.8}
\]

For a canonical bounded exceptional face every boundary edge is a unit contact, so `P(C)=d` and `r_X=r(P)`. This proves (WQ.2).

Numerically,

\[
\boxed{
\kappa=0.0773502691896257\ldots .
}
\tag{WQ.9}
\]

## 2. The first residual jump bounds interior population

Because `L_N-d` is an integer, (WQ.2) has an immediate discrete consequence:

\[
r(P)<\kappa
\quad\Longrightarrow\quad
L_N\le d.
\tag{WQ.10}
\]

The latter condition is equivalent to

\[
12N-3\le(d+3)^2.
\]

Hence

\[
\boxed{
N\le
\left\lfloor{(d+3)^2+3\over12}\right\rfloor,
}
\tag{WQ.11}
\]

or, in terms of assigned interior isolates,

\[
\boxed{
z\le z_{\max}(d):=
\left\lfloor{d^2-6d+12\over12}\right\rfloor.
}
\tag{WQ.12}
\]

Examples:

```text
d=5  -> z<=0,
d=6  -> z<=1,
d=7  -> z<=1,
d=8  -> z<=2,
d=22 -> z<=30,
d=42 -> z<=127.
```

Thus any pentagonal exceptional face with even one assigned interior isolate already pays at least `kappa` of true fixed-boundary residual.

More generally, if `r(P)<m*kappa` for a positive integer `m`, then `L_N-d<=m-1`, giving

\[
N\le
\left\lfloor{(d+m+2)^2+3\over12}\right\rfloor.
\tag{WQ.13}
\]

The first jump `m=1` is the useful one below.

## 3. Combine with the linear bounded-degree face population

The AG42/§171 bootstrap and `Q<=P_F` give

\[
\liminf {f_{\le42}\over D}
\ge
\ell_{42}
=0.086570985682155\ldots .
\tag{WQ.14}
\]

Let `R_F` be the exact force-hull residual

\[
R_F=\sum_j r_j,
\]

where the sum ranges over all inactive chambers and every term is nonnegative.

Assume the small-residual Type-II branch

\[
R_F=o(D).
\tag{WQ.15}
\]

Then the number of exceptional faces with `r(P)>=kappa` is at most

\[
{R_F\over\kappa}=o(D).
\tag{WQ.16}
\]

Consequently, among the degree-at-most-42 exceptional faces, at least

\[
(\ell_{42}-o(1))D
\]

satisfy simultaneously

\[
\boxed{
r(P)<\kappa,
\qquad
N=d+z\le169.
}
\tag{WQ.17}
\]

The number `169` is exact from (WQ.11) at `d=42`:

\[
\left\lfloor{45^2+3\over12}\right\rfloor=169.
\]

Thus Branch B is not merely a collection of bounded-degree faces. It is a linear family of chambers containing at most 169 source points each.

## 4. The same faces have zero fixed-boundary spare capacity

The contact-wall repacking theorem gives, for an exceptional face `P`,

\[
0\le M_\partial(P)-z\le r(P),
\tag{WQ.18}
\]

where `M_partial(P)` is the maximum number of interior points that can be packed unit-separated from each other and from the fixed cyclic boundary vertices.

For every face in (WQ.17),

\[
r(P)<\kappa<1.
\]

The left side of (WQ.18) is an integer. Therefore

\[
\boxed{M_\partial(P)=z.}
\tag{WQ.19}
\]

So almost all of the linear low-degree population in Branch B is **exactly locally cardinality-saturated**: there is no room for one extra point behind the fixed unit-contact wall.

This rules out the simplest diameter-cover exchange on those faces. The contact-wall theorem is protective, but there is no one-point spare capacity to exploit.

## 5. Combine with anchored Groemer stability

The hostile audit of the all-degree Groemer theorem proves that, for every fixed `eta>0`, all but `o(D)` of the same degree-at-most-42 faces contain an anchored almost-equilateral triple

\[
|u-v|=1,
\qquad
1\le|u-w|<1+\eta,
\qquad
1\le|v-w|<1+\eta,
\tag{WQ.20}
\]

with `uv` an existing cyclic boundary contact.

After a greedy face-conflict selection, a linear subfamily is pairwise vertex-disjoint. Diagonalization gives `eta_D->0` and at least

\[
0.000256127176574\ldots D-o(D)
\]

vertex-disjoint anchored almost-equilateral triples.

Combining this with (WQ.17)--(WQ.19), the small-residual branch has the following finite local normal form:

```text
Omega(D) pairwise-disjoint exceptional chambers,
    degree <= 42,
    at most 169 source points total,
    zero fixed-boundary spare capacity,
    one exact unit boundary edge uv,
    a third source point w with uw,vw = 1+o(1).
```

This is a substantially smaller local search space than the original Type-II branch.

## 6. What Wegner does not provide

Wegner's inequality does not give the quantitative geometric modulus needed to turn `1+o(1)` into `1+O(1/D)`, and local capacity saturation does not imply local rigidity. A same-cardinality fixed-boundary packing can have continuous degrees of freedom even when one additional point cannot be inserted.

Therefore no exact unit triangle or strict sub-`D` source follows yet.

The next Branch-B target is now finite-dimensional:

> classify or control near-Groemer, fixed-boundary-saturated unit-separated configurations with at most 169 points, and show that one cannot occur as an inactive defect chamber of a global diameter minimizer unless an anchored almost-equilateral triple activates exactly or a source-preserving diameter-decreasing exchange exists.

The large-residual branch `R_F=Omega(D)` is unchanged.

## 7. Scope audit

- Wegner is applied to the convex hull of the **disks** only after doubling the source centers; Steiner's formula is used explicitly to return to the center hull.
- The perimeter convention for a degenerate segment is irrelevant here because canonical exceptional faces have `d>=5` and positive area.
- `r(P)` is the existing canonical fixed-boundary residual, not raw chamber Oler slack.
- `M_partial` is the existing contact-wall capacity; (WQ.19) uses only integrality and its audited upper bound.
- All asymptotic constants inherit the proof-only status of AG42 and the §171 bootstrap.

**Disposition:** new proof-only quantitative reduction. C-II and Level I remain open.
