> Generated reading edition · [exact source](../../../docs/reports/target_c_self_stress_quadrangulation_defect_2026-08-31.md) · source SHA-256 `8cafe47c40aabf26306200ce47384206190e23cd904b05eba5f608d8447ef38c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-3A5778BB4AF5","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C42: pinned self-stress leaves only linear quadrangulation defect

**Date:** 2026-08-31  
**Target:** C-II  
**Depends on:** C26, C33, connected triangle-free penny-graph planarity  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

Let the fully force-visible nonisolated contact core have

- `m` vertices,
- `e` unit contacts,
- `q=|B_+|` loaded force-hull vertices,
- `c_I` connected components after deleting `B_+`, and
- `e_BB` direct loaded-loaded unit contacts.

Let `h` be the outer-face boundary-walk length, counted with multiplicity, and put

```math
\Sigma_4:=\sum_{f\text{ bounded}}(\deg f-4).
```

Then C33's positive-self-stress edge surplus and Euler's formula give the exact defect bound

```math
\boxed{
h+\Sigma_4
\le
4q-2c_I-2e_{BB}-4.
}
\tag{C42.1}
```

Every loaded vertex is a convex-hull vertex of the contact core, so `h>=q`. Hence

```math
\boxed{
\Sigma_4
\le
3q-2c_I-2e_{BB}-4.
}
\tag{C42.2}
```

If `F_4` is the number of bounded degree-four faces, then

```math
\boxed{
F_4
\ge
m-5q+3c_I+3e_{BB}+5.
}
\tag{C42.3}
```

Every such face is a strict unit rhombus with both angles strictly between `60` and `120` degrees.

Thus any C-II core with `m>>D` has `m-O(D)` genuine strict unit-rhombic bounded faces. More strongly, the total number of outer/nonquadrilateral face-edge incidences is at most

```math
\boxed{
16q-10c_I-10e_{BB}-20.
}
\tag{C42.4}
```

The result is a planar-combinatorial transport theorem. It is not a lattice classification or a density gap; disk-clipped oblique rhombic grids remain a binding regression.

---

## 1. C33 supplies the sharpened edge lower bound

Work in the contact-minimal fully force-visible branch. C26 gives

```math
Q^\circ=B_+.
\tag{C42.5}
```

C33 proves

```math
e-e_{BB}\ge2(m-q)+c_I.
```

Equivalently,

```math
\boxed{
e\ge2m-2q+c_I+e_{BB}.}
\tag{C42.6}
```

Because `C_+=C`, the nonisolated contact core is connected and has its ordinary straight-line penny-graph embedding.

---

## 2. Euler gives an exact quadrangulation-defect identity

Let `f_b` be the number of bounded faces. Euler gives

```math
f_b=e-m+1.
\tag{C42.7}
```

The sum of all face-boundary walk lengths is `2e`, so

```math
\sum_{f\text{ bounded}}\deg f=2e-h.
\tag{C42.8}
```

Triangle-freeness and simplicity imply every bounded face boundary walk has degree at least four. Define

```math
\Sigma_4:=\sum_{f\text{ bounded}}(\deg f-4)\ge0.
\tag{C42.9}
```

Using C42.7-C42.8,

```math
\begin{aligned}
\Sigma_4
&=(2e-h)-4(e-m+1)\\
&=4m-2e-h-4.
\end{aligned}
```

Therefore

```math
\boxed{h+\Sigma_4+4=4m-2e.}
\tag{C42.10}
```

Insert C42.6:

```math
4m-2e
\le
4q-2c_I-2e_{BB}.
```

This proves C42.1. `square`

The identity remains valid in the presence of bridges because face degrees and `h` are boundary-walk lengths counted with multiplicity.

---

## 3. The outer walk contains every loaded hull vertex

C26 says every unloaded contact vertex is a strict positive barycenter of its contact neighbors and therefore is not an extreme point of the contact-core convex hull. Every point of `B_+`, on the other hand, is a source diameter endpoint and hence an extreme source point. Therefore

```math
\boxed{B_+=V(\operatorname{conv}V(C)).}
\tag{C42.11}
```

as sets of extreme vertices.

Every convex-hull vertex appears on the unbounded-face boundary walk of a connected straight-line plane graph. Hence

```math
\boxed{h\ge q.}
\tag{C42.12}
```

Combining C42.12 with C42.1 proves C42.2. `square`

---

## 4. Almost every bounded face is a quadrilateral when `m>>D`

Let `F_bad` be the number of bounded faces of degree at least five. Each such face contributes at least one to `Sigma_4`, so

```math
F_{bad}\le\Sigma_4.
\tag{C42.13}
```

C42.6-C42.7 give

```math
f_b
=e-m+1
\ge
m-2q+c_I+e_{BB}+1.
\tag{C42.14}
```

Therefore, using C42.2,

```math
\begin{aligned}
F_4
&=f_b-F_{bad}\\
&\ge
m-2q+c_I+e_{BB}+1
-
(3q-2c_I-2e_{BB}-4)\\
&=
\boxed{m-5q+3c_I+3e_{BB}+5}.
\end{aligned}
\tag{C42.15}
```

This is C42.3.

Because `q<=per(F)<=pi D`, the error term is `O(D)`. Thus `m>>D` implies

```math
F_4=m-O(D).
\tag{C42.16}
```

---

## 5. Degree-four faces are strict unit rhombi

### Lemma C42.1

Every bounded face of degree four is a simple convex rhombus with side length one. If `theta` is either acute/obtuse interior angle representative, then

```math
\boxed{\pi/3<\theta<2\pi/3.}
\tag{C42.17}
```

#### Proof

A bounded degree-four face in a simple triangle-free plane graph has a simple four-cycle as its boundary; a repeated edge or vertex would produce a shorter closed walk or a bridge spur and increase the face-walk length.

All four sides are unit contact edges. A simple equilateral quadrilateral is a rhombus: one diagonal divides it into two congruent triangles by SSS, forcing opposite sides parallel. The face is therefore convex.

Its diagonal lengths are

```math
2\sin(\theta/2),
\qquad
2\cos(\theta/2).
\tag{C42.18}
```

Unit separation makes both diagonals at least one. Equality for either diagonal would make that diagonal and the two adjacent unit sides a unit equilateral triangle, forbidden by hypothesis. Hence both diagonals are strictly greater than one, which is equivalent to C42.17. `square`

---

## 6. Only linearly many face-edge incidences touch the defect set

For a bad bounded face `f`, write `d_f=deg f`. Then

```math
\sum_{f\ bad}d_f
=4F_{bad}+\sum_{f\ bad}(d_f-4)
\le5\Sigma_4.
\tag{C42.19}
```

Therefore the total number of edge incidences on the outer face or on a nonquadrilateral bounded face satisfies

```math
h+\sum_{f\ bad}d_f
\le h+5\Sigma_4.
```

Using `h+Sigma_4<=4q-2c_I-2e_BB-4` and `h>=q`,

```math
\begin{aligned}
h+5\Sigma_4
&=5(h+\Sigma_4)-4h\\
&\le
5(4q-2c_I-2e_{BB}-4)-4q\\
&=
\boxed{16q-10c_I-10e_{BB}-20}.
\end{aligned}
\tag{C42.20}
```

This proves C42.4.

Thus all but `O(D)` face-edge incidences of a large C-II core lie entirely in the strict-rhombic bounded-face bulk.

---

## 7. Exact effect on the C-II frontier

C42 couples the C33 boundary-surplus decomposition to planar geometry:

```text
positive self-stress row surplus:
    e >= 2m-2q+c_I+e_BB

