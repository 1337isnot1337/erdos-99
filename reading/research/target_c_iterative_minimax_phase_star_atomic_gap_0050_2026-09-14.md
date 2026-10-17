> Generated reading edition · [exact source](../../research/target_c_iterative_minimax_phase_star_atomic_gap_0050_2026-09-14.md) · source SHA-256 `55114bc38cc15a8b531eec230a477f81012065c3478e0e1047ee7b46887857d2`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Erdos Problem #99 - iterative-pruning minimax phase-star gap `0.0050`

**Date:** 2026-09-14  
**Target:** Target C-II, canonical full-core Type-II branch  
**Repository branch:** `research/c2-gluing-sol-20260914-r10`  
**Claim class:** proof-only strengthening of the matched all-train/rhombic atomic gap  
**LEVEL I STATUS:** `STILL OPEN`

The hostile-audited minimax phase-star theorem used the effective one-pair bound

```math
 C+L-6\sqrt m\le {2\over\sqrt3}
```

for a center phase family of normalized mass `C`, a leaf phase family of mass `L`,
and normalized missing-pair mass `m`.  The iterative-pruning theorem on this branch
implies a stronger unconditional pair bound.  Substituting it into the same weighted
two-leaf minimax gives

```math
\boxed{g=0.0050.}
\tag{IM50.1}
```

Consequently, at the same proof-only train-measure scope,

```math
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.0050,
\qquad \Delta_2={\pi\over2\sqrt3},
}
\tag{IM50.2}
```

and, by running the same argument on the strict-rhombus train graph,

```math
\boxed{
\liminf {T_R\over D}\ge2\sqrt{\Delta_2}+0.0050,
\qquad
\liminf {\sigma_R\over D}\ge0.0100.
}
\tag{IM50.3}
```

The non-load-bearing scalar ceiling of this minimax architecture is about
`0.00505782508`; `0.0050` retains a large exact margin.

---

## 1. Unconditional iterative-pruning pair corollary

Put

```math
K={2\over\sqrt3}.
```

For two stopped-train atom families of normalized masses `a,b<=K`, with limiting
projective axes separated by `pi/3`, let `rho` denote their normalized missing-pair
mass.  Commit `a85427bc` proves, with

```math
e=(a+b-K)_+,
\qquad m_*=\min\{a,b\},
```

that

```math
\rho\ge
\min\left\{{e^2\over10},{2m_*^2\over29}\right\}.
\tag{IM50.4}
```

Since `max(a,b)<=K`, every positive excess satisfies

```math
e=a+b-K\le m_*.
\tag{IM50.5}
```

Both entries of the minimum in (IM50.4) are therefore at least `2e^2/29` because
`1/10>2/29`.  Thus every such pair obeys

```math
\boxed{
\rho\ge {2\over29}(a+b-K)_+^2.
}
\tag{IM50.6}
```

Equivalently, if

```math
\lambda:=\sqrt{29/2}=3.8078865529\ldots,
```

then

```math
\boxed{
a+b-\lambda\sqrt\rho\le K.}
\tag{IM50.7}
```

This corollary has no lower-size hypothesis.  The common-neighbor and opposite-corner
work is already internal to the iterative-pruning theorem; it is not re-assumed below.

---

## 2. Dominant orbit and exact deficit control

Along a Type-II train-measure subsequence let

```math
x=\lim T/D,
\qquad A=x\sigma,
```

where `sigma` is total atomic projective-direction mass.  For each exact projective
`pi/3` orbit let `M_r` be its absolute mass and `E_r` its limiting strict-rhombus
crossing mass.  The audited train-measure stack gives

```math
E_r\le {M_r^2\over4},
\qquad \sum_rE_r=\Delta_2,
\qquad \sum_rM_r=A.
\tag{IM50.8}
```

Assume for contradiction

```math
A\le\bar A:=2s+g,
\qquad s:=\sqrt{\Delta_2},
\qquad g:=0.0050.
\tag{IM50.9}
```

