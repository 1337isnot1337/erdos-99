> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_weighted_cycle_transfer_2026-09-09.md) · source SHA-256 `14dd5b9e30b8cfb171e3b309bbc2cdf0919209a733d8c0de503c9f17303a9281`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 9 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-0F149E05BB71","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic endpoint: exact weighted-cycle transfer formulas

**Date:** 2026-09-09  
**Repository base:** PR #118 after TC  
**Run type:** exact electrical reduction  
**Target:** cyclic endpoint / C56-G endpoint analysis  
**Depends on:** CY full positive contact cycle and standard Laplacian effective-resistance identities  
**External web search:** not used in the proof  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

In the cyclic primitive endpoint every normalized KKT stress has positive contact graph exactly `C_q`. There are no positive-contact interior vertices. Therefore the C53/C56 transfer matrix can be written explicitly in the edge resistances of one weighted cycle.

Let the unit cycle edges in cyclic order have conductances

```math
\alpha_0,\ldots,\alpha_{q-1}>0
```

and resistances

```math
r_i:=\alpha_i^{-1}.
```

For a cyclic boundary arc `I`, write

```math
R(I):=\sum_{i\in I}r_i,
```

and let

```math
R:=\sum_{i=0}^{q-1}r_i.
```

Then:

1. effective resistance across a terminal pair is the parallel combination of the two cycle arcs;
2. transfer between two crossing diameter chords is an exact difference of opposite arc products;
3. transfer between two chords sharing an endpoint has exact magnitude equal to a product of the two exterior arc resistances divided by `R`.

These formulas convert the C56 transfer phase into finite multiplicative inequalities on cyclic resistance arcs.

---

## 1. Effective resistance on a weighted cycle

Let `x,y` be two terminals. The two simple `x-y` arcs of the cycle have total resistances

```math
s,
\qquad
R-s.
```

They are in parallel, so

```math
\boxed{
W_{xy}=\frac{s(R-s)}{R}.}
\tag{WT.1}
```

This formula is independent of which of the two arcs is called `s`.

Let `Lambda` be the weighted cycle Laplacian and `Lambda^+` its pseudoinverse. For oriented terminal pairs

```math
e=(a,b),
\qquad
f=(c,d),
```

put

```math
q_e=e_a-e_b,
\qquad
q_f=e_c-e_d.
```

The transfer coefficient is

```math
K_{ef}=q_e^{\mathsf T}\Lambda^+q_f.
\tag{1.1}
```

The standard resistance polarization identity gives

```math
\boxed{
K_{ef}
=\frac12
\left(
W_{ad}+W_{bc}-W_{ac}-W_{bd}
\right).}
\tag{WT.2}
```

### Proof

Using

```math
W_{xy}
=\Lambda^+_{xx}+\Lambda^+_{yy}-2\Lambda^+_{xy},
```

the diagonal terms cancel in the displayed combination and leave

```math
\Lambda^+_{ac}-\Lambda^+_{ad}-\Lambda^+_{bc}+\Lambda^+_{bd}
=q_e^{\mathsf T}\Lambda^+q_f.
```
`\square`

---

## 2. Two vertex-disjoint crossing chords

Assume the four endpoints occur in cyclic order

```math
a<c<b<d.
```

Let the four consecutive cycle-resistance arcs be

```math
A=R(a,c),
\quad
B=R(c,b),
\quad
C=R(b,d),
\quad
D=R(d,a),
```

so

```math
R=A+B+C+D.
```

Choose chord orientations

```math
e=(a,b),
\qquad
f=(c,d).
```

Using WT.1,

```math
\begin{aligned}
W_{ad}&=\frac{D(A+B+C)}R,\\
W_{bc}&=\frac{B(A+C+D)}R,\\
W_{ac}&=\frac{A(B+C+D)}R,\\
W_{bd}&=\frac{C(A+B+D)}R.
\end{aligned}
```

Substitute into WT.2. The numerator is

```math
2(BD-AC),
```

so:

### Theorem WT.1 — crossing-chord product formula

```math
\boxed{
K_{(a,b),(c,d)}
=\frac{BD-AC}{A+B+C+D}.}
\tag{WT.3}
```

Reversing either chord orientation changes the sign, as it must.

Hence the unsigned zero-transfer condition between these two crossing chords is exactly

```math
\boxed{AC=BD.}
\tag{WT.4}
```

For the displayed orientation,

```math
\boxed{
K_{ef}<0
\iff
AC>BD.}
\tag{WT.5}
```

Thus negative transfer is a strict multiplicative imbalance between opposite cyclic resistance-arc products.

---

## 3. Two chords sharing one endpoint

Now let the two chords be

```math
e=(a,b),
\qquad
f=(a,c),
```

and suppose the cyclic order is

```math
a<c<b.
```

Let

```math
A=R(a,c),
\quad
B=R(c,b),
\quad
C=R(b,a),
```

with

```math
R=A+B+C.
```

WT.2 becomes

```math
K_{ef}
=\frac12(W_{ac}+W_{ab}-W_{bc}).
```

Using WT.1 and simplifying gives:

### Theorem WT.2 — shared-endpoint product formula

With both chords oriented away from their common endpoint `a`,

```math
\boxed{
K_{(a,b),(a,c)}
=\frac{AC}{A+B+C}>0.}
\tag{WT.6}
```

Again reversing one orientation changes the sign.

