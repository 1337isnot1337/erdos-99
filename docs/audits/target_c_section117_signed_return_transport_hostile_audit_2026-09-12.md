<!-- theorem-state: {"artifact_id":"ART-040484A0BCA6","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 117 signed-return transport hostile audit

**Date:** 2026-09-12  
**Verdict:** **PASS as a proof-only theorem.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit reviews the corrected head of PR #335,
`research/target-c-signed-return-transport-117-20260912` at
`52d27c93db4ef6c5a57a9371d16d9f8869894f38`.

The arithmetic regression is not the main object of review.  The load-bearing points
are the wider stability window, physical endpoint orientation, the finite signed-return
area theorem, the diffuse-bad-train estimate, and the extension of the integrated tooth
bound from one `o(1)` phase family to an arbitrary fixed projective direction window.
All of those steps survive hostile review.

The valid proof-only conclusion is the full-core carrier bound

\[
\boxed{
\operatorname{diam}(P_*)
\ge(0.9761078160770649\ldots-o(1))D
}
\]

through scalar slack `sigma<=0.0029`.  The corresponding decoupled signed-return
envelope near `sigma=0.0029068729001` is also numerically correct.  Neither statement
closes C-II or LEVEL I.

## 1. The Section-113 stability proof really extends to `sigma=0.0029`

The largest-gap transfer function is

\[
h_\theta(t)
=f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi),
\qquad f(x)=\sin(x/2).
\]

On the rectangle used in the proof,

\[
\theta\ge\theta_8,
\qquad0\le t\le0.1,
\]

its derivative is increasing in `theta` and decreasing in `t`; hence the minimum is
at `(theta_8,0.1)`, where it is `0.3084268...>0.30`.  The coarse `delta>=0.1`
transfer costs more than `0.03`, still far above the present `0.0029` slack.  Thus

\[
\delta\le{10\over3}\sigma,
\qquad
x_2,x_3,\tau\le{13\over3}\sigma
\]

remain valid.

At the endpoint,

\[
{13\over3}\sigma=0.0125666\ldots
\]

while the mandatory principal-gap scale is above `0.876`, so the adjacent-span/fourth-
gap argument retains large strict slack.

The Section-104 oriented tangent lift is also safe.  The main support-region extent is
bounded by

\[
|S|+\tau
\le U(\theta)+{13\over3}\sigma
=1.8399556597\ldots<\pi.
\]

Therefore no projective-lift ambiguity appears in the directional tooth argument at
the wider endpoint.

## 2. Area, train count, and principal-route excess are on the same carrier

The hostile-audited compact-support circular-segment identity gives the conservative
normalized area floor

\[
A(\sigma)
={\pi\over4}
-G(\theta)
-2G\left(\phi_8+{13\sigma\over3}\right)
-G\left({13\sigma\over3}\right),
\qquad
G(x)={x-\sin x\over8}.
\]

At `sigma=0.0029`,

\[
A=0.4722552235794338\ldots .
\]

Local rhombic saturation transfers this to
`A_{4,D}/D^2>=A-o(1)`.

Retaining the favorable Section-101 face currency gives

\[
Q_D/D\le\sigma+o(1).
\]

Canonical Sections 82 and 89 therefore yield

\[
T_D/D
\le U(\theta)+2\sigma+o(1)
=:C_T(\sigma)+o(1),
\]

with

\[
C_T(0.0029)=1.833188993111448\ldots .
\]

For the three principal complement-gap routes, count actual directed outer-walk
occurrences and orient every eligible endpoint occurrence with its incident strict
rhombus on the left.  Opposite bridge traversals or occurrences with no retained
rhombus on the left are not silently accepted as good endpoints; they remain bad.

The countable route exhaustion gives, on this same finite-carrier sequence,

\[
E_D/D
=\sum_{i=1}^3(\ell_i-|z_i|)/D
\le\sigma+o(1).
\]

Thus the lower and upper route-excess estimates are not taken from different relaxed
configurations.

## 3. The finite signed-return theorem and three-host constant are valid

Canonical complete-train geometry gives exactly two physical terminal edges per train.
If `u` is one orientation of the train's parallel contact edges and the transverse
coordinate `h_u=det(u,x)` is chosen increasing along the centerline, then the initial
physical boundary orientation is `u` and the terminal orientation is `-u`.  This
remains true for hole boundaries and disconnected rhombus components.

For a directed walk of unit steps `v_e`, displacement `z`, and unit chord direction
`q=z/|z|`,

\[
\ell-|z|=\sum_e(1-q\cdot v_e).
\]

If a train's two good ends are assigned injectively to walks `i,j`, their exact loss is

\[
(1-q_i\cdot u)+(1+q_j\cdot u)
=2-(q_i-q_j)\cdot u
\ge2-w_Q(u).
\]

Summation over injectively assigned occurrences proves

