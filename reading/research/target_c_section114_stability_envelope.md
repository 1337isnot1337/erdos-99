> Generated reading edition · [exact source](../../research/target_c_section114_stability_envelope.md) · source SHA-256 `39a49a31b77c53569670e0d364017c78f7438c2e739161c4954dc4775b946063`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Section 114: optimized stability envelope of the aggregate phase route

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate pending independent hostile audit/promotion.

Section 113 extends the quantitative wrapping contradiction to

```math
\sigma(\theta)\le 1.4\times10^{-3},
\qquad
\sigma(\theta)=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
```

Its endpoint constants are deliberately rounded.  The same proof has a little more
room if the circular-segment area floor, exact train ceiling, corrected joint-shore
capacity, and tooth-leakage cutoff are optimized together.

This section does two things.

1. It gives a conservative finite theorem through
   ```math
   \boxed{\sigma\le1.46\times10^{-3}}.
   
   ```
2. It records the limiting **decoupled scalar envelope** of the present argument.  The
   envelope closes only up to
   ```math
   \sigma_{\rm env}=1.4756731748\ldots\times10^{-3}.
   
   ```
   This is not a no-go theorem for all refinements: it is the barrier obtained when the
   current area lower bound, train upper bound, joint-shore counting theorem, leakage
   formula, and corridor-mismatch bound are used only through their separate scalar
   guarantees.

No theorem-state mutation is proposed here.

---

## 114.1 Safe extension to `sigma=1.46e-3`

Let `theta_8` and `mu_8` be the canonical Section-101 endpoint.  Let `theta_18` be the
unique root above `theta_8` of

```math
\boxed{\sigma(\theta_{18})=1.46\times10^{-3}.}
\tag{114.1}
```

Then

```math
\boxed{
\theta_{18}=2.7032185359365495\ldots,
\qquad
\mu_{18}:=\sin(\theta_{18}/2)
=0.9760745346846268\ldots .
}
\tag{114.2}
```

Thus

```math
\boxed{
\mu_{18}-\mu_8
=3.37694175748\ldots\times10^{-5}>0.
}
\tag{114.3}
```

Assume for contradiction that every positive-area macroscopic harmonic-cell limit in a
full-core Type-II countersequence has normalized diameter at most `mu_18`.  Canonical
Section 103 gives the unique wrapping carrier.  The Section-113 gap-stability proof
continues verbatim on this slightly larger interval: the transfer derivative used there
is still bounded below by `0.30` on the same rectangle `0<=delta<=0.1`, while
`1.46e-3 << 0.03`.  Therefore

```math
0\le\delta\le {10\over3}\sigma,
\qquad
0\le x_2,x_3,\tau\le {13\over3}\sigma,
\tag{114.4}
```

and the three principal corridor directions satisfy

```math
\boxed{
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>
 m(\sigma):={\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
}
\tag{114.5}
```

At maximal slack,

```math
\boxed{m=0.2864931302942528\ldots .}
\tag{114.6}
```

## 114.2 Keep the actual area floor and train ceiling

Put

```math
G(x)={x-\sin x\over8},
\qquad
\phi_8=2\pi-2\theta_8,
\qquad
q(\sigma)={13\over3}\sigma.
```

The hostile-audited Section-107 circular-segment identity and the Section-113
majorization give the conservative area floor

```math
A(\sigma)
:={\pi\over4}
-G(\theta(\sigma))
-2G(\phi_8+q(\sigma))
-G(q(\sigma)).
\tag{114.7}
```

At `sigma=1.46e-3`,

```math
\boxed{A=0.4729024642799754\ldots .}
\tag{114.8}
```

Hence, for all sufficiently large members, local rhombic saturation permits the safe
finite lower bound

```math
\boxed{R_D\ge0.47289D^2.}
\tag{114.9}
```

The exact Section-82/89 currency used in Section 113 gives

```math
{T_D\over D}
\le U(\theta)+2\sigma+o(1),
\qquad U(\theta)=3\theta-2\pi.
\tag{114.10}
```

At the same endpoint,

```math
U(\theta_{18})+2\sigma
=1.8293903006300618\ldots,
```

so eventually

```math
\boxed{T_D\le1.8294D.}
\tag{114.11}
```

## 114.3 Two `0.086D` inverse-phase shores

Use the corrected joint-shore version of the Section-90 bin count.  Take

```math
a:=0.086.
\tag{114.12}
```

The asymptotic joint-shore threshold from the safe constants is

```math
{0.47289\over3(1.8294)}
=0.0861648627965\ldots>a.
\tag{114.13}
```

For a completely finite regression, after the `O(D)` phase cut retain at least
`0.47288D^2` crossings, take defect cutoff `K=20000`, and use randomly shifted bins of
width `2000K/D`.  One label pair retains internal-bin crossing density at least

```math
{1999\over2000}
{0.47288-5.317/20000\over3}
=0.157459280975\ldots .
\tag{114.14}
```

If every occupied bin had one shore below `0.086D`, the corrected disjoint-shore
capacity would be at most

```math
(0.086)(1.8294)=0.1573284,
\tag{114.15}
```

strictly smaller than (114.14).  Thus one bin contains two distinct phase-label
families `A_D,B_D` with

```math
\boxed{|A_D|,|B_D|\ge0.086D.}
\tag{114.16}
```

