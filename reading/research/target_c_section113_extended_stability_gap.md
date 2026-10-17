> Generated reading edition · [exact source](../../research/target_c_section113_extended_stability_gap.md) · source SHA-256 `8bdb7fedfab73ae5cda2ffd3bda7ed10ffc9e89ef31d9e496774293220342161`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 2 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — Section 113: extend wrapping stability and aggregate phase loss

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit/promotion.

Canonical Section 104 and the proof-only Section-107/112 research chain leave an
artificial cutoff at

```math
\sigma(\theta)\le10^{-3}.
```

That cutoff is not a geometric threshold. The Section-107 gap-stability proof has much
more room. This section extends the same argument to

```math
\boxed{\sigma(\theta)\le1.4\times10^{-3}}
```

and then reruns the exact local-train, joint-shore, and aggregate two-family projection
argument directly. Sections 105--112 are not logical premises.

Put

```math
\sigma(\theta)
=3\theta-2\pi-\sin(\theta/2)-2\sin\theta,
\qquad
U(\theta)=3\theta-2\pi.
```

Let `theta_17` be the unique root above the canonical Section-101 endpoint `theta_8`
of

```math
\boxed{\sigma(\theta_{17})=1.4\times10^{-3}.}
\tag{113.1}
```

Then

```math
\boxed{
\theta_{17}=2.703205775845795918\ldots,
\qquad
\mu_{17}:=\sin(\theta_{17}/2)
=0.976073147411914233\ldots .
}
\tag{113.2}
```

Hence

```math
\boxed{
\mu_{17}-\mu_8
=3.2382144862251\times10^{-5}>0.
}
\tag{113.3}
```

The final normalized route-loss margin is about `1.1259e-4`, so the theorem is not
being pushed to the numerical edge of the method.

---

## 113.1 Extend the complement-gap stability window

Assume for contradiction that every positive-area macroscopic harmonic-cell limit in
a full-core Type-II countersequence has normalized diameter at most `mu_17`.
Canonical Section 103 gives a unique wrapping macroscopic carrier. Canonical Section
101 gives an angular diameter `theta` satisfying

```math
\theta_8\le\theta\le\theta_{17},
\qquad
0\le\sigma:=\sigma(\theta)\le1.4\times10^{-3}.
\tag{113.4}
```

Let `S` be the limiting attachment support on the radius-`1/2` circle. Put

```math
\phi=2\pi-2\theta,
\qquad
f(x)=\sin(x/2),
\qquad
C=\sum_j f(g_j),
```

where `g_1>=g_2>=...` are the connected complement-gap lengths. Canonical Sections
94, 100, and 101 give three distinct gaps at least `phi` and the scalar chain

```math
M\le C\le2\alpha\le|S|\le U,
\qquad
U-M=\sigma.
\tag{113.5}
```

Write

```math
g_1=\theta-\delta.
```

### Lemma 113.1 — the Section-107 largest-gap bound remains valid

Throughout (113.4),

```math
\boxed{0\le\delta\le{10\over3}\sigma.}
\tag{113.6}
```

#### Proof

If `delta>=0.1`, the same concavity/majorization step used in Sections 104 and 107 gives

```math
C-M
\ge
h_\theta(0.1),
```

where

```math
h_\theta(t)
=f(\theta-t)+f(\phi+t)-f(\theta)-f(\phi).
```

For `0<=t<=0.1`,

```math
\partial_t h_\theta(t)
={1\over2}\cos{\phi+t\over2}
-{1\over2}\cos{\theta-t\over2}.
\tag{113.7}
```

On the rectangle

```math
\theta_8\le\theta\le\theta_{17},
\qquad 0\le t\le0.1,
```

this derivative increases with `theta` and decreases with `t`. Its minimum is therefore
at `(theta_8,0.1)`, where direct evaluation gives

```math
\partial_t h_{\theta_8}(0.1)
=0.3084268133\ldots>0.30.
\tag{113.8}
```

Thus `h_theta(0.1)>0.03`, contradicting `C-M<=sigma<=0.0014`.
Hence `delta<0.1`. Integrating (113.7) from `0` to `delta` now gives

```math
C-M\ge h_\theta(\delta)>0.30\delta,
```

which proves (113.6). `square`

Write

```math
g_2=\phi+x_2,
\qquad
g_3=\phi+x_3,
\qquad
\tau=\sum_{j\ge4}g_j.
```

