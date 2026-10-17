# Target C-II — exact turn-angle identities exclude eight more convex support-seven `H8` orbits

**Date:** 2026-09-19  
**Claim class:** exact affine exclusion inside the degree-pure support-seven endpoint  
**Scope:** fully convex `H8` branch after the support-seven endpoint reduction  
**Depends on:** `target_c_support7_endpoint_reduction_2026-09-19.md`; audited force/raw-angle conversion; exact reciprocal triangle angle sum; strict pentagon one-turn and adjacent-two-turn bounds  
**Certificate:** `research/verify_target_c_support7_h8_angle_exclusion_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The first support-seven endpoint reduction leaves 20 fully convex reciprocal `H8` reflection orbits after removing the two ground-`2+5` trace cases and one direct ground-projection case. Eight of those 20 violate exact affine triangle-angle identities together with the already-proved strict turn inequalities of the seven physical pentagons.

Therefore the fully convex support-seven branch drops to

\[
\boxed{12\text{ reflection orbits}=9\ C_7+3\ (C_3\sqcup C_4).}
\tag{A.0}
\]

This does not exclude support seven. The remaining 12 convex cases and the nonconvex `H6/H7` branches remain.

---

## 1. Exact angle variables

Fix one of the fully convex reciprocal candidates with hull order

\[
0,1,\ldots,7,
\]

where `0` is the reciprocal ground point. Let `P` be one chosen positive reciprocal-edge sign class and let `M` be the seven missing non-ground edges.

At vertex `i`, delete from the convex raw-ray order

\[
i+1,i+2,\ldots,i+7\pmod 8
\]

the neighbors joined to `i` by missing edges. The result is the raw order of the present reciprocal rays. For each present ray, keep it if its reciprocal sign is positive and reverse it by `pi` if its sign is negative. Because the raw rays lie in one open hull cone of width `<pi`, the force-cycle order is exactly

\[
(\text{positive raw rays in raw order}),
(\text{negative raw rays in raw order}).
\tag{1.1}
\]

At every non-ground vertex this cycle has length five. At the ground it has length seven.

Let

\[
x_{i,k}={\delta_{i,k}\over\pi}
\]

be the normalized counterclockwise gap after force ray `k` in this force cycle. Put

\[
p_{i,k}=x_{i,k}+x_{i,k+1}
\]

cyclically at a non-ground pentagon.

The physical strict equilateral-pentagon theorems already give, for every `i=1,...,7`,

\[
0<x_{i,k}<\frac23,
\qquad
\frac23<p_{i,k}<1.
\tag{1.2}
\]

At the ground, distinct force rays give only the positivity needed below:

\[
x_{0,k}>0.
\tag{1.3}
\]

Every complete force cycle satisfies

\[
F_i:=\sum_kx_{i,k}=2.
\tag{1.4}
\]

---

## 2. Reciprocal triangle angles are exact affine functions of force gaps

For every present reciprocal triangle `abc`, let `T_abc` be the sum of its three ordinary raw interior angles divided by `pi`. Convex Euclidean geometry gives

\[
T_{abc}=1.
\tag{2.1}
\]

The audited force-to-raw conversion used in the support-six `H5` exclusion applies verbatim. If `R_i(a,b)` is the counterclockwise force-ray arc from edge `ia` to edge `ib`, then the ordinary raw angle at `i`, divided by `pi`, is one of

\[
R_i(a,b),\quad
2-R_i(a,b),\quad
R_i(a,b)-1,\quad
1-R_i(a,b),
\tag{2.2}
\]

according to the two edge signs and the exact raw orientation of the rays. Thus every `T_abc` is an affine integer-coefficient function of the `x_{i,k}`.

The companion verifier reconstructs these affine forms from only:

- the missing graph `M`;
- the positive edge set `P`;
- the convex hull order `0,...,7`.

No coordinates, floating point, optimization, or numerical rank calculation enter the certificate.

---

## 3. Eight sparse boundary identities

For each of the eight cases below, define a linear functional `C` of the force gaps. The listed strict inequalities from (1.2)--(1.3) imply

\[
C<B.
\tag{3.1}
\]

But exact affine coefficient comparison expresses the same `C` as a combination of `F_i` and `T_abc`. Substitution of `F_i=2` and `T_abc=1` forces

\[
C=B,
\tag{3.2}
\]

a contradiction.

The identities are:

### Case A: `C7`

\[
C=-p_{2,0}-p_{2,2}-p_{3,0}+p_{6,1}
=-F_3+F_6-T_{236}=-1.
\tag{3.3}
\]

By (1.2),

\[
C<-\frac23-\frac23-\frac23+1=-1.
\]

### Case B: `C7`

\[
C=x_{3,4}-p_{4,0}+p_{7,1}
=F_3-F_4+F_7-T_{347}=1.
\tag{3.4}
\]

But

\[
C<\frac23-\frac23+1=1.
\]

### Case C: `C7`

\[
C=p_{3,3}-p_{6,0}+x_{7,2}
=F_0-T_{036}+T_{037}-T_{067}=1,
\tag{3.5}
\]

whereas

\[
C<1-\frac23+\frac23=1.
\]

### Case D: `C3+C4`

\[
C=x_{3,1}-p_{4,2}+p_{7,4}
=F_3-F_4+F_7-T_{347}=1,
\tag{3.6}
\]

while again `C<1`.

### Case E: `C3+C4`

\[
C=-x_{0,4}-p_{3,2}-p_{4,2}-p_{5,2}
=-F_4+F_5-T_{035}-T_{345}=-2.
\tag{3.7}
\]

Since the ground gap is strict positive and the three physical adjacent pairs are each `>2/3`,

\[
C<0-3\cdot\frac23=-2.
\]

### Case F: `C3+C4`

\[
\begin{aligned}
C={}&-x_{0,0}-p_{2,0}-p_{3,0}-p_{3,1}-p_{6,0}+x_{7,2}\\
={}&2-F_2-F_6+F_7-T_{023}-T_{367}=-2.
\end{aligned}
\tag{3.8}
\]

The strict bounds give

\[
C<0-4\cdot\frac23+\frac23=-2.
\]

### Case G: `C3+C4`

\[
C=p_{3,4}-p_{6,0}+x_{7,2}
=F_3-F_6+F_7-T_{367}=1,
\tag{3.9}
\]

but `C<1-2/3+2/3=1`.

### Case H: `C3+C4`

\[
C=p_{2,4}-p_{5,0}+x_{6,2}
=4-F_5-T_{025}+T_{026}-T_{056}=1,
\tag{3.10}
\]

while `C<1-2/3+2/3=1`.

Every contradiction is strict. None uses a limiting or generic-position argument beyond the already-audited strict convex `H8` setting.

---

## 4. Exact orbit identification

For reproducibility, the certificate identifies each case by its labelled missing-edge set `M` and one positive sign set `P`; global sign reversal does not create a new candidate. The eight missing sets are:

\[
\begin{array}{c|l}
A&12,16,27,34,35,46,57\\
B&13,16,23,27,45,46,57\\
C&13,17,24,27,35,46,56\\
D&12,13,23,45,46,57,67\\
E&12,13,23,46,47,56,57\\
F&12,17,27,34,35,46,56\\
G&13,17,23,27,45,46,56\\
H&12,16,27,34,35,45,67.
\end{array}
\tag{4.1}
\]

The verifier first reproduces the preceding 20-orbit census, then asserts that each `(type,M,P)` triple is present before checking its affine identity. Thus the proof does not rely on an unverified case-number convention.

Of the eight excluded cases, three have missing type `C7` and five have type `C3+C4`.

---

## 5. New convex endpoint

Before this note, the endpoint reduction left

\[
12\ C_7+8\ (C_3\sqcup C_4)=20
\]

fully convex reflection orbits.

The eight exact turn contradictions remove

\[
3\ C_7+5\ (C_3\sqcup C_4),
\]

so the fully convex branch is now

\[
\boxed{9\ C_7+3\ (C_3\sqcup C_4)=12.}
\tag{5.1}
\]

This is a finite reduction, not a support-seven exclusion. The remaining 12 orbits pass the linear system consisting of the exact reciprocal triangle-angle identities and the strict one-turn/two-turn pentagon bounds with positive margin; stronger metric or nonlinear closure information is required for them.

The nonconvex `H6/H7` branches are untouched here.

No theorem-state file is changed.

**Disposition:** eight additional fully convex support-seven reciprocal orbits are impossible by sparse exact triangle-angle/turn-bound identities; the convex `H8` branch drops from 20 to 12 reflection orbits. C-II remains open.