Euler defect identity:
    h+Sigma_4+4 = 4m-2e

therefore:
    h+Sigma_4 <= 4q-2c_I-2e_BB-4
    F_4 >= m-5q+3c_I+3e_BB+5
```

In the C33 near-minimal boundary phase, `c_I+e_BB=o(D)` and `q=Theta(D)`, so a macroscopic force-visible core still has only linear planar defect. In the boundary-surplus phase the same theorem remains valid without a near-minimal assumption.

The missing bridge to Level I is unchanged: the source may contain many contact-isolated points outside the force-visible core, and an `m-O(D)` strict-rhombic bulk alone does not force a triangle because oblique rhombic-grid regressions exist.

A useful closing route would combine C42 with either:

1. a force-bulk theorem showing `n-m=O(D)`; or
2. a new exact response/reciprocal constraint that a large strict-rhombic bulk cannot satisfy under global minimum-diameter geometry.

---

## 8. Regression audit

- **Unit square:** `m=4,q=4,c_I=0,e_BB=4,h=4`. C42.1 and C42.3 are equalities and give the unique bounded square face.
- **Bridge-heavy core:** allowed. Boundary-walk multiplicity is built into C42.10.
- **Reaction-free/loaded block refinements C34/C39:** compatible; C42 is global planar counting and does not replace their local terminal constraints.
- **Disk-clipped oblique rhombic grid:** binding regression. It can have quadratic strict-rhombic bulk and linear boundary defect without a unit triangle.
- **Contact-isolated source points:** not counted in `m`; C42 does not solve the force-bulk problem.
- **C-I:** outside scope because C33 and the identification of loaded boundary/extreme core vertices use full force visibility.

```text
C42:
C33 gives
    e >= 2m-2q+c_I+e_BB.
For the connected plane triangle-free contact core,
    h+Sigma_4+4=4m-2e,
so
    h+Sigma_4 <=4q-2c_I-2e_BB-4.
C26 makes B_+ exactly the extreme contact-core vertices, hence h>=q and
    Sigma_4<=3q-2c_I-2e_BB-4.
Therefore
    F_4>=m-5q+3c_I+3e_BB+5.
Every degree-four bounded face is a strict unit rhombus, and only O(D) total face-edge
incidences touch the outer or nonquadrilateral defect set.
```
