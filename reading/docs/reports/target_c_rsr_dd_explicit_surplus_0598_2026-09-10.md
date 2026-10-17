> Generated reading edition · [exact source](../../../docs/reports/target_c_rsr_dd_explicit_surplus_0598_2026-09-10.md) · source SHA-256 `156c91b90efd8c009db465892b8a2d5dc70c96cdbf6c4a46fc22c96d36b29bd3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-654B71246451","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — RSR/DD optimizer gives a generic post-ZF surplus floor above 0.598

**Date:** 2026-09-10  
**Repository branch base:** `ff31de4783ff49173d9f4bfdf61364735ff5a590`  
**Depends on:** RSJ, RD on this branch, FSDB, JC, DD  
**Run type:** exact optimizer localization + rational lower certificate  
**Target:** Target C, C-II after ZF  
**External input:** none beyond the already imported RSR theorem  
**Computation:** exact rational certificate for the displayed `0.598` bound; high-precision decimals only for orientation

## LEVEL I STATUS

`STILL OPEN`.

The preceding RD report proves that the generic post-ZF surplus

$$
\lambda_D:=\frac{e_{BB}+2s_C}{D}
$$

is bounded below by an explicit compact variational constant strictly larger than the
RSJ value `0.5921405436...`.  This report solves that variational problem analytically.

There is a unique number `y_RD` in `(y_R,pi/2)` at which the RSR/FSDB area-crossover
branch and the DD detour obstruction balance.  Define

$$
\Phi(y):=\frac{y+\sin y}{4},
\qquad
c_R:=\frac{\pi}{(\pi-2)^2},
\tag{RX.1}
$$

$$
\boxed{
p_e(y):=2+2\sqrt{\frac{\Phi(y)}{c_R}}.}
\tag{RX.2}
$$

Set

$$
u(y):=2y-p_e(y),
\tag{RX.3}
$$

and

$$
\boxed{
E(y):=
\Phi(y)-\frac{2}{\sqrt3}y^{3/2}\sqrt{u(y)}
}
\tag{RX.4}
$$

for `y>=y_R`, where RSJ gives `p_e(y)<=2y`.  Put

$$
\boxed{
d_e(y):=
\sqrt{\max\left\{0,\frac4\pi E(y)\right\}},}
\tag{RX.5}
$$

and let

$$
\boxed{
r_e(y):=
R\bigl(\Phi(y),p_e(y)-y\bigr),}
\tag{RX.6}
$$

where

$$
R(A,m)=
\frac{\sqrt{4\pi(\pi^2+1)A-\pi^2m^2}-m}{\pi^2+1}.
\tag{RX.7}
$$

Then `d_e` strictly decreases from above `r_e`, while `r_e` strictly increases.  Their
unique intersection defines `y_RD`:

$$
\boxed{d_e(y_{RD})=r_e(y_{RD}).}
\tag{RX.8}
$$

The generic post-ZF threshold is

$$
\boxed{
\lambda_{RD}:=r_e(y_{RD})=d_e(y_{RD}),
}
\tag{RX.9}
$$

and every unbounded post-ZF survivor satisfies

$$
\boxed{
\liminf_{D\to\infty}\frac{e_{BB}+2s_C}{D}
\ge\lambda_{RD}>0.598.
}
\tag{RX.10}
$$

Numerically, only for orientation,

$$
y_{RD}=1.5245227034919423744\ldots,
\tag{RX.11}
$$

$$
p_{RD}=p_e(y_{RD})
=3.0231369667364346005\ldots,
\tag{RX.12}
$$

and

$$
\boxed{
\lambda_{RD}
=0.5981536184601480388\ldots .
}
\tag{RX.13}
$$

The theorem claim is RX.10; the longer decimal in RX.13 is not a proof dependency.

---

## 1. Enlarge the perimeter domain

RD works on the actual DB domain

$$
2\rho\le y\le\pi,
\qquad
g(y):=y+2\cos(y/2)\le p\le\min\{2y,\pi\}.
$$

For a lower bound we may enlarge this to

$$
\boxed{
\widetilde{\mathcal R}:=
\{(y,p):2\rho\le y\le\pi,\ y\le p\le\min\{2y,\pi\}\}.
}
\tag{1.1}
$$

Every actual post-ZF survivor lies in this larger region, so the minimum of the RD
objective over `widetilde R` is a valid universal lower bound.  This enlargement is
useful because the lower DB perimeter boundary never has to be optimized separately.

Retain

$$
A(y,p)=\max\{\Phi(y),\Psi(p)\},
\qquad
\Psi(p)=c_R(p/2-1)^2.
\tag{1.2}
$$

Since `p<=2y`, the JC branch is always

$$
m=p-y.
$$

Define

$$
J(y,p):=R(A(y,p),p-y)
\tag{1.3}
$$

and

$$
D(y,p):=
\sqrt{\max\left\{0,
\frac4\pi\left[
A(y,p)-\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}
\right]
\right\}}.
\tag{1.4}
$$

RD proves every survivor satisfies

$$
\lambda\ge M(y,p):=\max\{J(y,p),D(y,p)\}.
\tag{1.5}
$$

---

## 2. Fixed-`y` geometry before the area crossover

For fixed `y`, RSJ's area crossover is `p=p_e(y)` from RX.2.  On the branch

$$
p\le p_e(y),
$$

we have

$$
A(y,p)=\Phi(y).
\tag{2.1}
$$

Hence:

1. `J(y,p)=R(Phi(y),p-y)` is strictly **decreasing** in `p`, because `R` is strictly
   decreasing in its second argument;
2. `D(y,p)` is strictly **increasing** in `p` wherever positive, because the detour
   factor `sqrt(2y-p)` strictly decreases.

At the left endpoint `p=y`,

$$
\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}
=\frac2{\sqrt3}y^2>1>\Phi(y),
$$

because `y>1` and `Phi(y)<=pi/4<1`.  Therefore

$$
D(y,y)=0<J(y,y).
\tag{2.2}
$$

If `y<=y_R`, RSJ gives `p_e(y)>=2y`; thus the entire enlarged interval
`[y,2y]` lies on the `Phi` branch.  At `p=2y`, the DD detour vanishes, so

$$
D(y,2y)=\sqrt{\frac{4\Phi(y)}\pi}.
\tag{2.3}
$$

JC at the same point has a strictly positive cavity term:

$$
\Phi(y)-\frac\pi4J(y,2y)^2
=\frac{(J(y,2y)+y)^2}{4\pi}>0.
$$

Hence

$$
D(y,2y)>J(y,2y).
\tag{2.4}
$$

By strict monotonicity there is a unique crossing `J=D` in `(y,2y)`.

For `y>=y_R`, the same argument applies on `[y,p_e(y)]` whenever

$$
d_e(y):=D(y,p_e(y))\ge r_e(y):=J(y,p_e(y)).
\tag{2.5}
$$

When the reverse strict inequality holds, there is no crossing before `p_e`: `J>D`
throughout that interval and the best point there is `p_e`.

For `p>=p_e(y)`, both obstructions increase.  RSJ proves `J` increases after the
area crossover.  Meanwhile `Psi(p)` increases and the DD detour decreases, so the
radicand defining `D` also increases.  Therefore no fixed-`y` minimizer lies strictly
to the right of `p_e(y)`.

Thus the complete fixed-`y` problem is controlled by whether `d_e(y)` is above or
below `r_e(y)`.

---

## 3. The DD value on the area crossover strictly decreases

RSJ proves

$$
y_R>3/2,
\qquad
p_e(y_R)=2y_R>3.
\tag{3.1}
$$

Differentiate RX.2:

$$
p_e'(y)=\frac{\Phi'(y)}{\sqrt{c_R\Phi(y)}}.
\tag{3.2}
$$

On `[y_R,pi/2]`, `Phi(y)>1/2` and `c_R>2`, while

$$
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
$$

Therefore

$$
\boxed{p_e'(y)<1/2.}
\tag{3.3}
$$

Consequently, with `u(y)=2y-p_e(y)`,

$$
\boxed{u'(y)>3/2.}
\tag{3.4}
$$

For `y in (y_R,pi/2]`,

$$
0<u(y)<\pi-3<1.
\tag{3.5}
$$

Differentiate the untruncated DD radicand `E(y)` from RX.4:

$$
E'(y)=
\Phi'(y)
-
\frac2{\sqrt3}
\left[
\frac32y^{1/2}\sqrt u
+
\frac12y^{3/2}\frac{u'}{\sqrt u}
\right].
\tag{3.6}
$$

Using `Phi'<=1/2`, `y>1`, `u'>1`, and `0<u<1`,

$$
E'(y)
<\frac12-\frac1{\sqrt3}<0.
\tag{3.7}
$$

Hence `d_e(y)` is strictly decreasing until its radicand reaches zero, and is zero
thereafter.

At `y=y_R`, `u=0`, so

$$
d_e(y_R)=\sqrt{\frac{4\Phi(y_R)}\pi}.
$$

The defining RSJ JC equality has a positive cavity term, hence

$$
\boxed{d_e(y_R)>r_e(y_R)=\lambda_R.}
\tag{3.8}
$$

At `y=pi/2`, the DD radicand is already negative.  Here

$$
p_e(\pi/2)
=2+(\pi-2)\sqrt{\frac{\pi+2}{2\pi}},
$$

so

$$
u(\pi/2)
=(\pi-2)\left(1-\sqrt{\frac{\pi+2}{2\pi}}\right).
\tag{3.9}
$$

Using `pi>31/10`,

$$
\frac{\pi+2}{2\pi}
=\frac12+\frac1\pi
<\frac{51}{62}<\frac{100}{121},
$$

and `pi-2>11/10`, therefore

$$
\boxed{u(\pi/2)>1/10.}
\tag{3.10}
$$

Also

$$
\Phi(\pi/2)=\frac{\pi+2}{8}<\frac9{14}.
$$

The squared DD term satisfies

$$
\Delta(\pi/2,p_e)^2
=\frac43\left(\frac\pi2\right)^3u
>
\frac43\left(\frac{31}{20}\right)^3\frac1{10}.
$$

Direct rational arithmetic gives

$$
\frac43\left(\frac{31}{20}\right)^3\frac1{10}
-\left(\frac9{14}\right)^2
=\frac{244759}{2940000}>0.
\tag{3.11}
$$

Thus the DD term exceeds `Phi(pi/2)`, so

$$
\boxed{d_e(\pi/2)=0<r_e(\pi/2).}
\tag{3.12}
$$

RSJ proves `r_e(y)` is strictly increasing for `y>=y_R`.  Equations
(3.7), (3.8), and (3.12) therefore give a unique

$$
\boxed{y_{RD}\in(y_R,\pi/2)}
$$

with `d_e(y_RD)=r_e(y_RD)`.

---

## 4. The pre-transition crossing value strictly decreases

For every `y<=y_RD`, the fixed-`y` minimizer in the enlarged domain is the unique
point before or at `p_e(y)` where

$$
J(y,p)=D(y,p)=:\lambda.
\tag{4.1}
$$

On this branch `A=Phi(y)`.  Put

$$
S:=\Phi(y)-\frac\pi4\lambda^2>0.
\tag{4.2}
$$

JC equality gives

$$
p-y=2\sqrt{\pi S}-\lambda.
\tag{4.3}
$$

DD equality gives

$$
2y-p=\frac{3S^2}{4y^3}.
\tag{4.4}
$$

Eliminating `p`, the crossing value is characterized by

$$
\boxed{
F(y,\lambda):=
 y+\lambda-2\sqrt{\pi S}
 -\frac{3S^2}{4y^3}=0.
}
\tag{4.5}
$$

The partial derivative in `lambda` is strictly positive:

$$
F_\lambda
=1+
\frac{\pi^{3/2}\lambda}{2\sqrt S}
+
\frac{3\pi\lambda S}{4y^3}
>0.
\tag{4.6}
$$

We now prove `F_y>0` uniformly on every such crossing.  This is the only quantitative
monotonicity estimate needed in the optimizer.

First, RSJ applies on the enlarged domain `y<=p<=pi`, so every JC threshold, hence
every crossing value, satisfies

$$
\lambda\ge\lambda_R>\lambda_{FSJC}>7/12.
\tag{4.7}
$$

For completeness, the last rational inequality follows by evaluating the FSJC
quadratic at `lambda=7/12` and `y=pi/2`:

$$
Q(7/12)
=\frac{13\pi^2-60\pi+49}{144}
<\frac{13(22/7)^2-60(22/7)+49}{144}
=-\frac{547}{7056}<0.
\tag{4.8}
$$

Next `rho>73/100`, because

$$
\cos(73/100)
\ge1-\frac12(73/100)^2
>73/100.
$$

Thus

$$
y\ge2\rho>73/50>7/5.
\tag{4.9}
$$

Since `y<=y_RD<pi/2`,

$$
\Phi(y)<9/14.
$$

Using (4.7) and `pi>3`,

$$
S
<\frac9{14}-\frac34\left(\frac7{12}\right)^2
=\frac{521}{1344}<\frac25.
\tag{4.10}
$$

Let `m=p-y`.  By DD equality (4.4),

$$
m=y-\frac{3S^2}{4y^3}.
$$

Using (4.9)--(4.10),

$$
\frac{3S^2}{4y^3}
<\frac{15}{343}<\frac3{50},
$$

so

$$
\boxed{m>7/5.}
\tag{4.11}
$$

We also need a crude derivative bound for `Phi`.  The alternating cosine estimate

$$
\cos(3/4)
<1-\frac12(3/4)^2+\frac1{24}(3/4)^4
=\frac{1499}{2048}<\frac34
$$

shows `rho<3/4`.  Therefore, because `y>=2rho` and cosine decreases on this interval,

$$
\cos y\le\cos(2\rho)=2\rho^2-1<1/8,
$$

and hence

$$
\boxed{\Phi'(y)<9/32.}
\tag{4.12}
$$

Differentiate (4.5) at fixed `lambda`:

$$
F_y
=1-
\frac{\sqrt\pi\,\Phi'(y)}{\sqrt S}
-
\frac{3S\Phi'(y)}{2y^3}
+
\frac{9S^2}{4y^4}.
\tag{4.13}
$$

By JC equality,

$$
2\sqrt{\pi S}=\lambda+m.
$$

Using `pi<22/7`, (4.7), (4.11), and (4.12),

$$
\frac{\sqrt\pi\,\Phi'}{\sqrt S}
=\frac{2\pi\Phi'}{\lambda+m}
<\frac{1485}{1666}.
\tag{4.14}
$$

Using (4.9)--(4.12),

$$
\frac{3S\Phi'}{2y^3}
<\frac{675}{10976}.
\tag{4.15}
$$

Discarding the final positive term in (4.13),

$$
\boxed{
F_y
>
1-\frac{1485}{1666}-\frac{675}{10976}
=\frac{8797}{186592}>0.
}
\tag{4.16}
$$

Therefore implicit differentiation of `F(y,lambda(y))=0` gives

$$
\boxed{
\lambda'(y)=-F_y/F_\lambda<0
}
\tag{4.17}
$$

throughout the pre-transition branch.

---

## 5. Global minimum

Sections 2--4 give the complete optimizer on the enlarged domain.

- For `2rho<=y<=y_RD`, the fixed-`y` optimum is the unique JC/DD crossing and its
  value strictly decreases with `y` by (4.17).
- At `y=y_RD`, that crossing reaches the RSR/FSDB area-crossover perimeter
  `p=p_e(y_RD)`.
- For `y_RD<=y<=pi/2`, `d_e<=r_e`; the fixed-`y` optimum is therefore `p=p_e(y)`
  with value `r_e(y)`, which RSJ proves strictly increases.
- For `y>=pi/2`, the RD objective is at least its JC component.  RSJ proves the
  minimum JC value at fixed `y` is `r_e(y)` and that `r_e` continues to increase.
  Hence this range is also strictly above the value at `y_RD`.

Thus the enlarged-domain objective has the unique global minimum

$$
\boxed{
(y,p)=(y_{RD},p_e(y_{RD})).
}
\tag{5.1}
$$

The actual DB domain is a subset of the enlarged domain, so the same value is a valid
generic post-ZF lower bound.

Equivalently, the optimizing triple `(y_RD,p_RD,lambda_RD)` is the unique transition
in `y_R<y<pi/2` satisfying

$$
\boxed{
\Phi(y)=\Psi(p),
}
\tag{5.2}
$$

$$
\boxed{
\Phi(y)-\frac\pi4\lambda^2
=\frac{(\lambda+p-y)^2}{4\pi},
}
\tag{5.3}
$$

$$
\boxed{
\Phi(y)-\frac\pi4\lambda^2
=\frac2{\sqrt3}y^{3/2}\sqrt{2y-p}.
}
\tag{5.4}
$$

These three elementary equations define the exact constant in RX.9.

---

## 6. Exact rational certificate `lambda_RD>0.598`

It remains to certify a simple explicit decimal below the exact transition.  Take

$$
\boxed{y_0=3811/2500=1.5244.}
\tag{6.1}
$$

The following elementary rational enclosures are sufficient:

$$
\frac{333}{106}<\pi<\frac{355}{113},
\tag{6.2}
$$

and the alternating Taylor series for sine at `y_0` gives

$$
\boxed{
\frac{4994619}{5000000}
<\sin y_0
<\frac{249731}{250000}.
}
\tag{6.3}
$$

Let `A_0=Phi(y_0)` and `p_0=p_e(y_0)`.  Since
`c_R=pi/(pi-2)^2` is decreasing for `pi>2`, exact rational propagation of
(6.2)--(6.3) gives

$$
\boxed{
0.51152
<\sqrt{A_0/c_R}
<0.51158.
}
\tag{6.4}
$$

Thus, with `m_0=p_0-y_0`,

$$
1.49864<m_0<1.49876,
\tag{6.5}
$$

with the slightly sharper exact interval generated by (6.4) used below.

Consider the JC quadratic

$$
Q(\lambda)
=(\pi^2+1)\lambda^2+2m_0\lambda+m_0^2-4\pi A_0.
\tag{6.6}
$$

Exact rational interval substitution gives

$$
\boxed{Q(299/500)<-0.0012<0,}
\tag{6.7}
$$

and

$$
\boxed{Q(599/1000)>0.0138>0.}
\tag{6.8}
$$

Since `Q` is strictly increasing at its positive root,

$$
\boxed{0.598<r_e(y_0)<0.599.}
\tag{6.9}
$$

Now bound the DD branch.  From (6.4),

$$
0<2y_0-p_0<0.02576.
$$

Use

$$
\sqrt3>433/250,
\qquad
\sqrt{y_0}<247/200,
\qquad
\sqrt{0.02576}<321/2000.
\tag{6.10}
$$

These are certified by squaring.  Therefore the DD detour term at `p_0` is bounded
above by

$$
\Delta(y_0,p_0)
<
\frac{500}{433}
\cdot\frac{3811}{2500}
\cdot\frac{247}{200}
\cdot\frac{321}{2000}.
\tag{6.11}
$$

Combining this with the lower bound for `A_0` from (6.3), exact rational arithmetic
gives

$$
\boxed{
A_0-\Delta(y_0,p_0)
>
\frac{355}{113}\frac{(599/1000)^2}{4}.
}
\tag{6.12}
$$

Hence

$$
\boxed{d_e(y_0)>0.599.}
\tag{6.13}
$$

Together with (6.9),

$$
d_e(y_0)>r_e(y_0),
$$

so the unique transition satisfies

$$
y_{RD}>y_0.
$$

Since `r_e` is strictly increasing,

$$
\boxed{
\lambda_{RD}=r_e(y_{RD})
>r_e(y_0)>0.598.
}
\tag{6.14}
$$

This proves RX.10.  A companion exact-Fraction verification script records every
rational comparison in this section.

---

## 7. Numerical orientation and gain

Solving the exact system (5.2)--(5.4) at high precision gives

$$
y_{RD}=1.5245227034919423744289493856\ldots,
$$

$$
p_{RD}=3.0231369667364346004511626049\ldots,
$$

$$
\Phi(y_{RD})=0.6308630676027113234822087061\ldots,
$$

$$
2y_{RD}-p_{RD}
=0.0259084402474501484067361663\ldots,
$$

and

$$
\lambda_{RD}
=0.5981536184601480387743485877\ldots .
$$

Relative to the generic RSJ base point,

$$
0.5981536184\ldots-0.5921405436\ldots
=0.0060130748\ldots .
$$

The rigorous advertised improvement is the simpler

$$
\boxed{\lambda_D\ge0.598-o(1).}
$$

---

## 8. Equality-near localization

Any sequence approaching the exact RD variational endpoint must force

$$
\boxed{
\frac hD\to y_{RD},
\qquad
\frac{\operatorname{per}F}{D}\to p_{RD},
}
\tag{8.1}
$$

and both cavity bounds must be active:

$$
\boxed{
A-rac\pi4\lambda_{RD}^2
=
\frac{(\lambda_{RD}+p_{RD}-y_{RD})^2}{4\pi}
=
\frac2{\sqrt3}y_{RD}^{3/2}\sqrt{2y_{RD}-p_{RD}}.
}
\tag{8.2}
$$

Unlike the old RSJ endpoint, the outer-walk detour is now positive:

$$
2y_{RD}-p_{RD}
=0.02590844\ldots .
$$

Thus the next structural target is not another zero-detour compactness argument.  It
is equality/stability in DD itself: the total cavity capacity must simultaneously
saturate the Dirichlet mean-height estimate, the global Cauchy aggregation, the
`x_B+a<=b` relaxation, and the `z=0` maximization.  Those equality conditions are
highly restrictive and expose several independent positive defect currencies.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| enlarged domain is valid for lower bounding | proved | actual DB region is a subset |
| fixed-`y` optimizer before crossover | proved | JC decreases and DD increases in `p` |
| `d_e` decreases on `[y_R,pi/2]` | proved | explicit derivative bound |
| unique transition `y_RD` | proved | `d_e(y_R)>r_e(y_R)`, `d_e(pi/2)=0`, opposite monotonicities |
| pre-transition optimum decreases in `y` | proved | implicit equation with `F_y>0`, `F_lambda>0` |
| global optimizer at `y_RD` | proved | decreasing branch meets increasing RSJ branch |
| `lambda_RD>0.598` | proved | rational certificate at `y_0=3811/2500` |
| long decimal `0.5981536184...` | numerical orientation | not a proof dependency |
| Level I | still open | no universal upper contradiction for high-surplus survivors |

---

## 10. Next run

Exploit the equality ledger behind RD rather than immediately optimizing another
scalar inequality.  Near the new endpoint, the proof requires simultaneously:

1. `z=(Q+2s_Z)/D` near zero, because Section 3 of RD showed any positive `z` reduces
   the DD/exceptional-face capacity;
2. `x_B+a` near the full outer-walk length `b`, so `a/q` must be close to one;
3. near equality in DD's one-pocket Dirichlet estimate and in the global Cauchy step;
4. near equality in GU attachment-cell capacity and in the JC perimeter budget.

The first two conditions say almost every loaded hull side is missing as a contact
side while bounded exceptional-face and mixed-rank defects vanish.  Combine that with
PC's exact identity `a+k=c_I+c_B+s_C+2` and the diameter/contact ledgers.  A positive
linear incompatibility among these currencies would either exclude the RD endpoint or
raise the explicit floor again.
