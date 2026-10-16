<!-- theorem-state: {"artifact_id":"ART-7C64275A1E46","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: universal PSD and null-face selection

**Date:** 2026-08-31  
**Repository base:** `679eb736` (main after C53 / PR #54)  
**Run type:** exact second-order/KKT-polytope reduction  
**Target:** Target C Gate C-I  
**Depends on:** C6 critical-cone duality, C13.3 direction-dependent second-order certificate, C22 two-terminal collapse mechanism, C53 universal two-dimensional response PSD

## LEVEL I STATUS

**STILL OPEN.**

C53 proves that every normalized KKT stress with two-dimensional positive diameter
endpoint hull has positive semidefinite signed stress matrix. This report closes the
remaining one-dimensional selected-support case and then exploits the quantifiers in
C13.3.

The result is stronger than selecting one zero-energy stress for one critical
velocity. There is one **extreme normalized KKT stress** whose PSD stress matrix
annihilates the entire linear span of the fixed-diameter critical cone, equivalently
the complete infinitesimal-flex space of the maximal strong framework.

Thus C-I is reduced to the geometry of one extreme positive equilibrium circuit and
its stress kernel.

## 1. C54.1 — the one-dimensional selected support is PSD

### Lemma C54.1

Let `s=(alpha,beta)` be any normalized KKT stress whose positive diameter endpoint
set `B=V(H_s)` is one-dimensional. Then `B` consists of exactly two source hull
vertices `b,k`, `H_s={bk}`, `beta_bk=1`, the connected positive contact graph is one
straight unit chain from `b` to `k`, and

\[
\boxed{\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta)\succeq0.}
\tag{C54.1}
\]

Its scalar kernel on the positive-contact vertices is exactly the affine functions
of the chain coordinate.

#### Proof

Every diameter endpoint is a genuine convex-hull vertex after the canonical
contact-preserving diametral saturation. Three distinct convex-hull vertices cannot
be collinear with one between the other two, so a one-dimensional positive diameter
endpoint set contains only two vertices. Hence the normalized positive diameter
support is the single edge `bk` with weight one.

By the canonical positive-support connectivity theorem, the positive contact graph
`G_s` is connected and contains `b,k`. All positive diameter reaction is applied at
those two vertices and is parallel to `p_b-p_k`.

Project the vertex-equilibrium equations perpendicular to the line `bk`. The right
side is zero at every vertex. The left side is the positive weighted contact
Laplacian applied to the perpendicular coordinate. Since `G_s` is connected and all
contact weights are positive, the only harmonic scalar functions are constants.
Therefore every positive-contact vertex lies on the line `bk`.

A connected unit-contact graph on distinct unit-separated collinear points is the
path through consecutive unit-spaced points. Write its vertices in order as

\[
x_0=b,x_1,\ldots,x_D=k.
\]

The endpoint distance is `D`, so the number of unit edges is exactly `D`; in
particular this selected one-dimensional phase can occur only when `D` is an integer.
Interior equilibrium makes every contact stress equal. The endpoint equilibrium
identity `L_C P=L_H P` then gives that common contact weight as `D`.

For any scalar vector `z`,

\[
\begin{aligned}
z^{\mathsf T}\Omega_s z
&=D\sum_{r=0}^{D-1}(z_{r+1}-z_r)^2-(z_D-z_0)^2\\
&=D\sum_{r=0}^{D-1}\delta_r^2-
   \left(\sum_{r=0}^{D-1}\delta_r\right)^2\ge0
\end{aligned}
\tag{C54.2}
\]

by Cauchy-Schwarz. Equality holds exactly when all increments `delta_r` are equal,
i.e. exactly when `z` is affine in the chain coordinate. This proves the lemma.
`\square`

Combining C54.1 with C53 gives the universal statement

\[
\boxed{
\Omega_s\succeq0
\quad\text{for every normalized KKT stress }s.
}
\tag{C54.3}
\]

No support-selection hypothesis is left in (C54.3).

## 2. C54.2 — every critical velocity has zero energy for an extreme stress

Let `S` denote the normalized KKT polytope. It is a nonempty compact polytope. Let
its finitely many extreme points be

\[
s^1,\ldots,s^N.
\]

For a velocity field `v`, write

\[
q_s(v)=\operatorname{tr}(V^{\mathsf T}\Omega_sV).
\tag{C54.4}
\]

For fixed `v`, this is linear in `s`.

### Lemma C54.2

For every `v in K_D(A)`,

\[
\min_{s\in S}q_s(v)=0,
\tag{C54.5}
\]

and the minimum is attained by at least one extreme stress `s^a`. For that extreme
stress,

\[
\Omega_{s^a}V_x=0,
\qquad
\Omega_{s^a}V_y=0.
\tag{C54.6}
\]

#### Proof

C13.3 supplies some normalized KKT stress `s` with

\[
q_s(v)\le0.
\]

By (C54.3), every `Omega_s` is PSD, so `q_s(v)>=0` for every normalized stress.
Hence the minimum is exactly zero. A linear functional on a compact polytope attains
its minimum at an extreme point, proving the first claim.

For a PSD matrix, a zero scalar quadratic form implies membership in its kernel.
Since

\[
q_{s^a}(v)=V_x^{\mathsf T}\Omega_{s^a}V_x
          +V_y^{\mathsf T}\Omega_{s^a}V_y=0
\]

and both summands are nonnegative, both vanish and give (C54.6). `\square`

## 3. C54.3 — one extreme stress annihilates the whole critical-cone span

For each extreme stress define the linear velocity subspace

\[
Z_a=
\{v:\Omega_{s^a}V_x=0,\ \Omega_{s^a}V_y=0\}.
\tag{C54.7}
\]

Lemma C54.2 gives

\[
\mathcal K_D(A)\subseteq\bigcup_{a=1}^N Z_a.
\tag{C54.8}
\]

### Theorem C54 (extreme null-face selection)

Let

\[
L=\operatorname{span}\mathcal K_D(A).
\]

There exists an extreme normalized KKT stress `s^dagger` such that

\[
\boxed{L\subseteq Z_{\dagger}.}
\tag{C54.9}
\]

Equivalently,

\[
\boxed{
\Omega_{s^\dagger}V_x=\Omega_{s^\dagger}V_y=0
\quad\text{for every fixed-diameter critical velocity }v.
}
\tag{C54.10}
\]

Moreover `L` is exactly the infinitesimal-flex space of the maximal strong mixed
framework:

\[
\boxed{
L=\{v:\phi_e(v)=0\text{ for every }e\in E_*\}.
}
\tag{C54.11}
\]

Thus one extreme PSD KKT stress annihilates every infinitesimal flex of
`C_* union H_*`.

#### Proof

A nonempty polyhedral cone has nonempty relative interior in its linear span. Hence
`ri K_D(A)` is a relatively open subset of `L`. Equation (C54.8) covers this open
set by finitely many linear subspaces `Z_a cap L`. A finite union of proper linear
subspaces cannot contain a relatively open subset of a finite-dimensional real
vector space. Therefore some `Z_a cap L` equals all of `L`, proving (C54.9).

For (C54.11), C6 says every strong active row vanishes on all of `K_D(A)`, so

\[
L\subseteq L_*:=\bigcap_{e\in E_*}\ker\phi_e.
\]

C6 also supplies a relative-interior critical velocity `v^circ` on which every weak
active row is strict. Therefore sufficiently small perturbations of `v^circ` inside
`L_*` remain feasible on every weak row. Thus `K_D(A)` has nonempty relative
interior in `L_*`, and its span is `L_*`. Hence `L=L_*`. `\square`

## 4. Face formulation

The theorem can be expressed without choosing a particular extreme point. Choose a
basis `v^1,...,v^r` of `L` and define the nonnegative linear functional on the KKT
polytope

\[
F(s)=\sum_{j=1}^r q_s(v^j)\ge0.
\tag{C54.12}
\]

Then

\[
\mathcal F_0=\{s\in S:F(s)=0\}
\tag{C54.13}
\]

is a nonempty exposed face of the normalized KKT polytope. Every stress in this face
has a PSD stress matrix annihilating all of `L`, and a relative-interior point of
`F_0` maximizes support within this **second-order null face**.

This is the exact support object relevant after C53. The direction-dependent stress
in C13.3 no longer needs to be followed separately for different velocities.

## 5. Exact C-I effect

If a weak unit contact survives in a contact-minimal minimizer, C13.4 says the strong
framework has a non-Euclidean infinitesimal flex. C54 now says that all of those
flexes lie in the kernel of one extreme PSD equilibrium stress.

Therefore the remaining C-I statement is:

> **C55 null-face kernel rigidity.** Show that the second-order null face contains a
> stress whose kernel on the strong-framework flex space forces one common angular
> rate on `H_*`; equivalently, show that a nontrivial diameter-shear flex cannot be
> annihilated by every stress in the exposed null face.

A proof would combine with C7 and contradict contact minimality, forcing `C=C_*`.

The point of C54 is that C55 is now a single-face support problem. It is no longer a
velocity-by-velocity KKT selection problem.

## 6. What C54 does not prove

- The selected extreme stress `s^dagger` need not have maximal KKT support.
- Its scalar stress kernel may be larger than `span{1,x,y}`.
- PSD alone does not exclude affine shear.
- The exposed null face need not equal the entire KKT polytope.
- No uniform spectral gap is obtained.
- C-II is untouched until weak contacts are eliminated.

## 7. Verification and regressions

- The one-dimensional proof is exact and uses only connected positive equilibrium,
  hull extremality, and Cauchy-Schwarz.
- The finite-union step uses finiteness of the extreme points of the normalized KKT
  polytope; there is no compactness-to-countability shortcut.
- The finite-union statement is applied in the linear span of the polyhedral critical
  cone, not in the ambient velocity space.
- Affine-shear regressions remain compatible: an exposed null face can have a kernel
  containing affine velocity fields.

## 8. Compact handoff

**LEVEL I STATUS:** still open.

**C54.1:** the only one-dimensional selected KKT support is a straight `D`-edge unit
chain with contact weight `D`; its stress matrix is PSD by Cauchy-Schwarz.
Together with C53, every normalized KKT stress is PSD.

**C54.2:** C13.3 plus universal PSD forces zero second-order energy, and a minimizing
extreme KKT stress realizes that zero for each critical velocity.

**C54:** finitely many extreme stress kernels cover the critical cone. One kernel
must contain the cone's entire span. That span is exactly the infinitesimal-flex
space of the maximal strong framework. Equivalently, there is a nonempty exposed
second-order null face of the KKT polytope whose every member annihilates all strong
framework flexes.

**Next:** prove null-face kernel rigidity/common angular rate, then invoke C7 to
eliminate weak contacts.
