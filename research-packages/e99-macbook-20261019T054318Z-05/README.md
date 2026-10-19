# Independent audit of PR #103: cross-component determinant payment

**Disposition:** PASS for the supplied-hypothesis implication below. This is one
independent AI-agent audit of the exact pinned report, not a theorem promotion.
The PR #103 claim remains unreviewed and noncanonical until the repository's
separate lifecycle process changes it.

**Audited report:** `docs/reports/target_b_two_component_virtual_determinant_payment_2026-10-18.md`
at PR #103 head `4b708e27e9e26f8c163685dfe8b033b6d6369177`; SHA-256
`c755e9508fc28ae6765eef4e704367deef73ff692e4b397f685b011705967882`.
The PR head is based on `7d0a450fe66991036541023f95c44c064a04b6a8`, the
current `main` at audit time. The source bytes were read with `git show` and
their hash was checked independently.

**State / priority / catalogue:** `2026-10-15.publication.2` /
`public-frontier.3` / `public-frontier.9`.
**Investigation:** `audit-pr103-cross-component-deletions-macbook-20261019`.
**Auditor:** OpenAI Codex, GPT-6 Luna xhigh, in a separate reviewer worker.
The originating report also credits OpenAI Codex, GPT-6 Luna xhigh. This audit
reconstructs the local implication from the train-crossing definitions and the
Section 50.1 deletion procedure. It takes the stated total angular-defect
estimate as an input; it does not independently establish or promote that
estimate.

## Exact conditional claim

Let a finite pure, simply connected, strict-rhombic disk have diameter `D`.
Fix `0 < eta, lambda < 1`. In its train-crossing graph, first delete each edge
whose angular defect is greater than `D^(-1+eta)`, then iteratively delete
vertices of current degree less than `lambda D`. Let `H_1` and `H_2` be distinct
components of the final graph. Suppose there are disjoint train subsets
`A subset H_1`, `B subset H_2` and fixed constants `alpha,beta > 0` with
`|A| >= alpha D`, `|B| >= beta D`. In the projective direction circle
`R/pi Z`, suppose every direction in `A` is within angular radius `epsilon`
of `phi_1` and every direction in `B` is within radius `epsilon` of `phi_2`.
Set `s = |sin(phi_1-phi_2)|` and assume `s > 2 epsilon`. Define

```text
V_AB = sum_{tau in A, sigma in B, tau and sigma do not cross}
       |det(u_tau,u_sigma)|.
```

Then the exact bound is

```text
V_AB >= alpha beta (s - 2 epsilon) D^2 - C_delta D^(2-eta),
```

where `C_delta` is the constant in the canonical angular-defect estimate
`sum_e delta_e <= C_delta D`. In particular, if all displayed constants are
fixed independently of `D`, then the right side is at least half its positive
quadratic term for sufficiently large `D`.

The affected canonical quantity is only this sub-sum of the Section 26.4
missing-crossing mass
`M = sum_{noncrossing train pairs} |det(u_tau,u_sigma)|`. This statement does
not supply the angularly separated subsets or insert `V_AB` into the Target B
shell endpoint.

## Proof reconstruction

1. Section 50.1 gives `sum_e delta_e <= C_delta D`. For the initial high-defect
   set `E_hi = {e : delta_e > D^(-1+eta)}`, positivity of each defect gives

   ```text
   |E_hi| D^(-1+eta) < sum_e delta_e <= C_delta D,
   |E_hi| <= C_delta D^(2-eta).
   ```

2. Put `P=A x B`. Since the two components are disjoint, every element of `P`
   is one distinct unordered cross-component train pair. Split `P` into pairs
   whose trains cross and pairs whose trains do not cross. Every crossing pair
   has at least one physical crossing occurrence. The route states the stronger
   no-double-crossing property, so each pair contributes exactly one rhombus;
   however, the inequality below only needs to select one occurrence per pair.

