<!-- theorem-state: {"artifact_id":"ART-666D492CA3D5","canonical":true,"claim_ids":["C-AFFINE-LATTICE-EXTREME-VERTEX-COUNT","C-DIAMETER-NORMAL-APPROX-LATTICE-EXCLUSION","C-EXACT-LATTICE-ATTACHMENT-REMAINDER","C-NEAR-DISK-APPROX-LATTICE-BOUNDARY-EXCLUSION"],"claim_statuses":{"C-AFFINE-LATTICE-EXTREME-VERTEX-COUNT":"canonical","C-DIAMETER-NORMAL-APPROX-LATTICE-EXCLUSION":"canonical","C-EXACT-LATTICE-ATTACHMENT-REMAINDER":"canonical","C-NEAR-DISK-APPROX-LATTICE-BOUNDARY-EXCLUSION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit: loaded attachment lattice obstructions

Date: 2026-10-07. Audit base: `8ed253ecbff85b0f1ee7f2b20a17fadc4f256e3c`, state `2026-10-07.audit.90`; Target C C-II open. Frozen source: PR #722, branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: [`target_c_loaded_attachment_lattice_obstruction_2026-10-05.md`](../reports/target_c_loaded_attachment_lattice_obstruction_2026-10-05.md), SHA-256 `6af268a4ba51b8a86de6d9ea0652957bf4c8f3e85bb66fe0255fcb1cc2275c27`.

## Verdict

**PASS — promote** four modular claims at their exact scopes:

1. the finite extreme-vertex count for a uniformly conditioned affine lattice;
2. the `O(D^(8/9))` bound on actual loaded endpoints in exact-lattice attachment sets and the resulting necessary nonlattice/unused alternative;
3. the quantitative near-disk approximate-lattice boundary bound and its fixed-carrier exclusion;
4. the branch-independent diameter-normal bound and its fixed-carrier exclusion.

The near-disk result bounds `q=|B|`; the branch-independent result instead bounds the number `h` of actual diameter edges. The latter uses the full actual diameter graph and applies in either canonical branch. Neither result says canonical phase coherence gives an `o(1)` physical-position lattice cover. The bent-grid transport report is a separate proof-only regression under reduced hypotheses; it is not used as a premise or promoted here. No finite verifier or new certificate is claimed, and no C-II or Level I closure follows.

## Exact objects and audited statements

For a finite unit-separated source `A` of diameter `D`, let `H` be its full actual diameter graph, `B` its actual diameter-endpoint set, `q=|B|`, and `h=|H|`. The canonical C-II normal form retains every source point, including contact isolates. Each `b in B` is an extreme point of the full source hull: if `b` were a nontrivial convex combination of other source points, pairing that combination with a diameter partner and applying strict convexity of squared norm would contradict the upper bound `D` on every source distance. In particular every point of any `E subset B` is a vertex of `conv(E)`.

### Uniformly conditioned lattice hull count

If `E` consists of `m` extreme source-hull vertices, lies in an affine lattice `a+t Z^2` with `t` invertible and `||t^(-1)||<=K0`, and `P_E=per(conv(E))`, then

```text
m <= 2 + 10 K0^(2/3) P_E^(2/3).
```

The separate `2` covers sets of at most two points, including segments. If `L` such carriers cover `B` except for `B0`, and `P_j` are their convex-hull perimeters, then

```text
q <= |B0| + 2L + 10 K0^(2/3) L^(1/3) (sum_j P_j)^(2/3).
```

Thus `L=o(D)`, `sum P_j=O(D)`, and `|B0|=o(D)` imply `q=o(D)`. Without a total-perimeter hypothesis, `P_j<=pi D` gives the separate consequence `q=o(D)` if `L=o(D^(1/3))`.

### Exact-lattice attachment remainder

For the canonical unloaded harmonic components `I_r` and their actual loaded attachment sets `A_r`, call `r` uniformly exact-lattice if `A_r` lies in an affine lattice whose inverse-basis norm is at most one fixed `K0`. Canonical Sections 62 and 75 give

```text
c_I=O(D^(2/3)),
sum_r per(conv(A_r)) <= pi(2+2q)=O(D).
```

Applying the finite count and Holder's inequality to all uniformly exact-lattice attachment sets gives

```text
|union_{r exact} A_r| = O(D^(8/9)) = o(D).
```

Since the canonical diameter graph satisfies `q>=h>=ceil(D)`, the union of unused loaded endpoints and loaded endpoints attached to components that fail this uniform exact-lattice condition has size at least `D-O(D^(8/9))`. If unused loaded endpoints are `o(D)`, the nonlattice attachment union is therefore linear. This conclusion does not count defects, contacts, components, or spare sites, and contact-isolated source points remain outside `c_I` and retained.

### Approximate lattices in the full-core near-disk branch

Assume the actual loaded hull `F=conv(B)`, after translation, satisfies `B(0,r) subset F subset B(0,R)`. Put `alpha=acos(r/R)`. Apart from `B_bad`, partition `B` into `J` sets `E_j`; each point of each `E_j` is within `epsilon<1/4` of some point of an affine lattice `a_j+t_j Z^2`, with `||t_j^(-1)||<=K0`. The lattices may vary between carriers and between sources. For `1<=L<2r`, set

```text
delta=asin(2 epsilon),
Delta=2 asin(L/(2r)),
M=(2 K0 (L+2 epsilon)+1)^2.
```

If `Delta+2 alpha<pi`, the exact finite bound is

```text
q <= |B_bad| + 2J + J pi D/L
     + 2 J M R/cos(alpha) * (delta+alpha+Delta).
```

In a canonical full-core near-disk sequence, `r/D,R/D -> 1/2`, so `alpha->0`. For fixed `J,K0`, `|B_bad|=o(D)`, and positional error `epsilon=o(1)`, fix `L` first and then send `D->infinity`; the last term is `o(D)` and `limsup q/D<=J pi/L`. Send `L->infinity` afterward to obtain `q=o(D)`, contradicting `q>=h>=ceil(D)`. No rate for near-disk convergence or `epsilon` is needed. This claim is scoped to the full-core near-disk branch.

### Approximate lattices and actual diameter normals in either branch

For any finite unit-separated source with `D>=2`, use the same `B_bad`, partition, positional error, and affine-lattice condition. Put

```text
delta=asin(2 epsilon),
delta_D=2 asin(1/(2D)),
M=(2 K0 (L+2 epsilon)+1)^2.
```

For every `L>=1`, the exact finite estimate is

```text
h <= |B_bad| + 2J pi D/L + J(2M+2) + 2 J M delta/delta_D.
```

For fixed `J,K0`, `epsilon=o(1)`, and `|B_bad|=o(D)`, fix `L` while `D->infinity`, then send `L->infinity`; this yields `h=o(D)`. For a canonical C-II sequence, Section 57 gives `h>=ceil(D)`, so such a cover cannot occur in either the full-core or macroscopic-container branch.

## Independent proof reconstruction

### Integer polygon estimate

Apply `t^(-1)` and translation to send `E` into `Z^2`; the transformed perimeter is at most `K0 P_E`. In a convex polygon with its collinear nonvertices removed, oriented side vectors are distinct. For `R>=1`, at most `(2 floor(R)+1)^2-1<=9R^2` nonzero integer vectors have length at most `R`, while at most `P'/R` sides can be longer than `R`, where `P'` is the transformed perimeter. Taking `R=(P')^(1/3)` gives at most `10(P')^(2/3)` sides. A set with fewer than three hull vertices is bounded separately by two. Summing this estimate and applying Holder proves the carrier inequality; overlaps only make the upper bound looser.

### Attachment composition

For each `r`, harmonic trapping gives `diam(A_r)<=delta_r+2`; Cauchy's convex perimeter-diameter inequality gives `per(conv(A_r))<=pi(delta_r+2)`. Summing Section 75's exact component ledger yields `sum delta_r+2 c_I<=2+2q`; summing perimeters gives the stated `pi(2+2q)` cap. With `c_I=O(D^(2/3))`, the lattice vertex count is at most

```text
2c_I + 10 K0^(2/3) c_I^(1/3) [pi(2+2q)]^(2/3) = O(D^(8/9)).
```

The subtraction from `q>=D` leaves the claimed residual union. It cannot be strengthened to a statement that every attachment component has a lattice defect.

### Near-disk boundary arcs

For one carrier with at least three points, order its vertices around `F`. At most one forward radial gap is at least `pi`; discard that edge. An edge longer than `L` is charged to its length, so there are at most `per(conv(E_j))/L<=pi D/L` of them. For each remaining short edge `ab`, its radial gap `eta` is below `pi`. Since `|a|,|b|>=r`, the identity

```text
|a-b|^2=(|a|-|b|)^2+4|a||b| sin^2(eta/2)
```

gives `eta<=Delta`. Choose lattice approximants `a',b'`; their difference is nonzero because `|a-b|>=1>2 epsilon`, and it is within `2 epsilon` of the chord. The chord normal is therefore within `delta` of one of at most `M` lattice-vector normals. Every outward hull normal is within `alpha` of its radial direction because its support value is at least `r` and boundary radius is at most `R`. Along the short forward hull arc, edge tangents lie in an angular interval of width at most `eta+2alpha<pi`; their positive vector sum puts the chord normal within `alpha+eta` of every radial direction on that arc. The entire arc thus lies in at most `M` radial intervals of width `2(delta+alpha+Delta)`. On each hull side, the radial arclength density satisfies `ds/dtheta<=R/cos(alpha)`: the radial direction makes angle at most `alpha` with the side normal, so its angle with the tangent has sine at least `cos(alpha)`. The carrier's short-arc interiors are disjoint and each short chord has length at least one, proving the finite estimate after adding the one discarded gap, long edges, and at most two points for a small carrier.

### Diameter-normal bound

For each `E_j`, every actual loaded endpoint is extreme, hence a vertex of `conv(E_j)`. A short edge's actual normal is within `delta` of the normal to a nonzero lattice difference vector of length at most `L+2 epsilon`; there are at most `M` possible vectors. Let `W_j` be the union of their closed normal intervals, each of width `2delta`. Long-edge incident vertices contribute at most `2 pi D/L`. Among vertices with two short incident sides, each normal cone whose endpoints lie in `W_j` but is not wholly contained in `W_j` contains a full connected component of the open complement. Distinct vertex normal-cone interiors are disjoint, and the complement has at most `M` components. Small carriers contribute at most two more bad vertices. Hence each carrier has at most `2 pi D/L+M+2` bad endpoints.

At every remaining endpoint, its actual diameter normal lies in the carrier's `W_j`: expanding `|x-q|^2<=D^2=|p-q|^2` gives

```text
n dot (x-p) <= -|x-p|^2/(2D) < 0
```

for every other source point `x`, so `p` is the unique support point of `conv(E_j)`. Canonical DB.3 separates distinct actual diameter directions projectively by `delta_D`. There is at most one actual diameter edge per projective direction: if two pairs had common oriented displacement `D n`, the two cross-pair upper bounds imply `|w-Dn|^2<=D^2` and `|w+Dn|^2<=D^2` for the difference `w` of their first endpoints; adding forces `w=0`, so the pairs coincide. Each of at most `M` projected intervals contains at most `1+2delta/delta_D` actual diameter directions. Thus at most `JM(1+2delta/delta_D)` edges have a good endpoint. All remaining diameter edges lie in the induced diameter graph on the bad endpoint set. Canonical Woodall topology is hereditary under vertex deletion and has at most as many edges as vertices, giving the displayed finite estimate.

## Hostile scope checks

- `E_j` must consist of actual loaded diameter endpoints, which are extreme; the lattice vertex estimate is false for unrestricted interior lattice patches.
- `J` and `K0` are uniform in the asymptotic exclusions. The lattices themselves, including their translations and orientations, may vary.
- Positional error is physical Euclidean distance. Coherent phase labels or small per-train angular changes do not imply this hypothesis. The separate bent-grid transport report is an unreviewed reduced-hypothesis guardrail, not a premise here and not a counterexample to the canonical conditional theorem.
- Section 7 is only the near-disk full-core conclusion. Section 8 uses every actual diameter edge and no selected-stress subset, so it covers either canonical branch.
- `B_bad` and every source point outside the counted sets remain in the configuration. Contact isolates are not counted as unloaded components and are never removed.
- The asymptotic limit order is fixed `L`, then `D->infinity`, then `L->infinity`; no uniform rate is assumed.
- No lattice cover is established for canonical sources, no finite source move or packet is made, and no global-optimality or Level I implication is asserted.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Extreme-vertex count in a uniformly conditioned affine lattice | PASS | Promote `C-AFFINE-LATTICE-EXTREME-VERTEX-COUNT` |
| Exact-lattice attachment population and nonlattice/unused residual | PASS | Promote `C-EXACT-LATTICE-ATTACHMENT-RESIDUAL` |
| Near-disk approximate-lattice boundary bound and fixed-carrier exclusion | PASS | Promote `C-NEAR-DISK-AFFINE-LATTICE-EXCLUSION` |
| Actual diameter-normal bound and branch-independent fixed-carrier exclusion | PASS | Promote `C-DIAMETER-NORMAL-LATTICE-EXCLUSION` |
| Coherent grains imply boundedly many `o(1)` positional lattice carriers | NOT ESTABLISHED | Do not promote or infer from the four theorems above |
| C-II or Level I closure | NOT ESTABLISHED | The active finite-move and capacity obligations remain open |
