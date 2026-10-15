<!-- theorem-state: {"artifact_id":"ART-658205CD4E3D","canonical":true,"claim_ids":["C-ALL-BRANCH-HULL-TRAIN-DEPLETION","C-FS-DIAMETER-MIDPOINT-D2-3"],"claim_statuses":{"C-ALL-BRANCH-HULL-TRAIN-DEPLETION":"canonical","C-FS-DIAMETER-MIDPOINT-D2-3":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent audit of the sharper midpoint bound and quantitative hull-train depletion

Date: 2026-10-09  
Audit base: `origin/main` `d9e88fffc427926b71aa5435ab4acb14cf1bef17`, state `2026-10-09.audit.199`  
Frozen source: `origin/research/level-i-fused-review-20261009` at `6132201c1d3056ca68a222217094acb819f5b4d7`  
Source artifact: Sections 11.1–11.3 of `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`.

## Claims and verdicts

**PASS — promote `C-FS-DIAMETER-MIDPOINT-D2-3`.** For every noncollinear global minimum-diameter unit-separated source with `D>=7`, every circumcenter `o` of its full-source convex hull `K`, and every actual diameter pair with midpoint `m`,

\[
|m-o|\le 7D^{2/3}.
\]

Consequently, for `D>=21952`, the maximum degree in the full actual diameter graph satisfies

\[
\Delta(H)\le56D^{2/3}+1.
\]

The midpoint proof is universal over global minimizers. It retains all source points, including contact-isolated points. The degree estimate uses the same midpoints and actual partner points.

**PASS — promote a quantitative strengthening of `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`.** For every unbounded canonical post-ZF C-II sequence in either exhaustive global branch, with all source points retained and `D\to\infty`, the existing definitions of `R_H`, `N_0`, `R_4`, `P_F`, `q`, `k`, `x_B`, `m_H`, and `\mu_D` satisfy

\[
R_H=O(D^{5/3}),\qquad N_0\ge2\sqrt{R_4}-O(D^{5/6}),
\]

and the Audit.204 ledger consequences sharpen to

\[
5(q-k)+x_B+m_H+2\ge3P_F+2\sqrt{R_4}-O(D^{5/6}),
\]

\[
4\mu_DD\ge2P_F+2\sqrt{R_4}+k+3m_H-O(D^{5/6}).
\]

The constants are universal for canonical C-II sources. This is an asymptotic error estimate, not a finite zero-error statement. It deletes only auxiliary train-graph edges/vertices and gives no capacity, source move, strict-D competitor, C-II closure, or Level-I conclusion.

The Section 11.3 matching and odd-cycle lower bounds are **PASS — already subsumed** by the canonical square-root matching and odd-girth results; they are not separately promoted. The stronger maximum-degree corollary is retained with its exact finite threshold above.

## Independent proof of the midpoint bound

Let `R,r` be the circumradius and inradius of `K`; use the canonical full-source geometry `D/2<=R<D/2+eta`, `R-r<eta`, `eta=3^(1/4)sqrt(D)`, `P<=pi D`, and

\[
A(K)>\pi D^2/4-c_0P,\qquad c_0=\sqrt3/4.
\]

Translate the minimum-enclosing-circle center `o` to zero. If `o'` is an incenter, then `|o'|+r<=R`, so `|o'|<eta`. The support function therefore obeys

\[
D/2-2\eta<h\le D/2+\eta,
\]

and `g=h-D/2` has `|g|<=2eta` and `\int g<=0`, since `\int h=P` and `P<=pi D`. For a polygon the distributional Minkowski formula `2A=\int(h^2-(h')^2)` follows by integration by parts from its curvature measure. Hence

\[
\begin{aligned}
\int(h')^2
&=\int h^2-2A\\
&\le\pi D^2/2+8\pi\eta^2-2A\\
&<8\pi\eta^2+2c_0\pi D
=\frac{17\pi\sqrt3}{2}D=:C_ED.
\end{aligned}
\]

For `D>=7`, `R<=D`, and `h''+h` is a nonnegative curvature measure. Thus `h''>=-D` distributionally. At any differentiability point with `h'=s>0`, this forces `h'(\theta+t)>=s-Dt` for almost every `0<=t<=s/D`. Since `|h'|<=R<=D`, this interval has length at most one, and

\[
\frac{s^3}{3D}\le\int(h')^2<C_ED.
\]

For `s<0`, apply the same argument backwards. Therefore `|h'|<(3C_E)^{1/3}D^{2/3}<6D^{2/3}`; the last inequality follows from `C_E<187/4`, using `pi<22/7` and `sqrt(3)<7/4`. For a polygon, `h'` is differentiable inside each strict vertex normal cone and has only upward jumps at side normals. Each actual diameter normal strictly exposes its endpoint: for `n=(p-p')/D` and every other source point `x`,

\[
n\cdot(x-p)\le-|x-p|^2/(2D)<0.
\]

Thus the derivative estimate applies at the diameter normal, even with contact-isolated points present.

For `m=(p+p')/2`, the support values satisfy

\[
h(n)+h(-n)=D,\qquad |m\cdot n|\le\eta,
\]

and the tangential coordinate is `m\cdot Jn=h'(n)`, so `|m\cdot Jn|<6D^{2/3}`. Finally,

\[
|m|^2<36D^{4/3}+\sqrt3D<38D^{4/3}<49D^{4/3}
\]

for `D>=7`. This proves the stated midpoint radius.

For the degree consequence, every actual diameter partner `q` of a fixed source point `p` obeys

\[
|q-(2o-p)|=2|m-o|\le14D^{2/3}.
\]

The partners lie on the circle of radius `D` centered at `p`. Their intersection with that ball is one circular arc of span less than `pi` for `D>=21952`; any two points in the ball have chord length at most `28D^{2/3}`, so that arc has length at most `2D\arcsin(14D^{-1/3})`. When `D>=21952`, `14D^{-1/3}<=1/2`, and `\arcsin x<=2x` gives arc length at most `56D^{2/3}`. Consecutive actual partners are unit-separated, so their arc-length gaps are at least one. The number of partners is at most `56D^{2/3}+1`.

## Independent reconstruction of the quantitative depletion

The Audit.204 proof uses the all-branch normal-window estimate

\[
h_j\le6\epsilon D+120L_D+54
\]

for the number of trains carrying a unit loaded-hull side in one phase bin, where `L_D=o(D)` bounds all actual diameter midpoints. Replacing that coarse localization by the newly audited `L_D=7D^{2/3}` gives

\[
h_j\le6\epsilon D+840D^{2/3}+54.
\]

Take `\epsilon=D^{-1/3}`. Section 68's angular-defect phase cut has `O(D)` deletions. Section 69's coarea bin cut has at most `(3/pi+1/epsilon)Delta` deletions, with `Delta=O(D)` from the promoted angular budget, hence `O(D^{4/3})` deleted train-crossing edges. This estimate remains valid for the D-dependent width because it is the exact bound `(3/pi+D^{1/3})Delta`, not an `O_epsilon(D)` statement with a hidden fixed-epsilon constant.

The full train population obeys `T<=3pi D`. In each retained phase bin, the actual train-crossing graph is simple, so crossing edges incident to hull-ended trains are at most `h_j T_j`. Summing and adding deleted edges gives

\[
R_H\le(6D^{2/3}+840D^{2/3}+54)3\pi D+O(D^{4/3})=O(D^{5/3}).
\]

Deleting `H_L` only from the auxiliary triangle-free train graph leaves `N_0` vertices and `R_4-R_H` edges. Mantel gives

\[
N_0\ge2\sqrt{R_4-R_H}\ge2\sqrt{R_4}-2\sqrt{R_H}
=2\sqrt{R_4}-O(D^{5/6}).
\]

The exact Audit.204 train/face inequalities then give the first scalar bound with the same error. For the second, use the exact loaded-hull slack identity and canonical `c_I=O(\sqrt D)`; this term is absorbed into `O(D^{5/6})`. The error rate is therefore uniform and the statement is valid in both exhaustive branches. The degree, train, and crossing arguments use actual full-source objects, not a selected stress graph, virtual chart, or completion scaffold.

## Hostile checks, scope, and disposition

- The midpoint estimate is for every actual diameter pair, not only positive-stress pairs. Strict support is checked against every other source point, so isolates are retained.
- The full-source area/perimeter inputs are exactly `C-FS-GEOM`; no Type-II hypothesis is used for the midpoint or degree claims.
- The depletion improvement reuses the canonical post-ZF phase-cut/coarea and stopped-train topology in both exhaustive branches. Its only new scale is the full-source `D^(2/3)` midpoint bound.
- The matching lower bound `Omega(D^(1/3))` and odd-cycle lower bound `Omega(D^(1/3))` in the source report are weaker than canonical square-root conclusions and add no new authority.
- No finite certificate checks the analytic support estimate or the asymptotic D-dependent phase-bin argument. The reported claims are analytic; no verifier is asserted to certify them.
- No prompt or live-frontier rewrite is justified. The more explicit all-branch error rate improves the ledger but leaves the required capacity or finite strict-D competitor untouched.

Dependencies for `C-FS-DIAMETER-MIDPOINT-D2-3`: `C-FS-GEOM`.  
Dependencies for the quantitative `C-ALL-BRANCH-HULL-TRAIN-DEPLETION`: `C-FS-GEOM`, `C-LINEAR-NONMATCH`, `C-LOADED-HULL`, `C-RHOMBUS-POP`, `C-PUNCTURED-PHASE`, `C-COHERENT-GRAINS`, `C-TRAIN-INTERFACE-CURRENCY`, `C-NEARBY-DIAMETER-ENDPOINTS-FULL-HULL-SIDE`, and `C-HARMONIC-COMPONENT-SQRT-COUNT`.

**Target C frontier: unchanged. C-I remains closed, C-II remains open, and Level I remains open.** No discovery-worker branch or worktree was modified.
