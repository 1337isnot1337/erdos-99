> Generated reading edition · [exact source](../../../docs/audits/target_c_contact_opening_transversal_independent_audit_2026-10-07.md) · source SHA-256 `67aad6b548ca0a3db8fbcfdf2fcc149f315ed106274849142ddeeb3a544897ae`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F3356CCDE30C","canonical":true,"claim_ids":["C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE","C-KKT-CAGE-FIRST-ORDER-FINITE-RELEASE-REGRESSION","C-LOADED-KKT-DIAMETER-SUPPORT-TRANSVERSAL"],"claim_statuses":{"C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE":"canonical","C-KKT-CAGE-FIRST-ORDER-FINITE-RELEASE-REGRESSION":"regression","C-LOADED-KKT-DIAMETER-SUPPORT-TRANSVERSAL":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"mixed","target":"target-c"} -->
# Independent audit: contact-opening KKT transversal

Date: 2026-10-07. Audit base: `f90b9465874cbc783b2dd122a040763218c72914`, state `2026-10-07.audit.86`, Target C C-II open. Frozen source: PR #722 branch `research/target-c-residual-closure-20261005` at `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: `docs/reports/target_c_contact_opening_cage_transversal_2026-10-05.md`.

## Verdict

**PASS — promote the finite KKT / strict-motion alternative and the canonical loaded-diameter-support transversal.** The first is a full-source finite theorem for an arbitrary finite unit-separated configuration. The second is a canonical C-II consequence: any loaded vertex set meeting every positive diameter support of every normalized source stress leaves a reduced source with a velocity that strictly opens all its surviving contacts and strictly shortens all its surviving old diameter pairs.

**REGRESSION VALID — promote the abstract first-order versus finite-release example.** It refutes equality between the strict-negative covector deletion cost and the true nonlinear finite-release cost without making a geometric-source claim.

No finite active-set pivot, refill packet, or same-cardinality sub-`D` competitor follows. The missing card-restoration step remains open.

## 1. Exact audited claims

Let `A` be a finite unit-separated source with diameter `D>1`. For a deleted label set `U`, write `A_U` for the source after deleting those labels, and assume `A_U` is nonempty. Let `C_U` be all actual unit pairs in `A_U`, and let `H_U` be all actual pairs in `A_U` at the original length `D`. For every such pair define covectors on the full velocity space of the retained labels by

```text
lower row for ij in C_U:  a_ij(u) = (p_i-p_j) dot (u_i-u_j)
upper row for ij in H_U:  a_ij(u) = -(p_i-p_j) dot (u_i-u_j)
```

A normalized old-`D` KKT stress on `A_U` is a nonnegative pair of coefficient families `(alpha,beta)` satisfying vertex equilibrium on `A_U` over these retained actual rows and `sum_{h in H_U} beta_h=1`. It need not exist if deletion has already removed every old-`D` pair.

**Finite alternative.** There is a velocity `u` with `a_e(u)>0` for every row indexed by `C_U union H_U` if and only if `A_U` has no normalized KKT stress. When it exists, a sufficiently small positive straight step `p+t u` keeps every pair at least one apart and puts every pair strictly below the old `D`. If the active row set is empty, the reduced configuration already has these strict inequalities and no motion is needed.

Now assume `A` is the canonical contact-minimal then diameter-pair-minimal Target C source with `C=C_*` and `H=H_*`. Write `P(A)` for its normalized KKT polytope and `B` for the loaded diameter-endpoint set. Define

```text
kappa_open(A) = min |U| over U subset B such that
                every s in P(A) has a positive beta edge incident to U.
```

The minimizing `U` can be taken proper: for any loaded endpoint `b`, the set `B minus {b}` meets every actual diameter edge, and `H` is nonempty. Thus `A_U` is nonempty. It has no normalized old-`D` KKT stress and admits the strict first motion above. Every endpoint of an actual diameter pair is an exposed hull vertex, so a stress with no positive diameter reaction incident to a deleted `u in U` cannot have any positive contact reaction incident to `u` either. The source report's support criterion therefore reduces exactly to the displayed diameter-support condition.

With `kappa(H,G)` denoting the minimum deletion size for a common strict-negative direction on the exact-contact tangent, the audited comparison is

```text
kappa_open(A) <= kappa(H,G) <= tau_*(H,G) <= s_Z+1.
```

The first inequality is a stress-pairing argument. The second and third follow from the canonical contact-manifold basis and its `s_Z+1` residual active diameter rows. These costs guarantee an initial strict motion only; they are not packet capacities.

## 2. Independent proof reconstruction

A nonnegative dependence among the signed rows is exactly vertex equilibrium with contact coefficients `alpha>=0` and diameter coefficients `beta>=0`. Pairing that dependence with the position field gives the virial identity

```text
sum_c alpha_c = D^2 sum_h beta_h.
```

If `beta=0`, this forces `alpha=0`, so every nonzero nonnegative row dependence can be normalized to `sum beta=1`. Conversely, every normalized KKT stress is a nonzero nonnegative row dependence. Thus the KKT condition is equivalent to the origin belonging to the convex hull of the signed rows.

If the origin is outside that compact convex hull, choose its nearest point `z`. Projection minimality gives `<z,a_e> >= ||z||^2 > 0` for each row. The velocity dual to `z` strictly evaluates every row positively. This proves the strict alternative without invoking PSD, an exact-contact manifold, or a finite pivot algorithm.

