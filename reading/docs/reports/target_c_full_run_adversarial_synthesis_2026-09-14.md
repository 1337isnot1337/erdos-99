> Generated reading edition · [exact source](../../../docs/reports/target_c_full_run_adversarial_synthesis_2026-09-14.md) · source SHA-256 `5c6d1d66ec0d60af8a6b9052c4637dffe337620247a6aa9fcbfd39a75feedefc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E645A7A5FA8D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_full_run_adversarial_synthesis_2026-09-14.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=ed75d93619e1ca5c25d7d5ec97976075c0c0e6c9; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — C-II full-run adversarial synthesis

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.49`
**Run type:** closing proof / adversarial synthesis
**Target:** C-II / Level I
**Starting status:** canonical Target C-II frontier through normalized Sections 122–123; diameter-budget, loaded-chord, and train-coupled-surplus promotions completed during this run
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for status and rigidity near-miss checking; no external theorem imported
**Computation:** exact scalar, chamber, hex-window, multi-grain, state-check, and finite rigidity audits

## LEVEL I STATUS

`STILL OPEN`

The original quantifiers remain untouched:

$$
\exists n_0\ \forall n\ge n_0\ \forall A\quad
 A\text{ a global }D(n)\text{-minimizer}
 \Longrightarrow A\text{ contains a unit equilateral triangle}.
$$

No construction in this run is asserted to be a global minimizer, and no asymptotic
packing statement is promoted to a theorem about every minimizer.

## 1. Starting canonical endpoint and implication chain

The selected route was the canonical C-II full-core branch. The live endpoint was

$$
\liminf_{D\to\infty}\frac1D\sum_r
 (L_r+P_{{\rm exc},r}-2d_r)
 \ge \frac\pi2(2-\sqrt3),
$$

with the exact Section-123 payment

$$
\sum_rP_{{\rm exc},r}\le 10(e_{BB}-k),
\qquad k=d_H+s_Z.
$$

The required chain was written before pursuing the bridge:

```text
source-level upper bound on Σᵣ(Lᵣ−2dᵣ)
    -> combine with the Section-122 detour floor and Section-123 payment
    -> contradiction, exact unit triangle, or finite same-cardinality strict sub-D competitor
    -> exclude C-II and then Level I
```

The run established that the displayed scalar ledgers do not supply the first line,
and that the macroscopic-container branch still lacks the third line.

## 2. Strongest established progress

### 2.1 Repaired Type-II aggregate payment

**Classification:** audited-working; not canonical in this run.

Under the canonical post-ZF normal form, in the full-core near-disk Type-II branch,
and with no loaded-loaded interior chord in any attachment polygon, the finite
cellwise ledger gives

$$
\sum_r(L_r+P_{{\rm exc},r}-2a_r)
\le 10(e_{BB}-k-d_{\rm tile})
       -4M_{\rm miss}-6C_\partial,
\tag{2.1}
$$

and hence

$$
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
\le 10(e_{BB}-k-d_{\rm tile})
 +2\sum_r(a_r-d_r)-4M_{\rm miss}-6C_\partial.
\tag{2.2}
$$

Here `L_r` is occurrence-counted, `a_r=|A_r|`, `d_r=diam(conv(A_r))`,
`M_miss` is the missing-side defect, `C_partial` counts actual loaded contacts on
attachment-polygon sides, and `d_tile` is the Section-123 dissection deficit. All
contact-isolated source points remain in the global source; they are not silently
deleted from the normal form.

The near-disk support argument used to justify the extra hypothesis is finite:
for sufficiently large `D`, every unit chord between loaded force-hull vertices is a
hull side. Consequently `c_B=0`, `e_BB=q-m`, and a loaded-loaded unit edge cannot
occur as an interior attachment-polygon chord. The local identity follows by
partitioning augmented faces into missing-side, actual-contact-side, and ordinary
faces, then using

$$
P_{{\rm exc},r}\le5(Q_{C,r}+Q_{I,r}).
$$

The exact remaining quantity is not eliminated: no sign or sufficiently small upper
bound for `Σ_r(a_r-d_r)` has been proved. The full proof and independent audit are in
[`target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md`](target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md)
and
[`target_c_typeii_aggregate_payment_independent_audit_2026-09-14.md`](../audits/target_c_typeii_aggregate_payment_independent_audit_2026-09-14.md).

### 2.2 Exact scalar no-go for the remaining full-core ledger

**Classification:** exact regression; unreviewed and noncanonical.

