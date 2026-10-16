<!-- migration-source: path=docs/reports/target_c_low_surplus_tripod_normal_form_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=21e57b50eda2a83191adfcc01872f77ba44012e8; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — low-surplus tripod / double-triangulation normal form

**Date:** 2026-09-09  
**Repository base:** current `research/target-c-loaded-boundary-capacity-2026-09-09` after PC  
**Run type:** exact stability reduction  
**Target:** Target C C-II low pinned-boundary-surplus branch  
**Depends on:** PC outer-pocket/internal-chord ledger, ZJ planar-incidence decomposition, ZK component-slack cancellation, C26/C36/C37/C49  
**LEVEL I STATUS:** STILL OPEN

Put

\[
\boxed{S:=e_{BB}+2s_C.}
\]

The GU/PI low-surplus branch is governed by `S/D`.  The PC ledger resolves `S` into nonnegative geometric currencies.  This note pushes that resolution to the actual contact graph.

The main conclusion is finite:

> apart from `O(S+1)` exceptions, the unloaded positive contact core consists of singleton degree-three vertices, each joined to exactly three loaded force-hull terminals; their attachment triangles have pairwise disjoint interiors.  Simultaneously, apart from `O(S)` exceptions, every missing force-hull side cuts off a triangular convex outer pocket.

Thus if `S=o(D)`, the post-ZF survivor is not a diffuse low-stress graph.  It is an `o(D)`-defect perturbation of two simultaneous maximal planar triangle systems on `q=Theta(D)` loaded terminals, while the force hull itself still has quadratic area.  Any remaining macroscopic cavity must therefore be carried by only `o(D)` exceptional regions.

---

## 1. Exact decomposition of `S`

Use the PC notation

- `a`: number of missing force-hull side contacts, equal to the number of OP outer pockets;
- `d_P=sum_P(deg P-3)` over those pockets;
- `c_B`: loaded-loaded unit contacts that are not force-hull sides;
- `Q`: bounded nonquadrilateral face defect;
- `k=d_H+s_Z`.

PC proves

\[
e_{BB}=d_P+Q+2k+c_B.
\]

Therefore

\[
\boxed{
S=d_P+Q+2k+c_B+2s_C.
}
\tag{TN.1}
\]

Every term on the right is nonnegative.  Consequently

\[
\boxed{
d_P,Q,c_B\le S,\qquad k,s_C\le S/2.}
\tag{TN.2}
\]

This simple equality is the source of all stability estimates below.

---

## 2. Almost every hull interval is a triangular outer pocket

PC also gives

\[
q=a+d_P+Q+2k.
\tag{TN.3}
\]

Hence

\[
\boxed{0\le q-a=d_P+Q+2k\le S.}
\tag{TN.4}
\]

So at least `q-S` force-hull sides are missing contact edges and therefore create OP outer pockets.

A nontriangular outer pocket has degree at least four and contributes at least one to `d_P`. Thus

\[
\boxed{
\#\{P:\deg P\ge4\}\le d_P\le S.
}
\tag{TN.5}
\]

Therefore at least

\[
\boxed{a-S\ge q-2S}
\tag{TN.6}
\]

outer pockets are triangles.

No positive lower area per triangular pocket is claimed: a two-unit-edge pocket can become arbitrarily thin as its hull-side chord approaches length two.

---

## 3. The unloaded component count is within `S+2` of `q`

PC gives

\[
a+k=c_I+c_B+s_C+2.
\tag{TN.7}
\]

Eliminate `a` using TN.3:

\[
\begin{aligned}
q-c_I
&=d_P+Q+k+c_B+s_C+2.
\end{aligned}
\]

Thus

\[
\boxed{
q-c_I=d_P+Q+k+c_B+s_C+2.
}
\tag{TN.8}
\]

By TN.1,

\[
\boxed{2\le q-c_I\le S+2.}
\tag{TN.9}
\]

In particular

\[
\boxed{c_I\ge q-S-2.}
\tag{TN.10}
\]

So a low-`S` source has almost one unloaded component per loaded terminal, just as in the exact zero-surplus triangulation branch.

---

## 4. Almost every unloaded component has exactly three distinct attachments

Use the ZJ incidence slacks

\[
u_A:=\sum_r(|A_r|-3)\ge0,
\]

\[
p_A:=q_{used}+2c_I-2s-a_{inc}\ge0,
\]

`u_0=q-q_used>=0`, and let `s` be the number of nontrivial connected components of the attachment-incidence graph.  ZJ proves

\[
\boxed{
e_{BB}+s_C-k
=u_A+p_A+2(s-1)+u_0.
}
\tag{TN.11}
\]

