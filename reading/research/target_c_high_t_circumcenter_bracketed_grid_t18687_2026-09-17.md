> Generated reading edition · [exact source](../../research/target_c_high_t_circumcenter_bracketed_grid_t18687_2026-09-17.md) · source SHA-256 `d192acea4a1baec86de8e18b047618a68efdf6fcaa0f9161eedec739c1447225`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "b14b92de015f61aaed196974180231d449868c20", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_circumcenter_bracketed_grid_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "eee75c07b8f409ae6757cca313668528c54b8c46604f91d6bcb63d54c710dde5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — a synchronized train block brackets the source circumcenter on every row

**Date:** 2026-09-17  
**Status:** proof-only high-`t` geometric strengthening; no canonical promotion claimed  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch with `t=(q-k)/D<=1.8687`  
**Dependencies:** optimized interior-block synchronization; canonical exact train-step metric bound; canonical full-source circumradius/midpoint localization; common-order signed train grid  
**Certificate:** `research/verify_target_c_high_t_circumcenter_bracketed_grid_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The latest interior-block theorem gives, for every fixed integer `N>=8`, synchronized families

```math
E_N,\qquad A_N,\qquad B_N
```

with

```math
|E_N|,|A_N|>a_ND-o(D),
\qquad
|B_N|>b_ND-o(D),
```

where

```math
a_N={0.0002038\over N},
\qquad
b_N=0.6536-{3.0605\over N-3},
\tag{CB.1}
```

such that `E_N x A_N` is complete in exact selected-cut support incidence and `A_N x B_N` is a complete common-order strict-rhombus train rectangle.

This note uses the full-source circumcenter `o` to choose a different parameter regime from the earlier `N=8` and `N=14` specializations. Once

```math
b_N>{1\over\sqrt3},
```

the common transverse shore is too large to fit on only one side of `o` in the exact train-monotone coordinate of any row. Because the crossing order is common, this produces **two common column flanks**, one uniformly before the circumcenter coordinate on every row and one uniformly after it.

With a fixed metric margin `mu>0`, the same argument gives flanks whose crossing centers lie at least `mu D` from the circumcenter coordinate. Combining this with the source-wide midpoint localization of every actual diameter chord converts the remaining topological support seam into an exact location-or-angle dichotomy: a synchronized diameter either crosses a row inside the central train corridor, or its direction is bounded away from that row axis by a fixed angle.

The clean concrete choice `mu=0.01`, `N=99` gives

```math
|E_{99}|,|A_{99}|>2.05858\times10^{-6}D-o(D),
```

```math
|B_{99}|>0.6217197D-o(D),
```

and two **common** transverse flank families, each of size

```math
>0.0328225D-o(D),
```

whose row-crossing centers lie respectively below `h_{u_a}(o)-0.01D` and above `h_{u_a}(o)+0.01D` for every `a in A_{99}`.

This is the first current synchronized scaffold in which the global source circumcenter is metrically bracketed on every retained row by the same two linear column families.

---

## 1. One-sided capacity in the circumdisk

Let `K` be the full source hull and let `o` be the canonical full-source circumcenter. The canonical source-hull estimate gives

```math
K\subset B(o,R_D),
\qquad
{D\over2}\le R_D<{D\over2}+\eta_D,
\qquad
\eta_D=3^{1/4}\sqrt D.
\tag{CB.2}
```

Fix a row train `a` and a unit vector `u_a` parallel to its track edges. Orient its centerline so that

```math
h_a(x):=\det(u_a,x-o)
```

strictly increases. The exact train-step metric lemma gives, for any two consecutive selected crossing-rhombus centers `z,z'` on this oriented row,

```math
h_a(z')-h_a(z)>{\sqrt3\over2}.
\tag{CB.3}
```

All crossing-rhombus centers lie in `K`, hence

```math
-R_D\le h_a(z)\le R_D.
\tag{CB.4}
```

Fix `0<=mu<1/2`. Any crossing center satisfying

```math
h_a(z)\ge-\mu D
```

lies in a coordinate interval of length at most

```math
R_D+\mu D.
```

By (CB.3), the number of such centers is at most

```math
1+{R_D+\mu D\over\sqrt3/2}
\le
\left({1+2\mu\over\sqrt3}+o(1)\right)D.
\tag{CB.5}
```

The symmetric estimate holds for centers with `h_a(z)<=mu D`.

Therefore, if a common transverse family `B` has

```math
|B|>bD-o(D),
```