The `Fraction` certificate constructs abstract scalar ledger assignments satisfying
the displayed promoted constraints from Sections 61–63, 80, 85, 122, and 123,
including the repaired Type-II payment, while retaining positive outer detour. One
near-disk scalar witness has

$$
\sum_r(L_r-2d_r)=\frac{163}{100}D-12,
\qquad
P_{\rm exc}=\frac54D,
$$

at `D=10^6`, and satisfies the local zero-host, train-end, area–train, and
Section-123 inequalities with rational margins. This proves only that the listed
scalar inequalities do not close C-II by elimination. It is not a planar packing,
contact graph, KKT stress, source, or global-minimality certificate.

The exact identity audited in the same certificate is

$$
L_r+Q_r=4a_r-6-2s_r-2c_r,
\qquad
L_r+P_{{\rm exc},r}=4a_r-6-2s_r-2c_r+4f_r,
$$

with repeated outer-walk and bridge occurrences counted. The certificate is in
[`target_c_scalar_ledger_compatibility_2026-09-14.md`](target_c_scalar_ledger_compatibility_2026-09-14.md).

### 2.3 Exact macroscopic-container consequences, but no exchange

**Classification:** audited-working, not canonical in this run.

For a convex inactive chamber or exterior cap `C` with area `Ω(D²)`, perimeter
`O(D)`, and a unit-separated actual source population `S` satisfying the canonical
Oler-scale population lower bound, the convex hull `H=conv(S)` obeys

$$
\operatorname{area}(C\setminus H)=O(D),
\qquad d_H(C,H)=O(\sqrt D),
$$

and contains a disk of radius `Ω(D)`. This is a finite convex-geometric consequence
of Oler's inequality and a cap-area estimate. It applies to the actual external
source points, not to a scaffold.

Contact minimality also gives the exact covering statement

$$
C_{-1}\subseteq\bigcup_{s\in S}\overline B(s,1)
$$

when all nonisolated source points lie outside the interior of `C`. The proof deletes
one nonisolated point and inserts an uncovered point, preserving cardinality and
diameter while reducing contacts.

These facts still do not yield a protected strict add-one exchange: a strictly
separated triangular lattice with spacing `1+o(1)` can cover the eroded chamber while
having no site at distance strictly greater than one from all existing sources. The
exact saturated-chamber regression and the exterior-cap proof are in
[`target_c_strict_saturated_chamber_regression_2026-09-14.md`](target_c_strict_saturated_chamber_regression_2026-09-14.md)
and
[`target_c_exterior_cap_hull_and_cover_2026-09-14.md`](target_c_exterior_cap_hull_and_cover_2026-09-14.md).

### 2.4 Rigidity audit: Maxwell counting is not the missing bridge

The contact graph of a triangle-free separated planar configuration is triangle-free
and hence has at most `2v-4` edges when it is a simple planar graph. That count alone
does not imply a diameter-decreasing motion. An exact finite regression is the unit
square

$$
(0,0),(1,0),(1,1),(0,1),
$$

with its four unit sides and one active diameter pair, the diagonal from `(0,0)` to
`(1,1)`. If the four vertex velocities are `a,b,c,d`, side preservation forces

$$
b_x=a_x,\quad c_y=b_y,\quad d_x=c_x,\quad a_y=d_y,
$$

and diagonal preservation adds

$$
(c_x-a_x)+(c_y-a_y)=0.
$$

The solution space has dimension exactly three, the Euclidean rigid motions. Thus a
triangle-free contact framework plus an active diameter constraint can already be
infinitesimally rigid. This is only a finite regression against a contact-count
shortcut; it is not a claim about large global minimizers.

The external rigidity literature likewise treats rigidity as a property of both the
graph and its realization, and its available density theorems concern unit-distance
graphs with much denser edge counts than the planar contact setting. No imported
rigidity theorem supplies the required source-preserving strict diameter decrease.

### 2.5 Exact full-core renormalized-surplus floor

**Classification:** canonical in the checkout's `2026-09-14.audit.49` manifest;
the surrounding synthesis remains unreviewed.

There is an additional source-level consequence of the canonical full-core area and
cell-tiling hypotheses. Define

$$
 \mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}{D}.
$$

For every unbounded sequence in the canonical full-core branch,

$$
\boxed{\liminf_{D\to\infty}\mu_D\ge1.}
\tag{2.5.1}
$$

Let `P_r=conv(A_r)`, `u_r=area(P_r)`, and `d_r=diam(P_r)`. Canonical near-disk
saturation and cell tiling give a fixed finite constant `C` with

$$
 \sum_r u_r=\frac\pi4D^2-o(D^2),
 \qquad
 \sum_r\sqrt{u_r}\le CD.
