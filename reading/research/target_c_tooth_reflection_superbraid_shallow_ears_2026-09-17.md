> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_superbraid_shallow_ears_2026-09-17.md) · source SHA-256 `929eea7fcabd9211eb810528c825970d92a1373dcad44820c38ddd2e302efd6e`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a0fcd96098060a18cb98ed3692480469dd134988", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_superbraid_shallow_ears_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "fca9e2dcd4ef887dab027c6465f2fa1ef05505a79309ca25a2b6a08e26002260"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — superbraid terminal deficit forces shallow inactive hull ears

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the BLOCK-SQRT-SUPER-BRAID branch  
**Scope:** block-optimized FREE superdiameter braid in the contact-minimal, then diameter-pair-minimal C-II representative  
**Dependencies:** block-optimized FREE square-root fork; superbraid forest-transversal theorem; full-source hull perimeter bound  
**Certificate:** `research/verify_target_c_tooth_reflection_superbraid_shallow_ears_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current BLOCK-SQRT-SUPER-BRAID branch has

```math
 m_D=(c_{\rm blk}-o(1))\sqrt D,
 \qquad
 c_{\rm blk}=0.925539574680581\ldots,
```

pairwise-crossing inactive superdiameter chords. Their `2m_D` endpoints are distinct
vertices of the full source hull `K=conv(A)` and are disjoint from the `q` actual
diameter endpoints.

The preceding outer-walk note used only the count of those extra hull vertices:

```math
 q+2m_D\le \operatorname{per}(K)\le \pi D.
```

This note retains the *local convex geometry* at the braid endpoints. It shows that
when the terminal deficit

```math
 t_D:=\pi D-q
```

is sublinear, almost every superbraid endpoint is an `o(1)`-deep ear of the full source
hull. At the square-root terminal scale `t_D=O(\sqrt D)`, a positive proportion of
the braid endpoints are already `O(D^{-1/2})`-deep.

The same ear geometry gives an exact source-preserving inward move: moving such an
inactive hull endpoint to the chord between its two neighboring hull vertices can
never create a new diameter violation. The only metric obstruction is a lower
unit-distance collision. Hence every shallow endpoint has a finite dichotomy:

1. it is guarded by an original source pair of length at most `1 + ear depth`; or
2. it can be pushed off the hull through that depth while preserving unit separation,
   the diameter `D`, the old contact graph, and the old diameter-pair graph.

No tertiary normalization is assumed. In particular this note does **not** claim that
case 2 contradicts global minimality; it records the exact deformation that a future
source-level closure has to exploit.

---

## 1. Ear notation

Let

```math
S=\{v_1,\ldots,v_N\}
```

be the set of all endpoints of a selected BLOCK-SQRT-SUPER-BRAID, so

```math
\boxed{N=2m_D=(2c_{\rm blk}-o(1))\sqrt D.}
\tag{SE.1}
```

Every `v in S` is a fully inactive source point and a vertex of the full source hull
`K`. Let `a_v,b_v` be its two neighboring vertices on `partial K`. Write

```math
\alpha_v=|a_v-v|,
\qquad
\beta_v=|b_v-v|,
\qquad
s_v:=\min(\alpha_v,\beta_v),
```

and let `theta_v in (0,pi)` be the exterior turning angle at `v`. Thus the interior
angle of the hull polygon at `v` is `pi-theta_v`.

For `theta_v<pi/2`, the perpendicular from `v` to the chord `[a_v,b_v]` lands in the
relative interior of that chord. Let

```math
 p_v\in(a_v,b_v),
 \qquad
 d_v:=|v-p_v|=\operatorname{dist}(v,[a_v,b_v])
