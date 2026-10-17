> Generated reading edition · [exact source](../../../docs/audits/target_c_normalized_contact_isometry_interpolation_independent_audit_2026-10-08.md) · source SHA-256 `8c358cbb9749ccf31828298806f0ca4aced3b8d75ac8a295a23cbd82ebb361e3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A7FD7BE58B92","canonical":true,"claim_ids":["C-CONTACT-ISOMETRY-SPARSE-STRESS-BARRIER","C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD","C-TWO-VALUED-SLAB-INTERPOLATION-BLOCKER"],"claim_statuses":{"C-CONTACT-ISOMETRY-SPARSE-STRESS-BARRIER":"canonical","C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD":"canonical","C-TWO-VALUED-SLAB-INTERPOLATION-BLOCKER":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: normalized contact-isometry interpolation barriers

Date: 2026-10-08. Audit base: `origin/main=fcd7ef1ee5cd4368c2475615616c5aa263e0d543`, state `2026-10-08.audit.120`; Target C C-II remains open.

Frozen source: `origin/swarm/sol/contact-convexity-exclusion-20261002` at `b79aa0cfd8ceb2d10685890fe06b12a71607745b`. Source artifact `docs/reports/target_c_finite_core_rigidity_and_cut_anchoring_2026-10-02.md`, SHA-256 `3e28bda1b7b64d86a220d77aae1ee036a4cd47770a1ef9ead556082669bbc99d`. This audit covers only Section 5.2 and Theorem 5.3 of Section 5.3. Later source claims remain unaudited.

## Verdict

**PASS — promote** `C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD`, `C-CONTACT-ISOMETRY-SPARSE-STRESS-BARRIER`, and `C-TWO-VALUED-SLAB-INTERPOLATION-BLOCKER`, at the separate scopes below. The identities exactly characterize the old contact and core-diameter rows along one specified normalized straight interpolation. They do not check inactive full-source pairs or provide an endpoint. The slab result rules out this interpolation rescue when the stated two-valued endpoint has an old-diameter blocker.

## Exact statements and scope

Use the canonical contact-minimal, then actual-diameter-pair-minimal triangle-free global minimizer with `D>=9`. Let `V` be the nonisolated positive-contact core, `P` its coordinate matrix, `C` its actual contact edges, and `H` its actual diameter pairs. Let `Q` be any planar placement of `V` preserving every old contact exactly, and put `U=Q-P`. Define

```text
c_e = |U_i-U_j|^2                  (e in C)
c_* = max_C c_e
a_h = |U_i-U_j|^2                  (h in H)
g_h = |Q_i-Q_j|^2-D^2              (h in H)
s(t) = 1-t(1-t)c_*
R_i(t) = (P_i+tU_i)/sqrt(s(t)).
```

For every `0<t<=1` with `s(t)>0`, the old core contact squared length before normalization is exactly `1-t(1-t)c_e`; after normalization every old core contact has length at least one. For each old core diameter pair `h`, its normalized length is strictly below `D` if and only if

```math
\boxed{g_h+(1-t)(D^2c_*-a_h)<0.}
```

This is an exact finite family of linear tests in `t`, plus `s(t)>0`. It tests only old contacts and old diameter pairs on `V`. Every other source pair, including pairs involving contact isolates, still needs its own lower and upper check before `R(t)` can be a full-source competitor.

Set

```math
E_C=\sum_C\alpha_ec_e,\qquad E_H=\sum_H\beta_ha_h,
\qquad G=E_C-E_H=\operatorname{tr}(U^T\Omega U)\ge0,
\qquad A_*=D^2c_*-E_C\ge0.
```

The `beta`-weighted sum of the left sides of the diameter tests is exactly

```math
A_*-t(A_*+G).
```

If `A_*+G>0`, simultaneous strict shortening of every old core diameter requires

```math
\boxed{t>\frac{A_*}{A_*+G}.}
```

If `A_*+G=0`, the weighted sum is zero for every `t`, so simultaneous strict shortening is impossible. The threshold is necessary, not sufficient; it is source- and move-dependent and has no uniform lower bound. Also, if a contact-isometry is affine in the source, its core stress energy is zero. Hence a noncongruent contact-isometry that does not lengthen any old core diameter cannot be affine: otherwise positive diameter weights and the zero weighted slack force every old diameter length to remain `D`, and `C-MIXED-CORE-FINITE-RIGIDITY` gives congruence.

For the stress-mass refinement, let (F_C={ein C:c_e>0}) and

```math
f_C=\frac{\sum_{e\in F_C}\alpha_e}{D^2}.
```

Whenever the threshold is defined,

```math
\boxed{\frac{A_*}{A_*+G}\ge1-f_C.}
```

Here `f_C` is moved contact **stress mass**, not a fraction of contact edges; no lower bound on individual stress coefficients or source-independent stress-mass estimate follows.

For the two-valued slab restriction, suppose all core displacements have values in `{0,Delta}` with `Delta!=0`, at least one old contact crosses the two classes, and some old core diameter has `g_h>=0` at the endpoint. Then (c_*=|\Delta|^2), every (a_h\in\{0,|\Delta|^2\}), and for `D>1`

```math
D^2c_*-a_h\ge(D^2-1)|\Delta|^2>0.
```

For the blocked old diameter, the strict test is positive at every `0<t<1` and equals `g_h>=0` at `t=1`. Thus no parameter in the normalized straight interpolation strictly shortens all old core diameters. If `g_h=0`, every interior interpolant has diameter greater than `D` on that pair. The statement is conditional on the exact two-class endpoint assignment; it does not extract such an endpoint from a source or move isolates for it.

## Independent proof reconstruction

For an old contact vector `r=P_i-P_j` and displacement difference `d=U_i-U_j`, both endpoint lengths are one. The polarization identity gives

```math
|r+td|^2=(1-t)|r|^2+t|r+d|^2-t(1-t)|d|^2
       =1-t(1-t)c_e.
