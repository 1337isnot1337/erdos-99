> Generated reading edition · [exact source](../../research/target_c_convex_route_split_energy_sharpening_2026-09-15.md) · source SHA-256 `fa44216bf2f9ba25dc97618d3a78524c777195f9dd1e5ca559f2d5aeed8b7619`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 11 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "25cd8a850c2bf356188f2b4d4226b3e26d47e90b", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_convex_route_split_energy_sharpening_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9f2f4b8a6feecee845a01d659a4e9df3e8531d635b6d59bb409317e51ee6f28c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — split-route excess is already paid by the angular energy budget

**Date:** 2026-09-15  
**Repository base:** branch `sol/2026-09-15-c2-convex-routes` after the convex-route theorem  
**Status:** proof-only sharpening; theorem-state authority unchanged  
**Scope:** same low-`t` Type-II scope as the convex-route theorem  
**LEVEL I STATUS:** `STILL OPEN`

For one convex Section-63 route, the principal-angle `beta`-good edges may have two blocks. The convex-route theorem therefore loses one additional straight occurrence on every split route. A naive estimate would pay that split-route count from the directional-energy budget a second time.

That double payment is unnecessary. A split route already contains a central reversal whose energy exceeds the ordinary per-bad-edge baseline by at least

```math
2\cos\beta.
```

Consequently the exact global energy satisfies

```math
\boxed{
d_{out}
\ge
(1-\cos\beta)A_\beta+2\cos\beta\,r,
}
```

where `A_beta` is the total number of angularly bad edges and `r` is the number of split routes. For `beta<=pi/6`, the extra cost `2cos(beta)` is much larger than the baseline `1-cos(beta)`, so

```math
\boxed{A_\beta+r\le {d_{out}\over1-\cos\beta}.}
```

Thus the convex-route straight-occurrence bound is as strong as if every route had only one good block:

```math
\boxed{S_\beta\ge x_B-{d_{out}\over1-\cos\beta}.}
```

At `beta=pi/6`, after signed edge-injective selection and joint low-`t` optimization, this gives

```math
\boxed{1.3020617081548316\ldots D-o(D)}
```

distinct signed inward penetration contacts.

---

## 1. Per-route baseline energy

Fix one nontrivial convex Section-63 route `W_i`. Let its monotonically lifted edge angles relative to the loaded-hull chord be

```math
\vartheta_1\le\cdots\le\vartheta_\ell
```

(or reverse all inequalities). Fix

```math
0<\beta<\pi/2
```

and write

```math
c_\beta:=1-\cos\beta.
```

Let `A_i` be the number of edges whose principal angular distance from the chord direction is at least `beta`. Every such edge has

```math
1-\cos\vartheta_j\ge c_\beta.
```

Therefore every route, split or not, has the baseline bound

```math
E_i:=\sum_j(1-\cos\vartheta_j)
\ge c_\beta A_i.
\tag{SE.1}
```

---

## 2. A split route has an extra `2 cos(beta)` beyond baseline

Assume the principal-angle good set has two nonempty blocks. After adding an integer multiple of `2pi` to the lift, the first good block lies near angle `0` and the second near `2pi`; the bad angles between them cross the central region around `pi`.

### Lemma SE.1 — split-route excess energy

For a split route,

```math
\boxed{
E_i
\ge
c_\beta A_i+2\cos\beta.
}
\tag{SE.2}
```

### Proof

There are two cases.

**Case 1: one edge enters the central interval.**  Suppose some edge angle satisfies

```math
\vartheta_j\in[\pi-\beta,\pi+\beta].
```

Then

```math
1-\cos\vartheta_j
\ge1+\cos\beta.
```

The ordinary bad-edge baseline assigned only

```math
c_\beta=1-\cos\beta
```

to this edge. Its excess above baseline is therefore at least

```math
(1+\cos\beta)-(1-\cos\beta)=2\cos\beta.
```

Every other bad edge still contributes at least its own baseline `c_beta`, proving (SE.2).

**Case 2: the monotone angle sequence jumps across the central interval.**  Then there are consecutive edge angles

```math
\vartheta_a<\pi-\beta,
\qquad
\vartheta_{a+1}>\pi+\beta.
```

For a simple convex polygon every exterior turn is strictly less than `pi`; collinear consecutive sides have turn zero. Hence

```math
\vartheta_{a+1}-\vartheta_a<\pi.
```

Put

```math
x=\pi-\vartheta_a>\beta,
\qquad
y=\vartheta_{a+1}-\pi>\beta.
```

Then `x+y<pi`. The two edge energies satisfy

