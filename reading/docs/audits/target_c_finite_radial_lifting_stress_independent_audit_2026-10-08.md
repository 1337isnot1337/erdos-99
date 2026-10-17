> Generated reading edition · [exact source](../../../docs/audits/target_c_finite_radial_lifting_stress_independent_audit_2026-10-08.md) · source SHA-256 `48443134c18b7660f99522c65d2063ce7de4472d43724ede8e45293b53ad98ab`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-4ACDFD74B1F0","canonical":true,"claim_ids":["C-FINITE-SORTING-PACKET-RADIAL-LIFTING-STRESS"],"claim_statuses":{"C-FINITE-SORTING-PACKET-RADIAL-LIFTING-STRESS":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — finite radial-lifting stresses for selected sorting packets

**Date:** 2026-10-08  
**Audit base:** ca26397adb06a7335458d603d852eb465d61e28c, state 2026-10-08.audit.143.  
**Target:** C-II; C-II and Level I remain open.  
**Frozen source:** research/sol/target-c-overnight-closure-20261007 at c6a75bd708e553c4feb3a540e0b17f3b65e22a82.  
**Source report:** docs/reports/target_c_sorting_radial_lifting_finite_stress_checkpoint_2026-10-07.md, SHA-256 15c1e7e97fe8be17cf9bf4546a2cd35f8a104f673bf11391e67ae42fa637a139.  
**Frozen source verifier:** research/verify_target_c_sorting_radial_lifting_stress_2026_10_07.py, SHA-256 beb2669b771364f6877f79e20dde47b8ddb3ee58eed76f8df5a694eac0be6915.  
**Saved source certificate:** research/target_c_sorting_radial_lifting_stress_certificate_2026_10_07.json, SHA-256 854b47a986c78bbc42f4b66e226a4c6b7bd6ec726891ab12a788fb03098e0a10.

## Verdict and exact scope

**PASS — promote the finite certificate at its listed cases only.** It gives exact positive pinned equilibrium stresses for 33 specified sorting packets. It proves no all-$`M`$, all-permutation, or uniform-curvature assertion.

Let $`A_M=(M-1,M-3,\ldots,-M+1)`$. The listed cases are:

- $`M=4`$, every permutation of $`A_4=(3,1,-1,-3)`$;
- $`M\in\{6,8,10\}`$, the descending and ascending orders of $`A_M`$, and the order formed by listing its even-indexed entries followed by its odd-indexed entries.

For each order $`(\tau_0,\ldots,\tau_{M-1})`$, set $`t=\tan(\theta/2)=1/(200M^2)`$. Use the exact sorting packet in the canonical sorted-rate packet regression: in one sector, with $`u=1`$, $`v=e^{i\pi/3}`$, $`w=v-u`$, and $`z_h=e^{i\tau_h\theta}`$, its sites are

```math
p_{r,j}=\left(\sum_{h<r}z_h\right)u+\left(\sum_{h\in I_{r,j}}z_h\right)w,
```

where $`I_{r,j}`$ indexes the $`j`$ smallest rates among $`\tau_0,\ldots,\tau_{r-1}`$, for $`0\le j\le r\le M`$. Rotate through the six sectors and identify shared radial-edge sites. For triangular-chart address $`(i,j)`$, write

```math
\rho(i,j)=\max(|i|,|j|,|i+j|),
```

and lift each site to $`H(p)=\rho(i,j)^2`$.

For every listed packet, the piecewise-affine face gradients give an exact pinned equilibrium stress on the complete set of unit contact rows touching an interior (moving) site. All $`6M^2`$ such rows receive positive weights. Each moving vertex is in exact equilibrium. The $`3M(M-1)`$ internal nonunit diagonals have zero gradient jump; the $`6M`$ outer wall rows have both endpoints pinned. Ring weights lie in $`[2,3]`$, radial weights are at least $`1`$, weak weights exceed $`t`$, and the total weight is below $`30M^2`$.

All arithmetic is exact in $`\mathbb Q(\sqrt3)`$. Since $`\theta=2\arctan(t)`$, $`0<\theta<1/(100M^2)`$; the theorem is only at this one parameter for each listed case.

## Independent reconstruction and hostile support check

On each triangular face the audit replay solves the two affine-gradient equations for the vertex heights. Across a shared oriented edge $`e`$, the two face gradients agree tangentially; their difference is therefore $`\lambda_e J(e)`$. It computes this coefficient exactly, checks $`\lambda_e=0`$ on every internal nonunit diagonal, and checks $`\lambda_e>0`$ on every unit edge in the triangulation. It then sums the signed $`\lambda_e e`$ forces at each moving vertex and verifies exact zero.

The frozen source verifier's stress loop alone did not compare its support with every actual unit pair at the larger sampled curvature. I therefore added the registered audit checker research/verify_target_c_radial_lifting_support_audit_2026_10_08.py. It enumerates all source pairs from the same exact coordinates, verifies every pair is at least one apart, reconstructs the triangle-edge support, and checks that every actual unit pair incident to a moving vertex belongs to an internal supported edge. It finds exactly $`6M^2`$ such contacts in every case and zero omitted contacts. The boundary-only $`6M`$ unit contacts are on the pinned outer wall.

The frozen source verifier was run at the immutable source tip; its output matched the saved JSON byte-for-byte. Its old import expected a three-argument helper API that has since narrowed on main. The canonical replay research/verify_target_c_sorting_radial_lifting_stress_2026_10_07.py therefore embeds the frozen exact geometry constructor; it preserves the source stress calculation. The added support checker and replay both pass on the promotion base.

Aggregate exact checks over the 33 cases:

| Quantity | Count |
| --- | ---: |
| Point-pair distance comparisons in stress replay | 302,076 |
| Independent contact-census point-pair comparisons | 302,076 |
| Total point-pair distance comparisons in the support-check run | 604,152 |
| Triangular faces | 5,904 |
| Internal gradient-jump checks | 8,352 |
| Positive moving-involving unit rows | 5,904 |
| Zero nonunit-diagonal jumps | 2,448 |
| Moving-vertex equilibrium sums | 2,481 |
| Actual moving-involving unit rows omitted from the stress | 0 |

The support checker reruns the stress reconstruction for each case and separately repeats the exact pair-distance enumeration to assess complete-contact coverage; the table distinguishes the two full pair passes.

## Scope limits and canonical disposition

These packets contain actual unit equilateral triangles. The result is not a triangle-free source, does not give a strict energy gap, and says nothing about global optimality or canonical source extraction. In particular, finite positivity cannot be extrapolated to all $`M`$, all rate orders, or an interval of curvature. It does not change C-II.

Promote C-FINITE-SORTING-PACKET-RADIAL-LIFTING-STRESS as an exact finite reusable certificate for the packet construction also used by C-SORTED-RATE-NESTED-ENERGY-EQUALITY-REGRESSION. This audit reproduces the coordinates and rechecks feasibility and full support rather than importing the regression's conclusion. Keep the proposed uniform radial-lifting continuation unreviewed.
