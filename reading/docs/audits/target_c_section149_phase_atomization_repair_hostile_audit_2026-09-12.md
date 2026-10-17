> Generated reading edition · [exact source](../../../docs/audits/target_c_section149_phase_atomization_repair_hostile_audit_2026-09-12.md) · source SHA-256 `7b82bea41eee300e62e0323eb08cbc192170088d45e792075baacd3596d7a012`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-54F157561D04","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — Section 149 phase-atomization repair

**Date:** 2026-09-12  
**Reviewed:** `research/target_c_section149_phase_atomization_repair_2026-09-12.md`  
**Base state:** `2026-09-12.audit.46`  
**Disposition:** **PASS as a conditional finite-to-limit repair.**  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

## 1. Local-Mantel lemma

The label-space lemma uses exactly the needed order of limits. First select the
finitely many atoms of mass at least `rho`, then choose disjoint neighborhoods and a
fixed separation scale, then let `n` tend to infinity. Mantel applies to each induced
selected-neighborhood graph because the full graph is simple and triangle-free.

For the complement, a non-far edge has its two labels in a small metric
neighborhood. The degree bound by the local empirical mass, together with compactness,
controls the normalized edge count by the largest small-ball mass. After the selected
atom neighborhoods are removed, that small-ball mass tends to at most `rho`; the
nonatomic part tends uniformly to zero. The annular boundary pieces can be chosen of
zero limiting mass and then shrunk.

The omitted atomic tail has squared mass at most `rho mu(X)`, so the final
`rho -> 0` limit gives the factor `1/4` in (A149R.3). No factor `1/2` is lost: the
`1/4` comes from Mantel inside each macroscopic atomic neighborhood, while the
non-atomic remainder is discarded in the limit.

**Verdict:** PASS, with the fixed-`epsilon` hypothesis (A149R.2) understood as part
of the theorem.

## 2. Phase-quotient application

The quotient by `pi/3` is the correct label space for rhombus crossings whose angle
tends to `pi/3` from above. A fixed angular excess gives a fixed quotient separation,
so the §142 fixed-`epsilon` saturation statement implies (A149R.9). The train crossing
graph is simple and triangle-free under the existing stopped-train conventions.

Thus the application yields

```math
\Delta_2\le\frac{x^2}{4}\sum_jS_j^2,
```

provided `T/D -> x` and `R_4/D^2 -> Delta_2` on the same subsequence. The proof does
not silently replace a weak pair-measure support statement by atomization; the
atomization is supplied by the finite lemma.

**Verdict:** PASS conditionally on the fixed-`epsilon` form of §142.

## 3. What remains outside this repair

The repair does not prove Section-149 endpoint capacity, does not establish the
outer Fourier hypotheses for every C-II survivor, and does not address Type I. It
does not imply a unit equilateral triangle or a strict-diameter source-preserving
competitor. The theorem-state cutoff remains canonical §123.

**Final verdict:** the missing atomic phase-orbit inference is repaired at a clearly
scoped proof-only level. Section 149 may use (A149R.10) only after explicitly adding
this lemma and verifying the fixed-`epsilon` §142 input; C-II remains open.
