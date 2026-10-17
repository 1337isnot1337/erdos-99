> Generated reading edition · [exact source](../../../docs/reports/target_c_fan_flip_isolate_escape_2026-10-02.md) · source SHA-256 `aa64b1299a7e4f1bb4fc4a5e3c2f882e94272e6ba971d0666ff789ce92dc0d13`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CD1DD48A2F24","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — finite fan flips force core attachment or macroscopic isolate escape

**Preservation and audit (2026-10-15):** restored from original dirty-worktree12
and its hash-verified private archive. The [full AI audit](../audits/original12_fan_flip_archive_audit_2026-10-15.md)
checks FF.1–FF.3, FE and all finite fixtures. These remain noncanonical candidates
or regressions, requiring independent human mathematical review. The current
state is `2026-10-10.audit.234`; Level I/C-II remain open. The verified original
head replaces the archived nonexistent full identifier. The checker refuses
optimized Python and now verifies12 complete strict competitors for the finite
nonglobal fixtures; this supplies no global-minimizer closure.

```text
finite inward fan flip + simultaneous isolated-component translation
 -> source-preserving reduction of actual diameter-pair count
 -> canonical contradiction unless a 1/D-near-contact chain reaches the
    positive contact core or reaches a 1/D-near-diameter blocker at depth Theta(D).
```