```

Since `c_e<=c_*`, division by the positive `s(t)=1-t(1-t)c_*` gives a squared length at least one.

For an old diameter edge, put `r=P_i-P_j` and `d=U_i-U_j`. Then `|r|^2=D^2`, `|d|^2=a_h`, and `|r+d|^2=D^2+g_h`. Another polarization identity gives

```math
|r+td|^2=D^2+t g_h-t(1-t)a_h.
```

Comparing this with (D^2s(t)=D^2-t(1-t)D^2c_*), subtracting and dividing by `t>0` gives exactly the displayed strict test. Its linearity in `t` is literal; only positivity of `s(t)` is an additional nonlinear domain restriction.

From Audit.120,

```math
\sum_H\beta_h g_h=-G,
\qquad \sum_H\beta_h=1,
```

so the weighted test sum is

```math
-G+(1-t)(D^2c_*-E_H)
=(1-t)A_*-tG
=A_*-t(A_*+G).
```

Positive `beta_h` makes this sum strictly negative whenever every row test is strict. This proves the necessary threshold. If `c_*>0`, then `A_*+G=D^2c_*-E_H<=D^2c_*`; also (A_*=\sum_C\alpha_e(c_*-c_e)\ge(1-f_C)D^2c_*). Dividing by the positive threshold denominator proves the stress-mass bound; the zero-`c_*` case has `A_*+G=0` and is excluded by “whenever the threshold is defined.”

For a two-class displacement, every edge displacement difference is either zero or `Delta`; a crossing old contact therefore makes `c_*=|Delta|^2`, while every diameter displacement difference is also either zero or `Delta`. The displayed positive margin then makes the blocked row test fail strictly for all interior `t`; at `t=1` it is exactly `g_h>=0`.

Finally, if `Q=b+TP` is affine, each coordinate column lies in `ker Omega`, so (G=0). If no old diameter lengthens, every `D^2-|Q_i-Q_j|^2` is nonnegative; positive weights and the stress identity force all old diameter lengths to remain `D`. Exact contacts and diameters then invoke finite mixed-core rigidity. This verifies the affine exclusion without any common lattice or full-source affine assumption.

## Adversarial scope and exact checks

- The exact square rhombus endpoint in the source has `c_*=2/5`, `E_C=E_H=2/5`, `A_*=2/5`, and `G=0`, so the threshold requires `t>1`. One old diameter is lengthened to squared length `16/5` while the other shortens to `4/5`. This square has `D=\sqrt2` and is only a finite arithmetic check, not a canonical-source instance. It is consistent: noncongruence alone is not the affine-exclusion hypothesis because an old diameter lengthens.
- If `s(t)<=0`, `R(t)` is not defined; no feasibility conclusion is attached to those values.
- New contacts, inactive lower pairs, inactive upper pairs, contact isolates, and any source labels outside `V` are outside the row identities. They remain mandatory checks for an actual source competitor.
- The mass bound charges multiplier mass, not number of moved edges. It cannot be turned into a count without new multiplier information.
- The slab statement rules out only this straight normalized interpolation. It does not rule out nonlinear or multi-axis endpoint motions, a different normalization, or a finite move that changes the exact contact graph.
- Audit.97's common-angle half-angle threshold concerns a different path. It neither subsumes this exact straight-interpolation identity nor supplies its endpoint assumptions.

The frozen source verifier `research/verify_target_c_finite_core_rigidity_2026_10_02.py` (SHA-256 `5005feac3244fe835262a9c5f1671631da7ca4403a288856f08267ea932f18b0`) was inspected and rerun under Python 3 with SymPy exact arithmetic. Its square calculation checks the interpolation identity, weighted threshold, stress-mass bound, and the two-valued-blocker specialization on one exact example. This is a finite arithmetic check, not evidence for the universal identities. The proof above supplies those identities directly.

## Dependencies and disposition

| Claim | Verdict | Canonical dependencies |
| --- | --- | --- |
| Restored normalized interpolation row identity, necessary threshold, and affine-endpoint exclusion | PASS — promote `C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD` | `C-FINITE-CONTACT-ISOMETRY-DIAMETER-GAIN`, `C-MIXED-CORE-FINITE-RIGIDITY` |
| Moved-contact-stress-mass lower bound for the threshold | PASS — promote `C-CONTACT-ISOMETRY-SPARSE-STRESS-BARRIER` | `C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD` |
| Two-valued slab endpoint blocker for normalized straight interpolation | PASS — promote `C-TWO-VALUED-SLAB-INTERPOLATION-BLOCKER` | `C-NORMALIZED-CONTACT-ISOMETRY-INTERPOLATION-THRESHOLD` |
| Feasibility of a full-source endpoint, inactive-pair checks, or a global strict sub-`D` competitor | Not claimed | — |
| C-II or Level I closure | NOT CLAIMED; both remain open | — |

These theorems eliminate one proposed interpolation rescue only after a two-valued endpoint with a nonshortened old diameter has been produced. They supply no such endpoint and leave the current C-II obligation unchanged.