\tag{2.5.2}
$$

Fix `eta>0`, and call a cell large when `u_r >= eta D^2`. The small cells
have total area at most `C sqrt(eta) D^2`, so the large cells carry at least

$$
 \left(\frac\pi4-C\sqrt\eta-o(1)\right)D^2.
$$

The planar isodiametric inequality therefore gives

$$
 \sum_{\mathrm{large}}d_r^2
 \ge\frac4\pi\sum_{\mathrm{large}}u_r
 \ge\left(1-\frac{4C}{\pi}\sqrt\eta-o(1)\right)D^2.
\tag{2.5.3}
$$

There are at most `C/sqrt(eta)` large cells, hence

$$
 \sum_{\mathrm{large}}d_r
 \ge\left(\sum_{\mathrm{large}}d_r^2\right)^{1/2}.
$$

The exact attachment currency ledger supplies `d_r <= delta_r + 2` and

$$
 \sum_r\delta_r+R_I+s_B+3(d_H+s_Z)=6+e_{BB}+2s_C.
\tag{2.5.4}
$$

The residual terms are nonnegative, so `sum_r delta_r <= 6 + mu_D D`. Combining
this with (2.5.3), then dividing by `D` and sending `D -> infinity`, yields

$$
 \liminf\mu_D
 \ge\sqrt{1-\frac{4C}{\pi}\sqrt\eta}.
$$

Finally let `eta -> 0`. The additive `2C/sqrt(eta) + 6` term disappears because
`eta` was fixed before `D -> infinity`. This proves (2.5.1). The
argument does not delete contact-isolated source points; it uses only the positive-
contact cells, exactly within their canonical scope.

The resulting chain is

```text
full-core cell area saturation + square-root perimeter budget
    -> total large-cell diameter >= D-o(D)
    -> exact component-diameter currency gives mu_D >= 1
    -> all subunit-mu full-core sequences are excluded.
```

This floor remains compatible with the Section-122 detour demand, the Section-123
payment, and the macroscopic-container branch. It supplies neither an upper bound
on `mu_D`, a source-preserving strict sub-`D(n)` competitor, nor an exact unit
equilateral triangle.

### 2.6 Loaded-chord/train coupling: the current strongest scalar floor

**Classification:** canonical as `C-FULLCORE-TRAIN-SURPLUS-FLOOR`; full proof and
independent audit are in the separately registered report and audit.

In the Type-II near-disk branch the actual loaded force hull satisfies

$$
B(0,r_D)\subset F\subset B(0,R_D),
\qquad r_D/D,R_D/D\to1/2.
$$

If two loaded hull vertices at unit distance had an intervening hull vertex, the
short hull arc between them would have at least two unit-separated side occurrences.
All side directions on that arc lie in a cone of width (o(1)), so projection onto
the cone bisector would give a chord projection at least (2\cos(o(1))>1), a
contradiction. Hence every loaded-loaded unit contact is a hull side, so

$$
c_B=0,
\qquad e_{BB}=q-m_B.
$$

The exact loaded-hull/pinned ledger then gives

$$
\mu_DD=q+m_B-k-2c_I-4,
\qquad k=d_H+s_Z,
$$

and canonical component deatomization gives (c_I=O(D^{2/3})). If

$$
u_D=(q-k)/D,\quad p_D=P_F/D,\quad x_D=f/D,
\quad r_D^{(4)}=R_4/D^2,
$$

the occurrence-counted outer ledger and train-boundary currency imply

$$
u_D\ge p_D/2+x_D/2,
\qquad
u_D\ge2\sqrt{r_D^{(4)}}-2x_D.
$$

The (4/5,1/5) convex combination cancels (x_D), while
$p_D\to\pi$ and (r_D^{(4)}\to\pi/(2\sqrt3)). Therefore

$$
\boxed{
\liminf\mu_D\ge
\frac{2\pi+2\sqrt{\pi/(2\sqrt3)}}5
=1.6375621841815\ldots.}
$$

This strengthens the prior floor but does not change the endpoint: the scalar
witness in `target_c_scalar_ledger_compatibility_2026-09-14.md` still satisfies
the displayed ledgers with μ above (2) and positive aggregate detour. The
remaining obstruction is geometric/source-level, not another scalar constant.

## 3. Exact frontier effect

The checkout's authoritative `2026-09-14.audit.49` manifest canonically registers
the diameter-budget, loaded-chord, and train-coupled surplus claims. This synthesis
remains a noncanonical summary; theorem authority is held by those manifest entries
and their dedicated reports/audits.

