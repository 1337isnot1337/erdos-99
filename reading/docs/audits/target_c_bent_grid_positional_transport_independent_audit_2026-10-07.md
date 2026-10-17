> Generated reading edition · [exact source](../../../docs/audits/target_c_bent_grid_positional_transport_independent_audit_2026-10-07.md) · source SHA-256 `cc759acabee7765577bcb11ab91ba928173606adffb9b5e1b6a3a82f5950a766`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-710FDD6028F8","canonical":false,"claim_ids":["C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION"],"claim_statuses":{"C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"regression","target":"target-c"} -->
# Independent audit: bent-grid positional transport regression

Date: 2026-10-07. Audit base: `10e5859453fda7f4b16a5932200e72805f943c0f`, state `2026-10-07.audit.91`; Target C C-II and Level I remain open. Frozen source: PR #722, branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. The source branch still had this exact tip after the proof audit. Source report SHA-256 `9d965182d76d12ad8a33b3b6cf896b6154ae71b3645c1108d6def91d85af6f2a`; verifier SHA-256 `30e235b2ed3b110678655c6139d2448bed1c40f70dbdb87b84d74254c0d2f8b4`.

## Verdict

**REGRESSION VALID — promote** `C-BENT-GRID-REDUCED-POSITIONAL-TRANSPORT-REGRESSION` at the reduced-input scope below.

For every even `M>=8`, the source report gives a triangle-free rhombic contact grid with `M^2` cells, diameter comparable to `M`, phase span below `1/M`, positive pinned contact equilibrium, full pinned contact rank, and total positive angular and area excess each below `2M`. Nevertheless, its bottom row stays a fixed positive distance from every single affine lattice whose inverse basis operator norm is uniformly bounded. This refutes deriving a single-lattice physical-position approximation for the whole grain from those reduced properties alone.

The boundary pins are not shown to be actual diameter endpoints. The family is not shown globally minimum-diameter. The result does not refute positional covers of the actual canonical loaded set, does not refute bounded multiple-lattice covers, and implies no C-II or Level I counterexample. It is a strategy regression against an angular-coherence-to-physical-transport shortcut.

## Exact statement

For each even `M>=8`, define

```text
t_i=i/(2M^2),
u_i=((1-t_i^2)/(1+t_i^2), 2t_i/(1+t_i^2)),
U_0=0, U_i=sum_{a<i}u_a,
v=rotation of (1/2,sqrt(3)/2) by 2 atan(1/M),
p_ij=U_i+jv, 0<=i,j<=M.
```

The complete unit-contact graph of these `(M+1)^2` points is the rectangular grid; every other pair is strictly farther than one. Thus the source is triangle-free and consists of `M^2` strict unit rhombi. If `D_M` is its diameter, `M/2<=D_M<=2M`. The horizontal direction angles have spread below `1/M`. The sum of the positive angular excess above `pi/3` and the total rhombus-area excess above `sqrt(3)/2` are each strictly between zero and `2M`.

Pin every boundary vertex. There are strictly positive weights on all grid edges that give equilibrium at every unpinned vertex, and the pinned contact-flex kernel is zero.

Now let `L=a+T Z^2` be any affine lattice with invertible `T` and `||T^(-1)||<=K`. If `M>2K`, then

```text
max_{0<=i<=M} dist(U_i,L) >= min(1/(8K),1/20).
```

The lattice, its orientation, and its translate may vary with `M`. The same lower bound applies to the error of any one-lattice approximation of the whole source, because its bottom row is a subset.

## Independent proof reconstruction

### Contact graph and grain bounds

Write `v_0=(1/2,sqrt(3)/2)`. For index differences `a,b`, the displacement between source points differs from `a(1,0)+b v_0` by norm at most `(|a|+2|b|)/M`. Since

```text
|a(1,0)+b v_0|^2=a^2+ab+b^2 >= (a^2+b^2)/2,
```

the relative error is at most `sqrt(10)/M`. The integer quadratic form is one exactly on the four horizontal/vertical basis steps and the two short-diagonal steps `(1,-1),(-1,1)`; otherwise it is at least three. For `M>=8`, all those other index differences have length at least `sqrt(3)*(1-sqrt(10)/M)>1`. Basis steps are exactly unit contacts. A short diagonal has vector `u_i-v`; its angle is strictly greater than `pi/3`, so it too is strictly longer than one. This checks every pair, not only adjacent rhombus vertices.

