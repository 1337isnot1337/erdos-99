> Generated reading edition · [exact source](../../../docs/audits/target_c_fullcore_endpoint_unbalanced_pseudosegment_completion_independent_audit_2026-09-14.md) · source SHA-256 `a29bccfc6edacbef9042a887f38c6fcd6974b8cc11fd5af23f29ac4dee837325`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AFA8613E806D","canonical":true,"claim_ids":["C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION"],"claim_statuses":{"C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — full-core floor endpoint unbalanced pseudosegment completion

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-14.audit.50
**Target:** Target C-II / Level I
**Audited artifact:** docs/reports/target_c_fullcore_endpoint_unbalanced_pseudosegment_completion_2026-09-14.md
**Status:** independent audit supporting canonical promotion in state `2026-09-14.audit.50`

## Audit conclusion

The endpoint-exclusion proof is mathematically sound after two corrections now
recorded in the report:

1. right-angle crossings are not assumed to follow the arbitrary phase-cut
   orientation; they are charged separately to the O(D) angular-defect budget;
2. the global phase cut has width pi/3, so an additional O(D^(1/4)) phase-tail
   deletion is made before invoking the Section-76 common-cone theorem.

Subject to the canonical endpoint package and the exact hypotheses listed below,
the report proves

    no canonical full-core Type-II sequence has mu_D -> mu_TC,

where

    mu_TC = (2*pi + 2*sqrt(pi/(2*sqrt(3))))/5.

This is not a Level-I closure: it removes only convergence to the lower endpoint
of the full-core scalar floor. Together with the canonical floor, it gives a
qualitative but non-explicit uniform gap above that floor. It does not eliminate
higher-surplus full-core sequences or the macroscopic-container branch.

The gap is qualitative and non-explicit; no numerical value or effective threshold
is claimed.

## 1. Exact audited statement

Assume a sequence of canonical contact-minimal, then diameter-pair-minimal,
triangle-free global minimizers with D tending to infinity in the full-core
no-macroscopic-container branch, and assume

    mu_D -> mu_TC.

Use the full source throughout. Contact-isolated points remain in the source;
they are not train vertices, but they remain available in the source hull and
in the definition of D.

The audited conclusion is:

    contradiction.

The proof is asymptotic and sequence-level. It does not assert a finite threshold
uniform over all cardinalities or all minimizers.

## 2. Dependency audit

### 2.1 Canonical inputs

The proof uses the following canonical results with their current scopes.

- C-FULLCORE-NEAR-DISK: the Type-II full-core branch and near-disk/rhombic
  saturation, with all source points retained.
- C-FULLCORE-TRAIN-SURPLUS-FLOOR: the scalar lower bound
  liminf mu_D >= mu_TC in the full-core near-disk branch.
- C-TRAIN-INTERFACE-CURRENCY / canonical Section 85: the finite train boundary
  inequalities, including the occurrence-counted identity T_D=B_D/2 and
  R_D <= T_D^2/4.
- C-PUNCTURED-PHASE / canonical Section 68: a phase cut deleting
  F_D=O(D) crossing pairs, with reduced phases x_tau in one interval of width
  L=pi/3 and retained oriented crossings satisfying x_v-x_u=delta_e>0.
- The canonical train pseudosegment theorem: two train curves cross at most once
  and no three have a common crossing point.
- C-HOLE-GRID-DIAMETER / canonical Section 76: the finite source-hull
  diameter inequality for a complete phase-pure forward grid, including holes
  and repeated boundary occurrences.

The external theorem is Fox–Pach–Suk, Theorem 2.10, whose exact statement was
checked in the primary arXiv HTML source:
https://arxiv.org/html/2312.01028v1
It concerns equal-size red/blue pseudosegment families of size n with at
least epsilon*n^2 crossings and produces complete crossing subfamilies of
size at least epsilon^c*n. It has no packing or diameter conclusion; that
conclusion is supplied separately by Section 76.

### 2.2 Endpoint equality package

The report-level endpoint calculation is rechecked here. Put

    Delta_2 = pi/(2*sqrt(3)),
    p_D/D -> pi,
    R_D/D^2 -> Delta_2.

The exact loaded-hull identity and canonical component currency give

    mu_D - (q_D-k_D)/D = (m_B - 2*c_I - 4)/D.

At a sequence with mu_D -> mu_TC, the train-coupled weighted lower-bound proof,
with nonnegative gaps, gives

    m_B/D -> 0,
    (Q_D-f_D)/D -> 0,
    (q_D-k_D)/D -> mu_TC,
    (b_D-p_D)/D -> 0,
    f_D/D -> (4*sqrt(Delta_2)-pi)/5,
    c_I/D -> 0.