3. Consider any physical crossing edge between a train in `H_1` and a train in
   `H_2`. If it survived the initial high-defect deletion, both its endpoints
   survive the later vertex pruning. The edge would then remain in the final
   graph and join the endpoints into one connected component, contradicting
   `H_1 != H_2`. Thus every such physical crossing belongs to `E_hi`. An edge
   removed by vertex pruning is incident to a vertex deleted by that pruning,
   so it cannot have both endpoints in the final retained vertex set.

4. Let `W_AB` be the determinant sum over crossing pairs in `P`. Select one
   physical crossing occurrence for each such pair. Occurrences selected for
   different pairs are distinct because their train endpoints differ. By step
   3 they all belong to `E_hi`, so the number of crossing pairs is at most
   `|E_hi|`. Each pair determinant is at most one, giving
   `W_AB <= |E_hi| <= C_delta D^(2-eta)`. This counting remains valid even if
   a train pair had multiple physical crossings. The pruning term
   `C_T lambda D^2` in the total Section 50.1 deletion estimate is not charged:
   none of those pruned-endpoint edges can join two final retained components.

5. Write the projective train directions in lifts
   `phi_tau = phi_1 + a_tau`, `phi_sigma = phi_2 + b_sigma`, with
   `|a_tau|, |b_sigma| <= epsilon`. Since `x -> |sin x|` is 1-Lipschitz,

   ```text
   |det(u_tau,u_sigma)|
     = |sin(phi_tau-phi_sigma)|
     >= |sin(phi_1-phi_2)| - |a_tau-b_sigma|
     >= s - 2 epsilon.
   ```

   This uses directions modulo `pi`; reversing either unit representative
   changes only the determinant sign, which is removed by the absolute value.

6. Therefore the sum over all pairs in `P` is at least
   `|A||B|(s-2 epsilon) >= alpha beta(s-2 epsilon)D^2`. It is exactly
   `V_AB + W_AB`. Subtracting the bound on `W_AB` proves the claim. Since all
   pairs in `A x B` are distinct noncrossing pairs in the global sum, `V_AB`
   is a genuine sub-sum of `M`, with no factor-of-two change.

This establishes the displayed inequality, including the deletion order,
train-pair counting and angle convention. No extra `O(lambda D^2)` term is
needed. The claim that `V_AB` is a sub-sum of `M` uses only the definition of
`M` as the sum over noncrossing train pairs. The global identity
`area(Z)=S+M` is not needed for this inequality.

## Adversarial controls and scope

- **Aligned directions:** if `s=0`, the proposed quadratic coefficient is not
  positive. The inequality reduces to a nonpositive lower bound and gives no
  useful positive virtual mass. This is a limitation, not a counterexample.
- **At the angular threshold:** writing `q_D=s_D-2 epsilon_D`, the proven
  lower bound is `alpha beta q_D D^2 - C_delta D^(2-eta)`. It is positive only
  when `alpha beta q_D D^eta > C_delta`; a half-strength conclusion needs
  `C_delta D^(-eta) <= alpha beta q_D/2`. A fixed positive gap satisfies this
  eventually. A gap of order `D^(-eta)` need not.
- **Sublinear populations:** for actual sizes `m_D=|A|`, `n_D=|B|`, the same
  proof gives

  ```text
  V_AB >= m_D n_D (s - 2 epsilon) - C_delta D^(2-eta).
  ```

  If both sizes are `D^(1-gamma)` and the angular gap is fixed, the first term
  dominates the error only when `2 gamma < eta`. The stated fixed `alpha,beta`
  hypothesis cannot be dropped without a product-size condition.
- **Pruning charge:** replacing `E_hi` with all of `E_del` would add a possibly
  quadratic `C_T lambda D^2` loss for fixed `lambda`. The endpoint argument
  rules out that loss for these cross pairs, because a pruned vertex is not a
  final endpoint. This relies on the actual Section 50.1 order and on pruning
  deleting only a vertex and its incident current edges.
- **No-double-crossing and lifecycle:** the route records a two-crossing
  exclusion and uses it for the Section 26.4 identity. The prior artifact
  `docs/audits/target_b_virtual_zonotope_missing_crossing_audit_2026-09-05.md`
  is indexed `unreviewed`; this audit does not certify that global identity.
  The local `W_AB` estimate needs only at least one physical crossing per
  crossing pair, and the injection in step 4 handles repeated occurrences.
  Thus the supplied-hypothesis inequality does not depend on promoting the
  separate zonotope identity.

