> Generated reading edition · [exact source](../../../docs/reports/target_c_renorm_lp_endpoint_exclusion_2026-09-10.md) · source SHA-256 `a11cda2250bdfbb4246899d4b8593457d0a377b61db21baad6a184e1495d3e60`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E86D5E49443B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — FSDB flat-side stability excludes the `mu_rho` endpoint

**Date:** 2026-09-10  
**Repository branch:** `research/c2-renorm-paired-pocket-20260910` after RL  
**Target:** Target C, all post-ZF survivors  

## LEVEL I STATUS

`STILL OPEN`.

RL proves

```math
\liminf\mu_D\ge\mu_\rho
=0.809273370477446\ldots,
```

where `mu_rho` is the unique root of RL.4.  This report proves that equality is
impossible.  Therefore the all-phase renormalized surplus has a uniform positive gap
above `mu_rho`.

The contradiction is geometric: RL equality occurs at the **minimum** possible
asymptotic diameter-edge density `h/D=2rho`, and simultaneously saturates the FSDB
area inequality.  FSDB equality then creates two opposite force-hull sides of length
`rho D+o(D)`.  Their two outer-pocket chains alone require more pocket degree than the
RL endpoint permits.

---

## 1. RL endpoint data

Assume for contradiction that an unbounded survivor sequence satisfies

```math
\mu_D\to\mu_\rho.
\tag{1.1}
```

RL proves that its only possible scalar endpoint is

```math
\boxed{h/D\to y_0:=2\rho.}
\tag{1.2}
```

Put

```math
X=d_P+Q.
```

The exact remainder identity from RPE is

```math
2X=\mu_DD+h-s_Z-a-c_B-2s_C.
\tag{1.3}
```

At the RL endpoint, the paired-pocket cavity upper bound and the scalar equality are
sharp.  Hence the discarded nonnegative remainder in (1.3) is sublinear:

```math
\boxed{
s_Z+a+c_B+2s_C=o(D).
}
\tag{1.4}
```

Therefore

```math
\boxed{
X/D\to x_0:=\frac{\mu_\rho+2\rho}{2}.
}
\tag{1.5}
```

Since `mu_rho<0.82<2rho`,

```math
\boxed{x_0<2\rho.}
\tag{1.6}
```

RL also identifies the diameter-component defect

```math
\frac{d_H}{D}
\to\frac{2\rho-\mu_\rho}{2}>0,
```

but that value is not needed for the contradiction below.

---

## 2. Scalar equality forces FSDB area equality

Let `C_att` be the GR/ZK attachment-cell area and

```math
G=area(F)-C_{att}.
```

At the endpoint, RL.4 is exactly

```math
\Phi(2\rho)
=
\frac\pi4\mu_\rho^2
+
\frac{x_0^2}{4\pi},
\qquad
\Phi(y)=\frac{y+\sin y}{4}.
\tag{2.1}
```

GR/ZK gives

```math
\limsup\frac{C_{att}}{D^2}
\le\frac\pi4\mu_\rho^2,
\tag{2.2}
```

while the paired-pocket theorem gives

```math
\limsup\frac G{D^2}
\le\frac{x_0^2}{4\pi}.
\tag{2.3}
```

FSDB gives

```math
\liminf\frac{area(F)}{D^2}
\ge\Phi(2\rho).
\tag{2.4}
```

Since `area(F)=C_att+G`, equations (2.1)-(2.4) force equality throughout:

```math
\boxed{
\frac{area(F)}{D^2}
\to\Phi(2\rho).
}
\tag{2.5}
```

---

## 3. Equality in the FSDB projective-gap inequality

As in RP, define

```math
P_H=D\,conv\{\pm u_e:e\in H\}.
```

The FS midpoint identity gives the two-sided Hausdorff estimate

```math
\boxed{
d_{Haus}(F-o,P_H/2)=o(D).
}
\tag{3.1}
```

Hence (2.5) implies

```math
\boxed{
\frac{area(P_H)}{D^2}
\to4\Phi(2\rho)=2\rho+\sin(2\rho).
}
\tag{3.2}
```

Order the `h` projective diameter directions and let their gaps be

```math
\gamma_1,\ldots,\gamma_h,
\qquad
\gamma_i\ge\delta_D:=2\arcsin\frac1{2D},
\qquad
\sum_i\gamma_i=\pi.
```

FSDB gives the exact area identity

```math
\frac{area(P_H)}{D^2}=\sum_i\sin\gamma_i
\tag{3.3}
```

and the concavity minimum

```math
M_D=(h-1)\sin\delta_D
+
\sin\bigl(\pi-(h-1)\delta_D\bigr).
\tag{3.4}
```

Since `h/D->2rho` and `D delta_D->1`,

```math
M_D\to2\rho+\sin(2\rho).
```

Thus (3.2)-(3.4) imply

```math
\sum_i\sin\gamma_i-M_D\to0.
\tag{3.5}
```

### Lemma RLE.1 — one macroscopic projective gap

After cyclic relabeling,

```math
\boxed{
\gamma_1\to B_0:=\pi-2\rho,
}
\tag{3.6}
```

and

```math
\boxed{
\sum_{i=2}^h(\gamma_i-\delta_D)\to0.
}
\tag{3.7}
```

#### Proof

Write `e_i=gamma_i-delta_D>=0`.  If two excesses stay at least `epsilon>0`, merging
them into one gap and resetting the other to `delta_D` decreases the sine sum by

