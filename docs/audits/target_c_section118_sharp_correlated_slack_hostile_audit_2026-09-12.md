<!-- theorem-state: {"artifact_id":"ART-E15A98D2AEB8","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — Section 118 sharp correlated-slack hostile audit

**Date:** 2026-09-12
**Verdict:** **PASS as a proof-only theorem at the safe `sigma<=0.0088` endpoint.**
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit reviews
`research/target_c_section118_correlated_slack_signed_return.md` together with its
sharpening
`research/target_c_section118_sharp_correlated_envelope.md`.
It checks the exact four-way scalar-slack decomposition, the common-subsequence face
currency, the refined exceptional-micro-route count, the correlated bad-train bound,
the analytic slack-simplex maximization, the widened area/stability window, reuse of
the hostile-audited Section-117 signed-return theorem, and the final endpoint
arithmetic.

The safe proof-only conclusion is

\[
\boxed{
\operatorname{diam}(P_*)
\ge (0.9762439137425688\ldots-o(1))D
}
\]

for a quadratic-area locally rhombus-saturated harmonic carrier in every sufficiently
large full-core Type-II survivor. The associated safe scalar window is

\[
\boxed{\sigma\le0.0088.}
\]

The companion relaxation has scalar zero
`0.0089758762244767...` and coefficient `0.9762479642481726...`, but this audit treats
that number as the boundary of the relaxed scalar inequality, not as the promoted
finite theorem endpoint. The explicit `0.0088` theorem has a substantial positive
margin.

No theorem-state mutation is made here. The canonical state remains
`2026-09-12.audit.44`; C-II and Level I remain open.

## 1. Dependency and scope check

The proof uses the following load-bearing inputs.

1. Canonical Section 101 supplies
   \[
   M\le C\le2\alpha\le |S|\le U
   \]
   and therefore the exact nonnegative decomposition of `U-M`.
2. Canonical Sections 82 and 89 supply the exact bounded-face/outer-walk/train ledgers.
3. Canonical Section 104 supplies the finite-cover base-spacing theorem and the
   tangent-window capacity argument. Section 118 refines which scalar currency pays
   those terms; it does not strengthen the geometric theorem.
4. The hostile-audited Section-107 circular-segment identity supplies the exact support
   area formula. Section 118 redoes the wider-window gap bounds needed to apply it.
5. The hostile-audited Section-117 theorem supplies the finite signed-return inequality,
   three-host constant `2-sqrt(3)`, exact train area transport, diffuse-bad-direction
   inequality, and ordered limit `epsilon fixed -> D->infinity -> epsilon->0`.

The Section-118 sharpening does not import the numerical Section-117 bad-end bound.
It recomputes that bound using correlated currencies. It also does not depend on the
misnumbered Sections 109--112.

The theorem is still a **carrier theorem**. It does not force an exact unit equilateral
triangle, construct a source-preserving strict sub-`D` competitor, or close the
macroscopic inactive-container branch.

## 2. The four scalar currencies are exact and nonnegative

Put

\[
x=U-|S|,\qquad
y=|S|-2\alpha,\qquad
z=2\alpha-C,\qquad w=C-M.
\]

The canonical Section-101 chain makes each term nonnegative and telescopes exactly:

\[
\boxed{x+y+z+w=U-M=\sigma.}
\]

Nothing asymptotic is hidden in this decomposition. In particular, using the same
letter `sigma` separately for every later defect is unnecessarily lossy; Section 118
is entitled to keep the four currencies correlated until the final scalar relaxation.

## 3. Gap and tail geometry spend only `x` and `w`

Write the largest complement gap as

\[
g_1=\theta-\delta,
\qquad
\phi=2\pi-2\theta.
\]

The standard transfer function obeys

\[
h_\theta(\delta)\le C-M=w.
\]

On the entire Section-118 window the transfer derivative on
`0<=delta<=0.1` remains above `0.30`. The old `delta>=0.1` alternative costs more than
`0.0326`, while `w<=sigma<=0.0088`; hence that alternative is impossible. Therefore

\[
\boxed{\delta\le{10\over3}w.}
\]

Writing

\[
g_2=\phi+x_2,
\quad g_3=\phi+x_3,
\quad \tau=\sum_{j\ge4}g_j,
\]

the exact complement-measure identity is

\[
x_2+x_3+\tau=\delta+x.
\]

Hence

\[
\boxed{
\tau\le x+{10\over3}w,
\qquad
C_{tail}\le{x\over2}+{5\over3}w.
}
\]

The adjacent-support-span argument also spends only `w`, giving endpoint capacity
`20w/3` there. At `sigma=0.0088`, the coarse total perturbation
`(10/3)sigma=0.029333...` remains far below `0.1` and far below the secondary gap
scale `phi`; the main oriented tangent region remains shorter than `pi`.

Thus there is no unsupported extrapolation of the tiny Section-104 numerical window.
The geometric hypotheses of the scale-free finite-cover/tangent theorem are reproved
on the larger window.

## 4. The retained face currency is a joint currency, not separate limsups

Pass to one further subsequence on which

\[
Q_D/D\to q,
\qquad c_D/D\to c,
\qquad s_D/D\to s_0.
\]

The retained finite Section-101 face currency gives

\[
\boxed{2s_0+c+q\le z.}
\]

In particular

\[
\boxed{q+c\le z.}
\]

This step must use a common subsequence. Separate limsups of `q` and `c` could not be
added this way. The Section-118 companion explicitly uses one common subsequence, so
that defect is absent.

## 5. The refined exceptional-micro-route bound is `3z+6c`

This is the most delicate new bookkeeping step, because an occurrence/contact factor
error here would erase much of the sharpening.

Canonical Section 104 decomposes micro routes into three classes.

### Direct one-edge loaded-loaded micro routes

Each such direct side is one loaded-loaded contact from the local `c_D` currency. Its
normalized outer-route edge density is therefore at most

\[
c+o(1).
\]

### Non-direct routes of length at least three

After subtracting the ordinary two-edge baseline, their total normalized excess is at
most

\[
z+c+o(1).
\]

A route of length `k>=3` has baseline excess `k-2` and

\[
k\le3(k-2).
\]

Therefore these routes have total edge-occurrence density at most

\[
3(z+c)+o(1).
\]

### Length-two routes with loaded middle vertex

Both route edges are loaded-loaded contacts. Canonical Section 104 bounds their total
outer-face occurrence density by

\[
2c+o(1).
\]

Adding the three disjoint categories gives

\[
\boxed{
\text{exceptional micro-route endpoint density}
\le3z+6c.
}
\]

This is exactly the refinement asserted by the sharp companion. It is not obtained by
subtracting two independently maximized limsups.

## 6. The non-tooth shared currency reduces to `10z+C_tail`

The other two non-tooth categories are

- bounded nonquadrilateral boundary: at most `5q`;
- nonprincipal macroscopic routes: at most `z+C_tail`.

Together with Section 5, their total is

\[
4z+5q+6c+C_{tail}.
\]

Since `q+c<=z`,

\[
5q+6c\le6(q+c)\le6z,
\]

so

\[
\boxed{
4z+5q+6c+C_{tail}
\le10z+C_{tail}.
}
\]

The factor is safe even though the coefficients of `q` and `c` differ: replacing
`5q+6c` by `6(q+c)` only enlarges the expression.

## 7. Base-spacing and double-leg teeth spend only `y`

Canonical Section 104 gives the exact micro-base excess budget

\[
\limsup_D{1\over D}
\sum_{\rm micro\ bases}(|p_k-p_{k+1}|-1)
\le{|S|\over2}-\alpha={y\over2}.
\]

For one projective endpoint-direction interval of width `epsilon`, the hostile-audited
tangent-window theorem gives, for either leg choice,

\[
\limsup_D{N([0,X])\over D}
\le C_{tail}+{X+\epsilon\over2}.
\]

The same quantile/bathtub calculation audited in Section 117 therefore yields for the
two single-leg classes

\[
q_1+q_2
\le Q_{tooth}(y)+2C_{tail}+\epsilon,
\]

where `Q_tooth(y)` is the unique nonnegative solution of

\[
\sin Q+\sqrt3(1-\cos Q)-Q={y\over2}.
\]

If both legs of one tooth fall into the same width-`epsilon` projective interval,
triangle-freeness forces the apex angle onto the near-`pi` branch. The base excess is
at least

\[
2\cos(\epsilon/2)-1,
\]

so after `epsilon->0` the double-leg endpoint density costs at most `y`.
Consequently the full regular-tooth directional capacity is

\[
\boxed{Q_{tooth}(y)+y+2C_{tail}.}
\]

No full `sigma` is needed in this step.

## 8. The correlated bad-direction bound is correct

Add Sections 3, 6, and 7:

\[
B(x,y,z,w)
\le
Q_{tooth}(y)+y+10z+3C_{tail}+{20\over3}w.
\]

Using

\[
3C_{tail}\le{3\over2}x+5w
\]

gives

\[
\boxed{
B(x,y,z,w)
\le
Q_{tooth}(y)+y+{3\over2}x+10z+{35\over3}w.
}
\]

This agrees with the post-104 reconciliation audit. Every term is an actual global
physical endpoint-capacity budget, so the bound applies to the arbitrary bad trains in
the fixed direction interval used by the Section-117 diffuse estimate.

## 9. The slack-simplex maximization is analytic

Because

\[
{3\over2}<10<{35\over3}
\]

and `x+y+z+w=sigma`,

\[
B(x,y,z,w)
\le {35\over3}\sigma
+Q_{tooth}(y)-{32\over3}y.
\]

Let

\[
F(Q)=\sin Q+\sqrt3(1-\cos Q)-Q.
\]

Then `F(Q_tooth(y))=y/2`, while

\[
F'(Q)=\cos Q+\sqrt3\sin Q-1,
\]

\[
F''(Q)=-\sin Q+\sqrt3\cos Q>0
\qquad(0<Q<\pi/3).
\]

Thus `F'` is strictly increasing on the relevant interval and

\[
{dQ_{tooth}\over dy}={1\over2F'(Q_{tooth})}
\]

is strictly decreasing. The function

\[
Q_{tooth}(y)-{32\over3}y
\]

therefore has one global maximum at

\[
F'(Q_0)={3\over64}.
\]

Independent high-precision recomputation gives

\[
Q_0=0.0272815201203264009\ldots,
\]

\[
y_0=2F(Q_0)=0.0012822850180674681\ldots,
\]

\[
\kappa_0
=Q_0-{32\over3}y_0
=0.0136038132609400741\ldots .
\]

Hence, in particular for the safe window,

\[
\boxed{
B\le B_*(\sigma):={35\over3}\sigma+\kappa_0.
}
\]

The inequality is actually safe even for `sigma<y_0`: `kappa_0` is the unrestricted
global maximum of the one-variable correction, so restricting `0<=y<=sigma` can only
lower it.

## 10. The area floor and tangent domain remain valid at `0.0088`

From the exact gap identities,

\[
r:=x+{10\over3}w
\le {10\over3}\sigma.
\]

The circular-segment identity therefore gives

\[
A_*(\sigma)
={\pi\over4}
-G(\theta)
-2G\left(\phi_8+{10\sigma\over3}\right)
-G\left({10\sigma\over3}\right).
\]

At `sigma=0.0088`, independent high-precision computation gives

\[
\theta=2.70477923521549347\ldots,
\qquad
\lambda=\sin(\theta/2)=0.976243913742568741\ldots,
\]

\[
A_*=0.470375286800424054\ldots .
\]

The main tangent-region extent is bounded by

\[
U(\theta)+{10\over3}\sigma
=1.8604857318\ldots<\pi,
\]

so the unique oriented tangent lift required by the finite-cover theorem survives with
large margin.

Canonical Sections 82/89 plus the face currency give the safe train ceiling

\[
{T_D\over D}
\le C_T(\sigma)+o(1),
\qquad
C_T=U(\theta)+2\sigma,
\]

which evaluates to

\[
C_T=1.84875239846689394\ldots .
\]

The global selected-route excess is at most `zD+o(D)` and therefore, conservatively,

\[
E_D/D\le\sigma+o(1).
\]

## 11. Section 117 signed return applies unchanged

The Section-117 hostile audit proves on the actual finite carrier

\[
dE_D\ge(2-\sqrt3)A_{gg,D}
\]

and

\[
A_{gg,D}
\ge A_{4,D}-2T_DM_{bad}(\epsilon)-{\Delta_D\over\epsilon}.
\]

The Section-118 changes above only improve the upper bound on
`M_bad(epsilon)/D`; they do not alter train orientation, host assignment, endpoint
injectivity, the three-host collision constant, or the order of limits. Consequently
Section 117's finite theorem can be reused verbatim.

After dividing by `D^2`, taking the ordered limits, and using `d/D<=lambda`, every
putative survivor in the window must satisfy

\[
\boxed{
\lambda\sigma
\ge
(2-\sqrt3)
\left[A_*(\sigma)-2C_T(\sigma)B_*(\sigma)\right]_+.
}
\]

## 12. Endpoint arithmetic has a large positive margin

At `sigma=0.0088`, independent recomputation gives

\[
B_*=0.116270479927606741\ldots,
\]

\[
A_*-2C_TB_*
=0.040464629526304432\ldots>0.
\]

The signed-return lower bound therefore forces normalized route excess

\[
{2-\sqrt3\over\lambda}
\left(A_*-2C_TB_*\right)
=0.011106307195331664\ldots .
\]

The available budget is only `0.0088`, leaving contradiction margin

\[
\boxed{0.002306307195331664\ldots>0.}
\]

This is too large to be a numerical-rounding artifact.

The supplied regression
`research/verify_target_c_correlated_slack_sharp_118.py` reproduces the same values.
The regression uses binary64 for diagnostics; the analytic inequalities above are the
proof, and the displayed endpoint has much more margin than its floating-point error.

## 13. Monotonicity closes the whole safe interval

For increasing scalar slack on this neighborhood:

- `theta` and `lambda=sin(theta/2)` increase;
- the area floor `A_*` decreases;
- `C_T` increases;
- `B_*=(35/3)sigma+kappa_0` increases;
- the available route budget `sigma` increases.

Therefore

\[
{2-\sqrt3\over\lambda}
[A_*-2C_TB_*]-\sigma
\]

is strictly decreasing wherever the residual is positive. Since it remains positive at
`0.0088`, every smaller positive slack is excluded as well. For very small slack the
constant `kappa_0` bound is deliberately coarse but still valid, as noted in Section 9.

The scalar relaxation has its unique zero at

\[
\sigma_{env}=0.008975876224476734\ldots,
\]

\[
\mu_{env}=0.976247964248172612\ldots .
\]

This audit does **not** promote the equality root as a theorem endpoint. The safe
`0.0088` value already gives the stated explicit coefficient with a robust strict
margin.

## 14. Disposition

The sharp Section-118 correlated-slack companion survives hostile review.

The valid proof-only theorem is

\[
\boxed{
\sigma\le0.0088
\Longrightarrow
\operatorname{diam}(P_*)
\ge(0.9762439137425688\ldots-o(1))D
}
\]

for the full-core Type-II harmonic carrier under the canonical selection/normalization.
This strictly supersedes the proof-only Section-117 numerical endpoint while retaining
Section 117's signed-return geometry as a dependency.

It remains a quantitative carrier theorem only. It does not prove that every Type-II
survivor lies in the small-slack regime, does not force an exact unit equilateral
triangle, does not construct a same-cardinality strict sub-`D` source, and does not
address the separate macroscopic inactive-container branch.

**Audit verdict:** PASS as proof-only. **Theorem state unchanged.**