\[
E\ge\sum_{\tau\in\mathcal T_{gg}}(2-w_Q(u_\tau)).
\]

For two train directions `u,v` at projective angle `varphi` and at most three unit host
directions, the support-function collision argument gives

\[
a(2-w_Q(u))+b(2-w_Q(v))
\ge
 a+b-\sqrt{a^2+b^2+2ab\cos\varphi}.
\]

At a strict unit-rhombus crossing `varphi>pi/3`, so for `a=b=1`

\[
(2-w_Q(u))+(2-w_Q(v))
\ge2-\sqrt3=:c_{ret}.
\]

The constant is sharp for the host relaxation; no hidden factor of two is missing.

## 4. Area transport uses the exact train transverse span

Retain only trains whose two ends are good.  Let `A_gg` be the total area of rhombi
whose two crossing trains are both retained.  Multiply the local `c_ret` inequality by
rhombus area and sum.  Reorganizing by trains gives

\[
c_{ret}A_{gg}
\le
\sum_{\tau\ retained}
(2-w_Q(u_\tau))
\sum_{R\in\tau,\,gg}\operatorname{area}(R).
\]

Along a complete train, the sum of the areas of its rhombi is exactly the transverse
endpoint displacement and therefore at most the diameter `d` of the same convex
attachment cell.  Hence

\[
\boxed{dE\ge c_{ret}A_{gg}.}
\]

This is a finite identity/inequality on the actual embedding, not an asymptotic phase
heuristic.

## 5. The diffuse-bad-direction inequality counts every omitted rhombus

Select all complete trains, and call a train bad when at least one endpoint is not good
for the three principal routes.  Let `M_bad(epsilon)` be the largest number of bad
trains in a projective interval of width `epsilon`.

Fix another train.  Bad trains crossing it at projective angle in
`(pi/3,pi/3+epsilon]` lie in two direction intervals of width `epsilon`, so there are
at most `2M_bad(epsilon)` such crossings.  Complete trains cross at most once.  Summing
over all `T_D` possible other trains may double-count bad--bad crossings, but that only
increases the upper bound.

Every remaining omitted rhombus has angle defect larger than `epsilon`, so their count
is at most `Delta_D/epsilon`.  Since every unit rhombus has area at most one,

\[
\boxed{
A_{gg,D}
\ge
A_{4,D}-2T_DM_{bad}(\epsilon)-{\Delta_D\over\epsilon}.
}
\]

The required order of limits is exactly the one stated in Section 117: fix `epsilon`,
let `D->infinity`, then let `epsilon->0`.

## 6. The non-tooth bad-end capacities are global physical capacities

A bad train has at least one physical endpoint away from the three principal routes.
Choose one such endpoint per bad train.  Distinct trains have distinct physical
terminal edge occurrences, and the projective direction of the chosen edge is the
train direction.  Therefore `M_bad(epsilon)` is bounded by the number of off-principal
physical endpoint occurrences in the same direction window.

The four non-tooth Section-104 budgets used in Section 117 are global occurrence
budgets, not estimates that require a preselected phase family:

1. bounded nonquadrilateral boundary: at most `5Q_D`, hence `5sigma D+o(D)`;
2. nonprincipal macroscopic corridors: total route length at most
   `(sigma+C_tail)D+o(D)<=19sigma D/6+o(D)`;
3. exceptional micro routes: total edge-occurrence density at most `9sigma`;
4. teeth on the two tiny support spans adjacent to the largest gap: total endpoint
   density at most `20sigma/3`.

Their combined coefficient is

\[
5+{19\over6}+9+{20\over3}={143\over6}.
\]

Thus it is legitimate to apply these capacities to arbitrary bad trains in a fixed
direction interval.

## 7. The integrated tangent estimate extends from `o(1)` phase windows to fixed `epsilon`

The only genuinely new directional estimate is for regular unit-unit teeth on the main
support region.

For a tooth base `b=1+e`, put

\[
x={\pi\over3}-\arccos(b/2),
\qquad
\psi(x)=\cos x+\sqrt3\sin x-1=e.
\]

Fix one of the two leg choices and a projective endpoint-direction interval `I` of
width `epsilon`.  If the base offset satisfies `0<=x<=X`, then after using the unique
oriented lift from §1, the corresponding oriented base directions lie in one interval
of width at most

\[
X+\epsilon+o(1).
\]

The hostile-audited Section-104 tangent-window theorem is a finite boundary-direction
capacity statement.  It therefore gives

\[
\limsup {N([0,X])\over D}
\le C_{tail}+{X+\epsilon\over2}.
\]

Put

\[
F_\epsilon=C_{tail}+{\epsilon\over2}.
\]

For one leg class with normalized endpoint mass `q`, the increasing quantile of the
offset distribution obeys `x(t)>=2(t-F_epsilon)` above the free mass.  Since `psi` is
increasing, the minimum base-excess cost is

