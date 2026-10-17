> Generated reading edition · [exact source](../../../docs/reports/target_c_full_source_delaunay_strain_and_branching_2026-10-08.md) · source SHA-256 `22e830500cf097702c66ff9d9ed4b5b2d48ef288e899eb12de803dd5d546d177`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "10b96629ea26d8b37576a943f4edd442b89380c4", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "4a2505e7adfef864f0fd572aa4ff3366b734bf55", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_full_source_delaunay_strain_and_branching_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "5d3308597879966a95a03bc58ff8c3dea92827c5a9efe93ade5d1f3a0c25b1ae"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: full-source Delaunay defect and near-unit branching budget

Date: 2026-10-08. Research start: `871c56111c479d536b17a51d21fcd04fa86d8931`.
Fixed main: `163010ca099dd6e21505ae574484fb8006a5a5de`.
State: `2026-10-08.audit.157`, including Audit.161.
Classification: **proved candidates awaiting independent audit**.
Registry status: unreviewed; canonical=false. C-II and Level I remain open.

The intended bridge is

`contact-minimal full source -> full-source Delaunay strain budget
-> located obstruction/payment for a finite move -> Level I contradiction`.

This report proves the first implication. It also proves a local
two-blocker consequence. The located payment and compatible
finite move are not supplied. All source labels, including
contact isolates, remain in the triangulation.

## 1. Hypotheses and notation

Let `A` be the canonical triangle-free global minimizer, chosen
contact-minimal and then diameter-pair-minimal. Set

```math
n=|A|,\quad D=\operatorname{diam}A,\quad K=\operatorname{conv}A,
\quad a=\sqrt3/4,\quad a_0=2a,\quad
g_A=n-1-\frac{\pi}{2\sqrt3}D^2>0,
```
```math
\delta_K=\frac{\pi D^2}{4}-\operatorname{area}K,
\qquad \kappa=\frac{2-\sqrt3}{4}.
```

The global population comparison is
[canonical full-source geometry](../targets/target-c/58-full-source-geometry-audit.md).
The [previous candidate](target_c_full_source_voronoi_defect_spacing_debit_2026-10-08.md)
proves that closed unit disks about all source labels cover `K`.
Its short proof is source-preserving: replace any nonisolated
contact vertex by a strictly uncovered hull point; no new unit
pair occurs, no upper bound increases, and the contact count drops.

Let `J` consist of labels whose hull-clipped Voronoi cells touch
`partial K`, and write `m=|J|`. Every label outside `J` has its
full bounded Voronoi cell inside `K` and inside its radius-one
ball. The previous candidate proves

```math
m\le (8/\pi)\operatorname{per}K+1\le8D+1. \tag{1}
```

Take any finite Delaunay triangulation of `A`, choosing diagonals
at cocircular degeneracies. Let `b` count **all** labels on the
hull boundary, including labels collinear along a hull side.
Thus `b<=m` and the triangulation has `2n-b-2` faces.
No auxiliary packing points are introduced.

## 2. Only boundary-label triangles can have large circumradius

Call a face `bad-boundary` if all its vertices lie in `J`.
Write `f_B` for their number and `A_B` for their total area.
Every other face belongs to `G`.

For `T in G`, its circumcenter belongs to the full bounded
Voronoi cell of at least one vertex outside `J`. Consequently

```math
R_T\le1. \tag{2}
```

This does not hold for every boundary triangle. The checker
includes a hull-covered three-point thin triangle with
circumradius greater than one and area less than `a`.
Discarding this distinction would invalidate the surplus ledger.

Complete the planar subgraph induced by `J` to a triangulation
on `J` in `K`, preserving its edges. Every original all-`J`
triangular face remains a face. Euler gives

```math
f_B\le2m-b-2. \tag{3}
```

Every Delaunay edge joining `J` to its complement has length at
most two, by its incident circumcenter in a bounded complement
cell. The unit-separated neighbors within distance two of a
fixed site number at most 24: their radius-half disks, together
with the central disk, lie inside the radius-`5/2` disk.
Thus the number `E_{JI}` of these mixed edges is at most `24m`.

Every mixed triangular face has exactly two mixed edges, and
every mixed edge is internal and has two mixed incident faces.
The number of mixed faces therefore equals `E_{JI}`. In
particular, the number of faces touching `J` is at most
`26m-b-2`, and

```math
W:=J\cup N_{\rm Del}(J),\qquad |W|\le25m. \tag{4}
```

This boundary removal is analytical accounting. No source label
is deleted from a configuration.

## 3. Exact full-source triangle ledger

The local triangle calculation reconstructed in
[Audit.161](../audits/target_c_one_deficit_delaunay_defect_budget_independent_audit_2026-10-08.md)
uses only separation one and circumradius at most one.
It gives `area(T)>=a` for every `T in G`.
Explicitly, with circumradius `R`, every angle is at least
`ell=arcsin(1/(2R))`. Concavity of `log sin` at fixed `R`
minimizes area when two angles are `ell`:

