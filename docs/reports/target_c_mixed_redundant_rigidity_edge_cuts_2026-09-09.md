<!-- migration-source: path=docs/reports/target_c_mixed_redundant_rigidity_edge_cuts_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=e2273064f1e7b00e4a5d113af98f2adc10a922c3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — full-support KKT stress makes the mixed framework redundantly rigid

**Date:** 2026-09-09  
**Repository base:** current PR #143 branch after MC/TF/BM/CS  
**Run type:** exact rigidity strengthening  
**Target:** Target C C-II after ZF  
**Depends on:** C65 relative-interior full actual support and ZF mixed infinitesimal rigidity  
**LEVEL I STATUS:** STILL OPEN

The post-ZF mixed equality framework

\[
G_M=(V,C\cup H)
\]

is not merely infinitesimally rigid.  The relative-interior KKT row dependence is nonzero on **every** actual contact and diameter row.  Therefore every individual mixed edge is redundant in the rigidity matrix:

\[
\boxed{
(G_M-e,p)\text{ is infinitesimally rigid for every }e\in C\cup H.
}
\tag{RR.1}
\]

This holds for every post-ZF survivor, with no assumption `s_Z=0`.

Combined with MC, the mixed support is therefore a 3-vertex-connected redundantly rigid graph in its actual realization.  One immediate cut consequence is

\[
\boxed{
|\delta_{G_M}(A)|\ge4
}
\tag{RR.2}
\]

whenever both `A` and its complement contain at least two vertices.  Hence every contact bridge separating two nonsingleton sides is bypassed by at least **three** actual diameter edges.

---

## 1. Every mixed row lies in a full-support self-stress

Let

\[
R=R(G_M,p)
\]

be the ordinary planar bar-rigidity matrix, with one row for every edge of `C union H`.

ZF proves

\[
\boxed{\operatorname{rank}R=2v-3.}
\tag{RR.3}
\]

Choose the relative-interior normalized KKT stress supplied by C65.  Its multipliers satisfy

\[
\alpha_e>0\quad(e\in C),
\qquad
\beta_h>0\quad(h\in H).
\]

After changing the sign of the diameter coordinates, the vector

\[
\omega=(\alpha,-\beta)
\]

is an ordinary bar self-stress:

\[
\boxed{\omega^TR=0.}
\tag{RR.4}
\]

Every coordinate of `omega` is nonzero.

---

## 2. Theorem RR — redundant infinitesimal rigidity

### Theorem RR.1

For every mixed edge `f in C union H`, deleting `f` leaves rigidity rank unchanged:

\[
\boxed{
\operatorname{rank}R(G_M-f,p)=2v-3.
}
\tag{RR.5}
\]

### Proof

Write the full-support stress relation as

\[
\sum_{e\in E(G_M)}\omega_e R_e=0,
\]

where `R_e` is the rigidity row of edge `e`.

Fix `f`. Since `omega_f !=0`,

\[
R_f
=-\frac1{\omega_f}
\sum_{e\ne f}\omega_eR_e.
\]

Thus row `R_f` lies in the span of all other rows. Deleting it does not change the row span or the rank. ZF gives the common rank `2v-3`. `square`

The argument uses only one full-support row dependence.  The dimension `s_Z+1` of the full stress space may be larger than one.

### Corollary RR.2

Every actual mixed edge lies in a rigidity circuit of the actual row matroid.

In the special case `s_Z=0`, the whole mixed graph is itself that unique circuit, recovering MC/CS.  For `s_Z>0`, RR says the mixed graph is a union of overlapping actual rigidity circuits covering every edge.

---

## 3. Four-edge lower bound for every nontrivial mixed cut

Let

\[
V=A\sqcup B,
\qquad |A|\ge2,
\qquad |B|\ge2,
\]

and let

\[
k:=|\delta_{G_M}(A)|
\]

be the number of mixed edges crossing the cut.

### Theorem RR.3 — essentially four-edge-connected mixed support

\[
\boxed{k\ge4.}
\tag{RR.6}
\]

### Proof

Choose any crossing edge `f`.  RR.1 says `G_M-f` is infinitesimally rigid, so its rigidity matrix has rank `2v-3`.

