<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "f041aec552b0617a9c11942722085039e27b721b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_free_module_linear_inactive_chain_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "0b93e2dce928fabf4b611a5b8a0a8202f883683170d5e7d7d8c774e11d3c7853"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a non-anchored FREE reflection module forces a linear inactive near-unit chain

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only strengthening of the FREE-MODULE repair branch  
**Scope:** slow-scale reflection modules after ANCHORED, `Q-DIAMETER`, and `CORE-GATE` have been converted to actual source-diameter anchors  
**Dependencies:** free-module rigid repair; inactive-guard absorption; C65 full diameter visibility; canonical farthest-blocker support width; full-source circumradius bound; `q`-diameter absorption; core-gate diameter anchoring  
**Certificate:** `research/verify_target_c_tooth_reflection_free_module_linear_inactive_chain_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The finite gate-jam theorem can be pushed much farther. A finite gate network made only from old fully inactive vertices is not itself a terminal obstruction: once the upper blockers have been cleared, every such gate component can be expanded by an arbitrarily small factor, opening all newly created unit contacts while preserving every other strict distance. Therefore a genuinely non-anchored FREE module cannot clear after any bounded or submacroscopic inward propagation.

Fix any constant

\[
0<\lambda<\frac12.
\]

Then every FREE module which does **not** convert to the exact source-diameter braid forces a simple chain of original fully inactive vertices

\[
z_0,z_1,\ldots,z_\ell
\]

with

\[
\boxed{z_0\in U,}
\tag{LC.1}
\]

\[
\boxed{
1<|z_{j+1}-z_j|
<1+h_*+o(1)
=1.3347479843\ldots+o(1),
}
\tag{LC.2}

and support-depth penetration

\[
\boxed{
a_{z_\ell}>\lambda D,
\qquad
a_{z_0}=O(\sqrt D),
}
\tag{LC.3}

where

\[
a_v:=H-N\cdot v
\]

is depth from the module's canonical blocker support line.

Consequently

\[
\boxed{
\ell\ge
\left(
{\lambda\over1+h_*}-o(1)
\right)D.
}
\tag{LC.4}

Since `lambda` may be any fixed constant below `1/2`, the coefficient can be taken arbitrarily close to

\[
\boxed{
{1\over2(1+h_*)}
=0.374602551093811\ldots .
}
\tag{LC.5}

Thus the surviving FREE obstruction is no longer a bounded gate jam. It contains a **linear-length chain of old contact- and diameter-isolated source points** running from the blocker-side boundary layer to any prescribed support depth strictly below `D/2`.

---

## 1. Run the absorption process without a finite gate cutoff

Fix one FREE module. Let

\[
U=\{z\in A:|z-q|>D\}
\]

and let `N` be the exact canonical support normal at the farthest blocker head `y`. Write

\[
H=h_A(N),
\qquad
a_v=H-N\cdot v,
\]

and use the usual clearing time

\[
t_D=\delta+D^{-1/3}<\frac12.
\tag{LC.6}
\]

All original blockers move with velocity `-N`. Whenever a moving point reaches a still-fixed source point at unit distance:

1. if the fixed point belongs to the old nonisolated contact core, `CORE-GATE` applies and the module has already entered the exact-braid branch;
2. otherwise C65 makes the fixed point fully inactive, so absorb it and continue it with velocity `-N`.

Likewise, if an unmoved original point satisfies `|q-r|=D`, the `q`-diameter theorem converts the module to the exact-braid branch.

Hence on the branch studied below, **every** absorbed point is an original fully inactive rattler.

Assign each newly absorbed vertex one parent: choose any moving vertex which met it at its first absorption event. This produces an acyclic parent forest rooted in the original blocker set `U`, because parent join times are strictly earlier than child join times.

---

## 2. Upper-distance safety extends to every cap of fixed fractional depth below `D/2`

The earlier absorbed-guard arguments used the convenient depth scale `O(sqrt(D))`. The same geometry has a much larger validity range.

The canonical width theorem gives

\[
W_K(N)>D-h_*,
\tag{LC.7}
\]

while the full-source circumradius bound gives one center `o` with

\[
K\subset B(o,R_D),
\qquad
R_D={D\over2}+O(\sqrt D).
\tag{LC.8}
\]

Let

\[
c=N\cdot o.
\]

Since the opposite support value is at least `c-R_D`, (LC.7) implies

\[
\boxed{
H-c\ge {D\over2}-O(\sqrt D).
}
\tag{LC.9}

Now consider original source points with

\[
a_v\le\lambda D+O(1),
\qquad
0<\lambda<\frac12.
\]

Their `N`-coordinate relative to `o` is at least

\[
N\cdot(v-o)
\ge
\left({1\over2}-\lambda\right)D-O(\sqrt D).
\tag{LC.10}
\]

Inside the disk (LC.8), the diameter of this cap is therefore at most

\[
\boxed{
\left(
2\sqrt{\lambda-\lambda^2}+o(1)
\right)D.
}
\tag{LC.11}

Because `lambda<1/2`,

\[
\rho_\lambda:=2\sqrt{\lambda-\lambda^2}<1.
\tag{LC.12}
\]

So the cap has a fixed positive subdiameter margin:

\[
\operatorname{diam}(\text{cap})
\le(\rho_\lambda+o(1))D<D.
\tag{LC.13}
\]

This is the key extension.

### Moving point versus fixed source point

Suppose an absorbed original point `p` has

\[
a_p\le\lambda D
\]

and has moved by `tau N`, with

\[
0\le\tau<t_D<\frac12.
\]

If for a fixed source point `v`

\[
|p-\tau N-v|\ge D,
\tag{LC.14}
\]

while originally `|p-v|<D`, then squaring gives

\[
N\cdot(p-v)<{\tau\over2}<\frac14.
\tag{LC.15}
\]

Hence

\[
a_v-a_p=N\cdot(p-v)<\frac14,
\]

so `v` also lies in the depth-`lambda D+O(1)` cap. Equation (LC.13) then gives

\[
|p-v|\le(\rho_\lambda+o(1))D,
\]

and adding the displacement `<1/2` still leaves the moved distance strictly below `D`, contradicting (LC.14).

Thus no absorbed point of depth at most `lambda D` can create a new upper-diameter equality or violation with a fixed source point.

### Two moving points

If two absorbed points both have original support depth at most `lambda D`, their original distance is at most `(rho_lambda+o(1))D` by the same cap estimate. Their relative displacement differs from the original one by less than one, so their current distance is also strictly below `D` for large `D`.

Therefore:

\[
\boxed{
\text{as long as every absorbed vertex has }a_v\le\lambda D,
\text{ the entire repair is strictly upper-safe.}
}
\tag{LC.16}

No bound on the **number** of absorbed vertices is needed.

---

## 3. Absorbed guards remain safely away from `q` on the lower side

Every newly absorbed guard was originally outside `U`, hence

\[
|q-v|\le D.
\]

Also

\[
N\cdot(v-q)=L-a_v.
\]

If `a_v\le\lambda D` with `lambda<1/2`, then

\[
N\cdot(v-q)
\ge(1-\lambda)D-o(D)>1.
\tag{LC.17}

Moving `v` by `-N` strictly decreases its distance from `q`, but by only `O(1)`. Consequently throughout the repair

\[
oxed{1<|q-v(s)|<D}
\tag{LC.18}

for every absorbed guard, unless the module had already entered the separate `Q-DIAMETER` exact-anchor branch before absorption.

The original blockers are handled by the existing clearing estimate: at `t_D` they satisfy `1<|q-z(t_D)|<D`.

---

## 4. A terminal inactive gate network can be removed locally

Assume, for contradiction, that the repair reaches `t_D` without a core gate, without a `q`-diameter anchor, and without ever absorbing a point of support depth greater than `lambda D`.

By (LC.16), all upper distances are strict. By the event construction, every lower equality involving a moved old-inactive point is one of the recorded gate edges. All other lower distances are strict.

The source is finite. Let `G_g` be the final gate graph. Every nontrivial component of `G_g` consists entirely of vertices that were fully inactive in the original source and is disjoint from the old contact core.

For one nontrivial component with current vertex positions `p_1,...,p_m`, let `c_G` be its centroid and apply the arbitrarily small expansion

\[
p_j\longmapsto
c_G+(1+\varepsilon)(p_j-c_G).
\tag{LC.19}
\]

for `epsilon>0`.

Every internal gate edge has length exactly one before (LC.19), so afterwards its length is `1+epsilon>1`. Every other pair involving this component had strict lower and upper slack. By finiteness, choose `epsilon` sufficiently small that all those strict inequalities remain in `(1,D)`. Do this independently for every nontrivial gate component, with successively smaller perturbations if necessary.

Thus **all** newly created gate contacts can be opened while preserving feasibility and while keeping all repaired blockers strictly below diameter from `q`.

Now replace `x` by `q` and use the existing arbitrarily small base-opening perturbation of `q`. Since there is no `q`-diameter equality, all nonbase `q`-distances are strict. The perturbation removes every one of the

\[
d=\deg_C(x)\ge3
\]

old contacts at `x`, and no new gate contact remains.

The resulting source is triangle-free, unit-separated, and has diameter at most `D`, but has strictly fewer unit contacts than the canonical triangle-free global minimizer. Global optimality forces its diameter to be `D`, contradicting primary contact minimality.

Therefore the assumed terminal repair is impossible.

We have proved:

\[
\boxed{
\text{before clearing, some absorbed inactive vertex }v
\text{ must satisfy }a_v>\lambda D.
}
\tag{LC.20}

---

## 5. A deep absorbed vertex forces a linear parent chain

Let `z_ell` be the first absorbed vertex with

\[
a_{z_\ell}>\lambda D.
\]

Follow its parent ancestry back to a blocker root

\[
z_0\in U.
\]

The chain is simple because join times strictly increase.

Suppose `z_{j+1}` is absorbed when its parent `z_j` has already moved for a time `tau_j<=t_D`. At the event,

\[
|z_j-\tau_jN-z_{j+1}|=1.
\tag{LC.21}
\]

Therefore

\[
\begin{aligned}
a_{z_{j+1}}-a_{z_j}
&=N\cdot(z_j-z_{j+1})\\
&=N\cdot(z_j-\tau_jN-z_{j+1})+\tau_j\\
&\le1+t_D.
\end{aligned}
\tag{LC.22}

The blocker root satisfies

\[
a_{z_0}=O(\sqrt D).
\tag{LC.23}
\]

Summing (LC.22),

\[
\lambda D-O(\sqrt D)
< a_{z_\ell}-a_{z_0}
\le\ell(1+t_D).
\]

Since

\[
t_D\le h_*+o(1),
\]

we obtain

\[
\boxed{
\ell\ge
\left(
{\lambda\over1+h_*}-o(1)
\right)D,
}
\tag{LC.24}

which is (LC.4).

Finally, every parent-child pair was an old strict noncontact. Equation (LC.21) gives

\[
1<|z_{j+1}-z_j|
\le1+\tau_j
\le1+t_D
<1+h_*+o(1),
\]

proving (LC.2).

Every chain vertex is fully inactive in the original canonical source, so

\[
\boxed{
\deg_C(z_j)=\deg_H(z_j)=0
\qquad(0\le j\le\ell).
}
\tag{LC.25}

---

## 6. Quantitative choices

The theorem holds for every fixed `lambda<1/2`.

For example, `lambda=1/4` gives

\[
\boxed{
\ell\ge
(0.1873012755\ldots-o(1))D.
}
\tag{LC.26}

Taking `lambda=0.49` gives

\[
\boxed{
\ell\ge
(0.3671105001\ldots-o(1))D.
}
\tag{LC.27}

As `lambda` approaches `1/2` from below, the coefficient approaches

\[
{1\over2(1+h_*)}
=0.374602551093811\ldots .
\]

The barrier at `lambda=1/2` is geometric: the circumdisk cap of depth `D/2` can itself have diameter `D`, so the strict upper-safety argument no longer follows from cap geometry alone.

---

## 7. Source-wide reflection reduction

The slow-scale reflection family has

\[
M_D>
(c_*-o(1)){D^{1/4}\over\kappa_D},
\qquad
c_*=0.129220199818177\ldots .
\tag{LC.28}

Every selected module is now in one of two effective classes:

1. `EXACT-BRAID`: ANCHORED, `Q-DIAMETER`, or CORE-GATE, hence one localized actual source diameter;
2. `LINEAR-INACTIVE-CHAIN`: for every fixed `lambda<1/2`, a fully inactive near-unit parent chain satisfying (LC.1)--(LC.4).

One class therefore contains at least

\[
\boxed{
\left({c_*\over2}-o(1)\right){D^{1/4}\over\kappa_D}
}
\tag{LC.29}

modules.

If the exact class wins, the selected source diameters are vertex-disjoint and pairwise crossing in the common `O(D/kappa_D)` central core.

If the chain class wins, each retained module individually forces a macroscopic inactive chain from its blocker-side cap to depth `lambda D`. Different deep chains may merge and are **not** claimed to remain globally vertex-disjoint. Their initial prefixes remain disjoint as long as their gate-path radius is `o(kappa_D D^(3/4))`, by the existing slow-scale module separation.

For subpolynomial divergent `kappa_D`, the number of modules in the surviving class is `D^(1/4-o(1))`.

---

## 8. Frontier effect

The bounded inactive-jam endpoint has disappeared. The reflection branch is now

```text
slow-scale shallow-tooth module
    |
    +-- actual source-diameter anchor
    |      -> exact central crossing braid
    |
    +-- no source-diameter anchor
           -> absorb every newly hit inactive rattler
           -> upper safety persists through any fixed fractional
              support depth lambda D with lambda < 1/2
           -> terminal finite gate networks can be opened locally
           -> therefore a fully inactive near-unit chain must penetrate
              linearly far into the source
```

This ties the reflection branch directly to the repository's macroscopic inactive-rattler geometry. The next seam is no longer a finite three- or four-edge jam: it is a linear chain of fully inactive source points, with every consecutive original distance below `1.334748+o(1)`, crossing a fixed positive fraction of the source width.

**Disposition:** proved that every non-anchored FREE reflection module forces a linear-depth, linear-length inactive near-unit chain. C-II remains open.
