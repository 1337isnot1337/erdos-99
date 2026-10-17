> Generated reading edition · [exact source](../../../../docs/research/tracks/global-population-lattice-interface-pr956.md) · source SHA-256 `d7f0e845a295893ed306c612558c532006f7d237f5a9e6ccc0279f29e9f2b258`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Global population reserve, lattice defect, and interface payment

**Source:** open draft PR #956, frozen at `bbc549f36ac964fd7eee211782eb2c979d12af32` (tree `3d8550adf520dcacd17876d6ddf1970a6c9e857e`), based on source main `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. **Lifecycle:** all four analytic reports are unreviewed candidates; the stress-ring family is a proved regression, not a global minimizer. The destination theorem-state and current Target C status remain authoritative. See the [per-file migration ledger](../../../../docs/research/migration/2026-10-16/ledger/source-pr-files.jsonl), [scientific reconciliation](../../../../docs/research/migration/2026-10-16/scientific-reconciliation.md), and [source PR audit](../../audits/pr956_autonomous_proof_audit_2026-10-15.md).

## Route map

| Program | Strongest preserved statement | Exact limitation / next obligation |
| --- | --- | --- |
| Boundary zigzag | For every `R >= 640000`, each translate of the unit triangular lattice cropped to the radius-`R` disk admits a unit-separated replacement gaining at least `R/160000` labels. Thus every global minimizer with `D > 1280000` satisfies `g_A = n - 1 - pi D^2/(2 sqrt(3)) >= D/320000`. | This is an independent whole competitor and population lower bound; it does not identify a minimizer with a lattice, force a triangle, or give a C-II endpoint. It is numerically weaker and has a larger stated threshold than source PR #1008's unreviewed `D/600` bound for `D >= 10^6`, but the construction and proof are distinct. |
| Lattice count and periodic motif | Any finite subset of any translated unit-separated rank-two lattice with actual diameter at most `D` obeys `|S| <= pi D^2/(2 sqrt(3)) + 86 D^(4/5) + 1`. With the boundary reserve, at least `D/640000` labels of every sufficiently large global minimizer lie farther than `10^-7` from every fixed such lattice. A globally unit-separated periodic packing with `1 <= q <= D/16` sites per cell obeys `|S| <= pi D^2/(2 sqrt(3)) + 114 q^(6/5) D^(4/5) + q`; every global minimizer with `D > 1280000` inside one such packing must have `q >= D^(1/6)/(36800000)^(5/6)`. | The defect and motif consequences are conditional on the unreviewed reserve. No lattice, periodic motif, or grain decomposition is extracted from every triangle-free global minimizer. Periodic bounds require separation of the *entire infinite packing*, including cross-coset pairs. The exact 39-lattice regression rejects a finite-union shortcut. |
| Straight interface payment | For complete unit-separated rank-two lattice half-planes with parallel front rows and the report's exact cross-separation hypotheses, `2g >= a0(1/s_A+1/s_B) - N(V_A-a0)/s_A - M(V_B-a0)/s_B`; when both covolumes equal `a0=sqrt(3)/2`, `g >= (h_A+h_B)/2`. A finite-window theorem gives explicit endpoint costs. | Canonical coherent grains do not imply complete lattice half-planes, `o(D)` junction/outer terms, disjoint area allocation, or an all-label decomposition. Derive those from actual sources before summing payments. |
| Stress-density regression | For every odd `q >= 5`, the regular contact ring has positive contact and diameter equilibrium weights, exact mixed rank `2q-3`, and local isolation among same-label feasible configurations modulo rigid motions. Adding strictly separated interior labels gives triangle-free sources with `n_q/D^2 -> pi/(2 sqrt(3))`. | These sources are strictly nonglobal: a same-cardinality competitor has diameter `< D-4`. They prove no fixed positive density loss follows from the listed local stress, rigidity, hull, and isolate conditions alone; they are not a global-minimizer counterexample. |

## 1. Boundary zigzag: full competitor and global comparison

The report uses a triangular lattice with horizontal rows. In a guarded interval on a shallow circular arc, it removes the old row labels and inserts a zigzag with horizontal spacing `19/20` and alternating heights `1/6` and `1/2`. Adjacent inserted squared distance is `3649/3600 > 1`; all lower-row, retained same-row, higher-row, and cross-packet pairs are covered. Each eligible row yields at least one net label. Translation averaging supplies enough rows for the stated `R/160000` gain for every disk radius `R >= 640000`.

For a global minimizer of diameter `D > 1280000`, take `R < D/2`, so the replacement has strict smaller diameter. Global optimality bounds every competitor's population by `n-1`; only then does the radius tend to `D/2`, yielding `g_A >= D/320000`. The comparison retains all original source labels and does not move them. This is a Level I population consequence, not a triangle or C-II closure.

**Verifier:** [`verify_global_boundary_zigzag_2026_10_11.py`](../../../../research/verify_global_boundary_zigzag_2026_10_11.py). It checks exact finite configurations and pair ledgers; the infinite-row estimate and global implication remain analytic proof claims, not finite-verifier output.

## 2. Lattice defect and full periodic packing