```math
4\sin(e_i/2)\sin(e_j/2)
\sin\left(\delta_D+\frac{e_i+e_j}{2}\right),
```

which has a fixed positive lower bound.  This contradicts (3.5).  Hence all excesses
except the largest are `o(1)` individually.

Let `r_D` be the sum of the remaining excesses.  Because their maximum tends to zero,
`sum_{i>=2}(gamma_i-sin gamma_i)->0`.  If `r_D->r`, the excess over the minimum tends to

```math
r+\sin(B_0-r)-\sin B_0.
```

This function is zero only at `r=0`, because its derivative is
`1-cos(B_0-r)>=0` and is positive after integration over every nontrivial interval.
Thus `r=0`, proving (3.6)-(3.7). `square`

---

## 4. Two opposite `rho D` force-hull sides

The vertices of `P_H/2` lie on the radius-`D/2` circle.  A projective gap of angular
size `B_0+o(1)` gives an ordinary polygon side of length

```math
D\sin(B_0/2)+o(D).
```

Since

```math
B_0/2=\frac\pi2-\rho,
```

and `rho=cos rho`,

```math
\sin(B_0/2)=\cos\rho=\rho.
```

Therefore `P_H/2` has two antipodal sides of length

```math
\boxed{\rho D+o(D).}
\tag{4.1}
```

The radial flat-side transfer used in RP applies: (3.1) plus the FS uniform radial
annulus `|b-o|=D/2+o(D)` prevents force-hull vertices from subdividing a fixed angular
portion of either limiting flat.  Hence `F` itself has two distinct opposite sides
with

```math
\boxed{s_1/D,s_2/D\to\rho.}
\tag{4.2}
```

Since these side lengths are linear in `D`, they exceed one for all sufficiently large
sources.  They are therefore missing force-hull contact sides and determine two
distinct OP outer pockets.

---

## 5. Their two pocket chains exceed the total RL budget

Let the two corresponding old contact-chain lengths be `ell_1,ell_2`.  The triangle
inequality gives

```math
ell_j\ge s_j.
```

Each pocket contributes `ell_j-2` to `d_P`.  Hence

```math
\begin{aligned}
d_P
&\ge(\ell_1-2)+(\ell_2-2)\\
&\ge s_1+s_2-4\\
&=(2\rho+o(1))D.
\end{aligned}
```

Thus

```math
\boxed{
\liminf\frac{d_P}{D}\ge2\rho.
}
\tag{5.1}
```

But `Q>=0`, so (1.5) gives

```math
\limsup\frac{d_P}{D}
\le
\lim\frac{d_P+Q}{D}
=x_0
<2\rho,
\tag{5.2}
```

contradicting (5.1).

Therefore no RL endpoint sequence exists.

### Theorem RLE.2 — endpoint exclusion

There is no unbounded post-ZF survivor sequence satisfying

```math
\mu_D\to\mu_\rho.
\tag{RLE.1}
```

### Corollary RLE.3 — uniform gap above `mu_rho`

There exist absolute constants `epsilon_rho>0` and `D_0<infinity` such that every
post-ZF survivor with `D>=D_0` satisfies

```math
\boxed{
\mu_D\ge\mu_\rho+\epsilon_\rho.
}
\tag{RLE.2}
```

The standard sequential proof applies: otherwise choose survivors with `D_j->infinity`
and `mu_{D_j}<mu_rho+1/j`; RL supplies the lower limit and RLE.2 rules out equality.

---

## 6. Exact new frontier

The all-phase chain on this branch is now

```math
0.5947
\quad\longrightarrow\quad
0.7811638\ldots
\quad\longrightarrow\quad
0.8092733\ldots
```

with the first two scalar endpoints and now the `mu_rho` endpoint structurally
excluded.

Thus the strongest statement is not merely the explicit number:

```math
\boxed{
\mu_D\ge0.809273370477446\ldots+\epsilon_\rho
}
```

for some absolute nonexplicit `epsilon_rho>0` and all sufficiently large post-ZF
survivors.

## 7. Next target

Quantify the one-gap/two-flat-side contradiction away from exact equality.  The endpoint
margin is macroscopic:

```math
2\rho-x_0
=\rho-\frac{\mu_\rho}{2}
>0.33.
```

A stability theorem converting an FSDB area excess above the minimum into a lower bound
on the total length of the two largest opposite force-hull sides should turn this
fixed structural margin into a substantially larger **explicit** lower bound on
`mu_D`.

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

RL endpoint mu_D->mu_rho forces
  h/D->2rho,
  (d_P+Q)/D->x0=(2rho+mu_rho)/2<2rho,
  s_Z,a,c_B,s_C=o(D).
Scalar equality also forces
  area(F)/D^2->Phi(2rho).
FS midpoint Hausdorff equality transfers this to equality in the FSDB projective-gap
minimum.  Hence one projective gap tends to pi-2rho, all other excess gap mass tends
to zero.  It occurs antipodally, producing two P_H/2 sides and therefore two actual
F sides of length rho D+o(D).  Both are missing contact sides, so their two OP chains
give
  d_P/D>=2rho-o(1),
contradicting
  (d_P+Q)/D->(2rho+mu_rho)/2<2rho.

Therefore there is epsilon_rho>0 such that
  mu_D>=mu_rho+epsilon_rho,
  mu_rho=0.809273370477446...
for all sufficiently large survivors.

Next: quantify this two-flat-side margin to raise the explicit constant.
```
