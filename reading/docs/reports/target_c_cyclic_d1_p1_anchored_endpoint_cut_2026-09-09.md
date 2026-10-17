> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_p1_anchored_endpoint_cut_2026-09-09.md) · source SHA-256 `1876ed7cb3298528f61df2b9985e590dfae32200b7bd6b7d8a60edfca0320193`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 7 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-F8C842D457EB","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — P1 rectangle diagonals are KKT-frozen leaves and every endpoint cut is side-anchored

**Date:** 2026-09-09  
**Repository branch:** PR #118 after PR/LF/TC/WM  
**Run type:** exact convex-thrackle / KKT endpoint refinement  
**Target:** cyclic primitive phase `d_H=1`, P1  
**Depends on:** PR rectangle/twin completion, LF leaf-edge forcing, TC two-interval cut, WM four-force moment lift  
**Computation:** small abstract convex-thrackle enumeration was used as a regression check before proof; not a proof dependency

## LEVEL I STATUS

`STILL OPEN`

PR gives the P1 rectangle

```math
a,b,c,d
```

in cyclic shell order, with

```math
|ab|=|cd|=1,
\qquad
|ac|=|bd|=D,
\qquad
|ad|=|bc|=\sqrt{D^2-1}.
```

The two short rectangle sides `ad,bc` separately complete the diameter tree `H` to maximal convex thrackles.

This report proves two stronger facts.

1. Each rectangle diagonal `ac,bd` is incident to a full-`H` leaf. Hence its beta coefficient is positive throughout the entire KKT interval.
2. Every zeroed KKT endpoint edge therefore separates the rectangle vertices as
   
   ```math
   \boxed{\{a,c\}\mid\{b,d\},}
   ```

   so the two parallel unit hull sides `ab,cd` are permanently two of the four TC transition contacts.

This converts every P1 KKT endpoint into a four-force wrench system anchored on the same exact rectangle.

---

## 1. Rectangle diagonal `ac` has a leaf endpoint

Assume for contradiction that

```math
\deg_H(a)\ge2,
\qquad
\deg_H(c)\ge2.
\tag{1.1}
```

Choose diameter edges

```math
ax\in H,
\qquad
cy\in H
```
with

```math
ax\ne ac,
\qquad
cy\ne ac.
```

Because `ab` is a unit contact side and `ad` is short, `x` is neither `b` nor `d`; similarly `y` is neither `b` nor `d` in the degenerate ways that would identify one of the rectangle sides.

PR proves that

```math
H+bc
```
is a convex thrackle. The edge `ax` is vertex-disjoint from `bc`, so it must cross `bc` properly. In the cyclic order

```math
a,b,\ldots,c,d,\ldots,
```
this forces

```math
\boxed{x\in(b,c),}
\tag{1.2}
```
where `(b,c)` denotes the open shell arc from `b` to `c`.

Likewise PR proves that

```math
H+ad
```
is a convex thrackle. The edge `cy` is vertex-disjoint from `ad`, so it must cross `ad`. Therefore

```math
\boxed{y\in(d,a).}
\tag{1.3}
```

Now the four endpoints of `ax` and `cy` occur around the convex boundary in the order

```math
a,\ldots,x,\ldots,c,\ldots,y.
```

The chords `ax` and `cy` do **not** have alternating endpoints. They are vertex-disjoint, so they do not meet at an endpoint either. Hence they do not intersect.

But both are diameter edges of `H`, and `H` is a convex geometric thrackle. Any two vertex-disjoint diameter edges must cross properly. Contradiction.

Thus

```math
\boxed{
\min\{\deg_H(a),\deg_H(c)\}=1.
}
\tag{AE.1}
```

By the same argument after the half-turn relabeling

```math
a\leftrightarrow b,
\qquad
c\leftrightarrow d,
```
we obtain

```math
\boxed{
\min\{\deg_H(b),\deg_H(d)\}=1.
}
\tag{AE.2}
```

So both rectangle diagonals `ac` and `bd` are full-`H` leaf edges.

---

## 2. Both rectangle diagonal stresses are frozen positive

LF.1 says every diameter edge incident to a full-`H` leaf occurs with positive coefficient in every normalized cyclic KKT stress.

Applying LF to AE.1-AE.2 gives

```math
\boxed{
\beta_{ac}(s)>0,
\qquad
\beta_{bd}(s)>0
\quad\text{for all }s\in\mathcal S.
}
\tag{AE.3}
```

