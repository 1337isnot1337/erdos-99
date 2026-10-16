<!-- migration-source: path=docs/reports/target_c_minimal_interface_internal_exceptional_perimeter_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=a91a61825625670ae4ff6bb95519769f2362f677; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — CE exceptional perimeter nearly exhausts the internal defect budget at minimal interface

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** cross-route scalar sharpening with exact equality geometry  
**Target:** full-core near-circle endpoint with `Q_B/D->2`  
**Depends on:** CE one-ended train theorem on PR #119, CF central-face concentration, HBd exact terminal budget  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

IP used only CE's count lower bound `f>=sqrt(Delta)D`. CE contains a strictly stronger statement at the same endpoint: the total perimeter of all bounded nonquadrilateral contact faces satisfies

\[
\boxed{
K_{exc}:=Q+4f
\ge(\pi+4\sqrt\Delta-o(1))D,
\qquad
\Delta=\frac\pi{2\sqrt3}.
}
\tag{EP.1}

Under the minimal loaded-interface equality

\[
Q_B=(2+o(1))D,
\]

CF proves that one central exceptional face `F_*` has

\[
k_{F_*}=(2+o(1))D
\]

and every other loaded-interface exceptional face has total degree excess `o(D)`. The number of those remaining interface faces is therefore `o(D)`, so their total perimeter is also `o(D)` because

\[
\sum_{F\ne F_*\atop F\text{ interface}}\deg F
=4f_{B,\ne *}+(Q_B-Q_{F_*})=o(D).
\]

Consequently almost all of CE's exceptional perimeter not used by the central face must occur **inside** the harmonic components:

\[
\boxed{
Q_{int}+4f_{int}
\ge
(\pi-2+4\sqrt\Delta-o(1))D.
}
\tag{EP.2}

Numerically,

\[
\pi-2+4\sqrt\Delta
=4.9508438810\ldots .
\]

Since `f_int<=Q_int`,

\[
Q_{int}+4f_{int}\le5Q_{int},
\]

and therefore

\[
\boxed{
Q_{int}
\ge
\frac{\pi-2+4\sqrt\Delta}{5}D-o(D)
=0.9901687762\ldots D-o(D).
}
\tag{EP.3}

This substantially strengthens IP.3's `sqrt(Delta)=0.9523128...` lower bound.

HBd gives the exact near-circle identity

\[
Q+2s_C=(\pi+o(1))D.
\]

With `Q=Q_B+Q_int`, EP.3 yields

\[
\boxed{
s_C
\le
\frac{1}{2}\left[
\pi-2-
\frac{\pi-2+4\sqrt\Delta}{5}
\right]D+o(D)
}
\tag{EP.4}

or, after simplification,

\[
\boxed{
s_C
\le
\frac{2}{5}(\pi-2-\sqrt\Delta)D+o(D)
=0.07571193869\ldots D+o(D).
}
\tag{EP.5}

HBd also gives

\[
d_H+s_Z=s_C+o(D),
\]

so

\[
\boxed{
d_H+s_Z\le0.07571193869\ldots D+o(D).}
\tag{EP.6}

Because `q=(pi+o(1))D` and `d_H=q-h`,

\[
\boxed{
h
\ge
\left[
\pi-\frac{2}{5}(\pi-2-\sqrt\Delta)-o(1)
\right]D
=3.0658807149\ldots D-o(D).
}
\tag{EP.7}

Thus the diameter graph has at least `97.59%` of the extremal `q` edge count at the minimal-interface endpoint.

The previous pentagon floor remains unchanged and still follows from the joint constraints:

\[
\boxed{
p_5\ge
(2\sqrt\Delta-\pi+2-o(1))D
=0.7630329601\ldots D-o(D).
}
\tag{EP.8}

The reason EP improves `Q_int` and `s_C` but not the universal pentagon lower bound is that the latter is minimized at the opposite end of the allowed `Q_int` interval.

---

## 1. Interface exceptional perimeter is only `2D+o(D)`

Let `f_B` count bounded nonquadrilateral faces touching loaded terminals. CF gives

\[
Q_{F_*}=(2+o(1))D,
\qquad
Q_B-Q_{F_*}=o(D).
\]

Every other interface exceptional face contributes at least one to `Q_B-Q_{F_*}`, hence

\[
f_B-1=o(D).
\]

For exceptional faces `deg F=4+(deg F-4)`. Therefore

\[
\begin{aligned}
K_{exc,B}
&:=\sum_{F\text{ interface exc}}\deg F\\
&=4f_B+Q_B\\
&=(2+o(1))D.
\end{aligned}
\tag{1.1}

So the central face asymptotically carries the entire interface exceptional perimeter, not only its degree excess.

---

## 2. Subtract from CE

Split

\[
K_{exc}=K_{exc,B}+K_{exc,int}.
\]

For the internal exceptional faces,

\[
K_{exc,int}=Q_{int}+4f_{int}.
\]

CE gives EP.1 and (1.1) gives `K_exc,B=(2+o(1))D`. Hence

\[
K_{exc,int}
\ge
(\pi+4\sqrt\Delta-2-o(1))D,
\]

which is EP.2.

---

## 3. Optimize the internal degree defect

Every internal exceptional bounded face has degree at least five, so

\[
f_{int}\le Q_{int}.
\]

Then

\[
Q_{int}+4f_{int}\le5Q_{int}.
\]

Combine with EP.2:

\[
Q_{int}
\ge
\frac{\pi-2+4\sqrt\Delta}{5}D-o(D),
\]

proving EP.3.

Equality in this scalar minimization forces

\[
f_{int}=Q_{int}+o(D),
\]

so every but `o(D)` units of internal defect are pentagonal in the branch that minimizes `Q_int`. This is only an equality condition, not a global assertion that EP.3 is attained.

---

## 4. Tight remaining stress/diameter budget

HBd gives exactly

\[
Q_{int}+2s_C=(\pi-2+o(1))D
\tag{4.1}

at minimal interface equality. Inserting EP.3 gives EP.5.

The same relation gives the complementary upper bound

\[
Q_{int}\le(\pi-2+o(1))D.
\tag{4.2}

Thus the internal face-defect coefficient is trapped in the short interval

\[
\boxed{
0.9901687762\ldots
\le\liminf Q_{int}/D
\le\limsup Q_{int}/D
\le1.1415926536\ldots .
}
\tag{4.3}

Correspondingly the entire pinned/mixed diameter currency satisfies

\[
0\le s_C/D\le0.07571193869\ldots+o(1).
\]

This is a much narrower equality regime than the original GP/FS interface theorem.

---

## 5. Pentagon lower bound

Write `p_5` for the internal pentagon count. As in IP,

\[
Q_{int}\ge2f_{int}-p_5,
\]

so

\[
p_5\ge2f_{int}-Q_{int}.
\tag{5.1}

EP.2 gives

\[
f_{int}\ge\frac{\pi-2+4\sqrt\Delta-Q_{int}/D}{4}D-o(D).
\]

Insert this in (5.1):

\[
\frac{p_5}{D}
\ge
\frac{\pi-2+4\sqrt\Delta}{2}
-\frac32\frac{Q_{int}}D-o(1).
\]

The right side decreases with `Q_int`, so use the upper bound `Q_int/D<=pi-2` from (4.2):

\[
\frac{p_5}{D}
\ge
2\sqrt\Delta-(\pi-2)-o(1),
\]

which is EP.8.

---

## 6. Consequence for the diameter pseudoforest

The canonical diameter graph is a geometric thrackle and hence a pseudoforest; the post-ZF notation `d_H=q-h` counts its tree components, with at most one odd-unicyclic component.

EP.6 gives

\[
d_H\le0.07571193869\ldots D+o(D).
\]

Since `q~pi D`, a minimal-interface survivor has at most about `2.41%` as many tree components as loaded terminals. Either a large fraction of the loaded vertices lies in the possible odd-unicyclic component, or the tree components have average order at least about

\[
\frac{\pi}{0.0757119}=41.49
\]

among vertices not assigned to that cycle component, modulo the distribution between the two classes.

No stronger structural classification is claimed here. The regular odd shell shows that `d_H=0` itself is geometrically possible at leading order.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `K_exc,B=(2+o(1))D` | proved | CF plus `f_B=o(D)` |
| EP.2 internal exceptional perimeter floor | proved | subtract interface perimeter from CE |
| `Q_int>=0.9901687762D-o(D)` | proved | `f_int<=Q_int` |
| `s_C,d_H+s_Z<=0.07571193869D+o(D)` | proved | HBd exact budget |
| `h>=3.0658807149D-o(D)` | proved | `q~pi D` |
| pentagon floor `0.7630329601D` | proved | joint EP.2 and HBd upper bound |
| Level I | still open | narrow internal-fault / near-maximal-thrackle endpoint survives |

---

## 8. Next target

The minimal-interface equality branch is now squeezed simultaneously by

- one central doubled-geodesic face carrying `2D+o(D)` interface defect;
- internal exceptional perimeter at least `4.95084D`;
- internal degree defect in `[0.99017D,1.14159D]`;
- at least `0.76303D` internal pentagons;
- `d_H+s_Z<=0.075712D`;
- diameter graph edge count `h>=3.06588D` with `q~pi D`.

The next high-value theorem is a stability classification for convex geometric thrackles with `q-h=o(q)` that retains the near-circular metric order. A useful conclusion would be that all but `O(d_H)` terminals lie on one odd-cycle backbone with only short leaf bushes. That would make the normalized diameter reaction graph essentially one-dimensional and expose its compatibility with the two half-disk KKT response blocks.

A second route is to use the dense pentagon count: each pentagon terminates five stopped-train strands, while the central face and annular shell have only a tightly controlled endpoint budget. A nonovercounting train-flow theorem through the two dominant carriers could turn `0.763D` pentagons into a strict boundary-capacity contradiction.