# Linear Oler slack does not extract the collective-refill deficit

**Classification:** unreviewed exact regression and source-extraction obstruction.  
**Baseline:** `7d0a450fe66991036541023f95c44c064a04b6a8`.  
**State / priority / catalogue:** `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.  
**Target status:** Level I open; C-I closed; C-II open.
**Assignment:** producer for `frontier-target-c-capacity-collective-refill-20261018`.

Contributor: OpenAI Codex (GPT-6 Luna, xhigh), homelab-06. This AI session reconstructed the two
frozen predecessor statements, derived the ledger below, and wrote the exact
finite checker. No independent audit has been performed. The two predecessor
reports and their attribution remain intact. The contribution is first-party
research compatible with Apache-2.0; no external material is copied.

## Exact question and result

The two-side collective-refill theorem applies to an actual simple unit wall
that is within

\[
\eta_L=\frac{3}{10^6L^{14}(L+1)}
\]
of an ordered oblique rectangular grid wall, with `L=m+n`, `m,n>=4`. This
specific cardinality comparison is funded only if the full enclosed source population has
deficit at least `J=m+n-1`: if `K=(m-1)(n-1)` is the strict target capacity and
`z` is the number of **all** source labels inside the wall, the required
condition is `K-z >= J`. Then deleting the `z` interior labels and `J` wall
labels is funded by `z+J<=K` target positions. All source labels, including
isolates, must be counted; every new lower pair and every old/new diameter
upper pair must be checked.

This package tests whether scale, an exact near-triangular wall, and positive
linear all-label Oler slack alone force that deficit. For every integer
`m>=7`, set

\[
d_m=m^2-6m-3,\qquad
c_m=\frac{\sqrt{d_m}}{2m},\qquad
s_m=\frac{\sqrt3(m+1)}{2m},\qquad
u=(1,0),\quad v=(c_m,s_m),
\]
and take the full source
\[
A_m=\{iu+jv:0\le i,j\le m\}.
\]
Since `d_m+3(m+1)^2=4m^2` and `0<d_m<m^2`, these are unit basis vectors
with `0<c_m<1/2`; hence the angle is strictly above 60 degrees and tends to
60 degrees. The outer grid boundary is an exact simple unit-contact cycle.
Its ordered wall error is zero, which is below every positive `eta_(2m)`.

The source has `N=(m+1)^2` labels, exact unit-contact graph the rectangular
bipartite grid, and diameter squared
\[
D_m^2=m^2(2+2c_m)=2m^2+m\sqrt{d_m}.
\]
For an integer label difference `(a,b)`, squared distance is
`a^2+b^2+2ab*c_m`. Axis differences have length at least one, with equality
only for the unit steps. If `ab>0`, squared distance exceeds one. If
`ab<0`, writing `r=|a|, s=|b|` gives
`(r-s)^2+2rs(1-c_m)>(r-s)^2+rs>=1`. Thus exactly the horizontal and
vertical grid steps are contacts, so the contact graph is bipartite and
triangle-free. The quadratic norm is convex on `[-m,m]^2`; its maximum is
attained at a corner, and the same-sign corners give `D_m^2` above. Hence
every source lower and upper pair constraint is accounted for. All-label
Oler slack is exactly `m`: the hull has area
`(sqrt(3)/2)m(m+1)`, perimeter `4m`, and `N=(m+1)^2`. In particular,
`sqrt(2)m < D_m < sqrt(3)m`, so area is quadratic while perimeter and slack
grow linearly with diameter.

For comparison only, the algebraic frame quantity
`rho_m=m(m+1)-2m+1-z` also equals `m` when `z=K`. This is the same
expression as the local wall residual in the refill track, but no inactive-
chamber consequence is invoked here. The key count is still `z=K`: the
interior population deficit is **zero**. The two-side refill asks to delete
`J=2m-1` wall labels, so a same-cardinality replacement would need
`z+J=K+J` target points. Its construction provides `K`, leaving a shortfall
of exactly `J`.

The fixed-wall insertion capacity of `conv(A_m)` is zero. Split each unit
oblique grid rhombus along its shorter diagonal into two triangles. Each has
circumradius
\[
R_m^2=\frac{1}{2(1+c_m)}<\frac12.
\]
For a point `x` in one triangle with vertices `w_i` and barycentric weights
`lambda_i`, its circumcenter `o` gives
\[
\sum_i\lambda_i|x-w_i|^2=R_m^2-|x-o|^2\le R_m^2<1.
\]
At least one existing label is therefore strictly within unit distance of
every point in the full parallelogram, so no new point can be inserted while
all original labels stay fixed. This is a fixed-wall capacity result; it
does not rule out moved-wall, outside-container, or nonlocal replacements.

### Exact opened-wall endpoint at `m=n=7`

The verifier also reconstructs the two-side construction on the `m=7` member
of this family, where `c_7=1/7` and `s_7=4sqrt(3)/7`. With `L=14`,
`epsilon=1/(10L^4)`, `t=1/(100L^3)`, and
\[
\lambda_{ij}=(7-i)(7-j)(1+\epsilon(7-i)),\qquad
p'_{ij}=iu+jv-t\lambda_{ij}(u+v),
\]
it removes the lower row `0<=i<7,j=0` and left column `i=0,1<=j<7`,
retains the top/right wall, and moves all 36 interior labels. Coordinates are
stored as `(x,y/sqrt(3))` in `Q x Q`, so every squared distance is rational.
The finite checker verifies all `51 choose 2 = 1,275` lower pairs and all
1,275 upper pairs against the original `D_7^2=112`. All 1,170 pairs involving
a moved interior target are strictly longer than one; the retained wall has
14 unit contacts. Its exact new maximum squared distance is 84, so this
reduced 51-label configuration has diameter below the 64-label source's
diameter. The ledger is complete for this reduced endpoint, but it deletes
exactly 13 source labels and therefore is not a same-cardinality competitor.

### Complete ledger for this countertest

| Quantity | Exact value | Refill obligation / disposition |
| --- | ---: | --- |
| All source labels | `(m+1)^2` | Every grid label is included; none is an isolate. |
| Wall labels | `4m` | The exact unit cycle is within tolerance with error `0`. |
| Deleted wall labels | `{(i,0):0<=i<m} union {(0,j):1<=j<m}` | Disjoint sets of sizes `m` and `m-1`; the retained wall has `2m+1` labels. |
| Interior labels | `z=K=(m-1)^2` | All interior labels are counted. |
| Deficit `K-z` | `0` | Required deficit is `J=2m-1`; condition fails. |
| Wall labels deleted by two-side theorem | `J=2m-1` | Distinct source labels, disjoint from the interior. |
| Labels removed for a proposed endpoint | `z+J=K+J` | Same-cardinality endpoint needs this many new positions. |
| Strict positions supplied by the construction | `K` | Exact shortfall is `J`; these positions alone cannot restore cardinality. |
| Original lower-pair ledger | all `N choose 2` pairs | Checked exactly in the finite verifier; analytically proved for all `m>=7`. |
| Original upper-pair ledger | all `N choose 2` pairs | Checked against `D_m`; no proposed replacement endpoint exists. |
| Fixed-wall extra insertion capacity | `0` | Continuous cover proof above; does not constrain moved or nonlocal endpoints. |
| Global-minimum status | nonglobal | Same-size square grid has diameter `sqrt(2)m < D_m`. |

For the exact moved `m=7` endpoint, the complete pair ledger is:

| Category | Count | Exact disposition |
| --- | ---: | --- |
| Old source labels retained | `51` | 36 interior labels are moved; 15 top/right wall labels stay fixed. |
| Old source labels deleted | `13` | The named lower row and left column; no other source label is omitted. |
| New lower pairs checked | `1,275` | All are at least one; 1,170 pairs involving a moved target are strictly greater than one. |
| Original-diameter upper pairs checked | `1,275` | Every pair is at most `112`; exact new maximum is `84`. |
| Remaining unit contacts | `14` | All lie on the retained wall; no inserted point creates a contact or triangle. |
| Cardinality restoration still needed | `13` | This endpoint has 51 labels, while the requested comparison needs 64. |

No replacement endpoint is asserted. Thus the package does not claim a
complete lower/upper-pair certificate for a nonexistent endpoint; the exact
ledger identifies the unresolved `J` positions and the fixed-wall obstruction.

## What this establishes

The example falsifies a statistic-only extraction rule: exact wall alignment,
macroscopic diameter and area, triangle-free contact graph, and linear Oler
slack do not force the population deficit required by this refill theorem.
Merged PR #97 already supplied the zero-fixed-wall-capacity family with exact
slack `m`; this package adds the direct comparison with the two-side refill's
`L^-15`-scale wall tolerance and `L-1` population payment, plus an exact full
lower/upper pair ledger for one opened-wall endpoint. It does not duplicate
PR #102's Target A Hall-overlap result, which is outside this assignment.

The known capacity controls remain intact. The triangular two-pin theorem
blocks a universal `K+1` inference in thin frames; this package uses only the
two-side construction's stated `K` target set and, at `m=n=7`, explicitly
counts the `J=13` deletions. The universal unit-pentagon theorem blocks paying
each activation from its own pentagon interior; no pentagon interiors are
summed here. The exact opened-wall example is a collective rectangular-frame
motion, and its remaining label deficit is still unpaid.

The example is **nonglobal**, so it does not falsify a source-extraction
theorem that uses global minimality or a canonical C-II structural branch.
The two-side refill, vacancy activation and capacity predecessors remain
unreviewed. Nothing here changes the manifest or theorem state, closes C-II,
or proves that no qualifying wall can be extracted from every canonical
source. In particular, passing the exact finite checks is not an audit of
the universal geometric proof.

## Exact finite checks and falsification controls

Run from the repository root:

```sh
python research-packages/e99-pass-20261018-homelab-06/verify.py
```

The package verifier uses integer comparisons in `Q(sqrt(d_m))` for every
source pair at `m=7,8,12,24`, and rational arithmetic for every pair of the
opened `m=7` endpoint; no floating-point distances are used. It checks
the source's lower and upper pair constraints, exact contact count and
population ledger. On Python 3.14.6 it reported respectively 2,016, 3,240,
14,196 and 195,000 source pairs; deficits were zero and target shortfalls
were 13, 15, 23 and 47. This package's `VERIFY.json` declares only this
standalone checker. Additional predecessor controls were also run during the
pass:

```sh
python research/verify_target_c_contact_rhombic_grid_capacity_2026_10_17.py
python research/verify_target_c_two_side_polynomial_refill_2026_10_05.py
python research/verify_target_c_triangular_two_pin_capacity_2026_10_05.py
```

Those existing verifier files are controlled by their own reports. They
checked the linear-slack family, six complete two-side replacement packets,
the polynomial gap/tolerance, and the `m=3`/`4-by-4` strict-capacity
obstructions. Universal claims in the predecessor reports come from their
proofs, not from these finite controls.

## Open next questions

- **Downstream decision:** Can the two-side theorem change the C-II finite
  endpoint decision for every sufficiently large canonical global minimizer?
- **Exact quantity:** Its population payment is `K-z-(m+n-1)` after a wall
  with side indices `m,n` is extracted.
- **Changed hypothesis:** Add the canonical full-source/global-minimality
  information absent from this nonglobal control, and prove extraction of a
  complete ordered unit wall within `eta_(m+n)` with nonnegative population
  payment `K-z-(m+n-1) >= 0`.
- **Either outcome:** A proof supplies the full funded refill route; a
  counterexample under the strengthened canonical hypotheses rejects that
  route and directs work to moved guards, outside capacity or a nonlocal
  endpoint.
- **First step:** Test whether an existing canonical train/face theorem
  outputs all ordered wall vertices with error at most `eta_L` and counts
  every enclosed contact isolate in `z`.
- **Blocker:** Current canonical estimates do not provide that wall or
  deficit, and the present regression is nonglobal.

Required repository-wide theorem replay is **deferred to the merging agent**.