The transfer magnitude is therefore

```math
\boxed{|K_{ef}|=AC/R.}
\tag{WT.7}
```

No shared-endpoint pair has zero transfer in the weighted positive cycle.

---

## 4. General cross-ratio interpretation

For four alternating endpoints, WT.3 can be normalized by `R`:

```math
K_{ef}
=R\left(
\frac BR\frac DR
-
\frac AR\frac CR
\right).
```

Thus transfer sign compares the two products of opposite normalized resistance arcs.

Equivalently, defining the positive ratio

```math
\chi:=\frac{AC}{BD},
```

we have

```math
\operatorname{sgn}K_{ef}
=\operatorname{sgn}(1-\chi)
```

for the displayed orientation.

The zero-transfer equality `chi=1` is a multiplicative four-arc balance, not an additive length equality.

---

## 5. Consequence for C56-G on the cycle

CG proves that every selected cyclic stress is in C56-G, never C56-Z. Therefore the projectively ordered selected diameter system has a strictly negative minimum off-diagonal transfer after the canonical C56 orientation.

WT now identifies every candidate source of that negative minimum explicitly:

- a shared-endpoint pair contributes a nonzero transfer with magnitude `AC/R`, with sign determined only by the orientation choices;
- a vertex-disjoint pair is necessarily a crossing pair in the diameter thrackle and contributes `(BD-AC)/R`.

Thus the generic phase is controlled by finitely many strict inequalities between products of cycle-resistance arc sums.

No matrix inversion remains in the cyclic endpoint once the contact stresses are known.

---

## 6. Tree-endpoint interface

In TC, a zeroed full diameter-tree edge at a KKT endpoint gives a `2+2` cyclic cut and an exact reciprocal-force parallelogram

```math
v_i+v_k=v_j+v_\ell,
\qquad
v_r=\alpha_r t_r.
\tag{6.1}
```

WT provides the complementary electrical language in the reciprocal edge variables

```math
r_r=1/\alpha_r.
```

The primal equality (6.1) is linear in the conductances `alpha`, while WT.3 is multiplicative in sums of their reciprocals. This mismatch is potentially rigid: the same endpoint stress must satisfy both simultaneously, together with C56-G's strict negative-transfer ordering.

The next tree-endpoint theorem should exploit this conductance/resistance duality rather than another abstract rank count.

---

## 7. Selected perfect matching specialization

Suppose a selected diameter support is a perfect matching on `q=2m` cyclic terminals. Pairwise crossing of all diameter chords forces, after cyclic relabeling, the matching

```math
(i,i+m),
\qquad 0\le i<m.
```

For such a matching, every off-diagonal transfer is given by WT.3. The entire C56 matrix is therefore an explicit function of the `2m` positive cycle resistances.

In particular, C56-Z would require the product balance `AC=BD` for **every** pair of matching chords. CG excludes this simultaneous system for the cyclic global-minimizer endpoint. Any future selected-matching classification can work directly with these product equations/inequalities.

---

## 8. Regression audit

### Equal-resistance regular cycle

WT.3 reduces to a difference of products of integer arc lengths. Symmetric chord pairs may have zero transfer, while the full selected system need not be in C56-Z. CG only excludes simultaneous all-pair zero transfer.

### Four-cycle opposite pair

The equal weighted four-cycle with two crossing opposite chords realizes the small-support zero-transfer regression. WT.3 gives `AC=BD` exactly. This lies below the large cyclic endpoint hypotheses and is retained.

### Orientation

The sign of `K_ef` depends on the orientation of each incidence vector. WT.3 always states the displayed orientation explicitly. Only zero/nonzero status and absolute magnitude are orientation-invariant.

---

## 9. Next theorem

For the connected-tree `d_H=1` cyclic branch, combine:

1. TC endpoint cut: one beta-zero nonleaf tree edge gives a `2+2` cyclic partition and reciprocal parallelogram;
2. WT: every remaining selected diameter transfer is a four-arc product expression;
3. CG: the endpoint stress is C56-G with exact two-dimensional edge kernel and maximal scalar rank.

The desired result is a finite incompatibility between the parallelogram conductance equality and the strict Robinson/C56 product inequalities forced by the remaining diameter-tree edges.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

WT.1-WT.2 are elementary and self-contained; their Target C consequences depend on report-level CG/TC.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cyclic contact network = weighted cycle, r_i=1/alpha_i, total R.
For any pair x,y whose two arc resistances are s,R-s:
  W_xy=s(R-s)/R.
For oriented chords e=(a,b), f=(c,d):
  K_ef=1/2(W_ad+W_bc-W_ac-W_bd).

If a<c<b<d and the four cyclic resistance arcs are A,B,C,D:
  K_ef=(BD-AC)/(A+B+C+D).
Thus zero transfer iff AC=BD and, for the displayed orientation,
  K_ef<0 iff AC>BD.

If e=(a,b), f=(a,c), a<c<b, with arcs A,B,C and both oriented away from a:
  K_ef=AC/(A+B+C)>0.

So C56 transfer on the cyclic endpoint is an explicit multiplicative cross-ratio
system in cycle-resistance sums. No Schur inversion is needed.

TC endpoint cuts simultaneously give a reciprocal parallelogram linear in alpha.
Next: combine that conductance equality with these reciprocal-resistance product
inequalities to close the d_H=1 connected-tree branch.
```
