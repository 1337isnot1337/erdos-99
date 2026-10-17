> Generated reading edition · [exact source](../../research/target_c_cut_gram_nullity_and_finite_deficit_2026-10-02.md) · source SHA-256 `7064906a964e4a5ecc71934b32378613f4a95d4e134581bbdfbcff34821b684a`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8214e1e1ed2b1cedd86e05a12025c893c4a3c8c5", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_cut_gram_nullity_and_finite_deficit_2026-10-02.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "e9f7778d52f86ad678df90aabc7ed247d8bd8decd8f5355da086805e58ca9d83"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — exact cut-Gram nullity and finite diameter turnover

`cut-Gram nullity determined by untouched contact directions -> strict finite
weighted diameter deficit -> new source-pair activation/diameter turnover at any
feasible nontrivial endpoint -> strict competitor if those blockers are excluded`

**Date:** 2026-10-02  
**Starting checkout HEAD:** `78a65968d51af7871a0ce5a865bf2db1a2c2e0ec`  
**Fetched research base:** `fbeae9b3fa18a63e07573676b4e2e512a91ca4d5`  
**State version:** `2026-09-14.audit.51`  
**Source branch:** `swarm/root/threshold-stress-compatibility-20261002`  
**Source tip:** `935d96cc0aaee8e7c3b619fdbb253a9411f7d997`  
**Mission:** couple source equilibrium/PSD to the full finite train chart, rather
than infer a release from a private gap-tree basis row. No coordination issue or
individual assignment was present in the fetched open issue list.  
**Classification:** unreviewed proof candidate; conditional application to
unpromoted train cuts; exact regression against curvature-only closure. This
salvage preserves research content only and does not promote any premise or claim.  
**Active prompt:** [current Target C prompt](../docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md)  
**Literature:** no new import.

**LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Authority and dependencies

Canonical inputs are [C-I restoration](../docs/targets/target-c/56-ci-restored-frontier.md)
and [Section 57](../docs/targets/target-c/57-zr-zf-rigidity-audit.md): on the
nonisolated positive-contact core (V), a relative-interior normalized stress has

```math
 \Omega=L_C(\alpha)-L_H(\beta)\succeq0,
 \quad \ker\Omega=\operatorname{span}\{\mathbf1,P_x,P_y\},
 \quad \alpha_e,\beta_h>0,
 \quad \sum_h\beta_h=1,
 \quad \sum_e\alpha_e=D^2.
 \tag{1}
```

All contact-isolated source points are retained. They are moved by their actual
cut memberships, and their pair constraints are checked when feasibility is
asserted. They are absent from (1); no full-source affine-kernel assertion is used.

The geometric cut hypotheses below are stated explicitly. Their application to
complete O--O stopped trains uses the unpromoted
[finite multishear](target_c_global_outer_train_exact_multishear_2026-09-15.md)
and its [audit](target_c_global_outer_train_exact_multishear_hostile_audit_2026-09-15.md),
which establish the full-source cutset formula. The current threshold application
also uses the proof-only [paired staircase](../docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md)
and [transverse rails](../docs/reports/target_c_exact_phase_threshold_transverse_rail_saturation_2026-10-01.md).
No unpromoted extraction is treated as canonical.

Two fetched proof-only packets were inspected, without importing them as premises:
`4e1017c4`, edgewise KKT packets, and `32fc39b3`, two-cut cross-shore escape.
The results here do not depend on either new packet theorem.

## 2. Uniform contact cuts and the exact scalar Gram kernel

Let (k) cuts of the full source have indicators $`\chi_i\in\{0,1\}`$.
Restrict these indicators to (V), and let (X_{vi}=\chi_i(v)).
For each (i), assume the contacts crossing cut (i) form a nonempty set (C_i).
Assume the (C_i) are pairwise disjoint and that a contact in (C_i), oriented
from $`\chi_i=0`$ to $`\chi_i=1`$, has the same unit vector (u_i).
Every other selected indicator is constant across that contact. Let

```math
 C_0=C\setminus\bigcup_i C_i,
 \quad a_i=\sum_{e\in C_i}\alpha_e,
 \quad \sigma_{hi}=\chi_i(y_h)-\chi_i(x_h),
```

where each actual diameter (h=x_hy_h) has an arbitrary fixed orientation.
Put

```math
 W=X^T\Omega X
   =\operatorname{diag}(a_i)
     -\sum_{h\in H}\beta_h\sigma_h\sigma_h^T.
 \tag{2}
```

The equality follows by expanding Laplacian energies. A contact contributes to
at most one cut, and its nonzero indicator difference is $`\pm1`$.

### Theorem CG.1 — exact nullity classification

Let $`U_0=\operatorname{span}\{p_y-p_x:xy\in C_0\}`$, with the empty span
equal to $`\{0\}`$. Then