**Date:** 2026-10-02
**Starting HEAD:** `75aac1464f80ca91256e96dc70ca0c865e0b3b0e` (verified from the unique
short identifier and the original worktree metadata; archived full-ID typo corrected)
**State version:** `2026-09-14.audit.51`
**Branch:** `swarm/sol/fan-geometry-20261002`
**Assigned mission:** actual Euclidean leaf-fan / diameter ball-hull geometry.
**Classification:** proved candidates awaiting independent audit and promotion;
the exact sources below are regressions. Artifact lifecycle: unreviewed.
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`.
**Level I / C-II:** STILL OPEN / OPEN.
**External literature:** none imported.

## 1. Authority, dependencies, and source scope

The state lock and manifest leave C-II and Level I open. This report changes no
canonical theorem state, route, or prompt.

The geometric results below concern an arbitrary finite unit-separated source
`A` of diameter `D>=4`. A fan is an ordered sequence of distinct actual source
points `p_0,...,p_g` with a source carrier `a`, satisfying

```math
|p_i-a|=D,\qquad |p_{i+1}-p_i|=1.
\tag{1}
```

Its order agrees with angular order on one arc of width at most `pi/3` about
`a`. This is the source geometry of the same-carrier fan branch. No source
point, including any contact-isolated point, is deleted from a diameter test.

The finite-competitor application additionally uses the canonical
contact-minimal, then diameter-pair-minimal representative, with `C=C_*` and
`H=H_*`. Its inputs are the normal form and full support in
[`56-ci-restored-frontier.md`](../targets/target-c/56-ci-restored-frontier.md),
the scoped nonisolated-core conclusions of
[`57-zr-zf-rigidity-audit.md`](../targets/target-c/57-zr-zf-rigidity-audit.md),
and the canonical force-hull support theorem in
[`01-force-hull-and-shear.md`](../targets/target-c/01-force-hull-and-shear.md).
In particular every actual diameter endpoint belongs to the positive contact
core in this normal form; a contact-isolated source point has no actual
diameter edge. No ZR/ZF rank assertion is extended to isolated coordinates.

The existence and population of long fans remain conditional on the
unpromoted reductions
[`target_c_leaf_fan_outerwalk_fork_2026-10-02.md`](../../research/target_c_leaf_fan_outerwalk_fork_2026-10-02.md)
and
[`target_c_leaf_fan_inward_spoke_kkt_fork_2026-10-02.md`](../../research/target_c_leaf_fan_inward_spoke_kkt_fork_2026-10-02.md).
The present statements do not need their counting or multiplier estimates:
they apply directly whenever an actual source fan satisfying (1) is supplied.

The arbitrary-source geometric proofs use only Euclidean distance identities
and convexity. Neither full-source roundness, a packing-density estimate,
an unpromoted atlas, nor any uniform KKT multiplier lower bound is assumed.

## 2. Exact inward flip and removal of every diameter at that leaf

Put

```math
\epsilon={1\over2D},\qquad \tau=\sqrt{1-\epsilon^2},\qquad
u_i={p_i-a\over D},\qquad \delta={1\over D}.
```

For an internal index `i`, choose the unit tangent `t_i` so that

```math
p_i-p_{i-1}=\epsilon u_i+\tau t_i,
\qquad p_i-p_{i+1}=\epsilon u_i-\tau t_i.
\tag{2}
```

Define the **finite flipped position**

```math
p_i^\flat=p_i-\delta u_i=p_{i-1}+p_{i+1}-p_i.
\tag{3}
```

**Theorem FF.1 (proved candidate).** The replacement (3) preserves both
adjacent unit contacts. It satisfies

```math
|p_i^\flat-x|<D\qquad(x\in A).
\tag{4}
```

**Proof.** Subtracting `delta u_i=2 epsilon u_i` from both vectors in (2)
reverses their radial component, so their lengths remain one.

The midpoint of the two adjacent fan vertices is
`a+(D-epsilon)u_i`. For `D>1`,

```math
p_i^\flat
=\eta a+{1-\eta\over2}(p_{i-1}+p_{i+1}),\qquad
\eta={\epsilon\over D-\epsilon}\in(0,1).
\tag{5}
```

Thus the flipped point is a convex combination with strictly positive
coefficients of three distinct noncollinear actual source points. For any
fixed `x in A`, all three distances to `x` are at most `D`. The weighted
squared-norm identity subtracts a strictly positive variance from the
weighted average of these three squared distances; hence (4) is strict.
This is a finite replacement, with all source pairs tested. It is not an
integration of a first variation. QED.

If the leaf has exactly the two contacts in (2) and the closed unit disk
about `p_i^flat` contains no other retained source point besides its two
preserved neighbors (the old label `p_i` is replaced), its replacement preserves
the full contact count and decreases the actual diameter-pair count. It
therefore contradicts canonical secondary diameter-pair minimality. If
the entire diameter drops below `D`, primary global minimality already
gives the contradiction. Thus every canonical degree-two fan leaf forces
a source point other than `p_i,p_{i-1},p_{i+1}` with

```math
|z-p_i^\flat|\le1,
\qquad 1<|z-p_i|\le1+\delta.
\tag{6}
```

The non-strict inequality at the new position is deliberate: creation of
an extra unit contact can increase the primary contact count, so a final
equality cannot be discarded by secondary minimality alone.

## 3. Every additional blocker is unloaded and lies inside a source triangle

**Theorem FF.2 (proved candidate).** Suppose `z in A` is distinct from
`p_i,p_{i-1},p_{i+1}` and satisfies `|z-p_i^flat|<=1`. For `D>=4`,

```math
z\in\operatorname{int}\operatorname{conv}\{a,p_{i-1},p_{i+1}\},
\qquad |z-x|<D\quad(x\in A).
\tag{7}
```

In particular `z` is never an actual diameter endpoint. This conclusion
holds for inactive blockers and for actual third-contact neighbors.

**Proof.** Write `v=p_i-z=r u_i+s t_i`. Unit separation and the new-disk
condition imply

```math
1\le |v|\le1+\delta\le5/4.
\tag{8}
```

The source pair `az` has distance at most `D`, so

```math
r\ge\epsilon |v|^2\ge\epsilon.
\tag{9}
```

Equality `r=epsilon` in (9) forces `|v|=1` and
`v=epsilon u_i +/- tau t_i`, making `z` one of the excluded adjacent
vertices. Thus `r>epsilon`.

Separation from both adjacent fan vertices and the new-disk condition give

```math
2\tau |s|\le |v|^2-2\epsilon r,
\qquad |v|^2\le1+4\epsilon r-4\epsilon^2.
```

Because `r<=1+delta`, these imply

```math
|s|\le{1+\delta\over2\tau}\le {40\over63}.
\tag{10}
```

Here `epsilon<=1/8` and `tau>=63/64` were used. The triangle in (7) has
vertices `0,(D-epsilon)u_i +/- tau t_i` after subtracting `a`. At radial
coordinate `D-r`, its open transverse width is

```math
\tau{D-r\over D-\epsilon}
\ge {63\over64}{D-5/4\over D}
\ge {693\over1024}>{40\over63}.
\tag{11}
```

Also `0<D-r<D-epsilon`. Equations (10)--(11) put `z` strictly inside
the triangle. The positive convex-combination squared-norm argument of
FF.1 proves every distance in (7) is strict. QED.

This is stronger than a constant inward-depth bound alone. No near-disk
full-core hypothesis or loaded-loaded chord elimination is needed to
prove that these witnesses are unloaded.

## 4. Blocker multiplicity and exact near-triangle alternatives

**Theorem FF.3 (proved candidate).** One source point can block at most
two internal flips of the same ordered fan. If it blocks two, their
indices are consecutive. Hence `N` internal canonical degree-two leaves
force at least `ceil(N/2)` distinct unloaded inactive blockers satisfying
(6). The same multiplicity statement holds when actual third-contact
neighbors are included as blockers.

**Proof.** Put `x=asin(1/(2D))` and `R=D-1/D`. The flipped positions lie
on the radius-`R` circle about `a`, with angular step `2x`. If indices
differ by at least three, monotonicity of sine on the fan arc gives

```math
|p_i^\flat-p_j^\flat|
\ge (1-D^{-2})(3-D^{-2})>2\quad(D\ge4).
\tag{12}
```

They cannot share a radius-one blocker.

For indices `i,i+2`, let `m` be the midpoint of their flipped positions.
The intersection of their two closed unit disks is contained, by the
parallelogram identity, in the disk about `m` of radius

```math
b_D={3-D^{-2}\over2D}.
\tag{13}
```

Indeed their half-separation is `tau(1-D^{-2})`, and
`1-tau^2(1-D^{-2})^2=b_D^2`. The original middle fan point `p_{i+1}`
is at distance exactly `b_D` from `m`. Any common blocker would therefore
have distance at most

```math
2b_D={3\over D}-{1\over D^3}<1
\tag{14}
```

from that unchanged source point, violating unit separation. QED.

If a point blocks two consecutive leaves, it is within `5/D` of the
inward unit-equilateral completion of their unit base. For completeness,
write their midpoint as `m`, their unit-base tangent as `t`, and their
outward radial normal as `n`. Write `z=m+s t-y n`. Both original
endpoint distances lie in `[1,1+delta]`, so

```math
|s|\le\delta+\delta^2/2,
\qquad
3/4-s^2\le y^2\le3/4+2\delta+\delta^2-s^2.
\tag{15}
```

The outward choice `y<0` is impossible: (15) gives `|y|>4/5`, while
`|m-a|=D tau` and `D-D tau<1/16` for `D>=4`, contradicting
`|z-a|<=D`. Dividing the squared-height differences by the sum of the
heights gives `|y-sqrt(3)/2|<=3delta`. Together with (15),

```math
|z-(m-(\sqrt3/2)n)|<5/D.
\tag{16}
```

This is a near-triangle statement only; no exact unit triangle is inferred.

## 5. Simultaneous isolated-component translation: a macroscopic escape theorem

FF.1 permits a precise repair when the blockers are isolated. It does not
justify merely counting them as immovable obstructions.

Fix one canonical degree-two leaf `p=p_i`, put `u=u_i` and
`w=-delta u`, and define its additional blocker set

```math
Z=\{z\in A\setminus\{p,p_{i-1},p_{i+1}\}:|z-(p+w)|\le1\}.
\tag{17}
```

On `A\setminus\{p\}`, form the **actual-source augmented near-contact
graph** whose edges satisfy `|x-y|<=1+delta`. Let `S` be the union of
all graph components meeting `Z`. This graph includes all source points;
in particular it is not restricted to the contact core.

**Theorem FE (proved candidate, conditional only on an actual fan).**
`Z` is nonempty. Either:

1. some component meeting `Z` contains a nonisolated positive-contact-core
   point; or
2. all of `S` consists of contact-isolated points, and there are `z in S`
   and `x in A\setminus(S\cup\{p\})` with

   
   ```math
   D-\delta\le|z-x|<D,\qquad |z+w-x|\ge D,
   \qquad (z-a)\cdot u\le {\sqrt3\over2}D+\delta.
   \tag{18}
   ```


   The component of this `z` contains a blocker `z_0 in Z`, and any
   near-contact path from `z_0` to `z` has at least

   
   ```math
   { (1-\sqrt3/2)D-1-2\delta\over 1+\delta}
   =(1-\sqrt3/2)D-O(1)
   \tag{19}
   ```


   edges. All its vertices are actual isolated source points, and every
   path edge is an inactive source pair within `1/D` of contact activity.

**Proof.** Nonemptiness is FF.1 plus secondary diameter-pair minimality.
Suppose alternative 1 fails, so every point in `S` is isolated. It does
not contain the two adjacent fan vertices. Perform the finite move

```math
p\mapsto p+w,
\qquad z\mapsto z+w\quad(z\in S),
\tag{20}
```

fixing every other source point.

All separations are preserved or remain at least one:

- the two fan contacts at `p` are exactly preserved by FF.1;
- distances inside `S` and between `p` and `S` are unchanged;
- a fixed point outside `S\cup{p}` has original distance greater than
  `1+delta` from every point in `S`, by graph-component closure, so its
  final distance is strictly greater than one;
- any remaining fixed point other than the two fan neighbors has final
  distance greater than one from `p+w`, since otherwise it would be in
  `Z` and hence `S`.

Thus the old contact set is exactly preserved. The equality issue in (6)
is removed by translating all the blockers with `p`: their original
distances to `p` were strict, and remain strict. There is no new contact
at a component boundary.

All diameter pairs involving the new leaf are strict, except its
distances to translated points of `S`, which retain their original
strict values. Every old diameter pair meeting `S` was absent, since
isolates are not actual diameter endpoints in canonical full support.
Distances inside `S` are unchanged. If every translated-to-fixed cross
distance were strict below `D`, the move would preserve contacts and
delete at least the pendant diameter `pa`, without introducing any new
diameter. This contradicts canonical secondary minimality. Therefore a
cross pair in (18) exists. The triangle inequality gives its old gap
`D-|z-x|<=delta`; its old distance is strict because `z` was isolated.

It remains to localize this failure. Subtract `a` from coordinates and
write `r=z dot u`. If `r>(sqrt(3)/2)D+delta`, then `|z+w|<D`, because
translation decreases its squared distance to `a`. Expanding the failed
diameter constraint gives

```math
(z-x)\cdot u<\delta/2,
```

since `|z-x|<D`. Thus both `z+w` and `x` belong to the disk `B(a,D)`
and to its cap `u dot y >= c`, for some `c>(sqrt(3)/2)D` (one may take
`c=r-delta`). Any point of this cap lies in

```math
B(a+c u,\sqrt{D^2-c^2}),
```

because `|y-c u|^2<=D^2-2c(u dot y)+c^2<=D^2-c^2`.
That cap has diameter less than `D`, contradicting the failed cross
constraint. This proves the final bound in (18).

Every initial blocker satisfies `|z_0-p|<=1+delta`, hence
`(z_0-a) dot u>=D-1-delta`. Each edge of the near-contact path has
length at most `1+delta`; its change in projection is at most that
length. Comparing this initial projection to (18) proves (19). QED.

The isolated case cannot therefore be represented by a bounded local
cluster of near-unit blockers. It must escape through a macroscopic
actual-source near-contact chain to an inactive near-diameter pair.
Alternative 1 can be local; the theorem claims no macroscopic chain to
the positive contact core in that alternative.

## 6. Exact regressions: geometry and local positive equilibrium do survive

The following attempted closing statements are rejected as geometric
lemmas. Their missing global assumptions are explicit.

### 6.1 All one-leaf flips can be blocked by isolated near-triangle points

Choose rational `epsilon,tau` on the unit circle, set `D=1/(2epsilon)`,
and use central rotation `(tau^2-epsilon^2,2epsilon tau)` to form a
short rational unit-chord fan of even cardinality. Group its consecutive
vertices in disjoint pairs. For each pair, let `m` be its midpoint and
`n=m/(D tau)` its radial unit normal. Add the rational source point

```math
z=m-h n,\qquad h>\sqrt3/2,
\tag{21}
```

with `h-sqrt(3)/2` chosen smaller than `1/(100D^2)`. The exact certificate
uses an integer square-root construction of this rational `h`.

Every pair endpoint has squared distance `h^2+1/4>1` from its blocker.
The corresponding two flipped endpoints have squared distance

```math
(h-\tau/D)^2+{1\over4}(1-D^{-2})^2<1.
\tag{22}
```

The checked sources are unit-separated, triangle-free, and have only
the fan edges as unit contacts and only the carrier-star edges as
diameters. All added blockers are contact-isolated and strictly inside
the source hull. The source's diameter ball hull is an intersection of
finitely many Euclidean disks and is strictly convex. Thus strict
ball-hull convexity and exact unit fan geometry alone do not rule out
all local flips being blocked by inactive points.

This is not a global-minimizer counterexample. Indeed the exact verifier
also repairs each internal flip by translating its paired blocker by
the same `-u_i/D`. In every checked source this preserves the entire
contact graph and removes precisely one diameter edge. This confirms
why a movable isolated blocker must not be treated as a closing obstruction.

### 6.2 A long fan with inward spokes admits exact positive local equilibrium

Take a short circular fan centered about `(D,0)` and put

```math
v=(1,0),\qquad z_i=p_i-v.
\tag{23}
```

For a fan of sufficiently small angular width and `D>=4`, the source
`{a,p_i,z_i}` is unit-separated and triangle-free. Its exact contact
graph is the two-row ladder: both unit fan rows plus all unit spokes
`p_i z_i`. Its only diameter edges are `a p_i`; in particular the
interior row is unloaded. Pairwise checks are certified for the rational
instances below, including every nonlocal source pair.

There is an exact strictly positive local KKT equilibrium at every
internal vertex in both rows. Let

```math
\zeta_i={1\over y_{i+1}-y_i}>0,
\qquad C>\max_i\zeta_i,
\qquad \lambda_i=C-\zeta_i>0.
\tag{24}
```

The inner-row reaction at `z_i` is

```math
\zeta_{i-1}(z_i-z_{i-1})+\zeta_i(z_i-z_{i+1})
=\gamma_i v,\quad
\gamma_i={x_i-x_{i-1}\over y_i-y_{i-1}}
         -{x_{i+1}-x_i\over y_{i+1}-y_i}>0.
