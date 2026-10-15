# Target C — Section 118: correlate the scalar slacks before paying signed-return leakage

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate stacked on Section 117.

Section 117 bounds every off-principal endpoint category by replacing each of several
nonnegative scalar slacks by the same total scalar slack `sigma`.  Those slacks are not
independent.  Canonical Section 101 gives an exact four-term decomposition

\[
\boxed{
\sigma
=(U-|S|)+(|S|-2\alpha)+(2\alpha-C)+(C-M).
}
\]

Keeping these currencies separate cuts the linear part of the directional bad-train
bound from `175 sigma/6` to at most `15 sigma` without changing any geometric theorem.
The square-root tooth term is also paid only by the base-spacing slack before the final
one-variable relaxation.

The resulting signed-return contradiction closes the explicit window

\[
\boxed{\sigma(\theta)\le4.7\times10^{-3}}
\]

and gives the proof-only carrier coefficient

\[
\boxed{
\mu_{21}=0.9761493823116423\ldots .
}
\]

The corresponding one-variable correlated-slack envelope of this deliberately coarse
final relaxation is

\[
\boxed{
\sigma_{21,\rm env}=0.004733405294\ldots,
\qquad
\mu_{21,\rm env}=0.9761501533\ldots .
}
\]

No theorem-state mutation is proposed.  C-II and LEVEL I remain open.

---

## 118.1 Exact decomposition of the Section-101 scalar slack

Use the wrapping-support notation

\[
U=3\theta-2\pi,
\qquad
M=\sin(\theta/2)+2\sin\theta,
\]

\[
C=\sum_j\sin(g_j/2),
\qquad
{a_D\over D}\to\alpha.
\]

Canonical Section 101 gives

\[
M\le C\le2\alpha\le|S|\le U.
\]

Define

\[
\boxed{
\begin{aligned}
x&:=U-|S|,\\
y&:=|S|-2\alpha,\\
z&:=2\alpha-C,\\
w&:=C-M.
\end{aligned}}
\tag{118.1}
\]

Every term is nonnegative and telescoping gives the exact identity

\[
\boxed{x+y+z+w=U-M=\sigma.}
\tag{118.2}
\]

The point of the section is simply not to replace `x,y,z,w` by `sigma` until the very
end.

## 118.2 Gap and tail geometry spend only `x` and `w`

Let

\[
g_1=\theta-\delta,
\qquad
\phi=2\pi-2\theta.
\]

The largest-gap transfer argument used in Sections 107, 113, and 117 actually gives

\[
h_\theta(\delta)\le C-M=w,
\]

not merely `h_theta(delta)<=sigma`.  On `0<=delta<=0.1` the transfer derivative is
uniformly greater than `0.30`.  Since the present total slack is below `0.03`, the
coarse `delta>=0.1` branch is impossible exactly as before.  Therefore

\[
\boxed{\delta\le{10\over3}w.}
\tag{118.3}
\]

Write

\[
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau=\sum_{j\ge4}g_j.
\]

The exact complement-measure identity is now

\[
\boxed{x_2+x_3+\tau=\delta+x.}
\tag{118.4}
\]

Hence

\[
\boxed{
\tau\le x+{10\over3}w,
\qquad
C_{tail}:=\sum_{j\ge4}\sin(g_j/2)
\le{x\over2}+{5\over3}w.
}
\tag{118.5}
\]

The two support spans adjacent to the largest gap each have angular width at most
`delta`.  The Section-104 polar-arc count therefore bounds the endpoint density on
those tiny spans by

\[
\boxed{{20\over3}w.}
\tag{118.6}
\]

This is the first place where the old proof paid a full `sigma` for a quantity that is
controlled only by the gap-shape slack `w`.

## 118.3 Contact-face and route currencies spend only `z`

The finite Section-101 route ledger retains the favorable local face currency.  After
passing to the same subsequence as above it gives

\[
\boxed{
\limsup_D{2s_D+c_D+Q_D\over D}\le2\alpha-C=z.
}
\tag{118.7}
\]

Consequently

\[
{Q_D\over D},{c_D\over D}\le z+o(1).
\tag{118.8}
\]

Several Section-104 endpoint categories therefore depend on `z`, not on the full
`sigma`.

### Bounded nonquadrilateral faces

Canonical Section 82 gives at most `5Q_D` strict-rhombus boundary occurrences there,
so their normalized endpoint capacity is at most

\[
\boxed{5z.}
\tag{118.9}
\]

### Nonprincipal macroscopic routes

The total length of all nonprincipal positive-gap routes satisfies

\[
L_{tail}
\le2\alpha-\sum_{i=1}^3\sin(g_i/2).
\]

