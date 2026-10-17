> Generated reading edition · [exact source](../../../docs/reports/target_c_db_nm_branching_constant_2026-09-09.md) · source SHA-256 `2075bd72ed96222b96abbe5c72a081e66e74b5a7e2d985ad0418d24291e2d592`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8C96E43E072E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — sharp DB+NM diameter-branching constant

**Date:** 2026-09-09  
**Repository base:** `78b922cbbbf09a63c0cfa3f1d6b786cc1fcdfa24` plus GU on this branch  
**Run type:** exact inequality coupling / asymptotic optimization  
**Target:** Target C C-II after ZF  
**Depends on:** DB difference-body perimeter theorem and NM near-matching train stability  
**External web search:** not used  
**Computation:** decimal root evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

NM proves the post-ZF diameter graph has linear degree excess above a matching:

```math
r_H:=2h-q=x_B+Q+2s_Z.
```

Its first universal constant was

```math
\liminf r_H/D\ge2\rho/3=0.4927234221\ldots .
```

That estimate uses DB only to lower-bound `h`. A stronger result follows by feeding DB's **defect-dependent** inequality back into the NM train-end count.

### Theorem NB — sharp constant from DB+NM

Every unbounded post-ZF survivor sequence satisfies

```math
\boxed{
\liminf_{D\to\infty}\frac{2h-q}{D}
\ge c_*
=0.6099043189\ldots ,
}
\tag{NB.1}
```

where `c_*` is the unique positive solution of

```math
\boxed{
c_*=\cos\left(\frac{3c_*}{2}\right).}
\tag{NB.2}
```

Equivalently, if `y_*=3c_*`, then `y_*=1.8297129568...` is the unique positive solution of

```math
\boxed{
\frac{y_*}{3}=\cos\frac{y_*}{2}.
}
\tag{NB.3}
```

This is the optimal universal constant obtainable from the current NM train-end inequality together with the current DB defect inequality: the underlying two-variable linear program attains equality at the crossover in NB.3.

---

## 1. Separate the DB-controlled defect from outer-walk excess

Write

```math
\boxed{
z:=Q+2s_Z=f+g_F+2s_Z.}
\tag{1.1}
```

Then

```math
\boxed{r_H=x_B+z.}
\tag{1.2}
```

NM proves

```math
h-2\le2x_B+3f+g_F+s_Z.
\tag{1.3}
```

For fixed `z`, the right side is at most

```math
2x_B+3z,
```

because

```math
3z-(3f+g_F+s_Z)
=2g_F+5s_Z\ge0.
```

Using `x_B=r_H-z`,

```math
\boxed{
h-2\le2r_H+z.}
\tag{1.4}
```

This retains the distinction between outer-walk excess and the face/mixed-row defect that DB directly controls.

---

## 2. DB supplies an upper bound on `z`

Put

```math
a_D:=\arcsin\frac1{2D}.
```

DB proves the exact finite inequality

```math
\boxed{
z=Q+2s_Z
\le
h+1-2D\cos((h-1)a_D).}
\tag{2.1}
```

Insert (2.1) into (1.4):

```math
h-2
\le2r_H+h+1-2D\cos((h-1)a_D).
```

Cancel `h` and rearrange:

```math
\boxed{
r_H
\ge
D\cos((h-1)a_D)-\frac32.}
\tag{2.2}
```

NM independently gives

```math
\boxed{
r_H\ge\frac{h-2}{3}.}
\tag{2.3}
```

Thus every finite survivor obeys both lower bounds.

---

## 3. Asymptotic optimization

The diameter thrackle bound and force-hull perimeter give `h=O(D)`. Pass to a subsequence on which

```math
\frac hD\to y.
```

DB already implies `y>=2rho`, but the exact lower endpoint will not be needed separately.

Since

```math
a_D=\frac1{2D}+O(D^{-3}),
```

we have

```math
(h-1)a_D\to\frac y2.
```

Divide (2.2)-(2.3) by `D` and pass to the limit. Any subsequential limit `r` of `r_H/D` satisfies

```math
\boxed{
r\ge\max\left\{\frac y3,\cos\frac y2\right\}.}
\tag{3.1}
```

On the relevant interval `0<y<pi`, the first function is strictly increasing and the second strictly decreasing. Therefore their maximum is minimized at their unique intersection

```math
\frac y3=\cos\frac y2.
\tag{3.2}
```

Let `y_*` denote that intersection. Then

```math
\inf_y\max\left\{\frac y3,\cos\frac y2\right\}
=\frac{y_*}{3}
=:c_*.
```

Substituting `y_*=3c_*` gives

```math
c_*=\cos(3c_*/2),
```

proving NB.1-NB.3.

Uniqueness is immediate because

```math
F(c)=c-\cos(3c/2)
```

has

```math
F'(c)=1+\frac32\sin(3c/2)>0
```

on the relevant positive interval, while `F(0)<0` and `F(1)>0`.

---

## 4. Why the constant is optimal for these two inequalities

The asymptotic optimization can be written as a two-currency linear program.

For fixed normalized diameter-edge count `y=h/D`, let