The occurrence-counted train inequalities then squeeze

    T_D/D -> 2*sqrt(Delta_2).

Since each strict rhombus is one crossing edge and the train graph is triangle-free,

    R_D/T_D^2 -> 1/4.

No equality or uniformity stronger than these sequence limits is used.

## 3. Mantel and three-label allocation audit

For the phase-cut crossing graph, e_D=R_D-O(D), so e_D/T_D^2 tends to 1/4.
The elementary degree-square argument gives a partition X_D union Y_D with

    |X_D|, |Y_D| = T_D/2 + o(T_D),

    internal edges = o(T_D^2),

    missing cross edges = o(T_D^2).

Let x_i and y_i be the three label populations on the two sides. Same-label
pairs are never retained crossings, so

    sum_i x_i*y_i = o(T_D^2).

Therefore sum_i min(x_i,y_i)=o(T_D). Passing to a normalized subsequence,
the positive label supports on the two sides are disjoint subsets of a
three-element set. The largest class on each side is therefore at least T_D/4
in the limiting normalization, and their labels are distinct. More precisely,
for A_D and B_D the largest distinct-label classes,

    |A_D|+|B_D| >= 3*T_D/4 - o(T_D),
    min(|A_D|,|B_D|) >= T_D/4 - o(T_D).

The second inequality follows because if one side has support size two, each
of its two positive coordinates can be as small as one quarter of T_D; if it
has support size one it is one half. The maximizing labels cannot agree,
because each is at least T_D/6 before the support-disjoint limit, and an equal
label would create Theta(T_D^2) forbidden cross pairs.

The Mantel missing-cross-edge count then yields

    |A_D||B_D| - e(A_D,B_D) = o(T_D^2).

This is a relative crossing density 1-o(1) because both shores are linear.

## 4. Unbalanced extraction audit

Fox–Pach–Suk Theorem 2.10 is stated only for equal red and blue sizes. The
report's cloning reduction is valid:

- replace every red curve by b sufficiently close parallel copies and every
  blue curve by a sufficiently close parallel copies, where a and b are the
  original shore sizes;
- choose the perturbation small enough that every clone pair crosses exactly
  when the corresponding originals cross;
- the cloned color classes both have size ab and remain a pseudosegment family;
- at least epsilon*(ab)^2 cloned pairs cross if the original density is epsilon;
- Theorem 2.10 gives complete clone shores of size at least epsilon^c*ab;
- projection to originals gives complete original shores of size at least
  epsilon^c*a and epsilon^c*b.

At the endpoint epsilon=1-o(1), this is (1-o(1)) of each original shore.
The cloned curves are a proof device only; no clone is treated as a source
point or packing competitor.

## 5. Phase-lift and forbidden-orientation audit

Let L=pi/3 and choose fixed labels with ell_B-ell_A=+1 modulo three.
For an actual crossing write d=x_B-x_A. The two possible orientation equations
from phi_v-phi_u = L+delta modulo pi are exactly:

    d = delta,        if the crossing is oriented A -> B;
    d = L-delta,      if it is oriented B -> A.

Thus every strict reverse-oriented pair has d>L/2 and is one of the pairs
whose positive reduced phase arc contains the selected cut point. Such pairs
belong to the deleted set F_D.

At d=L/2 the arbitrary right-angle orientation may disagree with the chosen
A-to-B direction. Each such pair has delta=L/2, so the total O(D) defect budget
gives at most 2*Delta_train/L=O(D) equality pairs. Therefore

    H_D={actual A-B crossings with d>=L/2}

has O(D) edges.

The graph H_D is a chain graph: after ordering A by x_A, the neighborhoods
are nested threshold sets {B:x_B>=x_A+L/2}. A chain graph with m edges has
matching number nu satisfying m>=nu(nu+1)/2, hence has a vertex cover of size
at most sqrt(2m). Deleting this cover removes every wrong/equality orientation
while losing O(sqrt(D))=o(D) trains from the complete actual biclique.

Every remaining pair is a retained forward crossing and satisfies

    delta_AB = x_B-x_A > 0.

No assumption that an arbitrary O(D)-edge graph has an o(D) cover is made; the
threshold/chain structure is essential.

## 6. Section-76 phase-bin audit

Section 76 requires the selected reduced phases to lie in one interval of
width strictly less than L/2. The original report now supplies this missing
step.

