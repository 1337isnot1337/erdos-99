> Generated reading edition · [exact source](../../../docs/audits/target_c_tau_d_binary_loaded_witness_pocket_independent_audit_2026-10-09.md) · source SHA-256 `83e5bbea8d1c60b143c02f03551c50b996ae7515a9c5b6f97e5dd59ad0f49c60`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-8CD0F39752A5","canonical":true,"claim_ids":["C-TAU-D-BINARY-OWNER-SIDE-POCKET-BUDGET"],"claim_statuses":{"C-TAU-D-BINARY-OWNER-SIDE-POCKET-BUDGET":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.213 — tau-D binary loaded-owner side pocket budget

Date: 2026-10-09. Audit base: `origin/main=0539c5fee6e0e6bfee653efcbcb10c2219ff2444`, state `2026-10-09.audit.206`.

## Frozen candidate and verdict

- Source branch: `origin/research/sol/target-c-owner-order-closure-20261006`.
- Frozen source commit: `bf288c82e8a62466d5580025c94e750a177e63e2`.
- Candidate artifact: Section 1 of `docs/reports/target_c_terminal_oo_depletion_and_short_pocket_clauses_2026-10-06.md`, SHA-256 `5c560eafe95149b7e0694fa0f54e595cef2d4ee5be92e019a0621a949034b0ee`.
- Related prior canonical result: `C-BINARY-LOADED-WITNESS-POCKET-BUDGET`, Audit.63, scoped to witness distances through `13/12`.
- Verdict: **PASS — promote the wider owner-side scope** as `C-TAU-D-BINARY-OWNER-SIDE-POCKET-BUDGET`, which subsumes the narrower loaded-witness theorem.

## Exact statement

Use the canonical narrow-window independent-binary O--O owner model: selected cut directions lie in one projective interval of width strictly less than `pi/3`, independent owner choices preserve every old contact, and an old contact cannot join two distinct nonzero moving owners. Let `D>=4`, let `B` be the actual loaded set, and define

$$
 \tau_D=\frac{3D}{\sqrt{3D^2+4}+1}.
$$

Count distinct physical pairs `ab` of actual loaded endpoints whose endpoints have distinct nonzero owner labels and whose lengths satisfy

$$
 1<|a-b|<\tau_D.
$$

Each such pair is counted once, whether or not it generates a lower clause. If `u_B=x_B-m_B=\sum_I(\ell_I-2)` is the canonical loaded-hull outer-interval budget over nonunit intervals, then

$$
 N_{\rm owner}\le u_B.
$$

Since `tau_D>sqrt(2)` for `D>=4` and `tau_D` tends to `sqrt(3)`, this strictly extends the promoted `13/12` band and covers more than the source report's lower-witness range. The exact `tau_D` threshold is retained; no uniform `sqrt(3)` endpoint is claimed for finite `D`.

## Independent proof

First, the canonical loaded-near-unit theorem gives, for any nonconsecutive loaded endpoints with distance less than `D`,

$$
 |a-b|\ge\tau_D.
$$

Thus every counted pair with `|a-b|<tau_D` is a side of the actual loaded hull. Here `|a-b|<tau_D<D` for `D>=4`. Direct comparison gives `tau_D<sqrt(3)` for every finite `D`; direct squaring of positive sides shows `tau_D>sqrt(2)` exactly when `D>2+sqrt(2)`, so it holds for `D>=4`.

Charge each distinct physical pair to its unique nonunit outer interval between consecutive loaded endpoints. An interval of length two has actual boundary path `a-z-b` with `|a-z|=|z-b|=1`. If its endpoints had distinct nonzero owner labels, `z` could not have either label or a third nonzero label: in every case an old contact would join distinct moving owners. Hence `z` is fixed, and both contacts are selected cut contacts in the common direction window.

Write `d=|a-b|`. In the charged range, `1<d<tau_D<sqrt(3)`, so the angle between the two unit contact rays at `z` is

$$
 \theta=2\arcsin(d/2)\in(\pi/3,2\pi/3).
$$

Their projective distance is `min(theta,pi-theta)>pi/3`. They therefore cannot both lie in a projective interval of width strictly less than `pi/3`, contradicting the selected-window hypothesis. So no counted pair uses a length-two interval.

Every counted pair is a distinct loaded-hull side, so distinct physical pairs charge to distinct outer intervals. Unit separation and `d>1` exclude a length-one contact interval. The previous paragraph excludes length two. Each remaining interval has integer length `ell_I>=3` and contributes at least one to `ell_I-2`; summing gives `N_owner<=sum_I(ell_I-2)=u_B`.

## Verifier boundary and scope checks

I inspected and reran `research/verify_target_c_terminal_oo_geometry_2026_10_06.py` from the frozen source snapshot. It reports 1,154 anchor checks, 32 short-pocket binary checks, 47,314 positive-cone checks, and 36,138 finite ledger checks, plus the exact `1/65` long-pocket regression. Its binary loop only tests chord lengths through `13/12`; it does not certify the widened `tau_D` range or the loaded-hull asymptotic implication. The widened claim is proved by the exact angle argument above and canonical loaded-near-unit geometry, not by the sampled verifier.

The result counts distinct actual loaded-endpoint pairs assigned different nonzero owners, not logical clauses. It applies to the whole stated `tau_D` pair range, including pairs that are not lower witnesses. It excludes unary clauses, arbitrary-angle witnesses, general crossing multishears, and any claim that an abstract owner packet is source-realized. It gives no finite motion, strict-`D` competitor, C-II closure, or Level-I conclusion. Contact-isolated source points are retained.

**Frontier effect:** none. In the canonical narrow-window binary owner branch, the long-pocket budget now applies to all pairs of distinct nonzero owners among loaded endpoints below `tau_D`, approaching `sqrt(3)` as `D` grows. This contains the earlier lower-witness claim but adds no source-level endpoint.
