> Generated reading edition · [exact source](../../../docs/audits/target_c_single_port_lattice_chain_independent_audit_2026-10-09.md) · source SHA-256 `2bf979db70b08787e5bee53fbff1f448f39008406b421364fca2833abe1e8550`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-90A40D90B1EB","canonical":true,"claim_ids":["C-LOADED-UNIT-CHAIN-LATTICE-ALIGNMENT","C-SINGLE-PORT-ATLAS-OBSTRUCTION","C-UNIT-CHAIN-TRIANGULAR-LATTICE-DIRECTION"],"claim_statuses":{"C-LOADED-UNIT-CHAIN-LATTICE-ALIGNMENT":"canonical","C-SINGLE-PORT-ATLAS-OBSTRUCTION":"canonical","C-UNIT-CHAIN-TRIANGULAR-LATTICE-DIRECTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.208 — single-port lattice chain obstruction

Date: 2026-10-09. Audit base: `origin/main=cfdc1b0c3ae94e97f6921c1a748eef0c95e5eef9`, state `2026-10-09.audit.201`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate artifact: Sections 13.1–13.3 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Verdicts: **PASS — promote** the exact seven-site lattice lemma as `C-UNIT-CHAIN-TRIANGULAR-LATTICE-DIRECTION`; **PASS WITH NARROWED SCOPE — promote** its uniform actual-source consequence as `C-LOADED-UNIT-CHAIN-LATTICE-ALIGNMENT`; **PASS WITH NARROWED SCOPE — promote** the exact local-atlas count as `C-SINGLE-PORT-ATLAS-OBSTRUCTION`.
- The audit is conditional on the explicit local lattice approximation, finite orientation set, and sublinear defect hypotheses in the last two statements. It proves no global lattice phase or extraction of those hypotheses.

## Exact finite lemma

Let `p_i=i t`, `0<=i<=6`, for a unit vector `t`, and let `Lambda` be a translate of a unit triangular lattice. Suppose `a_1,...,a_5` lie in one closed half-plane bounded by the line through the `p_i`, and

$$
 |a_i-p_i|=1,\qquad |a_i-p_j|\ge1\ (0\le j\le6),\qquad a_i\ne a_{i+1}\ (1\le i<5).
$$

Then `t` is one of the six unit vectors of the underlying triangular lattice. No uniqueness of the anchor displacement follows or is claimed.

## Independent reconstruction of the finite lemma

Rotate and translate so `t=(1,0)` and the anchor half-plane is below the line. Write `a_i=(i+x_i,y_i)`. The lower-distance constraints to `p_{i-1}` and `p_{i+1}` give `-1/2<=x_i<=1/2`; the unit distance to `p_i` then gives `-1<=y_i<=-sqrt(3)/2`. Put `delta=1-sqrt(3)/2<1/7` and `w_i=a_{i+1}-a_i`.

Each `w_i` is a nonzero lattice vector, with horizontal component in `(0,2]` and vertical component of magnitude at most `delta`. Its squared length is below five. The triangular-lattice norm form is `r^2+rs+s^2`; its nonzero values below five are `1,3,4`. Thus the only possible lengths are `1,sqrt(3),2`, with the latter two directions respectively halfway between unit directions and parallel to unit directions.

At least one of the four increments has length one. Otherwise each horizontal component is at least `sqrt(3-delta^2)>5/4`, while their sum is `4+x_5-x_1<=5`. Let `u` be a unit increment. Its angle from `t` is at most `arcsin(delta)`. A length-`sqrt(3)` vector has nearest direction at angle `pi/6` from `u`, and its vertical component is at least `sqrt(3)sin(pi/6-arcsin(delta))`; at `delta=1/7` this is `9/14`, which exceeds `1/7`. Every other unit axis is at least `pi/3` from `u`, and its vertical component is at least `sin(pi/3-arcsin(delta))`; at `delta=1/7` this is `11/14`. These lower bounds increase as `delta` decreases. Thus the vertical strip excludes all such directions and their doubles; positivity excludes `-u` and `-2u`. Hence every increment is `u` or `2u`.

Two consecutive increments must both equal `u`: if no adjacent pair did, at most two of the four increments would be `u`, so the total horizontal displacement would be at least `6(u dot t)>=6sqrt(1-delta^2)>5`, a contradiction. For three consecutive pairs the relative anchor-site displacements are `v`, `v+(t-u)`, and `v+2(t-u)`, all of norm one. The second finite difference of their squared norms is `2|t-u|^2`, so `t=u`.

The noncoincidence of consecutive anchors is load-bearing. In the source application, a shared anchor for adjacent loaded unit sites would be an actual unit triangle. The finite lemma is not a finite-motion statement.

## Uniform actual-source consequence

Consider any sequence of noncollinear, triangle-free global minimum-diameter unit-separated sources with `D->infinity`. In a seven-vertex window, require seven consecutive actual diameter endpoints on the full-source hull, with all six hull sides unit. At each of the five interior vertices choose an actual source point outside the loaded endpoint set at unit distance. Suppose all five chosen points lie within a common error `epsilon_D->0` of one translate of a unit triangular lattice whose orientation belongs to a fixed finite set `J`; the error is uniform over the windows under consideration, while the translation may vary freely. Then every side in the window is within `tau_D->0` of one common unit direction of that window's reference lattice. The convergence is uniform over windows and translations. No rate for `tau_D` is asserted.