For the complete forward grid let

    S=sum_{a,b}(x_B-x_A) <= C_phase*D.

Set x_A^+=max x_A, x_B^-=min x_B and define

    g=x_B^- - x_A^+,
    r_A=x_A^+ - x_A,
    q_B=x_B - x_B^-.

Then

    x_B-x_A = g+r_A+q_B,

with all terms nonnegative. Since both shores are Theta(D),

    g=O(D^-1), sum r_A=O(1), sum q_B=O(1).

Delete rows with r_A>D^-1/4 and columns with q_B>D^-1/4.
Only O(D^1/4)=o(D) tracks are removed. The remaining phase interval has
width O(D^-1/4)<L/2. A new representative of the reduced phase circle is
chosen on that short interval; this changes no actual crossing relation or
label. Section 76 therefore applies with its exact common-cone and
common-order hypotheses.

The Section-76 defect term is still bounded by C_phase*D because the remaining
grid rhombi are a subset of the actual source rhombi.

## 7. Final sign audit

After all o(D) deletions,

    a_D+b_D >= 3*T_D/4-o(T_D),
    min(a_D,b_D) >= T_D/4-o(T_D).

Section 76 gives

    D >= (sqrt(3)/2)(a_D+b_D)
         - S/min(a_D,b_D) - 2.

The defect term is O(1). Also

    (a_D+b_D)/D >= (3/4)*(2*sqrt(Delta_2))-o(1)
                 = (3/2)*sqrt(Delta_2)-o(1).

Thus the leading coefficient is

    (sqrt(3)/2)*(3/2)*sqrt(Delta_2)
    = (3*sqrt(3)*sqrt(Delta_2))/4 > 1

because Delta_2=pi/(2*sqrt(3)) > 16/27. The elementary bounds pi>3 and
sqrt(3)<2 imply Delta_2>3/4>16/27. Hence D >= (1+eta)D-O(1),
a contradiction for large D.

The inequality is a contradiction with the diameter of the original full
source. Section 76 uses centers of actual rhombi, which lie in the convex hull
of their four source vertices; the convex-hull diameter is D. No scaffold
diameter is substituted.

## 8. Regression audit

| Regression | Result | Reason |
| --- | --- | --- |
| Random near-complete bipartite graph | irrelevant | Fox–Pach–Suk supplies only the pseudosegment extraction; the graph is not used as a geometric source |
| Branched train crosscuts | pass | No interval assumption is made; the external theorem handles arbitrary pseudosegments |
| Holes/interfaces | pass | Section 76 is explicitly hole-stable; no dual-tree or single-boundary assumption is used in the final route |
| Right-angle rhombi | pass | Equality pairs are separately bounded by the angular-defect budget |
| Phase-tail outliers | pass | O(D^(1/4)) rows/columns are deleted before Section 76 |
| Contact-isolated points | pass | Retained in the full source and its convex hull |
| Local positive stress | irrelevant | No infinitesimal-to-finite deformation is used |
| Source/scaffold mismatch | pass | The final diameter inequality is applied to actual rhombus centers in the source hull |
| Source cardinality | irrelevant to this endpoint exclusion | The contradiction is D(source) >= (1+eta)D(source), not a replacement source |

## 9. Remaining status

The audited theorem excludes sequences with mu_D converging to mu_TC. Together
with the canonical floor, it also gives the exact quantifier statement

    exists epsilon_*>0 exists D_*>0 such that every canonical full-core
    minimizer with D>=D_* has mu_D >= mu_TC+epsilon_*.

Indeed, if this failed, choose for each j a full-core minimizer with D_j>=j and
mu_{D_j}<mu_TC+1/j. The floor gives liminf mu_{D_j}>=mu_TC, so the chosen
sequence converges to mu_TC, contradicting endpoint exclusion. The value of
epsilon_* is not explicit. The theorem still does not exclude liminf mu_D above
mu_TC+epsilon_*. The macroscopic
inactive chamber/exterior-cap branch remains open. Therefore:

    Level I: STILL OPEN
    Target C-II: OPEN, with exact floor endpoint removed and a non-explicit
    qualitative gap above it.

## 10. Promotion recommendation

The exact theorem is promoted as canonical ID
`C-FULLCORE-FLOOR-ENDPOINT-EXCLUSION` in state `2026-09-14.audit.50`. The
report remains the detailed proof artifact; the theorem-state entry carries only
the exact sequence-level conclusion and scope.

The primary literature citation for the imported theorem is:
https://arxiv.org/html/2312.01028v1
