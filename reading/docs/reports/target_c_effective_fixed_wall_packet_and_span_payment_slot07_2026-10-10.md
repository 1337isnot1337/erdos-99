> Generated reading edition · [exact source](../../../docs/reports/target_c_effective_fixed_wall_packet_and_span_payment_slot07_2026-10-10.md) · source SHA-256 `dc562b728b3a574730e0a71eaebd996dbebc85eb2bc01f9f2ce375c771a01b90`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4944383024AA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II: an effective discrete packet and forced wall-span contraction

**Worker:** 07. **Date:** 2026-10-10. **Start:** `35f8c0c6c46b72b0455dfddaf29fbf8650087613`, based on main `ab6dd3336f9f8d440f2bada76edb32153391cddc`, state `2026-10-10.audit.234`.

**Classification:** proved candidates awaiting independent audit; conditional reduced-source descent; regression against monotone grid restoration. No canonical promotion, C-II closure, or Level I resolution.

## 1. Exact chain

```text
actual labeled chart within an explicit quadratic phase tolerance
 + actual simple unit boundary
 -> discrete one-vacancy interior packet with that actual boundary fixed
 -> all packet-involving lower and upper pairs are strict in the full source
 -> if the original interior hits every normalized stress, reduced strict D descent
 -> exact source stress forces contraction of a row/column wall span
 -> a full-cardinality endpoint needs a nonlinear restoration or another compartment.
```

The new positive bridge is a discrete fixed-boundary statement. It is compatible with the preceding near-coherent pinning regression, which forbids a continuous motion from its old punctured source. The explicit tolerance is quadratic in the rhombus separation from the triangular endpoints. The new negative bridge is an exact elimination of actual interior equilibrium, giving physical wall-span obligations rather than an assumed expanding container.

Canonical dependencies: Audit 195 `C-OBLIQUE-ONE-VACANCY-STRICTIFICATION` supplies the two-stage velocity pattern; Audit 88 `C-NONCONTACT-WALL-STRICT-SHIELD` supplies exterior safety; Audit 87 `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE` supplies reduced strict descent. The stress identity below is proved directly on the full source. The finite diameter-star fixtures also check Audit 172's exact chain regime, without importing an unreviewed claim.

## 2. Effective reference packet

Fix integers `m,n>=3`, `L=m+n`, `M=max(m,n)`, unit vectors `u=(1,0)`, `v=(c,s)`, with `s>0`, `|c|<1/2`, and put

```text
h=1-2|c| in (0,1], s=sqrt(1-c^2)>=sqrt(3)/2,
T={i u+j v:0<=i<=m,0<=j<=n}, K=conv(T),
I={i u+j v:0<i<m,0<j<n}, W=T\I,
g=h^2/(10^7 L^3), eta=h^2/(10^8 L^3).
```

Choose any interior vacancy `(a,b)`. Use the exact Audit 195 first-stage velocities on its punctured row and column:

```text
w_(i,b)=-(i/a)Jv for i<a,
w_(i,b)=((m-i)/(m-a))Jv for i>a,
w_(a,j)=(j/b)Ju for j<b,
w_(a,j)=-((n-j)/(n-b))Ju for j>b.
```

All other labels and W have velocity zero. Take first amplitude `d=h/100`. All these velocities have norm at most one. A nonbasis old grid pair has distance at least `sqrt(1+h)>=1+h/3`, so its distance after this stage is at least `1+h/3-2d>1+h/4`.

Every old unit pair touching a first-stage mover becomes strict. For a contact perpendicular to the mover, its squared-distance gain is at least `d^2/M^2`; the smallest nonzero coefficient is at least `1/M`. For a contact along the punctured row or column, its positive radial derivative is at least `s/M`, and its gain is also at least `d^2/M^2`. No old unit pair joins a row mover and a column mover across the missing intersection. Thus every pair touching those movers has distance at least `1+d^2/(3M^2)`, using `sqrt(1+z)-1>=z/3` for `0<=z<=1`.

For the remaining four blocks use the canonical dual-basis velocities

```text
u*=(1,-c/s), v*=(0,1/s),
z_ij=s_x I_i u*+s_y J_j v*,
```

where the signs point away from the adjacent outer sides and `I_i,J_j` are the positive distances in indices from those sides. Their norm is at most `B=2L`. Take second amplitude

```text
t=d^2/(100 M^2 B), so the maximum second displacement is d^2/(100M^2).
```

