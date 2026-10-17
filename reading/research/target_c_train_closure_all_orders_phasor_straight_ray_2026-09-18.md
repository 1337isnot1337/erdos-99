> Generated reading edition · [exact source](../../research/target_c_train_closure_all_orders_phasor_straight_ray_2026-09-18.md) · source SHA-256 `956c59f13760a596190d2020d6d3e30ad4c52655e580e8460dba2759e9ab3caf`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "8662a8c5cb5f2e1745d76ff7f3fd211fbc5f1850", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_train_closure_all_orders_phasor_straight_ray_2026-09-18.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "8eeb52dcd5ff9be810b2e4143fabdb9c185a7663c13d38aa7ed097c83aaf1aa5"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — exact dual phasors and rigidity of straight train-angle rays

**Date:** 2026-09-18  
**Status:** proved candidate; theorem-state authority unchanged  
**Scope:** canonical full-core stopped-train angle closure system; proof-only live terminal consequence  
**Depends on:** exact nonlinear train-angle closure map; coherent train orientations; the dual coefficient definition from `target_c_free_terminal_train_closure_hessian_2026-09-18.md`; bounded contact-pentagon no-parallel-side lemma  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The preceding Hessian reduction identifies the first nonlinear obstruction by
contracting the face-closure Hessian against a dual closure mode.  In fact the same
dual coefficients satisfy an exact finite identity to all orders.  Separately, an
exact closure path that is a straight line in train-angle coordinates can be classified
face by face by a finite Vandermonde argument.

These two observations remove one tempting escape from the current singular
integration problem.  Equal-magnitude kernel vectors do integrate exactly, but on a
bounded contact pentagon every exact straight train-angle ray forces all five incident
train speeds to be equal.  Thus, away from the sparse superpentagonal defect set, new
non-Euclidean exact motion cannot be obtained by assigning fixed unequal angular
velocities and following the resulting straight ray.  Any additional macroscopic
integration mechanism has to be genuinely curved in train-angle space, except for
outer--outer trains and componentwise common rotations.

No theorem-state file is changed.

---

## 1. Exact notation

Let

```math
\Psi:(\mathbb R/2\pi\mathbb Z)^T\to\mathbb R^{2f}
```

be the bounded-exceptional-face closure map.  Fix a coherent unit direction `u_tau`
for every complete stopped train `tau`, and occurrence signs
`epsilon_{F tau} in {+1,-1}` so that

```math
\Psi_F(\theta)
=\sum_{\tau\sim F}\epsilon_{F\tau}R_{\theta_\tau}u_\tau.
\tag{1.1}
```

At the canonical source, `Psi(0)=0`.  Its derivative is the audited face-closure
matrix

```math
C=D\Psi(0).
```

Fix a dual closure mode

```math
y=(y_F)_F\in\ker C^T.
```

For every train put

```math
v_\tau(y)
:=\sum_{F:\tau\sim F}\epsilon_{F\tau}y_F.
```

The transpose closure equation says `v_tau(y)` is parallel to `u_tau`, so there is a
unique real scalar `lambda_tau(y)` with

```math
\boxed{v_\tau(y)=\lambda_\tau(y)u_\tau.}
\tag{1.2}
```

For an outer--outer train, `lambda_tau(y)=0`.

---

## 2. Exact all-orders dual phasor identity

### Theorem 2.1

If `theta` is any exact train-angle closure,

```math
\Psi(\theta)=0,
```

then every `y in ker C^T` satisfies

```math
\boxed{
\sum_\tau\lambda_\tau(y)\cos\theta_\tau=0,
\qquad
\sum_\tau\lambda_\tau(y)\sin\theta_\tau=0.
}
\tag{2.1}
```

Equivalently, after identifying the angle circle with complex phases,

```math
\boxed{
\sum_\tau\lambda_\tau(y)e^{i\theta_\tau}=0.
}
\tag{2.2}
```

### Proof

Contract the exact closure equations with `y`:

```math
\begin{aligned}
0
&=\sum_F y_F\cdot\Psi_F(\theta)\\
&=\sum_\tau v_\tau(y)\cdot R_{\theta_\tau}u_\tau\\
&=\sum_\tau\lambda_\tau(y)\cos\theta_\tau.
\end{aligned}
```

Now contract the same exact closure equations with the blockwise-rotated test vector
`Jy=(Jy_F)_F`.  It need not belong to `ker C^T`; no such assumption is used.  Since
`Jv_tau=lambda_tau Ju_tau`,

```math
\begin{aligned}
0
&=\sum_F Jy_F\cdot\Psi_F(\theta)\\
&=\sum_\tau Jv_\tau(y)\cdot R_{\theta_\tau}u_\tau\\
&=\sum_\tau\lambda_\tau(y)\sin\theta_\tau.
\end{aligned}
```

This proves (2.1)--(2.2).  The statement is finite and exact.  It is not a Taylor
approximation.

At `theta=0`, (2.2) gives the already proved rotation identity

