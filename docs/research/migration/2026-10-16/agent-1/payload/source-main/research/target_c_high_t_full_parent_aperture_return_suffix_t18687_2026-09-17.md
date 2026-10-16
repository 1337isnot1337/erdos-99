# Target C-II — every non-TT paired cell has the full parent-density aperture

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural/metric strengthening; no canonical promotion claimed  
**Scope:** the no-positive-density-TB1 near-full paired exact-force shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** TT-prefix/return-suffix theorem; ordered bilateral narrow-pair theorem; paired destination prefix structure; exact diameter-normal order; C67 projective direction separation  
**Certificate:** `research/verify_target_c_high_t_full_parent_aperture_return_suffix_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding TT-prefix/return-suffix theorem bounded the aperture of a nonterminal suffix by its own suffix length `L`. That loses information: the ordered bilateral gap ramp starts at the first exact-force center, not at the first non-TT center.

If a later non-TT pair were projectively narrow, the ordered bilateral theorem says every earlier pair is narrow as well and the projective gap has already accumulated two C67 direction gaps per earlier center. Independently, the same-host return interval at the current non-TT center contains two actual diameter directions from every later center. The forward and backward counts meet at the full parent size `N`.

Hence every non-TT cell, wherever it occurs after the TT prefix, obeys

\[
\boxed{
\eta_s\ge N\delta_D-o(1),
\qquad
\delta_D=2\arcsin{1\over2D}.
}
\]

Since

\[
N>\left({c\over2}-o(1)\right)D,
\qquad c={113\over5{,}000{,}000},
\]

we obtain the uniform parent-density aperture

\[
\boxed{
\eta_s\ge{c\over2}-o(1)
=1.13\times10^{-5}-o(1)
}
\]

for **every non-TT center**. The aperture does not deteriorate when the non-TT suffix is short.

Thus the paired destination word now has a sharper interpretation:

```text
TT prefix:
    spends 2*delta_D of terminal normal span per additional cell;

mixed/OO suffix:
    every single cell already has projective force-pair gap
    at least the full parent density scale c/2-o(1).
