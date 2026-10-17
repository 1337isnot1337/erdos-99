> Generated reading edition · [exact source](../../../docs/reports/target_c_rooted_quantitative_phase_gap_2026-09-30.md) · source SHA-256 `1aff5c679e08d73a61a38cee6bc97815b485a993b67dedd5cabec69c67f0a439`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-2FEDCA428009","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- explicit quantitative phase gap above the rooted-detour root

**Date:** 2026-09-30
**Base main:** \`43c1bd4eb6983578bdd6e7b9633df8fba8eea789\`
**Status:** proof-only strengthening; theorem-state authority unchanged
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Result

Put
$$
A(\lambda):=\lambda+4\lambda\sqrt{1-\lambda^2}.
$$

Current main proves that every positive-area center-wrapping harmonic-cell limit has
normalized diameter at least the unique root $\lambda_1$ of
$$
A(\lambda_1)=\frac{\pi}{2},
\qquad
\lambda_1=0.9891345915624005433\ldots .
$$

Fix
$$
\boxed{\sigma_0:=10^{-5}}
$$
and let $\lambda_2\in(\lambda_1,1)$ be the unique root
$$
\boxed{
A(\lambda_2)=\frac{\pi}{2}-\sigma_0.
}
\tag{1.1}
$$
Numerically,
$$
\boxed{
\lambda_2=0.9891349910402891632\ldots
}
\tag{1.2}
$$
and
$$
\boxed{
\lambda_2-\lambda_1
=3.994778886199029\ldots\times10^{-7}.
}
\tag{1.3}
$$

Then no positive-area locally rhombus-saturated wrapping harmonic-cell limit has
normalized diameter in $[\lambda_1,\lambda_2]$. Consequently canonical cap-family
transfer gives an actual harmonic cell $P_*$ with
$$
\boxed{
\operatorname{diam}(P_*)\ge(\lambda_2-o(1))D,
\qquad
\operatorname{area}(P_*)\ge c_2D^2
}
\tag{1.4}
$$
for one absolute $c_2>0$, with local strict-rhombus filling ratio tending to one.

The theorem is the exact root equation (1.1). The decimals only evaluate it.

## 2. Retain the complement scalar in the rooted-detour ledger

Let $P_{w,D}$ be a positive-area center-wrapping harmonic-cell sequence with
$$
\frac{d_w}{D}\to\lambda\in[\lambda_1,\lambda_2].
$$
Put
$$
\theta:=2\arcsin\lambda,
\qquad
\phi:=2\pi-2\theta,
\qquad
C:=\sum_j\sin(g_j/2),
$$
where $g_j$ are the complement gaps of the limiting circle support.

The uncapped complement-gap moment used by current main gives
$$
S_D:=\sum_r d_r\ge d_w+CD-o(D).
\tag{2.1}
$$
Canonical Section 101 gives
$$
C\ge A(\lambda)
=\sin(\theta/2)+2\sin\theta.
\tag{2.2}
$$

Write
$$
P_D:=\operatorname{per}(F_D),\qquad
Q_{\rm loc}:=\sum_rQ_r,\qquad
k=d_H+s_Z.
$$
The perimeter-retaining form of the rooted chord-dissection argument gives
$$
\sum_r(p_r-2d_r)\ge P_D-2d_w-o(D),
\tag{2.3}
$$
where $p_r=\operatorname{per}(P_r)$.

The exact aggregate upper ledger is
$$
S_{\rm out}:=\sum_r(L_r-2d_r)
\le
2(q-k-S_D)+4c_I-4-Q_{\rm loc},
\qquad c_I=o(D).
\tag{2.4}
$$

Combining (2.1)--(2.4), using $q\le P_D$, gives
$$
(P_D-q)+k+\frac12Q_{\rm loc}
\le
\frac12P_D-CD+o(D).
\tag{2.5}
$$
Since $P_D/D\to\pi$, define
$$
\sigma:=\frac{\pi}{2}-A(\lambda).
$$
Then
$$
0\le\sigma\le\sigma_0,
$$
and
$$
0\le C-A(\lambda)\le\sigma+o(1),
\tag{2.6}
$$
together with
$$
\boxed{
\frac{P_D-q}{D}\le\sigma+o(1),\quad
\frac{k}{D}\le\sigma+o(1),\quad
\frac{Q_{\rm loc}}{D}\le2\sigma+o(1).
}
\tag{2.7}
$$

There is a second consequence. Since
$$
S_{\rm out}
=
\sum_r(p_r-2d_r)+\sum_r(L_r-p_r),
$$
equations (2.1), (2.3), and (2.4) imply
$$
\sum_r(L_r-p_r)
\le
P_D-2CD-2k-Q_{\rm loc}+o(D).
$$
Therefore
$$
\boxed{
\sum_r(L_r-p_r)\le(2\sigma+o(1))D.
}
\tag{2.8}
$$
Every summand is nonnegative, so the selected wrapping carrier itself satisfies
$$
\boxed{
L_w-p_w\le(2\sigma+o(1))D.
}
\tag{2.9}
$$

This is the quantitative route-excess budget used below.

## 3. Complement-gap stability

Sort the gaps and write
$$
g_1=\theta-\delta,\qquad
g_2=\phi+x_2,\qquad
g_3=\phi+x_3,\qquad
\tau:=\sum_{j\ge4}g_j.
$$
Write the total complement mass as
$$
\sum_jg_j=\theta+2\phi+e.
\tag{3.1}
$$
Then
$$
x_2+x_3+\tau=\delta+e.
\tag{3.2}
$$

The present window lies in $2.8<\theta<2.85$. Indeed
$$
\sin(1.4)+2\sin(2.8)>\pi/2,
$$
while
$$
\sin(1.425)+2\sin(2.85)<\pi/2-10^{-5},
$$
and $M(\theta)=\sin(\theta/2)+2\sin\theta$ is strictly decreasing there.

Let $f(x)=\sin(x/2)$. For $2.8\le\theta\le2.85$ and $0\le t\le0.1$,
$$
\frac{d}{dt}
\left[
f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi)
\right]
>0.30.
\tag{3.3}
$$
The same concavity/majorization transfer as canonical Section 104 first rules out
$\delta\ge0.1$, then gives
$$
\boxed{
\delta\le\frac{10}{3}\sigma.
}
\tag{3.4}
$$

The excess total complement mass is also controlled. Reduce total gap mass by $e$,
preserving three coordinates at least $\phi$, until the total is exactly
$\theta+2\phi$. Since every gap is at most $\theta<2.85$,
$$
f'(x)\ge f'(\theta)=\frac12\cos(\theta/2)>\frac1{14}.
$$
The reduced vector still has chord sum at least $A(\lambda)$ by Section 101, so
$$
C-A(\lambda)\ge e/14.
$$
Thus
$$
\boxed{
e\le14\sigma.
}
\tag{3.5}
$$
Equations (3.2)--(3.5) give
$$
\boxed{
x_2,x_3,\tau\le\frac{52}{3}\sigma.
}
\tag{3.6}
$$
Consequently
$$
\boxed{
C_{\rm tail}:=\sum_{j\ge4}\sin(g_j/2)
\le\tau/2
<9\sigma.
}
\tag{3.7}
$$

## 4. A $0.40D^2$ strict-rhombus core

The exact support-area identity is
$$
\operatorname{area}(\operatorname{conv}S)
=
\frac{\pi}{4}
-\frac18\sum_j(g_j-\sin g_j).
\tag{4.1}
$$
Let $H(x)=x-\sin x$. Since $0\le H'(x)\le2$ on $[0,\pi]$, $H$ is
2-Lipschitz.

Relative to the model vector $(\theta,\phi,\phi)$, padding by zeros for tail gaps,
the $\ell^1$ gap-vector change is
$$
\delta+x_2+x_3+\tau=2\delta+e<21\sigma.
\tag{4.2}
$$
Hence
$$
\operatorname{area}(\operatorname{conv}S)
\ge
\frac{\pi}{4}
-\frac18[H(\theta)+2H(\phi)]
-6\sigma.
\tag{4.3}
$$
For $2.8<\theta<2.85$,
$$
0<\phi<0.684,\qquad
H(\theta)<2.85,\qquad
H(\phi)\le\phi^3/6.
$$
Therefore
$$
\boxed{
\operatorname{area}(\operatorname{conv}S)>0.415.
}
\tag{4.4}
$$

Canonical summed local rhombic deficit is nonnegative and $o(D^2)$, so this
macroscopic carrier itself is locally rhombus-saturated. Since one unit rhombus has
area at most one, its strict-rhombus count $R_D$ satisfies, for large $D$,
$$
\boxed{
R_D>0.40D^2.
}
\tag{4.5}
$$

## 5. Two explicit inverse-phase train families

Let $T_D$ be the number of local carrier train segments. Canonical Sections 82 and
89 give
$$
2T_D=P_R,\qquad P_R\le L+5Q,
$$
and the local face identity gives
$$
T_D\le2a_D+2Q_D.
\tag{5.1}
$$
Section 100 gives
$$
2a_D/D\le3\theta-2\pi+o(1),
$$
and $Q_D\le Q_{\rm loc}$. Thus
$$
\boxed{
T_D<2.27D.
}
\tag{5.2}
$$

Canonical Section 68 gives total acute-angle defect
$$
\sum_R\delta_R<5.317D.
\tag{5.3}
$$
Apply the canonical phase cut, which removes only $O(D)$ carrier rhombi. Fix
$$
K=5000.
$$
At most
$$
(5.317/5000)D^2<0.001064D^2
$$
retained crossings have defect exceeding $K/D$. From (4.5), more than
$0.3988D^2$ good crossings remain for large $D$.

One of the three unordered phase-label pairs gets at least one third. Randomly shift
reduced-phase bins of width $500K/D$. A good crossing is split by a bin boundary
with probability at most $1/500$, so one shift retains more than
$$
\boxed{
0.1326D^2
}
\tag{5.4}
$$
same-bin crossings on one fixed pair of labels.

If every occupied bin had one shore smaller than $0.058D$, split bins according to
which label shore is small. Simplicity of the train-crossing graph and disjointness of
the two label classes give the corrected joint-shore capacity
$$
E_{\rm bin}\le0.058D\,T_D
<(0.058)(2.27)D^2
=0.13166D^2,
$$
contradicting (5.4).

Hence one common reduced-phase bin contains train families
$$
\boxed{
|{\cal A}_D|,\ |{\cal B}_D|\ge0.058D.
}
\tag{5.5}
$$
Their limiting projective terminal-edge directions $u_A,u_B$ satisfy
$$
\boxed{
\operatorname{dist}_{\mathbb{RP}^1}(u_A,u_B)=\pi/3.
}
\tag{5.6}
$$
Each local train has two physical boundary ends, so each family supplies at least
$$
\boxed{
0.116D
}
\tag{5.7}
$$
terminal-edge occurrences.

## 6. Quantitative endpoint leakage

At most $5Q_D$ strict-rhombus terminal occurrences face bounded nonquadrilateral
faces. By (2.7),
$$
N_{\rm bounded}\le(10\sigma+o(1))D.
\tag{6.1}
$$

Every other selected terminal edge lies on the carrier outer walk. Partition that walk
into routes between consecutive attachment vertices. For route $i$, let $b_i$ be
its polygon-base length, $q_i$ its oriented base direction, and $\ell_i$ its
unit-edge length. Then
$$
\ell_i-b_i
=
\sum_{z\in R_i}(1-q_i\cdot z).
\tag{6.2}
$$
Summing (6.2) gives exactly $L_w-p_w$, hence at most
$$
(2\sigma+o(1))D
\tag{6.3}
$$
by (2.9).

Fix
$$
\eta:=0.035.
$$
A selected phase endpoint lying on a route whose projective base direction is at least
$\eta$ from the phase direction contributes at least $1-\cos\eta-o(1)$ to
(6.2). Hence the number of such endpoints is at most
$$
\left[
\frac{2\sigma}{1-\cos\eta}+o(1)
\right]D.
\tag{6.4}
$$

For the remaining nonprincipal routes, whose bases lie within projective distance
$\eta$ of the phase direction, convex boundary-direction monotonicity gives
$$
\limsup\frac1D\sum b_i\le2\eta+C_{\rm tail}.
\tag{6.5}
$$
Indeed a projective $\eta$-window lifts to two oriented tangent windows on the
radius-$1/2$ circle, contributing at most $2\eta$ total circular boundary length,
while all nonprincipal gap chords contribute at most $C_{\rm tail}$. Adding the
route excess (6.3), these routes contain at most
$$
(2\eta+C_{\rm tail}+2\sigma+o(1))D
\tag{6.6}
$$
selected terminal occurrences.

Combining (6.1), (6.4), (6.6), and (3.7),
$$
N_{\rm off}
\le
\left[
2\eta+21\sigma+
\frac{2\sigma}{1-\cos\eta}
+o(1)
\right]D.
\tag{6.7}
$$
Taylor's inequality gives
$$
1-\cos(0.035)
\ge0.035^2/2-0.035^4/24
>0.000612.
$$
For $\sigma\le10^{-5}$, the bracket in (6.7) is below $0.103$. Therefore each
phase family leaves at least
$$
\boxed{
0.013D
}
\tag{6.8}
$$
terminal-edge occurrences on the union of the three principal corridors.

## 7. Principal corridor mismatch

Let $s_+,s_-$ be the support spans adjacent to the largest gap $g_1$, up to the
next principal gap on each side. The canonical Section-104 fourth-gap argument applies:
if $s_+>\delta$, the angular-diameter condition creates a fourth complement gap of
length at least $\phi$, contradicting
$$
\tau\le(52/3)\sigma<\phi.
$$
Thus
$$
s_+,s_-\le\delta.
\tag{7.1}
$$

A circle chord direction is its angular midpoint plus $\pi/2$. Using (3.4)--(3.6)
and (7.1), the two principal-corridor separations involving $g_1$ differ from the
model value $\theta/2$ by at most
$$
2\delta+e/2\le(41/3)\sigma,
\tag{7.2}
$$
while the third differs from $\pi-\theta$ by at most
$$
4\delta+e\le(82/3)\sigma<28\sigma.
\tag{7.3}
$$

Since $\theta>2.8$, the model separations are already more than $0.35$ away from
a $\pi/3$ separation. The perturbation in (7.2)--(7.3) is at most $0.00028$.
Therefore every distinct pair of principal corridor directions $q_i,q_j$ satisfies
$$
\boxed{
\left|
\operatorname{dist}_{\mathbb{RP}^1}(q_i,q_j)-\pi/3
\right|>0.35.
}
\tag{7.4}
$$

## 8. Spend the one route budget on both phase families

Let $p_{F,i}D$ be the selected endpoint count from family $F\in\{A,B\}$ on
principal corridor $i$. By (6.8),
$$
\sum_i p_{F,i}\ge0.013.
\tag{8.1}
$$

The two phase families have disjoint physical terminal occurrences. The projection
identity (6.2) and the single carrier route budget (6.3) therefore give
$$
2\sigma
\ge
\sum_{F\in\{A,B\}}\sum_{i=1}^3
p_{F,i}
\left[
1-\cos
\operatorname{dist}_{\mathbb{RP}^1}(u_F,q_i)
\right].
\tag{8.2}
$$

For each family choose a nearest principal corridor, with distances $x,y$.
If both choose the same corridor, (5.6) gives
$$
x+y\ge\pi/3.
$$
If they choose different corridors, (7.4) and the projective triangle inequality give
$$
x+y>0.35.
$$
Thus always $x+y>0.35$.

Since $1-\cos t$ is convex on $[0,\pi/2]$, (8.1)--(8.2) imply
$$
2\sigma
\ge
2(0.013)[1-\cos(0.175)].
\tag{8.3}
$$
Taylor gives
$$
1-\cos(0.175)>0.015,
$$
so (8.3) forces
$$
2\sigma>0.00039,
$$
contradicting $\sigma\le10^{-5}$.

Therefore
$$
\boxed{
\text{no positive-area locally rhombus-saturated wrapping harmonic-cell limit has }
\lambda\in[\lambda_1,\lambda_2].
}
\tag{8.4}
$$

## 9. Transfer and remaining obstruction

Current main already excludes wrapping limits below $\lambda_1$. Hence every
positive-area harmonic-cell limit of normalized diameter at most $\lambda_2$ is cap
type. Canonical Section 88 bounds the total area of that cap family by
$$
\mathcal C(\lambda_2)<\pi/4.
$$
Full-core cell-area saturation leaves a fixed positive area outside this family.
Canonical total cell perimeter $O(D)$, together with
$\operatorname{per}(P_r)\ge2d_r$, bounds the number of cells longer than
$\lambda_2D-o(D)$ by an absolute constant. One such actual cell therefore has
quadratic area. The globally summed nonnegative local rhombic deficit is $o(D^2)$,
so the selected long cell is locally rhombus-saturated. This proves (1.4).

This is theorem/proof work. No exhaustive computation or unexecuted verifier is
load-bearing.

The remaining full-core obstruction begins at
$$
\lambda\ge0.9891349910402891632\ldots .
$$
At that point the present coarse endpoint-leakage constants no longer spend the
rooted route-excess budget. A useful next step is either a sharper all-phase endpoint
transport inequality or a direct coupling of the same positive defect currency to the
Woodall diameter topology. The two-half-disk alternative and the macroscopic
inactive-container branch remain unresolved.
