> Generated reading edition · [exact source](../../../docs/audits/target_c_accessible_stress_face_independent_audit_2026-10-08.md) · source SHA-256 `dbcd256a41c9a7be8bcb94867ab03b23d29dea7b5ad8bc7220b2fa39a8cff336`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-26F60AE4DD5E","canonical":true,"claim_ids":["C-ACCESSIBLE-STRESS-FACE-DICHOTOMY","C-SEVEN-SITE-TAGGED-STRESS-MASS-REGRESSION"],"claim_statuses":{"C-ACCESSIBLE-STRESS-FACE-DICHOTOMY":"canonical","C-SEVEN-SITE-TAGGED-STRESS-MASS-REGRESSION":"regression"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: accessible stress-face dichotomy

**Date:** 2026-10-08
**Audit base:** `origin/main=b1b7d627651f8a6b9d2bcce8750c139d9eaaaec8`, state `2026-10-08.audit.165`.
**Frozen source branch:** `research/level-i-closure-20261007` at `12f6833725f281ce39a6d04ebcb45630b3a6768f` (9 main-only / 24 branch-only commits at refresh).
**Candidate commit:** `3f753f5f9bcc09442c0649383255937a4b77ada3`.
**Source report SHA-256:** `76cf36122cc622b407a6d66ac5bccd675068fc58be99ad471204c1eb69cbd2b4`.
**Source verifier SHA-256:** `195f076d5580bbe082c732ab578f6e2a6d16eb624fb538d3980cb621dc5cecca`.
**Shared exact-arithmetic helper SHA-256:** `179f20fb42827f6b3aa3b7afa5b982b16ff4da49abb77373edaf1a48bd514252`.

The report and verifier are unchanged at the refreshed branch tip. The research branch was not modified. The candidate report was authored against state `.147`; all imported premises below were checked in the `.165` authority stack.

## Verdict

- **PASS — promote `C-ACCESSIBLE-STRESS-FACE-DICHOTOMY`**, with the finite-source deletion conclusion explicitly requiring a nonempty retained source. The result does not prove that an accessible loaded set exists.
- **REGRESSION VALID — promote `C-SEVEN-SITE-TAGGED-STRESS-MASS-REGRESSION`** at its exact triangle-containing, nonglobal scope.
- **CONDITIONAL ONLY:** the report's grid-access application remains conditional on the separate unreviewed uniform-cell/global-diameter-access candidate. No grid extraction or bound `b_0<=eta D` is promoted here.
- C-II and Level I remain open; the canonical source-move/payment obligation is unchanged.

## 1. Exact canonical inputs and scope

I checked current `docs/targets/target-c/57-zr-zf-rigidity-audit.md`, Section 64, the current theorem-state entries `C-EXTREME-TRANSFER`, `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE`, and `C-LOADED-KKT-DIAMETER-SUPPORT-TRANSVERSAL`, and the current full-source scope rule. The active source is the contact-minimal, then diameter-pair-minimal triangle-free C-II representative with `D>=9`. Its nonisolated positive-contact core `V` carries the normalized stress polytope `P` and has `dim_aff(P)=s_Z`. Contact-isolated labels remain in the full source and are not assigned core coordinates by Section 57.

Let `B` be the loaded endpoints of the canonical active diameter set `H`. For any supplied `W subset B`, define `f_b(x)=sum_{e in H, e incident to b} beta_e`, `F_b={x in P:f_b(x)=0}`, and `P_0=intersection_{b in W}F_b`. Each `f_b` is nonnegative on `P`, so each `F_b` is a face. Put `b_0=|H[B\\W]|`, the number of active diameter edges with both endpoints outside `W`.

The promoted finite dichotomy is:

1. If `P_0` is empty, there is `U subset W` with `|U|<=s_Z+1` such that every normalized source stress has positive diameter support incident to `U`. If deleting `U` leaves at least one label, the reduced **full source** has a strict first motion opening every retained actual unit contact and shortening every retained actual old-`D` pair. All contact isolates remain present.
2. If `P_0` is nonempty and `1<=b_0<=D`, every extreme point `x_*` of `P_0` is an extreme point of `P` and its Section 64 circuit defect obeys

   `sigma_* >= D*cos((b_0-1)*asin(1/(2D))) - (b_0+1)/2`.

   Thus `b_0<=eta D`, for fixed `0<eta<1`, forces `liminf sigma_*/D >= cos(eta/2)-eta/2`; if `b_0=o(D)`, then `sigma_*/D >= 1-o(1)`.

When `b_0>D`, branch 2 gives no quantitative defect bound. The conclusion does not supply a refill packet or restore the deleted labels.

## 2. Independent reconstruction of the empty-face branch

The affine hull of `P` has dimension `s_Z`. Helly's theorem applies to the finite family of closed convex faces `{F_b:b in W}` in that affine space. If their total intersection is empty, some subfamily indexed by `U subset W`, `|U|<=s_Z+1`, already has empty intersection. Equivalently, every normalized stress has positive beta mass on an active diameter edge incident to `U`.

Suppose the retained full source had a normalized KKT stress on its complete actual contact and old-`D` rows. Extend its coefficients by zero on every row incident to `U`. This is a normalized equilibrium stress of the original source with zero beta mass at every vertex in `U`, hence a point of `P_0`, contradiction. The canonical weak-diameter-row convention is respected: any stress on a previously weak old-`D` row would zero-extend to a full-source stress making that row nonweak, so no such row is silently omitted from this argument.

