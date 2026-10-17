# Target C-II — modern all-train gap plus `t>1.844` forces chamber surplus `>0.586223D`

**Date:** 2026-09-15  
**Status:** proof-only source-level composition; theorem-state authority unchanged  
**Scope:** canonical full-core/no-macroscopic-container Type-II branch after the hostile-audited exclusion of `t=(q-k)/D<=1.844`  
**Dependencies:** hostile-audited full-core `t<=1.844` exclusion; scope-safe matched all-train gap `g=0.007707`; canonical difference-body terminal floor; canonical Sections 63, 80, and 85  
**Certificate:** `research/verify_target_c_high_t_chamber_surplus_0586223.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The low-`t` full-core branch is now gone.  The remaining full-core branch can therefore
be coupled to a second modern input that was not used in the original Section-85
interface bound: the corrected matched all-train gap

\[
\liminf {T-q/2\over D}
\ge 2\sqrt{\Delta_2}+0.007707,
\qquad
\Delta_2={\pi\over2\sqrt3}.
\tag{HC.1}
\]

The exact stopped-train ledger converts (HC.1) into a large floor for the old
train-boundary slack `tau_D`.  Feeding that floor and `t>=1.844` simultaneously into
the exact Section-85 chamber ledger gives

\[
\boxed{
\liminf_{D\to\infty}
{A_{ch}-a_0Z_{ch}\over D}
\ge0.586223,
}
\tag{HC.2}
\]

where

\[
a_0={\sqrt3\over2}.
\]

This is a modern-scope replacement for the older `0.557720...D` correlated-interface
calculation, whose numerical gain inherited the pre-audit AG42 `0.00042` input.  The
present proof instead uses the scope-safe `g=0.007707` theorem and also exploits the
new full-core floor `t>=1.844`.

The theorem is not a C-II closure.  It says that every remaining full-core survivor
must carry substantially more source-derived inactive-interface packing surplus than
was previously known.

---

## 1. Exact stopped-train bookkeeping

Let `T` be the full stopped-train count, including singleton positive-contact edges, and
let `R_4` be the number of bounded strict unit-rhombus faces.  Use the canonical
Section-85 train-boundary slack

\[
\tau_D:=(q-k)+2f-2\sqrt{R_4}\ge0.
\tag{HC.3}
\]

The exact stopped-train handshake gives

\[
T-q=2f-k.
\tag{HC.4}
\]

Therefore

\[
\begin{aligned}
T-2\sqrt{R_4}
&=(q-k)+2f-2\sqrt{R_4}\\
&=\tau_D.
\end{aligned}
\]

Hence

\[
\boxed{\tau_D=T-2\sqrt{R_4}.}
\tag{HC.5}
\]

This is the same exact identity that can also be written

\[
2\tau_D=\rho_{rec}+\sigma_R
\]

in the older singleton/rhombic stopped-train decomposition.  No asymptotic estimate is
used in (HC.5).

---

## 2. The corrected `g=0.007707` theorem forces linear train slack

The modern scope-safe matched all-train theorem proves

\[
\boxed{
\liminf {T-q/2\over D}
\ge 2\sqrt{\Delta_2}+g,
\qquad g=0.007707.
}
\tag{HC.6}
\]

The canonical difference-body terminal theorem gives

\[
\boxed{
\liminf {q\over D}\ge2\rho,
}
\tag{HC.7}
\]

where `rho` is the positive fixed point

\[
\rho=\cos\rho
=0.7390851332151606\ldots .
\tag{HC.8}
\]

Canonical full-core Type-II rhombic saturation gives

\[
{\sqrt{R_4}\over D}\to\sqrt{\Delta_2}.
\tag{HC.9}
\]

Write (HC.5) as

\[
{\tau_D\over D}
={T-q/2\over D}
+{q\over2D}
-2{\sqrt{R_4}\over D}.
\tag{HC.10}
\]

Taking lower limits and using (HC.6)--(HC.9),

\[
\boxed{
\liminf {\tau_D\over D}
\ge \rho+g
=0.7467921332\ldots .
}
\tag{HC.11}
\]

Thus the remaining full-core branch does not merely have nonnegative train-boundary
slack.  It has a universal linear amount of it.

This is a substantial strengthening of the old post-endpoint four-way split: one of
its currencies is now known to be linearly large on every survivor, not merely on one
branch of a disjunction.

---

## 3. Exact Section-85 interface identity

Put

\[
U:=q-k.
\tag{HC.12}
\]

Canonical Section 63 gives

\[
\boxed{b+Q=2U,}
\tag{HC.13}
\]

where `b` is the occurrence-counted outer contact-face walk and `Q` is the global
bounded-face degree-above-four defect.

Section 85 uses the smaller raw chamber-interface currency

\[
H_D:=(b-p)+(Q+2f),
\qquad p=\operatorname{per}(F).
\tag{HC.14}
\]

Using (HC.13) and the definition (HC.3),

\[
\begin{aligned}
H_D
&=(b+Q)-p+2f\\
&=2U-p+2f\\
&=U+\tau_D-p+2\sqrt{R_4}.
\end{aligned}
\]

Therefore

\[
\boxed{
H_D=(q-k)+\tau_D-p+2\sqrt{R_4}.
}
\tag{HC.15}
\]

This is a finite identity.  It retains the train slack instead of discarding it.

Canonical Section 85 then proves the source-level Oler inequality

\[
\boxed{
A_{ch}-a_0Z_{ch}
\ge c_0 H_D,
\qquad
c_0={\sqrt3\over4},
\qquad
a_0={\sqrt3\over2}.
}
\tag{HC.16}
\]

All quantities here are the canonical occurrence-counted/full-source quantities.  In
particular, contact-isolated source points remain present and contribute to `Z_ch`.

---

## 4. Insert the new high-`t` floor

The hostile-audited phase-resolved remainder theorem excludes all sufficiently large
full-core/no-container survivors with

\[
{q-k\over D}\le1.844.
\]

For the present asymptotic composition it is enough to use the adverse closed-endpoint
statement

\[
\boxed{
\liminf {q-k\over D}\ge1.844.
}
\tag{HC.17}
\]

No uniform positive gap above `1.844` is assumed.

Canonical Type-II near-disk asymptotics also give

\[
{p\over D}\to\pi,
\qquad
{\sqrt{R_4}\over D}\to\sqrt{\Delta_2}.
\tag{HC.18}
\]

Divide (HC.15) by `D` and combine (HC.11), (HC.17), and (HC.18):

\[
\begin{aligned}
\liminf {H_D\over D}
&\ge
1.844+(\rho+0.007707)-\pi+2\sqrt{\Delta_2}\\
&=1.35382509\ldots .
\end{aligned}
\tag{HC.19}
\]

The exact companion certificate proves the safe rounded form

\[
\boxed{
\liminf {H_D\over D}\ge1.353825.
}
\tag{HC.20}
\]

Finally, (HC.16) yields

\[
\begin{aligned}
\liminf {A_{ch}-a_0Z_{ch}\over D}
&\ge
{\sqrt3\over4}
\left[
1.844+\rho+0.007707-\pi+2\sqrt{\Delta_2}
\right]\\
&=0.58622346\ldots .
\end{aligned}
\tag{HC.21}
\]

The exact certificate proves

\[
\boxed{
\liminf {A_{ch}-a_0Z_{ch}\over D}\ge0.586223.
}
\tag{HC.22}
\]

This proves the main claim.

---

## 5. A simultaneous positive-core second-order floor

Canonical face counting gives

\[
m=R_4+f+(q-k)+1.
\tag{HC.23}
\]

Equation (HC.14) is equivalently

\[
H_D=2[(q-k)+f]-p,
\]

so

\[
\boxed{
m-R_4={p+H_D\over2}+1.}
\tag{HC.24}
\]

Using (HC.15) makes the perimeter cancellation explicit:

\[
m-R_4
={q-k+\tau_D+2\sqrt{R_4}\over2}+1.
\tag{HC.25}
\]

Thus the same modern inputs give

\[
\boxed{
\liminf {m-R_4\over D}
\ge
{1.844+(\rho+0.007707)+2\sqrt{\Delta_2}\over2}
>2.247708.
}
\tag{HC.26}
\]

This improves the older proof-only `2.21479...` correlated-interface population floor
without importing its pre-audit AG42 numerical dependency.

---

## 6. Relation to the older correlated-interface calculation

The September 14 correlated stopped-train note used an all-train gap `0.00042` and
obtained, at proof-only scope,

\[
{A_{ch}-a_0Z_{ch}\over D}\gtrsim0.5577209.
\]

That note explicitly inherited the then-unresolved AG42 audit status.  The current
stack has since replaced that numerical input by the scope-safe matched theorem
`g=0.007707`.  Simply updating the old stopped-train algebra already makes the train
slack much larger.  The new full-core exclusion through `t<=1.844` then adds an
independent source of interface currency through (HC.15).

The result is the stronger `0.586223` floor above.  No assertion is made that the old
artifact is theorem-state authority; the present note is a fresh composition of the
current proof-only and canonical inputs.

---

## 7. What remains open

The new floor is large, but it is not a contradiction with Type II.  The quantity

\[
A_{ch}-a_0Z_{ch}
\]

is an Oler-weighted area/population surplus.  A full-core source may still distribute a
linear amount of this currency across thin doubled near-geodesic corridors and
near-degenerate exceptional faces while keeping total inactive area `o(D^2)`.

Therefore the invalid implication

```text
linear chamber surplus
    -> one macroscopic empty chamber
    -> Type-II contradiction
```

is still unavailable.

The next closing target is now sharper.  Every surviving full-core source must
simultaneously have

```text
t > 1.844 at the asymptotic endpoint,
train-boundary slack tau_D >= (0.7467921-o(1))D,
Section-85 interface H_D >= (1.353825-o(1))D,
Oler chamber surplus A_ch-a0 Z_ch >= (0.586223-o(1))D,
positive-core excess m-R4 >= (2.247708-o(1))D.
```

A closing theorem should couple this forced train slack to the Section-84
near-geodesic corridor classification, the new high-`t` same-phase O--O hub/saturation
normal form, or a protected source-level repacking.  The separate Type-I
macroscopic-container/exterior-cap branch remains untouched.

**Disposition:** proved proof-only high-`t` full-core strengthening on the modern
scope-safe all-train stack.  C-II and Level I remain open.