```math
\begin{aligned}
(1-\cos\vartheta_a)+(1-\cos\vartheta_{a+1})
&=2+\cos x+\cos y\\
&=2+2\cos{(x+y)\over2}\cos{(x-y)\over2}\\
&>2.
\end{aligned}
```

Both edges are bad, so their combined baseline is

```math
2c_\beta=2-2\cos\beta.
```

Thus their excess over baseline is strictly greater than

```math
2-(2-2\cos\beta)=2\cos\beta.
```

Again all remaining bad edges contribute their ordinary baselines. This proves (SE.2). `square`

---

## 3. Global joint energy inequality

Let `r_i` be one for a split route and zero otherwise, and let

```math
r=\sum_i r_i,
\qquad
A_\beta=\sum_iA_i.
```

The distinguished routes partition the outer walk and their directional energies sum exactly to `d_out`. Summing (SE.1)--(SE.2) gives

```math
\boxed{
d_{out}
\ge c_\beta A_\beta+2\cos\beta\,r.
}
\tag{SE.3}
```

For the straight-event range `beta<=pi/6`,

```math
2\cos\beta>1-\cos\beta=c_\beta.
```

Therefore

```math
c_\beta(A_\beta+r)
\le c_\beta A_\beta+2\cos\beta\,r
\le d_{out},
```

hence

```math
\boxed{
A_\beta+r
\le {d_{out}\over1-\cos\beta}.
}
\tag{SE.4}
```

The convex-route theorem gives

```math
S_\beta\ge x_B-A_\beta-r.
```

Insert (SE.4):

```math
\boxed{
S_\beta
\ge x_B-{d_{out}\over1-\cos\beta}.
}
\tag{SE.5}
```

This is stronger than separately estimating `A_beta` and `r`; the same central energy that makes a route split already pays its extra combinatorial loss.

---

## 4. Signed edge-injective physicalization

The merged signed penetration theorem applies to these straight occurrences and proves the occurrence-to-selected-contact map is globally injective in the present low-detour Type-II scope. Therefore

```math
\boxed{
E_\perp(\beta)
\ge x_B-{d_{out}\over1-\cos\beta}.
}
\tag{SE.6}
```

Every selected contact points to the core side of its route and has signed inward component

```math
>\sin(\pi/3-\beta).
```

At `beta=pi/6`, this component is strictly greater than `1/2`.

---

## 5. Type-II normalized form

On a convergent low-`t` Type-II subsequence,

```math
{x_B\over D}
=\pi+\delta-t-\kappa+o(1),
\qquad
\delta={d_{out}\over D}.
```

Divide (SE.6) by `D`:

```math
\boxed{
\liminf {E_\perp(\beta)\over D}
\ge
\pi-t-\kappa-
\left({1\over1-\cos\beta}-1\right)\delta.
}
\tag{SE.7}
```

At

```math
\beta={\pi\over6},
```

we have

```math
{1\over1-\sqrt3/2}-1
=3+2\sqrt3.
\tag{SE.8}
```

Thus

```math
\boxed{
\liminf {E_\perp\over D}
\ge
\pi-t-\kappa-(3+2\sqrt3)\delta.
}
\tag{SE.9}
```

---

## 6. Joint low-`t` endpoint

The network squeeze is

```math
2\delta+{\kappa\over2}\le R(t).
```

Since

```math
3+2\sqrt3>4,
```

the penalty `kappa+(3+2sqrt3)delta` is maximized at

```math
\delta={R(t)\over2},
\qquad
\kappa=0.
```

Therefore

```math
\boxed{
\liminf {E_\perp\over D}
\ge
\pi-t-\left({3\over2}+\sqrt3\right)R(t).
}
\tag{SE.10}
```

At the current endpoint

```math
t=t_{42}=1.8208886379794447041\ldots,
\qquad
R(t)=0.00576795,
```

this gives

```math
\boxed{
{E_\perp\over D}
\ge
1.30206170815483162854568\ldots-o(1).
}
\tag{SE.11}
```

This is the strongest current local physical count from the convex-pocket/signed-penetration stack.

---

## 7. Remaining obstruction

The improvement removes occurrence multiplicity and almost all angular-tail bookkeeping from the low-`t` boundary. It still does not close C-II. A macroscopic one-rhombus-thick boundary strip can carry a linear population of distinct signed inward contacts on a small train family.

The remaining problem is therefore genuinely train/strip occupancy: either the selected contacts consume many distinct stopped-train/interface resources, or a few macroscopic strips absorb them and must be coupled to the near-extremal Woodall diameter thrackle or a source-preserving multi-train shear.

No theorem-state promotion is requested.
