# Target C — linear-density biclique extraction from ordered interval neighborhoods

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate; theorem authority unchanged.

Canonical Section 91 reaches a slab in which one shore of the train-crossing graph is a pairwise-disjoint spanning family and every neighborhood on the other shore is an interval in the common vertical order. Its Lemma 91.3 then extracts a balanced complete grid with shore coefficient quadratic in the edge-density parameter.

That combinatorial loss is unnecessary. An interval-neighborhood bipartite graph with `e` edges and shore sizes `a,b` contains a balanced biclique of order essentially `e/(a+b)`. Applied to the exact Section-91 slab, this replaces

\[
 c_{grid}={\varepsilon_0^2\over18C_0^3}
\]

by the much larger proof-only coefficient

\[
 c_{grid}^{\rm int}={\varepsilon_0\over2C_0}
\]

at leading order. The gain is structural rather than a carrier-decimal optimization: it uses the full consecutive-ones geometry already proved in Section 91.

The strengthened coefficient is still not, with the currently certified upstream constants, large enough by itself to force the Section-76 diameter contradiction. Thus this note removes a genuine avoidable loss but does not claim C-II closure.

---

## 1. Exact interval biclique theorem

Let `G=(A,B,E)` be a finite bipartite graph. Fix a linear order on `B`, and suppose that for every `x in A`, the neighborhood `N(x)` is an interval in that order. Put

\[
a=|A|,\qquad b=|B|,\qquad e=|E|.
\]

For an integer `k>=1`, call a consecutive `k`-set in the order on `B` a **`k`-block**.

### Theorem 1 — exact interval-block criterion

If

\[
\boxed{
 e+a\ge k(a+b-k+1),
}
\tag{1.1}
\]

then `G` contains a copy of `K_{k,k}` whose `B` shore is one consecutive `k`-block.

In particular, with

\[
\boxed{
 k_0=\left\lfloor{e\over a+b}\right\rfloor,
}
\tag{1.2}
\]

one always has a `K_{k_0,k_0}` whenever `k_0>=1`.

### Proof

Write `d_x=|N(x)|`. A row interval of length `d_x` contains exactly

\[
\max\{d_x-k+1,0\}
\]

consecutive `k`-blocks. Therefore the total number `I_k` of incidences

\[
(x,J),\qquad J\subseteq N(x),\quad J\text{ a consecutive }k\text{-block},
\]

satisfies

\[
\begin{aligned}
I_k
&=\sum_{x\in A}\max\{d_x-k+1,0\}\\
&\ge\sum_{x\in A}(d_x-k+1)\\
&=e-a(k-1).
\end{aligned}
\tag{1.3}
\]

There are exactly `b-k+1` consecutive `k`-blocks in `B`. If every such block were contained in the neighborhoods of at most `k-1` rows, then

\[
I_k\le(k-1)(b-k+1).
\tag{1.4}
\]

But (1.1) gives

\[
\begin{aligned}
e-a(k-1)
&\ge k(a+b-k+1)-a-a(k-1)\\
&=k(b-k+1).
\end{aligned}
\tag{1.5}
\]

Thus some `k`-block is contained in at least `k` row neighborhoods, proving `K_{k,k}`.

For (1.2), `e>=k_0(a+b)`. Hence

\[
e+a\ge k_0(a+b)+a\ge k_0(a+b-k_0+1),
\]

because `a+k_0(k_0-1)>=0`. The exact criterion applies. `square`

---

## 2. A sharper asymptotic coefficient

The exact criterion can be used directly rather than only through (1.2). Suppose along a sequence

\[
a,b\le CD,
\qquad
e\ge\varepsilon D^2,
\tag{2.1}
\]

with fixed `C>0` and `0<\varepsilon\le C^2`. If `c>0` satisfies

\[
\boxed{
 c(2C-c)<\varepsilon,
}
\tag{2.2}
\]

then for all sufficiently large `D`, Theorem 1 with `k=\lfloor cD\rfloor` gives a `K_{k,k}`. Hence every

\[
\boxed{
 c<C-\sqrt{C^2-\varepsilon}
}
\tag{2.3}
\]

is valid asymptotically.

The transparent weaker form obtained from (1.2) is

\[
\boxed{
 k\ge {\varepsilon\over2C}D-1.
}
\tag{2.4}
\]

For small `\varepsilon/C^2`, the sharp coefficient in (2.3) is

\[
C-\sqrt{C^2-\varepsilon}
={\varepsilon\over2C}+O\!\left({\varepsilon^2\over C^3}\right),
\]

so the leading dependence is linear in edge density. Section 91's current Lemma 91.3 instead loses another factor of order `\varepsilon/C^2`.

---

## 3. Application to the canonical Section-91 slab

Retain exactly the notation of canonical Section 91 after its endpoint-balanced slab extraction. It produces a slab `S`, a pairwise-disjoint spanning shore `B_S`, and the incident `A` trains such that

\[
E_S\ge\varepsilon_0D^2,
\tag{3.1}
\]

while each shore has at most `C_0D` trains. Lemma 91.2 proves that every `A`-neighborhood in the common vertical order of `B_S` is an interval.

Therefore Theorem 1 applies directly with

\[
a,b\le C_0D,
\qquad e=E_S.
\]

It gives complete train families `A_0,B_0` in the same harmonic cell with every cross-shore pair meeting in an actual strict rhombus and

\[
\boxed{
|A_0|,|B_0|
\ge {\varepsilon_0\over2C_0}D-1.
}
\tag{3.2}
\]

More sharply, for every fixed

\[
 c<C_0-\sqrt{C_0^2-\varepsilon_0},
\]

one has

\[
\boxed{|A_0|,|B_0|\ge cD}
\tag{3.3}
\]

for all sufficiently large `D`.

All the geometric conclusions of Section 91.6 are unchanged:

- the two shores have fixed distinct phase labels;
- every crossing has the same sign and the same common order;
- every crossing defect is `O(1/D)`;
- the grid lies in the same actual harmonic carrier; and
- canonical Section 76 gives
  \[
  d_*\ge {\sqrt3\over2}(|A_0|+|B_0|)-O(1).
  \]

Thus the complete-grid extraction loss at the final consecutive-ones step is now linear, not quadratic, in `\varepsilon_0`.

---

## 4. Hostile scope check

The proof uses only the consecutive-ones conclusion already established in canonical Section 91. It does **not** assume that the entire dense Section-90 graph is interval-convex; Section 91 proves interval neighborhoods only after selecting the spanning slab. No endpoint occurrence is identified or reused by this combinatorial replacement.

The theorem also does not improve the upstream losses from

1. the ordered phase threshold cut, or
2. the endpoint-balanced spanning-slab extraction.

Those losses are substantial. With the presently recorded Section-90/91 constants, replacing Lemma 91.3 by Theorem 1 does not make the guaranteed value of

\[
|A_0|+|B_0|
\]

large enough to exceed the Section-76 threshold `2D/sqrt(3)`. Therefore

\[
\boxed{\text{this theorem strengthens the full-core ordered-grid route but does not close C-II.}}
\]

No source point is moved, deleted, or reclassified. The macroscopic inactive-container branch is untouched. The theorem state remains `2026-09-12.audit.44`.