If `W=max_r M_r`, then

```math
\boxed{W\ge W_0:={4s^2\over\bar A}.}
\tag{IM50.10}
```

For the dominant orbit write

```math
\delta={W^2\over4}-E.
```

If `R=A-W`, then

```math
{A^2\over4}-s^2-\delta
={A^2-W^2\over4}-\sum_{r\ne r_*}E_r
\ge {R(2W+R)-R^2\over4}
={RW\over2}\ge0.
```

Hence

```math
\boxed{
\delta\le {A^2\over4}-s^2
\le d_0:=sg+{g^2\over4}.
}
\tag{IM50.11}
```

---

## 3. Three phase classes and the weighted two-leaf deficit

Freeze shrinking continuity windows around the at most three atoms of the dominant
orbit and pass sufficiently far along the finite source sequence.  Suppressing `o(1)`
terms, write the populations as

```math
C\ge U\ge V\ge0,
\qquad C+U+V=W.
\tag{IM50.12}
```

Same-window train pairs do not cross and the physical train-crossing graph is
triangle-free.  Therefore

```math
E\le C(U+V)=C(W-C),
```

so

```math
\left(C-{W\over2}\right)^2\le\delta.
\tag{IM50.13}
```

Put `z=C-W/2`.  Define the two center-leaf missing masses

```math
x_m=CU-e(C,U),
\qquad y_m=CV-e(C,V),
```

and let `e_{UV}=e(U,V)`.  Set

```math
h=C(U+V)-E=x_m+y_m-e_{UV}.
\tag{IM50.14}
```

For every actual `UV` crossing, triangle-freeness makes the two endpoint
neighborhoods in the center class disjoint.  Summing the center-degree deficits gives

```math
C e_{UV}\le Vx_m+Uy_m.
```

With

```math
a=1-{V\over C},
\qquad b=1-{U\over C},
```

this is

```math
\boxed{a x_m+b y_m\le h.}
\tag{IM50.15}
```

Also

```math
0\le h=\delta-z^2\le d_0-z^2.
\tag{IM50.16}
```

This is the same weighted two-leaf correlation that passed the hostile audit of the
`0.0021` minimax theorem.

---

## 4. Insert the stronger physical pair theorem

Define

```math
F_U=C+U-\lambda\sqrt{x_m},
\qquad
F_V=C+V-\lambda\sqrt{y_m},
\tag{IM50.17}
```

where `lambda=sqrt(29/2)`.  The exact certificate below verifies that every possible
center population in the contradiction domain satisfies `C<K`.  Since `U,V<=C`, all
three phase families also lie below `K`.  The unconditional pair theorem (IM50.7)
therefore forces

```math
F_U\le K,
\qquad F_V\le K.
\tag{IM50.18}
```

On the other hand, a maximum dominates every positive weighted average, and Cauchy
plus (IM50.15) gives

```math
a\sqrt{x_m}+b\sqrt{y_m}
\le\sqrt{(a+b)h}.
\tag{IM50.19}
```

Let `L=U+V=W-C`.  Direct algebra gives

```math
{aU+bV\over a+b}
={CL-2UV\over2C-L}
\ge {CL-L^2/2\over2C-L}
={L\over2},
\tag{IM50.20}
```

where `UV<=L^2/4`.  Since `a+b=(3C-W)/C`, equations (IM50.17)--(IM50.20) imply

```math
\boxed{
\max(F_U,F_V)
\ge {W+C\over2}
-\lambda\sqrt{h\,{C\over3C-W}}.
}
\tag{IM50.21}
```

Substitute `C=W/2+z` and use (IM50.16):

```math
\max(F_U,F_V)
\ge
{3W\over4}+{z\over2}
-\lambda\sqrt{(d_0-z^2){W+2z\over W+6z}}.
\tag{IM50.22}
```

