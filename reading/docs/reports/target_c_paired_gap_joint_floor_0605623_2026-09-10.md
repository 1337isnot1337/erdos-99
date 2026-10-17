> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_gap_joint_floor_0605623_2026-09-10.md) · source SHA-256 `e0d7e7eabad4fc02c0b659857396d5e1d39511366366e40a20efab907d7835fb`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3ABD05F07685","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — paired cyclic gaps raise the post-ZF floor to 0.605623

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after PG paired-gap capacity  
**Run type:** exact asymptotic inequality synthesis / closing-proof continuation  
**Target:** Target C, C-II after ZF/DB/FS/MA/JC/DD/CC/PG  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

The paired-gap cubic-moment theorem PG upgrades the defect-aware outer-pocket capacity.
Combined with the independent MA/JC threshold, it gives

```math
\boxed{
\liminf_{D\to\infty}
\frac{e_{BB}+2s_C}{D}
\ge
\lambda_{PGJC}
=0.6056233188699899552\ldots .
}
\tag{PJ.1}
```

This is the first explicit floor in this chain above `0.60`.

The constant is defined analytically as the unique crossover of an increasing MA/JC
threshold and a decreasing paired-gap/DD threshold. No numerical optimizer is used in
the proof.

---

## 1. The paired-gap cavity function

Pass to an arbitrary convergent audited survivor subsequence and write

```math
\lambda:=\lim\frac{e_{BB}+2s_C}{D},
\qquad
y:=\lim\frac hD.
```

DB gives `y>=2rho`, where `rho=cos rho`.

Put

```math
u(y):=y-2\cos(y/2),
\qquad
\Phi(y):=\frac{y+\sin y}{4}.
\tag{1.1}
```

On `2rho<=y<pi/2`, define `theta_0(y)` by

```math
\boxed{
\theta_0-\sin\theta_0=\frac\pi2-y,
\qquad 0<\theta_0<\frac\pi2,
}
\tag{1.2}
```

and set

```math
c_0(y):=\sin\theta_0(y).
\tag{1.3}
```

PG gives

```math
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{[2y-c_0(y)]^3+c_0(y)^3}
\sqrt{u(y)}.
\tag{1.4}
```

CC gives, with `z=(Q+2s_Z)/D`,

```math
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}
\le\frac{u(y)^2}{4\pi}.
\tag{1.5}
```

Define the relaxed paired cavity capacity

```math
\boxed{
V(y):=
\frac1{\sqrt6}
\sqrt{[2y-c_0(y)]^3+c_0(y)^3}
\sqrt{u(y)}
+\frac{u(y)^2}{4\pi}.
}
\tag{1.6}
```

ZG/GU and MA then imply the necessary condition

```math
\Phi(y)-\frac\pi4\lambda^2\le V(y).
\tag{1.7}
```

Equivalently, whenever the right side below is positive,

```math
\boxed{
\lambda\ge T_P(y):=
\sqrt{\frac4\pi\,[\Phi(y)-V(y)]}.
}
\tag{1.8}
```

---

## 2. The paired-gap threshold decreases on the critical interval

Take

```math
I:=\left[2\rho,\frac{31}{20}\right].
```

The function `u` is strictly increasing. At `y=31/20`, put `x=31/40`. The alternating
Taylor bounds give

```math
1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
<\cos x
<1-\frac{x^2}{2}+\frac{x^4}{24}.
\tag{2.1}
```

The lower bound in (2.1) exceeds `57/80`, hence

```math
0\le u(y)<\frac18
\qquad(y\in I).
\tag{2.2}
```

Differentiate (1.2):

```math
(1-\cos\theta_0)\theta_0'=-1.
```

Thus

```math
\theta_0'(y)<0,
\qquad
c_0'(y)<0.
\tag{2.3}
```

Let

```math
L(y)=2y,
\qquad
M(y)=[L(y)-c_0(y)]^3+c_0(y)^3.
```

