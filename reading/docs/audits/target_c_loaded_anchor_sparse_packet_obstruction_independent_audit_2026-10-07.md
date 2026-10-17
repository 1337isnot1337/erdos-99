> Generated reading edition · [exact source](../../../docs/audits/target_c_loaded_anchor_sparse_packet_obstruction_independent_audit_2026-10-07.md) · source SHA-256 `926ab2780de971a4e4ff61a4c8401a46e81c7a6a689effabf45d1c7905707cd6`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-CFE5C364285F","canonical":true,"claim_ids":["C-LOADED-ANCHOR-SPARSE-PACKET-OBSTRUCTION"],"claim_statuses":{"C-LOADED-ANCHOR-SPARSE-PACKET-OBSTRUCTION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C loaded-anchor sparse-packet obstruction: independent audit

Date: 2026-10-07. Audit base: `f15e2d830a48c4034a75263527c293cfed92059a` (`2026-10-07.audit.102`).

Source: PR #722 branch `research/target-c-residual-closure-20261005` at the frozen commit `ed535f5a3a45e3921d91a29c38a0cb37f1d27921`. Source artifact: `docs/reports/target_c_loaded_anchor_sparse_packet_release_2026-10-05.md`, SHA-256 `2a1dc181969ca11bd37c349f2ba1a101d4fc2b9c006fefcd4362616effd858e6`.

## Exact statement audited

Let `A` be a canonical triangle-free C-II global minimum-diameter source in contact-minimal, then actual-diameter-pair-minimal form `C=C_*`, `H=H_*`, with `D>=9`. Let `V` be its nonisolated positive-contact core and `B` its actual loaded diameter endpoints. Set

```text
eta_D = 3^(1/4) * sqrt(D)
L_D   = sqrt(D*eta_D + eta_D^2).
```

Delete `R subset A`, where at least one old unit contact is incident to `R`, and insert `Y` with `|Y|=|R|`. Suppose the resulting source `A'=(A\R) union Y` is unit-separated, every distance involving an inserted point is strictly below `D`, and every retained old core vertex incident to a new unit edge belongs to `B`. Let `J` count every unit pair of `A'` having at least one endpoint in `Y`, including pairs within `Y`.

Then

```text
J (J + 2 L_D) >= D/4.
```

In particular, no such replacement exists with `J=0`; in the all-loaded core case a replacement must use at least

```text
J >= sqrt(L_D^2 + D/4) - L_D
  = (1/(8*3^(1/8)) + o(1)) D^(1/4).
```

This statement does not assume that `A'` is triangle-free. It excludes packets touching only loaded retained core vertices; a packet touching an unloaded retained core vertex, creating an inserted-involving diameter pair, or lacking strict inserted upper slack is outside its scope.

## Independent proof reconstruction

The old source's contact isolates are retained in `A'` and are treated as free coordinates during the motion. Canonical `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE` gives strict old lower and upper slack for every isolate-involving pair in `A`; all inserted-involving upper pairs are strict by hypothesis. Therefore every inactive lower pair and every upper pair involving a free coordinate has positive slack at `A'`. Fixed core-core pairs are unchanged.

If `J=0`, `A'` itself preserves cardinality and diameter at most `D`, but removes at least one contact and adds none. If its diameter is below `D`, global optimality fails; otherwise its contact count contradicts contact minimality. Assume henceforth `J>=1` and define the active rows on free coordinates to be exactly the `J` new unit-contact constraints. Old contacts between fixed retained core vertices are not rows of this motion.

Take the union `E+` of supports of all nonnegative equilibrium stresses on those active rows. A finite sum of witnessing stresses has strictly positive coefficient on every edge of `E+` and remains an equilibrium stress. In any component of its positive support, equilibrium at a free vertex says its position is the positive weighted average of its neighbors. A component with no fixed vertex is impossible: a linear functional with a unique maximum at one of its finitely many free positions has strictly positive value on the sum of the incident equilibrium forces. In a component with pins, the grounded discrete maximum principle places every free position in the convex hull of its fixed pins.

Every such pin is a retained loaded core vertex by the hypothesis. For pins `v_i,v_j` in one positive-support component, a simple support path joins them with at most `J` unit edges, so `|v_i-v_j|<=J`. Choose any actual diameter partner `a_i` for each pin and put

```text
n_i = (v_i-a_i)/D,     m_i = (v_i+a_i)/2.
```

By canonical `C-FS-GEOM`, every actual diameter midpoint lies within `L_D` of one common center. Thus `|m_i-m_j|<=2L_D`, and the vector identity

```text
D(n_i-n_j) = 2(v_i-v_j) - 2(m_i-m_j)
```

implies

```text
sin(angle(n_i,n_j)/2) <= (J+2L_D)/D =: rho.
```

If `J(J+2L_D)<D/4`, then `rho<1/(4J)<=1/4`. The pin normals consequently lie in one angular interval of width at most `alpha=2 asin(rho)<pi/2`: lift every normal relative to one pin into `[-alpha,alpha]`; the extreme pair has angle less than `pi`, so its pairwise bound reduces the full interval width to at most `alpha`.

Each `n_i` strictly supports the old full-source hull at `v_i`, since for every other source point `w`, the old-diameter bound `|w-a_i|<=D` gives

```text
n_i dot (w-v_i) <= -|w-v_i|^2/(2D) < 0.
```