```

---

## 1. Setup

Order the near-full paired exact-force population by

\[
i_1<i_2<\cdots<i_N<k,
\qquad
N>\left({c\over2}-o(1)\right)D.
\tag{PA.1}
\]

Let `M` be the TT-prefix length. If `s>M`, one force lane has already left `T_m` and remains on its opposite physical host for the rest of the population. Relabel the hosts so at the current non-TT center

\[
x_s^A,\ y_s^B
\]

lie on the same physical host `A`, with `x_s^A` the mate birth and `y_s^B` the opposite-host partner.

Let

\[
\eta_s=d_{\mathbb{RP}^1}([d_s^A],[d_s^B])
\tag{PA.2}
\]

be the projective force-pair gap.

Fix the harmless threshold

\[
\rho_0={\gamma_H\over2},
\qquad
\gamma_H=\arcsin c_H.
\tag{PA.3}
\]

The target lower bound `N delta_D` is `o(1)` and in fact tends to at most `c/2`, so it is far below `rho_0`. Therefore a center with `eta_s>=rho_0` automatically satisfies the theorem for all sufficiently large sources. It remains only to consider

\[
\eta_s<\rho_0.
\tag{PA.4}
\]

Then the force pair is in the near-antipodal ordinary realization.

---

## 2. Forward count: all earlier centers contribute two C67 gaps

The ordered bilateral theorem proves that the `rho_0`-narrow exact-force centers form an initial segment of the ordered population. Therefore (PA.4) implies that all centers

\[
1,2,\ldots,s
\]

are `rho_0`-narrow.

For narrow pairs, the projective gap grows by at least `2 delta_D` per retained center. Hence

\[
\boxed{
\eta_s\ge2(s-1)\delta_D.
}
\tag{PA.5}

The important point is that the count begins at center `1`, including any TT prefix. Resetting it at `M+1` is unnecessary and loses strength.

---

## 3. Backward count: all later cells contribute two support normals

Because `s` is non-TT, choose the force lane which has left `T_m` by center `s`. As in the return-suffix theorem, the physical host arc from mate birth `x_s^A` to opposite-host partner `y_s^B` contains, for every `t>s`, both

\[
x_t^A
\quad\text{and}\quad
y_t^B.
\tag{PA.6}
\]

Their outward diameter support normals are

\[
d_t^A,\qquad -d_t^B.
\tag{PA.7}
\]

Together with the two endpoint normals `d_s^A,-d_s^B`, this gives

\[
2(N-s)+2
\]

distinct actual diameter directions inside the same-host normal interval whose width is exactly `eta_s` in the near-antipodal regime.

Canonical C67 separates distinct projective diameter directions by at least `delta_D`. Since this interval has width below `rho_0<pi/2`, projective and ordinary angular separations agree. Therefore

\[
\boxed{
\eta_s\ge[2(N-s)+1]\delta_D.
}
\tag{PA.8}

---

## 4. Exact discrete minimax gives the full parent size

Combine (PA.5) and (PA.8):

\[
\eta_s
\ge
\max\{2(s-1),\ 2(N-s)+1\}\delta_D.
\tag{PA.9}

For every integer `1<=s<=N`,

\[
\boxed{
\max\{2(s-1),\ 2(N-s)+1\}\ge N.
}
\tag{PA.10}

Indeed, if both terms were below `N`, adding the two strict inequalities would give

\[
2N-1<2N,
\]

but the integer parity cases give the sharper exact minimum

\[
\min_{1\le s\le N}
\max\{2(s-1),2(N-s)+1\}=N.
\tag{PA.11}

Thus every narrow non-TT center satisfies

\[
\boxed{
\eta_s\ge N\delta_D.
}
\tag{PA.12}

The large-gap case was already automatic, so (PA.12) holds asymptotically for every non-TT center, with at most the harmless host-margin `o(1)` bookkeeping inherited from identifying the near-antipodal branch.

---

## 5. Asymptotic aperture and central diamond

Since

\[
D\delta_D\to1
\]

and (PA.1) holds,

\[
\boxed{
\eta_s\ge{c\over2}-o(1)
=1.13\times10^{-5}-o(1)
}
\tag{PA.13}

uniformly over all non-TT centers.

For any fixed

\[
0<\rho<{c\over2},
\]

the fixed-angle central-diamond theorem therefore applies to every non-TT center for all sufficiently large sources. Letting `rho` approach `c/2`, its endpoint-separation scale approaches

\[
\boxed{
D\sin{c\over4}-2L_D,
}
\tag{PA.14}

where `L_D=o(D)`. Numerically,

\[
\boxed{
\sin{c\over4}
=5.64999999997\ldots\times10^{-6}.
}
\tag{PA.15}

Thus every non-TT force pair has a central diamond of fixed positive linear size at the full parent density scale.

---

## 6. Updated TT-prefix / non-TT-suffix normal form

Let the TT prefix have size `M` and the remaining suffix size

\[
L=N-M.
\]

The ordered bilateral theorem gives

\[
\boxed{
\operatorname{normalspan}(T_m)
\ge2\gamma_H+2(M-1)_+\delta_D-o(1).
}
\tag{PA.16}

The present theorem gives, simultaneously,

\[
\boxed{
\eta_s\ge N\delta_D-o(1)
\quad\text{for every }s>M.
}
\tag{PA.17}

Therefore the tradeoff is now only in **cardinality**, not aperture:

- a long TT prefix forces a wider terminal normal interval;
- every cell that survives outside TT is already uniformly wide at aperture `c/2-o(1)`, regardless of how short the suffix is.

Along a subsequence with

\[
{M\over D}\to\theta,
\qquad
{L\over D}\to\ell,
\qquad
\theta+\ell\ge{c\over2},
\]

we have

\[
\liminf\operatorname{normalspan}(T_m)
\ge2\gamma_H+2\theta,
\tag{PA.18}
\]

while every non-TT suffix cell has

\[
\boxed{
\liminf\eta_s\ge{c\over2}.
}
\tag{PA.19}
\]

This substantially narrows the exact-force frontier. Projectively collapsing force cells can occur only inside the TT prefix. The first cell outside TT immediately has a fixed parent-density aperture.

C-II remains open. A closing argument may now treat the paired branch as a clean cardinality split between terminal-terminal cells and fixed-wide central-diamond cells, without an aperture/cardinality optimization on the latter.

**Disposition:** restored the global forward C67 count across the TT prefix and proved that every non-TT paired force cell has aperture at least `N delta_D`, asymptotically `c/2=1.13e-5`, independent of suffix length. C-II and Level I remain open.