After deleting `f`, at most `k-1` rows cross between `A` and `B`.  The rows internal to `A` have rank at most

\[
2|A|-3,
\]

and the rows internal to `B` have rank at most

\[
2|B|-3.
\]

Therefore

\[
\begin{aligned}
2v-3
&=\operatorname{rank}R(G_M-f,p)\\
&\le(2|A|-3)+(2|B|-3)+(k-1)\\
&=2v+k-7.
\end{aligned}
\]

Hence `k>=4`. `square`

No generic rigidity theorem is used; this is a direct rank count in the actual realization.

The singleton-side exception is necessary.  `K_4` is redundantly rigid and has a three-edge cut around each vertex.

---

## 4. Contact bridges have three diameter bypass edges

Let `uv` be a contact bridge with bridge sides `A,B`.  The mixed cut consists of

1. the unique contact edge `uv`;
2. actual diameter edges in `E_H(A,B)`.

If

\[
|A|,|B|\ge2,
\]

RR.3 gives

\[
1+|E_H(A,B)|\ge4.
\]

Therefore:

### Corollary RR.4 — three-diameter bridge bypass

\[
\boxed{|E_H(A,B)|\ge3.}
\tag{RR.7}
\]

This strengthens TF's universal lower bound `>=2` on every bridge cut.  The exact cases are now:

- if one bridge side is a singleton, at least two diameter edges cross, by mixed minimum degree / TF;
- if both bridge sides have at least two vertices, at least three diameter edges cross.

When both sides have at least three vertices, BM simultaneously gives a mixed matching of size three, hence at least two vertex-disjoint diameter bypasses.

In the `s_Z=0` circuit phase, CS sharpens RR.7 to the exact formula

\[
|E_H(A,B)|=3+\delta_A+\delta_B.
\]

---

## 5. Any nontrivial two-block decomposition needs four mixed bars

RR.3 is not specific to contact bridges.  If a vertex partition with both sides of size at least two has only three mixed edges crossing, then one of those edges is essential for rigidity.  This cannot happen because every mixed edge belongs to a full-support stress relation.

This removes a common body-bar regression from the post-ZF endgame:

```text
two internally rigid subframeworks connected by exactly three mixed bars
```

may be minimally rigid, but it cannot occur as a cut of the current full-support KKT framework.  There must be at least one fourth mixed bar providing redundancy.

---

## 6. Relation to generic global rigidity

MC + RR give the two classical graph-theoretic ingredients associated with generic planar global rigidity: 3-vertex-connectivity and redundant rigidity.

No generic-global-rigidity theorem is needed here, and no genericity of the source is asserted.  U1 already supplies the stronger realization-specific statement that the equality framework is universally rigid.  RR is useful because it converts the full-support KKT stress directly into finite cut inequalities in the **actual** source graph.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| every edge deletion preserves rigidity rank | proved | full-support KKT row relation |
| every edge lies in an actual rigidity circuit | proved | matroid consequence |
| every nonsingleton mixed cut has >=4 edges | proved | delete one cut edge + rank count |
| nonsingleton contact bridge has >=3 H bypasses | proved | only one contact edge crosses |
| singleton contact bridge has >=3 H bypasses | false/not claimed | `K_4`-type degree-three cut is possible; universal lower bound is 2 |
| Level I | still open | redundancy is structural, not yet a global packing contradiction |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Relative-interior C65 KKT gives a bar self-stress omega=(alpha,-beta) with every
mixed coordinate nonzero. Therefore for each mixed edge f,
    R_f = -(1/omega_f) sum_{e!=f} omega_e R_e.
Deleting f preserves the full ZF rank 2v-3. Hence C union H is redundantly
infinitesimally rigid in the actual realization.

For any cut A|B with |A|,|B|>=2 and k mixed crossing edges, delete one crossing edge.
The remaining rigid framework has rank at most
    (2|A|-3)+(2|B|-3)+(k-1)=2v+k-7.
Since the rank is 2v-3, k>=4.

Therefore a contact bridge with two nonsingleton sides has at least three actual
diameter bypass edges. If both sides have >=3 vertices, BM also forces at least two
of those H bypasses to be vertex-disjoint.
```
