> Generated reading edition · [exact source](../../../docs/audits/target_c_section103_unique_wrapping_cap_deficit_hostile_audit_2026-09-12.md) · source SHA-256 `880bae6dcb7154653247db2d94b2f4aaf3bf9ddf67f64f038dbdc546a34bab31`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-B23E5F538839","canonical":true,"claim_ids":["C-UNIQUE-WRAP-CAP-DEFICIT"],"claim_statuses":{"C-UNIQUE-WRAP-CAP-DEFICIT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — Section 103 unique-wrapping cap-deficit hostile audit

**Date:** 2026-09-12
**Verdict:** **PASS as a proof-only theorem, with one cutoff/diagonal clarification recommended.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit checks the proof-only theorem in
[`../targets/target-c/103-unique-wrapping-cap-deficit-audit.md`](../targets/target-c/103-unique-wrapping-cap-deficit-audit.md)
against the canonical audit.42 Target C stack.

The result is correctly scoped as a concentration theorem under a common macroscopic
diameter cap. It does **not** assert that every Type-II survivor unconditionally has a
unique wrapping cell. Its useful form is:

> Fix `mu<1` and a Type-II full-core subsequential regime in which every positive-area
> macroscopic harmonic-cell limit has diameter at most `mu`. Then there is exactly one
> wrapping macroscopic cell sequence, and it carries normalized area at least
> `Gamma(mu)=pi/4-C(mu)`. All other macroscopic cells are cap type.

At `mu=mu_8=0.976040765267051982...`, the canonical cap-capacity formula gives

```math
\Gamma(\mu_8)=0.202319755440525\ldots .
```

The theorem passes hostile review. The only repair is to state the `eta->0` selection
as a diagonal argument, rather than implicitly treating a cell label selected at one
macroscopic cutoff as fixed for every smaller cutoff.

## 1. Canonical inputs are sufficient

The proof uses only already-canonical facts:

- Section 83 / `C-HARMONIC-CELL-TILING`: harmonic attachment cells are pairwise
  interior-disjoint, their total area is `pi D^2/4-o(D^2)` in the full-core branch,
  and
  
  ```math
  \sum_r\sqrt{\operatorname{area}(P_{r,D})}=O(D);
  ```

- Section 88 / `C-HARMONIC-WRAPPING`: every cap-type finite macroscopic limit family
  of diameter at most `mu<1` has total normalized area at most
  
  ```math
  \mathcal C(\mu)
  ={1\over8}\left[2\pi-k_\mu\sin\theta_\mu-\sin r_\mu\right]
  <{\pi\over4};
  ```

- audit.42 Section 102 is not needed to prove the concentration theorem itself; it is
  only a downstream use of the explicit constants.

No KKT coefficient floor, endpoint equality theorem, or deletion of contact-isolated
source points is used.

## 2. Interior-disjointness survives the macroscopic Hausdorff limit

Fix `eta>0` and retain cells with area at least `eta D^2`. Section 83's square-root
budget leaves only uniformly finitely many. After scaling by `D`, pass to a subsequence
on which all retained convex cells converge in Hausdorff distance to positive-area
convex bodies `K_r`.

Canonical Section 88 already uses the fact that these limits remain pairwise
interior-disjoint. For completeness, the point is robust: if
`int K_r cap int K_s` contained a point, it would contain a small closed disk. Convex
Hausdorff convergence of positive-area bodies puts a smaller concentric disk inside
both approximating interiors for all large indices, contradicting the finite Section-83
interior-disjointness.

Thus

```math
\operatorname{int}K_r\cap\operatorname{int}K_s=\varnothing
\qquad(r\ne s).
```

## 3. A wrapping cell of diameter below one contains the center in its interior

Let `S subset partial B_{1/2}` be compact, wrapping, and let
`K=conv(S)` have diameter `<1`.

Wrapping means that `S` is not contained in an open semicircle, equivalently
`0 in conv(S)`. Suppose instead that `0 in partial K`. A supporting line through the
origin places all of `S` in one closed half-plane. Any convex combination of points of
`S` equal to zero has zero value under the corresponding supporting functional, so
all points used by that combination lie on the supporting line. The radius-`1/2`
circle meets a line through the origin in one antipodal pair, and obtaining zero as a
convex combination requires both members of that pair. This would put two points of
`S` at Euclidean distance `1`, contradicting `diam K<1`.

Therefore

```math
\boxed{0\in\operatorname{int}K.}
```

The strict diameter assumption is available in every Section-103 application because
the common cap is a fixed `mu<1`.

## 4. At most one macroscopic wrapping limit

If two positive-area macroscopic limits `K_r,K_s` were wrapping, Step 3 would put
`0` in both interiors. This contradicts Step 2. Hence at most one retained macroscopic
cell can be wrapping.

This argument is purely convex-geometric. It does not assume that the original contact
graph is 2-connected and does not use the Section-102 corridor theorem.

## 5. The cap deficit forces existence and the full area lower bound

Put

```math
\Gamma(\mu):={\pi\over4}-\mathcal C(\mu)>0.
```

Section 83 gives the small-cell tail estimate

```math
\sum_{\operatorname{area}(P_{r,D})<\eta D^2}
\operatorname{area}(P_{r,D})
=O(\sqrt\eta D^2).
```

