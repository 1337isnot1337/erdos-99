# Target C — Section 117: signed-return area transport uses the whole rhombic core

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit/promotion.

Sections 113--115 use two extracted inverse-phase shores. This section instead uses
**all complete trains**. A complete train has two physical boundary ends with opposite
oriented edge vectors. With only three directed principal corridors, that return
constraint converts quadratic rhombic area into a linear lower bound for route excess.

The resulting explicit window is

\[
\boxed{\sigma(\theta)\le 2.9\times10^{-3}},
\qquad
\sigma(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\]

with carrier coefficient

\[
\boxed{\mu_{20}=0.9761078160770649\ldots .}
\]

The corresponding decoupled scalar envelope is approximately

\[
\boxed{\sigma_{\rm SR}=0.0029068729001\ldots,\qquad
\mu_{\rm SR}=0.9761079748635\ldots .}
\]

No theorem-state mutation is proposed here.

---

## 117.1 Stability on the wider scalar window

Let `theta_8` and `mu_8` be the canonical Section-101 endpoint. Let `theta_20` solve

\[
\sigma(\theta_{20})=2.9\times10^{-3}.
\]

Then

\[
\boxed{
\theta_{20}=2.703524766763678\ldots,
\qquad
\mu_{20}=\sin(\theta_{20}/2)=0.9761078160770649\ldots .
}
\tag{117.1}
\]

The Section-113 transfer derivative is uniformly greater than `0.30` on
`0\le\delta\le0.1`; the present slack is still far below `0.03`. Hence the same
largest-gap and tail estimates remain valid:

\[
0\le\delta\le{10\over3}\sigma,
\qquad
0\le x_2,x_3,\tau\le{13\over3}\sigma.
\tag{117.2}
\]

At the endpoint, `(13/3)sigma=0.0125666...`, while the mandatory principal-gap scale
is above `0.876`. Thus the adjacent-span/fourth-gap argument remains valid.

The oriented tangent lift used later also has a large margin. After deleting the three
principal gaps and the two tiny spans adjacent to the largest principal gap, the main
support-region extent is at most

\[
|S|+\tau
\le U(\theta)+{13\over3}\sigma
=1.8399556597781\ldots<\pi,
\tag{117.3}
\]

where `U(theta)=3theta-2pi`.

## 117.2 Area, train, and principal-route budgets

Put

\[
G(x)={x-\sin x\over8},
\qquad
\phi_8=2\pi-2\theta_8,
\qquad
q={13\over3}\sigma.
\]

The hostile-audited Section-107 circular-segment identity and the Section-113
majorization give the normalized area floor

\[
A(\sigma)
:={\pi\over4}-G(\theta)-2G(\phi_8+q)-G(q).
\tag{117.4}
\]

At `sigma=0.0029`,

\[
\boxed{A=0.4722552235794338\ldots .}
\tag{117.5}
\]

Local rhombic saturation therefore gives

\[
{A_{4,D}\over D^2}\ge A(\sigma)-o(1),
\tag{117.6}
\]

where `A_{4,D}` is the total area of the strict unit rhombi in the carrier.

Retaining the favorable Section-101 face currency gives

\[
{Q_D\over D}\le\sigma+o(1).
\]

Canonical Sections 82 and 89 then imply

\[
{T_D\over D}
\le C_T(\sigma)+o(1),
\qquad
C_T(\sigma)=U(\theta)+2\sigma.
\tag{117.7}
\]

At the endpoint,

\[
\boxed{C_T=1.833188993111448\ldots .}
\tag{117.8}
\]

Let the three principal complement-gap routes be directed in their outer-face
orientation. A physical rhombus-boundary occurrence on such a route is eligible to be
**good** only when that route occurrence has the incident rhombus on its left. An
opposite bridge traversal, or any route occurrence with no incident rhombus on its
left, is bad and is charged below. This is the same occurrence convention used in the
canonical Section-102 endpoint proof.

Write the three route lengths and displacements as `(ell_i,z_i)` and put

\[
E_D=\sum_{i=1}^3(\ell_i-|z_i|).
\]

The full complement-route exhaustion gives

\[
\boxed{{E_D\over D}\le\sigma+o(1).}
\tag{117.9}
\]

Indeed the total excess over all positive complement-gap chords is at most
`2alpha-C<=sigma`.

---

## 117.3 Finite signed-return theorem

Consider a finite edge-to-edge complex of strict unit rhombi. Orient each physical
boundary edge with its incident rhombus on its left. A complete train chains opposite
parallel rhombus edges.

### Lemma 117.1 — opposite train-end orientations

If `u_tau` is either unit orientation of the parallel edges of a complete train `tau`,
its two physical boundary ends have oriented vectors

\[
u_\tau,\qquad -u_\tau.
\tag{117.10}
\]

This follows from monotone transverse motion of a complete train: the retained rhombi
lie on opposite sides of its two terminal parallel lines. The argument is local and is
unchanged by holes or disconnected components.

Let `W_1,...,W_m` be directed unit-edge walks with nonzero displacements and unit chord
directions `q_1,...,q_m`. A selected train endpoint is good if it is assigned
injectively to the exact physical boundary-edge occurrence of one walk with matching
orientation. All other selected endpoints are bad.

Define

\[
w_Q(u)=\max_j q_j\cdot u-\min_j q_j\cdot u.
\]

### Lemma 117.2 — signed return

For the trains whose two ends are both good,

\[
\boxed{
E\ge
\sum_{\tau\in\mathcal T_{gg}}
\bigl(2-w_Q(u_\tau)\bigr),
}
\tag{117.11}
\]

where `E=sum_j(ell_j-|z_j|)`.

**Proof.** For a directed unit-edge walk with chord direction `q`,

\[
\ell-|z|=\sum_e(1-q\cdot v_e).
\]

Every term is nonnegative. If the two ends of one train are assigned to walks `i,j`,
their combined contribution is

\[
(1-q_i\cdot u_\tau)+(1+q_j\cdot u_\tau)
=2-(q_i-q_j)\cdot u_\tau
\ge2-w_Q(u_\tau).
\]

Injectivity permits summation over trains. `square`

## 117.4 Three hosts force a per-rhombus return deficit

Let `u,v` be unit vectors at projective angle `varphi`, and let `a,b>0`. For any set
`Q` of at most three unit host directions,

\[
\boxed{
a(2-w_Q(u))+b(2-w_Q(v))
\ge
a+b-\sqrt{a^2+b^2+2ab\cos\varphi}.
}
\tag{117.12}
\]

To see this, write the weighted width sum as the four support maxima for
`au,-au,bv,-bv`. With at most three hosts, at least two of those four vectors share a
maximizing host. Combining them replaces their separate norm sum by the norm of their
vector sum. The smallest possible loss is an acute cross pair, giving (117.12). The
bound is attained by hosts parallel to `au+bv`, `-u`, and `-v`.

At a strict unit-rhombus crossing the projective train angle is strictly greater than
`pi/3`. Taking `a=b=1` gives

\[
\boxed{
(2-w_Q(u))+(2-w_Q(v))
\ge c_{ret}:=2-\sqrt3.
}
\tag{117.13}
\]

### Lemma 117.3 — area transport

Retain only trains with two good ends, and let `A_gg` be the sum of areas of rhombi
whose two crossing trains are both retained. If the whole rhombus complex lies in a
convex container of diameter `d`, then

\[
\boxed{dE\ge c_{ret}A_{gg}.}
\tag{117.14}
\]

**Proof.** Multiply (117.13) by each retained-retained rhombus area and sum. For one
complete train, the sum of rhombus areas along it is its transverse endpoint
displacement, at most `d`. Then apply (117.11). `square`

---

## 117.5 Diffuse bad directions

Select all complete trains. Call a train bad if at least one endpoint is bad, counting
the train only once. For `0<epsilon<pi/6`, let `M_bad(epsilon)` be the largest number
of bad trains whose projective directions lie in one closed interval of angular width
`epsilon`.

Let

\[
\Delta_D=\sum_R(\varphi_R-\pi/3)
\]

be the canonical total rhombus-angle defect; Section 68 gives `Delta_D=O(D)`.

For any fixed other train, bad trains crossing it at angle in
`(pi/3,pi/3+epsilon]` occupy two projective intervals of width `epsilon`, so there are
at most `2M_bad(epsilon)` such crossings. Summing over all `T_D` other trains may
overcount but remains an upper bound. Crossings at angle greater than
`pi/3+epsilon` number at most `Delta_D/epsilon`.

Since every unit-rhombus area is at most one,

\[
\boxed{
A_{gg,D}\ge
A_{4,D}-2T_DM_{bad}(\epsilon)-{\Delta_D\over\epsilon}.
}
\tag{117.15}
\]

Combining with (117.14),

\[
\boxed{
d_DE_D\ge
c_{ret}
\left(
A_{4,D}-2T_DM_{bad}(\epsilon)-{\Delta_D\over\epsilon}
\right)_+.
}
\tag{117.16}
\]

The limit order is fixed throughout:

```text
fix epsilon > 0 -> D -> infinity -> epsilon -> 0.
```

---

## 117.6 Directional concentration of bad trains

For bad trains in one projective direction interval `I` of width `epsilon`, choose one
bad endpoint per train. Distinct trains give distinct physical boundary-edge
occurrences, and each chosen endpoint direction lies in `I`. Hence
`M_bad(epsilon)` is bounded by the number of bad physical endpoint occurrences with
directions in `I`.

The audited Section-104 decomposition gives the following global off-principal
capacities:

- bounded nonquadrilateral boundary: `5sigma D+o(D)`;
- nonprincipal macroscopic corridors: `(sigma+C_tail)D+o(D)`;
- exceptional micro routes: `9sigma D+o(D)`;
- the two tiny support spans adjacent to the largest principal gap:
  `(20/3)sigma D+o(D)`;

where

\[
C_{tail}\le{13\over6}\sigma.
\tag{117.17}
\]

Any principal-route occurrence whose orientation does not match the physical
incident-rhombus-left orientation is included among the bad occurrences; the canonical
outer-walk occurrence convention charges such bridge traversals in the same boundary
currency rather than silently treating them as good.

### Integrated directional tooth estimate

For a regular unit-unit tooth with base `b=1+e`, set

\[
x={\pi\over3}-\arccos(b/2),
\qquad
\psi(x)=\cos x+\sqrt3\sin x-1=e.
\tag{117.18}
\]

For one leg choice, endpoint directions in `I` and offset at most `X` force the base
directions into one oriented interval of width at most `X+epsilon+o(1)`. The audited
convex tangent-window theorem therefore gives

\[
\limsup_{D\to\infty}{N([0,X])\over D}
\le C_{tail}+{X+\epsilon\over2}.
\tag{117.19}
\]

Let `F_epsilon=C_tail+epsilon/2`. After removing teeth contributing both legs, the
quantile/bathtub argument gives, for the two leg classes,

\[
q_1+q_2\le Q(\sigma)+2F_\epsilon,
\tag{117.20}
\]

where `Q(sigma)` is the unique nonnegative solution of

\[
\boxed{
\sin Q+\sqrt3(1-\cos Q)-Q={\sigma\over2}.
}
\tag{117.21}
\]

For a tooth contributing both selected endpoint legs in the same interval `I`, their
projective separation is at most `epsilon`. Since the apex angle is greater than
`pi/3` and `epsilon<pi/6`, the apex angle is at least `pi-epsilon`. Hence the base
excess is at least

\[
c_\epsilon=2\cos(\epsilon/2)-1.
\]

The global micro-base excess is at most `(sigma/2+o(1))D`, so all double-leg teeth
contribute at most

\[
\left({\sigma\over c_\epsilon}+o(1)\right)D
\]

selected endpoint occurrences.

Combining all categories,

\[
\limsup_{D\to\infty}{M_{bad}(\epsilon)\over D}
\le
Q(\sigma)
+{143\over6}\sigma
+{13\over3}\sigma
+\epsilon
+{\sigma\over c_\epsilon}.
\tag{117.22}
\]

Letting `epsilon->0`,

\[
\boxed{
\lim_{\epsilon\downarrow0}
\limsup_{D\to\infty}{M_{bad}(\epsilon)\over D}
\le B(\sigma):=Q(\sigma)+{175\over6}\sigma.
}
\tag{117.23}
\]

No inverse-phase extraction is used.

---

## 117.7 Whole-area signed-return inequality

Fix `epsilon`, apply (117.16), divide by `D^2`, and take `D->infinity`; then let
`epsilon->0`. Using (117.6)--(117.9) and (117.23), every surviving wrapping carrier
must satisfy

\[
\boxed{
\lambda\sigma
\ge
c_{ret}
\left[
A(\sigma)-2C_T(\sigma)B(\sigma)
\right]_+,
}
\tag{117.24}
\]

where

\[
\lambda=\sin(\theta/2).
\]

Equivalently,

\[
\boxed{
\sigma
\ge
{2-\sqrt3\over\lambda}
\left[
A(\sigma)-2C_T(\sigma)B(\sigma)
\right]_+.
}
\tag{117.25}
\]

This is the new bridge: quadratic rhombic area is transported directly into signed
return loss, without selecting a phase pair.

## 117.8 Numerical contradiction at `sigma=0.0029`

At the endpoint,

\[
\boxed{
Q=0.0410840313512094\ldots,
\qquad
B=0.1256673646845427\ldots .
}
\tag{117.26}
\]

Together with (117.5) and (117.8),

\[
\boxed{
A-2C_TB=0.0115111641133817\ldots>0.
}
\tag{117.27}
\]

Since `lambda=mu_20`, the right side of (117.25) is

\[
\boxed{0.00315990413899035\ldots,}
\tag{117.28}
\]

which exceeds the available `sigma=0.0029` by

\[
\boxed{2.59904138990\ldots\times10^{-4}.}
\tag{117.29}
\]

The guaranteed right side deteriorates as `sigma` increases: the area floor decreases,
the train ceiling and bad-direction concentration increase, and `lambda` increases.
Thus contradiction at the top endpoint closes the whole interval.

Therefore every full-core Type-II survivor contains a quadratic-area locally
rhombus-saturated harmonic carrier `P_*` satisfying

\[
\boxed{
\operatorname{diam}(P_*)
\ge(0.9761078160770649\ldots-o(1))D.
}
\tag{117.30}
\]

C-II remains open.

## 117.9 Decoupled signed-return envelope

Define

\[
H(s)=
{2-\sqrt3\over\lambda(s)}
\left[A(s)-2C_T(s)B(s)\right]-s.
\tag{117.31}
\]

On the live neighborhood the bracket decreases, while `lambda` and `s` increase, so
`H` decreases. The regression certificate finds its unique zero at

\[
\boxed{\sigma_{\rm SR}=0.0029068729001\ldots .}
\tag{117.32}
\]

The corresponding values are

\[
\boxed{
\theta_{\rm SR}=2.7035262283044\ldots,
\qquad
\mu_{\rm SR}=0.9761079748635\ldots .
}
\tag{117.33}
\]

This is only the envelope of the current separately worst-case scalar inputs. The
structural result is more important than the last digits: the argument now spends the
entire quadratic rhombic core rather than two selected shores.

## 117.10 Next obligations

The strongest next routes are:

1. reduce the directional bad-train concentration in (117.23), preferably by sharing
   the same slack currencies instead of adding every leakage category independently;
2. replace the coarse per-train transverse-span bound `<=d` in (117.14) by an average
   or direction-sensitive span estimate;
3. exploit four or more macroscopic oriented routes rather than declaring every
   nonprincipal route bad; or
4. connect signed return to the source-preserving deformation / exact-triangle gate.

## 117.11 Scope

The proof uses canonical Sections 68, 82, 89, 100, 101, 103, and 104; the
hostile-audited Section-107 circular-segment and tangent-window geometry; and the merged
Section-113 stability framework. The signed-return, three-host, area-transport, diffuse
bad-direction, and integrated directional-tooth arguments are rederived here rather
than imported from draft PRs #325 or #326.

No source point is deleted. Boundary bridges and holes are occurrence-counted. This is
a stronger full-core carrier theorem, not a proof of C-II or Level I, and it does not
address the separate macroscopic inactive-container branch.
