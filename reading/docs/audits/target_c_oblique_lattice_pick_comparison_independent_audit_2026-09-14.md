> Generated reading edition · [exact source](../../../docs/audits/target_c_oblique_lattice_pick_comparison_independent_audit_2026-09-14.md) · source SHA-256 `23d0d8f107c51e382609c68eeafe209253a80f46b3ee96a935d8ffbd1be53b53`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 2 paragraph(s) with malformed inline math are preserved as explicit source excerpts rather than guessed equations.

<!-- theorem-state: {"artifact_id":"ART-DE35C6813859","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — exact lattice-point comparison for an oblique source

**Date:** 2026-09-14  
**Audited artifact:** `docs/reports/target_c_oblique_lattice_pick_comparison_2026-09-14.md`  
**Verdict:** PASS for its restricted theorem; no C-II promotion

## Scope check

The source is the full finite set (A\subset\Lambda_\theta), not a contact
core. Its hull (K) has lattice vertices because the vertices of a convex hull
of a finite set are members of that set. The comparison preserves (n=|A|)
exactly and constructs a genuine (n)-point source.

## Proof audit


**Source formatting excerpt (unbalanced inline math in the original):**

```text

1. For $`\theta\in(\pi/3,\pi/2]`$, every nonzero lattice difference has
   length at least one. In the opposite-sign case,
   $`(a-b)^2+2ab(1-\cos\theta)>1`$ because (a,b\ge1) and
   \(2(1-\cos\theta)>1). The open endpoint is essential.
```





**Source formatting excerpt (unbalanced inline math in the original):**

```text
2. The affine form of Pick's theorem is correctly normalized: the covolume of
   \(\Lambda_\theta\) is $`s=\sin\theta`$, so
   $`N_\Lambda(K)=\operatorname{area}(K)/s+b_\Lambda(K)/2+1`$.
   This counts all lattice points in (K), so it remains an upper bound when
   (A) omits interior lattice points.
```



3. The boundary count satisfies $`b_\Lambda(K)\le\operatorname{per}(K)`$
   because each successive lattice boundary segment has length at least one.
   Cauchy's $`\operatorname{per}(K)\le\pi D`$ and the isodiametric bound are
   applied to the actual source hull. No contact-isolated point is discarded.

4. Translation averaging over the open disk is exact. If its mean population
   is strictly larger than the integer (n), one translate contains at least
   (n+1) points. Selecting (n) sites gives pairwise distances at least one
   and, because the disk is open, diameter strictly less than (D). This is
   the required finite strict competitor, not an asymptotic density claim.

5. Rearranging the uniform inequality gives (PL.9). Since
   $`s-a_0\le 2(1-\sqrt{a_0/s})`$ is not needed here, no hidden weakening
   enters the exact threshold. The stated (O(D^{-1})) endpoint is correct.

## Adversarial checks

- **Vanishing shear:** if $`\theta-\pi/3=O(D^{-2})`$, the left side of
  (PL.1) is (O(1)), while the right side is $`\Theta(D)`$; the theorem
  correctly remains silent.
- **Square lattice:** $`\theta=\pi/2`$ satisfies (PL.1) for large (D).
  This excludes square-lattice subsets as global minimizers at those source
  sizes; it does not claim that the square patches themselves contain unit
  triangles.
- **Boundary holes in the source:** omitted lattice points only reduce (n),
  so the Pick upper bound becomes stronger. No source completion is assumed.
- **Degenerate hull:** the main Pick step is two-dimensional; the report
  separately handles a segment by (n\le D+1) and quadratic triangular-disk
  capacity.
- **Endpoint $`\theta=\pi/3`$:** the strict density comparison vanishes, so
  no endpoint conclusion is claimed.
- **Global-minimality bridge:** the contradiction uses only the definition of
  (D(n)): a feasible (n)-point source with diameter (<D(n)) is impossible.
  Nothing local, KKT-based, or representative-dependent is substituted.

## Exact remaining obstruction

The improvement is confined to an exact affine lattice. It does not show that a
canonical full-core source is one affine lattice, does not control a union of
grains or interface defects, and does not resolve the macroscopic inactive
container/cap branch. Even in the affine class, (PL.9) allows an inverse-(D)
angle excess; the boundary term in Pick's theorem is itself linear and cannot be
discarded at that scale.

**Audit disposition:** retain as proof-only research. Do not alter the Level-I
status or canonical C-II frontier on the basis of this artifact alone.
