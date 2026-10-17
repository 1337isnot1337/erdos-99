<!-- theorem-state: {"artifact_id":"ART-BB90CE5EA227","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — terminal low-\(t\) frontier supersession after hull depletion

**Date:** 2026-10-04
**Status:** proof-only scope audit / frontier supersession; theorem-state authority unchanged
**Depends on:** the independently audited proof-only PR #667 hull-depletion theorem and
`research/target_c_hull_depletion_post_endpoint_synthesis_2026-10-04.md`
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The post-#667 synthesis proves the exact finite identity
\[
5t_DD
=
3q+M_D+m_B+2u_B+2(Q-f)-d_D,
\tag{TS.1}
\]
where
\[
u_B=x_B-m_B\ge0,\qquad
M_D\ge(2s-o(1))D,\qquad
s=\sqrt{\frac{\pi}{2\sqrt3}},
\qquad d_D\le2.
\]
Consequently every terminal full-core Type-II sequence satisfying
\[
\frac qD\to\pi
\tag{TS.2}
\]
obeys
\[
\boxed{
\liminf t_D
\ge
t_{\rm term}
:=
\frac{3\pi+2s}{5}
=
2.265880714899459\ldots.
}
\tag{TS.3}
\]

This note records the research-state consequence of (TS.3). It does not delete old
proof artifacts. A historical conditional theorem can remain mathematically correct
even when its former survivor window has become empty.

**Priority / overlap.** The constant in (TS.3) is not new. The September report
`docs/reports/target_c_clean_endpoint_fullcore_boost_2026-09-09.md` already proves
the same (2.2658807149ldots) threshold under (x_B=o(D)). More strongly, open PR
#663 at head `70e2f6a95adcc5bac1ade91da9ea26ffdfe78cfd` contains an exact all-unit-hull
identity
[
5t_DD+x_B+m_B+d_D=3b+2(Q-f)+N_0
]
and proves (N_0/Dge2s-o(1)) for every Type-II sequence. Substituting
(x_B=m_B+u_B), (b=q+x_B), and then (q/D	opi) gives (TS.1)--(TS.3)
directly. The #667 audit supplies a parallel proof with (M_D=N_0).

Accordingly this file claims frontier reconciliation and explicit supersession
bookkeeping, not priority for the terminal threshold.

---

## 1. Three distinct dispositions

An older terminal artifact can fall into one of three classes.

### A. Strictly superseded but still valid

A theorem whose conclusion is merely a weaker lower bound
\[
\liminf t_D\ge c<t_{\rm term}
\]
remains a valid implication if its own dependencies are valid. It is no longer a live
frontier theorem.

The principal examples are
\[
\texttt{target_c_free_terminal_t_gap_00659_2026-09-18.md}
\]
with
\[
t_D\ge1.959852849540479\ldots,
\]
and
\[
\texttt{target_c_free_terminal_t_gap_correlated_00704_2026-09-18.md},
\]
which only raises that terminal floor by another small amount.

These should be retained as provenance for the train/phase machinery, not used as the
current numerical terminal floor.

### B. Empty asymptotic antecedent

Any structural theorem whose own scope includes both (TS.2) and
\[
\limsup t_D\le T<t_{\rm term}
\tag{TS.4}
\]
has no unbounded survivor sequence after the #667 audit.

This does **not** refute its finite conditional lemmas. It says that the full
asymptotic branch described by all of its hypotheses is empty in the stronger
proof-only stack.

### C. Not superseded by this theorem alone

A bounded-\(t\) theorem that does **not** assume or derive \(q/D\to\pi\) is not
retired by (TS.3). In particular, a Type-II disk limit
\[
P_F/D\to\pi
\]
is not by itself the same statement as \(q/D\to\pi\).

This distinction is binding below.

---

## 2. Terminal FREE live windows near \(1.96\) are empty

The September terminal FREE stack uses
\[
\mu_*=
\frac\pi2+\frac25\sqrt{\frac{\pi}{2\sqrt3}}+\frac{0.007707}{5}
=
1.953262849540479\ldots.
\]
Therefore
\[
\mu_*+0.00710
=
1.960362849540479\ldots
<
t_{\rm term}.
\tag{TS.5}
\]

The gap is
\[
\boxed{
t_{\rm term}-(\mu_*+0.00710)
=
0.305517865358980\ldots.
}
\tag{TS.6}
\]

Hence every terminal FREE structural branch with
\[
\pi D-q=o(D),
\qquad
\limsup t_D\le\mu_*+0.00710
\]
has empty asymptotic antecedent.

This applies directly to the stated scopes of:

- `research/target_c_free_terminal_live_detour_pinching_2026-09-18.md`;
- `research/target_c_free_terminal_live_degree_excess_parallel_escape_2026-09-18.md`;
- `research/target_c_free_terminal_outer_star_exact_flex_2026-09-18.md`;
- `research/target_c_free_terminal_live_universal_flex_reservoir_2026-09-18.md`.

The same conclusion applies to downstream results that explicitly import this live
window as a premise.

The geometry proved inside those reports is still useful as local technology. Their
old role as descriptions of an actual surviving terminal \(t\approx1.96\) regime is
superseded.

---

## 3. The near-\(t_*\) terminal near-contact window is empty

The terminal near-floor matching report
\[
\texttt{target_c_free_terminal_t_near_floor_near_contact_matching_2026-09-18.md}
\]
works under
\[
\frac qD\to\pi,
\qquad
\limsup t_D\le t_*+\eta_t,
\qquad
t_*=1.959852849540479\ldots.
\tag{TS.7}
\]

Its concrete live-window corollary takes
\[
\eta_t=10^{-4}
\]
and therefore
\[
\limsup t_D
\le1.959952849540479\ldots
<t_{\rm term}.
\tag{TS.8}
\]

That concrete branch is empty after (TS.3). More generally, every instance of the
same theorem with
\[
\boxed{
\eta_t
<
t_{\rm term}-t_*
=
0.306027865358980\ldots
}
\tag{TS.9}
\]
has empty asymptotic antecedent.

Thus the previously advertised \(0.0461D\) near-contact matching is no longer the
next obligation at the old near-\(t_*\) terminal frontier. The finite extraction
mechanism may be reused in a different scope, but the former low-\(t\) terminal
application is obsolete.

---

## 4. Old terminal surplus-endpoint geometry is also off the live frontier

Several terminal FREE reports work at or within a small positive window of the old
all-phase surplus endpoint \(\mu_D\to\mu_*\), including

- `research/target_c_free_terminal_transport_phase_separation_2026-09-18.md`;
- `research/target_c_free_terminal_dominant_orbit_pentagon_near_contact_2026-09-18.md`;
- `research/target_c_free_terminal_transport_fan_ladder_2026-09-18.md` in its
  endpoint-surplus application.

On the same terminal loaded-chord scope the old stack itself gives
\[
\mu_D=t_D+\frac{m_B}{D}+o(1),
\qquad m_B\ge0.
\tag{TS.10}
\]
Therefore
\[
\mu_D\to\mu_*
\quad\Longrightarrow\quad
\limsup t_D\le\mu_*<t_{\rm term},
\]
contradicting (TS.3).

More generally, any terminal surplus-window application with
\[
\limsup\mu_D<t_{\rm term}
\tag{TS.11}
\]
is empty because (TS.10) implies
\[
t_D\le\mu_D+o(1).
\]

This does not erase the endpoint transport, atomic-orbit, or exact-flex lemmas. It
removes their former endpoint survivor as the live branch.

---

## 5. The October high-\(t\), low-\(x_B\) fan/collar chain is empty

The October good-fan report
\[
\texttt{target_c_high_t_degree3_fan_forcing_2026-10-02.md}
\]
explicitly has
\[
\frac qD\to\pi
\]
in its live high-\(t\), low-outer-walk, square-root-matching branch and evaluates the
branch through
\[
t_D\le1.860+o(1).
\tag{TS.12}
\]
Since \(1.860<t_{\rm term}\), that asymptotic survivor is empty.

The following reports explicitly inherit that high-\(t\) branch:

- `research/target_c_high_t_boundary_rhombus_floor_2026-10-02.md`;
- `research/target_c_high_t_collar_augmented_defect_budget_2026-10-03.md`;
- `research/target_c_high_t_collar_good_end_train_charge_2026-10-03.md`;
- `research/target_c_high_t_collar_pentagon_transport_2026-10-03.md`.

Their finite collar, train-end, augmented-cell, and pentagon-transport inequalities are
not rejected. The former claim that they describe a surviving \(t_D\le1.860\)
full-core branch is superseded.

This is stronger than the earlier #667 observation that the
\(x_B=O(\sqrt D),t_D\le1.860\) endpoint was empty: (TS.3) gives the terminal cutoff
\(2.26588\ldots\), not merely \(3\pi/5=1.88495\ldots\).

---

## 6. Nonterminal bounded-\(t\) pentagon theorems are not retired automatically

The report
\[
\texttt{target_c_modern_all_train_pentagon_sea_t18623_2026-09-15.md}
\]
has the stated scope
\[
t_D\le1.8623
\]
in a canonical full-core Type-II train-measure branch, but its scope statement does
not itself impose \(q/D\to\pi\). The force-hull disk limit
\(P_F/D\to\pi\) is insufficient to insert (TS.2).

Accordingly this supersession audit does **not** declare that report empty.

The same caution applies to
\[
\texttt{target_c_modern_pentagon_isolate_concentration_corollary_2026-09-15.md},
\]
which inherits the bounded-\(t\) pentagon-sea scope. It may become obsolete after an
additional theorem proving terminality in that branch, but that implication is not
supplied here.

This rule also protects any other bounded-\(t\) research artifact whose hypotheses do
not establish \(q/D\to\pi\).

---

## 7. Open-cell / deep-port work is not killed by the terminal theorem

The October strong open-cell / same-host deep-port chain and open drafts #668/#671 do
not currently have \(q/D\to\pi\) as a proved load-bearing hypothesis in their stated
strong-branch applications.

Therefore (TS.3) does not close:

- the strong open-cell staircase / host-cap route;
- the fixed-port nearby-grid route of PR #668;
- the bulk-separator / disjoint-loaded-return route of PR #671; or
- the persistent high-degree-tail obstruction exposed by those drafts.

Those remain legitimate Type-II research directions after the terminal low-\(t\)
cleanup.

The post-#667 synthesis does, however, couple #668's high-degree tail to the global
weighted penalty \(2(Q-f)\), while #671 supplies face-local loaded-return pressure.
The missing cross-face bounded-overlap or direct finite-competitor theorem remains
real.

---

## 8. Type I remains untouched

The Type-I macroscopic inactive-container branch does not satisfy the full-core
premise of the #667 depletion theorem.

Nothing in (TS.1)--(TS.3) changes
\[
\texttt{docs/targets/target-c/162-typeI-container-exchange-unification-audited.md}.
\]

Its remaining obligation is still a collective protected finite density-increasing
repacking, with the exact contact/diameter bookkeeping stated there.

---

## 9. Revised proof-only route map

After the #667 audit, the terminal low-\(t\) research stack should be read as:

```text
full-core Type II
  |
  +-- terminal q/D -> pi
  |     |
  |     +-- t_D >= 2.265880714899459...
  |     |
  |     +-- old terminal t ~ 1.95--1.96 gap theorems:
  |     |      valid provenance, numerically superseded
  |     |
  |     +-- old live-window structural descendants below 2.26588:
  |            empty asymptotic antecedent
  |
  +-- nonterminal bounded-t branches:
  |      NOT removed by terminal theorem alone
  |
  +-- strong open-cell / deep-port / high-degree routes:
  |      still live unless terminality is proved separately
  |
  +-- Type I macroscopic container:
         separate branch; unchanged
```

The immediate closing targets are therefore no longer the terminal FREE
near-\(1.96\) fan/pentagon/flex refinements. They are:

1. the nonterminal full-core weighted-defect frontier;
2. the strong open-cell/deep-port high-degree/loaded-return bridge;
3. the bounded-degree Groemer activation/rigidity bridge; and
4. the separate Type-I protected collective repacking theorem.

**Disposition:** proof-only frontier cleanup. Preserve historical reports, but do not
spend new runs extending terminal low-\(t\) windows already below (TS.3).
