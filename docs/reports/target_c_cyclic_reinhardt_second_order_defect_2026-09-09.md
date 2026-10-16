<!-- theorem-state: {"artifact_id":"ART-774CF2674477","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic Reinhardt ladder defect is bounded explicitly by `d_H`

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RP/MT/SL  
**Run type:** second-order asymptotic extraction from exact DA and polygonal-isoperimetric bounds  
**Target:** complete cyclic primitive endpoint  
**Depends on:** RP `q_R(D)-q=O(D^-2)`, DA exact difference-body lower bound, polygonal isoperimetry  
**External literature:** no new input  
**Computation:** symbolic expansion was used as a check only; proof below is analytic

## LEVEL I STATUS

`STILL OPEN`

RP proves that every cyclic phase lies within `O(D^-2)` in side count of the exact Reinhardt ladder. Keeping the phase parameter `d_H` through the next term gives an explicit coefficient.

Put

\[
\delta:=2\arcsin\frac1{2D},
\qquad
q_R(D):=\frac\pi\delta,
\qquad
s:=q_R(D)-q\ge0,
\qquad
d:=d_H\in\{0,1,2\}.
\tag{1.1}
\]

Then `q_R(D)` is the real side count for which the Reinhardt equality relation

\[
D=\frac1{2\sin(\pi/(2q_R))}
\]

holds exactly. RP gives `s=O(D^-2)=O(delta^2)`.

### Theorem R2 — phase-dependent second-order ladder defect

Every unbounded cyclic survivor sequence satisfies

\[
\boxed{
\limsup_{D\to\infty}
\frac{s}{\delta^2}
\le
\frac{d(d+1)(d+2)}{12}.}
\tag{R2.1}
\]

Since only `d=0,1,2` occur,

\[
\boxed{
\begin{array}{c|c}
 d_H & \displaystyle\limsup D^2\bigl(q_R(D)-q\bigr)\\ \hline
0 & 0,\\[2mm]
1 & \le\frac12,\\[2mm]
2 & \le2.
\end{array}}
\tag{R2.2}
\]

The `d_H=0` phase is already strengthened by RE to exact equality `s=0` for every sufficiently large survivor. The new content is the explicit constants in the two tree phases.

Equivalently, if

\[
D_R(q):=\frac1{2\sin(\pi/(2q))},
\]

then

\[
\boxed{
\limsup D^2\bigl(D-D_R(q)\bigr)
\le
\frac{d(d+1)(d+2)}{12\pi},}
\tag{R2.3}
\]

so in particular

\[
D-D_R(q)
\le
\begin{cases}
(2\pi D^2)^{-1}+o(D^{-2}), & d_H=1,\\
2(\pi D^2)^{-1}+o(D^{-2}), & d_H=2.
\end{cases}
\tag{R2.4}
\]

Thus the one- and two-defect maximal-thrackle shells of MT are forced into an explicit second-order tube around exact Reinhardt equality.

---

## 1. Rewrite the DA lower bound in ladder coordinates

The number of actual diameter directions is

\[
h=q-d
=q_R-s-d
=\frac\pi\delta-(s+d).
\tag{1.2}
\]

DA gives

\[
\operatorname{area}(F-F)
\ge
D^2\left[(h-1)\sin\delta+\sin((h-1)\delta)\right].
\tag{1.3}
\]

Since

\[
(h-1)\delta
=\pi-(s+d+1)\delta,
\]

we can rewrite the lower side exactly as

\[
L
:=
D^2\left[
\left(\frac\pi\delta-s-d-1\right)\sin\delta
+
\sin((s+d+1)\delta)
\right].
\tag{1.4}
\]

This is the useful form: the only deviation from the exact ladder appears through the bounded integer `d` and the small real defect `s`.

---

## 2. Expand the DA lower side

Use

\[
D^2
=\frac1{4\sin^2(\delta/2)}
=\frac1{\delta^2}+\frac1{12}+O(\delta^2),
\tag{2.1}
\]

\[
\sin\delta
=\delta-\frac{\delta^3}{6}+O(\delta^5),
\tag{2.2}
\]

and RP's

\[
s=O(\delta^2).
\tag{2.3}
\]

Let

\[
r:=d+s,
\qquad a:=r+1.
\]

The bracket in (1.4) is

\[
\frac\pi\delta\sin\delta-a\sin\delta+\sin(a\delta).
\]

The first term is

\[
\pi-\frac\pi6\delta^2+O(\delta^4).
\tag{2.4}
\]

For the last two terms,

\[
-a\sin\delta+\sin(a\delta)
=
-\frac{a(a^2-1)}6\delta^3+O(\delta^5).
\tag{2.5}
\]

Because `s=O(delta^2)`, replacing `a=d+1+s` by `d+1` in the cubic coefficient changes (2.5) only by `O(delta^5)`. Hence

\[
-a\sin\delta+\sin(a\delta)
=
-\frac{d(d+1)(d+2)}6\delta^3
+O(\delta^5).
\tag{2.6}
\]

Multiplying (2.4)+(2.6) by (2.1) gives

\[
\boxed{
L
=
\frac\pi{\delta^2}
-\frac\pi{12}
-
A_d\,\delta
+O(\delta^2),}
\tag{2.7}
\]

where

\[
\boxed{A_d:=\frac{d(d+1)(d+2)}6.}
\tag{2.8}
\]

For the actual phases,

\[
A_0=0,\qquad A_1=1,\qquad A_2=4.
\tag{2.9}
\]

---

## 3. Expand the polygonal-isoperimetric upper side

The difference body has at most `2q` sides and perimeter `2q`. Therefore

\[
\operatorname{area}(F-F)
\le
U(q):=\frac{q}{2\tan(\pi/(2q))}.
\tag{3.1}
\]

The standard expansion is

\[
U(q)
=
\frac{q^2}{\pi}-\frac\pi{12}+O(q^{-2}).
\tag{3.2}
\]

Now

\[
q=\frac\pi\delta-s,
\]

so

\[
\frac{q^2}{\pi}
=
\frac\pi{\delta^2}
-
\frac{2s}{\delta}
+
\frac{s^2}{\pi}.
\]

Since `s=O(delta^2)`, the last term is `O(delta^4)` and `q^-2=O(delta^2)`. Hence

\[
\boxed{
U(q)
=
\frac\pi{\delta^2}
-
\frac\pi{12}
-
\frac{2s}{\delta}
+O(\delta^2).}
\tag{3.3}
\]

---

## 4. Compare lower and upper bounds

We have

\[
L\le\operatorname{area}(F-F)\le U(q).
\]

Subtract (2.7) from (3.3):

\[
0
\le
U(q)-L
=
A_d\delta
-
\frac{2s}{\delta}
+O(\delta^2).
\tag{4.1}
\]

Divide by `delta>0`:

\[
0
\le
A_d
-
2\frac{s}{\delta^2}
+O(\delta).
\]

Therefore

\[
\limsup\frac{s}{\delta^2}
\le\frac{A_d}{2}
=
\frac{d(d+1)(d+2)}{12}.
\]

This proves R2.1. Since

\[
D\delta\to1,
\]

R2.2 follows. `square`

---

## 5. Convert side-count defect to diameter defect

The ladder function

\[
q_R(D)=\frac\pi{2\arcsin(1/(2D))}
\]

has derivative

\[
q_R'(D)=\pi+O(D^{-2}).
\tag{5.1}
\]

By definition

\[
q_R(D_R(q))=q,
\qquad
q_R(D)-q=s.
\]

The mean value theorem gives some `xi` between `D_R(q)` and `D` such that

\[
s=q_R'(\xi)\,[D-D_R(q)].
\]

RP already gives `D-D_R(q)=O(D^-2)`, so `xi~D` and

\[
D-D_R(q)
=
\frac{s}{\pi}+o(D^{-2}).
\tag{5.2}
\]

Combining with R2.2 gives R2.3-R2.4. `square`

---

## 6. Interaction with the maximal-thrackle completion MT

MT proves that there is a maximal odd-cycle-plus-leaves convex thrackle `T` containing the full diameter graph and that exactly `d` cycle edges of `T` are missing from `H`, hence have Euclidean length strictly below `D`.

R2 now says the **whole shell** has only

\[
O_d(D^{-2})
\]

room above the exact Reinhardt diameter corresponding to its side count.

This does not yet bound each missing chord deficit `D-|g|`: a short completion chord can in principle coexist with a shell whose perimeter is nearly extremal, and no quantitative Reinhardt stability theorem with the required labeled-edge conclusion has been proved here.

But the target is now numerical rather than qualitative. Any MT-gap theorem of the form

\[
D-D_R(q)
\ge
c\,\Phi(D-|g_1|,\ldots,D-|g_d|)
\]

with a source-independent positive `c` can be combined with R2 immediately.

---

## 7. Power-of-two regression

The R2 scale is not absurdly strong relative to the classical small-polygon literature. Power-of-two constructions of Mossinghoff and Bingane--Audet approach the universal Reinhardt perimeter bound at very high order while using non-Reinhardt diameter skeletons.

Thus one should not infer from R2 alone that `d=0`. The new fact is the combination:

- only one or two maximal-thrackle cycle chords are subdiametral (MT);
- the entire shell diameter excess above the Reinhardt ladder is at most the explicit `d`-dependent `D^-2` scale (R2);
- the shell is a genuine local diameter minimum (SL);
- the complete dense source lies inside the same shell (UFB).

---

## 8. Next theorem

The shortest geometric target is now an **edge-labeled Reinhardt stability lemma**:

> Let an equilateral convex `q`-gon have a maximal convex-thrackle completion in which all but `d<=2` edges have length exactly `D`. Bound the short-edge defects in terms of `D-D_R(q)`.

R2 supplies the right-hand scale explicitly:

\[
D-D_R(q)
\le
\frac{1}{2\pi D^2}+o(D^{-2})
\quad(d=1),
\]

\[
D-D_R(q)
\le
\frac{2}{\pi D^2}+o(D^{-2})
\quad(d=2).
\]

If the missing-edge defect must be appreciably larger in a local equilateral diameter minimum, the tree phases close.

---

## 9. Promotion recommendation

**Hold as report pending independent audit.**

The proof is an explicit expansion of already-audited exact inequalities; no new external theorem is imported.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Let
  delta=2asin(1/(2D)), q_R=pi/delta, s=q_R-q>=0, d=d_H.
RP gives s=O(delta^2).
DA lower with h=q-d becomes exactly
  L=D^2[(pi/delta-s-d-1)sin(delta)+sin((s+d+1)delta)].
Expanding:
  L=pi/delta^2-pi/12-A_d delta+O(delta^2),
  A_d=d(d+1)(d+2)/6.
Polygonal-isoperimetric upper:
  U=q/[2tan(pi/(2q))]
   =pi/delta^2-pi/12-2s/delta+O(delta^2).
Since L<=U,
  0<=A_d delta-2s/delta+O(delta^2),
so
  limsup s/delta^2 <= A_d/2=d(d+1)(d+2)/12.
Thus
  d=1: q_R-q <= (1/2+o(1))/D^2,
  d=2: q_R-q <= (2+o(1))/D^2.
And because q_R'(D)=pi+o(1),
  d=1: D-D_R(q) <= 1/(2pi D^2)+o(D^-2),
  d=2: D-D_R(q) <= 2/(pi D^2)+o(D^-2).

Next: edge-labeled Reinhardt stability for the one/two short MT completion chords.
```
