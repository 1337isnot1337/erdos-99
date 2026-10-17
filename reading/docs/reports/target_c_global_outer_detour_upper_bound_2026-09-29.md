> Generated reading edition · [exact source](../../../docs/reports/target_c_global_outer_detour_upper_bound_2026-09-29.md) · source SHA-256 `ce6d995f98a148c0a351c8bddf64a0c22b71c19adf75482f22de17135e3f90e0`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-ABE82E88D4FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_global_outer_detour_upper_bound_2026-09-29.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=52d7dc5ca0df051065069508c960816fc132b1b3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Target C-II — current-main global outer-detour upper bound

**Date:** 2026-09-29  
**Base main:** 2a906636dc133e2652d9ec722f1f07d6c3c34203  
**Status:** current-main revalidation / proof-only; theorem-state authority unchanged  
**LEVEL I STATUS:** STILL OPEN. C-II remains open.

## 1. Result

For every sufficiently large canonical full-core Type-II survivor, define

```math
S_{\rm out}:=\sum_r(L_r-2d_r),
\qquad
S_D:=\sum_r d_r,
```

where $`L_r`$ is the occurrence-counted outer-face walk length of the induced
harmonic graph and $`d_r=\operatorname{diam}P_r`$, with
$`P_r=\operatorname{conv}(A_r)`$. Also define

```math
Q_{\rm loc}:=\sum_rQ_r,
\qquad
C_A:=\sum_rc_r,
```

where $`Q_r`$ is the local bounded nonquadrilateral degree excess and $`c_r`$
counts loaded-loaded unit contacts whose endpoints both lie in $`A_r`$. Put
$`k=d_H+s_Z`$, and let $`c_I`$ be the number of unloaded positive-contact
components.

Then

```math
\boxed{
0\le S_{\rm out}
\le
2(q-k-S_D)+4c_I-4-Q_{\rm loc}.
}
\tag{1.1}
```

In particular,

```math
\boxed{
S_{\rm out}
\le
2(q-k)-2S_D+4c_I-4.
}
\tag{1.2}
```

The current canonical full-core inputs
$`c_I=O(D^{2/3})`$, $`S_D\ge D-o(D)`$, and
$`q\le\operatorname{per}(F)\le\pi D`$ therefore give the diameter-only global cap

```math
\boxed{
\limsup_{D\to\infty}{S_{\rm out}\over D}
\le2\pi-2.
}
\tag{1.3}
```

Combining (1.1) with canonical Section 122 also gives the strict
diameter-moment gap

```math
\boxed{
\liminf_{D\to\infty}
{q-k-\sum_rd_r\over D}
\ge
{\pi\over20}(2-\sqrt3)
=0.0420893607\ldots .
}
\tag{1.4}
```

Thus a full-core survivor cannot have
$`q-k=\sum_rd_r+o(D)`$.

The finite inequality (1.1) appeared previously in
research/target_c_outer_detour_diameter_moment_floor_2026-09-12.md and passed
its hostile audit. This note does not relabel that historical statement as new.
It rederives it directly from the current-main canonical identities, gives a
self-contained proof of the completion-triangle cancellation on the current
hypotheses, and records the clean global cap (1.3) and current Section-122
consequence (1.4).

## 2. Exact local and global identities

Fix one unloaded component $`I_r`$. Use the canonical Section-82 quantities
$`a_r=|A_r|`$, local pinned surplus $`s_r`$, loaded-loaded contact count
$`c_r`$, local degree excess $`Q_r`$, and occurrence-counted outer walk $`L_r`$.

Canonical Section 82 gives

```math
L_r+Q_r=4a_r-6-2s_r-2c_r.
\tag{2.1}
```

Canonical Section 123 gives, with its augmented quantities $`T_r,Q_r^+`$,

```math
a_r-3-s_r
={a_r-T_r+Q_r^+\over2}.
\tag{2.2}
```

Set

```math
\eta_r:=a_r-3-s_r.
```

Then (2.1) becomes

```math
L_r=2a_r+2\eta_r-2c_r-Q_r,
```

so

```math
L_r-2d_r
=
2(a_r-d_r)+2\eta_r-2c_r-Q_r.
\tag{2.3}
```

