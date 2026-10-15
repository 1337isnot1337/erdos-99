# Target C — C42 quadrangulation-defect frontier

**LEVEL I STATUS: STILL OPEN.**

This module records the planar consequence of combining C33's positive-self-stress edge surplus with the fully force-visible contact-core embedding.

Let

- `m` be the number of nonisolated contact-core vertices;
- `q=|B_+|`;
- `c_I` be the number of components after deleting `B_+`;
- `e_BB` be the direct loaded-loaded contact count;
- `h` be the outer-face boundary-walk length; and
- `Sigma_4=sum_bounded(deg f-4)`.

C42 proves

`h+Sigma_4 <= 4q-2c_I-2e_BB-4`.

Because C26 makes `B_+` exactly the extreme vertices of the contact core, `h>=q`, so

`Sigma_4 <= 3q-2c_I-2e_BB-4`.

If `F_4` is the number of bounded quadrilateral faces, then

`F_4 >= m-5q+3c_I+3e_BB+5`.

Every such face is a strict unit rhombus with both angles in `(60,120)` degrees. Moreover only

`16q-10c_I-10e_BB-20`

outer/nonquadrilateral face-edge incidences can touch the planar defect set.

Since `q<=pi D`, any force-visible core with `m>>D` therefore has an `m-O(D)` strict-rhombic face bulk and only `O(D)` total planar defect.

## C49 — two-scale strict-rhombus capacity

Let `F=conv V(C)`, `A_F=area(F)`, and, when `c_I>=1`, let

`G=area(F)-sum_r area(conv A_r)`.

C49 charges all bounded quadrilateral faces to `F` and obtains the unconditional
whole-hull estimate

`m < 2A_F/sqrt(3)+5q-3c_I-3e_BB-5`.

It also charges every quadrilateral face without a loaded vertex to its harmonic
attachment cell. A loaded convex-hull vertex has one exterior face sector and C35
gives contact degree at most three, so at most `2q` quadrilateral faces are lost at
the loaded boundary. C36-C38 imply that the attachment cells have pairwise disjoint
interiors. Therefore the refined estimate is

`m < 2(A_F-G)/sqrt(3)+7q-3c_I-3e_BB-5`.

The exact two-scale theorem and proof are in
[the C49 audited report](../../reports/target_c_two_scale_face_capacity_2026-08-31.md).
Using `A_F<=pi D^2/4` and `q<=pi D` gives the explicit `Delta_2D^2+O(D)` forms.

The [force-bulk audit](../../reports/target_c_force_bulk_and_correction_audit_2026-09-08.md)
rejects the localization argument formerly used to bound the outside-core population
by `pi D`. That population remains uncontrolled by this argument; no positive lower
bound for `G` is supplied either.

## Exact role in C-II

C42 applies in both C33 phases:

- **near-minimal boundary:** `c_I+e_BB=o(D)`; the C35-C41 noncrossing harmonic-response normal form coexists with an almost-everywhere strict-rhombic planar core;
- **boundary surplus:** no near-minimal assumption is needed; C42 still gives only linear face defect because `q=O(D)`.

This does not close C-II. The force-visible core may omit contact-isolated source points, and a disk-clipped oblique rhombic grid can have quadratic rhombic bulk with linear boundary defect while remaining triangle-free. Therefore a closing theorem must use additional global-minimum-diameter information.

The two shortest transports are:

1. **population/area-gap closure:** control the omitted isolated source population
   and prove a sufficient lower bound on `G` (or an equivalent strict-packing charge),
   retaining all population and boundary terms; or
2. **response/rhombus incompatibility:** combine C41's strict response diameter
   defect and C35-C40's noncrossing harmonic structure with the exact unit-rhombic
   bulk to force either a unit triangle or a strict sub-`D` motion/container.

Do not import Target B train or shell conclusions without proving their hypotheses on this C42 core.
