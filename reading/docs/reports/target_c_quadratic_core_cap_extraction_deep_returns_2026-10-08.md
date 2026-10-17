> Generated reading edition · [exact source](../../../docs/reports/target_c_quadratic_core_cap_extraction_deep_returns_2026-10-08.md) · source SHA-256 `d950294d1cdbd8d2fd88d944c0921af51a77cbd56e53f63ddb8132ec8622285e`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "4844913807b6e907541ca446a0a36a673fdc2d45", "source_branch_refs": ["refs/heads/research/level-i-closure-20261007"], "source_commit": "eca2414c17be705857e3922d9302393e7bd0265f", "source_lifecycle": "unreviewed", "source_path": "docs/reports/target_c_quadratic_core_cap_extraction_deep_returns_2026-10-08.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "35cedb4005ef51cf38b12ee1fc672b33a7a7f4ee428a93758b1f4376fa2cead3"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: extracting a loaded-chord cap from a quadratic harmonic grain

Date: 2026-10-08.
Run base: `4ed6561832f1eafcd7bac24373215f1a2992e4a2`.
Canonical base: `023917ace0719d0050664a8a08fed1eb5cdb2013`.
State: `2026-10-08.audit.139`.
Classification: proved candidate awaiting independent audit/promotion.
Registry: unreviewed; noncanonical. Level I and C-II remain open.

Rechecked after rebasing onto `419ab570f137bb5243155086285d10354b6c9616`,
state `2026-10-08.audit.142`. The new fixed exterior-wall capacity,
weak-guard ledger and edge-completion regression do not alter the
canonical cap/grain/return inputs used here.

## 1. Exact source conclusion and missing closing step

Work along a canonical contact-minimal, then diameter-pair-minimal
triangle-free global-source sequence with `D -> infinity`. Retain all
source points. Assume its positive-contact core has quadratic population
along the selected subsequence. Fix `0<epsilon<pi/6`.

The candidate conclusion is that the source supplies the following
objects with fixed positive quadratic and linear constants:

- one unloaded contact component `I`, its actual loaded attachment set
  `A`, and its harmonic cell `P=conv(A)`;
- a chord `[a,b]` between two nonconsecutive vertices of the full loaded
  hull `F=conv(B)`, with `a,b in A`;
- a proper convex force-hull cap `C=F intersect {eta>=0}` based on
  that chord, and an attachment `a_* in A` of maximum signed height;
- an epsilon-coherent, edge-connected grain `G` of actual strict unit
  rhombi, all vertices in `I`, contained in `int(C) intersect int(P)`,
  with area `A_G>=alpha D^2` and physical perimeter `O(D)`;
- `H=eta(a_*)>=A_G/D>=alpha D`.

Thus the written cap/grain/port antecedents of
[Audit.136](../audits/target_c_typeii_near_port_grid_independent_audit_2026-10-08.md)
and [Audit.137](../audits/target_c_deep_far_cap_grid_independent_audit_2026-10-08.md)
can be supplied for a cap selected from this grain. This does not
establish an antecedent for a separately prescribed cap or port.

Trimming this cap yields a complete actual train grid with both shores
linear in `D`, at linear distance from every loaded endpoint, and linear
vertex-disjoint actual contact returns with quadratically many distinct
internal vertices outside the cropped grid region.

A whole-cell variant puts those outside vertices in the boundary strip
of `P`. Neither variant supplies independently usable exchange capacity
or a finite source move. The implication chain is:

    canonical same-cell quadratic coherent grain
      -> a proper loaded-chord cap containing quadratic coherent mass
      -> a deep cropped complete grid and simultaneous actual returns
      -> distinct source population outside the entire cropped region.

The remaining Level I step is to pay this packet against a global
population/phase budget or realize a full-source strict-D replacement.
No such step is proved here; the subquadratic-core branch remains separate.

## 2. Canonical inputs

- [Section 78](../targets/target-c/78-harmonic-cell-grid-localization-audit.md)
  supplies one quadratic coherent grain `G_0` inside one unloaded component
  `I` and its cell `P=conv(A)`, with `area(G_0)>=alpha_0 D^2` and
  `P(G_0)<=C_0 D`.
- [Section 83](../targets/target-c/83-attachment-cell-disjoint-tiling-audit.md):
  `A subset B=Vert(F)`; harmonic cells are convex, with
  `I subset P subset F`. Every attachment set has at least three
  noncollinear vertices.
- [Section 73](../targets/target-c/73-pseudosegment-grid-extraction-audit.md)
  extracts a complete distinct-phase grid from a quadratic coherent
  strict-rhombus complex with perimeter `O(D)`, allowing holes.
- [Audit.133](../audits/target_c_rhombus_bulk_separator_independent_audit_2026-10-08.md):
  any `R` actual rhombi in `I` yield at least `ceil(F(R))` vertex-disjoint
  contact paths to distinct actual attachments, where
  $$
  F(R)={\sqrt{25+4cR}-5\over2c},\qquad c={8\pi\over\sqrt3}.
  \tag{CE1}
  $$
