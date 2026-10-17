> Generated reading edition · [exact source](../../../docs/reports/target_c_multibody_shunt_collapse_2026-08-31.md) · source SHA-256 `7ed9d842f2b915f035086dad4ec017ecc8475a49589285b0c8fbdad46ccc83c3`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C4D14A84A89E","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
<!-- migration-source: path=docs/reports/target_c_multibody_shunt_collapse_2026-08-31.md; commit=42f0296d1aca068c809f74cee5dcdb4ebdb27c73; blob=f92908bd28dab3f9ad97b2ba74b922a0f5c6a3e3; lifecycle=unreviewed; canonical=false -->
> **Migration record:** Preserved from source-main commit `42f0296d1aca068c809f74cee5dcdb4ebdb27c73`. The source artifact index marks this report unreviewed; this import preserves its complete argument and does not promote its claims. The destination theorem manifest and current Target C state remain authoritative.

# Erdős Problem #99 — Target C: multi-body shunt collapse

**Date:** 2026-08-31  
**Repository base:** `105249d7` (main after star-center C60 / PR #62)  
**Run type:** exact electrical equality + finite integration  
**Target:** Target C Gate C-I  
**Depends on:** C11 affine response, C53/C54 universal PSD, C56 zero-transfer dichotomy, C57 extreme-body rigidity, C59 hinge integration, C60 star-center articulation

## LEVEL I STATUS

**STILL OPEN.**

C59 removes the two-body null hinge and C60 constrains every remaining three-body mixture to a bounded articulated star forest. This report eliminates the genuinely cyclic multi-body alternative altogether.

For a fixed strong-framework flex, merge null-face extreme stresses that induce the same planar rigid motion. Distinct motion classes meet pairwise in one source vertex. If three classes met at three different hinge vertices, the other two classes would form a positive-conductance shunt between two attachment vertices of the first class. The average of the three stresses is still in the null face and carries nonconstant diameter angular rates, so C56 forces it into the exact zero-transfer phase. Its diameter-current energies are therefore already equal to the maximal values allowed by C53. Rayleigh monotonicity leaves no room for the shunt to lower any of them.

The equality case is rigid: Sherman-Morrison says every diameter dipole of the first body must induce zero voltage across its two attachment vertices. The body's affine KKT equilibrium then says the two source coordinates themselves are equal. Contradiction.

Hence all distinct null-body motion classes share one common source hinge. A finite motion rotating every class about that common hinge with its own angular rate simultaneously has the favorable C59 sign on every cross-class active row. Thus the entire covered null-body bouquet integrates.

The only C-I obstruction left by this chain is a **null-face coverage defect**: a vertex incident to a strong active constraint may lie outside the union of the extreme positive contact components of the second-order null face.

## 1. Motion classes in the C54 null face

Let `F_0` be the exposed C54 null face and let `L` be the infinitesimal-flex space of the maximal strong framework. Fix `v in L`.

By C57, every extreme stress `s^a in F_0` has one connected positive contact component `P_a` on which `v` is an infinitesimal rigid motion

$$
v(p)=t_a+\omega_aJp.
\tag{C61.1}
$$

Any two extreme bodies intersect in at least one source vertex. If two bodies have the same angular rate, equality of their velocities at a shared source vertex forces the same translation, so they have exactly the same rigid velocity field. Merge all such bodies into one **motion class**.

If two motion classes `A,B` are distinct, their rigid velocity fields are distinct. They can agree at at most one point in the plane. Since the underlying extreme bodies intersect, the class vertex sets satisfy

$$
P_A\cap P_B=\{x_{AB}\},
\tag{C61.2}
$$

where `x_AB` is the unique instantaneous center of the relative rigid motion and is an actual source vertex.

Positive diameter supports of distinct motion classes are disjoint: sharing one diameter edge would make the two bodies share both endpoints and hence the same rigid motion by C57.

## 2. Three distinct hinges create a positive electrical shunt

Take three distinct motion classes `A,B,C`, represented by extreme null-face stresses `s^A,s^B,s^C`. Suppose for contradiction that

$$
x:=x_{AB}\ne y:=x_{AC}.
\tag{C61.3}
$$

Let `z=x_{BC}`. Then `x,y,z` are all distinct. For example, if `z=x`, then `x` belongs to both `A` and `C` in addition to `y`, so `A` and `C` would share two vertices and have the same rigid motion.

The positive contact component of `B` contains a positive-conductance path from `x` to `z`; the component of `C` contains one from `z` to `y`. Their union therefore gives a connected positive-conductance network from `x` to `y` which is otherwise disjoint from the vertex set of `A` except at the two attachment vertices `x,y`.

Kron-reducing that union onto `{x,y}` produces one effective conductance

$$
g>0.
\tag{C61.4}
$$

Thus, from the electrical viewpoint of body `A`, adding bodies `B,C` adds a strict positive shunt `g` between the two distinct attachment vertices `x,y`.

C60's articulation theorem is compatible with this setup but is not needed below: the contradiction comes already from exact response saturation.

## 3. The three-body average must be zero-transfer

Set

$$
\bar s=\frac13(s^A+s^B+s^C).
\tag{C61.5}
$$

This is still in the null face, so `v` lies in the vector stress kernel of `Omega_bar`.

The three positive diameter supports are disjoint, and their angular rates under `v` are `omega_A,omega_B,omega_C`, not all equal because the motion classes are distinct. The positive diameter endpoint hull of `bar s` is two-dimensional: a one-dimensional normalized KKT support has only one positive diameter edge by C54.1, while (C61.5) contains at least one distinct positive diameter edge from each class.

Therefore C56 applies. The generic C56 phase would force one common selected diameter angular rate, impossible here. Hence `bar s` lies in C56-Z:

$$
\boxed{
Q^{\mathsf T}\bar L^+Q=\bar B^{-1},
}
\tag{C61.6}
$$

where `bar L` is the positive contact Laplacian of the averaged stress and `bar B` its diagonal positive diameter weight matrix.

For every positive diameter edge `h` of body `A`, its coefficient in the average is `beta_h^A/3`, so (C61.6) gives the full-network unit-current energy

$$
q_h^{\mathsf T}\bar L^+q_h
=\frac{3}{\beta_h^A}.
\tag{C61.7}
$$

## 4. Saturation plus Rayleigh monotonicity kills the shunt

Let `L_A` be the positive contact Laplacian of the extreme stress `s^A`, on its connected component. The part of the averaged contact network inside `A` has Laplacian

$$
L_0=\frac13L_A.
$$

By universal response contraction for `s^A`,

$$
q_h^{\mathsf T}L_A^+q_h\le\frac1{\beta_h^A}.
\tag{C61.8}
$$

Therefore the same current in the isolated scaled body has energy

$$
q_h^{\mathsf T}L_0^+q_h
=3q_h^{\mathsf T}L_A^+q_h
\le\frac3{\beta_h^A}.
\tag{C61.9}
$$

Adding the positive shunt through `B union C` can only decrease effective resistance. Hence

$$
q_h^{\mathsf T}\bar L^+q_h
\le q_h^{\mathsf T}L_0^+q_h
\le\frac3{\beta_h^A}.
\tag{C61.10}
$$

But the left side is exactly `3/beta_h^A` by (C61.7). Thus equality holds throughout (C61.10) for every `h in H_A`.

After Kron reduction of the rest of the three-body network, the Laplacian seen on `P_A` is

$$
L_0+gq_{xy}q_{xy}^{\mathsf T},
\qquad
q_{xy}=e_x-e_y,
\tag{C61.11}
$$

with `g>0`.

On the centered space, the rank-one inverse identity gives for any zero-sum current `j`

$$
\begin{aligned}
j^{\mathsf T}(L_0+gq_{xy}q_{xy}^{\mathsf T})^+j
&=j^{\mathsf T}L_0^+j\\
&\quad-
\frac{g\,(q_{xy}^{\mathsf T}L_0^+j)^2}
{1+gq_{xy}^{\mathsf T}L_0^+q_{xy}}.
\end{aligned}
\tag{C61.12}
$$

Equality in (C61.10) therefore implies

$$
q_{xy}^{\mathsf T}L_0^+q_h=0
\qquad(h\in H_A).
$$

Since `L_0^+=3L_A^+` on zero-sum currents,

$$
\boxed{
q_{xy}^{\mathsf T}L_A^+q_h=0
\qquad(h\in H_A).
}
\tag{C61.13}
$$

So every positive diameter dipole of body `A` produces exactly the same electrical potential at its two distinct hinge attachments `x,y`.

## 5. The affine equilibrium identity makes that impossible

Let `P_A` denote the full vertex-coordinate matrix of the positive contact component of `s^A`, and let `Q_A` be the full vertex-by-positive-diameter incidence matrix. The KKT affine equilibrium equation is

$$
L_AP_A=Q_AB_AU_A,
\qquad
U_A=Q_A^{\mathsf T}P_A.
\tag{C61.14}
$$

Apply `q_xy^T L_A^+`. Since `q_xy` is zero-sum, the harmless constant projection disappears:

$$
\begin{aligned}
p_x-p_y
&=q_{xy}^{\mathsf T}P_A\\
&=q_{xy}^{\mathsf T}L_A^+Q_AB_AU_A\\
&=\sum_{h\in H_A}
\beta_h^A
(q_{xy}^{\mathsf T}L_A^+q_h)
\,u_h.
\end{aligned}
\tag{C61.15}
$$

Every coefficient in the last sum is zero by (C61.13). Hence

$$
p_x=p_y,
$$

contradicting that `x,y` are distinct source vertices.

We have proved:

### Theorem C61.1 (three-body shunt collapse)

For three distinct null-face rigid-motion classes,

$$
\boxed{x_{AB}=x_{AC}=x_{BC}.}
\tag{C61.16}
$$

There is no flexible null-body triangle with three different source hinges, collinear or otherwise. This strictly sharpens the C59 instantaneous-center collinearity statement and closes the covered collinear-cycle branch left by C60.

## 6. All distinct motion classes share one common source hinge

Take any finite collection of distinct motion classes. If there is only one, there is no internal null-body shear; if there are two, C59 handles them. If there are at least three, choose two classes `A,B` and write their hinge as `x`. For any third class `C`, Theorem C61.1 applied to `A,B,C` gives

$$
x_{AC}=x_{BC}=x.
$$

Repeating for every class gives one common source vertex

$$
\boxed{x\in P_a\quad\text{for every motion class }a,}
\tag{C61.17}
$$

and distinct classes meet only at `x`.

Thus every null-body shear is a **bouquet of rigid bodies about one common source hinge**.

## 7. The common-hinge bouquet integrates simultaneously

Subtract the rigid motion of one reference class. Since every class contains the same source vertex `x`, each class velocity has the form

$$
v(p)=\delta_aJ(p-x)
\qquad(p\in P_a)
\tag{C61.18}
$$

for a class-dependent scalar `delta_a`.

Define the finite motion

$$
p(t)=x+R_{t\delta_a}(p-x)
\qquad(p\in P_a),
\tag{C61.19}
$$

and keep `x` fixed. Distinct classes intersect only at `x`, so this is well-defined.

For `p in P_a\setminus\{x\}` and `q in P_b\setminus\{x\}`, applying the inverse rotation of class `b` preserves distance and reduces the cross distance to

$$
|R_{t(\delta_a-\delta_b)}(p-x)-(q-x)|.
\tag{C61.20}
$$

This is exactly the two-body formula of C59. Therefore every stationary cross-class unit contact lengthens, every stationary cross-class diameter pair shortens, strict first-order rows stay strict, and inactive rows retain slack.

Internal distances within each motion class remain exactly constant.

### Theorem C61.2 (covered null-body bouquet integration)

Suppose every vertex incident to a **strong** active constraint lies in the union of the null-face extreme-body motion classes for a relative-interior weak-release velocity `v`. Then the simultaneous finite rotations (C61.19), together with straight first-order motion for vertices incident only to weak constraints, produce same-diameter feasible configurations for all sufficiently small positive `t`, with every weak active row strict.

Hence a contact-minimal minimizer with a weak contact cannot satisfy this strong-vertex coverage condition.

#### Proof

The covered strong vertices are handled by (C61.19) and the C59 pairwise sign argument. A vertex outside the body union is, by hypothesis, incident to no strong active row. Move such a vertex by its original relative-interior velocity to first order. Every active row involving it is weak and therefore has a strict feasible first derivative; the `O(t^2)` difference between the hybrid path and its tangent cannot reverse that sign for sufficiently small positive `t`. Inactive rows have strict slack.

At least one positive diameter edge lies inside a null-face body and is preserved exactly by its rigid rotation, so the new diameter remains exactly `D`. Every weak contact becomes strict. $\square$

## 8. Exact remaining Gate C-I obstruction

C61 removes all internal and multi-body hinge compatibility from the null face. The only surviving C-I possibility is:

> **Null-face strong-vertex coverage defect.** Some vertex incident to a strong active constraint belongs to no positive contact component of any extreme stress in the exposed second-order null face `F_0`.

Equivalently, the maximal support `E_*` contains a strong edge whose endpoint support is not covered by the union support of `F_0`.

This is now the sole support-selection issue separating the universal PSD/null-face machinery from the C7 finite-release contradiction.

## 9. Why this does not silently assume maximal support

The C54 null face can be a proper face of the full KKT polytope. C61 does **not** claim its support equals `E_*`. The proof closes every mechanical hinge inside the null-face body union and then states the uncovered strong-support case explicitly.

That residual is real: C6 says `E_*` is the union of supports of all normalized KKT stresses, not necessarily of stresses in `F_0`.

## 10. Next exact target

### C62 null-face support saturation

Prove that every strong active vertex is contained in the support union of the second-order null face, or derive a contradiction from an edge of `E_*` omitted by that face.

A promising convex-PSD formulation is:

- `F_0` is the intersection of the KKT polytope with one face of the PSD cone determined by the strong-flex space `L`;
- a strong edge outside the support of `F_0` is positive only in stresses that are strictly coercive on some vector of `L`;
- use relative-interior perturbations inside `L` and the C13.3 zero-minimum condition to force that edge into a zero-energy stress, or convert its permanent exclusion into the C9 tangential separator.

No remaining selected-response topology or body-hinge geometry needs classification before C62.

## 11. Compact handoff

**LEVEL I STATUS:** still open.

**C61.1:** three distinct null-body motion classes cannot meet at three different hinges. The other two bodies form a positive electrical shunt across two attachment vertices of the first. C56-Z saturation plus Rayleigh equality forces every diameter dipole to have zero voltage across those attachments; the affine KKT equation then forces the two source vertices to coincide.

**C61.2:** all distinct null-body motion classes therefore share one common source hinge. Simultaneous finite rotations about that hinge reduce every cross-class active row to the C59 two-body formula, so the whole covered bouquet integrates.

**Only remaining C-I obstruction:** a strong active vertex outside the support union of the exposed null face.

**Next:** prove null-face support saturation or turn permanent support exclusion into the C9 separator contradiction.
