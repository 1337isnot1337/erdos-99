> Generated reading edition · [exact source](../../../docs/reports/target_c_defect_squaregraph_train_inequality_2026-09-09.md) · source SHA-256 `d2be8170874b5bc3842d0ce3fb7090c49668ddf3c413ef616f8a446bc9af1962`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-213080F802E3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — stopped trains give a defect-stable squaregraph inequality

**Date:** 2026-09-09  
**Repository branch:** `research/post-uf-attachment-fill-2026-09-09`  
**Run type:** exact finite train/Mantel theorem and cap-carrier application  
**Target:** TS/SI cap-minimal full-core branch  
**Depends on:** DT stopped-train theorem, Mantel, SI semicircle hull convergence  
**External comparison:** David Eppstein, *Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs*, JGAA 22(3) (2018), Theorem 5. Eppstein proves the exact squaregraph maximum `floor(2n-2sqrt(n))`; the theorem below recovers its leading finite inequality in the zero-defect case but is proved independently from DT and remains valid with exceptional faces.  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

The two TS half-disk carriers need not be squaregraphs: they may contain exceptional bounded faces. The exact stopped-train theorem nevertheless extends the squaregraph edge mechanism through arbitrary defect faces.

Let `G` be any finite connected straight-line unit-contact graph of a unit-separated triangle-free point set. Write

- `n` for vertices;
- `R` for bounded quadrilateral faces;
- `f` for bounded nonquadrilateral faces;
- `k` for the outer-face boundary-walk length, bridges counted twice;
- `Q=sum_F(deg F-4)` over the `f` exceptional bounded faces;
- `T` for the DT stopped-train count.

Then

$$
\boxed{
k+Q+4f\ge4\sqrt{n+f}-4.}
\tag{DS.1}
$$

Equivalently,

$$
\boxed{
T\ge2\sqrt{n+f}-2.}
\tag{DS.2}
$$

This is exact and finite. It uses no global optimality, KKT weight, convex-hull saturation, or squaregraph hypothesis.

For one of the two TS semicircle carriers `I_i`, with internal Eppstein slack

$$
r_i=2n_i-\delta_i-2-e_i,
$$

DS combines with the semicircle perimeter to give the asymptotic two-sided lower envelope

$$
\boxed{
\frac{r_i}{D}
\ge
\max\left\{
 a+\frac{Q_i}{2D},
 b-\frac{2f_i}{D}
\right\}-o(1),
}
\tag{DS.3}
$$

where

$$
a:=\frac\pi4-\frac12=0.2853981633\ldots,
\qquad
b:=\sqrt{\frac\pi{\sqrt3}}-1=0.3467736871\ldots .
$$

Since `f_i<=Q_i`, a defect-only version is

$$
\boxed{
\frac{r_i}{D}
\ge
\max\left\{
 a+\frac{Q_i}{2D},
 b-rac{2Q_i}{D}
\right\}-o(1).
}
\tag{DS.4}

$$

The minimum of the right side occurs at

$$
\frac{Q_i}{D}
=\frac25(b-a)
=0.0245502094\ldots,
$$

and equals

$$
\boxed{
\frac{4a+b}{5}
=0.2976732681\ldots .
}
\tag{DS.5}

$$

Thus even after allowing the worst possible amount of exceptional-face degradation, each TS carrier pays at least `0.297673D` of internal Eppstein slack by the combined train/perimeter mechanism. More importantly, DS.3 retains the actual variables `f_i,Q_i`, which gives strict improvement in the near-squaregraph phase.

---

## 1. DT identities

DT constructs train paths by passing through opposite edges of every bounded rhombus and stopping at the outer face or a nonquadrilateral face. It proves

$$
\boxed{
T=e-2R=\frac{k+Q}{2}+2f.
}
\tag{1.1}
$$

The train-crossing graph is simple and triangle-free, has `T` vertices, and has exactly `R` edges. Therefore Mantel gives

$$
\boxed{R\le\frac{T^2}{4}.}
\tag{1.2}
$$

Euler and the DT count also give

