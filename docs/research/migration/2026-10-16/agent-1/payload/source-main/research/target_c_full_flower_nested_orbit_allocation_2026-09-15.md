# Target C-II — four near-orbit sides force the fifth: a two-complement allocation law for full flowers

**Date:** 2026-09-15\
**Status:** proof-only exact finite geometric allocation theorem\
**Scope:** any strict convex unit pentagonal contact face; downstream use with the dominant exact `pi/3` train orbit\
**Dependencies:** only polygon closure and elementary triangular-lattice arithmetic for the local theorem\
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Fix one exact triangular projective orbit

\[
\mathcal O=\{[u_0],[u_1],[u_2]\},
\qquad
u_j=e^{i(\phi+j\pi/3)},
\]

with its six oriented unit rays

\[
\widetilde{\mathcal O}=\{\pm u_0,\pm u_1,\pm u_2\}.
\]

For projective radius `rho`, let `W_rho` be the union of the three closed projective
`rho`-neighborhoods of `mathcal O`.  Put

\[
\eta(\rho):=2\arcsin(2\rho).
\]

For every

\[
0<\rho<{1\over10},
\tag{NA.1}
\]

we prove the finite implication

\[
\boxed{
\text{four sides in }W_\rho
\quad\Longrightarrow\quad
\text{all five sides in }W_{\eta(\rho)}.
}
\tag{NA.2}

Since `eta(rho)->0`, this has a useful atomic consequence: in the exact orbit limit a
unit pentagon cannot have exactly four dominant-orbit side incidences.  Its dominant
side count may be `0,1,2,3,5`, but not `4`.

For a collection of fully rhombic pentagons, let

- `M` be the number of flowers;
- `C_rho` be the number of their train-terminal occurrences whose projective
  directions lie outside `W_rho`;
- `P_eta` be the number of flowers all five of whose side-train directions lie in
  `W_eta(rho)`.

The contrapositive of (NA.2) gives the exact allocation inequality

\[
\boxed{
M-P_\eta\le {C_\rho\over2},
\qquad
P_\eta\ge M-{C_\rho\over2}.
}
\tag{NA.3}

Thus every full flower that fails to become an all-dominant flower in the slightly
larger window spends **at least two** complement terminal occurrences in the smaller
window.

Because one complete stopped train has only two terminal occurrences, if `N_c(rho)`
is the number of distinct trains with at least one selected flower terminal outside
`W_rho`, then

\[
\boxed{N_c(\rho)\ge {C_\rho\over2}.}
\tag{NA.4}

Combining (NA.3)--(NA.4) gives the clean finite dichotomy

\[
\boxed{
P_\eta\ge {M\over2}
\quad\text{or}\quad
N_c(\rho)>{M\over2}.
}
\tag{NA.5}

At the current `t<=1.8623` full-flower floor `M>0.1327D-o(D)`, for every sufficiently
small fixed inner window this means, up to the usual window-boundary `o(D)` term,

```text
either >0.06635 D full flowers are all in the enlarged dominant orbit window,
or     >0.06635 D distinct complement trains terminate on full flowers.
```

The first side is exactly the population needed by dominant-pentagon through-splicing;
the second side is a new bounded-terminal complement population, disjoint from
complement outer-to-outer trains.  The theorem therefore supplies a rigorous bridge
between the general full-flower normal form and the existing dominant/complement train
allocation program.

---

## 1. Replace four near-orbit sides by exact lattice rays

Let a unit pentagon have oriented boundary vectors

\[
e_1+e_2+e_3+e_4+e_5=0,
\qquad |e_i|=1.
\tag{NA.6}
\]

Assume the projective directions of `e_1,...,e_4` lie in `W_rho`.  For each `i<=4`,
choose the oriented ray

\[
v_i\in\widetilde{\mathcal O}
\]

with the same sign lift as `e_i` and angular distance at most `rho`.  Unit-vector chord
length is at most angular distance, so

\[
|e_i-v_i|\le\rho.
\tag{NA.7}
\]

Put

\[
s:=v_1+v_2+v_3+v_4.
\]

By closure,

\[
e_5+s
=\sum_{i=1}^4(v_i-e_i),
\]

hence

\[
\boxed{|e_5+s|\le4\rho.}
\tag{NA.8}
\]

In particular

\[
\bigl||s|-1\bigr|\le4\rho.
\tag{NA.9}
\]

---

## 2. Triangular-lattice norm discreteness forces `|s|=1`

After one rigid rotation, write the triangular lattice basis as

\[
a=(1,0),
\qquad b=(1/2,\sqrt3/2).
\]

Every ray in `widetilde O` is a triangular-lattice unit vector, so

\[
s=ma+nb
\]

for integers `m,n`.  Therefore

\[
|s|^2=m^2+mn+n^2.
\tag{NA.10}
\]

The quadratic form `m^2+mn+n^2` takes only values congruent to `0` or `1` modulo `3`.
Thus

\[
|s|^2\in\{0,1,3,4,7,9,\ldots\}.
\tag{NA.11}
\]

In particular, if `|s|!=1` then either `|s|=0` or

\[
|s|\ge\sqrt3.
\]

But `rho<1/10` gives

\[
4\rho<0.4<\sqrt3-1
\]

and also `4rho<1`.  This contradicts (NA.9) in both nonunit cases.  Hence

\[
\boxed{|s|=1.}
\tag{NA.12}
\]

The integer solutions of `m^2+mn+n^2=1` are exactly the six triangular-lattice unit
rays, so

\[
-s\in\widetilde{\mathcal O}.
\tag{NA.13}
\]

---

## 3. The fifth side lies in the enlarged orbit window

Equation (NA.8), (NA.12), and `|e_5|=1` say that two unit vectors `e_5` and `-s` have
chord distance at most `4rho`.  If `theta` is their acute angular distance, then

\[
2\sin(\theta/2)\le4\rho.
\]

Since `rho<1/10`, `2rho<1`, and therefore

\[
\theta\le2\arcsin(2\rho)=\eta(\rho).
\tag{NA.14}
\]

Thus the projective direction of `e_5` lies in `W_eta(rho)`.  The original four sides
lie in `W_rho subset W_eta(rho)` because `eta(rho)>rho`.  This proves (NA.2).

No convexity or unit-separation diagonal estimate is needed in this local lemma; unit
side lengths and vector closure suffice.

---

## 4. Two-complement cost for a non-all-dominant flower

Take one fully rhombic pentagon `F` which is not counted by `P_eta`.  At least one of
its five side directions lies outside `W_eta(rho)`.  By the contrapositive of (NA.2),
it cannot have four side directions in `W_rho`.  Hence at most three lie in `W_rho`
and at least two lie outside `W_rho`.

Summing this two-occurrence cost over the `M-P_eta` non-all-dominant flowers gives

\[
C_\rho\ge2(M-P_\eta),
\]

which is (NA.3).

Every such side is a terminal occurrence of a non-singleton strict-rhombus train,
because the flower is fully rhombic.  One complete train has two terminal occurrences,
so `N_c(rho)>=C_rho/2`, proving (NA.4).

If `P_eta<M/2`, then (NA.3) gives `C_rho>M`, hence (NA.4) gives
`N_c(rho)>M/2`.  This proves (NA.5).

---

## 5. Atomic-limit formulation

The atomic statement does not require synchronizing a prescribed shrinking-window
rate with convergence of the polygon.  Take any convergent sequence of unit pentagons
for which four oriented side vectors converge, after passing to a subsequence, to
four rays

\[
v_1,\ldots,v_4\in\widetilde{\mathcal O}.
\]

The fifth unit side also has a convergent subsequence, say `e_5 -> w` with `|w|=1`.
Passing to the limit in polygon closure gives

\[
w+v_1+v_2+v_3+v_4=0.
\]

Thus the triangular-lattice vector `s=v_1+...+v_4` has `|s|=|w|=1`.  By the exact
norm-discreteness argument of Section 2, `-s` is one of the six rays in
`widetilde O`.  Hence `w in widetilde O` and the fifth projective side direction also
lies in `mathcal O`.

Equivalently:

\[
\boxed{
\text{an atomic pentagon has dominant-orbit multiplicity }4
\text{ only if it actually has multiplicity }5.
}
\tag{NA.15}
\]

For finite nested windows, use (NA.2) with a fixed inner `rho`, take the source limit,
and only then send `rho->0`; this is the standard order of limits in the train-measure
arguments and requires no rate assumption.

When all five sides converge to the orbit, the existing dominant-pentagon
classification sharpens the multiplicities to `3,1,1` across the three projective
phases and supplies the through-splice.

---

## 6. Why this is stronger than the trivial endpoint count

Without (NA.2), a non-all-dominant flower pays only one complement terminal occurrence,
so one only gets

\[
P_{all}\ge M-C.
\]

The lattice-norm argument doubles that payment in a window-stable way:

\[
P_\eta\ge M-C_\rho/2.
\]

This matters because the live full-flower branch is linear while the through-splicing
penalty is quadratic in the all-dominant flower population.  It also means any attempt
to evade splicing by inserting complement directions must spend complement train
terminal capacity twice per evading flower.

The current complement complete-train ceiling is still too loose for (NA.3) alone to
close C-II at `t≈1.86177`; that numerical check has been made and should not be hidden.
The new theorem instead supplies the correct allocation interface for the next joint
optimization: combine

1. the two-complement bounded-terminal cost here;
2. the existing complement O--O outer-terminal population; and
3. the quadratic dominant through-splicing deficit when `P_eta` is large.

**Disposition:** proved proof-only finite four-implies-five / two-complement full-flower
allocation theorem.  C-II and Level I remain open.
