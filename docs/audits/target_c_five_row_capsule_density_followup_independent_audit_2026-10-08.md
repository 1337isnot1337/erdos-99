<!-- theorem-state: {"artifact_id":"ART-4218CCBA996D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent Audit.151: five-row capsule consequences for high-t density claims

**Date:** 2026-10-08  
**Audit base:** `origin/main=318cd6fd2ac8289c63f98455f0d5c5a6e572f386`, state `2026-10-08.audit.148`  
**Frozen source branch:** `research/sol/target-c-owner-order-closure-20261006` at `bf288c82e8a62466d5580025c94e750a177e63e2`  
**Source:** `research/target_c_high_t_tb1_five_row_capsule_packing_t18687_2026-09-17.md`, SHA-256 `f7f6b6d6db9838b88fbc46bb9b3e79f767fa7708dc8f2eddc015f4ab1e24395a`  
**Source verifier:** `research/verify_target_c_high_t_tb1_five_row_capsule_packing_t18687.py`, SHA-256 `2c064f61abf5a4e3d5712126c5679ec9bccda40968e73b4485b844c2b07ace37`  
**Audited scope:** source Sections 3--5 only. Sections 1--2 were separately audited and promoted in Audit.149.

## Verdict

**PASS — already subsumed** for the local geometric consequence that a supplied path of at most five crossed rows cannot connect two retained layer indices separated by at least six. This is a direct corollary of canonical `C-OO-SHORT-PAIR-PATH-BANDWIDTH-5` when `D>=20K` and `|x-y|<=1+K/D`.

**CONDITIONAL ONLY — no new theorem promotion** for the source-level six-spacing density, Horn/poison-forest counts, LOWER ladders, or UPPER localization in Sections 3--5. Their required population, exact-swap extraction, genuine-upper exception bound, poison-forest, train-incidence, and path-incidence inputs are not canonical theorem dependencies and are not proved in those sections. The conditional scalar substitutions are correct at the displayed formulas, but do not establish those missing inputs.

## Exact claims and independent checks

### Section 3: six-spacing and LOWER coupling

Put `s_0=791/320000000` and suppose a source-level family of layer indices has cardinality

\[
|M_D|>(s_0/2)D-o(D).
\]

Partitioning into six residue classes gives one class of size greater than

\[
(s_0/12)D-o(D)=\gamma_6D-o(D),
\qquad \gamma_6=791/3840000000.
\]

Distinct indices in that class differ by at least six. The arithmetic is exact. In the supplied proper crosscut path regime of canonical `C-OO-SHORT-PAIR-PATH-BANDWIDTH-5`, if `D>=20K` and `|x-y|<=1+K/D`, then `|x-y|<=21/20` and the row span is at most five. Therefore such a pair cannot have its endpoints in two retained regions whose indices differ by at least six, provided every intervening path row separates `x` and `y` as required by the canonical theorem.

This verifies only the geometric exclusion of a short LOWER pair between two selected layers. To conclude that all LOWER clauses in an exact-swap Boolean system have at most one selected variable also requires the source's layer/owner assignment and the clause-to-pair correspondence. The source invokes simultaneous exact-swap active-contact/old-diameter decoupling, but the canonical `C-DISJOINT-SWAP-2SAT` theorem is only a compiler under its prescribed-move and all-binary-contact-preservation hypotheses; it does not construct or extract the six-spaced source moves. The population bound for `M_D` and the `O(1)` deletion of coordinates incident to genuinely-upper binary exceptions are also not established by this source section or by a canonical theorem entry.

### Section 4: poison-forest and LOWER-ladder counts

The scalar substitutions from `\gamma_6` are arithmetically consistent:

\[
\gamma_6/4=791/15360000000,\quad
\gamma_6/8=791/30720000000,\quad
\gamma_6/2=791/7680000000,\quad
\gamma_6/16=791/61440000000.
\]

The threaded coefficient in (FP.18) also follows exactly from the displayed inputs `0.6436=1609/2500` and `T_*=6121/2000`:

\[
\frac{\gamma_6}{16}\frac{1609/2500}{6121/2000}
=\frac{1272719}{470092800000000}.
\]

These computations do not prove the invoked poison-forest theorem, the source-wide train-defect/terminal-variation extraction, the five-deep-window count, or the complete-train bound in the canonical source regime. The report does not reconstruct those arguments in Sections 3--5. Consequently the lower/upper population alternatives and local-ladder count remain conditional.

### Section 5: UPPER localization

The exact ratio for the two stated densities is

\[
\gamma_6/\gamma_7
=\frac{791/3840000000}{113/640000000}
=7/6.
\]

Using only the displayed constants, the proposed coefficient identity is also algebraically correct:

\[
\frac{\gamma_6}{48(14/(3\sqrt3))}
=\frac{113\sqrt3}{122880000000}.
\]

The source does not prove in these sections that the same-type upper-localization/path-incidence argument yields the denominator `48 A_*` under the stated exact-swap hypotheses. The flexible-scale alternatives are likewise asserted without their incidence construction. These source-level conclusions remain conditional.

## Verifier boundary and dependency audit

I inspected the verifier at the frozen snapshot and its exact code hash is the one recorded above. The finite capsule search supports the already-promoted Sections 1--2 theorem. Its `check_propagated_constants()` function asserts `gamma_6`, the `7/6` ratio, and the threaded coefficient. It does not check the Section 4 poison-forest alternatives or their derivation. The proposed Section 5 coefficient is assigned as a `Fraction` and returned, but the verifier does not assert its equality with `gamma_6/(48 A_*)`. No finite check establishes any source-level population, extraction, Horn, or path-incidence premise.

The relevant canonical inputs are `C-OO-SHORT-PAIR-PATH-BANDWIDTH-5` and `C-DISJOINT-SWAP-2SAT`, each at its manifest scope. No canonical manifest entry supplies the `M_D` population estimate, the exact-swap source extraction used here, the claimed bounded genuine-upper exception set, the poison-forest population theorem, the LOWER-ladder extraction, or the UPPER path-incidence construction. No contact-isolate deletion or full-source motion is concluded.

## Disposition

Record the five-row-to-six-spacing geometric implication as already subsumed by the canonical supplied-path bandwidth theorem. Keep the `\gamma_6` density, (FP.14)--(FP.18) population/ladders, and (FP.19)--(FP.21) UPPER localization at **conditional** status until their source-level dependencies are independently proved or promoted. There is no new theorem ID, no state-version change, and no Target C frontier change. C-II and Level I remain open.
