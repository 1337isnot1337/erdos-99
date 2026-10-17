> Generated reading edition · [exact source](../../../docs/reports/target_c_post_zf_near_matching_train_stability_2026-09-09.md) · source SHA-256 `676140ba8863f14f57189fa28346c39e1a23c4b2693d305f689afdd7ef0eaaab`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-4E744BE863E4","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF near-matching train stability forces linear diameter branching

**Date:** 2026-09-09  
**Repository base:** `faa60082283fb0c3c64b59c9817219083d46962e` plus MC on this branch  
**Run type:** exact stability theorem / branch closure  
**Target:** Target C C-II after ZF  
**Depends on:** C77 rhombic train pseudolines, DT exact stopped-train count, ZE/ZT/DB, C42/C51 outer-face topology  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

MC excludes the exact perfect-matching diameter graph. This report proves the quantitative stability theorem suggested by that closure: a post-ZF survivor cannot even be **sublinearly close** to a diameter matching.

Let

```math
\boxed{r_H:=2h-q
=\sum_{b\in B_+}(\deg_H(b)-1)
=x_B+Q+2s_Z.}
\tag{NM.1}
```

Then every sufficiently large post-ZF survivor satisfies the exact finite inequality

```math
\boxed{
3r_H\ge h-2.
}
\tag{NM.2}
```

Consequently

```math
\boxed{
r_H\ge\frac{\lceil D\rceil-2}{3},}
\tag{NM.3}
```

and, using DB's stronger diameter-edge density,

```math
\boxed{
\liminf_{D\to\infty}\frac{r_H}{D}
\ge\frac{2\rho}{3}
=0.4927234221\ldots ,
}
\tag{NM.4}
```

where `rho` is the positive solution of `rho=cos rho`.

Thus the low-branching regime

```math
2h-q=o(D)
```

is completely eliminated. The post-ZF diameter graph must carry a definite linear amount of degree excess above a perfect matching.

---

## 1. Outer-walk excess localizes bad hull intervals

Write the loaded force-hull vertices in cyclic order as

```math
b_1,\ldots,b_q.
```

The outer contact-face boundary walk encounters these extreme vertices in the same cyclic order, possibly with repeated vertices/bridge excursions between consecutive hull vertices. Choose one cyclic pass and split the outer walk into `q` subwalks

```math
W_i:b_i\leadsto b_{i+1}.
```

Let `ell_i` be the number of contact-edge occurrences in `W_i`. Every consecutive hull pair is distinct and every contact path has at least one edge, so

```math
ell_i\ge1.
```

Since

```math
b=q+x_B,
```

we have

```math
\sum_{i=1}^q(\ell_i-1)=x_B.
\tag{1.1}
```

Call `W_i` **good** if `ell_i=1` and **bad** otherwise. Let `m_bad` be the number of bad intervals. Then

```math
m_{bad}\le x_B.
\tag{1.2}
```

The total number of outer-walk edge occurrences lying in bad intervals is

```math
\sum_{W_i\ bad}\ell_i
=m_{bad}+\sum_{W_i\ bad}(\ell_i-1)
\le2x_B.
\tag{1.3}
```

If `W_i` is good, its unique edge joins two consecutive vertices of the convex force hull. The straight segment between those vertices is the hull side itself. Hence every good interval is one **unit convex-hull side contact**.

Thus at most `2x_B` outer-face edge incidences can be train ends that are not on good unit hull sides.

---

## 2. Exact exceptional-face train-end count

Let

- `f` be the number of bounded nonquadrilateral contact faces;
- `Q=sum_F(deg F-4)` over those faces;
- `g_F=sum_F(deg F-5)`.

Then

```math
Q=f+g_F.
\tag{2.1}
```

The total boundary length of all exceptional bounded faces is not merely bounded by `5Q`; it is exactly

```math
\boxed{
L_{exc}:=\sum_{F\ exc}\deg F
=5f+g_F.
}
\tag{2.2}
```

Every rhombic train end not on the outer contact face lies on an edge incident to a bounded nonquadrilateral face. Counting by face incidences therefore gives at most

```math
5f+g_F
\tag{2.3}
```

such bad train-end incidences.

---

## 3. At most two trains can have two good convex-hull ends

Call a rhombic train **good** if both of its terminal edges are good unit hull-side contacts from Section 1.

C77 proves every train has one fixed unoriented edge direction; hence the two boundary ends of a good train are parallel unit hull sides.

