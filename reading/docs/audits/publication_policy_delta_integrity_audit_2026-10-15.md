> Generated reading edition · [exact source](../../../docs/audits/publication_policy_delta_integrity_audit_2026-10-15.md) · source SHA-256 `deda1270436dfbbefa2c09437d4360a909d89508ecbe2d755fc367f206b31833`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-774AA2447CC2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"shared"} -->
# Publication policy delta: retained integrity audit

Classification: operational agent audit, not a mathematical proof audit or
canonical promotion. Substantial AI assistance: the integration Codex session
compared immutable objects and reproduced the integrity failure below.

## Exact scope and reproduced defect

Destination PR #8 advanced `0b78e49159451d346e2333bb4019a15c3db04f9b` to
`2bccea305a50f179428829acb03a85af16b4fc2a`. Private source main concurrently
advanced from the scientific freeze `eb51394f371aee958b0d9332f80faf75ae694b9e`
to `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.

The 14 destination paths change review/governance documentation plus one Python
comment. Comparing `ast.dump(ast.parse(...))` for `tools/localized_ci/plan.py`
at both destination commits gives identical trees. No theorem manifest, proof,
registered certificate or mathematical parameter changed in that delta.

At `2bccea3`, `python tools/check_public.py` reported exactly two stale inclusion
hashes: `.github/PULL_REQUEST_TEMPLATE.md` and `docs/STATE.md`. In addition, the
pending sequence-proof descriptions still required the superseded human-review
gate. The current policy requires one independent AI-agent mathematical audit;
rights, contributor consent and final visibility remain owner decisions.

## Correction and falsification boundary

Publication revision `2026-10-15.publication.2` updates those byte records and
pending-review descriptions and regenerates the public theorem views. Immutable
source identities stay pinned. Claim IDs, dependencies, lifecycles, hypotheses,
conclusions other than the review-gate wording, and all 94 certificate files stay
unchanged. The unsupported global chart/rate remains withdrawn and the repaired
sequence exclusion remains audited-working; this audit does not promote it.

The complete public integrity and theorem-state checks must pass on the corrected
candidate. A future proof/verifier or lifecycle delta falls outside this operational
audit and requires its own scope-aware review. Final detached receipts identify
the actual corrected candidate and preserve the earlier full replay at `0b78e49`.