```math
\operatorname{area}T\ge
\frac{\sqrt{4R^2-1}}{4R^2}\ge a,
\qquad 1/\sqrt3\le R\le1.
```

Set

```math
\sigma_T=\operatorname{area}T-a\quad(T\in G),\qquad
\Sigma=\sum_{T\in G}\sigma_T\ge0.
```

Counting every face and every original label yields the identity

```math
\boxed{
\Sigma+A_B+\delta_K+a_0g_A=a(b+f_B).
} \tag{5}
```

Indeed the triangle-area partition gives
`Sigma=area K-A_B-a(2n-b-2-f_B)`.
Using (3),

```math
\boxed{
\Sigma+A_B+\delta_K+a_0g_A\le a_0(m-1),
\qquad \Sigma<4\sqrt3D.
} \tag{6}
```

Unlike the unit-wall theorem, (5) assumes no unit hull sides
and no maximal auxiliary completion. It uses the actual
full-source hull covering and retains an exact boundary-area term.

## 4. Right/obtuse faces and the exceptional labels

Let `H_0` count right/obtuse faces with no vertex in `J`.
For such a face, its longest edge is internal. Its Delaunay
neighbor across that edge belongs to `G`, since both edge
endpoints lie outside `J`. Both circumradii are at most one.

The same local paired calculation as Audit.161 therefore applies.
If the largest angle is `alpha>=pi/2` and the neighboring
opposite angle is `beta<=pi-alpha`, the two excesses pay

```math
\sigma_T+\sigma_{T'}\ge
\frac12\sin\alpha-a(1+\cos\alpha)\ge\kappa.
```

Here `alpha<=2pi/3` follows from separation and `R_T<=1`;
the neighbor's other angles are at least `pi/6`.
Each excess is charged at most four times. Hence

```math
H_0\le4\Sigma/\kappa. \tag{7}
```

Mark `W`, all vertices incident to a face in `G` with
`sigma_T>=1/100`, and all vertices incident to the `H_0` faces.
Outside these marks, every incident face is acute with small
excess. The standalone acute-triangle estimates proved in
Audit.161 give

```math
1\le |e|<11/10,\qquad
\max_e(|e|-1)\le5\sigma_T,\qquad
|\angle-\pi/3|\le50\sigma_T. \tag{8}
```

For clarity, this is a new full-source extension of its local
proof, not an application of the promoted fixed-unit-wall claim
outside its scope. The acute longest-side lower bound is
`L sqrt(4-L^2)/4`; above `L=sqrt(2)` area is at least `1/2`.
The derivative exceeds `1/5` on `[1,11/10]`. The cosine-law
derivative bound on `[1,11/10]^3` gives the angle estimate.

A remaining interior vertex of valence `q!=6` has total incident
angle error at least `pi/3`, so its incident excess is greater
than `1/50`. Summing charges every face at most three times.
There are fewer than `150Sigma` such vertices.

The exceptional set `E` can therefore be chosen with

```math
\boxed{
|E|\le25m+(450+12/\kappa)\Sigma.
} \tag{9}
```

Every label outside `E` has Delaunay valence six and satisfies
(8) on all incident faces. All these labels are actual source
points; they may be contact-isolated.

## 5. Total strain and six near neighbors

For all acute small-excess faces in `G`, (8) implies

```math
\sum_T\sum_{e\subset T}(|e|-1)\le15\Sigma,\qquad
\sum_T\sum_{\theta\subset T}|\theta-\pi/3|\le150\Sigma. \tag{10}
```

These are total budgets, not budgets supported only on `E`.
Diffuse strain in quadratically many faces is allowed.

For `epsilon>0`, mark endpoints of an edge in such a face with
length greater than `1+epsilon`. At most `30Sigma/epsilon`
additional labels are marked. Consequently all but

```math
\boxed{
25m+(450+12/\kappa)\Sigma+30\Sigma/\epsilon
} \tag{11}
```

source labels have six distinct Delaunay neighbors within
`1+epsilon`.

For `0<epsilon<=1/10` there are at most six source neighbors in
that radius. Indeed, for two neighbor radii in `[1,11/10]`,
the cosine law gives angular separation at least
`2arcsin(5/11)>2pi/7`. The cosine expression increases in
each radius on this interval. The last inequality follows from
`arcsin t>=t` and `pi<22/7`. Seven neighbors would exceed
total angle `2pi`. Thus every unmarked site has exactly six near
neighbors, and they are precisely its Delaunay neighbors.

For `epsilon(D)->0` with `D epsilon(D)->infinity`,
the exceptions in (11) are `o(D^2)`. This strengthens the
previous empty-neighborhood count to a full six-neighbor statement.
It still supplies no common global orientation.

## 6. Two bracketing lower blockers for an arbitrary small translation