A strict convex polygon has strictly increasing oriented edge direction around its boundary. Therefore an oriented edge direction occurs at most once, and an unoriented direction occurs at most twice, once in each opposite orientation. It follows that:

1. the two ends of one good train are an opposite-oriented parallel pair;
2. two distinct good trains have distinct unoriented directions.

Take two good trains with projective directions represented by

```math
0\le\theta_i<\theta_j<\pi.
```

Their four oriented hull-side directions occur cyclically as

```math
\theta_i,
\theta_j,
\theta_i+\pi,
\theta_j+\pi.
\tag{3.1}
```

Hence their two pairs of boundary edges alternate around the convex hull.

Represent the train tracks by C77's embedded simple dual arcs connecting the midpoints of their two terminal edges. Two disjoint arcs in a disk cannot connect alternating boundary pairs. Therefore every two good trains cross.

C77 says the train-intersection graph is triangle-free. Thus there cannot be three pairwise-crossing good trains.

### Lemma NM.1

```math
\boxed{
T_{good}\le2.
}
\tag{3.2}
```

This is the stable form of the complete-crossing argument used in MC.

---

## 4. Every other train consumes a bad end

C77 proves every train has exactly two boundary ends. A train that is not good has at least one end either

1. on an outer-face edge occurrence belonging to a bad hull interval; or
2. on a bounded exceptional-face edge.

By (1.3) and (2.3), the total number of available bad train-end incidences is at most

```math
2x_B+5f+g_F.
\tag{4.1}
```

Different train ends are distinct track states, so charging each nongood train to one bad end gives

```math
T-T_{good}
\le2x_B+5f+g_F.
```

Using `T_good<=2`,

```math
\boxed{
T-2\le2x_B+5f+g_F.
}
\tag{4.2}
```

This is the key stability inequality.

---

## 5. Convert train-end loss into diameter branching

DT and ZE give the exact train count

```math
T=\frac{b+Q}{2}+2f
=h-s_Z+2f.
\tag{5.1}
```

Insert this into (4.2):

```math
h-s_Z+2f-2
\le2x_B+5f+g_F.
```

Therefore

```math
\boxed{
h-2
\le2x_B+3f+g_F+s_Z.}
\tag{5.2}
```

ZT/DB give the exact diameter branching currency

```math
\boxed{
r_H=2h-q=x_B+Q+2s_Z
=x_B+f+g_F+2s_Z.}
\tag{5.3}
```

Multiply (5.3) by three. Since all currencies are nonnegative,

```math
\begin{aligned}
3r_H-(2x_B+3f+g_F+s_Z)
&=x_B+2g_F+5s_Z\\
&\ge0.
\end{aligned}
\tag{5.4}
```

Combine (5.2)-(5.4):

```math
\boxed{
3r_H\ge h-2.
}
```

This proves NM.2.

---

## 6. Diameter-scale consequences

ZS gives

```math
h\ge\delta\ge\lceil D\rceil.
```

Hence NM.2 immediately gives the finite bound

```math
\boxed{
2h-q
\ge
\frac{\lceil D\rceil-2}{3}.
}
\tag{6.1}
```

Since the left side is an integer one may insert a ceiling on the right if desired.

DB strengthens the diameter-edge density to

```math
\liminf\frac hD\ge2\rho,
\qquad
\rho=\cos\rho.
```

Divide NM.2 by `D` and pass to an unbounded sequence:

```math
\boxed{
\liminf\frac{2h-q}{D}
\ge\frac{2\rho}{3}
=0.4927234221\ldots .
}
\tag{6.2}
```

This is NM.4.

---

## 7. Diameter-component consequences

Since

```math
d_H=q-h
```

and

```math
r_H=2h-q=q-2d_H,
```

NM.2 gives

```math
q-2d_H
\ge\frac{q-d_H-2}{3}.
```

Rearranging,

```math
\boxed{
5d_H\le2q+2.
}
\tag{7.1}
```

Thus asymptotically

```math
\boxed{
\frac{d_H}{q}\le\frac25+o(1).
}
\tag{7.2}
```

The canonical planar diameter pseudoforest interpretation identifies `d_H` with the number of tree components of `H`. Therefore a post-ZF survivor cannot decompose into almost all two-vertex matching components: at least a linear fraction of the terminal budget must be absorbed inside larger tree components and/or the possible odd-unicyclic component.

Equivalently, the average diameter degree satisfies

```math
\frac{2h}{q}
=1+\frac{r_H}{q}
\ge\frac65-o(1),
\tag{7.3}
```

