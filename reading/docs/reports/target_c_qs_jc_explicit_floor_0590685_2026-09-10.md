> Generated reading edition · [exact source](../../../docs/reports/target_c_qs_jc_explicit_floor_0590685_2026-09-10.md) · source SHA-256 `080b52c3fa1dca359138edf4ebafbd3aed8962c780a98c2c4d94c0afb15601c0`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 2 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 41 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-B6ED6DCECD60","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — QS/JC raises the explicit post-ZF floor to 0.590686

**Date:** 2026-09-10  
**Branch base:** `f977f2d0d25f5022c2a587e59cab38375d85caee`  
**Depends on:** DB, FSDB, FD/JC, QS, and SJ on this branch  
**Run type:** exact monotonic optimization / explicit floor improvement  
**Target:** Target C, C-II after ZF  
**External input:** none  
**Computation:** high-precision decimal evaluation only; exact implicit equations are the proof

## LEVEL I STATUS

`STILL OPEN`.

The QS stability envelope can be optimized analytically.  Its derivative is uniformly
larger than `1/2` throughout the post-ZF perimeter range.  This gives the same unique
crossover structure used in SJ, but with the strictly stronger area currency
`mathcal Z`.

The result is

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{QS}
=0.5906857322625200\ldots .
}
\tag{QX.1}
```

The exact optimizing state is characterized below.  Numerically,

```math
\boxed{
y_{QS}=1.5347842224020880\ldots,}
\tag{QX.2}
```

```math
\boxed{
p_{QS}=2y_{QS}=3.0695684448041760\ldots,}
\tag{QX.3}
```

and the actual centered-inradius ratio in the QS stability envelope is

```math
\boxed{
a_{QS}=0.8255674705463349\ldots .}
\tag{QX.4}
```

This is a certified analytic improvement over the exact SJ constant
`lambda_SA`; the displayed decimals are numerical evaluations of exact implicit
constants and are not proof dependencies.

---

## 1. Differentiate the QS stability crossing

For `p in [4rho,pi)`, QS defines `a=a_s(p)` as the unique crossing

```math
L(a,p)=B(a,p),
\tag{1.1}
```

where

```math
L(a,p)=\frac{ap}{4},
\tag{1.2}
```

```math
B(a,p)
=
\tau(a)-pq-\pi q^2,
\tag{1.3}
```

```math
q:=\sqrt{\frac{f(a)-p}{2}}>0,
\tag{1.4}
```

```math
f(a)=2\left(\arcsin a+\sqrt{1-a^2}\right),
\qquad
\tau(a)=\frac12\left(\arcsin a+a\sqrt{1-a^2}\right).
\tag{1.5}
```

QS proves

```math
\mathcal Z(p)=\frac{p a_s(p)}4.
\tag{1.6}
```

Put

```math
s:=\sqrt{1-a^2},
\qquad
f'(a)=2\frac{1-a}{s},
\qquad
\tau'(a)=s.
\tag{1.7}
```

Since

```math
q_a=\frac{f'(a)}{4q},
\qquad
q_p=-\frac1{4q},
```

the partial derivatives of `B` are

```math
\boxed{
B_a
=s-\frac{p f'(a)}{4q}-\frac\pi2 f'(a),
}
\tag{1.8}
```

```math
\boxed{
B_p
=-q+\frac{p}{4q}+\frac\pi2.
}
\tag{1.9}
```

QS already proves `B_a<0`.  Hence the crossing is transversal and

```math
\frac{da}{dp}
=
\frac{B_p-a/4}{p/4-B_a}.
\tag{1.10}
```

The numerator is positive on the post-ZF range, so `a_s(p)` is increasing.  Indeed,
QS gives `a>alpha(p)>1/2`, while the bounds established below give `q<5/12` and
`p>14/5`; therefore

```math
-q+\frac{p}{4q}>-\frac5{12}+\frac{14/5}{4(5/12)}>0,
```

and `pi/2-a/4>0`.

Differentiate (1.6).  Substituting (1.10) and simplifying gives

```math
\boxed{
\mathcal Z'(p)
=
\frac{pB_p-aB_a}{p-4B_a}.
}
\tag{1.11}
```

Since the denominator is positive, `mathcal Z'(p)>1/2` is equivalent to

```math
\boxed{
S:=p(2B_p-1)+(4-2a)B_a>0.
}
\tag{1.12}
```

---

## 2. A uniform exact derivative bound

Insert (1.8)--(1.9) into (1.12):

```math
\begin{aligned}
S
={}&
\frac{p}{2q}\left[p-(2-a)f'(a)\right]
-2pq+p(\pi-1)\\
&+2(2-a)s
-\pi(2-a)f'(a).
\end{aligned}
\tag{2.1}
```

We now bound every potentially negative term by crude rational constants.  These
bounds are deliberately loose; the derivative margin is large.

First, DB gives

```math
p\ge4\rho.
```

Since `rho>7/10`,

```math
\boxed{p>14/5.}
\tag{2.2}
```

QS has `a>alpha(p)>1/2`.  Also

```math
(2-a)f'(a)
=2(2-a)\sqrt{\frac{1-a}{1+a}}.
\tag{2.3}
```

Both positive factors decrease with `a`, so for `a>=1/2`,

```math
(2-a)f'(a)
\le
3\sqrt{\frac13}
=\sqrt3
<\frac74.
\tag{2.4}
```

Next, because `f(a)<=pi`,

```math
2q^2=f(a)-p
<\pi-\frac{14}{5}
<\frac{22}{7}-\frac{14}{5}
=\frac{12}{35}.
```

Thus

```math
q^2<\frac6{35}<\frac{25}{144},
\qquad
\boxed{q<5/12.}
\tag{2.5}
```

Use (2.2)--(2.5), `pi>3`, `pi<22/7`, and discard the positive term
`2(2-a)s`.  Then (2.1) gives

```math
\begin{aligned}
S
&>
\frac{14/5}{2(5/12)}
\left(\frac{14}{5}-\frac74\right)
-2\frac{22}{7}\frac5{12}
+\frac{14}{5}(3-1)
-\frac{22}{7}\frac74\\
&=
\frac{441}{125}
-\frac{55}{21}
+\frac{28}{5}
-\frac{11}{2}\\
&=
\boxed{\frac{5297}{5250}>0.}
\end{aligned}
\tag{2.6}
```

Therefore

```math
\boxed{
\mathcal Z'(p)>\frac12
\qquad(4\rho\le p<\pi).
}
\tag{2.7}
```

This is the key new analytic fact.

---

## 3. The unique FSDB/QS crossover

For fixed `y in [2rho,pi)`, DB allows

```math
g(y):=y+2\cos(y/2)\le p\le\pi.
\tag{3.1}
```

At the lower perimeter endpoint, QPA gives

```math
\alpha(g(y))=\sin(y/2).
```

Evaluating the QS minimization at this left endpoint value `a=alpha(g(y))` gives

```math
\mathcal Z(g(y))
\le
\tau(\sin(y/2))
=
\frac{y+\sin y}{4}
=\Phi(y).
\tag{3.2}
```

The inequality is in fact strict for `y<pi`: at `a=alpha(g(y))`, the QS stability
branch equals `Phi(y)` while the support branch is strictly smaller; moving `a`
slightly to the right decreases the stability branch continuously and leaves the
support branch below `Phi(y)`.  Hence

```math
\boxed{
\mathcal Z(g(y))<\Phi(y)
\qquad(2\rho\le y<\pi).
}
\tag{3.3}
```

At the other endpoint,

```math
\mathcal Z(\pi)=\pi/4>\Phi(y)
\qquad(y<\pi).
\tag{3.4}
```

By (2.7), `mathcal Z` is strictly increasing.  Thus for each `y<pi` there is a unique

```math
\boxed{
c(y)\in(g(y),\pi)
\quad\text{such that}\quad
\mathcal Z(c(y))=\Phi(y).
}
\tag{3.5}
```

Implicit differentiation and (2.7) give

```math
\boxed{
0\le c'(y)
=
\frac{\Phi'(y)}{\mathcal Z'(c(y))}
<1,
}
\tag{3.6}
```

because

```math
\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
```

---

## 4. Optimize the actual perimeter for fixed `y`

For the strengthened area currency

```math
A(y,p)=\max\{\Phi(y),\mathcal Z(p)\},
```

the JC threshold is

```math
R(A(y,p),m(y,p)),
\qquad
m(y,p)=\min\{y,p-y\}.
\tag{4.1}
```

As in SJ, `R` increases with `A` and decreases with `m`.

For `p<=c(y)`, the area is fixed at `Phi(y)`.  Increasing `p` increases `m` until
`p=2y`; thus the threshold decreases until that balance point.

For `p>=c(y)` and `p>=2y`, `m=y` is fixed while `mathcal Z(p)` increases, so the
threshold increases.

In the only remaining region

```math
c(y)<p<2y,
```

one has `m=p-y` and

```math
\frac d{dp}R(\mathcal Z(p),p-y)
=
\frac{2\pi\mathcal Z'(p)-(R+m)}{(\pi^2+1)R+m}.
\tag{4.2}
```

As in SJ, `A<=pi/4` implies `R<1`, and `p<2y` implies `m<=pi/2`.  By (2.7),

```math
2\pi\mathcal Z'(p)>\pi>1+\frac\pi2>R+m.
\tag{4.3}
```

Hence (4.2) is strictly positive.

Therefore the fixed-`y` optimizer is exact:

- if `c(y)>=2y`, the minimum is `R(Phi(y),y)`;
- if `c(y)<2y`, the unique minimum is attained at `p=c(y)` and equals
  `R(Phi(y),c(y)-y)`.

---

## 5. Unique global transition

At `y=2rho`, DB's defining equality gives

```math
g(2\rho)=4\rho=2(2\rho).
```

By (3.3),

```math
c(2\rho)>2(2\rho).
\tag{5.1}
```

At `y=pi/2`,

```math
2y=\pi,
\qquad
c(\pi/2)<\pi
```

by (3.4), so

```math
c(\pi/2)<2(\pi/2).
\tag{5.2}
```

Because `c'(y)<1`,

```math
(c(y)-2y)'<-1.
```

Hence there is a unique

```math
\boxed{
y_{QS}\in(2\rho,\pi/2)
\quad\text{such that}\quad
c(y_{QS})=2y_{QS}.
}
\tag{5.3}
```

Equivalently,

```math
\boxed{
\mathcal Z(2y_{QS})=\Phi(y_{QS}).
}
\tag{5.4}
```

For `y<=y_QS`, the optimized threshold is the FSJC left branch
`R(Phi(y),y)`, which FSJC proves is strictly decreasing on `[2rho,pi/2]`.
For `y>=y_QS`, `Phi(y)` increases while `c(y)-y` decreases by (3.6), so the
optimized threshold strictly increases.

Therefore the unique global minimum occurs at

```math
\boxed{
(y,p)=(y_{QS},2y_{QS}).
}
\tag{5.5}
```

---

## 6. Exact implicit characterization

Let

```math
a_{QS}:=a_s(2y_{QS}),
\qquad
q_{QS}:=\sqrt{\frac{f(a_{QS})-2y_{QS}}2}.
\tag{6.1}
```

The transition equation `mathcal Z(2y)=Phi(y)` becomes

```math
\boxed{
2a_{QS}y_{QS}=y_{QS}+\sin y_{QS}.
}
\tag{6.2}
```

The QS crossing equation becomes

```math
\boxed{
\frac{a_{QS}y_{QS}}2
=
\tau(a_{QS})
-2y_{QS}q_{QS}
-\pi q_{QS}^2,
}
\tag{6.3}
```

with

```math
\boxed{
2q_{QS}^2=f(a_{QS})-2y_{QS}.
}
\tag{6.4}
```

Equations (6.2)--(6.4), together with

```math
2\rho<y_{QS}<\pi/2,
\qquad
\alpha(2y_{QS})<a_{QS}<1,
\qquad q_{QS}>0,
```

uniquely define the optimizing state.

Finally define

```math
\boxed{
\lambda_{QS}:=R(\Phi(y_{QS}),y_{QS}).
}
\tag{6.5}
```

Equivalently, it is the positive root of

```math
\boxed{
(\pi^2+1)\lambda^2
+2y_{QS}\lambda
+y_{QS}^2
-\pi(y_{QS}+\sin y_{QS})=0.
}
\tag{6.6}
```

Sections 1--5 prove QX.1 exactly.

---

## 7. Numerical orientation

High-precision evaluation of the exact system gives

```math
y_{QS}
=1.5347842224020879842723098096\ldots,
```

```math
p_{QS}
=3.0695684448041759685446196192\ldots,
```

```math
a_{QS}
=0.8255674705463349127305636050\ldots,
```

```math
q_{QS}
=0.0269494537595010695113653015\ldots,
```

```math
\Phi(y_{QS})
=0.6335339641614576520496906312\ldots,
```

and

```math
\boxed{
\lambda_{QS}
=0.5906857322625200333351113418\ldots .
}
```

The exact improvement over SJ is positive by QS/SJ even without decimals; numerically
it is approximately

```math
4.2894953\times10^{-5}.
```

---

## 8. Endpoint localization

Any sequence approaching the QX lower endpoint must force all strict optimization
steps to equality.  In particular,

```math
\boxed{
\frac hD\to y_{QS},
\qquad
\frac{\operatorname{per}F}{D}\to2y_{QS},
}
\tag{8.1}
```

```math
\boxed{
\frac{s_C}{D}\to0,
}
\tag{8.2}
```

and the force-hull area must satisfy

```math
\boxed{
\frac{\operatorname{area}F}{D^2}
\to
\Phi(y_{QS})=\mathcal Z(2y_{QS}).
}
\tag{8.3}
```

The central symmetral's centered inradius ratio must simultaneously tend to
`a_QS`, and QS's two lower bounds must balance:

```math
\frac{a_{QS}p_{QS}}4
=
B(a_{QS},p_{QS}).
\tag{8.4}
```

Unlike the SJ endpoint, QS deliberately builds enough geometric slack into the area
bound that the old strip/tangency contradiction no longer fires immediately: the
support-area and clipped-disk-stability branches meet at a positive perimeter deficit
`2q_QS^2`.  The next structural attack must use the *equality geometry of the
support-deficit Lipschitz estimate* or the DB/FSDB direction-gap equality conditions.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `mathcal Z'(p)>1/2` on post-ZF range | proved | explicit derivative + rational lower bound `5297/5250` |
| unique FSDB/QS crossover `c(y)` | proved | strict endpoint signs + `mathcal Z` monotonicity |
| fixed-`y` optimizer | proved | JC root monotonicity and (4.2)--(4.3) |
| unique global transition `y_QS` | proved | `c'<1` + FSJC left monotonicity |
| exact floor `lambda_QS` | proved asymptotically | complete compact optimization |
| decimal `0.59068573226252...` | numerical evaluation | exact equations (6.2)--(6.6) are authoritative |
| Level I | still open | endpoint geometry remains feasible under current scalar bounds |

---

## 10. Next run

Audit equality in QS.1.10, the triangular support-deficit estimate

```math
\int d\ge M^2,
```

and in Steiner's outer-parallel bound.  Equality would require a highly specific
single-tent support deficit and parallel-body geometry.  Combine that with FSDB's
near-extreme diameter-direction gap concentration.  If those equality geometries are
incompatible, QX's endpoint is excluded and the floor rises again without changing
the scalar framework.