For `z<0`, the ratio `(W+2z)/(W+6z)` decreases in both `W` and `z`; for `z>=0` it is
at most one.  The raw term is increasing in `W` and `z`.  These are exactly the safe
monotonicity directions used by the previous hostile-audited interval proof.

---

## 5. Exact certificate at `g=0.0050`

The outward rational verifier

`research/verify_target_c_iterative_minimax_atomic_gap_0050.py`

covers the enlarged interval

```math
-0.075\le z\le0.075
```

by 15,000 rational subintervals.  This contains the entire actual domain because
`0.075^2>d_0`.  It derives outward brackets for `s`, `sqrt(29/2)`, and `2/sqrt(3)` and
checks all denominator signs.

It certifies

```math
W_0>1.8996387052,
\qquad
d_0<0.0047678141,
```

and

```math
0.87481935<C<1.02981281<K.
\tag{IM50.23}
```

The worst interval is

```math
[-0.01387,-0.01386],
```

where the outward lower bound still gives

```math
\boxed{
\max(F_U,F_V)
>1.1563091097
>{2\over\sqrt3}+0.00160857.
}
\tag{IM50.24}
```

This contradicts (IM50.18), proving (IM50.2).

A non-load-bearing one-dimensional solve places the scalar ceiling near

```math
\boxed{g_*=0.00505782508\ldots .}
\tag{IM50.25}
```

Further decimal tuning is therefore low-value.

---

## 6. Rhombic-only transfer

The hostile audit of the earlier minimax theorem separately checked that the same
argument can be run on the strict-rhombus crossing graph itself.  It is not obtained by
selecting from the all-train graph and then deleting singleton trains.  The inherited
facts are:

- vertices are non-singleton complete rhombic trains;
- the graph is simple and triangle-free;
- its edge count is exactly `R_4`;
- limiting crossings are supported at projective separation `pi/3`; and
- the same finite train-order/opposite-corner geometry applies to any selected
  center-leaf pair.

The new ingredient (IM50.6) is itself a physical two-family train theorem and applies
unchanged to the rhombic-only families.  Repeating Sections 2--5 on that graph proves

```math
\boxed{
\liminf {T_R\over D}\ge2s+0.0050.
}
\tag{IM50.26}
```

The standard rhombic transfer then yields

```math
\boxed{
\liminf {\sigma_R\over D}\ge0.0100.
}
\tag{IM50.27}
```

This matched rhombic floor is the main operational gain over the all-train-only
six-pair theorem.

---

## 7. Frontier effect

At proof-only scope the strongest matched floors on this branch are now

```text
(T-q/2)/D >= 2 sqrt(Delta_2) + 0.0050 - o(1)
T_R/D       >= 2 sqrt(Delta_2) + 0.0050 - o(1)
sigma_R/D   >= 0.0100 - o(1)
```

The older hostile-audited minimax value `0.002123` is quantitatively superseded here.
The next useful work is to propagate the matched gain through Section 171, flat-center
unloading, inactive near-contact activation, weak-contact stress, and the low-`t`
network ledgers.  Those routes genuinely use the rhombic-only gain; further tuning of
(IM50.25) does not.

---

## 8. Scope audit

- The new pair input is the iterative-pruning theorem committed at `a85427bc`.
- The unconditional corollary (IM50.6) is proved algebraically from that theorem and
  uses only `a,b<=2/sqrt(3)`.
- The weighted two-leaf triangle-free correlation is rederived above.
- The exact verifier rounds every load-bearing radical outward.
- No post-selection common-neighbor claim is added: it is already internal to the
  physical pair theorem used to derive (IM50.6).
- The rhombic-only transfer uses the same proof-only graph facts independently checked
  by the committed hostile audit of the minimax route.
- Contact-isolated source points remain in the full source.
- No exact unit equilateral triangle or strict same-cardinality sub-`D` competitor is
  claimed.

**Disposition:** proof-only matched atomic strengthening. C-II and Level I remain open.