For a finite source step, every original contact has first squared-distance derivative `2a_c(u)>0`, and every old diameter pair has derivative `-2a_h(u)<0`. There are finitely many such rows, so all are strict for one sufficiently small positive time. Every other old pair has strict lower and upper slack; finite continuity preserves those inequalities. The move acts on all retained labels, including contact-isolated labels, which remain in the configuration.

For the canonical support theorem, a normalized stress on `A\\U` extends by zero to a stress on `A` with no positive contact or diameter edge incident to `U`; restriction gives the converse. At a deleted loaded vertex with no positive diameter coefficient, equilibrium contains only nonnegative contact forces. Since the vertex is an exposed extreme point, one strict supporting functional has the same nonzero sign on every vector from that vertex to another source point. Its value on the contact equilibrium is a sum of strictly same-sign terms, so every incident contact coefficient must also vanish. Therefore a surviving-source stress would contradict the definition of `kappa_open`, and the finite alternative supplies the strict motion.

The normalized stress polytope is compact: the virial identity fixes `sum alpha=D^2` and normalization fixes `sum beta=1`. It has finitely many vertices. For fixed `U`, positivity of the total beta mass on edges incident to `U` is a linear functional, so it suffices to check the polytope's extreme stresses; a missed face contains a missed extreme point. This gives a finite support description but no useful enumeration bound or geometric upper bound on `kappa_open`.

For `kappa_open<=kappa`, suppose `U` admits a tangent vector `w` strictly shortening every surviving actual diameter row. A normalized KKT stress on `A\\U`, extended by zero, pairs to zero with `w` by stationarity. Its surviving contact terms vanish because `w` lies in the exact-contact tangent; every positive diameter term is strictly negative, and at least one is positive because `sum beta=1`. Contradiction. The basis bound uses `C-CONTACT-DIAMETER-COORDINATES`: deleting a cover of the `s_Z+1` residual rows leaves only an independent subset of a basis, which admits simultaneous strict-negative evaluation.

## 3. Exact regression: first-order cost is not finite-release cost

Take an abstract one-dimensional chart with active excess functions

```text
ell_1(t)=t,  ell_2(t)=-t,  ell_3(t)=-t^2.
```

The differential rows are `1,-1,0`, have rank one, and admit the positive equal dependence. To make every surviving differential strictly negative, one must delete one of the opposing rows and also the zero row, so the strict-negative deletion cost is two. Yet deleting row 2 and taking `t<0` strictly shortens both remaining excesses, including `ell_3`, quadratically. One deletion suffices for finite release.

This is an exact analytic regression for the inference “first-order strict-negative deletion cost equals finite nonlinear release cost.” It is not a planar unit-contact framework, a global minimizer, or a counterexample to the source-specific KKT theorem.

## 4. Hostile checks and limits

- `C_U` and `H_U` are the complete actual retained contact and old-`D` pair sets. The theorem does not use selected stress rows in place of actual active constraints.
- The first motion is a straight step in the full retained-source coordinates. Contact isolates are retained; their old pair constraints are inactive and persist by finite slack.
- The canonical `kappa_open` step does not preserve original contacts at deleted vertices; it only opens every contact that remains in `A\\U`. No claim is made that the motion extends to a feasible move before deleting `U`.
- The theorem only says the reduced source has diameter below `D`. It has fewer points. No source-realized refill packet restoring `|U|` points is supplied.
- Any packet strict at the original canonical source and already large enough to pay a spare site is excluded by `C-CONTACT-BUDGET-DIAMETER-EXCHANGE-ENDPOINT`. The useful unresolved possibility is a packet whose strict availability is certified only after an actual finite contact-opening motion.
- No first-order inequality is treated as a finite endpoint without the small-time continuity argument. No equilibrium or stress-energy average is substituted for checking all old diameter rows.
- The abstract quadratic chart only refutes a generic linear-to-nonlinear inference; it lacks a Euclidean source realization.

## 5. Dependencies and exact frontier effect

The general finite alternative is proved directly. The canonical transversal application uses `C-ZTA` for full actual contact/diameter normalization and the normalized KKT polytope, `C-ZRF` for the loaded nonisolated-core convention, and `C-CONTACT-DIAMETER-COORDINATES` for the exact-contact tangent and residual-basis bound. It makes no use of contact-isolated coordinates as stress variables. The `kappa_open<=kappa` comparison uses only the stationarity pairing and exact-contact tangent definition.

This promotes an initial strict-opening mechanism and sharpens the discrete support set that must be hit. It does not bound `kappa_open` by a useful number beyond the inherited `s_Z+1`, prove a finite pivot to a packet-rich state, or restore cardinality. The C-II source-capacity and finite-competitor obligation is unchanged.

## 6. Claim disposition

| Claim | Verdict | Scope / disposition |
| --- | --- | --- |
| No normalized retained-source KKT stress iff a strict opening velocity exists | PASS | Promote as `C-FINITE-KKT-STRICT-MOTION-ALTERNATIVE` |
| Loaded-set transversal of every normalized diameter support gives strict motion of the reduced canonical source | PASS | Promote as `C-LOADED-KKT-DIAMETER-SUPPORT-TRANSVERSAL` |
| `kappa_open<=kappa<=tau_*<=s_Z+1` | PASS | Include in the canonical loaded-transversal statement with its recorded dependencies |
| First-order cost equals finite release cost | REGRESSION VALID | Promote as `C-KKT-CAGE-FIRST-ORDER-FINITE-RELEASE-REGRESSION` |
| A finite pivot reaches refill capacity before new constraints obstruct it | UNPROVED | Leave at the research frontier; no pivot or cardinality-restoration theorem |
| C-II or Level I closure | NOT PROVED | Both remain open |

No computational certificate is load-bearing or claimed.
