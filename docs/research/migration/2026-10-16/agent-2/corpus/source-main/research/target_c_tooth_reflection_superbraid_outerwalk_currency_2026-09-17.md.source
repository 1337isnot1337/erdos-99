# Target C-II — an optimized FREE superbraid forces square-root outer-walk excess

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; forest-side continuation of the optimized FREE square-root fork  
**Scope:** OPT-SQRT-SUPER-BRAID branch  
**Dependencies:** optimized FREE square-root tradeoff; FREE superbraid forest transversal; DG.1 doubled diameter-direction-gap perimeter theorem; standard Cauchy perimeter formula  
**Certificate:** `research/verify_target_c_tooth_reflection_superbraid_outerwalk_currency_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The optimized superbraid does more than force the actual diameter graph into the
caterpillar-forest topology.  Its inactive endpoints are additional exposed vertices of
the full source hull.  Full-hull perimeter then forces a square-root deficit in the
number `q` of actual diameter endpoints.  The existing doubled-gap perimeter theorem
converts exactly that near-`pi D` terminal deficit into square-root outer-walk excess.

Let

\[
c_{\rm opt}
=\left(2+{1\over2}{\sqrt{303}\over52}\right)^{-1/2}
=0.679255355387642\ldots .
\]

In OPT-SQRT-SUPER-BRAID choose a sub-braid of size

\[
\boxed{
 m_D=(c_{\rm opt}-o(1))\sqrt D.
}
\tag{OW.1}

Then, writing `K=conv(A)` for the full source hull and `q=|B|` for the complete actual
diameter endpoint set,

\[
\boxed{
 q+2m_D\le \operatorname{per}(K)\le\pi D.
}
\tag{OW.2}

Consequently

\[
\boxed{
 \pi D-q
 \ge(2c_{\rm opt}-o(1))\sqrt D
 =(1.358510710775284\ldots-o(1))\sqrt D.
}
\tag{OW.3}

The superbraid forest-transversal theorem already gives that the complete actual
diameter graph `H` is a caterpillar forest.  If `H` is a star, then in fact

\[
\boxed{x_B\ge2D-2.}
\tag{OW.4}

If `H` is not a star, the DG.1 direction-gap perimeter inequality and the elementary
outer-walk bound `per(F)<=b=q+x_B` give

\[
\boxed{
 x_B
 \ge
 2D\cos((q-2)a_D)
 -2
 -2(d_H-1)(1-\cos a_D),
 \qquad
 a_D:=\arcsin{1\over2D},
}
\tag{OW.5}

where `d_H=q-h` is the number of tree components.  Combining (OW.3) with (OW.5)
yields

\[
\boxed{
 x_B
 \ge
 (2c_{\rm opt}-o(1))\sqrt D
 =(1.358510710775284\ldots-o(1))\sqrt D.
}
\tag{OW.6}

Thus the optimized superbraid branch cannot coexist with `x_B=o(sqrt(D))`.  This is a
direct bridge from the inactive reflection obstruction into the old force-visible
outer-walk currency.  It applies before using any exceptional-face allocation.

---

## 1. Every actual diameter endpoint is an exposed full-hull vertex

Let `xy` be an actual diameter edge, `|x-y|=D`, and put

\[
u={x-y\over D}.
\]

For every source point `z`,

\[
u\cdot(z-y)\le|z-y|\le D=u\cdot(x-y).
\]

If equality holds, equality in Cauchy and the diameter bound force

\[
z-y=Du=x-y,
\]

so `z=x`.  Hence `x` is the unique maximizer of the linear functional `u dot z` on
`A`, and therefore an exposed vertex of `K=conv(A)`.  The same holds for `y`.

Thus every point of the complete diameter endpoint set `B` is a full source-hull
vertex.

The sharp superdiameter theorem used in the FREE braid construction separately proves
that every inactive braid endpoint is also a full source-hull vertex.  Those endpoints
are fully diameter-inactive, so they are disjoint from `B`.

Therefore a braid matching of size `m` contributes `2m` full-hull vertices in addition
to the `q` vertices of `B`:

\[
|\operatorname{Vert}(K)|\ge q+2m.
\tag{OW.7}

---

## 2. Full-hull perimeter charges every extra extreme point

Consecutive vertices of `K` are distinct source points and hence are at distance at
least one.  Therefore

\[
\operatorname{per}(K)\ge|\operatorname{Vert}(K)|\ge q+2m.
\tag{OW.8}

For completeness, Cauchy's perimeter formula gives

\[
\operatorname{per}(K)
=\int_0^\pi w_K(\theta)\,d\theta.
\]

Every width is at most the diameter `D`, so

\[
\operatorname{per}(K)\le\pi D.
\tag{OW.9}

Equations (OW.8)--(OW.9) prove the exact finite inequality

\[
\boxed{q+2m\le\pi D.}
\tag{OW.10}

Taking the selected sub-braid (OW.1) proves (OW.3).

This terminal deficit is not an external-population count with multiplicity.  It comes
from `2m` distinct exposed full-hull source vertices, all outside the force hull `F`.

---

## 3. The star forest already pays linear outer-walk excess

Suppose first that the diameter forest `H` is a star, with center `c` and `q-1` leaves.
All `q` diameter endpoints are vertices of the force hull `F=conv(B)`.  The two hull
edges incident with `c` join it to two leaves and therefore have length exactly `D`.
Every other hull edge joins two distinct source points and has length at least one.
Consequently

\[
\operatorname{per}(F)\ge2D+(q-2).
\tag{OW.11}

The old outer contact walk has length `b=q+x_B` and convex hull `F`, hence

\[
q+x_B=b\ge\operatorname{per}(F).
\]

Thus

\[
\boxed{x_B\ge2D-2.}
\]

So the star subcase is much stronger than the square-root target and needs no DG input.

---

## 4. A nonstar diameter forest converts terminal deficit into outer-walk excess

Assume now that `H` is not a star.  Let

\[
d_H=q-h>0
\]

be its number of tree components.  DG.1 is a geometric theorem for the complete actual
diameter graph: at least `d_H` consecutive projective diameter-direction gaps come from
vertex-disjoint diameter edges and therefore have doubled minimum angular size.  It
proves

\[
\operatorname{per}(F)
\ge
h-d_H+2(d_H-1)\cos a_D
+2D\cos((q-2)a_D),
\tag{OW.12}

with

\[
a_D=\arcsin{1\over2D}.
\]

Because a forest has `h=q-d_H`, subtracting `q` from (OW.12) gives

\[
\operatorname{per}(F)-q
\ge
2D\cos((q-2)a_D)
-2-2(d_H-1)(1-\cos a_D).
\tag{OW.13}

The inequality `per(F)<=b=q+x_B` is purely geometric and does not use the exact
circuit identity.  Therefore (OW.13) proves (OW.5) directly for this superbraid forest.

The correction term is negligible at square-root scale.  Since `d_H<=q<=pi D`,

\[
2(d_H-1)(1-\cos a_D)=O(D^{-1}).
\tag{OW.14}

---

## 5. Near-`pi D` expansion at the forced terminal deficit

Write

\[
\Delta_D:=\pi D-q.
\]

By (OW.3),

\[
\Delta_D\ge2m_D=(2c_{\rm opt}-o(1))\sqrt D.
\tag{OW.15}

Because cosine is decreasing on the relevant interval and `q<=pi D-2m_D`,

\[
\cos((q-2)a_D)
\ge
\cos((\pi D-2m_D-2)a_D).
\tag{OW.16}

Now

\[
a_D={1\over2D}+O(D^{-3}),
\]

and `m_D=Theta(sqrt(D))`, so

\[
\begin{aligned}
{\pi\over2}-(\pi D-2m_D-2)a_D
&={m_D+1\over D}+O(D^{-2})\\
&={c_{\rm opt}+o(1)\over\sqrt D}.
\end{aligned}
\tag{OW.17}

Hence

\[
\begin{aligned}
2D\cos((\pi D-2m_D-2)a_D)
&=2D\sin\left({m_D+1\over D}+O(D^{-2})\right)\\
&=2m_D+o(\sqrt D).
\end{aligned}
\tag{OW.18}

Insert (OW.14) and (OW.18) into (OW.5).  This gives

\[
x_B\ge2m_D-o(\sqrt D)
=(2c_{\rm opt}-o(1))\sqrt D,
\]

which is (OW.6).

---

## 6. Resulting FREE fork

The all-inactive non-anchored FREE branch now has the following stronger topology-aware
normal form:

```text
OPT-SQRT-FACE
    one original outer-face lower run
    support span >= (0.679255...-o(1)) sqrt(D)
    + parameterized sqrt(D) near-unit inactive matching

or

OPT-SQRT-SUPER-BRAID
    >= (0.679255...-o(1)) sqrt(D) crossing inactive superdiameters
    + H is a caterpillar forest
    + pi D - q >= (1.358510...-o(1)) sqrt(D)
    + x_B >= (1.358510...-o(1)) sqrt(D)
    + every diameter component remains trapped in complementary braid cells.
```

The superbraid is therefore no longer compatible with the previously live
near-maximal-terminal endpoint `q=pi D-o(sqrt(D))`, nor with sub-square-root outer-walk
excess.

This still does not close C-II.  The forest branch can pay `Theta(sqrt(D))` outer-walk
excess without violating any currently promoted first-order inequality.  The next
useful step is to combine this forced square-root outer-walk currency with the
complementary-cell localization or with a second-order pocket/annular capacity estimate.

**Disposition:** converted the optimized inactive superbraid into an exact full-hull
terminal deficit and, through DG.1, a matching square-root lower bound on old outer-walk
excess.  The star forest is handled separately with the stronger bound `x_B>=2D-2`.
