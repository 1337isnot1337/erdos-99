> Generated reading edition · [exact source](../../research/target_c_section115_integrated_leakage_envelope.md) · source SHA-256 `ec9ddc5998cac26bafbd4f25c9f643f9c34e177e9d757968470553cdda813593`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Section 115: integrated tooth leakage breaks the cutoff envelope

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit/promotion.

Section 114 computes the limiting envelope of the **cutoff-based** Section-104 tooth
leakage argument.  That envelope stops near

$$
\sigma=1.47567317\times10^{-3}.
$$

The cutoff is not intrinsic.  The integrated tangent-capacity argument developed on the
older proof-only integrated-leakage branch gives a strictly stronger estimate.  This
section rederives that estimate against the current Section-113 geometry, combines it
with the exact train budget, corrected joint-shore capacity, and aggregate two-family
projection, and obtains the conservative explicit window

$$
\boxed{\sigma(\theta)\le1.75\times10^{-3}.}
$$

It also computes the decoupled scalar envelope of this improved chain:

$$
\boxed{\sigma_{\rm int}=0.00176783502507\ldots .}
$$

No theorem-state mutation is proposed here.

---

## 115.1 Stability remains valid at `sigma=1.75e-3`

Let

$$
\sigma(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\qquad
U(\theta)=3\theta-2\pi.
$$

Let `theta_8` be the canonical Section-101 endpoint and let `theta_19` solve

$$
\boxed{\sigma(\theta_{19})=1.75\times10^{-3}.}
\tag{115.1}
$$

Then

$$
\boxed{
\theta_{19}=2.703280209175034\ldots,
\qquad
\mu_{19}:=\sin(\theta_{19}/2)
=0.9760812392179798\ldots .
}
\tag{115.2}

The Section-113 largest-gap proof uses the uniform derivative lower bound

\[
\partial_t h_\theta(t)>0.30
\qquad(0\le t\le0.1),
$$

whose minimum occurs at `(theta_8,0.1)` and is independent of the upper endpoint as
long as `theta>=theta_8`.  Since `1.75e-3<<0.03`, the same argument yields

$$
0\le\delta\le{10\over3}\sigma,
\qquad
0\le x_2,x_3,\tau\le{13\over3}\sigma.
\tag{115.3}
$$

The fourth-gap/adjacent-span argument also remains valid because

$$
{13\over3}\sigma<0.00759
$$

while the mandatory principal-gap scale satisfies `phi>0.876`.

Thus the principal corridor directions obey

$$
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>
 m(\sigma):={\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
}
\tag{115.4}
$$

At maximal slack,

$$
\boxed{m=0.2829647969609195\ldots .}
\tag{115.5}
$$

The oriented tangent-lift hypothesis needed below is also explicit.  After removing the
three principal gaps and the two tiny spans adjacent to the largest gap, the main
support-region extent is bounded by

$$
|S|+\tau\le U(\theta)+{13\over3}\sigma.
$$

At the endpoint,

$$
U(\theta_{19})+{13\over3}\sigma
=1.834238653678849\ldots<\pi.
\tag{115.6}
$$

So the audited convex tangent-window estimate has more than `1.30` radians of oriented
lift margin.

## 115.2 Area floor and exact train ceiling

Put

$$
G(x)={x-\sin x\over8},
\qquad
\phi_8=2\pi-2\theta_8,
\qquad
q={13\over3}\sigma.
$$

The hostile-audited circular-segment identity and the same superadditive majorization as
Section 113 give

$$
A(\sigma)
:={\pi\over4}
-G(\theta)-2G(\phi_8+q)-G(q)
\lefteqn{\phantom{A(\sigma)}}
$$

as a conservative lower bound on the normalized wrapping-carrier area.  At maximal
slack,

$$
\boxed{A(1.75\times10^{-3})=0.4727727270422313\ldots .}
\tag{115.7}
$$

Hence local rhombic saturation gives the safe finite bound

$$
\boxed{R_D\ge0.47276D^2}
\tag{115.8}
$$

for all sufficiently large members.

Retaining the favorable Section-101 face currency as in Sections 110--114 gives

$$
{Q_D\over D}\le\sigma+o(1)
$$

and therefore

$$
{T_D\over D}
\le U(\theta)+2\sigma+o(1).
\tag{115.9}
$$

At the endpoint,

$$
U(\theta_{19})+2\sigma
=1.830155320345514\ldots,
$$

so eventually

$$
\boxed{T_D\le1.8302D.}
\tag{115.10}
$$

## 115.3 Corrected joint-shore extraction

Take

$$
\boxed{a=0.086.}
\tag{115.11}
$$

The asymptotic corrected joint-shore threshold from (115.8)--(115.10) is

$$
{0.47276\over3(1.8302)}
=0.08610352238\ldots>a.
\tag{115.12}
$$

For a finite regression, after the canonical `O(D)` phase cut retain at least
`0.47275D^2` crossings.  Use defect cutoff `K=50000` and random reduced-phase bins of
width `5000K/D`.  One unordered label pair retains internal-bin crossing density at
least

$$
{4999\over5000}
{0.47275-5.317/50000\over3}
=0.1575163770893\ldots .
\tag{115.13}
$$

If every occupied bin had one shore smaller than `0.086D`, the corrected joint-shore
capacity would be at most

$$
(0.086)(1.8302)=0.1573972,
\tag{115.14}
$$

strictly smaller than (115.13).  Therefore one common `O(1/D)` reduced-phase bin
contains two distinct-label train families satisfying

$$
\boxed{|A_D|,|B_D|\ge0.086D.}
\tag{115.15}
$$

Their limiting projective terminal-edge directions are exactly `pi/3` apart.  Each
full train has two distinct physical boundary ends, so each family supplies endpoint
density

$$
\boxed{E_0=0.172.}
\tag{115.16}
$$

## 115.4 Integrated tangent capacity

We now replace the good/bad-base cutoff by an integrated estimate.

Consider a regular two-edge unloaded-apex tooth with unit legs and base

$$
b=1+e\in[1,2].
$$

Let

$$
x={\pi\over3}-\arccos(b/2)\in[0,\pi/3].
$$

Then

$$
\boxed{e=\psi(x):=\cos x+\sqrt3\sin x-1,}
\tag{115.17}
$$

and `psi` is increasing on `[0,pi/3]`.

For one fixed phase family and one of the two oriented leg choices, the audited tangent
window theorem gives the cumulative endpoint-capacity bound

$$
\limsup_{D\to\infty}{N([0,X])\over D}
\le C_{tail}+{X\over2},
\tag{115.18}
$$

where

$$
C_{tail}=\sum_{j\ge4}\sin(g_j/2)
\le{13\over6}\sigma.
\tag{115.19}
$$

After removing teeth for which the same phase family uses both legs, every selected
base contributes at most one selected endpoint.  If one leg class has normalized mass
`q`, its increasing offset quantile satisfies

$$
x(t)\ge2(t-C_{tail})
\quad(t>C_{tail}).
$$

Thus the required normalized base excess is at least

$$
J((q-C_{tail})_+),
$$

where

$$
J(p)
={1\over2}
\left[
\sin(2p)+\sqrt3(1-\cos(2p))-2p
\right].
\tag{115.20}
$$

On the relevant range `p<pi/6`, `J` is increasing and convex.  If the two leg classes
have masses `q_1,q_2`, the audited micro-base excess budget gives

$$
J(p_1)+J(p_2)\le{\sigma\over2},
\qquad
p_i=(q_i-C_{tail})_+.
$$

Convexity then implies

$$
p_1+p_2\le Q(\sigma),
\tag{115.21}
$$

where `Q(sigma)` is the unique nonnegative solution of

$$
\boxed{
\sin Q+\sqrt3(1-\cos Q)-Q={\sigma\over2}.
}
\tag{115.22}
$$

The restriction `p<pi/6` is automatic here because `J(pi/6)>0.34`, while
`sigma/2<0.001` throughout the present window.

### Double-leg teeth

If both tooth legs belong to the same selected phase family, their projective
separation is `O(1/D)`.  Triangle-freeness gives apex angle `gamma>pi/3`; therefore

$$
\min\{\gamma,\pi-\gamma\}=O(1/D)
$$

forces `gamma=pi-O(1/D)`.  Hence the base length tends uniformly to `2`, and each such
base has excess `1-o(1)`.  Since total micro-base excess is at most
`(sigma/2+o(1))D`, all double-leg teeth contribute at most

$$
(\sigma+o(1))D
$$

selected endpoint occurrences.

Combining the two leg classes, the tail allowance, and the double-leg correction, one
phase family places at most

$$
Q(\sigma)+{16\over3}\sigma+o(1)
\tag{115.23}
$$

endpoints on regular main-region teeth.

The other audited Section-104 leakage categories contribute

$$
5\sigma+{19\over6}\sigma+9\sigma+{20\over3}\sigma.
$$

Therefore the full off-principal leakage of one selected phase family is

$$
\boxed{
L_{int}(\sigma)
=Q(\sigma)+{175\over6}\sigma.
}
\tag{115.24}
$$

At `sigma=1.75e-3`,

$$
\boxed{
Q=0.0318855384885934\ldots,
\qquad
L_{int}=0.0829272051552600\ldots .
}
\tag{115.25}
$$

Thus each phase family has principal-corridor endpoint density at least

$$
\boxed{
P=E_0-L_{int}
=0.0890727948447400\ldots .
}
\tag{115.26}

## 115.5 Aggregate projection closes the window

The two phase families use disjoint physical terminal-edge occurrences.  Summing their
projection losses over all three principal corridors against the one total route-excess
budget gives, exactly as in the hostile-audited aggregate argument,

\[
\boxed{
\sigma
\ge
2P\left(1-\cos{m(\sigma)\over2}\right).
}
\tag{115.27}

At maximal slack, the right side equals

\[
\boxed{0.00178002186318775\ldots,}
\tag{115.28}
$$

which exceeds the available `0.00175` by

$$
\boxed{3.00218631877\ldots\times10^{-5}.}
\tag{115.29}
$$

All quantities on the right deteriorate monotonically as `sigma` increases, so the
endpoint contradiction closes the whole interval.

Consequently every full-core Type-II countersequence has a quadratic-area locally
rhombus-saturated harmonic carrier `P_*` with

$$
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760812392179798\ldots-o(1))D.
}
\tag{115.30}
$$

This is still not C-II closure.

---

## 115.6 Integrated decoupled scalar envelope

As in Section 114, define the separately worst-case scalar guarantees

$$
r_*(s)
={\pi\over4}
-G(\theta(s))
-2G\left(\phi_8+{13s\over3}\right)
-G\left({13s\over3}\right),
$$

$$
C_*(s)=3\theta(s)-2\pi+2s,
\qquad
a_*(s)={r_*(s)\over3C_*(s)},
$$

where `theta(s)` solves `sigma(theta)=s`.  The maximum endpoint supply guaranteed by
these decoupled bounds is

$$
E_*(s)=2a_*(s).
$$

Let `Q(s)` solve (115.22), and set

$$
P_*(s)
=E_*(s)-Q(s)-{175\over6}s,
$$

$$
\Phi_{int}(s)
=2P_*(s)
\left(1-\cos{m(s)\over2}\right).
\tag{115.31}
$$

Here `r_*(s)` and `m(s)` decrease, while `C_*(s)` and `Q(s)` increase, so
`Phi_int(s)-s` is strictly decreasing on the relevant interval.  The accompanying
regression certificate finds the unique root

$$
\boxed{
\sigma_{int}=0.00176783502507091\ldots .
}
\tag{115.32}
$$

At the root,

$$
\boxed{
\theta_{int}=2.7032840020556765\ldots,
\qquad
\mu_{int}=0.9760816515139280\ldots .
}
\tag{115.33}
$$

Thus integrating tangent capacity raises the present decoupled scalar envelope by about

$$
2.92\times10^{-4}
$$

in `sigma` beyond the cutoff-based Section-114 envelope.

As before, this is a barrier only for the **separately worst-case scalar** use of the
current ingredients.  A substantive next advance must exploit more information than
another cutoff optimization.  The most promising targets are now:

1. correlate the rhombus count and train count instead of replacing them by independent
   worst-case scalars;
2. use all three phase-label pairs or the full crossing graph instead of one selected
   pair;
3. couple route excess to endpoint distribution corridor-by-corridor rather than only
   through the total scalar excess;
4. improve the `169/6` linear leakage currency or avoid paying some categories
   independently; or
5. leave the quantitative carrier route and use the resulting near-boundary structure
   to force an exact triangle or a source-preserving strict deformation.

## 115.7 Scope

The proof uses canonical Sections 68, 82, 89, 90, 100, 101, 103, and 104; the
hostile-audited Section-107 circular-segment identity and tangent-window theorem; and
the merged Section-113 stability framework.  The integrated tooth argument is rederived
here and does not depend on the stale Section-110 numbering of the older branch.

No source point is deleted.  Bridge and hole boundaries are handled by physical
edge-occurrence counting.  C-II and Level I remain open.
