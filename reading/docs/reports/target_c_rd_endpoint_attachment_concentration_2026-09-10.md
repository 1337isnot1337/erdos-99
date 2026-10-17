> Generated reading edition · [exact source](../../../docs/reports/target_c_rd_endpoint_attachment_concentration_2026-09-10.md) · source SHA-256 `e577cc34f00df696b62eecbab65f7482a0ee90d95e65b4e1f2478c9e886b0c39`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

> Source formatting note: 4 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-C98BE98A9F28","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — RD endpoint attachment equality forces one macroscopic cell and a 0.926D singleton layer

**Date:** 2026-09-10  
**Branch base:** `734cc2d318d5932d305ead56af58992e091a3cad`  
**Depends on:** RD/RX, SL on this branch; ZK, C44, C49/GU  
**Run type:** equality concentration / endpoint structural theorem  
**Target:** Target C, C-II after ZF

## LEVEL I STATUS

`STILL OPEN`.

The preceding SL report shows that any sequence approaching the exact RSR/DD endpoint
must contain at least `0.328D` singleton unloaded components.  That estimate uses only
the total component-diameter budget.  The attachment-cell area equality is much more
rigid.

Assume an unbounded post-ZF survivor sequence satisfies

```math
\lambda_D:=\frac{e_{BB}+2s_C}{D}\to\lambda_{RD}.
\tag{AC.1}
```

Then there is one unloaded component `I_*` whose internal contact-graph diameter
`delta_*` satisfies

```math
\boxed{
\frac{\delta_*}{D}\to\lambda_{RD}.
}
\tag{AC.2}
```

All other unloaded components together have sublinear graph diameter:

```math
\boxed{
\frac1D\sum_{r\ne *}\delta_r\to0.
}
\tag{AC.3}
```

Consequently all but `o(D)` of the unloaded components other than `I_*` are singletons.
In particular, if `N_1` denotes the number of singleton unloaded components, then

```math
\boxed{
\liminf\frac{N_1}{D}
\ge y_{RD}-\lambda_{RD}
=0.9263690850317943\ldots .
}
\tag{AC.4}
```

This is almost three times the first SL bound.

Moreover the attachment hull of `I_*` itself asymptotically saturates the planar
isodiametric inequality:

```math
\boxed{
\frac{\operatorname{diam}(A_*)}{D}\to\lambda_{RD},
\qquad
\frac{\operatorname{area}(\operatorname{conv}A_*)}{D^2}
\to\frac\pi4\lambda_{RD}^2.
}
\tag{AC.5}
```

After scaling by `D`, every Hausdorff limit of `conv(A_*)` is therefore a disk of
diameter `lambda_RD`.

Thus an RD endpoint would have an extremely specific two-scale structure:

- one macroscopic unloaded harmonic component with a disk-like attachment hull of
  diameter about `0.59815D`;
- at least `0.92636D-o(D)` singleton unloaded components;
- `Q,s_Z,d_H,d_P=o(D)` and almost all OP outer pockets triangular, by SL.

---

## 1. Endpoint equality saturates the attachment-cell area budget

Let

```math
C_D:=\sum_r\operatorname{area}(\operatorname{conv}A_r),
```

and let `G_D` be the remaining force-hull gap used in ZG/RD, so that up to the
`O(D)` boundary charging term already absorbed in RD,

```math
\operatorname{area}F
\le C_D+H_{out}+A_{exc}+O(D).
\tag{1.1}
```

At the unique RX endpoint, the lower force-hull area and the two upper capacities meet:

```math
A_{RD}
:=\Phi(y_{RD})=\Psi(p_{RD})
=
\frac\pi4\lambda_{RD}^2+\Delta(y_{RD},p_{RD}).
\tag{1.2}
```

RD gives

```math
\limsup\frac{C_D}{D^2}
\le\frac\pi4\lambda_{RD}^2,
\tag{1.3}
```

and

```math
\limsup\frac{H_{out}+A_{exc}}{D^2}
\le\Delta(y_{RD},p_{RD}).
\tag{1.4}
```

while FSDB/RSR gives

```math
\liminf\frac{\operatorname{area}F}{D^2}\ge A_{RD}.
\tag{1.5}
```

If (1.3) had a fixed positive deficit along a subsequence, then (1.1), (1.4), and
(1.5) would contradict (1.2).  Therefore

```math
\boxed{
\frac{C_D}{D^2}
\to\frac\pi4\lambda_{RD}^2.
}
\tag{1.6}
```

So the GU attachment-cell upper bound itself is asymptotically sharp at the RD
endpoint.

---

## 2. ZK supplies the exact total diameter budget

ZK gives

