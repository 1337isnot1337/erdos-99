# Hostile audit — adjacent-strip translation and finite switching forest

**Date:** 2026-09-15  
**Reviewed:** `research/target_c_adjacent_strip_translation_forest_2026-09-15.md`  
**Disposition:** **PASS with one slack wording correction, plus a sharper `<1763` support corollary.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate leaves the exact old-contact manifold: for two consecutive O--O cuts on the current smallest-leaf backbone it translates the full source strip between their nested shores.  The two boundary train contact families open, while every source pair whose strip membership does not change is fixed exactly.

The proof is correct.  Its useful consequence is stronger than the advertised Pareto `<1800` version: because strip translation does not need phase closeness or a small switching KKT mass, direct averaging of the switch-count budget alone produces an adjacent strip with fewer than `1763+o(1)` moving diameter edges.  Those edges form a bipartite straight-line thrackle and therefore a caterpillar forest.

The one correction is purely explicit bookkeeping: when the proof invokes the canonical contact-minimal global-minimizer normalization, sufficiently small translation must preserve not only strict lower-distance slack `>1`, but also strict old nondiameter upper slack `<D`.  Finiteness supplies both simultaneously.  With that sentence inserted, the normalization argument is complete.

---

## 1. Consecutive rooted shores really define one full-source strip

Let `tau_i,tau_{i+1}` be consecutive edges on the audited complement-dual path of pairwise noncrossing O--O leaf trains.  Root the dual on the preceding side and let `S_i,S_{i+1}` be the far shores.

For consecutive edges on one rooted tree path,

\[
S_{i+1}\subset S_i.
\]

The audited one-train shore construction already assigns every full-source point, including contact isolates, to a geometric shore.  Therefore

\[
R=S_i\setminus S_{i+1}
\]

is a legitimate subset of the entire source, not merely of the nonisolated contact core.

If `chi_j` is the far-shore indicator, then

\[
1_R=\chi_i-\chi_{i+1}.
\]

**Verdict:** PASS.

---

## 2. Exactly two old contact families cross the strip boundary

The audited O--O cutset theorem says that an old unit contact crosses the shore split of `tau_j` if and only if that contact belongs to `tau_j`.  Thus for an old unit contact `xy`,

\[
1_R(y)-1_R(x)
=[\chi_i(y)-\chi_i(x)]-[\chi_{i+1}(y)-\chi_{i+1}(x)]
\]

can be nonzero only for contacts in `tau_i` or `tau_{i+1}`.

Every other old contact has both endpoints translated together or both endpoints fixed, hence its vector is unchanged exactly.

For each boundary train orient every contact from the endpoint outside `R` to the endpoint inside `R`.  Coherence of a stopped train makes these oriented vectors constant within the train; call them unit vectors `a,b`.  Translating `R` by `v` sends them to

\[
a+v,\qquad b+v.
\]

If `a+b!=0`, choose `v=s(a+b)`, `s>0`.  Then

\[
a\cdot v=b\cdot v=s(1+a\cdot b)>0,
\]

so both contact lengths strictly increase.  If `b=-a`, any nonzero `v` perpendicular to `a` gives squared lengths `1+|v|^2` on both boundaries.

Thus there are arbitrarily small nonzero strip translations opening both train boundaries simultaneously.  No phase-closeness assumption is needed.

**Verdict:** PASS.

---

## 3. Exact support identity is correct for every source pair

For an oriented source pair `h=xy`, put

\[
\delta_h=1_R(y)-1_R(x).
\]

The translated vector is exactly

\[
r_h(v)=r_h+\delta_hv.
\]

Using `1_R=chi_i-chi_{i+1}` gives

\[
\delta_h=\varepsilon_{hi}-\varepsilon_{h,i+1}.
\]

On the rooted laminar path each diameter incidence row is a single signed interval, so adjacent values differ by `0,+1,-1`.  Hence `delta_h!=0` exactly when that row starts or stops at the selected internal boundary.

Therefore every non-switching source-pair distance is unchanged exactly, not only to first order.

For a switching actual diameter edge,

\[
|r_h(v)|^2=D^2+2\delta_hr_h\cdot v+|v|^2.
\]

**Verdict:** PASS.

---

## 4. The moving diameter graph is bipartite, hence a caterpillar forest

If `delta_h!=0`, exactly one endpoint of `h` belongs to `R`.  The switching diameter graph is therefore bipartite with shores `R` and `R^c`.

Every planar diameter graph is a straight-line thrackle: two diameter segments with disjoint endpoints cannot be geometrically disjoint.  Woodall's straight-line classification, already used in the Target-C topology stack, says every connected straight-line thrackle is either a caterpillar tree or a spiked odd cycle.