Canonical Section 123 also gives

```math
e_{BB}-k
=\sum_r\eta_r+d_{\rm tile}.
\tag{2.4}
```

Writing $`a=\sum_ra_r`$, summing (2.3) and using (2.4) gives the exact finite identity

```math
\boxed{
S_{\rm out}
=
2(a-S_D)+2(e_{BB}-k)-2d_{\rm tile}
-2C_A-Q_{\rm loc}.
}
\tag{2.5}
```

The same Section-123 dissection identity is

```math
d_{\rm tile}
=q-2-\sum_r(a_r-2)
=q-2-a+2c_I,
```

hence

```math
\boxed{
a=q-2+2c_I-d_{\rm tile}.
}
\tag{2.6}
```

No asymptotic argument has entered.

## 3. Completion-triangle cancellation

The key geometric lemma is

```math
\boxed{
e_{BB}-C_A\le2d_{\rm tile}.
}
\tag{3.1}
```

Canonical C-FULLCORE-LOADED-CHORD says that, for sufficiently large full-core
Type-II survivors, every loaded-loaded unit contact is a side of the actual
loaded force hull $`F`$. Thus the $`e_{BB}`$ loaded-loaded contacts are unit
outer sides of the convex $`q`$-gon $`F`$.

Triangulate every attachment polygon $`P_r`$ using only attachment vertices.
Canonical cell-interior disjointness makes the union of these triangulations a
noncrossing straight-line graph on the $`q`$ loaded hull vertices. The cell
triangulations contain

```math
\sum_r(a_r-2)=q-2-d_{\rm tile}
```

triangles. Extend their union to a triangulation of the whole loaded $`q`$-gon.
Since a triangulation of a $`q`$-gon has $`q-2`$ triangles, exactly
$`d_{\rm tile}`$ triangles are completion triangles.

A loaded unit hull side is counted in $`C_A`$ exactly when it is covered by an
attachment polygon. If both endpoints of a global hull side belong to $`A_r`$,
they are consecutive in the cyclic subset $`A_r`$, so the side is a side of
$`P_r`$; inducedness of $`H_r`$ then counts the unit contact in $`c_r`$.
The same positive-area cell side cannot be used by two distinct cells: both
cells lie in the inward half-plane of the supporting line and would overlap
near the relative interior of the side, contradicting canonical
cell-interior disjointness.

Therefore $`e_{BB}-C_A`$ is exactly the number of loaded unit hull sides that
are not covered by a cell. Each such side is incident, on the inside, to a
completion triangle. For sufficiently large Type II, $`q\ge4`$, and a triangle
in a triangulation of a convex $`q`$-gon has at most two outer hull sides.
Hence

```math
e_{BB}-C_A\le2d_{\rm tile},
```

proving (3.1).

## 4. Global outer-detour upper bound

Substitute (2.6) into (2.5):

```math
\begin{aligned}
S_{\rm out}
={}&
2(q-k-S_D)+4c_I-4-Q_{\rm loc}\\
&+2(e_{BB}-C_A-2d_{\rm tile}).
\end{aligned}
\tag{4.1}
```

By (3.1), the second line is nonpositive. Therefore

```math
S_{\rm out}
\le
2(q-k-S_D)+4c_I-4-Q_{\rm loc}.
```

For the lower bound, choose attachment vertices realizing $`d_r`$. They occur
on the outer face of the induced harmonic graph. The two occurrence-counted
outer-walk arcs between chosen occurrences each join points at distance $`d_r`$,
so each has Euclidean path length at least $`d_r`$. Thus

```math
L_r\ge2d_r
```

even with repeated outer vertices and bridge occurrences. Summing gives
$`S_{\rm out}\ge0`$. This proves (1.1).

## 5. Diameter-only global cap

Canonical full-core attachment-cell area saturation gives

```math
\sum_r\operatorname{area}(P_r)
={\pi\over4}D^2-o(D^2).
```

Planar isodiametry gives

```math
\operatorname{area}(P_r)\le{\pi\over4}d_r^2,
```

so

```math
\sum_rd_r^2\ge D^2-o(D^2)
```

and therefore