```math
\sum_\tau\lambda_\tau(y)=0.
\tag{2.3}
```

Differentiating (2.2) along a smooth exact path recovers the first-order identity and
the diagonal Hessian obstruction from the preceding note.  Thus the Hessian theorem is
the quadratic truncation of one exact signed-phasor closure law.

### Corollary 2.2 — exact signed angular-energy identity

For every exact closure,

```math
\boxed{
\sum_{\tau<\sigma}
\lambda_\tau\lambda_\sigma
\bigl(1-\cos(\theta_\tau-\theta_\sigma)\bigr)=0.
}
\tag{2.4}
```

Indeed, square the modulus in (2.2) and subtract the square of (2.3).

### Corollary 2.3 — singleton-sign dual modes lock their support

Suppose a nonzero dual coefficient vector `lambda(y)` has exactly one positive
coordinate, or exactly one negative coordinate.  Then every sufficiently small exact
closure has

```math
\theta_\tau=\theta_\sigma
```

for all trains `tau,sigma` in the support of `lambda(y)`.

For example, if `lambda_p=M>0` is the unique positive coefficient and
`lambda_j=-m_j<0` otherwise on the support, then (2.3) gives

```math
M=\sum_jm_j.
```

Equation (2.2) becomes

```math
M e^{i\theta_p}=\sum_jm_j e^{i\theta_j}.
```

After division by `M`, a convex combination of unit complex numbers has modulus one.
Equality in the triangle inequality forces all phases in the combination to coincide
with `e^{i theta_p}`.  In a sufficiently small angular neighborhood the angles
therefore coincide as real numbers, not merely modulo `2pi`.

So a genuinely singular dual obstruction that permits non-common motion on its support
must have at least two positive and at least two negative nonzero coefficients.

---

## 3. Exact classification of straight train-angle rays

Identify `R^2` with `C`.  For a real train-speed vector `x in R^T`, consider the
straight angle ray

```math
\theta(t)=tx.
```

For one bounded exceptional face `F`, and for each real number `a` appearing among the
incident speeds, define the oriented side-vector sum

```math
S_{F,a}(x)
:=\sum_{\substack{\tau\sim F\\x_\tau=a}}
\epsilon_{F\tau}u_\tau.
\tag{3.1}
```

### Theorem 3.1 — slope-group criterion

The face `F` remains exactly closed for every `t` in an interval around zero if and
only if

```math
\boxed{S_{F,a}(x)=0}
\tag{3.2}
```

for every distinct incident speed `a`.

Consequently, the full straight ray `theta(t)=tx` is an exact zero of `Psi` on an
interval if and only if (3.2) holds for every bounded exceptional face and every speed
group on that face.

### Proof

In complex notation,

```math
\Psi_F(tx)=\sum_{\tau\sim F}
\epsilon_{F\tau}u_\tau e^{itx_\tau}
=\sum_{a\in A_F}S_{F,a}(x)e^{ita},
\tag{3.3}
```

where `A_F` is the finite set of distinct incident speeds.

If every group sum vanishes, (3.3) is identically zero.  Conversely suppose (3.3)
vanishes on an interval.  If `A_F={a_1,...,a_m}`, differentiate at `t=0` for orders
`0,...,m-1`.  The resulting system is

```math
\sum_{j=1}^m (ia_j)^k S_{F,a_j}(x)=0,
\qquad k=0,\ldots,m-1.
```

The coefficient matrix is a Vandermonde matrix on the distinct real numbers `a_j`, so
it is invertible.  Hence every `S_{F,a_j}(x)=0`.  This proves the criterion.

This is stronger than checking every Taylor obstruction separately: it classifies the
entire affine-in-angle path at once.

---

## 4. Equal-magnitude kernel vectors really do integrate exactly

The Hessian note observed that a kernel vector with equal coordinate magnitudes passes
every quadratic dual test.  There is no higher-order obstruction for such a vector.

### Corollary 4.1

Suppose

```math
s\in\ker C,
\qquad
s_\tau\in\{+1,-1\}
```

for every train.  Then

```math
\boxed{\Psi(ts)=0\quad\text{for every real }t.}
\tag{4.1}
```

The same statement holds when every coordinate has one common absolute value `c`,
after rescaling `t`.

### Proof

For each face,

```math
R_{ts_\tau}u_\tau
=\cos t\,u_\tau+s_\tau\sin t\,Ju_\tau.
```

Therefore

```math
\Psi_F(ts)
=\cos t\,\Psi_F(0)
+\sin t\,(Cs)_F
=0.
```

So the equal-magnitude observation is an exact finite integration theorem, not merely a
second-order compatibility test.

The next section shows why this does not supply a new macroscopic route on the
near-pure pentagonal core.

---

## 5. A bounded contact pentagon has no proper zero-sum side subset

Let `F` be a strictly convex bounded pentagonal face of the complete unit-contact
graph.  Write its five oriented unit side vectors in boundary order as

