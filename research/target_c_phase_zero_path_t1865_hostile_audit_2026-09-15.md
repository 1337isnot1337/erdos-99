<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "cda27d95aaeaa753fd1cc7d8c3273c2945b1e87a", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_phase_zero_path_t1865_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "a1748b746c5dab5eb4465b59f90ff4a8d7d940e4a8bfa740b97bc7c24bf21858"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — phase-zero path / hub / finite interface through `t<=1.865`

**Date:** 2026-09-15
**Reviewed:**
- `research/target_c_phase_zero_path_t1865_2026-09-15.md`
- `research/verify_target_c_phase_zero_path_t1865_interface.py`
- `research/target_c_phase_zero_path_post_retraction_audit_2026-09-15.md`
- `research/target_c_dominant_oo_pair_weight_t1865_hostile_audit_2026-09-15.md`
- current conditional hub theorem `research/target_c_hub_path_one_sided_switch_2026-09-15.md`

**Disposition:** **PASS after the frontier-reference repair in `3c2e917d`.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks only the composition from the independently audited `t<=1.865`
retained-pair floor and the post-retraction phase-zero path theorem to the path/hub and
finite-interface conclusions.  It does not re-audit the scalar retained-mass bootstrap
or the two-shore oriented-branch proof; those have separate hostile audits.

---

## 1. The path density really is `>0.0009D-o(D)`

The retained-pair theorem gives

\[
P_{OO}^{dom}>0.0027D-o(D).
\]

The dominant limiting orbit has at most three projective phase atoms.  Pigeonhole
therefore gives one shrinking phase window with retained pair weight

\[
>0.0009D-o(D).
\]

For one train the retained pair weight is

\[
w_\tau=\min(a_\tau,b_\tau)\le1.
\]

Hence positive pair weight `W` requires at least `W` actual trains.  The post-retraction
phase-zero audit proves that deleting the two shrinking marker neighborhoods removes
only `o(D)` pair weight.  Therefore the cleaned family has

\[
m>0.0009D-o(D)
\]

actual proper O--O crosscuts.

No low-energy Markov truncation or now-retracted path theorem is used.

**Verdict:** PASS.

---

## 2. The path conclusion is now independently repaired

The post-retraction audit proves, for every surviving train, that the two complementary
shore normal arcs contain the two **distinct antipodal** oriented phase zeros.  The
fixed limiting markers can then be moved to those zeros without crossing a terminal,
so every cleaned crosscut separates the same two fixed boundary markers.

Pairwise noncrossing proper disk crosscuts separating the same two markers have totally
ordered marker-side shores.  Therefore their complement dual is a simple path.

This is the exact topological hypothesis needed below and is not the retracted
projective-energy inference.

**Verdict:** PASS.

---

## 3. Exact laminar support applies to the cleaned path

For a finite family of pairwise disjoint proper O--O crosscuts whose complement dual is
a path

\[
R_0\xleftrightarrow{\tau_1}R_1
\xleftrightarrow{\tau_2}\cdots
\xleftrightarrow{\tau_m}R_m,
\]

every source pair has contiguous selected-cut support.  If its endpoints lie in
`R_a,R_b`, `a<b`, the separating selected cuts are exactly

\[
I=\{a+1,\ldots,b\}.
\]

This exact incidence statement is topological; it does not require exact equality of
the shrinking train phases.  The phase-zero theorem correctly removed a former
statement which could have been read as importing an exact-phase rank factorization.

**Verdict:** PASS.

---

## 4. The diameter-path Helly hub is available

Any two actual diameter segments intersect or share an endpoint.  Under the selected
crosscut decomposition, each diameter segment traverses the unique dual path between
its endpoint regions.  The physical intersection belongs to a common complementary
region (source vertices do not lie on train midpoint crosscuts), so the corresponding
dual paths intersect.

Subpaths of a tree have the Helly property.  Therefore all actual-diameter endpoint
paths contain one common region `R_k`.

This is exactly the hypothesis of the current conditional theorem
`target_c_hub_path_one_sided_switch_2026-09-15.md`.  That theorem was retained after
main's path retractions because its proof is conditional only on path+hub structure.

**Verdict:** PASS.

---

## 5. Every nonhub switch is one-sided

For one diameter interval with endpoint indices `a_h<b_h`, the hub condition is

\[
a_h\le k\le b_h.
\]

