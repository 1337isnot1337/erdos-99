> Generated reading edition · [exact source](../../../docs/reports/target_c_extreme_circuit_difference_body_2026-09-10.md) · source SHA-256 `26d6ab8b87a61e0ccfc87638295afb27f8531bf25f9bb4af47014cdba248a65c`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CECF14CCF1F3","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — difference-body forcing for every extreme positive KKT circuit

**Date:** 2026-09-10  
**Repository state:** PR #178 after EC/CT/TP/ESR; `main` through Woodall commit `1adc420e`  
**Run type:** exact convex-geometric / rigidity-circuit synthesis  
**Target:** Target C, C-II after ZF  
**Depends on:** canonical selected force-hull trapping, C67/PI diameter-direction separation, EC extreme-circuit face identity  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The full-support DB theorem uses two ingredients: all positive diameter vectors lie in
the difference body of their force hull, and the outer positive-contact walk gives an
upper bound on that force-hull perimeter. Neither ingredient requires the selected
stress to have full actual support.

Consequently the same difference-body mechanism applies to **every extreme normalized
KKT circuit**. Let an extreme stress have selected counts

```math
(v_*,e_*,h_*,b_*,Q_*,\sigma_*),
\qquad
\sigma_*:=2v_*-2-(e_*+h_*)\ge0,
```

as in EC. Put

```math
a_D:=\arcsin\frac1{2D}.
```

Then the selected force hull `F_*` satisfies the exact finite inequality

```math
\boxed{
Q_*
\le
h_*+2\sigma_*+1
-2D\cos\bigl((h_*-1)a_D\bigr).
}
\tag{EDB.1}
```

In particular,

```math
\boxed{
h_*+2\sigma_*+1
\ge
2D\cos\bigl((h_*-1)a_D\bigr).}
\tag{EDB.2}
```

Thus if along an unbounded sequence

```math
\frac{h_*}{D}\to y,
\qquad
\frac{\sigma_*}{D}\to s,
```

then

```math
\boxed{y+2s\ge2\cos(y/2).}
\tag{EDB.3}
```

This strictly strengthens the TP three-terminal tradeoff throughout the range in which
that tradeoff was active. In particular, every asymptotically maximal extreme circuit
(`sigma_*=o(D)`) has

```math
\boxed{
\liminf\frac{h_*}{D}
\ge2\rho
=1.478170266430321\ldots,
\qquad \rho=\cos\rho.}
\tag{EDB.4}
```

So a low-degeneracy extreme circuit automatically recovers the **same** diameter-edge
density forced for the full relative-interior support by DB. The selected-support
problem is no longer weakened to the earlier `1.358918...` TP constant.

---

## 1. The selected force hull

Fix any normalized KKT stress `x*=(alpha*,beta*)`, not necessarily full-support.
The canonical support theorem gives one connected positive contact component `C_*`
containing every endpoint of every positive diameter edge. The force-hull trapping
theorem says every vertex of this positive component lies in the convex hull of its
positive diameter endpoints.

Let `B_*` be those positive diameter endpoints. Since `B_*` is contained in the
positive contact component,

```math
\boxed{F_*:=\operatorname{conv}V(C_*)=\operatorname{conv}B_*.}
\tag{1.1}
```

Some positive diameter edge has Euclidean length exactly `D`, so

```math
\operatorname{diam}F_*=D.
\tag{1.2}
```

The outer face of the connected unit-contact graph `C_*` is a closed walk of geometric
length exactly `b_*`, counting a bridge twice when it occurs twice in the walk. Its
convex hull is `F_*`. Therefore the closed-walk perimeter lemma gives

```math
\boxed{\operatorname{per}F_*\le b_*.}
\tag{1.3}
```

This is valid also for a degenerate segment, using the usual convex-perimeter
continuation convention.

---

## 2. Difference-body lower bound for selected diameter directions

Choose one projective unit direction `u_j` for each of the `h_*` positive selected
diameter edges. Since both endpoints lie in `F_*`,

```math
\pm D u_j\in F_*-F_*.
```

Hence

```math
P_*:=D\operatorname{conv}\{\pm u_j:1\le j\le h_*\}
\subseteq F_*-F_*.
\tag{2.1}
```

