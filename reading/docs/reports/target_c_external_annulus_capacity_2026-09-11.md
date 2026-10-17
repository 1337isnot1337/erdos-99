> Generated reading edition · [exact source](../../../docs/reports/target_c_external_annulus_capacity_2026-09-11.md) · source SHA-256 `061951d1bc28d3a0fbab53e0d3036a093d354bba8a041cd91fb9093d98f52f84`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-F06132C6131F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — external-annulus capacity for a force core

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** closing proof / convex-capacity lemma  
**Target:** Target C C-II, perfect-matching subbranch  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** used only to confirm that the underlying Erdős problem remains listed as open  
**Computation:** arithmetic only for the displayed constants

## LEVEL I STATUS

`STILL OPEN`

This report closes the perfect-matching subbranch by a source-capacity argument. That
subbranch was already excluded by the NB matching theorem in the report stack, so this
does not remove a currently surviving branch. The useful new input is an annular
packing estimate that can be reused whenever all non-core points lie outside the force
hull.

## 1. Starting endpoint

In the perfect-matching branch, the matching report gives a pure strict-rhombic force
core with vertex count

```math
v\le \frac{q^2}{16}+\frac q2+1,
\tag{EA.1}
```

and every source point not in the core lies outside the force hull $`F`$. The matching
report only used this to state that a quadratic external population is required. The
closing implication is

```text
external points outside F + full-source diameter-D hull K
  -> annular disk-capacity bound
  -> contradiction with n/D^2 -> pi/(2 sqrt(3))
```

## 2. Strongest new theorem

### Theorem EA — external-annulus capacity

Let $`K`$ and $`F`$ be compact convex planar sets with $`F\subseteq K`$, and let
$`X\subseteq K\setminus F`$ be a finite set with pairwise distances at least one.
Then

```math
\boxed{
|X|\frac{\pi}{4}
\le
\operatorname{area}(K)-\operatorname{area}(F)
 +\frac12\bigl(\operatorname{per}K+\operatorname{per}F\bigr)
 +\frac\pi4.
}
\tag{EA.2}
```

In particular, if both sets have diameter at most $`D`$, then

```math
\boxed{
|X|\le \frac4\pi\bigl(\operatorname{area}(K)-\operatorname{area}(F)\bigr)+4D+1.
}
\tag{EA.3}
```

### Scope

This is an exact finite packing statement. It does not assume that $`F`$ is a
scaffold, that $`X`$ is globally optimal, or that the points of $`X`$ have contacts.
It applies to points outside a convex force hull. It does not bound isolated points
lying inside $`F`$.

### Proof

Put $`r=1/2`$, let $`B_r`$ be the closed radius-$`r`$ disk, and define the outer
parallel body $`K_r=K+B_r`$. Define the inner parallel body

```math
F_{-r}:=\{y\in F:y+rB_1\subseteq F\}.
```

The disks $`x+B_r`$, $`x\in X`$, have pairwise disjoint interiors. Their union is
contained in

```math
K_r\setminus F_{-r}.
\tag{EA.4}
```

Indeed, every disk is contained in $`K_r`$. If a point of $`x+B_r`$ belonged to
$`F_{-r}`$, its distance from the point $`x\in K\setminus F\subseteq F^c`$ would be
less than or equal to $`r`$, contradicting the definition of $`F_{-r}`$ (the harmless
boundary equality is removed by using open disks and then taking limits).

For every convex planar body, the elementary inner-parallel estimate is

```math
\operatorname{area}(F)-\operatorname{area}(F_{-r})
\le r\operatorname{per}F.
\tag{EA.5}
```

If the inner parallel body becomes empty before distance $`r`$, (EA.5) follows by
integrating the nonincreasing perimeters of the inner parallels up to the inradius.
Otherwise it follows from the same coarea integral over $`[0,r]`$. Steiner's formula
gives

```math
\operatorname{area}(K_r)=\operatorname{area}(K)+r\operatorname{per}K+\pi r^2.
\tag{EA.6}
```

Therefore

```math
\begin{aligned}
|X|\pi r^2
&\le \operatorname{area}(K_r)-\operatorname{area}(F_{-r})\\
&\le \operatorname{area}(K)-\operatorname{area}(F)
 +r(\operatorname{per}K+\operatorname{per}F)+\pi r^2.
\end{aligned}
```

Substitute $`r=1/2`$ to obtain EA.2. For a convex body of diameter at most $`D`$,
$`\operatorname{per}\le\pi D`$; EA.3 follows. $`\square`$

## 3. Perfect-matching closure

Let $`F`$ be the C65 force hull, $`K=\operatorname{conv}A`$, and let $`X`$ be the
source points outside $`F`$. In the perfect-matching branch:

1. the matching report proves that every source point outside the positive contact
   core lies outside $`F`$;
