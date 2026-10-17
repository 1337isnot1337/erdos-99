> Generated reading edition · [exact source](../../../docs/reports/target_c_antipodal_exterior_cap_pairing_2026-09-25.md) · source SHA-256 `40d03e694318f912ee032917b83f7df35c8f2c8d7b4d55b46d81e8050c2afee0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C260F41AC9AA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — antipodal pairing of macroscopic exterior isolate caps

**Date:** 2026-09-25  
**Repository commit:** `404e8d49ddb1ee14cd0f69a83e7f120e77b3ab33`  
**State version:** `2026-09-14.audit.51`  
**Run type:** closing-proof continuation  
**Target:** C-II, macroscopic exterior-container branch  
**Starting status:** canonical `C-FS-GEOM`, `C-DB-DENSITY`, `C-INACTIVE-CHAMBER`, `C-FULLCORE-NEAR-DISK`
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`  
**External literature search:** a narrow search found no theorem used in the proof  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`.

## 1. Starting canonical endpoint

Canonical Sections 77--80 leave a Type-I branch in which one exterior cap of the
actual force hull contains `Omega(D^2)` contact-isolated source points with
`O(D)` Oler slack. Its cap is an actual component of the source hull outside the
force hull. No source-preserving strict sub-`D` competitor is known.

The attempted closure chain was

```text
diameter-partner antipodality + near-disk source hull
  -> paired macroscopic exterior isolate caps (proved below)
  -> paired-cap source replacement or exact triangle (still missing)
  -> Type-I exclusion, then C-II/Level-I closure (not obtained).
```

The first arrow is a source-level theorem. The second arrow is an open bridge;
pairing itself is not a diameter improvement.

## 2. Antipodal cap theorem

**Classification:** proved candidate awaiting independent audit; as a repository
artifact this report remains `unreviewed` and noncanonical.

Let `A_j` be any sequence of canonical contact-minimal, then
diameter-pair-minimal triangle-free global minimizers with `D_j -> infinity`.
Retain **all** source points. Let `K_j=conv(A_j)`, let `o_j` be its circumcenter,
and let `F_j` be the convex hull of every endpoint of the full actual diameter
graph. Let `C_j` be a Section-77 exterior cap between consecutive vertices of
`F_j`. Write `a_j=area(C_j)` and let `z_j` count its assigned actual
contact-isolated source points.

### Theorem 1 (macroscopic caps pair)

If `liminf a_j/D_j^2 > 0`, there are **distinct** exterior caps `C'_j` of the
same sources, for all sufficiently large `j`, such that