\[
J((q-F_\epsilon)_+),
\qquad
J(p)={1\over2}
[\sin(2p)+\sqrt3(1-\cos(2p))-2p].
\]

On the relevant range `J` is increasing and convex.  For the two leg classes,
convexity and the global micro-base excess budget `sigma D/2+o(D)` give

\[
q_1+q_2
\le Q(\sigma)+2F_\epsilon,
\]

where `Q(sigma)` is the unique nonnegative root of

\[
\sin Q+\sqrt3(1-\cos Q)-Q={\sigma\over2}.
\]

This is exactly the Section-110 bathtub argument with the direction window widened by
`epsilon`; no phase-label assumption is used in the cumulative tangent theorem itself.

## 8. Double-leg teeth are correctly charged

One tooth can contribute both leg endpoints to the same bad-direction interval.  If the
two projective leg directions both lie in an interval of width `epsilon`, their
projective separation is at most `epsilon`.

Let `gamma` be the tooth apex angle.  Triangle-freeness gives `gamma>pi/3`.  Since
`epsilon<pi/6`, the branch `gamma<=epsilon` is impossible, so

\[
\pi-\gamma\le\epsilon,
\qquad
\gamma\ge\pi-\epsilon.
\]

The base therefore satisfies

\[
b=2\sin(\gamma/2)
\ge2\cos(\epsilon/2),
\]

so every such double-leg tooth has base excess at least

\[
c_\epsilon=2\cos(\epsilon/2)-1.
\]

The total micro-base excess is at most `(sigma/2+o(1))D`, hence there are at most
`sigma D/(2c_epsilon)+o(D)` such teeth and at most

\[
{\sigma\over c_\epsilon}D+o(D)
\]

selected endpoint occurrences.  As `epsilon->0`, `c_epsilon->1`.

Combining the regular-tooth bound, the two `C_tail` allowances, the double-leg term,
and the four global non-tooth capacities gives

\[
\boxed{
\lim_{\epsilon\downarrow0}
\limsup_{D\to\infty}
{M_{bad}(\epsilon)\over D}
\le
B(\sigma)
:=Q(\sigma)+{175\over6}\sigma.
}
\]

The coefficient is correct:

\[
{143\over6}+{13\over3}+1={175\over6}.
\]

## 9. The final scalar inequality and endpoint arithmetic are correct

Divide the finite area-transport inequality by `D^2`, fix `epsilon`, let `D->infinity`,
then let `epsilon->0`.  Canonical `Delta_D=O(D)` makes the defect term vanish at fixed
`epsilon`.  The previous sections give the necessary inequality

\[
\boxed{
\lambda\sigma
\ge
(2-\sqrt3)
\left[A(\sigma)-2C_T(\sigma)B(\sigma)\right]_+,
}
\]

with `lambda=sin(theta/2)`.

Independent numerical reproduction at `sigma=0.0029` gives

\[
\begin{aligned}
\theta&=2.703524766763678\ldots,\\
\lambda&=0.9761078160770649\ldots,\\
A&=0.4722552235794338\ldots,\\
C_T&=1.833188993111448\ldots,\\
Q(\sigma)&=0.0410840313512094\ldots,\\
B&=0.1256673646845427\ldots,\\
A-2C_TB&=0.0115111641133817\ldots .
\end{aligned}
\]

Therefore the signed-return lower bound forces normalized route excess

\[
0.00315990413899035\ldots,
\]

strictly larger than the available `0.0029` by

\[
2.59904138990\times10^{-4}.
\]

The guaranteed right side deteriorates monotonically as `sigma` increases on this
small interval: the area floor decreases, `C_T` and `B` increase, and `lambda`
increases.  Thus endpoint contradiction closes the entire interval.

The reported decoupled root

\[
\sigma_{SR}=0.0029068729001\ldots,
\qquad
\mu_{SR}=0.9761079748635\ldots
\]

is consistent with the same monotone scalar equation.

## 10. Scope and non-conclusions

Section 117 is a real structural improvement over the two-shore scalar route: it uses
quadratic rhombic area through all complete trains and only then pays a directional
bad-end concentration term.

It remains a carrier theorem.  It does not prove that the scalar wrapping slack is
small for every Type-II survivor, does not force an exact unit triangle, and does not
construct a source-preserving strict sub-`D` competitor.  The separate macroscopic
inactive-container branch is untouched.

A subsequent independent improvement can target the bad-direction coefficient
`B(sigma)`, the use of the coarse span bound `<=d`, or a route system with more than
three macroscopic directions.  The zero-displacement closed-face observation in
proof-only Section 116 is also compatible with this program and may remove some
bounded-face endpoint loss in a later refinement.

**Disposition:** Section 117 survives full geometric hostile review.  Theorem state
unchanged; no promotion is performed here.
