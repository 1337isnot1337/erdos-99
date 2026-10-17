> Generated reading edition · [exact source](../../../docs/audits/target_c_profile_first_stress_correction_independent_audit_2026-10-07.md) · source SHA-256 `3bf628906bd200f063e3b9b0d91a597cbb309c91e6419c156c86ded43a302da9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CBFFC4B07475","canonical":true,"claim_ids":["C-SIX-SIDED-WALL-ACTIVE-ROW-RANK","C-SIX-SIDED-WALL-PRINCIPAL-STRESS-CORRECTION"],"claim_statuses":{"C-SIX-SIDED-WALL-ACTIVE-ROW-RANK":"canonical","C-SIX-SIDED-WALL-PRINCIPAL-STRESS-CORRECTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit — fixed-profile active-row rank and principal stress correction

**Audit base:** `main` at `905c1e51b0866b59af8b723141f1670a43f0c7d3`,
state `2026-10-07.audit.78`.

**Frozen source:** `research/sol/target-c-overnight-closure-20261007` at
`3b595c9f50b4715a4f6ef16d36212c82f8371326`.

At refreshed tip `5a4b063711ff055d0fcc387312bda40e2e355ccc`, the first-stress
report appendix, verifier, input, and certificate are unchanged. The separate
uniform-curvature-window report is not part of this audit.

## Exact claims audited

Fix `M>=3` and a strictly decreasing symmetric real profile
`a_0>...>a_(M-1)`, with `a_(M-1-h)=-a_h`.

1. **Active-row rank.** For every permutation of the profile, the limiting
   moving-column matrix of the exact sorting packet's active unit-contact rows
   has full column rank. The exact active matrix therefore also has full
   moving-column rank for each fixed profile and permutation at sufficiently
   small positive curvature.
2. **Principal stress correction.** For the descending-rate sorting packet,
   the principal six-axis radial-chain stress has an explicit first correction
   whose coefficients are strictly positive on every weak diagonal-chain row.
   After adding a sufficiently small positive combination of the nested
   strong stresses and correcting through the full-rank active matrix, this
   gives a positive exact equilibrium stress for each fixed `M` and profile
   at sufficiently small curvature.

The second statement has a fixed-parameter onset. It supplies no common
isolation or rank-inverse bound as `M` or the profile varies.

## Active-row rank reconstruction

Use axial lattice coordinates with Euclidean metric
`G=((2,1),(1,2))`. For a fixed permutation `t*` of the rates, the first-order
feasible set projects to the rate permutahedron: if `t_h` are the radial
increments, then `sum t_h=0` and every `j`-element subset has sum at least
the sum of the `j` smallest profile entries. The two layer recurrences

after a sector point `(r-j,j)` give these subset inequalities. Conversely,
the prefix-smallest construction satisfies both recurrences. At a
permutation vertex the same inequalities force every intermediate layer
coordinate, so the velocity fiber is a singleton.

The central six-chain energy has gradient proportional, in rate coordinates,
to `t*`. The linear functional `t* dot t` uniquely exposes the permutation
vertex on the permutahedron; the singleton fiber makes `t*`'s full velocity
field the unique maximizer on the full first-order polytope.

Let `J` be the exact packet's active contact rows at small positive curvature,
and `R_0` their limiting moving-column matrix. If `R_0 x=0`, then every row
in `J` remains an equality at both `d*+epsilon*x` and `d*-epsilon*x`. Every
other first-order inequality has strict slack at `d*`, so both perturbations
remain feasible for sufficiently small `epsilon`. This contradicts the
unique maximizer just established unless `x=0`. Thus `R_0` has full column
rank; continuity gives the same rank for the exact active matrix near zero.

This is the rank argument in Audit.78's packet proof, now registered as an
explicit reusable theorem. It uses the selected packet and its complete
first-order constraint system; it does not infer rank from generic rigidity
or from the full source's ZR/ZF theorem.

## Explicit first correction

For the descending packet write a sector site as `(r-j,j)`, let
`alpha_r=sum_(h<r) a_h`, and let
`s_(r,j)=-sum_(h=r-j)^(r-1) a_h`. In axial coordinates the packet's first
velocity divided by `sqrt(3)` is

`d_(r,j)=((s_(r,j)-alpha_r)/3, (s_(r,j)+2*alpha_r)/3)`.

The active flat contact rows split into ring edges, six radial axes, and the
weak diagonal chains. The principal stress `lambda_0` has coefficient one
on each edge from `r*e_k` to `(r+1)*e_k`, for `0<=r<M` and all six rays, and
zero elsewhere. Its moving-vertex forces cancel in opposite radial pairs.

Write the first correction as `lambda_1=sqrt(3)*kappa`. Set:

- `kappa=0` on each ring edge;
- on the radial edge `r*e_k` to `(r+1)*e_k`, set
  `kappa=(a_r-a_0)/3`;
- on each diagonal chain edge `(a,b)` to `(a,b+1)`, for
  `1<=a<M` and `0<=b<M-a`, set
  `kappa=2*(a_(a-1)-a_a)/3`, and rotate this assignment through the six
  sectors.

Thus every weak row has coefficient

`lambda_1 = 2/sqrt(3) * (a_(a-1)-a_a) > 0`,

with minimum at least

`(2/sqrt(3))*min_(1<=a<M)(a_(a-1)-a_a)`.

Here row derivatives are those of one half the squared-distance constraint.
In the scaled coordinates above, the first-order equilibrium equation is
`R_0^T*kappa + (R_1/sqrt(3))^T*lambda_0=0`; rescaling gives
`R_0^T*lambda_1 + R_1^T*lambda_0=0` in physical parameter units.

The force check is local. At an off-axis moving vertex, the two incident
parallel diagonal-chain rows have the same coefficient and opposite limiting
vectors; ring corrections vanish and the principal radial stress has no
incident row. At an axis vertex of radius `r`, put
`Delta=a_(r-1)-a_r>0`. The principal stress's first force is
`(0,Delta)` in axial covector coordinates. The radial correction contributes
`Delta*(2,1)/3`, and the single incident diagonal correction contributes
`-2*Delta*(1,2)/3`; their sum is `(0,-Delta)`. At the center the six rotated
first forces cancel and the radial correction at `r=0` is zero. Rotational
symmetry gives the same identities on all six sectors. Boundary vertices are
pinned and impose no moving-column equilibrium equation.

The ring rows are strong affine equalities, although this principal stress
alone gives them zero coefficient. Add a small positive sum `sigma` of the
nested ring stresses; this makes every strong-row coefficient positive and
keeps `R_0^T sigma=0`. Since `R_0` has full column rank,
`R_0^T xi=-R_1^T sigma` has a solution. For sufficiently small fixed
`eta>0`, replacing `(lambda_0,lambda_1)` by
`(lambda_0+eta*sigma, lambda_1+eta*xi)` keeps every weak first-correction
coefficient positive. Expanding the exact contact matrix as
`R_theta=R_0+theta*R_1+O(theta^2)` leaves an `O(theta^2)` residual; a bounded
right inverse of `R_theta^T` removes it. Strong coefficients retain positive
order-one margins and weak coefficients retain positive order-theta margins.
This proves positive exact-stress continuation for each fixed parameter
choice, without claiming uniform bounds for the right inverse.

## Certificate audit

The frozen verifier and input were inspected and rerun; output matches the
saved certificate byte-for-byte. The checker verifies 14 rational cases from
`M=3,...,6`, exact zero-order and first-order force identities, strict
positivity of listed weak coefficients, and full limiting rank from nonzero
modular minors. Its input coefficients were produced by numerical discovery
and exact rational projection; the checker itself uses exact arithmetic.

The certificate does **not** encode the explicit all-`M` coefficient rule
above: its finite cases use a separate optimized coefficient array with small
positive ring weights. It is finite corroboration only. The all-`M` formula
is justified by the vertex-force calculation in this audit, not by
extrapolating the fourteen samples.

A second independent exact checker, `research/verify_target_c_principal_stress_formula_audit_2026_10_07.py`, implements the displayed coefficient rule directly. It verifies all active-row classes, zero-order and first-correction equilibrium, strict weak-row signs, and modular full column rank for four fixed profiles at `M=3,4,5,6`. Its output is saved in `research/target_c_principal_stress_formula_audit_certificate_2026_10_07.json`. These are finite formula checks; the all-`M` conclusion still follows from the analytic vertex-class calculation above.

## Verdict and frontier effect

**PASS — promote** `C-SIX-SIDED-WALL-ACTIVE-ROW-RANK` and
`C-SIX-SIDED-WALL-PRINCIPAL-STRESS-CORRECTION` at the stated scopes. Adding
these IDs makes explicit the rank lemma used by Audit.78 and records the
stronger direct stress bridge. No new source exclusion follows, no onset is
uniform in growing `M` or changing profiles, and the C-II obligation remains
arbitrary-source extraction or a source-realized replacement.
