# Hostile audit — `g=0.0050` propagation through complement bracing

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_complement_bracing_g0050_2026-09-15.md`
- `research/verify_target_c_complement_bracing_g0050.py`

**Base:** audited complement-bracing theorem through
`74fd0e6ab9a810a878998426524cd80d9153132a`, plus the already merged and audited
iterative-pruning gap `g=0.0050`.  
**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate does not introduce new geometry.  It composes two results that were
merged in rapid succession: the stronger all-train lower bound

\[
C=(T-q/2)/D\ge2\sqrt{\Delta_2}+0.0050-o(1)
\]

and the complement outer-to-outer bracing energy theorem, whose published numerical
certificate still used `+0.00042`.  The audit therefore concentrates on dependency
scope, inequality directions after strengthening `C_0`, the feasible-region
minimization, and the numerical endpoint.

---

## 1. The complement theorem is genuinely symbolic in the atomic floor

Inspect the proof of the audited complement theorem before its numerical endpoint.
The scalar lower input appears only as

\[
C_0\le C\le U,
\qquad
U={9t\over2}-2\pi-2\delta-\kappa/2.
\]

Every geometric statement after that point is independent of the numerical value of
`C_0`:

1. dominant orbit mass `M>=4Delta_2/C`;
2. complement train-count upper bound obtained from `C<=U`;
3. joint dominant-window occurrence-energy inequality `delta>=Phi(K)`;
4. fractional complement pair retention under hull-side capacity;
5. Section-157 two-sided actual-diameter bracing;
6. outer-pocket cyclic-order retraction;
7. three projective phase sectors of noncrossing trains;
8. the near-antipodal laminar capacity lemma; and
9. disjoint addition of dominant-window and complement terminal edge energies.

None of these steps invokes `0.00042`, AG42's old grid size, or a theorem whose scope
would fail for the stronger `g=0.0050` input.  The latter gap has independently been
proved for the same all-stopped-train scalar `C` and the same full-core Type-II scope.

**Verdict:** PASS.

---

## 2. Strengthening the lower bound on `C` gives the stated feasible triangle

Put

\[
C_{50}=2\sqrt{\Delta_2}+0.0050.
\]

The Section-171 upper envelope is unchanged, so

\[
C_{50}\le U
\]

is equivalent to

\[
2\delta+\kappa/2
\le
R_{50}(t):={9t\over2}-2\pi-C_{50}.
\]

This is the correct direction: increasing the atomic lower floor shrinks the feasible
`(delta,kappa)` triangle.  It does not enlarge the allowed detour.

At the maximal-detour boundary with `kappa=0`,

\[
\delta=R_{50}(t)/2,
\qquad U=C_{50}.
\]

**Verdict:** PASS.

---

## 3. Dominant and complement population bounds keep their directions

For fixed `U`, the complement train-count upper bound is

\[
N_*=U+{t+\kappa\over2}-{4\Delta_2\over U}.
\]

The dominant-window occurrence upper bound is

\[
K\le Q(\delta)=\Phi^{-1}(\delta).
\]

Thus complement trains carry at least

\[
\pi+\delta-Q(\delta)
\]

outer occurrences.  If `P_c` complement trains have two outer terminal incidences,
then all other complement trains have at most one, so

\[
P_c\ge\pi+\delta-Q(\delta)-N_*.
\]

Fractional hull-side retention loses at most `delta` pair mass, giving

\[
p_*
\ge
\pi-Q(\delta)-N_*.
\]

Substitution of the stronger `C_{50}` occurs only through `U>=C_{50}` and the final
maximal-detour endpoint.  No inequality reverses.

**Verdict:** PASS.

---

## 4. The two edge-energy payments remain disjoint

The candidate inherits exactly the same additive payment as the audited complement
theorem:

\[
\delta\ge F(z_*)+J(p_*),
\]

where

\[
z_*=\pi-t-\kappa-2U+8\Delta_2/U,
\]

\[
p_*=\left[\pi-Q(\delta)-U-(t+\kappa)/2+4\Delta_2/U\right]_+.
\]

The `F` term uses retained edge occurrences on trains inside the frozen dominant-orbit
windows.  The `J` term uses terminal edge occurrences on trains outside those windows.
The occurrence sets are disjoint before any scalar bound is inserted.  Replacing the
lower floor on `C` does not alter this disjointness.

**Verdict:** PASS.

---

## 5. `kappa=0` remains the weakest point

At fixed `t,delta`,

\[
{\partial z_*\over\partial\kappa}
={4\Delta_2\over U^2}>0.
\]

For

\[
N_*=U+(t+\kappa)/2-4\Delta_2/U,
\]

\[
{\partial N_*\over\partial\kappa}
=-{2\Delta_2\over U^2}<0.
\]

Therefore the complement retained-pair floor `p_*` increases with `kappa`.  Both
`F` and `J` are increasing on the relevant positive ranges.  Hence the contradiction
margin is minimized at

\[
\kappa=0.
\]

This argument is independent of the numerical atomic gap.

**Verdict:** PASS.

---

## 6. Maximal `delta` remains the weakest point

The stronger denominator `U>=C_{50}` only decreases the derivative coefficients that
contain `1/U^2`.  The companion certificate verifies on the full interval through
`t=1.82890` that

\[
z_*<1.30,
\qquad
p_*>0.61,
\qquad
Q(\delta)<1.61.
\]

The corresponding uniform bounds are

\[
F'(z_*)<0.024,
\]

\[
{\partial z_*\over\partial\delta}<8,
\]

\[
\Phi'(Q)<0.04,
\qquad
Q'(\delta)>25,
\]

\[
-\partial N_*/\partial\delta<4,
\]

and

\[
J'(p_*)>0.041.
\]

Therefore

\[
{\partial\over\partial\delta}
[F(z_*)+J(p_*)-\delta]
<8(0.024)-21(0.041)-1<-1.66.
\]

The contradiction margin strictly decreases with detour.  Thus the maximal allowed
`delta=R_50(t)/2` is the correct worst case.

**Verdict:** PASS.

---

## 7. Boundary formulas and monotonicity in `t`

At the worst feasible point,

\[
U=C_{50},\qquad\kappa=0,\qquad\delta=R_{50}(t)/2.
\]

The boundary quantities are

\[
z_{50}(t)=\pi-t-2C_{50}+8\Delta_2/C_{50},
\]

\[
N_{50}(t)=C_{50}+t/2-4\Delta_2/C_{50},
\]

\[
p_{50}(t)=\pi-Q(\delta)-N_{50}(t).
\]

Since `delta'(t)=9/4`, `z_50'(t)=-1`, and

\[
p_{50}'(t)
=-{9/4\over\Phi'(Q(\delta))}-{1\over2}<0,
\]

all three terms in

\[
\mathcal M_{50}(t)=F(z_{50})+J(p_{50})-\delta
\]

strictly decrease with `t`.  One positive endpoint value excludes every lower `t` in
the interval already covered from below by the preceding floor theorem.

**Verdict:** PASS.

---

## 8. Independent numerical verification

The committed Decimal certificate gives at `t=1.82890`

\[
\begin{aligned}
\delta_{50}&=0.0186195395462494\ldots,\\
z_{50}&=1.2927188367325205\ldots,\\
Q(\delta_{50})&=1.5996201137927153\ldots,\\
p_{50}&=0.6175356313684415\ldots,
\end{aligned}
\]

with contradiction margin

\[
\boxed{
\mathcal M_{50}(1.82890)
=0.0000622842731984975\ldots>0.
}
\]

It also finds

\[
\mathcal M_{50}(1.82891)>0.0000118
\]

and brackets the scalar zero by

\[
1.8289123539<t_*<1.8289123540.
\]

A separate Pyroam regression independently reproduced these signs and also checked the
coarse derivative bounds:

- `F'(1.30) = 0.02338...`;
- `Phi'(1.61) = 0.03495...`;
- `J'(0.61) = 0.04120...`;
- `dz/ddelta < 7.980`;
- `-dN/ddelta < 3.990`.

**Verdict:** PASS.

---

## 9. Scope and final disposition

The theorem is a missing composition, not a new geometric lemma.  It inherits all
scope restrictions of both dependencies:

- full-core/no-container Type II;
- proof-only matched atomic gap `g=0.0050`;
- audited complement outer-to-outer bracing geometry;
- Type-II near-disk perimeter and actual-diameter normalization.

It does not close C-II and does not construct a strict source-preserving diameter
decrease.  It safely raises the best current low-`t` floor to

\[
\boxed{1.82890}.
\]

The retained complement-pair population remains linear (`>0.617D`) at this endpoint,
so a useful next theorem must improve the noncrossing near-antipodal capacity or couple
these complement pairs directly to the near-extremal Woodall diameter topology.

**Final verdict:** PASS at proof-only full-core Type-II scope. C-II remains open.