```math
S_D=\sum_rd_r\ge D-o(D).
\tag{5.1}
```

Canonical component deatomization gives

```math
c_I=O(D^{2/3})=o(D).
\tag{5.2}
```

Every side of the loaded convex hull joins two source points and hence has
length at least one. Thus

```math
q\le\operatorname{per}(F).
```

Every planar convex body of diameter $`D`$ has perimeter at most $`\pi D`$, so

```math
q-k\le q\le\pi D.
\tag{5.3}
```

Apply (5.1)--(5.3) to (1.2) and divide by $`D`$. This proves (1.3).

The constant $`2\pi-2`$ is not claimed sharp. The point is that the requested
aggregate outer detour is now globally $`O(D)`$ with an explicit universal
coefficient on the full-core Type-II branch.

## 6. Composition with canonical Section 122

Let

```math
F_{\rm loc}:=\sum_rf_r,
```

where $`f_r`$ is the number of bounded nonquadrilateral faces of $`H_r`$. By
definition,

```math
E_{\rm agg}
:=
\sum_r(L_r+P_{{\rm exc},r}-2d_r)
=
S_{\rm out}+4F_{\rm loc}+Q_{\rm loc}.
\tag{6.1}
```

Every bounded nonquadrilateral local face has degree at least five, so

```math
F_{\rm loc}\le Q_{\rm loc}.
\tag{6.2}
```

Put

```math
X:=q-k-S_D.
```

Since $`S_{\rm out}\ge0`$, (1.1) gives

```math
Q_{\rm loc}\le2X+4c_I-4.
\tag{6.3}
```

Using (1.1), (6.2), and (6.3) in (6.1),

```math
\begin{aligned}
E_{\rm agg}
&\le
2X+4c_I-4+4F_{\rm loc}\\
&\le
2X+4c_I-4+4Q_{\rm loc}\\
&\le
10X+20c_I-20.
\end{aligned}
\tag{6.4}
```

Canonical Section 122 gives

```math
\liminf_{D\to\infty}{E_{\rm agg}\over D}
\ge
c_{\rm det},
\qquad
c_{\rm det}:={\pi\over2}(2-\sqrt3).
\tag{6.5}
```

Since $`c_I/D\to0`$, equations (6.4)--(6.5) imply

```math
\liminf_{D\to\infty}{X\over D}
\ge
{c_{\rm det}\over10}
=
{\pi\over20}(2-\sqrt3).
```

This proves (1.4).

## 7. Status and exact remaining obstruction

The selected target, a global upper bound on

```math
\sum_r(L_r-2d_r),
```

is achieved by the finite inequality (1.1), with the diameter-only global
corollary (1.3).

This does not close C-II. The upper bound still permits linear detour because
the loaded-boundary currency $`q-k`$ can exceed the aggregate cell-diameter
moment $`S_D`$ by a linear amount. Canonical Section 122 in fact forces that
excess to satisfy the positive lower bound (1.4).

The next closing target is therefore sharper and no longer asks merely for any
upper bound on $`S_{\rm out}`$. One must do at least one of the following:

1. strengthen (1.1) by charging a positive fraction of
   $`q-k-S_D`$ back to $`Q_{\rm loc}`$, completion geometry, or the actual
   diameter topology;
2. prove an upper bound on $`q-k-S_D`$ below
   $`\pi(2-\sqrt3)D/20`$;
3. turn the forced linear gap into a source-preserving strict decrease of the
   global diameter or an exact unit equilateral triangle.

The separate macroscopic inactive-container branch is not addressed here.

## 8. Scope and provenance

- Remote main was rechecked immediately before writing this report.
- The proof uses current canonical Section 82, Section 123,
  C-FULLCORE-LOADED-CHORD, C-HARMONIC-CELL-TILING, and component deatomization,
  plus elementary convex triangulation and planar isodiametry.
- Section 122 is used only for (1.4), not for the upper bound itself.
- No rejected Euler-path, FB4, Reuleaux-cap, full-source ZR/ZF, or
  Section-121 scaling inference is used.
- Contact-isolated source points remain in the full source.
- The theorem-state manifest is not changed by this report. It is a proof
  artifact pending any separate promotion transaction.
