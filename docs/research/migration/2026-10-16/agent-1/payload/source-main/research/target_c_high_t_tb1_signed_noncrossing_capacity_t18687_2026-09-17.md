# Target C-II - fixed-slack near-diameter matchings have bounded noncrossing capacity

**Date:** 2026-09-17  
**Status:** proof-only metric strengthening for the SIGNED upper Horn branch; no canonical promotion claimed  
**Scope:** planar unit-separated diameter-`D` sources; application to SIGNED upper TB1 blockers through `t=(q-k)/D<=1.8687`  
**Dependencies:** upper-blocker dense-grid localization; generic inactive near-diameter degree bound; standard finite Ramsey bound  
**Certificate:** `research/verify_target_c_high_t_tb1_signed_noncrossing_capacity_t18687.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The THIN branch has a true thrackle because its slack is below the sharp `1/(2D)` scale. SIGNED upper blockers have much larger but still fixed inverse-`D` slack, so that theorem does not apply.

There is nevertheless a uniform replacement: for every fixed `A`, a vertex-disjoint family of source pairs of length at least `D-A/D` contains only `O_A(1)` pairwise-noncrossing members. Equivalently, the proper-crossing graph of any such matching has bounded independence number depending only on `A`.

The proof is elementary. Two noncrossing near-diameters must have a pair of endpoints at distance at most `sqrt(2A)+o(1)`. Fixing one reference edge therefore forces every other edge in a noncrossing matching to contribute a distinct endpoint to one of two fixed-radius disks. Unit separation bounds those disks by constant packing.

Applied after the existing SIGNED localization and matching extraction, this converts every localized SIGNED winner into a genuinely growing pairwise-crossing braid. Quantitatively, if `K=31.4e6` is the current global swap constant and one takes `A=K+1`, the resulting crossing braid has size
\[
D^{\varepsilon_K-o(1)},
\qquad
\varepsilon_K>4.97\times10^{-10}.
\]
The exponent is numerically tiny and is not the point. The point is qualitative: the SIGNED branch can no longer remain a large collection of mutually noncrossing almost-diameters inside its low-defect train scaffold.

---

## 1. Four near-diameter endpoints are convex unless a cross-endpoint is subunit

Fix `A>0` and put
\[
\ell_D:=D-{A\over D},
\qquad
\Delta_D:=D^2-\ell_D^2
=2A-{A^2\over D^2}<2A.
\tag{NC.1}
\]
Let `AB` and `CD` be two vertex-disjoint source pairs with
\[
|AB|,|CD|\ge\ell_D.
\tag{NC.2}
\]
All six source distances are at most `D` and all nonzero source distances are at least one.

We first exclude the case in which one of the four points lies in the convex hull of the other three.

Suppose, after relabeling, that `D_0` lies in the triangle `ABC`, where `CD_0` is one of the selected long pairs and `AB` is the other. The ray from `C` through `D_0` meets the opposite side `AB` at a point `E`, and
\[
|CE|\ge|CD_0|\ge\ell_D.
\tag{NC.3}
\]
Because `E` is a convex combination of `A,B`,
\[
|CE|\le\max(|CA|,|CB|)\le D.
\tag{NC.4}
\]
Write
\[
p=|AE|,
\qquad q=|EB|,
\qquad p+q=|AB|\ge\ell_D.
\tag{NC.5}
\]
Choose the unit vector `u` along `AB` from `E` toward `B`, and write `c=C-E`. From
\[
|c+pu|=|CA|\le D,
\qquad
|c-qu|=|CB|\le D,
\qquad
|c|=|CE|\ge\ell_D,
\]
we get
\[
2p(c\cdot u)+p^2\le\Delta_D,
\tag{NC.6}
\]
\[
-2q(c\cdot u)+q^2\le\Delta_D.
\tag{NC.7}
\]
Eliminating `c dot u` gives
\[
\boxed{pq\le\Delta_D.}
\tag{NC.8}
\]
Indeed (NC.6) gives `2 c dot u <= Delta_D/p-p`, while (NC.7) gives `2 c dot u >= q-Delta_D/q`; comparing and multiplying by `pq` yields `(p+q)pq <= (p+q)Delta_D`.

Hence
\[
\min(p,q)\le{2\Delta_D\over p+q}
\le{2\Delta_D\over\ell_D}.
\tag{NC.9}
\]
Also `D_0` lies between `C` and `E`, so
\[
|D_0E|=|CE|-|CD_0|
\le D-\ell_D={A\over D}.
\tag{NC.10}
\]
Therefore
\[
\min(|D_0A|,|D_0B|)
\le {A\over D}+{2\Delta_D\over\ell_D}
=O_A(D^{-1}).
\tag{NC.11}
\]
For all sufficiently large `D` this is less than one, contradicting source separation.

Boundary-degenerate triangle cases obey the same estimate by a limit, or directly by taking `E=D_0`. Thus, for sufficiently large `D`, the four endpoints of two vertex-disjoint near-diameter pairs are in strict convex position unless all four are collinear.

The collinear case is also impossible for two distinct matching edges once `D` is large. Write the four ordered coordinates as `t_1<t_2<t_3<t_4` with unit gaps `g_i=t_{i+1}-t_i>=1` and total span at most `D`. There are only three perfect matchings. The disjoint matching `(t_1t_2,t_3t_4)` would require total span at least `2 ell_D+1>D`. For the interleaving matching `(t_1t_3,t_2t_4)`, the two long-edge inequalities give `g_2>=2 ell_D-D=D-2A/D`, hence `g_1+g_3<=2A/D<2`, contradicting `g_1,g_3>=1`. For the nested matching `(t_1t_4,t_2t_3)`, the inner long edge gives `g_1+g_3<=D-ell_D=A/D<2`, again impossible. Thus no two distinct matching edges in the range (NC.2) can be collinear for sufficiently large `D`.

---

## 2. Two noncrossing near-diameters have a close connector

Assume now that the straight segments `AB` and `CD` do not cross properly. By Section 1 their four endpoints form a convex quadrilateral. Since the selected edges are vertex-disjoint and are not crossing diagonals, they are opposite sides. Relabel cyclically
\[
A,B,C,D.
\]
Put
\[
x=B-A,
\quad y=C-B,
\quad z=D-C,
\quad w=A-D.
\tag{NC.12}
\]
The long sides are `x,z`, while `y,w` are the two connectors.

The diagonals are source pairs, so
\[
|x+y|,|y+z|,|z+w|,|w+x|\le D.
\tag{NC.13}
\]
If `|y|^2>Delta_D`, then
\[
2x\cdot y
=|x+y|^2-|x|^2-|y|^2
\le D^2-\ell_D^2-|y|^2
=\Delta_D-|y|^2<0,
\tag{NC.14}
\]
and identically
\[
y\cdot z<0.
\tag{NC.15}
\]
If also `|w|^2>Delta_D`, then
\[
z\cdot w<0,
\qquad
w\cdot x<0.
\tag{NC.16}
\]
The four exterior turning angles of a convex quadrilateral lie in `(0,pi)` and sum to `2pi`. Equations (NC.14)--(NC.16) would make all four strictly larger than `pi/2`, impossible.

Therefore
\[
\boxed{
\min(|BC|,|DA|)\le\sqrt{\Delta_D}<\sqrt{2A}.
}
\tag{NC.17}
\]
For the other cyclic orientation the same conclusion gives one of the other two cross-endpoint pairs. In invariant form:
\[
\boxed{
\min\{|A-C|,|A-D|,|B-C|,|B-D|\}<\sqrt{2A}
}
\tag{NC.18}
\]
whenever the two selected near-diameter matching edges do not cross properly.

For `A<1/2`, the right side is below one and (NC.18) immediately recovers the superdiameter-thrackle phenomenon. The point here is that the same argument remains useful for arbitrary fixed `A`.

---

## 3. Bounded noncrossing capacity

Let `E_D` be a vertex-disjoint matching of source pairs satisfying
\[
|e|\ge D-{A\over D}
\quad(e\in E_D),
\tag{NC.19}
\]
and suppose no two matching edges cross properly.

Fix one reference edge `AB in E_D`. By (NC.18), every other edge has at least one endpoint in
\[
B(A,\sqrt{2A})\cup B(B,\sqrt{2A}).
\tag{NC.20}
\]
All source points are unit-separated. Disjoint radius-`1/2` disks around source points whose centers lie in a disk of radius `R` fit inside the concentric radius-`R+1/2` disk. Hence each radius-`R` disk contains at most
\[
4(R+1/2)^2
\tag{NC.21}
\]
source points.

Because the matching is vertex-disjoint, the witness endpoints contributed by distinct edges are distinct. Taking `R=sqrt(2A)` gives
\[
\boxed{
|E_D|
\le
\alpha_A
:=1+\left\lceil8\left(\sqrt{2A}+{1\over2}\right)^2\right\rceil
}
\tag{NC.22}
\]
for all sufficiently large `D`.

Thus the proper-crossing graph of **every** vertex-disjoint `D-A/D` near-diameter matching has
\[
\boxed{\alpha(G)\le\alpha_A,}
\tag{NC.23}
\]
a source-independent constant.

---

## 4. Ramsey consequence: every growing matching contains a growing crossing braid

Let `M=|E_D|` be any vertex-disjoint matching in the same near-diameter range, without assuming it is noncrossing. Make a graph whose vertices are the matching edges and whose adjacency means proper geometric crossing. Section 3 says its independence number is at most `alpha_A`.

The standard Ramsey estimate
\[
R(r,\alpha_A+1)
\le {r+\alpha_A-1\choose\alpha_A}
\le(r+\alpha_A)^{\alpha_A}
\tag{NC.24}
\]
shows that the crossing graph contains a clique of size at least
\[
\boxed{
\left\lfloor M^{1/\alpha_A}\right\rfloor-\alpha_A
}
\tag{NC.25}
\]
whenever the right side is positive. In particular,
\[
M\to\infty
\quad\Longrightarrow\quad
\omega(G)\to\infty.
\tag{NC.26}
\]
If `M=D^{beta-o(1)}` for a fixed `beta>0`, the crossing clique has size
\[
D^{\beta/\alpha_A-o(1)}.
\tag{NC.27}
\]

---

## 5. Apply to the localized SIGNED upper Horn branch

The upper-blocker localization theorem gives, whenever SIGNED wins, more than
\[
(c_*-o(1)){D\over\log D}
\tag{NC.28}
\]
SIGNED blockers in one of two low-defect train scaffolds:

- **COMMON-CUT:** all blockers support one selected row whose full train defect is `o(D)`; or
- **LOCAL-WINDOW:** all blocker endpoints lie in one `O(D/log D)` path window carrying `(0.6536-o(1))D` common near-`60 degree` trains and common circumcenter flanks.

Every such blocker satisfies
\[
D-{K+o(1)\over D}<|e|<D,
\qquad
r_e\cdot w_*
\le-\left({1\over4K}-o(1)\right)D,
\tag{NC.29}
\]
with the current source-independent TB1 constant
\[
K=31.4\times10^6.
\tag{NC.30}
\]
Fix
\[
A:=K+1.
\tag{NC.31}
\]
For all sufficiently large `D`, every localized SIGNED blocker lies in the range (NC.19).

The existing inactive near-diameter degree theorem gives
\[
\Delta
\le(8\,3^{1/8}+o(1))D^{3/4}.
\tag{NC.32}
\]
Greedy matching therefore extracts a vertex-disjoint SIGNED matching of size
\[
\boxed{
M_D=\Omega\!\left({D^{1/4}\over\log D}\right)
=D^{1/4-o(1)}.
}
\tag{NC.33}
\]
Apply Section 4. The matching contains a pairwise-properly-crossing SIGNED sub-braid of size
\[
\boxed{
D^{\varepsilon_K-o(1)},
\qquad
\varepsilon_K={1\over4\alpha_{K+1}}>0.
}
\tag{NC.34}
\]
All selected chords preserve the fixed negative projection in (NC.29) and remain inside the same COMMON-CUT or LOCAL-WINDOW low-defect train scaffold.

With `K=31.4e6`, the explicit conservative packing constant is
\[
\alpha_{K+1}
=502{,}463{,}417,
\tag{NC.35}
\]
so
\[
\boxed{
\varepsilon_K
=4.9754866\ldots\times10^{-10}.
}
\tag{NC.36}
\]
The numerical exponent is intentionally not optimized.

---

## 6. Frontier effect

The upper Horn geometry now has crossing braids on both sides of the SIGNED/THIN split.

```text
THIN:
    much stronger linear-origin structure;
    logarithmic braids synchronized to polynomial row/train grids;
    exact ROW-UNIQUE / GUARD-UNIQUE ordered normal forms.

SIGNED:
    D/log D localized blockers in a vanishing-defect scaffold;
    D^(1/4-o(1)) vertex-disjoint near-diameter matching;
    bounded noncrossing capacity for every fixed inverse-D slack;
    hence a D^(epsilon_K-o(1)) pairwise-crossing SIGNED braid,
    all retaining one fixed macroscopic transverse sign.
```

This does not yet close SIGNED. The new braid is far smaller than the THIN braid, and SIGNED endpoints are not promoted to convex-hull vertices. The next useful target is to combine pairwise crossing plus the fixed negative `w_*` projection with the localized common train scaffold. In COMMON-CUT, every braid chord already has the same selected-cut support. In LOCAL-WINDOW, every endpoint lies in one `o(D)` path window with a common dense train ladder.

**Disposition:** proved a fixed-slack extension of the superdiameter crossing phenomenon and used it to convert every localized SIGNED winner into a growing pairwise-crossing braid. C-II and Level I remain open.
