<!-- theorem-state: {"artifact_id":"ART-3901E738FD3A","canonical":false,"claim_ids":["C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION"],"claim_statuses":{"C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: positive pinned rigidity does not control face tails

Date: 2026-10-08. Audit base: `origin/main=7d95fa30f685c526297448f8f58ae71f33553345`, state `2026-10-08.audit.122`; Target C C-II remains open.

Frozen source: `origin/research/sol-positive-rigid-face-tail-20261004` at `9b228cb753519ae9c3357b255742010dc78f4c4d`. Source report `docs/reports/target_c_positive_rigid_face_tail_regression_2026-10-04.md`, SHA-256 `d0ed7183f3842e9675b529d8f464d18c8a4daf32d5b769d53d89c68135903c05`. Exact finite verifier `research/verify_target_c_positive_pinned_face_tail_2026_10_04.py`, SHA-256 `37c50a57d50b0365224d2083a82ec9c5885a179e646bb78f87152f0e26ceb16d`.

## Verdict

**PASS — promote `C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION`.** The infinite rational family satisfies the report's local pinned equilibrium and rigidity hypotheses and has one bounded contact face whose degree-defect tail remains asymptotically `2D`. It is explicitly nonglobal and fails the full-source positive KKT/actual-loading hypotheses. This rejects the local-to-tail implication at exactly its stated scope, while leaving the canonical Type-II question intact.

## Exact statement and independent reconstruction

For each even `L>=12`, form a strictly convex unit-edge polygon `P_L` with `m=2L+4` vertices. The bottom chain has edge vectors `u_i=h_i^2`, where

```text
t_i=(2i-L-1)/(100L^2),
h_i=((1-t_i^2)/(1+t_i^2),2t_i/(1+t_i^2)),   i=1,...,L.
```

The top chain is the vertical reflection of the bottom chain traversed in reverse. Since `t_{L+1-i}=-t_i` and `(u_i)_y` is odd in `t_i`, the bottom chain ends at `(X_L,-24/25)`. Two two-edge caps join the chains through apices at `(-7/25,0)` and `(X_L+7/25,0)`. At every nonapex polygon vertex insert the outward unit angular-bisector pin; at each apex insert the two stated unit pins with offsets `(±4/5,±3/5)`. The free set is the polygon vertex set `I_L`; the inserted pins form `B_L`.

### Separation, hull and face checks

The parameters are rational, and `|t_i|<1/(100L)`. Direct algebra gives

```text
(u_i)_x=1-8t_i^2/(1+t_i^2)^2 >= 1-1/(1250L^2),
|(u_i)_y| <= 4|t_i| < 1/(25L),
L-1/(1250L) <= X_L <= L.
```

The bottom and top walls remain in `y<=-24/25` and `y>=24/25`; their vertical excursion is less than `1/50`. The half-angle sequence for the directed polygon edges is

```text
h_1,...,h_L, (4/5,3/5), (3/5,4/5),
(h_L.y,h_L.x),...,(h_1.y,h_1.x), (-3/5,4/5), (-4/5,3/5).
```

Squaring these unit vectors gives the actual edge directions. The `t_i` increase, are all smaller than `1/(100L)` in magnitude, and are symmetric about zero; the cap half-angles lie strictly between the wall-direction blocks. Thus the edge directions increase strictly once around the circle and every turn is in `(0,pi)`. Together with the two separated monotone walls and the two exterior caps, this makes `P_L` simple and strictly convex.

The only unit pairs among polygon vertices are consecutive edges: any nonconsecutive same-wall pair has horizontal separation at least `2(1-1/(1250L^2))>1`, and opposite walls are at vertical separation at least `48/25`. At a normal pin `q_i=p_i+n_i`, its supporting normal gives `|q_i-p_j|^2>=1+|p_i-p_j|^2>=2` for every other polygon vertex. For distinct normal pins, supporting-normal monotonicity gives

```text
|q_i-q_j|^2 >= |p_i-p_j|^2+|n_i-n_j|^2 > 1.
```

Each tip pin has unit distance to its own apex, sibling distance `6/5`, and horizontal separation at least `27/25>1` from every other polygon vertex on that side; points on the opposite side are farther. A wall-end normal is within `1/(50L)` of the corresponding vector `(±3/5,±4/5)`, so its pin has absolute height at least `7/4`; its vertical separation from the nearest tip pin is at least `23/20`. Every other normal pin is based at least one wall edge away, giving horizontal separation from a nearby tip pin at least `27/25-1/(1250L^2)>1`; all opposite-side cases are farther. These cases exhaust all pairs. Thus the actual contact graph is exactly the polygon cycle plus its `m+2` pendant pin edges; it is triangle-free and has no isolates.

The straight-line contact embedding has no crossings. Normal spokes from distinct polygon vertices cannot intersect: if `p_i+s n_i=p_j+t n_j` with `s,t>0`, then

```text
(p_i-p_j) dot (n_i-n_j)=-(s+t)(1-n_i dot n_j)<0,
```

while the two supporting-normal inequalities imply this dot product is nonnegative. The normal directions at distinct strictly convex vertices are distinct. Tip spokes lie between heights `-3/5` and `3/5`, while bottom and top normal spokes stay below `-24/25` and above `24/25`; left and right tip-spoke groups are horizontally disjoint. Hence the only bounded face of the embedded contact graph is `P_L`.

Every normal pin is uniquely exposed by its outward normal: the source lies in `P_L+B(0,1)`, and that pin attains the corresponding support value. The four tip pins are uniquely exposed by the stated functionals `-x±y/10` and `x±y/10`, using the non-tip rectangle bounds. Every free vertex is a strict positive convex combination of its noncollinear contact neighbors by the equilibrium below, so it is interior to the full source hull. The pins are exactly the hull vertices.

### Positive pinned equilibrium and rigidity

At each nonapex free vertex, let `a_i,b_i` be signed unit half-angle vectors for the incoming and outgoing cycle edges, chosen with half-angle increment in `(0,pi/2)`. Set `n_i=-J(a_i b_i)` and `beta_i=2 det(a_i,b_i)>0`. The exact identity `u_i-u_{i-1}=-beta_i n_i` balances the two unit cycle contacts, each of weight one, against the normal spoke of weight `beta_i`. At either apex, the cycle-force sum is `∓(14/25,0)` and the two tip-spoke weights `7/20` balance it. Thus every free vertex has a strictly positive equilibrium on all its actual contacts, with noncollinear contact directions.

For pinned infinitesimal rigidity, the two pin rows at the left apex are independent. Traverse the cycle from that apex, omitting the final closing edge. At each new free vertex, keep its incoming cycle row and one spoke row. Their two-coordinate determinant is nonzero: at a normal spoke it is `-cos(turn_i/2)`, and at the right apex the chosen tip spoke gives `-3/5`. This produces a block-triangular `2m`-row minor with nonzero determinant, so the pinned contact matrix has rank `2m`.

There is also exact finite rigidity with these pins fixed. For any finite displacements `x_i` preserving all old unit contact lengths, sum each squared-length equation against its strictly positive contact weight. Equilibrium cancels all linear terms and leaves

```text
sum_{contact ij} w_ij |x_i-x_j|^2=0.
```

Every term is nonnegative, so every contact displacement difference is zero. Each free vertex has a positive spoke to a fixed pin, hence every free displacement is zero. This is global rigidity of the pinned contact framework only; it does not fix the pins as actual diameter endpoints or make the source globally optimal.

### Diameter, area and tail

The four tip pins have two opposite-height cross-tip pairs of squared length

```text
D_L^2=(X_L+54/25)^2+36/25.
```

Using the non-tip rectangle and the tip-to-nontip coordinate bounds, the gaps from this value to every non-tip/non-tip and tip/non-tip squared-distance upper bound are respectively

```text
(47/25)X_L-27661/2500,
(47/50)X_L-34069/10000,
```

both positive for `L>=12`. The other tip pairs are shorter. Therefore these are the only two diameter pairs and there are exactly four diameter endpoints, all pins. Also `D_L/L->1`. The polygon lies in a rectangle of width `X_L+14/25` and height `49/25`, so its area is `O(D_L)`; the full source lies in a rectangle of width `X_L+54/25` and constant height `99/25`, so its convex-hull area and perimeter are also `O(D_L)`.

The cycle is the only bounded face and has degree and perimeter `m=2L+4`. For every fixed finite `M`, eventually `m>M`, so

```text
T_M(A_L)=m-4=2L,    T_M(A_L)/D_L -> 2.
```

Thus even with a strictly positive unloaded equilibrium, extreme pins, full pinned infinitesimal and finite contact rigidity, and exceptional-face area `O(D_L)=o(D_L^2)`, the face-degree defect tail need not be `o(D_L)`.

The source is not a global minimizer. With `n=4L+10` points, a unit square-grid subset of a `ceil(sqrt(n))` square has squared diameter `<2n=8L+20<L^2<D_L^2` for `L>=12`. Also, all but four pins are contact leaves without a diameter row, so they cannot balance in a positive full-source KKT equilibrium. The example therefore does not refute any conclusion requiring the canonical global minimizer, full-source positive KKT stress, actual loaded-pin conditions, disk-like hull, or quadratic rhombus population. It is not a Level I counterexample.

## Certificate and hostile checks

The frozen verifier uses exact `Fraction` arithmetic and was independently rerun. It checked all `19,372` source pairs in the four `L=12,16,24,32` packets; exact contact and diameter sets; strict pin hull membership; convex face orientation; positive free-vertex equilibrium; explicit pinned minors; and same-cardinality square-grid competitors. These finite packets do not prove the all-even-`L` construction or the limit. The universal inequalities and limit are reconstructed analytically above.

I checked the lower bounds at the weakest size `L=12`, where both diameter-separation margins are positive and increase with `L`; the same-wall two-edge gap is greater than one uniformly for every `L>=12`. The normal-pin separation uses supporting geometry rather than finite sampling. Potential hidden scope failures are excluded explicitly: there are no contact isolates, the pins are all hull vertices but not all loaded, the example is nonglobal, the fixed-pin theorem is not a source-motion theorem, and the area estimate supplies no capacity claim.

| Candidate | Verdict | Canonical disposition |
| --- | --- | --- |
| Positive pinned rigidity plus small exceptional-face area forces vanishing high-degree tail | REGRESSION VALID | Promote `C-POSITIVE-PINNED-RIGIDITY-FACE-TAIL-REGRESSION` |
| Regression refutes the canonical loaded Type-II tail obligation | REJECTED SCOPE | Actual diameter loading, full-source KKT, disk geometry and global optimality are absent |

The regression narrows the required proof inputs but does not reduce the canonical C-II frontier. C-I remains closed; C-II and Level I remain open.
