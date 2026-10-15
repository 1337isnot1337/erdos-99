<!-- theorem-state: {"artifact_id":"ART-3DBF8E489012","canonical":true,"claim_ids":["C-CANONICAL-LOADED-WALK-STRAIN","C-LOADED-WALK-DIRECTIONAL-STRAIN"],"claim_statuses":{"C-CANONICAL-LOADED-WALK-STRAIN":"canonical","C-LOADED-WALK-DIRECTIONAL-STRAIN":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C Audit.203 — directional strain on actual loaded boundary walks

Date: 2026-10-09. Audit base: `origin/main=2b98ec79a1b219d9476a7a879e0aaacd8bc8fcf4`, state `2026-10-09.audit.196`.

## Frozen candidate and verdict

- Source branch: `origin/research/level-i-fused-review-20261009`.
- Frozen source commit: `6132201c1d3056ca68a222217094acb819f5b4d7`.
- Candidate report: `docs/reports/target_c_global_inverse_phase_face_tail_exclusion_2026-10-09.md`, SHA-256 `2a2c12e3b63e9b0295e1106eda89b68449ed1b37a14d114a8e24d6e5f7e73bcd`, Section 8.
- Verdicts: **PASS — promote** the general loaded-endpoint walk theorem `C-LOADED-WALK-DIRECTIONAL-STRAIN`; **PASS WITH NARROWED SCOPE — promote** its exact canonical core and Type-II cell applications as `C-CANONICAL-LOADED-WALK-STRAIN`.
- Sections 9 onward of the source report remain unreviewed here.

## Exact general theorem

Let `A_D` be any sequence of noncollinear global minimum-diameter unit-separated sources with `D -> infinity`. Let `S` be a subset of its actual diameter endpoints, with `a` distinct members in convex cyclic order. Suppose a closed walk of actual unit-contact edges encounters one chosen occurrence of every point of `S` in that order; repeated vertices and bridge occurrences are allowed.

Let `Lambda=t+Z u+Z v`, where `|u|=|v|=1` and `angle(u,v)` lies in `[pi/3,2pi/3]`. Define `U(Lambda)={z in Lambda: |z|=1}` and, for each unit step `w`,

\[
d_\Lambda(w)=\min_{z\in U(\Lambda)}|w-z|,
\qquad
A_\Lambda=\sum_{\text{walk steps }w}d_\Lambda(w),
\]

with occurrences counted. The lattice and its orientation may vary with `D`. For every fixed `gamma>0`, if `a>=gamma D`, then for all sufficiently large `D`, uniformly over the lattice basis and orientation,

\[
A_\Lambda\ge\kappa(\gamma)D,
\]

where one valid explicit choice is

\[
M=\lceil32/\gamma\rceil+1,\quad N_M=4(M+1)^2,\quad
\epsilon_0=\min\{1/32,\gamma/(32N_M)\},\quad
\kappa(\gamma)=\gamma\epsilon_0/2.
\]

This theorem is a source-geometry statement. It does not assume C-II, triangle-freeness, a positive contact stress, a global phase, or a face-tail bound. It applies to actual diameter endpoints and actual unit-contact walks in the full source.

## Independent reconstruction

### Diameter endpoints have strict full-source normals

For every actual diameter endpoint `p`, choose an actual partner `p'` at distance `D` and set

\[
m_p=(p+p')/2,\qquad n_p=(p-p')/D.
\]

For every distinct source point `x`, `|x-p'|<=D` and expansion of the square gives

\[
p=m_p+(D/2)n_p,
\qquad n_p\cdot(x-p)\le-|x-p|^2/(2D)<0.
\tag{1}
\]

Thus `n_p` is a strict supporting normal of the full-source hull, including contact isolates. Canonical `C-FS-GEOM` gives the uniform midpoint localization `|m_p-o|<L_D`, where

\[
\eta_D=3^{1/4}\sqrt D,\qquad L_D=\sqrt{D\eta_D+\eta_D^2}=o(D).
\tag{2}
\]

### Normal-window count

Fix an oriented normal window of half-width `t<pi/2` and let `J n_0` be its central tangent. For selected endpoints whose chosen normals lie in the window, the tangent projections of the endpoints lie in an interval of length at most `D sin(t)+2L_D`, by (1) and (2). In the corresponding convex boundary chain, each forward chord has length at least one by source separation and direction within `t` of `J n_0`; it advances tangent projection by at least `cos(t)`. Hence the window contains at most

\[
1+\frac{D\sin t+2L_D}{\cos t}
\tag{3}
\]

selected endpoints. Strict support normals occur in the same cyclic order as their hull points. Intervening hull vertices do not alter the projection bound.

### Finite walk inequality

For fixed `M>=1`, `0<epsilon<=1/8`, put

\[
t=2\epsilon+(4M+8L_D)/D,
\qquad N_M=4(M+1)^2.
\]

When `t<=1/4`, I reconstruct

\[
a\le {\pi D\over M}+{A_\Lambda\over\epsilon}+2
 +N_M(4D\epsilon+8M+20L_D+1).
\tag{4}
\]

For each oriented unit step, choose a nearest unit vector of `Lambda`, form reference lattice prefixes `ell_j`, and set `g_j=p_j-ell_j`. The variation of `g` along the walk is exactly `A_Lambda`. Partition the prefix indices by `floor(TV(g_0,...,g_j)/epsilon)`. There are at most `floor(A_Lambda/epsilon)+1` bins; within one bin, all displacement values differ by less than `epsilon`.

At most `pi D/M` cyclic chords of `S` have length greater than `M`, since `per(conv S)<=pi D`. Charge the cyclic closing chord separately: the reference prefixes need not close, so no holonomy assumption is made. Any other chord of length at most `M` whose endpoint occurrences are in one bin differs by less than `epsilon` from a nonzero vector `z` of `Lambda`, with `|z|<=M+epsilon`. Nonzeroness follows from `|w|>=1` and `epsilon<=1/8`.

The shortest nonzero vector of this unit-rhombic lattice class has length one: the Gram matrix has least eigenvalue at least `1/2`, so integer coordinate vectors with squared norm at least three have lattice norm squared at least `3/2`; coordinate squared norm one gives a basis vector, and the four vectors of coordinate squared norm two have norm squared at least one. Disjoint radius-`1/2` disks therefore bound the number of possible `z` by `4(M+epsilon+1/2)^2<=N_M`. For a short chord `w=q-p`, midpoint localization gives

\[
|n_p-n_q|\le(2M+4L_D)/D.
\]

Let `delta=(2M+4L_D)/D`. The support inequalities (1) have opposite signs on `w`, so `n_p·(w/|w|)<0<n_q·(w/|w|)` and `|n_p·(w/|w|)|<=|n_p-n_q|<=delta`. Therefore `n_p` is within angle `arcsin(delta)<=2delta=(4M+8L_D)/D` of one of the two normals to `w` for all sufficiently large `D`. Since `|w-z|<epsilon` and `|w|=1`, the angle between `w` and `z` is at most `arcsin(epsilon)<2epsilon`. Each good chord starts at an endpoint in a normal window of half-width `t` centered at `Jz/|z|` or its opposite. Symmetry under `z -> -z` means the number of distinct windows is at most `N_M`, not `2N_M` beyond that. Formula (3), with `sin(t)<=t` and `1/cos(t)<=2`, bounds each window by `4D epsilon+8M+20L_D+1`.

Among the non-closing cyclic intervals, endpoints in different bins force the nondecreasing prefix variation to cross a distinct multiple of `epsilon`; there are at most `floor(A_Lambda/epsilon)` such crossings. Charge the cyclic closing chord separately, whether or not its endpoint occurrences lie in one bin. Every remaining good chord has a distinct starting endpoint. Counting long chords, threshold crossings, the closing chord, and normal windows proves (4), with the displayed `+2` allowing the integer endpoint convention.

For fixed `gamma`, choose `M,epsilon_0` above. The long-chord term in (4) is less than `gamma D/8`; the `4N_M D epsilon_0` term is at most `gamma D/8`; and the terms involving `L_D` and the fixed constants are at most `gamma D/4` for sufficiently large `D`. Since `a>=gamma D`, rearrangement gives `A_Lambda>=gamma epsilon_0 D/2`. The window condition `t<=1/4` also holds eventually. This proves the uniform theorem.

## Canonical applications

### Whole positive-contact core

In canonical post-ZF C-II, the core is a connected triangle-free plane contact graph and `C-RHOMBUS-POP` gives `F=conv(B)=conv(V)`. Its outer contact facial walk is a closed actual unit-edge walk visiting all `q` loaded vertices in convex cyclic order. Write `v=|V|`, `e` for core contacts, `h` for actual diameter edges, and `b` for the outer-walk length. If `Q` is the sum of bounded-face degrees minus four, triangle-freeness gives `Q>=0`, and Euler's formula gives `b+Q=4v-4-2e`. `C-ZRF` gives `e+h>=2v-2` and `h>=ceil(D)`; `C-WOODALL` gives `h<=q`. Thus `b<=2h<=2q`, `q>=D`, and `q<=pi D` by unit separation and the convex perimeter-diameter bound. The general theorem applies with `gamma=1`. Since `b<=2pi D<16D`, for every lattice at least `kappa(1)D/8` distinct physical core contact edges on this walk satisfy

\[
d_\Lambda(w)>\kappa(1)/32.
\]

### Each Type-II harmonic cell

Fix a nonempty Type-II unloaded component `I_r` and its actual loaded attachments `A_r`. The contact graph using only internal contacts of `I_r` and contacts from `I_r` to `A_r` is connected; loaded-loaded contacts are omitted. Harmonic trapping places `I_r` inside `conv(A_r)`, whose vertices are the distinct actual loaded endpoints. Its outer contact facial walk therefore visits every member of `A_r` in convex cyclic order and uses only actual contacts.

For each fixed `c<sin(pi/12)/2`, `C-UNIFORM-HARMONIC-CELL-AREA` gives `a_r=|A_r|>=cD/3` uniformly. `C-ATTACH-CURRENCY` gives `s_r=e_r+t_r-2|I_r|-1>=0`. If `L_r^0` is the contact-only outer walk and `Q_r^0=sum_f(deg(f)-4)` over bounded faces of this triangle-free contact graph, Euler's formula gives

\[
L_r^0+Q_r^0=4a_r-6-2s_r.
\]

Each bounded face has degree at least four, so `Q_r^0>=0`; hence `L_r^0<=4a_r<=4pi D<16D`. Apply the general theorem with fixed `gamma=c/3`. For every unit-rhombic lattice, that cell's actual contact walk has strain at least `kappa(c/3)D`, and at least `kappa(c/3)D/8` distinct internal-or-attachment contact edges satisfy

\[
d_\Lambda(w)>\kappa(c/3)/32.
\]

No loaded-loaded contact is charged in this cell application.

## Hostile scope checks

- The walk and its steps are actual source contacts; no scaffold or virtual chart edges are used.
- The lattice can vary with `D`, and the constants are uniform in its orientation and basis angle.
- Repeated vertices and bridge occurrences are counted in the walk variation. The closing chord is charged separately, so nonzero reference-prefix holonomy is allowed.
- Midpoint localization uses the full-source circumradius theorem. Contact isolates remain in the hull and in the support inequalities.
- The source claim's C-II count `q>=D` needs both canonical inputs: `C-ZRF` supplies `h>=ceil(D)` and `C-WOODALL` supplies `h<=q`. Neither alone is the endpoint lower bound.
- The per-cell corollary uses the actual cell and its attachment set, not an independently chosen loaded subset or selected grid.
- Linear strain yields neither disjoint motions nor a contact-loss payment, finite competitor, C-II closure, or Level I conclusion.

No finite verifier certifies the analytic normal-window and convex-boundary arguments; none is claimed. The finite lattice-point count and constants are reconstructed directly.

**Frontier effect:** none. Every required boundary walk has linearly many contacts at a fixed positive distance from every fixed-orientation unit-rhombic direction alphabet, but no compatible source move or payment follows.

## Promotion transaction

PR #903 head `aa0956eaab93c57af9291075d61c3fec603f9bb5` merged to main as `baa7a450757f39a28a0e44770bc2ffe4d2896f3e`. Protected `state-consistency` run `37960978558` passed, including all 94 registered certificates.
