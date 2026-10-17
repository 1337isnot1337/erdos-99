> Generated reading edition · [exact source](../../../docs/reports/target_c_unit_cut_stress_projection_regression_2026-10-01.md) · source SHA-256 `28f21c2e3c8216bb001e9c4c3a27e63a65ca8653515ad3080c4b31ad1a408baa`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-8CD70C3B3ACA","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II — unit-cut stress projection and its two-shore shell regression

**Date:** 2026-10-01<br>
**Base:** `14b2c4cfd7e4ff828fbe62a8cfefebb4ca121e79`<br>
**Branch:** `swarm/gap-thrackle-20261001`<br>
**State:** `2026-09-14.audit.51`; Level I OPEN; C-II OPEN.<br>
**Classification:** proved candidate awaiting promotion for the necessary matrix;
regression for its proposed sufficiency.<br>
**External literature:** none.

```text
actual unit-cutsets + source stress kernel + transverse grid geometry
-> exclude the one-sided CROSS source system or integrate a strict competitor
-> Level I only after the other source branches are covered.
```

The attack here retains more of the first hypothesis than a geometric crosscut:
it tests the exact scalar matrix that unit-cutsets impose. The shell still passes
this projected condition. It is therefore insufficient by itself.

## 1. Exact necessary matrix from actual train cutsets

Work on the nonisolated positive-contact core `V`. Let `Omega=L_C-L_H` be
the canonical PSD scalar stress with its affine kernel. Select actual O–O
train shore indicators `f_i=1_(S_i)`; selected trains may be on both shores
of a complete rectangle. Assume their exact contact cutsets are pairwise
edge-disjoint, as they are for distinct actual trains. Put

```math
A_i=\sum_{e\in E(\tau_i)}\alpha_e>0,\qquad
E_{hi}=f_i(y_h)-f_i(x_h),\qquad B=\operatorname{diag}(\beta_h).
```

Let `F` have columns `f_i`. For the contact Laplacian,

```math
f_i^TL_Cf_j=
\sum_{e=xy\in C}\alpha_e(f_i(y)-f_i(x))(f_j(y)-f_j(x)).
```

Distinct cutsets are disjoint, so this is zero for `i!=j` and is `A_i`
for `i=j`. Similarly `F^TL_HF=E^TBE`. Thus necessarily

```math
\boxed{Q:=\operatorname{diag}(A_i)-E^TBE=F^T\Omega F\succeq0.}
\tag{1}
```

The exact vector cut balance also gives

```math
A_i u_i=\sum_h\beta_h E_{hi}(p_{y_h}-p_{x_h}).
\tag{2}
```

This uses the physical unit train direction and force convention, not a
generic rank theorem. Equation (1) applies jointly to both shores, with
all mixed diameter incidences retained. It is a necessary consequence of
canonical scalar PSD and actual unit cutsets. It does not assert that arbitrary
vectors satisfying (1) and (2) can be realized by those contact cutsets.

If `Q` has a null vector `c`, PSD implies that `Fc` lies in the affine
kernel of `Omega`. This is another necessary restriction, not a forced
Schur deficiency or a finite release theorem.

## 2. The two-shore odd shell passes the joint projected matrix

Use Section 7 of the [shell regression](target_c_odd_shell_gap_regression_2026-10-01.md):
`q=12t+1>=109`, `L=floor(q/100)`, and two axes at the actual polygon
vertices `0` and `2t+1`. Their separation is
`pi/3+5pi/(3q)`. Each shore has `L` positive-projection geometric cuts,
all at projections below `R/8`, and all cross-shore pairs intersect.

For each geometric cut define `A_i` by the axial actual diameter resultant
on its positive-projection side, with the actual uniform `beta_h=1/q`.
Reflection about the corresponding polygon vertex axis makes the transverse
component zero. These `A_i` are strictly positive. Define the **formal**
joint matrix `Q` by (1) with these masses and the actual diameter incidences.
The actual shell contact cutsets do not satisfy the diagonal contact-Gram
identity used to derive (1); the point is that the resulting necessary
matrix test nevertheless passes.

Every cut has

```math
A_i>D/8.
\tag{3}
```

