<!-- theorem-state: {"artifact_id":"ART-8F1C5613E419","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Wrapping-root defect stability: proof

Put S_out=sum_r(L_r-2d_r). Current main's rooted chord dissection, before replacing P by (pi+o(1))D, gives

sum_r(per(P_r)-2d_r) >= P-2d_*-o(D).

Therefore

S_out >= P-2d_*+Z-o(D).                                  (2)

The exact aggregate outer-walk identity is

S_out = 2(q-k-S)+4c_I-4-Qloc+2(e_BB-C_A-2d_tile).

Since c_I=o(D) and Y=2d_tile-(e_BB-C_A),

S_out <= 2(q-k-S)-Qloc-2Y+o(D).                          (3)

Combining (2) and (3),

(P-q)+k+(S-d_*)+Qloc/2+Y+Z/2 <= P/2+o(D).

Substitute S-d_*=A(lambda)D+M:

(P-q)+k+Qloc/2+Y+Z/2+M <= P/2-A(lambda)D+o(D).

Finally P<=pi D for every planar convex body of diameter D. Adding
(pi D-P)/2 proves inequality (1) in the statement file.

All displayed defect terms are nonnegative; only M may be negative, and its
negative part is o(D) by the current complement-gap diameter-moment theorem.
This yields the termwise bounds in the statement.