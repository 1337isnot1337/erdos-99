<!-- migration-source: path=docs/reports/target_c_forest_retained_currency_doubled_gap_2026-09-11.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=c07ddaaae3e4b7694820c2b06d6821609f836b42; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — exact retained forest currency and doubled-gap constraint

**Date:** 2026-09-11  
**Target:** Target C, C-II  
**Status:** unpromoted research report; the route map is unchanged  
**LEVEL I STATUS:** STILL OPEN

This report isolates the exact term that prevents the maximal-extreme transfer from
closing the forest diameter branch, and proves the independent metric constraint that
must accompany it.

Let \(C\) be the positive contact core, \(B\) its loaded vertices, \(q=|B|\),
\(c_I\) the number of components of \(C[B^c]\), \(e_{BI}\) the loaded--unloaded
contact count, and \(e_{BB}\) the loaded--loaded contact count. Put

\[
u:=e_{BI}-3c_I\ge0,
\qquad s_B:=3q-e_{BI}-2e_{BB}\ge0.
\]

In the exact circuit phase \(s_Z=0\), write \(d=d_H=q-h>0\) for the number of
diameter-graph components and \(S=e_{BB}+2s_C\). Then the exact ledger gives

\[
\boxed{
S-3d-\frac23s_B
 =\frac{2u+e_{BB}-3d}{3}-4.}
\tag{FRC.1}
\]

Consequently the forest transfer inequality needed by the maximal-extreme argument,
\[
\frac{S-3d-(2/3)s_B}{D}\ge0.597+\varepsilon,
\tag{FRC.2}
\]
is equivalent, up to the vanishing finite constant \(4/D\), to the genuinely new
geometric demand
\[
\boxed{\frac{2u+e_{BB}-3d}{3D}\ge0.597+\varepsilon.}
\tag{FRC.3}
\]
The previously proved \(S-3d>0.597D+o(D)\) does not imply (FRC.3), because it may
be paid entirely by the unused loaded degree \(s_B\).

## 1. Proof of the exact retained-currency identity

The post-ZF incidence ledger is

\[
c_I+e_{BB}+s_C=q-2+d.
\tag{FRC.4}
\]

Hence

\[
S=e_{BB}+2s_C=2q-4+2d-2c_I-e_{BB}.
\tag{FRC.5}
\]

From the definition of \(s_B\),

\[
e_{BI}=3q-s_B-2e_{BB},
\qquad
c_I=\frac{e_{BI}-u}{3}.
\tag{FRC.6}
\]

Substitute (FRC.6) into (FRC.5):

\[
\begin{aligned}
S
&=2q-4+2d-\frac23(3q-s_B-2e_{BB}-u)-e_{BB}\\
&=2d-4+\frac23s_B+\frac23u+\frac13e_{BB}.
\end{aligned}
\]

Subtracting \(3d+(2/3)s_B\) proves (FRC.1). This is an exact finite identity; no
asymptotics, circuit equality beyond (FRC.4), or hull saturation is used.

The same calculation applies to a selected maximal \(s_Z=0\) circuit, with stars on
all quantities. Thus the general transfer
\[
S\ge S_*-3d_*-(2/3)s_{B,*}+d_*+2d_H
\]
can close the forest branch only after a lower bound of the form (FRC.3) is proved
for the selected circuit.

## 2. Metric constraint from vertex-disjoint diameter edges

Let \(a_D=\arcsin(1/(2D))\). Two diameter segments with four distinct endpoints and
acute projective angle \(\theta\) satisfy

\[
\min\{\text{four cross-distances}\}
\le2D\sin(\theta/4).
\tag{FRC.7}
\]

Indeed, after centering one segment, write the midpoint displacement as

\[
m=\alpha\widehat w+\beta\widehat z,
\quad |w|=\sin(\theta/2),\quad |z|=\cos(\theta/2),
\]

where \(w\perp z\). The two cross-distance bounds involving \(z\) give
\(\alpha^2+(|\beta|+|z|)^2\le1\). The smaller \(w\)-pair is then at most
\(2\sin(\theta/4)\), after the elementary one-variable maximization. Therefore
unit separation forces

