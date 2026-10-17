> Generated reading edition · [exact source](../../../docs/reports/target_c_global_capacity_face_transport_2026-09-10.md) · source SHA-256 `cca942f9afb9832d2aa0c76709a04c455d3b38908c96d8403c8df69c0bb9792c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AF01B5248F8E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_capacity_face_transport_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=39305a9fd226a972871c2999ba7acf58d9a95ac3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — global-capacity / face-transport continuation

**Date:** 2026-09-10  
**Repository state:** `main` at `3f37ef0eab4407a411f9a6d51d016ba600302be7`; research branch `research/c-ii-global-capacity-2026-09-10`  
**Run type:** closing proof / audit  
**Target:** Target C, C-II  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`, resolved against `docs/targets/target-c/56-ci-restored-frontier.md`  
**External web search:** not yet used  
**Computation:** not yet used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

C-I is closed. Work with a triangle-free global minimizer selected first to minimize contacts and then diameter pairs. The selected representative has `C=C_*`, `H=H_*`; all contact-isolated source points remain in the population.

The first exact full-source endpoint is

$$
\delta_K+\mathscr O_A\ge c_0P,
$$

where

$$
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,
\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1),
$$

$$
a_0=\frac{\sqrt3}{2},\qquad c_0=\frac{\sqrt3}{4}.
$$

The strict translated-lattice comparison gives the opposite inequality for every global minimizer.

The post-ZF alternative endpoint is

$$
b+Q_f>2h,
$$

which is equivalent by Euler to `e+h<=2v-3` and contradicts ZF's `e+h>=2v-2`.

## 2. Exact reduction of the NC endpoint

There is a useful cancellation that should be kept explicit in every attempted NC proof:

$$
\begin{aligned}
\delta_K+\mathscr O_A
&=\left(\frac{\pi D^2}{4}-\operatorname{area}K\right)
  +\left(\operatorname{area}K+c_0P-a_0(n-1)\right)\\
&=\frac{\pi D^2}{4}+c_0P-a_0(n-1).
\end{aligned}
$$

Hence

$$
\boxed{
\delta_K+\mathscr O_A\ge c_0P
\iff
D^2\ge\frac{2\sqrt3}{\pi}(n-1).
}
\tag{2.1}
$$

This is not a new closing theorem; it is an exact diagnostic for proposed bridges. In particular, no argument that only reallocates hull area between `delta_K` and `O_A` can close NC. The missing theorem must force a finite capacity loss from the triangle-free/global-source structure, or construct a strict sub-`D` competitor.

The regular odd shell plus dense isolated filling remains a binding regression: near-minimal circumradius, `P_*/D->2`, near-antipodal diameter geometry, actual circular-planar PSD response, and affine kernel do not by themselves imply (2.1). The missing information must use global optimality beyond those properties.

## 3. Audited candidate inputs currently retained

The 2026-09-10 full-source report supplies candidate FS.1–FS.4:

- `R(K)=D/2+O(sqrt(D))` from the full source population;
- every selected force hull inherits the same containing disk;
- `P_*=2D-O(sqrt(D))` uniformly over normalized KKT stresses;
- every shared-endpoint diameter angle is `O(D^(-1/4))`;
- diameter midpoints lie `O(D^(3/4))` from one source circumcenter;
- the actual response is radialized only on the two coordinate fields.

The audited post-ZF chain supplies the report-level consequences

$$
e+h\ge2v-2,
\qquad
q\ge h\ge\delta\ge\lceil D\rceil,
\qquad
\sigma_B\ge\lceil D\rceil-2.
$$

The old `sigma_B=o(D)` response normal form is therefore unavailable on this route.

## 4. Proof-obligation ledger

### Trusted canonical inputs

- `docs/targets/target-c/56-ci-restored-frontier.md`: C-I closure, `C=C_*`, `H=H_*`, common-kernel local form.
- `docs/targets/target-c/01-force-hull-and-shear.md`: force hull, connected full-diameter positive contact support, reciprocal response, diameter geometry.
- `docs/theory/03-oler-shell.md`: Oler inequality and exact shell bookkeeping.

### Candidate dependencies under audit

- `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`: FS.1–FS.4.
- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`: Z/ZR/ZF.
- `docs/reports/campaign_zero_transfer_defect_review_2026-09-09.md`: consolidated ZF audit.
- `docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md`: ZS.
- `docs/reports/target_c_zf_exact_defect_budget_addendum_2026-09-09.md`: ZE/ZT/ZU.
- `docs/reports/target_c_mixed_redundant_rigidity_edge_cuts_2026-09-09.md`: RR.

### Rejected shortcuts

- `P_*/D->2` does not imply an almost-full-weight diameter matching.
- Near radiality on coordinate fields is not an operator-norm response bound.
- A nearly minimal containing radius does not imply near-maximal force-hull area.
- Linear many positive response minors do not give a quantitative conductance floor.
- Linear boundary surplus alone does not imply the face contradiction; regular odd shells are exact regressions.

## 5. Current exact remaining implication

The preferred new theorem must have one of these two forms:

1. a triangle-free/global-optimality capacity theorem forcing (2.1), equivalently `n-1<=Delta_2 D^2`; or
2. a full-source bridge from FS plus ZF/RR into `b+Q_f>2h` (or a strict smaller-diameter competitor), with exceptional faces, bridges, and isolates retained.

No Level I claim is made at this checkpoint.
