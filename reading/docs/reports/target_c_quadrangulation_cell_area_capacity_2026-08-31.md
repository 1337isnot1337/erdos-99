> Generated reading edition · [exact source](../../../docs/reports/target_c_quadrangulation_cell_area_capacity_2026-08-31.md) · source SHA-256 `5e685cdb30496cc50ccbf61d56aebfae86597c95e1c06d19f7dadef8abad2a39`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-4F249B658A29","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C48: quadrangulation plus attachment cells gives an O(D)-error core-capacity bound

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** canonical C30, mainline C42 quadrangulation defect, C43 and elementary rhombus area  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

C45 applies Oler separately to the harmonic attachment cells and pays a perimeter term of order `D c_I`. Mainline C42 gives a stronger route once the force-visible contact core is large: all but `O(D)` of its bounded contact faces are quadrilaterals. C43 makes the harmonic attachment cells interior-disjoint.

Let

- `m` be the force-visible contact-core population;
- `F_4` be the number of bounded quadrilateral contact faces in the C42 sense;
- `q=|B_+|`;
- `P_r=conv(A_r)` the C43 attachment cells; and
- `G=area(F)-sum_r area(P_r)>=0`.

Then

```math
\boxed{
 m
<
\frac{2}{\sqrt3}(\operatorname{area}(F)-G)
+(m-F_4)+3q.}
```

Because C42 gives `m-F_4=O(D)`, canonical convex perimeter gives `q<=pi D`, and `area(F)<=pi D^2/4`,

```math
\boxed{
 m
\le
\Delta_2D^2
-
\frac{2}{\sqrt3}G
+O(D),
\qquad
\Delta_2=\frac\pi{2\sqrt3}.}
```

Thus the attachment-cell area gap now survives with only a linear finite-error term, independent of the number of harmonic components.

---

## 1. Quadrilateral faces touching the loaded boundary are only O(q)

Every loaded vertex `b in B_+` has full contact degree at most three by C35. In a plane graph, the number of bounded face incidences at a vertex is at most its degree. Therefore the number of bounded quadrilateral faces having at least one loaded vertex is at most

```math
\sum_{b\in B_+}\deg_C(b)
\le3q.
\tag{C48.1}
```

Hence at least

```math
\boxed{F_4-3q}
\tag{C48.2}
```

quadrilateral faces have all four vertices in the unpinned set `I=V(C)\setminus B_+`.

No issue arises if `F_4-3q` is negative for small sources; the asymptotic use is in the C42 large-core regime.

---

## 2. Every internal quadrilateral is a strict unit rhombus

A bounded quadrilateral contact face has four unit-length sides. Therefore it is a Euclidean rhombus.

Let its acute angle be `theta`. The two diagonals have lengths

```math
2\sin(\theta/2),
\qquad
2\cos(\theta/2).
```

Both diagonals join distinct source points, so unit separation gives both lengths at least one. Hence

```math
\frac\pi3\le\theta\le\frac{2\pi}3.
\tag{C48.3}
```

Equality at either endpoint would make the shorter diagonal exactly one. Together with two unit sides, that diagonal would form a unit equilateral triangle, forbidden in the triangle-free branch. Therefore

```math
\frac\pi3<\theta<\frac{2\pi}3.
\tag{C48.4}
```

The rhombus area is `sin theta`, so

```math
\boxed{\operatorname{area}(R)>\frac{\sqrt3}{2}.}
\tag{C48.5}
```

---

## 3. Internal rhombi lie inside the attachment cells

Take one quadrilateral face whose four vertices are unpinned. Its four contact edges connect those vertices, so all four lie in the same connected component `I_r` of the unpinned contact graph.

C36 gives

```math
I_r\subseteq P_r=\operatorname{conv}A_r.
```

Therefore the whole rhombus, being the convex hull of its four vertices, lies in `P_r`.

Distinct bounded faces of the plane contact graph have disjoint interiors. C43 additionally gives pairwise disjoint interiors for distinct cells. Consequently the areas of all internal quadrilateral faces can be summed inside the attachment-cell area budget:

```math
\sum_r\operatorname{area}(P_r)
>
\frac{\sqrt3}{2}(F_4-3q).
\tag{C48.6}
```

By definition of `G`,

```math
\operatorname{area}(F)-G
>
\frac{\sqrt3}{2}(F_4-3q).
\tag{C48.7}
```

---

## 4. Exact core-capacity inequality

Rearrange C48.7:

```math
F_4
<
\frac{2}{\sqrt3}(\operatorname{area}(F)-G)+3q.
\tag{C48.8}
```

Write

```math
m=F_4+(m-F_4).
```

Then:

### Theorem C48.1 — exact quadrangulation-cell capacity

```math
\boxed{
 m
<
\frac{2}{\sqrt3}(\operatorname{area}(F)-G)
+(m-F_4)+3q.}
\tag{C48.9}
```

This statement is exact and isolates the only two finite corrections:

1. the canonical C42 quadrangulation defect `m-F_4`;
2. the loaded boundary count `3q`.

There is no `D c_I` term.

---

## 5. O(D)-error asymptotic form

Mainline C42 proves

```math
m-F_4=O(D)
\tag{C48.10}
```

for the fully force-visible core in the large-core regime.

Canonical C30 gives `q=Theta(D)` and the convex perimeter bound gives the explicit upper estimate

```math
q\le\operatorname{per}(F)\le\pi D.
\tag{C48.11}
```

Finally, the isodiametric inequality gives

```math
\operatorname{area}(F)\le\frac\pi4D^2.
\tag{C48.12}
```

Therefore C48.9 yields:

### Theorem C48 — O(D)-error force-visible core capacity

```math
\boxed{
 m
\le
\Delta_2D^2
-
\frac{2}{\sqrt3}G
+O(D),
\qquad
\Delta_2=\frac\pi{2\sqrt3}.}
\tag{C48.13}
```

The implicit constant is completely effective from the explicit C42 defect bound plus `3pi D`; no new asymptotic theorem is imported.

---

## 6. Why C48 is stronger than C45

C45 gave

```math
m
\le
\Delta_2D^2
-
\frac{2}{\sqrt3}G
+
\frac\pi2D c_I
+c_I+e_{BB}.
```

In the near-minimal phase `c_I=o(D)`, this is only an `o(D^2)` correction.

C48 replaces the entire component-perimeter term by the C42 quadrangulation defect plus loaded-boundary face incidences, both `O(D)`. Thus the finite correction is linear **regardless of `c_I`** whenever C42's quadrangulation regime applies.

---

## 7. Remaining global obstruction

C48 controls only the force-visible contact core. The source may still contain contact-isolated KKT-invisible points outside that core. Therefore C48 does not imply

```math
n\le\Delta_2D^2+O(D)
```

with the favorable cell-area gap unless one additionally proves a force-bulk theorem such as

```math
n-m=O(D).
```

This identifies the contact-isolated population as an exact remaining global-capacity obstruction.

Even if `n-m=O(D)` were proved, one would still need either a cell-area gap `G` exceeding the finite `O(D)` correction or another strict finite-packing term. The theorem does not hide either requirement.

## Regression audit

- A quadrangulated near-triangular bulk with rhombus angles approaching `60` degrees is allowed; C48 uses only the strict area `>sqrt3/2` face by face and makes no uniform angular-gap claim.
- One giant attachment cell with `G=0` is allowed; C48 then becomes a sharp `Delta_2D^2+O(D)` core-capacity estimate.
- Contact-isolated source points remain outside the bound and are explicitly identified as the main force-bulk gap.
