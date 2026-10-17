> Generated reading edition · [exact source](../../../docs/reports/target_c_central_support_area_floor_059336_2026-09-10.md) · source SHA-256 `7c0c417802ff034ed50b667101a6eb4723cfaed8abb91b65fe677a5182de2ec8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C0E447FFCF7C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — central support-function area raises the post-ZF surplus floor to 0.593361

**Date:** 2026-09-10  
**Repository base:** `a64364e1a3a79370e8c2b342a1fdd6b1f86b66e4`  
**Run type:** exact convex-geometric inequality synthesis / explicit branch narrowing  
**Target:** Target C, C-II after ZF / FS / FSDB / JC  
**External input:** none  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`.

The current FSJC theorem gives

```math
\liminf\frac{e_{BB}+2s_C}{D}
\ge 0.5882283437736394\ldots,
```

and the subsequent FS disk-rigidity report excludes equality by a qualitative gap.
This report turns part of that qualitative gap into a new explicit theorem:

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{CS}
=0.5933612807422635245\ldots .
}
\tag{CSF.1}
```

The new ingredient is a self-contained area inequality for centrally symmetric planar convex bodies:

```math
\boxed{
A\ge\frac{P^2}{2\pi}-\frac{\pi D^2}{4},
}
\tag{CSF.2}
```

where `A,P,D` are area, perimeter, and diameter. Equality occurs only for a disk.

FS.4 and the current central-symmetral report provide, for each force hull `F`, a centrally symmetric body

```math
S=\frac12((F-o)-(F-o))
```

with exactly the same diameter and perimeter as `F`, while

```math
\operatorname{area}S-\operatorname{area}F=o(D^2).
```

Therefore CSF.2 supplies a new asymptotic force-hull area lower bound depending on its actual normalized perimeter `p=P_F/D`:

```math
\frac{\operatorname{area}F}{D^2}
\ge
\Psi(p)-o(1),
\qquad
\Psi(p):=\frac{p^2}{2\pi}-\frac\pi4.
\tag{CSF.3}
```

Combining this with FSDB's independent diameter-density floor

```math
\Phi(y)=\frac{y+\sin y}{4},
\qquad y=h/D,
```

and the unrelaxed actual-perimeter JC cavity bound produces CSF.1.

The minimizing normalized geometry is explicit. Let `rho` be the Dottie number `rho=cos rho`. There is a unique

```math
\boxed{
y_0\in(2\rho,\pi/2)}
```

satisfying

```math
\boxed{
8y_0^2-\pi y_0-\pi\sin y_0-\pi^2=0.
}
\tag{CSF.4}
```

Numerically

```math
y_0=1.4861348981098190445\ldots .
```

The minimizing force-hull perimeter is

```math
\boxed{p_0=2y_0=2.9722697962196380891\ldots,}
\tag{CSF.5}
```

where the FSDB and central-symmetry area floors meet:

```math
\Phi(y_0)=\Psi(2y_0).
```

Finally `lambda_CS` is the unique positive root of

```math
\boxed{
(\pi^2+1)\lambda^2+2y_0\lambda+\pi^2-7y_0^2=0.
}
\tag{CSF.6}
```

No numerical optimizer is used in the proof of the minimizer.

---

## 1. A self-contained centrally symmetric area inequality

### Theorem CSA

Let `K` be a centrally symmetric planar convex body with area `A`, perimeter `P`, and diameter `D`. Then

```math
\boxed{
A\ge\frac{P^2}{2\pi}-\frac{\pi D^2}{4}.
}
\tag{1.1}
```

If equality holds, `K` is a disk.

### Proof

Translate the center of symmetry to the origin. Since `K=-K` and `diam(K)=D`, every `x in K` satisfies

```math
2|x|=|x-(-x)|\le D.
```

Hence

```math
K\subseteq \overline B(0,D/2).
\tag{1.2}
```

Let `h(theta)` be the support function of `K`. Central symmetry gives `pi`-periodicity:

```math
h(\theta+\pi)=h(\theta).
\tag{1.3}
```

The support function is Lipschitz. At almost every angle its supported boundary point is

```math
x(\theta)=h(\theta)u_\theta+h'(\theta)u_\theta^\perp.
```

By (1.2),

```math
\boxed{
h(\theta)^2+h'(\theta)^2\le D^2/4}
\tag{1.4}
```

for almost every `theta`.

The standard support-function perimeter and area formulas are

```math
P=\int_0^{2\pi}h(\theta)\,d\theta
=2\int_0^\pi h(\theta)\,d\theta,
\tag{1.5}
```

and

```math
A=\frac12\int_0^{2\pi}(h^2-h'^2)\,d\theta
=\int_0^\pi(h^2-h'^2)\,d\theta.
\tag{1.6}
```

These formulas hold for arbitrary convex bodies by the usual support-function approximation; equivalently they hold in the `W^{1,2}` support-function formulation.

From (1.4),

```math
h^2-h'^2\ge2h^2-D^2/4.
```

Insert this in (1.6):

```math
A
\ge
2\int_0^\pi h^2\,d\theta
-\frac{\pi D^2}{4}.
\tag{1.7}
```

Cauchy--Schwarz and (1.5) give

```math
\int_0^\pi h^2\,d\theta
\ge
\frac1\pi\left(\int_0^\pi h\,d\theta\right)^2
=\frac{P^2}{4\pi}.
\tag{1.8}
```

Combining (1.7) and (1.8) proves (1.1).

If equality holds, equality must hold in Cauchy--Schwarz, so `h` is constant almost everywhere and hence everywhere. A convex body with constant support function is a disk centered at the origin. Its diameter is `D`, so its radius is `D/2`. `square`

### Remarks

1. The inequality is useful only in the high-perimeter regime; near the segment endpoint its right side is negative.
2. No smoothness or strict convexity is assumed.
3. The proof uses central symmetry essentially through both the radius bound `D/2` and the `pi`-periodic support formulas.

---

## 2. Transport CSA to every post-ZF force hull

Let `F` be a post-ZF force hull and let `o` be the common source circumcenter from FS. Define the central symmetral

```math
S:=\frac12((F-o)-(F-o)).
\tag{2.1}
```

The current FS disk-rigidity report proves exactly

```math
\operatorname{diam}S=D,
\qquad
\operatorname{per}S=\operatorname{per}F,
\tag{2.2}
```

and

```math
0\le\operatorname{area}S-\operatorname{area}F=o(D^2).
\tag{2.3}
```

Apply CSA to `S`. Put

```math
p:=\frac{\operatorname{per}F}{D}.
\tag{2.4}
```

Then

```math
\operatorname{area}S
\ge
D^2\left(\frac{p^2}{2\pi}-\frac\pi4\right).
```

Using (2.3),

```math
\boxed{
\frac{\operatorname{area}F}{D^2}
\ge
\Psi(p)-o(1),
\qquad
\Psi(p):=\frac{p^2}{2\pi}-\frac\pi4.
}
\tag{2.5}
```

FSDB independently gives, with

```math
y:=\frac hD,
```

```math
\boxed{
\frac{\operatorname{area}F}{D^2}
\ge
\Phi(y)-o(1),
\qquad
\Phi(y):=\frac{y+\sin y}{4}.
}
\tag{2.6}
```

Consequently every convergent post-ZF subsequence satisfies

```math
\boxed{
\liminf\frac{\operatorname{area}F}{D^2}
\ge
M(y,p):=\max\{\Phi(y),\Psi(p)\}.
}
\tag{2.7}
```

The geometric domain is

```math
\boxed{
2\rho\le y\le p\le\pi.
}
\tag{2.8}
```

Indeed DB gives `y>=2rho`; every diameter endpoint is a force-hull vertex, so `h<=q`; the `q` consecutive force-hull vertices are distinct source points and every force-hull side has length at least one, hence

```math
\operatorname{per}F\ge q\ge h;
```

and Cauchy's perimeter-diameter inequality gives `p<=pi`.

---

## 3. Insert the two area floors into the exact JC cavity budget

Pass to a subsequence on which

```math
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
t:=\lim\frac{e_{BB}}D,
\qquad
y:=\lim\frac hD,
\qquad
p:=\lim\frac{\operatorname{per}F}{D}
\tag{3.1}
```

exist. Then

```math
0\le t\le\lambda.
\tag{3.2}
```

The GU/ZK attachment-cell estimate, after only the weakening `d_H+s_Z>=0`, gives

```math
\limsup
\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\lambda^2.
\tag{3.3}
```

Thus (2.7) gives the attachment-gap lower bound

```math
\boxed{
\liminf\frac GD^2
\ge
M(y,p)-\frac\pi4\lambda^2.
}
\tag{3.4}
```

The actual-perimeter JC identity gives

```math
E_{out}+Q
\le
 e_{BB}+\min\{h,\operatorname{per}F-h\}.
```

After the standard joint convex-cavity estimate and division by `D^2`, this yields

```math
\boxed{
\limsup\frac GD^2
\le
\frac{(t+m(y,p))^2}{4\pi},
\qquad
m(y,p):=\min\{y,p-y\}.
}
\tag{3.5}
```

Using `t<=lambda`, every survivor limit must satisfy

```math
\boxed{
M(y,p)-\frac\pi4\lambda^2
\le
\frac{(\lambda+m(y,p))^2}{4\pi}.
}
\tag{3.6}
```

Equivalently,

```math
\boxed{
F(y,p,\lambda):=
(\pi^2+1)\lambda^2
+2m(y,p)\lambda
+m(y,p)^2
-4\pi M(y,p)
\ge0.
}
\tag{3.7}
```

For fixed `(y,p)`, `F` is strictly increasing in `lambda>=0`. Therefore the smallest possible survivor `lambda` is the minimum, over (2.8), of the positive threshold root of (3.7).

---

## 4. Optimize the actual force-hull perimeter exactly

For fixed `y`, define `p_y` by

```math
\boxed{
\Psi(p_y)=\Phi(y).
}
\tag{4.1}
```

Since `Psi` is strictly increasing and `Phi(y)<=pi/4`, this gives

```math
p_y
=\sqrt{2\pi\left(\Phi(y)+\frac\pi4\right)}
\le\pi.
\tag{4.2}
```

On the interval under consideration one also has `p_y>=y`. For completeness, put

```math
H(y):=4(\Phi(y)-\Psi(y))
=\pi+y+\sin y-\frac{2y^2}{\pi}.
```

One has `H(pi)=0`, while `H` is decreasing on `[2rho,pi]`; hence `H(y)>=0`. Thus (4.1) is attained in `[y,pi]`.

We now maximize `F(y,p,lambda)` over `p` for fixed `y` and fixed `lambda<1`. The threshold root is minimized exactly where this maximum occurs.

- For `p<=2y` and `Psi(p)<=Phi(y)`, one has `M=Phi(y)` and `m=p-y`; hence `F` strictly increases with `p`.
- For `p>=2y` while `Psi(p)<=Phi(y)`, one has `m=y` and `M=Phi(y)`; hence `F` is constant in `p`.
- For `p<=2y` and `Psi(p)>Phi(y)`, one has `M=Psi(p)` and `m=p-y`. Since
  ```math
  4\pi\Psi(p)=2p^2-\pi^2,
  
  ```
  differentiation gives
  ```math
  \partial_pF
  =2(\lambda+p-y)-4p
  =2(\lambda-y-p)<0,
  \tag{4.3}
  
  ```
  because every relevant threshold is `<1` while `y+p>1`. The bound threshold `<1` follows directly from `M<=pi/4`: at `lambda=1`, the left side of (3.7) is positive.
- For `p>=2y` and `Psi(p)>Phi(y)`, `m=y` is fixed while `M=Psi(p)` increases, so `F` strictly decreases.

Therefore the best perimeter for a fixed `y` is

```math
\boxed{
 p_*(y)=
 \begin{cases}
 2y,& p_y\ge2y,\\
 p_y,& p_y\le2y.
 \end{cases}
}
\tag{4.4}
```

with the obvious interpretation when `2y>pi`.

---

## 5. The unique crossover `y_0`

The condition `p_y=2y` is equivalent to

```math
\Psi(2y)=\Phi(y),
```

or

```math
\boxed{
G(y):=
8y^2-\pi y-\pi\sin y-\pi^2=0.
}
\tag{5.1}
```

At `y=2rho`, direct substitution gives `Psi(4rho)<Phi(2rho)`, so `G(2rho)<0`. At `y=pi/2`,

```math
\Psi(\pi)-\Phi(\pi/2)
=\frac{\pi-2}{8}>0,
```

so `G(pi/2)>0`.

Moreover

```math
G'(y)=16y-\pi(1+\cos y)>0
\tag{5.2}
```

throughout `[2rho,pi/2]`, since `16y>16>2pi>=pi(1+cos y)` there. Thus there is a unique root

```math
\boxed{y_0\in(2\rho,\pi/2).}
\tag{5.3}
```

For `y<=y_0`, `p_y>=2y`, so the maximizing choice in (4.4) is `p=2y`. For `y>=y_0`, it is `p=p_y`.

---

## 6. Optimize the diameter-edge density exactly

Let `lambda_CS` be the positive root in (CSF.6). At `y=y_0`, `p=2y_0`, one has

```math
m=y_0,
\qquad
M=\Phi(y_0)=\Psi(2y_0),
```

and (3.7) becomes exactly

```math
(\pi^2+1)\lambda^2+2y_0\lambda+\pi^2-7y_0^2=0.
```

Thus

```math
F(y_0,2y_0,\lambda_{CS})=0.
\tag{6.1}
```

We prove that for every admissible `(y,p)`,

```math
F(y,p,\lambda_{CS})\le0.
\tag{6.2}
```

Since `F` increases with `lambda`, (6.2) proves every threshold root is at least `lambda_CS`.

### 6.1 Left of the crossover

For `2rho<=y<=y_0`, Section 4 shows the largest value over `p` is attained at `p=2y`. Put

```math
F_1(y)
:=F(y,2y,\lambda_{CS})
=(\pi^2+1)\lambda_{CS}^2
+2y\lambda_{CS}+y^2
-\pi(y+\sin y).
\tag{6.3}
```

Then

```math
F_1'(y)
=2\lambda_{CS}+2y-\pi(1+\cos y),
\tag{6.4}
```

and

```math
F_1''(y)=2+\pi\sin y>0.
\tag{6.5}
```

The FSJC proof already establishes positivity of (6.4) at `y=2rho` for every `lambda>1/2`. The present `lambda_CS` is strictly larger than the old FSJC endpoint and hence exceeds `1/2`. Therefore `F_1` is strictly increasing on `[2rho,y_0]`.

Using (6.1),

```math
F_1(y)\le F_1(y_0)=0.
\tag{6.6}
```

### 6.2 Right of the crossover

For `y>=y_0`, Section 4 shows the maximizing perimeter is `p=p_y`. Put

```math
m_y:=p_y-y.
```

Since `Psi(p_y)=Phi(y)`,

```math
F_2(y)
:=(\pi^2+1)\lambda_{CS}^2
+2m_y\lambda_{CS}+m_y^2
-4\pi\Phi(y).
\tag{6.7}
```

Differentiate (4.2):

```math
p_y'
=\frac{\pi\Phi'(y)}{p_y}
=\frac{\pi(1+\cos y)}{4p_y}.
\tag{6.8}
```

For `y>=y_0`,

```math
p_y\ge p_{y_0}=2y_0>\pi/2,
```

so

```math
0\le p_y'<1.
\tag{6.9}
```

Therefore `m_y'=p_y'-1<0`. Since `lambda_CS+m_y>=0` and `Phi'(y)>=0`,

```math
\boxed{
F_2'(y)
=2(\lambda_{CS}+m_y)m_y'
-4\pi\Phi'(y)
<0.
}
\tag{6.10}
```

Thus `F_2` is strictly decreasing for `y>=y_0`. Again (6.1) gives

```math
F_2(y)\le F_2(y_0)=0.
\tag{6.11}
```

Sections 6.1 and 6.2 prove (6.2), and therefore CSF.1.

---

## 7. Numerical orientation

The exact defining equations are the proof objects. Their numerical values are

```math
\rho
=0.7390851332151606416553\ldots,
```

```math
y_0
=1.4861348981098190445498\ldots,
```

```math
p_0=2y_0
=2.9722697962196380890996\ldots,
```

```math
\Phi(y_0)=\Psi(p_0)
=0.6206383148558300788605\ldots,
```

and

```math
\boxed{
\lambda_{CS}
=0.5933612807422635245853\ldots .
}
```

The improvement over FSJC is

```math
0.0051329369686240858\ldots .
```

No decimal value is used in the proof.

---

## 8. Equality and the next structural target

The minimization is rigid at the scalar level. Any sequence with

```math
\frac{e_{BB}+2s_C}{D}\to\lambda_{CS}
```

must asymptotically satisfy

```math
\frac hD\to y_0,
\qquad
\frac{\operatorname{per}F}{D}\to2y_0,
\tag{8.1}
```

and both independent force-hull area lower bounds must meet:

```math
\frac{\operatorname{area}F}{D^2}
\to
\Phi(y_0)=\Psi(2y_0).
\tag{8.2}
```

But CSA has equality only for a disk, while `2y_0<pi`. Thus exact equality in the symmetric-area step is impossible for a fixed centrally symmetric limit with perimeter `2y_0`.

By compactness of the centrally symmetric diameter-one class at fixed perimeter `2y_0`, this already implies a further **qualitative** gap above `lambda_CS`. The report does not assign a numerical value to that second gap because doing so requires a quantitative strengthening of CSA.

This gives the next precise target:

> Quantify the strictness of CSA away from `P=pi D`, insert that quantitative defect into Sections 3--6, and obtain the next explicit floor. A support-function variance argument around a diameter direction is a self-contained candidate.

---

## 9. Regression audit

### Regular odd shell

Its normalized force hull tends to a disk, so it satisfies CSA near equality only as `p->pi`. The new optimizer has `p_0<pi`, so the shell is not falsely declared impossible merely from central symmetry.

### Perfect matching

Already excluded by the FSDB/MFS branch closure. The present theorem concerns the general nonmatching post-ZF phase.

### Dense isolated fillings

No force-visible population saturation is assumed. The central symmetral and FSDB area bound are properties of the same force hull transported from full-source optimality; isolated source points remain allowed.

### Noncentrally symmetric force hulls at finite `D`

CSA is not applied directly to `F`. It is applied to the exact central symmetral `S`, and the current FS.4 report proves `area(S)-area(F)=o(D^2)`. Thus no false finite central-symmetry assumption is introduced.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| CSA inequality (1.1) | proved | support-function radius bound + Cauchy--Schwarz |
| equality in CSA only for disk | proved | equality in Cauchy--Schwarz forces constant support |
| force-hull asymptotic bound `area(F)/D^2>=Psi(p)-o(1)` | proved from current FS symmetral theorem | exact `D,P` preservation plus `o(D^2)` area transfer |
| joint necessary inequality (3.7) | proved | FSDB/CSA area floors + GU + actual-perimeter JC |
| unique optimizer `(y_0,p_0)` | proved | monotone perimeter split and one crossover |
| explicit floor `lambda_CS` | proved asymptotically | exact one-variable monotonicity on both sides of `y_0` |
| endpoint `lambda_CS` attainable | rejected qualitatively | CSA equality would require disk but `p_0<pi` |
| explicit larger floor beyond `lambda_CS` | not yet proved | requires quantitative CSA stability |
| Level I | still open | high-surplus branch remains |

---

## 11. Promotion recommendation

**Hold as report pending independent audit.** CSA itself is a short self-contained convex-geometric lemma suitable for shared theory. The `0.593361...` application depends on the current report-level FSDB, FS central-symmetral area transport, GU/ZK, and actual-perimeter JC stack.

No Level I status change is warranted.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New centrally symmetric area lemma CSA:
For every centrally symmetric planar convex body with area A, perimeter P,
diameter D,
    A >= P^2/(2pi) - pi D^2/4,
with equality only for the disk.
Proof: center at 0; support h is pi-periodic and h^2+h'^2<=D^2/4 a.e.;
A=int_0^pi(h^2-h'^2), P=2int_0^pi h; apply Cauchy-Schwarz.

Current FS central symmetral S=(F-F)/2 has
    diam S=D,
    per S=per F,
    area S-area F=o(D^2).
Thus if p=per(F)/D,
    area(F)/D^2 >= Psi(p)-o(1),
    Psi(p)=p^2/(2pi)-pi/4.
FSDB independently gives Phi(y)=(y+sin y)/4, y=h/D.

GU+JC imply every limit satisfies
    M(y,p)-pi lambda^2/4 <= (lambda+min(y,p-y))^2/(4pi),
where M=max(Phi(y),Psi(p)), 2rho<=y<=p<=pi,
and lambda=(e_BB+2s_C)/D.

For fixed y, the optimal p is 2y until Psi(2y)=Phi(y), then the unique p_y
with Psi(p_y)=Phi(y). The crossover y_0 is the unique root in (2rho,pi/2) of
    8y^2-pi y-pi sin y-pi^2=0.
It equals
    y_0=1.4861348981098190445...
The global threshold is minimized there, at p_0=2y_0, and
    (pi^2+1)lambda_CS^2+2y_0 lambda_CS+pi^2-7y_0^2=0.
Hence
    liminf (e_BB+2s_C)/D >= lambda_CS
      =0.5933612807422635246...

Since CSA equality at p_0<pi is impossible, the true floor is again strictly
above lambda_CS. Next: quantify CSA strictness using the diameter-direction
support-function variance forced by max h=D/2.
```
