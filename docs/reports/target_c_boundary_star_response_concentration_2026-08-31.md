<!-- theorem-state: {"artifact_id":"ART-AA20F42D5220","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C70: mechanical stress-star concentration forces boundary-response starization

**Date:** 2026-08-31  
**Repository base:** `3f724491` (main after C69 / PR #73)  
**Run type:** exact PSD cut consequence / response-support reduction  
**Target:** Target C Gate C-II  
**Depends on:** C41 response defect normalization, C64 PSD response-cut domination, C66 mechanical stress-star concentration  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C66 proves that if the response trace defect is too small, almost all mechanical diameter weight is incident to one diameter vertex `z`. C70 shows that the electrical response itself must then concentrate on the same boundary-centered star.

Let

\[
\varepsilon
:=\sum_{b<k}c_{bk}-1
=\frac12\operatorname{tr}(\Lambda-L_H),
\]

where `c_bk=-Lambda_bk` are the response conductances, and for a diameter vertex `z` write

\[
S_z:=\sum_{zk\in H}\beta_{zk},
\qquad
\delta_z:=1-S_z.
\]

Define the response mass not incident to `z` by

\[
X_z:=
\sum_{\substack{b<k\\z\notin\{b,k\}}}c_{bk}.
\]

Then

\[
\boxed{X_z\le\delta_z+\varepsilon.}
\tag{C70.1}
\]

For the C66 star center,

\[
\boxed{
X_z
\le
\left(1+\frac{2\pi}{\kappa_0}D\right)\varepsilon.
}
\tag{C70.2}
\]

Hence

\[
D\varepsilon\to0
\quad\Longrightarrow\quad
X_z\to0.
\tag{C70.3}
\]

So the remaining near-zero phase is simultaneously

1. a mechanical diameter stress star;
2. an electrical boundary-response star; and
3. by C68, an almost-radial unit-contact stress carrier.

This is stronger than the old additive/internal-star regression. The remaining quantitative theorem is now a bounded-degree **boundary-star near-separator** problem for the actual unit-contact network.

---

## 1. Response and diameter cut degrees

Let

\[
d_b:=\sum_{k\ne b}c_{bk}
\]

be the response degree at a loaded boundary vertex and

\[
s_b:=\sum_{bk\in H}\beta_{bk}
\]

its mechanical diameter-load degree.

C64 gives

\[
M:=\Lambda-L_H\succeq0.
\]

Apply the singleton cut vector at `z`. Equivalently use the diagonal entry of `M`:

\[
\boxed{d_z\ge s_z=S_z.}
\tag{C70.4}
\]

The total response conductance is

\[
\sum_{b<k}c_{bk}=1+\varepsilon.
\tag{C70.5}
\]

Split this total into pairs incident and not incident to `z`:

\[
1+\varepsilon=d_z+X_z.
\tag{C70.6}
\]

Combining C70.4-C70.6 gives

\[
X_z
=1+\varepsilon-d_z
\le1+\varepsilon-S_z
=\delta_z+\varepsilon.
\]

This proves C70.1.

No circular-minor inequality is needed. C70 is the direct scalar consequence of the PSD cut order.

---

## 2. Insert the C66 mechanical star estimate

C66 gives a diameter vertex `z` satisfying

\[
S_z
\ge
1-C_0D\varepsilon,
\qquad
C_0:=\frac{2\pi}{\kappa_0}.
\tag{C70.7}
\]

Therefore

\[
\delta_z\le C_0D\varepsilon.
\tag{C70.8}
\]

Substitute C70.8 into C70.1:

\[
\boxed{
X_z
\le
(C_0D+1)\varepsilon.
}
\tag{C70.9}
\]

This is C70.2.

If `D epsilon ->0`, then both `delta_z` and `X_z` tend to zero.

Moreover C70.4 and C70.5 give

\[
1-C_0D\varepsilon
\le d_z\le1+\varepsilon,
\tag{C70.10}
\]

so the response star degree itself tends to one.

---

## 3. The response-star phase is a boundary-separator problem

If `X_z=0` exactly, then the response graph on the loaded terminals has no conductance between two terminals different from `z`. By the circular-planar connection theorem, no two such terminals can be connected in the physical positive-contact network after deleting `z`; otherwise the corresponding two-terminal connection produces a positive response coupling.

Thus exact `X_z=0` would force every component of `C-z` to contain at most one loaded terminal other than `z`. Since the physical contact degree of a loaded vertex is at most three in C-II,

\[
\deg_C(z)\le3,
\]

so there could be at most three other loaded terminals. This contradicts C34 for large `D`.

This recovers a qualitative exact-star obstruction directly for the **boundary-centered** star. It is different from SEPq, whose equality mode was an additive response represented by an internal star separator.

The live problem is stability:

> quantify how much non-`z` response mass is forced when `C-z` has only at most three physical branches but contains `Theta(D)` loaded terminals, the total positive contact conductance is exactly `D^2`, and the branches are embedded as a unit-distance triangle-free network of Euclidean scale `D`.

The old abstract near-star network regression does not settle this boundary-star problem.

---

## 4. Interaction with C68

For the same C66 center, C68 gives

\[
Q_z
:=\sum_{ij\in C}\alpha_{ij}
[1-(r_i-r_j)^2]
\le C_0D^3\varepsilon.
\]

Thus under `D epsilon ->0`:

- mechanical nonstar beta mass is `o(1)`;
- response nonstar conductance mass is `o(1)`; and
- normalized transverse/angular contact-stress energy is `o(D^2)`.

The remaining phase can therefore be described without ambiguity as an approximate boundary-star separator carried by almost radial high-stress contact corridors, with the two-dimensional geometry relegated to low-stress branches.

---

## 5. What a closing C71 would need

A sufficient next theorem is any bound of the form

\[
X_z\ge\frac{c}{D}
\]

for every C-II force-visible contact network and every loaded terminal `z`, unless the configuration already contains a unit triangle.

Combined with C70.9 this would imply

\[
(C_0D+1)\varepsilon\ge\frac cD,
\]

which gives only `epsilon=Omega(D^-2)` and is not yet enough to contradict the C66 threshold. A stronger constant lower bound on `X_z`, or a direct relation between `X_z` and `Q_z`, would be preferable.

More generally, if

\[
X_z\ge cD^{-a},
\]

then C70 converts it into an explicit response-defect scale. The physical geometry and total conductance budget must determine the sharp exponent.

The bounded-degree rooted-tree model suggests that topology alone cannot give a constant bound; very high conductance on shared trunks can suppress cross-response. The exact stress budget `sum_C alpha=D^2` and Euclidean length of those trunks are therefore essential.

## Compact handoff

For any diameter vertex `z`,

`X_z := sum response conductance on pairs not incident z`

satisfies

`X_z <= (1-S_z)+epsilon`.

At the C66 center,

`X_z <= (1+(2pi/kappa_0)D)epsilon`.

Thus `D epsilon ->0` makes both the mechanical diameter stress and the boundary response converge in total mass to the same star centered at `z`.

Exact `X_z=0` would force at most `deg_C(z)<=3` other loaded terminals, contradicting C34. The unresolved theorem is quantitative stability of that boundary separator under the `D^2` contact-conductance budget and unit-distance geometry.