The left side is nonnegative and is at most `e_BB+s_C<=S`. Therefore

\[
\boxed{
u_A,p_A,u_0\le S,
\qquad
2(s-1)\le S.
}
\tag{TN.12}
\]

Every component with more than three distinct loaded attachments contributes at least one to `u_A`. Hence

\[
\boxed{
\#\{r:|A_r|>3\}\le S.
}
\tag{TN.13}
\]

At least `c_I-S` unloaded components therefore have exactly three distinct loaded attachments.

C49.1 gives pairwise disjoint interiors for the convex attachment cells

\[
P_r:=\operatorname{conv}(A_r).
\]

Thus the `|A_r|=3` components produce a family of pairwise interior-disjoint nondegenerate triangles on the convex terminal set `B_+`.

---

## 5. Almost every unloaded component is a singleton

ZK gives the exact component-diameter ledger

\[
\sum_r\delta_r+R_I+s_B+3k
=6+e_{BB}+2s_C
=6+S.
\tag{TN.14}
\]

Therefore

\[
\boxed{
\sum_r\delta_r\le6+S-3k\le6+S.
}
\tag{TN.15}
\]

A connected unloaded component with at least two vertices has graph diameter at least one. Hence

\[
\boxed{
\#\{r:|I_r|>1\}\le6+S.
}
\tag{TN.16}
\]

Combining TN.10, TN.13, and TN.16, at least

\[
\boxed{
q-3S-8
}
\tag{TN.17}
\]

unloaded components are simultaneously

1. singleton components;
2. attached to exactly three distinct loaded terminals.

The constant is deliberately crude but finite and explicit.

---

## 6. Almost every such singleton has contact degree exactly three

For a singleton component `I_r={z}`, there are no internal contact edges and `delta_r=0`.  ZK's component identity is

\[
t_r-\delta_r-3=s_r+r_r.
\]

For a singleton,

\[
r_r=2|I_r|-\delta_r-2-e_r=0,
\]

so

\[
\boxed{t_r-3=s_r.}
\tag{TN.18}
\]

ZK also proves

\[
\sum_rs_r=s_C.
\]

Thus at most `s_C<=S/2` singleton components have more than three loaded contact edges.  Combining with TN.17 gives at least

\[
\boxed{
q-\frac72S-8
}
\tag{TN.19}
\]

unloaded vertices `z` with exactly three unit contacts, all to three distinct loaded terminals, and no other contact.

For an integer statement one may replace the right side by its floor; the asymptotic use is what matters.

Because `z` is unloaded, positive equilibrium at `z` uses those three positive contact forces. Hence `z` lies strictly inside the triangle formed by its three unit-contact neighbors.  Since all three neighbors lie on the unit circle centered at `z`, this attachment triangle has circumradius one and is acute.  Triangle-freeness makes each of its three side lengths strictly greater than one.

These are genuine geometric **tripods**, not merely incidence nodes.

---

## 7. A uniform area floor for one regular tripod cell

Let `T` be one of the attachment triangles from TN.19 and let `z` be its singleton component.  The circumradius of `T` is one and its circumcenter `z` lies in the interior, so `T` is acute.  Every side is strictly greater than one.

Write the three central gaps between the contact directions at `z` as

\[
\theta_1+\theta_2+\theta_3=2\pi.
\]

Acuteness gives `theta_i<pi`, while unit separation plus triangle-freeness gives `theta_i>pi/3`.  The area is

\[
\operatorname{area}(T)
=\frac12\sum_{i=1}^3\sin\theta_i.
\tag{TN.20}
\]

On the open polytope

\[
\theta_i\in(\pi/3,\pi),\qquad \sum\theta_i=2\pi,
\]

the infimum occurs at the boundary configuration `(pi,pi/3,2pi/3)` up to permutation. Hence

\[
\boxed{
\operatorname{area}(T)>\frac{\sqrt3}{2}.
}
\tag{TN.21}
\]

The inequality is strict, but the constant is only an infimum.  Therefore the regular tripod cells already contribute at least

\[
\boxed{
\sum_{r\ regular}\operatorname{area}(P_r)
>
\frac{\sqrt3}{2}
\max\left\{0,q-\frac72S-8\right\}.
}
\tag{TN.22}
\]

This is only `Omega(D)` area because `q=Theta(D)`; it is not a force-bulk closure.  It is nevertheless a useful exact regression against treating the attachment triangles as arbitrarily thin.

---

## 8. Sublinear-surplus asymptotic normal form

Assume

\[
S=o(D).
\tag{TN.23}
\]

DB gives `q>=h>=(2rho-o(1))D`, so `q=Theta(D)`.  Then the preceding finite estimates imply