where the final asymptotic form follows from (7.2).

---

## 8. What the theorem closes

Before NM, DB gave the exact split

```text
low branching x_B+Q+2s_Z=o(D)
    -> almost perfect matching diameter graph

linear branching
    -> explicit contact/topology defect currency
```

NM eliminates the first side completely. Every unbounded post-ZF survivor now lies in the **linear branching/contact-defect phase**:

```math
\boxed{
 x_B+Q+2s_Z
 =2h-q
 =\Omega(D).
}
\tag{8.1}
```

Thus future work does not need a near-matching stability theorem; NM is that theorem.

The remaining problem is to convert this mandatory linear currency into one of:

1. the forbidden face sign `b+Q>2h`;
2. a quantitative ZM response mass;
3. a finite strict sub-`D` motion;
4. a global source-capacity contradiction.

---

## 9. Regression audit

### Perfect matching

Then `r_H=0`. NM.2 gives `h<=2`, reproducing MC. Thus NM strictly contains the exact matching exclusion.

### One or two good train families plus many defect ends

Allowed. The theorem charges every additional train to explicit outer-walk or exceptional-face currencies. It does not assume global pure-rhombic topology.

### Giant exceptional face

Allowed, but expensive in the exact end budget `5f+g_F`. A high-degree face contributes only one unit per degree above five to `g_F`, which is why the final universal factor is three rather than an artificially stronger constant.

### Bridge-heavy outer face

Allowed. Repeated/bridge excursions increase `x_B`; Section 1 counts their edge occurrences rather than silently replacing the outer walk by a simple polygon.

### Oblique two-family rhombic grid

Compatible with C77. Such a grid can have many crossing trains without a train triangle, but only if its train ends are not all paired on the convex unit hull. NM charges the necessary boundary/face failures.

---

## 10. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| bad outer train-end incidences `<=2x_B` | proved | exact hull-interval excess count |
| exceptional train-end incidences `<=5f+g_F` | proved | exact exceptional-face perimeter |
| at most two good trains | proved | convex parallel pairing + alternating endpoints + C77 triangle-freeness |
| `T-2<=2x_B+5f+g_F` | proved | one bad-end charge per nongood train |
| `3(2h-q)>=h-2` | proved | DT/ZE/ZT exact algebra |
| branching `Omega(D)` | proved post-ZF | ZS, strengthened by DB |
| near-matching branch remains | rejected | NM excludes it |
| Level I | still open | mandatory linear defect still needs conversion to contradiction |

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

If the ZF/ZE/ZT/DB stack is promoted, NM should replace both MC and the former low-branching branch in the active Target C frontier. MC remains a useful transparent endpoint proof but is mathematically subsumed by NM.

---

## 12. Next theorem

After NM the exact survivor class satisfies

```math
x_B+Q+2s_Z\ge(2\rho/3-o(1))D.
```

The next split should use which currency is large:

1. `x_B=Omega(D)`: many outer-face excursion edges beyond the convex loaded cycle;
2. `Q=Omega(D)`: linear bounded nonquadrilateral face defect;
3. `s_Z=Omega(D)`: linear extra mixed active-row dependence.

A theorem excluding each currency at that scale, or transporting any one of them into the ZM mass/finite-motion endpoint, would close the remaining post-ZF topology.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

NM near-matching stability:
Let
    r_H=2h-q=x_B+Q+2s_Z.
Split the outer contact walk between consecutive force-hull vertices.
Since b=q+x_B, at most 2x_B outer edge occurrences lie in non-single-edge
hull intervals. Exceptional bounded faces contribute exactly
    5f+g_F
train-end incidences.

Any train with both ends on good convex unit hull sides is paired between two
parallel hull sides. Any two such trains have alternating boundary endpoints and
must cross. C77's train graph is triangle-free, so at most two such trains exist.
Hence
    T-2 <= 2x_B+5f+g_F.
Using
    T=h-s_Z+2f,
    Q=f+g_F,
    r_H=x_B+f+g_F+2s_Z,
we get
    3r_H >= h-2.

Therefore
    2h-q >= (ceil(D)-2)/3,
and DB sharpens asymptotically to
    liminf (2h-q)/D >= 2rho/3 = 0.4927234221...,
where rho=cos rho.

Also
    d_H/q <= 2/5+o(1),
so the full diameter graph cannot be close to a disjoint matching decomposition.

The low-branching post-ZF phase is closed. Every survivor has mandatory linear
outer/face/mixed-row defect x_B+Q+2s_Z.
```
