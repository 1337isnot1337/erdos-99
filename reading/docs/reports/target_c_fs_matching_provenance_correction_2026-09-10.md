> Generated reading edition · [exact source](../../../docs/reports/target_c_fs_matching_provenance_correction_2026-09-10.md) · source SHA-256 `1cfca9950c556e68165660213023ec821b82c07d4c21eba2862386fdaa619223`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-AB169210B03D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_fs_matching_provenance_correction_2026-09-10.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=2ef332de31ca80832fb9afdd867a0227fe17119b; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — provenance correction for the FSDB matching argument

**Date:** 2026-09-10  
**Repository state:** `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4`  
**Run type:** dependency/provenance correction  
**Target:** Target C, post-ZF diameter branching  

## LEVEL I STATUS

`STILL OPEN`

The September 10 report
`target_c_annular_voronoi_matching_exclusion_2026-09-10.md` proves a valid new
**independent** exclusion of the perfect-matching diameter branch:

$$
\operatorname{area}F\le\frac{\pi^2}{16}D^2
\quad\text{under MB matching topology,}
$$

while FSDB gives

$$
\liminf\frac{\operatorname{area}F}{D^2}
\ge\frac{2\rho+\sin2\rho}{4}
>\frac{\pi^2}{16}.
$$

Its exact rational sign certificate remains correct.

However, that branch had already been excluded at report level on September 9 by the
NB theorem in `target_c_db_nm_branching_constant_2026-09-09.md`, which proves the
strictly stronger quantitative conclusion

$$
\boxed{
\liminf\frac{2h-q}{D}
\ge0.6099043189\ldots>0.
}
$$

A perfect matching has `q=2h`, so it is impossible along any unbounded post-ZF
survivor sequence directly from NB.

Therefore the correct provenance is:

1. **NB is the first existing report-level exclusion of the perfect-matching branch.**
2. **MFS is a new independent geometric proof**, using the September 10 FSDB area
   theorem and MB's rhombic/Mantel capacity.
3. MFS remains useful as an audit cross-check because it uses different hypotheses and
   mechanisms from NB, but it must not be cited as the first elimination of that
   branch.
4. The annular Voronoi theorem AV remains independent of both arguments and is not
   needed for either matching exclusion.

No mathematical conclusion is weakened by this correction. The only correction is the
novelty/provenance claim.

## Promotion disposition

Treat any wording in the September 10 MFS report saying that FSDB newly *closes* an
otherwise-live matching branch as historical shorthand. In the canonical theorem
ledger, record NB as the quantitative matching exclusion and MFS as an independent
FSDB-based reproof/check.