then every row contains at least

```math
\boxed{
\left(b-{1+2\mu\over\sqrt3}\right)D-o(D)
}
\tag{CB.6}
```

crossings from `B` with `h_a(z)<-mu D`, and the same number with `h_a(z)>mu D`, provided the displayed coefficient is positive.

For `mu=0`, this says that any row family with transverse density above `1/sqrt(3)` must straddle the source circumcenter coordinate on every row.

---

## 2. Common order upgrades rowwise straddling to two common column flanks

Apply Section 1 to the synchronized rectangle `A_N x B_N`. Orient all rows by the signed common-order convention. The `B_N` columns then occur in one order

```math
b_1,b_2,\ldots,b_M
\tag{CB.7}
```

along every oriented row, and `h_a` is strictly increasing in that order.

Put

```math
q_N(\mu):=
 b_N-{1+2\mu\over\sqrt3}.
\tag{CB.8}
```

Assume `q_N(mu)>0`, and let

```math
Q_D=\lfloor(q_N(\mu)-o(1))D\rfloor
```

be any asymptotically valid lower count from (CB.6). On every row, at least `Q_D` columns have crossing center below `-mu D`. Since those crossings form an initial segment of the common order (CB.7), the **same first `Q_D` columns** work for every row. Likewise the same last `Q_D` columns lie above `+mu D` on every row.

Thus there are common subfamilies

```math
B_N^-,B_N^+\subset B_N
```

with

```math
\boxed{
|B_N^-|,|B_N^+|>
\left(q_N(\mu)-o(1)\right)D
}
\tag{CB.9}
```

such that for every `a in A_N`,

```math
\boxed{
h_a(z_{ab})<-\mu D\quad(b\in B_N^-),}
\tag{CB.10}
```

```math
\boxed{
h_a(z_{ab})>\mu D\quad(b\in B_N^+).}
\tag{CB.11}
```

The two flank families are global: they do not depend on the row.

Let `C_a(mu)` denote the closed row-centerline subarc between the last `B_N^-` crossing and the first `B_N^+` crossing. By strict monotonicity of `h_a`, every point of the row centerline with

```math
|h_a|\le\mu D
```

lies on `C_a(mu)`.

---

## 3. Parameter choices

### 3.1 Zero-margin product optimum

For `mu=0`,

```math
q_N(0)=0.6536-{3.0605\over N-3}-{1\over\sqrt3}.
\tag{CB.12}
```

Positivity starts at `N=44`. The product

```math
a_N q_N(0)
```

is maximized over integers `N>=44` at

```math
\boxed{N=85.}
\tag{CB.13}
```

At `N=85`,

```math
\boxed{a_{85}=2.3976470588\ldots\times10^{-6},}
\tag{CB.14}
```

```math
\boxed{b_{85}=0.6162768292\ldots,}
\tag{CB.15}
```

and

```math
\boxed{q_{85}(0)=0.0389265600\ldots .}
\tag{CB.16}
```

Hence a synchronized row/diameter family of density `2.3976e-6` has two common circumcenter-side column flanks of density `0.03892` each.

### 3.2 A fixed one-percent metric margin

Take

```math
\mu={1\over100}.
```

Then

```math
q_N(0.01)=
0.6536-{3.0605\over N-3}-{1.02\over\sqrt3}.
\tag{CB.17}
```

The product `a_N q_N(0.01)` is maximized over the positive integer range at

```math
\boxed{N=99.}
\tag{CB.18}
```

There

```math
\boxed{a_{99}=2.0585858585\ldots\times10^{-6},}
\tag{CB.19}
```

```math
\boxed{b_{99}=0.6217197916\ldots,}
\tag{CB.20}
```

and

```math
\boxed{q_{99}(0.01)=0.0328225170\ldots .}
\tag{CB.21}
```

Therefore the high-`t` survivor contains synchronized families

```math
E_{99},A_{99},B_{99}^-,B_{99}^+
```

with

```math
\boxed{|E_{99}|,|A_{99}|>2.05858\times10^{-6}D-o(D),}
\tag{CB.22}
```

```math
\boxed{|B_{99}^-|,|B_{99}^+|>0.0328225D-o(D),}
\tag{CB.23}
```

and the uniform metric bracketing (CB.10)--(CB.11) with `mu=0.01`.

The parent transverse shore itself has

```math
|B_{99}|>0.6217197D-o(D).
\tag{CB.24}
```

---

## 4. Diameter support now has a geometric location-or-angle dichotomy

