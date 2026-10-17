> Generated reading edition · [exact source](../../research/target_c_section112_aggregate_projection_gap.md) · source SHA-256 `52b64f2efe76917b122eac2b308b77626a30de3b2d5a0d60f3903a6f136e64ba`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 5 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C — Section 112: aggregate both phase families before pigeonholing

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only stacked research candidate; depends on Sections 110--111.

Sections 104--111 project one phase family at a time onto one principal corridor.  They
first pigeonhole the family's principal-corridor endpoints among three corridors, which
loses a factor three in the usable endpoint mass.

That loss is unnecessary.  The three principal route excesses share one global budget,
and the two selected phase families use disjoint physical terminal-edge occurrences.
Therefore the projection losses of **all** principal-corridor endpoints from both
families can be summed before choosing any corridor.

This closes the entire current Section-107 stability window

```math
\boxed{\sigma(\theta)\le10^{-3}}
```

and gives the explicit carrier coefficient

```math
\boxed{0.9760638978066385\ldots .}
```

No theorem-state mutation is proposed here.

---

## 112.1 Inputs on the full Section-107 window

Let

```math
\sigma(\theta)
=3\theta-2\pi-\sin(\theta/2)-2\sin\theta.
```

Let `theta_8` and `mu_8` be the canonical Section-101 endpoint.  Let `theta_16` solve

```math
\boxed{\sigma(\theta_{16})=10^{-3}.}
\tag{112.1}
```

The regression certificate gives

```math
\boxed{
\theta_{16}=2.7031207076068693\ldots,
\qquad
\mu_{16}:=\sin(\theta_{16}/2)
=0.9760638978066385\ldots .
}
\tag{112.2}
```

Assume for contradiction that a full-core Type-II countersequence has every
positive-area macroscopic harmonic-cell limit of normalized diameter at most `mu_16`.
Canonical Section 103 gives the unique wrapping carrier, while canonical Section 101
gives

```math
0\le\sigma:=\sigma(\theta)\le10^{-3}.
\tag{112.3}
```

Proof-only Section 107 applies on exactly this full window.  Proof-only Section 110's
exact local train bound remains below `1.83D`, since at the upper endpoint

```math
U(\theta_{16})+2\sigma
=1.8281768156\ldots<1.83.
\tag{112.4}
```

Proof-only Section 111 therefore supplies two distinct-label inverse-phase families
`A_D,B_D`, each with at least

```math
0.08D
```

full train segments and hence at least

```math
\boxed{E_0D,\qquad E_0=0.16}
\tag{112.5}
```

physical boundary-end occurrences.  Their limiting projective terminal-edge
directions `u_A,u_B` satisfy

```math
\boxed{
\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
}
\tag{112.6}
```

## 112.2 Principal endpoint mass without corridor pigeonholing

The Section-104 technical leakage theorem is scale-free once the Section-107 gap
stability estimates hold.  For a base cutoff `h>0`, each selected phase family can
place at most

```math
L(\sigma,h)D+o(D)
```

endpoints away from the three principal corridors, where

```math
L(\sigma,h)
=w(h)+\left({1\over h}+{169\over6}\right)\sigma,
\tag{112.7}
```

```math
w(h)={\pi\over3}-\arccos((1+h)/2).
\tag{112.8}
```

Take

```math
\boxed{h:=0.0413.}
\tag{112.9}
```

At the worst slack `sigma=10^-3`,

```math
\boxed{
L=0.0763930692197\ldots .
}
\tag{112.10}
```

Thus each family has total principal-corridor endpoint density at least

```math
\boxed{
P:=E_0-L
=0.0836069307803\ldots .
}
\tag{112.11}
```

No division by three is made.

For `F in {A,B}` and principal corridor `i in {1,2,3}`, let `p_{F,i}` be the limiting
normalized number of selected terminal-edge occurrences from family `F` on corridor
`i`, after passage to a subsequence.  Then

```math
\sum_i p_{F,i}\ge P.
\tag{112.12}
```

## 112.3 Sum the projection losses of both families

Let the three principal projective chord directions be `q_1,q_2,q_3`.  Define

```math
d_{F,i}:=\operatorname{dist}_{RP^1}(u_F,q_i),
\qquad
\psi(x):=1-\cos x.
```

Orient each principal outer route along its chord.  A selected terminal edge from
family `F` on corridor `i` contributes projection loss at least `psi(d_{F,i})`.
The phase labels are distinct, so the selected terminal edges from `A_D` and `B_D` are
disjoint physical edge occurrences.  Hence their losses may be summed.