Already strict pairs lose at most twice that displacement and remain above `1+d^2/(4M^2)`. Original nonbasis pairs remain above `1+h/8`. Each remaining old unit pair has second-stage radial derivative exactly one, and therefore endpoint distance at least `1+2t/3`. All contacts between different blocks pass through the already released row or column; there is no omitted stationary unit interface.

The endpoint packet Q has `|I|-1` sites. Every internal pair and every packet-to-reference-wall pair has distance at least

```text
1+2t/3=1+h^2/(3,000,000 M^2 L) >= 1+g.
```

All packet sites remain more than `1/2` from the geometric boundary of K. Originally that distance is at least s; each site moves in only one of the two stages by at most `d` or `d^2/(100M^2)`, both at most `1/100`. These estimates check the finite endpoint and its complete reference pair set. At a triangular endpoint h=0 the strict margin disappears; neither endpoint is included.

## 3. Actual-boundary discrete theorem

Let A be a finite actual unit-separated source. Suppose it contains a specified bijective labeled copy `T'={t':t in T}` with `max_t |t'-t|<eta`. Require that its cyclic matched boundary W' is a simple polygon F' and every consecutive boundary edge has actual length one. No coherence of the interior train directions is required. A unit-rhombus separable chart is one admissible special case.

**Theorem P_eta (proved candidate).** Delete the one matched vacancy, replace the other matched interior labels by Q, and keep W' and every original exterior label fixed. The resulting `|A|-1` points are unit-separated. Every packet-involving lower pair is strict, and every packet-involving upper pair is strictly below `D=diam(A)`. This is a discrete replacement; a continuous fixed-boundary motion is not asserted.

**Actual wall clearance.** Moving a guard by less than eta reduces a packet-to-guard distance by less than eta, so these distances exceed `1+g-eta>1+9g/10`. The packet's internal pairs retain the reference margin.

**Containment.** Match the reference and actual boundary edges linearly. Their straight homotopy stays within eta of the corresponding reference edges. Every point of Q is more than `1/2` from the reference boundary, so none meets this homotopy. Its winding number remains one. Since F' is simple, Q is strictly inside F'. The same argument places all matched interior source labels inside F'.

