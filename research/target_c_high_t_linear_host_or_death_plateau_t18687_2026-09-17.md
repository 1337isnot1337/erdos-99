<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "254bd5825a77c9107498e8010068568cac58e394", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_linear_host_or_death_plateau_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "94c092a7690f8db423d9b253b4d6118640f803e1fde442fd723cfeac0f93e8b4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the host/death-plateau dichotomy already holds at linear density

**Date:** 2026-09-17  
**Status:** proof-only high-`t` structural strengthening; no canonical promotion claimed  
**Scope:** the no-fixed-margin-TB1 exact-antipodal high-`t` shore through `t=(q-k)/D<=1.8687`  
**Dependencies:** linear nested partner rail; one-turn hubward path-region order; common-hub interval support; source-wide diameter-degree bound; optional global one-sided reaction budget  
**Certificate:** `research/verify_target_c_high_t_linear_host_or_death_plateau_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The previous host-versus-death-plateau theorem was stated only after partner-endpoint thinning, at `Omega(D^(1/4))` scale. That thinning is not needed for the dichotomy itself.

The linear nested-rail theorem already gives one actual diameter bar from every cell of a `Theta(D)` deep-force population, with distinct birth endpoints, weakly ordered partner incidences, and strictly nested support intervals. Partner endpoints may repeat. Repetition only creates ties in the hubward boundary order, and the one-turn argument uses only path-region labels. Therefore the same host/death split works before any degree thinning.

This gives a stronger normal form: either a linear cross-host nested rail survives, or one single post-hub interface carries a linear number of distinct diameter switches.

---

## Theorem LHD — linear host rail versus macroscopic death interface

Fix the parameterized deep family on one pre-hub shore,

\[
Q_D=Q_D(r;\rho,\eta,\delta),
\qquad
|Q_D|=N>\lambda D-o(D),
\tag{LHD.1}
\]

where

\[
\lambda=c_0-6\rho-\eta-2\delta>0,
\qquad
c_0={113\over20{,}000{,}000}.
\tag{LHD.2}
\]

By the linear nested-rail theorem there is a fixed birth side `sigma in {+,-}` and one selected actual diameter bar `h_s` from every center

\[
i_1<i_2<\cdots<i_N<k
\tag{LHD.3}
\]

such that

\[
I_s=\{i_s+1,\ldots,b_s\},
\qquad b_s\ge k,
\tag{LHD.4}
\]

and

\[
\boxed{
b_1\ge b_2\ge\cdots\ge b_N.}
\tag{LHD.5}
\]

Hence

\[
I_1\supsetneq I_2\supsetneq\cdots\supsetneq I_N.
\tag{LHD.6}
\]

The birth endpoints are pairwise distinct. Partner endpoints may repeat.

Let the hubward boundary shore be

\[
Q=Q^\uparrow\cup T_m\cup Q^\downarrow,
\tag{LHD.7}
\]

in ambient cyclic order, with path-region labels weakly increasing on `Q^uparrow`, constant on the far terminal piece `T_m`, and weakly decreasing on `Q^downarrow`.

Then one host arc `Q^host` has the property

\[
\boxed{
\text{every selected partner incidence outside }Q^{host}
\text{ has one common support-end tag }b_*.
}
\tag{LHD.8}

Consequently the full linear rail splits as

\[
L=L_{host}\sqcup L_{plateau},
\tag{LHD.9}
\]

with

\[
|L_{host}|+|L_{plateau}|=N,
\tag{LHD.10}
\]

where

1. every bar in `L_host` joins the fixed pre-hub birth host arc to one fixed hubward host arc and retains the strict support nesting;
2. every bar in `L_plateau` satisfies
   \[
   \boxed{b_s=b_*}
   \tag{LHD.11}
   \]
   and therefore belongs to the same post-hub switching set `X_{b_*}`.

Thus

\[
\boxed{
|L_{host}|\ge {N\over2}
\quad\text{or}\quad
|L_{plateau}|\ge {N\over2}.}
\tag{LHD.12}
\]

In the plateau alternative the bars are distinct because their birth endpoints are distinct. Hence, writing

\[
N_j:=|X_j|,
\tag{LHD.13}
\]

one has the macroscopic local switch bound

\[
\boxed{
N_{b_*}\ge |L_{plateau}|
>{\lambda\over2}D-o(D).}
\tag{LHD.14}
\]

So the failure of a linear cross-host rail is not diffuse: it forces a single post-hub interface to absorb a positive linear number of distinct actual diameter interval ends.

---

## 1. Partner collisions do not affect the one-turn proof

The only new point relative to the endpoint-disjoint theorem is that several selected bars may share one hubward source vertex.

The linear nested-rail theorem orders partner **incidences** on `Q`. If two bars have distinct partner vertices, their independent diameter chords cross and the partner order is forced by the convex-thrackle order. If they share a partner vertex, record the two incidences consecutively at that vertex in the birth-induced tie order. Both incidences have the same path-region tag.

Therefore partner collisions create only repeated equal entries in the selected region-label word. They cannot create an inversion.

For the `+` nested lane the selected partner labels, in ambient order on `Q`, are weakly nondecreasing. The ambient labels on `T_m union Q^downarrow` are weakly nonincreasing. Any selected subsequence lying there is therefore constant. Take

\[
Q^{host}=Q^\uparrow.
\tag{LHD.15}
\]

For the `-` nested lane the selected partner labels are weakly nonincreasing. The ambient labels on `Q^uparrow union T_m` are weakly nondecreasing. The selected subsequence there is constant. Take

\[
Q^{host}=Q^\downarrow.
\tag{LHD.16}
\]

This proves (LHD.8) without any endpoint-degree estimate.

---

## 2. A common tag is still one common switch-off interface

The exact support interval of the selected pre-hub bar is

\[
I_s=\{i_s+1,\ldots,b_s\}.
\tag{LHD.17}
\]

Its unique post-hub switch is the right endpoint `b_s`. Therefore every bar with `b_s=b_*` lies in `X_{b_*}`.

Distinct birth endpoints imply distinct edges even when partner endpoints collide. Hence all plateau bars contribute separately to the raw switching count at `b_*`, proving (LHD.14).

No KKT multiplier lower bound is used. The conclusion is a **cardinality concentration**, not a stress-mass concentration.

---

## 3. Endpoint-disjoint extraction can be postponed until after the dichotomy

The source-wide diameter-degree bound is

\[
\Delta(H)\le(4\,3^{1/8}+o(1))D^{3/4}.
\tag{LHD.18}
\]

Birth endpoints in the linear rail are already distinct. Greedily retain at most one selected rail bar per partner vertex. Every partner vertex can account for at most `Delta(H)` rail bars, so either branch in (LHD.12), once it has size at least `N/2`, contains an endpoint-disjoint subrail of size

\[
\boxed{
>
\left({\lambda\over8\,3^{1/8}}-o(1)\right)D^{1/4}.}
\tag{LHD.19}
\]

All retained bars then have pairwise disjoint endpoints and therefore cross pairwise.

This is four times the leading coefficient obtained by first keeping two-bar force bundles and only then applying the host/death split.

For the ninety-percent parameter choice

\[
\lambda={9c_0\over10}=5.085\times10^{-6},
\tag{LHD.20}
\]

the full linear branch size is

\[
\boxed{
>{2.5425\times10^{-6}}D-o(D),}
\tag{LHD.21}
\]

and the endpoint-disjoint branch coefficient is

\[
\boxed{
{\lambda\over8\,3^{1/8}}
\approx5.54065123188\times10^{-7}.}
\tag{LHD.22}
\]

As the fixed parameter losses tend to zero, the coefficient in (LHD.19) approaches

\[
\boxed{
{c_0\over8\,3^{1/8}}
\approx6.15627914653\times10^{-7}.}
\tag{LHD.23}
\]

---

## 4. Coherent-sign version

The linear nested rail contains a coherent-transverse-sign subrail of size

\[
>{\lambda\over2}D-o(D).
\tag{LHD.24}
\]

Apply the same one-turn argument to that subsequence. One obtains either a coherent-sign cross-host rail or a coherent-sign one-death plateau of size

\[
\boxed{
>{\lambda\over4}D-o(D).}
\tag{LHD.25}
\]

After partner-degree thinning, the coherent-sign endpoint-disjoint branch has size

\[
\boxed{
>
\left({\lambda\over16\,3^{1/8}}-o(1)\right)D^{1/4}.}
\tag{LHD.26}
\]

For (LHD.20), these constants are

\[
1.27125\times10^{-6}
\tag{LHD.27}
\]

at linear scale and

\[
2.77032561594\times10^{-7}
\tag{LHD.28}
\]

at endpoint-disjoint `D^(1/4)` scale.

---

## 5. Low-stress version

First impose the existing one-sided KKT quantile with fixed `0<sigma<1`. The surviving nested rail has size

\[
>(1-\sigma)\lambda D-o(D)
\tag{LHD.29}
\]

and every birth cell obeys

\[
B_i\le {1\over\sigma\lambda D},
\qquad
0<|G_i|\le {1\over\sigma\lambda}.
\tag{LHD.30}
\]

Applying the linear host/death dichotomy after this pruning gives a branch of size

\[
\boxed{
>{(1-\sigma)\lambda\over2}D-o(D).}
\tag{LHD.31}
\]

A coherent-sign branch has size

\[
\boxed{
>{(1-\sigma)\lambda\over4}D-o(D).}
\tag{LHD.32}
\]

and the corresponding endpoint-disjoint coefficients are

\[
{(1-\sigma)\lambda\over8\,3^{1/8}}
\quad\text{and}\quad
{(1-\sigma)\lambda\over16\,3^{1/8}}.
\tag{LHD.33}
\]

For the ninety-percent choice and `sigma=1/2`, the unsigned linear branch density is

\[
1.27125\times10^{-6},
\tag{LHD.34}
\]

while the coherent-sign linear branch density is

\[
6.35625\times10^{-7}.
\tag{LHD.35}
\]

The corresponding endpoint-disjoint coefficients are

\[
2.77032561594\times10^{-7}
\quad\text{and}\quad
1.38516280797\times10^{-7}.
\tag{LHD.36}
\]

The stress control is attached to the **birth cells**. No stress bound at the common death interface `b_*` is inferred.

---

## 6. The plateau branch is forced to be a macroscopic separator

Fix any constant threshold `T`. The joint-cost quantities used in the deep-cell construction dominate the raw switching count:

\[
J_j\ge N_j.
\tag{LHD.37}
\]

If the plateau alternative in (LHD.12) occurs, then by (LHD.14)

\[
J_{b_*}\ge N_{b_*}>{\lambda\over2}D-o(D).
\tag{LHD.38}
\]

Hence for all sufficiently large `D`, `b_*` is not `T`-good for any fixed `T`; it is one of the threshold-bad separator interfaces removed when constructing fixed-depth exact-phase neighborhoods.

Thus the plateau normal form has a precise interpretation:

```text
linear density of deep exact-phase births
+ strictly nested supports
+ all selected supports terminate at one interface
=> that one death interface carries Theta(D) raw switching complexity
=> it is necessarily a macroscopic separator outside every fixed-threshold good class.
```

This is not a contradiction. It shows exactly where the complexity must concentrate if the host branch fails.

On a growing-depth diagonal, any selected birth whose clean neighborhood reaches `b_*` would contradict the threshold-good neighborhood condition. Therefore the common death interface stays outside each retained clean birth neighborhood. The argument does not claim a global metric separation beyond that index-distance statement.

---

## 7. Order alone cannot eliminate the plateau

The strengthened cardinality statement should not be mistaken for a combinatorial contradiction. For every `N` there is an abstract weak-thrackle support pattern with

\[
i_1<\cdots<i_N<k<b_*
\tag{LHD.39}
\]

and

\[
b_1=\cdots=b_N=b_*.
\tag{LHD.40}
\]

Then

\[
\{i_1+1,\ldots,b_*\}
\supsetneq\cdots\supsetneq
\{i_N+1,\ldots,b_*\}
\tag{LHD.41}
\]

is a perfectly valid nested interval chain. Partner incidences may be assigned to distinct vertices of `R_{b_*}` in weak boundary order, or several may share a partner vertex. Thus the laminar/order axioms alone allow arbitrarily long death plateaus.

A closure of this branch must therefore use information not present in the one-turn support order, such as the metric near-diameter geometry, the KKT/resultant structure at `b_*`, the common inverse-`D` train grid, or terminal/face complexity.

---

## 8. Frontier effect

The exact-antipodal no-TB1 branch now has a linear-scale normal form before any endpoint-degree loss:

```text
HOST:
  > (lambda/2) D - o(D) nested bars
  from one fixed pre-hub host arc
  to one fixed hubward host arc
  with weak partner ties allowed

or

PLATEAU:
  > (lambda/2) D - o(D) distinct bars
  all in one post-hub switching set X_{b_*}
  so N_{b_*} > (lambda/2)D - o(D)
  and b_* is a macroscopic threshold-bad separator.
```

The useful next attacks are different in the two branches. The host branch should be compared directly with near-central diameter endpoint order and the common inverse-`D` train grid. The plateau branch should be compared with the exact post-hub cut resultant and terminal complexity at its single macroscopic separator. Endpoint thinning can now be postponed until a later step and costs only one partner-degree factor.

No C-II or Level-I closure is claimed.

**Disposition:** lifted the host/death-plateau dichotomy from `Omega(D^(1/4))` endpoint-disjoint rails to the full linear nested force rail, and identified failure of the host branch with a single `Theta(D)` raw switching interface. C-II and Level I remain open.