2. the core-size bound is EA.1;
3. the full-source and force-hull diameters are at most $`D`$;
4. FSDB gives
   
   ```math
   \liminf\frac{\operatorname{area}F}{D^2}
   \ge A_{FS}:=\frac{2\rho+\sin(2\rho)}4,
   \qquad \rho=\cos\rho.
   \tag{EA.7}
   ```


Theorem EA and the isodiametric inequality for $`K`$ give

```math
\limsup\frac{|X|}{D^2}
\le 1-\frac{4A_{FS}}\pi.
\tag{EA.8}
```

The matching core bound and $`q\le\pi D`$ give

```math
\limsup\frac v{D^2}\le\frac{\pi^2}{16}.
\tag{EA.9}
```

Since $`n=v+|X|`$ in this branch and every global minimizer satisfies

```math
\frac n{D^2}\longrightarrow\Delta:=\frac\pi{2\sqrt3},
\tag{EA.10}
```
we obtain

```math
\Delta
\le
\frac{\pi^2}{16}+1-\frac{4A_{FS}}\pi.
\tag{EA.11}
```

But the right side is

```math
0.8293886873\ldots,
```

whereas

```math
\Delta=0.9068996821\ldots.
```

The strict gap is approximately $`0.0775109948`$. This contradiction excludes every
unbounded perfect-matching sequence.

## 4. Exact target implication

The matching branch is removed without using a separate lower bound on the number of
external points. The stronger finite inequality is EA.2, which charges the external
population to the area deficit between the full diameter hull and the force hull,
with only a linear boundary error.

This does not close the forest branch with $`d_H>0`$, the cyclic branch with
$`d_H=0`$ and nonzero pinned/contact surplus, or the $`s_Z>0`$ branch. In particular,
it does not solve the global problem.

## 5. Dependencies

- `docs/reports/target_c_matching_branch_externalization_2026-09-09.md`, matching core
  normal form and EA.1.
- `docs/reports/target_c_fs_symmetric_difference_body_area_2026-09-10.md`, FSDB area
  floor (EA.7).
- `docs/problem/literature_baseline.md`, $`n/D^2\to\pi/(2\sqrt3)`$.
- The planar Steiner formula and perimeter-diameter inequality.

## 6. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| EA.2 external-annulus capacity | proved | disjoint radius-1/2 disks and inner/outer parallel bodies |
| EA.3 diameter form | proved | convex perimeter bound |
| perfect-matching closure | proved conditionally on the report-level matching/FSDB inputs | finite gap in EA.11 |
| all external rattler branches excluded | not proved | interior isolated points are not charged by EA |
| Level I | still open | forest, cyclic high-surplus, and positive (s_Z) branches remain |

## 7. Regression tests

- A thin force hull: EA remains valid; its boundary error is only (O(D)), but the
  theorem gives no quadratic saving if $`F`$ has small area.
- Points inside $`F`$: deliberately excluded from EA. They are the binding rattler
  regression for the general C-II branch.
- A disk force hull: EA reduces to the expected outer-annulus capacity estimate.
- The perfect matching shell: all non-core points are external by the matching ledger,
  so the theorem applies.

## 8. Failed routes and no-go

Applying EA to all contact-isolated source points in the general C-II branch is invalid:
the force-bulk audit permits contact-isolated points inside $`F`$. The inclusion (EA.4)
fails for centers in $`F`$, and no source-preserving transfer theorem currently moves
them outside $`F`$ while retaining the C65 positive support.

Thus EA is not a general rattler-elimination theorem.

## 9. Literature and computation

No external theorem beyond standard planar Steiner and inner-parallel estimates is
needed. The displayed decimals were evaluated directly from the exact expressions; no
numerical search is used.

## 10. Canonical promotion recommendation

**Hold as report.** The theorem is proved, but the matching branch is already excluded
by an independent report-level NB argument and is not the surviving global endpoint.
The reusable part is EA.2, not a change to the authoritative status.

## 11. Exact remaining lemma

The next decisive statement would have to extend EA.2 to the full source by proving an
interior-rattler capacity/transfer inequality of the form

```math
|A\cap\operatorname{int}F| - |V(C)|
\le \text{capacity charged to the uncovered source region},
```

with enough strictness to beat the asymptotic packing density. The present reports do
not prove such a transfer, and assuming it would be circular.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New theorem EA:
For convex F subset K and any 1-separated X in K\F,
    |X| pi/4 <= area(K)-area(F) + (per K+per F)/2 + pi/4.

Application:
In the perfect-matching branch, the positive core is pure rhombic,
v <= q^2/16+q/2+1, all non-core points are outside F, and FSDB gives
area(F)/D^2 >= (2rho+sin(2rho))/4. Therefore
    n/D^2 <= pi^2/16 + 1 - 4 A_FS/pi + o(1)
             = 0.8293886873...,
contradicting n/D^2 -> pi/(2sqrt3)=0.9068996821....

Binding no-go:
EA does not charge contact-isolated points inside F. Extending it to those
points is exactly the missing full-source capacity theorem.
```