\[
\theta\ge4a_D
\tag{FRC.8}
\]

for distinct-endpoint diameter pairs. Shared-endpoint pairs only force the generic
\(2a_D\) bound.

If the actual diameter graph is a non-star forest, at least \(d=q-h\) cyclically
consecutive direction pairs have distinct endpoints: at most \(2h-q\) consecutive
pairs can share an endpoint. Concavity of \(g\mapsto\sin(g/2)\), applied to the
projective direction gaps, gives

\[
\operatorname{per}F\ge h-d+2(d-1)\cos a_D
 +2D\cos((q-2)a_D).
\tag{FRC.9}
\]

The star alternative is asymptotically impossible in the post-ZF branch because a
diameter star has \(h/D\le\pi/3+o(1)\), whereas the difference-body floor gives
\(h/D\ge2\rho+o(1)\), \(\rho=\cos\rho\).

In the \(s_Z=0\) forest phase, the exact perimeter identity is
\(b+Q=2h\), with \(b=q+x_B\), and \(\operatorname{per}F\le b\). Thus

\[
\boxed{
x_B\ge2D\cos((q-2)a_D)-2-2(d-1)(1-\cos a_D).}
\tag{FRC.10}
\]

Since \(x_B+Q=2h-q\), this also implies

\[
2h-q\ge2D\cos((q-2)a_D)-O(D^{-1}).
\tag{FRC.11}
\]

For normalized limits \(x=q/D\), \(y=h/D\),

\[
\boxed{2y-x\ge2\cos(x/2).}
\tag{FRC.12}
\]

This is a valid extra constraint on the forest branch, but it does not control the
currency in (FRC.3): it constrains the outer-walk/diameter branching allocation,
whereas \(u\) and \(e_{BB}\) are contact-incidence quantities.

## 3. Why the present ledgers still do not imply the needed bound

The attachment-subfamily circuit inequalities and the one-block diameter theorem
control how \(u\), \(e_{BB}\), and diameter edges can be distributed, but they do not
show that the cross-block diameter edges must be replaced by contacts. A whole
attachment-incidence block can contain all loaded vertices, and then the proper-subset
circuit inequalities have their one-edge whole-circuit exception.

At the scalar ledger level, the obstruction is already visible in the finite assignment

\[
q=3,\quad h=2,\quad d=1,\quad c_I=2,\quad e_{BB}=0,\quad e_{BI}=6,
\quad s_B=3,\quad s_C=0.
\]

It satisfies the exact incidence equality
\(c_I+e_{BB}+s_C=q-2+d\), the loaded degree cap
\(e_{BI}+2e_{BB}\le3q\), and \(u=0\), while
\(S-3d-(2/3)s_B=-5\). This is not a geometric counterexample or a global minimizer;
it proves only that algebraic ledgers and degree caps cannot establish (FRC.3).

The exact remaining theorem must therefore use a source-specific fact absent from
this scalar model: force-balance directions at deficient loaded vertices, the
common 2-connected contact block, or a simultaneous strict competitor. No such
fact is proved here.

## 4. Regression audit and status

- The cyclic \(d=0\) branch is not covered by (FRC.9)--(FRC.12).
- Regular odd shells have \(s_Z=2\), so neither (FRC.1) nor \(b+Q=2h\) is applied.
- Shared-endpoint diameter pairs retain the \(2a_D\), not the doubled \(4a_D\), gap.
- A star diameter graph is excluded only using the independent post-ZF difference-body
  lower bound, not by assuming bounded diameter degree.
- Contact-isolated source points are absent from the core ledgers but remain in the
  full-source population; no hull saturation is imposed.
- The whole-circuit attachment exception is retained explicitly.

**Conclusion:** FRC.1 and FRC.10 are proved new bookkeeping/metric constraints, but
the missing lower bound (FRC.3) remains an actual closure theorem. Target C-II and
Erdős Problem #99 remain open.
