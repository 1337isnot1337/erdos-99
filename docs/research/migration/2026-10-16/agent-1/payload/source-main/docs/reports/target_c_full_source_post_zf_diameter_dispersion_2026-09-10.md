<!-- theorem-state: {"artifact_id":"ART-72317C6CB485","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — full-source/post-ZF diameter dispersion

**Date:** 2026-09-10  
**Repository state:** branch `research/target-c-full-source-closure-2026-09-10` from `3f37ef0eab4407a411f9a6d51d016ba600302be7`  
**Run type:** closing-proof continuation / dependency audit  
**Target:** Target C, Gate C-II  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used for the theorem below  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The full-source circumradius report gives an asymptotically vanishing angle between any two actual diameter edges sharing an endpoint. The audited post-ZF chain independently forces at least `ceil(D)` actual diameter edges. Combining the two gives a support-dispersion theorem that is stronger than the previous one-star exclusion: no bounded set of diameter vertices can cover the actual diameter support, and there is a growing family of vertex-disjoint pairwise crossing diameter chords.

This does not yet give a quantitative lower bound on their KKT weight. The regular odd-shell regression satisfies the new conclusion. Thus the theorem is structural progress toward C-II, not Level I closure.

## 1. Starting endpoint

For the contact/diameter-lexicographically minimal hypothetical C-II source, the audited report-level ZF/ZS chain gives

\[
 h\ge\delta\ge\lceil D\rceil,
\]

where `h=|H|` is the number of actual diameter pairs.

The unpromoted full-source report proves, for the same source and in fact for every global minimizer, that with

\[
\eta_D=3^{1/4}\sqrt D,
\]

any two actual diameter edges sharing an endpoint make angle less than

\[
\vartheta_D
:=
\min\left\{
\frac\pi3,
2\arccos\frac{D}{D+2\eta_D}
\right\}
=O(D^{-1/4}).
\]

It also proves that, about a common circumcenter `o` of the full source hull, every actual diameter-pair midpoint lies within

\[
L_D:=\sqrt{D\eta_D+\eta_D^2}=O(D^{3/4})
\]

of `o`.

The implication attacked here is

```text
h >= D + full-source shared-endpoint angle collapse
    -> sublinear maximum diameter degree
    -> growing diameter vertex-cover number
    -> growing vertex-disjoint crossing diameter matching.
```

## 2. Audit of the full-source inputs

The parts of `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md` used below survive a direct dependency check.

1. Its source-hull Bonnesen estimate uses only the unconditional strict translated-lattice inequality from Target B Section 36.1, Oler, Cauchy's perimeter bound, and the source-hull part of Target A Section 155. No smaller optimum, very-super-boundary hypothesis, hull saturation, or isolate bound is used.
2. The shared-diameter angle estimate is purely geometric after that circumradius bound: three source points consisting of one common endpoint and two diameter partners lie in the same source circumdisk.
3. The midpoint estimate is the parallelogram identity applied to an actual diameter pair in that same circumdisk.
4. These statements concern the full source and therefore retain contact-isolated points. They are compatible with the contact/diameter lexicographic representative used by ZF/ZS.

The response-radialization part of the full-source report is not needed for the theorem below.

## 3. Strongest genuinely new audited theorem

### Theorem FSD — post-ZF diameter support dispersion

Assume a sufficiently large triangle-free global minimizer has been chosen first to minimize unit contacts and then to minimize diameter pairs, and assume the audited ZR/ZF/ZS conclusions. Let `H` be its full actual diameter graph and put

\[
a_D:=2\arcsin\frac1{2D},
\qquad
\Delta_D:=
\left\lceil\frac{\vartheta_D}{a_D}\right\rceil.
\]

Then:

\[
\boxed{\Delta(H)\le\Delta_D,}
\tag{FSD.1}
\]

\[
\boxed{
\tau(H)\ge
\left\lceil\frac{h}{\Delta_D}\right\rceil
\ge
\left\lceil\frac{\lceil D\rceil}{\Delta_D}\right\rceil,
}
\tag{FSD.2}
\]

where `tau(H)` is the minimum vertex-cover number, and

\[
\boxed{
\nu(H)\ge
\left\lceil\frac{h}{2\Delta_D}\right\rceil
\ge
\left\lceil\frac{\lceil D\rceil}{2\Delta_D}\right\rceil,
}
\tag{FSD.3}
\]

where `nu(H)` is the maximum matching number.

Moreover the matching in FSD.3 consists of pairwise properly crossing straight diameter chords, and every one of those chords meets the common disk

\[
\boxed{B(o,L_D).}
\tag{FSD.4}
\]

Asymptotically,

\[
\boxed{
\Delta_D=(4\,3^{1/8}+o(1))D^{3/4},
}
\tag{FSD.5}
\]

so

\[
\boxed{
\tau(H)\ge
\left(\frac1{4\,3^{1/8}}+o(1)\right)D^{1/4},
}
\tag{FSD.6}
\]

and

\[
\boxed{
\nu(H)\ge
\left(\frac1{8\,3^{1/8}}+o(1)\right)D^{1/4}.
}
\tag{FSD.7}
\]

Thus every bounded-hub or `O(1)`-vertex-cover model of the actual post-ZF diameter support is impossible.

### Scope

FSD concerns the full actual diameter graph of the lexicographically normalized C-II source. It uses global minimum-diameter information through the full-source circumradius estimate and ZF/ZS. It does not include contact-isolated points as vertices of the diameter graph: the promoted `H=H_*` normalization and KKT endpoint visibility already exclude isolates from actual diameter pairs.

FSD is a support theorem only. It does not give a lower bound on the total `beta`-weight carried by a matching or outside a small vertex set.

### Proof

Fix an actual diameter vertex `b`, with distinct diameter partners

\[
k_1,\ldots,k_d,
\qquad d=\deg_H(b).
\]

All partners lie on the radius-`D` circle centered at `b`. Unit separation gives

\[
|k_i-k_j|\ge1
\qquad(i\ne j).
\]

If `phi_ij` is the smaller angle between the rays `bk_i` and `bk_j`, then

\[
|k_i-k_j|=2D\sin(\phi_{ij}/2),
\]

hence

\[
\phi_{ij}\ge a_D.
\tag{FSD.8}
\]

The full-source shared-endpoint theorem gives

\[
\phi_{ij}<\vartheta_D
\qquad(i\ne j).
\tag{FSD.9}
\]

Because `vartheta_D<=pi/3<pi`, the partner directions lie in one ordinary angular interval of width strictly less than `vartheta_D`. Ordering them in that interval and applying FSD.8 to consecutive directions gives

\[
(d-1)a_D<\vartheta_D.
\]

Therefore

\[
d\le\left\lceil\frac{\vartheta_D}{a_D}\right\rceil=\Delta_D,
\]

proving FSD.1.

If `S` is any vertex cover of `H`, every one of the `h` edges is incident to a vertex of `S`. Thus

\[
h\le\sum_{v\in S}\deg_H(v)\le |S|\Delta_D,
\]

which proves FSD.2.

Let `M` be a maximum matching. It is maximal, so the set of its `2|M|` endpoints is a vertex cover: otherwise an edge with neither endpoint covered could be added to `M`. Hence

\[
\tau(H)\le2\nu(H).
\]

Together with FSD.2 this proves FSD.3.

The planar diameter graph is a straight-line thrackle: two diameter edges either share an endpoint or cross. Distinct edges in a matching share no endpoint, so they cross properly pairwise. The full-source midpoint theorem gives

\[
\left|\frac{b+k}{2}-o\right|\le L_D
\]

for every actual diameter edge `bk`; its midpoint lies on the chord itself, proving FSD.4.

Finally

\[
\eta_D=3^{1/4}D^{1/2},
\]

so

\[
2\arccos\frac{D}{D+2\eta_D}
=(4\,3^{1/8}+o(1))D^{-1/4},
\]

while

\[
a_D=(1+o(1))D^{-1}.
\]

For large `D` the arccosine term is below `pi/3`; division proves FSD.5. Insert `h>=ceil(D)` into FSD.2-FSD.3 to obtain FSD.6-FSD.7. `square`

### Dependencies

- `docs/targets/target-c/56-ci-restored-frontier.md`: contact/diameter lexicographic source and full actual support.
- `docs/reports/campaign_zero_transfer_and_narrow_paths_2026-09-09.md`: audited report-level ZR/ZF.
- `docs/reports/target_c_zf_boundary_surplus_collapse_2026-09-09.md`: ZS, in particular `h>=delta>=ceil(D)`.
- `docs/reports/target_c_full_source_circumradius_response_2026-09-10.md`: full-source shared-endpoint angle and midpoint bounds.
- Canonical Hopf-Pannwitz/diameter-thrackle structure already used in the Target C stack.

### Why it is new

ZS proves only that every single star misses a linear number of actual diameter edges, using the older asymptotically linear maximum-degree bound. FSD upgrades the maximum degree to `O(D^(3/4))`. Consequently every vertex cover must grow as `Omega(D^(1/4))`, and the actual support contains `Omega(D^(1/4))` vertex-disjoint pairwise crossing diameter chords. No such matching/cover consequence appears in the starting full-source report or the ZS report.

## 4. Exact target implication

FSD removes all bounded-hub support models from the post-ZF source. Any closing argument may now assume a growing family of disjoint diameter pairs whose endpoints are all force-hull vertices and whose chords are simultaneously near-centered at the full-source circumcenter.

A response-theoretic closure would follow from either of these stronger quantitative transports:

\[
\boxed{
\text{FSD matching}\Longrightarrow
\sum_{h\in M}\beta_h\ge c>0,
}
\tag{FSD-W}
\]

for some matching `M` of the guaranteed type, or

\[
\boxed{
\text{FSD matching + circular-planar response}
\Longrightarrow
\delta_K+\mathscr O_A\ge c_0P
\text{ or a strict sub-}D\text{ competitor.}
}
\tag{FSD-C}
\]

Neither implication is proved here. Relative-interior positivity alone gives no uniform weight floor.

## 5. Exact remaining lemma

The whole-source scalar endpoint is

\[
\delta_K+\mathscr O_A\ge c_0P.
\]

Since

\[
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,
\qquad
\mathscr O_A=\operatorname{area}K+c_0P-a_0(n-1),
\]

this is exactly equivalent to

\[
\boxed{
D^2\ge\frac{2\sqrt3}{\pi}(n-1).
}
\tag{FSD.10}
\]

The unconditional translated-lattice comparison gives the strict reverse inequality for every global minimizer. Therefore proving FSD.10 from the triangle-free post-ZF/full-source structure would close Level I immediately.

FSD does not yet supply the required order-`D` boundary-capacity loss. The highest-value next lemma is a quantitative transport from the growing near-centered crossing matching into either finite packing capacity or aggregate response weight/defect.

## 6. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| full-source FS.1 circumradius bound | proved in source report; dependency-audited here | uses unconditional source-hull inputs only |
| full-source shared-endpoint angle collapse | proved in source report; dependency-audited here | direct three-point circumradius geometry |
| full-source midpoint localization | proved in source report; dependency-audited here | parallelogram identity in common circumdisk |
| ZF/ZS `h>=ceil(D)` | report-level audited dependency | September 9 consolidated audit plus ZS |
| FSD.1-FSD.7 | proved | elementary combination of the preceding exact inputs |
| positive `beta` mass on an FSD matching | not proved | support positivity has no uniform numerical floor |
| Level I | still open | boundary-capacity/weight transport remains |

## 7. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| regular odd shell | yes | `Delta(H)=2`, it has a matching of order `D`, and all diameter chords are nearly centered; it lacks large-`n` global optimality |
| dense isolated shell filling | yes | isolates do not change `H`, the shell stress, or midpoint geometry; no global-optimality certificate exists |
| exact support star | excluded | FSD.1 and `h>=D` force vertex-cover number to diverge |
| asymptotic weight star | survives | many off-hub edges may carry arbitrarily small positive total `beta` mass |

## 8. Failed routes and no-go results

1. `many support edges -> positive aggregate beta mass` is unjustified. Relative-interior KKT positivity is qualitative only.
2. `near-centered diameter matching -> small response trace` is false. The regular odd shell has near-centered diameter chords but response trace defect of order `D^2`.
3. `near-centered diameter matching -> near-disk force-hull area` is not established. A geometric area theorem would need additional directional-spread information.

## 9. Computation and reproducibility

No computation is used in FSD. The constants follow from elementary asymptotic expansions; they are not numerical certificates.

## 10. Canonical promotion recommendation

**Hold as report.**

FSD is exact and useful, but it depends on the still-unpromoted full-source report and report-level ZF/ZS chain. It should be promoted only after those dependencies are independently promoted or the theorem is re-proved from promoted equivalents.

## 11. Next run

Attack the following single transport theorem:

> Given the FSD family of `Omega(D^(1/4))` pairwise crossing actual diameter chords, all with midpoints in `B(o,O(D^(3/4)))`, prove either an order-`D` finite-packing loss relative to the full source hull or a quantitative aggregate response/diameter-weight obstruction. The conclusion must imply FSD.10 or construct a strict sub-`D` competitor.

The first regression is the regular odd shell with dense isolated filling. Any successful statement must identify the exact global-optimality input that this regression lacks.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem FSD:
For the post-ZF lexicographic C-II source, set
  eta_D=3^(1/4)sqrt(D),
  vartheta_D=min(pi/3,2 arccos(D/(D+2 eta_D))),
  a_D=2 asin(1/(2D)),
  Delta_D=ceil(vartheta_D/a_D).
Then
  Delta(H)<=Delta_D=(4*3^(1/8)+o(1))D^(3/4),
  tau(H)>=h/Delta_D=Omega(D^(1/4)),
  nu(H)>=h/(2Delta_D)=Omega(D^(1/4)).
A matching of that size consists of pairwise crossing actual diameter chords, and
each chord midpoint lies within L_D=sqrt(D eta_D+eta_D^2)=O(D^(3/4)) of the common
full-source circumcenter.

Exact endpoint now:
  delta_K+O_A>=c0 P
is exactly
  D^2 >= (2sqrt3/pi)(n-1),
which contradicts the unconditional strict translated-lattice bound.

Binding regression:
regular odd shells and dense isolated shell fillings satisfy the new support geometry;
they fail only at global optimality.

Highest-value next lemma:
transport the growing near-centered crossing matching into an order-D packing loss or
a quantitative aggregate response/weight obstruction.
```