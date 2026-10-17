> Generated reading edition · [exact source](../../../docs/audits/target_c_oblique_lattice_pick_comparison_hostile_audit_2026-09-14.md) · source SHA-256 `64c0ca3234d503af4ad032f9cefb92c41a65f939a10c319e64fb3c4fe32f347b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-44DA50C80A79","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Hostile audit — exact Pick comparison for one oblique affine source

**Date:** 2026-09-14  
**Audited artifact:** docs/reports/target_c_oblique_lattice_pick_comparison_2026-09-14.md  
**State version:** 2026-09-14.audit.51  
**Target:** Target C-II / restricted affine-source subroute  
**Disposition:** PASS at restricted proof-only scope; not promoted

## Audited statement

Let $`u,v`$ be unit vectors with
$`\theta=\angle(u,v)\in(\pi/3,\pi/2]`$, let
$`\Lambda_\theta=\mathbb Zu+\mathbb Zv`$, and put
$`s=\sin\theta`$, $`a_0=\sqrt3/2`$. If $`A\subset\Lambda_\theta`$ is finite
with two-dimensional convex hull $`K`$, $`n=|A|`$, and
$`D=\operatorname{diam}(A)`$, then

```math
 \frac{\pi D^2}{4}\left(\frac1{a_0}-\frac1s\right)
 > \frac{\pi D}{2}+1
```

implies the existence of an exactly $`n`$-point subset of a unit triangular
lattice having diameter strictly less than $`D`$. The source counted by $`n`$ is
the full set $`A`$, including any contact-isolated points.

The source-specific sufficient condition

```math
 \frac{\operatorname{area}(K)}s+\frac{b_\Lambda(K)}2+1
 <\frac{\pi D^2}{4a_0}
```

is also valid, where $`b_\Lambda(K)`$ counts boundary lattice points once.

## Proof audit

1. **Unit separation and triangle-free affine regression.** For a nonzero
   $`z=iu+jv`$, same-sign coefficients give
   $`\lVert z\rVert^2\ge i^2+j^2\ge1`$. Opposite signs, written
   $`z=au-bv`$, give
   $`\lVert z\rVert^2=(a-b)^2+2ab(1-\cos\theta)>1`$.
   Thus every finite subset is feasible, and the only unit differences are
   $`\pm u,\pm v`$. Their pairwise differences cannot make a unit
   equilateral triangle in the open angle range. This is a regression check and
   is not needed for the competitor-count argument.

2. **Pick population identity.** The vertices of $`K=\operatorname{conv}(A)`$
   are lattice points, so $`K`$ is a lattice polygon. Under the affine map
   sending $`u,v`$ to the coordinate basis, lattice area is Euclidean area
   divided by $`s`$. Pick's theorem therefore gives
   
   ```math
   |K\cap\Lambda_\theta|
   =\frac{\operatorname{area}(K)}s+\frac{b_\Lambda(K)}2+1.
   ```

   Since $`A\subset K\cap\Lambda_\theta`$, this is an upper bound for $`n`$.

3. **Boundary bound.** Subdivide each edge of $`K`$ at successive lattice
   points. Consecutive points differ by a nonzero lattice vector and hence are
   at distance at least one by Step 1. Summing along the boundary gives
   $`b_\Lambda(K)\le\operatorname{per}(K)`$. Cauchy's
   perimeter-diameter inequality gives
   $`\operatorname{per}(K)\le\pi D`$, while the isodiametric inequality gives
   $`\operatorname{area}(K)\le\pi D^2/4`$. Hence
   
   ```math
   n\le\frac{\pi D^2}{4s}+\frac{\pi D}{2}+1.
   ```


4. **Strict same-cardinality competitor.** For a unit triangular lattice and
   a translation $`t`$, let $`M(t)`$ count sites in the open disk of radius
   $`D/2`$. Translation averaging over one fundamental cell of area $`a_0`$
   gives
   
   ```math
   \frac1{a_0}\int M(t)\,dt=\frac{\pi D^2}{4a_0}.
   ```

   The strict hypothesis makes this average larger than $`n`$, so some
   translate has at least $`n+1`$ sites in the open disk. Select exactly $`n`$.
   The selected source is unit-separated and every pair has distance strictly
   less than $`D`$, because both points lie in the open disk. This proves the
   source-cardinality and strict-diameter claims without deleting, moving, or
   reinterpreting any point of $`A`$.

5. **Uniform condition.** The displayed uniform condition is exactly the
   rearrangement
   
   ```math
   \frac{\pi D^2}{4s}+\frac{\pi D}{2}+1
   <\frac{\pi D^2}{4a_0}.
   ```

   The source-specific condition is the same argument before applying the
   area and perimeter upper bounds.

6. **Lower-dimensional case.** If $`K`$ is a segment, ordering the points along
   it gives $`n\le D+1`$. For sufficiently large $`D`$,
   $`D+1<\pi D^2/(4a_0)`$, so the same open-disk averaging gives a strict
   triangular competitor. This is an asymptotic auxiliary statement and is not
   silently used in the two-dimensional Pick proof.

## Adversarial scope checks

- A vanishing-shear family with $`\theta-\pi/3=O(D^{-2})`$ fails the strict
  condition, so the audit does not falsely eliminate the critical affine model.
- A square-lattice patch is covered by the theorem only when its finite
  threshold holds; the conclusion is nonoptimality, not a classification of
  all square patches.
- The averaging competitor may contain equilateral triangles. That is allowed:
  it is a competitor, not the original source.
- Contact-isolated source points are included in $`n`$ and in the Pick count.
- No statement is made about non-affine grains, phase interfaces, holes,
  macroscopic inactive chambers, KKT stresses, or the ZR/ZF kernel on isolated
  coordinates.
- The argument is finite and exact. It does not use an asymptotic
  source/scaffold substitution or a numerical global-optimality certificate.

## Verdict

The proof is correct at the stated restricted affine-lattice scope. The exact
remaining bridge is unchanged:

    canonical C-II full-core source
        -> one exact affine lattice containing the full source

No such bridge is currently canonical. The result therefore improves the
restricted affine subroute but does not close C-II or Level I.