To prove this, rotate its axis to the x-axis. All vertices with signed
indices `|j|<=floor(q/12)` have x-projection at least `R cos(pi/6)>R/8`,
so they lie on the positive side of every chosen cut. Their diameter partners
are on the negative side: their angles differ by `pi-pi/q`, and
`pi/6+pi/q<pi/3`. Each such diameter has axial displacement greater than
`R`, hence at least `D/2`, since `D<2R`.

There are at least `q/6-1` such positive-side vertices and exactly two
diameters per vertex. No edge is counted twice because its other endpoint
is negative. Thus

```math
A_i>{1\over q}(q/3-2){D\over2}>D/8
```

for `q>=109`. All remaining crossing diameter contributions have positive
axial projection and can be omitted for this lower bound.

For one diameter row, its total absolute incidence across the `2L`
selected cuts is at most `2L`. Put `T=E^TBE`. At every column,

```math
\sum_j|T_{ij}|
\le\sum_h\beta_h|E_{hi}|\sum_j|E_{hj}|
\le2L\sum_h\beta_h\le2L.
\tag{4}
```

By (1) of the shell report, `D>q/pi>q/4`, and `2L<=q/50`. Therefore

```math
Q_{ii}-\sum_{j\ne i}|Q_{ij}|
\ge A_i-\sum_j|T_{ij}|
>D/8-2L
>q/32-q/50={9q\over800}>0.
\tag{5}
```

The real symmetric matrix `Q` is strictly diagonally dominant with positive
diagonal, hence positive definite. For completeness this follows directly
by bounding each off-diagonal quadratic term using
`2|c_i c_j|<=c_i^2+c_j^2`; the result is
`c^T Q c >= sum_i (Q_ii-sum_(j!=i)|Q_ij|)c_i^2>0` for `c!=0`.

Thus the regression satisfies **joint** projected stress PSD, a trivial
projected nullspace consistent with the source affine kernel, and axial
vector balance on both geometric shores. It has the actual positive KKT
stress, PSD affine scalar kernel, and mixed rigidity proved in the shell
report. This does not repair its lack of actual unit-contact train cuts.

## 3. Failed closing step and exact next obligation

The matrix restriction (1) captures contact-cut disjointness only through
one scalar Gram identity. It forgets which physical source pairs supply
the unit contacts and where the actual rhombus faces lie. The shell's formal
matrix passes while its contact cycle has no non-singleton exact-phase
shore or quadratic rhombus core. Hence projected PSD plus the current
two-shore geometry is not sufficient for closure.

An attempted route using an upper bound on `A_i` from normalized diameter
weight also fails at the required scale: (2) gives only
`A_i<=D sum_(h crosses i) beta_h`, and the shell has `A_i=Theta(D)`.
Those train masses comfortably dominate the incidence Gram at the small
but linear extracted shore sizes. Positivity alone supplies no lower bound
on stress at each of the transverse rhombus contacts, so it does not force
the reaction centroids to sample the whole physical rectangle.

The surviving source-level bridge must retain actual contact positions,
train extensions and face/circuit closure, or a global competitor. Another
PSD test of the same abstract cut-incidence matrix is not a sufficient next
lemma. A two-bar force compression also must not be assumed to preserve
the strip's torque: moment preservation needs its own argument.

No contact-isolated point is dropped, no infinitesimal motion is integrated,
and no canonical source is replaced with a shell. This is a rejected
sufficiency claim and a precise surviving compatibility obligation, not a
proof of C-II or Level I.

## 4. Verification and dependencies

- Canonical: positive full-support normal form and PSD scalar stress on `V`
  from Sections 56–57; `C-WOODALL` for actual diameter geometry.
- Unpromoted conditional application: the October 1 complete O–O rectangle
  and exact train-cutset extraction.
- Self-contained new proof: equations (1)–(5).
- Companion exact verifier: `verify_target_c_odd_shell_gap_regression.py`
  certifies the discrete two-shore system and all the listed finite
  algebraic source stresses/ranks. It does not perform floating-point PSD
  decisions; (5) is an analytic uniform positive-definiteness certificate.

The `9q/800` margin is a sufficient margin for this formal regression;
it is not a bound on a canonical global minimizer's stress eigenvalues.