```math
\boxed{
\sum_r\delta_r+R_I+s_B+3(d_H+s_Z)
=6+e_{BB}+2s_C,
}
\tag{2.1}
```

where `R_I,s_B>=0`.  SL already gives

```math
d_H+s_Z=o(D).
\tag{2.2}
```

Hence

```math
\boxed{
S_D:=\sum_r\delta_r
\le\lambda_{RD}D+o(D).
}
\tag{2.3}
```

C44 gives for every unloaded component

```math
\operatorname{diam}(A_r)\le\delta_r+2.
\tag{2.4}
```

The planar isodiametric inequality then gives

```math
\operatorname{area}(\operatorname{conv}A_r)
\le\frac\pi4(\delta_r+2)^2.
\tag{2.5}
```

Summing,

```math
C_D
\le\frac\pi4\sum_r(\delta_r+2)^2.
\tag{2.6}
```

The linear and constant pieces are lower order.  Indeed `c_I=O(D)` and
`S_D=O(D)`, so

```math
\frac1{D^2}
\left[
\sum_r(\delta_r+2)^2-\sum_r\delta_r^2
\right]
=
\frac{4S_D+4c_I}{D^2}
\to0.
\tag{2.7}
```

Combining (1.6), (2.6), and (2.7),

```math
\boxed{
\liminf\frac1{D^2}\sum_r\delta_r^2
\ge\lambda_{RD}^2.
}
\tag{2.8}
```

On the other hand

```math
\sum_r\delta_r^2
\le\left(\sum_r\delta_r\right)^2
=S_D^2,
```

and (2.3) gives the matching upper bound.  Therefore

```math
\boxed{
\frac{S_D}{D}\to\lambda_{RD},
\qquad
\frac1{D^2}\sum_r\delta_r^2\to\lambda_{RD}^2.
}
\tag{2.9}
```

Equation (2.1) then also forces

```math
\boxed{R_I=o(D),\qquad s_B=o(D).}
\tag{2.10}
```

Thus almost all loaded contact-degree capacity is used, and the total internal
Eppstein slack is sublinear.

---

## 3. Sum-of-squares equality forces one component to dominate

Let

```math
M_D:=\max_r\delta_r
```

and choose `I_*` with `delta_*=M_D`.  Since

```math
\sum_r\delta_r^2\le M_D\sum_r\delta_r=M_DS_D,
\tag{3.1}
```

(2.9) gives

```math
\liminf\frac{M_D}{D}
\ge
\lim\frac{\sum_r\delta_r^2/D^2}{S_D/D}
=\lambda_{RD}.
```

But `M_D<=S_D`, so

```math
\boxed{
\frac{M_D}{D}\to\lambda_{RD}.
}
\tag{3.2}
```

Subtracting from the total diameter budget,

```math
\boxed{
\frac{S_D-M_D}{D}\to0.
}
\tag{3.3}
```

This proves AC.2--AC.3.

Every nonsingleton unloaded component has graph diameter at least one.  Therefore the
number of nonsingleton components other than `I_*` is at most

```math
\sum_{r\ne *}\delta_r=o(D).
\tag{3.4}
```

Hence

```math
N_1=c_I-o(D).
\tag{3.5}
```

---

## 4. The singleton density is at least `y_RD-lambda_RD`

SL proves, after passing to a subsequence with

```math
\frac{s_C}{D}\to s\ge0,
```

that

```math
\frac{c_I}{D}
\to y_{RD}-\lambda_{RD}+s.
\tag{4.1}
```

Combining with (3.5),

```math
\liminf\frac{N_1}{D}
\ge y_{RD}-\lambda_{RD}+s
\ge y_{RD}-\lambda_{RD}.
\tag{4.2}
```

This proves AC.4.

Numerically,

```math
y_{RD}-\lambda_{RD}
=0.9263690850317943\ldots .
```

The lower bound is again independent of the unknown split except for a favorable
`+s` term.

---

## 5. The macroscopic attachment hull is asymptotically a disk

Let

```math
A_*\subseteq B_+
```

be the distinct loaded attachment set of `I_*`, and write

```math
K_*:=\operatorname{conv}A_*.
```

From (2.5),

```math
\operatorname{area}K_*
\le\frac\pi4(\delta_*+2)^2
=\frac\pi4\lambda_{RD}^2D^2+o(D^2).
\tag{5.1}
```

All other components have total diameter `o(D)`.  Their total squared diameter is
also `o(D^2)` because

```math
\sum_{r\ne *}\delta_r^2
\le\left(\sum_{r\ne *}\delta_r\right)^2=o(D^2),
```

and the `+2` terms contribute only `O(D)`.  Hence (1.6) forces

```math
\boxed{
\frac{\operatorname{area}K_*}{D^2}
\to\frac\pi4\lambda_{RD}^2.
}
\tag{5.2}
```

