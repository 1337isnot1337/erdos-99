<!-- theorem-state: {"artifact_id":"ART-6C694D2C1FB2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — extreme normalized KKT stresses are positive rigidity circuits

**Date:** 2026-09-10  
**Repository state:** PR #178 branch, using the merged C53/C65/ZF/ES stack on `main` as dependencies  
**Run type:** exact convex-dual / rigidity-matroid sharpening  
**Target:** Target C, C-II after ZF  
**Depends on:** C53 universal selected-stress PSD, C65 full actual support, ZF full mixed rigidity, ES normalized stress polytope  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The ES report proves that the normalized nonnegative KKT stress polytope

\[
\mathcal P=
\{x=(\alpha,\beta)\ge0:R^T(\alpha,-\beta)=0,\ \sum_H\beta=1\}
\]

has affine dimension `s_Z`, and that every vertex of `P` has at most `2v-2`
positive coordinates. The stronger fact is that an extreme support is a genuine
circuit of the actual bar-rigidity row matroid.

Let `x*` be a vertex of `P` and let

\[
S:=\operatorname{supp}x^*.
\]

Write `R_S` for the ordinary signed bar-rigidity rows indexed by `S` (after changing
the sign of diameter coordinates in the stress vector). Then

\[
\boxed{\dim\ker R_S^T=1,}
\tag{EC.1}
\]

and every proper subset of `S` is row-independent. Hence

\[
\boxed{S\text{ is a rigidity-matroid circuit}.}
\tag{EC.2}
\]

This turns every extreme selected KKT stress into a minimal positive dependence, not
merely a sparse one.

For the positive selected support, let

- `v_*` be the number of vertices incident to `S`;
- `e_*` be the number of positive contact edges;
- `h_*` be the number of positive diameter edges;
- `b_*` be the outer-face walk length of the connected positive contact graph;
- `Q_*:=sum_F(deg F-4)` over its bounded faces;
- `sigma_*:=2v_*-2-(e_*+h_*)`.

The canonical support theorem says the positive contact support is one connected
nontrivial component, contains every positive diameter endpoint, and spans Euclidean
diameter `D`. Therefore all edges of `S` live on this same `v_*`-vertex support.
The circuit bound gives `sigma_*>=0`, and planar Euler counting gives the exact identity

\[
\boxed{b_*+Q_*=2h_*+2\sigma_*.}
\tag{EC.3}
\]

Thus an extreme selected support has two statuses:

1. `sigma_*=0`: a maximal planar rigidity circuit with `e_*+h_*=2v_*-2`, lying on
   the exact face equality `b_*+Q_*=2h_*`;
2. `sigma_*>0`: an underbraced positive circuit with
   `b_*+Q_*>2h_*`, whose bar framework has exactly `sigma_*` non-rigid infinitesimal
   degrees of freedom beyond Euclidean motions.

The second case does **not** by itself close Level I because the omitted actual C65
constraints can block those selected-support flexes. Later CT/TP/ESR reports quantify
this obstruction and give an exact two-dimensional regression.

---

## 1. Extreme vertices have one-dimensional supported stress space

Let

\[
W_S:=\{w:\operatorname{supp}w\subseteq S,\ R^Tw=0\}.
\]

Here the coordinates of `w` use the same signed convention as the KKT stress, so the
strictly positive KKT vector `x*` corresponds to a nonzero vector in `W_S` after the
fixed contact/diameter sign change.

### Theorem EC.1

For every vertex `x*` of the normalized KKT polytope,

\[
\dim W_S=1.
\]

### Proof

Certainly `dim W_S>=1` because `x*` itself is a nonzero supported equilibrium stress.
Suppose `dim W_S>=2`. Choose `w in W_S` not proportional to `x*`.

Let

\[
L(\alpha,\beta)=\sum_{h\in H}\beta_h.
\]

The normalized vertex satisfies `L(x*)=1`. Put

\[
w_0:=w-L(w)x^*.
\]

Then

\[
R^Tw_0=0,
\qquad
L(w_0)=0,
\qquad
\operatorname{supp}w_0\subseteq S.
\]

Also `w_0!=0`, because otherwise `w` would be proportional to `x*`.

Every coordinate of `x*` on `S` is strictly positive, and every coordinate outside
`S` is zero for both `x*` and `w_0`. Hence for sufficiently small `t>0`, both

\[
x^*+tw_0,
\qquad
x^*-tw_0
\]

remain nonnegative, normalized, and in equilibrium. They are distinct points of
`P` whose midpoint is `x*`, contradicting extremality. Therefore `dim W_S=1`.
`square`

---

## 2. Minimality of the row dependence

### Corollary EC.2

Every proper subset `T proper subset S` is row-independent.

### Proof

If `R_T` were dependent, there would be a nonzero self-stress `u` supported on `T`.
Extend `u` by zero to `S`. Then `u in W_S`.

By EC.1, `W_S=span{x*}`. But `x*` is nonzero on every coordinate of `S`, while `u`
vanishes on the nonempty set `S\T`; they cannot be proportional. Contradiction.
`square`

Thus `S` is an ordinary rigidity-matroid circuit. Positivity of the KKT coordinates
adds the oriented sign pattern: the unique circuit dependence has one sign on contact
rows and the opposite sign on diameter rows.

This is strictly stronger than ES.3. ES.3 bounds the cardinality of an extreme
support using ambient polytope dimension; EC identifies its internal linear matroid
structure exactly.

---

## 3. The circuit lives on one connected diameter-spanning selected core

For any normalized selected KKT stress, the canonical support theorem gives exactly
one nontrivial positive contact component, every positive diameter endpoint lies in
that component, and the component spans Euclidean diameter `D`.

Every edge in `S` is either a positive contact or positive diameter edge. Therefore
all vertices incident to `S` lie in that one component. In particular the selected
contact graph `C_*` is connected on the `v_*` support vertices and has Euclidean
diameter `D`.

No full-force-bulk assertion is made: actual C65 core vertices on which this extreme
stress vanishes are simply absent from `v_*`.

---

## 4. Circuit size and flex deficit

Since `S` is a circuit,

\[
\operatorname{rank}R_S=|S|-1=e_*+h_*-1.
\tag{4.1}
\]

A planar bar framework on `v_*` vertices has rigidity rank at most `2v_*-3` because
the selected support spans a nondegenerate diameter configuration. Therefore

\[
e_*+h_*-1\le2v_*-3,
\]

so

\[
\boxed{e_*+h_*\le2v_*-2.}
\tag{4.2}
\]

Define

\[
\boxed{\sigma_*:=2v_*-2-(e_*+h_*)\ge0.}
\tag{4.3}
\]

Then

\[
\operatorname{rank}R_S=2v_*-3-\sigma_*.
\tag{4.4}
\]

Hence the infinitesimal motion space of the selected equality framework has dimension

\[
2v_*-(2v_*-3-\sigma_*)=3+\sigma_*.
\]

After quotienting the three Euclidean rigid motions, the selected support has exactly

\[
\boxed{\sigma_*}
\tag{4.5}
\]

non-rigid infinitesimal degrees of freedom.

Thus `sigma_*` has three simultaneous meanings:

1. deficit of the extreme circuit from the maximal `2v_*-2` planar circuit size;
2. excess of the selected face ledger over the equality wall, below;
3. dimension of the non-rigid infinitesimal selected-support flex space.

---

## 5. Exact selected-support face identity

Because the positive selected contact graph is connected and triangle-free, its
bounded face degrees are at least four. Standard Euler/face-incidence counting gives

\[
\boxed{e_*=2v_*-2-\frac{b_*+Q_*}{2}.}
\tag{5.1}
\]

On the other hand, (4.3) gives

\[
e_*=2v_*-2-\sigma_*-h_*.
\tag{5.2}
\]

Equating (5.1) and (5.2) yields

\[
\boxed{b_*+Q_*=2h_*+2\sigma_*.}
\tag{5.3}
\]

This is exact and finite.

### Corollary EC.3 — equality wall iff maximal circuit

\[
\boxed{b_*+Q_*=2h_*
\iff
\sigma_*=0
\iff e_*+h_*=2v_*-2.}
\tag{5.4}
\]

### Corollary EC.4 — every underbraced extreme support is strictly on the desired face side

If `sigma_*>0`, then

\[
\boxed{b_*+Q_*>2h_*.}
\tag{5.5}
\]

This resembles the full-source C-II closing inequality, but it is a statement for the
selected extreme support only. The full actual C65 graph still obeys

\[
b+Q=2h-2s_Z.
\]

There is no contradiction until one controls the omitted actual constraints.

---

## 6. Local sparsity on every proper selected subframework

Circuit minimality immediately gives a selected-support analogue of the SZ local
component inequality without assuming full `s_Z=0`.

Let `U` be a proper subset of the selected support vertices and let `E_S(U)` be the
selected mixed edges with both endpoints in `U`. Since `E_S(U)` is a proper subset of
the circuit, it is independent. Therefore

\[
\boxed{|E_S(U)|\le2|U|-3}
\tag{6.1}
\]

whenever `|U|>=2`; if the realization on `U` is degenerate the true rank bound is only
smaller.

More generally, any proper selected edge set on `r` incident vertices has at most
`2r-3` rows. This is an exact matroid statement in the actual realization, not a
generic Laman assumption.

---

## 7. Relation to `s_Z`

ES proves that the full normalized stress polytope has dimension `s_Z` and every
extreme vertex omits at least `s_Z` actual rows. EC now says those surviving rows form
one circuit.

Thus every post-ZF source, including `s_Z>0`, admits a family of positive selected
rigidity circuits whose union covers the relative-interior full support. The
full-support KKT stress is a convex combination of at most `s_Z+1` extreme circuits,
and ES gives

\[
\ker\Omega(x^0)=\bigcap_r\ker\Omega(x^{(r)}).
\]

The remaining structural problem can therefore be restated without a vague
"high-dimensional stress space":

> how can a collection of positive diameter-spanning selected rigidity circuits, each
> individually obeying (5.3), cover the full C65 mixed graph whose exact face defect is
> on the opposite side by `2s_Z`?

Any closure along this route must use compatibility between those circuits, not merely
count the rows each one omits.

---

## 8. Regression audit

| Regression / issue | Result |
| --- | --- |
| extreme stress may have larger scalar PSD kernel | allowed; EC concerns rigidity-row dependence, not stress-matrix nullity |
| selected support may omit actual C65 core vertices | allowed; `v_*` counts only incident selected vertices |
| support may have fewer than `2v_*-2` edges | allowed and measured exactly by `sigma_*` |
| underbraced selected circuit immediately closes Level I | false; omitted strong actual constraints may block its flexes |
| regular even-shell circuit | binding regression: `sigma=N/2-2` while the support is 2D and its PSD stress kernel is exactly affine; see ESR |
| regular odd shell | compatible; exploratory exact-rank checks show its positive extreme circuits are maximal, not a counterexample |
| generic Laman assumptions | not used; independence follows from circuit minimality in the actual row matroid |

---

## 9. Corrected next lemma

The original version of EC proposed a blanket flex-cover lemma for every underbraced
extreme circuit. ESR shows why this is the wrong level of generality: a regular even
shell is a genuinely two-dimensional positive PSD circuit with a linear bar-flex
deficit and no extra scalar stress-matrix kernel.

CT supplies the exact degeneracy parameter

\[
\kappa_*:=z_*-s_Z=2(v-v_*)+\sigma_*.
\]

TP supplies the geometric tradeoff: if `h_*/D->y` and `sigma_*/D->s`, then

\[
y+s
\ge
\sqrt{1+\frac{\sqrt3}{2}\sin(\min\{y,\pi/2\})}.
\]

Therefore the live structural target is:

> **Extreme-circuit degeneracy transfer.** Show that the full-support C65 KKT cone
> contains at least one extreme positive circuit with `kappa_*=o(D)`, or prove that
> `kappa_*=Omega(D)` for every extreme circuit forces a contradiction using omitted
> full actual rows / whole-source capacity.

The first outcome immediately forces a selected extreme support with at least
`(1.3589183533-o(1))D` positive diameter bars by TP. The second is where the full
actual graph, rather than the selected circuit alone, must enter.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a vertex x* of the normalized nonnegative KKT stress polytope, S=supp(x*) has
one-dimensional supported self-stress space. Otherwise a second supported stress can
be normalized to zero beta-sum and used to perturb x* in both signs. Therefore every
proper subset of S is independent: S is an actual rigidity-matroid circuit.

With v_*,e_*,h_* and
    sigma_*=2v_*-2-(e_*+h_*)>=0,
rank R_S=e_*+h_*-1=2v_*-3-sigma_*, and Euler gives exactly
    b_*+Q_*=2h_*+2sigma_*.

CT:
    z_*-s_Z=2(v-v_*)+sigma_*.
TP:
    if h_*/D->y and sigma_*/D->s,
    y+s >= sqrt(1+(sqrt3/2)sin(min(y,pi/2))).
ESR blocks the false shortcut `sigma_*>0 -> 1D/extra PSD kernel`.

Next: force one extreme circuit with kappa_*=z_*-s_Z=o(D), or use the omitted full
C65 rows to contradict uniform linear kappa_*.
```