Take any actual diameter bar `e in E_N`, and any synchronized row `a in A_N`. Exact selected-cut support means that the endpoints of `e` lie in opposite components of the source cut by the O--O crosscut `a`. The straight segment `e` therefore meets the row crosscut geometrically. Let `x` be one such intersection point.

Write the diameter chord as

```math
e=\{m+td:-D/2\le t\le D/2\},
\qquad |d|=1,
```

where `m` is its midpoint. The canonical full-source midpoint theorem gives

```math
|m-o|<L_D,
\qquad
L_D=\sqrt{D\eta_D+\eta_D^2}=O(D^{3/4})=o(D).
\tag{CB.25}
```

If `x` lies outside the central row corridor `C_a(mu)`, then by (CB.10)--(CB.11) and monotonicity,

```math
|h_a(x)|>\mu D.
\tag{CB.26}
```

On the other hand,

```math
\begin{aligned}
|h_a(x)|
&=|\det(u_a,m-o)+t\det(u_a,d)|\\
&\le L_D+{D\over2}|\det(u_a,d)|.
\end{aligned}
\tag{CB.27}
```

Combining (CB.26)--(CB.27) gives

```math
\boxed{
|\det(u_a,d)|
>2\mu-{2L_D\over D}.
}
\tag{CB.28}
```

Equivalently, with `theta(e,a)` the projective angle between the diameter direction and the row track-edge direction,

```math
\boxed{
\sin\theta(e,a)>2\mu-o(1).
}
\tag{CB.29}
```

Thus every synchronized diameter-row pair satisfies an exact alternative:

```text
CENTRAL THREADING:
    the straight diameter chord meets the row inside C_a(mu),
    between the common B_N^- and B_N^+ flank blocks;

or

FIXED ANGULAR SEPARATION:
    sin(theta(e,a)) > 2 mu - o(1).
```

For `mu=0.01`, failure of central threading forces

```math
\sin\theta(e,a)>0.02-o(1).
\tag{CB.30}
```

This is a direct geometric refinement of the prior statement that `E_N x A_N` is only topological support incidence.

---

## 5. Common row phase makes the angular alternative global

The selected O--O rows already lie in one shrinking projective phase window. Therefore there is a common projective row direction `[u_*]` with

```math
\max_{a\in A_N}d_{\mathbb{RP}^1}([u_a],[u_*])=o(1).
\tag{CB.31}
```

Consequently, for any fixed `mu>0`, a diameter direction satisfying

```math
\sin d_{\mathbb{RP}^1}([d],[u_*])<2\mu-o(1)
```

must centrally thread **every** row of the synchronized block for which it has exact support incidence. Conversely, if it misses the central corridor on even one synchronized row, its direction is bounded away from the common row phase by the fixed `2mu` sine threshold up to `o(1)`.

This does not yet force either alternative to dominate. It does remove one ambiguity in the current frontier: once the common transverse shore is taken above the `1/sqrt(3)` circumdisk capacity threshold, a synchronized diameter cannot avoid a metrically central common grid corridor without paying a definite directional separation from the entire row phase.

---

## 6. Frontier effect

The earlier `N=8` and `N=14` synchronized rectangles optimized diameter density and raw grid product. They left the train patch free to sit entirely on one side of the source circumcenter in the row monotone coordinate. The `N=85/99` regime removes that escape.

The current high-`t` survivor now has an unconditional synchronized scaffold with

```text
Theta(D) actual diameters E_N;
Theta(D) selected rows A_N;
>0.62 D common transverse trains B_N in the 1%-margin specialization;
two common >0.0328 D column flanks on opposite sides of the source circumcenter coordinate on every row;
exact diameter support across every synchronized row;
and a location-or-angle dichotomy for the straight diameter intersection.
```

The remaining closure step is sharper than before. One must now show either

1. a positive-density diameter subfamily is forced into the common central corridors, where the ordered near-triangular train geometry can act directly on the straight chords; or
2. the fixed angular-separation alternative is incompatible with the one-sided nested diameter rail / exact-force / strong-TB1 structure.

No such final incompatibility is claimed here. C-II and Level I remain open.

**Disposition:** pushed the synchronized transverse shore past the exact `1/sqrt(3)` one-sided circumdisk capacity threshold, extracted two common circumcenter-bracketing column flanks (including a `1% D` metric-margin version), and converted selected-cut incidence into a central-threading versus fixed-angle dichotomy for every synchronized diameter-row pair.