Since `c_0(y)<1<y=L/2`,

```math
\partial_L M=3(L-c_0)^2>0,
```

while

```math
\partial_c M=3[c_0^2-(L-c_0)^2]<0.
```

Together with `L'>0` and (2.3),

```math
\boxed{M'(y)>0.}
\tag{2.4}
```

Hence every factor in the first term of `V(y)` is increasing. More quantitatively,

```math
V'(y)
\ge
\frac1{\sqrt6}
\sqrt{M(y)}\frac{u'(y)}{2\sqrt{u(y)}}.
\tag{2.5}
```

Now `u'>1`. Also the elementary convex minimum

```math
(L-c)^3+c^3\ge\frac{L^3}{4}
\qquad(0\le c\le L)
```

gives

```math
\sqrt{M(y)}\ge\frac{(2y)^{3/2}}2>2
```

because `2y>14/5`. From (2.2), `2sqrt(u)<3/4`; and `1/sqrt6>2/5`.
Therefore

```math
V'(y)>
\frac25\cdot\frac2{3/4}
=\frac{16}{15}.
\tag{2.6}
```

By contrast

```math
0\le\Phi'(y)=\frac{1+\cos y}{4}\le\frac12.
```

Thus

```math
\boxed{[T_P(y)^2]'<0}
\tag{2.7}
```

wherever `T_P` is real. The paired-gap threshold is strictly decreasing on `I`.

---

## 3. The MA/JC threshold still increases

The MAJC report proves that every survivor with diameter density `y` satisfies

```math
\boxed{\lambda\ge R(y),}
\tag{3.1}
```

where `R(y)` is the positive root

```math
\boxed{
(\pi^2+1)R^2
+4\cos(y/2)R
+4\cos^2(y/2)
-\pi(y+\sin y)=0,
}
\tag{3.2}
```

and `R` is strictly increasing for `y>=2rho`.

At `y=2rho`, `u=0`, so `V=0`. The MAJC root identity gives

```math
\Phi(2\rho)-\frac\pi4R(2\rho)^2>0.
```

Hence

```math
\boxed{R(2\rho)<T_P(2\rho).}
\tag{3.3}
```

At the other end of `I`, the inequalities reverse. The MADD arithmetic audit already
proves

```math
R(3/2)>3/5.
```

Since `R` increases,

```math
R(31/20)>3/5.
\tag{3.4}
```

For `T_P`, the upper Taylor bound in (2.1) gives

```math
u(31/20)>
\frac{3703679}{30720000}
>\left(\frac{69}{200}\right)^2.
\tag{3.5}
```

Also

```math
\sqrt{M(31/20)}
\ge\frac{(31/10)^{3/2}}2
>\frac{27}{10},
\tag{3.6}
```

because `(31/10)^3> (27/5)^2`. Therefore the first term of `V` alone satisfies

```math
V(31/20)>
\frac25\cdot\frac{27}{10}\cdot\frac{69}{200}
=\frac{1863}{5000}.
\tag{3.7}
```

Since

```math
\Phi(31/20)<\frac{51}{80},
```

we obtain

```math
T_P(31/20)^2
<\frac4\pi\left(\frac{51}{80}-\frac{1863}{5000}\right)
<\frac43\cdot\frac{2649}{10000}
=\frac{883}{2500}
<\frac9{25}.
\tag{3.8}
```

Thus

```math
\boxed{T_P(31/20)<3/5<R(31/20).}
\tag{3.9}
```

---

## 4. Unique crossover and global minimum

Since `R` is strictly increasing and `T_P^2` is strictly decreasing, (3.3) and (3.9)
produce a unique

```math
\boxed{y_P\in(2\rho,31/20)}
\tag{4.1}
```

with

```math
\boxed{R(y_P)=T_P(y_P).}
\tag{4.2}
```

Every survivor with `y in I` satisfies

```math
\lambda\ge\max\{R(y),T_P(y)\},
```

