> Generated reading edition · [exact source](../../../docs/audits/target_c_nested_hexagon_packet_stress_independent_audit_2026-10-06.md) · source SHA-256 `144a67c17a894105913e2915240e55f2b4ed8f6409feca0a8b24e8c7dc5c1e6a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-85193030A3F7","canonical":true,"claim_ids":["C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND"],"claim_statuses":{"C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: nested-hexagon stress and energy demand

Date: 2026-10-06. Source branch: `research/sol/target-c-owner-order-closure-20261006`, immutable snapshot `d9404c4974b4f0c699a49c49a0450c9752e83182`. Source report: [`target_c_nested_hexagon_packet_stress_energy_obligation_2026-10-06.md`](../reports/target_c_nested_hexagon_packet_stress_energy_obligation_2026-10-06.md).

**Verdict: PASS — promote the exact selected-stress and necessary per-ring energy theorem.** The numerical LP discovery and any energy upper bound remain exploratory/unproved. The theorem is a local kinematic statement about a specified limiting triangular-lattice packet and six fixed-direction guards. It says nothing about extracting that chart from a canonical source.

## Exact statement

Let M >= 3, R = M-1, and let P_R = {i u + j v : |i|, |j|, |i+j| <= R}, where u=(1,0) and v=(1/2,sqrt(3)/2). Define rays e_k = Rot(k pi/3)u for k=0,...,5, and six guard points M e_k.

For r=1,...,R, let S_r consist of the unit edges around the radius-r hexagonal ring and the six radial chains from r e_k through R e_k to M e_k. Let S_0 consist of the six radial chains from the center through R e_k to M e_k. Give every edge in each S_r weight one.

Suppose the packet and guards are the initial points of a one-sided C2 feasible family, every pair in S_r remains at distance at least one for small theta >= 0, and each guard has expansion

    q_k(theta) = M e_k - C theta^2 e_k + o(theta^2),
    C = M(M^2-1)/6.

Then for every r=0,...,R, all first variations on S_r vanish and

    E_r(d) = sum over ij in S_r of |d_i-d_j|^2 >= 12C = 2M(M^2-1),

where guard velocities are zero. The union of all selected supports has exactly 3M(M+1) distinct rows, including the six guard edges. No conclusion is asserted for unselected rows.

## Independent reconstruction

For a positive-radius ring, each noncorner vertex has opposite selected ring gradients. At a corner on ray e_k, the two ring gradients sum to e_k, canceled by the outward radial edge gradient -e_k. At later vertices of each selected spoke chain, the two selected gradients are opposite. For S_0, the six gradients at the center sum to zero and all later chain vertices cancel in pairs. Thus every moving point has zero net selected force; each fixed guard has net force e_k.

For a selected unit edge ij, feasibility gives first coefficient 2(p_i-p_j) dot (d_i-d_j) >= 0. Summing with unit weights cancels all moving-point terms by equilibrium. Guard terms vanish because d_(M e_k)=0. The sum is zero, so every selected first coefficient is zero.

The second coefficient of the squared distance on an edge is

    |d_i-d_j|^2 + 2(p_i-p_j) dot (b_i-b_j).

Summing over S_r cancels all moving b_i terms. At each fixed guard, the reaction e_k pairs with guard coefficient -C e_k, contributing -2C. The total is E_r(d)-12C. Since every selected distance is at least one and its first coefficient is zero, each summed second coefficient is nonnegative. This proves the claimed energy demand for every ring, without adding overlapping ring stresses as independent energy budgets.

The support count is sum from r=1 to R of 6r, plus 6M radial edges, giving 3R(R+1)+6M=3M(M+1). Each individual S_r contains 6M distinct unit edges. These are selected rows only; the proof does not claim completeness of the forced-zero set.

## Adversarial scope checks and computation

- The stress is on the limiting packet, which contains unit triangles. It is not claimed to be an admissible triangle-free source or a strict replacement packet.
- The conclusion requires a feasible C2 one-sided family with all listed lower constraints and the stated guard expansion. First-order feasibility alone does not imply the second-order bound.
- Equality in E_r >= 12C is allowed. Strict finite feasibility does not force a positive second coefficient when an edge opens at higher order.
- The different S_r overlap. Their lower bounds cannot be summed as independent currency.
- No affine restriction is imposed, but no energy upper bound, finite motion, arbitrary-source extraction, global optimality, C-II closure, or Level I result follows.

The independent exact checker [`verify_target_c_nested_hexagon_stress_audit_2026_10_06.py`](../../../research/verify_target_c_nested_hexagon_stress_audit_2026_10_06.py) uses axial-coordinate rational arithmetic. It checks all selected supports, interior equilibrium vectors, guard reactions, and counts for M=3,...,12, including 16,365 moving-site equilibrium checks. The all-M conclusion comes from the ring/spoke identities above, not extrapolation from those finite cases.

The source verifier's field named `arbitrary_field_cancellation_checks` counts 225 chosen polynomial-field samples. That label overstates the computation. The exact cancellation for arbitrary acceleration fields is justified by the analytic equilibrium identity above; the samples are not load-bearing and are not registered as a certificate here.

## Canonical disposition

Promote `C-NESTED-HEXAGON-STRESS-ENERGY-DEMAND` as a scoped local necessary-condition theorem. Keep the source's floating LP and nonaffine packet search unreviewed. The local nonaffine-packet obligation is now sharper: any feasible C2 packet must meet every nested ring's threshold, but a violated threshold or a feasible packet has not been proved. The global C-II frontier is unchanged.