### Precision about the remaining extraction

The source report says Section 50.1 alone gives neither fixed linear angular
subsets nor separated centers, and notes that its population bound depends on
`lambda`. More precisely, for each fixed `lambda > 0`, every nonempty final
component has minimum degree at least `lambda D`, hence at least `lambda D+1`
vertices. For any fixed `0 < epsilon < 1/2`, partition `R/pi Z` into a finite
number `K(epsilon)` of half-open arcs of diameter at most `2 epsilon`. One arc
in each component contains at least `(lambda/K(epsilon))D` train directions.
Thus a fixed-linear angular subset in each component follows with constants
depending on `lambda` and `epsilon`; it is not uniform as `lambda` tends to
zero.
Section 50.1 does not by this counting argument force the two selected arc
centers to satisfy `|sin(phi_1-phi_2)| > 2 epsilon`. That separated-center
extraction remains open and is outside this audit's proof claim.

The inequality also does not establish that `V_AB` survives the support-depth
term in `M`, yields a grid or PC penetration bound, or proves
`G+E >= (sqrt(3)/4)B + (sqrt(3)/2)(t+chi-1)`. Level I, Target B and C-II remain
open; C-I remains closed.

## Comparison with existing work

- Discussion #83 / PR #86 concerns an abstract supplied-grid shared-interface
  inventory. It does not realize the train graph, use determinant area, or
  establish the present physical-versus-high-defect partition.
- PR #125's exact Euler correction handles the component/hole/outside-label
  count on a supplied rhombic complex. It changes the topology bookkeeping, not
  the missing-crossing mass proved here.
- The canonical GPI result remains a one-dominant-component statement; it does
  not imply the separated two-component hypothesis audited here.

## Evidence, checks, and limits

- `git fetch origin main`: `origin/main` remains
  `7d0a450fe66991036541023f95c44c064a04b6a8`; theorem state, priority, and
  catalogue revisions match the assigned checkpoint.
- The exact PR #103 report bytes were obtained with `git show` and hash-checked
  against the assigned SHA-256 above.
- The proof was reconstructed from the train-crossing definitions and
  `docs/targets/target-b/01-jammed-rhombic-branch.md` Sections 49 and 50.1,
  plus the current Target B route. Section 50.1's total defect estimate is a
  supplied premise. The Section 26.4 global area identity is cited by PR #103,
  but is not needed for this implication and its separately indexed audit is
  unreviewed. The proof is analytic. The package's exact-rational `verify.py`
  checks the algebraic subtraction and scale controls only; it does not certify
  any geometric hypothesis or the analytic proof.
- `SOURCES.json` pins the route, state, priority, and relevant predecessor
  artifacts at the baseline. It records the exact PR #103 source head and
  digest without copying the candidate's original bytes into this package.
- `python -I -B research-packages/e99-macbook-20261019T054318Z-05/verify.py`:
  passed; output says the exact-rational algebra and scale controls passed,
  with geometry explicitly uncertified.
- `python -I -O -B research-packages/e99-macbook-20261019T054318Z-05/verify.py`:
  same pass under optimized Python.
- `python scripts/research_package.py --package
  research-packages/e99-macbook-20261019T054318Z-05 --check-only`:
  `metadata-valid`; the only unresolved item is the external PR #103 source
  pin. Metadata checking did not execute the verifier or certify the proof.
- This audit adds no theorem-state, manifest, priority, or canonical dependency
  change. Repository integrity and CI-planner commands are recorded in the PR
  and handoff after they are actually run. Required full theorem-certificate
  replay is deferred to the merging agent.

The report is an original independent reconstruction under Apache-2.0-compatible
project terms. It copies no external literature or nonpublic source. OpenAI
Codex assisted with the proof audit and report; the originating PR's credit is
retained above. No human mathematical review or theorem promotion is claimed.
