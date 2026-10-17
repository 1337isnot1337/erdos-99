> Generated reading edition · [exact source](../../../docs/reports/target_c_renorm_perimeter_lp_080927_2026-09-10.md) · source SHA-256 `1c198ad11d1890e0ecea83c76a8937cfd95439b2e8d5906bca0e8f2842faf4fd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 4 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-D8B1B1FA98CE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — perimeter-capped renormalized pocket LP raises the floor to 0.80927

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after RP/RPE  
**Run type:** exact finite linear-program sharpening / scalar optimization  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

The RP theorem proved

```math
\liminf\mu_D\ge0.7811638359\ldots
```

and RPE excluded that endpoint.  This report retains the convex-perimeter cap on the
diameter-graph component defect inside the exact pocket ledger.  It raises the
explicit lower endpoint to

```math
\boxed{
\liminf\mu_D\ge\mu_\rho,
\qquad
\mu_\rho=0.809273370477446\ldots,
}
\tag{RL.1}
```

where `mu_rho` is defined analytically below.  In particular `mu_rho>0.8` by a
proof-level rational margin.

The new scalar endpoint is `h/D -> 2rho`, not `pi`.

---

## 1. Exact finite variables

Put

```math
X=d_P+Q,
\quad
x=X/D,
\quad
d=d_H/D,
\quad s=s_Z/D,
\quad
\alpha=a/D,
\quad c=c_B/D,
\quad \sigma=s_C/D,
\quad y=h/D.
```

The exact PC identities and the definition of `mu_D` give

```math
\boxed{x=\mu_D+d+s-c-2\sigma,}
\tag{1.1}
```

and

```math
\boxed{x=y-d-2s-\alpha.}
\tag{1.2}
```

Every loaded force-hull vertex is separated from the next by at least one, hence

```math
q\le P_F.
```

Cauchy's perimeter-diameter inequality gives `P_F<=pi D`.  Since `q=h+d_H`,

```math
\boxed{0\le d\le\pi-y.}
\tag{1.3}
```

Equations (1.1)-(1.3) are the complete small linear program used here.

---

## 2. Solve the pocket-currency LP exactly

Since `c,sigma,alpha>=0`, equations (1.1)-(1.2) imply

```math
x\le\mu_D+d+s,
\qquad
x\le y-d-2s.
\tag{2.1}
```

For fixed `mu,y`, maximize the right-side minimum over

```math
d\ge0,\quad s\ge0,\quad d\le\pi-y.
```

Because the first affine function increases and the second decreases in `d,s`, an
interior optimum equalizes them:

```math
2d+3s=y-\mu.
\tag{2.2}
```

On this line

```math
d+s=\frac{y-\mu}{3}+\frac d3,
```

so the objective is maximized by taking `d` as large as allowed.

If

```math
\pi-y\ge\frac{y-\mu}{2},
```

equivalently

```math
y\le y_c(\mu):=\frac{2\pi+\mu}{3},
```

one takes `d=(y-mu)/2`, `s=0` and obtains

```math
x\le\frac{\mu+y}{2}.
```

If `y>=y_c(mu)`, the perimeter cap binds: `d=pi-y`.  Equalization then gives

```math
s=\frac{3y-2\pi-\mu}{3}
```

and

```math
x\le\frac{2\mu+\pi}{3}.
```

Thus:

### Theorem RL.1 — exact perimeter-capped pocket budget

For every post-ZF source with `mu_D<2rho` (the only range needed below),

```math
\boxed{
\frac{d_P+Q}{D}
\le
M(\mu_D,y):=
\begin{cases}
(\mu_D+y)/2,
&2\rho\le y\le(2\pi+\mu_D)/3,\\[1ex]
(2\mu_D+\pi)/3,
&(2\pi+\mu_D)/3\le y\le\pi.
\end{cases}
}
\tag{RL.2}
```

The two formulas agree at the breakpoint.

---

## 3. Feed the LP into paired-pocket capacity

The RP opposite-pocket theorem and the exceptional-face estimate give, along every
convergent subsequence,

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le
\frac{\tau^2+\nu^2}{4\pi}
\le
\frac{x^2}{4\pi},
\tag{3.1}
```

where

```math
\tau=d_P/D,
\qquad \nu=Q/D,
\qquad x=\tau+\nu.
```

ZG and RL.2 therefore give

