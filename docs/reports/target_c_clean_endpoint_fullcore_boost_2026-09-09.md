<!-- theorem-state: {"artifact_id":"ART-CBEF0CB23C69","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — one-ended train exposure boosts the near-circle full-core branch

**Date:** 2026-09-09  
**Repository base:** PR #119 after DG/DC/DS/OW/GF/FC  
**Run type:** asymptotic train-direction stability / cross-route strengthening  
**Target:** post-ZF `x_B=o(D)`, `n-v=o(D^2)` branch  
**Depends on:** DT/DE train-direction compactness, NM good-train theorem, DG/DC near-circle endpoint  
**External web search:** not used  
**Computation:** decimal evaluation only; proof is analytic

## LEVEL I STATUS

`STILL OPEN`

DE's exposed-hull theorem uses only the fact that each train has at most two outer occurrences. In the DG near-circle endpoint almost every loaded hull interval is a direct unit-contact hull side, and NM proves that at most two trains can have two such good hull ends. This improves the endpoint-capacity factor from two to one.

For an asymptotically full core this yields

\[
\boxed{
\liminf\frac{T-q}{D}
\ge
2\sqrt{\Delta},
\qquad
\Delta:=\frac\pi{2\sqrt3}.
}
\tag{CE.1}
\]

Numerically

\[
2\sqrt\Delta=1.9046256137\ldots .
\]

Consequently every such survivor satisfies

\[
\boxed{
\liminf\frac fD\ge\sqrt\Delta
=0.9523128069\ldots,
}
\tag{CE.2}
\]

\[
\boxed{
\liminf\frac hD
\ge
\frac{3\pi+2\sqrt\Delta}{5}
=2.2658807149\ldots,
}
\tag{CE.3}
\]

and

\[
\boxed{
\liminf\frac{Q+2s_Z}{D}
\ge
\frac\pi5+\frac45\sqrt\Delta
=1.3901687762\ldots .
}
\tag{CE.4}
\]

This supersedes FC.1-FC.3 in the same branch. The improvement is not an algebraic rearrangement: it uses the one-good-end-per-train geometry that becomes available only after DG/DC.

---

## 1. Full-core train limit

Assume a post-ZF sequence satisfies

\[
x_B=o(D),
\qquad
n-v=o(D^2).
\tag{1.1}
\]

The second hypothesis is the one used by DE/DF. As in DE, let

- `R` be the number of bounded rhombic contact faces;
- `T` the stopped-train count;
- `mu_D` the empirical probability measure of projective train directions.

Then

\[
\frac{R}{D^2}\to\Delta,
\tag{1.2}
\]

the total rhombus area excess is `o(D^2)`, the force hulls scaled by `D` converge to the diameter-one disk, and `T=Theta(D)`.

After taking a subsequence, write

\[
\frac TD\to\tau
\]

and let `mu_D` converge weakly to `mu`. Let

\[
s:=\text{total atomic mass of }\mu.
\tag{1.3}
\]

DE's finite-Mantel argument is unchanged and gives

\[
\boxed{
\frac\Delta{\tau^2}\le\frac{s^2}{4}.
}
\tag{1.4}
\]

Equivalently,

\[
\boxed{
\tau s\ge2\sqrt\Delta.
}
\tag{1.5}
\]

The only point improved below is DE's relation between `s` and the hull-end population.

---

## 2. Almost every hull interval is a good unit side

Partition the outer contact-face walk into its `q` subwalks between consecutive loaded force-hull vertices. Write their positive integer lengths as

\[
\ell_1,\ldots,\ell_q.
\]

Then

\[
\sum_i(\ell_i-1)=x_B=o(D).
\tag{2.1}
\]

Hence all but `o(D)` intervals have length one. Every length-one interval is exactly the straight unit contact joining two consecutive force-hull vertices, so it is a **good hull side** in the terminology of NM.

Thus the number of good hull-side train-end incidences is

\[
\boxed{
q-o(D).
}
\tag{2.2}
\]

DG/DC also gives

\[
\boxed{
q/D\to\pi.
}
\tag{2.3}
\]

---

## 3. At most one good end per train, except twice

NM proves that a train with two good hull-side ends is a good train and that

\[
\boxed{T_{good}\le2.}
\tag{3.1}
\]

Therefore every train contributes at most one good hull endpoint, except that at most two trains contribute one additional good endpoint.

This is the exact finite statement that DE did not have in its general outer-walk setting.

---

## 4. Atomic train directions cannot carry macroscopic good hull population

Fix `epsilon>0`. Choose finitely many atoms of `mu` carrying total mass at least

\[
s-\epsilon.
\]

Let `U_delta` be a union of sufficiently small disjoint projective-direction neighborhoods of those atoms, with `mu`-null boundaries.

A good hull endpoint on a train in `U_delta` is a unit hull side whose projective edge direction lies in `U_delta`.

Because the normalized force hulls converge to the disk, their perimeter measures converge weakly to the nonatomic circular perimeter measure. Each good hull side has length exactly one. Therefore, for fixed chosen atoms,

\[
\#\{\text{good hull sides with direction in }U_\delta\}
=O(\delta D)+o_\delta(D).
\tag{4.1}
\]

In particular, after first taking the sequence limit and then `delta->0`, trains in the selected atomic neighborhoods contribute only `o(D)` good hull endpoints.

The number of trains outside `U_delta` is at most

\[
(1-s+\epsilon+o(1))T.
\tag{4.2}
\]

By NM.3.1, those trains contribute at most one good endpoint each, plus at most two extra endpoints globally.

Combining with (2.2),

\[
q-o(D)
\le
(1-s+\epsilon+o(1))T
+O(\delta D)+o_\delta(D)+2.
\tag{4.3}
\]

Divide by `D`, pass to the sequence limit, then `delta->0`, then `epsilon->0`. Using `q/D->pi`, we obtain the strengthened exposed-hull inequality

\[
\boxed{
\pi\le\tau(1-s).
}
\tag{4.4}
\]

Equivalently,

\[
\boxed{
\tau s\le\tau-\pi.
}
\tag{4.5}
\]

Compare DE's general factor-two relation, which gives only `q/T<=2(1-s)`.

---

## 5. Train excess is at least `2sqrt(Delta)D`

Combine (1.5) and (4.5):

\[
2\sqrt\Delta
\le\tau s
\le\tau-\pi.
\]

Therefore

\[
\boxed{
\tau\ge\pi+2\sqrt\Delta.
}
\tag{5.1}
\]

Since `q/D->pi`, this is exactly

\[
\boxed{
\liminf\frac{T-q}{D}
\ge2\sqrt\Delta.
}
\]

This proves CE.1.

Numerically

\[
\pi+2\sqrt\Delta
=5.0462182673\ldots .
\tag{5.2}
\]

Thus the near-circle full-core survivor requires more than five stopped trains per diameter unit.

---

## 6. Almost one exceptional bounded face per diameter unit

ZE gives the exact identity

\[
2f=(T-q)+d_H+s_Z.
\tag{6.1}
\]

Since `d_H,s_Z>=0`, CE.1 gives immediately

\[
\boxed{
\liminf\frac fD
\ge\sqrt\Delta.
}
\tag{6.2}
\]

This proves CE.2.

The old DF lower bound in a general full-core phase was

\[
f/D\ge\sqrt\Delta-\pi/4
=0.1669146\ldots .
\]

The near-circle good-end theorem raises it to

\[
0.9523128\ldots .
\]

The improvement is large because essentially every train beyond the two clean exceptions must spend at least one endpoint in the defect network.

---

## 7. Diameter-edge density rises to `2.26588...D`

Pass to a subsequence on which

\[
\frac hD\to y,
\qquad
\frac{s_Z}{D}\to\sigma.
\]

Because `q/D->pi`,

\[
\frac{d_H}{D}=\frac{q-h}{D}\to\pi-y.
\tag{7.1}
\]

From (6.1) and CE.1,

\[
\liminf\frac fD
\ge
\sqrt\Delta+\frac{\pi-y+\sigma}{2}.
\tag{7.2}
\]

The exact terminal ledger with `x_B=o(D)` gives

\[
\frac QD
=2y-\pi-2\sigma+o(1).
\tag{7.3}
\]

Every exceptional face contributes at least one unit to `Q`, so `Q>=f`. Hence

\[
2y-\pi-2\sigma
\ge
\sqrt\Delta+\frac{\pi-y+\sigma}{2}.
\tag{7.4}
\]

Multiply by two:

\[
4y-2\pi-4\sigma
\ge
2\sqrt\Delta+\pi-y+\sigma.
\]

Thus

\[
\boxed{
5y\ge3\pi+2\sqrt\Delta+5\sigma.
}
\tag{7.5}
\]

In particular

\[
y\ge\frac{3\pi+2\sqrt\Delta}{5},
\]

proving CE.3.

Numerically

\[
\frac{3\pi+2\sqrt\Delta}{5}
=2.2658807149\ldots .
\]

As before, the retained surplus form is stronger:

\[
\boxed{
\frac hD
\ge
\frac{3\pi+2\sqrt\Delta}{5}
+\frac{s_Z}{D}-o(1).
}
\tag{7.6}
\]

---

## 8. Branching/contact defect rises to `1.39016...D`

Since `q/D->pi`, CE.3 gives

\[
\liminf\frac{2h-q}{D}
\ge
2\frac{3\pi+2\sqrt\Delta}{5}-\pi
=
\frac\pi5+\frac45\sqrt\Delta.
\tag{8.1}
\]

The exact branching identity is

\[
2h-q=x_B+Q+2s_Z.
\]

With `x_B=o(D)`, this proves CE.4.

Numerically

\[
\frac\pi5+\frac45\sqrt\Delta
=1.3901687762\ldots .
\]

---

## 9. Total exceptional-face perimeter

The total exceptional bounded-face perimeter is

\[
K_{exc}=Q+4f.
\tag{9.1}
\]

DT gives exactly

\[
2T=b+K_{exc}.
\tag{9.2}
\]

In the present phase

\[
b=q+x_B=\pi D+o(D).
\]

Using CE.5.1,

\[
\boxed{
\liminf\frac{K_{exc}}D
\ge
\pi+4\sqrt\Delta
=6.9508438810\ldots .
}
\tag{9.3}
\]

Thus the near-circle full-core branch carries nearly seven units of exceptional-face perimeter per diameter unit, despite its force hull itself having perimeter only `pi D+o(D)`.

---

## 10. Why this still does not close Level I

A family of many strict near-triangular pentagonal defects can have arbitrarily small individual Oler surplus. The DP pentagon regression remains binding. A linear number of defect faces and even total defect perimeter `6.95D` do not automatically produce a linear Oler penalty with a coefficient known to exceed the global boundary allowance.

The new theorem changes the remaining target substantially:

```text
near-circle + full core
    -> q ~ pi D direct unit hull sides
    -> T >= (pi+2sqrt(Delta))D
    -> f >= sqrt(Delta)D
    -> h >= 2.2658807 D
    -> Q+2s_Z >= 1.3901688 D
    -> K_exc >= 6.9508439 D.
```

A closing theorem now only needs to show that this much defect perimeter cannot coexist with near-isodiametric/Oler-saturated packing without producing an exact unit triangle or a strict diameter decrease.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

In x_B=o(D), n-v=o(D^2):
- normalized hull -> disk;
- R/D^2->Delta;
- DE still gives Delta/tau^2 <= s_atom^2/4.

New endpoint count:
- q-o(D) hull intervals are good unit sides;
- NM gives at most two trains with two good hull ends;
- trains in neighborhoods of limiting direction atoms supply only o(D) good hull ends;
- every other train supplies at most one good end.
Therefore
    pi <= tau(1-s_atom).
Together with tau*s_atom>=2sqrt(Delta):
    tau>=pi+2sqrt(Delta),
so
    liminf(T-q)/D>=2sqrt(Delta).

Then ZE gives
    f/D>=sqrt(Delta)=0.9523128069... .
Using Q>=f and the exact terminal ledger gives
    h/D>= (3pi+2sqrt(Delta))/5
       =2.2658807149...,
    (Q+2s_Z)/D>=pi/5+4sqrt(Delta)/5
       =1.3901687762... .
Also
    K_exc/D>=pi+4sqrt(Delta)
       =6.9508438810... .
```