```math
 \boxed{\ker W=
   \{(g\cdot u_i)_{i=1}^k:g\in U_0^\perp\}},
 \qquad
 \boxed{\dim\ker W=2-\dim U_0.}
 \tag{3}
```

In particular (W\succ0) exactly when the untouched contacts contain two
nonparallel directions. This is an exact finite statement, not an asymptotic
phase estimate or a generic-rank assertion.

**Proof.** Since $`\Omega\succeq0`$, (z^TWz=0) is equivalent to
$`Xz\in\ker\Omega`$. By (1), this means

```math
 (Xz)_v=b+g\cdot p_v\quad(v\in V)
 \tag{4}
```

for some (b\in\mathbb R), (g\in\mathbb R^2).
Across any untouched contact, (Xz) has zero difference, so (g\in U_0^\perp).
Across an oriented contact of (C_i), its difference is exactly (z_i), hence
$`z_i=g\cdot u_i`$.

Conversely choose (g\in U_0^\perp) and put $`z_i=g\cdot u_i`$.
Across every contact, the difference of (Xz) equals the difference of
$`g\cdot p`$. The core contact graph is connected, so these two functions differ
by a constant. Thus (4) holds and (z\in\ker W).

The displayed map from (g) is injective: if all $`g\cdot u_i=0`$ and
$`g\in U_0^\perp`$, then (g) is perpendicular to every contact vector.
Connectivity would put all core points on one line unless (g=0); the canonical
force hull is two-dimensional. This proves both parts of (3). $`\square`$

### Consequences for actual train families

An untouched strict rhombus supplies the two independent directions needed in
(3). More generally two adjacent untouched nonparallel contacts suffice.

In a complete (A\times B) rectangle with (n\ge3), select two (B)-trains
and leave every other train unchanged. An unselected (B)-train crosses any
(A)-train in an untouched strict rhombus. Thus the two-coordinate cut Gram is
positive definite, regardless of whether the two selected phases are equal.

For the family of **all** actual O--O stopped trains, any bounded nonquadrilateral
face has at least two nonparallel boundary-contact directions. Each such contact
is a terminal occurrence at a bounded stopping host, so its train is not O--O.
Consequently the complete O--O cut Gram is positive definite whenever at least
one bounded nonquadrilateral face exists. This conclusion uses the audited stopped
train interpretation, not a renaming of arbitrary equal-direction contacts.

If every contact is selected instead, (3) gives nullity exactly two. In particular
one must not claim that the scalar cut Gram is universally positive definite.

## 3. Angular curvature has a finer kernel than the scalar Gram

Let (J) denote quarter-turn rotation, and set

```math
 S_{ij}=W_{ij}(u_i\cdot u_j).
 \tag{5}
```

For rates (c_i), the full-core velocity is
$`v_x=\sum_i\chi_i(x)c_iJu_i`$. Its two coordinate fields give

```math
 \boxed{c^TSc=(v^{(1)})^T\Omega v^{(1)}
                  +(v^{(2)})^T\Omega v^{(2)}\ge0.}
 \tag{6}
```

Equality holds exactly when there are a matrix (A\in\mathbb R^{2\times2})
and a vector (b) with (v_x=b+Ap_x) on (V). Equivalently,

```math
 \boxed{A r_e=0\ (e\in C_0),\qquad
        A u_i=c_iJu_i\ (1\le i\le k).}
 \tag{7}
```

Necessity follows by taking contact differences of the affine velocity.
For sufficiency, the differences prescribed by (7) agree with the cut velocity
on every contact, and connectivity makes their difference constant.
Thus (7) is a complete kernel test, without an omitted global compatibility
condition.

In particular (S\succ0) if the untouched directions span the plane.
It is also positive definite if the untouched directions have rank one but
the selected directions not parallel to that line include two distinct
projective directions: a matrix killing the untouched direction has rank at most
one; its image would have to lie in two distinct lines $`\mathbb R Ju_i`$,
and is therefore zero.

When every contact is selected, (7) says (u_i^TAu_i=0) for all (i).
If at least three projective contact directions occur, the symmetric part of
(A) is zero because its homogeneous quadratic has at least three projective
zeros. The only zero angular mode is common rotation. If exactly two directions
occur, the kernel has dimension two: common rotation and the affine oblique-angle
flex. The contact directions span the plane, so these cases exhaust that regime.

The weighted diameter (t^2) coefficient in GM.13 is exactly **minus** (6).
This supplies the sign missing from the proof-only identity, under canonical
PSD. It does not turn a negative weighted curvature into diameter descent.

## 4. Exact finite weighted deficit

For arbitrary angles $`\theta`$, use the full-source contact-preserving placement

```math
 q_x=p_x+\sum_i\chi_i(x)\Delta_i,
 \quad \Delta_i=(R_{\theta_i}-I)u_i.
 \tag{8}
```

