> Generated reading edition · [exact source](../../../docs/reports/target_c_paired_gap_cubic_capacity_2026-09-10.md) · source SHA-256 `4bce611fd089f661d6df24a6391c45882549166b551d50d00989e538aa2eac84`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-9DE1FC330303","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — paired cyclic gaps constrain the DD cubic moment

**Date:** 2026-09-10  
**Repository state:** branch `research/c-ii-cyclic-gap-2026-09-10`, after paired MADD endpoint exclusion  
**Run type:** structural convex/contact coupling  
**Target:** Target C, C-II after FS/MA/OP/DD  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The paired-pocket loss at exact MADD equality has a uniform form. Let a normalized
force-hull limit have projective missing-circle gaps `alpha_i`. Each positive projective
gap lifts to **two** antipodal macroscopic force-hull sides, so the corresponding OP
outer-pocket chain lower bounds occur in pairs.

If

```math
X:=\sum_i\alpha_i,
\qquad
c_X:=\sin(X/2),
```

and the total normalized old-contact chain length is at most `L`, then the paired gap
obligations imply

```math
\boxed{
\limsup\frac{\sum_P\ell_P^3}{D^3}
\le
(L-c_X)^3+c_X^3,
}
\tag{PG.1}
```

provided `c_X<=L/2`.

For the post-ZF source, perimeter feasibility itself lower-bounds `X`. On the critical
range `2rho<=y<pi/2`, if

```math
y=\lim h/D,
\qquad
z=\lim(Q+2s_Z)/D,
```

let `theta(y,z)` be the unique solution in `(0,pi/2)` of

```math
\boxed{
\theta-\sin\theta
=\frac\pi2-y+\frac z2.
}
\tag{PG.2}
```

Then

```math
\boxed{X\ge2\theta(y,z),}
\tag{PG.3}
```

so PG.1 holds with the smaller, explicit lower bound

```math
\boxed{c_X\ge c(y,z):=\sin\theta(y,z).}
\tag{PG.4}
```

This is the missing structural input that the scalar DD bound discarded.

---

## 1. Gap sides occur in antipodal pairs

Let `K_infty` be any normalized force-hull limit supplied by FS/MA. It is centrally
symmetric, contained in the radius-`1/2` disk, and every extreme point lies on the
boundary circle.

Let the complementary open intervals of its circle set on the projective circle have
lengths

```math
\alpha_1,\alpha_2,\ldots>0.
```

A projective gap of length `alpha_i` lifts to two antipodal ordinary-circle gaps of the
same angular length. The convex hull replaces each missing arc by a chord of length

```math
\boxed{c_i=\sin(\alpha_i/2)}
\tag{1.1}
```

in the normalization where the circle radius is `1/2`.

FS radial vertex localization implies that, for each fixed positive limit gap, the
finite force hull has a side converging to each of these two antipodal chords. The
argument is the same as in the paired MADD endpoint report: finite force-hull vertices
cannot converge to the interior of a missing circle arc because every such vertex is
`o(1)` from the radius-`1/2` circle.

Each chord has physical length `c_iD+o(D)`, hence is not a unit contact. OP therefore
assigns each of the two sides to a distinct outer pocket. If the corresponding contact
chain lengths are `ell_i^+` and `ell_i^-`, the triangle inequality gives

```math
\boxed{
\ell_i^\pm/D\ge c_i-o(1).
}
\tag{1.2}
```

---

## 2. Every one pocket leaves a fixed amount of chain in the others

Put

```math
S:=\sum_i c_i,
\qquad
c_{max}:=\sup_i c_i.
```

The total paired lower-bound mass is `2S`.

For any one outer pocket `P`, even if `P` is one of the two pockets associated with a
largest gap, the other pockets have total normalized chain length at least

```math
2S-c_{max}-o(1).
\tag{2.1}
```

If `P` is not one of those paired gap pockets, the lower bound is even `2S-o(1)`.

Now repeated gap merging gives

```math
S=\sum_i\sin(\alpha_i/2)
\ge\sin\left(\frac12\sum_i\alpha_i\right)
=\sin(X/2).
\tag{2.2}
```

Also `c_max<=S`, so

```math
2S-c_{max}\ge S\ge\sin(X/2).
\tag{2.3}
```

Consequently, writing

```math
c_X:=\sin(X/2),
```

we have the asymptotic **outside-every-pocket** bound

```math
\boxed{
\sum_{P'\ne P}\frac{\ell_{P'}}D
\ge c_X-o(1)
\qquad\text{for every outer pocket }P.
}
\tag{2.4}
```

For countably many projective gaps, apply the finite argument to the first `N` gaps and
then let `N->infinity`; monotone convergence gives (2.2)--(2.4).

---

## 3. Cubic moment under an outside-mass constraint

### Lemma PG.1

Let `r_1,r_2,...>=0` have total at most `L`, and suppose every coordinate leaves at
least `c` in the others:

```math
\sum_{j\ne i}r_j\ge c
\qquad\text{for every }i.
\tag{3.1}
```

If `0<=c<=L/2`, then

```math
\boxed{
\sum_i r_i^3\le(L-c)^3+c^3.
}
\tag{3.2}
```

### Proof

Condition (3.1) says every coordinate is at most `L-c`. Among nonnegative vectors with
total at most `L` and coordinate cap `L-c`, a convex function is maximized by filling
one coordinate to the cap, then putting the remaining mass `c` into a second
coordinate. Thus the extremal vector is `(L-c,c,0,...)` up to permutation, giving
(3.2). Equivalently, repeatedly transfer mass from the smaller of two non-cap
coordinates to the larger until at most one non-cap positive coordinate remains.
`square`