Their limiting projective terminal-edge directions are exactly `pi/3` apart.  Each
full train has two distinct physical boundary-end occurrences, so each family supplies
endpoint density

```math
\boxed{E_0=0.172.}
\tag{114.17}
```

## 114.4 Optimized leakage at the safe endpoint

The independently audited Section-104 technical theorem gives, for every cutoff
`0<h<1`, off-principal endpoint density at most

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\qquad
w(h)={\pi\over3}-\arccos((1+h)/2).
\tag{114.18}
```

Use the round value

```math
\boxed{h=0.05.}
\tag{114.19}
```

At maximal slack,

```math
\boxed{L=0.0994396708318175\ldots .}
\tag{114.20}
```

Thus each phase family has total principal-corridor endpoint density at least

```math
\boxed{
P:=E_0-L
=0.0725603291681825\ldots .
}
\tag{114.21}
```

The two families use disjoint physical terminal-edge occurrences.  Therefore the
Section-112 aggregate projection inequality applies directly:

```math
\sigma
\ge
2P\left(1-\cos{m(\sigma)\over2}\right).
\tag{114.22}
```

At `sigma=1.46e-3`, the right side is

```math
\boxed{0.00148636312650447\ldots,}
\tag{114.23}
```

which exceeds the available slack by

```math
\boxed{2.63631265045\ldots\times10^{-5}.}
\tag{114.24}
```

For fixed `h`, decreasing `sigma` decreases leakage, increases the principal endpoint
mass, and increases the corridor mismatch, while the left side of (114.22) decreases.
Hence contradiction at the upper endpoint closes the whole interval.

Therefore no full-core Type-II countersequence can have every positive-area
macroscopic harmonic cell of normalized diameter at most `mu_18`.  The standard
finite-macroscopic-cell transfer gives an actual locally rhombus-saturated carrier
`P_*` of quadratic area with

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760745346846268\ldots-o(1))D.
}
\tag{114.25}
```

C-II remains open.

---

## 114.5 The decoupled scalar envelope of the present mechanism

It is useful to know where the present chain actually stops before spending more work
on hand-tuned constants.

For `s>=0`, let `theta(s)` be the unique solution of `sigma(theta)=s` above `theta_8`.
Define

```math
r_*(s)
={\pi\over4}
-G(\theta(s))
-2G\!\left(\phi_8+{13s\over3}\right)
-G\!\left({13s\over3}\right),
\tag{114.26}
```

```math
C_*(s)=3\theta(s)-2\pi+2s,
\qquad
a_*(s)={r_*(s)\over3C_*(s)}.
\tag{114.27}
```

The corrected joint-shore counting theorem can guarantee shore density arbitrarily
close to `a_*(s)` using only these separate scalar bounds.  Thus the corresponding
endpoint supply is arbitrarily close to

```math
E_*(s)=2a_*(s).
\tag{114.28}
```

Optimize the audited leakage formula over its cutoff:

```math
L_*(s)
:=\min_{0<h<1}
\left[
 w(h)+\left({1\over h}+{169\over6}\right)s
\right].
\tag{114.29}
```

Set

```math
P_*(s)=E_*(s)-L_*(s),
\qquad
m(s)={\theta_8\over2}-{\pi\over3}-{73\over6}s,
\tag{114.30}
```

and

```math
\Phi(s)
:=2P_*(s)\left(1-\cos{m(s)\over2}\right).
\tag{114.31}
```

On the present neighborhood, `r_*(s)` decreases, `C_*(s)` increases, `L_*(s)`
increases, and `m(s)` decreases.  Hence `Phi(s)-s` is strictly decreasing wherever
`P_*(s)>0`.  The regression certificate finds its unique zero at

```math
\boxed{
\sigma_{\rm env}
=0.00147567317481145\ldots .
}
\tag{114.32}
```

At this point,

```math
\boxed{
\theta_{\rm env}=2.7032218691158647\ldots,
\qquad
\mu_{\rm env}=0.9760748970601998\ldots,
}
\tag{114.33}
```

with optimizing cutoff

```math
\boxed{h_{\rm env}=0.05011776\ldots .}
\tag{114.34}
```

Interpretation: with **only** the separately worst-case scalar guarantees
(114.26)--(114.31), the aggregate projection contradiction has no positive guaranteed
margin once `s>=sigma_env`.  This does not prove that the geometric method itself is
exhausted.  To go materially farther, one should improve or correlate at least one of

- the circular-segment area/rhombus floor;
- the exact train ceiling;
- the joint-shore extraction using more than one phase-label pair or more crossing
  structure;
- the off-principal leakage coefficient;
- the principal-corridor mismatch estimate; or
- the use of the route excess beyond the scalar sum in (114.22).

That list is the real output of the envelope calculation: another isolated choice of
`h`, `K`, or bin multiplier cannot yield a substantial improvement by itself.

## 114.6 Dependencies and scope

- canonical Sections 68, 82, 89, 90, 100, 101, 103, and 104;
- hostile-audited Section-107 circular-segment area identity and finite geometric
  transfer;
- merged proof-only Section 113 for the extended gap-stability framework;
- the corrected joint-shore and aggregate-projection arguments already audited in the
  live research chain.

No source point is deleted.  Physical train ends are occurrence-counted, and distinct
phase labels use disjoint terminal-edge occurrences.  This is a stronger quantitative
full-core carrier theorem plus a method-envelope diagnosis, not a proof of C-II or
Level I.
