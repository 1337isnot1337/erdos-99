<!-- theorem-state: {"artifact_id":"ART-58F56A3322D3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — generic-versus-singular classification of extreme positive circuits

**Date:** 2026-09-10  
**Repository state:** PR #178 after QP  
**Run type:** exact rigidity-matroid rank audit  
**Target:** Target C extreme-circuit degeneracy  
**Depends on:** EC actual circuit theorem, CT rank-gap identity, standard planar generic rigidity/Laman characterization  
**External input:** no new specialized theorem beyond standard planar generic rigidity  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

EC shows that every extreme normalized KKT stress has positive support `S` equal to a
circuit of the **actual realized** rigidity-row matroid. Let

\[
\sigma_*:=2v_*-2-|S|\ge0.
\]

There is an exact dichotomy that separates generic combinatorial rigidity from
special-position dependence.

### Theorem GS — generic/singular extreme-circuit dichotomy

Let `M_gen` be the ordinary generic planar rigidity matroid of the abstract selected
mixed graph `S`, and let `M_p` be the row matroid at the actual source placement `p`.
Then:

1. if `sigma_*=0`, `S` is a generic planar rigidity circuit;
2. if `sigma_*>0`, `S` is **generically independent** but is a circuit in `M_p`.

Equivalently,

\[
\boxed{
\operatorname{rank}_{gen}S
=
\operatorname{rank}_{p}S+\mathbf1_{\{\sigma_*>0\}}.
}
\tag{GS.1}
\]

Thus every underbraced extreme positive circuit is created by exactly one unit of rank
loss at the actual geometry. Its large bar-flex deficit `sigma_*` is not a large
algebraic specialization rank loss: generic placement already has `sigma_*-1`
non-rigid flex dimensions, and the source placement creates exactly one additional
mechanism paired with the positive self-stress.

Since the full post-ZF mixed framework has actual rank `2v-3`, which is the maximum
possible planar rank, its generic and actual ranks agree. Therefore if

\[
\kappa_*:=\operatorname{rank}R-\operatorname{rank}_pR_S,
\]

then the generic completion gap is

\[
\boxed{
\operatorname{rank}R-\operatorname{rank}_{gen}R_S
=
\kappa_*-\mathbf1_{\{\sigma_*>0\}}.
}
\tag{GS.2}
\]

This identifies precisely what a high-`sigma_*` QP pivot must change: a codimension-one
special-position circuit singularity sitting inside an otherwise generically
underbraced graph.

---

## 1. Proper selected edge sets are generically independent

EC proves that `S` is an actual circuit. Therefore every proper edge subset

\[
J\subsetneq S
\]

is row-independent at the actual placement `p`.

Row independence at one placement implies generic independence of the same abstract
edge set: a maximal minor of the rigidity matrix is a polynomial in the vertex
coordinates, and if it is nonzero at `p`, it is not the zero polynomial. Hence

\[
\boxed{
J\subsetneq S
\quad\Longrightarrow\quad
J\text{ is independent in }M_{gen}.
}
\tag{1.1}
\]

This direction uses no genericity assumption on the source.

---

## 2. The `sigma_*=0` case is a genuine generic circuit

If `sigma_*=0`, then

\[
|S|=2v_*-2.
\tag{2.1}
\]

A generic planar framework on `v_*` incident vertices has rigidity rank at most
`2v_*-3`, so `S` is generically dependent. By (1.1), every proper subset is
generically independent. Therefore `S` is a circuit of the generic planar rigidity
matroid.

This proves the first half of GS.

---

## 3. An underbraced actual circuit is generically independent

Assume

\[
\sigma_*>0.
\]

Then

\[
|S|=2v_*-2-\sigma_*
\le2v_*-3.
\tag{3.1}
\]

Suppose for contradiction that `S` were generically dependent. By (1.1), every proper
subset is generically independent, so `S` would be a **generic rigidity circuit**.
The standard Laman circuit characterization says a planar generic rigidity circuit on
its incident vertex set has exactly

\[
2v_*-2
\]

edges. This contradicts (3.1).

Hence

\[
\boxed{\operatorname{rank}_{gen}S=|S|.}
\tag{3.2}
\]

EC gives

\[
\operatorname{rank}_{p}S=|S|-1.
\tag{3.3}
\]

Thus the actual source geometry lowers the selected row rank by exactly one. This
proves GS.1 in the underbraced case.

---

## 4. Mechanism count

For a framework on `v_*` vertices, quotient the infinitesimal motion space by the three
Euclidean rigid motions.

If `sigma_*>0`, generic independence gives

\[
\begin{aligned}
\dim\mathcal M_{gen}
&=(2v_*-3)-|S|\\
&=\sigma_*-1.
\end{aligned}
\tag{4.1}
\]

At the actual source placement, EC gives row rank `|S|-1`, so

\[
\begin{aligned}
\dim\mathcal M_p
&=(2v_*-3)-(|S|-1)\\
&=\sigma_*.
\end{aligned}
\tag{4.2}
\]

Therefore

\[
\boxed{
\dim\mathcal M_p-\dim\mathcal M_{gen}=1.
}
\tag{4.3}
\]

The positive KKT circuit stress and the extra infinitesimal mechanism are the unique
Maxwell rank-drop pair introduced by the special source geometry.

ESR's even-shell family is the exact model: it has a linear total flex deficit but
only one more mechanism than its generic abstract graph.

---

## 5. Full-framework generic rank and completion gap

The full mixed framework has actual rigidity rank

\[
\operatorname{rank}_pR=2v-3.
\]

This is the maximum possible rank for a nondegenerate planar framework. Hence the
generic rank of the same abstract mixed graph is also

\[
\boxed{\operatorname{rank}_{gen}R=2v-3.}
\tag{5.1}
\]

Let

\[
\kappa_*
=\operatorname{rank}_pR-\operatorname{rank}_pR_S.
\]

If `sigma_*=0`, GS.1 gives equal selected generic/actual rank, so the generic
completion gap is `kappa_*`.

If `sigma_*>0`, GS.1 gives

\[
\operatorname{rank}_{gen}R_S
=\operatorname{rank}_pR_S+1,
\]

so

\[
\operatorname{rank}_{gen}R-\operatorname{rank}_{gen}R_S
=\kappa_*-1.
\]

This proves GS.2.

### Nullity interpretation

The full generic and actual mixed graphs both have stress-space dimension

\[
s_Z+1.
\]

For an underbraced extreme circuit, the selected graph has

\[
\dim\mathcal S_{gen}(S)=0,
\qquad
\dim\mathcal S_p(S)=1.
\]

So one selected positive stress dimension is created by specialization even though the
**total** full stress nullity does not change. Necessarily, one generic dependence
involving omitted rows is exchanged for this local singular circuit at the actual
placement. QP is the positive-cone mechanism through which such exchanges can occur.

---

## 6. Interaction with QP

Take an underbraced extreme circuit `S`, so `sigma_*>0` and `S` is generically
independent. QP chooses a positive quotient circuit `T` among omitted actual rows and
forms the two-stress union

\[
U=S\cup T.
\]

At the actual placement,

\[
\dim\mathcal S_p(U)=2.
\]

The generic nullity of `U` now distinguishes two structurally different pivots:

1. **generic-crossing pivot:** `U` already contains at least one generic rigidity
   circuit, so part of the second dependence is combinatorial;
2. **double-singular pivot:** `U` is generically independent, so both independent
   actual stress directions are created by special-position rank loss.

The second case means

\[
\operatorname{rank}_{gen}U-\operatorname{rank}_pU=2.
\]

Thus a chain of minimum-`kappa` QP pivots that never reaches a `sigma=0` circuit must
continually transport or accumulate explicit algebraic rank singularities. This is a
more rigid obstruction than arbitrary polytope degeneracy, though it is not yet a
geometric contradiction.

---

## 7. Regressions and limits

- ESR proves that one unit of specialization rank loss can coexist with a large
  `sigma_*`, a two-dimensional force hull, and an affine-kernel PSD stress. Therefore
  GS does not turn the singularity into a finite release by itself.
- A generic rigidity-matroid connectivity theorem cannot simply be substituted for
  the actual row matroid: specialization can create new circuits and can split or
  merge circuit structure. GS keeps the two matroids explicit.
- The full mixed graph itself is generically rigid because its actual rank is already
  maximal. This does not imply that every actual positive circuit is generic.

---

## 8. Exact next target

QP reduces high circuit degeneracy to adjacent positive pivots. GS shows that every
underbraced endpoint of such a pivot contains a codimension-one special-position
rank defect.

The next useful theorem is therefore:

> **Singularity-breaking pivot.** From a minimum-`kappa` underbraced extreme circuit,
> find a QP adjacent pivot whose union contains a generic rigidity circuit in a way
> that forces either `a<t` or the new extreme to have `sigma'=0`.

A weaker quantitative form would suffice: prove that a sequence of `a>=t` pivots
cannot carry `Omega(D)` distinct loaded-terminal/diameter additions while every
endpoint remains an underbraced specialization circuit. LI and ENB provide the
boundary/diameter scale on any low-`kappa` endpoint.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Every extreme KKT support S is an actual rigidity-row circuit (EC). Every proper
subset of S is independent at the actual placement, hence generically independent.

If sigma_*=2v_*-2-|S|=0, then |S|=2v_*-2 and S is a genuine generic planar rigidity
circuit.

If sigma_*>0, then |S|<=2v_*-3. If S were generically dependent, it would be a generic
circuit because all proper subsets are generically independent, but a planar generic
rigidity circuit has 2v_*-2 edges. Contradiction. Therefore S is generically
independent and
    rank_gen(S)=rank_p(S)+1.
So an underbraced extreme is exactly one codimension-one specialization dependency;
its actual mechanism count is sigma_*, versus sigma_*-1 generically.

The full mixed graph has maximal rank 2v-3 both actually and generically. Hence its
generic completion gap from S is
    kappa_*                    if sigma_*=0,
    kappa_*-1                  if sigma_*>0.

Next: combine this singularity classification with QP adjacent pivots to force either
a<t (lower kappa) or a sigma=0 generic circuit endpoint.
```