The run advances the research ledger in four precise ways:

1. the broad Type-II aggregate payment is restricted to the verified near-disk
   no-interior-loaded-chord regime;
2. the remaining displayed scalar package is certified compatible with positive
   outer detour, so scalar constant optimization cannot by itself close the route;
3. full-core area saturation plus the exact attachment currency forces
   $\liminf\mu_D\ge1$, and loaded-chord/train coupling strengthens this to
   $\liminf\mu_D\ge1.6375621841815\ldots$ in the same Type-II branch;
4. the exact scalar regression remains compatible with the strengthened floor and
   positive detour, so scalar optimization is exhausted for the displayed package;
5. the macroscopic-cap hull/cover facts are source-specific but are shown compatible
   with strict saturated packing, so one-point contact creation is not enough.

The vanishing-shear and oblique-hexagon families additionally reject a fixed density
loss, a uniform rhombus-angle gap, and an arbitrary affine-window
“equilateralization” argument. They remain feasible-packing regressions only; no
global optimality is inferred.

## 4. Exact remaining obligations

The full-core branch requires at least one of:

1. an upper bound on the same occurrence-counted quantity
   `Σ_r(L_r-2d_r)` strong enough to contradict the Section-122 lower bound after
   the exact Section-123 payment;
2. a theorem converting forced aggregate detour/non-rhombic area into an explicitly
   source-preserving, same-cardinality, unit-separated competitor of diameter `<D(n)`;
3. an exact unit equilateral triangle forced by the carrier, loaded hull, or diameter
   geometry; or
4. a global theorem eliminating the full-core branch.

The macroscopic-container branch requires a separate theorem: a finite exchange or
other global contradiction that retains all isolated source points and pays the
deleted core's contact/diameter budget. Hull stability, covering, and possible contact
creation alone are insufficient.

Target A remains at its exact locked-response sink-surplus obligation; Target B
remains at the joint outer-shell stability inequality. Neither route was promoted or
silently substituted for the C-II source-level bridge.

## 5. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Sections 122–123 detour floor and exceptional-face payment | canonical | `C-AGGREGATE-TWO-ARC-DETOUR`, `C-AUGMENTED-CELL-DEFECT-BUDGET` | Current state lock; occurrence and source conventions retained |
| Loaded unit chord is a force-hull side in Type-II near-disk regime | canonical | `C-FULLCORE-NEAR-DISK`, `C-LOADED-HULL` | Independently audited finite angular-width proof; no interior loaded-hull chord follows |
| Train-coupled full-core surplus floor `liminf mu_D >= 1.6375621841815...` | canonical | `C-FULLCORE-LOADED-CHORD`, `C-COMP-DEATOMIZATION`, `C-TRAIN-INTERFACE-CURRENCY` | Exact (4/5,1/5) coupling; stronger floor still has no source-level bridge |
| Repaired Type-II payment (2.1)–(2.2) | audited-working | canonical Type-II cell and Section-123 ledgers | Exact face accounting; restricted hypothesis stated |
| Full-core surplus floor `liminf mu_D >= 1` | canonical, superseded numerically by the stronger floor in the same branch | `C-FULLCORE-NEAR-DISK`, `C-HARMONIC-CELL-TILING`, `C-ATTACH-CURRENCY` | Fixed-threshold large-cell isodiametric argument; retained as the underlying budget proof |
| Scalar package closes C-II | rejected | Sections 61–63, 80, 85, 122, 123 | Exact rational witness retains positive detour |
| Macroscopic cap hull is `O(D)` area-deficient and `O(sqrt(D))` Hausdorff-close | audited-working | canonical inactive-cap population/Oler hypotheses | Convex hull stability proof retains actual source points |
| Cap covering forces a strict spare site | rejected | cap covering plus contact minimality | Strict triangular-lattice saturation regression |
| Triangle-free contact count alone gives a finite diameter-decreasing flex | rejected | planar triangle-free contact graph | Unit-square/active-diagonal rank regression |
| Vanishing shear gives a Level I disproof | rejected | finite feasible packing only | No global `D(n)` optimality or every-minimizer quantifier |
| Target C-II is closed | rejected | all candidate bridges | Aggregate detour and macroscopic branches remain |

## 6. Regression checks and computation

The following commands were run in `[local filesystem path omitted]`:

