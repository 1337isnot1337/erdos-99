<!-- theorem-state: {"artifact_id":"ART-42109523E6C1","canonical":false,"claim_ids":["C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION"],"claim_statuses":{"C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: pentagon-capped locked train-bank regression

Date: 2026-10-07. Audit base: `e23d88c14fbc95568c41cc8e37ddd2454dec8cd5`, state `2026-10-07.audit.92`; Target C C-II remains open. Frozen source: PR #722, branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. The branch still had this exact tip after the audit. Source report SHA-256 `3b8f9a4c66297a3c448e1a072c36c8424068d265cf3475af0f6b7a423b935432`; verifier SHA-256 `fbe7055cf7ee146f4edac2d0ec48e9d36d8401a149a41f59ff19e213ea1de855`.

## Verdict

**REGRESSION VALID — promote** `C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION` for the explicit finite source family and arbitrary pairwise interior-disjoint actual contact-wall banks stated below.

For every integer `M>=24`, the construction gives a triangle-free source with a quadratic strict-rhombus grid core, a linear bank of long actual contact trains, `Omega(D^2)` train crossings, and pairwise source-vertex-disjoint regular pentagon terminal walls. The pentagons carry five reduced side directions separated by `pi/15`, while the grid angle excess tends to zero. Despite that structure, **every** family of wall-safe packets inside pairwise interior-disjoint simple contact cycles has total capacity at most the total number of old source points in those wall interiors. No fixed-wall bank in this family has positive aggregate surplus, even when composite cycles are allowed.

The source has no certified actual diameter loads and is not asserted globally optimal. It therefore does not refute a canonical C-II theorem that uses actual loaded-return ends, global-minimizer hypotheses, or movable walls. This is a regression against deriving fixed-wall refill surplus from the listed train and phase geometry alone.

One scope repair is needed to the source report's proof citation. The promoted `C-EMBEDDED-WALL-REFILL` theorem is recorded in the state manifest for a canonical contact-minimal global source. Its wall-shield lemma is not the right dependency for this nonglobal example. The needed finite-source shield follows from canonical `C-NONCONTACT-WALL-STRICT-SHIELD`, which applies to arbitrary unit-separated sources and the unit sides here. `C-SHORT-WALL-ZERO-CAPACITY` rules out a packet point in a retained regular-pentagon cap. I reconstructed the remaining containment and Oler steps directly. The reported result survives this correction.

## Exact statement

For every integer `M>=24`, set

```text
t=1/(200 M^3), delta=2 atan(t), phi=pi/3+delta,
u=(1,0), v=(cos(phi),sin(phi)),
X={i u+j v: 0<=i,j<=M}, Q=conv(X), N=(M+1)^2,
I_M={8+6j: j>=0 and 8+6j<=M-9}.
```

For each edge indexed by `I_M` on each of the four sides of `Q`, attach an external regular unit pentagon sharing exactly that edge. The resulting source `A_M` has

```text
|A_M|=N+12|I_M|,
|C(A_M)|=2M(M+1)+16|I_M|,
M<=D(A_M)<=2M+4.
```

Its unit-contact graph is exactly the rectangular grid plus the attached pentagon cycles sharing their prescribed edge. It is triangle-free. All grid boundary vertices and all cap vertices lie on the outer contact cycle; the `(M-1)^2` interior grid vertices have a positive pinned equilibrium and full pinned contact rank when the outer boundary is fixed.

There are `2|I_M|=Omega(D)` complete stopped grid trains, each of length `M=Omega(D)`. Each pair from the two train directions crosses in exactly one of the `|I_M|^2=Omega(D^2)` selected strict rhombi. The terminal pentagon walls are pairwise source-vertex-disjoint, and their five reduced side directions are spaced by `pi/15`; no one reduced direction lies within `pi/30` of all five. The construction also has `|I_M|` vertex-disjoint contact paths of length at least `M/3` to distinct boundary pins. These boundary pins are not asserted actual diameter endpoints.

For **any** finite family of simple cycles `C_1,...,C_b` in the actual contact graph with pairwise disjoint polygon interiors, let

```text
S = union_l (A_M intersect int(C_l)),
Y_l subset W_(C_l),
```

where each `Y_l` is internally unit-separated and `W_(C_l)` is the strict wall-safe region (inside the polygon and at distance greater than one from every wall vertex). Then

```text
sum_l |Y_l| <= |S|.
```

This covers cap faces and arbitrary composite contact cycles. It is a fixed-container statement for the explicit finite family, not a global-optimality theorem.

## Independent proof reconstruction

### Grid contacts and pentagon attachment

For integers `a,b`,

```text
|a u+b v|^2 = a^2+b^2+2ab cos(phi),  pi/3<phi<pi/2.
```

If `a,b` have the same sign and are both nonzero, this is greater than one. If their signs differ, putting `x=|a|`, `y=|b|` gives

```text
(x-y)^2+2xy(1-cos(phi)).
```

It is one only for the six horizontal/vertical unit steps; the diagonal `x=y=1` is strictly longer than one because `phi>pi/3`, and all other integer pairs have length greater than one. Thus the grid contact graph is exactly the bipartite rectangular grid.

Use coordinates `(w,n)` along a shared unit edge and its outward unit normal. A regular pentagon has successive added vertices

```text
c=b+cos(2pi/5)w+sin(2pi/5)n,
d=a+(1/2)w+(sin(2pi/5)+sin(pi/5))n,
e=a-cos(2pi/5)w+sin(2pi/5)n.
```

The five cyclic sides are unit and its diagonals exceed one. The normal depths of `c,e` exceed `9/10`; the depth of `d` exceeds one. Any off-row grid point has inward normal depth at least `sin(phi)>sqrt(3)/2`, so its distance to each added cap vertex is greater than one. On the supporting grid row, `c` has its prescribed anchor `b` as its only unit neighbor: the nearest other row point has squared distance `2-2cos(2pi/5)>1`; `e` is symmetric and `d` is already more than one away by normal depth.

Each cap vertex lies within distance two of its shared-edge midpoint. Midpoints on one side are at least six apart; those on adjacent sides are at least `8.5` apart because the first selected edge index is eight and the side angle is at least `pi/3`; opposite-side midpoints are separated normally by `M sin(phi)>20`. Hence cap vertices on distinct pentagons are more than two apart. There are no unintended contacts or cap intersections. The embedded contact graph is the grid plus the prescribed five-cycles, which is triangle-free. Attaching these disjoint caps along separate boundary edges leaves a topological disk; all cap vertices and all original grid boundary vertices stay on its outer contact cycle.

### Exact container capacity

The finite Oler inequality from `docs/theory/03-oler-shell.md`, Lemma 21.1, gives for every unit-separated set in the convex parallelogram `Q`

```text
N_pack(Q) <= 2 area(Q)/sqrt(3) + perimeter(Q)/2 + 1.
```

Here `area(Q)=M^2 sin(phi)` and `perimeter(Q)=4M`. With `a0=sqrt(3)/2`, the right side is

```text
N + r,   r=M^2(cos(delta)-1+sin(delta)/sqrt(3)).
```

The identity

```text
r=M^2 sin(delta)*(1/sqrt(3)-tan(delta/2))
```

shows `r>0`, because `tan(delta/2)=t<1/sqrt(3)`. Also `r<M^2 sin(delta)/sqrt(3)<2M^2t=1/(100M)<1`. Oler and integer rounding therefore give `N_pack(Q)<=N`. The grid `X` supplies `N` points, so the exact packing capacity of `Q` is `N`.

### Arbitrary contact-wall packet bank

Let `P` be the union of `Q` and the attached caps. Any simple contact cycle lies in this planar disk, so its bounded interior lies in `P`. Every vertex on the outer contact cycle has an exterior path to infinity avoiding every contact cycle; therefore no grid-boundary or cap vertex lies strictly inside any `C_l`. In particular `S` consists only of grid points in `int(Q)`.

The general finite-source `C-NONCONTACT-WALL-STRICT-SHIELD` applies to each `W_(C_l)` and to pairwise interior-disjoint walls: each packet is strictly separated from all retained source vertices outside its wall, and distinct wall packets are jointly unit-separated. Cap vertices are retained outside every wall interior. If a packet point lay inside a cap pentagon, the shield would put it at distance greater than one from all five cap vertices, contradicting `C-SHORT-WALL-ZERO-CAPACITY`; points on cap edges are likewise within one of a retained cap endpoint. Thus every `Y_l` lies in `Q`.

The old grid points `X\S` and all new sites `Y_l` form a unit-separated set in `Q`. Its cardinality is `N-|S|+sum_l|Y_l|`. Oler's capacity bound forces this to be at most `N`, proving `sum_l|Y_l|<=|S|`. This argument does not assume the wall cycles are pentagons or single faces.

### Stress, trains, and scope

At every unpinned grid-interior vertex, unit weights on the four grid directions `+u,-u,+v,-v` balance exactly. For pinned rank, vertical flex equations make the `v`-component constant along each column and the pinned endpoints make it zero; horizontal equations then make the remaining normal component constant along each row and the pinned row endpoints make it zero.

For each selected edge index, the grid strip across `M` successive rhombi is a stopped train between the opposing pentagons. Opposite train directions cross once per selected index pair. The phase calculation is local to the regular pentagon: its edge directions reduced modulo `pi/3` are five equally spaced values with gap `pi/15`. None of these facts assigns any boundary pin as a diameter endpoint or produces a KKT stress for the full decorated source.

## Certificate, exclusions, and frontier effect

I inspected and reproduced `research/verify_target_c_pentagon_capped_lock_2026_10_05.py`. Its directed rational interval arithmetic for `Q(sqrt(3),sqrt(5))` ran all five cases `M=24,30,36,32,40`, checking 3,921,688 source pairs, intended unit contacts, strict noncontacts, triangle-freeness, cap separation, the Oler residual bound, source/contact counts, and selected crossing cells. The default script also checks finite radial-leaf variants at `M=32,40`; those extra cases are not part of the promoted theorem. Analytic all-`M` claims and the arbitrary-wall inequality are proved above; finite samples alone do not establish them.

The source report's non-effective Theorem L.2 uniqueness-window variant and its Section 9 radial-leaf equilibrium strengthening are **not promoted**. No actual diameter loading, full-source canonical equilibrium, global optimality, actual loaded-return path, fixed-wall positive surplus, C-II closure, or Level I result follows.

The exact implication chain is: quadratic actual train crossings plus disjoint direction-frustrated pentagon terminals do not force a positive fixed-wall bank surplus; Oler capacity forces every such aggregate packet bank to have nonpositive surplus in this family. A canonical argument using this geometry must still add actual load/global-minimizer information or move/break the outer guard vertices. The face-coupled finite-move and arbitrary-container capacity obligations remain open.

| Claim | Verdict | Canonical disposition |
| --- | --- | --- |
| Explicit triangle-free grid with disjoint regular-pentagon train terminals and quadratic crossings | PASS — exact finite-family theorem | Include in the regression scope |
| No positive aggregate capacity for any bank of interior-disjoint actual contact walls | REGRESSION VALID | Promote `C-PENTAGON-CAPPED-LOCKED-TRAIN-BANK-REGRESSION` |
| Radial-leaf strengthening from source Section 9 | Not audited for all `M` | Do not promote |
| Non-effective fixed-`M` uniqueness-window variant | Not needed for the explicit family | Do not promote |
| Canonical global-minimum or actual-loaded-endpoint conclusion | Not claimed | No C-II/Level I effect |
