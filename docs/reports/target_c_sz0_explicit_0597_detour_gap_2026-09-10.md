<!-- theorem-state: {"artifact_id":"ART-09E6CE31250C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — explicit `0.597` circuit-phase surplus floor from DD detour capacity

**Date:** 2026-09-10  
**Repository base:** `ff31de4783ff49173d9f4bfdf61364735ff5a590`  
**Run type:** explicit quantitative branch exclusion / rational certificate  
**Target:** Target C, C-II after ZF, `s_Z=0` circuit phase  
**Depends on:** SZ, RSJ, FSDB, DD, exceptional-face isoperimetry, ZG  
**External input:** none beyond already merged dependencies  
**Computation:** decimal exploration suggested the cutoff; the proof below uses displayed rational barriers

## LEVEL I STATUS

`STILL OPEN`.

The preceding SZ theorem proves a nonexplicit positive gap above

\[
\lambda_R=0.592140543606288\ldots
\]

for the renormalized circuit-phase currency

\[
\nu_D:=\frac{e_{BB}+2s_C-3d_H}{D}.
\]

This report makes part of that gap explicit:

\[
\boxed{
\liminf_{D\to\infty}\nu_D>\frac{597}{1000}.
}
\tag{E597.1}
\]

Equivalently, there are absolute constants `epsilon_597>0` and `D_0<infinity` such
that every sufficiently large post-ZF survivor with `s_Z=0` satisfies

\[
\boxed{
\frac{e_{BB}+2s_C-3d_H}{D}
\ge0.597+\epsilon_{597}.
}
\tag{E597.2}
\]

Hence

\[
\boxed{
\frac{e_{BB}+2s_C}{D}
\ge0.597+\epsilon_{597}+3\frac{d_H}{D}.
}
\tag{E597.3}
\]

The proof has a fixed area margin. Assuming `nu<=0.597`, the RSJ feasibility theorem
first traps the normalized diameter density and the exact circuit detour in

\[
\boxed{
y:=h/D<1.523,
\qquad
\delta:=2y-p<0.024,
\quad p:=P_F/D.
}
\tag{E597.4}
\]

DD and exceptional-face isoperimetry then give

\[
\frac{H_{out}+A_{exc}}{D^2}<0.33720072282+o(1),
\]

while FSDB and the retained ZK attachment radius give

\[
\frac{G}{D^2}>0.3378803714-o(1).
\]

The certified gap is

\[
\boxed{0.00067964858.}
\tag{E597.5}
\]

---

## 1. Normalized circuit variables

Assume `s_Z=0`. Suppose for contradiction that an unbounded survivor sequence has a
subsequence with

\[
\nu_D\to\nu\le u_0,
\qquad
u_0:=\frac{597}{1000}.
\tag{1.1}
\]

Pass further to subsequences so that

\[
y=\lim h/D,
\qquad
p=\lim P_F/D
\]

exist. SZ gives

\[
2\rho\le y,
\qquad y\le p\le2y,
\qquad p\le\pi.
\tag{1.2}
\]

Put

\[
\delta:=2y-p\ge0.
\tag{1.3}
\]

Because `p<=2y`, the RSJ cavity-perimeter variable is

\[
m=p-y=y-\delta.
\tag{1.4}
\]

Define

\[
\Phi(y)=\frac{y+\sin y}{4},
\qquad
\Psi(p)=\frac\pi{(\pi-2)^2}\left(\frac p2-1\right)^2,
\tag{1.5}
\]

and

\[
J_u(m)=\frac\pi4u^2+\frac{(u+m)^2}{4\pi}.
\tag{1.6}
\]

The SZ/RSJ necessary inequality is

\[
\boxed{
\max\{\Phi(y),\Psi(2y-\delta)\}
\le J_\nu(y-\delta).
}
\tag{1.7}
\]

For nonnegative `u,m`, `J_u(m)` is strictly increasing in both variables. Hence

\[
\boxed{
\max\{\Phi(y),\Psi(2y-\delta)\}
\le J_{u_0}(y-\delta).
}
\tag{1.8}
\]

---

## 2. Rational constants

We use

\[
\boxed{
\frac{6283}{2000}<\pi<\frac{3927}{1250}<\frac{22}{7}.
}
\tag{2.1}
\]

Thus

\[
\frac\pi4<\frac{3927}{5000},
\qquad
\frac1{4\pi}<\frac{500}{6283}.
\tag{2.2}
\]

The audited FSDB/MFS certificate gives

\[
\frac{739}{1000}<\rho<\frac{37}{50},
\qquad
\sin\rho>\frac{84}{125}.
\tag{2.3}
\]

Since `rho=cos rho`,

\[
A_{FS}:=\Phi(2\rho)
=\frac{\rho(1+\sin\rho)}2
>
\boxed{\frac{154451}{250000}}
=0.617804.
\tag{2.4}
\]

---

## 3. RSJ forces `y<1.523`

RSJ proves that for `y>=y_R`, where `y_R` is the unique FSDB/RS crossover, the best
perimeter is

\[
p_e(y)=2+2\sqrt{\frac{\Phi(y)}{c_R}},
\qquad
c_R=\frac\pi{(\pi-2)^2},
\tag{3.1}
\]

and the corresponding threshold `r_+(y)` is strictly increasing.

Set

\[
y_0:=\frac{1523}{1000}.
\tag{3.2}
\]

Write `y_0=pi/2-z`. From `pi<22/7`,

\[
0<z<\frac{11}{7}-\frac{1523}{1000}
=\frac{339}{7000}.
\]

Since `cos z>=1-z^2/2`,

\[
\sin y_0>\frac{4993}{5000}.
\tag{3.3}
\]

Therefore

\[
\boxed{\Phi(y_0)>\frac{6304}{10000}=0.6304.}
\tag{3.4}
\]

We next bound the optimal perimeter at `y_0`. Since

\[
\Phi(y_0)<\frac{y_0+1}{4}=\frac{2523}{4000}
\]

and `c_R>77/32`,

\[
\frac{\Phi(y_0)}{c_R}
<\frac{2523}{4000}\frac{32}{77}
<\left(\frac{64}{125}\right)^2.
\]

Hence

\[
p_e(y_0)<2+2\frac{64}{125}=3.024.
\tag{3.5}
\]

But

\[
2y_0=3.046,
\]

so

\[
p_e(y_0)<2y_0.
\tag{3.6}
\]

The crossover is exactly characterized by `p_e(y_R)=2y_R`, and RSJ proves the
crossing is unique. Thus (3.6) gives

\[
\boxed{y_0>y_R.}
\tag{3.7}
\]

Also

\[
m_e(y_0):=p_e(y_0)-y_0<1.501.
\tag{3.8}
\]

Use monotonicity of `J_{u_0}` in `m` and (2.2):

\[
\begin{aligned}
J_{u_0}(m_e(y_0))
&<J_{u_0}(1.501)\\
&<
\frac{3927}{5000}\left(\frac{597}{1000}\right)^2
+
\frac{500}{6283}\left(\frac{2098}{1000}\right)^2\\
&<0.630203.
\end{aligned}
\tag{3.9}
\]

By (3.4),

\[
J_{u_0}(m_e(y_0))<\Phi(y_0).
\tag{3.10}
\]

Thus even the optimal perimeter at `y_0` requires `nu>u_0`. Since `r_+` is strictly
increasing for `y>=y_R` and `y_0>y_R`, no feasible state with `nu<=u_0` can have
`y>=y_0`. Therefore

\[
\boxed{y<1.523.}
\tag{3.11}
\]

We also need a lower bound on `p_e(y_0)`. Since `pi>6283/2000` and
`x/(x-2)^2` decreases for `x>2`, direct rational comparison gives

\[
c_R<2.411.
\tag{3.12}
\]

Together with (3.4),

\[
\frac{\Phi(y_0)}{c_R}
>\frac{0.6304}{2.411}>(0.511)^2.
\]

Hence

\[
p_e(y_0)>2+2(0.511)=3.022,
\]

and therefore

\[
\boxed{
0<2y_0-p_e(y_0)<3.046-3.022=0.024.
}
\tag{3.13}
\]

---

## 4. RSJ forces `delta<0.024`

Assume instead

\[
\delta\ge\delta_0:=\frac{24}{1000}.
\tag{4.1}
\]

If `y<=y_R`, then `p_e(y)>=2y`, so

\[
p=2y-\delta<p_e(y).
\]

If `y_R<=y<y_0`, RSJ gives `p_e'(y)<1`, so

\[
\delta_e(y):=2y-p_e(y)
\]

is strictly increasing. By (3.13),

\[
\delta_e(y)<\delta_e(y_0)<0.024\le\delta,
\]

again giving `p=2y-\delta<p_e(y)`.

Thus throughout the possible range (3.11),

\[
p<p_e(y),
\]

so by definition of the crossover perimeter,

\[
\Psi(p)<\Phi(y).
\tag{4.2}
\]

The necessary inequality (1.8) reduces to

\[
\Phi(y)
\le J_{u_0}(y-\delta)
\le J_{u_0}(y-0.024).
\tag{4.3}
\]

Define

\[
F(y):=J_{u_0}(y-0.024)-\Phi(y).
\tag{4.4}
\]

On `[2rho,y_0]`, `F` is strictly increasing because

\[
F'(y)
=\frac{u_0+y-0.024}{2\pi}-\frac{1+\cos y}{4}.
\tag{4.5}
\]

Using `rho>0.739` and `pi<22/7`,

\[
\frac{u_0+y-0.024}{2\pi}
>
\frac{2.051}{44/7}
>0.326.
\tag{4.6}
\]

Also `y>1.478` and `y<1.523<pi/2`, hence

\[
0<\cos y
=\sin(\pi/2-y)
<\frac{11}{7}-1.478
<0.1,
\]

so

\[
\frac{1+\cos y}{4}<0.275.
\tag{4.7}
\]

Thus `F'(y)>0.051`.

At `y=y_0`, the argument is `1.499`, and (2.2) gives

\[
\begin{aligned}
J_{u_0}(1.499)
&<
\frac{3927}{5000}\left(\frac{597}{1000}\right)^2
+
\frac{500}{6283}\left(\frac{2096}{1000}\right)^2\\
&<0.629535.
\end{aligned}
\tag{4.8}
\]

By (3.4), `Phi(y_0)>0.6304`, so

\[
F(y_0)<-0.000865.
\tag{4.9}
\]

Since `F` is increasing, `F(y)<0` throughout the allowed interval, contradicting
(4.3). Therefore

\[
\boxed{\delta<0.024.}
\tag{4.10}
\]

---

## 5. DD gives an absolute cavity-capacity ceiling

Return to the finite sequence. Put

\[
\delta_D:=\frac{2h-P_F}{D},
\qquad
\xi_D:=\frac QD.
\tag{5.1}
\]

After passage to the selected subsequence,

\[
\delta_D\to\delta<0.024.
\]

Because `s_Z=0`,

\[
\frac{b-P_F}{D}
=\delta_D-\xi_D\ge0.
\tag{5.2}
\]

Thus

\[
0\le\xi_D<0.024+o(1).
\tag{5.3}
\]

Also

\[
x_B=2h-q-Q=h-d_H-Q.
\]

Since `a<=x_B` and `y<1.523`,

\[
\frac{x_B+a}{D}
\le2\frac{x_B}{D}
\le2\frac hD
<3.046+o(1).
\tag{5.4}
\]

DD gives

\[
H_{out}
\le
\frac1{\sqrt6}(x_B+a)^{3/2}\sqrt{b-P_F}.
\tag{5.5}
\]

Use

\[
\frac1{\sqrt6}<\frac{409}{1000},
\qquad
\sqrt{3.046}<1.746,
\qquad
\sqrt{0.024}<0.155.
\tag{5.6}
\]

These follow by direct squaring. Hence

\[
\limsup\frac{H_{out}}{D^2}
<
\frac{409}{1000}
\frac{3046}{1000}
\frac{1746}{1000}
\frac{155}{1000}
=0.33715464282.
\tag{5.7}
\]

The exceptional-face estimate is

\[
A_{exc}\le\frac{Q^2+O(D)}{4\pi}.
\]

Since `xi_D<0.024+o(1)` and `1/(4pi)<2/25`,

\[
\limsup\frac{A_{exc}}{D^2}
<
\frac2{25}(0.024)^2
=0.00004608.
\tag{5.8}
\]

Therefore

\[
\boxed{
\limsup\frac{H_{out}+A_{exc}}{D^2}
<0.33720072282.
}
\tag{5.9}
\]

ZG gives `G<=H_out+A_exc+O(D)`, so

\[
\boxed{
\limsup\frac G{D^2}<0.33720072282.
}
\tag{5.10}
\]

---

## 6. FSDB and ZK force a larger cavity

FSDB gives

\[
\liminf\frac{\operatorname{area}F}{D^2}
\ge A_{FS}
>
\frac{154451}{250000}
=0.617804.
\tag{6.1}
\]

SZ/ZK gives

\[
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
\le\frac\pi4\nu^2.
\]

Under `nu<=u_0` and `pi/4<3927/5000`,

\[
\limsup\frac{\sum_r\operatorname{area}(P_r)}{D^2}
<
\frac{3927}{5000}\left(\frac{597}{1000}\right)^2
=0.2799236286.
\tag{6.2}
\]

Therefore

\[
\boxed{
\liminf\frac G{D^2}
>
0.617804-0.2799236286
=0.3378803714.
}
\tag{6.3}
\]

This contradicts (5.10). The certified separation is

\[
\boxed{
0.3378803714-0.33720072282
=
\frac{33982429}{50000000000}
=0.00067964858>0.
}
\tag{6.4}
\]

Hence no unbounded survivor subsequence can have a limit `nu<=0.597`.

---

## 7. Uniform gap and consequences

If no uniform positive gap above `0.597` existed, one could choose `s_Z=0` survivors
with `D_j>=j` and

\[
\nu_{D_j}<0.597+1/j.
\]

A subsequence would converge to a limit at most `0.597`, contradicting Section 6.
Therefore E597.2 holds.

Since

\[
\frac{e_{BB}+2s_C}{D}
=\nu_D+3\frac{d_H}{D},
\]

E597.3 follows.

---

## 8. Audit notes

- No numerical optimizer is a proof dependency. The constants `1.523`, `0.024`, and
  `0.597` are rational barriers.
- The placement `y_0>y_R` is certified by `p_e(y_0)<3.024<3.046=2y_0`; no decimal
  approximation to `y_R` is needed.
- The detour bound uses the separate lower estimate `p_e(y_0)>3.022`, giving
  `2y_0-p_e(y_0)<0.024`.
- `Q` is not set to zero. It is bounded by the exact identity
  `b-P_F=D(delta_D-xi_D)>=0` and then charged through `A_exc`.
- `c_B`, `s_C`, and `d_H` are not silently set to zero; they are absorbed into the
  renormalized currency before the final relaxation.
- Contact-isolated source points remain allowed.
- No uniform area floor per outer pocket is used.

---

## 9. Remaining obstruction

This does not prove Level I. It eliminates the entire circuit-phase region

\[
\frac{e_{BB}+2s_C-3d_H}{D}\le0.597+o(1).
\]

A next useful step is structural: combine the local circuit sparsity theorem from SZ
with the near-common-circle diameter geometry to obtain an upper tradeoff on
`e_{BB}+2s_C-3d_H`, or classify the near-unicyclic diameter-thrackle regime forced when
ordinary surplus is close to the lower frontier.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In s_Z=0 define
    nu_D=(e_BB+2s_C-3d_H)/D.
Assume nu<=0.597 along an unbounded subsequence.
The SZ/RSJ inequality is
    max(Phi(y),Psi(2y-delta)) <= J_nu(y-delta),
    delta=2y-p >=0.
RSJ monotonicity plus rational checks force
    y<1.523,
    delta<0.024.
Then
    (x_B+a)/D <3.046,
    (b-P_F)/D <0.024,
    Q/D<0.024.
DD + exceptional-face isoperimetry give
    (H_out+A_exc)/D^2 <0.33720072282.
But FSDB gives
    area(F)/D^2 >154451/250000=0.617804,
and ZK with nu<=0.597 gives
    attachment area/D^2 <0.2799236286.
Hence
    G/D^2 >0.3378803714,
contradiction with fixed margin 0.00067964858.
Therefore, for some epsilon_597>0 and all sufficiently large s_Z=0 survivors,
    (e_BB+2s_C-3d_H)/D >=0.597+epsilon_597.
```
