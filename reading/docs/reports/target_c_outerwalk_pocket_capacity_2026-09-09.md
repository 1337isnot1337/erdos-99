> Generated reading edition · [exact source](../../../docs/reports/target_c_outerwalk_pocket_capacity_2026-09-09.md) · source SHA-256 `cf5b9fc843bbdb11c2a32c4b3fe2c7c5a9d2eea59ba570933342158f04d433a4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BC0ED2838082","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact outer-walk pocket-capacity theorem

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG/DC/DS  
**Run type:** exact outer-pocket geometry / currency coupling  
**Target:** post-ZF outer-walk branch  
**Depends on:** OP hull augmentation and pocket identities, post-ZF notation `x_B=b-q`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The post-ZF currency

$$
x_B=b-q
$$

measures the excess length of the outer contact-face walk over one edge occurrence per loaded hull vertex. DG shows this currency is linear unless the force hull approaches the maximum-perimeter endpoint.

This report gives `x_B` a direct geometric meaning. The total area of the portions of the outer contact face lying inside the force hull is at most quadratic in `x_B`:

$$
\boxed{
H_{out}\le\frac4\pi x_B^2.
}
$$

OP then gives the same quadratic control on the contact-isolated source population in those pockets:

$$
\boxed{
Z_{in}\le\frac8{\pi\sqrt3}x_B^2.
}
$$

Thus a sublinear outer-walk currency cannot hide a quadratic internal outer-face cavity or population. More generally, any theorem forcing a macroscopic outer cavity immediately forces an explicit linear lower bound on `x_B`.

---

## 1. OP notation

Let

- `F` be the force hull;
- `q` its loaded hull-vertex count;
- `B=b=q+x_B` the outer contact-face boundary-walk length;
- `a` the number of hull sides missing from the contact graph and therefore added in OP to form the hull-augmented graph;
- `L_add` the total Euclidean length of those added hull sides;
- `P=per(F)`;
- `P_1,...,P_a` the new convex outer pockets cut off by the added hull cycle;
- `L_j=per(P_j)`;
- `H_out=sum_j area(P_j)`.

OP proves exactly

$$
P=(q-a)+L_{add}
\tag{1.1}
$$

and

$$
\boxed{
\sum_{j=1}^a L_j
=B+2L_{add}-P.
}
\tag{1.2}
$$

It also proves that every new pocket is convex and that their total area is precisely the part of the old outer contact face lying inside `F`.

---

## 2. Missing hull sides are paid by outer-walk excess

Partition the outer contact walk into its `q` subwalks between consecutive loaded hull vertices. If their positive integer lengths are

$$
\ell_1,\ldots,\ell_q,
$$

then

$$
\sum_i(\ell_i-1)=x_B.
\tag{2.1}
$$

Every interval with `ell_i=1` is the straight unit contact edge joining the two consecutive hull vertices, hence that hull side is already present in the contact graph.

Therefore every missing hull side must correspond to an interval with `ell_i>=2`. There are at most `x_B` such intervals, because each consumes at least one unit of the sum in (2.1).

### Lemma OW.1

$$
\boxed{a\le x_B.}
\tag{2.2}
$$

This is finite and integer exact.

---

## 3. Total outer-pocket perimeter is at most `4x_B`

From (1.1),

$$
L_{add}=P-q+a.
\tag{3.1}
$$

Insert this and `B=q+x_B` into OP.1.2:

$$
\begin{aligned}
\sum_jL_j
&=q+x_B+2(P-q+a)-P\\
&=x_B+(P-q)+2a.
\end{aligned}
\tag{3.2}
$$

The loaded hull vertices are unit-separated, so every hull side has length at least one and hence

$$
P\ge q.
\tag{3.3}
$$

OP's closed-walk perimeter theorem gives

$$
P\le B=q+x_B,
$$

so

$$
0\le P-q\le x_B.
\tag{3.4}
$$

Together with `a<=x_B`, (3.2) yields:

### Theorem OW.2 — pocket-perimeter capacity

$$
\boxed{
\sum_jL_j\le4x_B.
}
\tag{3.5}
$$

The estimate deliberately retains no `O(D)` term. If the outer walk has little excess, the entire convex pocket boundary has little total length.

---

## 4. Exact quadratic outer-area bound

Each pocket is convex. The planar isoperimetric inequality gives

$$
area(P_j)\le\frac{L_j^2}{4\pi}.
\tag{4.1}
$$

Therefore

$$
H_{out}
=\sum_jarea(P_j)
\le\frac1{4\pi}\sum_jL_j^2
\le\frac1{4\pi}\left(\sum_jL_j\right)^2.
$$

Apply OW.2:

### Theorem OW — exact outer-pocket area capacity

$$
\boxed{
H_{out}
\le\frac4\pi x_B^2.
}
\tag{OW.1}
$$

In particular

$$
x_B=o(D)
\quad\Longrightarrow\quad
H_{out}=o(D^2).
\tag{OW.2}
$$

This strengthens the qualitative outer-pocket collapse used after DG.

---

## 5. Internal outer-face rattlers are quadratically controlled by `x_B`

OP proves

$$
Z_{in}
\le
\frac2{\sqrt3}H_{out}
+\frac{P-B}{2}
\le
\frac2{\sqrt3}H_{out},
\tag{5.1}
$$

because `P<=B`.

Combine with OW.1:

### Corollary OW.3 — population capacity

$$
\boxed{
Z_{in}
\le
\frac8{\pi\sqrt3}x_B^2.
}
\tag{OW.3}
$$

Thus sublinear `x_B` forces a subquadratic invisible population in the internal outer face without any separate force-bulk hypothesis.

---

## 6. Coupling to any macroscopic outer-cavity theorem

Suppose some independent argument proves

$$
H_{out}\ge gD^2
$$

for a constant `g>0` along a subsequence. OW.1 immediately gives

$$
\frac4\pi x_B^2\ge gD^2.
$$

Hence:

### Corollary OW.4

$$
\boxed{
H_{out}\ge gD^2
\quad\Longrightarrow\quad
x_B\ge\frac{\sqrt{\pi g}}2D.
}
\tag{OW.4}
$$

For example, GU's component-gap localization states that a quadratic attachment-cell gap `G>=gD^2` forces either

$$
H_{out}\ge(g/2)D^2
$$

or a giant bounded exceptional face. In its outer-cavity alternative, OW improves this to

$$
\boxed{
x_B\ge\sqrt{\frac{\pi g}{8}}D.}
\tag{6.1}
$$

Thus GU's geometric cavity branch is no longer an independent uncontrolled resource: it is quantitatively paid by the same outer-walk currency that DG controls from diameter directions.

---

## 7. The DG endpoint now has no quadratic outer-face escape

Combine OW with DC.

If

$$
x_B=o(D),
$$

then

- OW gives `H_out=o(D^2)` and `Z_in=o(D^2)`;
- DC gives `Z_ext=o(D^2)`;
- DC/OP give `area(F)/D^2->pi/4`;
- DG gives `q/D->pi`, `h/D>=3pi/5-o(1)`, and `Q+2s_Z>=pi D/5-o(D)`.

Therefore any remaining quadratic source population not lying in the positive contact core must occur in **bounded nonquadrilateral contact faces**. Quadrilateral contact faces cannot contain contact-isolated source points in the C49/C52 decomposition.

This localizes the residual population obstruction much more tightly than the original outer-shell alternative.

---

## 8. Remaining branch

OW does not exclude a bounded convex exceptional face of perimeter `Theta(D)` and area `Theta(D^2)` containing a quadratic isolated population. Such a giant face is an actual surviving regression target.

The next geometric theorem should therefore combine:

1. `x_B=o(D)` near-circular force hull;
2. `H_out=o(D^2)` and `Z_ext=o(D^2)`;
3. almost complete loaded unit-contact boundary;
4. linear `Q+2s_Z`;
5. any quadratic non-core population localized to bounded convex exceptional faces.

A successful bounded-face capacity/stability theorem would close the remaining population escape in this endpoint.

---

## 9. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

OP gives
    sum pocket perimeters = B+2L_add-per(F),
    per(F)=q-a+L_add.
Outer-walk interval counting gives
    a<=x_B,
while
    0<=per(F)-q<=x_B.
Therefore exactly
    sum pocket perimeters
      = x_B+(per(F)-q)+2a
      <=4x_B.

By convex-pocket isoperimetry,
    H_out<=4 x_B^2/pi.
By OP,
    Z_in<=2H_out/sqrt3
        <=8 x_B^2/(pi sqrt3).

Thus x_B=o(D) eliminates quadratic internal outer-face cavity/population.
Any theorem forcing H_out>=gD^2 now forces
    x_B>=sqrt(pi g)/2 * D.

Together with DC, the remaining x_B=o(D) population escape is localized to bounded
convex exceptional faces.
```
