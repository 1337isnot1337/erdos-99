> Generated reading edition · [exact source](../../../docs/audits/target_c_joint_orbit_capacity_energy_g0050_hostile_audit_2026-09-15.md) · source SHA-256 `1a349d108940a61ce1309aba58c77fc3dfd5a23af220f9dd677445afcc8c4bf9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-7585ACE156BB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — `g=0.0050` joint orbit-capacity / phase-energy floor

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_iterative_pruning_conditional_pair_payment_2026-09-14.md`
- `research/target_c_iterative_minimax_phase_star_atomic_gap_0050_2026-09-14.md`
- `research/verify_target_c_iterative_minimax_atomic_gap_0050.py`
- `research/target_c_joint_orbit_capacity_energy_g0050_2026-09-15.md`
- `research/verify_target_c_joint_orbit_capacity_energy_g0050.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks two possible failure points: whether the old side-branch atomic gap `g=0.0050` is actually strong enough and scoped correctly to replace the merged `0.00042` input, and whether the merged joint orbit-capacity/phase-energy theorem remains valid under that substitution. Both pass.

---

## 1. The `g=0.0050` input is independently load-bearing

The imported iterative-pruning pair theorem does not merely tune a previous numerical optimization. After the phase-inversion cover, it prunes the residual missing graph iteratively across both shores. Each residual missing edge disappears at its first deleted endpoint and therefore pays for at most one pruning deletion. This gives the total residual pruning loss

$$
\sqrt{2v}\,D+o(D)
$$

rather than two separately charged `sqrt(v)D` losses.

The resulting exhaustive pair branches are

$$
\rho\ge {g_*^2\over10}
$$

or

$$
\rho\ge {2m_*^2\over29}.
$$

For train families bounded by `2/sqrt(3)`, positive pair excess satisfies `g_*<=m_*`, so both branches imply the unconditional physical inequality

$$
\boxed{
\rho\ge {2\over29}(a+b-2/\sqrt3)_+^2.
}
$$

The inequality direction is correct: `1/10 > 2/29`, so the minimum of the two branch lower bounds is still at least `2g_*^2/29`.

**Verdict:** PASS.

---

## 2. The matched minimax theorem really proves `0.0050`

The dominant three-phase calculation uses the same triangle-free two-leaf correlation as the earlier hostile-audited minimax route. The only replaced input is the stronger unconditional pair theorem above.

The exact outward rational verifier covers a strict superset of the center-imbalance domain with 15,000 rational intervals. It proves a worst-case leaf lower bound exceeding the geometric cap `2/sqrt(3)` by more than

$$
0.0015.
$$

This is far larger than the final `0.0000578...` distance between the claimed `0.0050` gap and the non-load-bearing numerical ceiling of the architecture.

The theorem is also rerun on the strict-rhombus train graph rather than inferred by deleting singleton trains after an all-train argument. Thus the matched consequences

$$
{T-q/2\over D}\ge2\sqrt{\Delta_2}+0.0050-o(1),
$$

$$
{T_R\over D}\ge2\sqrt{\Delta_2}+0.0050-o(1),
\qquad
{\sigma_R\over D}\ge0.0100-o(1)
$$

are valid at the stated proof-only scope.

**Verdict:** PASS.

---

## 3. The merged joint-orbit theorem is symbolic in `C0`

The merged joint orbit-capacity/phase-energy proof uses

$$
C_0\le C={T-q/2\over D}\le U
$$

and then derives

$$
2\delta+\kappa/2\le 4.5t-2\pi-C_0.
$$

Its exact dominant-orbit lower bound is

$$
K_*(t,\delta,\kappa)
=\pi+\delta-t-\kappa-2U+{8\Delta_2\over U}.
$$

Its route dual is

$$
\delta\ge\Phi(K_*),
\qquad
\Phi(z)=z-6\arcsin(\tanh(z/6)).
$$

None of these derivations uses `0.00042` except through the numerical assignment of `C0`. Replacing the old lower bound by the stronger hostile-audited value

$$
C_0=2\sqrt{\Delta_2}+0.0050
$$

therefore preserves every inequality.

**Verdict:** PASS.

---

## 4. Atomic orbit mass is not silently assumed

A dangerous shortcut would be to infer an exact three-point atomic orbit from only pairwise concentration near projective separation `pi/3`. The current argument does not do that.

Canonical hostile-audited Section 168 already proves, after the finite-to-limit atomization repair, that the entire limiting strict-rhombus crossing mass is carried by exact atomic `pi/3` orbits:

$$
\sum_r E_r=\Delta_2.
$$

The dominant-orbit estimate

$$
M\ge {4\Delta_2\over C}
$$

therefore remains legitimate. The stronger `C0` changes only the scalar feasible interval, not the atomization theorem.

**Verdict:** PASS.

---

## 5. The two-parameter minimization still occurs at maximal detour

With the stronger `C0`, the feasible region is

$$
2\delta+\kappa/2\le R_{50}(t).
$$

At fixed `t,delta`,

$$
\partial K_*/\partial\kappa=4\Delta_2/U^2>0,
$$

so `Phi(K_*)-delta` is minimized at `kappa=0`.

At fixed `t,kappa`,

$$
{\partial K_*\over\partial\delta}
=5+{16\Delta_2\over U^2}
\le
5+{16\Delta_2\over C_0^2}
=8.9790809080\ldots<9.
$$

For the relevant orbit masses `K<1.33`,

$$
\Phi'(K)=1-\operatorname{sech}(K/6)<0.025.
$$

Hence

$$
{\partial\over\partial\delta}
[\Phi(K_*)-\delta]
<9(0.025)-1<0.
$$

The easiest feasible point is therefore still

$$
\kappa=0,
\qquad
\delta=R_{50}(t)/2,
\qquad
U=C_0.
$$

The verifier gives the sharper derivative product

$$
0.21618\ldots<1.
$$

**Verdict:** PASS.

---

## 6. The one-variable root and claimed rounding are safe

At the boundary endpoint define

$$
K_{50}(t)
=\pi+R_{50}(t)/2-t-2C_0+8\Delta_2/C_0
$$

and

$$
H_{50}(t)=\Phi(K_{50}(t))-R_{50}(t)/2.
$$

The exact derivative relation

$$
K_{50}'(t)=5/4
$$

and `Phi'<0.025` give