In particular neither rectangle diagonal can define either endpoint facet of the one-dimensional KKT polytope.

This is stronger than PR's common-path localization: the two most geometrically distinguished diameter edges are removed from the zeroable core altogether.

---

## 3. Every endpoint-zero cut separates the two diagonals as whole pairs

Let

```math
e\in E(H)
```
be any diameter edge with

```math
\beta_e(s)=0
```
at a KKT endpoint stress `s`.

PR says `e` lies on the common twin-cycle path

```math
J=P_H(a,d)\cap P_H(b,c).
```

Therefore deleting `e` separates

```math
a\text{ from }d
```
and
```math
b\text{ from }c.
\tag{3.1}
```

AE.3 gives

```math
e\ne ac,
\qquad
e\ne bd.
```

Because `H` is a tree, `e` is the only full-H edge crossing the component cut of `H-e`. Since `ac` and `bd` remain edges distinct from `e`, their endpoints must lie in common components:

```math
a\sim c,
\qquad
b\sim d
\quad\text{in }H-e.
\tag{3.2}
```

Together with (3.1), the two components therefore separate the rectangle vertices exactly as

```math
\boxed{
\{a,c\}\mid\{b,d\}.
}
\tag{AE.4}
```

No other pairing is possible.

---

## 4. The two parallel unit sides are permanent transition contacts

Traverse the shell counterclockwise from `a`.

By AE.4:

- `a` and `c` have one component color, call it `A`;
- `b` and `d` have the other, call it `B`.

Hence the unit side

```math
ab
```
always crosses the `A|B` cut, and so does the opposite parallel unit side

```math
cd.
```

TC says each component of a zeroed nonleaf tree-edge cut occupies exactly two cyclic intervals. Thus there are exactly four cycle-contact transition sides.

The other two transitions consist of

- one unit shell side `f` on the open boundary chain from `b` to `c`;
- one unit shell side `h` on the open boundary chain from `d` to `a`.

Therefore every P1 endpoint cut has the exact cyclic transition pattern

```math
\boxed{
ab,\ f,\ cd,\ h.}
\tag{AE.5}
```

The first and third transition sides are the fixed parallel rectangle sides; only `f,h` move as the zeroed core edge varies along `J`.

---

## 5. Exact anchored force relation

Orient all shell sides counterclockwise and put

```math
t:=b-a,
\qquad
t_{cd}=d-c=-t.
```

Let

```math
v_r:=\alpha_r t_r
```
be the positive contact-force vector attached to side `r` in the TC convention.

For the component coloring in Section 4, the transition directions alternate `A->B,B->A,A->B,B->A`. The TC cut resultant is

```math
v_{ab}-v_f+v_{cd}-v_h=0.
```

Using `t_cd=-t`,

```math
\boxed{
(\alpha_{ab}-\alpha_{cd})t
=\alpha_f t_f+\alpha_h t_h.
}
\tag{AE.6
}
```

This is the two-dimensional force part of the anchored WM wrench dependence.

Because P1 has a **unique** parallel pair of hull sides, `f` and `h` are not parallel. Therefore the right side of AE.6 cannot vanish: a positive combination of two nonparallel unit vectors cannot equal zero.

Hence every P1 KKT endpoint stress satisfies the strict asymmetry

```math
\boxed{
\alpha_{ab}\ne\alpha_{cd}.
}
\tag{AE.7}
```

The unique parallel primal side pair can never carry equal contact stress at a KKT endpoint.

---

## 6. Moment equation and line-of-action form

WM adds the scalar moment balance. Write the oriented line-wrench vector of a shell side `r` as

```math
\ell_r=(t_{r,x},t_{r,y},p_r\times t_r),
```
where `p_r` is either endpoint of its supporting line.

Then the complete endpoint relation is

```math
\boxed{
\alpha_{ab}\ell_{ab}
-\alpha_f\ell_f
+\alpha_{cd}\ell_{cd}
-\alpha_h\ell_h
=0.
}
\tag{AE.8
}
```

IB proves these four line wrenches have rank exactly three, so their coefficient ratio is unique up to scale.

There is a useful mechanical interpretation. The nonparallel forces on `f,h` have a resultant whose line of action passes through the intersection of the two supporting lines of `f,h`. Equation AE.6 says this resultant is parallel to the rectangle sides. The two forces on `ab,cd` have the opposite horizontal resultant. Thus AE.8 fixes the ratio

