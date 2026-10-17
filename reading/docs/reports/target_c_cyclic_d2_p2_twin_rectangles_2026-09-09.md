> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_p2_twin_rectangles_2026-09-09.md) · source SHA-256 `d5b707a67a5b9612f770557425be8558594a280ec210e3245a1a7ef7786befce`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-417F6173E9E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` P2 is a two-rectangle four-completion endpoint

**Date:** 2026-09-09  
**Run type:** exact P2 geometry / KKT / maximal-thrackle classification  
**Target:** primitive cyclic endpoint `d_H=2`, AD subcase P2  
**Depends on:** AD P2 difference-body count, D2 two-tree/four-block normal form, WM/IB four-contact wrench rank, MT maximal-thrackle completion  
**External literature:** no new input  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

In P2 the force hull has exactly two unordered pairs of parallel unit sides and the difference body `K=F-F` has no short vertices. This forces a much more rigid endpoint than the raw AD label suggests.

Let

$$
\delta:=2\arcsin\frac1{2D},
\qquad
\Delta:=2\arcsin\frac1D.
$$

Then P2 satisfies the exact direction equation

$$
\boxed{(q-4)\delta+2\Delta=\pi.}
\tag{P2R.1}
$$

Equivalently

$$
\boxed{
q
=4+\frac{\pi-2\Delta}{\delta}
=\pi D-\frac{\pi}{24D}-\frac1{2D^2}+O(D^{-3}).
}
\tag{P2R.2}
$$

Each parallel side pair determines an exact rectangle of four shell vertices. Its parallel sides have length one, its two diagonals are actual diameter edges of length `D`, and its other two sides are antipodal short chords of length

$$
\boxed{\sqrt{D^2-1}.}
\tag{P2R.3}
$$

The two diameter diagonals of each such rectangle belong to different D2 diameter-tree components. Therefore the two parallel shell sides are A/B transition contacts. Since there are exactly two parallel pairs and exactly four A/B transition contacts, the four transition contacts are precisely those four sides, paired as two opposite parallel pairs.

The WM/IB four-contact circuit then forces

$$
\boxed{
\alpha_i=\alpha_j=\alpha_k=\alpha_\ell
}
\tag{P2R.4}
$$

for the four transition contact coefficients.

Finally, each length-two Minkowski edge has two canonical unit-step refinements. Refining the two independent P2 ties gives four maximal `q`-edge convex-thrackle completions of the full diameter forest. The actual diameter diagonals adjacent to the ties are leaf edges, and every nonleaf edge of either D2 diameter tree lies in the common path shared by all four completion cycles on that component.

Thus P2 reduces to two isostatic bodies coupled through an **equal-weight parallelogram four-contact cage**, with four canonical defective-Reinhardt completions.

---

## 1. Difference-body edge lengths

For a convex polygon `F`, the edge sequence of

$$
K=F+(-F)
$$

is the angular merge of the edge sequences of `F` and `-F`. Every side of `F` has length one.

- If no side of `F` is parallel to the opposite-oriented side contributed by `-F`, the corresponding K-edge has length one.
- If a pair of distinct shell sides are parallel with opposite boundary orientations, the two codirected unit Minkowski contributions merge into one K-edge of length two.

P2 has exactly two unordered parallel side pairs. Hence `K` has

- four length-two edges, arranged in two antipodal pairs;
- all remaining edges of length one.

AD gives

$$
|V(K)|=2q-4
$$

in P2, and by definition of the P2 subcase every K-vertex lies on the radius-`D` circle.

A circle chord of length one subtends central angle

$$
\delta=2\arcsin\frac1{2D},
$$

while a chord of length two subtends

$$
\Delta=2\arcsin\frac1D.
$$

There are `2q-8` unit K-edges and four doubled K-edges. Summing central angles around the full circle gives

$$
(2q-8)\delta+4\Delta=2\pi,
$$

which is P2R.1.

Solving for `q` gives the exact expression in P2R.2. The expansion follows from

$$
2\arcsin\frac1{2D}
=\frac1D+\frac1{24D^3}+O(D^{-5}),
$$

$$
2\arcsin\frac1D
=\frac2D+\frac1{3D^3}+O(D^{-5}).
$$

---

## 2. Every parallel pair forms an exact rectangle

Take one parallel shell-side pair

$$
ab,\qquad cd
$$

in cyclic order, oriented so

$$
b-a=t,
\qquad
d-c=-t,
\qquad |t|=1.
\tag{2.1}
$$

In the Minkowski merge, this pair produces the length-two K-edge

$$
[a-c,\ b-d],
$$

whose vector is `2t`.

P2 has no short K-vertices, so both endpoints are actual radius-`D` difference vectors:

$$
|a-c|=|b-d|=D.
\tag{2.2}
$$

Also

$$
b=a+t,
\qquad d=c-t,
$$

so

$$
a+c=b+d.
\tag{2.3}
$$

Thus `a,b,c,d` form a parallelogram. Its diagonals `ac` and `bd` have equal length `D`, hence the parallelogram is a rectangle.

The other rectangle side length is therefore

$$
\boxed{L=\sqrt{D^2-1}.}
\tag{2.4}
$$

Moreover

$$
a-d=b-c
$$

as directed vectors, so `ad` and `bc` are the two equal short antipodal chords associated with the tie.

This is exactly the P1 rectangle mechanism, now occurring twice independently.

---

## 3. The two diameter diagonals lie in different D2 components

Write the D2 diameter forest as

$$
H=T_A\sqcup T_B.
$$

For the rectangle above, both diagonals

$$
ac,\qquad bd
$$

belong to `H`, because they are endpoints of a P2 K-edge and all K-vertices are actual diameter states.

We claim they cannot lie in the same tree component.

Refine the length-two Minkowski edge by choosing either intermediate support state

$$
a-c\to b-c\to b-d
$$

or

$$
a-c\to a-d\to b-d.
$$

Perform either choice here and an arbitrary analogous choice at the second P2 tie. The full rotating-calipers support state sequence is still monotone, so the resulting `q` antipodal chords form a convex thrackle containing `H`. It has `q` edges on `q` vertices and is therefore maximal.

MT says that in every maximal completion of the D2 two-tree forest, both added chords join `T_A` to `T_B` and lie on the unique odd cycle.

If `ac` and `bd` belonged to the same component, then all four vertices `a,b,c,d` would belong to that component. Both possible intermediate chords `ad` and `bc` would then be internal to the same component, contradicting MT for either refinement.

Therefore, after swapping labels if necessary,

$$
\boxed{a,c\in A,
\qquad b,d\in B.}
\tag{3.1}
$$

Thus `ac` is an A-tree diameter edge and `bd` is a B-tree diameter edge.

Consequently the shell sides

$$
ab,\qquad cd
$$

both cross the A/B component cut. They are transition contacts of the four-block D2 decomposition.

---

## 4. The parallel pairs exhaust the four transition contacts

D2 gives exactly four shell edges crossing `A|B`, at the four transitions in

$$
A_0\mid B_0\mid A_1\mid B_1.
$$

Section 3 shows that each of the two P2 parallel pairs contributes two such transition contacts.

The two unordered parallel pairs use four distinct shell edges. Indeed a side direction occurs only once with each boundary orientation in a strictly convex polygon, so one shell side cannot belong to two different opposite-parallel pairs.

Therefore the four P2 parallel sides are exactly all four transition contacts.

Index the transitions cyclically as

$$
i<j<k<\ell.
$$

The two A-to-B transitions are opposite in this cyclic list, as are the two B-to-A transitions. Hence the parallelism pattern is

$$
\boxed{
t_k=-t_i,
\qquad
t_\ell=-t_j,
}
\tag{4.1}

where `t_r` is the oriented unit shell tangent on transition side `r`.

The directions `t_i,t_j` are not parallel, because the two unordered parallel pairs are distinct.

---

## 5. Force balance equalizes opposite transition weights

WM gives the cut force balance

\[
\alpha_i t_i-
\alpha_j t_j+
\alpha_k t_k-
\alpha_\ell t_\ell=0.
\tag{5.1}
$$

Using (4.1),

$$
(\alpha_i-\alpha_k)t_i
+(\alpha_\ell-\alpha_j)t_j=0.
$$

Since `t_i,t_j` are linearly independent,

$$
\boxed{
\alpha_i=\alpha_k=:a,
\qquad
\alpha_j=\alpha_\ell=:b.
}
\tag{5.2}

So each opposite parallel transition pair already has equal KKT weight.

---

## 6. Moment balance equalizes the two pairs

For a transition side `r`, WM writes

\[
m_r=p_r\times t_r.
$$

For the first rectangle pair `(i,k)`, with shell sides `ab,cd` as in Section 2,

$$
m_i+m_k
=a\times t+c\times(-t)
=(a-c)\times t.
$$

In the rectangle this signed quantity has absolute value exactly the separation of the two parallel unit sides,

$$
\boxed{|m_i+m_k|=L=\sqrt{D^2-1}.}
\tag{6.1}
$$

The convex cyclic orientation fixes the same sign convention for the second opposite transition pair. Its rectangle has the same dimensions `1 x L`, so

$$
\boxed{|m_j+m_\ell|=L.}
\tag{6.2}
$$

WM moment balance is

$$
\alpha_i m_i-\alpha_jm_j+\alpha_km_k-\alpha_\ell m_\ell=0.
\tag{6.3}
$$

Insert (5.2):

$$
a(m_i+m_k)=b(m_j+m_\ell).
\tag{6.4}
$$

The two signed couples oppose each other in the positive cut equilibrium, so their magnitudes are equal. By (6.1)-(6.2), both geometric lever arms equal `L`. Hence

$$
aL=bL.
$$

Since `L>0`,

$$
\boxed{a=b.}
$$

Together with (5.2), this proves P2R.4.

Thus the four transition resistances `1/alpha` are also exactly equal.

---

## 7. Four canonical maximal-thrackle completions

Each of the two length-two K-edges has two possible unit-step refinements, corresponding to the two long rectangle sides of length `L=sqrt(D^2-1)`.

The choices at the two independent ties may be made independently. Hence P2 has

$$
\boxed{2\times2=4}
$$

canonical refined antipodal state lists.

Each list consists of

- the `q-2` actual diameter chords in `H`, and
- one chosen short rectangle chord from each tie.

The rotating-calipers support indices remain monotone under either local tie order, so each refined list is a convex thrackle. It has `q` edges on `q` convex vertices, hence is maximal.

Denote the four completions

$$
T^{\epsilon_1,\epsilon_2},
\qquad
\epsilon_s\in\{0,1\}.
$$

By MT, in every completion both added short chords lie on the unique odd cycle and join the two D2 diameter-tree components.

---

## 8. Special rectangle diagonals are leaf edges

Fix one P2 rectangle. Its A-diameter diagonal is, say,

$$
e_A=ac.
$$

The two short completion choices from this rectangle attach to opposite endpoints of `e_A`: one uses A-endpoint `a`, the other uses A-endpoint `c`.

Fix the completion choice at the other rectangle. Compare the two maximal completions obtained by switching only this tie.

In one completion, the unique odd cycle reaches the A-tree through endpoint `a`; in the other, through endpoint `c`. Since `T_A` is a tree, the two corresponding cycle paths through `T_A` cannot both contain the edge `ac`: the path starting at `a` may use `ac`, while the path starting at `c` can begin on the opposite side of that edge, and vice versa. More invariantly, among the two endpoint-to-fixed-endpoint tree paths, exactly one contains the edge `ac` unless the fixed endpoint lies on the edge itself; in that degenerate case the other completion omits it.

Hence there exists at least one maximal completion whose unique odd cycle does not contain `e_A`.

In a maximal convex thrackle, every edge outside the unique odd cycle is a pendant edge. Since both added short chords lie on the cycle, the pendant edge `e_A` is an actual H-edge with a degree-one endpoint already in `H`.

Thus `e_A` is a leaf edge of `T_A`.

The same argument applies to the B-diameter diagonal of this rectangle and to both diameter diagonals from the second rectangle.

Therefore:

$$
\boxed{
\text{all four actual diameter diagonals adjacent to the two P2 ties are H-leaf edges.}
}
\tag{8.1}

---

## 9. Common completion paths contain every nonleaf edge

For one tree component, say `T_A`, each of the four maximal completions contributes a unique tree path between its two chosen A-endpoints of the added short chords. Let

\[
J_A
:=
\bigcap_{\epsilon_1,\epsilon_2}
P_{T_A}
\bigl(a_1^{\epsilon_1},a_2^{\epsilon_2}\bigr),
\tag{9.1}
$$

where `a_s^epsilon` is the A-endpoint selected at tie `s`.

Take any actual A-tree edge

$$
e\notin J_A.
$$

Then some completion cycle omits `e`. In that maximal thrackle, `e` lies outside the unique odd cycle and is therefore pendant. The added edges are on the cycle, so `e` is a leaf edge of the original `T_A`.

Hence every nonleaf A-tree edge lies in `J_A`:

$$
\boxed{
\{e\in E(T_A):e\text{ is not a leaf edge}
\}
\subseteq J_A.
}
\tag{9.2}
$$

The same holds for `T_B` with a common path `J_B`.

Since intersections of tree paths are paths or empty, `J_A,J_B` are each a path, a single vertex, or empty. D2 already makes both diameter components caterpillars; P2R localizes every nonleaf edge to these canonical four-completion intersections.

---

## 10. Exact P2 endpoint package

The P2 phase is therefore constrained simultaneously by:

```text
shell:
  exactly two opposite-parallel unit-side pairs;
  exact gap code (q-4)delta + 2Delta = pi;
  q = pi D-pi/(24D)-1/(2D^2)+O(D^-3);

