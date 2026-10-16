<!-- theorem-state: {"artifact_id":"ART-0C48C138C410","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2`: the two cross-tree switches are exact one-defect cells

**Date:** 2026-09-09  
**Repository branch:** `research/post-zf-currency-coupling-2026-09-09`  
**Run type:** exact metric parameterization of the two missing diameter states  
**Target:** cyclic primitive endpoint, `d_H=2`  
**Depends on:** D2/D2S/D2R/SW on this branch; DG/DGE from PR #119; AD/D1 difference-body defect interpretation  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

D2S localizes all projective diameter-direction defect to the two switches between the two diameter-tree direction blocks. D2R says the four shell contacts at the A/B block transitions are the only shell sides not certified by a shared-endpoint diameter pair.

At each cross-tree direction switch, those four transition contacts occur in two opposite pairs. The two diameter edges adjacent to the switch are vertex-disjoint, and the two corresponding cross distances are exactly the two unit transition contacts.

This determines each switch completely up to one scalar angle.

Put

\[
\delta:=2\arcsin\frac1{2D},
\qquad
\Delta_2:=2\arcsin\frac1D,
\qquad
q_R:=\frac\pi\delta,
\qquad
s:=q_R-q.
\]

### Theorem D2C — two exact defect cells

Let `G_1,G_2` be the two cross-tree projective direction gaps in a cyclic `d_H=2` survivor. Then

\[
\boxed{2\delta<G_j\le\Delta_2\qquad(j=1,2).}
\tag{D2C.1}

Define

\[
\boxed{s_j:=\frac{G_j}{\delta}-2.}
\tag{D2C.2}

Then

\[
\boxed{s=s_1+s_2,}
\tag{D2C.3}

and

\[
\boxed{0<s_j\le s_P(D):=\frac{\Delta_2}{\delta}-2.}
\tag{D2C.4}

For each switch exactly one of the following occurs.

### Short cell

If `0<s_j<s_P(D)`, the canonical missing antipodal completion state is a genuine off-circle difference-body vertex. Its length is

\[
\boxed{
L_j
=D\cos\frac{G_j}{2}
+\sqrt{1-D^2\sin^2\frac{G_j}{2}},
\qquad
\sqrt{D^2-1}<L_j<D.
}
\tag{D2C.5}

### Parallel cell

If `s_j=s_P(D)`, equivalently `G_j=\Delta_2`, the off-circle completion state collapses: the two unit transition sides at that switch are parallel and oppositely oriented, the difference body has a length-two merged edge, and

\[
\boxed{L_j=\sqrt{D^2-1}.}
\tag{D2C.6}

Therefore the AD branches are exactly the endpoint/interior cases of the two scalar cells:

```text
S2: 0<s_1,s_2<s_P;
PS: one s_j=s_P and the other lies in (0,s_P);
P2: s_1=s_2=s_P.
```

In P2,

\[
\boxed{s=2s_P(D),}
\]

recovering D1's exact P2 equation

\[
(q-4)\delta+2\Delta_2=\pi.
\]

The gain is not the P2 formula itself. The gain is that **all** true `d_H=2` metric departure from the SSR/Reinhardt selected-support regression is encoded by the two positive scalars `s_1,s_2` and the explicit completion lengths D2C.5.

---

## 1. Local four-endpoint coordinates

Take one cross-tree switch. Let the two consecutive actual diameter edges be

\[
AC,
\qquad
BD,
\]

with oriented diameter vectors

\[
u=C-A,
\qquad
v=D-B,
\qquad
|u|=|v|=D.
\]

Let their acute projective angle be `G`. Put

\[
m_1=\frac{A+C}{2},
\qquad
m_2=\frac{B+D}{2},
\qquad
w=m_2-m_1,
\]

\[
p=\frac{u-v}{2},
\qquad
r=\frac{u+v}{2}.
\]

Then

\[
p\perp r,
\qquad
|p|=D\sin(G/2)=:P,
\qquad
|r|=D\cos(G/2)=:R.
\tag{1.1}

D2's four-block order and D2R's identification of the four exceptional transition shell sides imply that, after the harmless endpoint relabeling used by DG, the two shell transitions belonging to this switch are

\[
AB,
\qquad
CD,
\]

and both have length one:

\[
\boxed{|A-B|=|C-D|=1.}
\tag{1.2}

The vector identities are

\[
A-B=-(w+p),
\qquad
C-D=p-w.
\]

Squaring (1.2) and subtracting gives

\[
w\cdot p=0.
\]

Adding gives

\[
\boxed{|w|^2+P^2=1.}
\tag{1.3}

Because `p perpendicular r`, the midpoint offset `w` is parallel to `r`. Write

\[
W:=|w|=\sqrt{1-D^2\sin^2(G/2)}.
\tag{1.4}

Reality of `W` immediately gives

\[
D\sin(G/2)\le1,
\]

hence

\[
\boxed{G\le2\arcsin(1/D)=\Delta_2.}
\tag{1.5}

DGE gives the strict lower bound for vertex-disjoint consecutive actual diameter directions,

\[
\boxed{G>2\delta.}
\tag{1.6}

This proves D2C.1.

---

## 2. The other cross distance is the missing completion length

The two other cross-difference vectors are

\[
A-D=-(r+w),
\qquad
C-B=r-w.
\]

The source diameter bound determines the sign of `w` relative to `r`: the larger of these two lengths is

\[
R+W,
\]

and must be at most `D`.

At the strict DGE lower endpoint `G=2delta`, the DG equality geometry gives `R+W=D`; for every `G>2delta`, direct monotonicity of

\[
L(G):=D\cos(G/2)+\sqrt{1-D^2\sin^2(G/2)}
\]

on `(2delta,Delta_2]` gives

\[
L(G)<D.
\]

At the upper endpoint,

\[
L(\Delta_2)=D\cos(\Delta_2/2)=\sqrt{D^2-1}.
\]

Hence

\[
\boxed{
\sqrt{D^2-1}\le L(G)<D.
}
\tag{2.1}

For `G<Delta_2`, the midpoint offset has `W>0`; the canonical difference-body boundary therefore has an actual off-circle vertex at radius `L(G)` between the two neighboring circular diameter states. This is exactly the D1 short-antipodal construction, now localized to one of the two D2 switches.

At `G=Delta_2`, `W=0`: the two diameter chords have the same midpoint. Then

\[
A-B=-p,
\qquad
C-D=p,
\]

so the two unit transition sides are parallel and oppositely oriented. In the Minkowski edge merge they become one length-two difference-body edge, exactly the AD parallel-side defect.

This proves D2C.5-D2C.6 and the short/parallel interpretation.

---

## 3. The two local defects add exactly to the Reinhardt ladder defect

D2S proves every within-tree projective gap is exactly `delta`. There are

\[
h=q-2
\]

diameter directions and exactly two cross-tree gaps, so the number of within-tree gaps is

\[
h-2=q-4.
\]

The projective circle sum is therefore

\[
(q-4)\delta+G_1+G_2=\pi.
\tag{3.1}

Since

\[
\pi=(q+s)\delta,
\]

we obtain

\[
G_1+G_2=(s+4)\delta.
\]

Subtract `4delta` and divide by `delta`:

\[
\boxed{s=s_1+s_2.}
\]

Together with D2C.1 this gives D2C.4.

Thus the global second-order Reinhardt deficit has been decomposed into the sum of two nonnegative **local** defect parameters.

---

## 4. Exact recovery of AD's P2/PS/S2 split

A switch is parallel exactly when `G_j=Delta_2`, equivalently

\[
s_j=s_P(D).
\]

Otherwise it contributes one short antipodal pair.

There are exactly two switches, so the number of parallel cells plus the number of short cells is two. Hence the local classification reproduces

\[
d_H=r_{parallel}+a_{short}=2
\]

with no separate global counting argument.

The three possibilities are precisely P2, PS, S2 as displayed in the theorem statement.

In P2 both cells are at the endpoint. Therefore

\[
s=2s_P(D)
=2\left(\frac{\Delta_2}{\delta}-2\right),
\]

which rearranges to

\[
(q-4)\delta+2\Delta_2=\pi.
\]

---

## 5. Small-defect scale

D1 gives

\[
s_P(D)=\frac1{4D^2}+\frac5{64D^4}+O(D^{-6}).
\]

Therefore every true D2 cell satisfies

\[
0<s_j\le\frac1{4D^2}+O(D^{-4}),
\]

and

\[
0<s\le\frac1{2D^2}+O(D^{-4}).
\]

This is sharper and more local than the generic RP statement `s=O(D^-2)`.

The canonical missing completion chord deficit is correspondingly second-order/transition-scale: for `s_j downarrow0`, D2C.5 tends to `D`, while at the parallel endpoint it reaches only

\[
D-\sqrt{D^2-1}=\frac1{2D}+O(D^{-3}).
\]

No uniform positive gap from `D` is available, consistent with SSR.

---

## 6. Relation to the staircase words

SW proves that everything away from the two switches is encoded by two exact binary staircase words. D2C now shows that everything **at** the switches is encoded by two scalar numbers `s_1,s_2` satisfying one sum equation.

Thus the complete cyclic D2 shell has the finite normal form

```text
staircase word w_A;
staircase word w_B;
local defect s_1 in (0,s_P];
local defect s_2 in (0,s_P];
s_1+s_2=q_R(D)-q;
four transition unit contacts determined by the two cells.
```

The SSR/Reinhardt selected-support regression is the boundary point

\[
s_1=s_2=0,
\]

where both missing completion lengths become actual diameter equalities.

A true D2 source lies strictly inside the positive quadrant in these local coordinates, with P-type cells represented by the finite endpoint of the corresponding one-defect compactification.

---

## 7. Next target

The remaining local problem is now a **two-cell closure equation**.

The primal unit shell must close after the two exact staircase bodies and four transition contacts are assembled. Because all internal staircase diameter vectors form arithmetic `delta`-direction progressions, SW expresses every block displacement as a signed partial sum of one geometric progression. D2C supplies the two transition angles explicitly.

The next theorem should write shell closure as two scalar equations in

\[
(w_A,w_B,s_1,s_2),
\qquad s_1+s_2=s,
\]

and test whether any solution exists with `s_1,s_2>0` and the required convex ordering.

This is now a finite combinatorial/trigonometric problem. It directly detects the two genuinely missing diameter states and is not defeated by the SSR selected-support stress regression.

---

## 8. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| both cross distances at one switch are unit transition sides | proved downstream of D2/D2R block order |
| `G<=Delta_2` | proved | midpoint equations from two unit cross distances |
| `G>2delta` | proved | DGE strict consecutive disjoint-gap theorem |
| exact completion length D2C.5 | proved | midpoint decomposition |
| `G=Delta_2` iff parallel transition pair | proved | `W=0` iff common midpoint |
| two defect parameters add to `s=q_R-q` | proved | exact projective gap sum |
| P2/PS/S2 = endpoint/interior cell cases | proved | local short/parallel classification |
| shell closure in `(w_A,w_B,s_1,s_2)` | open | next target |
| Level I | still open | positive two-cell solutions not yet excluded |
