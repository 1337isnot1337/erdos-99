<!-- theorem-state: {"artifact_id":"ART-3FF535CAC3BD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — extreme-circuit completion budget and selected Woodall topology

**Date:** 2026-09-10  
**Repository state:** PR #178 after EC; uses Woodall report `1adc420e` from current `main`  
**Run type:** exact matroid/topology synthesis  
**Target:** Target C, C-II after ZF  
**Depends on:** ZF, ES, EC, canonical positive-support connectivity, force-hull boundary order, Woodall diameter-thrackle classification  
**External input:** none beyond the already imported Woodall theorem  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

Let the full C65 mixed equality graph have `v` nonisolated vertices, `e` contact edges,
`h` actual diameter edges, and mixed surplus

\[
s_Z=e+h-(2v-2)\ge0.
\]

Let `x*` be an extreme normalized KKT stress. By EC its positive mixed support `S` is
an actual rigidity-matroid circuit. Write

- `v_*` for the number of vertices incident with `S`;
- `e_*`,`h_*` for its positive contact and diameter edges;
- `q_*` for its positive diameter endpoints;
- `sigma_*:=2v_*-2-(e_*+h_*)>=0` for its circuit flex deficit.

Then the number `z_*` of full actual mixed rows omitted by this extreme stress is not
merely bounded below by `s_Z`. It is exactly

\[
\boxed{
z_*=(e+h)-(e_*+h_*)
=2(v-v_*)+s_Z+\sigma_*.
}
\tag{CT.1}
\]

The excess over the ES lower bound has a precise rank meaning:

\[
\boxed{
z_*-s_Z=2(v-v_*)+\sigma_*
=\operatorname{rank}R-\operatorname{rank}R_S.
}
\tag{CT.2}
\]

Thus an extreme stress omits exactly `s_Z` rows if and only if it is simultaneously
full-vertex and a maximal planar circuit:

\[
\boxed{
z_*=s_Z
\iff v_*=v\text{ and }\sigma_*=0.
}
\tag{CT.3}
\]

This separates two fundamentally different reasons for sparsification: the inevitable
`s_Z` redundant-row deletion, versus actual loss of rigidity rank caused by omitted
vertices or an underbraced circuit.

Woodall applies independently to the selected positive diameter graph `H_*`, because
it is still a straight-line subthrackle of the source diameter graph. Put

\[
d_*:=q_*-h_*\ge0.
\]

Then exactly one of the following occurs:

1. `d_*=0`: `H_*` is connected and consists of one odd cycle with possible pendant
   leaves attached directly to that cycle;
2. `d_*>0`: `H_*` is a caterpillar forest with exactly `d_*` components.

Combining this with the EC selected face identity gives the exact selected terminal
ledger

\[
\boxed{
q_*=x_*+Q_*+2d_*-2\sigma_*,
}
\tag{CT.4}
\]

where `x_*:=b_*-q_*>=0` and `Q_*` is the bounded-face degree defect of the positive
selected contact support.

Equivalently,

\[
\boxed{
q_*+2\sigma_*=x_*+Q_*+2d_*.
}
\tag{CT.5}
\]

So every selected flex-deficit unit consumes two units of the same outer/face/diameter-
component budget that pays for the loaded terminal set. This is the selected-support
counterpart of the full post-ZF terminal partition, but with `sigma_*` on the opposite
side.

---

## 1. Exact omitted-row identity

ZF gives for the full actual mixed framework

\[
e+h=2v-2+s_Z.
\tag{1.1}
\]

EC gives for an extreme support circuit

\[
e_*+h_*=2v_*-2-\sigma_*.
\tag{1.2}
\]

Subtract (1.2) from (1.1):

\[
\begin{aligned}
z_*
&=(e+h)-(e_*+h_*)\\
&=(2v-2+s_Z)-(2v_*-2-\sigma_*)\\
&=2(v-v_*)+s_Z+\sigma_*.
\end{aligned}
\]

This proves CT.1.

For the rank statement, ZF gives

\[
\operatorname{rank}R=2v-3,
\]

while EC circuit minimality gives

\[
\operatorname{rank}R_S=e_*+h_*-1=2v_*-3-\sigma_*.
\]

Subtracting proves CT.2. Since both `v-v_*` and `sigma_*` are nonnegative integers,
CT.3 follows.

### Interpretation

Among the `z_*` omitted full rows, exactly

\[
2(v-v_*)+\sigma_*
\]

independent rank units are needed merely to recover the full ZF rigidity rank. The
remaining exactly `s_Z` omitted rows are the full framework's redundant dependence
surplus. Therefore a highly sparse extreme stress does not automatically represent a
large redundant face of the same rigid framework: some of its zeros may only be
paying to restore missing vertices or selected-support flexes.

---

## 2. Woodall applies to every selected positive diameter support

Every positive selected diameter edge is an actual source diameter edge. Two such
straight segments sharing no endpoint cross, while two sharing an endpoint meet there.
Thus `H_*` is a finite straight-line thrackle.

Every vertex counted in `q_*` has positive selected diameter degree. Woodall's
classification therefore gives two cases.

### CT-C: selected cyclic case

If `H_*` contains an odd cycle, every selected diameter endpoint is adjacent to that
cycle. Counting the cycle edges and one incident edge for every outside vertex gives
`h_*>=q_*`. Hopf-Pannwitz gives `h_*<=q_*`. Hence

\[
\boxed{h_*=q_*,\qquad d_*=0.}
\tag{2.1}
\]

There is exactly one odd cycle and every vertex off it is a pendant leaf.

### CT-F: selected forest case

If no odd cycle occurs, `H_*` is a disjoint union of caterpillars. If it has `c_*`
components, then

\[
h_*=q_*-c_*.
\]

Therefore

\[
\boxed{d_*=c_*>0.}
\tag{2.2}
\]

The same exact topology switch used on the full diameter graph thus exists on every
extreme positive support.

---

## 3. Exact selected terminal ledger

Every positive diameter endpoint is a distinct convex vertex of the selected force
hull. Along the outer face of the connected selected positive contact graph, these
`q_*` vertices occur cyclically. Write

\[
\boxed{x_*:=b_*-q_*\ge0.}
\tag{3.1}
\]

EC proves

\[
b_*+Q_*=2h_*+2\sigma_*.
\tag{3.2}
\]

Use `b_*=q_*+x_*` and `h_*=q_*-d_*`:

\[
q_*+x_*+Q_*
=2q_*-2d_*+2\sigma_*.
\]

Rearranging gives CT.4 and CT.5.

### Cyclic specialization

If `d_*=0`,

\[
\boxed{q_*+2\sigma_*=x_*+Q_*.}
\tag{3.3}
\]

Thus an underbraced cyclic extreme circuit requires outer-walk plus bounded-face
defect strictly exceeding the entire selected loaded-terminal count.

### Forest specialization

If `H_*` is a caterpillar forest with `d_*` components,

\[
\boxed{q_*+2\sigma_*=x_*+Q_*+2d_*.}
\tag{3.4}
\]

Each selected diameter component supplies exactly two units of the topology budget.

---

## 4. Immediate constraints on the flex deficit

Since all terms in CT.5 are nonnegative,

\[
\boxed{
2\sigma_*\le x_*+Q_*+2d_*.
}
\tag{4.1}
\]

More sharply, CT.5 determines `sigma_*` exactly once the selected outer/face/diameter
ledger is known:

\[
\boxed{
\sigma_*
=\frac{x_*+Q_*+2d_*-q_*}{2}.
}
\tag{4.2}
\]

In particular the selected topology obeys the parity constraint

\[
\boxed{x_*+Q_*-q_*\equiv0\pmod2,}
\tag{4.3}
\]

because `2d_*-2sigma_*` is even.

This parity is weak asymptotically but is exact and can be useful in finite circuit
classification.

---

## 5. Why this does not yet close `s_Z>0`

One might hope that every extreme stress has `z_*=s_Z`, which would reduce all
extremes to full-vertex maximal circuits. CT.3 shows precisely what must be proved for
that hope: every extreme support must use every full core vertex and have
`sigma_*=0`.

Neither follows from polytope dimension alone. A vertex of a standard-form
nonnegative polytope can be degenerate, and the C54 one-dimensional chain stress is a
concrete warning that a positive PSD extreme circuit can be heavily underbraced in
principle.

Likewise, EC.5.5 for `sigma_*>0` is only a selected-support face inequality. The
omitted actual C65 rows can supply exactly the rank completion in CT.2 and block every
selected flex.

The new value is that this obstruction is now quantified exactly rather than hidden
inside the phrase "many zero multipliers".

---

## 6. Next theorem

The high-value target is one of the following equivalent structural advances.

### Route A — nondegenerate extreme existence

Prove that the full-support positive KKT vector lies in a face decomposition containing
at least one extreme circuit with

\[
z_*=s_Z.
\]

By CT.3 this produces a full-vertex maximal positive rigidity circuit, to which the
`s_Z=0` circuit topology/area machinery may be compared directly.

### Route B — degeneracy costs geometry

Prove a lower bound on the geometric cost of

\[
\kappa_*:=z_*-s_Z=2(v-v_*)+\sigma_*.
\]

For example, show that `kappa_*=Omega(D)` forces a force-hull perimeter/area loss or an
actual critical release incompatible with the full-source FS/CP bounds.

### Route C — cyclic extreme exclusion

Use CT.3.3 together with the selected contact degree caps and the near-antipodal FS
geometry to show that a cyclic extreme support cannot have `sigma_*>0`. This would
force every cyclic extreme ray onto the maximal-circuit wall, leaving only caterpillar
extremes to control.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For the full post-ZF graph:
    e+h=2v-2+s_Z.
For any extreme normalized KKT stress, EC says its positive support is a circuit. Put
    sigma_*=2v_*-2-(e_*+h_*)>=0.
Then exactly
    z_*=(e+h)-(e_*+h_*)
       =2(v-v_*)+s_Z+sigma_*.
Also
    z_*-s_Z=rank(R)-rank(R_S)=2(v-v_*)+sigma_*.
Hence z_*=s_Z iff the extreme circuit uses every full vertex and sigma_*=0.

Woodall applies to selected H_*:
    d_*=q_*-h_*=0  -> connected odd unicycle + pendant leaves;
    d_*>0          -> caterpillar forest with exactly d_* components.

EC face identity plus b_*=q_*+x_* gives
    q_*+2sigma_*=x_*+Q_*+2d_*.
So underbracing is paid exactly by selected outer/face/component defect.

Next: force one nondegenerate extreme with z_*=s_Z, or prove the degeneracy cost
kappa_*=2(v-v_*)+sigma_* has forbidden geometry.
```
