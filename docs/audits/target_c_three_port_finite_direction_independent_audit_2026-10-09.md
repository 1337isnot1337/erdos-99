<!-- theorem-state: {"artifact_id":"ART-B1E2A549A7A2","canonical":true,"claim_ids":["C-THREE-PORT-FINITE-DIRECTION-BOUND"],"claim_statuses":{"C-THREE-PORT-FINITE-DIRECTION-BOUND":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.209 — three-port finite chain direction bound

Date: 2026-10-09. Audit base: `origin/main=37f295d30333509d64d59803d80ddbe307ee3589`, state `2026-10-09.audit.202`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate artifact: Lemma 13.4 in `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.
- Verdict: **PASS — promote** the distinct-anchor theorem as `C-THREE-PORT-FINITE-DIRECTION-BOUND`.
- The separate repeated-anchor variant in the source report is not part of this promotion; it needs its explicit extra cross-pair lower bound.

## Exact theorem

Fix distinct planar anchors `a_0,a_1,a_2` and integers `0<r<s`. Consider unit directions `t` for which there is a translation `z` satisfying

\[
 p_0=z,\qquad p_r=z+rt,\qquad p_s=z+st,
 \qquad |p_0-a_0|=|p_r-a_1|=|p_s-a_2|=1.
\]

There are at most ten distinct directions `t`. Translating all three anchors does not change the direction set. Several translations `z` may occur at one fixed `t`.

## Independent proof reconstruction

Translate `a_0` to zero and put `A=a_1-a_0`, `B=a_2-a_0`. Since the anchors are distinct, `A`, `B`, and `A-B` are all nonzero. For a fixed `t`, subtracting `|z|^2=1` from the other two squared-distance equations gives

\[
 z\cdot(rt-A)=-\tfrac12|rt-A|^2,
 \qquad z\cdot(st-B)=-\tfrac12|st-B|^2. \tag{1}
\]

The determinant of this two-equation system in `z` is

\[
 d(t)=\det(t,C)+\det(A,B),\qquad C=sA-rB.
\]

If `d` vanishes identically on the unit circle, then `C=0`. Thus `A/r=B/s=c`; equations (1) become

\[
 z\cdot(t-c)=-\tfrac r2|t-c|^2=-\tfrac s2|t-c|^2,
\]

so `t=c`. This identity branch contributes at most one direction.

Otherwise `d(t)` has at most two zeros on the unit circle. At every other direction, (1) determines `z(t)` uniquely by Cramer's rule. The denominator is affine in `(t_x,t_y)`, and each numerator coordinate has degree at most two: the right sides of (1) are affine on the unit circle and the coefficient entries are affine. Clearing denominators from `|z(t)|^2=1` gives a polynomial of degree at most four restricted to the unit circle. Unless it vanishes identically there, it has at most eight roots (equivalently, a nonzero trigonometric polynomial of degree at most four has at most eight zeros). Including the at most two singular directions gives the bound ten.

It remains to exclude the identity case for `|z(t)|^2=1`. Here `C` is nonzero. Taking `s` times the first equation of (1) minus `r` times the second shows that `z(t)\cdot C` is affine in `t`. Rotate coordinates so `C` is horizontal; then

\[
 z_x(t)=L(t)=c_0+c_1t_x+c_2t_y
\]

for real constants. Since `z_y` is rational on the unit circle, `1-L^2=z_y^2` is a rational square.

If `L` is constant, any real solution has constant `z_y` as well, so `z` is constant. The identity `|z+rt-A|=1` then forces `A=z` and `r=1`; the third distance identity forces `B=z` and `s=1`, contradicting `r<s`.

If `L` is nonconstant, each of the two distinct level lines `L=1` and `L=-1` meets the complexified unit circle with even intersection multiplicity, because `1-L^2` is a rational square and the two factors have no common zero. A line has two intersections with the circle counting multiplicity, so each must be tangent. Their tangency equations are

\[
 (c_0-1)^2=c_1^2+c_2^2=(c_0+1)^2,
\]

hence `c_0=0` and `c_1^2+c_2^2=1`. It follows that `1-L^2` is the square of the perpendicular linear coordinate on the unit circle, and therefore `z(t)=Ot` for one fixed orthogonal matrix `O`.

Put `M=O+rI`. The first distance identity becomes

\[
 |Mt-A|^2=1\quad\text{for all }|t|=1.
\]

Its second Fourier harmonic forces `M^TM` to be scalar, and its first harmonic forces `M^TA=0`. A reflection has `M^TM=(1+r^2)I+2rO`, which is not scalar, so `O` must be a rotation. The matrix `O+rI` is invertible unless `r=1` and `O=-I`. In the invertible cases `A=0`, contrary to distinct anchors. In the exceptional case, the third identity has matrix `(s-1)I`, which is invertible since `s>=2`, and forces `B=0`, again impossible. Thus the norm identity cannot hold identically.

The degree count and identity exclusion prove at most eight regular solutions plus at most two singular directions, without a numerical root count.

## Hostile scope and regression checks

- Singular determinant directions were counted separately even if the linear system admits many translations there; they contribute directions, not solutions `z`.
- The identity-determinant branch was handled independently and contributes at most one direction.
- Constant and orthogonal rational identity branches were both checked against the distinct-anchor hypothesis and `r<s`.
- No pairwise lower bound between chain sites and anchors is assumed in this theorem. The repeated-anchor extension is not included; its source-side extra lower bound may not be dropped.
- This is an exact finite direction theorem only. It does not prove an actual source chain exists, create a motion, or imply a global diameter improvement.

## Dependencies and verifier boundary

- Dependencies: none.
- No dedicated computational verifier is claimed. The proof uses exact algebraic identities and the finite degree-four root count; numerical root sampling is not used.

**Frontier effect:** none. No C-II branch or Level-I quantifier is eliminated.