\tag{SE.2}
```

be the ear foot and ear depth.

Elementary triangle geometry gives

```math
\boxed{d_v\le s_v\sin\theta_v\le s_v\theta_v.}
\tag{SE.3}
```

At most four hull vertices can have `theta_v>=pi/2`, because the total exterior turn
is `2pi`.

---

## 2. The special-edge budget is the terminal deficit

Let the full hull have `H` vertices and side lengths `ell_e`. Unit separation gives

```math
\ell_e\ge1
```

for every full-hull side. Put

```math
X_K:=\sum_e(\ell_e-1)=\operatorname{per}(K)-H.
```

The `q` actual diameter endpoints and the `N` inactive superbraid endpoints are
disjoint hull vertices, so

```math
H\ge q+N.
```

Cauchy's diameter-perimeter inequality gives `per(K)<=pi D`; therefore

```math
\boxed{
X_K
\le \pi D-q-N
=t_D-N.
}
\tag{SE.4}
```

For one special endpoint,

```math
s_v
\le 1+{(\alpha_v-1)+(\beta_v-1)\over2}.
```

Summing over `S`, every hull-side excess appears with total coefficient at most one:

```math
\begin{aligned}
\sum_{v\in S}s_v
&\le
N+{1\over2}\sum_{v\in S}
\bigl[(\alpha_v-1)+(\beta_v-1)\bigr]\\
&\le N+X_K\\
&\le t_D.
\end{aligned}
```

Hence

```math
\boxed{\sum_{v\in S}s_v\le t_D.}
\tag{SE.5}
```

This is sharper than the raw bound `sum s_v<=per(K)`: the entire adjacent-side budget
at the inactive superbraid endpoints is paid by the terminal deficit `pi D-q`.

---

## 3. Square-root ear-depth ledger

Let

```math
S_0:=\{v\in S:\theta_v<\pi/2\}.
```

By (SE.3), Cauchy-Schwarz, (SE.5), and the total-turn identity,

```math
\begin{aligned}
\sum_{v\in S_0}\sqrt{d_v}
&\le
\sum_{v\in S_0}\sqrt{s_v\theta_v}\\
&\le
\sqrt{
\left(\sum_{v\in S_0}s_v\right)
\left(\sum_{v\in S_0}\theta_v\right)}\\
&\le
\sqrt{2\pi t_D}.
\end{aligned}
```

Thus

```math
\boxed{
\sum_{v\in S_0}\sqrt{d_v}
\le\sqrt{2\pi(\pi D-q)}.
}
\tag{SE.6}
```

For every `lambda>0`, Markov immediately gives

```math
\boxed{
\#\{v\in S_0:d_v>\lambda\}
\le
\sqrt{\frac{2\pi t_D}{\lambda}}.
}
\tag{SE.7}
```

Since only four braid endpoints were discarded when passing from `S` to `S_0`,

```math
\boxed{
\#\{v\in S:d_v\le\lambda,\ \theta_v<\pi/2\}
\ge
N-4-\sqrt{\frac{2\pi t_D}{\lambda}}.
}
\tag{SE.8}
```

This is the main quantitative theorem.

---

## 4. Sublinear terminal deficit makes almost every braid endpoint shallow

Assume along a superbraid sequence that

```math
t_D=o(D).
```

The preceding forest doubled-gap theorem already identifies this as the only regime in
which the forest outer-walk currency can remain sublinear.

Set

```math
\lambda_D:=\sqrt{t_D/D}.
\tag{SE.9}
```

The block-superbraid lower bound gives `t_D>=N=(2c_blk-o(1))sqrt(D)`, so `lambda_D`
is defined and positive for large `D`. Also `lambda_D=o(1)`. From (SE.7),

```math
{1\over\sqrt D}
\#\{v\in S_0:d_v>\lambda_D\}
\le
\sqrt{2\pi}
\left({t_D\over D}\right)^{1/4}
=o(1).
```

Therefore

```math
\boxed{
(2c_{\rm blk}-o(1))\sqrt D
}
\tag{SE.10}
```

superbraid endpoints satisfy

```math
\boxed{d_v\le\sqrt{t_D/D}=o(1).}
\tag{SE.11}
```

So a sublinear-terminal survivor cannot realize its inactive near-diameter braid with
macroscopically deep convex-hull ears. Almost every braid endpoint lies `o(1)` from the
chord joining its two neighboring full-hull vertices.

---

## 5. The square-root terminal window gives inverse-square-root ears

Suppose more quantitatively that for some fixed `C>0`,

```math
t_D\le C\sqrt D.
\tag{SE.12}
```

Take

```math
\lambda={K\over\sqrt D}
```

with fixed `K>0`. Equations (SE.1) and (SE.8) give

```math
\boxed{
\#\left\{v\in S_0:d_v\le {K\over\sqrt D}\right\}
\ge
\left(
2c_{\rm blk}-\sqrt{\frac{2\pi C}{K}}-o(1)
\right)\sqrt D.
}
\tag{SE.13}
```

In particular this is a positive square-root population whenever

```math
\boxed{
K>{\pi C\over2c_{\rm blk}^2}
=1.833706778894253\ldots\,C.
}
\tag{SE.14}
```

Thus the near-minimal superbraid terminal window has the same `D^{-1/2}` local scale as
the BLOCK-SQRT-FACE branch, but it appears as a full-hull ear depth rather than as a
near-unit lower-gate excess.

---

## 6. Exact inward ear deformation

The shallow-ear conclusion has a source-level interpretation that does not use any
KKT extension to isolated coordinates.

Fix a fully inactive hull vertex `v` with `theta_v<pi/2`, and let `p=p_v` be its ear
foot. Move only `v` along

```math
v(t)=(1-t)v+tp,
\qquad 0\le t\le1.
\tag{SE.15}
```

All other source points remain fixed.

### Upper-distance safety

For every fixed source point `u != v`, both `v` and `p` belong to the original convex
hull `K`, whose diameter is `D`. Therefore

```math
|v-u|\le D,
\qquad
|p-u|\le D.
```

Convexity of the Euclidean norm gives

```math
\boxed{
|v(t)-u|
\le(1-t)|v-u|+t|p-u|
\le D.
}
\tag{SE.16}
```

There is in fact no new equality at `D`. Since `v` is diameter-inactive,
`|v-u|<D`. Since `p` is a strict convex combination of the distinct hull neighbors
`a_v,b_v`, strict convexity gives

```math
|p-u|<D.
```

Hence

```math
\boxed{|v(t)-u|<D\quad(0\le t\le1).}
\tag{SE.17}
```

So the motion cannot create a new diameter pair and cannot destroy any old diameter
pair, because no old diameter pair uses `v`.

### The only obstruction is a unit collision

If the motion remains unit-separated through `t=1`, the terminal source has the same
cardinality, the same diameter `D`, the same contact count and contact graph, and the
same diameter-pair graph. The point `v(1)=p` lies on the chord `[a_v,b_v]` rather than
at the old extreme position, so the full hull has lost the old ear at `v`.

Otherwise there is a first time `t_* in (0,1]` and a source point `u != v` such that

```math
|v(t_*)-u|=1.
```

Because `v` was contact-inactive in the original source,

```math
|v-u|>1.
```

The triangle inequality and `|v-v(t_*)|<=d_v` give

```math
\boxed{
1<|v-u|\le1+d_v.
}
\tag{SE.18}
```

Therefore every shallow inactive braid endpoint has the exact finite fork

```math
\boxed{
\begin{array}{ll}
\text{GUARDED:} & \exists u\in A:\ 1<|v-u|\le1+d_v,\\[1mm]
\text{MOVABLE:} & v\text{ can be pushed to }[a_v,b_v]
\text{ while preserving all source constraints and both old graphs.}
\end{array}}
\tag{SE.19}
```

No claim is made that MOVABLE by itself contradicts the existing two-stage canonical
normalization. It is a genuine same-diameter flat direction of the global minimizer
stratum. A future closure can either exploit the resulting near-unit guards or add a
legitimate source-level argument that rules out a large simultaneous family of such
flat ear removals.

---

## 7. Frontier effect

The BLOCK-SQRT-SUPER-BRAID branch now has an additional internal split.

If `t_D=pi D-q` is linear, the existing forest doubled-gap / outer-walk machinery
already has linear currency.

If `t_D=o(D)`, then almost every one of the

```math
(2c_{\rm blk}-o(1))\sqrt D
```

inactive braid endpoints is an `o(1)`-deep full-hull ear. At the sharp square-root
terminal scale, a positive square-root population has depth `O(D^{-1/2})`.
Every one of those shallow ears is either guarded by an original source pair at the
same scale or supports an explicit inward same-diameter deformation with no upper
metric obstruction.

This does not close C-II. It removes a previously implicit geometric freedom in the
superbraid branch: a sublinear-terminal survivor must place its inactive almost-
diameter endpoints nearly on the chords between neighboring hull vertices. The next
source-level target is to rule out a square-root family of MOVABLE shallow ears, or to
show that enough of them are GUARDED to feed the existing short-edge / near-unit
machinery.

**Disposition:** converted the full-hull perimeter deficit from the block superbraid
into a quantitative ear-depth ledger and an exact guard-or-inward-deformation theorem.