At an internal middle region `R_i`, a switch is either an interval ending at `i` or an
interval starting at `i`.  If `i<k`, an end at `i` would violate `b_h>=k`; if `i>k`, a
start at `i` would violate `a_h<=k`.

Thus all switches at every nonhub boundary point toward the hub side.  Removing the one
possibly mixed hub index from a family of `0.0009D-o(D)` cuts leaves the same
asymptotic density.

**Verdict:** PASS.

---

## 6. The switching-count budget is exact

Let `N_i` count actual diameter intervals which change incidence across middle region
`R_i`.  One interval has at most one start and one end, so

\[
\sum_iN_i\le2|H|.
\]

The straight-line diameter graph is a thrackle, hence Hopf--Pannwitz gives

\[
|H|\le|B_+|.
\]

Every actual diameter endpoint is an extreme source-convex-hull vertex.  The convex
polygon on the loaded endpoint subset has unit-separated consecutive vertices and
perimeter at most the force-hull perimeter.  Cauchy's perimeter bound gives

\[
|B_+|\le\operatorname{per}(F)\le\pi D.
\]

Therefore

\[
\sum_iN_i\le2\pi D.
\]

Averaging over `>0.0009D-o(D)` nonhub boundaries and using
`pi<355/113` gives

\[
{2(355/113)\over0.0009}=6981.3176\ldots<6982.
\]

Since `N_i` is integral, an eventual boundary with `N_i<=6981` exists.

**Verdict:** PASS.

---

## 7. The KKT switching-mass budget is exact

Use the canonical relative-interior normalized diameter stress

\[
\sum_{h\in H}\beta_h=1,
\qquad \beta_h>0.
\]

A diameter support interval changes incidence at no more than its two endpoint
regions.  Hence

\[
\sum_i B_i
=\sum_i\sum_h\beta_h
 |\varepsilon_{h,i+1}-\varepsilon_{hi}|
\le2\sum_h\beta_h=2.
\]

Thus

\[
\sum_iDB_i\le2D.
\]

No individual KKT multiplier lower bound is used.

**Verdict:** PASS.

---

## 8. The loaded-middle population budget is exact

Let

\[
L_i=|B_+\cap R_i|.
\]

Distinct complementary regions are disjoint, so every loaded diameter endpoint belongs
to one region only.  Therefore

\[
\sum_iL_i\le|B_+|\le\pi D.
\]

Combining this with the preceding two budgets gives

\[
\sum_i(N_i+DB_i+L_i)\le(3\pi+2)D.
\]

The exact certificate checks

\[
{3(355/113)+2\over0.0009}
=12694.1986\ldots<12695.
\]

All three terms are nonnegative.  Thus one nonhub boundary has

\[
N_i,L_i\le12694,
\qquad
B_i<{12695\over D}+o(D^{-1}).
\]

The integrality step is valid because the average has a fixed positive gap below the
next integer while the asymptotic error is `o(1)`.

**Verdict:** PASS.

---

## 9. Current-frontier references were repaired

The original theorem text compared itself to a former main path through `1.8623`.
Main subsequently retracted that theorem.  Commit `3c2e917d` now states the correct
frontier:

- main's independently repaired low-energy/opposite-branch path is valid through
  `t<=1.8593`;
- the phase-zero path overlaps it below that endpoint and extends the path/hub
  structure through `t<=1.865` using a different oriented-branch argument.

No mathematical dependency on the retracted `1.860`/`1.8623` paths remains.

**Verdict:** PASS.

---

## 10. What this does and does not accomplish

The valid proof-only full-core stack now contains

```text
t <= 1.844:
    excluded.

1.844 < t <= 1.8593:
    repaired main path and the phase-zero path both apply.

1.8593 < t <= 1.865:
    phase-zero path;
    common diameter-routing hub;
    one-sided switching away from the hub;
    finite adjacent interface with the bounds above.
```

This is a structural extension, not C-II closure.  It gives no theorem for `t>1.865`,
and a one-sided finite switching set may still block every local middle-layer
translation.  Main's repacking barrier remains relevant.

**Final disposition:** **PASS.**  The phase-zero path/hub/finite-interface theorem is
valid through `t<=1.865` and survives the September 15 path retractions because its
oriented-branch input is separately proved by the two-shore Section-157 argument.
C-II and Level I remain open.
