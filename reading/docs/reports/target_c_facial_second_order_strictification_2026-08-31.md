> Generated reading edition · [exact source](../../../docs/reports/target_c_facial_second_order_strictification_2026-08-31.md) · source SHA-256 `8c3405016086d8b929d182114954c036f31ee6ae719d316dd7c1c9ceea58337b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-0E4050546EF1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: facial second-order strictification

**Date:** 2026-08-31  
**Repository base:** `ee50a9db` (main after C61 / PR #63)  
**Run type:** exact Farkas/facial reduction  
**Target:** Target C Gate C-I, null-face coverage defect  
**Depends on:** C6 strong rows, C13.3 second-order normal stress, C54 universal PSD, C57 extreme-body rigidity, C61 bouquet integration

## LEVEL I STATUS

**STILL OPEN.**

C61 leaves one obstruction: a strong active vertex may lie outside the support union of
the common null face `F_0`. For a **fixed** relative-interior weak-release velocity
`v`, the correct face is larger:

$$
\mathcal F_v
=\{s\in\mathcal S:q_s(v)=0\},
\qquad
q_s(v)=\operatorname{tr}(V^{\mathsf T}\Omega_sV).
$$

Universal PSD makes `q_s(v)>=0` for every normalized KKT stress, while C13.3 supplies
one stress with `q_s(v)<=0`; hence `F_v` is a nonempty exposed face of the normalized
KKT polytope `S`.

This report proves that the support union of `F_v` is exactly the set on which a
second-order correction is **forced to remain tangent**. Every strong row omitted by
`F_v` can be made **strictly feasible at second order simultaneously**.

Thus the C61 coverage defect is not an arbitrary second-order lock. Any remaining
failure is at least third order and is confined to the zero-energy body bouquet.

## 1. Signed second-order rows

For an active pair `e=ij`, write

$$
r_e=p_i-p_j,
\qquad
u_e=v_i-v_j.
$$

For every strong row, C6 gives

$$
r_e\cdot\nu_e=0.
\tag{C62.1}
$$

Let `a=(a_i)` be an acceleration field. Define the signed rigidity row

$$
(\mathcal Ra)_e=
\begin{cases}
 r_e\cdot(a_i-a_j),&e\in C_*,\\
-r_e\cdot(a_i-a_j),&e\in H_*,
\end{cases}
\tag{C62.2}
$$

and the signed quadratic term

$$
b_e(v)=
\begin{cases}
 |\nu_e|^2,&e\in C_*,\\
-|\nu_e|^2,&e\in H_*.
\end{cases}
\tag{C62.3}
$$

For the quadratic jet

$$
p_i(t)=p_i+t v_i+\frac12t^2a_i,
\tag{C62.4}
$$

the signed second-order coefficient of every strong feasibility inequality is

$$
(\mathcal Ra)_e+b_e(v).
\tag{C62.5}
$$

A normalized KKT stress is a nonnegative vector `s` on the strong active rows satisfying

$$
s^{\mathsf T}\mathcal R=0,
\qquad
\sum_{h\in H_*}\beta_h=1.
\tag{C62.6}
$$

Its second-order energy is exactly

$$
\boxed{q_s(v)=s^{\mathsf T}b(v).}
\tag{C62.7}
$$

C54 gives `q_s(v)>=0` for every `s in S`.

## 2. The fixed-direction zero face

Define

$$
\mathcal F_v=\{s\in\mathcal S:s^{\mathsf T}b(v)=0\}.
\tag{C62.8}
$$

C13.3 and universal PSD imply `F_v` is nonempty. Let

$$
E_v^0=\bigcup_{s\in\mathcal F_v}\operatorname{supp}s
\tag{C62.9}
$$

and choose a relative-interior point `s^0 in F_v`. Then

$$
s^0_e>0
\quad\Longleftrightarrow\quad
e\in E_v^0.
\tag{C62.10}
$$

Write `E_1=E_*\setminus E_v^0`.

The following elementary lemma is the key facial fact.

### Lemma C62.1 (all signed equilibrium tangents on the zero support have zero energy)

Let `y` be any real signed coefficient vector supported on `E_v^0` such that

$$
y^{\mathsf T}\mathcal R=0.
\tag{C62.11}
$$

Then

$$
\boxed{y^{\mathsf T}b(v)=0.}
\tag{C62.12}
$$

#### Proof

Because `s^0` is strictly positive on all of `E_v^0`, for sufficiently large `M` both

$$
Ms^0+y,
\qquad
Ms^0-y
$$

are coordinatewise nonnegative equilibrium stresses. Their total diameter coefficient
is positive for large `M`; normalize each one to obtain elements of `S`.

Universal PSD says their second-order energies are nonnegative. Since
`(s^0)^Tb(v)=0`, before the harmless positive normalization factors those two energies
are

$$
y^Tb(v)
\quad\text{and}\quad
-y^Tb(v).
$$

Both are nonnegative, hence both vanish. `\square`

## 3. Exact tangency on the whole zero-face support

### Theorem C62.2 (zero-support second-order equations are solvable)

There exists an acceleration field `a` satisfying

$$
\boxed{
(\mathcal Ra)_e+b_e(v)=0
\qquad(e\in E_v^0).
}
\tag{C62.13}
$$

#### Proof

The linear system

$$
\mathcal R_0a=-b_0
\tag{C62.14}
$$

is solvable exactly when every left-nullvector `y` of `R_0` annihilates `b_0`.
Every such `y` is a signed equilibrium vector supported on `E_v^0`, so Lemma C62.1
gives precisely that condition. `\square`

This is stronger than the direction-dependent existence statement C13.3: no selected
stress has to be chosen. The complete support union of the zero-energy face admits a
single common second-order tangent acceleration.

## 4. Every omitted strong row can be strictified simultaneously

### Theorem C62 (facial second-order strictification)

There exists an acceleration field `a` such that

$$
\boxed{
(\mathcal Ra)_e+b_e(v)=0
\quad(e\in E_v^0),
}
\tag{C62.15}
$$

and

$$
\boxed{
(\mathcal Ra)_e+b_e(v)>0
\quad(e\in E_1).
}
\tag{C62.16}
$$

#### Proof

By Theorem C62.2, the affine equality system (C62.15) is nonempty. Suppose no point of
that affine space makes every row of `E_1` strict.

The strict affine Farkas/Stiemke alternative then supplies coefficients

$$
y\in\mathbb R^{E_v^0},
\qquad
\lambda\in\mathbb R_{\ge0}^{E_1},
\qquad
\lambda\ne0,
\tag{C62.17}
$$

such that

$$
y^{\mathsf T}\mathcal R_0
+\lambda^{\mathsf T}\mathcal R_1=0
\tag{C62.18}
$$

and

$$
y^{\mathsf T}b_0
+\lambda^{\mathsf T}b_1
\le0.
\tag{C62.19}
$$

Let `r=(y,lambda)`. Add a sufficiently large multiple of the relative-interior
zero-face stress:

$$
x=r+Ms^0.
\tag{C62.20}
$$

For large `M`, every coordinate of `x` is nonnegative; on `E_1` it equals the
nonnegative vector `lambda`, which is nonzero. Equation (C62.18) makes `x` an
equilibrium stress. Its diameter total is positive for large `M`, so after
normalization `x` is a member of `S`.

Its second-order energy is

$$
x^Tb(v)=r^Tb(v)+M(s^0)^Tb(v)=r^Tb(v)\le0.
\tag{C62.21}
$$

Universal PSD forces the normalized energy to be nonnegative, so equality holds in
(C62.21). Therefore the normalized `x` belongs to `F_v`.

But `x` has a positive coordinate in `E_1` because `lambda!=0`, contradicting the
definition of `E_v^0` as the union support of `F_v`. Thus the strict solution exists.
`\square`

## 5. Consequence for actual quadratic jets

Take the acceleration from C62. For a strong active row, the squared-distance
constraint along (C62.4) has zero first derivative. Therefore:

- every row in `E_1` becomes strict with a uniform signed `+Theta(t^2)` margin;
- every row in `E_v^0` is tangent through second order;
- every weak active row is already strict at order `t` because `v` is relative
  interior;
- every inactive pair retains its fixed initial slack.

Hence

$$
\boxed{
\text{all possible third- or higher-order locking is confined to }E_v^0.
}
\tag{C62.22}
$$

There is no second-order obstruction on a strong row omitted by the zero-energy face.

## 6. The fixed-direction zero face has the same body-bouquet structure

C57-C61 were stated using the common null face `F_0`, but their fixed-velocity proofs
need only the following facts:

1. the relevant set is a convex face of `S`;
2. every stress in the face is PSD and has `v` in its stress kernel;
3. extreme points of the face are extreme points of `S`;
4. convex averages remain in the face.

All four hold for `F_v`. Therefore the same arguments apply verbatim:

### Corollary C62.3 (fixed-direction bouquet)

Every extreme point of `F_v` is a rigid body for `v`. After merging equal rigid
motions, all distinct motion classes share one common source hinge, and their union
admits the simultaneous finite bouquet rotation of C61.

Moreover every row of `E_v^0` lies in the support of at least one extreme point of
`F_v`; hence both endpoints of every zero-face row lie in that rigid-body union.

Thus C62 removes the original **support coverage** problem at second order. The rows
outside the body union are precisely among the rows receiving strict second-order
slack in (C62.16).

## 7. What still prevents an immediate Gate C-I closure

The acceleration supplied by C62 need not equal the second derivative of the exact
C61 bouquet rotation on the covered vertices.

Both accelerations solve the zero-support equations (C62.15), so their difference is
an infinitesimal flex of the zero-support mixed framework. But an arbitrary such flex
is not known to integrate while keeping all zero-face rows feasible. If one simply
adds the C62 quadratic correction to the exact bouquet path, the zero-face constraints
remain correct through order two but may acquire signed cubic terms.

Therefore C62 does **not** silently identify a second-order jet with an actual feasible
curve.

The remaining C-I issue is now sharper than “coverage”:

> **C63 compatible strictification.** Choose the strictifying solution of C62 inside
> the second-derivative family of exact common-hinge bouquet motions, or prove that
> the difference flex can be absorbed by a higher-order correction without losing the
> `Theta(t^2)` margins on `E_1`.

Any such theorem closes Gate C-I: the omitted rows have quadratic margin, the zero-face
rows follow an exact bouquet motion, weak rows have linear margin, and inactive rows
have fixed margin.

## 8. Independent second-order corollary

Even without the strict facial refinement, universal PSD gives a useful global fact.
The ordinary non-strict Farkas alternative applied to

$$
\mathcal Ra+b(v)\ge0
$$

has dual obstructions exactly the nonnegative equilibrium stresses. Every nonzero such
stress has positive diameter total (a pure positive contact self-stress is impossible
by taking the coordinate trace), so it normalizes into `S`; universal PSD makes its
pairing with `b(v)` nonnegative. Hence:

### Corollary C62.4

Every fixed-diameter critical velocity admits at least one globally feasible
second-order acceleration.

Thus after C54 there is no second-order infeasibility anywhere in the critical cone.
All remaining Target C difficulty is genuinely higher order.

## 9. Binding cautions

- `F_v` depends on the chosen weak-release velocity. C62 does not produce one face for
  the whole flex space `L`.
- Equality through second order on `E_v^0` is not exact finite preservation.
- The difference between a C62 acceleration and a bouquet acceleration can be a
  non-rigid infinitesimal flex of the zero-support framework.
- Strict `Theta(t^2)` margins on `E_1` are robust under `O(t^3)` corrections, which is
  why the remaining problem is localized to constructing those higher-order
  corrections on `E_v^0`.
- C-II is still separate until Gate C-I is fully closed.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

For fixed `v in ri K_D(A)`, let `F_v={s:q_s(v)=0}` and let `E_v^0` be its support
union.

**C62:** there is one acceleration with zero signed second-order slack on every row of
`E_v^0` and strictly positive signed second-order slack on every strong row outside
`E_v^0`.

The proof is pure facial Farkas: any failed strictification yields a signed equilibrium
certificate; adding a large relative-interior zero-face stress turns it into a
nonnegative KKT stress. Universal PSD rules out negative energy, while zero energy
would put an omitted coordinate back into `F_v`.

**Body consequence:** C57-C61 apply to the fixed-direction face `F_v`; its support
union is a common-hinge rigid-body bouquet for `v`.

**Only remaining C-I issue:** make the C62 strictifying acceleration compatible with
an exact bouquet motion, or absorb its zero-support difference flex at order three and
higher.