The current finite KKT/strict-motion alternative then supplies a velocity on all retained source coordinates. Since all retained active rows are strict in the desired direction and every other pair has strict slack, finiteness and continuity give one sufficiently small positive straight step with all retained pairs above one and below the old `D`. This is only a reduced-cardinality strict endpoint. The nonempty-retained-source condition is necessary and was retained explicitly. Contact-isolated labels are neither removed nor treated as stress variables.

## 3. Independent reconstruction of the nonempty-face branch

An intersection of exposed faces is a face of `P`; every extreme point of `P_0` is therefore extreme in `P`. For `x_* in P_0`, no positive diameter edge of `x_*` meets `W`, so its positive diameter support is contained in the induced edge set `H[B\\W]`. Hence its positive diameter-edge count `h_*` satisfies `1<=h_*<=b_0`.

Section 64 gives

`Q_* <= h_* + 2*sigma_* + 1 - 2*D*cos((h_*-1)*a_D)`,

where `Q_*>=0` and `a_D=asin(1/(2D))`. Rearranging yields

`sigma_* >= D*cos((h_*-1)*a_D) - (h_*+1)/2`.

For `1<=h_*<=b_0<=D`, the right side decreases with `h_*`: `(D-1)*a_D<1/2`, since `asin(x)<=x/sqrt(1-x^2)` gives `(D-1)*a_D< (D-1)/(2D*sqrt(1-1/(4D^2)))<1/2`; cosine decreases on this interval, and the affine term also decreases. Substitution of `b_0` proves the displayed bound. Since `a_D~1/(2D)`, division by `D` gives the `eta` limit and the `o(D)` corollary. The rational weakening follows from `a_D<=1/D` and `cos x>=1-x^2/2`:

`sigma_* >= D - (b_0-1)^2/(2D) - (b_0+1)/2`.

Section 64 also gives `kappa_*=2(v-v_*)+sigma_*>=sigma_*`, so the same lower bound applies to excess degeneracy. The proof is an extreme-circuit support bound. It does not extend a selected bar flex over omitted actual rows, eliminate the exceptional face, or establish a full-source finite motion in this branch.

## 4. Exact seven-site regression

The independent exact fixture consists of a unit regular hexagon and its center. Its 21 pairs give exactly 12 unit contacts (six perimeter edges and six spokes), three opposite diameter pairs of length two, and six unit triangles. It is not asserted to be a global minimizer or a triangle-free canonical source.

For a normalized equilibrium stress, let `c` be the common perimeter multiplier and `beta_i` the three opposite-pair diameter multipliers. Equilibrium at the center makes opposite spoke multipliers equal, and equilibrium at each outer vertex gives spoke multiplier `alpha_i=2*beta_i-c`. Thus `sum beta_i=1`, `beta_i>=0`, and `0<=c<=2*min_i beta_i`. The change of variables `w_i=beta_i-c/2` and `w_P=3c/2` makes this exactly a four-vertex simplex: three straight-diameter stresses and one pure-perimeter stress.

The three straight-diameter stress matrices are rank-one PSD squares `(z_i+z_{i+3}-2*z_center)^2`. The perimeter stress is rank three and is twice the orthogonal projection on the outer six coordinates off `span{1,P_x,P_y}`. Any relative-interior mixture has positive coefficients on these four PSD matrices; their common kernel is exactly the three affine scalar modes, so the mixture has rank four. The mixed rigidity matrix has exact rank 11 and `s_Z=3`.

Tag the four endpoints of two diameter pairs. The straight stress on the remaining pair lies in `P_0`. Mixing it with weight `1-3*epsilon` and the other three vertices with weight `epsilon` gives a relative-interior stress for `0<epsilon<1/3`, with every contact and diameter multiplier positive, but tagged beta mass `8*epsilon/3` and untagged mass `1-8*epsilon/3 -> 1`. Therefore relative-interior positivity, PSD, maximal affine kernel, and full mixed rigidity alone do not force stress mass onto a prescribed tagged set. The six unit triangles and absent global-optimality proof are binding scope limits; this is not a regression against canonical triangle-free sources.

## 5. Verifier audit

Inspected the full verifier and its exact-arithmetic helper. Pair geometry, rank elimination, stress matrices, PSD Schur pivots, and rational bounds use exact rational or `Q(sqrt(3))` arithmetic; no floating tolerance is used. Reran the verifier from a detached worktree at the frozen source tip. It passed:

- all 21 source pairs, 12 contacts, three diameter pairs, and six triangles;
- rigidity rank 11, stress-polytope dimension 3, vertex PSD ranks `(1,1,1,3)`, and rank 4 for the tested relative-interior mixtures;
- all 64 tagged endpoint subsets, including 27 with nonempty exceptional faces and maximum minimum transversal 3;
- simplex fixtures of dimensions 1 through 6, cube fixtures of dimensions 1 through 4, and rational defect bounds for `D=10,100,1000`.

These computations certify only the finite fixture and encoded abstract polytopes. They do not prove Helly's theorem, the Section 64 inequalities, existence of `W`, grid access, or global optimality; those analytic steps were reconstructed separately above.

## 6. Canonical disposition

Promote the finite-source face dichotomy and the seven-site generic-mass regression under separate theorem IDs. Keep the grid-access corollary conditional on its unreviewed candidate. The source branch and its candidate artifacts remain unchanged. The C-II finite-move/payment obligation and Level I remain open.