Every old contact remains exactly unit for **every** angle vector. This is
because its relative displacement is either zero or exactly its own $`\Delta_i`$.
Feasibility of strict source-pair constraints is a separate issue.

Write $`d_x=q_x-p_x`$. Since $`\Omega p^{(1)}=\Omega p^{(2)}=0`$, (1) gives

```math
 \boxed{\sum_{h\in H}\beta_h|q_{y_h}-q_{x_h}|^2
   =D^2-\sum_{i,j}W_{ij}\Delta_i\cdot\Delta_j.}
 \tag{9}
```

Indeed the difference between the old contact and diameter weighted squared sums
is the two-coordinate $`\Omega`$-energy of (q). Old contacts sum to (D^2),
and the same energy is the energy of (d), which is the final term in (9).
No Taylor remainder appears.

If (W\succ0), every nontrivial angle vector modulo $`2\pi`$ has a strictly
positive deficit. More precisely, with $`\lambda=\lambda_{\min}(W)>0`$,

```math
 \boxed{D^2-\sum_h\beta_h|r_h(\theta)|^2
      \ge2\lambda\sum_i(1-\cos\theta_i).}
 \tag{10}
```

There is no asserted uniform lower bound for $`\lambda`$ over sources or stresses.

The exact deficit may be strict even when (W) is singular: its complete zero
condition is that both coordinate vectors $`(\Delta_i^{(a)})_i`$ lie in
the kernel (3). One must check this condition rather than conflate (5) with (2).

## 5. Global-normal-form consequence: finite diameter turnover

Assume (W\succ0). Suppose a nontrivial endpoint of (8) satisfies **all** full-source
unit-separation and diameter bounds. Then it is a global minimizer of diameter
(D). If it creates no new contact, it has exactly the original minimal contact
count. Let (k_{\rm lost}) be the number of old diameter pairs made strict.
Equation (9) implies $`k_{\rm lost}\ge1`$. Secondary diameter-pair minimality
therefore forces

```math
 \boxed{\#\{\text{previously inactive pairs now at distance }D\}
       \ge k_{\rm lost}.}
 \tag{11}
```

Thus **every** feasible nontrivial finite endpoint either creates a new unit
contact or replaces at least as many diameter pairs as it loses. This conclusion
uses the actual secondary normalization and retains isolated source points.
It does not assert that any nontrivial feasible endpoint exists.

Furthermore the feasible angle set has empty interior and measure zero on the
parameter torus. Away from the trivial angle vector, every feasible point lies
on a new-contact or new-diameter equality for some originally inactive source
constraint. Each equality is a proper real-analytic zero set: at the original angle
vector that distance constraint was strict. A finite union of those zero sets has
measure zero. This is an all-amplitude statement about the prescribed chart,
not merely the local mixed-rigidity conclusion.

The remaining source-level obligation is exact: construct a nontrivial finite
endpoint satisfying every full-source pair inequality, with no new contacts and
fewer new diameter pairs than lost old ones, or force an exact unit triangle in
the unavoidable contact blockers. Equations (9)--(11) alone do not provide it.

## 6. Exact regression: positive stress and negative curvature still allow a cusp

Take the six vertices of the unit-radius regular hexagon,

```math
 p_j=(\cos(j\pi/3),\sin(j\pi/3)),\quad j=0,\ldots,5.
```

Its only unit contacts are the six consecutive sides; its only diameter pairs
are the three antipodal pairs, all of length (2). The contact graph has no
triangle. Set $`\alpha_e=2/3`$, $`\beta_h=1/3`$. These are a normalized,
strictly positive **full vertex-equilibrium** stress, with $`\sum\alpha=4`$.
The exact matrix has $`\Omega^2=2\Omega`$, rank three, and precisely the affine
kernel. In particular it satisfies the PSD/kernel inputs, not merely projected
stationarity.

For (i=0,1,2), put
$`S_i=\{i+1,i+2,i+3\}`$ modulo six. Cut (i) crosses exactly sides (i)
and (i+3), both with the same oriented unit vector
$`u_i=p_{i+1}-p_i`$. These three uniform contact cuts partition the contacts.
They are **not** complete O--O stopped trains: the hexagon is a bounded stopping
face and each side is a separate stopped-train terminal. No source-extraction
claim is made for this example.

The scalar Gram for all three cuts has nullity two. Selecting any two leaves one
untouched contact direction, so its scalar Gram has nullity one while its angular
matrix is positive definite. Selecting one leaves two untouched directions and
both matrices are positive definite. These realize all three nullity cases of
(3) and the distinction between scalar and angular kernels.

For cut zero alone, translate (S_0) by $`(R_\theta-I)u_0`$.
Every old contact stays unit. The three old diameter squares are exactly

