# Target C-II — opening an adjacent O--O strip leaves only a `<1763` switching caterpillar

**Date:** 2026-09-15  
**Status:** proof-only finite/source-level structural strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited O--O shore cutsets; live dual-tree backbone; exact signed interval support; adjacent switching-caterpillar theorem; canonical contact-minimal global-minimizer normalization  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The adjacent finite-cusp theorem stays on the old contact manifold.  There is a simpler finite move once two consecutive O--O cuts have been selected: translate the entire source layer between their nested shores.

This move intentionally opens both boundary train contact families.  Every source pair whose endpoints do not straddle that one layer is unchanged **exactly**.  Therefore all moving diameter constraints are precisely the switching edges already classified as a caterpillar forest.

For this move no phase-gap or switching-multiplier estimate is needed.  Direct averaging of the switch-count budget alone gives an adjacent layer with fewer than

\[
\boxed{1763+o(1)}
\]

moving actual diameter edges.

---

## 1. Choose the count-optimal adjacent boundary

The triple-small construction contains more than

\[
pD-o(D)
\]

internal adjacent boundaries, where

\[
p={278778993\over78216868750}
=0.0035641799\ldots .
\tag{SO.1}
\]

Let `N_i` be the number of actual diameter interval rows whose rooted incidence changes between boundary cuts `tau_i,tau_{i+1}`.  Every diameter interval starts and stops at most once, so the audited interval budget is

\[
\sum_iN_i\le2|H|\le2\pi D.
\tag{SO.2}
\]

Hence some internal boundary satisfies

\[
N_i\le{2\pi\over p}+o(1).
\]

Using the outward rational bound `pi<355/113`,

\[
{2(355/113)\over p}
={55533976812500\over31502026209}
=1762.8699958\ldots<1763.
\]

Therefore one adjacent pair obeys

\[
\boxed{N_i<1763+o(1).}
\tag{SO.3}
\]

This adjacent pair need not be the Pareto pair that also minimizes phase gap and KKT switching mass.  The present theorem spends only the support-count budget.

---

## 2. The full-source layer between the two cuts

Root the complement dual of the selected noncrossing leaf family.  Let `S_i,S_{i+1}` be the far shores of the selected consecutive cuts, ordered so that

\[
S_{i+1}\subset S_i.
\]

The audited shore construction assigns every source point, including contact isolates, to a geometric shore.  Put

\[
R:=S_i\setminus S_{i+1}.
\tag{SO.4}
\]

If `chi_i,chi_{i+1}` are the two far-shore indicators, then

\[
\mathbf1_R=\chi_i-\chi_{i+1}.
\tag{SO.5}
\]

The O--O cutset theorem says an old unit contact crosses cut `tau_j` if and only if it belongs to `tau_j`.  Therefore the contact-graph boundary of `R` consists exactly of the contact edges in

\[
\tau_i\cup\tau_{i+1}.
\tag{SO.6}
\]

---

## 3. Translate the layer and open both boundary train families

For `v in R^2`, define

\[
p_x(v)=
\begin{cases}
p_x+v,&x\in R,\\p_x,&x\notin R.
\end{cases}
\tag{SO.7}
\]

Every old contact outside the two boundary trains has both endpoints translated together or both endpoints fixed, so its vector is unchanged exactly.

Orient every `tau_i` contact from the endpoint outside `R` to the endpoint inside `R`; the coherent train vector is one unit vector `a`.  Orient `tau_{i+1}` the same way and call its unit vector `b`.  Under (SO.7), the two contact vectors become

\[
a+v,
\qquad b+v.
\tag{SO.8}
\]

There are arbitrarily small nonzero `v` making both strictly longer than one.

If `a+b\ne0`, take

\[
v=s(a+b),\qquad s>0.
\]

Then

\[
a\cdot v=b\cdot v=s(1+a\cdot b)>0,
\]

so both squared lengths exceed one.  If `b=-a`, take any nonzero `v\perp a`; then both squared lengths are exactly `1+|v|^2`.

Because the source is finite, one sufficiently small choice of such `v` simultaneously preserves

- every old strict lower-distance slack `|xy|>1`, and
- every old strict nondiameter upper slack `|xy|<D`.

Thus the only constraints that can stop this contact-opening finite move are old actual diameter pairs whose endpoints have different strip membership.

---

## 4. Exact support identity for every source pair

For an oriented source pair `h=xy`, put

\[
r_h=p_y-p_x,
\qquad
\delta_h:=\mathbf1_R(y)-\mathbf1_R(x).
\]

