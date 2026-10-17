> Generated reading edition · [exact source](../../../docs/reports/target_c_minimal_interface_single_central_face_2026-09-09.md) · source SHA-256 `d851380304235d869ea5a8e58f3df3ca0ca7ab3f1469a58ce4ddcffa52578e9e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 25 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-3D85201F6CE0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_minimal_interface_single_central_face_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=afca4495c8fe103883240b4d01f203a21b4cf6b3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal interface defect collapses to one central doubled-geodesic face

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** equality-topology / geometric concentration theorem  
**Target:** full-core near-circle endpoint with `Q_B/D->2`  
**Depends on:** FS minimal-perimeter stability, AS annular saturation, MF macroscopic-face collapse, HG two semicircle groups, C36/C49 attachment geometry  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The previous reports left two apparent ways to realize the sharp interface lower bound

```math
Q_B=(2+o(1))D:
```

- diffuse excess through many annular exceptional faces;
- concentration in one or a few long transition faces.

At equality the diffuse option disappears.

There are two dominant harmonic components `I_1,I_2` whose attachment hulls and component convex hulls converge to complementary half-disks. Their outer contact-face walks split into

- shell-facing arcs of length `(pi/2+o(1))D`;
- inward diameter-side paths of length `D+o(D)`.

The regular shell-facing interface faces carry only `o(D)` total defect. Every remaining harmonic component has total attachment-cell perimeter `o(D)` and therefore lies in an `o(D)` boundary layer near the force hull. Thus the two diameter-side paths face one another across one graph-free central region throughout all but `o(D)` of their length.

That region is a single bounded contact face `F_*`. Consequently

```math
\boxed{
k_{F_*}=(2+o(1))D,
\qquad
Q_{F_*}=(2+o(1))D,
}
\tag{CF.1}
```

and

```math
\boxed{
Q_B-Q_{F_*}=o(D).
}
\tag{CF.2}
```

Moreover the two long sides of `F_*` are exactly the diameter-side outer-boundary paths of `I_1,I_2`, each of length `D+o(D)`, and MF implies that the normalized convex face converges to their common diameter segment.

Therefore the sharp full-core near-circle equality model is no longer a generic loaded-interface network. It is:

```text
near-circular loaded shell
+ two half-density harmonic components
+ almost-saturated one-spoke annulus
+ one central convex exceptional face
+ central face boundary = two D+o(D) unloaded contact paths
+ central face area o(D^2)
+ central face normalized shape -> one diameter segment.
```

This still does not prove Level I. A thin staggered two-row contact corridor can approach the facewise Oler lower area while remaining triangle-free, so no fixed local area gap is asserted.

---

## 1. Dominant-cell and minor-cell perimeter at equality

Assume throughout

```math
Q_B=(2+o(1))D.
\tag{1.1}
```

FS gives one dominant attachment cell `P_i` in each HG semicircle group such that

```math
\operatorname{area}(P_i)
=\left(\frac\pi8+o(1)\right)D^2,
\tag{1.2}
```

```math
P_i/D\to H_i
```

in Hausdorff distance, where `H_1,H_2` are complementary diameter-one semicircles, and

```math
|I_i|=(\Delta/2+o(1))D^2.
\tag{1.3}
```

Convex perimeter continuity gives

```math
\operatorname{per}(P_i)
=\left(1+\frac\pi2+o(1)\right)D.
\tag{1.4}
```

FS also gives total attachment-cell perimeter

```math
P_A:=\sum_r\operatorname{per}(P_r)
=(\pi+2+o(1))D.
\tag{1.5}
```

Therefore all nondominant attachment cells together satisfy

```math
\boxed{
\sum_{r\ne1,2}\operatorname{per}(P_r)=o(D).
}
\tag{1.6}
```

Every attachment point is a vertex of the strictly convex-position loaded set and distinct attachment points are unit-separated, so

```math
|A_r|\le\operatorname{per}(P_r).
\tag{1.7}
```

Hence nondominant components use only `o(D)` loaded attachment vertices in total.

Also every convex body satisfies

```math
2\operatorname{diam}(K)\le\operatorname{per}(K)
```

with the degenerate segment giving equality in the limiting sense. Thus

```math
\max_{r\ne1,2}\operatorname{diam}(P_r)=o(D).
\tag{1.8}
```

Since `I_r subset P_r`, every nondominant harmonic component has Euclidean diameter `o(D)`.

Its attachment vertices lie on the near-circular loaded hull, so a set of boundary points of chord diameter `o(D)` lies in an angular interval of width `o(1)`. Its convex hull, and hence `I_r`, lies within `o(D)` Euclidean distance of the force-hull boundary. Therefore

```math
\boxed{
\bigcup_{r\ne1,2}I_r
\subset
\{x:\operatorname{dist}(x,\partial F)=o(D)\}.
}
\tag{1.9}
```

The `o(D)` here is uniform because the largest nondominant cell perimeter is bounded by the total in (1.6).

---

## 2. The dominant component convex hulls are the same half-disks

Let

```math
K_i:=\operatorname{conv}(I_i).
```

C36 gives `K_i subset P_i`. Conversely every loaded attachment vertex lies at unit distance from a vertex of `I_i`, so

```math
P_i\subset K_i+B(0,1).
\tag{2.1}
```

Thus

```math
d_H(K_i,P_i)\le1.
```

After division by `D`,

```math
\boxed{K_i/D\to H_i}
\tag{2.2}
```

in Hausdorff distance. In particular

```math
\operatorname{per}(K_i)
=\left(1+\frac\pi2+o(1)\right)D.
\tag{2.3}
```

AS proves

```math
\sum_rk_r=(\pi+2+o(1))D.
\tag{2.4}
```

The outer-face walk of `C[I_i]` has length `k_i>=per(K_i)`. Therefore (2.3)--(2.4) and nonnegativity of all other `k_r` imply

```math
\boxed{
k_i=\left(1+\frac\pi2+o(1)\right)D,
\qquad i=1,2,}
\tag{2.5}
```

and

```math
\boxed{
\sum_{r\ne1,2}k_r=o(D).
}
\tag{2.6}
```

So not only attachment-cell perimeter but also actual nondominant component outer-walk length is sublinear.

---

## 3. Dominant loaded attachments occupy the two half-circle sides

AS proves that all but `o(D)` loaded terminals have exactly one unloaded neighbor. By (1.7), only `o(D)` of these neighbors belong to nondominant components. Hence all but `o(D)` loaded terminals attach to `I_1` or `I_2`.

The attachment sets of distinct harmonic components are noncrossing in cyclic loaded order. In particular, after deleting the `o(D)` nondominant/irregular terminals, the attachment sets of `I_1` and `I_2` cannot alternate: an `I_1,I_2,I_1,I_2` cyclic quadruple would give crossing chords and interior intersection of `P_1,P_2`, contradicting C49.

Thus the dominant labels occupy two complementary cyclic blocks up to `o(D)` deleted terminals.

Because `P_i/D->H_i`, the extreme attachments of `I_i` converge to the endpoints of the corresponding semicircle. Perimeter-measure convergence of the near-circular loaded hull and the fact that its side lengths have total excess `o(D)` over their unit lower bound give

```math
\boxed{
M_i=\left(\frac\pi2+o(1)\right)D
}
\tag{3.1}
```

loaded shell edges whose two regular endpoints attach to `I_i`, for each `i=1,2`.

All but `o(D)` of those shell edges are AS-regular interface faces.

---

## 4. Regular annular defect is sublinear

For every AS-regular shell edge of the `I_i` block, the adjacent bounded face consists of

- the loaded shell edge;
- the two unique loaded-to-`I_i` spokes;
- an internal contact path in `I_i` of length `L>=1`.

AS gives

```math
Q_F=L-1.
\tag{4.1}
```

Following these faces in shell order gives edge occurrences on one side of the outer-face walk of `C[I_i]`. Let `L_i^{ann}` be the total length of these internal paths and `Q_i^{ann}` their total defect. Then

```math
L_i^{ann}=M_i+Q_i^{ann}+o(D).
\tag{4.2}
```

Let `u_i^-`, `u_i^+` be interior attachment neighbors within `O(1)` of the two extreme loaded attachments of `I_i`. The latter approach antipodal endpoints of the semicircle, so

```math
|u_i^--u_i^+|=D-o(D).
\tag{4.3}
```

The closed outer walk of `I_i` contains a complementary route from `u_i^+` back to `u_i^-` outside the annular path occurrences. By the triangle inequality that complementary route has length at least

```math
D-o(D).
\tag{4.4}
```

Hence, using (2.5), (3.1), and (4.2),

```math
\begin{aligned}
\left(1+\frac\pi2+o(1)\right)D
=k_i
&\ge L_i^{ann}+D-o(D)\\
&=\left(\frac\pi2+o(1)\right)D+Q_i^{ann}+D-o(D).
\end{aligned}
```

Therefore

```math
\boxed{Q_i^{ann}=o(D),
\qquad i=1,2.}
\tag{4.5}
```

Let `Gamma_i` be the complementary outer-walk route in (4.4). Equality in the same estimate gives

```math
\boxed{|\Gamma_i|=D+o(D).}
\tag{4.6}
```

Since its endpoints have Euclidean separation `D-o(D)`, every point of `Gamma_i` lies within `o(D)` of the straight segment joining its endpoints. One elementary proof is that if a path point has perpendicular distance `h` from that segment, the two subpath lengths are at least the two sides of the broken line through that point; the excess over the chord is at least a positive multiple of `h^2/D` when `h=o(D)` and is a fixed multiple of `D` when `h` is a fixed fraction of `D`. Since the total path excess is `o(D)`, necessarily `h=o(D)` uniformly.

Thus each `Gamma_i` is a `D+o(D)` near-geodesic contact path converging to the common diameter side of its half-disk.

---

## 5. The central strip contains no nondominant graph

By (1.9), every nondominant component lies in an `o(D)` neighborhood of the outer circular boundary. Every loaded terminal lies on that boundary, and every loaded-to-interior contact has unit length, so loaded vertices and their incident spokes also remain in an `o(D)` boundary layer except for edges entering the two dominant components at their near-boundary attachment points.

Fix any `epsilon>0`. For all sufficiently large `D`, the central portion of the common diameter segment at Euclidean distance at least `epsilon D` from its two endpoints is therefore separated from

- every loaded terminal;
- every nondominant component;
- every contact edge incident to either of those sets.

The paths `Gamma_1,Gamma_2` both lie within `o(D)` of that diameter segment and bound their respective dominant components on opposite sides. The open region between their central subpaths contains no contact-graph vertex or edge.

Hence that connected open region belongs to one face of the full plane contact graph. Call it `F_*`. It is bounded because the near-complete loaded shell surrounds both dominant components and the central region.

For fixed `epsilon`, the boundary of `F_*` contains subpaths of each `Gamma_i` whose lengths are at least

```math
(1-O(\epsilon))D-o(D).
```

Let first `D->infinity` and then `epsilon->0`. We obtain

```math
\boxed{k_{F_*}\ge(2-o(1))D.}
\tag{5.1}
```

The face is necessarily exceptional for large `D`.

---

## 6. MF makes the lower bound sharp

MF proves that every macroscopic exceptional bounded face in the full-core near-circle branch satisfies

```math
k_F\le(2+o(1))D.
```

Apply this to `F_*` and combine with (5.1):

```math
\boxed{k_{F_*}=(2+o(1))D.}
```

Therefore

```math
Q_{F_*}=k_{F_*}-4=(2+o(1))D.
```

But the entire loaded-interface defect satisfies (1.1), and `F_*` is a loaded-interface face: its boundary connects to the shell through the two endpoint transition regions, while a bounded face with vertices from two distinct unloaded components cannot close without passing through loaded terminals because there are no contact edges between different `I_r` components.

Thus

```math
Q_B-Q_{F_*}=o(D),
```

proving CF.1-CF.2.

The two long boundary subpaths of `F_*` are precisely `Gamma_1,Gamma_2` up to `o(D)` endpoint pieces. MF therefore gives the same diameter-segment Hausdorff limit for the central face.

---

## 7. What the equality model now says

At the sharp interface coefficient two, every source in the sequence has the following asymptotic decomposition:

1. a near-circular loaded shell with `q=(pi+o(1))D` direct unit contacts;
2. exactly two dominant harmonic components, each with `(Delta/2+o(1))D^2` vertices;
3. each dominant component convex hull tends to a half-disk;
4. each dominant outer walk has length `(1+pi/2+o(1))D`;
5. regular shell-annular faces have total defect `o(D)`;
6. each dominant component has one inward outer path of length `D+o(D)`;
7. all nondominant components live in an `o(D)` outer boundary layer and have total outer-walk length `o(D)`;
8. one central bounded exceptional face contains both long inward paths and carries `2D-o(D)` interface defect.

This is substantially stronger than the earlier statement `Q_B>=2D-o(D)`: equality is now reduced to one explicit doubled-corridor geometry.

---

## 8. Why this is not yet a contradiction

C51 gives strict convexity and unit edges on `F_*`. Facewise Oler therefore implies a boundary-order area floor of order `(sqrt(3)/2)D` when `k_{F_*}~2D`.

That scale alone does not contradict the known global area allowance. More importantly, a staggered pair of nearly triangular unit rows can approach the Oler coefficient while keeping all forbidden cross distances strictly above one. Thus no fixed local face-area gap is available from triangle-freeness alone.

The existing near-diameter-path report also contains a local equilibrium regression showing that a nearly straight unloaded path may be balanced by arbitrarily small one-sided transverse stress. Therefore the face-side emptiness condition cannot simply be converted into a local zero-stress contradiction.

Any closure must still use exact global attainment, simultaneous density of the two half-disks, or a finite boundary-layer capacity theorem.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| nondominant attachment perimeter/outer-walk is `o(D)` | proved | equality in FS and AS plus dominant half-disk perimeter |
| nondominant components lie in outer `o(D)` boundary layer | proved | `diam(P_r)=o(D)` and `I_r subset P_r` |
| each dominant outer walk splits into `pi D/2+o(D)` annular side and `D+o(D)` inward path | proved | shell count + chord lower bound + exact outer-walk equality |
| regular annular defect is `o(D)` | proved | no linear perimeter room remains |
| central graph-free region belongs to one bounded face | proved | no nondominant graph in central bulk; dominant paths are outer boundaries |
| central face degree/defect `2D+o(D)` | proved | lower boundary inclusion + MF upper theorem |
| central face alone closes Level I | not proved | boundary-order thin-strip regression remains |

---

## 10. Next target

The minimum-interface equality branch has become a finite-width separator problem.

The central face `F_*` is a strictly convex unit polygon with

```math
k_{F_*}=2D+o(D),
```

whose boundary is two `D+o(D)` unloaded contact paths belonging to distinct positive-density harmonic components. The two component interiors lie on opposite sides and each fills an asymptotic half-disk at optimal leading density.

The next useful theorem is a **two-sided boundary-layer capacity inequality**: quantify the number of unit-separated points that two near-optimal half-disk packings lose when they are separated by a convex empty corridor bounded by two near-geodesic unit chains. A boundary-order loss exceeding the known global finite-packing allowance would close the equality branch. A construction matching that allowance would instead identify a serious disproof candidate.