As before, if `e=U-|S|`, exact complement measure gives

```math
x_2+x_3+\tau=\delta+e,
\qquad 0\le e\le\sigma.
```

Therefore

```math
\boxed{
0\le x_2,x_3,\tau\le{13\over3}\sigma.
}
\tag{113.9}
```

At maximal slack the right side is below `0.00607`, while
`phi>0.876`. Thus the Section-104 adjacent-span/fourth-gap argument remains valid with
enormous room: the two angular spans `s_+,s_-` between the large principal gap and its
neighboring principal gaps satisfy

```math
\boxed{s_+,s_-\le\delta.}
\tag{113.10}
```

The Section-104 midpoint calculation therefore also remains valid and gives, for every
pair of principal projective corridor directions,

```math
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|
>
m(\sigma)
:={\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
}
\tag{113.11}
```

At maximal slack,

```math
\boxed{m=0.287223130294252762\ldots .}
\tag{113.12}
```

## 113.2 The wrapping carrier still has more than `0.472D^2` rhombi

Use the hostile-audited Section-107 circular-segment identity

```math
\operatorname{area}(\operatorname{conv}S)
={\pi\over4}-{1\over8}\sum_j(g_j-\sin g_j).
\tag{113.13}
```

Put

```math
G(x)={x-\sin x\over8},
\qquad
q_*={13\over3}(1.4\times10^{-3}).
```

`G` is increasing and superadditive on nonnegative sums at most `pi`. From
(113.6)--(113.9), the worst permitted segment loss is therefore bounded by

```math
G(\theta_{17})+2G(\phi_8+q_*)+G(q_*),
```

where `phi_8=2pi-2theta_8`. Consequently

```math
\boxed{
\operatorname{area}(\operatorname{conv}S)
\ge0.472929268186874395\ldots>0.472.
}
\tag{113.14}
```

Hausdorff area continuity and local rhombic saturation transfer this to the finite
carrier. Every strict unit rhombus has area at most one, so for all sufficiently large
members

```math
\boxed{R_D\ge0.472D^2.}
\tag{113.15}
```

## 113.3 Exact outer currency gives `T_D<1.83D`

Use the canonical Section-82/89 notation. Their exact identities give

```math
L_D+Q_D=4a_D-6-2s_D-2c_D,
```

```math
P_{R,D}\le L_D+5Q_D,
\qquad
2T_D=P_{R,D}.
```

Hence

```math
T_D\le2a_D-3-s_D-c_D+2Q_D
\le2a_D+2Q_D.
\tag{113.16}
```

Retaining the favorable currency in the finite Section-101 route proof gives

```math
C\le2\alpha-\limsup_D{2s_D+c_D+Q_D\over D},
\tag{113.17}
```

while

```math
0\le2\alpha-C\le\sigma,
\qquad
2\alpha\le U.
```

Thus

```math
{Q_D\over D}\le\sigma+o(1)
```

and

```math
\boxed{
{T_D\over D}
\le U(\theta)+2\sigma+o(1).
}
\tag{113.18}
```

At the top of the window,

```math
U(\theta_{17})+2(1.4\times10^{-3})
=1.8292320203578013\ldots<1.83.
\tag{113.19}
```

Therefore `T_D<=1.83D` for all sufficiently large members.

## 113.4 Joint-shore extraction gives two `0.085D` train families

Canonical Section 68 bounds total acute-angle defect by `<5.317D`. The canonical phase
cut deletes only `O(D)` crossing rhombi. From (113.15), eventually at least
`0.4719D^2` crossings remain.

Use defect threshold

```math
K=5000
```

and randomly shifted reduced-phase bins of width

```math
W={500K\over D}.
```

At most `(5.317/5000)D^2` retained crossings are nongood. One of the three unordered
phase-label pairs gets at least one third of the good crossings, and a random shift
retains at least `499/500` inside common bins. Hence one fixed label pair has total
internal-bin crossing density at least

```math
\boxed{
{499\over500}{0.4719-5.317/5000\over3}
=0.1566316422666667\ldots .
}
\tag{113.20}
```

Fix

```math
\boxed{a=0.085.}
```

If every occupied bin had one shore smaller than `aD`, partition bins into those small
on the first shore and the remaining bins small on the second. The selected label
classes are disjoint subsets of the same local train set, so the joint bad-bin capacity
is at most

