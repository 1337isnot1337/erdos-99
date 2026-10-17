<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "42712e303506ef5892dd8d39e7139d8795f22c4f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_monotone_corridor_linear_outer_currency_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "59114a19f6dc61494220dcaeb6239944aec12518e49f79ebc440f5a7ed0c695d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the original monotone FREE corridor forces linear outer/external currency

**Date:** 2026-09-18  
**Status:** proved candidate awaiting audit; proof-only strengthening of the all-inactive FREE branch  
**Scope:** every non-anchored all-inactive FREE reflection module  
**Dependencies:** FREE-blocker outer-face localization; near-halfdepth outer corridor; outer-corridor total-slack telescope; canonical Sections 63 and 67; the one-run pocket-width routing lemma  
**Certificate:** `research/verify_target_c_tooth_reflection_monotone_corridor_linear_outer_currency_2026_09_18.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The recent one-FREE routing theorem is applied to the two-sided LOWER/UPPER activation ancestry. That path is support-monotone only on each maximal lower run, so its pocket-width bound pays the OP pocket budget once per lower run. The reflected-pocket sharpening improves the resulting square-root capacity, but does not remove that run multiplicity.

The older parent ancestry contains a stronger object. Every non-anchored FREE module has one original-source chain

\[
C=(z_0,z_1,\ldots,z_\ell)
\]

such that:

1. `z_0` lies strictly outside the force hull `F`;
2. every `z_j` is an old contact- and diameter-isolate in the original outer contact face;
3. the complete chain is strictly monotone in the module support direction `N`;
4. every parent edge is shorter than `sqrt(3)` and obeys the old-face localization theorem;
5. with `sigma_j=|z_j-z_{j+1}|-1`, the total slack satisfies
   \[
   \sum_j\sigma_j\le t_D<h_*+D^{-1/3},
   \qquad h_*={\sqrt{303}\over52};
   \]
6. its support-depth span
   \[
   S_D:=a_{z_\ell}-a_{z_0}
   \]
   satisfies, for every `omega_D -> infinity` with `omega_D=o(D^(1/4))`,
   \[
   S_D\ge {D\over2}-3^{1/8}D^{3/4}-\omega_D\sqrt D-O(\sqrt D).
   \tag{MC.0}
   \]

Because the **whole parent chain** is support-monotone, each convex OP pocket can spend its directional width only once over the entire ancestry. This removes the upper-gate/run factor completely.

Put

\[
x_B=b-q,
\qquad
Z_{\rm ext}=|A\setminus F|.
\]

The finite conclusions are

\[
\boxed{
2x_B+2Z_{\rm ext}\ge S_D+1-t_D,
}
\tag{MC.1}
\]

and the sharper route-count version

\[
\boxed{
x_B+3Z_{\rm ext}\ge S_D+1-t_D.}
\tag{MC.2}
\]

Consequently

\[
\boxed{
x_B+Z_{\rm ext}\ge
{D\over4}-{3^{1/8}\over2}D^{3/4}
- {\omega_D\over2}\sqrt D-O(\sqrt D),}
\tag{MC.3}
\]

\[
\boxed{x_B+3Z_{\rm ext}\ge
{D\over2}-3^{1/8}D^{3/4}
-\omega_D\sqrt D-O(\sqrt D).}
\tag{MC.4}
\]

In particular,

\[
\boxed{
\liminf {x_B+Z_{\rm ext}\over D}\ge{1\over4}.}
\tag{MC.5}
\]

If `Z_ext=o(D)`, the stronger second inequality gives

\[
\boxed{x_B\ge(1/2-o(1))D.}
\tag{MC.6}
\]

If instead `x_B=o(D)`, (MC.1) forces

\[
\boxed{Z_{\rm ext}\ge(1/4-o(1))D.}
\tag{MC.7}
\]

Thus the square-root one-FREE outer/external frontier is not a terminal scale for a non-anchored FREE module: the original monotone parent ancestry itself forces a **linear** payment in canonical source-wide currencies.

---

## 1. The full parent ancestry uses each OP pocket width at most once

Write

\[
g_j:=N\cdot(z_j-z_{j+1})>0.
\tag{MC.8}
\]

Strict support monotonicity gives

\[
S_D=\sum_{j=0}^{\ell-1}g_j.
\tag{MC.9}
\]

Partition the chain edges into

- `E_in`: both endpoints lie in `F`;
- `E_ext`: at least one endpoint lies outside `F`.

For an edge `e in E_in`, convexity puts the whole segment in `F`. The same short-edge planarity/face-localization argument used in the existing pocket-width routing theorem applies: an old fully inactive parent edge cannot properly cross a positive unit-contact edge or pass through a positive contact vertex. Thus it lies in the closure of one Section-67 OP outer pocket; a segment on an added hull side is assigned to that side's unique interior pocket, exactly as in the canonical OP convention.

For a fixed pocket `P`, all `N`-projection intervals contributed by **all** edges of `C` assigned to `P` have pairwise disjoint interiors. This is global, because `N dot z_j` is strictly monotone along the entire parent chain. Hence the total support gain spent in `P` is at most its directional width `w_N(P)`.

The existing convex-pocket estimate is

\[
2w_N(P)\le \operatorname{per}(P),
\]

and the Section-67 perimeter ledger gives

\[
\sum_P\operatorname{per}(P)\le4x_B.
\]

Therefore

\[
\boxed{
G_{\rm in}:=\sum_{e\in E_{\rm in}}g_e\le2x_B.
}
\tag{MC.10}
\]

The key point is the absence of the old `U+1` multiplier.

---

## 2. Exact external-edge count on the parent path

Let

\[
z_C:=|V(C)\setminus F|\le Z_{\rm ext}
\]

and let `r_C` be the number of maximal nonempty blocks of consecutive chain vertices lying in `F`. The parent path starts at `z_0 outside F`. Since it is a simple source-vertex path,

\[
\boxed{r_C\le z_C.}
\tag{MC.11}
\]

More precisely, the number of parent edges with at least one endpoint outside `F` is

\[
\boxed{|E_{\rm ext}|=z_C+r_C-1.}
\tag{MC.12}
\]

Indeed, if the inside blocks have sizes `s_1,...,s_{r_C}`, then the number of inside-inside edges is `sum_i(s_i-1)`. Subtracting this from the total `|V(C)|-1` path edges gives (MC.12).

For every parent edge,

\[
g_j\le|z_j-z_{j+1}|=1+\sigma_j.
\]

The total-slack theorem therefore gives

\[
\boxed{
G_{\rm ext}:=\sum_{e\in E_{\rm ext}}g_e
\le z_C+r_C-1+t_D.
}
\tag{MC.13}
\]

Combining (MC.9), (MC.10), and (MC.13),

\[
S_D\le2x_B+z_C+r_C-1+t_D
\le2x_B+2Z_{\rm ext}-1+t_D,
\]

which proves (MC.1).

---

## 3. The exact outer-route ledger sharpens `2x_B` to `x_B+r_C`

Each nondegenerate OP pocket `P` has one added force-hull chord of length `s_P` and one old outer-contact route of `ell_P` unit edges. Hence

\[
s_P\le\ell_P,
\qquad
\operatorname{per}(P)=s_P+\ell_P,
\]

so

\[
\boxed{w_N(P)\le{\operatorname{per}(P)\over2}\le\ell_P.}
\tag{MC.14}
\]

Canonical Section 63 gives the exact route identity

\[
\boxed{x_B=\sum_i(\ell_i-1).}
\tag{MC.15}
\]

Let `p_C` be the number of distinct OP pockets containing at least one internal parent edge. A maximal inside block cannot switch from one OP pocket to a distinct OP pocket without meeting or crossing their positive/contact-loaded boundary. The parent vertices are fully inactive and the short-edge face-localization theorem forbids such a crossing. Thus each inside block lies in one pocket, and

\[
\boxed{p_C\le r_C.}
\tag{MC.16}
\]

If the chain leaves and later revisits the same pocket, global support monotonicity still makes that pocket pay its width only once. Therefore

\[
\begin{aligned}
G_{\rm in}
&\le\sum_{P\ {m visited}}w_N(P)\\
&\le\sum_{P\ {m visited}}\ell_P\\
&=\sum_{P\ {m visited}}(\ell_P-1)+p_C\\
&\le x_B+r_C.
\end{aligned}
\tag{MC.17}
\]

Together with (MC.13),

\[
S_D\le x_B+z_C+2r_C-1+t_D
\le x_B+3Z_{\rm ext}-1+t_D,
\]

which proves (MC.2).

The useful exact chain-currency form is

\[
\boxed{
2x_B+z_C+r_C\ge S_D+1-t_D,
\qquad
x_B+z_C+2r_C\ge S_D+1-t_D.
}
\tag{MC.18}
\]

---

## 4. Linear normalized frontier

Insert (MC.0) and `t_D=O(1)` into (MC.1)--(MC.2). This proves (MC.3)--(MC.4).

If along a subsequence

\[
{x_B\over D}\to\xi,
\qquad
{Z_{\rm ext}\over D}\to\zeta,
\]

then

\[
\boxed{
\xi\ge
\max\left\{0,{1\over4}-\zeta,{1\over2}-3\zeta\right\}.
}
\tag{MC.19}
\]

The two nonzero affine pieces meet at

\[
\boxed{\zeta=\xi={1\over8}.}
\tag{MC.20}
\]

For `zeta<1/8`, the exact pocket-count law (MC.2) is stronger. For `zeta>1/8`, the global pocket-perimeter law (MC.1) is stronger.

This also shows why the reflected-pocket square-root minimax is not the final one-FREE regime. A hypothetical sequence with both `x_B=O(sqrt(D))` and `Z_ext=O(sqrt(D))` violates (MC.5) outright. The reflected-pocket theorem remains a valid capacity theorem; its joint square-root endpoint is simply inaccessible once the original parent-chain monotonicity is retained.

---

## 5. Direct rewrites in canonical Target-C currencies

Section 63 gives

\[
q-x_B=Q+2k,
\qquad k=d_H+s_Z.
\tag{MC.21}
\]

Therefore

\[
\boxed{
q-Q-2k+Z_{\rm ext}\ge {D\over4}-o(D),
}
\tag{MC.22}
\]

\[
\boxed{
q-Q-2k+3Z_{\rm ext}\ge {D\over2}-o(D).
}
\tag{MC.23}
\]

The same section writes

\[
x_B=m+u_B,
\tag{MC.24}
\]

where `m` is the number of nonunit loaded force-hull sides and `u_B` is the integer outer-route surplus. Hence

\[
\boxed{m+u_B+Z_{\rm ext}\ge {D\over4}-o(D),}
\tag{MC.25}
\]

\[
\boxed{m+u_B+3Z_{\rm ext}\ge {D\over2}-o(D).}
\tag{MC.26}
\]

There is also a metric version. Put

\[
\lambda_D:=b-\operatorname{per}(F),
\qquad
\Theta_D:=\pi D-q.
\]

The exact metric split is

\[
x_B=(\operatorname{per}(F)-q)+\lambda_D,
\]

and Cauchy's perimeter-diameter bound gives `per(F)<=pi D`. Thus

\[
x_B\le\Theta_D+\lambda_D.
\]

Equations (MC.3)--(MC.4) imply

\[
\boxed{
\lambda_D+\Theta_D+Z_{\rm ext}\ge {D\over4}-o(D),
}
\tag{MC.27}
\]

\[
\boxed{
\lambda_D+\Theta_D+3Z_{\rm ext}\ge {D\over2}-o(D).
}
\tag{MC.28}
\]

In particular,

\[
Z_{\rm ext}=o(D),\quad \pi D-q=o(D)
\quad\Longrightarrow\quad
\boxed{b-\operatorname{per}(F)\ge(1/2-o(1))D.}
\tag{MC.29}
\]

Likewise,

\[
Z_{\rm ext}=o(D),\quad m=o(D)
\quad\Longrightarrow\quad
\boxed{u_B\ge(1/2-o(1))D.}
\tag{MC.30}
\]

These are existing canonical outer-walk currencies, not new geometric surrogates.

---

## 6. What remains open

This theorem removes a scale mismatch in the FREE branch. The split two-sided ancestry only forced square-root `x_B/Z_ext` currency because it repeatedly paid the same pocket-width budget after every upper interruption. The original parent chain is globally monotone and reaches half-depth, so the same OP geometry forces linear payment.

It does **not** prove that `Z_ext=o(D)`, `pi D-q=o(D)`, or `m=o(D)` in every C-II survivor. Linear external population and linear loaded-hull/outer-route defect remain compatible with the promoted scalar ledger. Therefore C-II is not closed.

The remaining seam is now:

```text
all-inactive non-anchored FREE module
  -> one old support-monotone outer-face chain reaches D/2-o(D) depth
  -> either that chain uses linear external population,
     or the canonical loaded outer walk pays linear x_B
  -> if Z_ext=o(D), x_B >= D/2-o(D)
  -> if also pi D-q=o(D), actual metric outer-walk detour >= D/2-o(D).
```

The next closure step should attack this **linear recipient side**. A useful theorem would upper-bound `Z_ext/D` in the reflection full-core branch, or couple the linear `m+u_B` payment to the promoted Sections 122--123 aggregate detour/loaded-hull ledger strongly enough to exclude the remaining profiles.

**Disposition:** reused the globally monotone original FREE parent ancestry in the OP pocket-width ledger, proved the exact chain-block laws (MC.18), and upgraded one-module outer/external currency from square-root to linear scale. The authoritative theorem-state ledger is unchanged; C-II remains open.
