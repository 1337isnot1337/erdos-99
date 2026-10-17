> Generated reading edition · [exact source](../../research/target_c_section121_local_return_oler_bridge.md) · source SHA-256 `220f6779896198468a3b864689b96b5a6f2a2caae95442aac4f35fd7f02024b8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Section 121: local harmonic return-to-Oler bridge

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** corrected proof-only structural candidate stacked on Section 120; independent hostile audit required.

Section 120 keeps the exact direction-sensitive signed-return currency of one harmonic
carrier. Canonical Section 82 supplies the exact local face ledger. This section gives
a finite conversion from that return currency to geometric Oler area inside the same
convex attachment cell.

A previous draft incorrectly claimed that the Type-II local filling estimate
`G_loc=o(D^2)` makes the Section-121 moment error negligible after division by `d^2`.
That is false: the finite moment inequality contains `d G_loc`, so the normalized error
is `G_loc/d`, not `G_loc/d^2`. The asymptotic moment statement formerly numbered
(121.18) is withdrawn. The finite inequalities below are unaffected.

Fix one unloaded harmonic component with induced positive-contact graph `H` and convex
attachment polygon

$$
P=\operatorname{conv}(A).
$$

Use the canonical Section-82 notation:

- `L` = occurrence-counted outer-face walk length of `H`;
- `f` = number of bounded nonquadrilateral faces;
- `Q=sum(deg F-4)` over bounded faces;
- `P_exc=4f+Q` = total perimeter of bounded nonquadrilateral faces;
- `A_4` = total Euclidean area of the bounded strict-rhombus faces of `H`;
- `p=per(P)`;
- `d=diam(P)`.

Put

$$
G_{loc}:=\operatorname{area}(P)-A_4,
\qquad
c_0={\sqrt3\over4}.
$$

Then

$$
\boxed{
G_{loc}
\ge
c_0\bigl[(L-p)+(2f+Q)\bigr].
}
\tag{121.1}
$$

Since `L>=p` and `Q>=f`,

$$
\boxed{
G_{loc}
\ge
{3c_0\over5}
\bigl(L+P_{exc}-p\bigr).
}
\tag{121.2}
$$

Now assume Section 120. For any two distinct attachment vertices `p_-,p_+` occurring
on the outer walk, let

$$
r=|p_+-p_-|,
\qquad
q={p_+-p_-\over r},
$$

and let

$$
M(q)=
\sum_R\operatorname{area}(R)
\bigl(|q\cdot u_R|+|q\cdot v_R|\bigr).
$$

Then

$$
\boxed{
G_{loc}
\ge
{3c_0\over5}
\left[
2r-p+{4A_4-2M(q)\over d}
\right]_+ .
}
\tag{121.3}
$$

Equivalently,

$$
\boxed{
M(q)
\ge
2A_4
-{d\over2}
\left[
 p-2r+{5G_{loc}\over3c_0}
\right].
}
\tag{121.4}
$$

Equations (121.1)--(121.4) are finite statements on the actual harmonic carrier. They
do not require the carrier to be a standalone global minimizer and do not delete or
reclassify any source point.

---

## 121.1 Convexification of the local outer face

Canonical Section 82 proves that every unloaded vertex lies in `int(P)` and that adding
every missing side of `P` to `H` produces a 2-connected plane graph `Hhat` whose
bounded faces are convex.

Let

- `a=|A|` be the number of attachment vertices;
- `c_partial` be the number of sides of `P` already present as loaded-loaded contact
  edges;
- `h=a-c_partial` be the number of missing polygon sides added in forming `Hhat`;
- `L_add` be their total Euclidean length.

Every pre-existing polygon-side contact has unit length, so

$$
\boxed{p=c_{partial}+L_{add}.}
\tag{121.5}
$$

The `h` added sides split the old outer face into `h` convex pockets. For a new pocket
`C`, let `k_C`, `P_C`, and `A_C` be its boundary-edge count, Euclidean perimeter, and
area. Euler/face-incidence subtraction gives

$$
\boxed{
\sum_C k_C=L+2h-a,
}
\tag{121.6}
$$

and Euclidean perimeter incidence gives

$$
\boxed{
\sum_C P_C=L+2L_{add}-p.
}
\tag{121.7}
$$

Each pocket boundary vertex is a source point, hence the boundary vertices are
unit-separated. Oler gives

$$
A_C\ge a_0(k_C-1)-c_0P_C,
\qquad a_0={\sqrt3\over2}=2c_0.
\tag{121.8}
$$

Summing and using (121.5)--(121.7),

$$
\boxed{
H_{out}:=\sum_CA_C\ge c_0(L-p).
}
\tag{121.9}
$$

The incidence identities count old outer-face occurrences with multiplicity, so
bridges/repeated vertices cause no loss.

## 121.2 Bounded nonquadrilateral faces

Every old bounded face remains a bounded face of `Hhat`, and Section 82 proves it is
convex. A nonquadrilateral face of degree `m=4+r`, `r>=1`, is an equilateral polygon
with unit-separated boundary vertices. Oler on those vertices yields

$$
\operatorname{area}(F)
\ge a_0(m-1)-c_0m
=c_0(m-2)
=c_0(2+r).
\tag{121.10}
$$

Summing over all `f` nonquadrilateral bounded faces and using `sum r=Q`,

$$
\boxed{
A_{exc}\ge c_0(2f+Q).
}
\tag{121.11}
$$

The strict rhombi, bounded nonquadrilateral faces, and new outer pockets tile `P` up
to common boundaries. Hence

$$
G_{loc}=A_{exc}+H_{out},
\tag{121.12}
$$

which proves (121.1).

## 121.3 Three-fifths conversion

Set

$$
H=(L-p)+(2f+Q),
\qquad
J=(L-p)+(4f+Q)=L+P_{exc}-p.
$$

The outer walk has convex hull `P`, so `L>=p`. Also each nonquadrilateral face
contributes at least one to `Q`, so `Q>=f`. Therefore

$$
5H-3J=2\bigl[(L-p)+(Q-f)\bigr]\ge0,
$$

and

$$
\boxed{H\ge{3\over5}J.}
\tag{121.13}
$$

Combining with (121.1) proves (121.2).

## 121.4 Insert the anisotropic Section-120 return

Section 120 gives

$$
d\bigl(L+P_{exc}-2r\bigr)
\ge4A_4-2M(q).
\tag{121.14}
$$

Since `J=L+P_exc-p`,

$$
J\ge2r-p+{4A_4-2M(q)\over d}.
$$

Also `J>=0`. Inserting this into (121.2) proves (121.3). Conversely, (121.2) gives
`J<=5G_loc/(3c_0)`; substituting that upper bound into (121.14) proves (121.4).

## 121.5 Correct asymptotic interpretation

Suppose `d=Theta(D)`. Dividing (121.4) by `d^2` gives

$$
{M(q)\over d^2}
\ge
2{A_4\over d^2}
+{r\over d}
-{p\over2d}
-{5\over6c_0}{G_{loc}\over d}.
\tag{121.15}
$$

The last term is `G_loc/d`, not `G_loc/d^2`.

Canonical Section 83 supplies only local filling defect `G_loc=o(D^2)` for almost all
macroscopic-cell area. With `d=Theta(D)`, this does **not** imply
`G_loc/d=o(1)`. Therefore Section 83 does not by itself turn (121.15) into a
nontrivial limiting moment constraint.

A sufficient additional hypothesis would be the genuinely boundary-order statement

$$
G_{loc}=o(d),
\tag{121.16}
$$

or any explicit `G_loc=O(d)` bound strong enough for the desired constants. No such
bound is proved here.

This correction is binding: the former inference

```text
G_loc=o(D^2) -> normalized moment error o(1)
```

is rejected.

## 121.6 What remains useful

The finite bridge (121.1)--(121.4) is still new. It converts local outer-walk/defect
interface directly into Oler area and, when a genuinely boundary-order local filling
estimate is available, converts Section-120 signed return into a train-direction
moment constraint.

Without such a boundary-order local area estimate, the canonical use of Section 121
is diagnostic rather than closing: it identifies exactly what must be strengthened in
the local filling theorem before anisotropic return can constrain the train-direction
distribution.

**Theorem state:** unchanged pending independent hostile audit/promotion.
