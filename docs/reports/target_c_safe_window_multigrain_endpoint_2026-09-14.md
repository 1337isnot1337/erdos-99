<!-- theorem-state: {"artifact_id":"ART-D56AE224BFA6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — safe-window multi-grain endpoint certificate

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-12.audit.46`
**Run type:** closing proof / adversarial audit / exact computation
**Target:** C-II / Level I
**Starting status:** canonical C-II frontier through normalized Sections 122–123; Target A and Target B open
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** used for status only; no external theorem imported
**Computation:** used — `research/target_c_multigrain_endpoint_capacity.py`, `research/verify_target_c_multigrain_endpoint_capacity_exact.py`

## LEVEL I STATUS

`STILL OPEN`

The result below removes a proof-only safe subwindow of the C-II full-core
carrier branch. It does not prove that all full-core survivors lie in that
subwindow, does not address the macroscopic inactive-container branch, and does
not construct a global same-cardinality competitor. The original quantifiers
over every sufficiently large cardinality and every global minimizer therefore
remain open.

## 1. Starting canonical endpoint

For a contact-minimal, then diameter-pair-minimal, triangle-free global
minimizer, the canonical C-II full-core route supplies occurrence-counted local
outer walks and the two inequalities

\[
 \liminf_{D\to\infty}{1\over D}
 \sum_r\left(L_r+P_{{\rm exc},r}-2d_r\right)
 \ge {\pi\over2}(2-\sqrt3),
 \tag{1}
\]

and

\[
 \sum_rP_{{\rm exc},r}\le 10(e_{BB}-k),
 \qquad k=d_H+s_Z.
 \tag{2}
\]

The intended chain was

```text
full-core carrier geometry
    -> upper bound on the same aggregate detour after the Section-123 payment
    -> contradiction, exact triangle, or source-preserving strict sub-D competitor
    -> C-II and then Level I
```

The canonical Section-118 carrier estimate, together with the proof-only
sparse/directional return split, eliminates only the safe endpoint-slack window
\(\sigma\le 0.0088\). The remaining question attacked here was whether a
quadratic rhombus mass could evade that endpoint argument by splitting into many
phase-separated grains. The answer is no, subject to the explicitly listed
proof-only carrier hypotheses below.

## 2. Strongest genuinely new result

**Classification:** conditional / audited scalar sublemma; unreviewed and
noncanonical.

### Statement

Let \(D\to\infty\) and let \(\mathcal K_D\) be the retained crossing graph of
a proof-only Section-118 full-core carrier. Let \(n_i\) and \(e_i\) denote the
number of train vertices and crossing edges in its surviving connected
components. Assume the following normalized hypotheses.

1. The carrier has at least
   \[
   (0.4703752-o(1))D^2
   \]
   strict-rhombus crossing edges before pruning.

2. The total number of complete trains is at most
   \[
   (1.8488+o(1))D.
   \]

3. The total positive reduced-phase defect is at most
   \(5.317D+o(D)\). After deleting crossings with defect greater than
   \(K/D\), where \(K=10000\), and repeatedly deleting vertices of current
   degree less than \(\eta D\), where \(\eta=10^{-5}\), the surviving graph
   retains at least \((0.4697-o(1))D^2\) edges and every surviving component
   has minimum degree at least \(\eta D\).

4. The proof-only phase lift has at most three projective phase labels. Within
   each surviving connected component and each label, the phase width tends to
   zero, and the Section-118 bad-train estimate bounds the trains in one such
   phase window by \((0.1163+o(1))D\).

5. The two endpoint occurrences of each retained train are charged with their
   physical boundary multiplicity, and the total principal-route endpoint
   capacity is at most \((1.8693+o(1))D\).

6. The retained crossing graph is simple and triangle-free.

Then no such sequence \(\mathcal K_D\) exists. More precisely, if

\[
 x_i={n_i\over D},\qquad
 K_0=3(0.1163)=0.3489,qquad
 S=\sum_i\max\{x_i-K_0,0\},
 \]

the endpoint accounting forces

\[
 2S\le 1.8693+o(1),
 \tag{3}
\]

whereas Mantel's theorem and the retained edge mass force

\[
 S>0.9499,
 \tag{4}
\]

so the two bounds differ by a strict margin greater than \(0.0305-o(1)\).

The statement is an asymptotic proof-only exclusion. It is not a claim that the
canonical theorem state has already promoted hypotheses 1–5, and it supplies no
explicit numerical threshold for the original \(n\)-quantifier.

### Scope and normalization

The carrier is a selected positive-contact object inside the full source. The
argument does not delete or relocate contact-isolated source points, but it also
does not place their coordinates in the crossing graph or in the ZR/ZF affine
kernel. The boundary quantities in hypothesis 5 are occurrence counts, so a
repeated boundary vertex or bridge occurrence is charged repeatedly. The result
is not a theorem about arbitrary unit-separated sets, locally jammed packings, or
all global minimizers unless the proof-only carrier extraction is first promoted
with exactly these hypotheses.

### Proof

Write \(T_D\) for the pre-pruning number of trains and \(E_D\) for the number
of crossing edges. A crossing with positive defect greater than \(K/D\)
accounts for more than \(K/D\) of the defect budget. Hence the number of such
crossings is at most

\[
 {5.317D+o(D)\over K/D}
 =\left({5.317\over10000}+o(1)\right)D^2.
 \tag{5}
\]

During the low-degree pruning, each deleted train removes fewer than \(\eta D\)
currently surviving incident edges. Since there are at most
\((1.8488+o(1))D\) trains in total, the number of removed edge occurrences is
at most

\[
 \eta D T_D\le (0.000018488+o(1))D^2.
 \tag{6}
\]

Therefore the retained graph has normalized edge mass at least

\[
 0.4703752-0.0005317-0.000018488-o(1)
 >0.4697-o(1).
 \tag{7}
\]

Now take two vertices in one surviving component and a shortest graph path
between them. Vertices at path positions differing by at least three have
disjoint closed graph neighborhoods. Every such neighborhood contains at least
\(\eta D+1\) vertices. Since the whole graph has only
\((1.8488+o(1))D\) train vertices, every shortest path has bounded length,
independently of \(D\). Each retained edge changes reduced phase by at most
\(K/D\). Thus the phase diameter of a surviving component is \(O(D^{-1})\).

This is the only graph-connectedness argument used. The proof-only three-label
phase lift then places the trains of each component in at most three projective
windows of vanishing width. Hypothesis 4 applies the one-window bad-train bound
to each of these windows.

For a surviving component put \(x_i=n_i/D\). At most
\(3(0.1163+o(1))D\) of its trains can be charged as bad in those windows. Thus
the excess \(\max\{x_i-K_0,0\}D\) must be represented by endpoint occurrences
on the principal routes. Charging each train's two occurrences and summing over
all components gives

\[
 2\sum_i\max\{x_i-K_0,0\}
 \le 1.8693+o(1),
 \tag{8}
\]

which is (3). This charge is deliberately componentwise; overlapping phase
windows only make the right-hand side of the allowed off-route population
larger, so no disjointness between different components is assumed.

For the lower bound, apply Mantel's theorem to each simple triangle-free
component:

\[
 e_i\le {n_i^2\over4}.
 \tag{9}
\]

Set \(C_0=1.8488\), and note \(\sum_i x_i\le C_0+o(1)\). For
\(x_i\le K_0\), \(x_i^2\le K_0x_i\). For \(x_i>K_0\), write
\(x_i=K_0+y_i\). Then

\[
 \sum_i x_i^2
 \le K_0C_0+K_0S+S^2+o(1),
 \tag{10}
\]

because \(\sum y_i=S\) and \(\sum y_i^2\le S^2\). Combining (7), (9),
and (10) yields

\[
 S^2+K_0S+K_0C_0-4(0.4697)+o(1)\ge0.
 \tag{11}
\]

The polynomial on the left without \(o(1)\) is strictly increasing for
\(S\ge0\). At \(S=0.9499\), its exact rational value is negative; the exact
certificate records this as

\[
 S^2+0.3489S+0.3489(1.8488)-4(0.4697)<0.
 \tag{12}
\]

Since the value at zero is also negative, (11) forces
\(S>0.9499-o(1)\), proving (4). But (3) gives

\[
 2S\le1.8693+o(1),
 \qquad
 2S>1.8998-o(1),
 \]

and the exact limiting gap is

\[
 1.8998-1.8693=0.0305>0.
 \tag{13}
\]

This contradiction proves the conditional scalar sublemma.

### Dependencies

The dependency boundary is important.

| Input | Lifecycle | Exact use here |
| --- | --- | --- |
| `C-HARMONIC-CELL-TILING` / canonical Section 116 | canonical | supplies the strict-rhombus carrier and the area-to-crossing interpretation; no global boundary simplification is used |
| `C-CORRELATED-SLACK-RETURN` / canonical Section 118 endpoint data | canonical | supplies the safe-window constants and the three-label/bad-window framework as stated in the current route |
| Sections 117–118 sparse/directional split | proof-only, unpromoted | supplies the safe-window extraction and the numerical train/bad-capacity constants |
| `C-DENSE-PHASE-CORE` and `C-WRAP-COMPLEMENT-CHORD` | canonical/proof-only as marked in the manifest | supplies reduced phases, defect budget, and route occurrence accounting; only the hypotheses explicitly restated above are used |
| `target_c_multigrain_endpoint_capacity_2026-09-12.md` | proof-only candidate | records the phase-component reduction; this report rederives its scalar step and makes its error budget explicit |
| `verify_target_c_multigrain_endpoint_capacity_exact.py` | this report's exact certificate | checks (7), (12), and (13) with rational arithmetic |

No claim in this report uses the affine-kernel theorem on isolated points. No
external theorem is imported beyond the elementary graph-theoretic Mantel bound;
the latter is applied only under hypothesis 6.

## 3. Exact frontier effect

The result closes the multi-grain endpoint-accounting gap inside the proof-only
safe window:

```text
safe Section-118 carrier
    -> angular-defect pruning and low-degree pruning
    -> bounded-diameter phase components
    -> at most three bad windows per component
    -> route endpoint capacity 2S <= 1.8693 + o(1)
    -> Mantel lower bound 2S > 1.8998 - o(1)
    -> safe-window carrier excluded
```

It does not advance the canonical state because the sparse/directional extraction
and its safe-window endpoint estimates remain proof-only. Even if that dependency
were promoted, the theorem would cover only \(\sigma\le0.0088\). It gives no
upper bound on the aggregate detour

\[
 \sum_r(L_r-2d_r),
\]

for the remaining full-core slack regime, and it creates no source-preserving
finite deformation.

## 4. Exact remaining obligations

The first uncovered C-II obligation is:

> For every Type-II full-core triangle-free global minimizer with endpoint slack
> beyond the safe Section-118 window, prove either an upper bound on
> \(\sum_r(L_r-2d_r)\) strong enough to contradict (1) after the exact payment
> (2), an explicitly source-preserving same-cardinality unit-separated
> competitor with smaller diameter, or an exact unit equilateral triangle.

The separate Type-I obligation is:

> Exclude an actual internal inactive chamber or exterior cap containing
> \(\Omega(D^2)\) retained source points with only linear perimeter/slack by an
> exact triangle, a source-preserving strict sub-\(D\) competitor, or a theorem
> that globally changes the diameter-carrying core while preserving the source
> cardinality.

Neither obligation is implied by contact creation, positive local KKT force, a
selected scaffold, or an affine-kernel statement restricted to the
nonisolated core.

## 5. Proof-obligation ledger and claim audit

| Obligation/claim | Status | Exact scope and reason |
| --- | --- | --- |
| Canonical Section-122 aggregate detour floor (1) | canonical | full-core route; walks are occurrence-counted |
| Canonical Section-123 exceptional-face payment (2) | canonical | full-core route; source points are not silently deleted |
| Angular-defect pruning loss (5) | proved conditional | follows from the stated `5.317D+o(D)` budget and cutoff `K/D` |
| Low-degree pruning loss (6) | proved conditional | counts removed edge occurrences against the full `1.8488D+o(D)` train ceiling |
| Bounded phase diameter after pruning | proved conditional | graph-distance packing plus the explicit minimum-degree hypothesis |
| Three-window bad capacity | conditional | requires the proof-only Section-118 phase lift and bad-train theorem |
| Endpoint inequality (3) | proved conditional | occurrence-counted endpoint charge; no Euler path or boundary injectivity assumed |
| Mantel excess inequality (4) | proved conditional | simple triangle-free crossing graph; exact scalar root test |
| Safe-window multi-grain exclusion | conditional / unreviewed | complete scalar proof, but inherited carrier extraction is proof-only |
| All Type-II full-core minimizers are in the safe window | not proved | the current sharp envelope permits slack above `0.0088` |
| Type-I inactive chamber/cap is globally impossible | not proved | local activation and contact-minimality arguments lack core relocation or source-preserving descent |
| Target A endpoint `d_sc\ge\Delta_\Lambda` | open | exact response-to-source deficiency bridge remains missing |
| Target B global shell inequality | open | multi-grain/global transfer and source-level contradiction remain missing |
| Level I | not proved | no uniform threshold and no every-minimizer conclusion |

## 6. Adversarial regression checks

The proposed scalar argument was tested against the following failure modes. The
listed regressions are not being used as positive theorems.

| Regression | Result | Precise limitation retained |
| --- | --- | --- |
| Locally jammed but non-global packings | pass | local equilibrium/contact creation does not imply global diameter optimality |
| Dense isolated fillings | pass | quadratic inactive population can survive shell statistics; isolates are outside the core affine kernel |
| Near-equilateral triangle-free/sheared lattices | pass | no fixed density loss or uniform angle gap follows from local near-rhombic geometry |
| Full-rank planar response matrices | pass | full rank does not by itself produce the Target A source-to-Schur deficiency |
| Overlapping Hall circuits | pass | separate Hall obstructions need not yield simultaneous Schur nullity |
| Fixed-hull Hall capacity | pass | recounting the same hull cannot create missing source capacity |
| Individually feasible exchanges | pass | pairwise feasible exchanges need not be jointly compatible |
| Boundary-order losses | pass | the proof counts route occurrences and never reduces them to one simple integer |
| Bridges/repeated vertices | pass | endpoint and outer-walk counts retain multiplicity |
| Contact-isolated points | pass | no isolate coordinate is inserted into the core response/kernel calculation |
| Universally zero KKT multipliers | pass | no infinitesimal zero multiplier is integrated into a finite release |
| Incident diameter edges | pass | no Euler path is inferred from incidence alone |
| Rejected FB4 force-bulk localization | pass | positive force or bulk contact is not converted into a source-preserving competitor |
| Incompatible-cut C53 pentagon | pass | its missing compatible cut is not smuggled into the phase argument |
| RSR disk-equality uniqueness | pass | equality in a disk inequality is not assumed for a non-disk source |
| Eppstein near-equality | pass | near-quadrangulation does not provide the missing global minimizer bridge |
| Five-host angular saturation | pass | occupancy saturation does not force an exact unit triangle without its full hypotheses |
| Inward-pocket/exterior-Reuleaux cap | pass | cap containment alone does not control the diameter-carrying core |
| Withdrawn `r/(6 C_T)` sharpness claim | pass | no withdrawn constant is used |
| Full-source ZR/ZF extension | pass | the affine kernel is used only on the nonisolated positive-contact core |
| Rejected PR #191 coefficient | pass | no unpromoted numerical coefficient is used as a theorem |
| Finite `(q=13)` S1 object | pass | it is treated only as a regression, not as a global-minimizer result |

Two exact 2026-09-14 regressions are particularly binding. The scalar-ledger
compatibility witness has positive aggregate outer detour and zero exceptional
perimeter while satisfying the listed scalar equalities, so scalar elimination
alone cannot close Sections 122–123. The vanishing-shear lattice family has
triangle-free contacts and asymptotically optimal planar density up to boundary
order while its rhombus angle gap tends to zero; it blocks density-only and
uniform-angle-gap closures. Neither is a global-minimizer construction.

## 7. Literature imports

No external theorem is imported into the proof. The official problem page was
checked only to confirm that the underlying Erdős Problem #99 is still presented
as open: <https://www.erdosproblems.com/99>. The Bezdek–Fodor paper
“Minimal Diameter of Certain Sets in the Plane,” JCTA 85 (1999), 105–111,
was checked only as historical finite context (it determines finite cases such as
the known \(n=8\) result); it supplies no large-\(n\) every-minimizer theorem:
<https://www.sciencedirect.com/science/article/pii/S0097316598928898>.

## 8. Computation

### Exact scalar certificate

```text
python3 research/verify_target_c_multigrain_endpoint_capacity_exact.py
```

This uses only `fractions.Fraction`. It checks the outward-rounded retained edge
floor, the negativity of the Mantel polynomial at \(S=0.9499\), and the exact
endpoint margin \(2(0.9499)-1.8693=0.0305\). It omits every geometric and
global-optimality hypothesis.

### Floating-point diagnostic

```text
python3 research/target_c_multigrain_endpoint_capacity.py
```

It reports retained edge mass `0.4698250992764395`, forced excess
`0.9499104771157691`, and route margin `0.0305209542315383`. These values are
diagnostic only; the exact rational script is the certificate for the scalar
sign.

### Related safe-window checks

```text
python3 research/verify_target_c_sparse_split_fullcore_closure.py
python3 research/verify_target_c_correlated_slack_sharp_118.py
python3 research/verify_target_c_protected_contact_creation.py
python3 research/verify_target_c_stress_transversal_reinsertion.py
python3 research/verify_target_c_phase_component_endpoint_closure.py
python3 research/verify_target_c_inactive_chamber_activation_grid_regression.py
python3 research/verify_target_c_inactive_chamber_core_coupling_regression.py
```

The first two reproduce the proof-only safe-window margins and the current
Section-118 slack envelope. The next three reproduce finite contact,
stress-transversal, and phase-component checks. The last two reproduce exact
inactive-chamber regressions. None certifies source-preserving reinsertion,
global optimality, or Level I.

## 9. Corrections / supersessions

This report does not supersede a canonical theorem and does not alter the state
version. It corrects the possible overreading of the existing multi-grain note:
the endpoint-capacity contradiction is a conditional scalar result, not a
canonical C-II closure. It also preserves the distinction between the exact
scalar-ledger compatibility regression and an actual geometric survivor. The
vanishing-shear family is a regression only and is not a disproof sequence.

No claim is made that a locally feasible contact release integrates to a finite
motion, that a scaffold is embeddable as the full source, or that a selected
representative controls every original minimizer.

## 10. Promotion recommendation

**conditional**

The scalar proof and its exact rational sign certificate are complete. The result
should remain noncanonical because its carrier extraction, phase lift, and
safe-window return theorem are proof-only or otherwise scoped inputs. No
`state_version`, route map, active prompt, or canonical theorem module should be
updated from this report. If a future independent audit promotes the inherited
extraction, only the safe-window subbranch should be updated; the high-slack
full-core and Type-I branches must remain open.

## 11. Handoff

1. **Strongest result:** a conditional multi-grain endpoint-capacity exclusion of
   the proof-only \(\sigma\le0.0088\) full-core carrier window, with exact scalar
   margin `0.0305`.
2. **Canonical dependency chain:** `C-ZRF` → `C-ATTACH-CURRENCY` →
   `C-LOADED-HULL` → `C-FULLCORE-NEAR-DISK` → `C-HARMONIC-CELL-TILING` →
   `C-CORRELATED-SLACK-RETURN` / `C-AGGREGATE-TWO-ARC-DETOUR` →
   `C-AUGMENTED-CELL-DEFECT-BUDGET`; the sparse/directional and multi-grain
   endpoint steps remain proof-only.
3. **Exact remaining lemma:** handle every high-slack full-core survivor by an
   embedded detour bound, exact triangle, or finite source-preserving strict
   diameter decrease; independently eliminate the macroscopic inactive
   chamber/exterior cap with the same source/cardinality guarantees.
4. **Binding dead routes:** scalar-only detour elimination, density-only angle
   gaps, contact creation without core movement, full-source ZR/ZF extension,
   and local response rank without a source-deficiency bridge.
5. **Files to read next:** `docs/targets/target-c/84-typeII-interface-collapse-audit.md`,
   `docs/targets/target-c/85-train-boundary-interface-currency-audit.md`, the
   current Target A Section-177 modules, and `docs/targets/target-b/README.md`.