$$
 {area(C'_j)-area(C_j)\over D_j^2}\longrightarrow0,
 \qquad {z'_j-z_j\over D_j^2}\longrightarrow0.
$$

Along every convergent subsequence of the normalized caps, the normalized
`C'_j-o_j` converge to the half-turn image of the limit of `C_j-o_j`. In
particular, an exterior cap with quadratic population forces a second,
opposite exterior cap with the same leading population. A single cap cannot
carry more than half of the total exterior source population to leading order:

$$
 z_j\le {Z_{{ext},j}\over2}+o(D_j^2).
$$

Let `I_j` and `I'_j` be the convex hulls of the actual assigned isolates in
the two caps. For every fixed positive lower bound on `a_j/D_j^2`,

$$
 d_H(I_j,C_j)=O(\sqrt{D_j}),\qquad
 d_H(I'_j,C'_j)=O(\sqrt{D_j}),\qquad
 {d_H(I'_j-o_j,-(I_j-o_j))\over D_j}\longrightarrow0.
$$

Thus the paired **actual isolate hulls**, as well as the containers, have
antipodal normalized limits. The `O(sqrt D)` constant can depend on the fixed
cap-area lower bound.

The `o(D_j^2)` terms are sequence-uniform in the usual contradiction sense:
for each fixed positive lower bound on `a_j/D_j^2`, no sequence violates the
conclusions by a fixed positive multiple of `D_j^2`.

### Proof

Write `D=D_j` temporarily, and translate by `o_j`. Canonical `C-FS-GEOM`
(Section 58, FS.1) gives a circumradius `R` and inradius `r` for `K_j` with

$$
 D/2\le R<D/2+\eta_D,\qquad R-r<\eta_D,
 \qquad \eta_D=3^{1/4}\sqrt D.
$$

If `c` is an incenter, containment of its inscribed disk in the circumdisk
gives `|c-o_j|+r <= R`. Thus

$$
 B(o_j,D/2-2\eta_D)\subseteq K_j
 \subseteq B(o_j,D/2+\eta_D).
 \tag{1}
$$

After division by `D`, `K_j-o_j` therefore converges in Hausdorff distance to
the centered radius-`1/2` disk `B`.

Every vertex `b` of `F_j` is an actual diameter endpoint. It has a partner
`k` at distance `D`. FS.1 puts both vertices in the circumdisk, whence
`D/2-eta_D <= |b-o_j| <= D/2+eta_D`. Canonical FS.6 further gives

$$
 |k-(2o_j-b)|<2L_D,
 \qquad L_D=\sqrt{D\eta_D+\eta_D^2}=o(D).
 \tag{2}
$$

Consequently the normalized loaded-vertex sets lie within `o(1)` of the
radius-`1/2` circle and are `o(1)`-invariant under a half-turn. Canonical
`C-DB-DENSITY` (Section 59, DB.29--DB.30) gives an origin-centered disk of
radius `(sin(rho)/2-o(1))D` inside `F_j`, where `rho=cos(rho)>0`. Thus `o_j`
lies in the interior of `F_j` for large `j`, and the cyclic loaded-vertex
order is their polar-angle order.

Pass to any subsequence on which the two endpoints `u_j,v_j` of the side
closing `C_j`, divided by `D_j` after centering, converge to `u,v` on the
radius-`1/2` circle. The outward polar arc from `u_j` to `v_j` contains no
other loaded vertex. It has angular length less than `pi` by the centered
inball. Because `a_j/D_j^2` is bounded away from zero, its limiting length
`theta` is positive: by (1), a cap with angular length tending to zero has
vanishing normalized area.

Take a Hausdorff limit `S` of the normalized loaded-vertex sets. Equation
(2) makes `S=-S`. The open arc from `u` to `v` contains no point of `S`,
while `u,v` belong to `S`. Its antipodal arc from `-u` to `-v` likewise
contains no point of `S`, and its endpoints belong to `S`. Choose a fixed
angle in the middle of that opposite arc. For each large `j`, take the
consecutive loaded vertices immediately before and after that angle. Their
normalized positions converge to `-u,-v`: any other limiting endpoint would
be a point of `S` strictly inside the empty opposite arc. They close an
exterior cap `C'_j` for large `j`, since the opposite limiting arc has
positive length. It is distinct from `C_j` because the two limiting arcs are
antipodal and have length less than `pi`.

By (1), intersection of `K_j/D_j` with the outward half-plane of either
closing chord converges to the circular segment of `B` cut off by its limit
chord. These two limit chords are antipodal, so their circular segments are
half-turn images and have equal area. This proves
`[area(C'_j)-area(C_j)]/D_j^2 -> 0`. It also proves the asserted limit-shape
statement.

Canonical Section 80, equations (80.13)--(80.14), gives for every cap

$$
 z_i={area(C_i)\over a_0}+{per(C_i)\over2}-1-\sigma_i,
 \qquad a_0=\sqrt3/2,
 \qquad \sum_i\sigma_i=O(D),
 \tag{3}
$$

with all `sigma_i>=0` and `sum_i per(C_i)<=2pi D`. Hence, uniformly over
individual caps, `z_i=area(C_i)/a_0+O(D)`. Applying this to the pair proves
`(z'_j-z_j)/D_j^2 -> 0`. Since the two caps are distinct and all exterior
populations are nonnegative, `Z_ext>=z_j+z'_j=2z_j-o(D_j^2)`.

It remains to transfer the container statement to the actual isolate hulls.
For either member `C_i` of the pair, put `I_i=conv(Z_i)`. Equation (3) and
`sigma_i=O(D)` give `a_0 z_i >= area(C_i)-O(D)`. Oler applied directly to the
unit-separated set `Z_i` in its own hull, together with convex perimeter
monotonicity, gives

$$
 a_0 z_i\le area(I_i)+c_0 per(I_i)+a_0
 \le area(I_i)+c_0 per(C_i)+a_0
 =area(I_i)+O(D),
 \qquad c_0=\sqrt3/4.
$$

Hence `area(C_i)-area(I_i)=O(D)`. Both caps have area at least a fixed
positive multiple of `D^2` and perimeter at most `2pi D`. Here is the
convex estimate at the needed external-cap scope. If `r_i` is the inradius
of `C_i`, coarea for its inner parallel bodies gives
`area(C_i)=integral_0^{r_i} per((C_i)_{-t}) dt <=r_i per(C_i)`. Thus
`r_i>=area(C_i)/per(C_i)=Omega(D)`.

For a unit direction `u`, put `t=h_{C_i}(u)-h_{I_i}(u)`. Choose an inball
`B(c,r_i)` and a support point `v` of `C_i` in direction `u`. Set
`s_0=h_{C_i}(u)-u dot c`; then `r_i<=s_0<=D`. If `w` is perpendicular to
`u`, the triangle with vertices `v,c+r_i w,c-r_i w` lies in `C_i`. Its
height-`s` cap, for `s=min(t,r_i)`, lies outside `I_i` and has area
`r_i s^2/s_0 >=(r_i/D)s^2`. Since the total area outside `I_i` is
`O(D)` while `r_i=Omega(D)`, the case `t>r_i` would give an `Omega(D^2)`
deficit and is impossible for large `D`. Hence `t^2=O(D)` uniformly in
`u`. The supremum of these support gaps is `d_H(I_i,C_i)` for nested
convex bodies, so it is `O(sqrt D)`. The asserted antipodal isolate-hull
limit now follows from the triangle inequality and the cap limit already
proved. These are the general convex arguments previously used for
internal chambers in CH.1--CH.2; they are proved here to avoid extending
that promoted theorem beyond its internal-chamber scope.

If the theorem failed uniformly for a fixed positive cap-area fraction,
choose a violating sequence, extract the subsequences above, and obtain the
same contradiction. This removes any hidden choice of a preferred cap or
limit. $\square$

### Corollary 2 (individual cap ceiling)

Every exterior cap satisfies

$$
 \limsup {area(C_i)\over D^2}
 \le {\pi-2\rho-\sin(2\rho)\over8}
 ={1\over2}\left({\pi\over4}-A_{SC}\right),
 \qquad A_{SC}={2\rho+\sin(2\rho)\over4},
 \tag{4}
$$

and its assigned source population has limsup at most the right-hand side
divided by `a_0`. This ceiling also follows directly from canonical DB.30:
every loaded-hull closing chord has distance at least
`(sin(rho)/2-o(1))D` from `o_j`; its limiting circular-segment angle is at
most `pi-2rho`, and a radius-`1/2` segment of angle `theta` has area
`(theta-sin theta)/8`. It is recorded here to state the scope of the
pairing, not as an independent improvement over Section 59.

### Corollary 3 (all quadratic exterior mass lies in paired caps)

For every fixed `epsilon>0`, at most `pi/(4epsilon)+o(1)` caps have area at
least `epsilon D^2`. The caps below that threshold satisfy

$$
 \sum_{area(C_i)<\epsilon D^2}area(C_i)
 \le\sqrt{\pi\epsilon}\,D^2,
 \qquad
 \sum_{area(C_i)<\epsilon D^2}z_i
 \le {\sqrt{\pi\epsilon}\over a_0}D^2+O(D).
 \tag{5}
$$

Indeed, Section 80 gives `sum_i per(C_i)<=2pi D`. Isoperimetry then yields
`sum_i sqrt(area(C_i))<=sqrt(pi)D`; multiply by the largest square root
among the small caps. The population estimate follows by summing the upper
side of (3). The number of large caps follows from their disjoint areas and
`area(K)<=pi D^2/4`. Theorem 1 pairs each large cap at leading order;
letting `epsilon` decrease shows that **all** quadratic exterior population
is accounted for by finitely many antipodal pairs up to an arbitrarily small
quadratic remainder. This is an order-of-limits statement, not a uniform
fixed number of cap pairs.

### Scope and dependencies

The theorem applies only to the canonical C-II source with the full actual
diameter graph and its relative-interior stress. It is a statement about
**actual source hull caps and actual contact-isolated source points**, not a
scaffold or a selected proper subset of diameter edges. It is asymptotic and
does not assert a finite exact symmetry, a triangle, or a strict competitor.

- `C-FS-GEOM`: `docs/targets/target-c/58-full-source-geometry-audit.md`, FS.1
  and FS.6, canonical.
- `C-DB-DENSITY`: `docs/targets/target-c/59-difference-body-density-audit.md`,
  DB.29--DB.30 and the full actual diameter-endpoint identification, canonical.
- `C-INACTIVE-CHAMBER` and `C-FULLCORE-NEAR-DISK`:
  `docs/targets/target-c/77-inactive-chamber-saturation-audit.md`, Section
  77.2, and `80-global-isolate-concentration-fullcore-disk-audit.md`,
  Section 80.1, canonical.

The elementary convex cap estimates are fully proved above. The internal-
chamber conclusion of `C-INACTIVE-HULL-STABILITY` is **not** imported to
an exterior cap.

## 3. Frontier effect and failed closure attempt

The theorem sharpens the **exterior** part of Type I: quadratic cap population
occurs in antipodal pairs with equal leading populations. It does not change
the canonical ledger, and it says nothing comparable about an internal inactive
chamber.

I tried to turn the paired caps into a same-cardinality competitor by
repacking their isolates while leaving the loaded core fixed. That cannot
lower the diameter: the old diameter pair remains in the fixed core. I also
tried to infer positive KKT support from newly created cap or chamber contacts;
proof-only Section 95 gives the exact obstruction for protected isolated
components. The missing step must move or replace old diameter-carrying
points while preserving **all** unit-separation constraints.

There is no scalar packing contradiction from the pairing alone. The
canonical translated-lattice comparison gives
`a_0(n-1)>pi D^2/4`, while Oler on the full source hull permits
`a_0 n<=pi D^2/4+c_0 pi D+a_0`. Pairing redistributes the exterior
population but does not remove this boundary-order allowance. A proposed
counting closure therefore still needs an additional **signed** boundary or
interface deficit that exceeds the allowance, or an explicit competitor.

## 4. Exact remaining lemma

**Paired-cap core release.** For all sufficiently large canonical Type-I
triangle-free global minimizers having a macroscopic exterior cap, prove that
the two actual antipodal quadratic isolate caps, together with the intervening
loaded core, force either an exact unit triangle in the original source or a
same-cardinality unit-separated configuration of diameter strictly below
`D`. The present theorem supplies the paired-cap hypothesis but no release.

The internal-chamber Type-I branch and the full-core Type-II branch remain
separate open obligations.

## 5. Claim and regression audit

| Claim | Status | Decisive scope check |
| --- | --- | --- |
| Macroscopic exterior caps and actual isolate hulls pair | proved candidate awaiting independent audit | Uses full actual diameter endpoints and every source point. |
| Pairing alone reduces diameter | rejected attempt | Keeping the old loaded core fixed retains an actual distance `D`. |
| One cap holds at most half the external population to leading order | proved candidate awaiting independent audit | Follows from a distinct paired cap and nonnegative remaining counts. |
| Cap ceiling (4) | canonical consequence restated | Already follows from DB.30; no new constant. |

The argument does not use the rejected Euler-trail inference, FB4, RSR
uniqueness, five-host occupancy, or a full-source extension of ZR/ZF. Contact-
isolated points are retained and counted. A near-antipodal loaded set is not
silently treated as exactly centrally symmetric. The known regular-shell and
strict near-equilateral packing regressions show why leading symmetry and
density are insufficient for global optimality or exact contacts.

## 6. Literature and computation

No external theorem is a dependency. A narrow literature search about
second-order disk-packing capacity found no result used here. No script or
numerical output is load-bearing.

## 7. Promotion recommendation and handoff

**Unreviewed.** Preserve this report and request an independent audit of the
opposite-gap selection and the cap-population transfer before considering
promotion. No canonical state or prompt change is warranted until that audit.

The next agent should read Sections 58, 59, 77, 80 and this report, then attack
the paired-cap core-release lemma above. Section 95 blocks a contact-creation
argument that leaves the old core unchanged.
