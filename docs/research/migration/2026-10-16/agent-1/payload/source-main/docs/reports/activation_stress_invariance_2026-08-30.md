<!-- theorem-state: {"artifact_id":"ART-2AE1901BACC0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Erdős Problem #99 — activation stress-polytope invariance

**Date:** 2026-08-30  
**Repository state:** main `82a4348577f01011cbba056a169b5a8ac9d11cd2`; work branch `research/activation-stress-invariance-2026-08-30`  
**Run type:** closing-proof / audit  
**Target:** A  
**Active prompt at run start:** `docs/prompts/erdos_problem_99_1.7.2_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The canonical Target A endpoint is

\[
\dim\ker S\ge \Delta_\Lambda-d_{\rm int},
\]

equivalently

\[
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
\]

Sections 142–145 produce a globally optimal monotone activation sequence and a large
independent activation-edge forest. Section 152 then shows that activation rank plus
fixed diameter and coherent local monomer incidence does not force scaffold nullity
without global minimum-diameter optimality.

The tempting remaining implication was

```text
large activation rigidity rank
-> positive/compensating first-order KKT stress on the new activation constraints
-> boundary-response dependence
-> Schur nullity
```

The present run disproves the first arrow for the canonical activation normalization,
even though every configuration in that normalization is a global minimizer.

## 2. Strongest genuinely new audited theorem

### Theorem: KKT-stress invariance under monotone activation

Let

\[
A_0,A_1,\ldots,A_s
\]

be the sequence supplied by Theorem 142.1. At step \(i\), one currently strict
rattler \(r_i\) moves while all other points remain fixed, every old active pair
persists, and exactly one new active pair \(e_i\) is created.

For each \(i\), let \(\mathcal K_i\) be the normalized KKT-stress polytope of
Theorem 4.1. Then:

1. the multiplier of \(e_i\) is zero in every element of
   \(\mathcal K_{i+1}\);
2. restriction to old active pairs is a canonical bijection
   \[
   \mathcal K_{i+1}\cong\mathcal K_i,
   \]
   with inverse given by zero-extension on \(e_i\);
3. consequently
   \[
   \mathcal K_s\cong\mathcal K_0,
   \]
   and every active pair created anywhere in the activation sequence has multiplier
   zero in every terminal normalized KKT stress;
4. every point that was a strict rattler in \(A_0\) is absent from the positive
   contact- and diameter-stress support of every terminal normalized KKT stress.

### Scope

This theorem concerns the exact globally optimal activation sequence of Theorem 142.1.
It is a first-order KKT statement. It does not assert that the new constraints are
kinematically irrelevant: they remain present in the active Jacobian and can shrink the
critical cone. It does not identify the source with the independent smaller optimum or
produce a Schur-kernel vector.

### Proof

Fix one step and let \(r=r_i\). Since \(r\) is strict in \(A_i\), it is incident to
no active unit or diameter pair of \(A_i\). Theorem 142.1 creates exactly one new
active pair and preserves every old active pair. Therefore \(r\) is incident to
exactly one active pair \(e_i\) in \(A_{i+1}\).

If \(e_i=rv\) is a unit contact, Theorem 142.1 says that \(r\) has no diameter
neighbor. The KKT equilibrium equation (4.2) at \(r\) is

\[
\alpha_{e_i}(p_r-p_v)=0.
\]

Since \(p_r-p_v\ne0\), every normalized KKT stress has
\(\alpha_{e_i}=0\).

If \(e_i=rv\) is a diameter pair, \(r\) has no unit neighbor and (4.2) becomes

\[
0=\beta_{e_i}(p_r-p_v),
\]

so every normalized KKT stress has \(\beta_{e_i}=0\).

All old active pairs avoid \(r\), and every point other than \(r\) is fixed during
the step. Hence every old active-pair vector is geometrically identical in \(A_i\)
and \(A_{i+1}\). After deleting the forced-zero new coordinate, the equilibrium
equations at fixed points are exactly those for \(A_i\), the equation at \(r\) is
\(0=0\), and the normalization \(\sum\beta=1\) is unchanged. Thus restriction maps
\(\mathcal K_{i+1}\) into \(\mathcal K_i\).

Conversely, any normalized KKT stress of \(A_i\) extends to \(A_{i+1}\) by assigning
zero to \(e_i\); the same unchanged active-pair vectors satisfy all equilibrium
equations and the diameter normalization. Restriction and zero-extension are inverse.
This proves the stepwise bijection.

Iteration gives \(\mathcal K_s\cong\mathcal K_0\) and forces every created active
pair to have zero multiplier in every terminal stress. An initially strict rattler had
no active incident pair in \(A_0\), so every terminal active pair incident to it was
created during the sequence and hence has zero multiplier. This proves item 4.
\(\square\)

### Dependencies

- `docs/theory/01-local-structure.md`, Theorem 4.1: normalized KKT equilibrium stress
  exists for every global minimizer.
- `docs/targets/target-a/03-source-response.md`, Theorem 142.1: globally optimal
  monotone activation creates exactly one active pair at each step while preserving all
  old active pairs.
- `docs/targets/target-a/03-source-response.md`, Lemmas 144.1 and 145.1: the unit
  activation trace contains an activation-edge forest whose rigidity rows are
  independent.

No external theorem or computation is used.

### Why it is new

Sections 142–145 record the activation count, forest structure, and rigidity rank but
stop at the warning that rank is not nullity. Section 152 supplies a non-global
geometric regression. The present theorem uses the exact global-minimizer activation
sequence and proves the stronger stress statement that the full normalized KKT-stress
polytope is invariant and every newly created constraint is universally zero-stressed.
That statement is not recorded in the active modules at the run-start commit.

## 3. Exact target implication

Combining Lemma 145.1 with the new theorem gives the exact coexistence

\[
\operatorname{rank}R_{F_{\rm act}}=|E(F_{\rm act})|
\]

and

\[
\alpha_e=0
\qquad
(e\in E(F_{\rm act}))
\]

for every normalized terminal KKT stress. With the quantitative activation bound,

\[
|E(F_{\rm act})|
\ge
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H-2\pi D\}}{2}
\right\rceil,
\]

this can be a large exact rigidity-rank contribution with zero KKT load.

Therefore the direct route

\[
\text{activation rank}
\Longrightarrow
\text{positive KKT stress on activation rows}
\Longrightarrow
\text{Schur dependence}
\]

is dead for the canonical activation normalization. A surviving activation-to-Schur
argument must use information outside the normalized first-order KKT stress polytope.

The Target A endpoint itself is unchanged.

## 4. Exact remaining lemma

If the activation route is retained, the next useful statement must use unweighted
constraint geometry or the global source/scaffold coupling rather than stress weights.
One exact form would be:

> **Activation-geometry-to-response transport.** From the global-optimum activation
> sequence and its independent active-constraint rows, derive at least
> \(s=\Delta_\Lambda-d_{\rm int}\) independent failures of the
> \(C^\partial\to O\) alternating linkage, without assigning positive KKT weight to
> the activation edges.

Equivalently, prove

\[
\dim\ker S\ge s
\]

from the finite geometry/critical-cone/source-to-scaffold relation rather than from
positive activation stress.

The result of this run gives no such transport.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| New activation pair has zero KKT multiplier at birth | proved | It is the moved strict rattler's only active incident pair, so equilibrium forces its multiplier to zero. |
| Terminal KKT-stress polytope is canonically identical to the initial one | proved | Stepwise restriction and zero-extension are inverse because all old active-pair vectors are unchanged. |
| Every activation-forest edge is zero-stressed in every terminal KKT stress | proved | Induction over the stress-polytope bijections. |
| Activation edges are kinematically redundant | rejected | Zero multiplier does not remove their active-Jacobian rows or critical-cone inequalities. |
| Activation rank cannot ever imply Schur nullity | rejected | The theorem only kills the direct first-order KKT-stress compensation mechanism. |
| Target A is solved | rejected | No Schur rank bound or strict smaller-diameter competitor is obtained. |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Section 152 activation/monomer family | yes | That family is not globally minimum-diameter optimal and need not possess the canonical KKT structure. The new theorem instead applies to the exact global-minimizer sequence of Theorem 142.1. |
| Unit-square positive-stress warning | yes | The square has no strict-rattler activation sequence of the required kind; the theorem is vacuous there and does not forbid positive stress on pre-existing contacts. |
| Section 139.1 two-leaf cage | yes | The cage concerns first-transition exchange geometry, not monotone strict-rattler activation. No conclusion about its Schur response is asserted. |
| Full-rank planar response / cage-to-Schur no-go | yes | The theorem does not infer a Schur kernel from stress invisibility. It explicitly leaves the source-to-response transport open. |
| Long straight chains / caged branch junctions | yes | Such new contacts may constrain the critical cone while remaining zero-stressed. The theorem does not claim movability. |

## 7. Failed routes and no-go results

### Direct activation-rank-to-KKT-load compensation

1. Proposed implication: independent activation rows force compensating positive KKT
   load in a globally optimal terminal representative.
2. Failure point: every new active pair is born at a vertex with no other active
   incident pair, forcing its multiplier to zero; stress-polytopes are then preserved
   exactly by induction.
3. Scope: dead for the canonical monotone activation sequence and any argument that
   requires positive normalized first-order KKT weight on the created pairs.
4. Durable consequence: large activation rigidity rank and global optimality coexist
   with universal zero KKT load on all activation rows.

This does not kill critical-cone, finite-amplitude, or direct source-to-scaffold uses of
the activation geometry.

## 8. Literature imported

None.

## 9. Computation and reproducibility

No computation was used. The result is purely algebraic from Theorems 4.1 and 142.1.

## 10. Canonical promotion recommendation

**Promote now** — the proof is complete and materially changes the activation-rank
frontier.

Files to edit:

- add `docs/targets/target-a/07-activation-stress-invariance.md`;
- update `docs/targets/target-a/README.md`;
- update `docs/README.md` section-range status;
- refresh the active continuation prompt so the naive KKT-compensation attack is no
  longer listed as open;
- retain this report as the audit/provenance record.

No literature or research script changes are required.

## 11. Next run

The highest-value activation-specific theorem is the activation-geometry-to-response
transport stated in Section 4. It must use the global finite geometry, critical cone,
or actual source/scaffold relationship, because positive KKT stress on the activation
forest is now proved impossible in this normalization.

Outside the activation route, the exterior-compatible monomer gap-concentration and
locked-cage-to-Schur transport attacks remain unaffected and should now rank above any
ordinary KKT-stress compensation attempt.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strongest new theorem:
For the exact monotone activation sequence of global minimizers from Theorem 142.1,
the normalized KKT-stress polytope is invariant at every step. The newly created
active pair has multiplier zero in every KKT stress, restriction to old active pairs
is a bijection, and therefore every activation pair is zero-stressed in every terminal
KKT stress. All initially strict rattlers remain universally outside positive stress
support.

Exact endpoint now:
dim ker S >= Delta_Lambda - d_int remains open.

Binding new no-go:
Large activation rigidity rank plus global optimality does not force positive KKT load
on the activation forest. The direct activation-rank -> positive KKT stress -> Schur
nullity route is dead for the canonical activation normalization.

Highest-value next lemma:
Transport the unweighted/global activation geometry (or another source invariant),
not activation stress weights, into at least s independent failures of the boundary
alternating linkage; alternatively prioritize exterior-compatible monomer gap
concentration or locked-cage-to-Schur transport.

Authoritative files:
docs/targets/target-a/07-activation-stress-invariance.md
docs/targets/target-a/README.md
docs/theory/01-local-structure.md (Theorem 4.1)
docs/targets/target-a/03-source-response.md (Sections 142-145)
```