C67/PI gives pairwise projective direction separation

```math
\delta_D=2a_D=2\arcsin\frac1{2D}.
\tag{2.2}
```

Order the selected projective directions around the projective circle, with gaps
`g_1,...,g_{h_*}`. Then

```math
g_i\ge2a_D,
\qquad
\sum_i g_i=\pi.
\tag{2.3}
```

Exactly as in DB, the `2h_*` points `+-Du_j` lie on the radius-`D` circle and

```math
\operatorname{per}P_*
=4D\sum_i\sin(g_i/2).
\tag{2.4}
```

Perimeter is monotone under convex inclusion and Minkowski additive, so

```math
2\operatorname{per}F_*
=\operatorname{per}(F_*-F_*)
\ge\operatorname{per}P_*.
```

Therefore

```math
\operatorname{per}F_*
\ge2D\sum_i\sin(g_i/2).
\tag{2.5}
```

The function `sin(g/2)` is concave. Under (2.3), its sum is minimized when all but
at most one gap are at the lower bound. Since `sin a_D=1/(2D)`, this gives

```math
\boxed{
\operatorname{per}F_*
\ge
h_*-1+2D\cos\bigl((h_*-1)a_D\bigr).}
\tag{2.6}
```

For `h_*=1`, (2.6) reads `per(F_*)>=2D`, which is the correct degenerate-segment
value.

---

## 3. Insert the extreme-circuit face identity

EC proves for every extreme positive circuit

```math
\boxed{b_*+Q_*=2h_*+2\sigma_*.}
\tag{3.1}
```

Thus

```math
b_*=2h_*+2\sigma_*-Q_*.
\tag{3.2}
```

Combine (1.3), (2.6), and (3.2):

```math
h_*-1+2D\cos((h_*-1)a_D)
\le2h_*+2\sigma_*-Q_*.
```

Rearranging gives EDB.1:

```math
Q_*
\le
h_*+2\sigma_*+1
-2D\cos((h_*-1)a_D).
```

Since `Q_*>=0`, EDB.2 follows.

No full-support ZF identity is used in this derivation. The role played by full-support
mixed surplus `s_Z` in DB is replaced exactly by the selected circuit flex deficit
`sigma_*` through EC.

---

## 4. Asymptotic tradeoff

The selected diameter directions are `delta_D`-separated on a projective circle of
length `pi`, so `h_*=O(D)`. Pass to a subsequence on which

```math
h_*/D\to y,
\qquad
\sigma_*/D\to s.
```

Since

```math
a_D=\frac1{2D}+O(D^{-3}),
```

we have

```math
(h_*-1)a_D\to y/2.
```

Divide EDB.2 by `D` and pass to the limit:

```math
y+2s\ge2\cos(y/2),
```

which is EDB.3.

Equivalently,

```math
\boxed{
s\ge\max\{0,\cos(y/2)-y/2\}.}
\tag{4.1}
```

The right side is strictly positive for `0<=y<2rho` and vanishes at

```math
y=2\rho,
\qquad
\rho=\cos\rho.
```

Therefore `sigma_*=o(D)` forces EDB.4.

---

## 5. Comparison with TP

TP proved

```math
y+s
\ge
\sqrt{1+\frac{\sqrt3}{2}\sin(\min\{y,\pi/2\})}.
\tag{5.1}
```

That theorem remains independently useful because it is based on a new three-terminal
penny-graph bound and controls a contact Steiner tree directly. But for the scalar
`(y,s)` extreme-circuit tradeoff, EDB is stronger on the active range.

Indeed, for `0<=y<=2rho`, EDB gives

```math
s\ge\cos(y/2)-y/2,
```

which exceeds the TP requirement

```math
s\ge
\sqrt{1+\frac{\sqrt3}{2}\sin y}-y
```

except at `y=0`, where both give `s>=1`. This comparison can be checked algebraically
or by monotonicity; no downstream theorem needs the strict comparison, only the EDB
bound itself.

The practical consequence is decisive for the route map:

```text
extreme circuit with kappa_*=o(D)
    -> sigma_*=o(D)
    -> h_*/D >= 2rho-o(1)
```

