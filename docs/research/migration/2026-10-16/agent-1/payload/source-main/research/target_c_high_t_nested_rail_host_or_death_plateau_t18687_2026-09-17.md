# Target C-II — a nested force rail is either cross-host or death-concentrated

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the endpoint-disjoint exact-antipodal deep-force braid on one pre-hub high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** partner-rainbow support order; complete nested partner-support rail; one-sided path-region support coordinates; parameterized deep grid-force density; optional global one-sided reaction budget  
**Certificate:** `research/verify_target_c_high_t_nested_rail_host_or_death_plateau_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The nested partner-support theorem deliberately avoided an unsafe step: it did not claim that the hubward partner endpoints of the nested rail lie on one physical host arc. The hubward boundary shore contains two ordered host-side pieces joined by the far terminal boundary piece, so an arbitrary partner family can pass through the turn.

For a **nested** rail, however, the turn can only be used in one very specific way. The partner-region tags are monotone in the ambient boundary order, while the hubward shore's region word changes monotonicity exactly once. Therefore every partner endpoint lying on the "wrong" side of the turn has one and the same region tag. Equivalently, the only obstruction to a genuine cross-host nested rail is concentration at a single post-hub death interface.

This gives an exact two-way normal form.

---

## Theorem HD — host rail versus death plateau

Let

\[
i_1<i_2<\cdots<i_M<k
\tag{HD.1}
\]

be the centers of a complete nested partner-support rail from the current high-`t` deep-force braid. Thus for one fixed birth side `sigma in {+,-}` there are actual diameter bars `h_s`, one from every selected force cell, with

\[
I_s=\{i_s+1,\ldots,b_s\},
\qquad
b_s\ge k,
\tag{HD.2}
\]

and

\[
\boxed{
b_1\ge b_2\ge\cdots\ge b_M.}
\tag{HD.3}
\]

The `2M` endpoints of the parent braid are pairwise distinct and every two selected bars cross geometrically.

Let `Q` be the hubward boundary shore cut off by `tau_k`. Write it in ambient cyclic order as

\[
Q=Q^\uparrow\cup T_m\cup Q^\downarrow,
\tag{HD.4}
\]

where

- `Q^uparrow` is the first hubward host-side arc, whose region labels run weakly upward from `R_k` to `R_m`;
- `T_m` is the far terminal boundary piece, entirely in `R_m`;
- `Q^downarrow` is the second hubward host-side arc, whose region labels run weakly downward from `R_m` to `R_k`.

Then one of the two host arcs, denoted `Q^host`, has the following property:

\[
\boxed{
\text{all selected partner endpoints outside }Q^{host}
\text{ have one common support-end tag }b_*.
}
\tag{HD.5}
\]

Consequently the nested rail splits as

\[
L=L_{host}\sqcup L_{plateau}
\tag{HD.6}
\]

with

\[
|L_{host}|+|L_{plateau}|=M,
\tag{HD.7}
\]

such that

1. every bar of `L_host` has its birth endpoint on one fixed pre-hub host arc and its partner endpoint on one fixed hubward host arc;
2. every bar of `L_plateau` satisfies
   \[
   \boxed{b_s=b_*}
   \tag{HD.8}
   \]
   and hence belongs to the same post-hub switching set `X_{b_*}`.

In particular,

\[
\boxed{
|L_{host}|\ge {M\over2}
\quad\text{or}\quad
|L_{plateau}|\ge {M\over2}.}
\tag{HD.9}
\]

Thus every large nested force rail contains either a large genuine cross-host nested subrail or a large pairwise-crossing endpoint-disjoint family dying at one post-hub interface.

---

## 1. The hubward region word has exactly one turn

The phase-free path coordinates are

\[
R_0-\tau_1-R_1-\cdots-\tau_m-R_m.
\tag{HD.10}
\]

Fix the common hub cut `tau_k`. Along the complementary hubward boundary interval `Q`, the first host side meets the regions in the order

\[
R_k,R_{k+1},\ldots,R_m,
\tag{HD.11}
\]

then the far terminal boundary piece lies in `R_m`, and the second host side returns through

\[
R_m,R_{m-1},\ldots,R_k.
\tag{HD.12}
\]

A region can contribute several consecutive hull vertices. Therefore the exact region-label word on `Q` is weakly nondecreasing on `Q^uparrow`, constant on `T_m`, and weakly nonincreasing on `Q^downarrow`.

This is the only topology used below.

---

## 2. If the nested rail is the `+` lane, the wrong-side tail is constant

For the `+` birth-side lane, the complete-crossing order theorem places partner endpoints on `Q` in the order

\[
y_M^+,y_{M-1}^+,\ldots,y_1^+.
\tag{HD.13}
\]

Nesting gives

\[
b_1^+\ge b_2^+\ge\cdots\ge b_M^+,
\]

so the region labels in the displayed boundary order are

\[
b_M^+\le b_{M-1}^+\le\cdots\le b_1^+.
\tag{HD.14}
\]

Thus the selected partner labels form a weakly **nondecreasing** subsequence of the one-turn word on `Q`.

Take all selected endpoints outside `Q^uparrow`, namely those on `T_m union Q^downarrow`. The ambient region word there is weakly nonincreasing. A sequence that is simultaneously a subsequence of this weakly nonincreasing word and part of the globally nondecreasing selected sequence must be constant. Hence all such endpoints have one common region tag `b_*`.

So in the `+` case take

\[
Q^{host}=Q^\uparrow.
\tag{HD.15}
\]

---

## 3. If the nested rail is the `-` lane, the wrong-side head is constant

For the `-` birth-side lane, the partner endpoints occur on `Q` in the order

\[
y_1^-,y_2^-,\ldots,y_M^-.
\tag{HD.16}
\]

Nesting gives directly

\[
b_1^-\ge b_2^-\ge\cdots\ge b_M^-.
\tag{HD.17}
\]

Thus the selected labels are weakly **nonincreasing** in ambient boundary order.

Now take all selected endpoints outside `Q^downarrow`, namely those on `Q^uparrow union T_m`. The ambient region word there is weakly nondecreasing. A subsequence that is also globally nonincreasing must be constant. Therefore all such selected endpoints have one common tag `b_*`.

So in the `-` case take

\[
Q^{host}=Q^\downarrow.
\tag{HD.18}
\]

This proves (HD.5) in both cases.

---

## 4. A common tag is a common death interface

For a pre-hub bar born at interface `i_s`, exact interval support is

\[
I_s=\{i_s+1,\ldots,b_s\}.
\tag{HD.19}
\]

Hence its only post-hub support switch is the terminal interface `b_s`. If `b_s=b_*`, then the bar belongs to the post-hub switching set `X_{b_*}`.

Therefore all bars in `L_plateau` switch off at one and the same post-hub interface. They remain pairwise endpoint-disjoint and pairwise crossing because they are a subfamily of the complete deep braid.

No assertion is made that their partner endpoints coincide; they are distinct hull vertices lying in the same path region `R_{b_*}`. The conclusion is concentration of the **support-end interface**, not a graph-theoretic endpoint star.

---

## 5. Quantitative extraction

Use the parameterized deep-force density

\[
\lambda=c_0-6\rho-\eta-2\delta>0,
\qquad
c_0={113\over20{,}000{,}000}.
\tag{HD.20}
\]

The current endpoint/window conflict extraction and nested-rail theorem give

\[
M>
\left({\lambda\over16\,3^{1/8}}-o(1)\right)D^{1/4}.
\tag{HD.21}
\]

Therefore one branch of (HD.9) has size

\[
\boxed{
>
\left({\lambda\over32\,3^{1/8}}-o(1)\right)D^{1/4}.}
\tag{HD.22}
\]

For the ninety-percent parameter choice

\[
\rho=\delta={c_0\over100},
\qquad
\eta={c_0\over50},
\qquad
\lambda={9c_0\over10},
\tag{HD.23}
\]

this coefficient is

\[
\boxed{1.38516280797\times10^{-7}.}
\tag{HD.24}
\]

As the fixed parameter losses tend to zero, the coefficient approaches

\[
\boxed{
{c_0\over32\,3^{1/8}}
\approx1.53906978663\times10^{-7}.}
\tag{HD.25}
\]

A further two-color thinning inside whichever branch survives gives one coherent transverse sign with half this leading coefficient.

---

## 6. Stress-dilute version

Impose the existing one-sided KKT quantile before the endpoint/window extraction. For fixed `0<sigma<1`, retain the parent cells with

\[
B_i\le {1\over\sigma\lambda D},
\qquad
0<|G_i|\le {1\over\sigma\lambda}.
\tag{HD.26}
\]

Their density is `>(1-sigma)lambda D-o(D)`. The same extraction and dichotomy give either a cross-host rail or a one-death-interface plateau of size

\[
\boxed{
>
\left({(1-\sigma)\lambda\over32\,3^{1/8}}-o(1)\right)D^{1/4}.}
\tag{HD.27}
\]

Every retained bar is still born at a cell satisfying (HD.26). If one also requires a common transverse sign, the coefficient is halved again.

For (HD.23) and `sigma=1/2`, the unsigned branch coefficient is

\[
6.92581403985\times10^{-8},
\tag{HD.28}
\]

and the coherent-sign coefficient is

\[
3.46290701992\times10^{-8}.
\tag{HD.29}
\]

---

## 7. Frontier effect

The earlier overstrong cross-host shortcut failed because the hubward partner block can use the far terminal piece and both host sides. The present theorem pays for exactly that missing possibility instead of discarding it.

A surviving exact-antipodal high-`t` branch now contains, at `Omega(D^(1/4))` scale, one of two concrete objects:

```text
HOST branch:
  fixed pre-hub birth host arc
  -> fixed hubward partner host arc
  + strictly nested train supports
  + pairwise crossing endpoint-disjoint diameter bars
  + common inverse-D near-triangular birth grid

PLATEAU branch:
  strictly nested births
  -> one common post-hub support-end interface b_*
  + Omega(D^(1/4)) pairwise crossing endpoint-disjoint bars in X_{b_*}
  + common inverse-D near-triangular birth grid.
```

The remaining closure problem is correspondingly sharper. The host branch can be attacked using two-sided boundary order and near-central diameter geometry. The plateau branch concentrates an unbounded force-rail population into one post-hub switching interface and should be attacked with the post-hub cut resultant, terminal complexity, and direction-separation budgets.

No C-II or Level-I closure is claimed.

**Disposition:** converted the safe one-turn partner-region order into an exact host-versus-single-death-interface dichotomy. This isolates the far-side ambiguity that invalidated the earlier half-turn shortcut instead of assuming it away. C-II and Level I remain open.