For the independent geometric reduction, Audit.206 gives `|m-o|<=7D^(2/3)` for every actual diameter midpoint and `|h'|<=6D^(2/3)` at both one-sided limits of the full-source support function. Each loaded endpoint `p` therefore satisfies `|p-o|>=D/2-7D^(2/3)`. By the canonical nearby-endpoint theorem, a unit side between two such endpoints is a full-source hull side for all sufficiently large `D`. At its outward normal, the one-sided support derivatives are the tangential coordinates of its endpoints, so the side normal differs from the endpoint radial direction by `O(D^(-1/3))`. Across a six-unit-side window the radial directions vary by `O(D^(-1))`; all six side directions therefore have a common limiting tangent.

If the asserted uniform lattice alignment failed, take a sequence of bad windows and a subsequence with one fixed orientation from `J`. Normalize the first loaded endpoint to the origin. The sides converge to a straight unit chain `p_i=i t`. The five chosen neighbors remain bounded, their lattice-site offsets have only finitely many possibilities, and the lattice translation modulo the lattice has a convergent subsequence. The limits are lattice anchors in one closed interior half-plane. Since the anchors are actual source points outside the loaded endpoint set, all source separation inequalities pass to the limit. Consecutive anchors are distinct: otherwise the actual triangle-free source would contain a unit triangle; also two distinct source anchors cannot round to the same lattice site once `2epsilon_D<1`. The finite lemma forces `t` to be a lattice unit direction, contradicting the assumed positive angular gap. This contradiction proves the uniform `o(1)` conclusion, including arbitrary translations and varying windows.

This consequence uses only actual source anchors and actual loaded endpoints. Contact-isolated points remain in the source-separation and full-source-hull arguments. The finite set of lattice orientations is essential; no claim is made for a growing or arbitrary orientation atlas.

## Single-port atlas obstruction

In a canonical post-ZF C-II sequence, choose one actual unloaded unit neighbor at each loaded vertex except `b_0` vertices. Assign the chosen neighbors to a fixed finite set of `J` unit-triangular charts, with `R_D` changes of chart in cyclic loaded-hull order. Assume that, in every seven-vertex window where the five interior neighbors belong to one chart, those five actual points are within a common `epsilon_D->0` of one translate of that chart's reference lattice. Let `m` count nonunit loaded-hull sides. Then

$$
 q\le 6m+5b_0+4R_D+o(D).
$$

Indeed, each nonunit side spoils at most six centered windows, each missing neighbor at most five, and each chart transition at most four. Every remaining center has six unit sides and five same-chart anchors, so the uniform alignment theorem applies. At the central loaded endpoint, both adjacent hull sides lie in the same shrinking tangent window; its full-source normal cone, and hence its chosen actual diameter normal, lies in the perpendicular window. The actual-diameter-normal window count proved in Audit.203 bounds any oriented window of half-width `tau_D` by

$$
1+\frac{D\sin(tau_D)+2L_D}{\cos(tau_D)}=o(D),\qquad
L_D=\sqrt{D\eta_D+\eta_D^2}=o(D),\quad \eta_D=3^{1/4}\sqrt D.
$$

There are only `6J` possible oriented normal windows, so all good centers contribute `o(D)`. The stated bound follows by the three exact defect counts and a union bound. Canonical `C-ZRF` and `C-WOODALL` give `q>=h>=ceil(D)`. Thus `m=o(D)`, `b_0=o(D)`, and `R_D=o(D)` cannot hold simultaneously under this actual local atlas hypothesis.

The atlas premise is local and explicit. This theorem does not extract such an atlas from a canonical source, establish small `m`, create a move, or close C-II or Level I. The candidate's observation that a particular globally defined slow chart may imply the local approximation is not separately promoted here.

## Dependencies, hostile checks, and verifier boundary

- `C-UNIT-CHAIN-TRIANGULAR-LATTICE-DIRECTION` is independent.
- `C-LOADED-UNIT-CHAIN-LATTICE-ALIGNMENT` depends on that lemma, `C-FS-DIAMETER-MIDPOINT-D2-3`, and `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`.
- `C-SINGLE-PORT-ATLAS-OBSTRUCTION` additionally uses `C-LOADED-HULL`, `C-LOADED-WALK-DIRECTIONAL-STRAIN` (only its audited full-source normal-window count), `C-ZRF`, and `C-WOODALL`.
- The one-port case is distinct from the two-unloaded-port theorem; the shared-anchor triangle and repeated lattice-site possibilities were checked explicitly. No local feasibility, first-order motion, source/scaffold substitution, or positional transport is used.
- No dedicated finite verifier is claimed for these compactness and geometric arguments. Audit.203's exact normal-window inequality is reused only in its audited scope; it counts actual diameter endpoints and retains contact isolates. A finite script is not used as evidence for the new lemmas.

**Frontier effect:** none. The package excludes only configurations satisfying all stated small-defect and local finite-lattice hypotheses. Target C remains C-I closed / C-II open, and Level I remains open.
