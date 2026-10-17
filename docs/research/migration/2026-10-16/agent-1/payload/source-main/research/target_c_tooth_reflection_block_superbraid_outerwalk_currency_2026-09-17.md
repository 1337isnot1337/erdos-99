# Target C-II — block-optimized superbraid forces 1.851079 sqrt(D) outer-walk currency

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; supersedes the weaker `0.679255...` superbraid outer-walk constant  
**Scope:** BLOCK-SQRT-SUPER-BRAID branch  
**Dependencies:** block-optimized FREE square-root fork; FREE superbraid forest transversal; full-hull perimeter accounting; DG.1 doubled diameter-direction-gap perimeter theorem  
**Certificate:** `research/verify_target_c_tooth_reflection_block_superbraid_outerwalk_currency_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The block-optimized FREE theorem raises the superdiameter-braid size from
`0.679255... sqrt(D)` to

\[
(c_{\rm blk}-o(1))\sqrt D,
\qquad
c_{\rm blk}=0.925539574680581\ldots .
\]

The full-hull and doubled-gap arguments of the preceding outer-walk note are linear in
the braid size. They therefore sharpen immediately.

Choose exactly

\[
\boxed{m_D=(c_{\rm blk}-o(1))\sqrt D}
\tag{BOW.1}

edges from the block-optimized superbraid. Every one of their `2m_D` endpoints is a
fully inactive exposed vertex of the full source hull `K`, while the `q` actual diameter
endpoints are disjoint exposed vertices of `K`. Unit separation of consecutive hull
vertices and Cauchy's perimeter-diameter inequality give the exact finite bound

\[
\boxed{q+2m_D\le\operatorname{per}(K)\le\pi D.}
\tag{BOW.2}

Hence

\[
\boxed{
\pi D-q
\ge
(2c_{\rm blk}-o(1))\sqrt D
=(1.851079149361162\ldots-o(1))\sqrt D.
}
\tag{BOW.3}

The superbraid forest-transversal theorem forces the complete actual diameter graph
`H` to be a caterpillar forest. If `H` is a star, the elementary force-hull perimeter
argument gives the stronger estimate

\[
\boxed{x_B\ge2D-2.}
\tag{BOW.4}

If `H` is not a star, DG.1 and `per(F)<=q+x_B` give

\[
x_B
\ge
2D\cos((q-2)a_D)-2
-2(d_H-1)(1-\cos a_D),
\qquad
a_D=\arcsin{1\over2D}.
\tag{BOW.5}

Since `d_H<=q<=pi D`, the final correction is `O(D^-1)`. Using (BOW.3), or directly
`q<=pi D-2m_D`, gives

\[
\begin{aligned}
2D\cos((q-2)a_D)
&\ge
2D\cos((\pi D-2m_D-2)a_D)\\
&=2m_D+o(\sqrt D).
\end{aligned}
\]

Therefore every nonstar BLOCK-SQRT-SUPER-BRAID satisfies

\[
\boxed{
x_B
\ge
(2c_{\rm blk}-o(1))\sqrt D
=(1.851079149361162\ldots-o(1))\sqrt D.
}
\tag{BOW.6}

Thus the complete superbraid branch, including the star alternative, is incompatible
with both

\[
\pi D-q=o(\sqrt D)
\]

and

\[
x_B=o(\sqrt D).
\]

The old exact pocket ledger `x_B=a+d_P` also gives the immediate structural
consequence

\[
\boxed{a+d_P\ge(1.851079149361162\ldots-o(1))\sqrt D,}
\tag{BOW.7}

where `a` is the number of convex outer pockets and `d_P=sum_P(k_P-3)` is total outer
pocket degree excess. In particular at least one of

\[
a\ge(0.925539574680581\ldots-o(1))\sqrt D
\]

or

\[
d_P\ge(0.925539574680581\ldots-o(1))\sqrt D
\]

must hold.

This does not close C-II. It does remove the sub-square-root near-maximal-terminal and
outer-walk endpoint from the superbraid branch. A remaining forest survivor must pay
square-root pocket complexity in addition to the complementary braid-cell localization
of every diameter-tree bipartition.

**Disposition:** propagated the upper-block improvement through full-hull perimeter,
DG.1, and the exact outer-pocket ledger. The sharp current superbraid currency is
`1.851079149361162... sqrt(D)` at both the terminal-deficit and outer-walk levels.