because CT gives `sigma_*<=kappa_*`.

Thus forcing one low-degeneracy extreme ray would recover full DB-scale diameter
density on a single positive rigidity circuit.

---

## 6. Near-endpoint rigidity information

Suppose

```math
sigma_*=o(D),
\qquad
h_*/D\to2\rho.
```

Then EDB.1 gives

```math
Q_*/D\to0.
\tag{6.1}
```

Also the lower and upper force-hull perimeter bounds asymptotically coincide:

```math
\frac{\operatorname{per}F_*}{D}
\to4\rho
=2.956340532860642\ldots,
\tag{6.2}
```

because (2.6) tends to

```math
2\rho+2\cos\rho=4\rho,
```

while (3.2) with `Q_*=o(D)` and `sigma_*=o(D)` gives

```math
b_*/D\to4\rho.
```

Hence any low-degeneracy extreme ray approaching the minimal selected diameter density
has simultaneously:

```math
\boxed{
Q_*=o(D),
\qquad
b_* - \operatorname{per}F_*=o(D),
\qquad
\operatorname{per}F_*/D\to4\rho.}
\tag{6.3}
```

This is a concrete selected-support normal form, analogous to the full `s_Z=0`
endpoint localizations but obtained without assuming the full actual graph is itself a
circuit.

---

## 7. Regressions and scope

- **Regular even-shell ESR family:** it has `h_*/D->pi/2` and
  `sigma_*/D->pi/2`; EDB.3 is easily satisfied. EDB does not falsely eliminate the
  binding two-dimensional underbraced regression.
- **One-diameter straight chain:** `h_*/D->0`, `sigma_*/D->1`; EDB.3 is equality at
  `y=0,s=1`.
- **Regular odd-shell maximal circuits:** exploratory exact-rank calculations have
  `sigma_*=0` and large selected diameter support; compatible with EDB.
- **Full-support DB:** EDB does not replace DB for the actual graph. It says that once
  an extreme ray has small circuit degeneracy, the same diameter-density mechanism is
  already present on that ray.
- **Global optimality:** used only through the canonical KKT/force-hull framework and
  the fact that selected positive diameter edges are actual length-`D` source pairs.
  No force-bulk or isolated-point claim is introduced.

---

## 8. Exact next target

CT defines

```math
\kappa_*:=z_*-s_Z=2(v-v_*)+\sigma_*.
```

EDB shows that any extreme ray with `kappa_*=o(D)` already has

```math
h_*\ge(2\rho-o(1))D.
```

Therefore the main missing theorem is no longer a selected diameter-density estimate.
It is purely the **extreme-circuit degeneracy transfer**:

> prove that the full-support positive C65 stress cone has at least one extreme circuit
> with `kappa_*=o(D)`, or show that every extreme circuit having
> `kappa_*=Omega(D)` forces a whole-source contradiction.

The second option must use interactions among extreme circuits or omitted actual rows;
ESR proves that the geometry of one high-degeneracy circuit alone is too flexible.

---

## Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For every extreme normalized KKT stress, let F_* be its selected force hull and
sigma_*=2v_*-2-(e_*+h_*).
Difference-body perimeter gives exactly
    per(F_*) >= h_*-1 + 2D cos((h_*-1)asin(1/(2D))).
The outer selected contact walk gives
    per(F_*) <= b_*.
EC gives
    b_*+Q_*=2h_*+2sigma_*.
Therefore
    Q_* <= h_*+2sigma_*+1
           -2D cos((h_*-1)asin(1/(2D))),
and in particular
    h_*+2sigma_*+1 >= 2D cos((h_*-1)asin(1/(2D))).

If h_*/D->y and sigma_*/D->s,
    y+2s >= 2cos(y/2).
Hence sigma_*=o(D) forces
    h_*/D >= 2rho-o(1)=1.4781702664...,
    rho=cos rho.
At the endpoint y=2rho with sigma=o(D), also
    Q_*=o(D),
    b_*-per(F_*)=o(D),
    per(F_*)/D->4rho.

Next: force one extreme circuit with kappa_*=z_*-s_Z=o(D), or contradict uniform
linear kappa_* using interactions among extreme circuits / omitted actual rows.
```
