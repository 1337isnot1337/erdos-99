<!-- theorem-state: {"artifact_id":"ART-73BAC479B764","canonical":true,"claim_ids":["C-TRIANGULAR-TWO-BOUNDARY-HOLE-POPULATION","C-TRIANGULAR-TWO-BOUNDARY-HOLE-STRICT-REFILL"],"claim_statuses":{"C-TRIANGULAR-TWO-BOUNDARY-HOLE-POPULATION":"canonical","C-TRIANGULAR-TWO-BOUNDARY-HOLE-STRICT-REFILL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: triangular two-boundary-hole refill

**Date:** 2026-10-09  
**Audit base:** `origin/main=ba7e9657c93e603f11b8af42557ce3ea20bf076b`, state `2026-10-09.audit.186`  
**Frozen source:** `origin/research/sol/target-c-level1-gpt61-2026-10-04` at `9875cd6a77939bb6347353fc798ab8f9ab03ec3e`  
**Classification:** independent proof reconstruction; **PASS — promote two exact claims**.  
**Target effect:** no route-map change; C-II and Level I remain open.

## Source and computational evidence

The source report is [`target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md`](../reports/target_c_boundary_vacancy_funded_collective_refill_2026-10-05.md), SHA-256 `a765e63ecf244e068558168c746b4253aa174e03ecccd678d4e4754f36182ea7`. Its exact finite verifier is [`verify_target_c_boundary_vacancy_funded_collective_refill_2026_10_05.py`](../../research/verify_target_c_boundary_vacancy_funded_collective_refill_2026_10_05.py), SHA-256 `df10fbcb19ebd1132407723dc901e58cdc20877c5fb4bc95e01e36af876e7c11`. It imports three helpers from the same frozen branch (hashes `53660a5a8d61c512065d1b188a3e6259a03cc4cf59f3510090c2c3d10b282746`, `959129b75bca577c6820ec00e96af8e28ac239c1ef6e4c3a07c450c6bc6eff4c`, and `a7dde4b19c70f31266d3e17c781d2523238e25d4e1abc04b251d8d5c7ec1249a`). I inspected and reran it at that snapshot. It passes 65,754 sequential pair checks, 382 strict final interior-pair checks, 9,802 complete guarded source-pair checks, and records 62 lost contacts on four frames `(3,3)`, `(3,4)`, `(4,3)`, `(4,4)`. All arithmetic is exact rational or in `Q(sqrt(3))`.

This verifier checks only those finite fixtures and its encoded guarded replacements. It does not prove the all-`m,n` release, near-wall homotopy, crossing lemma, or global-minimum consequence. Those claims below rest on the independent analytic reconstruction. The source verifier is not registered as a canonical certificate because it depends on unpromoted helper scripts and adds no proof of the general statements.

## Exact claims promoted

Let `m,n >= 3`, `u=(1,0)`, `v=(1/2,sqrt(3)/2)`, and `p_(i,j)=i*u+j*v` for `0<=i<=m`, `0<=j<=n`. Let `W0` be the simple boundary cycle of this triangular parallelogram. Put `K=(m-1)(n-1)`.

**`C-TRIANGULAR-TWO-BOUNDARY-HOLE-STRICT-REFILL`.** Delete and omit the two adjacent boundary labels `p_(1,0), p_(2,0)`. Keep every other boundary label fixed, and move all `K` interior labels. There is a finite sequential continuous motion that preserves all pairwise distances at least one throughout, keeps the moving labels inside the reference parallelogram, moves each by less than `1/100`, and ends with every pair involving a moved label strictly longer than one. No claim is made about the two omitted labels' former coordinates.

**`C-TRIANGULAR-TWO-BOUNDARY-HOLE-POPULATION`.** For each fixed `m,n>=3`, there is an `eta_(m,n)>0` such that if a triangle-free contact-minimal global minimum-diameter source contains a simple actual unit-contact cycle `W` with `2(m+n)` vertices in the order of `W0`, each within `eta_(m,n)` of its reference vertex after one Euclidean isometry, then

`|A intersect int(W)| >= (m-1)(n-1)-1`.

The count includes every source point strictly inside the cycle, including contact isolates. Contact-minimality is within the triangle-free global-minimizer class. The result is fixed-frame only: `eta_(m,n)` can depend on `m,n`, and no wall-extraction theorem is supplied.

## Independent reconstruction

### 1. All-interior release on the exact frame

The six contact directions in the triangular lattice are `±u, ±v, ±(u-v)`. When a mover has two adjacent contact neighbors already absent or released, call their unit directions `r1,r2` and move along `h=r1+r2`. Then `|h|^2=3`, and each remaining lattice contact direction `r` satisfies `h dot r<=0`. Along `p(t)=p+t h`, its squared distance to that neighbor is

`|t h-r|^2 = 1 - 2t(h dot r) + 3t^2 > 1` for every `t>0`.

Release in this order: for `j=1,...,n-1`, first `(1,j)` using absent/released `(1,j-1),(2,j-1)`, then `(2,j)` using `(1,j),(2,j-1)`. Next, for `i=3,...,m-1`, release `(i,1)` using `(i-1,1),(i-1,2)`, then `(i,j)` for `j=2,...,n-1` using `(i-1,j),(i,j-1)`. At each step the two indicated directions are adjacent, and the order removes every unit contact incident to the current mover. All other pairs have positive slack at that finite step; choose a sufficiently small positive amplitude to preserve every such inequality through the segment. There are finitely many labels and pairs, so amplitudes can be chosen successively, also below `1/(100 sqrt(3))`. This proves the claimed finite motion and displacement bound. Every reference interior label is at least `sqrt(3)/2` from the reference boundary, so these displacements keep it inside the parallelogram.

This proof does not require a positive lower bound on the amplitudes uniform in frame size. In particular, the sequence of amplitudes may shrink with `m,n`.

### 2. Full-source shielding for a nearby actual wall

Choose one strict endpoint realization of the finite release and choose `eta_(m,n)<=1/20` small enough that all endpoint refill points remain strictly separated from the retained actual wall whenever its vertices are within `eta_(m,n)` of `W0`. Since the reference interior sites have distance at least `sqrt(3)/2` from the reference boundary and the moved sites travel less than `1/100`, linear interpolation of the ordered wall vertices and the short target motions avoid the boundary. Winding number therefore keeps every target inside `W` and hence inside `int(conv(A))`.

For each target's original reference site `q` and every reference wall vertex `w0`, `|q-w0|>=1`. The corresponding actual wall vertex `w` has `|q-w|>=1-eta_(m,n)>=19/20`. Every retained exterior source point `y` is at least one from every actual wall vertex, including the two deleted vertices. The segment from `q` to `y` exits the simple cycle through a unit wall edge. For an interior edge crossing, apply the canonical `C-UNIT-SIDE-CROSSING-SEPARATION` theorem with `t=19/20` to get

`|q-y| >= sqrt(4*(19/20)^2-1) = sqrt(261)/10 > 151/100`.

At a vertex crossing, perturb the exterior endpoint through exterior points with guard distances tending to one and pass to the limit; a segment passing through the crossing vertex directly also has the stronger `2t` bound. Moving the target by less than `1/100` leaves it more than `3/2` from `y`. This applies to every exterior source point, including contact isolates, and does not use a contact-core or stress-coordinate restriction. The deleted boundary coordinates are not treated as points of the replacement.

### 3. Contradiction when the population is at most `K-2`

Write `z=|A intersect int(W)|`. If `z<=K-2`, delete all `z` interior source points and the two adjacent wall vertices. Insert `z+2<=K` endpoint targets, assigning the deleted labels bijectively to them. The refill proof gives strict separation from each other and all retained wall vertices; the crossing bound gives strict separation from all retained exterior points. All source labels are accounted for, and retained old pairs are unchanged.

Every inserted point lies in `int(W) subset int(conv(A))`. The convex hull of a finite set has the same diameter as the set, namely the old `D`; strict convexity of the Euclidean disk implies that an interior hull point is strictly less than `D` from every point of `conv(A)`. Thus every pair involving an inserted point is strictly shorter than `D`. The replacement diameter is at most `D`. If it is smaller, global minimum-diameter optimality is contradicted. If it equals `D`, no new unit contacts exist and retained old contacts are unchanged, while deleting the adjacent cycle vertices removes at least three distinct cycle contacts. The replacement remains triangle-free and has fewer contacts, contradicting contact-minimality. Therefore `z>=K-1`.

## Dependencies, limits, and frontier

The population theorem depends on the new exact-frame refill and canonical `C-UNIT-SIDE-CROSSING-SEPARATION`; the finite refill is proved directly. The two claims complement the canonical one-pin oblique refill: the triangular one-pin displacement regression blocks the one-hole motion, while this theorem uses two adjacent holes and only obtains the `K-1` population bound.

The source report's stronger activation narrative is not promoted. The result does not produce a near-triangular wall in an arbitrary source, a tolerance uniform as `m,n` grow, `z>=K`, spare capacity at the fixed wall, a contact activation, or a diameter decrease for an actual canonical C-II source without the stated wall and population hypotheses. No route is eliminated, and the active C-II finite-move/payment obligation is unchanged. Level I remains open.