difference body:
  all vertices lie on the radius-D circle;
  four edges have length 2, all others length 1;

diameter forest:
  T_A disjoint union T_B;
  each parallel rectangle contributes one D-diagonal leaf edge to A and one to B;
  every nonleaf edge lies in canonical common path J_A or J_B;

four-contact body-bar cage:
  the four transition contacts are exactly the two parallel side pairs;
  all four transition alpha weights are equal;

maximal completions:
  four canonical completions, one for each independent tie refinement.
```

This is a finite normal form. It is substantially narrower than generic D2/P2.

---

## 11. Regression audit

### Parallel-pair rectangles

The rectangle argument uses that P2 has no off-circle K-vertices. It does not extend unchanged to PS, where one antipodal K-vertex pair is short.

### Four completion choices

The two short chords from one rectangle are not inserted simultaneously. Each completion chooses exactly one from each rectangle, for two total added edges.

### Leaf-edge conclusion

The claim is that each special actual rectangle diagonal is a leaf edge of `H`, not that both endpoints have diameter degree one. A tree edge may have one leaf endpoint and one internal endpoint.

### Equal transition weights

Only the four A/B transition contact coefficients are shown equal. No claim is made that every shell contact coefficient is uniform.

### Second-order ladder bound

P2R.2 is compatible with R2: here

$$
q_R(D)-q
=2\left(\frac\Delta\delta-2\right)
=\frac1{2D^2}+O(D^{-4}),
$$

well below the general `d_H=2` R2 upper constant `2/D^2`.

---

## 12. Next theorem

The highest-value P2 continuation is now electrical rather than purely metric.

The four transition resistances are equal, and the two rectangle pairs supply two distinguished pairs of crossing actual diameter diagonals, one A-edge and one B-edge per rectangle. WT gives their exact weighted-cycle transfer coefficients in terms of the four arc resistances.

The target is to combine:

1. equality of the four transition resistances;
2. the two rectangle crossing-pair WT formulas;
3. C56-G's strict Robinson/PSD edge-defect kernel;
4. the common path localization `J_A,J_B`.

A sign or equality contradiction would eliminate P2 completely.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P2 has two shell parallel pairs and no short vertices of K=F-F. Each pair creates a
length-2 K edge whose endpoints are radius-D diameter states. Exactly as in P1, its four
primal endpoints form a 1 by sqrt(D^2-1) rectangle; the two diagonals are actual D-edges.

Refine each length-2 edge in either summand order. Independent choices at the two ties
give four q-edge maximal convex-thrackle completions of H. MT forces every added short
rectangle side to join the two D2 diameter-tree components. Therefore, in each rectangle,
its two D-diagonals lie in different components, and its two parallel shell sides are A/B
transition contacts. The two parallel pairs exhaust all four transitions.

Thus with transitions i<j<k<l,
  t_k=-t_i, t_l=-t_j.
WM force balance gives alpha_i=alpha_k and alpha_j=alpha_l. Both parallel pairs are
opposite sides of congruent 1 by sqrt(D^2-1) rectangles, so moment balance gives equality
of the pair weights. Hence all four transition alphas are equal.

K has 2q-8 unit edges and four length-2 edges on the radius-D circle, so exactly
  (q-4)delta+2Delta=pi,
  delta=2asin(1/(2D)), Delta=2asin(1/D),
and
  q=pi D-pi/(24D)-1/(2D^2)+O(D^-3).

Switching either tie changes which endpoint of the corresponding actual rectangle
diagonal enters the completion cycle. Therefore every one of the four special actual
D-diagonals is omitted from some completion cycle and is a leaf edge of H. Every nonleaf
edge of T_A (resp. T_B) lies in the intersection J_A (resp. J_B) of the four completion
paths.

Next: use equal transition resistances + the two rectangle crossing pairs in WT/C56-G.
```
