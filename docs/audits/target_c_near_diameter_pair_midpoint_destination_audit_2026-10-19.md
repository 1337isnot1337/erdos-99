<!-- theorem-state: {"artifact_id":"ART-1B9F2DE82E9E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Destination audit: near-diameter pair endpoint and midpoint localization

## Disposition

**PASS for the stated near-diameter endpoint and midpoint inequalities**, under the canonical full-source geometry hypotheses and the minimum-enclosing-circle convention below. The proof gives explicit bounds for every `s >= 0`; in particular they are uniform for `s` in `[0,2]`, including `s=0` and `s=2`.

This audits only the near-diameter component of `TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947`. It does not audit the companion endpoint-tail/moment or full diameter-edge transfer claims in Audit.246. The destination candidate remains `unreviewed`; this report is evidence for a later lifecycle decision and does not change the theorem state, priority, or canonical manifest. No pair count, stress estimate, atlas, source motion, finite endpoint, C-II closure, or Level-I conclusion follows.

## Exact scope and source pins

- Destination base: `7d0a450fe66991036541023f95c44c064a04b6a8`, tree `db766e0e25b562054df26aeec7e627d5a579dd6d`.
- Theorem state / priority / catalogue: `2026-10-15.publication.2` / `public-frontier.3` / `public-frontier.9`.
- Investigation: `audit-near-diameter-localization-macbook-20261019`; refined scope key `faf91742696c98aa6296d2ef328cf3acc1f69971376012678bf1305140cfa6c8`.
- Candidate: `TARGET-C-NEAR-DIAMETER-PAIR-MIDPOINT-BOUND-PR947`, source PR [#947](https://github.com/1337isnot1337/e-99/pull/947), source head `1afb7e64d47c5619d872d32759b0e01f1526fd5a`, source tree `48b678c0d2695002595dc8aa9eaa6d1ac909e31b`, source base `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`.
- Candidate proof report: `docs/audits/target_c_diameter_midpoint_mean_tail_independent_audit_2026-10-10.md`; source Git blob `16fcb7a8c1e8552f152709fa24fcdb37542061eb`, source SHA-256 `e4bf989843db0d85a6594d4129eed8cc2c59ec3605442d1ba722c2a219c3c4cf`, destination SHA-256 `a815cfd48e4f208a1891b853726897069909704fa0f359dad9f828c12668d797`, destination Git blob `b4266040d3e8004984f9fa090b075f915433ef6a`.
- Source second-referee record: `docs/audits/target_c_midpoint_mean_tail_second_referee_2026-10-10.md`; source and destination Git blob `ae888872f83e4d3520ffe41acaef4f71cc7db600`, source and destination SHA-256 `1a9ab31c0fa492cc56b4c625b279654a69005ad2d531a02da553b707da2a3d52`.
- Canonical dependency report `docs/audits/target_c_midpoint_and_quantitative_hull_train_independent_audit_2026-10-09.md` has destination SHA-256 `cd008165a6d2587f1dcdb03453048ded333ac9c9075cc409d8fc243f4ecb4495`; its `C-FS-DIAMETER-MIDPOINT-D2-3` proof depends on canonical `C-FS-GEOM`, whose geometry audit is `docs/targets/target-c/58-full-source-geometry-audit.md` (SHA-256 `f504349650423786a6091ba9b7a8699cd62b7e6b200d2a2ce3a6a34b3d0b473d`).
- The source SHA-256 values were recomputed from the GitHub contents API at the pinned source head; destination SHA-256 and Git blob values were recomputed from the assigned worktree. The cohort `source-pins.json` is empty, so the source pins above are the exact values recorded in the destination candidate registry and assignment.

The decisive input is canonical `C-FS-DIAMETER-MIDPOINT-D2-3` (scope `D>=7`), depending on canonical `C-FS-GEOM`. The proof uses the support-function derivative bound from that claim; the assigned `D>=216` domain lies inside its scope. The center `o` is the unique center of the minimum enclosing circle of the **full-source hull**. All vectors below are measured from `o`. This is the center used by the canonical dependency; the claim is not asserted for an arbitrary center of a larger containing circle. Every source label, including contact-isolated points, remains in the hull and in the support function.

## Reconstruction of the canonical derivative bound used here

Write `K` for the full-source hull, `h(theta)` for its support function about `o`, `P` for its perimeter, `A` for its area, `R,r` for its circumradius and inradius, and

\[
\eta=3^{1/4}\sqrt D.
\]

`C-FS-GEOM` gives `D/2 <= R < D/2+eta`, `R-r<eta`, `P<=pi D`, and

\[
A>\frac{\pi D^2}{4}-\frac{\sqrt3}{4}P.
\]

Let `o'` be an incenter. Since its inball is contained in the circumdisk, `|o'-o|+r<=R`, hence `|o'-o|<eta`; also `r>D/2-eta`. Thus

\[
D/2-2\eta<h(\theta)<D/2+\eta.
\]

Set `g=h-D/2`. The polygon support formulas give `\int h=P`, so `\int g=P-\pi D<=0`, and `|g|<2eta`. The support-area identity and area lower bound yield

\[
\begin{aligned}
E:=\int_0^{2\pi}(h')^2
&=\int h^2-2A\\
&<D(P-\pi D)+8\pi\eta^2+\frac{\sqrt3}{2}P\\
&\le 8\pi\sqrt3 D+\frac{\pi\sqrt3}{2}D
=\frac{17\pi\sqrt3}{2}D.
\end{aligned}
\]

The cancellation `D(P-pi D)<=0` is needed for this linear energy bound. Since `D>=216`, `D/2+eta<=D`, so `h<=D` and the curvature-measure identity `h''+h>=0` implies `h''>=-D`. If `h'(theta)=u>0` at a differentiability point, then along the next `u/D` radians the derivative is at least `u-Dt` almost everywhere; its positive jumps at hull side normals only help. Therefore

\[
\frac{u^3}{3D}\le E<\frac{17\pi\sqrt3}{2}D,
\qquad |h'|<(51\pi\sqrt3/2)^{1/3}D^{2/3}<6D^{2/3}.
\]

The negative case uses the backward interval. To ensure the ramp interval does not wrap around the circle, note that at differentiability points `h'` is a tangent coordinate of a hull point, so `|h'|<=R<=D`; hence its length `|h'|/D` is at most one radian. The last numerical comparison follows, for example, from `pi<22/7` and `sqrt(3)<7/4`, which give `51*pi*sqrt(3)/2 < 561/4 < 216`. This recovers the derivative part of `C-FS-DIAMETER-MIDPOINT-D2-3` used below. Absolute continuity of the support function then makes this derivative bound a global Lipschitz bound. No support direction is restricted to the positive-contact core.

## Near-diameter endpoint bound

For every noncollinear global minimum-diameter unit-separated source with `D>=216`, take any distinct source points `p,x` with `d=|p-x|>=D-s`, where `s>=0`, and let `nu=(p-x)/d`. Write `J` for rotation by `pi/2` and `h(nu)=h(theta)` for the support in direction `nu`. Define the two support deficits

\[
\delta_p=h(\nu)-(p-o)\cdot\nu,\qquad
\delta_x=h(-\nu)+(x-o)\cdot\nu.
\]

Both are nonnegative. If `w=h(nu)+h(-nu)` is the width of `K` in direction `nu`, then `d<=w<=D`, so

\[
0\le\delta_p+\delta_x=w-d\le D-d\le s,
\qquad 0\le\delta_p,\delta_x\le s.
\]

For `D>=216`, set `epsilon=D^{-1/3}<=1/6`. The support inequality at the tilted normal `nu cos(epsilon)+J nu sin(epsilon)` gives

\[
((p-o)\cdot\nu)\cos\epsilon+((p-o)\cdot J\nu)\sin\epsilon
\le h(\theta+\epsilon).
\]

Using `(p-o) dot nu >= h(theta)-s`, the `6D^{2/3}` Lipschitz bound for `h`, `h(theta)<=D`, `1-cos(epsilon)<=epsilon^2/2`, `0<=cos(epsilon)<=1`, and `sin(epsilon)>=epsilon/2`, the rightward tangent coordinate obeys

\[
\begin{aligned}
(p-o)\cdot J\nu
&\le\frac{6D^{2/3}\epsilon+D\epsilon^2/2+s}{\epsilon/2}\\
&=13D^{2/3}+2sD^{1/3}.
\end{aligned}
\]

Tilting by `-epsilon` gives the same lower bound. At `x`, use direction `-nu` and deficit `delta_x`; since `J(-nu)=-Jnu`, this proves

\[
|(p-o)\cdot J\nu|,\ |(x-o)\cdot J\nu|
\le13D^{2/3}+2sD^{1/3}.
\]

Each inequality is valid for every `s>=0`; no division by `s` occurs. The two signs require opposite tilts, and both are necessary for an absolute-value bound.

## Midpoint normal and boundary cases

The support interval gives `|h(nu)-h(-nu)|<=3eta`. Since

\[
2(m-o)\cdot\nu=h(\nu)-h(-\nu)-\delta_p+\delta_x,
\]

we obtain the slightly sharper intermediate estimate

\[
|(m-o)\cdot\nu|\le(3\eta+s)/2\le2\eta+s/2.
\]

The midpoint tangent coordinate is the average of the two endpoint tangent coordinates, so it has the same `13D^{2/3}+2sD^{1/3}` bound. Thus for fixed `s`, `|m-o|=O_s(D^{2/3})`; the displayed coordinate bounds themselves are uniform for `s` in any fixed bounded interval.

- At `s=0`, `d>=D` and the diameter condition forces `d=D`. Then `w=D` and `delta_p=delta_x=0`. The tangent bound reduces to `13D^{2/3}` and the normal bound to `2eta` (indeed the above intermediate bound gives `3eta/2`). This is also consistent with strict exposure of each actual diameter endpoint: for its partner `x` and every other source point `y`,
  `nu dot (y-p) <= -|y-p|^2/(2D)<0`.
- At `s=2`, each deficit is at most `2`; the endpoint tangent bound is `13D^{2/3}+4D^{1/3}` and the midpoint normal bound is `2eta+1`. All supporting trigonometric estimates still use the same `epsilon=D^{-1/3}` and do not depend on `s`.
- Consequently the constants are uniform over the full interval `0<=s<=2`, which includes the inputs named in PR #124. The exact formula also remains valid beyond that interval for all nonnegative `s`.

## Predecessor comparison, exposure, and limitations

The source PR #947 report records a PASS and proposed promotion for three claims. I have not imported that proposed lifecycle. The destination candidate registry records those bytes as unreviewed. The source second-referee note also records a PASS and clarifies the angular-band window for the separate midpoint-tail count. I saw prior outcome summaries in live PR bodies for #947, #113 and #124 before completing this reconstruction, and I read the source second-referee note afterward for comparison. This is a non-blind review; the inequalities above were reconstructed from the canonical hypotheses, but the prior exposure is part of the record. The earlier destination audit in PR #124 was conditional on these estimates and explicitly left them unaudited.

The endpoint estimates address the near-diameter prerequisite used by the positive-leaf boundary argument in PR #124 (live head `067af10523401461d80a399ef31ba429accc8fc1`, open draft) for `s=0,2`. They do not verify that argument or establish its source-realized move. PR #113 (live head `81de74d4ba5099c8572c1c76f6c28ac80d9c642a`, open) separately assumes the endpoint midpoint-tail/moment estimates when transferring them to every actual C-II diameter edge; that distinct tail/moment proof is outside this audit, so this result does not discharge PR #113's full analytic premise.

There is no finite verifier for the support energy and tilted-normal argument. Repository integrity checks do not certify the analytic proof; their actual outcomes are recorded in the accompanying PR body. The remaining Target C obstruction is still a source-level counting/replacement or finite-motion argument that uses the localization while retaining every label and checking every lower and actual-diameter upper pair. In particular, this audit supplies no count of near-diameter pairs.

The next lemma, if this localization is used further, must either bound the number or extract a source-compatible set of pairs with `d>=D-2` from the canonical full source, or directly build a same-cardinality replacement that checks every pair constraint. The exact quantity this audit controls is endpoint transverse spread (and the midpoint's longitudinal coordinate), which can feed the `K_D` anchor boundary input in PR #124; it does not control pair multiplicity. A successful extraction could make that boundary input useful in a finite-move proof. Without the extraction or replacement, the only consequence remains static localization.

OpenAI Codex (GPT-6 Luna xhigh), worker `macbook-04`, performed this destination audit. It uses the project-authored source and canonical dependencies listed above; no third-party text or code was copied. The contribution is offered under Apache-2.0. Level I, Target A, Target B and C-II remain open; C-I remains closed.