$$
\boxed{R=n+f-T-1.}
\tag{1.3}
$$

For completeness, substitute `e=2R+T` from (1.1) into

$$
n-e+(R+f)=1
$$

for the connected plane graph, obtaining (1.3).

---

## 2. Proof of the defect-squaregraph inequality

Combine (1.2) and (1.3):

$$
n+f-T-1\le\frac{T^2}{4}.
$$

Multiply by four and complete the square:

$$
4n+4f-4T-4\le T^2,
$$

hence

$$
(T+2)^2\ge4(n+f).
$$

Since `T>=0`,

$$
T\ge2\sqrt{n+f}-2.
$$

This proves DS.2. Insert the exact endpoint count

$$
2T=k+Q+4f
$$

to obtain

$$
k+Q+4f\ge4\sqrt{n+f}-4,
$$

proving DS.1.

The proof is exactly the squaregraph train/Mantel mechanism, but exceptional faces are retained as stopped-train endpoints rather than discarded.

---

## 3. Zero-defect case and Eppstein's squaregraph theorem

If

$$
f=Q=0,
$$

then every bounded face is a strict unit rhombus. In the Target C positive-contact setting, every interior vertex has degree at least four: C26 allows degrees `3,4,5`, but degree three is impossible when all three incident faces are rhombi. Indeed both diagonals of a unit-contact rhombus exceed one, so every rhombus angle lies strictly between `pi/3` and `2pi/3`. Three incident rhombus angles at an interior degree-three vertex would each be strictly below `2pi/3` and could not sum to `2pi`.

Thus the zero-defect internal graph is a squaregraph in Eppstein's sense: all bounded faces are quadrilaterals and all vertices not on the outer face have degree at least four.

DS.1 reduces to

$$
k\ge4\sqrt n-4.
$$

Together with

$$
e=2n-2-k/2,
$$

this gives

$$
e\le2n-2\sqrt n.
$$

Eppstein's Theorem 5 sharpens the integer bookkeeping to the exact maximum

$$
\left\lfloor2n-2\sqrt n\right\rfloor.
$$

The external theorem is not needed for DS.1; it confirms that the zero-defect endpoint is the correct squaregraph scale.

---

## 4. Apply to one TS semicircle carrier

Under the full-core cap-minimal TS hypotheses,

$$
\frac{n_i}{D^2}\to\frac\Delta2,
\qquad
\frac{\delta_i}{D}\to1,
\qquad
\Delta=\frac\pi{2\sqrt3}.
\tag{4.1}
$$

SI proves that the internal convex hull tends to a semicircle and therefore its internal outer walk obeys

$$
\frac{k_i}{D}\ge1+\frac\pi2-o(1).
\tag{4.2}
$$

The exact local slack identity is

$$
\boxed{
r_i=\frac{k_i+Q_i}{2}-\delta_i.}
\tag{4.3}
$$

Using (4.2) and `delta_i/D->1` gives

$$
\boxed{
\frac{r_i}{D}
\ge
\left(\frac\pi4-\frac12\right)
+rac{Q_i}{2D}
-o(1),
}
\tag{4.4}
$$

which is the first branch in DS.3.

Alternatively, from (1.1),

$$
r_i=T_i-2f_i-\delta_i.
\tag{4.5}
$$

DS.2 and (4.1) give

$$
\begin{aligned}
\frac{r_i}{D}
&\ge
\frac{2\sqrt{n_i+f_i}-2}{D}
-rac{2f_i}{D}
-rac{\delta_i}{D}\\
&=
\sqrt{\frac\pi{\sqrt3}}-1
-rac{2f_i}{D}
-o(1),
\end{aligned}
$$

because `f_i=O(D)` in the post-ZF face budget and therefore `sqrt(n_i+f_i)/D -> sqrt(Delta/2)`. This is the second branch of DS.3.

Since every exceptional face contributes at least one to `Q_i`,

$$
f_i\le Q_i,
$$

and DS.4 follows.

---

## 5. Optimize the defect-only envelope

Put