```text
python3 research/verify_target_c_scalar_ledger_compatibility.py
python3 research/verify_target_c_strict_saturated_chamber_regression.py
python3 research/verify_target_c_hex_window_shear_endpoint.py
python3 research/verify_target_c_multigrain_endpoint_capacity_exact.py
python3 research/verify_target_c_d6_affine_window_comparison.py
python3 research/verify_target_c_coembedded_protected_cover.py
python3 research/nearchain_vertex_regressions.py
python3 research/verify_target_c_protected_contact_creation.py
python3 research/verify_pr182_heplus_05983685.py
python3 tools/check_theorem_state.py
```

All listed research certificates returned `PASS` results. The scalar and multigrain certificates
use rational `Fraction` arithmetic; the chamber and hex-window certificates use exact
rational quadratic forms and integer enumeration. Their omitted hypotheses are,
respectively, planar realization/KKT/source optimality, carrier co-embedding, and
global optimality.

The theorem-state checker and artifact-index regeneration were rerun after
synchronizing the existing promotion metadata and passed. The analytic floor itself uses no floating-point
computation and is not certificate-backed.

The complete registered certificate runner also attempted
`research/target_c_s1_q13_shell_regression.py` and stopped because this environment
lacks the optional `sympy` package. That finite regression is not used in the floor
proof or in the claimed open-status conclusion.

The one-off unit-square rank calculation above is exact by the displayed linear
equations and is not load-bearing for any canonical claim.

The surplus floor in Section 2.5 is analytic and uses no floating-point computation.
Its order of limits is explicit: fix the cell-area threshold, send `D -> infinity`,
then send the threshold to zero.

The train-coupled floor in Section 2.6 is also analytic. Its displayed decimal is
only an evaluation of the exact expression; the proof uses the exact perimeter and
rhombus-density limits and no numerical optimization.

## 7. Literature imports and near misses

No external theorem is used as a premise. The public Erdős Problem 99 listing still
describes the problem as open; this agrees with the repository state. A recent rigidity
paper was checked only to confirm the scope of standard framework-rigidity results:
they depend on the realization and do not provide the global source-preserving
diameter comparison required here. These are status/near-miss checks, not proof
dependencies.

## 8. Corrections and disposition

The run preserves the following corrections already required by the state lock:

- no full-source extension of the ZR/ZF affine-kernel theorem;
- no deletion of contact-isolated source points;
- no inference from a scalar scaffold or selected carrier to the source;
- no finite integration of a zero KKT multiplier without a deformation theorem;
- no incident-diameter-to-Euler-path inference;
- no PR #191 ordinary-surplus theorem or withdrawn normalization claim.

The no-interior-chord projection audit was corrected during this run: a cone of width
`tau` gives a `cos(tau)` projection factor, not `cos(tau/2)`. Since `tau=o(1)`, the
corrected finite contradiction still has `2 cos(tau)>1`; no stronger conclusion is
being taken from the correction.

The new scalar witness is a regression against future attempts to close C-II using
only the current displayed ledgers. The saturated-chamber and affine-window families
are likewise preserved as regressions, not promoted theorem inputs.

## 9. Promotion recommendation

**Canonical floor claims promoted; synthesis remains noncanonical.** The report as a
whole is not a theorem source: the separately identified budget, loaded-chord, and
train-coupled claims are promoted under their manifest entries and audits.

The repaired Type-II payment and cap-hull results remain independently promotable only
through the repository's normal audit and state-lock procedure. The corresponding
promotion transaction is already recorded in audit.49; this summary does not control
the theorem authority.

## 10. Handoff

1. Strongest established progress: the promoted full-core train-coupled floor
   `liminf mu_D>=1.6375621841815...`, together with loaded-chord elimination, the
   restricted Type-II payment, exact scalar compatibility witness, and source-specific
   cap hull/cover theorem.
2. Canonical dependency chain: `C-FULLCORE-NEAR-DISK` + `C-HARMONIC-CARRIER-QUAD` +
   `C-HARMONIC-CELL-TILING` + `C-AGGREGATE-TWO-ARC-DETOUR` +
   `C-AUGMENTED-CELL-DEFECT-BUDGET`.
3. Exact remaining lemma: in the surviving full-core `mu_D>=1.6375621841815...`
   regime, bound or
   source-levelly monetize `Σ_r(L_r-2d_r)`; separately eliminate the macroscopic
   inactive chamber/exterior cap branch.
4. Binding dead routes: scalar-only elimination, density-only angle loss, one-point
   contact creation, local Maxwell flex, arbitrary affine equilateralization, and all
   source/scaffold identifications.
5. Files to read next: `docs/targets/target-c/CURRENT.md`, Sections 122–123, the
   current Target A Sections 175–177, and Target B's joint shell-stability endpoint.