```math
x=x_B/D,
\qquad
f'=f/D,
\qquad
g=g_F/D,
\qquad
s=s_Z/D.
```

Ignoring vanishing `O(1/D)` terms, NM requires

```math
2x+3f'+g+s\ge y,
\tag{4.1}
```

while DB gives the capacity

```math
f'+g+2s\le u(y):=y-2\cos(y/2).
\tag{4.2}
```

The branching cost is

```math
r=x+f'+g+2s.
\tag{4.3}
```

Among the DB-controlled currencies, `f'` supplies the most NM train-end capacity per unit branching cost: coefficient three in (4.1) for unit cost and unit DB capacity. Outer excess `x` supplies coefficient two without using DB capacity. The variables `g,s` are strictly less efficient for minimizing `r`.

Hence the optimum at fixed `y` is:

- if `u(y)>=y/3`, use `f'=y/3`, `x=0`, giving `r=y/3`;
- if `u(y)<y/3`, saturate `f'=u(y)` and pay the remainder with `x`, giving
  
  ```math
  r=u(y)+\frac{y-3u(y)}2
   =\cos(y/2).
  ```


Thus the exact asymptotic optimum permitted by DB+NM is

```math
\boxed{
r_{min}(y)=\max\{y/3,\cos(y/2)\}.}
\tag{4.4}
```

Its global minimum is exactly `c_*`.

Therefore improving NB's constant requires genuinely new geometry/topology, not a better algebraic rearrangement of DB and NM.

---

## 5. Consequences for the mandatory currencies

NB gives

```math
\boxed{
x_B+Q+2s_Z\ge(c_*-o(1))D.}
\tag{5.1}
```

Hence at least one of the three nonnegative weighted currencies is linear. A crude explicit three-way split is

```math
\boxed{
 x_B\ge(c_*/3-o(1))D
}
```

or

```math
\boxed{
 Q\ge(c_*/3-o(1))D
}
```

or

```math
\boxed{
 s_Z\ge(c_*/6-o(1))D.
}
```

Numerically these thresholds are

```math
c_*/3=0.2033014396\ldots,
\qquad
c_*/6=0.1016507198\ldots .
```

The weighted split is intentionally conservative; future work should exploit the distinct geometry of the three currencies rather than pigeonholing them.

---

## 6. Diameter-component consequence

Since

```math
r_H=q-2d_H,
```

NB gives

```math
q-2d_H\ge(c_*-o(1))D.
\tag{6.1}
```

Unlike NM's ratio-only bound `d_H/q<=2/5+o(1)`, NB supplies an absolute diameter-scale deficit from the matching-component endpoint.

The stronger statement still does not force one giant diameter component: a linear number of terminals may be spread across larger caterpillar tree components. It does, however, remove another substantial portion of the matching-component capacity.

---

## 7. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| `h-2<=2r_H+z` | proved | NM exact train-end inequality plus nonnegativity |
| `r_H>=D cos((h-1)a_D)-3/2` | proved | preceding inequality + DB exact defect bound |
| asymptotic NB constant `c_*` | proved | one-variable monotone crossover |
| `c_*` optimal under DB+NM alone | proved | explicit fixed-`y` linear program |
| one of `x_B,Q,s_Z` has displayed linear scale | proved by pigeonhole | direct from NB |
| Level I | still open | each linear currency remains individually possible |

---

## 8. Promotion recommendation

**Hold as report pending independent audit.**

If DB/NM are promoted, NB should replace NM's weaker `2rho/3` asymptotic branching constant. NM remains the source of the exact finite train-end inequality.

---

## 9. Next theorem

NB proves the source cannot hide near the matching endpoint. The remaining exact alternatives are now quantitatively separated:

1. linear outer-walk excess `x_B`;
2. linear bounded face defect `Q`;
3. linear extra mixed row dependence `s_Z`.

The highest-value next step is to attack each alternative with its native structure:

- `x_B`: C51 articulation/bridge topology and the loaded degree-three boundary budget;
- `Q`: convex exceptional-face capacity and stopped-train loss;
- `s_Z`: the `s_Z+1`-dimensional mixed stress space and ZM boundary defect rank.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

NB sharpens NM using DB's defect-dependent term.
Put
    r_H=2h-q=x_B+Q+2s_Z,
    z=Q+2s_Z.
NM gives
    h-2 <= 2r_H+z.
DB gives
    z <= h+1-2D cos((h-1)asin(1/(2D))).
Hence
    r_H >= D cos((h-1)asin(1/(2D)))-3/2,
while NM also gives
    r_H >= (h-2)/3.

If h/D->y, then
    liminf r_H/D >= max{y/3, cos(y/2)}.
The minimum occurs at
    y/3=cos(y/2).
Thus
    liminf (2h-q)/D >= c_*=0.6099043189...,
where
    c_*=cos(3c_*/2).

This constant is optimal using DB+NM alone; Section 4 solves the associated
fixed-y linear program exactly.

Therefore
    x_B+Q+2s_Z >= (0.6099043189-o(1))D.
Next: attack x_B, Q, and s_Z separately.
```