**No discarded interior labels.** Each reference unit parallelogram is split along its shorter diagonal. On either triangle the barycentric identity gives nearest-reference-site radius at most `q_0=sqrt(2/3)<1`. Every point of F' lies in `conv(W')`, which lies within eta of K by matched convex combinations. Its distance to some actual site of T' is therefore at most `q_0+2eta<1`. Any additional original source label inside F' would violate source separation. Thus the original interior population is exactly `|I|`; replacing it by `|I|-1` accounts for every label and exactly one deletion.

**Full exterior lower checks.** The retained actual source outside F' is unit-separated from W'. Q is strictly clear from W', whose sides are unit. The canonical strict wall shield checks all packet/exterior pairs, with distance greater than `sqrt(3)`. No Oler allowance is interpreted as an insertion site.

**All upper checks.** Q lies in the open polygon interior, hence in `int(conv(A))`. Every upper pair involving Q is strictly below D by the interior-hull argument: an interior point at distance D from a hull point could be extended slightly along that ray inside the hull to exceed its diameter. All fixed pairs stay unchanged. All exterior contact isolates stay fixed; all matched interior labels, including any original isolates, are retained and relocated except the one counted deletion.

For a separable actual chart `x_ij=x_00+sum_{r<=i}u_r+sum_{r<=j}v_r`, if each u_r differs in angle from u by at most zeta and each v_r from v by at most zeta, matched coordinate error is at most `L zeta`. Thus

```text
zeta < h^2/(10^8 L^4)
```

is an explicit sufficient phase-flatness condition. It is stronger than an undifferentiated `O(1/D)` phase interval. No theorem extracting this condition, consecutive physical cells, or a stress-transversal interior from a canonical source is claimed.

## 3.1. A stronger actual-unit-grid endpoint at linear tolerance

The previous theorem permits arbitrary near-reference interior coordinates. If all actual basis-grid edges are unit contacts, a different construction improves the tolerance and the displacement order.

Keep the reference definitions, and choose a positive number

```text
0<epsilon<h/(10^4 L), max_t |t'-t|<epsilon.
```

Assume every actual pair `(i,j),(i+1,j)` and `(i,j),(i,j+1)` in T' has distance one, and the matched cyclic unit boundary is simple. Use the same velocities as Section 2, but start at the actual coordinates and take

```text
d=16 M epsilon, B=2L, t=d^2/(100M^2B).
```

**Theorem P_unit (proved candidate).** A discrete first jump of amplitude d on the punctured row and column, followed by the second block displacement of amplitude t, gives `|I|-1` sites inside the actual polygon. Every internal and packet-to-actual-wall distance exceeds `1+t/3`. It leaves the actual boundary and every exterior source label fixed, retains the full lower/upper conclusions of P_eta, and displaces each retained interior label by at most `16M epsilon`. No first-jump path is asserted.

**Proof of the first jump.** An actual basis contact vector differs from its reference vector by less than `2epsilon`. Nonbasis source pairs have distance at least `sqrt(1+h)-2epsilon`; their relative first displacement is at most `2d`, and `d<h/625`, so these pairs remain above `1+h/4`.

For an old unit contact perpendicular to a single row or column mover, write its signed nonzero coefficient as k, with `1/M<=|k|<=1`. The reference radial work vanishes, while the actual radial work is at least `-2epsilon |k|`. Its exact squared-distance gain after the jump is consequently at least

```text
d^2 k^2-4d epsilon |k| >= (3/4)d^2 k^2 >= 3d^2/(4M^2),
```

because `d|k|>=16epsilon`. For a contact along the punctured row or column, the coefficient difference has magnitude at least `1/M`; its actual radial derivative has the same positive sign as the reference derivative and magnitude at least `(s-2epsilon)/M`. Its squared gain is at least `d^2/M^2`. No basis contact joins a row mover to a column mover across the absent intersection. Thus every pair touching a first-stage mover is now strictly longer than one, with distance gain at least `d^2/(4M^2)` on old unit pairs. Unlike a first-order proof, the positive quadratic term pays the possibly negative actual radial term.

**Proof of the second displacement.** It moves each untouched block label by at most `Bt=d^2/(100M^2)`. Earlier strict distances lose at most `2Bt` and remain above `1+d^2/(5M^2)`. Every remaining old unit pair has reference block radial derivative one. Its actual derivative differs by at most `4epsilon B<1/2`, so its squared gain is greater than t and its distance gain is greater than `t/3`. Nonbasis pairs stay above `1+h/8`. These bounds exceed the claimed minimum margin. Each retained label moves in just one stage; `Bt<d`, so its displacement is at most d.

The actual starting interior labels are at least `s-epsilon` from the reference boundary and the endpoint displacement is at most d. They stay more than `1/2` away. The same boundary homotopy, covering bound, strict wall shield, and interior-hull argument from Section 3 give actual containment, exact label accounting, every exterior lower bound, and every full-source upper bound. This proves the discrete endpoint. It is not necessary to integrate the possibly closing first jump.

For a separable actual train chart, the sufficient angle variation is now `zeta<h/(10^4 L^2)`, since coordinate error is at most `L zeta`. This is linear in h, whereas P_eta's tolerance is quadratic. Neither theorem supplies an actual canonical chart or its all-stress transversal.

## 4. Stress elimination on the actual coherent source

**Disconnected-packet corollary (proved candidate).** For every fixed `m,n>=3` and strict rhombic angle, the preceding report's positively pinned punctured train grids can be chosen within either explicit tolerance, while retaining a strictly positive deformation. Their old punctured interiors are locally isolated with the actual boundary fixed, yet P_eta and P_unit give different strictly feasible packets of the same punctured population behind that same fixed boundary. P_unit's displacement is linear in the actual coordinate-error bound and tends to zero with the deformation; the isolation radius from the preceding report also tends to zero. Positive pinned equilibrium and full column rank therefore do not imply global uniqueness of a punctured filling. No continuous path from the old puncture is supplied. The verifier checks the positive pinned equilibrium and both strict replacements on the same 48 actual fixtures.

This also gives a sharp order for the finite jump threshold of that pinned family. Write its positive train deformation as e, let `N=(m-1)(n-1)-1` be the moving population, and require `4sin(e)<h/(10^4 L)`. Its coordinate error is at most `4sin(e/2)<4sin(e)`. In the preceding report's positive stress, `alpha=sin(e)/s` is the smallest edge weight; the total weight W is at most `2L^2`. Indeed its alpha term is at most `(m^2+n^2)/2`, its gamma term at most `4mn<=L^2`, and its remaining term `L-4<=L^2/2`. The proved isolation radius therefore satisfies

```text
rho=s alpha/(2N L W) >= sin(e)/(4N L^3).
```

The infimum Euclidean displacement norm over all distinct labeled feasible punctured fillings with the old boundary fixed is consequently at least that lower bound. P_unit with `epsilon=4sin(e)` supplies a distinct strictly feasible filling at norm at most `64M sqrt(N) sin(e)`. Thus for each fixed frame this threshold is bounded above and below by positive constants times `sin(e)`. No uniform isolation radius survives the coherent limit; at e=0 the canonical continuous vacancy release is restored. The bounds concern punctured fillings, not full-cardinality endpoints.

Now let the original actual source contain the exact coherent T. It has no extra labels in K by the cover argument. Every original interior label is unloaded. Its only actual unit neighbors are its four basis neighbors: the wall shield's weighted-square proof with non-strict guard distances gives distance at least `sqrt(3)` to every exterior non-wall source label, and `|c|<1/2` excludes nonbasis grid contacts. Explicitly, at the first exit z across a unit wall side, both squared distances to z are at least `1-1/4=3/4`; their lengths add. The strict endpoint shield remains the promoted Audit 88 statement.

Let `(alpha,beta)` be any normalized nonnegative full-source equilibrium stress, with `sum_H beta=1`, and let `R=A\I`. Equilibrium at each interior point and independence of u,v force the two horizontal contact weights to agree and the two vertical contact weights to agree. Therefore each interior horizontal row has one constant channel weight `r_j>=0` on its entire m-edge chain, and each interior vertical column one constant channel weight `q_i>=0` on its entire n-edge chain.

For any velocity field on the actual retained R, define

```text
X_j=u dot(eta_(m,j)-eta_(0,j)), 1<=j<=n-1,
Y_i=v dot(eta_(i,n)-eta_(i,0)), 1<=i<=m-1.
```

**Theorem S (proved candidate).** The exact full-source stress identity is

```text
sum_j r_j X_j + sum_i q_i Y_i
 = sum_H beta_pq (p-q) dot(eta_p-eta_q)
   -sum_(C with both endpoints in R) alpha_pq (p-q) dot(eta_p-eta_q).
