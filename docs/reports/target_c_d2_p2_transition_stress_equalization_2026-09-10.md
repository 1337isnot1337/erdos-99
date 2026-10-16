<!-- theorem-state: {"artifact_id":"ART-EDB1A47B4E79","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — cyclic D2/P2 forces equal stress on all four transition contacts

**Date:** 2026-09-10  
**Repository branch:** `research/target-c-d2-transversality-2026-09-10`  
**Run type:** exact P2 statics / moment-balance theorem  
**Target:** cyclic primitive phase `d_H=2`, parallel-parallel cell endpoint P2  
**Depends on:** D2 four-block cut, D2C exact defect cells, WM force-and-moment lift from PR #118  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

The P2 endpoint is the D2 branch in which both cross-tree defect cells attain

\[
G_1=G_2=\Delta_2:=2\arcsin(1/D).
\]

D2C then makes the two transition contacts belonging to either switch parallel and oppositely oriented. The force part of WM equalizes the two stresses inside each opposite pair. The moment part of WM, together with the exact P2 strip width, equalizes the two pairs.

### Theorem P2E — four transition stresses are equal

Write the four A/B shell-transition contacts in cyclic order as

\[
t_1,t_2,t_3,t_4,
\qquad |t_j|=1,
\]

with the D2 component-cut signs chosen so that

\[
\alpha_1L_1-\alpha_2L_2+\alpha_3L_3-\alpha_4L_4=0,
\tag{P2E.1}
\]

where `L_j=(t_j,m_j)` is the WM line/wrench vector.

In the P2 branch the two D2C switch cells pair the transitions as

\[
(t_1,t_3),
\qquad
(t_2,t_4).
\]

Then

\[
\boxed{t_3=-t_1,
\qquad
t_4=-t_2,}
\tag{P2E.2}
\]

and each opposite pair of supporting lines is separated by

\[
\boxed{R_D:=\sqrt{D^2-1}.}
\tag{P2E.3}
\]

Consequently

\[
\boxed{
\alpha_1=\alpha_2=\alpha_3=\alpha_4>0.
}
\tag{P2E.4}

\]

Equivalently, the four distinguished cycle resistances `r_j=1/alpha_j` are also equal.

This is a new exact boundary condition for the P2 staircase closure and WT transfer systems. It does not by itself close P2.

---

## 1. Pairing of the four transition sides

D2 gives the cyclic force-hull blocks

\[
A_0\mid B_0\mid A_1\mid B_1.
\]

Label the four transition contacts respectively

\[
t_1:A_0|B_0,
\quad
t_2:B_0|A_1,
\quad
t_3:A_1|B_1,
\quad
t_4:B_1|A_0.
\]

At one cross-tree direction switch, D2C uses four cyclic endpoints `A,B,C,D` with the two adjacent diameter chords

\[
AC\in T_A,
\qquad
BD\in T_B.
\]

The two transition contacts belonging to that cell are `AB` and `CD`. In the four-block order these are exactly `t_1,t_3`, up to a cyclic relabeling of the switches. The other switch therefore contains `t_2,t_4`.

In a P-type D2C cell, the midpoint offset is zero. D2C then gives the two transition side vectors as negatives of one another. Hence

\[
t_3=-t_1,
\qquad
t_4=-t_2.
\]

This proves P2E.2.

---

## 2. Exact separation of one P-cell side pair

Use the D2C midpoint notation for one switch. Let the consecutive cross-tree diameter vectors be

\[
u=C-A,
\qquad
v=D-B,
\qquad |u|=|v|=D,
\]

with common midpoint in the P case. Put

\[
p=\frac{u-v}{2},
\qquad
r=\frac{u+v}{2}.
\]

Then

\[
p\perp r,
\qquad
|p|=D\sin(G/2),
\qquad
|r|=D\cos(G/2).
\]

At the P2 endpoint

\[
G=\Delta_2=2\arcsin(1/D),
\]

so

\[
|p|=1
\]

and

\[
\boxed{|r|=D\cos(\Delta_2/2)=\sqrt{D^2-1}.}
\tag{2.1}
\]

With common midpoint normalized to the origin, the four endpoints can be written

\[
A=-u/2,
\quad C=u/2,
\quad B=-v/2,
\quad D=v/2.
\]

The transition vectors `B-A` and `D-C` are opposite unit vectors parallel to `p`. Their midpoints differ by the vector `r`, which is perpendicular to `p`. Therefore the supporting lines of the two transition contacts are parallel and their perpendicular separation is exactly

\[
|r|=R_D=\sqrt{D^2-1}.
\]

The same calculation applies to the second P cell. This proves P2E.3.

---

## 3. Force balance equalizes each opposite pair

Take the first two coordinates of WM/P2E.1:

\[
\alpha_1t_1-\alpha_2t_2+
\alpha_3t_3-\alpha_4t_4=0.
\]

Insert P2E.2:

\[
(\alpha_1-\alpha_3)t_1
=(\alpha_2-\alpha_4)t_2.
\tag{3.1}
\]

The directions `t_1,t_2` are linearly independent. If they were parallel, P2E.2 would put all four transition sides in one unoriented direction. Since each pair already contains both orientations, this would repeat an oriented support direction on two distinct sides of the strictly convex force hull, impossible.

Therefore both coefficients in (3.1) vanish:

\[
\boxed{
\alpha_1=\alpha_3=:a,
\qquad
\alpha_2=\alpha_4=:b.
}
\tag{3.2}
\]

Positivity of the cyclic KKT stress gives `a,b>0`.

---

## 4. Moment balance equalizes the two pairs

Let

\[
m_j=p_j\times t_j
\]

be the WM signed moment coordinate of transition side `j`, with the shell oriented consistently around the strictly convex force hull.

For two oppositely oriented parallel unit sides `t_3=-t_1`,

\[
m_1+m_3
=(p_1-p_3)\times t_1.
\]

Its absolute value is exactly the perpendicular separation of their two support lines. With the consistent convex boundary orientation the signed value is positive. Section 2 therefore gives

\[
\boxed{m_1+m_3=R_D.}
\tag{4.1}
\]

Likewise

\[
\boxed{m_2+m_4=R_D.}
\tag{4.2}
\]

The third coordinate of WM/P2E.1 is

\[
\alpha_1m_1-\alpha_2m_2+
\alpha_3m_3-\alpha_4m_4=0.
\]

Use (3.2):

\[
a(m_1+m_3)=b(m_2+m_4).
\]

Equations (4.1)-(4.2) give

\[
aR_D=bR_D.
\]

Since `D>1`, `R_D>0`, hence

\[
a=b.
\]

Together with (3.2),

\[
\alpha_1=\alpha_2=\alpha_3=\alpha_4.
\]

This proves P2E.4. `square`

---

## 5. WT consequence

Put

\[
r_j:=1/\alpha_j.
\]

Then P2E gives

\[
\boxed{r_1=r_2=r_3=r_4=:r_* .}
\tag{5.1}
\]

WT expresses transfer between crossing selected diameter chords using products of total cycle resistances on the four intervening arcs. P2E fixes the four boundary contributions at the A/B interfaces to the same value exactly.

Any remaining asymmetry in a P2 WT numerator must therefore come entirely from the internal resistance sums of the four shell blocks, not from the transition contacts themselves.

This is useful because the two staircase bodies separately determine those block-internal contact stresses through statically determinate `D,D,1` triangle chains once the four boundary reactions and diameter loads are fixed.

---

## 6. Regression audit

- The theorem is P2-specific. In an S cell the opposite transition sides are not parallel and the equalization argument does not apply.
- Equal transition stresses are compatible with selected-support regular-shell regressions in principle; P2E does not claim a contradiction from equality alone.
- The moment equation is essential. Force balance gives only two pairwise equalities `alpha_1=alpha_3` and `alpha_2=alpha_4`.
- The common strip width is exactly `sqrt(D^2-1)` because both cells are at the same P endpoint `G=Delta_2`; no near-equality estimate is used.
- No C56 sign or PSD assumption beyond the existing cyclic KKT theorem is needed.

---

## 7. Next target

The next P2 theorem should propagate the four equal boundary contact reactions into the two isostatic staircase bodies.

For one `D,D,1` triangle-chain body, solve the central-force equilibrium recursively from its two boundary transition reactions. The target is one of:

1. show that equal transition reactions force the staircase word to be the regular/Reinhardt selected-support word, in which case the two formally omitted diameter states return as actual diameter equalities and `d_H=2` collapses;
2. derive explicit block resistance sums from the word and insert them into WT, showing that the unique P2 stress cannot satisfy the required C56-G transfer sign pattern;
3. identify an exact nonregular staircase word realizing P2E, which would be a binding local regression and would redirect the proof away from statics.

---

## Compact handoff

```text
P2: both D2 defect cells have G=Delta_2=2 asin(1/D) and zero midpoint offset.
Four shell transition sides t1,t2,t3,t4 pair by switch as (t1,t3),(t2,t4).
D2C gives
    t3=-t1, t4=-t2.
For either pair the support-line separation is
    R_D=D cos(Delta_2/2)=sqrt(D^2-1).
WM force balance:
    alpha1 t1-alpha2 t2+alpha3 t3-alpha4 t4=0.
Since t1,t2 are independent,
    alpha1=alpha3=a, alpha2=alpha4=b.
WM moment balance gives
    a(m1+m3)=b(m2+m4).
Both signed sums equal R_D, hence a=b.
Therefore
    alpha1=alpha2=alpha3=alpha4,
and the four transition resistances are equal as well.
```
