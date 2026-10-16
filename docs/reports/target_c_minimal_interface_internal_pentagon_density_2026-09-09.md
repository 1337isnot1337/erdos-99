<!-- theorem-state: {"artifact_id":"ART-FDED21FAE4E2","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_minimal_interface_internal_pentagon_density_2026-09-09.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=c2540e0f9592ac926015455d39810484f027b1e1; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — minimal interface equality forces a dense internal pentagon fault network

**Date:** 2026-09-09  
**Repository branch:** `research/fullcore-interface-perimeter-2026-09-09`  
**Run type:** cross-route exact defect-count sharpening  
**Target:** full-core near-circle endpoint with `Q_B/D->2`  
**Depends on:** CE one-ended train exposure from PR #119, CF single-central-face theorem, HBd exact near-circle terminal budget  
**Computation:** displayed decimals only

## LEVEL I STATUS

`STILL OPEN`

The minimal loaded-interface equality branch is much more internally defective than the first stopped-train estimate IT shows.

CE proves that every full-core near-circle survivor has at least

\[
\boxed{
f\ge(\sqrt\Delta-o(1))D,
\qquad
\Delta=\frac\pi{2\sqrt3},
}
\tag{IP.1}

bounded nonquadrilateral contact faces in total.

CF proves that when

\[
Q_B=(2+o(1))D,
\]

one central loaded-interface face `F_*` carries

\[
Q_{F_*}=(2+o(1))D,
\qquad
Q_B-Q_{F_*}=o(D).
\]

Every other loaded-interface exceptional face contributes at least one unit to `Q_B-Q_{F_*}`. Hence there are only `o(D)` such faces. The single central face adds only one more. Therefore the number `f_int` of bounded exceptional faces containing no loaded terminal satisfies

\[
\boxed{
f_{int}\ge(\sqrt\Delta-o(1))D
= (0.9523128069\ldots-o(1))D.
}
\tag{IP.2}

Since each internal exceptional face contributes at least one to the internal degree excess,

\[
\boxed{
Q_{int}\ge(\sqrt\Delta-o(1))D.
}
\tag{IP.3}

HBd gives the exact near-circle terminal relation

\[
Q+2s_C=(\pi+o(1))D.
\]

At minimal interface defect,

\[
Q=Q_B+Q_{int}.
\]

Thus

\[
\boxed{
Q_{int}\le(\pi-2+o(1))D,
}
\tag{IP.4}

and

\[
\boxed{
s_C\le
\frac{\pi-2-\sqrt\Delta}{2}D+o(D)
= (0.09463992336\ldots+o(1))D.
}
\tag{IP.5}

Consequently

\[
\boxed{
d_H+s_Z\le(0.09463992336\ldots+o(1))D,}
\tag{IP.6}

using HBd's `d_H+s_Z=s_C+o(D)`. In particular

\[
\boxed{
h\ge(3.0469527302\ldots-o(1))D,}
\tag{IP.7}

because `q=(pi+o(1))D` and `d_H=q-h`.

Even more, most internal exceptional faces must be pentagons. Let `p_5` be the number of internal bounded faces of degree exactly five. Every pentagon contributes one unit to `Q_int`, while every nonpentagonal exceptional face contributes at least two. Therefore

\[
Q_{int}\ge p_5+2(f_{int}-p_5)=2f_{int}-p_5.
\]

Hence

\[
\boxed{
p_5\ge2f_{int}-Q_{int}.}
\]

Using IP.2 and IP.4,

\[
\boxed{
\frac{p_5}{D}
\ge
2\sqrt\Delta-(\pi-2)-o(1)
=0.7630329601\ldots-o(1).
}
\tag{IP.8}

Thus the sharp loaded-interface equality model necessarily contains at least `0.763D` internal convex unit pentagons, while the diameter graph simultaneously has edge deficit plus mixed-stress surplus below `0.095D`.

This is a substantial tightening of the endpoint. The surviving configuration is no longer merely two half-disk carriers separated by one giant face; it must also support a dense linear pentagon fault network inside those carriers (or minor harmonic components), while its diameter graph is within about three percent of the maximum convex-thrackle edge count.

---

## 1. CE's exceptional-face count

CE is the one-good-end-per-train theorem on PR #119. In the full-core near-circle phase it proves

\[
T-q\ge(2\sqrt\Delta-o(1))D.
\]

The exact identity

\[
2f=(T-q)+d_H+s_Z
\]

and nonnegativity of `d_H,s_Z` give

\[
f\ge(\sqrt\Delta-o(1))D.
\]

This is IP.1. No face-area gap is used.

---

## 2. CF removes loaded-interface faces from the count

Assume the sharp interface endpoint

\[
Q_B=(2+o(1))D.
\]

CF gives one loaded-interface exceptional face `F_*` with

\[
Q_{F_*}=(2+o(1))D
\]

and

\[
Q_B-Q_{F_*}=o(D).
\]

Let `f_B` count bounded nonquadrilateral faces incident to at least one loaded terminal. Every member of `f_B` other than `F_*` contributes at least one to `Q_B-Q_{F_*}`. Therefore

\[
f_B-1\le Q_B-Q_{F_*}=o(D),
\]

so

\[
\boxed{f_B=o(D).}
\tag{2.1}

Every bounded exceptional face is either internal to one harmonic component or touches a loaded terminal. Therefore

\[
f=f_{int}+f_B.
\]

Combine CE and (2.1) to prove IP.2.

Since `Q_int>=f_int`, IP.3 follows.

---

## 3. Exact terminal budget upper-bounds internal defect

HBd gives

\[
Q+2s_C=(\pi+o(1))D.
\tag{3.1}

Both terms on the left are nonnegative. Under `Q_B=(2+o(1))D`,

\[
Q=Q_B+Q_{int}
=(2+o(1))D+Q_{int}.
\]

Equation (3.1) gives

\[
Q_{int}+2s_C=(\pi-2+o(1))D.
\tag{3.2}

Therefore

\[
Q_{int}\le(\pi-2+o(1))D,
\]

which is IP.4.

Combine (3.2) with IP.3:

\[
2s_C
\le
(\pi-2-\sqrt\Delta+o(1))D.
\]

This proves IP.5.

HBd also gives

\[
d_H+s_Z=s_C+o(D),
\]

so IP.6 follows.

Because `d_H=q-h` and `q=(pi+o(1))D`,

\[
h=q-d_H
\ge q-(d_H+s_Z)
\ge
\left(\pi-rac{\pi-2-\sqrt\Delta}{2}-o(1)\right)D.
\]

The coefficient simplifies to

\[
\frac{\pi+2+\sqrt\Delta}{2}
=3.0469527302\ldots,
\]

proving IP.7.

---

## 4. Pentagons dominate the internal fault count

Let `p_5` be the internal degree-five face count and let `f_{>=6}=f_int-p_5`. Then

\[
Q_{int}
=\sum_{F\text{ int}}(\deg F-4)
\ge p_5+2f_{>=6}
=2f_{int}-p_5.
\]

Hence

\[
p_5\ge2f_{int}-Q_{int}.
\]

Use IP.2 and IP.4:

\[
\begin{aligned}
\frac{p_5}{D}
&\ge
2\sqrt\Delta-(\pi-2)-o(1)\\
&=0.7630329601\ldots-o(1).
\end{aligned}
\]

This proves IP.8.

A companion excess bound is

\[
\boxed{
Q_{int}-f_{int}
\le
(\pi-2-\sqrt\Delta+o(1))D
=0.1892798467\ldots D+o(D).
}
\tag{4.1}

Thus the total degree excess above the pentagonal baseline is at most `0.18928D`.

---

## 5. Diameter graph is almost edge-maximal

For the complete diameter graph on the loaded convex terminals, put

\[
d_H=q-h.
\]

IP.6 gives

\[
d_H\le(0.09463992336\ldots+o(1))D.
\]

Since

\[
q=(\pi+o(1))D,
\]

we have

\[
\frac{h}{q}
\ge
1-rac{0.09463992336\ldots}{\pi}-o(1)
=0.969875\ldots-o(1).
\]

Thus the full diameter graph has at least about `96.99%` of the maximum `q` edges allowed by a convex geometric thrackle.

This does not force a single odd cycle: convex-thrackle equality and near-equality may include leaves attached to an odd cycle, and no stability theorem is imported here. It does identify the next exact combinatorial target.

---

## 6. Interaction with IT

IT previously proved only

\[
Q_{int}\ge0.0491004189\ldots D-o(D)
\]

from the stopped-train inequality applied to the two dominant components. IP.3 supersedes that numerical lower bound by almost a factor of twenty:

\[
Q_{int}\ge0.9523128069\ldots D-o(D).
\]

IT remains useful because it is local to each dominant component and does not rely on CE's global exceptional-face count. IP, in contrast, allows the internal pentagons to live in any harmonic component.

---

## 7. Audit classification

| Claim | Status | Reason |
| --- | --- | --- |
| `f_B=o(D)` under sharp interface equality | proved | CF central face consumes all but `o(D)` of `Q_B` |
| `f_int>=sqrt(Delta)D-o(D)` | proved | CE global face count minus `f_B=o(D)` |
| `Q_int>=sqrt(Delta)D-o(D)` | proved | every internal exceptional face contributes at least one |
| `s_C<=(pi-2-sqrtDelta)D/2+o(D)` | proved | HBd exact terminal budget |
| `h>=3.0469527302D-o(D)` | proved | `q~pi D`, `d_H<=s_C+o(D)` |
| `p_5>=0.7630329601D-o(D)` | proved | degree-excess accounting |
| near-maximal diameter graph classified | not proved | requires separate convex-thrackle stability |
| Level I | still open | dense pentagon faults + near-maximal diameter graph remain compatible a priori |

---

## 8. Next target

The sharp equality branch now couples two highly constrained networks on the same `q~pi D` loaded shell:

1. a diameter graph with edge deficit
   \[
   d_H\le0.09464D+o(D),
   \]
   hence almost maximal convex-thrackle density;
2. an internal contact complex containing at least
   \[
   0.76303D-o(D)
   \]
   pentagonal bounded faces, with only `0.18928D+o(D)` total higher-degree excess above the pentagon baseline.

A promising continuation is a near-extremal convex-thrackle classification coupled to the two half-disk attachment blocks. If near-maximality forces almost all loaded terminals into one odd-cycle-like diameter backbone, the KKT response and annular spoke structure may become one-dimensional enough to conflict with the two positive-density half-disk harmonic components.

A second route is to treat the `0.763D` pentagons as stopped-train branch points and prove that their required train-end incidence exceeds the remaining shell/interface transition capacity.