```math
aDT_D
\le(0.085)(1.83)D^2
=0.15555D^2,
\tag{113.21}
```

strictly below (113.20). Thus one bin contains two distinct-label train families
`A_D,B_D` satisfying

```math
\boxed{|A_D|,|B_D|\ge0.085D.}
\tag{113.22}
```

Their reduced phases lie in one `O(1/D)` interval, so their limiting projective
terminal-edge directions are exactly `pi/3` apart. Each train has two physical boundary
ends, hence each family supplies endpoint density

```math
\boxed{E_0=0.17.}
\tag{113.23}
```

## 113.5 Off-principal leakage at the wider endpoint

Canonical Section 104's independently audited technical leakage theorem is scale-free
once (113.6)--(113.10) hold. For one selected phase family,

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\qquad
w(h)={\pi\over3}-\arccos((1+h)/2)
\tag{113.24}
```

bounds normalized endpoints away from the three principal corridors.

Take

```math
\boxed{h=0.0488.}
\tag{113.25}
```

At maximal slack,

```math
\boxed{
L=0.09653338038289313\ldots .
}
\tag{113.26}
```

Thus each family has principal-corridor endpoint density at least

```math
\boxed{
P=E_0-L
=0.07346661961710687\ldots .
}
\tag{113.27}
```

## 113.6 Aggregate both phase families against the one route budget

Let `p_{F,i}` be the limiting normalized number of selected endpoint occurrences from
family `F in {A,B}` on principal corridor `i`. Then

```math
\sum_i p_{F,i}\ge P.
\tag{113.28}
```

The selected physical terminal-edge occurrences from the two phase labels are disjoint.
The full complement-route ledger gives total principal-route excess at most `sigma`.
If `u_F` is the limiting projective direction of family `F` and `q_i` the projective
corridor direction, then exact projection loss yields

```math
\boxed{
\sigma
\ge
\sum_{F\in\{A,B\}}\sum_{i=1}^3
p_{F,i}
\left[1-\cos\operatorname{dist}_{RP^1}(u_F,q_i)\right].
}
\tag{113.29}
```

For each family choose a nearest principal corridor and call the two nearest distances
`x,y`. Since the phase directions are `pi/3` apart, either both choose the same
corridor, in which case `x+y>=pi/3`, or they choose distinct corridors, in which case
(113.11) gives

```math
x+y>m(\sigma).
```

Because `1-cos t` is increasing and convex on `[0,pi/2]`, both cases imply

```math
\boxed{
\sigma
\ge
2P\left(1-\cos{m(\sigma)\over2}\right).
}
\tag{113.30}
```

At maximal slack, the right side is

```math
\boxed{0.001512593891191816\ldots,}
\tag{113.31}
```

which exceeds

```math
\sigma=0.0014
```

by

```math
\boxed{0.000112593891191816\ldots .}
\tag{113.32}
```

For the fixed `h=0.0488`, decreasing `sigma` decreases leakage, increases `P`, and
increases `m`, while the left side of (113.30) decreases. Thus contradiction at the
upper endpoint implies contradiction throughout the full interval (113.4).

## 113.7 Carrier consequence and scope

No full-core Type-II countersequence can have every positive-area macroscopic harmonic
cell of normalized diameter at most `mu_17`. The usual finite-macroscopic-cell transfer
therefore gives a locally rhombus-saturated harmonic carrier of quadratic area with

```math
\boxed{
\operatorname{diam}(P_*)
\ge
(0.976073147411914233\ldots-o(1))D.
}
\tag{113.33}
```

This is an explicit full-core carrier theorem, not a C-II closure. It neither forces an
exact unit equilateral triangle nor resolves the separate macroscopic inactive-container
branch.

Logical dependencies:

- canonical Sections 68, 82, 89, 90, 100, 101, 103, and 104;
- the hostile-audited Section-107 circular-segment area identity;
- standard compactness/Hausdorff area continuity already used in Sections 83 and 107.

Sections 105--112 are not premises: the wider gap stability, exact train budget,
joint-shore extraction, and aggregate projection inequality are all rederived here.
Contact-isolated source points are retained, and bridge multiplicity is handled by the
canonical outer-walk occurrence convention.

**Theorem state:** unchanged. Independent hostile audit is required before promotion.