$$
H_{50}'(t)<0.
$$

The independent high-precision certificate checks

$$
H_{50}(1.82515)
=2.5373341\times10^{-5}>0,
$$

$$
H_{50}(1.82516)
=3.1640100\times10^{-6}>0,
$$

$$
H_{50}(1.82517)
=-1.9045315\times10^{-5}<0,
$$

and brackets the zero by

$$
1.82516142463113334<t_*<1.82516142463113335.
$$

The theorem claims only

$$
\boxed{t\ge1.82515-o(1),}
$$

leaving more than `2.5e-5` contradiction margin at the displayed round endpoint.

The verifier originally used exact equality for one derived `Decimal` identity. That was correctly repaired: the expression differs from its algebraic decimal value by only `2e-99` because the decimal square roots are rounded, and the code now checks an outward `1e-95` tolerance. This is a certificate implementation issue only and does not affect any mathematical margin.

**Verdict:** PASS.

---

## 7. Scope and non-conclusions

The result remains proof-only. It depends on the proof-only iterative-pruning atomic theorem and the proof-only merged joint orbit-capacity/phase-energy theorem. It does not mutate canonical theorem state, prove an exact unit equilateral triangle, or construct a strict same-cardinality sub-`D` competitor.

The joint route relaxation has already optimized the simultaneous local inequalities

$$
d_i\ge n_i g_i,
\qquad
d_i\ge n_i-s_i.
$$

The remaining gap is structural, not another algebraic recombination of those same two costs. The most plausible next interfaces are dominant-orbit terminal routing, outer-to-outer train bracing, exceptional-face closure rank, and simultaneous train shears.

**Final disposition:** **PASS at proof-only full-core Type-II scope. C-II and Level I remain open.**