For fixed `eta`, pass to the finite macroscopic limit family. If every retained limit
were cap type, Section 88 would bound their total normalized area by `C(mu)`, while the
small-cell tail contributes only `O(sqrt eta)`. Choosing `eta` so small that this tail
is less than `Gamma(mu)/2` contradicts the total cell-area limit `pi/4`.

Thus, for every sufficiently small fixed cutoff, one retained macroscopic cell is
wrapping; Step 4 makes it unique.

The precise `eta->0` conclusion should be stated diagonally. Choose `eta_j downarrow0`.
For each `j`, after taking the large-`D` limit select the unique wrapping cell in the
`eta_j`-macroscopic family. Its normalized area satisfies

```math
{\operatorname{area}(P_{w,D})\over D^2}
\ge {\pi\over4}-\mathcal C(\mu)-O(\sqrt{\eta_j})-o_D(1).
```

Choose a diagonal sequence `D_j->infinity`. Compactness of convex subsets of the unit
disk gives a limiting wrapping cell `K_w`, and the displayed lower bound yields

```math
\boxed{
\operatorname{area}(K_w)\ge\Gamma(\mu).
}
```

Equivalently one obtains a finite cell sequence with

```math
\operatorname{area}(P_{w,D})
\ge(\Gamma(\mu)-o(1))D^2.
```

This is the same conclusion as Section 103. The clarification removes only an implicit
cell-label persistence assumption across changing cutoffs.

## 6. The numerical cap-deficit constant is correct

At the canonical Section-101 endpoint

```math
\theta_8=2.70290802964836768\ldots,
\qquad
\mu_8=\sin(\theta_8/2)=0.976040765267051982\ldots,
```

we have `k_mu8=2` and

```math
r_{\mu_8}=2\pi-2\theta_8=\phi_8.
```

Substituting in the canonical Section-88 capacity formula gives

```math
\mathcal C(\mu_8)=0.583078407956923\ldots,
```

and hence

```math
\boxed{
\Gamma(\mu_8)
={\pi\over4}-\mathcal C(\mu_8)
=0.202319755440525\ldots .
}
```

This agrees with the independently registered Section-101 scalar certificate.

Audit.42 Section 102 makes the exact `mu_8` endpoint impossible, so this number should
not be advertised as an attained current carrier area. Its correct role is a stability
constant in hypothetical common-cap regimes with `mu>mu_8` close to `mu_8`, where
continuity keeps `Gamma(mu)` close to the displayed value.

## 7. The local rhombus/train constants follow

For `mu>mu_8` sufficiently close to `mu_8`, continuity gives

```math
\Gamma(\mu)>0.19.
```

The unique wrapping carrier then has area at least `(0.19-o(1))D^2`. Section 83's
nonnegative summed local rhombic deficit is `o(D^2)`, so that carrier itself has
strict-rhombus area

```math
A_{4,w}\ge(0.19-o(1))D^2.
```

Every unit rhombus has area at most one, hence its strict-rhombus count satisfies, for
all large `D`,

```math
\boxed{R_D\ge0.18D^2.}
```

Canonical Section 89 gives

```math
T_D\le6a_D-15-5s_D-3c_D\le6a_D+O(1).
```

For a wrapping limit with `theta` in a sufficiently small fixed neighborhood of
`theta_8`, canonical Section 100 gives

```math
{a_D\over D}
\le {3\theta-2\pi\over2}+o(1)<1.
```

(The endpoint value of the right-hand side is approximately `0.91276939`.) Therefore
one may indeed use the coarse uniform bound

```math
\boxed{T_D\le6D}
```

for all sufficiently large members of that fixed neighborhood.

## 8. The phase-defect constant is the canonical Section-68 quantity

Section 68 defines

```math
\Delta_{train}:=\sum_R\delta_R
```

for the same strict-rhombus angular defects used by the Section-90 phase binning. It
proves

```math
{3\Delta_{train}\over\pi}
\le(2+\sqrt3)E_4
<(2+\sqrt3)c_0\operatorname{per}(K),
\qquad c_0={\sqrt3\over4},
```

and `per(K)<=pi D`. Therefore

```math
\boxed{
\Delta_{train}
<{\pi^2\sqrt3(2+\sqrt3)\over12}D
=5.31651047915437\ldots D.
}
```

Restriction to one harmonic carrier can only decrease this nonnegative defect sum, so
Section 103's rounded constant `5.317` is valid.

Thus the explicit local constants

```math
(r,C_T,C_{phase})=(0.18,6,5.317)
```

are legitimate inputs for a quantitative stability version of canonical Section 102.

## 9. Disposition

**PASS.** Section 103 is mathematically valid under its stated common-macroscopic-cap
scope. The recommended source repair is only to make the cutoff/diagonal selection in
Section 103.4 explicit.

Recommended lifecycle action after that wording repair: promote the theorem as a
structural concentration result, not as a new unconditional diameter bound. A suitable
claim should state that, in any Type-II full-core subsequential regime with all
positive-area macroscopic cell diameters bounded by a fixed `mu<1`, exactly one
wrapping macroscopic carrier exists and has area at least
`(Gamma(mu)-o(1))D^2`; near `mu_8`, the explicit constants above are available for
quantifying the canonical Section-102 phase/corridor contradiction. C-II remains open.