\[
\boxed{a=q-o(D),\qquad c_I=q-o(D),}
\tag{TN.24}
\]

and:

- all but `o(D)` outer pockets are triangles;
- all but `o(D)` unloaded components are singleton degree-three tripods;
- all but `o(D)` attachment sets have exactly three loaded terminals;
- only `o(D)` loaded terminals are unused by the attachment incidence graph;
- `sum_r delta_r=o(D)`;
- `d_P,Q,k,c_B,s_C=o(D)`.

At the same time the ZK attachment-cell area upper bound gives

\[
\sum_r\operatorname{area}(P_r)=o(D^2),
\tag{TN.25}
\]

while PI gives

\[
\operatorname{area}(F)
\ge(0.4978566363\ldots-o(1))D^2.
\tag{TN.26}
\]

Thus a sublinear-surplus survivor has a paradoxical but not yet contradictory form:

```text
q-o(D) tiny/local degree-three attachment tripods
+ q-o(D) triangular convex outer pockets
+ only o(D) combinatorial defects
+ nevertheless a Theta(D^2) force-hull area not covered by attachment cells.
```

The macroscopic area can be concentrated in a sublinear number of large complementary regions; a single large triangular cavity is a binding regression.  Therefore an argument that charges only face degree cannot close this branch.

---

## 9. Eppstein peeling interpretation

For completeness, the Eppstein diameter edge bound has an exact stability certificate useful for future shell work.

Fix a graph-diameter pair `u,w` in a connected triangle-free penny graph `G` with `n` vertices, `e` edges and graph diameter `delta`.  Unroll Eppstein's induction: while the graph contains a cycle, remove a non-articulation vertex `v_i` of current degree `d_i<=2`, avoiding `u,w`.  Stop at a tree `T` on `t` vertices.  Then

\[
e=(t-1)+\sum_i d_i,
\qquad
n=t+\#\{i\}.
\]

Since deletion cannot shorten the fixed `u-w` distance, `t>=delta+1`.  Therefore the exact Eppstein slack is

\[
\boxed{
2n-\delta-2-e
=(t-\delta-1)+\sum_i(2-d_i).
}
\tag{TN.27}
\]

Every term is nonnegative.  Thus small Eppstein slack means the terminal tree has few vertices off a diameter geodesic and only few peeling steps have degree below two.  It does **not** imply a path-like original graph: square grids have zero slack and quadratic many degree-two peeling steps.  This is why TN.27 is recorded only as a shelling certificate, not as a closure.

---

## 10. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `S=d_P+Q+2k+c_B+2s_C` | proved | PC exact ledger |
| `q-c_I<=S+2` | proved | PC elimination |
| at most `S` nontriangular outer pockets | proved | definition of `d_P` |
| at most `S` attachment sets have size >3 | proved | ZJ exact slack |
| at most `S+6` non-singleton unloaded components | proved | ZK diameter ledger |
| `q-(7/2)S-O(1)` regular singleton tripods | proved | preceding three bounds + `sum s_r=s_C` |
| tripod cell area `>sqrt(3)/2` | proved | acute circumradius-one geometry |
| sublinear `S` closes Level I | false / not proved | macroscopic area may sit in few large cavities |
| Eppstein slack forces path-like graph | rejected | square-grid regression |

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Set S=e_BB+2s_C.  PC gives exactly
    S=d_P+Q+2(d_H+s_Z)+c_B+2s_C.
Hence every displayed term is <=S at its natural weight.
Also
    q-c_I=d_P+Q+(d_H+s_Z)+c_B+s_C+2 <= S+2.
ZJ gives at most S components with >3 distinct loaded attachments.
ZK gives
    sum delta_r <= S+6,
so at most S+6 unloaded components are non-singletons.
Since sum component stress surplus=s_C, at most S/2 singleton components
have degree >3.
Therefore at least
    q-(7/2)S-8
unloaded vertices are exact degree-three singleton tripods attached to three
distinct loaded terminals.  Their attachment triangles are pairwise interior-disjoint,
have circumradius one, are acute, have all sides >1, and each has area >sqrt(3)/2.

If S=o(D), simultaneously:
    a=q-o(D), c_I=q-o(D),
    almost every outer pocket is triangular,
    almost every unloaded component is one regular tripod,
    d_P,Q,d_H+s_Z,c_B,s_C=o(D),
    sum delta_r=o(D).
Yet PI forces area(F)>=0.4978566...D^2 while all attachment cells have o(D^2)
area.  The remaining obstruction is therefore a sublinear number of macroscopic
cavities, not diffuse combinatorial defect.
```