whose minimum is exactly the crossover value

```math
\boxed{\lambda_{PGJC}:=R(y_P)=T_P(y_P).}
\tag{4.3}
```

For `y>=31/20`, monotonicity of `R` gives

```math
\lambda\ge R(y)>R(y_P)=\lambda_{PGJC}.
```

Hence (4.3) is the global post-ZF lower threshold. This proves PJ.1. `square`

---

## 5. Numerical evaluation

Solving (1.2), (3.2), and (4.2) gives

```math
\boxed{
y_P
=1.5088485158564479590\ldots,}
\tag{5.1}
```

```math
\boxed{
\lambda_{PGJC}
=0.6056233188699899552\ldots .
}
\tag{5.2}
```

At the crossover,

```math
\theta_0(y_P)=0.7253308831203855660\ldots,
```

```math
c_0(y_P)=0.6633830721819369058\ldots,
```

```math
u(y_P)=0.0515165719056206688\ldots .
```

The paired relaxed cavity capacity is

```math
V(y_P)=0.3386645633017670\ldots .
```

These decimals are evaluations of the analytic crossover, not proof inputs.

---

## 6. What equality would force

A sequence approaching `lambda_PGJC` must have

```math
\frac hD\to y_P.
\tag{6.1}
```

It must also simultaneously saturate the MA/JC minimization and the z-free PG
relaxations. In particular:

1. `P_F/D -> p_0(y_P)` and `e_BB/D -> lambda_PGJC`, so `s_C/D->0`;
2. the total missing projective-circle angle must approach its maximum `pi-y_P`, with
   a single gap asymptotically minimizing perimeter;
3. the PG cavity upper bound would need the smallest allowed paired outside-chain mass;
4. the z-free exceptional-face relaxation would need to coexist with the PG outer
   capacity even though its two terms favor incompatible values of `z`.

The fourth point already indicates that PJ.1 is not expected to be sharp: (1.6)
maximizes the outer-pocket term by setting `z=0` but simultaneously maximizes the
exceptional-face term by replacing `z^2` with `u(y)^2`. Those two maxima cannot occur in
the same source.

---

## 7. Regression audit

- **Regular odd shell:** `y->pi`, outside the critical paired-gap regime and far above
  the new pinned/contact floor.
- **Single giant detour pocket:** PG forces positive chain mass outside it whenever
  perimeter feasibility requires a macroscopic missing circle angle.
- **Many tiny gaps:** paired chord lower bounds only become stronger under splitting.
- **Giant exceptional face:** the relaxed `u^2/(4pi)` term explicitly allows it, so PJ
  does not gain by assuming it absent.
- **Dense isolated fillings:** still lack the global post-ZF source certificate.
- **Response trace / matching regressions:** unused.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| paired-gap one-variable cavity `V(y)` | proved | PG outer capacity + CC exceptional-face relaxation |
| `T_P` decreases on critical interval | proved | paired capacity grows faster than `Phi` |
| unique crossover | proved | monotone thresholds with certified endpoint signs |
| explicit floor `0.6056233188...` | proved asymptotically | analytic crossover |
| crossover sharpness | rejected | z-free relaxation maximizes incompatible defect terms simultaneously |
| Level I | still open | the exact joint `z` optimization and later topology remain |

---

## 9. Exact next obligation

Do **not** stop at the `0.605623` scalar. Restore the same defect variable `z` in both
terms:

```math
\mathcal U(y,z)=
\frac1{\sqrt6}
\sqrt{[2(y-z)-c(y,z)]^3+c(y,z)^3}
\sqrt{u(y)-z}
+\frac{z^2}{4\pi},
```

with `c(y,z)=sin theta(y,z)` from PG.2. The outer term strictly decreases with `z`,
while the exceptional term increases quadratically. Determine the exact maximum on
`0<=z<=u(y)` and combine it with `R(y)`. This must improve PJ.1 and gives a more rigid
equality structure for the next geometric audit.
