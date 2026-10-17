> Generated reading edition · [exact source](../../../docs/reports/target_c_arbitrary_thrackle_response_contraction_2026-08-31.md) · source SHA-256 `e464eee9cfcf8efa947383d1c11ae73163a6b3e9058abb0d35d7eb180495d3ee`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-CA613948843D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C: arbitrary diameter-thrackle response contraction

**Date:** 2026-08-31  
**Repository base:** `278ad522` (main after C52 / PR #53)  
**Run type:** exact response inequality / selected-stress closure  
**Target:** Target C Gate C-I  
**Depends on:** C11 affine response, C30 Schur reduction, C50 Kalmanson split cone, C52 weighted Robinson equilibrium lemma

## LEVEL I STATUS

**STILL OPEN.**

> **Restoration audit (2026-09-09).** The September 5 purported regression used
> incompatible projective ordering and orientation and is withdrawn. The
> [complete dependency audit](target_c_c53_orientation_and_ci_restoration_2026-09-09.md)
> proves the universal chord-sign reduction, checks C52.R and the electrical
> import, restores C53.4--C53.6, and applies them to C63. Always choose the
> projective cut and common-half-plane orientation consistently.

C52 removed every selected positive diameter matching. This report removes the
matching hypothesis entirely.

For any normalized KKT stress whose positive diameter endpoints span two
dimensions, the positive diameter graph is a geometric thrackle: every two
diameter edges share an endpoint or cross. Order the **edges**, not the boundary
vertices, by projective chord direction. The same circular-interval split signs
used in C52 remain Robinson for this edge order even when endpoints are shared.
The C52 weighted Robinson lemma then proves that the complete selected signed
stress matrix is positive semidefinite.

Thus the remaining C-I obstruction is no longer a negative response mode of any
selected two-dimensional KKT support. What remains is the exact kernel / finite
integration problem identified already in the second-order variance audit.

## 1. Theorem C53

### Theorem C53 (arbitrary selected diameter-thrackle contraction)

Fix a normalized KKT stress `s=(alpha,beta)` in the Target C setting. Let
`G_s` be its connected positive unit-contact graph and let `H_s` be its positive
diameter graph on the loaded boundary set `B=V(H_s)`. Assume

$$
\operatorname{aff} B=\mathbb R^2.
\tag{C53.1}
$$

Let `Lambda` be the connected positive-contact Dirichlet response on `B`,
`R=Lambda^+`, and let `P` be the centered boundary coordinate matrix. Give each
positive diameter edge `e` an arbitrary orientation for the moment and let `Q` be
the resulting boundary-by-edge incidence matrix. Put

$$
B_H=\operatorname{diag}(\beta_e:e\in H_s),
\qquad
L_H=Q B_H Q^{\mathsf T},
\qquad
U=Q^{\mathsf T}P,
\qquad
K=Q^{\mathsf T}RQ.
\tag{C53.2}
$$

The C11 affine response identity is

$$
\Lambda P=L_HP.
\tag{C53.3}
$$

Then

$$
\boxed{B_H^{-1}-K\succeq0.}
\tag{C53.4}
$$

Consequently

$$
\boxed{\Lambda-L_H\succeq0\quad\text{on }\mathbf1^\perp,}
\tag{C53.5}
$$

and the full selected stress matrix satisfies

$$
\boxed{
\Omega_s=L_{C_s}(\alpha)-L_{H_s}(\beta)\succeq0.
}
\tag{C53.6}
$$

No restriction on `|H_s|`, maximum diameter degree, acyclicity, matching topology,
or equality of the KKT weights is required.

### Low-dimensional support

The theorem is stated under (C53.1) because that is the live C30 branch. The
canonical low-support audit already handles the one-dimensional case relevant to a
contact-minimal weak-contact survivor. In particular C13.4 gives a two-dimensional
maximal force hull and at least two strong diameter chords whenever a weak contact
survives. C53 is therefore exactly the response theorem needed for the live C-I
mechanism branch.

## 2. Edge-direction normalization

Distinct diameter edges cannot be parallel. If two are vertex-disjoint, the planar
diameter-thrackle property makes them cross; if they share a vertex, parallelism
would make three source vertices collinear, impossible for distinct saturated hull
vertices.

Choose a point of the projective direction circle that is not one of the finitely
many diameter-edge directions. Orient every edge vector into the corresponding open
half-plane and order the edges by their projective direction:

$$
e_0<e_1<\cdots<e_{m-1},
\qquad m=|H_s|.
\tag{C53.7}
$$

Let

$$
u_r=p_{a_r}-p_{b_r}
$$

be the oriented vector of `e_r=a_rb_r`. Choose covectors `ell,m_0` positive on
that half-plane and write

$$
a_r=\ell(u_r)>0,
\qquad
t_r=\frac{m_0(u_r)}{\ell(u_r)}.
$$

After orienting `(ell,m_0)` consistently with (C53.7),

$$
t_0<t_1<\cdots<t_{m-1},
\qquad
u_r=a_r(1,t_r).
\tag{C53.8}
$$

Thus, with

$$
E=\operatorname{diag}(a_r),
\qquad
V=\begin{pmatrix}1&t_0\\\vdots&\vdots\\1&t_{m-1}\end{pmatrix},
$$

we have

$$
U=EV.
\tag{C53.9}
$$

The response identity gives exactly the same edge-space affine equations as in C52:

$$
K B_H U=U.
\tag{C53.10}
$$

Indeed `R Lambda P=P` on centered coordinate columns, and premultiplication of
`R Q B_H U=P` by `Q^T` gives (C53.10). This derivation does not require the
columns of `Q` to have disjoint supports.

Define

$$
N=B_H-B_H K B_H,
\qquad
M=ENE,
\qquad
\gamma_r=a_r\beta_r>0.
\tag{C53.11}
$$

Then

$$
M\mathbf1=0,
\qquad
Mt=0,
\tag{C53.12}
$$

and, for distinct edges `r,s`,

$$
M_{rs}=-\gamma_r\gamma_sK_{rs}.
\tag{C53.13}
$$

Therefore C52.R will prove `M>=0`, and hence C53, once `K` is shown to be a
Robinson similarity in the edge-direction order.

## 3. Three-chord interval lemma

The only new point beyond C52 is that two diameter edges may share an endpoint.

### Lemma C53.T (thrackle interval signs)

Let `e<f<g` be three pairwise-intersecting chords of a strictly convex polygon,
ordered and oriented by projective direction as in (C53.7). For any circular
boundary interval `A`, put

$$
z_h=\mathbf1_A(\operatorname{head}h)
     -\mathbf1_A(\operatorname{tail}h)
\qquad(h=e,f,g).
\tag{C53.T1}
$$

Then

$$
\boxed{
z_g(z_e-z_f)\le0,
\qquad
z_e(z_g-z_f)\le0.
}
\tag{C53.T2}
$$

#### Proof

The incidence graph of three pairwise-intersecting chords has only five possible
endpoint types:

1. a triangle on three endpoints;
2. a three-edge star on four endpoints;
3. a three-edge path on four endpoints, whose disjoint end edges cross;
4. two edges sharing one endpoint and a third edge crossing both, on five endpoints;
5. three pairwise-crossing disjoint edges, on six endpoints.

Pairwise intersection fixes the cyclic endpoint order in each type up to dihedral
symmetry and relabeling. Projective direction order is invariant under a continuous
strictly convex deformation within one type: two disjoint crossing chords cannot
become parallel, and two chords sharing an endpoint cannot become parallel without
three hull vertices becoming collinear.

Thus each type may be checked on a regular polygon representative. Representatives
before orientation are

$$
\begin{array}{c|c}
\text{type}&\text{representative edges in cyclic labels}\\ \hline
\text{triangle}&01,12,02\\
\text{star}&01,02,03\\
\text{path}&02,03,13\\
\text{one shared pair}&02,03,14\\
\text{disjoint matching}&03,14,25.
\end{array}
\tag{C53.T3}
$$

For any cut of the projective direction circle, orient the three representatives
into the selected half-plane and list them by increasing direction. Restricting a
circular boundary interval to the three-to-six endpoint set gives a circular
consecutive-ones pattern. Across all five types and the three possible placements of
the projective cut, the resulting signed triples are contained in

$$
\begin{gathered}
(-1,-1,-1),(-1,-1,0),(-1,-1,1),(-1,0,0),(-1,0,1),(-1,1,1),\\
(0,-1,-1),(0,-1,0),(0,0,-1),(0,0,0),(0,0,1),(0,1,0),(0,1,1),\\
(1,-1,-1),(1,0,-1),(1,0,0),(1,1,-1),(1,1,0),(1,1,1).
\end{gathered}
\tag{C53.T4}
$$

This list is the same nineteen-pattern list already implicit in the six-endpoint
matching check of C52; the shared-endpoint types only remove patterns from it.
Substitution in (C53.T2) proves both inequalities in every case. `square`

### Audit note on the finite case check

The table (C53.T3) is not a computational assumption. It is the complete abstract
classification of three edges in a simple graph under the condition that every pair
of geometric chords intersects. The nineteen values in (C53.T4) follow by walking
the two endpoints of a circular interval around each representative endpoint cycle;
no metric quantity enters the check.

## 4. Kalmanson splits are Robinson on diameter edges

Use the C50 Kalmanson split-cone representation of the effective-resistance matrix.
Modulo a sum matrix, annihilated by `Q^T(\cdot)Q`, write `W` as a nonnegative
combination of circular interval cut metrics.

For one interval `A`, let

$$
z_A=Q^{\mathsf T}\mathbf1_A.
\tag{C53.14}
$$

Its contribution to

$$
K=Q^{\mathsf T}RQ
$$

is `z_A z_A^T`. The positive diameter graph is a geometric thrackle, so every
three of its edges satisfy Lemma C53.T. Therefore, for every `e<f<g`,

$$
\begin{aligned}
K_{eg}-K_{fg}
 &=\sum_A\lambda_A z_g(z_e-z_f)\le0,\\
K_{eg}-K_{ef}
 &=\sum_A\lambda_A z_e(z_g-z_f)\le0,
\end{aligned}
\tag{C53.15}
$$

with all `lambda_A>=0`. Hence

$$
\boxed{
K_{eg}\le\min(K_{ef},K_{fg})
\qquad(e<f<g).
}
\tag{C53.16}
$$

So `K` is a Robinson similarity in the projective diameter-edge order.

This is the exact point at which the diameter-thrackle geometry enters. No degree
bound, forest assumption, or matching decomposition is used.

## 5. Completion by C52.R

Equations (C53.12)-(C53.13) put `M` in the hypotheses of the weighted Robinson
equilibrium lemma C52.R, with the strictly increasing vector `t` from (C53.8).
Therefore

$$
M\succeq0.
\tag{C53.17}
$$

Since `E` and `B_H` are positive diagonal,

$$
N=E^{-1}ME^{-1}\succeq0
$$

and

$$
B_H^{-1}-K
=B_H^{-1}NB_H^{-1}\succeq0.
\tag{C53.18}
$$

This proves (C53.4).

As in C52, set

$$
Y=R^{1/2}Q B_H^{1/2}
$$

on `1^perp`. Then

$$
Y^{\mathsf T}Y=B_H^{1/2}KB_H^{1/2}\preceq I,
$$

so `YY^T<=I`. Hence

$$
R^{1/2}L_HR^{1/2}\preceq I,
$$

which is equivalent to `L_H<=Lambda` on the centered boundary space. The
positive interior contact block in the C30 Schur congruence then gives

$$
L_{C_s}(\alpha)-L_{H_s}(\beta)\succeq0.
$$

This proves C53. `square`

## 6. Exact C-I consequence

C30 originally left the possibility that a selected two-dimensional KKT stress had
a negative response mode. C50, C51, and C52 progressively removed finite forests,
four opposite pairs, and then every matching. C53 removes **all** selected positive
diameter topologies at once:

$$
\boxed{
\operatorname{aff}V(H_s)=\mathbb R^2
\Longrightarrow
\Omega_s\succeq0
\quad\text{for every normalized KKT stress }s.
}
\tag{C53.19}
$$

Now take a relative-interior weak-release critical velocity `v`. The canonical
second-order theorem C13.3 supplies a normalized KKT stress `s(v)` satisfying

$$
\operatorname{tr}(V^{\mathsf T}\Omega_{s(v)}V)\le0.
\tag{C53.20}
$$

Whenever the selected support of `s(v)` is two-dimensional, C53 and (C53.20) force

$$
\operatorname{tr}(V^{\mathsf T}\Omega_{s(v)}V)=0,
\qquad
\Omega_{s(v)}V_x=\Omega_{s(v)}V_y=0.
\tag{C53.21}
$$

Thus the second-order inequality has become an exact **stress-kernel condition**.
The earlier warning remains binding: C53 does not by itself classify that kernel.
The coordinate columns `1,x,y` are always in the stress kernel, so affine shear is
not automatically excluded by PSD.

This is a strict reduction of C-I. The remaining question is no longer to prove a
reverse quadratic inequality or find a PSD stress. It is:

> classify the equality kernel of the C53 contraction for the actual
> direction-dependent KKT support, and prove that any relative-interior critical
> velocity in that kernel has one common strong-diameter angular rate.

That kernel statement would feed directly into the already-proved C7 finite
integration theorem and eliminate every weak unit contact.

## 7. Shortest remaining lemma

### C54 target (C53 kernel rigidity)

For the normalized KKT stress selected by C13.3 for a relative-interior weak-release
velocity, prove that

$$
\Omega_s\succeq0,
\qquad
\Omega_sV=0
$$

forces the angular rates of all strong diameter chords to agree.

A sufficient version is:

> if the edge-space Robinson defect `M` in C53 has a non-affine kernel vector, then
> the Kalmanson split support has a zero-separation decomposition that forces a
> one-vertex terminal separator or another contact-network structure forbidden by
> the triangle-free unit-contact degree bounds.

The equality/separator mechanism from C50.2 is the model, but the general kernel is
not yet classified.

## 8. Regressions and no-go statements

C53 does not prove Level I by itself.

- PSD is not rigidity: `Omega_s` always annihilates `1,x,y`.
- An affine velocity field can therefore have zero C53 energy.
- The direction-dependent stress selected by C13.3 need not have maximal support.
- C53 does not give strict complementarity or a uniform spectral gap.
- The near-star strict-minor regression remains relevant to quantitative C-II
  transport.
- Decomposing the diameter graph into matchings is neither needed nor valid as an
  affine-response proof; C53 works on the total support.

## 9. Verification

Before promotion:

1. every triple of pairwise-intersecting chords on regular `n`-gons for
   `4<=n<=10` was exhaustively checked against every circular interval; no violation
   of (C53.T2) occurred;
2. the five abstract three-edge incidence types were then isolated, yielding the
   exact hand-checkable list (C53.T4), so the theorem does not depend on the finite
   computation;
3. the remainder is a direct invocation of the exact C52.R weighted Robinson lemma
   and the standard C30 Schur congruence.

## 10. Compact handoff

**LEVEL I STATUS:** still open.

**C53:** every normalized KKT stress with two-dimensional positive diameter endpoint
hull has `Omega_s>=0`, with no topology or support-size restriction.

**New mechanism:** diameter thrackle + projective edge order makes every Kalmanson
interval split Robinson even across shared endpoints; C52.R then applies unchanged.

**Immediate C-I effect:** the C13.3 second-order certificate is forced onto the exact
PSD equality boundary, so the weak-contact obstruction is now a stress-kernel
classification problem, not a negative-response problem.

**Next:** classify the C53 equality kernel strongly enough to force common diameter
angular rate and invoke C7 finite integration.
