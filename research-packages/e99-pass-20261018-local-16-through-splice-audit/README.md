# Independent exact-head audit: dominant-pentagon through-splicing

**Date:** 2026-10-18  
**Review head:** `7d0a450fe66991036541023f95c44c064a04b6a8`  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`  
**Candidate:** `TARGET-C-DOMINANT-PENTAGON-THROUGH-SPLICE-20261016`  
**Assignment:** reviewer; broad card `target-c-face-coupled-move`; exact investigation `exact-head-audit-target-c-dominant-pentagon-through-splice-20261016`  
**Disposition:** **Conditional PASS for the stated full-core Type-II structural lemma.** This is an unreviewed, noncanonical audit artifact; it does not promote the candidate or alter the theorem state. Level I, A, B and C-II remain open; C-I remains closed.

Reviewer and checker: OpenAI Codex (GPT-6 Luna xhigh), independent reviewer session. The exact pinned candidate report, companion verifier and historical source hostile-audit bytes were checked against their recorded hashes. The source report was imported from `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`; the destination candidate registry still says no destination exact-head independent audit had occurred at the review head. The source audit's PASS was treated as provenance and prior coverage, not as this review.

The source report's PR #522 provenance and prior contributor credit are preserved. This first-party review note and checker are offered under Apache-2.0; no third-party paper text or code is copied here. AI role: independent proof reconstruction, adversarial range check and exact finite verifier.

## Exact question and claim

Under the report's conditional fully force-visible, no-container, full-core Type-II train-measure hypotheses, do through-splices at all all-dominant strictly convex unit pentagons preserve monotone train paths and force the quadratic dominant-orbit crossing deficit

\[
E_D\le M_D^2/4-P_D^2/2+O(D),
\qquad d\ge p^2/2,
\]

and hence the stated lower constraint

\[
K\ge \frac{8\Delta_2}{U}-2U+t-\kappa-
\sqrt{U^2/2-2\Delta_2},
\quad
\Delta_2=\frac{\pi}{2\sqrt3},
\quad
U=\frac{9t}{2}-2\pi-2\delta-\kappa/2?
\]

Here `M_D` is the number of dominant-window trains, `P_D` the number of selected all-dominant pentagons, `E_D` their original strict-rhombus crossing count, `K` the dominant-orbit outer-terminal occurrence density, and `d` the dominant-orbit Mantel deficit. All limits below are taken on a common subsequence where the displayed normalized quantities converge (using liminf/limsup for `P_D`/`E_D`).

The report's hypotheses include: strict convexity of every selected bounded face; five distinct train terminal occurrences per pentagon; finite stopped-train geometry; no bounded train return or bounded singleton loop; three frozen atomic phase windows around the chosen \(\pi/3\) orbit; strict-rhombus phase-order crossing; and the exact endpoint ledgers. The conditional argument does not extract these premises from every canonical source. It asserts no physical new contact, feasible finite endpoint, or same-cardinality replacement.

## Reconstruction

### 1. Pentagon closure and the through connector

For the three triangular-lattice directions \(a=(1,0)\), \(b=(1/2,\sqrt3/2)\), and \(c=b-a\), let `r_a,r_b,r_c` be the signed side-count imbalances in an all-dominant limiting pentagon. Closure gives `r_a a+r_b b+r_c c=0`, hence `r_a=r_c=-r_b`. The three projective phase totals have the same parity as these imbalances, sum to five, and cannot have total below five unless the imbalance is zero (which would make the total even). Thus the totals are `3,1,1`; the repeated phase has one ray sign once and the opposite sign twice. Strict convexity fixes the cyclic limiting pattern up to rotation and reversal as `a,b,c,-b,-b`.

For this representative, joining the midpoint of `+b` to either `-b` midpoint gives connector vector `c` or `-a`. Each has unit length and positive dot product \(\sqrt3/2\) with the positive train normal `Jb`, so it continues an arriving train into a leaving train. Convexity keeps the connector inside its face. Finite ray patterns plus compactness make the projection uniformly positive for sufficiently small frozen phase windows; the limiting angle is `pi/6`, so the proof correctly uses `pi/6+o(1)`, not a uniform exact `pi/6` bound.

### 2. Splice forest and pseudosegments

Orient each train in its phase by positive projection on that phase's normal. Stopped-train midpoint steps and selected connectors have positive projection. The face-side orientation makes every splice join an incoming to an outgoing end, so the splice graph has indegree and outdegree at most one. A directed cycle would have strictly positive total projection, impossible for a closed curve. The splice graph is therefore a forest of directed paths and has `N_D=M_D-P_D` components.

For two distinct phases, their normals differ by `pi/3`. The bisector of the normals has positive projection on every sufficiently narrow train step and every connector. Each spliced component is a graph over that common coordinate. Connector interiors lie in distinct bounded-face interiors, away from train centerlines, so intersections between two distinct phase components can only be original strict-rhombus crossings. For a fixed ordered phase pair, the strict-rhombus crossing condition fixes the sign of the phase-offset difference and hence the oriented crossing sign. Two graphs over one coordinate cannot have two transverse crossings with the same sign. Same-phase components cannot cross because their train directions remain within one shrinking window while a strict-rhombus crossing needs projective separation greater than `pi/3`. Since a splice only joins trains of the repeated phase, no original crossing is turned into a self-crossing by contraction. Thus the quotient intersection graph is simple and retains all `E_D` crossings as distinct edges.

### 3. The quadratic graph count, including its range condition

Let `r_D` be the number of nonsingleton quotient components and `s_D=N_D-r_D`. The singleton induced graph is triangle-free, so it has at most `s_D^2/4` edges. Simplicity bounds all remaining edges by `r_D s_D+binom(r_D,2)`. Thus

\[
E_D\le F_{N_D}(r_D):=s_D^2/4+r_Ds_D+\binom{r_D}{2}
=N_D^2/4+(N_D-1)r_D/2-r_D^2/4.
\]

The report's monotonicity sentence needs its endpoint range made explicit. Each selected pentagon uses five distinct bounded terminal occurrences, and every one of the `M_D` complete trains has two terminal occurrences, of which `K_D` are outer. Therefore

\[
5P_D\le 2M_D-K_D\le2M_D,
\quad P_D\le2M_D/5,
\quad N_D=M_D-P_D\ge P_D+1\; (P_D>0).
\]

The five occurrences are disjoint across selected faces because a terminal occurrence belongs to one face. For integer `0<=r<P_D`,

\[
F_N(r+1)-F_N(r)=(2N-2r-3)/4>0
\]

on this admissible range. Hence `r_D<=P_D` permits substitution of `P_D`; direct simplification gives

\[
E_D\le M_D^2/4-P_D^2/2-P_D/2
\le M_D^2/4-P_D^2/2.
\]

This is stronger than the stated asymptotic bound. The independent checker exhausts the integer range `M_D<=350`; the all-size proof is the preceding incidence inequality and finite-difference identity. The control `M_D=5,P_D=3,r_D=2` shows why the incidence cap cannot be omitted: the quotient edge upper bound is `1`, while the substituted target expression is only `1/4`. This counterexample violates `5P_D<=2M_D` and is excluded by the actual pentagon ledger.

Dividing the finite inequality by `D^2` on the common limit subsequence yields `d>=p^2/2`, where `m=lim M_D/D`, `p=liminf P_D/D`, and `e=limsup E_D/D^2` give `d=m^2/4-e`.

### 4. Endpoint and scalar elimination

Write `f` for bounded exceptional faces and `Q=sum_F(deg(F)-4)`. Since every exceptional face has degree at least five, the number of pentagons is at least `2f-Q`. Total bounded train-terminal incidence is `Q+4f`; the dominant trains contribute `2M_D-K_D` bounded terminal occurrences. Every non-all-dominant pentagon consumes a distinct non-dominant occurrence. Therefore

\[
P_D\ge 2M_D-K_D-2Q-2f,
\quad
p\ge[2m-K-2\chi-2\varphi]_+,
\]

with `chi=lim Q/D`, `phi=lim f/D`. From the exact endpoint definitions used by the report,

\[
\chi=2t-\pi-\delta,
\qquad 2\varphi=C-t/2+\kappa/2,
\qquad C=(T-q/2)/D\le U.
\]

The preceding phase-star orbit ledger gives `m>=4 Delta_2/C` and `d<=A^2/4-Delta_2<=C^2/4-Delta_2`, with `A<=C`. Substitution into the face count gives

\[
p\ge[8\Delta_2/C-K-C+t-U-\kappa]_+
\ge[8\Delta_2/U-K-2U+t-\kappa]_+,
\]

because `8 Delta_2/C-C` decreases for positive `C` and `C<=U`. Combining `d>=p^2/2` with `d<=U^2/4-Delta_2` gives `p<=sqrt(U^2/2-2 Delta_2)`. Comparing these two bounds proves the stated `K` constraint whenever the radical's domain condition is met. The source's matched Type-II range supplies that domain; the numeric regression is not an argument outside it.

## Adversarial checks and result

- Checked destination SHA-256 values against the candidate registry: report `b567c562312438782fbde9cc62788fc843eccf331c09c2fbe3a9f31b27603b16`; original verifier `41e8a654c5b7db0452087f578ed0aafba93216200feea74bd73dae88cc4f78c9`; historical source audit `95de9b4e3e2f2e402565af1f88ec3390db4dccd8d62eecb03a59d91139ec08a2`.
- Reconstructed the named input scopes: canonical C51 gives simple strictly convex bounded force-visible faces; Theorem DT gives stopped paths, one crossing per train pair, a triangle-free train graph and the exact terminal ledger; the phase-star report gives the separate orbit deficit identity. The no-return/no-loop and exact phase/endpoint inputs remain explicit premises of this conditional result.
- Replayed `python research/verify_target_c_dominant_pentagon_through_splicing.py`: six closure patterns and connector/contraction/numerical checks passed; `K_sp=1.7117699302241673...` at the saved boundary point.
- Replayed this package's exact integer verifier; its output records the checked range and the excluded-cap counterexample. Separately, `scripts/research_package.py --check-only` verifies every declared source SHA-256 and commit pin.

The previous hostile audit at source head `2346fb9c3047f26525579df9aced37bc9759e7f6` reached PASS on the same proof-only scope, but did not establish destination exact-head review. This audit independently reconstructs the counting chain and supplies an explicit proof of the `P_D<=2M_D/5` range needed for the graph maximization. It does not improve the numerical floor and does not combine `K` with the direct energy functional.

## Coordination overlap checked before submission

The private refresh at `2026-10-19 04:50 UTC` covered paginated open PR titles/bodies (1 record), Issues (0), and Discussions/comments/replies (8). The exact through-splicing candidate appeared as a local source note; no live open PR or Discussion handoff for this candidate appeared. The known historical source PR #522 and source hostile audit remain predecessor evidence, while the destination registry says no exact-head review had occurred. The sole open PR, #102, is a distinct Target A source-image Hall-overlap result and does not use this candidate's lemma. The four current Discussion #83 handoffs concern other investigations. This freshness-bounded search is only overlap evidence; it does not establish novelty, and PR #102 is not duplicated here.

## Limits and next exact question

No step here proves that every sufficiently large canonical global minimizer enters this full-core Type-II branch, that every candidate hypothesis holds uniformly, or that a source-realized finite move exists. All contact-isolated source points remain in the original full source; they are simply outside this train-incidence lemma. Nothing here changes the universal minimizer quantifiers or closes C-II/Level I.

The next question is whether `K>=K_sp(t,delta,kappa)` excludes the direct energy functional's minimizing allocation on the exact current scalar domain. This changes only the allowed dominant outer-terminal density `K`, and either outcome determines whether the conditional Type-II `t` floor strengthens. A bounded exact interval comparison of both constraints is the first action. Even a positive result would leave the source extraction and full-source finite endpoint unresolved.

**Reproduction:**

```sh
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock python research/verify_target_c_dominant_pentagon_through_splicing.py
flock /home/cinna/.local/state/erdos99-pass/20261018-luna-xhigh/compute.lock python research-packages/e99-pass-20261018-local-16-through-splice-audit/verify.py
python scripts/research_package.py --package research-packages/e99-pass-20261018-local-16-through-splice-audit --check-only
```

This is a scoped reviewer artifact, not theorem promotion. Required repository-wide theorem-certificate replay is deferred to the merging agent if applicable. No claim of production, CI or global-source validation is made.