The isodiametric upper bound together with (3.2) and (2.4) then forces

```math
\boxed{
\frac{\operatorname{diam}A_*}{D}
\to\lambda_{RD}.
}
\tag{5.3}
```

Indeed any fixed relative deficit in `diam(A_*)` would create a fixed quadratic area
deficit in (5.2).

Normalize `K_*` by `D` and translate arbitrarily.  Its diameter tends to
`lambda_RD`, its area tends to `pi lambda_RD^2/4`, and it lies in a common bounded
container.  By Blaschke selection, every subsequence has a Hausdorff-convergent further
subsequence.  Diameter and area are continuous under planar convex Hausdorff
convergence, so every limit body has diameter `lambda_RD` and maximal possible area.
The equality case of the planar isodiametric inequality is the disk.  Therefore

```math
\boxed{
D^{-1}K_*\text{ is asymptotically disk-like in Hausdorff subsequential limits.}
}
\tag{5.4}
```

---

## 6. Consequences for the contact graph

The endpoint now has the following sharpened normal form.

```text
force hull:
    h/D -> y_RD = 1.52452270349...
    per(F)/D -> p_RD = 3.02313696674...

vanishing defect:
    Q,s_Z,d_H,d_P=o(D)
    q-a=o(D)
    almost every outer pocket is triangular

unloaded contact components:
    c_I/D >= y_RD-lambda_RD = 0.9263690850...
    one component I_* has graph diameter
        delta_*/D -> lambda_RD = 0.59815361846...
    all other component diameters sum to o(D)
    all but o(D) of those other components are singleton vertices

macroscopic cell:
    diam(A_*)/D -> lambda_RD
    area(conv A_*)/D^2 -> pi lambda_RD^2/4
    normalized conv(A_*) -> a disk along every Hausdorff limit

component ledger:
    R_I=o(D)
    s_B=o(D)
```

The contact graph therefore consists, to first order in component count, of one
macroscopic disk-like harmonic cell plus a linear dust of singleton harmonic cells.
At the same time the loaded diameter graph has `d_H=o(D)` and is governed by the
Woodall connected-cycle / few-caterpillar dichotomy on current `main`.

---

## 7. New shortest target

The previous candidate was a direct singleton-to-pocket turning lemma.  AC gives a
stronger target: almost every unloaded component is singleton, while one exceptional
component alone must carry essentially all quadratic attachment-cell area.

There are now two possible closing mechanisms.

1. **Disk-on-boundary obstruction.**  `A_*` is a linear subset of loaded vertices of
   the global convex force hull, but `conv(A_*)` must converge to a disk of diameter
   only `lambda_RD D`.  Prove that a convex polygon of diameter `D` and perimeter
   `p_RD D` cannot have a boundary-vertex subset whose hull is asymptotically such a
   smaller disk while the remaining attachment sets are noncrossing singleton cells.
2. **Singleton annulus obstruction.**  At least `0.926D` singleton cells must fit in
   the complement of the disk-like `K_*`, with three or more unit contacts to loaded
   force-hull vertices and pairwise disjoint attachment-cell interiors.  Convert that
   incidence into a positive perimeter/area cost exceeding the narrow RD cavity
   budget.

Either route would exclude the exact RD endpoint.  A quantitative version would raise
the explicit generic floor above `0.5981536184...` rather than merely prove another
nonattainment gap.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| attachment-cell area saturates | proved | endpoint lower area equals GU + DD capacities |
| `sum delta_r/D -> lambda_RD` | proved | ZK upper + saturated squared-area chain |
| `sum delta_r^2/D^2 -> lambda_RD^2` | proved | cell isodiametry + endpoint saturation |
| one `delta_*~lambda_RD D` | proved | `sum squares <= max * sum` |
| all other diameters total `o(D)` | proved | total minus maximum |
| singleton count `>= (y_RD-lambda_RD-o(1))D` | proved | SL component count + diameter concentration |
| macroscopic attachment hull asymptotically disk | proved | individual area saturation + isodiametric equality |
| Level I | still open | disk/singleton coexistence not yet excluded |

---

## 9. Next run

Audit the geometry of a disk-like attachment hull whose vertices are themselves
vertices of the larger force hull.  The first concrete question is whether the
cyclic-order/noncrossing attachment theorem forces the macroscopic attachment set
`A_*` to occupy one or a bounded number of boundary intervals.  If it occupies a
single interval, its convex hull cannot be disk-like unless its diameter is comparable
to the full force hull; if it occupies many alternating intervals, noncrossing of the
linear singleton attachment sets should fail.  Prove that combinatorial interval
lemma before attempting another scalar optimization.