\tag{25}
```

The horizontal-circle graph `x=sqrt(D^2-y^2)` is strictly concave on
this short arc, proving the strict positivity. The unit spoke supplies
`-gamma_i v` at `z_i`. At the outer row, its positive spoke force and
the two row-contact forces sum to

```math
\lambda_{i-1}(p_i-p_{i-1})+\lambda_i(p_i-p_{i+1})+\gamma_i v
=C(2p_i-p_{i-1}-p_{i+1})
={C\over D^2}(p_i-a).
\tag{26}
```

Thus each pendant diameter has the positive local weight `C/D^2`.
All inward spokes satisfy the exact third-contact cone. The combined
two-row contact stress is flat, `lambda_i+zeta_i=C`, although neither
individual row need be stress-flat.

The missing conditions are global carrier and endpoint equilibrium,
canonical core rigidity/rank, and global minimum-diameter optimality.
In the explicit source the carrier `a` has no unit contact. No complete
normalized KKT stress is claimed. Consequently this regression refutes
only a purported contradiction from the fan's local equilibrium and
strict ball-hull geometry. It does not refute a theorem using the
global positive-contact bridge block or a valid simultaneous Schur bound.

The naive completion by translating the carrier too is impossible:
if both `a,p_i` and `a-v,p_i-v` were retained as diameter pairs, the
two cross squared distances sum to `2D^2+2|v|^2`, so one exceeds `D^2`.
The interior row must be coupled to the actual global source rather
than silently promoted to a second translated diameter fan.

## 7. Certificate, hostile checks, and exact frontier effect

Run

```sh
python3 research/verify_target_c_fan_flip_geometry_2026_10_02.py
```

The certificate uses `Fraction` and integer `isqrt` only. It checks six
rational blocked-fan sources and six rational positive local ladders,
all source pair bounds, exact contact/diameter graphs, strict one-leaf
blockers, the finite co-move repair, and all interior positive equilibrium
identities. It additionally checks the exact lens-radius identities in
FF.3 and rational constants in FF.2. No floating result is load-bearing.
The general statements FF.1--FF.3 and FE are proved analytically above;
the finite certificate does not establish universal graph extraction,
global equilibrium completion, canonical rigidity, or global optimality.

Initial exact output before the co-move checks was:

```text
24 exact flip identities;
6 rational blocked-fan sources: 1968 source pair bounds,
68 strictly blocked internal flips, 40 isolated blockers;
6 positive local ladders: 3472 source pair bounds,
136 exact positive interior equilibrium identities.
```

The final run additionally checks all 68 finite isolate co-move repairs.

| Claim | Classification | Scope / audit limit |
| --- | --- | --- |
| FF.1: finite flip removes all diameters at the moved leaf | proved candidate awaiting promotion | arbitrary actual source fan |
| FF.2: every additional blocker is strictly interior and unloaded | proved candidate awaiting promotion | `D>=4`; all source points retained |
| FF.3: blocker multiplicity at most two, consecutive only | proved candidate awaiting promotion | one ordered source fan |
| FE: core attachment or macroscopic isolate near-contact escape | proved candidate awaiting promotion | canonical normal form plus an actual degree-two fan leaf |
| Near-triangle witness forces exact triangle | rejected | rational blocked-fan regressions have strict noncontacts |
| Local positive inward-spoke equilibrium is geometrically impossible | rejected | rational positive ladder interiors realize it |
| A blocker count by itself settles C-II | rejected | isolate co-moves and the global core branch remain |

Stars and paths are permitted; no Euler-trail shortcut is used.
Infinitesimal velocities are not integrated. Every replacement preserves
source cardinality. The report does not co-embed independently chosen
sources, harmonic scaffolds, or responses. Boundary losses do not occur
in the finite claims. The source isolate population is not bounded or
deleted. None of the regular-shell, inverse-diameter phase, or local
jammed regressions is treated as a globally optimal source.

## 8. Exact remaining gap and next source-level obligation

There is no canonical frontier change and no claim of C-II closure.

The degree-two fan branch now has a finite source-level obstruction,
rather than only a stress-flat first-order identity. It must be coupled
to the actual positive contact core or to a macroscopic isolated
near-contact chain ending at an inactive near-diameter pair. A useful
next theorem would show that the actual augmented component in FE can
be moved together with an attached portion of the positive core while
preserving all contacts and shortening all introduced diameter pairs.
That theorem must retain every contact-isolated source point and all
contact/diameter constraints; it is not proved here.

For the spoke-rich branch, the exact two-layer local equilibrium shows
why a geometric contradiction requires the global carrier/end reactions
or canonical rigidity. The positive-contact common-block and rank
coupling cannot be replaced by local fan positivity.

The high outer-walk excess branch, higher-surplus full-core branch,
split-star O--O, nonconstant-phase witness-cell swaps, inactive-interface,
and macroscopic inactive-container/exterior-cap branches remain open.

**Promotion recommendation:** preserve as unreviewed pending independent
audit of FF.1--FF.3 and FE. No lifecycle promotion is made by this report
or by its PR. Level I remains open.

## Preservation-time nonglobality control (2026-10-15)

For all12 rational fixtures the isolated carrier can be moved by a small
explicit rational positive x step while every other label stays fixed. The
checker verifies all5,440 endpoint pairs, preserves every old unit contact and
opens every old diameter. The [audit](../audits/original12_fan_flip_archive_audit_2026-10-15.md)
gives the finite lower-slack and upper-decrease bounds. This independently
certifies their nonglobal status; no global source is modeled by those fixtures.
