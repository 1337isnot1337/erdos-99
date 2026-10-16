<!-- theorem-state: {"artifact_id":"ART-FA22005235BF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — attachment-cell fill and residual-ledger cancellation

**Date:** 2026-09-09  
**Repository base:** `cf790155660ad46797e53c7f44371b078f7eab7b`  
**Run type:** exact ledger synthesis / finite packing theorem  
**Target:** Target C C-II after ZF; especially the UF near-circle phase  
**Depends on:** C36 harmonic attachment hulls, C49 disjoint attachment cells, C44/ZG attachment-diameter control, finite Oler, ZK, ZT, ZU  
**External web search:** not used  
**Computation:** not used in the proof

## LEVEL I STATUS

`STILL OPEN`

This report adds two exact links that were not extracted in the current post-ZF stack.

First, the ZK component ledger, ZU pinned-contact ledger, and ZT terminal partition cancel all diameter variables and give the exact residual identity

\[
\boxed{
\sum_r\delta_r+R_I+s_B
=x_B+Q+4-c_I+s_C.
}
\tag{AR.1}
\]

Thus the total unloaded-component graph diameter, internal Eppstein slack, and unused loaded-degree capacity are paid directly by outer-walk defect and bounded-face defect, with pinned-contact stress contributing and component count subtracting.

Second, the harmonic attachment cells themselves have a packing lower bound as well as the existing isodiametric upper bound. If

\[
S:=\sum_r\delta_r,
\qquad
a_0:=\frac{\sqrt3}{2},
\]

then every finite post-ZF survivor satisfies

\[
\boxed{
a_0(v-q)
\le
\frac\pi4S^2
+\pi\left(1+\frac{a_0}{2}\right)S
+\bigl[\pi+a_0(\pi-2)\bigr]c_I.
}
\tag{AR.2}
\]

Consequently, along any unbounded post-ZF subsequence for which

\[
\frac v{D^2}\to r,
\]

one has

\[
\boxed{
\liminf\frac SD
\ge
\sqrt{\frac{2\sqrt3}{\pi}\,r}
=\sqrt{\frac r\Delta},
\qquad
\Delta:=\frac\pi{2\sqrt3}.
}
\tag{AR.3}
\]

In the UF near-circle notation

\[
\zeta:=\lim\frac{n-v}{D^2},
\qquad
\frac v{D^2}\to\Delta-\zeta,
\]

this becomes

\[
\boxed{
\liminf\frac1D\sum_r\delta_r
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\tag{AR.4}
\]

Therefore the near-circle phase cannot place a positive-density force-visible core into only graph-small unloaded components. At the UF worst crossover `zeta_*=0.5572837714...`, AR.4 still gives the numerical obligation

\[
\liminf\frac SD\ge0.62089\ldots .
\]

The theorem does not yet imply that one component has linear diameter; the total `S` may be distributed over many components. It does, however, supply a new independent linear currency that is geometric, unweighted, and tied directly to the exact post-ZF ledgers by AR.1.

---

## 1. Notation and audited inputs

Work in the lexicographically normalized fully force-visible C-II source. Let

- `v` be the number of vertices in the positive contact core;
- `q=|B_+|` be the loaded force-hull terminal count;
- `I_1,...,I_{c_I}` be the connected components of the contact graph after deleting `B_+`;
- `n_r=|I_r|`;
- `delta_r` be the graph diameter of `C[I_r]`, with `delta_r=0` for a singleton;
- `A_r subset B_+` be the distinct loaded attachment set of `I_r`;
- `a_r=|A_r|`;
- `P_r=conv(A_r)`;
- `R_I=sum_r r_r` be the total internal Eppstein slack from ZK;
- `s_B=3q-e_{BI}-2e_{BB}` be the unused loaded contact-degree capacity;
- `x_B=b-q` be the outer-walk excess;
- `Q=sum_F(deg F-4)` over bounded nonquadrilateral faces;
- `d_H=q-h` and `s_Z=e+h-(2v-2)`;
- `s_C` be the pinned-contact stress surplus.

The needed geometry is already proved in the repository:

1. C36 gives
   \[
   I_r\subseteq P_r,
   \qquad a_r\ge3.
   \tag{1.1}
   \]
2. C49 proves
   \[
   \operatorname{int}P_r\cap\operatorname{int}P_s=\varnothing
   \quad(r\ne s).
   \tag{1.2}
   \]
3. C44/ZG gives
   \[
   \operatorname{diam}(A_r)=\operatorname{diam}(P_r)
   \le\delta_r+2.
   \tag{1.3}
   \]

No assumption that attachment sets are disjoint is needed. They may share loaded vertices; only cell interiors are used for area additivity.

---

## 2. Exact cancellation of the post-ZF ledgers

Put

\[
k:=d_H+s_Z.
\]

ZK gives

\[
\boxed{
S+R_I+s_B+3k
=6+e_{BB}+2s_C.
}
\tag{2.1}
\]

ZU gives

\[
\boxed{
c_I+e_{BB}+s_C=q-2+k.}
\tag{2.2}
\]

Hence

\[
e_{BB}=q-2+k-c_I-s_C.
\tag{2.3}
\]

Insert (2.3) into (2.1):

\[
\begin{aligned}
S+R_I+s_B
&=6+q-2+k-c_I-s_C+2s_C-3k\\
&=q+4-2k-c_I+s_C.
\end{aligned}
\tag{2.4}
\]

ZT gives the exact terminal partition

\[
\boxed{q=x_B+Q+2k.}
\tag{2.5}
\]

Substituting (2.5) into (2.4) proves AR.1:

\[
\boxed{
S+R_I+s_B=x_B+Q+4-c_I+s_C.
}
\]

### Immediate consequences

Since `R_I,s_B>=0`,

\[
\boxed{
S\le x_B+Q+4-c_I+s_C.
}
\tag{2.6}
\]

Equivalently,

\[
\boxed{
x_B+Q+s_C\ge S+c_I-4.}
\tag{2.7}
\]

Thus any lower bound on total unloaded graph diameter feeds directly into the outer/face/pinned-stress currencies. This implication does not pass through diameter branching or KKT weights.

---

## 3. Oler lower bound inside every attachment cell

The source points

\[
X_r:=I_r\cup A_r
\]

are unit-separated, lie in the convex body `P_r`, and have cardinality

\[
|X_r|=n_r+a_r.
\]

The finite Oler inequality in the normalization used throughout the repository is

\[
a_0(N-1)
\le
\operatorname{area}(K)+\frac{a_0}{2}\operatorname{per}(K),
\qquad
a_0=\frac{\sqrt3}{2},
\tag{3.1}
\]

for `N` unit-separated points in a convex planar container `K`.

Apply (3.1) to `X_r subset P_r`:

\[
\operatorname{area}(P_r)
\ge
a_0(n_r+a_r-1)
-\frac{a_0}{2}\operatorname{per}(P_r).
\tag{3.2}
\]

The planar convex perimeter-diameter inequality and (1.3) give

\[
\operatorname{per}(P_r)
\le\pi\operatorname{diam}(P_r)
\le\pi(\delta_r+2).
\tag{3.3}
\]

Using `a_r>=3`, equations (3.2)-(3.3) yield

\[
\boxed{
\operatorname{area}(P_r)
\ge
a_0n_r
-\frac{a_0\pi}{2}\delta_r
-a_0(\pi-2).
}
\tag{3.4}
\]

This lower bound is intentionally coarse in the boundary-order terms. Its quadratic leading coefficient is exact for the asymptotic consequence below.

Summing (3.4), and using

\[
\sum_rn_r=v-q,
\]

gives

\[
\boxed{
\sum_r\operatorname{area}(P_r)
\ge
a_0(v-q)
-\frac{a_0\pi}{2}S
-a_0(\pi-2)c_I.
}
\tag{3.5}

\]

---

## 4. Existing isodiametric upper bound in terms of the same `S`

By (1.3) and the planar isodiametric inequality,

\[
\operatorname{area}(P_r)
\le
\frac\pi4(\delta_r+2)^2.
\tag{4.1}
\]

Sum over components. Since every `delta_r>=0`,

\[
\sum_r\delta_r^2\le\left(\sum_r\delta_r\right)^2=S^2.
\]

Therefore

\[
\boxed{
\sum_r\operatorname{area}(P_r)
\le
\frac\pi4\left(S^2+4S+4c_I\right).
}
\tag{4.2}
\]

This is the same cell-area estimate used in the ZG/GU route, now paired with a lower bound on the cell area rather than only with `area(F)`.

---

## 5. Finite attachment-fill inequality

Combine (3.5) and (4.2):

\[
a_0(v-q)
-\frac{a_0\pi}{2}S
-a_0(\pi-2)c_I
\le
\frac\pi4S^2+\pi S+\pi c_I.
\]

Rearranging proves AR.2:

\[
\boxed{
a_0(v-q)
\le
\frac\pi4S^2
+\pi\left(1+\frac{a_0}{2}\right)S
+\bigl[\pi+a_0(\pi-2)\bigr]c_I.
}
\]

This is a finite theorem. It uses no asymptotic density assumption and no KKT coefficient lower bound.

---

## 6. Asymptotic component-diameter obligation

All lower-order quantities in AR.2 are `O(D)` in the post-ZF branch:

- `q<=pi D`;
- `c_I<=q` by the attachment incidence bounds;
- `S=O(D)` by ZK together with `e_BB=O(q)`, ZU, and `d_H+s_Z<=q/2` from ZT.

Let an unbounded subsequence satisfy

\[
\frac v{D^2}\to r.
\]

Divide AR.2 by `D^2`. The terms involving `q`, `S`, and `c_I` only linearly vanish except for `S^2`. Writing

\[
s:=\liminf\frac SD
\]

and passing to a further subsequence attaining that liminf gives

\[
a_0r\le\frac\pi4s^2.
\]

Hence

\[
\boxed{
s\ge\sqrt{\frac{4a_0}{\pi}r}
=\sqrt{\frac{2\sqrt3}{\pi}r}.
}
\tag{6.1}
\]

Since

\[
\Delta=\frac\pi{2\sqrt3},
\]

this is exactly AR.3:

\[
\boxed{
\liminf\frac SD\ge\sqrt{r/\Delta}.
}
\]

The constant is not an arbitrary packing estimate: `1/Delta=2sqrt(3)/pi` is exactly the global leading density coefficient already governing `n/D^2`.

---

## 7. Insert the UF near-circle population parameter

PR #119 proves in the `x_B=o(D)` near-circle phase that, along a subsequence with

\[
\frac{n-v}{D^2}\to\zeta,
\]

the global density relation gives

\[
\frac v{D^2}\to\Delta-\zeta.
\tag{7.1}
\]

Insert `r=Delta-zeta` in AR.3:

\[
\boxed{
\liminf\frac SD
\ge
\sqrt{1-\frac\zeta\Delta}.
}
\tag{7.2}
\]

At the UF crossover

\[
\zeta_*=0.5572837714\ldots,
\]

the right side is

\[
0.6208918647\ldots .
\]

Thus even the population split that minimizes UF's universal face-defect lower bound retains more than `0.62D` total graph diameter across the unloaded harmonic components.

Combining (7.2) with the exact residual ledger (2.7) gives, on the same near-circle subsequence,

\[
\boxed{
\liminf\frac{Q+s_C}{D}
\ge
\sqrt{1-\frac\zeta\Delta},
}
\tag{7.3}
\]

because `x_B=o(D)` and `c_I>=0`. UF separately gives a stronger lower bound on `Q` for part of the `zeta` range, but (7.3) is structurally different: it certifies that the component-diameter carrier is paid by the exact face/pinned-stress ledger.

---

## 8. What this theorem rules out

AR excludes several previously unseparated degenerations.

1. **Positive-density core with graph-small harmonic components.** If `v/D^2` stays bounded below, then `sum delta_r` is automatically linear in `D`.
2. **Near-circle core carried only by bounded-size unloaded components.** If all `delta_r=O(1)`, then AR.3 forces `c_I=Omega(D)` and total component diameter still has the displayed linear scale; there is no sublinear-diameter escape.
3. **Hiding the component geometry entirely in diameter branching.** AR.1 eliminates `d_H` and `s_Z`; the residual component geometry is coupled directly to `x_B,Q,s_C`.

What AR does **not** prove is equally important:

- it does not force one component to have diameter `Omega(D)`;
- it does not lower-bound any KKT coefficient;
- it does not exclude a linear number of bounded-size cells;
- it does not by itself reverse the face inequality `b+Q<=2h`.

The regular-shell and oblique-grid regressions therefore remain outside the claimed conclusion.

---

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| residual identity AR.1 | proved | exact substitution of ZK, ZU, ZT |
| cell lower bound AR.2 | proved | Oler + convex perimeter/diameter + C36/C44/C49 |
| `S/D >= sqrt(r/Delta)` | proved asymptotically | AR.2 and post-ZF `O(D)` lower-order budgets |
| UF specialization AR.4 | conditional on PR #119 UF | substitute `r=Delta-zeta` |
| one macroscopic harmonic component | not proved | `S` may be spread over many components |
| Level I | still open | linear residual currencies remain feasible |

---

## 10. Next target

AR creates a new finite target that is more specific than a generic force-bulk theorem.

In the near-circle branch, combine

\[
S=\sum_r\delta_r=\Omega(D)
\]

with

- the planar noncrossing attachment incidence graph C37;
- the almost complete loaded unit-contact hull cycle from DG/DC/HB;
- the loaded degree-three cap;
- and UF's mandatory `Q=Omega(D)` exceptional-face defect.

The highest-value next lemma is an **attachment-diameter versus defect-face incidence theorem**: show that a noncrossing family of harmonic cells carrying the required total graph diameter cannot coexist with the almost-unit loaded boundary and the UF face-defect density without spending more loaded contact incidence than C35 allows.

Until such a theorem is proved, AR should remain report-level and should not be promoted into the canonical route map.
