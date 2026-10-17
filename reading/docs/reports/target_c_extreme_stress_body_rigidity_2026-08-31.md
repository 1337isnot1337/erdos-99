> Generated reading edition · [exact source](../../../docs/reports/target_c_extreme_stress_body_rigidity_2026-08-31.md) · source SHA-256 `7c894c4c927940a6a44fdfc0c442ba046daee763314301b1d5c8e466cbf7f785`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5DF06DE09506","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: extreme-stress body rigidity

**Date:** 2026-08-31  
**Repository base:** `e38a1e57` (main after minimum-transfer C56 / PR #58)  
**Run type:** exact equality-kernel / KKT-face reduction  
**Target:** Target C Gate C-I  
**Depends on:** C6 critical-cone duality, positive-support connectivity, C54 null-face selection, C56 minimum-transfer kernel collapse

## LEVEL I STATUS

**STILL OPEN.**

C56 proves a sharp spectral dichotomy for each selected two-dimensional stress. This report attacks the orthogonal problem left by that result: how the different stresses in C54's exposed null face can fit together.

For an **extreme** normalized KKT stress, any fixed-diameter critical velocity in its PSD stress kernel has one common angular rate on every positive contact and positive diameter edge. Thus the entire connected positive contact component of an extreme null stress is one infinitesimal rigid body.

Applied to the C54 null face, every extreme point of that face is a rigid body for every strong-framework flex. Any two such bodies intersect in at least one source vertex, because their midpoint is again a normalized KKT stress and every normalized positive contact support is connected. If they share two source vertices, their rigid motions coincide.

Hence any surviving C-I shear is not an internal mode of a null-face extreme stress. It is a planar body-pin mechanism made from full-diameter extreme-stress bodies joined at one-vertex intersections.

## 1. Extreme normalized stresses have no normalized signed tangent

Let `S` be the normalized KKT polytope. Write a normalized stress as

```math
s=(\alpha,\beta)\in S,
\qquad
\alpha_e,\beta_h\ge0,
\qquad
\sum_h\beta_h=1,
\tag{C57.1}
```

with the usual vertex-equilibrium equations. Put

```math
C_s=\{e:\alpha_e>0\},
\qquad
H_s=\{h:\beta_h>0\}.
```

### Lemma C57.1

If `s` is an extreme point of `S`, there is no nonzero signed coefficient vector

```math
r=(a,b)
```

supported in `C_s union H_s` such that

1. `r` satisfies the homogeneous vertex-equilibrium equations; and
2. `sum_H b_h=0`.

#### Proof

Every coordinate of `s` on its support is strictly positive. Hence for any fixed signed `r` supported there, both

```math
s+\varepsilon r,
\qquad
s-\varepsilon r
```

remain coordinatewise nonnegative for all sufficiently small positive `epsilon`. Homogeneous equilibrium and zero diameter-weight sum make both perturbed vectors normalized KKT stresses. If `r!=0`, then `s` is the midpoint of two distinct points of `S`, contradicting extremality. $`\square`$

Equivalently: every signed equilibrium stress supported in `supp(s)` is proportional to `s` after fixing the total diameter coefficient.

## 2. A kernel velocity differentiates the stress weights

Fix an extreme normalized KKT stress `s=(alpha,beta)` and a fixed-diameter critical velocity `v` such that

```math
\Omega_s V_x=0,
\qquad
\Omega_s V_y=0,
\qquad
\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta).
\tag{C57.2}
```

Every positive support edge is strong, so C6 makes its radial first variation zero. Therefore there are real angular rates

```math
v_i-v_j=\kappa_eJ(p_i-p_j)
\qquad(e=ij\in C_s),
\tag{C57.3}
```

and

```math
v_i-v_j=\omega_hJ(p_i-p_j)
\qquad(h=ij\in H_s).
\tag{C57.4}
```

The vector kernel equation is

```math
\sum_{e=ij\in C_s}\alpha_e(v_i-v_j)
-
\sum_{h=ij\in H_s}\beta_h(v_i-v_j)=0
\tag{C57.5}
```

at every vertex, with the usual incidence signs. Apply `-J` and use (C57.3)-(C57.4):

```math
\sum_{e=ij\in C_s}\alpha_e\kappa_e(p_i-p_j)
-
\sum_{h=ij\in H_s}\beta_h\omega_h(p_i-p_j)=0.
\tag{C57.6}
```

Thus

```math
\widetilde s
=
\bigl((\alpha_e\kappa_e)_{e\in C_s},
      (\beta_h\omega_h)_{h\in H_s}\bigr)
\tag{C57.7}
```

is a signed equilibrium stress on exactly the same support.

Set

```math
c=\sum_{h\in H_s}\beta_h\omega_h.
\tag{C57.8}
```

Then

```math
r=\widetilde s-cs
\tag{C57.9}
```

is a signed equilibrium stress supported in `supp(s)` whose diameter coefficients sum to zero. Lemma C57.1 forces `r=0`.

## 3. Theorem C57 — an extreme null stress is a rigid body

### Theorem C57 (extreme-stress kernel rigidity)

Let `s=(alpha,beta)` be an extreme normalized KKT stress. If a fixed-diameter critical velocity `v` satisfies (C57.2), then there is one scalar `c` such that

```math
\boxed{
\kappa_e=c\quad(e\in C_s),
\qquad
\omega_h=c\quad(h\in H_s).
}
\tag{C57.10}
```

Consequently, after subtracting the infinitesimal rigid rotation `cJp`,

```math
\boxed{
v_i-cJp_i=t_s
\quad\text{for every vertex }i\text{ of the positive contact component},}
\tag{C57.11}
```

for one translation vector `t_s`.

#### Proof

Equation (C57.9) and Lemma C57.1 give

```math
\alpha_e(\kappa_e-c)=0,
\qquad
\beta_h(\omega_h-c)=0.
```

All coefficients on the selected support are positive, proving (C57.10). The canonical support-connectivity theorem says the positive contact graph has one nontrivial connected component containing every endpoint of every positive diameter edge. Along each positive contact edge,

```math
(v_i-cJp_i)-(v_j-cJp_j)=0.
```

Connectivity gives (C57.11). $`\square`$

### Relation to C56

C56 obtains common selected angular rate in the generic `c_min<0` transfer phase for **every** selected stress, not only extreme stresses. C57 is different:

- it applies to an extreme stress even in C56's zero-transfer forest phase;
- it uses KKT-polytope extremality rather than Robinson/Fiedler simplicity;
- it converts the entire positive contact component, not merely the diameter edge data, into a rigid body.

Thus C57 is especially useful precisely in the C56-Z phase left open by PR #58.

## 4. Apply C57 to the C54 null face

Let `L` be the infinitesimal-flex space of the maximal strong mixed framework, equivalently `span K_D(A)` by C54. Let

```math
\mathcal F_0
=
\{s\in S:\Omega_sV_x=\Omega_sV_y=0
\text{ for every }v\in L\}
\tag{C57.12}
```

be C54's nonempty exposed second-order null face.

Let its extreme points be

```math
s^1,\ldots,s^r.
```

Every extreme point of a face is extreme in the whole polytope `S`. Let `P_a` be the vertex set of the unique nontrivial positive contact component of `s^a`.

### Corollary C57.2 (null-face body cover)

For every `a` and every `v in L`, the restriction of `v` to `P_a` is an infinitesimal Euclidean rigid motion.

Moreover, for every pair `a!=b`,

```math
\boxed{P_a\cap P_b\ne\varnothing.}
\tag{C57.13}
```

If `P_a cap P_b` contains two distinct source vertices, then the two rigid motions coincide for every `v in L`.

#### Proof

The first claim is C57 because every stress in `F_0` annihilates all of `L`.

For the intersection claim, the midpoint

```math
\frac12(s^a+s^b)
```

is again a normalized KKT stress. Its positive contact support is exactly the union of the two positive supports. If `P_a` and `P_b` were disjoint, that midpoint would have two nontrivial positive-contact components, contradicting the canonical support-connectivity theorem. Hence the two bodies meet.

If they share two distinct vertices, their two planar infinitesimal rigid motions agree at two distinct points. Their angular velocities and translations are therefore equal. $`\square`$

## 5. Pairwise body mixing and C56

Take two null-face extremes `s^a,s^b` and their midpoint `s^{ab}`. It is again a null-face stress, so every `v in L` lies in its stress kernel.

If the positive diameter endpoint hull of `s^{ab}` is two-dimensional, C56 applies. There are only two possibilities.

### Generic midpoint

If

```math
\min_{e\ne f}K^{ab}_{ef}<0,
```

then C56-G forces one common angular rate on **all** positive diameter edges of the midpoint support. In particular the diameter rates carried by `s^a` and `s^b` agree for every `v in L`.

### Zero-transfer midpoint

If the two extreme bodies can rotate relatively for some `v in L`, their midpoint cannot be in C56-G. It must lie in C56-Z:

```math
K^{ab}=(B^{ab})^{-1},
\qquad
M^{ab}=0,
\qquad
H_{s^a}\cup H_{s^b}\text{ is a forest}.
\tag{C57.14}
```

Thus relative rotation of two null-face extreme bodies is possible only across a **zero-transfer forest midpoint**.

This is a substantial strengthening of the bare one-vertex intersection statement: every pair of extreme bodies that actually carries different angular rates is electrically decoupled in the exact C56 sense when their supports are mixed.

## 6. Exact C-I consequence

Suppose a contact-minimal triangle-free minimizer still has a weak contact. C13.4 gives a non-Euclidean flex in `L`. C57 says that flex cannot deform the interior of any null-face extreme positive support. After merging bodies that share two vertices, all remaining flex is relative rotation of rigid full-diameter bodies about one-vertex intersections.

For every pair of bodies with different angular rates, their midpoint stress is trapped in C56-Z. Hence:

```math
\boxed{
\text{surviving C-I shear}
\Longrightarrow
\text{pairwise one-vertex body hinges whose mixed stresses are zero-transfer forests}.}
\tag{C57.15}
```

The C55/C56 split description and the C57 primal description now align:

- C56-Z says every positive Kalmanson split is supported on one diameter edge or two adjacent projective directions;
- C57 says the corresponding physical stress supports are rigid bodies and shear only by one-vertex relative rotation.

The remaining issue is to turn this exact electrical decoupling into a graph separator or direct finite hinge motion.

## 7. Two-grove interpretation of the remaining zero-transfer phase

For a connected circular-planar electrical network, Devadoss--Forcey define the weight of a displayed circular split as the total weight of respecting spanning 2-groves divided by the spanning-tree partition function, and prove that this induced split system equals the Kalmanson split system of the resistance metric.

Therefore every positive split coefficient used in C55-C56 corresponds to an actual displayed split of the positive contact network with at least one positive-weight respecting two-grove. In C56-Z, the restriction that every positive split vector is supported on one diameter edge or two adjacent diameter directions is consequently a genuine graph-cut statement, not merely an algebraic cone decomposition.

This is the bridge for the next step; it is not used in the proof of C57.

## 8. Next exact target

### C58 zero-transfer body-hinge exclusion

Prove that two full-diameter extreme null-face bodies meeting at exactly one source vertex cannot have a zero-transfer midpoint unless their relative rotation is finitely integrable at fixed diameter.

Equivalent useful forms include:

1. prove the C56-Z two-grove support forces the union positive contact graph to be a one-sum at the shared hinge vertex;
2. prove any additional contact path between the two bodies creates a displayed split crossing nonlocal diameter directions, contradicting C56.30;
3. if the union is a one-sum, rotate the two rigid bodies finitely about the shared vertex and use the strong diameter thrackle inequalities to choose the sign that does not increase any cross-body diameter.

Any successful version gives a C7-style finite release and closes Gate C-I.

## 9. Binding cautions

C57 does not claim:

- that one extreme null body contains all of `C_*`;
- that pairwise intersection of all null bodies implies a common vertex;
- that a zero-transfer midpoint is automatically a literal graph one-sum;
- that all body-pin mechanisms integrate;
- that C-II is solved.

The theorem proves only the exact rigidity and mixing statements above.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C57:** for an extreme normalized KKT stress in the stress kernel of a critical velocity, multiplying positive stress coefficients by their angular rates produces a signed equilibrium stress on the same support. Extremality forces that signed stress to be proportional to the original stress. Hence every positive contact and diameter edge has one common angular rate, and the positive contact component is a rigid body.

**Null-face consequence:** every extreme point of C54's exposed null face is rigid for every strong-framework flex. Any two extreme bodies meet in at least one source vertex; sharing two vertices merges their motions.

**C56 interaction:** if two null-face extreme bodies rotate differently, their midpoint stress cannot be in the generic C56 phase. It must be C56-Z: exact zero transfer, zero edge defect, and forest diameter support.

**Next:** identify/exclude/integrate this zero-transfer one-vertex body hinge.