```

To prove it, apply original force balance to any extension of eta to the interior labels. Each interior contact chain has constant weight, so its radial work telescopes to its endpoint span; all interior velocities cancel. All diameter endpoints belong to R. Every other contact belongs to the displayed retained-contact sum. This includes every original source label; no core affine-kernel theorem is extended to isolates.

Suppose eta opens all retained contacts and strictly shortens every original diameter pair. With

```text
kappa=min_H[-(p-q) dot(eta_p-eta_q)]>0,
G=sum_j r_j+sum_i q_i,
```

the identity gives `sum_j r_j X_j+sum_i q_i Y_i<=-kappa`. Hence G>0 and at least one positively weighted physical span is negative. Moreover original equilibrium tested against the actual coordinates gives `sum_C alpha=D^2`; thus `min(m,n) G<=D^2` and at least one span obeys

```text
min of the positively weighted X_j,Y_i <= -kappa min(m,n)/D^2.
```

No uniform lower bound for kappa is asserted. If the interior hits every normalized stress, the strict packet kills all stresses supported outside it, and Audit 87 produces such a retained strict direction. The contraction is therefore compulsory for that legitimate reduced descent, rather than evidence that the packet cannot be made.

## 5. Why affine grid restoration fails at that descent

For the full coherent interior, a weak first-order lower-feasible extension of a given wall velocity exists exactly when every X_j and Y_i is nonnegative, assuming the prescribed wall velocities already satisfy the wall contact rows. Indeed the independent scalar projections `u dot w_ij` must be nondecreasing on each horizontal chain, and `v dot w_ij` on each vertical chain. Telescoping proves necessity. For sufficiency, interpolate the first projection between its two row endpoints and the second between its two column endpoints, then reconstruct `w_ij=(u dot w_ij)u*+(v dot w_ij)v*`. Strict span inequalities give strict contact derivatives. These are simultaneous scalar constraints on the same physical labels; the dual basis makes the two projections independent.

Theorem S makes this extension impossible along every retained strict diameter descent of the stress-bearing original source. Opening the actual wall's individual unit edges does not imply widening every interior cross-span. A valid restoration must use finite nonlinear rearrangement, a different compartment, or an independently funded packet; neither a monotone interpolation nor all wall-edge first derivatives supplies it.

This is a first-order restoration obstruction. It is not a proof that a disconnected finite equal-cardinality endpoint is impossible. The source-dependent finite core isolation result from the earlier report remains a separate constraint.

## 6. Exact checks and exceptional-chain diagnostic

The verifier `research/verify_target_c_effective_fixed_wall_packet_slot07_2026_10_10.py` tests perturbed actual unit-rhombus charts inside the explicit tolerance, with all actual boundary positions fixed, exterior unit neighbors, and retained isolates. It checks all old and new source pairs, winding/containment, and the exact margin bounds.

Its nonvacuous stress diagnostic uses a complete coherent `3 by 3` chart plus a long unit chain extending both ways from interior row one. The unique actual diameter pair is the chain's two endpoints, of integer diameter D. Weight D on every chain contact and beta one on that endpoint pair gives exact normalized equilibrium; all other contact weights are zero. The strict packet kills this stress. An explicit retained velocity opens every retained unit contact and shortens the diameter, while contracting the chart's stressed row span. Exact quadratic segment minima and a rational finite step certify the whole reduced motion.

Exact output: 48 actual perturbed fixtures certify 49,328 old-source pairs, 14,440 reference-margin pairs, 47,392 endpoint pairs, 32,720 strict packet-involving pairs, 928 unit wall edges, 768 packet winding tests, 48 retained isolates, 1,808 positive pinned weights, and 768 pinned equilibria. Eight star-chain fixtures certify 6,240 old-source pairs, 320 full-source equilibria, 288 strict retained-contact derivatives, 5,928 whole-segment pair minima, 6,240 restored full-source pairs, and 320 old-bay pair checks. All calculations use exact rational or `Q(sqrt(15))` arithmetic. These counts certify only the finite fixtures; the universal tolerance, arbitrary-exterior checks, and stress identity are analytic proofs.

P_unit adds 28,880 actual-grid margin checks, 47,392 full-source endpoint pair checks, and 32,720 strict packet-involving checks on those same fixtures. Each of the 48 positively pinned examples has an exactly certified first-jump straight-segment violation. Another 108 varied-train fixtures, including rational angles close to both triangular endpoints and vacancies at three distinct positions, certify 36,996 original source pairs, 106,632 endpoint pairs, 73,620 strict packet pairs, and 64,980 margin pairs. Their first-direction rotation scale is `h/(100000L^2)`, closer to the explicit linear tolerance; every old unit basis contact, every simple unit wall, every actual exterior label and isolate, and all upper constraints are checked. They too are explicitly nonglobal.

For these diagnostics an explicitly checked separate empty bay supplies one strict added point inside the moved retained hull, restoring full cardinality with diameter below the original D. The bay was already a strict spare site in the old source; these fixtures are therefore outside canonical contact minimality and are also certified nonglobal by explicit equal-population grid competitors. Their positive core is only the collinear chain and fails canonical mixed rank. This validates full pair bookkeeping and the boundary-work identity; it does not extract a bay from a canonical survivor or settle the restoration obligation.

## 7. Failed mechanisms and exact next implication

Three mechanisms were examined. A packet uniformly applicable at the triangular endpoint would give a finite rearrangement of a one-vacancy triangular packing when its exterior lattice is fixed; this enters a separate solidity problem. The original author source [Connelly and Dickinson, Section 1.3](https://pi.math.cornell.edu/~connelly/Connelly-Dickinson-V3.pdf) states the solidity conjecture and distinguishes finite rearrangement from continuous jamming. This is a near miss, not an imported impossibility theorem. Audit 83's source already records an unpromoted flat-window/solidity equivalence; no duplicate theorem is claimed here.

The second mechanism, expansion of every old wall edge followed by monotone interpolation of the missing grid, is killed by Theorem S's exact negative span. The third, discrete packet preparation, succeeds at the stated quadratic tolerance for arbitrary matched interiors and at linear tolerance for actual unit-basis grids. It retains every actual exterior label. Its remaining deficit is one.

**Next exact theorem:** in a sufficiently large canonical survivor with a supplied eligible chart whose interior hits every normalized stress, construct a finite restoration of its single vacancy after the forced contracting-span descent, checking every source lower pair and every upper pair below the original D. The explicit nonglobal bay does not furnish this canonical payment. Global chart extraction, exceptional loaded-only stress faces, and all remaining full-core/container branches stay open.