Let `0<delta<=1/10`. A site outside the exceptions in (11) for
`epsilon=delta/20` has six neighbors at distances at most
`1+delta/20`.

Their consecutive angular gaps are at least
`pi/3-2epsilon`. This follows by differentiating
`2arcsin(1/(2(1+epsilon)))`; the derivative magnitude is at most
two. Thus every gap is at most `pi/3+10epsilon`.

For any unit direction `u`, choose the two consecutive neighbor
vectors `r_i=x-y_i` bracketing `u`. Each makes angle at most
`pi/3+10epsilon` with `u`. Since `|r_i|>=1`,

```math
u\cdot r_i\ge\cos(\pi/3+10\epsilon)
\ge1/2-10\epsilon=1/2-\delta/2.
```

Translating `x` to `x-delta u` while fixing either neighbor gives

```math
|r_i-\delta u|^2-1
\le(1+\delta/20)^2-1
-2\delta(1/2-\delta/2)+\delta^2
```
```math
=-(9/10)\delta+(801/400)\delta^2<0.
\tag{12}
```

Therefore both neighbors are actual strict lower blockers for
that finite single-site translation. Their vectors bracket
the translation axis. This is an all-direction local statement.

It does not make a collection of translations compatible.
A closed set must include these blockers, but exceptional
seams can stop or redirect propagation, and different paths
can merge. Neither disjointness nor an integer payment follows.

## 7. A located front for a lower-closed set

For a fixed translation `-delta u`, call `S subset A` lower-closed
when every strict lower blocker of every label in `S` also lies
in `S`. Use all original labels in this relation. Let `E_delta`
be the exceptions from (11) with `epsilon=delta/20`.

If `x in S minus E_delta` and `nu!=0` supports `conv S` at `x`,
then

```math
\boxed{\nu\cdot u>0.} \tag{13}
```

To prove this, choose two strictly bracketing neighbor rays from
Section 6. If `u` coincides with one ray, choose its immediate
neighbors on both sides instead. Their angles with `u` remain
at most `pi/3+10epsilon<pi/2`, so (12) still makes them strict
lower blockers. Their independent vectors `r_1,r_2` have
`u=c_1r_1+c_2r_2` with `c_1,c_2>0`.

Lower closure puts both `y_i=x-r_i` in `S`. The supporting
inequalities give `nu dot r_i>=0`. Thus `nu dot u>=0`; equality
would make both independent `r_i` orthogonal to `nu`, forcing
`nu=0`. This proves (13).

In particular, all support labels on the forward face with
normal `-u`, and all transverse support labels, lie in `E_delta`.
This locates a front in the actual source rather than in an
auxiliary lattice.

Combining this with the
[half-depth closure candidate](target_c_half_depth_fan_forest_and_weight_budget_2026-10-08.md)
puts an exceptional support label at the deepest end of every
canonical root closure that must reach depth `D/2-o(D)`.
A bound on their total number does not bound root multiplicity:
many closures may share one front, and the exceptions can form
a boundary-order seam. No payment or compatible move follows.

## 8. Verification and scope

The [exact checker](../../../research/verify_target_c_full_source_delaunay_budget_2026_10_08.py)
uses six hull-covered finite oblique grids in Q(sqrt(3)).
It reconstructs the actual source Delaunay triangulation,
checks empty circumcircles against every source label,
reconstructs clipped Voronoi cells and `J`, checks the mixed-edge
and boundary-face counts, every full-source pair, the area ledger,
valences and local finite translation blockers.
It also computes full lower-blocker closures and checks their
actual convex support fronts against the exceptional labels.
Every grid has an explicit same-cardinality square competitor
with strictly smaller diameter.

The enlarged grids have no unit contacts: their entire source
is contact-isolated, yet their bulk has six near neighbors.
Thus the conclusions do not reclassify isolates as stressed
or contradict the separate inactive-chamber branch.

A thin rational triangle verifies that the bad-boundary faces
cannot be assigned nonnegative triangle excess. Its source is
nonglobal, certified by the three-point unit equilateral competitor.

The final exact run passed: 464 Delaunay faces and 29,392
empty-circumcircle comparisons; 9,432 complete source pairs and
9,432 complete square-competitor pairs; 310 clipped cells and
1,704 covering vertices; 228 mixed edges and 228 mixed faces;
70 bulk six-neighbor labels; 770 translation-direction checks
and 4,620 moving-neighbor pair checks. Three translation axes
also gave 56,592 complete lower-arrow pair checks, 54 closed
sets and 366 exceptional-front support checks. The thin triangle
adds three source pairs, three strict-competitor pairs, three
cells and eleven covering vertices. Python compilation passed.

The universal inequalities are analytic candidates, not proved
by these samples. This report establishes neither a globally
optimal fixture nor a common phase, an exact lattice vacancy,
a source-preserving packet, or a compatible strict-diameter move.
C-II and Level I remain open.
