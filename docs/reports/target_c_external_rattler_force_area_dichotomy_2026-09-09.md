<!-- theorem-state: {"artifact_id":"ART-94BD84F5F9FC","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — external rattlers pay the force-hull area deficit

**Date:** 2026-09-09  
**Repository base:** current `main` through the OP/RA reports plus PR #110 post-ZF stack  
**Run type:** exact source-capacity bridge  
**Target:** Target C Gate C-II / Level I  
**LEVEL I STATUS:** STILL OPEN

The OP outer-pocket theorem absorbs every source point lying inside the force hull `F`
into the ordinary Oler capacity of `F`. Therefore the only population not paid by the
force hull is the contact-isolated population lying outside `F`.

Combining OP with the canonical strict global lattice upper bound for `D(n)` gives an
exact quantitative dichotomy:

> every deficit of `area(F)` below the isodiametric maximum `pi D^2/4` forces a
> corresponding quadratic population of external rattlers.

Thus the residual C-II source-capacity obstruction is no longer an arbitrary invisible
population. Either the force hull is asymptotically isodiametric, or a positive
fraction of the source points lie outside the force hull.

## 1. Setup

Work with the C65 lexicographically normalized hypothetical triangle-free global
minimizer. Let

- `n` be the full source cardinality;
- `D=D(n)` its diameter;
- `F` the force hull of the nonisolated positive contact core;
- `A_F=area(F)`;
- `P_F=per(F)`;
- `Z_ext` be the number of source points outside `F`.

The OP theorem proves

\[
\boxed{
 n-Z_{ext}
 \le
 \frac{2}{\sqrt3}A_F+\frac12P_F+1.
}
\tag{ER.1}
\]

Indeed `n-Z_ext` consists of the core vertices, bounded-face rattlers, and outer-face
rattlers that still lie inside `F`.

The current strict lattice comparison is

\[
\boxed{
D(n)^2<\frac{2\sqrt3}{\pi}(n-1).
}
\tag{ER.2}
\]

Equivalently, with

\[
\Delta:=\frac\pi{2\sqrt3},
\]

\[
\boxed{n>\Delta D^2+1.}
\tag{ER.3}
\]

Finally convexity gives

\[
P_F\le\pi D
\tag{ER.4}
\]

and the isodiametric inequality gives

\[
A_F\le\frac\pi4D^2.
\tag{ER.5}
\]

## 2. Theorem ER — exact external-rattler lower bound

### Theorem ER

Every C65 hypothetical survivor satisfies

\[
\boxed{
Z_{ext}
>
\frac{2}{\sqrt3}
\left(\frac\pi4D^2-A_F\right)
-\frac12P_F.
}
\tag{ER.6}
\]

Consequently

\[
\boxed{
Z_{ext}
>
\frac{2}{\sqrt3}
\left(\frac\pi4D^2-A_F\right)
-\frac\pi2D.
}
\tag{ER.7}
\]

### Proof

Subtract ER.1 from ER.3:

\[
\begin{aligned}
Z_{ext}
&=n-(n-Z_{ext})\\
&>
\Delta D^2+1
-\left(\frac{2}{\sqrt3}A_F+\frac12P_F+1\right)\\
&=
\frac{2}{\sqrt3}
\left(\frac\pi4D^2-A_F\right)
-\frac12P_F.
\end{aligned}
\]

This proves ER.6. Insert `P_F<=pi D` to obtain ER.7. `square`

## 3. Fixed area-deficit consequence

Suppose along a sequence

\[
\frac{A_F}{D^2}\le\frac\pi4-\eta+o(1)
\]

for some fixed `eta>0`. Then ER.7 gives

\[
\boxed{
\liminf\frac{Z_{ext}}{D^2}
\ge\frac{2\eta}{\sqrt3}.
}
\tag{ER.8}
\]

Thus any fixed normalized force-hull area deficit produces a fixed positive density of
source points outside the force hull.

Conversely:

### Corollary ER.1 — subquadratic external population forces a near-disk force hull

If

\[
Z_{ext}=o(D^2),
\]

then

\[
\boxed{
\frac{A_F}{D^2}\longrightarrow\frac\pi4.
}
\tag{ER.9}
\]

### Proof

ER.7 gives

\[
\frac{2}{\sqrt3}
\left(\frac\pi4-\frac{A_F}{D^2}\right)
<
\frac{Z_{ext}}{D^2}+\frac\pi{2D}.
\]

The right side tends to zero, while ER.5 makes the left side nonnegative. `square`

So if external rattlers are not macroscopically numerous, the force hull itself must
asymptotically attain the planar isodiametric area maximum.

## 4. Interaction with post-ZF force-hull geometry

ZA proves the independent lower bound

\[
\liminf\frac{A_F}{D^2}\ge\frac12\sin1
=0.4207354924\ldots .
\]

ER upgrades the interpretation of the remaining interval

\[
0.420735\ldots
\le\frac{A_F}{D^2}
\le\frac\pi4=0.785398\ldots .
\]

If the normalized area stays a fixed amount below `pi/4`, then there are
`Theta(D^2)` external source points. If it approaches `pi/4`, then the force hull is
an asymptotically isodiametric convex body and the remaining route must exploit this
near-disk geometry together with the full actual diameter graph.

This gives the exact branch split

```text
C65 post-ZF survivor
    -> either Z_ext = Omega(D^2)
    -> or area(F) = (pi/4-o(1))D^2.
```

No compactness or stability theorem for near-isodiametric bodies is imported here;
ER.9 is only an area statement.

## 5. Interaction with ZP/ZG and OP

The post-ZF component ledger ZK shows that small `e_BB+2s_C` makes the nonisolated
core subquadratic. ZA/ZG simultaneously force a quadratic attachment-cell gap. OP
then absorbs every invisible point lying inside `F` against the force-hull area.

ER identifies the only remaining population escape quantitatively:

- either that low-surplus branch has a quadratic external population `Z_ext`;
- or its force hull must be asymptotically isodiametric.

Thus the previous phrase "quadratic isolated population" can now be sharpened. The
population not already absorbed by the force-hull Oler bound must be **outside the
force hull**.

## 6. Relation to RA

RA proves that the external rattlers are not unavoidable across all triangle-free
same-diameter global representatives: keeping the original C65 core fixed, one may
move each isolated source point to a first unit-contact event and obtain another
same-`n`, same-`D`, triangle-free global minimizer with no isolated vertices.

This does not contradict ER because ER is a theorem about the C65 lexicographic
representative and its particular force hull. RA's new contacts need not be KKT-positive,
so the ZR/ZF stack does not automatically transfer.

The combination isolates a precise representative-transfer target:

> prove an invariant of the RA rattler-free representative depending only on the fixed
> original C65 core, `n`, and `D`, strong enough to contradict the external population
> required by ER.

## 7. Quantitative corollary from the upgraded area floor

ZA alone gives

\[
\frac\pi4D^2-A_F
\le
\left(\frac\pi4-\frac12\sin1+o(1)\right)D^2,
\]

so ER does not force a positive external population from ZA alone. It is a lower bound
on `Z_ext` in terms of the **actual** area deficit, not in terms of the minimum area
allowed by ZA.

The coefficient is explicit:

\[
\frac{2}{\sqrt3}\left(\frac\pi4-\frac12\sin1\right)
=0.421\ldots .
\]

This only gives the maximum external density compatible with the current lower area
floor, not a compulsory one.

## 8. Binding regressions

- **Regular shell with dense interior filling:** may have large force-hull area deficit
  and quadratic external/interior population; ER merely quantifies the required
  population and does not certify global optimality.
- **Near-disk force hull:** lies in Corollary ER.1 and remains open.
- **RA contact-richer representative:** ER cannot be reapplied with the same positive
  force core without a transfer theorem.
- **Internal outer-pocket population:** already absorbed by OP and therefore does not
  appear in `Z_ext`.

## 9. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| ER.6 exact inequality | proved | OP + strict lattice bound. |
| fixed area deficit -> quadratic `Z_ext` | proved | Divide ER.7 by `D^2`. |
| `Z_ext=o(D^2)` -> `A_F/D^2->pi/4` | proved | ER + isodiametric upper bound. |
| near-maximal area -> geometric closeness to a disk | not imported/proved | Requires quantitative isodiametric stability. |
| quadratic `Z_ext` impossible | not proved | RA changes representatives but not KKT visibility. |
| Level I | still open | Two exact branches remain. |

## 10. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

OP:
    n-Z_ext <= (2/sqrt3) area(F) + per(F)/2 + 1.
Strict global lattice bound:
    n > [pi/(2sqrt3)] D^2 + 1.
Therefore
    Z_ext > (2/sqrt3)[pi D^2/4-area(F)] - per(F)/2
          >= (2/sqrt3)[pi D^2/4-area(F)] - pi D/2.

Hence:
- a fixed normalized force-hull area deficit eta forces
      liminf Z_ext/D^2 >= 2eta/sqrt3;
- if Z_ext=o(D^2), then
      area(F)/D^2 -> pi/4.

Remaining exact split:
    quadratic external rattlers
    OR asymptotically isodiametric force hull.
```
