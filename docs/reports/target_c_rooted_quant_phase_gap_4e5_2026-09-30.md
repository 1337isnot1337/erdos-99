<!-- theorem-state: {"artifact_id":"ART-7227F33EBDD1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- one-lift widening of the rooted quantitative phase window

**Date:** 2026-09-30
**Base:** current main 43c1bd4eb6983578bdd6e7b9633df8fba8eea789 plus the proof-only rooted quantitative phase-gap note on this branch
**Status:** proof-only strengthening; theorem-state authority unchanged
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Statement

Let
\[
A(\lambda)=\lambda+4\lambda\sqrt{1-\lambda^2},
\]
and let \(\lambda_1\) be the current-main root \(A(\lambda_1)=\pi/2\).

Set
\[
\boxed{\sigma_0=4\cdot10^{-5}}
\]
and let \(\lambda_2\in(\lambda_1,1)\) be the unique root
\[
\boxed{A(\lambda_2)=\pi/2-\sigma_0.}
\tag{1}
\]

Then no positive-area locally rhombus-saturated wrapping harmonic-cell limit has
normalized diameter in \([\lambda_1,\lambda_2]\). Therefore the full-core Type-II
branch contains an actual quadratic-area locally rhombus-saturated harmonic cell
\(P_*\) with
\[
\boxed{\operatorname{diam}(P_*)\ge(\lambda_2-o(1))D.}
\tag{2}
\]

For orientation only,
\[
\lambda_2=0.9891361894242655\ldots,
\]
an explicit increase of \(1.5978618649\ldots\times10^{-6}\) above \(\lambda_1\).
The exact root equation (1), not the decimal, is the theorem.

The preceding quantitative note proved the same statement with scalar slack
\(10^{-5}\). The new input here is a one-lift directional-length bound on the main
curved support region. It permits the larger slack \(4\cdot10^{-5}\).

## 2. Defect budget retained from the rooted ledger

Fix a wrapping carrier with normalized diameter \(\lambda\in[\lambda_1,\lambda_2]\) and put
\[
\sigma=\pi/2-A(\lambda)\le\sigma_0.
\]

The perimeter-retaining rooted dissection, the current-main exact outer-walk identity,
the completion-triangle inequality, and the uncapped complement-gap diameter moment
combine to give
\[
\frac{\pi D-P_D}{2}+(P_D-q)+k+\frac12Q_{\rm loc}
+Y+\frac12Z+M\le\sigma D+o(D),
\tag{3}
\]
where
\[
Y=2d_{\rm tile}-(e_{BB}-C_A)\ge0,
\]
\[
Z=\sum_r\bigl(L_r-\operatorname{per}(P_r)\bigr)\ge0,
\]
and
\[
M=S_D-d_w-A(\lambda)D\ge-o(D).
\]

Hence
\[
Q_{\rm loc}\le(2\sigma+o(1))D,
\qquad
Z\le(2\sigma+o(1))D.
\tag{4}
\]
If \(C=\sum_j\sin(g_j/2)\) is the limiting complement-chord sum of the wrapping
support, then the same diameter moment gives \(M\ge(C-A(\lambda))D-o(D)\), so
\[
0\le C-A(\lambda)\le\sigma.
\tag{5}
\]

These are proof-only current-main consequences; no numerical computation is used.

## 3. Gap stability remains valid up to \(4\cdot10^{-5}\)

Put
\[
\theta=2\arcsin\lambda,\qquad \phi=2\pi-2\theta.
\]
Throughout the present interval \(2.8<\theta<2.85\).

Sort the complement gaps and write
\[
g_1=\theta-\delta,\quad
g_2=\phi+x_2,\quad
g_3=\phi+x_3,\quad
\tau=\sum_{j\ge4}g_j.
\]
Let the total complement mass be \(\theta+2\phi+e\). Then
\[
x_2+x_3+\tau=\delta+e.
\tag{6}
\]

The Section-104 concavity transfer uses only the fixed interval
\(2.8\le\theta\le2.85\). Since
\[
\frac{d}{dt}\left[
\sin\frac{\theta-t}{2}+\sin\frac{\phi+t}{2}
-\sin\frac\theta2-\sin\frac\phi2
\right]>0.30
\]
for \(0\le t\le0.1\), equation (5) gives
\[
\boxed{\delta\le\frac{10}{3}\sigma.}
\tag{7}
\]

To bound \(e\), decrease gap mass until the total is exactly
\(\theta+2\phi\), keeping three gaps at least \(\phi\). Section 101 still gives
chord sum at least \(A(\lambda)\). Since every gap is at most \(\theta<2.85\),
\[
\frac12\cos(\theta/2)>\frac1{14},
\]
so deleting total mass \(e\) decreases \(C\) by at least \(e/14\). Thus
\[
\boxed{e\le14\sigma.}
\tag{8}
\]

Therefore
\[
x_2,x_3,\tau\le\frac{52}{3}\sigma,
\qquad
C_{\rm tail}:=\sum_{j\ge4}\sin(g_j/2)<9\sigma.
\tag{9}
\]

The Section-104 fourth-gap argument also gives, for the two support spans adjacent to
the largest gap,
\[
\boxed{s_+,s_-\le\delta.}
\tag{10}
\]

The three principal corridor directions \(q_i\in{\mathbb RP}^1\) consequently obey
\[
\left|
\operatorname{dist}(q_i,q_j)-\frac{\pi}{3}
\right|>0.35
\qquad(i\ne j).
\tag{11}
\]
Indeed the two separations involving \(g_1\) differ from \(\theta/2\) by at most
\(2\delta+e/2\), while the third differs from \(\pi-\theta\) by at most
\(4\delta+e<28\sigma\). At \(\theta>2.8\), the smaller unperturbed margin from
\(\pi/3\) exceeds \(0.352\), and \(28\sigma_0<0.0012\).

## 4. The same two phase families still have \(0.116D\) ends each

The exact circle-gap area formula and (7)-(9) give
\[
\operatorname{area}(\operatorname{conv}S)>0.415
\]
throughout \(\sigma\le\sigma_0\). One quick bound is
\[
\frac{\pi}{4}
-\frac18\left[2.85+2(0.684^3/6)\right]
-6\sigma_0>0.415.
\]
Local rhombic saturation therefore gives more than \(0.40D^2\) strict rhombi for
large \(D\).

As in the preceding quantitative note,
\[
T_D<2.27D.
\tag{12}
\]
Using the canonical phase-defect bound \(<5.317D\), threshold \(5000/D\), one of the
three phase-label pairs has, after a random phase-bin shift, more than
\(0.1326D^2\) same-bin good crossings. If every occupied bin had one shore below
\(0.058D\), simplicity would give at most
\[
0.058D\,T_D<0.13166D^2
\]
crossings. Hence one bin contains two distinct-label train families
\(\mathcal A_D,\mathcal B_D\) with
\[
|\mathcal A_D|,|\mathcal B_D|\ge0.058D.
\tag{13}
\]
Their limiting projective directions \(u_A,u_B\) differ by exactly \(\pi/3\).
Each train has two physical boundary ends, so each family has at least
\[
\boxed{0.116D}
\tag{14}
\]
terminal-edge occurrences.

## 5. One-lift directional length

Only \(5Q_w\le(10\sigma+o(1))D\) train ends can face bounded nonquadrilateral
faces. All other train ends are physical edges on the carrier outer walk; bridge
occurrences are not train ends.

Split the outer walk into routes \(R_i\) between consecutive attachments. If \(b_i\)
is the polygon-base length, \(q_i\) its oriented unit direction, and \(z\) are the
oriented unit route edges, then
\[
\ell_i-b_i=\sum_{z\in R_i}(1-q_i\cdot z).
\tag{15}
\]
Equation (4) gives
\[
\sum_i(\ell_i-b_i)
=L_w-\operatorname{per}(P_w)
\le(2\sigma+o(1))D.
\tag{16}
\]

Fix one phase family and let \(u\) be its limiting direction. Put
\[
\eta=0.068.
\]
Selected endpoints on routes whose base direction is at projective distance at least
\(\eta\) from \(u\) cost at least \(1-\cos\eta-o(1)\) each in (15), so their density is
at most
\[
\frac{2\sigma}{1-\cos\eta}+o(1).
\tag{17}
\]

For the remaining nonprincipal routes, the generic two-lift projective estimate can be
improved. After removing the two tiny support spans from (10), the entire main support
region is contained in an angular interval of length
\[
2\pi-g_1-g_2-g_3-s_+-s_-
\le3\theta-2\pi+\delta<2.3<\pi.
\tag{18}
\]
Hence a projective \(\eta\)-neighborhood has only one oriented tangent lift on this
region. Its circular boundary length is at most
\[
\frac12(2\eta)=\eta.
\]
The tiny spans contribute at most \(\delta\) normalized boundary length, and all tail
gap chords contribute at most \(C_{\rm tail}\). Convex boundary-direction
monotonicity and Hausdorff convergence therefore give total normalized base length
at most
\[
\eta+\delta+C_{\rm tail}+o(1).
\tag{19}
\]
Adding (16), the selected endpoint density on these near-direction nonprincipal routes
is at most
\[
\eta+\delta+C_{\rm tail}+2\sigma+o(1).
\tag{20}
\]

Combining (17), (20), and the bounded-face term gives
\[
N_{\rm off}/D
\le
\eta+\frac{73}{3}\sigma
+\frac{2\sigma}{1-\cos\eta}
+o(1).
\tag{21}
\]

Taylor's inequality gives
\[
1-\cos(0.068)
\ge\frac{0.068^2}{2}-\frac{0.068^4}{24}
>0.002311.
\]
At \(\sigma\le4\cdot10^{-5}\), the right side of (21) is below \(0.104\).
By (14), each phase family therefore has at least
\[
\boxed{0.012D}
\tag{22}
\]
ends on the three principal corridors.

## 6. The route budget is now impossible

Let \(x,y\) be the distances from \(u_A,u_B\) to their nearest principal corridor
directions. If both nearest corridors are the same, then \(x+y\ge\pi/3\). If they are
different, (11) and the projective triangle inequality give \(x+y>0.35\). Thus always
\[
x+y>0.35.
\tag{23}
\]

The two phase labels give disjoint terminal-edge occurrences. Spending the single
route-excess budget (16) on the principal-corridor endpoints from (22) yields
\[
2\sigma
\ge0.012\left[(1-\cos x)+(1-\cos y)\right].
\]
Convexity of \(1-\cos t\) on \([0,\pi/2]\) and (23) give
\[
2\sigma
>
0.024[1-\cos(0.175)].
\tag{24}
\]
But
\[
1-\cos(0.175)
\ge\frac{0.175^2}{2}-\frac{0.175^4}{24}
>0.01527,
\]
so the right side of (24) exceeds \(3.66\cdot10^{-4}\), while
\[
2\sigma\le8\cdot10^{-5}.
\]
Contradiction.

This proves (1)-(2) after the standard Section-88 cap-family transfer.

## 7. Status

This is theorem/proof work. No verifier or numerical search is load-bearing. The
decimal value of \(\lambda_2\) is only an evaluation of the exact root equation.

The exact remaining full-core bottleneck is now the wrapping regime
\(\lambda>\lambda_2\), together with the separate two-half-disk limiting alternative.
The same defect ledger (3) is still the natural currency: a larger window requires
either a stronger train-end lower bound, a sharper support-direction leakage estimate,
or a direct Woodall/topology charge. The macroscopic inactive-container branch is
unchanged.
