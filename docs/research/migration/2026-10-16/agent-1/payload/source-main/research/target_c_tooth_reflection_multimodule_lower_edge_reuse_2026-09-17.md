# Target C-II — many FREE modules force a superlinear near-unit matching or heavy corridor reuse

**Date:** 2026-09-17  
**Status:** proved candidate awaiting promotion; proof-only multi-module consequence of the two-sided FREE repair  
**Scope:** any selected family of all-inactive non-anchored FREE reflection modules in one source  
**Dependencies:** two-sided inactive gate absorption; two-sided outer-face localization; short inactive-edge planarity; slow-scale module-normal separation when the ordered-normal corollary is invoked  
**Certificate:** `research/verify_target_c_tooth_reflection_multimodule_lower_edge_reuse_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The one-module FREE theorem already gives a linear population of inverse-`D` near-unit lower gates. The unresolved multi-module escape was that many reflection modules might reuse the same inactive corridor. This note turns that ambiguity into a quantitative fork.

Fix

\[
h_*={\sqrt{303}\over52}=0.334747984337100\ldots
\]

and any fixed

\[
K>h_*.
\]

Suppose `m=m_D` selected reflection modules all survive in the all-inactive non-anchored FREE branch. Choose one near-opposite activation ancestry for each module. For module `i`, let `G_i(K)` be the set of lower ancestry edges whose original source length satisfies

\[
1<|e|\le 1+{K\over D}.
\]

Put

\[
\alpha_K:=1-{h_*\over K}>0.
\tag{MR.1}
\]

Then, uniformly over the selected modules,

\[
\boxed{|G_i(K)|\ge(\alpha_K-o(1))D.}
\tag{MR.2}
\]

Every edge in every `G_i(K)` has old fully inactive endpoints in the original outer contact face. All such edges belong to one common plane source-pair graph, and that inverse-`D` graph has maximum degree at most six for all sufficiently large `D`.

For a distinct original source pair `e`, define its module multiplicity

\[
\mu(e):=|\{i:e\in G_i(K)\}|.
\tag{MR.3}
\]

Let `R` be any integer with

\[
1\le R<m.
\]

Then at least one of the following holds.

### MULTI-MATCHING

The original source contains a vertex-disjoint matching of old fully inactive outer-face pairs of size

\[
\boxed{
\left({\alpha_K\over22}-o(1)\right){mD\over R}
}
\tag{MR.4}
\]

with

\[
\boxed{1<|x-y|\le1+{K\over D}.}
\tag{MR.5}
\]

### HEAVY-REUSE

There are at least

\[
\boxed{
\left({\alpha_K\over2}-o(1)\right)D
}
\tag{MR.6}
\]

distinct original inverse-`D` near-unit edges `e` satisfying

\[
\boxed{\mu(e)\ge R+1.}
\tag{MR.7}
\]

Thus the failure of the global matching conclusion forces a linear-size common inactive network in which every retained edge is reused by more than `R` separate reflection modules.

If the modules come from the ordered slow-scale extraction and their canonical normals have consecutive angular gap at least

\[
\gamma_D=(2-o(1))\kappa_DD^{-1/4},
\tag{MR.8}
\]

then every heavy edge in (MR.6) is a lower gate for two modules whose normals differ by at least

\[
\boxed{R\gamma_D.}
\tag{MR.9}
\]

Moreover, one fixed pair of selected modules with normal separation at least `R gamma_D` shares at least

\[
\boxed{
(\alpha_K-o(1)){D\over m^2}
}
\tag{MR.10}
\]

distinct edges of length at most `1+K/D`.

The balanced choice

\[
R=\lfloor\sqrt m\rfloor
\tag{MR.11}
\]

therefore gives either

\[
\boxed{
\left({\alpha_K\over22}-o(1)\right)D\sqrt m
}
\tag{MR.12}
\]

vertex-disjoint inverse-`D` pairs, or a linear family of edges each reused by more than `sqrt(m)` modules together with a pair of modules sharing

\[
\boxed{(\alpha_K-o(1))D/m^2}
\tag{MR.13}
\]

such edges.

For `K=1`,

\[
\alpha_1=0.6652520156628998\ldots,
\]

so the matching coefficient in (MR.12) is

\[
\boxed{\alpha_1/22=0.0302387279846773\ldots,}
\tag{MR.14}
\]

while the heavy-edge population in (MR.6) is at least

\[
\boxed{(0.332626007831450\ldots-o(1))D.}
\tag{MR.15}
\]

For a residual slow-scale FREE family

\[
m=\Theta(D^{1/4}/\kappa_D),
\]

with `kappa_D` subpolynomial, the balanced fork reads

\[
\boxed{
\text{either }\Omega(D^{9/8}/\sqrt{\kappa_D})\text{ disjoint }(1+K/D)\text{-pairs},
}
\tag{MR.16}
\]

or

\[
\boxed{
\Omega(D)\text{ distinct heavy edges and two modules sharing }\Omega(\kappa_D^2D^{1/2})\text{ of them}.}
\tag{MR.17}
\]

In the latter case the selected shared-module pair can be required to have normal gap

\[
\boxed{\Omega(\sqrt{\kappa_D}\,D^{-1/8}).}
\tag{MR.18}
\]

This does not close C-II. It does remove the unquantified statement that different FREE modules may simply merge into one planar inactive network. Either the network supplies a superlinear vertex-disjoint near-unit population, or a linear set of actual source pairs is reused by a diverging number of ordered modules, and one well-separated module pair has a growing common edge set. The latter is now the precise corridor-sharing obstruction.

---

## 1. The inverse-`D` source-pair graph has degree at most six

The earlier short-edge theorem proves that the source-pair graph on edges shorter than `sqrt(2)` is plane. For inverse-`D` edges one gets a sharper local degree bound.

Let `v` be a source point and let `x,y` be two distinct neighbors with

\[
1\le r:=|v-x|\le L,
\qquad
1\le s:=|v-y|\le L,
\]

where `L<sqrt(2)`. If `theta` is the smaller angle between the rays `vx` and `vy`, unit separation gives

\[
1\le|x-y|.
\]

By the law of cosines,

\[
\cos\theta
\le {r^2+s^2-1\over2rs}.
\tag{MR.19}
\]

On `1<=r,s<sqrt(2)`, the right side is strictly increasing in each variable because

\[
{\partial\over\partial r}
{r^2+s^2-1\over2rs}
={r^2-s^2+1\over2r^2s}>0,
\]

and symmetrically in `s`. Hence

\[
\cos\theta
\le1-{1\over2L^2}.
\tag{MR.20}
\]

Define

\[
L_7:=\left(2(1-\cos(2\pi/7))\right)^{-1/2}
=1.152382435481243\ldots .
\tag{MR.21}
\]

If `L<L_7`, then (MR.20) gives

\[
\theta>{2\pi\over7}.
\]

Seven neighbors around one center would have seven cyclic angular gaps summing to `2pi`, each strictly greater than `2pi/7`, impossible. Therefore

\[
\boxed{\Delta(P_{\le L}(A))\le6\qquad(L<L_7).}
\tag{MR.22}
\]

For fixed `K`, `L=1+K/D<L_7` for all sufficiently large `D`. Also `L<sqrt(2)`, so the same graph is plane by the short-edge theorem.

The degree bound is sharp asymptotically: six points equally spaced on a circle of radius `1+epsilon` around `v` are unit-separated for every `epsilon>0`, and all six radial edges tend to unit length as `epsilon->0`.

A graph of maximum degree six has a matching of size at least `|E|/11`: a greedy matching edge deletes itself and at most ten adjacent edges.

---

## 2. Every module contributes `alpha_K D` good lower edges

For one all-inactive FREE ancestry, the two-sided theorem gives

\[
|E_{\rm low}|\ge D-O(\sqrt D)
\tag{MR.23}
\]

and

\[
\sum_{e\in E_{\rm low}}(|e|-1)
\le h_*+D^{-1/3}.
\tag{MR.24}
\]

The number of lower edges with excess above `K/D` is therefore at most

\[
{D\over K}(h_*+D^{-1/3})
={h_*\over K}D+O(D^{2/3}).
\tag{MR.25}
\]

Subtracting (MR.25) from (MR.23) proves (MR.2).

The two-sided outer-face theorem says every endpoint is an old fully inactive outer-face source point. Since every good edge has length at most `1+K/D`, Section 1 puts all modules' good lower edges into one common plane graph of maximum degree six.

---

## 3. Incidence counting gives the matching-or-reuse fork

Let

\[
\mathcal E=\bigcup_{i=1}^mG_i(K)
\]

be the set of distinct good original source pairs and put

\[
I:=\sum_{e\in\mathcal E}\mu(e)
=\sum_{i=1}^m|G_i(K)|.
\]

By (MR.2),

\[
\boxed{I\ge(\alpha_K-o(1))mD.}
\tag{MR.26}
\]

Split the distinct edges into

\[
\mathcal E_{\rm light}:=\{e:\mu(e)\le R\},
\qquad
\mathcal E_{\rm heavy}:=\{e:\mu(e)\ge R+1\}.
\]

### Light incidence is at least half

If

\[
\sum_{e\in\mathcal E_{\rm light}}\mu(e)\ge I/2,
\]

then

\[
|\mathcal E_{\rm light}|
\ge {I\over2R}.
\]

The degree-six matching bound gives a vertex-disjoint matching of size at least

\[
{I\over22R}
\ge
\left({\alpha_K\over22}-o(1)\right){mD\over R},
\]

which is (MR.4)--(MR.5).

### Heavy incidence is more than half

Otherwise

\[
\sum_{e\in\mathcal E_{\rm heavy}}\mu(e)>I/2.
\]

Since every edge occurs in at most all `m` modules,

\[
|\mathcal E_{\rm heavy}|
>{I\over2m}
\ge
\left({\alpha_K\over2}-o(1)\right)D.
\]

Every such edge has multiplicity at least `R+1`, proving (MR.6)--(MR.7).

This counting is on distinct original source pairs. Repeated appearances of the same geometric edge in different module ancestries increase `mu(e)`; they do not artificially increase the matching side.

---

## 4. Ordered normals sharpen heavy reuse

Assume now that the `m` modules are inherited from the slow-scale ordered family, so consecutive selected normals differ by at least `gamma_D` from (MR.8).

A heavy edge belongs to at least `R+1` module good-edge sets. Its first and last participating modules in the normal order therefore have at least `R` selected normal gaps between them. This proves (MR.9).

For every heavy edge, assign the edge to that extremal participating module pair. There are at most

\[
{m\choose2}
\]

possible assigned pairs. Therefore one fixed pair receives at least

\[
{|\mathcal E_{\rm heavy}|\over {m\choose2}}
\ge
(\alpha_K-o(1)){D\over m^2}
\]

assignments. Every assigned edge belongs to the good-edge sets of both modules, and the pair has normal separation at least `R gamma_D`. This proves (MR.10).

---

## 5. Balanced slow-scale form

Take `R=floor(sqrt(m))`. Then (MR.4) becomes (MR.12), while (MR.6)--(MR.10) give the heavy conclusions (MR.13).

If

\[
m=\Theta(D^{1/4}/\kappa_D),
\qquad
\gamma_D=(2-o(1))\kappa_DD^{-1/4},
\]

then

\[
D\sqrt m=\Theta(D^{9/8}/\sqrt{\kappa_D}),
\]

\[
{D\over m^2}=\Theta(\kappa_D^2D^{1/2}),
\]

and

\[
R\gamma_D
=\Theta(\sqrt{\kappa_D}\,D^{-1/8}).
\]

This proves (MR.16)--(MR.18).

The light branch is a genuine multi-module amplification: it improves the one-module `Theta(D)` inverse-`D` matching to a superlinear matching whenever the selected module count diverges and reuse stays below the balanced threshold. The heavy branch is the complementary normal form: a linear number of actual near-unit source pairs must each support many separate module repairs, and a quantitatively separated pair of module normals must share a growing collection of the same edges.

C-II remains open. No theorem-state authority is changed.

**Disposition:** bounded the inverse-`D` lower-gate graph by degree six and converted multi-module corridor overlap into an explicit matching-or-heavy-reuse dichotomy, with a wide-normal shared-edge extraction in the heavy branch.