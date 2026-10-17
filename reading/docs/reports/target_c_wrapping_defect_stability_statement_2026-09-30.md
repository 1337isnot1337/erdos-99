> Generated reading edition · [exact source](../../../docs/reports/target_c_wrapping_defect_stability_statement_2026-09-30.md) · source SHA-256 `3f77f184e2ee6a488daea9323ba5cb55944def78dd78d04496b88ce228a8b711`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A1A726D5E56B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Wrapping-root defect stability: statement

Base main: 43c1bd4eb6983578bdd6e7b9633df8fba8eea789. Proof-only; C-II open.

Let a positive-area wrapping cell satisfy d_*/D -> lambda in [lambda_1,1), where

A(lambda)=lambda+4 lambda sqrt(1-lambda^2),
A(lambda_1)=pi/2,
lambda_1=0.9891345915624005...,
Delta(lambda)=pi/2-A(lambda).

Write P=per(F), S=sum_r d_r, Qloc=sum_r Q_r, and C_A=sum_r c_r. Define

Y=2 d_tile-(e_BB-C_A) >= 0,
Z=sum_r(L_r-per(P_r)) >= 0,
M=S-d_*-A(lambda)D >= -o(D).

Then

(pi D-P)/2 + (P-q) + k + Qloc/2 + Y + Z/2 + M
<= Delta(lambda)D + o(D).                                  (1)

Hence, up to o(1),

(pi D-P)/D <= 2Delta,
(P-q)/D <= Delta,
k/D <= Delta,
Qloc/D <= 2Delta,
Y/D <= Delta,
Z/D <= 2Delta.

The proof is in target_c_wrapping_defect_stability_proof_2026-09-30.md.
