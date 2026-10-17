> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_universal_sqrt_face_2026-09-17.md) · source SHA-256 `f71c54f96528743feed39ed8195f4b223af72602a4cdb2144641806dcb970d52`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a813a37de5ebbf7e80080d812fbe132b7552c0f8", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_universal_sqrt_face_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "ffeed72a5726ba525e8163559fb9ae0f6909e338b369d9518343a5f7f9f55084"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every non-anchored FREE ancestry has a sharp square-root outer-face run

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; strengthens the first universal square-root FREE-face theorem  
**Scope:** all-inactive non-anchored FREE reflection modules  
**Dependencies:** two-sided inactive gate absorption; two-sided outer-face localization; exact upper-event identity; source unit separation and diameter bound  
**Certificate:** `research/verify_target_c_tooth_reflection_universal_sqrt_face_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The block-optimized theorem left a per-module fork: either one all-lower outer-face run
has square-root support span, or a matching of upper ancestry edges forms a square-root
superdiameter braid.  The first universal-face theorem removed that logical escape by
showing that every maximal upper block pays quadratic support backtracking.  The first
version used the global chord bound `sin x >= 2x/pi` for the ultra-thin blocks and gave
run coefficient `0.735006...`.

At the only scale that can minimize the resulting run length, the number of upper
blocks is `Theta(sqrt(D))`.  Their forced angular spacing is `Theta(1/D)`, so the
relevant directions occupy an `o(1)` angular interval around the tangent.  A direct
layer-cake packing estimate therefore recovers the asymptotically sharp local relation
`sin x = (1-o(1))x`.  Large block counts are already more than sufficient under the
older global sine bound.  This raises the universal run constant to

```math
\boxed{c_{\rm univ}=0.868655543829230\ldots .}
```

Put

```math
h_*:=\frac{\sqrt{303}}{52}=0.334747984337100\ldots .
```

For a fixed split parameter `a in (0,1/2)`, define the sharp small-block coefficients

```math
A_\infty(a):=\frac{\sqrt{2(1-2a)}}4,
\qquad
C_\infty(a):=\frac{a}{h_*},
```

```math
K_\infty(a):=
\frac{A_\infty(a)C_\infty(a)}{A_\infty(a)+C_\infty(a)},
\qquad
c(a):=2\sqrt{K_\infty(a)}.
\tag{UF.1}
```

The function `c(a)` has a unique maximum on `(0,1/2)`.  If `y_* in (0,1)` is the
unique solution of

```math
\boxed{
\sqrt2\,h_*y_*^3=(1-y_*^2)^2,
}
\tag{UF.2}
```

then

```math
a_*:=\frac{1-y_*^2}{2}=0.221693032697319\ldots
\tag{UF.3}
```

is the maximizing split.  At this split,

```math
A_\infty=0.263774035541162\ldots,
\qquad
C_\infty=0.662268461858960\ldots,
```

```math
K_\infty=0.188640613456314\ldots,
\qquad
\boxed{
 c_{\rm univ}=2\sqrt{K_\infty}
 =0.868655543829230\ldots .
}
\tag{UF.4}
```

Then every sufficiently large all-inactive non-anchored FREE ancestry contains one
consecutive all-lower run, lying in the original outer contact face, whose support span
is at least

```math
\boxed{(c_{\rm univ}-o(1))\sqrt D.}
\tag{UF.5}
```

Consequently, for every fixed `Lambda>1`, the same run contains a vertex-disjoint
matching of old fully inactive source pairs of size

```math
\boxed{
\left(\frac{\Lambda-1}{2\Lambda}c_{\rm univ}-o(1)\right)\sqrt D
}
\tag{UF.6}
```

with

```math
\boxed{
1<|x-y|\le
1+\left(\frac{\Lambda h_*}{c_{\rm univ}}+o(1)\right)D^{-1/2}.
}
\tag{UF.7}
```

For `Lambda=2`, this is

```math
\boxed{(0.217163885957308\ldots-o(1))\sqrt D}
\tag{UF.8}
```

vertex-disjoint pairs with

```math
\boxed{
1<|x-y|
\le1+(0.770726640070598\ldots+o(1))D^{-1/2}.
}
\tag{UF.9}
```

A superbraid may still coexist with this run.  It is no longer an alternative that can
avoid the planar face population.

---

## 1. Upper-event notation and exact deficit payment

Use the two-sided activation notation.  Along an upper ancestry edge let

- `Delta>0` be the activation-time increment;
- `d` be the relative vector at the first upper event, with `|d|=D`;
- `b:=-N dot d>0` be the support backtracking;
- `r=d+Delta N` be the corresponding vector between the original source points;
- `rho:=D-|r|>0` be its original diameter deficit.

The clearing-time budget is

```math
\sum\Delta\le t_D<\bar t_D:=h_*+D^{-1/3}.
\tag{UF.10}
```

The exact upper-event identity is

```math
\boxed{2\Delta b=2D\rho-\rho^2+\Delta^2,}
\tag{UF.11}
```

hence

```math
\boxed{
b\ge\frac{\rho}{\Delta}\left(D-\frac\rho2\right).}
\tag{UF.12}
```

Let `B` be the number of maximal consecutive upper blocks and `R` the number of maximal
consecutive lower runs.  Then

```math
\boxed{R\le B+1.}
\tag{UF.13}
```

Fix `a in (0,1/2)`.  Call an upper edge **deficit-bearing** if

```math
\rho\ge\frac aD,
\tag{UF.14}
```

and **ultra-thin** otherwise.

Let `t` be the number of upper blocks containing a deficit-bearing edge.  Choose one
such representative per block.  Since `rho(D-rho/2)` is increasing on `(0,D)`, (UF.12)
gives

```math
b\ge
\frac{a-a^2/(2D^2)}{\Delta}.
```

Cauchy and (UF.10) therefore give

```math
\boxed{
B_{\rm def}\ge C_D(a)t^2,
\qquad
C_D(a):=
\frac{a-a^2/(2D^2)}{h_*+D^{-1/3}}
\longrightarrow\frac a{h_*}.
}
\tag{UF.15}
```

---

## 2. Metric angular separation of ultra-thin source pairs

### Lemma UF.1

Let `AB` and `CD` be two vertex-disjoint source pairs with lengths `L_1,L_2`.  Let
`theta in [0,pi/2]` be the acute projective angle between their supporting lines.  Then

```math
\boxed{
\cos\theta\le\frac{D^2-1}{L_1L_2}.
}
\tag{UF.16}
```

### Proof

Write

```math
A,B=m_1\pm au,
\qquad
C,D=m_2\pm cv,
```

where `2a=L_1`, `2c=L_2`, and orient the unit directions so that
`u dot v=cos theta>=0`.  Put `m=m_2-m_1`.

The two cross-endpoint vectors `m plus/minus (au+cv)` have source length at most `D`, so

```math
|m|^2+|au+cv|^2\le D^2.
```

The other two cross-endpoint vectors `m plus/minus (au-cv)` join distinct source points
and hence have length at least one, so

```math
1\le |m|^2+|au-cv|^2.
```

Subtracting the averaged inequalities gives

```math
1\le D^2-|au+cv|^2+|au-cv|^2
=D^2-4ac\cos\theta.
```

Since `4ac=L_1L_2`, (UF.16) follows. `square`

If both pairs are ultra-thin, then

```math
L_i>D-\frac aD.
```

Set

```math
\delta_D(a):=
\frac{\sqrt{2(1-2a+a^2/D^2)}}{D-a/D}.
\tag{UF.17}
```

Because `a<1/2`, this is positive for all sufficiently large `D`.  Using
`1-cos(theta)<=theta^2/2` in Lemma UF.1 gives

```math
\boxed{\theta\ge\delta_D(a),}
\tag{UF.18}
```

with

```math
\boxed{D\delta_D(a)\longrightarrow\sqrt{2(1-2a)}.}
\tag{UF.19}
```

---

## 3. Two projective packing bounds

Let `p` be the number of upper blocks containing no deficit-bearing edge.  Choose one
ultra-thin representative from each such block.  Distinct representatives are
vertex-disjoint because distinct maximal upper blocks have at least one lower ancestry
edge between them.  Their projective directions are therefore pairwise separated by
at least

```math
\delta:=\delta_D(a).
```

Let `phi_j in [0,pi/2]` be the projective distance of representative `j` from the fixed
tangent direction `N^perp`.

The standard one-dimensional packing inequality is

```math
\boxed{
\sum_{j=1}^p\phi_j
\ge\delta\left\lfloor\frac{p^2}{4}\right\rfloor.
}
\tag{UF.20}
```

It follows by packing the directions as close as possible to the tangent on its two
sides.  Combined with `sin x>=2x/pi`, this gives the global bound

```math
\boxed{
\sum_j\sin\phi_j
\ge\frac{2\delta}{\pi}
\left\lfloor\frac{p^2}{4}\right\rfloor.
}
\tag{UF.21}
```

For the square-root block regime one can do better.  For `0<=r<=pi/2`, a projective
ball of radius `r` about the tangent is an arc of length `2r`, so a `delta`-separated
set puts at most

```math
1+\frac{2r}{\delta}
```

directions in that ball.  Therefore

```math
\#\{j:\phi_j\ge r\}
\ge p-1-\frac{2r}{\delta}.
\tag{UF.22}
```

Put

```math
L:=\frac{\delta(p-1)}2.
```

Layer cake gives

```math
\begin{aligned}
\sum_j\sin\phi_j
&=\int_0^{\pi/2}\cos r\,\#\{j:\phi_j\ge r\}\,dr\\
&\ge
\int_0^L\cos r\left(p-1-\frac{2r}{\delta}\right)dr\\
&\ge
\boxed{
\cos L\,\frac{\delta(p-1)^2}{4}.
}
\end{aligned}
\tag{UF.23}
```

This is the sharp input.  If `p=O(D^(5/8))`, then by (UF.19)

```math
L=O(D^{-3/8})=o(1),
```

so `cos L=1-o(1)` uniformly.

---

## 4. Ultra-thin blocks force support backtracking

For one ultra-thin representative original vector `r_j=d_j+Delta_j N`,

```math
N\cdot r_j=\Delta_j-b_j.
```

Hence

```math
|r_j|\sin\phi_j=|\Delta_j-b_j|
\le\Delta_j+b_j,
```

and therefore

```math
b_j\ge |r_j|\sin\phi_j-\Delta_j.
\tag{UF.24}
```

All representatives have `|r_j|>D-a/D`, and their selected activation increments sum
to at most `bar t_D`.

The global packing bound (UF.21) gives

```math
B_{\rm thin}
\ge
A_D^{\rm flat}(a)p^2-O(1),
\qquad
A_D^{\rm flat}(a)\longrightarrow
\frac{\sqrt{2(1-2a)}}{2\pi}>0.
\tag{UF.25}
```

If `p=O(D^(5/8))`, the sharp bound (UF.23) instead gives

```math
\boxed{
B_{\rm thin}
\ge
(A_D^{\rm sharp}(a)-o(1))(p-1)^2-O(1),
}
\tag{UF.26}
```

where

```math
A_D^{\rm sharp}(a):=
\left(D-\frac aD\right)\frac{\delta_D(a)}4
=
\frac{\sqrt{2(1-2a+a^2/D^2)}}4
\longrightarrow A_\infty(a).
\tag{UF.27}
```

Thus the local small-angle coefficient is larger than the global one by the factor
`pi/2` asymptotically.

---

## 5. Every block count forces the sharp square-root run

The deficit-bearing and ultra-thin representative classes partition the `B=t+p` upper
blocks.

First suppose

```math
B\le D^{5/8}.
\tag{UF.28}
```

Then the sharp bound (UF.26), (UF.15), and weighted Cauchy give

```math
\boxed{
B_{\rm back}
\ge (K_D(a)-o(1))B^2-O(B),
}
\tag{UF.29}
```

where

```math
K_D(a)\longrightarrow K_\infty(a)
=\frac{A_\infty(a)C_\infty(a)}
{A_\infty(a)+C_\infty(a)}.
\tag{UF.30}
```

Indeed replacing `(p-1)^2` by `p^2` costs only `O(p)=O(B)`, while the uniform
`cos L=1-o(1)` factor in (UF.23) changes the quadratic term by `o(B^2)`.

Let `G_low` be total positive support progress of all lower ancestry edges.  The
near-opposite theorem gives net support traverse `D-O(sqrt D)`.  Every upper edge
contributes `Delta-b`, while all activation increments together are `O(1)`.  Hence

```math
G_{\rm low}
\ge
D+(K_D(a)-o(1))B^2-O(B+\sqrt D).
\tag{UF.31}
```

Since `R<=B+1`, some lower run has support span at least `G_low/(B+1)`.  The ideal
continuous minimum is

```math
\min_{x\ge0}\frac{D+Kx^2}{x+1}
=2K\left(\sqrt{1+D/K}-1\right)
=2\sqrt{KD}-O(1).
\tag{UF.32}
```

The error terms in (UF.31) are `o(sqrt D)` after division in the only range
`B=Theta(sqrt D)` where (UF.32) can be asymptotically minimal.  If
`B=o(sqrt D)` the `D/(B+1)` term is already larger; if `B/sqrt D -> infinity` inside
(UF.28), the positive quadratic term is larger.  Therefore

```math
\max_R\operatorname{span}_N(R)
\ge(c(a)-o(1))\sqrt D.
\tag{UF.33}
```

Now suppose

```math
B>D^{5/8}.
\tag{UF.34}
```

Use the global ultra-thin estimate (UF.25) instead.  Its limiting coefficient and
`C_D(a)` are both positive, so weighted Cauchy supplies some fixed `k(a)>0` with

```math
B_{\rm back}\ge k(a)B^2-O(1)
```

for all sufficiently large `D`.  Consequently

```math
\frac{G_{\rm low}}{B+1}
\ge (k(a)-o(1))B
\gg\sqrt D.
\tag{UF.35}
```

Thus large block counts cannot control the minimax constant; the sharp square-root
regime above does.

---

## 6. Optimize the split

Put

```math
y:=\sqrt{1-2a}.
```

Then

```math
A_\infty=\frac{y}{2\sqrt2},
\qquad
C_\infty=\frac{1-y^2}{2h_*}.
```

Maximizing `K_infty` is equivalent to minimizing

```math
\frac1{K_\infty}
=
\frac{2\sqrt2}{y}
+
\frac{2h_*}{1-y^2}.
\tag{UF.36}
```

The critical-point equation is

```math
\sqrt2\,h_*y^3=(1-y^2)^2,
```

which is (UF.2).  The left side is strictly increasing and the right side strictly
decreasing on `(0,1)`, so this solution is unique and is the global optimizer.  The
constants in (UF.3)--(UF.4) follow.

---

## 7. Planarity and the near-unit matching

Two-sided outer-face localization puts every maximal lower run in the original outer
contact face.  Every lower edge has old source length below `sqrt(2)` for sufficiently
large `D`, so the short-edge planarity theorem puts the run in the common plane graph
`P_{<sqrt(2)}(A)`.

For a lower edge `e`, let

```math
\sigma_e=|e|-1>0.
```

The activation-time ledger gives

```math
\sum_{e\in R}\sigma_e\le h_*+D^{-1/3}.
\tag{UF.37}
```

Support progress along one edge is at most `1+sigma_e`.  Hence a run with support span
`(c_univ-o(1))sqrt(D)` contains at least `(c_univ-o(1))sqrt(D)` edges.  Markov leaves a
fraction `1-1/Lambda` with

```math
\sigma_e\le
\left(\frac{\Lambda h_*}{c_{\rm univ}}+o(1)\right)D^{-1/2}.
```

A subset of edges of a path contains a matching of at least half its cardinality up to
an additive constant.  This proves (UF.6)--(UF.9).

---

## 8. Effect on the reflection frontier

The old per-module fork

```math
\text{BLOCK-SQRT-FACE}\quad\text{or}\quad\text{BLOCK-SQRT-SUPER-BRAID}
```

is no longer the logical endpoint.  Every non-anchored FREE module has

```math
\boxed{\text{UNIVERSAL-SQRT-FACE}}
```

with the sharp coefficient (UF.4).  A superbraid may coexist with it and retains all of
its forest, outer-walk, shallow-ear, and ear-flex consequences.

The surviving FREE obstruction is therefore uniform across Woodall topology: every
module carries an outer-face, support-monotone square-root population of old fully
inactive near-unit pairs, all lying in the same global short-edge plane graph.  The
next useful target is multi-module: exploit the ordered and angularly separated module
normals to force congestion, crossing, or shared outer-walk currency among these
planar runs, or convert one module to an exact diameter anchor.

C-II remains open.  No theorem-state authority is changed.

**Disposition:** replaced the global sine loss in the universal FREE-face theorem by a
sharp small-angle projective packing estimate, optimized the deficit split, and raised
the unconditional square-root face-run constant from `0.735006...` to `0.868655...`.