```math
\limsup\frac G{D^2}
\le
\frac{M(\mu,y)^2}{4\pi}.
\tag{3.2}
```

The GR/ZK+FSDB lower bound remains

```math
\liminf\frac G{D^2}
\ge
\Phi(y)-\frac\pi4\mu^2,
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
\tag{3.3}
```

Hence every survivor limit must satisfy

```math
\boxed{
\Phi(y)
\le
\frac\pi4\mu^2+\frac{M(\mu,y)^2}{4\pi},
\qquad 2\rho\le y\le\pi.
}
\tag{RL.3}
```

---

## 4. Only three candidate `y` values remain

On the first branch define

```math
F_1(\mu,y)
:=
\Phi(y)-\frac\pi4\mu^2-\frac{(\mu+y)^2}{16\pi}.
```

Then

```math
\frac{\partial^2F_1}{\partial y^2}
=-\frac{\sin y}{4}-\frac1{8\pi}<0.
\tag{4.1}
```

So `F_1` is strictly concave in `y`.

On the second branch define

```math
F_2(\mu,y)
:=
\Phi(y)-\frac\pi4\mu^2
-
\frac{(2\mu+\pi)^2}{36\pi}.
```

Here

```math
\frac{\partial^2F_2}{\partial y^2}
=-\frac{\sin y}{4}<0.
\tag{4.2}
```

Thus each branch attains its minimum at an endpoint.  Since the two formulas agree at

```math
y_c(\mu)=\frac{2\pi+\mu}{3},
```

the global minimum of the left-minus-right side of RL.3 occurs among exactly

```math
\boxed{y=2\rho,\quad y=y_c(\mu),\quad y=\pi.}
\tag{4.3}
```

---

## 5. The binding endpoint is `y=2rho`

At `y=2rho`, the first branch applies throughout the range below `0.82`.  Define

```math
R(\mu)
:=
\Phi(2\rho)
-
\frac\pi4\mu^2
-
\frac{(\mu+2\rho)^2}{16\pi}.
\tag{5.1}
```

It is strictly decreasing for `mu>=0`.  Let `mu_rho` be its unique positive zero:

```math
\boxed{
\Phi(2\rho)
=
\frac\pi4\mu_\rho^2
+
\frac{(\mu_\rho+2\rho)^2}{16\pi}.
}
\tag{RL.4}
```

Equivalently, since `Phi(2rho)=(2rho+sin(2rho))/4`, `mu_rho` is the positive root of

```math
(4\pi^2+1)\mu^2
+4\rho\mu
+4\rho^2
-8\pi\rho
-4\pi\sin(2\rho)=0.
\tag{5.2}
```

Numerically,

```math
\mu_\rho=0.809273370477446\ldots .
```

The decimal is diagnostic only.

### Exact lower bracket `mu_rho>0.8`

The preceding RP audit established

```math
\Phi(2\rho)>\frac{154451}{250000}
```

and, at `mu=4/5`,

```math
\frac\pi4\mu^2+
\frac{(\mu+2\rho)^2}{16\pi}
<\frac{42781}{70000}.
```

Their exact difference is

```math
\frac{727}{109375}>0.
```

Therefore

```math
\boxed{\mu_\rho>4/5.}
\tag{5.3}
```

### Exact upper bracket `mu_rho<0.82`

Use

```math
\frac{739}{1000}<\rho<\frac{37}{50},
\qquad
\sin\rho=\sqrt{1-\rho^2}<\frac{337}{500}.
```

Then

```math
\Phi(2\rho)
=\frac{\rho(1+\sin\rho)}2
<
\frac{30969}{50000}=0.61938.
\tag{5.4}
```

At `mu=41/50`, use `pi>6283/2000`, `pi<3927/1250`, and `rho>739/1000` to obtain

```math
\frac\pi4\mu^2+
\frac{(\mu+2\rho)^2}{16\pi}
>
0.63314416\ldots,
```

with exact excess over the right side of (5.4)

```math
\frac{360345757}{26180000000}>0.
```

Hence

```math
\boxed{\mu_\rho<41/50.}
\tag{5.5}
```

---

## 6. The breakpoint and `pi` candidates stay strictly positive

It remains to prove that neither other candidate in (4.3) becomes feasible before
`mu_rho`.

Since GR already excludes `mu<0.5947`, restrict to

```math
0.5947\le\mu\le\mu_\rho<0.82.
```