For two pins whose normals are ordered in that interval, the chord between them lies strictly between the corresponding quarter-turns of their supporting normals: its dot product has opposite signs at the two supporting endpoints. With the first quarter-turn as horizontal axis, every pin chord therefore has transverse component at most its length times `sin(alpha)`. Since each chord has length at most `J`, the pins lie in a common strip of width

```text
w <= J sin(alpha) <= 2J rho < 1/2.
```

The harmonic free positions lie in their pin convex hull and hence in the same strip. A one-pin component collapses all its free positions to the pin and is incompatible with unit edges. In every other positive-support component, a free vertex has at most one unit neighbor on either horizontal side: if two distinct unit neighbors were on the same side, their horizontal separation would be at most `1-sqrt(1-w^2)`, their transverse separation at most `w`, and their squared mutual distance at most

```text
(1-sqrt(1-w^2))^2+w^2 = 2-2sqrt(1-w^2) < 1,
```

contrary to source unit separation. Positive equilibrium rules out degree one. Every free vertex in `E+` therefore has degree two, and its two unit-edge vectors are opposite with equal stress weights. The positive support decomposes into straight chains between fixed pins; a free cycle is impossible by the same extreme-point argument.

The elementary polyhedral alternative supplies a velocity `u_0` with every active row nonnegative, every row outside `E+` strictly positive, and every row in `E+` zero. Indeed, if an outside row vanished on the cone of nonnegative row evaluations, its negative would lie in the cone generated by all rows and would give a nonnegative equilibrium stress containing that row, contradicting the definition of `E+`. Summing one witness per outside row makes all those evaluations strictly positive at once.

Perturb `u_0` within the kernel of the `E+` rows, sufficiently little to keep all strict outside evaluations positive. On each straight positive-support chain, perpendicular velocities of its free vertices are independent kernel coordinates. Thus for every `E+` edge the condition that its relative velocity vanish is a proper linear subspace. A generic choice outside the finite union of these subspaces gives `u_i-u_j != 0` on every positive-support edge while preserving the strict outside evaluations.

Move each free point linearly as `p_i(t)=p_i+t u_i` and keep all pins fixed. On an active squared-distance row,

```text
|p_i(t)-p_j(t)|^2 = 1 + t*(A_L u)_e + t^2*|u_i-u_j|^2.
```

Rows outside `E+` open linearly; rows in `E+` open quadratically with a strictly positive coefficient. Every new contact disappears for all sufficiently small `t>0`. The finite inactive lower and strict upper margins persist. Contact isolates remain among the moving coordinates throughout; none is dropped or used as a stress vertex unless it acquires a new edge in `A'`.

The endpoint has the same cardinality, is unit-separated, and has diameter at most `D`. It has no contacts involving a free point; its remaining contact graph is the induced subgraph of the old triangle-free contact graph on retained core vertices. At least one old contact incident to `R` was removed. If the endpoint diameter is below `D`, global optimality is contradicted; otherwise it is a triangle-free global minimizer with fewer contacts, contradicting contact minimality. Therefore the strict inequality `J(J+2L_D)<D/4` is impossible, proving the necessary bound.

Finally, solving `J(J+2L_D)>=D/4` gives the displayed square-root threshold. Since `L_D=3^(1/8)D^(3/4)(1+o(1))`, rationalization yields the asymptotic coefficient `1/(8*3^(1/8))`.

## Adversarial scope and disposition

- `C-FS-GEOM` is used only for the common-center bound on **actual** diameter midpoints. The canonical C-II source is noncollinear; the source geometry result is not applied to a scaffold or stress graph.
- The noncollinearity follows in this regime: a collinear unit-separated `n`-point source has `D>=n-1`, while the canonical strict triangular-lattice comparison gives `D^2<(2*sqrt(3)/pi)(n-1)<=(2*sqrt(3)/pi)D`, impossible for `D>=9`.
- `C-GENERIC-ISOLATE-ANCHOR-AVOIDANCE` supplies strict upper slack for retained source isolates under `C=C_*`, `H=H_*`. All those points remain in the finite motion.
- The abstract `C-KKT-CAGE-FIRST-ORDER-FINITE-RELEASE-REGRESSION` does not refute this claim: its chart has no Euclidean source geometry or straight-chain perpendicular kernel. Here the quadratic release coefficient is explicitly `|u_i-u_j|^2>0` on every positive-stress edge.
- The theorem creates no packet and proves no population or contact capacity. It does not move fixed core pins, cover packets that touch an unloaded retained core vertex, or handle inserted-involving pairs at distance `D`.
- It does not prove C-II or Level I closure. It only excludes bounded-`J` replacements in the all-loaded shell as `D` grows; a source-realized packet of growing contact budget, a move through an unloaded core anchor, or a different competitor remains necessary.

**Verdict: PASS WITH NARROWED SCOPE — promote** `C-LOADED-ANCHOR-SPARSE-PACKET-OBSTRUCTION` with the exact strict-upper, no-unloaded-core-anchor hypotheses above. No numerical verifier is claimed; the geometry, cone alternative, and finite straight motion are proved analytically.

## Repository validation

The source contains no theorem-specific verifier to rerun. Before promotion, the artifact index regenerated 1,263 records, generated theorem views refreshed, `check_theorem_state.py` and `check_active_route_summaries.py` passed, the 16 theorem-state tooling unit tests passed, all 70 registered theorem certificates passed, and `git diff --check` passed. These checks validate repository consistency; they are not used as substitutes for the proof above.
