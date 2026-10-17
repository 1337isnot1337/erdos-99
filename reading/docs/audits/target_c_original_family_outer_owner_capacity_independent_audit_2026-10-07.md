> Generated reading edition · [exact source](../../../docs/audits/target_c_original_family_outer_owner_capacity_independent_audit_2026-10-07.md) · source SHA-256 `9cdb02fea1dfe4bc62a212f6c918d53bff4e467f307a5a6e8e935d5d1deb3cc3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4F8E6F380ABE","canonical":true,"claim_ids":["C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY"],"claim_statuses":{"C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.114 — original-family O–O owner capacity

**Date:** 2026-10-07
**Audit base:** `aada804a6255fc8509041152d84a5b2ab5b9faff`, tree `2b30f402c4c3ddcb23ed85c4a8cbacb812a7b7e2`
**Starting state:** `2026-10-07.audit.113`; C-I closed, C-II open, Level I open
**Source branch:** `research/target-c-residual-closure-20261005`
**Frozen source commit:** `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`
**Source artifact:** `docs/reports/target_c_loaded_neighbor_outer_owner_bound_2026-10-05.md`, SHA-256 `73fcdb63e60c7104eede09e47d9dca9e82f7b0b5fb3bc89631de04d6d5863bff`
**Audit boundary:** Section 4.3's original-family extension only. The report's general multishear application and its source-family extraction claims are not audited here.
**Verdict:** PASS WITH EXPLICIT SUBFAMILY-STABILITY HYPOTHESES — promote `C-OO-ORIGINAL-FAMILY-OWNER-CAPACITY`.

## Exact statement promoted

Let `A` be a canonical contact-minimal, then diameter-pair-minimal, triangle-free C-II source in the `C=C_*`, `H=H_*` normalization. Let `H` be its actual diameter graph, with `d_H=|V(H)|-|E(H)|`. Use the canonical O–O localization and fixed full-source isolate assignment. Let `E` be the fixed inactive-long-pair exception set supplied by `C-LONG-PAIR-ISOLATE-DISPATCH`; thus `|E|<=d_H`.

Take a finite family of `r` fixed O–O owner proposals with pairwise-disjoint moving core sets and common translation-amplitude bound `s < D-sqrt(D^2-1)`. Require that taking a subfamily leaves each remaining proposal, its owner set, and the source-wide isolate assignment unchanged. Assume:

1. every old unit contact stays exactly unit under every binary selection;
2. each singleton proposal weakly shortens every old actual diameter pair and strictly shortens at least one;
3. each singleton passes the required strict unary-rhombus tests; and
4. each singleton satisfies the canonical owner-capacity hypotheses except that an inactive upper pair in `E` may fail its strict upper bound. In particular, after the canonical isolate assignment, every lower witness lies in the old outer contact face, has old length at most a fixed `t` with `1<t<sqrt(2)`, and these properties persist when proposals are discarded.

Then

`r <= 2 m_B + 3 (x_B + Z_out) + 2 d_H`,

where `x_B=b-q` is the occurrence excess of the old outer contact walk, `m_B` is the number of nonunit sides of the loaded hull, and `Z_out` is the number of contact isolates on that walk. In the canonical Type-II near-disk scope, the same hypotheses and the promoted collar replacement give

`r <= 147 (x_B + m_B) + 2 d_H`.

The conclusion bounds an already specified family of individually tested proposals. It does not assert simultaneous feasibility, extract such a family from a source, or close C-II.

## Independent reconstruction

The canonical long-pair dispatch fixes `E` before any owner is discarded. For a pair outside `E`, the full-source displacement bound and `s < D-sqrt(D^2-1)` keep every inactive upper pair strictly below `D`; every old diameter is weakly shortened by hypothesis. Thus only a pair in `E` can make a singleton fail an inactive upper check.

Call an owner bad if its singleton move makes some pair in `E` have length at least `D`. A fixed pair can be affected by at most two singleton proposals: each endpoint belongs to at most one moving set, and any retained isolate follows one fixed anchor or stays fixed. Consequently

`|Bad| <= 2 |E| <= 2 d_H`.

Discard those owners. The surviving fixed proposals still have disjoint moving sets, preserve all old contacts, pass their unary tests, weakly shorten all old diameters, and strictly shorten at least one. Their exceptional upper pairs are strict by the definition of `Bad`; all other inactive upper pairs are strict by the canonical dispatch. If a surviving singleton had no lower equality or violation, its replacement would have the old contact graph, no new diameter pair, and at least one fewer actual diameter pair (or diameter below `D`). That contradicts the canonical lexicographic source. Each survivor therefore has a lower witness.

Now apply the independently audited `C-OO-LOWER-WITNESS-OWNER-CAPACITY` to this subfamily. Its endpoint accounting gives at most `2m_B` owners charged to loaded-loaded witnesses, at most `x_B+Z_out` charged to a relatively moving outer nonloaded endpoint, and at most `2(x_B+Z_out)` charged to a loaded endpoint near a fixed outer nonloaded endpoint. If `k` owners survive, `k<=2m_B+3(x_B+Z_out)`. Since `r-k<=2d_H`, the stated bound follows.

In Type II, each isolate that actually appears in a surviving lower witness belongs to the Audit.105 collar. Repeating the same endpoint count with the collar population `N<=48(x_B+m_B)` gives `k<=147(x_B+m_B)`, hence the second bound.

## Hostile scope checks

- Discarding proposals is not a motion of source labels. It does not change the source or any remaining fixed singleton move.
- The fixed isolate assignment is essential. If an isolate were reassigned after a proposal is discarded, the subfamily-stability step would need a new proof.
- The factor two is per exceptional pair: its two endpoints can belong to at most two distinct owner moves. This does not bound the number of conflicts between simultaneous nonexceptional lower constraints.
- No simultaneous move is inferred from individually safe proposals. The theorem counts one-owner tests only and preserves the existing warning that individually feasible moves need not be jointly feasible.
- The result is conditional on an O–O proposal family satisfying all stated localization and singleton hypotheses. It proves no canonical source supplies one.

## Dependency and frontier disposition

Dependencies are canonical `C-DISJOINT-SWAP-2SAT`, `C-LONG-PAIR-ISOLATE-DISPATCH`, and `C-OO-LOWER-WITNESS-OWNER-CAPACITY`. This resolves the source report's explicitly conditional `2d_H` counting step under subset-stable proposals. It does not promote the report's more general multishear route or its family-extraction step. The one-spare-site endpoint in the same PR #722 branch is already subsumed by Audit.64 and is not a new claim. C-II and Level I remain open.
