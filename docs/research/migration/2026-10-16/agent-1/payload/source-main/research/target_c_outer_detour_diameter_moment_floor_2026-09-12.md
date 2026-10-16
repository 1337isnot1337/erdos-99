# Target C-II — outer-walk nonnegativity forces a diameter-moment floor

**Date:** 2026-09-12  
**Status:** proof-only Type-II candidate awaiting hostile audit; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This note extracts a new consequence from the exact aggregate outer-walk
decomposition. It uses the fact that the outer walk of each harmonic component has
length at least twice the diameter of its attachment polygon. The resulting floor is
not a closure: it pushes the Section-118 endpoint into the large-detour regime.

## 1. Finite inequality

For an unloaded component, let L_r be the occurrence-counted outer-face walk length
and d_r=diam(conv(A_r)). Choose two attachment vertices at distance d_r. They are
outer-face vertices of the induced harmonic graph; the two cyclic outer-walk arcs
between their occurrences each have Euclidean length at least d_r. Therefore

\[
L_r\ge2d_r.
\tag{1}
\]

Let

\[
S_{\rm out}:=\sum_r(L_r-2d_r),\qquad S_D:=\sum_r d_r,
\]

and use the exact Section-82/123 decomposition

\[
S_{\rm out}
=2\sum_r(a_r-d_r)+2(e_{BB}-k)-2d_{\rm tile}
-2C_A-Q_{\rm loc}.
\tag{2}
\]

Here a=sum a_r, C_A=sum c_r, and Q_loc=sum Q_r; all are occurrence-counted
with the local identities. In Type II, the completion-triangle theorem gives

\[
e_{BB}-C_A\le2d_{\rm tile}.
\tag{3}
\]

The attachment dissection identity is

\[
a=q-2+2c_I-d_{\rm tile},
\tag{4}
\]

and the global boundary ledger is

\[
b+Q=2(q-k).
\tag{5}
\]

Substituting (3)--(4) into (2) gives the finite bound

\[
S_{\rm out}
\le 2(q-k)-2S_D+4c_I-4-Q_{\rm loc}.
\tag{6}
\]

Since Q_loc>=0, the canonical component-count estimate c_I=O(D^{2/3}) and (1)
now imply

\[
\boxed{\quad
\liminf {q-k\over D}\ge\liminf {S_D\over D}.
\quad}
\tag{7}
\]

This is a Type-II source-level floor, not a carrier-specific scalar assumption.

## 2. Endpoint consequence

On the proof-only Section-118 common-cap endpoint, the independently audited
gap-profile moment gives

\[
{S_D\over D}\ge
S_* -o(1),
\qquad S_*=2.798596312209462\ldots .
\]

Therefore

\[
\boxed{\liminf {q-k\over D}\ge2.7985963122\ldots .}
\tag{8}
\]

This does not determine whether the additional linear currency is carried by the
global degree defect Q or by the outer-walk surplus
delta=(b-per(F))/D; the exact boundary ledger is
Q+delta=2(q-k)-per(F)/D.

## 3. Why this does not close C-II

The new floor invalidates low-t scalar witnesses such as t=1.9, but it does not
rule out a high-t witness. For example, the accompanying arithmetic certificate
uses t=2.9, delta=0, the endpoint moment/remainder floors, the Section-137 payment,
the all-regime atomic endpoint capacity, and the Section-123 capacity with positive
margins.

The implication chain is therefore

\[
\text{outer-walk nonnegativity}
\to t\ge S_D/D
\to\text{high loaded-boundary/defect currency at the endpoint}
\]

but the final source-level step is still missing: one must couple this larger t to
the actual loaded diameter graph and defect/outer-walk split, or turn the resulting
cell boundary structure into a source-preserving strict-diameter descent/exact unit
triangle.

**Classification:** proved candidate awaiting hostile audit; scoped to Type II and
the Section-118 endpoint for the numerical consequence; C-II remains open.
