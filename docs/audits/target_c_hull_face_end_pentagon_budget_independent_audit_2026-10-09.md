<!-- theorem-state: {"artifact_id":"ART-5399A3459330","canonical":true,"claim_ids":["C-ALL-BRANCH-HULL-FACE-END-BUDGET","C-HULL-TRAIN-FACE-END-NORMAL","C-SHORT-UNIT-POLYGON-DIRECTION-WINDOW"],"claim_statuses":{"C-ALL-BRANCH-HULL-FACE-END-BUDGET":"canonical","C-HULL-TRAIN-FACE-END-NORMAL":"canonical","C-SHORT-UNIT-POLYGON-DIRECTION-WINDOW":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of the all-branch hull-face end and pentagon budget

Date: 2026-10-09  
Audit base: `origin/main` `86b7e894543389efb4221c877b580229580a6946`, state `2026-10-09.audit.200`  
Frozen source: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`  
Source artifact: Sections 12.1–12.4 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.

## Verdicts

**PASS — promote `C-SHORT-UNIT-POLYGON-DIRECTION-WINDOW`.** For a simple closed unit-edge polygon whose vertices are pairwise at least unit-separated, in any oriented edge-direction window of half-width `delta=1/100`, the number of directed edges is at most two when the degree is five or six, and at most `d-4` when the degree `d>=7`. In particular the five-, six-, and seven-edge bounds are `2,2,3`.

**PASS — promote `C-HULL-TRAIN-FACE-END-NORMAL`.** In a canonical post-ZF C-II source, the outward normal of a bounded exceptional-face terminal edge of a hull-ended train agrees with the outward normal of its distinguished unit loaded-hull side. For sufficiently large `D`, that loaded side is a full-source hull side. With coordinates centered at the full-source circumcenter `o`, every point `y` on that side satisfies

\[
y\cdot n\ge D/2-2\eta,\qquad |y\cdot Jn|\le6D^{2/3},
\qquad \eta=3^{1/4}\sqrt D,
\]

so the side normal and radial direction `y/|y|` differ by `O(D^{-1/3})`.

**PASS — promote `C-ALL-BRANCH-HULL-FACE-END-BUDGET`.** Along every unbounded canonical post-ZF C-II sequence in either exhaustive branch, let `E_HF` count bounded physical nonquadrilateral-face terminal occurrences of trains with a distinguished unit loaded-hull end. Let `Q=\sum_F(\deg F-4)` over actual bounded nonquadrilateral contact faces, let `f_5` count actual bounded unit-pentagon contact faces, and use the canonical loaded-hull variables `q,m,k,b,u_B`, where `m` counts nonunit loaded-hull sides and `u_B=b-q-m`. Then

\[
E_{HF}\le Q+f_5+O(D^{5/6}),
\]

and the exact train-end count implies

\[
f_5\ge2(k-m)-O(D^{5/6}),\qquad
q+m\ge4k+u_B-O(D^{5/6}).
\]

The weaker source candidate `E_HF<=2Q+O(D^(5/6))` is already subsumed, since `f_5<=Q`. These are asymptotic bounds with universal constants; they do not assert a finite uniform two-end rule, face capacity for arbitrary packets, a source motion, or C-II/Level-I closure.

## Independent reconstruction

### Direction windows for unit polygons

For any closed unit-edge polygon, if `j` edge vectors lie within `delta` of a unit vector `t`, closure and projection give `j cos(delta)<=d-j`. For `d=5`, three selected edges would give `3cos(delta)>2`; for `d=7`, four would give `4cos(delta)>3`. The same calculation gives `j<=d-4` for every `d>=7`: if `j>=d-3`, then `j>=4`, so `jcos(delta)>=4cos(delta)>3>=d-j`.

For `d=6`, projection first rules out four selected edges. If three are selected, the other three unit vectors `w` satisfy

\[
\sum(1+w\cdot t)\le3(1-\cos\delta)\le\tfrac32\delta^2.
\]

For each remaining vector let `alpha` be its angle from `-t`. Then `1-cos(alpha)<=3delta^2/2`. The source proof's auxiliary estimate `alpha<=sqrt(3)delta` is slightly too sharp. The corrected estimate `alpha<1.75delta` follows because

\[
1-\cos(1.75\delta)\ge (1.75\delta)^2/2-(1.75\delta)^4/24>3\delta^2/2
\]

at `delta=1/100`. Replace the six edges, in their cyclic order, by three `+t` and three `-t` reference steps. Their closed line walk has at most four distinct vertices among its seven partial-sum vertices, so it has a repeated pair other than just the initial/final pair. The sum of deviations over any such segment is less than `3delta+3(1.75delta)=8.25delta<9delta<1`. The corresponding two distinct actual polygon vertices would be less than one apart, contradicting unit separation. Thus at most two directed edges lie in the window. This repairs the numerical slack without changing the lemma.

### Face-end normal agreement

The canonical train-link graph joins opposite unit sides of each strict rhombus. Along a train the transverse edge direction is fixed. Oriented from a bounded terminal face to its loaded-hull end, every step crosses a rhombus toward the same side of the contact-edge line; its midpoint advances in the face-edge outward normal by the rhombus altitude, a positive amount. At the loaded-hull end the preceding edge is inside the full-source convex hull, so the hull's outward normal has the same sign. For a singleton train, the bounded-face edge and the hull side are the same contact edge. Audit.103 promotes every unit loaded-loaded side to a full-source hull side for all sufficiently large `D`.

Theorem `C-FS-DIAMETER-MIDPOINT-D2-3` supplies the support-derivative estimate at the two one-sided limits of a full-source hull side normal. Every point on the side inherits the tangential-coordinate bound by linear interpolation along that side, and the support lower bound is constant there. Since the radial component is at least `D/2-2eta`, the normal-to-radial angular error is `O(D^{-1/3})`.

### Uniform all-branch count

Call a hull-ended train long if its rhombus degree exceeds `D^(5/6)`. Audit.206 gives `R_H=O(D^(5/3))`; the sum of degrees over hull-ended trains is at most `2R_H`, so there are `O(D^(5/6))` long trains. Each has at most one bounded-face end and is charged once to the error.

There are `O(D^(1/6))` exceptional faces with degree greater than `D^(5/6)`: their total excess is at most `Q`, and each such face contributes more than `D^(5/6)-4`; canonical `Q<=2q<=2pi D`. Charge every short-train terminal occurrence on a high-degree face trivially by its degree. Its degree exceeds its contribution `d-4` to `Q` by exactly four, so all these faces contribute at most their share of `Q` plus `O(D^(1/6))`.

This trivial occurrence count is valid because each terminal occurrence on a bounded face uses one of its boundary contact-edge sides. A contact edge is one train-link vertex and belongs to one train; the bounded physical face boundary is simple by the canonical hull augmentation. Thus each face side carries at most one such occurrence, including singleton trains.

On a remaining face, its diameter is at most its degree, hence at most `D^(5/6)`. A short train's face-edge midpoint and loaded-hull-side midpoint are also at distance at most `D^(5/6)`, because each rhombus crossing advances the terminal midpoint by at most one. Thus all loaded-side midpoints associated with one face lie within `O(D^(5/6))` of one another. Their radial normals, and then the corresponding oriented face edges, lie in one window of width `O(D^{-1/6})`, which is eventually less than `2/100`. The face-window lemma bounds the number of short terminal occurrences by `d-4` except for an additional one when `d=5`. Summing small faces, high faces, and long trains gives

\[
E_{HF}\le Q+f_5+O(D^{5/6}).
\]

At most two trains have two good loaded-hull terminal occurrences by canonical train topology. There are `g=q-m` good unit loaded-hull occurrences among the `b` outer-walk occurrences; after removing at most four good ends paired within those two trains, each remaining good end is paired with a distinct bad outer occurrence or a bounded exceptional-face end. Hence

\[
2(q-m)-b-4\le E_{HF}.
\]

Using the exact loaded-hull identity `Q=2(q-k)-b` and `f_5<=Q` gives the `q+m` inequality. Using the sharper `Q+f_5` budget and the same identity gives `f_5>=2(k-m)-O(D^{5/6})`. No sign or positivity of `k-m` is inferred.

## Hostile checks and scope

- Canonical `C-PENTAGON-FIVE-HULL-END-REGRESSION` remains binding: a finite nonglobal pentagonal flower has five incident hull-ended trains. The promotion is asymptotic and pays all long trains using Audit.206; it does not revive the false finite local two-end rule.
- Actual bounded face boundaries are simple convex polygons by canonical Section 67. Their vertices are source points, so pairwise unit separation applies. Contact isolates remain in the full-source support and radial estimates.
- The high-degree face count uses the canonical exact excess `Q`; it assumes no face-degree tail estimate and retains every large face.
- Reran `research/verify_target_c_all_unit_hull_end_currency_2026_10_04.py`: PASS with exact arithmetic on its six listed finite cases, including the pentagonal flower and the retained-isolate variant. Its code checks finite endpoint/incidence ledgers and falsifies a local two-end bound. It does not encode the support estimates, phase-independent face directions, or the asymptotic train/face count.
- The stronger error bounds strengthen canonical quantities `E_HF`, `f_5`, and `q+m` only. They give no packet, source move, strict-D competitor, or Level-I consequence.

Dependencies for `C-SHORT-UNIT-POLYGON-DIRECTION-WINDOW`: none.  
Dependencies for `C-HULL-TRAIN-FACE-END-NORMAL`: `C-FS-DIAMETER-MIDPOINT-D2-3`, `C-LINEAR-NONMATCH`, `C-LOADED-HULL`, `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, and `C-RHOMBUS-POP`.  
Dependencies for `C-ALL-BRANCH-HULL-FACE-END-BUDGET`: `C-SHORT-UNIT-POLYGON-DIRECTION-WINDOW`, `C-HULL-TRAIN-FACE-END-NORMAL`, `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`, `C-LINEAR-NONMATCH`, `C-LOADED-HULL`, and `C-RHOMBUS-POP`.

**Target C frontier: unchanged. C-I remains closed, C-II remains open, and Level I remains open.** This audit used the immutable source snapshot only; no discovery-worker branch or worktree was modified.