The exact full-complement route ledger used in Sections 105--111 gives total normalized
path excess of the three principal corridors at most `sigma`.  Therefore

```math
\boxed{
\sigma
\ge
\sum_{F\in\{A,B\}}\sum_{i=1}^3
p_{F,i}\,\psi(d_{F,i}).
}
\tag{112.13}
```

For each family choose an index `i_F` minimizing `d_{F,i}`.  Since `psi` is increasing
on `[0,pi/2]`, (112.12)--(112.13) imply

```math
\boxed{
\sigma
\ge
P\bigl[\psi(x)+\psi(y)\bigr],
}
\tag{112.14}
```

where

```math
x:=d_{A,i_A},
\qquad
y:=d_{B,i_B}.
```

## 112.4 A two-family metric lower bound

Let

```math
m(\sigma)
:={\theta_8\over2}-{\pi\over3}-{73\over6}\sigma.
\tag{112.15}
```

Section 107's gap stability gives, for distinct principal corridors,

```math
\left|
\operatorname{dist}_{RP^1}(q_i,q_j)-{\pi\over3}
\right|>m(\sigma).
\tag{112.16}
```

There are two cases.

### Case 1: `i_A=i_B`

Both families choose the same nearest corridor.  By the triangle inequality in
`RP^1`,

```math
x+y\ge\operatorname{dist}_{RP^1}(u_A,u_B)=\pi/3.
```

The function `psi(x)=1-cos x` is increasing and convex on `[0,pi/2]`.  Hence

```math
\psi(x)+\psi(y)
\ge2\psi(\pi/6)
=2-\sqrt3.
\tag{112.17}
```

### Case 2: `i_A!=i_B`

The distance function in any metric space is 1-Lipschitz in both endpoints, so

```math
\left|
\operatorname{dist}_{RP^1}(q_{i_A},q_{i_B})
-\operatorname{dist}_{RP^1}(u_A,u_B)
\right|
\le x+y.
```

Equations (112.6) and (112.16) give

```math
x+y>m(\sigma).
```

Convexity of `psi` therefore yields

```math
\psi(x)+\psi(y)
\ge2\psi(m(\sigma)/2)
=2\left(1-\cos{m(\sigma)\over2}\right).
\tag{112.18}
```

On the present window the right side of (112.18) is much smaller than
`2-sqrt3`, so both cases imply

```math
\boxed{
\psi(x)+\psi(y)
\ge
2\left(1-\cos{m(\sigma)\over2}\right).
}
\tag{112.19}
```

Combining with (112.14), every surviving wrapping carrier must satisfy

```math
\boxed{
\sigma
\ge
2P\left(1-\cos{m(\sigma)\over2}\right).
}
\tag{112.20}
```

## 112.5 Contradiction at the full `10^-3` endpoint

At `sigma=10^-3`,

```math
m=0.2920897969609\ldots,
\tag{112.21}
```

and

```math
2\left(1-\cos(m/2)\right)
=0.0212912283959\ldots .
\tag{112.22}
```

With `P` from (112.11), the forced selected-edge projection loss is

```math
\boxed{
P\cdot2(1-\cos(m/2))
=0.00178009425872\ldots .
}
\tag{112.23}
```

This is strictly larger than the entire available normalized route excess

```math
\sigma=0.001.
```

Moreover the contradiction is monotone on the present window: decreasing `sigma`
reduces the leakage `L`, increases `P`, and increases the corridor mismatch `m`, while
the left side `sigma` decreases.  Therefore (112.20) fails for every

```math
0\le\sigma\le10^{-3}.
```

## 112.6 Carrier consequence and scope

No full-core Type-II countersequence can have every positive-area macroscopic harmonic
cell of normalized diameter at most `mu_16`.  The standard macroscopic-cell transfer
yields an actual locally rhombus-saturated carrier of quadratic area satisfying

```math
\boxed{
\operatorname{diam}(P_*)
\ge(0.9760638978066385\ldots-o(1))D.
}
\tag{112.24}
```

This is still a carrier theorem, not a closure of C-II or Level I.

Dependencies:

- canonical Sections 82, 89, 100, 101, 103;
- proof-only Section 107 for area and gap stability on `sigma<=10^-3`;
- proof-only Sections 110--111 for the `T_D<1.83D` train budget and `0.08D` joint shores;
- the independently audited Section-104 technical leakage theorem.

The only new ingredient is the aggregate projection inequality (112.13)--(112.20).
It uses disjoint physical terminal-edge occurrences and does not delete source points.

**Theorem state:** unchanged. Independent hostile audit is required.