The lattice estimate uses the actual diameter of the finite lattice subset; it does not assume the set lies in a disk of radius `D/2`. Its proof combines a flat-side area deficit, uniform multiplicity estimates over lattice directions, Pick's theorem, and an optimized boundary parameter. The resulting `86 D^(4/5)` term is uniform in lattice shape, phase, and orientation.

Assuming the boundary reserve, match every source label within distance `rho < 1/2` to a distinct nearby lattice site. Those sites have diameter at most `D+2rho`. Subtracting the lattice count from the global lower reserve gives

`k_rho(A,Lambda) >= (c-4a rho)D - 4a rho^2 - 86(D+2rho)^(4/5)`,

where `c=1/320000` and `a=pi/(2 sqrt(3))`. At `rho=10^-7`, the report obtains at least `D/640000` labels farther away for every sufficiently large global minimizer and every translated unit-separated lattice. This is full-source counting, including contact isolates.

For a periodic packing with `1 <= q <= D/16` cosets, the proof first establishes a covolume lower bound using canonical finite Oler at the density limit, then sums lattice-subset bounds when the period cell is dense. A separate row-count handles sparse large-covolume cells. Cross-coset separation across the infinite packing is essential. The resulting growing lower bound on `q` rules out a uniformly bounded periodic motif for unbounded minimizers *if* the reserve and the periodic-packing hypothesis hold; it does not extract that periodic representation.

The exact 39-lattice fixture vertically expands a finite selected union into a triangle-free source while keeping each constituent lattice unit-separated. It is nonglobal. It blocks treating a finite union of lattice descriptions as one lattice or summing interface credits without verified cross-grain geometry; it does not refute paid nonoverlapping grain decompositions.

**Verifier:** [`verify_global_lattice_population_bound_2026_10_11.py`](../../../../research/verify_global_lattice_population_bound_2026_10_11.py). The exact fixture is built into the verifier and its report; do not replace the infinite cross-coset hypothesis with a finite screen.

## 3. Straight interfaces: a conditional payment rule

The theorem treats two complete lattice half-planes with parallel front rows. It requires every cross-pair between the two infinite half-planes to be at distance at least one. The lattice bases may have different horizontal periods and need not be commensurate. If both covolumes are minimal, the seam's normal gap pays the two triangular boundary-row credits exactly. For nonminimal covolumes, the statement retains explicit terms for each covolume defect and row count.

The finite-window extension charges a stated endpoint allowance. Its verifier checks representative exact seam, orientation, incommensurate-period, zero-gap, and invalid-infinite-continuation fixtures. The analytic whole-half-plane pair and density arguments are in the report. To use this in Target C, one still needs actual source regions satisfying those hypotheses, finite-window endpoint bounds that sum without double-counting, `o(D)` control of junction and outer terms, and allocation of every source label and isolate.

**Verifier:** [`verify_global_straight_interface_payment_2026_10_11.py`](../../../../research/verify_global_straight_interface_payment_2026_10_11.py).

## 4. Stress and density: a binding local-to-global warning

The regular odd ring has unit-contact graph `C_q` and diameter graph given by cyclic step `(q-1)/2`. The report derives exact positive equilibrium weights, the stress spectrum, and mixed rigidity rank `2q-3`. A positive-stress argument isolates the ring locally among same-label feasible configurations of diameter at most `D`, modulo Euclidean motions.

For large odd `q`, it adds `n_q-q` labels from a slightly expanded triangular lattice disk strictly inside the ring, where `n_q=floor(a(D-4)^2)`. All added labels are contact isolates and create no new unit or diameter edges. The population has asymptotic optimal leading coefficient `n_q/D^2 -> a`. Yet the canonical strict translated-lattice competitor gives a same-cardinality diameter `< D-4`, so these sources are not global minimizers.

The falsified implication is specifically a uniform positive quadratic-density loss from full support, scalar PSD, mixed-core rigidity, local diameter minimality, an asymptotically circular hull, and retention of isolates. A valid global proof must use further consequences of global optimality, resolve the boundary-order population comparison, or exhibit a full-source competitor. Do not cite this ring as a global minimizer or a counterexample to Level I.

**Verifier:** [`verify_global_stress_density_regression_2026_10_11.py`](../../../../research/verify_global_stress_density_regression_2026_10_11.py).

## 5. Reading and verification order

1. Read the boundary report, then its exact verifier. Compare its reserve to the stronger unreviewed PR #1008 twelve-arc candidate; do not merge their constants or proof hypotheses.
2. Read the lattice-defect report. Treat its conditional `D/640000` defect and periodic-motif bound as downstream of the boundary reserve.
3. Read the interface report with canonical `C-COHERENT-GRAINS` and the 39-lattice regression. The canonical grain result supplies neither full half-planes nor paid `o(D)` junctions.
4. Read the stress-density regression before proposing another argument based only on local positive stresses and rigidity.
5. Read the [source audit](../../audits/pr956_autonomous_proof_audit_2026-10-15.md) for proof reconstruction and negative checks. Its source-agent audit is provenance and is not the destination's required independent exact-head AI review for any consequential promotion.

The four verifiers are finite/formal evidence for their stated instances. They do not certify the universal analytic arguments, promote candidates, or alter Level I, Target A/B, C-I, or C-II status.
