<!-- theorem-state: {"artifact_id":"ART-3DC83A6B5992","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-b"} -->
# Audit — Target B local virtual-area / interface certificate

**Date:** 2026-09-05  
**Candidate:** `docs/reports/target_b_local_virtual_area_interface_certificate_2026-09-05.md`  
**Verdict:** PASS under the stated pure simply connected strict-rhombic hypotheses.  
**LEVEL I status:** STILL OPEN.

## Checks

1. For one train `tau`, Section 25 gives `w_K(nu_tau)=L_tau+h_tau`, where `L_tau` is the sum of transverse increments at physical crossings and `h_tau` is the two-terminal support-depth sum.

2. The centered train zonotope has width `sum_(sigma!=tau)|det(u_tau,u_sigma)|` in normal direction `nu_tau`. Train-coordinate inclusion gives a translate of `K` inside the zonotope, hence its width is no larger.

3. Subtracting the physical crossing terms gives exactly

`h_tau <= sum_(sigma noncross tau)|det(u_tau,u_sigma)|`.

4. Summing over a subset `I` is legitimate. The directed virtual sum counts a noncrossing pair twice only when both endpoints lie in `I`, and once otherwise, hence it is at most twice the unordered virtual mass incident with `I`.

5. In Section 50, after initial high-defect edge deletion, every crossing edge incident with a subsequently pruned train either was already high-defect or is removed when its first pruned endpoint is deleted. Therefore all such physical crossings lie in `E_hi union E_pr`.

6. The sum of physical spans over pruned trains counts any such crossing at most twice and each transverse increment is `<=1`, so `sum_I L_tau <=2|E_hi|+2|E_pr|`.

7. Theorem 50.1 gives `|E_hi|=O(D^(2-eta))=o(D^2)` and `|E_pr|<=C_T lambda D^2`. Uniform width saturation gives `w_K>=D-O(D^(1/3))`; since `r=O(D)`, the aggregate width error is `O(D^(4/3))=o(D^2)`.

Thus

`H_I>=rD-2C_T lambda D^2-o(D^2)`

and

`V_inc(I)>=rD/2-C_T lambda D^2-o(D^2)`.

## Scope

The lower bound can be vacuous when `r/D<=2C_T lambda`; it is intended for a linear pruned population with `lambda` chosen sufficiently small. It does not by itself identify which retained phase component is adjacent to the virtual pairs or produce a diameter contradiction.