```math
w_1,\ldots,w_5,
\qquad
\sum_{j=1}^5w_j=0.
```

The proved bounded-pentagon lemma says no two side vectors are projectively parallel.

### Lemma 5.1

No proper nonempty subset of `{w_1,...,w_5}` has vector sum zero.

### Proof

A one-element subset cannot sum to zero.  A two-element zero sum would consist of
opposite unit vectors and hence a projectively parallel side pair, which is excluded.
If a three-element subset summed to zero, its complementary two-element subset would
also sum to zero because all five vectors sum to zero; this is again impossible.  A
four-element zero sum would force the remaining unit vector to be zero.  These are all
proper subset sizes.

### Corollary 5.2 — pentagon straight-ray rigidity

If `theta(t)=tx` preserves the closure of a bounded contact pentagon for an interval of
`t`, then all five incident train speeds are equal.

Indeed, Theorem 3.1 says every nonempty speed group must have zero oriented side-vector
sum.  Lemma 5.1 says the only possible nonempty zero-sum group is the set of all five
sides.

In particular, if `s in ker C` has all coordinates in `{+1,-1}`, then on every bounded
contact pentagon the five incident signs are equal.  Thus the exact equal-magnitude ray
from Corollary 4.1 reduces on the pentagonal core to common rotation on each connected
pentagon-train component.  It does not create an additional alternating-sign flex
inside such a component.

---

## 6. Only superpentagons can carry unequal straight-ray speeds

Let

```math
X:=Q-f=\sum_F(\deg F-5)\ge0
\tag{6.1}
```

be the exact bounded-exceptional-face degree excess, and let `S` be the set of bounded
exceptional faces of degree at least six.  Then

```math
|S|\le X
```

and

```math
\sum_{F\in S}\deg F
=5|S|+\sum_{F\in S}(\deg F-5)
\le6X.
\tag{6.2}
```

Construct a graph `Gamma_5` whose vertices are complete trains incident to at least one
bounded pentagonal exceptional face, joining all train variables that occur on the
same pentagon.  Corollary 5.2 implies:

```math
\boxed{
 x_\tau\text{ is constant on every connected component of }\Gamma_5
}
\tag{6.3}
```

for every exact straight-ray speed vector `x`.

A non-outer--outer train not represented in `Gamma_5` has no pentagonal bounded
endpoint, hence has at least one endpoint in `S`.  Therefore the number of such train
variables is at most the incidence count in (6.2), hence at most `6X`.

So every exact straight ray has the following finite normal form:

- one common speed on each pentagon-train component;
- arbitrary outer--outer train speeds, which do not enter bounded-face closure; and
- all remaining unequal-speed freedom confined to at most `6(Q-f)` non-outer--outer
  train variables incident to superpentagonal faces.

This is a support statement, not a linear-dimension claim about the full nonlinear zero
set.  Superpentagon equations can further couple these speeds, and a genuinely curved
exact path need not be a straight ray.

In the proof-only live terminal window from the detour-pinching note,

```math
{Q-f\over D}<0.000141+o(1).
```

Hence the entire non-outer--outer defect support on which an exact straight ray can
avoid pentagon-component common speed has size

```math
\boxed{
< (0.000846+o(1))D.
}
\tag{6.4}
```

The constant is simply `6*0.000141`; no numerical optimization is involved.

---

## 7. Frontier effect

The latest Hessian theorem isolated the singular nonlinear integration gap.  The
results above sharpen that target in two ways.

1. Every dual closure mode has the exact all-orders phasor law (2.2), so its nonlinear
   obstruction is not confined to the quadratic square-map condition.
2. Straight train-angle rays are completely classified by zero-sum slope groups.
   On the near-pure pentagonal terminal core, unequal affine angular speeds can occur
   only through the `O(Q-f)` superpentagonal defect support, aside from outer--outer
   trains and componentwise common rotations.

Thus a future attempt to enlarge the current exact contact-flex manifold by taking a
large subspace of first-order kernel vectors and integrating them as constant-speed
train rotations cannot work on the degree-pure pentagonal bulk.  The missing
macroscopic integration, if it exists, must use curved train-angle paths whose higher
jets compensate the singular closure equations, or it must exploit the sparse
superpentagonal defect set.

A second exact target is supplied by Corollary 2.3: classify the sign patterns of
`lambda(y)` on the minimal five-face one-anchor dual blocks.  A singleton-sign mode is
already nonlinearly locked to common rotation by the exact phasor identity.

This still does not give a common diameter-decreasing finite motion and does not close
C-II.

**Disposition:** upgraded the diagonal Hessian obstruction to an exact all-orders dual
phasor identity, classified every exact straight train-angle ray, proved exact
integration of equal-magnitude kernel rays, and showed that bounded contact pentagons
force all incident straight-ray speeds to coincide.  In the current proof-only live
window, unequal non-outer--outer straight-ray speeds are confined to fewer than
`(0.000846+o(1))D` train variables.  C-II remains open.
