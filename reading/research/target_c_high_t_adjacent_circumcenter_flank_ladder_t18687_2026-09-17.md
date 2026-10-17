> Generated reading edition · [exact source](../../research/target_c_high_t_adjacent_circumcenter_flank_ladder_t18687_2026-09-17.md) · source SHA-256 `f7ea0b36ed872aa9f93bb80a2524d738d3a2b253a65cb71c7e3043964cef4949`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "de88290ee236c3e95963954e5d010d48ca662824", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_high_t_adjacent_circumcenter_flank_ladder_t18687_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c1279f8dd8c9a03e2dc335f10aad801633adaa8d1ec116f078b6af9897c83b26"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — every low-terminal adjacent row pair has one common circumcenter-bracketing train ladder

**Date:** 2026-09-17  
**Status:** proof-only high-`t` geometric strengthening; no canonical promotion claimed  
**Scope:** the selected high-`t` O--O path through `t=(q-k)/D<=1.8687`; in particular every fixed-good KKT/force interface  
**Dependencies:** high-`t` crossing-neighbor floor; adjacent-strip terminal-topology bound; triangle-free complete-train crossing graph; exact train-step metric bound; full-source circumradius/midpoint localization  
**Certificate:** `research/verify_target_c_high_t_adjacent_circumcenter_flank_ladder_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The global synchronized-grid argument can force one common transverse family to bracket the source circumcenter, but it pays a large block-averaging loss. Locally, no such loss is needed.

Every selected high-`t` O--O row has more than

$$
rD-o(D),\qquad r=0.6536,
$$

crossing trains. At an adjacent interface whose train-terminal symmetric-difference cost is `o(D)`, the two rows therefore have more than `rD-o(D)` **common** crossing trains. Those common trains are pairwise noncrossing and occur in one common order along both rows.

Because

$$
r>{1\over\sqrt3},
$$

the source circumdisk cannot place all these crossings on one side of its center in the exact train-monotone coordinate. More strongly, for every fixed

$$
0\le\mu<\mu_*:= {\sqrt3\,r-1\over2},
$$

the same common ordered train family contains linear prefixes and suffixes lying at row-normal coordinate less than `-mu D` and greater than `+mu D` on **both adjacent rows simultaneously**.

Numerically,

$$
\boxed{\mu_*=0.0660342039\ldots .}
$$

Thus every fixed-good high-`t` KKT cusp, exact-force cell, or strong-TB1 interface sits inside a two-row train ladder with common transverse flanks that may be placed almost `0.066D` to either side of the source circumcenter coordinate.

For example:

- at `mu=0.05`, each common flank has density `>0.0185147`;
- at `mu=0.06`, each common flank has density `>0.0069676`.

The same midpoint argument as in the global bracketing theorem then gives a local geometric consequence. Any actual diameter bar that crosses one of the two rows but meets it outside the central corridor between the common flanks must make a fixed angle with that row phase:

$$
\sin\theta>2\mu-o(1).
$$

At `mu=0.06`, failure of central threading forces `sin(theta)>0.12-o(1)`.

---

## 1. Adjacent rows share essentially the full `0.6536D` crossing population

Let

$$
\tau_i,\tau_{i+1}
$$

be adjacent selected O--O path rows. Write `Gamma_j` for the family of complete trains crossing `tau_j`.

The complete-rectangle theorem gives, uniformly over the selected path,

$$
\boxed{|\Gamma_j|>rD-o(D),\qquad r=0.6536.}
\tag{AF.1}

The adjacent-strip terminal-topology theorem gives

\[
|\Gamma_i\triangle\Gamma_{i+1}|\le L_i,
\tag{AF.2}

where `L_i` is the stopped-train terminal face-side count in the intervening region. Therefore

\[
\begin{aligned}
|\Gamma_i\cap\Gamma_{i+1}|
&={|\Gamma_i|+|\Gamma_{i+1}|-|\Gamma_i\triangle\Gamma_{i+1}|\over2}\\
&>rD-{L_i\over2}-o(D).
\end{aligned}
\tag{AF.3}

In particular, whenever

\[
L_i=o(D),
\tag{AF.4}

the common family

\[
C_i:=\Gamma_i\cap\Gamma_{i+1}
$$

satisfies

$$
\boxed{|C_i|>rD-o(D).}
\tag{AF.5}

Every fixed-good interface used in the current high-`t` KKT/force theorems has `L_i=O(1)` (for example `L_i<H=4,436,000` in the fixed-good normalization), so (AF.5) applies to all of them.

---

## 2. The common transverse family is internally noncrossing and has one order

Take two distinct trains `b,c in C_i`. Both cross `tau_i`. If `b` and `c` crossed each other, the three complete trains

\[
\tau_i,b,c
$$

would form a triangle in the complete-train crossing graph. That graph is triangle-free. Hence `C_i` is pairwise noncrossing.

The two rows are also noncrossing, and every row crosses every train in `C_i` exactly once. The standard two-shore pseudoline order lemma therefore gives one column order

$$
b_1,b_2,\ldots,b_M
\tag{AF.6}

common to both rows, up to one global reversal.

For each row `tau_j`, `j=i,i+1`, choose the oriented track-edge unit vector `u_j` so that

\[
h_j(x):=\det(u_j,x-o)
\tag{AF.7}

strictly increases along the centerline in the common column order (AF.6). This sign choice is made separately for the two projective row directions and does not change any projective phase statement.

---

## 3. Circumdisk capacity leaves common flanks on both rows

Let `z_{j,s}` be the crossing-rhombus center of `tau_j` and column `b_s`. The exact train-step metric inequality gives

\[
h_j(z_{j,s+1})-h_j(z_{j,s})>{\sqrt3\over2}.
\tag{AF.8}

The full source hull lies in

\[
B(o,R_D),
\qquad
R_D<{D\over2}+3^{1/4}\sqrt D.
\tag{AF.9}

Hence every crossing center satisfies

\[
-R_D\le h_j(z_{j,s})\le R_D.
\tag{AF.10}

Fix `mu>=0`. The number of crossings on one row with

\[
h_j(z_{j,s})\ge-\mu D
$$

is at most

$$
1+{R_D+\mu D\over\sqrt3/2}
=\left({1+2\mu\over\sqrt3}+o(1)\right)D.
\tag{AF.11}

Since `M>|C_i|>rD-o(D)`, the number with `h_j<-mu D` is therefore more than

\[
\left(r-{1+2\mu\over\sqrt3}\right)D-o(D).
\tag{AF.12}

The same estimate holds above `+mu D`.

Put

\[
\boxed{q(\mu):=r-{1+2\mu\over\sqrt3}.}
\tag{AF.13}

Then `q(mu)>0` exactly when

\[
\mu<\mu_*:={\sqrt3 r-1\over2}.
\tag{AF.14}

Because `h_j` is increasing in the **same** column order on both rows, the crossings below `-mu D` form an initial segment on each row. Each initial segment has at least `(q(mu)-o(1))D` labels, so their common first `(q(mu)-o(1))D` labels work simultaneously. The same argument with the final segments above `+mu D` gives a common suffix.

Thus for every fixed `mu<mu_*` there are common column subfamilies

\[
C_i^-(\mu),C_i^+(\mu)\subset C_i
$$

with

$$
\boxed{|C_i^-(\mu)|,|C_i^+(\mu)|>
(q(\mu)-o(1))D}
\tag{AF.15}

such that for both `j=i,i+1`,

\[
\boxed{h_j(z_{j,b})<-\mu D\quad(b\in C_i^-(\mu)),}
\tag{AF.16}

\[
\boxed{h_j(z_{j,b})>\mu D\quad(b\in C_i^+(\mu)).}
\tag{AF.17}

This is one common two-row circumcenter bracket, not two unrelated rowwise extractions.

---

## 4. Explicit margins

With `r=0.6536`,

\[
\boxed{\mu_*=0.0660342039135\ldots .}
\tag{AF.18}

At `mu=0.05`,

\[
\boxed{q(0.05)=0.0185147038914\ldots .}
\tag{AF.19}

At `mu=0.06`,

\[
\boxed{q(0.06)=0.00696769850762\ldots .}
\tag{AF.20}

So every fixed-good interface has, on both adjacent rows simultaneously,

```text
>0.0069676 D common columns crossing below the -0.06 D row-normal level
+ >0.0069676 D common columns crossing above the +0.06 D row-normal level,
```

all in one common transverse order.

The constants come from the full per-row crossing floor, so they are substantially larger than the flanks obtained after global block synchronization.

---

## 5. Local central-threading versus angular-separation alternative

For one row `tau_j`, let `K_j(mu)` be the centerline subarc from the last crossing in `C_i^-(mu)` to the first crossing in `C_i^+(mu)`. Strict monotonicity of `h_j` implies

\[
\{x\in\tau_j:|h_j(x)|\le\mu D\}\subset K_j(\mu).
\tag{AF.21}

Take any actual diameter chord `e` whose selected-cut support contains `tau_j`. Its endpoints lie on opposite sides of the proper centerline crosscut, so the straight chord meets `tau_j`; call one intersection `x`.

Write

\[
e=\{m+td:-D/2\le t\le D/2\},
\qquad |d|=1.
$$

The common source midpoint bound gives

$$
|m-o|<L_D=O(D^{3/4})=o(D).
\tag{AF.22}

If `x` lies outside `K_j(mu)`, then

\[
|h_j(x)|>\mu D.
$$

But

$$
|h_j(x)|
\le L_D+{D\over2}|\det(u_j,d)|.
$$

Therefore

\[
\boxed{
|\det(u_j,d)|>2\mu-{2L_D\over D},
}
\tag{AF.23}

or, in projective-angle notation,

\[
\boxed{
\sin\theta(e,\tau_j)>2\mu-o(1).
}
\tag{AF.24}

For `mu=0.06`,

\[
\boxed{
 e\text{ misses the common central ladder corridor on }\tau_j
\Longrightarrow
\sin\theta(e,\tau_j)>0.12-o(1).
}
\tag{AF.25}

Conversely any diameter direction with `sin theta < 2mu-o(1)` must thread the row between the two common flank families.

---

## 6. Direct application to the current force/blocker interfaces

The fixed-good robust fork, the deep exact-force cells, and the strong-TB1 interfaces all use adjacent selected O--O rows with `L_i=O(1)`. Therefore Theorem AF applies at every one of those retained interfaces without a further density loss.

On a pre-hub one-sided interface, every switching diameter is born between `tau_i` and `tau_{i+1}` and runs hubward, so it crosses the hubward adjacent row. Thus every selected exact-force diagonal or strong-TB1 blocker inherits the local alternative (AF.24) against a **common** pair of linear transverse flank families shared by both adjacent rows.

This does not yet rule out the fixed-angular-separation branch. It does remove the possibility that a row-near switching blocker can remain geometrically unlocalized inside an otherwise macroscopic train scaffold: every such blocker is forced through the central corridor of a two-row ladder whose two flank populations are linear in `D`.

---

## 7. Frontier effect

The previous finite-cusp and deep-force statements used a common inverse-`D` near-triangular column family of density `0.0783` or smaller. That family is too sparse to force circumcenter straddling by metric capacity alone. The full adjacent-row common neighborhood is different: after the `o(D)` terminal symmetric-difference loss it still has density `0.6536`, above the exact one-sided circumdisk threshold `1/sqrt(3)`.

Hence every fixed-good high-`t` interface now has two simultaneous transverse scaffolds:

1. an inverse-`D` near-triangular family used for phase/KKT arguments;
2. a much larger common two-row family with fixed-fraction circumcenter flanks.

A closing argument may therefore split each switching diameter into an exact geometric alternative: central threading of the large ladder, or a fixed angular separation as large as `arcsin(0.12)-o(1)` while retaining positive linear flank density.

The remaining step is to make those two scaffolds interact with the positive force cone / nested support order strongly enough to forbid both alternatives or produce a strict diameter descent.

**Disposition:** proved a common circumcenter-bracketing two-row train ladder at every low-terminal adjacent interface, with explicit `0.05D` and `0.06D` margins and a local central-threading versus fixed-angle diameter dichotomy. C-II and Level I remain open.