Since

\[
C=\sum_{i=1}^3\sin(g_i/2)+C_{tail},
\]

we get the sharper exact currency

\[
\boxed{L_{tail}\le z+C_{tail}.}
\tag{118.10}
\]

### Exceptional micro routes

Direct loaded-loaded micro routes cost at most `z`.  For non-direct micro routes, the
outer ledger gives total excess above the two-edge baseline at most

\[
z+{c_D\over D}+o(1)\le2z+o(1).
\]

Routes of length at least three have total edge count at most three times their excess,
so they cost at most `6z`.  Length-two routes with a loaded middle vertex use at most
`2c_D/D<=2z` outer occurrences.  Together with the direct routes,

\[
\boxed{
\text{exceptional micro-route endpoint density}\le9z.
}
\tag{118.11}
\]

Thus all three non-tooth contact/route categories above cost `15z+C_tail` rather than
`15sigma+C_tail`.

## 118.4 The base-spacing and double-leg costs spend only `y`

The Section-104 finite-cover theorem gives

\[
\limsup_D{1\over D}
\sum_{\rm micro\ bases}(|p_k-p_{k+1}|-1)
\le {|S|\over2}-\alpha
={y\over2}.
\tag{118.12}
\]

Fix a projective train-direction interval of width `epsilon` and one of the two tooth
leg choices.  The hostile-audited tangent-window theorem gives cumulative capacity

\[
\limsup_D{N([0,X])\over D}
\le C_{tail}+{X+\epsilon\over2}.
\tag{118.13}
\]

Put

\[
F_\epsilon=C_{tail}+{\epsilon\over2}.
\]

The same quantile/bathtub calculation as Section 117, now with base-excess budget
`y/2`, gives for the two single-leg classes

\[
q_1+q_2
\le Q_{tooth}(y)+2F_\epsilon,
\tag{118.14}
\]

where `Q_tooth(t)` is the unique nonnegative solution of

\[
\boxed{
\sin Q+\sqrt3(1-\cos Q)-Q={t\over2}.
}
\tag{118.15}
\]

If both legs of one tooth lie in the same `epsilon` direction interval, its apex angle
is at least `pi-epsilon`, so its base excess is at least

\[
c_\epsilon=2\cos(\epsilon/2)-1.
\]

Equation (118.12) therefore bounds all double-leg endpoint occurrences by

\[
{y\over c_\epsilon}D+o(D).
\]

After `epsilon->0`, the full regular-tooth directional capacity is at most

\[
\boxed{
Q_{tooth}(y)+y+2C_{tail}.
}
\tag{118.16}
\]

## 118.5 Correlated directional bad-train bound

Choose one off-principal physical endpoint from each bad train in one projective
`epsilon` interval, as in Section 117.  Combine

- bounded nonquadrilateral boundary: `5z`;
- nonprincipal macroscopic routes: `z+C_tail`;
- exceptional micro routes: `9z`;
- tiny adjacent spans: `20w/3`;
- regular teeth: `Q_tooth(y)+y+2C_tail`.

Using (118.5), after the ordered limits `D->infinity` and then `epsilon->0`,

\[
\boxed{
\begin{aligned}
B(x,y,z,w)
&:=\lim_{\epsilon\downarrow0}
\limsup_D{M_{bad}(\epsilon)\over D}\\
&\le
Q_{tooth}(y)
+y+{3\over2}x+15z+{35\over3}w.
\end{aligned}}
\tag{118.17}
\]

This formula is the main theorem-level gain.

For a one-variable explicit theorem, use monotonicity of `Q_tooth` and the exact
simplex identity (118.2).  Since every linear coefficient in (118.17) is at most `15`,

\[
\boxed{
B(x,y,z,w)
\le Q_{tooth}(\sigma)+15\sigma
=:B_{corr}(\sigma).
}
\tag{118.18}
\]

Section 117 instead paid the four currencies independently and obtained

\[
Q_{tooth}(\sigma)+{175\over6}\sigma.
\]

No new geometric estimate is needed for the improvement (118.18); it is purely the
restoration of the exact scalar bookkeeping.

## 118.6 The remaining carrier bounds can be kept conservative

To make the theorem independent of a multidimensional numerical optimization, retain
the same conservative one-variable estimates as Section 117.

The circular-segment area floor is

\[
A(\sigma)
={\pi\over4}
-G(\theta)
-2G\left(\phi_8+{13\sigma\over3}\right)
-G\left({13\sigma\over3}\right),
\tag{118.19}
\]

with `G(t)=(t-sin t)/8`.

Canonical Sections 82/89 and (118.7) give the sharper train count