Apply the lemma to `r_P=ell_P/D`, use (2.4), and pass to the limit. This proves PG.1.

---

## 4. Perimeter feasibility lower-bounds the total missing angle

Let

```math
p:=\lim P_F/D.
```

The exact cyclic gap formula from MA is

```math
p
=\pi-X+2\sum_i\sin(\alpha_i/2).
\tag{4.1}
```

By (2.2),

```math
\boxed{
p\ge f(X):=\pi-X+2\sin(X/2).}
\tag{4.2}
```

On the other hand ZE and OP give

```math
p\le\lim b/D=2y-z.
\tag{4.3}
```

On `2rho<=y<pi/2`, DB gives `0<=z<=u(y)`, so `2y-z<pi`. The function

```math
f(X)=\pi-X+2\sin(X/2)
```

has

```math
f(0)=\pi,
\qquad
f'(X)=-1+\cos(X/2)<0
\quad(X>0).
```

Hence there is a unique `X_0 in (0,pi)` with

```math
f(X_0)=2y-z.
\tag{4.4}
```

Equation (4.2)--(4.3) forces

```math
\boxed{X\ge X_0.}
\tag{4.5}
```

Write `X_0=2theta`. Then (4.4) is exactly

```math
\pi-2\theta+2\sin\theta=2y-z,
```

or PG.2. Since `sin` is increasing on `(0,pi/2)`, (4.5) gives PG.4.

---

## 5. Post-ZF paired DD capacity

PC/DD give the total chain-length bound

```math
\limsup\frac{L_{chain}}D\le2(y-z).
\tag{5.1}
```

For the critical range considered here, `c(y,z)<1<y-z` whenever the source is feasible,
so the `c<=L/2` condition in Lemma PG.1 is automatic in the nontrivial limit.

Combining PG.1, PG.4, and (5.1) gives

```math
\boxed{
\limsup\frac{\sum_P\ell_P^3}{D^3}
\le
[2(y-z)-c(y,z)]^3+c(y,z)^3.
}
\tag{5.2}
```

DD before its scalar cubic relaxation gives

```math
H_{out}
\le
\frac1{\sqrt6}
\left(\sum_P\ell_P^3\right)^{1/2}
(b-P_F)^{1/2}.
\tag{5.3}
```

MA gives `P_F/D>=p_0(y)-o(1)`, so

```math
\limsup\frac{b-P_F}{D}
\le u(y)-z.
\tag{5.4}
```

Therefore

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{[2(y-z)-c(y,z)]^3+c(y,z)^3}
\sqrt{u(y)-z}.
}
\tag{5.5}
```

This strictly improves scalar DD whenever `c(y,z)>0` and `u(y)>z`.

---

## 6. A convenient z-free relaxation

For later explicit optimization define `theta_0(y)=theta(y,0)` and

```math
c_0(y):=\sin\theta_0(y),
\qquad
\theta_0-\sin\theta_0=\frac\pi2-y.
\tag{6.1}
```

Equation PG.2 shows `theta(y,z)>=theta_0(y)`, hence

```math
c(y,z)\ge c_0(y).
\tag{6.2}
```

Also

```math
2(y-z)\le2y,
\qquad
u(y)-z\le u(y).
```

For `c<y`, the function

```math
M(L,c)=(L-c)^3+c^3
```

is increasing in `L` and decreasing in `c` on `c<=L/2`. Thus (5.5) implies the
simpler universal bound

```math
\boxed{
\limsup\frac{H_{out}}{D^2}
\le
\frac1{\sqrt6}
\sqrt{[2y-c_0(y)]^3+c_0(y)^3}
\sqrt{u(y)}.
}
\tag{6.3}
```

CC separately gives

```math
\limsup\frac{A_{exc}}{D^2}
\le\frac{z^2}{4\pi}
\le\frac{u(y)^2}{4\pi}.
\tag{6.4}
```

Equations (6.3)--(6.4) produce a one-variable cavity capacity used in the adjacent
explicit-floor report.

---

## 7. Regression audit

- **Full regular odd shell:** on the relevant limiting disk `X=0`, hence `c_X=0`; PG
  correctly reduces to the old scalar cubic bound.
- **One macroscopic missing interval:** PG is sharp at the level of paired lower bounds:
  there are exactly two mandatory chains of chord length `sin(X/2)`.
- **Many tiny gaps:** splitting increases total paired chord lower-bound mass. PG does
  not incorrectly treat those gaps as free.
- **One giant detour chain with tiny chord:** it may be the largest chain, but all
  macroscopic cyclic-gap chord obligations remain in the other pockets and enforce
  (2.4).
- **Dense isolated fillings:** the cyclic limit comes from FS/MA on the global source;
  PG does not infer global optimality from an arbitrary annular filling.

---

## 8. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| each projective gap gives two macroscopic OP sides | proved asymptotically | central symmetry + FS radial vertex localization + OP |
| outside-every-pocket mass `>=sin(X/2)` | proved | paired chord mass + gap-merging inequality |
| cubic moment PG.1 | proved | convex concentration under a coordinate cap |
| missing-angle lower bound PG.3 | proved | cyclic perimeter lower bound + `P_F<=b` |
| defect-aware capacity (5.5) | proved | PG + DD + MA perimeter |
| z-free capacity (6.3) | proved | monotonic relaxations |
| Level I | still open | the resulting capacity still permits positive-surplus survivors |

---

## 9. Exact next implication

Combine (6.3)--(6.4) with the MA/GU lower gap and the independent MA/JC threshold.
The paired cubic constraint is large enough to move the explicit pinned/contact floor
above `0.60`; the optimization is one-dimensional and requires no new geometric
assumption.