The projection onto a normal to `v` is strictly increasing with the column index, so the rhombi form a simple disk. The displacement from `p_00` to `p_M0` has horizontal component greater than `M/2`, giving the diameter lower bound; every point difference has norm at most `M+M`, giving the upper bound. The angle range is below `1/M`. Summing each cell's positive determinant excess over the regular-hexagonal value gives a quantity below `2M`; the same Lipschitz estimate for sine bounds the total angular excess by `2M`.

### Positive pinned equilibrium and full pinned rank

Let `n=(v_y,-v_x)`, so `n dot v=0` and `n dot u_i>0`. Define `alpha_i=1/(u_i dot n)`. The vector `alpha_i u_i-alpha_(i-1)u_(i-1)` is parallel to `v`; write it as `c_i v`. For interior columns put `B=1+M max_i |c_i|` and give the vertical edge from `(i,j)` to `(i,j+1)` weight `beta_ij=B-j c_i`. These are positive. Horizontal force at an unpinned vertex in column `i` is `c_i v`; vertical force is `(beta_ij-beta_i,j-1)v=-c_i v`. Equilibrium follows. Weights on vertical edges in the two pinned boundary columns may be arbitrary positive values.

For a pinned flex, the vertical contact equations make the `v`-component constant in each column, and the pinned top and bottom endpoints force it to zero. Every velocity is therefore a multiple `lambda_ij n`. The horizontal equations give `(u_i dot n)(lambda_(i+1,j)-lambda_ij)=0`; positivity makes `lambda` constant along each row. Pinned row endpoints then force every velocity to be zero.

### Uniform single-lattice obstruction

Distinct vectors in `T Z^2` are separated by at least `1/K`, since `|Tz|>=|z|/||T^(-1)||>=1/K` for every nonzero integer vector `z`. Suppose every bottom-row point `U_i` is within `epsilon` of a lattice point `a_i`. The increments `z_i=a_(i+1)-a_i` are lattice vectors and satisfy `|z_i-u_i|<=2 epsilon`. Since `|u_i-u_j|<1/M`,

```text
|z_i-z_j| <= 4 epsilon + 1/M.
```

If `M>2K` and `epsilon<1/(8K)`, the right side is strictly below `1/K`; all increments are equal. Hence `a_(M/2)=(a_0+a_M)/2`.

The rational vertical coordinates satisfy

```text
(U_M)_y/2-(U_(M/2))_y >= 1/8-1/(4M^2) > 1/10.
```

Indeed `(u_i)_y=(i/M^2)/(1+i^2/(4M^4))` differs from `i/M^2` by at most `1/(4M^3)`, and the half-sum minus first-half sum for `i/M^2` is exactly `1/8`. The three approximation errors would bound this midpoint residual by `2 epsilon`, so `epsilon>1/20`. Combining the two strict bounds proves the displayed lattice error lower bound.

## Certificate and limits

I inspected and ran `research/verify_target_c_bent_grid_transport_2026_10_05.py`. Its `Fraction`-based representation of `Q(sqrt(3))` exactly checks every source pair, equality on grid contacts, strict noncontacts, contact counts, the rational bow bound, and `0<E4<2M` for `M=8,12,16`; the registered default run checks 59,052 pairs. I additionally ran the same checker at `M=10` (7,260 pairs). There are no floating tolerances. This supports only those finite arithmetic checks. The infinite family, positive equilibrium, pinned rank, and uniform lattice obstruction are supplied by the analytic derivations above, not by the script.

The certificate does not verify actual diameter loading, global optimality, or a failure of multiple-lattice transport. In particular, boundary pins are not silently identified with canonical loaded endpoints. The precise implication chain is: reduced grain geometry plus pinned stress/rank and phase control does not ensure a single-lattice positional approximation of the physical grain; therefore any use of Audit.91's conditional actual-loaded-endpoint cover exclusions must independently establish positional approximation for actual loaded endpoints. No such derivation is provided here. C-II's face-coupled finite-move and arbitrary-container capacity obligations remain unchanged.
