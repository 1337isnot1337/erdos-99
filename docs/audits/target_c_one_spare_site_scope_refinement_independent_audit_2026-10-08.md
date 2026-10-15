<!-- theorem-state: {"artifact_id":"ART-4B16E4E33603","canonical":true,"claim_ids":["C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT"],"claim_statuses":{"C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: strict-packet contact loss and the one-spare-site endpoint

**Date:** 2026-10-08
**Audit base:** `origin/main=78343286a9d2176308d8b1787c00cc24e9ce6f91`, state `2026-10-08.audit.151`
**Frozen source:** `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`
**Source artifact:** `docs/reports/target_c_one_spare_site_contact_minimality_endpoint_2026-10-05.md`, SHA-256 `afd5a20ba695bd56ee8306beb1a0f78b961176b2a7b239603670f4e6466814f5`

## Verdict

**PASS — refine the scope of `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`.** In its strict contact-loss case `j<t`, contact minimality alone suffices and new-involving pairs may have length exactly `D`. The equal-contact case `j=t`, `d>0` still needs diameter-pair minimality and strict upper slack. The source report's one-spare-site endpoint is a corollary of the strict contact-loss case, so it does not receive a duplicate theorem ID.

The source's spare-site statement is valid with the wider upper condition `<=D`: if a contact-minimal global minimizer has a nonisolated contact vertex, a packet with one more strictly separated site than the explicit deletion set can replace that set and the vertex while creating no unit contacts. If the deletion set already contains a nonisolated contact vertex, the spare site is unnecessary.

No strict packet or spare site is constructed for a canonical source. C-II and Level I remain open.

## Exact refined endpoint

Let `A` be a finite triangle-free global minimum-diameter source of cardinality `n` and diameter `D`, chosen to minimize its number of unit contacts among all such minimizers. Let `R` be an explicitly deleted set of source labels and `Y` a finite replacement set with `|Y|=|R|`. Let `t` count old unit-contact edges incident to `R`, `j` count every unit-distance pair in the new source that touches `Y`, and `d` count actual old diameter pairs incident to `R`.

Assume the replacement is unit-separated and triangle-free, and every new-involving distance is at most `D`.

- If `j<t`, no such replacement exists. Diameter is at most `D`; if it is smaller, global minimality fails. If it equals `D`, the replacement is another triangle-free global minimizer with exactly `|C(A)|-t+j` unit contacts, contradicting contact minimality. This branch uses no diameter-pair-minimality assumption.
- If `j=t` and `d>0`, the same conclusion holds provided `A` is also diameter-pair-minimal and every new-involving distance is strictly below `D`. Then no new diameter pair is created and at least one old diameter pair is removed. This is the secondary-normalization branch already present in Audit.64.

Retained-retained pairs are unchanged. Contact-isolated labels remain part of the source unless explicitly included in `R`; no stress coordinates or affine-kernel claim is used.

## One-spare-site corollary

Let `S` be any explicitly removed label set, and suppose `A` has a nonisolated contact vertex `v`. Let `Y` have at least `|S|+1` sites, with every distinct pair in `Y` and every pair from `Y` to a retained old source point at distance strictly greater than one and at most `D`.

If `v` lies in `S`, replace `S` by any `|S|` sites of `Y`. Otherwise replace `S` together with `v` by any `|S|+1` sites. The selected sites remain strictly separated from each other and every retained old point. Hence they create no unit contacts and the new contact graph is the old induced graph plus isolated labels, so it remains triangle-free. The removed set contains a nonisolated contact vertex, giving `t>=1`, while `j=0`. The strict contact-loss endpoint rules out the packet. If `S` itself contains a nonisolated contact vertex, `|Y|>=|S|` suffices.

This covers the source report's stricter `<D` hypothesis and weakens it to `<=D`. It proves only an exclusion implication for an explicitly supplied packet. It does not produce protected capacity inside a wall or in an arbitrary source.

## Dependencies and hostile checks

The proof uses only global minimum diameter and contact minimality; the optional equality-contact branch also uses the canonical secondary diameter-pair minimum. It does not infer a packet from a wall, positive residual, KKT equilibrium, stress rank, or a local motion. All source labels are counted. A pair at distance exactly `D` is allowed in the strict contact-loss branch because the contact count drops; strict upper slack remains essential for the equal-contact, diameter-pair branch.

The source artifact states that it uses no computation or literature and supplies no verifier. No verifier is treated as evidence. The proof is a direct finite contact-count argument.

## Canonical disposition

- Refine the existing `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT` into its two exact normalization branches above.
- Record the one-spare-site claim as a corollary of the strict contact-loss branch; do not create a duplicate ID.
- Do not promote the source report's packet-existence target, residual-cage composition, or noncontact-wall application from this audit.
- No Target C frontier change follows.