### Breakpoint

Set

```math
K(\mu):=F_1(\mu,y_c(\mu))=F_2(\mu,y_c(\mu)).
```

A direct derivative gives

```math
K'(\mu)
=
\frac{1+\cos y_c}{12}
-
\frac\pi2\mu
-
\frac{2\mu+\pi}{9\pi}<0
\tag{6.1}
```

throughout the displayed interval; already

```math
K'(\mu)<\frac16-\frac32(0.5947)<0.
```

So it suffices to check `mu=0.82`.  Put `m=41/50`.  Using

```math
y_c>\frac{2(6283/2000)+m}{3},
\qquad
\sin y_c=\sin(\pi-y_c),
```

and

```math
\sin t>t-t^3/6
```

for the resulting `t in (0,1)`, while upper-bounding the two negative terms with
`pi<3927/1250` and `1/pi<2000/6283`, gives the exact positive margin

```math
\boxed{
K(0.82)
>
\frac{1166007719199799}{32571072000000000}>0.
}
\tag{6.2}
```

### `y=pi`

The second-branch endpoint is

```math
F_2(\mu,\pi)
=
\frac\pi4(1-\mu^2)
-
\frac{(2\mu+\pi)^2}{36\pi},
```

which is strictly decreasing in `mu>=0`.  At `mu=0.82`, the same rational pi barriers
give

```math
\boxed{
F_2(0.82,\pi)
>
\frac{62341266419}{1130940000000}>0.
}
\tag{6.3}
```

Thus for every `mu<mu_rho`, all three candidate minima are positive, contradicting
RL.3.  This proves RL.1.

---

## 7. Equality structure

Any sequence with

```math
\mu_D\to\mu_\rho
```

must satisfy

```math
\boxed{h/D\to2\rho.}
\tag{7.1}
```

The other two candidate minima have fixed positive margins.  Equality in the first
LP branch further forces

```math
\frac{s_Z}{D},\frac aD,\frac{c_B}{D},\frac{s_C}{D}\to0,
\tag{7.2}
```

and

```math
\frac{d_H}{D}	o\frac{2\rho-\mu_\rho}{2},
\qquad
\frac{d_P+Q}{D}	o\frac{2\rho+\mu_\rho}{2}.
\tag{7.3}
```

The endpoint therefore lies in the Woodall caterpillar-forest phase with a positive
linear number of diameter components.  It is not the near-unicyclic regime of the old
Dido/PP scalar endpoint.

---

## 8. Next target

The endpoint (7.1)-(7.3) is highly rigid.  Scalar equality also forces FSDB area
saturation.  The projective diameter-direction concavity minimum at `h/D=2rho`
therefore has one macroscopic projective gap of size

```math
\pi-2\rho,
```

which appears as two opposite flat sides of `P_H/2`.  FS midpoint geometry transfers
those to two actual force-hull sides of asymptotic length

```math
D\cos\rho=\rho D.
```

Their two OP chains alone appear to require

```math
d_P/D\ge2\rho,
```

whereas (7.3) gives

```math
(d_P+Q)/D\to(2\rho+\mu_\rho)/2<2\rho.
```

This is the next endpoint contradiction to formalize.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Exact LP variables satisfy
  x=(d_P+Q)/D <= min(mu+d+s, y-d-2s),
  0<=d=d_H/D<=pi-y.
Solving the 2-variable LP gives
  x<=M(mu,y),
  M=(mu+y)/2 for y<=(2pi+mu)/3,
  M=(2mu+pi)/3 afterward.
Paired-pocket capacity then forces
  Phi(y)<=pi mu^2/4+M(mu,y)^2/(4pi).
Each branch is concave in y, so only y=2rho, the breakpoint, and y=pi matter.
The latter two stay positive through mu=0.82 by exact rational margins.
The 2rho candidate vanishes at the unique root
  mu_rho=0.809273370477446...,
with exact bracket 0.8<mu_rho<0.82.
Therefore liminf mu_D>=mu_rho.

Endpoint:
  h/D->2rho,
  s_Z,a,c_B,s_C=o(D),
  d_H/D->(2rho-mu_rho)/2,
  (d_P+Q)/D->(2rho+mu_rho)/2.
Next: FSDB equality gives two opposite rho*D force-hull sides, apparently forcing
d_P/D>=2rho>(2rho+mu_rho)/2. Formalize this contradiction.
```