$$
x:=Q_i/D\ge0.
$$

The two affine lower bounds are

$$
a+x/2
$$

and

$$
b-2x.
$$

They are equal when

$$
\frac52x=b-a,
$$

so

$$
\boxed{x_*=\frac25(b-a).}
\tag{5.1}
$$

At this crossover,

$$
a+x_*/2
=a+\frac15(b-a)
=\boxed{\frac{4a+b}{5}}.
\tag{5.2}
$$

This proves DS.5.

Numerically,

$$
b-a=0.06137552369\ldots,
$$

$$
x_*=0.02455020948\ldots,
$$

and

$$
(4a+b)/5=0.2976732681\ldots .
$$

---

## 6. Interface consequence in the low-internal-defect phase

LI proves the baseline loaded-interface defect

$$
Q_B\ge(2-o(1))D.
$$

DS makes this strict whenever the two giant carriers have too little internal face defect.

Write

$$
x_i:=Q_i/D.
$$

Compared with SI, the extra per-carrier slack is

$$
\boxed{
\varepsilon_i
:=
\left[b-a-\frac52x_i\right]_+.
}
\tag{6.1}
$$

Indeed DS.4 says

$$
r_i
\ge
\left(a+\frac{x_i}{2}+\varepsilon_i-o(1)\right)D.
$$

Repeating the LI/NBd/ZU/ZT calculation with this extra nonnegative slack retained gives

$$
\boxed{
\frac{Q_B}{D}
\ge
2+2(\varepsilon_1+\varepsilon_2)-o(1).
}
\tag{6.2}
$$

In particular, if

$$
Q_1+Q_2=o(D),
$$

then

$$
\boxed{
Q_B
\ge
\left[
2+4(b-a)-o(1)
\right]D
}
\tag{6.3}
$$

with

$$
2+4(b-a)
=2.2455020947\ldots .
$$

Thus an almost-squaregraph pair of half-disk carriers forces more than `2.2455D` face defect onto the loaded interface, not merely `2D`.

This is not yet contradictory; it is a quantitative phase separation for the remaining interface theorem.

---

## 7. Binding regression

A rhombic grid clipped to a large semicircle is the correct zero-defect local regression. Its contact graph is a squaregraph, its point density can approach the triangular packing density by taking the rhombus angle to `pi/3` from above, and its outer combinatorial boundary exceeds the Euclidean semicircle perimeter by the squaregraph boundary term captured by DS.

Therefore the improvement in DS is real but cannot be replaced by a claim that high density plus no triangles forces a fixed positive area loss. Near-60-degree rhombic grids remain asymptotically dense.

Exceptional pentagons can break trains with arbitrarily small local Oler area excess, so the degradation term involving `f_i` is also structurally necessary. DS retains that currency explicitly.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `T>=2sqrt(n+f)-2` | proved | Euler + DT + Mantel |
| DS.1 | proved | exact DT endpoint identity |
| zero-defect graph is squaregraph in Target C setting | proved | C26 + strict rhombus angle sum |
| DS.3 semicircle-carrier envelope | proved | SI perimeter + DS train bound |
| universal per-carrier `0.297673D` slack | proved | one-variable minimization |
| low-internal-defect interface improvement | proved | retain DS excess in LI ledger |
| Level I | still open | interface can still carry the stronger linear defect |

---

## 9. Next target

The remaining cap-minimal full-core phase now splits quantitatively:

1. **near-squaregraph carriers:** `Q_i/D < 0.02455...` on one or both giants, which forces an extra loaded-interface defect through DS.6;
2. **internally defective carriers:** `Q_i=Omega(D)`, which already consumes the SI/NBd slack directly.

The next theorem should bound the capacity of the loaded interface as a function of the carrier train-end defect. A natural exact quantity is the number of stopped train ends from the two giant components that terminate on loaded-interface faces. Those endpoints are simultaneously controlled by `f_i,Q_i` on the inside and by the one-slot loaded boundary on the outside.

This is more specific than a generic face-area estimate and directly links the DS train currency to the LI interface currency.