- The additional Type-II corollary in Section 6 uses
  [Section 80](../targets/target-c/80-global-isolate-concentration-fullcore-disk-audit.md)
  for rhombic saturation of `F` and
  [Section 69](../targets/target-c/69-coherent-grain-interface-audit.md)
  for fixed-epsilon coherent grains of total perimeter `O_epsilon(D)`.

The proofs below also use planar isoperimetry, the area lower bound
`a_0=sqrt(3)/2` for a strict unit rhombus, its diameter bound `<2`,
and convex-body boundary tubes. No multiplier floor, cap-density
assumption, or contact-connectivity inference from mixed rank is used.

## 3. Strict trapping and a proper chord

In fact `I subset int(P)`. If a supporting functional of `P` attained
its maximum at an unloaded vertex, positive harmonic equilibrium would
propagate that maximum through the connected component `I` and then to
every attachment in `A`. This contradicts the noncollinearity of `A`.
Every closed rhombus face of `G_0` is consequently inside `int(P)`.

The full loaded set has `q>=ceil(D)`, so eventually `q>=4`. Among
any three distinct members of `A`, some pair `a,b` is nonconsecutive
on the cyclic hull `B`: a cycle of length at least four has no triangle.
The line `ab` therefore cuts the interior of `F`. Its intersection with
`F` is exactly `[a,b]`, since both endpoints are extreme vertices.
It defines two proper convex caps `C_+,C_-`.

Choose the side containing at least half of the physical area of
`G_0`. Let `eta` be signed unit-normal height, positive on that side.
Then
$$
\operatorname{area}(G_0\cap C)\ge A_0/2,\qquad A_0=\operatorname{area}(G_0).
\tag{CE2}
$$

All face omissions below restrict the auxiliary grain complex; no
source label or contact is changed. Omit every `G_0` rhombus meeting
the chord line. Such a rhombus
meets `[a,b]` and lies in its width-two tube. The tube area is at most
`4D+4pi`; disjoint rhombus interiors give at most
$$
M\le{4D+4\pi\over a_0}
\tag{CE3}
$$
removed faces. Their area is at most `M`, since a unit rhombus has
area at most one. The faces surviving wholly on the chosen side have
total area at least `A_0/2-M >= A_0/3` eventually.

Deleting a face exposes at most four unit-edge boundary occurrences.
The sum `P_1` of the surviving edge-connected component perimeters
therefore satisfies
$$
P_1\le C_0D+4M=O(D).
\tag{CE4}
$$
For their areas `A_j`, isoperimetry gives
`sum sqrt(A_j)<=P_1/(2sqrt(pi))`. Hence some one component has
$$
A_G\ge{4\pi(A_0/3)^2\over P_1^2}=\Omega(D^2).
\tag{CE5}
$$
Call it `G`. It is an epsilon-coherent subcomplex of the original
grain, still in `I`, with perimeter at most `P_1`. Its closed faces
lie in `int(C) intersect int(P)`. This proves the required cap/grain
extraction.

Choose `a_* in A` maximizing `eta`, and put `H=eta(a_*)`. Convexity
gives `eta<=H` on `P`, while `G` lies between heights zero and `H`.
Every tangential slice of `F` has length at most `D`. Therefore
$$
A_G\le DH,\qquad H\ge A_G/D.
\tag{CE6}
$$
The maximum is positive, so `a_*` lies on the chosen force-hull arc
between `a,b` and is an actual attachment of this same component.
All `B` vertices lie outside `int(C)`.

## 4. Deep complete grid and outside-region returns

Set
$$
h={A_G\over8\pi D},\qquad s={A_G\over4D},\qquad
W=C_{-h}\cap\{\eta\le H-s\}.
\tag{CE7}
$$
Keep only grain rhombi whose entire faces have distance greater than
`h` from `partial C` and height strictly below `H-s`.

Faces lost at the cap boundary lie in its inner strip of width `h+2`,
of area at most `pi D(h+2)=A_G/8+2pi D`. Faces lost at the height
cut lie in a slab of width `s+2`, of area at most `D(s+2)=A_G/4+2D`.
Thus at least half the grain area survives eventually.

The convex set `W` has perimeter at most `pi D`. Every discarded
face exposing a new retained boundary touches `partial W` and lies
in its width-two tube. That tube has area at most `4pi(D+1)`.
The sum `P_2` of the surviving component perimeters is bounded by
$$
P_2\le P(G)+{16\pi(D+1)\over a_0}=O(D).
\tag{CE8}
$$
The same square-root area argument gives one coherent retained
component of quadratic area. Section 73 supplies a complete grid
with shore sizes `u,v>=gamma D` in this component, hence entirely
in `W`, for a fixed `gamma>0`.

Apply CE1 to its `uv` crossing rhombi. There are
`p>=ceil(F(uv))=Omega(D)` mutually vertex-disjoint actual contact
paths in `I union A`, stopped at their first loaded endpoint.
For each path retain only the suffix after its last source vertex in
`W`. Its first vertex has distance at least `h` from every loaded
endpoint, so that suffix has at least `ceil(h)-1` internal vertices.
Every such internal vertex is in `I setminus W`. Disjointness is
preserved. Consequently
$$
\boxed{|I\setminus W|\ge p\,(\lceil h\rceil-1)=\Omega(D^2).}
\tag{CE9}
$$
These vertices lie outside the entire cropped region, not only outside
the crossing-rhombus vertex set. The last retained start need not be
one of the original grid vertices.

