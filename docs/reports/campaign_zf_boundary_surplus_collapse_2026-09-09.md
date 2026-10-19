<!-- theorem-state: {"artifact_id":"ART-699376642925","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "5a5ed7f0a22bb4e03f425a56e5bb5e5653f10f0e", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/campaign_zf_boundary_surplus_collapse_2026-09-09.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "db3a308c35695981c7e64a133a00b0b87eae53b2c51d0c95b3abdf04c9787c56"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — post-ZF boundary-surplus collapse and component-corrected defect budget

**Date:** 2026-09-09  
**Repository state:** `4bc7c9baddb38d12cbadde8394992c0e9f708104`  
**Run type:** closing-proof reduction / dependency audit  
**Target:** Target C, C-II after Z/ZC/ZR/ZF  
**Active prompt:** user-supplied 2026-09-09 Target C–Z full-settlement specification  
**External web search:** used only for public-status/novelty checking; no theorem imported  
**Computation:** not used in this report

The Level I problem remains open. Public problem trackers still list Erdős #99 as open, and this run does not supply either a proof for every sufficiently large global minimizer or an infinite family of exactly optimal triangle-free minimizers.

The strongest new result is an exact **post-ZF phase collapse**. Once the audited ZF rigidity count is assumed, the older C33 `sigma_B=o(D)` near-minimal loaded-boundary phase is impossible. Consequently the C35–C45 response normal form, including the C44 response-mass dichotomy, is not a live post-ZF branch. The general C-II campaign must instead close the boundary-surplus / exceptional-face / bridge / isolated-source side.

A second exact reformulation inserts the planar diameter-graph edge deficit into the exceptional-face endpoint. If

\[
d_H:=q-h,
\]

then every post-ZF survivor obeys

\[
T-q+d_H\le 2f,
\]

while the desired global face contradiction is exactly the strict reverse inequality

\[
T-q+d_H>2f.
\]

For the planar diameter graph, canonical pseudoforest structure identifies `d_H` with the number of tree components. Thus tree components of the diameter graph are exact positive credit on the contradiction side; they cannot be discarded from the defect bookkeeping.

---

## 1. Starting endpoint

Work with a hypothetical sufficiently large triangle-free global minimizer chosen first to minimize the number of unit contacts and then to minimize the number of diameter pairs, as in the audited ZF argument. Let

- `D` be the source diameter;
- `v` be the number of nonisolated vertices of the positive contact core;
- `e` be its number of unit-contact edges;
- `h` be the number of active diameter pairs;
- `q=|B_+|` be the number of diameter endpoints in the relative-interior C-II stress;
- `delta` be the contact-graph diameter;
- `b` be the outer-face walk length of the contact core;
- `f` be the number of bounded nonquadrilateral contact faces;
- `Q=sum_F(deg(F)-4)` over those bounded nonquadrilateral faces;
- `T` be the stopped-train count from DT.

The reviewed report-level stack gives

\[
e+h\ge 2v-2
\tag{ZF}
\]

and the connected triangle-free penny-graph theorem gives

\[
e\le 2v-\delta-2,
\qquad
\delta\ge\lceil D\rceil.
\tag{P}
\]

Hence

\[
h\ge\delta\ge\lceil D\rceil.
\tag{1.1}
\]

The planar diameter-graph bound gives

\[
h\le q.
\tag{1.2}
\]

The exact scalar closing endpoint retained by the September 9 campaign is

\[
\boxed{
b+Q>2h.
}
\tag{1.3}
\]

Euler then gives `e+h<2v-2`, contradicting ZF.

The implication chain established in this report is

```text
ZF + penny-graph deficit + planar diameter bound
    -> h >= delta and q >= h
    -> sigma_B >= q + (q-h) - 2 >= ceil(D) - 2
    -> C33 near-minimal boundary phase is impossible post-ZF

ZF + Euler + DT
    -> T-q+(q-h) <= 2f for every survivor
    -> closing target is exactly T-q+(q-h) > 2f.
```

---

## 2. Strongest genuinely new audited theorem

### Theorem ZS — post-ZF boundary-surplus collapse

Assume the hypotheses of the audited report-level ZF theorem for a lexicographically normalized triangle-free C-II global minimizer. Let

\[
d_H:=q-h\ge0
\]

and let the canonical C33 boundary-surplus parameter be

\[
\sigma_B:=2q-\delta-2.
\]

Then

\[
\boxed{
q\ge h\ge\delta\ge\lceil D\rceil,
}
\tag{ZS.1}
\]

and, more sharply,

\[
\boxed{
\sigma_B
\ge 2q-h-2
=q+d_H-2
\ge\lceil D\rceil+d_H-2.
}
\tag{ZS.2}
\]

In particular, along any sequence with `D->infinity`,

\[
\boxed{
\sigma_B\ne o(D).
}
\tag{ZS.3}
\]

Therefore the near-minimal loaded-boundary phase assumed by `04-near-minimal-response-frontier.md` cannot occur after ZF.

### Scope

This theorem is exact for the same lexicographically normalized C-II sources to which ZF applies. It is not a theorem about arbitrary feasible packings, local minima, or unnormalized global minimizers. It retains contact-isolated source points outside `v`; no source-population replacement is made.

### Proof

ZF and the connected triangle-free penny-graph bound give

\[
2v-2
\le e+h
\le (2v-\delta-2)+h.
\]

Cancel `2v-2` to obtain

\[
h\ge\delta.
\]

The contact core contains two source points at Euclidean distance `D`, and every contact edge has unit length, so every contact path joining those two points has at least `ceil(D)` edges. Hence

\[
\delta\ge\lceil D\rceil.
\]

The planar diameter graph on its `q` endpoints has at most `q` edges, so

\[
q\ge h.
\]

This proves (ZS.1).

Now use the definition of `sigma_B` and `delta<=h`:

\[
\begin{aligned}
\sigma_B
&=2q-\delta-2\\
&\ge 2q-h-2\\
&=q+(q-h)-2\\
&=q+d_H-2.
\end{aligned}
\]

Since `q>=h>=delta>=ceil(D)`, this gives

\[
\sigma_B\ge\lceil D\rceil+d_H-2,
\]

which is (ZS.2). Because `d_H>=0`, division by `D` gives

\[
\liminf_{D\to\infty}\frac{\sigma_B}{D}\ge1,
\]

so `sigma_B=o(D)` is impossible. QED.

### Dependencies

Only the following inputs are used:

1. `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`, Corollary ZF;
2. `docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md`, audit that Z/ZC/ZR/ZF survive with their stated dependencies;
3. the canonical connected triangle-free penny-graph bound `e<=2v-delta-2` already used throughout Target C;
4. the canonical planar diameter-graph edge bound `h<=q`;
5. `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md`, definition `sigma_B=2q-delta-2`;
6. `docs/targets/target-c/04-near-minimal-response-frontier.md`, explicit premise `sigma_B=o(D)`.

No external theorem is newly imported in this report.

### Why it is new

The C33/C35–C45 modules were written before ZF and split C-II into a positive-linear boundary-surplus phase and a near-minimal phase `sigma_B=o(D)`. The September 9 Z review proves `h>=delta`, but the reviewed campaign reports do not propagate that inequality back into `sigma_B`. Repository search found no prior statement of (ZS.2) or the resulting elimination of the C35–C45 near-minimal branch.

The result is not a new proof of ZF and does not promote ZF. It is a new exact consequence of the audited report-level stack.

---

## 3. Component-corrected exceptional-face budget

The same inputs give an exact reformulation of the remaining face inequality.

### Theorem ZD — exact train/diameter defect budget

Under the hypotheses of Theorem ZS, assume the DT stopped-train decomposition applies to the contact core. Then every post-ZF survivor satisfies

\[
\boxed{
T-q+d_H\le2f,
\qquad d_H=q-h.
}
\tag{ZD.1}
\]

Moreover the desired face inequality (1.3) is equivalent to

\[
\boxed{
T-q+d_H>2f.
}
\tag{ZD.2}
\]

Thus (ZD.2) is an exact integer closing theorem: it contradicts ZF immediately.

If the canonical planar diameter-graph pseudoforest characterization is used, `d_H` is exactly the number of tree components of the full diameter graph on `B_+`.

### Proof

For a connected plane contact graph, Euler and face-incidence counting give

\[
\boxed{
e=2v-2-\frac{b+Q}{2}.}
\tag{ZD.3}
\]

Indeed, if `R` is the number of bounded quadrilateral faces, Euler gives

\[
e=v+R+f-1,
\]

while face incidence gives

\[
2e=b+4R+\sum_{F\text{ exceptional}}\deg F
=b+4R+Q+4f.
\]

Eliminating `R` and `f` yields (ZD.3).

Insert (ZD.3) into ZF:

\[
2v-2-\frac{b+Q}{2}+h\ge2v-2,
\]

so

\[
\frac{b+Q}{2}\le h.
\tag{ZD.4}
\]

DT gives the exact stopped-train count

\[
T=\frac{b+Q}{2}+2f.
\tag{ZD.5}
\]

Combining (ZD.4) and (ZD.5),

\[
T-h\le2f.
\]

Since

\[
T-h=(T-q)+(q-h)=T-q+d_H,
\]

we obtain (ZD.1).

Conversely, the desired face inequality `b+Q>2h` is equivalent to

\[
\frac{b+Q}{2}>h.
\]

Using (ZD.5), this is equivalent to

\[
T-2f>h,
\]

or

\[
T-q+d_H>2f.
\]

This is (ZD.2). QED.

### Diameter-component interpretation

The repository already records the classical planar diameter-graph structure: each connected component is a caterpillar whose spine is either a path or one odd cycle; two vertex-disjoint odd cycles cannot occur. For a tree component with `q_i` vertices there are `q_i-1` edges, while a unicyclic component has `q_i` edges. Hence

\[
q-h
\]

counts the tree components exactly. This interpretation is canonical input, not claimed as new mathematics here.

Therefore ZD says:

> exceptional faces must pay not only the exposed-hull train surplus `T-q`, but also one exact unit for every tree component of the diameter graph.

That term was absent from the DF statement because DF used only `h<=q`.

---

## 4. Strengthened dense-core consequence

Let

\[
\Delta=\frac{\pi}{2\sqrt3}.
\]

Under the additional DE/DF hypotheses, in particular `n-v=o(D^2)`, the reviewed train theorem gives

\[
\liminf\frac{T-q}{D}
\ge
2\sqrt\Delta-\frac\pi2.
\tag{4.1}
\]

ZD.1 gives pointwise

\[
2f-d_H\ge T-q.
\]

Therefore

\[
\boxed{
\liminf
\frac{2f-d_H}{D}
\ge
2\sqrt\Delta-\frac\pi2,
}
\tag{4.2}
\]

or equivalently

\[
\boxed{
\liminf
\frac{f-d_H/2}{D}
\ge
\sqrt\Delta-\frac\pi4
=0.166914643466509\ldots.
}
\tag{4.3}
\]

This strictly refines DF whenever the diameter graph has a non-negligible number of tree components. It does not remove the `n-v=o(D^2)` hypothesis and therefore does not solve the isolated-source branch.

---

## 5. Exact target implication

Before this report, the post-ZF campaign still listed C44 response branches as possible continuations if the face inequality did not close immediately.

After Theorem ZS:

1. `sigma_B=o(D)` is impossible for every ZF survivor;
2. therefore the C35–C45 near-minimal harmonic-response normal form is a pre-ZF theorem, not a live post-ZF case split;
3. the C44 absolute-response and near-zero-multiport alternatives cannot be invoked as post-ZF branches without a different theorem that removes their `sigma_B=o(D)` premise;
4. the remaining general C-II work is concentrated in the boundary-surplus / exceptional-face / bridge / narrow-path / isolated-source geometry;
5. the exact scalar endpoint can be written as (ZD.2), with the diameter tree-component count retained rather than discarded.

This is a branch reduction, not Level I closure.

---

## 6. Audit classification of Z-route claims

| Claim | Classification in this run | Reason |
| --- | --- | --- |
| Theorem Z | proved at reviewed report level | Consolidated September 9 audit retains the all-gap split proof, terminal coverage, and the `m>=3` restriction. |
| ZC | proved at reviewed report level for `D>=9` | Z plus C34/SEPq excludes the additive zero-transfer response on the actual contact network. |
| ZR | proved at reviewed report level | Depends on the separately audited C56 generic kernel, SVD, Schur congruence, and exclusion of isolated vertices from `v`. |
| ZF | proved at reviewed report level | Finite integration is now promoted; ZR reduces critical velocities to affine motions; three diameter directions leave Euclidean motions; KKT dependence gives `e+h>=2v-2`. |
| ZB | proved under pure-rhombic-disk hypotheses | ZF gives `T<=h<=q`; Target B B39 gives a strict linear `T-q` gap. It does not cover general topology. |
| ZS | proved and new report-level consequence | Exact algebra from ZF, the penny-graph deficit, `h<=q`, and the C33 definition of `sigma_B`. |
| ZD | proved and new endpoint reformulation | Euler + DT + ZF; exact component correction `d_H=q-h`. |
| DF with component correction | proved conditional consequence | Requires the same dense-core/source hypothesis as DE/DF; no new population theorem is supplied. |

No claim in this table is promoted into the canonical Target C route map by this report.

---

## 7. Regressions checked

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Unit square | yes | It is far below the `D>=9` ZC regime; it also shows matching diameter support is geometrically possible. |
| Regular odd polygon / diameter cycle | yes | A planar diameter cycle can have `d_H=0`; ZS only forces large boundary surplus and does not claim a contradiction from that alone. |
| Crossing diameter matching | yes | Then every component is a tree and `d_H=q-h` is large; ZD charges that exact deficit, but no false uncrossing/star replacement is used. |
| Strict pentagon exceptional face | yes | ZD does not assign a uniform positive Oler surplus to one face; DP's vanishing local Oler excess remains binding. |
| Regular heptagon plus isolated center | yes | ZS/ZD use only the nonisolated core for `v,e,delta`; no claim that isolated source points are diametral is reintroduced. |
| Oblique rhombic fillings | yes | ZB closes only the contact-minimal pure-disk survivor under its full hypotheses; this report does not infer lattice structure from rhombic bulk. |

---

## 8. Failed routes and no-go results

### 8.1 Treating the diameter pseudoforest as new

This is not new. The repository already records the caterpillar / odd-unicycle structure of planar diameter-graph components and already uses the fact that two disjoint odd cycles cannot occur. Only the insertion of `d_H=q-h` into the exact post-ZF defect budget is new here.

### 8.2 Large `sigma_B` does not force many harmonic components

C33 proves

\[
c_I+e_{BB}\le\sigma_B.
\]

The inequality is one-sided. ZS proves `sigma_B` is large; it does **not** imply that `c_I`, `e_BB`, or any face-defect count is large. Reversing this implication would be invalid.

### 8.3 C44 is not a post-ZF fallback

`04-near-minimal-response-frontier.md` explicitly assumes `sigma_B=o(D)`. ZS gives `sigma_B>=ceil(D)-2`. Therefore C44's alternatives are not a post-ZF case split. The C44 theorem itself remains correct under its stated premise.

### 8.4 Reciprocal-force area still does not control rattlers

The exact force-polygon mixed-area identity does not prove that the force hull contains almost all source points. The existing force-polygon report explicitly allows a large KKT-invisible rattler population. ZS does not repair that gap.

### 8.5 No uniform face-local Oler charge

DP's strict unit-pentagon family has vanishing Oler excess. The required gain must couple faces to global shell, stress, source population, or train/diameter topology; it cannot be obtained by assigning a universal positive constant to each exceptional face.

---

## 9. Literature and computation

No external theorem is a proof dependency of ZS or ZD. Public web search was used only to confirm that Erdős #99 is still publicly listed as open and to check for an obvious duplicate of the phase-collapse observation. The mathematical proof uses only repository inputs.

No new computation was required. The September 9 consolidated review already records exact verification of Z/DT regressions and the full repository test suite. ZS and ZD are deterministic algebraic consequences of those audited statements, so rerunning the finite certificates would not test the new step.

---

## 10. Canonical promotion recommendation

**Hold as report.**

Reason: ZS and ZD are fully proved, but their strongest input ZF remains reviewed report-level mathematics rather than a promoted Target C route-map theorem. Promotion should occur only together with, or after, a deliberate promotion of the Z/ZC/ZR/ZF dependency stack.

If that promotion is approved, the exact files to update are:

1. `docs/targets/target-c/03-pinned-block-and-loaded-boundary-frontier.md` — add the post-ZF lower bound `sigma_B>=q+(q-h)-2`;
2. `docs/targets/target-c/04-near-minimal-response-frontier.md` — add an authority note that the entire module is incompatible with a ZF survivor;
3. `docs/targets/target-c/README.md` — remove the near-minimal response phase from the post-ZF frontier and retain it only as a pre-ZF theorem stack;
4. the active Target C–Z continuation prompt — replace the post-ZF C44 A/B branches with the boundary-surplus/defect endpoint;
5. `docs/reports/campaign_ledger_2026-09-09.md` — add the exact endpoint `T-q+(q-h)>2f` and the component-corrected DF consequence.

Do not modify the canonical route map merely from this report.

---

## 11. Highest-value next lemma

The shortest remaining exact theorem is now best written as follows.

### ZD+ target — global defect-payment strictness

For every sufficiently large lexicographically normalized triangle-free C-II global minimizer satisfying the audited Z stack,

\[
\boxed{
T-q+d_H>2f,
\qquad d_H=q-h.
}
\tag{ZD+}
\]

Because all quantities are integral, it is enough to prove

\[
T-q+d_H\ge2f+1.
\]

By ZD this is exactly equivalent to the old face inequality, but the new form identifies the only three currencies that matter:

1. exposed-hull train surplus `T-q`;
2. diameter-graph tree-component credit `d_H`;
3. exceptional-face stopping cost `2f`.

The highest-value new geometric input would be a stress-compatible stopped-train theorem showing that an exceptional face cannot consume two units of this combined surplus without paying either a diameter tree component, a boundary-surplus defect, or a source-capacity loss. Any such theorem must survive the strict-pentagon regression and must not assume `n-v=o(D^2)` unless that population hypothesis is proved separately.

A second route is an actual source-capacity theorem controlling `n-v`; if it yields `n-v=o(D^2)`, then DE and (4.3) become available, but an upper bound on the remaining exceptional-face budget is still needed for closure.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem (ZS):
For every lexicographic C-II survivor to which audited ZF applies,
    h >= delta >= ceil(D),
    q >= h,
and therefore
    sigma_B = 2q-delta-2
            >= 2q-h-2
            = q+(q-h)-2
            >= ceil(D)+(q-h)-2.
Hence sigma_B=o(D) is impossible after ZF. The C35-C45 near-minimal response
frontier, including C44, is not a live post-ZF branch.

Exact endpoint reformulation (ZD):
With DT stopped trains and f exceptional bounded faces,
    T = (b+Q)/2 + 2f,
while ZF gives (b+Q)/2 <= h. Thus every survivor obeys
    T-q+(q-h) <= 2f.
The desired face contradiction is exactly
    T-q+(q-h) > 2f.
For the planar diameter pseudoforest, q-h is the number of tree components.

Dense-core refinement:
Under the existing DE/DF hypothesis n-v=o(D^2),
    liminf [f-(q-h)/2]/D
      >= sqrt(pi/(2sqrt(3))) - pi/4
      = 0.166914643466509...

Z, ZC, ZR, ZF, ZB:
All survive the September 9 consolidated audit under their stated hypotheses.
They remain report-level and are not promoted by this report.

Binding no-go results:
- large sigma_B does not imply large c_I or e_BB;
- C44 requires sigma_B=o(D) and is therefore pre-ZF only;
- force-hull identities still do not control contact-isolated source population;
- strict pentagons kill any uniform face-local Oler charge.

Highest-value next lemma:
    T-q+(q-h) >= 2f+1
for every sufficiently large lexicographic C-II global minimizer.

Authoritative new file:
    docs/reports/campaign_zf_boundary_surplus_collapse_2026-09-09.md
```