Then exactly

\[
\boxed{r_h(v)=r_h+\delta_hv.}
\tag{SO.9}
\]

Using (SO.5) and the rooted incidences

\[
\varepsilon_{hj}=\chi_j(y)-\chi_j(x),
\]

we have

\[
\boxed{\delta_h=\varepsilon_{hi}-\varepsilon_{h,i+1}.}
\tag{SO.10}
\]

On the laminar path each diameter row is one signed interval, so `delta_h` belongs to `{-1,0,1}` and is nonzero exactly when the diameter row starts or stops at this internal boundary.

Consequently:

\[
\boxed{\delta_h=0\Longrightarrow |r_h(v)|=|r_h|\text{ exactly for every }v.}
\tag{SO.11}
\]

For a moving old diameter pair,

\[
\boxed{
|r_h(v)|^2
=D^2+2\delta_hr_h\cdot v+|v|^2.
}
\tag{SO.12}
\]

The moving actual diameter set is precisely the switching graph `H_sw` at this boundary, and (SO.3) gives

\[
\boxed{|E(H_{sw})|<1763+o(1).}
\tag{SO.13}
\]

---

## 5. The complete moving blocker is a caterpillar forest

The adjacent switching-caterpillar theorem proves for **every** adjacent nested pair that

\[
H_{sw}=\delta_H(R),
\]

so every moving diameter edge has exactly one endpoint in `R`.  Hence `H_sw` is bipartite.  As a subgraph of the planar diameter thrackle it has no even cycle, and each tree component is a caterpillar.

Therefore the count-optimal strip satisfies

\[
\boxed{
H_{sw}\text{ is a caterpillar forest with }<1763+o(1)\text{ edges}.
}
\tag{SO.14}

At most `3526+o(1)` loaded diameter endpoints are incident to the complete moving blocker set.

---

## 6. Canonical minimality reduces the finite move to the forest inequalities

For a moving diameter edge, keeping its length at most `D` is exactly

\[
2\delta_hr_h\cdot v+|v|^2\le0.
\tag{SO.15}
\]

Suppose some sufficiently small vector `v` simultaneously

1. opens both boundary contact families as in Section 3, and
2. satisfies (SO.15) for every edge of `H_sw`.

Then every old diameter pair is at most `D`, every old strict nondiameter pair remains below `D`, and every source distance remains at least one.  Hence the translated source has diameter at most `D`.

If its diameter is below `D`, global minimality is contradicted.  If its diameter is exactly `D`, it is another global minimizer with strictly fewer unit contacts: both boundary train contact families have opened and no new unit contact appears.  This contradicts the canonical contact-minimal choice.

Thus a survivor forces the finite infeasibility statement

\[
\boxed{
\text{no sufficiently small contact-opening }v
\text{ satisfies (SO.15) for every edge of }H_{sw}.
}
\tag{SO.16}

All other source-pair distances have been eliminated from the replacement problem exactly.

---

## 7. KKT interpretation

For the same strip, summing the two rooted cut resultants gives the exact switching-force identity

\[
F_i-F_{i+1}
=\sum_{h\in H_{sw}}\beta_h\delta_hr_h.
\tag{SO.17}
\]

This explains the local blocking but is not used to prove the support reduction.  In particular, the count-optimal `<1763` pair is not asserted to have the Pareto pair's small switching-beta mass.

The important point is conceptual: after leaving the old contact manifold, the complete local obstruction is a finite caterpillar forest acting through the explicit quadratic inequalities (SO.15).

---

## 8. Frontier effect

The live finite problem is now

```text
one source layer R between consecutive O--O cuts
+ a two-parameter family of small translations v
+ both boundary train contact families can be opened
+ every nonswitching source-pair distance is exactly invariant
+ <1763 switching diameter bars can move
+ the moving diameter graph is a caterpillar forest
+ each moving bar has exact inequality
    2 delta_h (r_h . v) + |v|^2 <= 0.
```

This is strictly smaller than the previous finite-cusp problem because old contacts are allowed to open and every nonswitching source pair disappears from the finite motion exactly.

The next closing target is a finite geometric blocker theorem: classify which straight-line diameter caterpillars can make (SO.16) hold for the two boundary contact directions, and show that none can occur on the selected thin O--O layer, or construct a source-preserving leaf/spine exchange that bypasses the blocked translation.

**Disposition:** proved proof-only adjacent-strip opening reduction with `<1763` moving diameter edges. C-II and Level I remain open.