The switching graph is bipartite, so it has no odd cycle.  Thus every nontrivial connected component is a caterpillar tree.

\[
\boxed{H_R\text{ is a caterpillar forest}.}
\]

This does not require the full diameter graph itself to be a tree or to lie in a low-degeneracy extreme KKT support.  It is a direct subgraph statement about the full actual diameter graph.

**Verdict:** PASS.

---

## 5. Sharper support count: `<1763+o(1)`

The original candidate deliberately chooses the Pareto boundary on which switch count, switching beta mass, and phase gap are all controlled at once, giving

\[
N_i<1800+o(1).
\]

For strip translation only `N_i` matters.  On the same triple-small backbone, the number of internal boundaries is

\[
>pD-o(D),
\qquad
p={278778993\over78216868750}.
\]

The audited signed-interval budget gives

\[
\sum_iN_i\le2\pi D.
\]

Hence some internal boundary satisfies

\[
N_i\le {2\pi\over p}+o(1).
\]

With the outward bound `pi<355/113`, exact rational arithmetic gives

\[
{2(355/113)\over p}
={55533976812500\over31502026209}
=1762.8699958\ldots<1763.
\]

Therefore there is an adjacent strip, possibly different from the Pareto one, for which

\[
\boxed{|H_R|<1763+o(1).}
\tag{HA.ST.1}
\]

All geometric conclusions in Sections 1--4 apply to this sharper pair.  No simultaneous small-`B_i` or small phase-gap assertion is attached to (HA.ST.1).

**Verdict:** PASS, stronger corollary.

---

## 6. KKT strip resultant identity is exact on the Pareto pair

For the Pareto pair, the rooted cut resultants are

\[
F_j=A_ju_j=\sum_h\beta_h\varepsilon_{hj}r_h.
\]

Subtracting gives

\[
F_i-F_{i+1}
=\sum_{h\in H_R}\beta_h\delta_hr_h.
\]

Because an interval starts or stops with difference magnitude one,

\[
B_i
=\sum_{h\in H_R}\beta_h.
\]

The Pareto certificate therefore gives

\[
\sum_{h\in H_R}\beta_h<{10^6\over D}+o(D^{-1}).
\]

This weighted statement belongs to the Pareto `<1800` pair, not automatically to the separately averaged `<1763` pair.  The candidate correctly separates those uses in its final discussion.

**Verdict:** PASS.

---

## 7. Normalization argument needs both strict slacks

The candidate says that sufficiently small `v` preserves every strict old noncontact lower-distance inequality.  For the global-minimizer comparison we must also preserve every strict old nondiameter upper inequality.

The full source is finite.  Hence among old pairs with length strictly between `1` and `D`, there is a positive minimum lower slack from `1` and a positive minimum upper slack from `D`.  The finitely many translated pair vectors depend continuously on `v`.  Thus one neighborhood of `v=0` preserves simultaneously

\[
|p_x(v)-p_y(v)|>1
\]

for every old strict noncontact and

\[
|p_x(v)-p_y(v)|<D
\]

for every old strict nondiameter pair.

Now suppose a sufficiently small contact-opening strip translation satisfies

\[
2\delta_hr_h\cdot v+|v|^2\le0
\]

for every switching actual diameter edge.  Every old diameter pair is then at most `D`; all old nondiameter pairs remain below `D`; and unit separation holds.  Hence the translated source has diameter at most `D`.

- If its diameter is below `D`, global minimality is contradicted.
- If its diameter equals `D`, it is another global minimizer but both boundary train contact families have been opened and no new unit contact has appeared.  Thus it has strictly fewer contacts, contradicting the canonical contact-minimal choice.

No secondary diameter-pair argument is required.

This is the clean corrected form of the candidate's Section 7.

**Verdict:** PASS after this explicit slack correction.

---

## 8. Final status

The correct structural conclusion is now:

```text
on one adjacent O-O strip:
  open both boundary contact families by a finite translation;
  all non-switching source-pair distances stay exactly fixed;
  only a finite switching diameter graph can move;
  on a Pareto pair it has <1800+o(1) edges plus small beta/phase budgets;
  on a count-optimized pair it has <1763+o(1) edges;
  in either case the switching graph is a caterpillar forest.
```

This is a real reduction beyond the exact-contact-preserving finite-cusp theorem: the candidate leaves the old contact manifold and identifies the complete finite blocker set exactly.

It does **not** yet show that every finite switching caterpillar admits a contact-opening diameter-safe translation.  KKT stationarity can still make such a finite forest block the local motion.  The next theorem should classify those finite forest blockers or give a nonlocal leaf/spine exchange.

**Final verdict:** **PASS with the stated slack correction and the stronger `<1763` support corollary. C-II and Level I remain open.**
