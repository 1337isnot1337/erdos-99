<!-- theorem-state: {"artifact_id":"ART-878A9DB9BEF3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — post-ZF diameter-matching branch externalization

**Date:** 2026-09-09  
**Repository base:** `58420d2f13ba3f75ea943d8b60e90b2984287081`  
**Run type:** exact branch collapse / asymptotic population theorem  
**Target:** Target C C-II after ZF, ZE/ZT, and OP  
**Depends on:** report-level ZF/ZE/ZT, DT, C42/C51, OP, canonical diameter-thrackle structure, global lattice/Oler asymptotics  
**External web search:** not used  
**Computation:** arithmetic only for the displayed decimal  

## LEVEL I STATUS

`STILL OPEN`

Assume the audited/report-level post-ZF stack and suppose the **full actual diameter graph is a perfect matching** on the loaded terminal set `B_+`, `q=|B_+|`. Then the exact terminal ledger forces the positive contact core into an extreme topology:

- its outer contact walk is exactly the convex force-hull cycle;
- every force-hull side is a unit contact;
- every bounded contact face is a strict unit rhombus;
- there are no bridges, outer indentations, or exceptional bounded faces;
- the train count equals the diameter-edge count: `T=h=q/2`;
- all contact-isolated source points lie outside the force hull.

Moreover the pure rhombic core can contain at most

\[
\frac{\pi^2}{16}D^2+O(D)
\]

vertices. Since a global minimum-diameter source has

\[
\frac n{D^2}\to\Delta:=\frac\pi{2\sqrt3},
\]

every unbounded matching-branch counterexample would therefore require at least

\[
\boxed{
\left(\frac\pi{2\sqrt3}-\frac{\pi^2}{16}\right)D^2-o(D^2)
=0.2900494070\ldots D^2-o(D^2)
}
\tag{MB.1}
\]

contact-isolated source points **outside** the force hull.

Thus a perfect-matching diameter graph is no longer a diffuse topology. It is an extreme pure-rhombic core surrounded by a quantitatively macroscopic external rattler shell.

---

## 1. Post-ZF exact currencies

Use the notation of the exact defect-ledger report:

\[
d_H=q-h,
\qquad
s_Z=e+h-(2v-2),
\]

and

\[
x_B=b-q,
\qquad
g_F=\sum_{F\text{ exceptional}}(\deg F-5),
\]

where `b` is the outer contact-face boundary-walk length and `f` is the number of bounded nonquadrilateral contact faces.

ZT proves

\[
\boxed{
q=x_B+f+g_F+2d_H+2s_Z,
}
\tag{1.1}
\]

with every term on the right nonnegative.

If the full diameter graph is a perfect matching, then

\[
h=\frac q2,
\qquad
d_H=q-h=\frac q2.
\tag{1.2}
\]

Substitute into (1.1):

\[
q=x_B+f+g_F+q+2s_Z.
\]

Therefore

\[
\boxed{
x_B=f=g_F=s_Z=0.}
\tag{1.3}
\]

In particular

\[
\boxed{b=q,\qquad Q=0.}
\tag{1.4}
\]

---

## 2. The outer contact walk is exactly the unit force-hull cycle

Let

\[
b_1,\ldots,b_q
\]

be the force-hull vertices in cyclic order. C42 puts all of them on the outer contact-face walk.

Partition the outer walk into the `q` consecutive subwalks from a distinguished occurrence of `b_i` to the next distinguished occurrence of `b_{i+1}`. Let their edge counts be `L_i`. Every contact edge has Euclidean length one, so

\[
L_i\ge |b_{i+1}-b_i|.
\tag{2.1}
\]

Unit separation gives

\[
|b_{i+1}-b_i|\ge1.
\tag{2.2}
\]

Summing,

\[
q=b=\sum_iL_i
\ge\sum_i|b_{i+1}-b_i|
=\operatorname{per}(F)
\ge q.
\tag{2.3}
\]

Thus equality holds everywhere. Hence for every `i`,

\[
\boxed{L_i=|b_{i+1}-b_i|=1.}
\tag{2.4}
\]

So each subwalk consists of the single unit contact edge `b_i b_{i+1}`. The outer-face walk is the simple force-hull cycle itself. In particular

\[
\boxed{\operatorname{per}(F)=q.}
\tag{2.5}
\]

There is no bridge excursion or repeated outer visit.

Since `Q=0`, every bounded face is quadrilateral; C51 makes every such face a simple strict convex unit rhombus. A connected plane graph for which every face boundary, including the outer one, is a simple cycle is 2-connected. Therefore the complete positive contact core is a simply connected strict-rhombic disk.

This statement concerns the **positive core**, not necessarily every source point.

---

## 3. Every contact-isolated source point is external

All bounded faces are rhombi. C49 excludes additional source points from every bounded strict-rhombus face.

Alternatively, in OP notation the bounded faces tile the entire force hull because the outer boundary is exactly `partial F`. Thus

\[
A_{bnd}=\operatorname{area}(F),
\qquad H_{OP}=0.
\]

OP gives

\[
Z_{in}\le\frac{2}{\sqrt3}H_{OP}=0.
\]

Therefore

\[
\boxed{
A\setminus V(C)\subseteq\mathbb R^2\setminus F.
}
\tag{3.1}
\]

Every non-core source point in the matching branch is an external C65 rattler.

---

## 4. Exact train count

DT gives

\[
T=\frac{b+Q}{2}+2f.
\]

Using (1.3)-(1.4),

\[
\boxed{T=\frac q2.}
\tag{4.1}
\]

But the diameter graph is a perfect matching, so

\[
\boxed{h=\frac q2=T.}
\tag{4.2}
\]

Thus the matching branch saturates the ZF train/diameter row count exactly.

For a pure rhombic disk let `R` be the number of rhombi. DT's train-crossing graph is simple and triangle-free, has `T` vertices and exactly `R` edges. Mantel therefore gives

\[
\boxed{R\le\frac{T^2}{4}=\frac{q^2}{16}.}
\tag{4.3}
\]

Euler for a pure rhombic disk gives

\[
\boxed{v=R+T+1.}
\tag{4.4}
\]

Hence

\[
\boxed{
v\le\frac{q^2}{16}+\frac q2+1.}
\tag{4.5}
\]

---

## 5. Diameter-scale terminal bounds

Since the force hull is a convex body of diameter `D`, every closed curve containing a diameter pair has length at least `2D`; in particular

\[
\operatorname{per}(F)\ge2D.
\]

Together with (2.5),

\[
\boxed{q\ge2D.}
\tag{5.1}
\]

The ordinary convex perimeter-diameter inequality gives

\[
q=\operatorname{per}(F)\le\pi D.
\tag{5.2}
\]

Thus the matching branch automatically strengthens the general post-ZF terminal lower bound `q>=D` to

\[
2D\le q\le\pi D.
\]

For the core-size upper bound we need only the upper endpoint. Insert (5.2) into (4.5):

\[
\boxed{
\limsup\frac v{D^2}
\le\frac{\pi^2}{16}
=0.6168502750\ldots.
}
\tag{5.3}
\]

---

## 6. Quadratic external population is mandatory

The canonical strict translated-lattice upper bound and finite Oler lower bound imply for global minimizers

\[
\boxed{
\frac n{D^2}\to
\Delta:=\frac\pi{2\sqrt3}
=0.9068996821\ldots.
}
\tag{6.1}
\]

Let

\[
Z_{ext}:=n-v.
\]

By Section 3 all these non-core points lie outside `F`. Equations (5.3)-(6.1) give

\[
\begin{aligned}
\liminf\frac{Z_{ext}}{D^2}
&\ge
\Delta-\frac{\pi^2}{16}\\
&=
\boxed{
\frac\pi{2\sqrt3}-\frac{\pi^2}{16}
=0.2900494070\ldots>0.
}
\end{aligned}
\tag{6.2}
\]

This proves MB.1.

The constant is deliberately conservative: it uses only Mantel and `q<=pi D`, not rhombus-area slack, reciprocal geometry, or the detailed diameter matching.

---

## 7. Relation to ZB

ZB excludes an unbounded sequence when the **complete source contact graph** is a pure simply connected strict-rhombic disk. MB does not silently apply ZB to the present source, because the matching branch may have external contact-isolated source points.

What MB proves instead is the exact alternative:

```text
full diameter graph is a perfect matching
    -> positive core is a pure strict-rhombic disk
    -> no internal rattlers
    -> at least 0.290049... D^2 - o(D^2) external rattlers.
```

Therefore any extension of the ZB exposed-hull theorem that tolerates an external population of the type above would immediately kill the matching branch. Until such an extension is proved, MB is a branch reduction rather than a closure.

---

## 8. Exact regression against a tempting shortcut

It is false that an equilateral convex polygon whose diameter graph is a perfect matching must be centrally symmetric or regular.

For an exact six-vertex family, choose

\[
\frac\pi6<a<\frac\pi2,
\qquad b=\frac{2\pi}{3}-a.
\]

Let the six successive unit edge directions be

\[
0,\ a,\ \frac{2\pi}{3},\ \frac{2\pi}{3}+a,\ rac{4\pi}{3},\ rac{4\pi}{3}+a.
\tag{8.1}
\]

The turning gaps alternate `a,b,a,b,a,b`, all strictly between zero and `pi`, and the two triples of edge vectors separately sum to zero. Hence these edges form a strict convex equilateral hexagon.

The two-step diagonal lengths alternate

\[
2\cos\frac a2,
\qquad
2\cos\frac b2.
\tag{8.2}
\]

Every opposite-index three-step diagonal has the same length

\[
D(a)=2\cos\frac{|a-\pi/3|}{2}.
\tag{8.3}
\]

For

\[
\frac\pi6<a<\frac\pi2,
\]

both inequalities

\[
|a-\pi/3|<a,
\qquad
|a-\pi/3|<b
\]

hold. Since cosine decreases on the relevant interval, (8.3) is strictly larger than both values in (8.2). Thus the full diameter graph is exactly the three opposite-index chords, a perfect crossing matching. Every nonedge length is greater than one, so the contact graph is exactly the six-cycle.

The polygon is centrally symmetric iff opposite edge vectors are negatives. For the first and fourth edge this requires

\[
\frac{2\pi}{3}+a=\pi,
\]

i.e.

\[
a=\frac\pi3.
\]

Therefore every parameter

\[
a\in(\pi/6,\pi/2)\setminus\{\pi/3\}
\]

gives a strict convex unit-edge polygon with a perfect-matching diameter graph that is **not** centrally symmetric.

This family is not claimed to be a large global minimizer or a pure rhombic disk. Its role is to kill any attempted convex-geometry shortcut from `H` matching directly to central symmetry/cyclicity. The post-ZF contact/topology ledger is essential.

---

## 9. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| matching `H` forces `x_B=f=g_F=s_Z=0` | proved | direct ZT substitution |
| outer walk equals unit force-hull cycle | proved | exact length equality between `b`, hull sides, and unit separation |
| positive core is pure strict-rhombic disk | proved | C51 plus zero exceptional defect and simple outer cycle |
| all rattlers are external | proved | pure disk/OP with `H_OP=0` |
| `T=h=q/2` | proved | DT and matching definition |
| `v<=q^2/16+q/2+1` | proved | Mantel on the train-crossing graph plus Euler |
| external density lower bound MB.1 | proved asymptotically | global `n/D^2 -> Delta` and `q<=pi D` |
| matching alone forces central symmetry | rejected | exact six-vertex family in Section 8 |
| matching branch impossible | not proved | quadratic external shell remains logically possible |

---

## 10. Promotion recommendation

**Hold as report.**

The branch reduction depends on report-level ZF/ZE/ZT/OP. If that stack is promoted after independent audit, MB should be folded into the post-ZF Target C frontier as the exact perfect-matching subcase.

---

## 11. Next theorem

The matching branch now asks for a quantitatively specific external theorem:

> **Matching-shell exclusion.** A triangle-free global minimum-diameter source cannot consist of a post-ZF pure-rhombic matching core together with at least
> \[
> \left(\frac\pi{2\sqrt3}-\frac{\pi^2}{16}-o(1)\right)D^2
> \]
> fully inactive source points outside that core's convex hull.

Potential inputs unavailable to generic convex geometry are:

1. the core outer cycle has unit side lengths and diameter `D`;
2. every core hull vertex has exactly one actual diameter partner;
3. all diameter matching chords pairwise cross;
4. `T=h=q/2` and the mixed rigidity framework has exactly one row dependence (`s_Z=0`);
5. RA can move the external population to first contacts in another same-diameter triangle-free representative, but those contacts cannot be assumed KKT-positive.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Matching-branch theorem MB:
If the full actual diameter graph H is a perfect matching, then h=q/2 and
d_H=q/2. The post-ZF terminal partition
    q=x_B+f+g_F+2d_H+2s_Z
forces
    x_B=f=g_F=s_Z=0.
Hence
    b=q=per(F),
every hull side is a unit contact, the outer contact walk is exactly the
convex hull cycle, every bounded contact face is a strict unit rhombus,
and all non-core source points lie outside F.

DT gives
    T=q/2=h.
The train crossing graph has R rhombi and is triangle-free, so
    R<=T^2/4=q^2/16,
    v=R+T+1<=q^2/16+q/2+1.
Since q<=pi D and n/D^2->pi/(2sqrt3),
    liminf (n-v)/D^2
      >= pi/(2sqrt3)-pi^2/16
      =0.2900494070... .
Thus every matching-branch survivor requires a quadratic external rattler shell.

Do not shortcut matching -> central symmetry: Section 8 gives an exact
one-parameter equilateral convex hexagon family with perfect matching diameter
graph and no central symmetry except at a=pi/3.
```