```math
 4+2\sqrt3\sin\theta,\qquad
 4-2\sqrt3\sin\theta,\qquad 2+2\cos\theta.
 \tag{12}
```

Their weighted average is

```math
 4-\frac23(1-\cos\theta)<4
 \quad(\theta\notin2\pi\mathbb Z),
 \tag{13}
```

yet their maximum is at least $`4+2\sqrt3|\sin\theta|`$.
All initially strict pair inequalities persist for sufficiently small angles,
so the actual source diameter has a strict cusp at zero in this chart.
Full equilibrium, PSD, maximal affine kernel, exact contact preservation, and
strict negative weighted curvature therefore do **not** imply a local diameter
decrease. Global optimality and the actual stopped-train extraction are not
certified here; no finite example is presented as a Level I disproof.

The unit square supplies the separate equality regression: a cut across its two
horizontal contacts has (a=w=1), and its indicator is an affine coordinate.
Strict single-cut domination without the affine-kernel/geometric qualification
is false.

## 7. Relation to older rejected and unpromoted assertions


**Source formatting excerpt (unbalanced inline math in the original):**

```text

The old [ZS report](../docs/reports/target_c_zs_strict_terminal_cut_domination_2026-09-09.md)
already states strict Boolean terminal cuts under the full affine kernel. This
is **not** claimed as a new theorem here. Its statement can be reconstructed
from canonical Section 57 after Kron reduction: the Schur complement has affine
kernel on the loaded terminals, and a nonconstant Boolean affine function would
place all terminals on two parallel lines, containing at most four extreme
vertices. The canonical bound gives at least six terminals for (D\ge9\).
```



Consequently the single-cut (a_i>w_i) sign previously withheld in the
proof-only [interval identity](target_c_interval_shear_kkt_curvature_identity_2026-09-15.md)
and GM.16 follows directly from canonical PSD/ZR for such a source. This does
not rehabilitate any unrelated old ZK population, transfer, or quantitative-gap
claim. The genuinely new statements of this report are the **entire cut-Gram
kernel classification**, the **angular kernel classification**, their
**all-amplitude finite deficit**, and the **finite turnover/measure-zero**
consequences under the specified cut hypotheses.

## 8. Computation and adversarial audit

The accompanying exact verifier checks the hexagon's 15 pair distances, full
vertex equilibrium, matrix PSD/affine kernel, every nonempty subset of its three
uniform contact cuts, both kernel classifications, the finite identities
(12)--(13), and the square equality regression. Arithmetic is exact in
$`\mathbb Q(\sqrt3)`$, with symbolic rational rotation parameters.

It does not encode global optimality, source extraction, large-cardinality
asymptotics, isolated population, or inactive-pair exclusion. Those are not
numerically inferred.

Executed verification:

```text
python3 research/verify_cut_gram_finite_deficit_2026_10_02.py
python3 tools/check_theorem_state.py --base-ref fbeae9b3
git diff --check
```

The exact verifier and final state/whitespace checks pass. The starting base had
28 missing generated report headers and a stale artifact index; regenerating them
adds conservative unreviewed metadata only. No claim lifecycle or canonical
mathematical statement is changed by that regeneration.

| Assertion | Classification | Decisive check |
| --- | --- | --- |
| CG.1 scalar nullity | proved candidate awaiting promotion | PSD zero energy, affine core kernel, connected contact differences |
| Angular kernel (7) | proved candidate awaiting promotion | both coordinate energies and affine velocity contact differences |
| Finite deficit (9) | proved candidate awaiting promotion | exact old contact lengths and annihilation of original coordinates |
| Complete O--O (f>0) strictness | conditional | audited cutset and bounded stopping-host interpretation |
| Two-cut rectangle strictness | conditional | actual complete rectangle supplies untouched rhombus |
| Finite turnover (11) | proved candidate awaiting promotion | full-source feasibility and both lexicographic minimalities |
| Negative curvature implies descent | rejected | exact regular-hexagon cusp, with full positive vertex equilibrium |
| Universal strict scalar cut Gram | rejected | two affine scalar zero modes when every contact is selected |

Stars and paths are not ruled out by rank. Isolates are not deleted. No inactive
pair is silently made active. No infinitesimal argument is promoted to finite
feasibility. The macroscopic inactive-container/exterior-cap branch, split-star
O--O branches, inactive interfaces, open witness cells, and other higher-surplus
full-core sources remain outside any closing conclusion here.

## 9. Frontier and promotion disposition

Preserve as an unreviewed proof candidate and regression packet. No canonical
state, prompt, or theorem version is changed. The next proof attack is to remove
the actual newly active pair alternatives in (11) for a finite two-shore move;
the exact stress deficit cannot substitute for that source-pair theorem.

Read next: the current finite block-transposition report and the original-pair
blocker classification, together with the complete full-source cut formula.