\[
{T_D\over D}
\le U-x-y+2z+o(1),
\]

but for the explicit scalar theorem it is enough to use

\[
\boxed{{T_D\over D}\le U+2\sigma+o(1)=:C_T(\sigma)+o(1).}
\tag{118.20}
\]

The total path excess of the three principal routes is at most

\[
zD+o(D),
\]

because the full complement-route excess is at most `2alpha-C=z`.  Again, for the
one-variable theorem we only use

\[
\boxed{E_D/D\le\sigma+o(1).}
\tag{118.21}
\]

Thus every survivor in the stability window must satisfy the necessary signed-return
inequality

\[
\boxed{
\lambda\sigma
\ge
(2-\sqrt3)
\left[
A(\sigma)-2C_T(\sigma)B_{corr}(\sigma)
\right]_+,
}
\tag{118.22}
\]

where `lambda=sin(theta/2)`.

## 118.7 Contradiction at `sigma=0.0047`

Let `theta_21` be the unique solution above `theta_8` of

\[
\sigma(\theta_{21})=0.0047.
\]

The regression certificate gives

\[
\boxed{
\theta_{21}=2.703907524666705\ldots,
\qquad
\mu_{21}=\sin(\theta_{21}/2)
=0.9761493823116423\ldots .
}
\tag{118.23}

The stability hypotheses retain large room:

\[
{10\over3}\sigma=0.0156666\ldots<0.1,
\]

\[
{13\over3}\sigma=0.0203666\ldots<\phi=0.8753702\ldots,
\]

and the main-region tangent extent is bounded by

\[
U+{13\over3}\sigma
=1.8489039334\ldots<\pi.
\]

At the endpoint,

\[
\boxed{
\begin{aligned}
A&=0.4714354422213568\ldots,\\
C_T&=1.837937266820529\ldots,\\
Q_{tooth}(\sigma)&=0.0523621835834795\ldots,\\
B_{corr}&=0.1228621835834795\ldots .
\end{aligned}}
\tag{118.24}
\]

The retained good-good area scalar is therefore

\[
\boxed{
A-2C_TB_{corr}
=0.0198094704393120\ldots>0.
}
\tag{118.25}

Dividing the signed-return lower bound by `lambda` forces normalized principal-route
excess at least

\[
\boxed{
{2-\sqrt3\over\mu_{21}}
\left(A-2C_TB_{corr}\right)
=0.00543762225626986\ldots .
}
\tag{118.26}

This exceeds the available `0.0047` by

\[
\boxed{7.37622256270\times10^{-4}.}
\tag{118.27}

The right side deteriorates as total `sigma` increases under the deliberately coarse
one-variable bounds: the area floor decreases, while `C_T`, `B_corr`, and `lambda`
increase.  Therefore contradiction at the endpoint closes the entire interval.

Every sufficiently large full-core Type-II survivor consequently contains a
quadratic-area locally rhombus-saturated harmonic carrier with

\[
\boxed{
\operatorname{diam}(P_*)
\ge(0.9761493823116423\ldots-o(1))D.
}
\tag{118.28}

## 118.8 Coarse correlated-slack envelope

Define

\[
H_{corr}(s)
={2-\sqrt3\over\lambda(s)}
\left[
A(s)-2C_T(s)
\bigl(Q_{tooth}(s)+15s\bigr)
\right]-s.
\tag{118.29}
\]

On the current neighborhood this function is strictly decreasing for the same
componentwise monotonicity reasons used in Sections 114 and 117.  Its unique zero is

\[
\boxed{
\sigma_{21,\rm env}
=0.004733405294\ldots .
}
\tag{118.30}
\]

with

\[
\boxed{
\mu_{21,\rm env}
=0.9761501533\ldots .
}
\tag{118.31}
\]

This envelope is not the limit of the correlated method.  It deliberately discards
most of (118.17) by replacing the slack simplex with the coarse bound (118.18), and it
also retains the old one-variable area and train ceilings.  The next quantitative step,
if useful, is a compact optimization over the exact simplex `x+y+z+w=sigma`; unlike
Sections 113--117, that optimization now has a mathematically justified correlated
objective.

## 118.9 Scope

The proof uses the same actual harmonic carrier throughout.  No source point is
deleted.  Boundary bridges and holes are occurrence-counted.  The finite signed-return,
three-host, area-transport, and diffuse-bad-direction theorems are those rederived in
Section 117; the only new input is the exact slack bookkeeping (118.1)--(118.18).

This is a stronger full-core carrier theorem, not C-II closure.  It does not resolve
the inactive-container branch and does not construct a strict global subdiameter
competitor.

**Theorem state:** unchanged.  Independent hostile audit is required before promotion.
