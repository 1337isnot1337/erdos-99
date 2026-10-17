> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d2_s2_exclusion_2026-09-09.md) · source SHA-256 `f38823eaf2f634a4dd28c4a6e46705274f1cf5fbfeb2b2b625cf4171e0b534fa`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 27 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-D89F55E29422","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=2` is impossible

**Date:** 2026-09-09  
**Run type:** exact S2 exclusion / complete `d_H=2` phase closure  
**Target:** primitive cyclic endpoint `d_H=2`, final AD/S2 branch  
**Depends on:** CP2 two-circular-path theorem and PSX center-separation formulas on this branch; PX P2 exclusion on PR #139  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

PX excludes P2 and PSX excludes PS. The only remaining AD branch for `d_H=2` is S2:

```math
r_\parallel=0,
\qquad
a_{short}=2.
```

CP2 identifies its complete antipodal graph canonically as

```math
T=H\cup\{g_1,g_2\},
```

where

- `H=P_A sqcup P_B` is the disjoint union of two circular diameter paths;
- `g_1,g_2` are two genuine short antipodal K-vertices;
- both `g_i` join the two path components and lie on the unique odd cycle of the maximal antipodal thrackle.

The two short states must represent the same component-center displacement

```math
S=C_B-C_A.
```

The exact defect-center map from PSX makes that impossible.

### Theorem S2X — S2 exclusion

For every sufficiently large primitive cyclic source,

```math
\boxed{d_H\ne2.}
\tag{S2X.1}
```

In fact the proof below works once the preceding CP2/PSX reductions apply and `D>=3`.

Therefore the cyclic endpoint is reduced to

```math
\boxed{d_H\in\{0,1\}.}
\tag{S2X.2}
```

Equivalently the zero-stress-surplus phase

```math
s_Z=0
```

is completely eliminated from the primitive cyclic branch.

---

## 1. Recall the one-defect center map

For a genuine short state `g` put

```math
|g|=\rho,
\qquad
L:=\sqrt{D^2-1}.
```

PSX proves strict convexity forces

```math
L<\rho<D.
```

Rotate so

```math
g=\rho e,
\qquad |e|=1.
```

Its neighboring actual diameter states are

```math
x=D(\cos a\,e-\sin a\,Je),
\qquad
y=D(\cos a\,e+\sin a\,Je),
```

with

```math
|g-x|=|g-y|=1.
```

Define

```math
\boxed{
\lambda
:=\rho-D\cos a
=\frac{\rho^2-D^2+1}{2\rho}.}
\tag{1.1}
```

Then

```math
\boxed{0<\lambda<\frac1{2D}}
\tag{1.2}
```

and

```math
\boxed{\lambda^2+D^2\sin^2a=1.}
\tag{1.3}
```

Let

```math
h_D:=\frac1{4\cos(\delta/2)},
\qquad
\delta=2\arcsin\frac1{2D}.
```

The fixed vector

```math
S=C_B-C_A
```

has one of three forms.

### Band I: same circle-side signs, subtracting

```math
\boxed{
S=-(\mu-\lambda)e,
\qquad
\mu:=2h_D\sin a,}
\tag{1.4}
```

with

```math
0<\mu-\lambda<s_L,
\qquad
s_L:=\frac{2h_D}{D}.
```

### Band II: same circle-side signs, adding

```math
\boxed{
S=(\mu+\lambda)e,}
\tag{1.5}
```

with, for `D>=3`,

```math
s_L<\mu+\lambda<s_S,
\qquad
s_S:=\frac{2h_D\sqrt{D^2-1}}{D}.
```

### Band III: opposite circle-side signs

```math
\boxed{
S=\lambda e+\tau\kappa Je,
\qquad
\tau\in\{+1,-1\},
\qquad
\kappa:=2h_D\cos a,}
\tag{1.6}
```

and

```math
|S|>s_S.
```

Thus the three types occupy disjoint magnitude intervals

```math
(0,s_L),
\quad
(s_L,s_S),
\quad
(s_S,\infty).
\tag{1.7}
```

---

## 2. The magnitude is injective inside each band

Equation (1.3) and `2h_D/D=s_L` give

```math
\boxed{
\mu=s_L\sqrt{1-\lambda^2}.}
\tag{2.1}
```

Therefore the Band-I magnitude is

```math
f_-(\lambda)
=s_L\sqrt{1-\lambda^2}-\lambda.
```

It is strictly decreasing:

```math
f_-'(\lambda)
=-\frac{s_L\lambda}{\sqrt{1-\lambda^2}}-1<0.
\tag{2.2}
```

The Band-II magnitude is

```math
f_+(\lambda)
=s_L\sqrt{1-\lambda^2}+\lambda.
```

For `0<lambda<1/(2D)` one has

```math
\frac{s_L\lambda}{\sqrt{1-\lambda^2}}<1,
```

so

```math
f_+'(\lambda)
=1-\frac{s_L\lambda}{\sqrt{1-\lambda^2}}>0.
\tag{2.3}
```

For Band III, PSX gives the exact identity

```math
\boxed{
|S|^2
=s_S^2+\frac{4D^2}{4D^2-1}\lambda^2,}
\tag{2.4}
```

which is strictly increasing in `lambda>0`.

Hence in each magnitude band the map

```math
\lambda\longmapsto |S|
```

is injective.

---

## 3. The two S2 defects have identical local scalar geometry

Let the two genuine short states have parameters

```math
(\lambda_1,a_1,\rho_1),
\qquad
(\lambda_2,a_2,\rho_2).
```

Both represent the same vector `S`, hence certainly the same magnitude `|S|`.

By the disjoint bands (1.7), they must belong to the same band. By Section 2's injectivity,

```math
\boxed{\lambda_1=\lambda_2=: \lambda.}
\tag{3.1}
```

Then (1.3), with `a_i in (0,pi/2)`, gives

```math
\boxed{a_1=a_2=:a.}
\tag{3.2}
```

Since (1.1) is strictly increasing in `rho` on `(L,D)`, also

```math
\boxed{\rho_1=\rho_2.}
\tag{3.3}
```

Thus the two short vertices have exactly the same radius and the same local angular defect.

Put

```math
\boxed{G:=2a.}
\tag{3.4}
```

Each short radial direction is the angular midpoint of its two neighboring actual diameter directions, and the neighboring diameter directions are separated by `G`.

---

## 4. Bands I and II are impossible for two distinct short states

In Band I, equation (1.4) says

```math
S=-f_-(\lambda)e.
```

The scalar `f_-(lambda)>0` is now the same at both defects. Therefore equality of the vector `S` forces

```math
e_1=e_2.
```

But `e_1,e_2` are the two distinct projective radial directions of distinct K-vertices in one projective half-boundary. They cannot coincide.

Thus Band I is impossible.

In Band II, equation (1.5) gives

```math
S=f_+(\lambda)e,
```

with the same positive scalar at both defects. Again `S` equality forces

```math
e_1=e_2,
```

impossible.

Therefore both S2 defects must be in Band III.

---

## 5. Band III fixes the angular separation of the two defects

In Band III,

```math
S=\lambda e_i+\tau_i\kappa Je_i,
\qquad
\tau_i\in\{+1,-1\},
```

with common positive parameters `lambda,kappa` by Section 3.

Identify the plane with the complex numbers and write

```math
e_i=e^{i\theta_i}.
```

Put

```math
\boxed{
\psi:=\arctan\frac\kappa\lambda
\in(0,\pi/2).}
\tag{5.1}
```

Then

```math
S
=\sqrt{\lambda^2+\kappa^2}
\,e^{i(\theta_i+\tau_i\psi)}.
\tag{5.2}
```

If `tau_1=tau_2`, equality of `S` forces `theta_1=theta_2 mod 2pi`, again impossible for distinct projective states in the same half-boundary.

Hence

```math
\boxed{\tau_2=-\tau_1.}
\tag{5.3}
```

Order the projective short directions so

```math
0<\theta_2-\theta_1<\pi.
```

After swapping indices if needed, (5.2)-(5.3) give

```math
\boxed{
\theta_2-\theta_1=2\psi.}
\tag{5.4}
```

Therefore the two arcs between the short radial directions on the projective direction circle have lengths

```math
\boxed{2\psi}
\qquad\text{and}\qquad
\boxed{\pi-2\psi.}
\tag{5.5}
```

---

## 6. The shorter center-forced arc is too short to contain a diameter component

We compare `pi-2psi` with the local defect gap `G=2a`.

From Section 2 / PSX,

```math
\mu=2h_D\sin a>\lambda
\tag{6.1}
```

for every genuine short state. Since

```math
\kappa=2h_D\cos a,
```

(6.1) is equivalent to

```math
\frac\kappa\lambda
>
\frac{\cos a}{\sin a}
=\cot a.
```

Both sides are positive, so

```math
\psi
=\arctan\frac\kappa\lambda
>
\arctan(\cot a)
=\frac\pi2-a.
\tag{6.2}
```

Therefore

```math
\boxed{
\pi-2\psi<2a=G.}
\tag{6.3}
```

Now use CP2. The two short states cut the projective antipodal sequence into the two diameter-path blocks `P_A,P_B`. Suppose one path has `m>=1` edges. Starting at the radial direction of one short state:

- the first actual diameter direction is `a` radians away;
- the `m` path edges contain `m-1` ordinary projective gaps, each exactly `delta`;
- the last actual diameter direction is another `a` radians from the next short radial direction.

Hence the projective angular length of that complete short-to-short arc is

```math
\boxed{
G+(m-1)\delta
=2a+(m-1)\delta
\ge G.}
\tag{6.4}
```

Both D2 components are nontrivial, so both projective arcs between `g_1,g_2` have this form with `m>=1`. Therefore **both** arcs have length at least `G`.

But Section 5 says one of the same two arcs has length `pi-2psi`, and (6.3) says

```math
\pi-2\psi<G.
```

Contradiction.

Thus S2 is impossible. `square`

---

## 7. Complete closure of `d_H=2`

The AD defect split for `d_H=2` was exhaustive:

```text
P2: two parallel ties, no genuine short pair;
PS: one parallel tie, one genuine short pair;
S2: no ties, two genuine short pairs.
```

The three exclusions are now:

- PX: P2 impossible for `D>sqrt2`;
- PSX: PS impossible for `D>=3`;
- S2X: S2 impossible under the same sufficiently-large endpoint hypotheses.

Therefore:

### Corollary S2X.1 — zero-surplus cyclic phase exclusion

For every sufficiently large primitive cyclic Target C survivor,

```math
\boxed{d_H\le1.}
\tag{7.1}
```

Since the exact cyclic ledger is

```math
d_H+s_Z=2,
```

this is equivalently

```math
\boxed{s_Z\ge1.}
\tag{7.2}
```

The unique-stress / zero-surplus phase is gone completely.

The only remaining primitive cyclic topologies are

```text
d_H=0, s_Z=2: exact Reinhardt unicyclic family;
d_H=1, s_Z=1: one spanning diameter tree, S1 or P1.
```

---

## 8. Strategic consequence

This is the first complete removal of one of the three exact post-ZF cyclic topology phases.

It also validates the defect-center method as more than a P2 special trick. The key invariant is the fixed displacement between the two universal component circles. The three possible local KKT-independent center-separation bands are mutually exclusive enough that two genuine short defects cannot close around the projective circle.

The remaining `d_H=1` tree phase has only one diameter component, so this two-center obstruction does not transfer directly. Its live S1/P1 endpoints must be attacked by their signed-closure / endpoint-KKT structures.

---

## 9. Regression audit

### Equal short radii were derived, not assumed

S2 does not begin with any symmetry between its two off-circle vertices. Equality of the fixed center-separation magnitude, the disjoint three-band decomposition, and monotonicity inside each band force `lambda_1=lambda_2`, then `a_1=a_2` and `rho_1=rho_2`.

### Projective versus oriented directions

The two short states are represented in one projective half, so their oriented radial angles may be chosen with difference strictly between zero and `pi`. This makes the Band-III equation select the `2psi` separation rather than an ambiguous `2pi-2psi` lift.

### Both path blocks are nonempty

D2's two components are nontrivial trees, so each has at least one diameter edge. Thus each short-to-short projective arc contains `m>=1` actual state and has length at least `2a`.

### No use of KKT coefficient equality

The S2 exclusion is purely geometric after CP2. It does not use P2's equal transition stresses and therefore survives independently of that special endpoint.

---

## 10. Next theorem

With `d_H=2` removed, the primitive cyclic campaign has only two phases.

The shortest remaining finite phase is `d_H=1`. Its AD split is

```text
P1: one parallel tie, no genuine short vertex;
S1: no tie, one genuine short vertex.
```

Unlike `d_H=2`, there is only one diameter component, so no center-difference invariant exists. The strongest current endpoints are:

- P1: exact rectangle/twin completion plus the Littlewood root condition;
- S1: canonical short cycle edge, exact signed-closure equations, and two KKT endpoint cuts.

A complete `d_H=1` exclusion would leave only the exact Reinhardt `d_H=0` family.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN, but d_H=2 is completely excluded.

In S2, both short K states are genuine. For one defect define
  lambda=(rho^2-D^2+1)/(2rho) in (0,1/(2D)),
  lambda^2+D^2 sin^2 a=1,
  h=1/[4cos(delta/2)].
The fixed component-center displacement S has three magnitude bands:
  I: |S|=2h sin a-lambda in (0,s_L),
 II: |S|=2h sin a+lambda in (s_L,s_S),
III: |S|^2=s_S^2+4D^2 lambda^2/(4D^2-1) > s_S^2.
Each band magnitude is strictly monotone in lambda.

The two defects represent the same S, so they lie in the same band and have equal
lambda, hence equal local half-angle a.
Bands I/II make S radial or antiradial; equal S would force the two distinct short
projective directions to coincide, impossible.
Thus both are Band III:
  S=lambda e_i+tau_i kappa J e_i,
  kappa=2h cos a.
Equal S forces opposite tau and projective separation 2psi, psi=atan(kappa/lambda).
But 2h sin a>lambda, so psi>pi/2-a and
  pi-2psi<2a.
The two short states bound the two nonempty diameter-path blocks. Each short-to-short
projective arc has length
  2a+(m-1)delta >=2a.
One of those arcs is pi-2psi<2a: contradiction.

Therefore S2 impossible. Together with PX and PSX, all d_H=2 cyclic survivors are
excluded for large D. Remaining cyclic phases: d_H=0 and d_H=1 only.
```