```math
\alpha_{ab}:\alpha_{cd}
```
from the height of that `f/h` line intersection relative to the two parallel rectangle support lines.

This gives a direct projective coordinate for comparing the two endpoint stresses along the common path `J`.

---

## 7. Consequence for the two KKT endpoints

The one-dimensional KKT polytope has two distinct coordinate facets. PR places both on `J`; AE excludes `ac,bd` and shows that every chosen endpoint-zero edge gives an anchored cut of the form AE.5.

Thus the two endpoint stresses produce

```math
(ab,f_-,cd,h_-)
```
and
```math
(ab,f_+,cd,h_+)
```
with the same fixed parallel pair and two possibly different moving side pairs.

At each endpoint:

1. the four positive contact weights are the unique WM cofactor ratios for those four lines;
2. `alpha_ab != alpha_cd`;
3. all rectangle-diagonal beta weights remain positive;
4. the selected scalar stress remains C56-G and maximal-rank by CG.

This is a substantially more explicit endpoint system than an arbitrary TC parallelogram.

---

## 8. Regression audit

### Could `ax` equal a short rectangle side?

No. `ad` and `bc` have length `sqrt(D^2-1)<D`, while `ax,cy` are chosen from the actual diameter graph.

### Could the contradiction chords share an endpoint?

No. The forced open arcs `(b,c)` and `(d,a)` are disjoint and exclude `a,c`; hence `ax` and `cy` are vertex-disjoint.

### Could `f,h` be parallel?

P1 has exactly one unordered pair of parallel primal hull sides, namely `ab,cd`. Since `f,h` are different transition sides on the two long arcs, they cannot form a second parallel pair.

### Does AE require only one beta zero at an endpoint?

No. Pick any zeroed nonleaf edge `e`. Other zero beta coordinates do not alter the full-tree component cut `H-e`, and the summed-equilibrium argument still applies.

---

## 9. Next theorem

P1 is now reduced to a nested sequence of anchored four-line self-stresses along one common tree path.

The best next target is a **two-cut monotonicity theorem**:

> as `e` moves along the common path `J`, the two moving shell transitions `f(e),h(e)` move monotonically along the two long rectangle boundary arcs. Prove that the WM line-of-action formula makes the ratio `alpha_ab/alpha_cd` strictly monotone in the same order.

If the two KKT-polytope endpoints correspond to opposite ends of the allowed coordinate interval, this monotonicity can be compared with the fact that every alpha coordinate itself varies affinely along the one-dimensional stress segment.

A second target is to insert AE.6-AE.8 directly into WT. The two frozen rectangle diameter edges `ac,bd` have four cyclic resistance arcs in which the first and third arcs are the single resistances

```math
r_{ab}=1/\alpha_{ab},
\qquad
r_{cd}=1/\alpha_{cd}.
```

Thus their transfer is an explicit expression involving the anchored unequal pair and the two long-arc resistance sums.

---

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

P1 rectangle: ab,cd are opposite unit sides; ac,bd are D-diagonals; ad,bc are short
antipodal sides sqrt(D^2-1). Both H+ad and H+bc are maximal convex-thrackle completions.

New leaf theorem:
If both a and c had another H-neighbor, addability of bc forces ax to cross bc, hence
x lies on open arc (b,c). Addability of ad forces cy to cross ad, hence y lies on
(d,a). Then diameter edges ax and cy are vertex-disjoint but have nonalternating
endpoints, so they do not cross: contradiction. Thus ac has a full-H leaf endpoint.
Symmetrically bd does too. LF freezes beta_ac,beta_bd>0 throughout the KKT interval.

For any endpoint-zero edge e on the PR common path J, e is distinct from ac,bd.
Since e separates a-d and b-c but cannot split ac or bd, the H-e components contain
  {a,c} | {b,d}.
Therefore TC's four transition contacts are always
  ab, f, cd, h,
where f lies on the b->c chain and h on the d->a chain.
With t_ab=t and t_cd=-t, endpoint force balance is
  (alpha_ab-alpha_cd)t = alpha_f t_f + alpha_h t_h.
The unique-parallel-pair hypothesis makes t_f,t_h nonparallel, hence
  alpha_ab != alpha_cd
at every KKT endpoint. WM supplies the corresponding unique moment/cofactor ratio.

Next: prove monotonicity of that four-line ratio along J, or insert the anchored
weights into WT for the frozen diameter pair ac,bd.
```