Every cropped grid vertex is also at distance at least `s` from
`a_*` by the unit Lipschitz bound on `eta`. Thus this construction
supplies the written deep/far hypotheses and conclusion of Audit.137
on every quadratic-core subsequence, without an additional prescribed
host-cap package.

## 5. Whole-cell boundary-strip variant

For an annulus population statement, start with `G_0` and use the
whole convex harmonic cell `P` instead of the proper cap. Put
`h_0=A_0/(8pi D)` and `W_0=P_{-h_0}`. Omit the height cutoff.
The preceding boundary trimming, component selection and complete-grid
argument still apply.

No loaded endpoint lies in `int(P)`, because every member of `B`
is an extreme vertex of `F`. All return paths lie in `I union A
subset P`. Taking suffixes after their last visits to `W_0` now gives
$$
\boxed{\#\{x\in I:\operatorname{dist}(x,\partial P)<h_0\}
\ge p_0\,(\lceil h_0\rceil-1)=\Omega(D^2)}
\tag{CE10}
$$
for `p_0=Omega(D)` disjoint paths. This is distinct source population
in a specified cell boundary strip. It is not outside-cell population.

## 6. Uniform near-port grids in the Type-II branch

Assume additionally the canonical Type-II branch. For every fixed
`0<rho<1` there is a fixed `gamma_rho>0` such that, eventually,
**every** actual attachment `a in A` has a complete epsilon-coherent
grid with both shores at least `gamma_rho D` in
`closed_ball(a,rho D) intersect int(P)`, belonging to this same
unloaded component `I`. The constant and the eventual threshold are
uniform over `a in A`.

To prove this, set `K_0=conv(G_0)` and
`K_{a,rho}=a+rho(K_0-a)`. This is an auxiliary region; no source
face is moved. Strict trapping and convexity give
`K_{a,rho} subset int(P)`, its area is at least `rho^2 A_0`,
and its diameter and perimeter are at most `rho D` and `pi rho D`.
Every point is within `rho D` of `a`.

Type-II saturation and Section 69 leave only `o(D^2)` force-hull area
outside fixed-epsilon coherent rhombi. That one global missing-area
bound applies uniformly to every moving region `K_{a,rho}`.
Rhombi meeting its boundary cost only `O(D)` area and expose only
`O(D)` new sides, uniformly in `a`. Thus the retained coherent
pieces have total area at least `rho^2 A_0-o(D^2)` and total
perimeter `O_epsilon(D)`. Isoperimetry selects a quadratic piece,
and Section 73 selects its linear-by-linear complete grid.

Each retained rhombus is wholly in `int(P)`, so all its vertices
are unloaded. Its actual contacts place it in an unloaded component
`I'` and harmonic trapping puts it in `P_{I'}`. If `I' != I`,
its positive-area interior would contradict the interior-disjointness
of harmonic cells. Hence the grid belongs to `I`.

For the selected high port `a_*` of Section 3 and
`rho<min(1,alpha/2)`, the unit Lipschitz bound on `eta` also gives
positive height at least `alpha D/2`. This recovers Audit.136's
geometric near-port conclusion for the package constructed here.
No linear shore constant is claimed when `rho=rho_D -> 0`, and
no contact-route length or multi-port route payment follows.

## 7. Scope and certificate

This selects a cap and port from the canonical grain. It does not
validate a cap or port specified before the selection, and it does
not establish a short fixed-port route or a uniform defect-tail bound.
In Type II, the extracted package satisfies Audit.136's written
antecedents; its vanishing-tail alternative remains a separate condition.

CE9 and CE10 count source vertices, not exchange sites or new capacity.
The paths may use other rhombi and grains. The boundary strip has
quadratic area available, so its quadratic population is not by itself
a contradiction. No simultaneous multi-cell payment or finite
full-source endpoint is inferred.

The rational checker
`research/verify_target_c_cap_crop_return_suffix_2026_10_08.py`
checks proper-cap extraction, whole-cell and cap interior crops,
actual unit contacts, complete rectangular subgrids, integral contact
flows, and the last-crop-visit suffix counts on three nonglobal boards.
Its designated boundary terminals are artificial pins, not certified
actual diameter endpoints; it also checks a strict square-grid
competitor. The universal canonical implication is proved above,
not by extrapolating those finite tests.

At `m=16,24,32` the certificate passed 829,032 full-source pair
checks, 1,856 strict rhombi, 210 chord-crossing face checks, 823 cap
rhombi, and 36 disjoint actual-contact returns. Both last-visit
truncations certify 80 distinct internal suffix vertices across the
three fixtures. The actual diameter calculation identifies two
loaded endpoints per fixture, distinct from the artificial terminal
sets of sizes 64, 96 and 128.
