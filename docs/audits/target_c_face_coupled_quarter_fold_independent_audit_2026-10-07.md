<!-- theorem-state: {"artifact_id":"ART-FD63E8F3C10B","canonical":true,"claim_ids":["C-FACE-COUPLED-QUARTER-FOLD-INTEGRATION","C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION","C-QUARTER-FOLD-FOUR-TRANSITION-REGRESSION","C-QUARTER-FOLD-INACTIVE-DIAMETER-REGRESSION","C-QUARTER-FOLD-LOWER-COLLISION-REGRESSION","C-QUARTER-FOLD-SOURCE-COMPATIBILITY","C-QUARTER-FOLD-STRESS-CURRENCY-ENDPOINT"],"claim_statuses":{"C-FACE-COUPLED-QUARTER-FOLD-INTEGRATION":"canonical","C-QUARTER-FOLD-CONVEX-FACE-CLASSIFICATION":"canonical","C-QUARTER-FOLD-FOUR-TRANSITION-REGRESSION":"regression","C-QUARTER-FOLD-INACTIVE-DIAMETER-REGRESSION":"regression","C-QUARTER-FOLD-LOWER-COLLISION-REGRESSION":"regression","C-QUARTER-FOLD-SOURCE-COMPATIBILITY":"canonical","C-QUARTER-FOLD-STRESS-CURRENCY-ENDPOINT":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Target C: independent audit of face-coupled quarter folds

Date: 2026-10-07. Base: `origin/main=12fb98e68f2f3f8f827e76c3759534edef93ed7c`, state audit.82.

## Immutable source and audit boundary

The audited source is Worker 1 branch `research/sol/target-c-overnight-closure-20261007` at `f65456766477da03711b1316ffde13e27acf70aa`, report `docs/reports/target_c_face_coupled_quarter_fold_currency_and_blockers_2026-10-07.md`, verifier `research/verify_target_c_face_coupled_quarter_folds_2026_10_07.py`, and saved certificate `research/target_c_face_coupled_quarter_folds_certificate_2026_10_07.json`. The branch has since advanced to `9204dc1469359e5b22a8bfe9429dfb391dec4b4d`; a direct file comparison found no change to these three artifacts. This audit uses only the frozen `f6545676` contents.

The source report mixes exact finite identities, conditional endpoint consequences, universal sign constraints, and three nonglobal finite regressions. The following are audited separately. No claim of a universally feasible nonconstant sign state is promoted.

## 1. Face equations integrate to an exact finite fold

Let the connected contact core be a finite plane graph. Its edges are partitioned into complete stopped trains, and every bounded quadrilateral face is a strict unit rhombus whose opposite edges belong to the same train. Give each train a sign `s_tau` in `{−1,+1}`. For an oriented contact edge `ij`, put `q_ij=p_j-p_i` and define the edge field

`w_ij=s_tau*J(q_ij)`, with `J(x,y)=(-y,x)`.

On a strict rhombus, the two occurrences of each train have opposite oriented edge vectors, so their contributions to the face sum cancel. Assume the remaining bounded faces satisfy `sum_(ij in boundary walk f) w_ij=0`, counting occurrences. The bounded face walks span the cycle space of a connected plane graph (bridges occur twice with opposite orientations). Hence the sum of `w` around every cycle is zero. Path integration gives a vertex field `U`, unique up to a translation, with `U_j-U_i=w_ij` on every contact edge.

For every real `phi`, set `X_i(phi)=cos(phi)*p_i+sin(phi)*U_i`. On a contact edge, `X_j-X_i=cos(phi)*q_ij+sin(phi)*s_tau*J(q_ij)`; the summands are perpendicular unit vectors, so the edge length is exactly one. The face sums also close exactly at every `phi`. This proves a finite formula, not only an infinitesimal velocity. It does not prove any noncontact lower bound, diameter upper bound, or feasible path between endpoints. Contact-isolated source labels are outside this integration; choosing their coordinates remains a full-pair constraint.

## 2. The canonical stress gives conditional diameter currency

For the contact-minimal, then actual-diameter-pair-minimal C-II representative with `D>=9`, retain the full source but let `V` be the nonisolated positive-contact core. The canonical C-I selected-stress PSD result and the core-scoped ZR theorem apply to a relative-interior normalized KKT stress: contact weights `alpha>0`, actual-diameter weights `beta>0`, `sum_H beta=1`, and

`Omega=L_C(alpha)-L_H(beta) >= 0`,

`ker(Omega|_V)=span{1,p_x,p_y}`.

The `D>=9` scope is required by the promoted zero-transfer exclusion used by ZR. This audit does not extend the kernel or PSD statement to isolates.

For an integrated fold field `U`, each contact difference has squared length one. KKT virial gives `sum_C alpha = D^2`; therefore

`sum_(h=ij in H) beta_h*|U_j-U_i|^2`
`= D^2 - trace(U^T*Omega*U)`.

If `U` is nonaffine on `V`, at least one coordinate is outside the exact kernel. Positive semidefiniteness then makes the trace strictly positive. Since the beta weights are positive and sum to one, at least one old actual diameter pair is strictly shorter than `D` at the quarter-turn. This is weighted mean currency only; it does not bound each diameter pair.

The lexicographic contradiction is valid under the complete endpoint conditions: retain every source label; keep every old contact exactly unit; keep every old noncontact pair strictly greater than one; keep every old actual diameter pair at most `D`; and keep every old nondiameter pair strictly below `D`. The contact graph is then unchanged, so the triangle-free condition and contact count persist. No new diameter pair is created. If the new diameter is below `D`, global minimality is contradicted; if it equals `D`, at least one old diameter was removed and the actual diameter-pair count decreases, contradicting the second lexicographic minimum. The isolates must satisfy these same complete pair checks.

**Narrowed scope:** this certifies a currency implication for an existing nonaffine face-coupled state that passes the full source endpoint ledger. It does not give such a state, and nonconstant train signs alone do not imply nonaffinity. With at least three distinct projective contact directions, an affine field satisfying `U_j-U_i=s_tau J(q_ij)` has zero symmetric part and then one common sign; this optional criterion follows by evaluating its symmetric quadratic form on three directions. In the two-direction case, nonconstant signs can be affine.

## 3. Source-realized compatibility graph

For two unit contacts `ij` and `jk`, write `a=p_j-p_i`, `b=p_k-p_j`, and `L=|p_k-p_i|=|a+b|`. Opposite train signs give

`|U_k-U_i|^2=|a-b|^2=4-L^2`.

The old graph is triangle-free, so `i,k` is a noncontact. If `L>sqrt(3)`, opposite signs produce a lower collision; if `L=sqrt(3)`, the new `i,k` pair is unit and forms a triangle with the two preserved contacts. Thus every lower-feasible triangle-free quarter-fold must assign equal signs whenever this actual source pair has `L>=sqrt(3)`.

Make a graph on train variables with exactly these source-realized relations. Signs are constant on each connected component; if this graph is connected, only the two constant sign assignments remain. On a connected contact core those give `U=±Jp+b`, an affine rigid quarter-turn, so this route supplies no stress currency.

The local geometric corollaries are sound: at a degree-five triangle-free unit vertex, each of the five neighbor gaps exceeds `pi/3`, every nonconsecutive neighbor pair has chord greater than `sqrt(3)`, and their relation graph is connected; at degree four, each opposite-neighbor pair is related; opposite signs on consecutive collinear contacts collide; and consecutive signs along a convex unit face must agree at every exterior turn at most `pi/3`. These statements use actual source contacts and distances, not a scaffold or owner graph.

## 4. Convex-face transition classification

Consider a simple convex face boundary with unit edges `q_0,...,q_(m-1)`, exterior turns `tau_i`, and signs `s_i` satisfying its closure equation `sum_i s_i*q_i=0`. (For the outer face of the contact core this equation follows by summing the bounded-face equations.) At a sign transition, the two incident signs are opposite. The quarter-fold distance between the two outer vertices of this two-edge path is `2*sin(tau_i/2)`. Lower feasibility requires this to be at least one; equality creates a unit triangle with the two retained unit edges. Therefore every transition has `tau_i>pi/3`.

The convex turns sum to `2*pi`, so at most five vertices are eligible. A cyclic sign sequence has an even number of transitions. If there were exactly two, the plus signs would form one contiguous arc from distinct vertices `a` to `b`; face closure and `sum_i q_i=0` force `p_b-p_a=0`, impossible. A nonconstant lower-feasible triangle-free pattern must therefore have exactly four transitions. If its positive arcs run from `a` to `b` and `c` to `d`, face closure gives

`(p_b-p_a)+(p_d-p_c)=0`, hence `p_a+p_c=p_b+p_d`.

Thus the four actual transition vertices form an inscribed parallelogram, each with exterior turn above `pi/3`. This is necessary, not sufficient. A convex face with fewer than four eligible vertices or no such parallelogram forces all its boundary signs equal. The statement allows the four-transition case; it does not rule it out generically.

## 5. Exact finite regressions and certificate

The source verifier uses exact rational or `Q(sqrt(3))` arithmetic for coordinates, squared distances, closure, pair ledgers, and the finite sign universes. It was inspected and rerun at the frozen source commit. Output and saved certificate match byte-for-byte; SHA-256 is `a4f9fcf2e94a8fca4f4ec188e6c04e0a1c3e073d4db25ee689241a876173253e`. Its maximum-pair selection uses a floating key only to nominate a candidate, then exact comparisons assert that candidate is at least every exact pair value; the subsequent claims are exact. The script proves only the listed finite enumerations.

- **Regular hexagon regression.** For the unit regular hexagon with its six singleton contact trains, exact closure leaves ten of 64 sign states. Eight nonconstant states strictly decrease the weighted old-diameter mean and keep each old diameter at most `D=2`; each nevertheless has a zero-distance collision. The explicit stress matrix is PSD with affine kernel (the integer matrix `A=3*Omega` satisfies `A^2=6A` and `trace(A)=18`). A center plus unit regular pentagon is a smaller-diameter, triangle-free configuration, so this finite source is not global. It refutes the inference from face closure, PSD mean descent, and old-diameter upper feasibility to a feasible endpoint.
- **Rhombic-grid regression.** For each listed `M=2,3,4`, exact enumeration of the `(M+1)^2` points `i*u+j*v`, with `u=(1,0)` and `v=(5/13,12/13)`, gives four lower-feasible quarter-fold states. In the two mixed-direction states the unique old diameter shortens, but an old inactive opposite-corner pair becomes a new diameter of the same length. This finite nonglobal family refutes diameter-count currency based only on shortening old diameter rows.
- **Eight-site rectangle regression.** On the perimeter points of `[0,2]^2`, there are 36 face-closed sign states and exactly four fully lower-feasible triangle-free states. Their only possible transitions are at the four right-angle corners; these corners form the required parallelogram. The four states are affine (two rotations and two reflections), with no new contact or diameter count. This is a sharp finite witness that the convex-face theorem cannot be strengthened to prohibit all four-transition patterns.

The certificate does not verify the analytic integration, stress theorem, or arbitrary-face classification; those were reconstructed above. It proves no global optimality, arbitrary sign existence, finite endpoint existence, or Level I result.

## Verdicts and remaining gap

| Claim | Verdict | Scope/disposition |
| --- | --- | --- |
| Face-coupled integration | PASS — promote | Exact cochain integration and finite contact-preserving fold |
| Stress diameter currency and endpoint criterion | PASS WITH NARROWED SCOPE — promote | Canonical C-II core, `D>=9`, nonaffine state, full endpoint pair ledger |
| Source compatibility graph | PASS — promote | Exact two-hop blocker relations and stated local corollaries |
| Convex-face transition theorem | PASS — promote | Face closure, convex unit boundary, lower-feasible triangle-free endpoint |
| Hexagon, rhombic-grid, and rectangle examples | REGRESSION VALID — promote | Exact listed finite sources only; none is a global-minimizer counterexample |

The remaining quarter-fold obligation is to produce, for a canonical source, a nonaffine coupled sign assignment satisfying face closure, the source compatibility relations, and every full-source endpoint lower/upper inequality, or to derive an alternate move from an exhaustive blocker classification. This audit supplies neither. C-II and Level I remain open.
