> Generated reading edition · [exact source](../../../docs/reports/target_c_stress_star_radialization_2026-08-31.md) · source SHA-256 `76c704c0ee72fb237e20e350c7fd5ea54162fc8ca84dff9cf065867cabd95ae2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-C6E7729FAB7D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C68: stress-star concentration forces radial contact stress

**Date:** 2026-08-31  
**Repository base:** `baa9486c` (main after C67 / PR #70)  
**Run type:** exact PSD-energy theorem / stress-star stability reduction  
**Target:** Target C Gate C-II  
**Depends on:** C11 stress-tensor identity, C53 full selected-support PSD, C64/C66 response defect, C65 full diameter visibility, C67 force-hull area floor  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN.**

C66 shows that a response defect `epsilon=o(1/D)` forces almost all normalized diameter stress onto one star centered at a diameter vertex `z`. C68 converts that statement into a mechanical geometric conclusion on the **actual unit-contact stress**.

Let

```math
r_i:=|p_i-z|.
```

Then the scalar PSD inequality for the radial function gives

```math
\sum_{ij\in C}\alpha_{ij}(r_i-r_j)^2
\ge
\sum_{ij\in H}\beta_{ij}(r_i-r_j)^2.
```

Every contact has length one, so `|r_i-r_j|<=1`. Since the normalized contact stress has total mass `D^2`, the contact radial energy is at most `D^2`. Every diameter edge incident to `z` contributes exactly `D^2 beta_e` to the diameter radial energy.

If

```math
S_z:=\sum_{e\ni z}\beta_e,
```

then the exact radial-defect inequality is

```math
\boxed{
Q_z+
\sum_{\substack{ij\in H\\z\notin\{i,j\}}}
\beta_{ij}(r_i-r_j)^2
\le
D^2(1-S_z),
}
```

where

```math
Q_z:=
\sum_{ij\in C}\alpha_{ij}
\left[1-(r_i-r_j)^2\right].
```

Moreover each unit contact has the exact polar formula

```math
1-(r_i-r_j)^2
=4r_ir_j\sin^2\frac{\theta_{ij}}2,
```

where `theta_ij` is the angle at `z` between the two endpoint rays. Thus `Q_z` is a weighted angular/transverse stress energy.

Combining with C66 gives

```math
\boxed{
Q_z\le C_0D^3\varepsilon,
\qquad
C_0=\frac{2\pi}{\kappa_0}.
}
```

Hence `D epsilon ->0` forces `Q_z=o(D^2)`: asymptotically all contact-stress mass lies on unit edges that make almost the maximum possible radial progress from the star center.

This is the missing source-level strengthening of the abstract near-star electrical regression. It does not yet give a uniform lower bound on `Q_z`; tiny positive stresses can still carry the geometrically two-dimensional low-weight part of the framework.

---

## 1. Full PSD inequality on scalar vertex functions

By C53, for the relative-interior fully visible KKT stress,

```math
\Omega:=L_C(\alpha)-L_H(\beta)\succeq0.
\tag{C68.1}
```

Therefore every real scalar function `f` on the force-visible contact vertices satisfies

```math
\boxed{
\sum_{ij\in C}\alpha_{ij}(f_i-f_j)^2
\ge
\sum_{ij\in H}\beta_{ij}(f_i-f_j)^2.
}
\tag{C68.2}
```

C11 gives the exact stress-tensor identity

```math
\sum_{ij\in C}\alpha_{ij}(p_i-p_j)(p_i-p_j)^T
=
\sum_{ij\in H}\beta_{ij}(p_i-p_j)(p_i-p_j)^T.
```

Taking traces and using `|p_i-p_j|=1` on contacts, `|p_i-p_j|=D` on diameter edges, and `sum_H beta=1`,

```math
\boxed{
\sum_{ij\in C}\alpha_{ij}=D^2.
}
\tag{C68.3}
```

---

## 2. Radial test function about a diameter vertex

Fix a diameter vertex `z` and define

```math
r_i=|p_i-p_z|.
\tag{C68.4}
```

For every contact `ij`, the reverse triangle inequality gives

```math
|r_i-r_j|\le|p_i-p_j|=1.
\tag{C68.5}
```

Consequently

```math
E_C(r):=
\sum_{ij\in C}\alpha_{ij}(r_i-r_j)^2
\le
\sum_{ij\in C}\alpha_{ij}
=D^2.
\tag{C68.6}
```

Apply C68.2 to `r`:

```math
E_C(r)\ge E_H(r),
\qquad
E_H(r):=
\sum_{ij\in H}\beta_{ij}(r_i-r_j)^2.
\tag{C68.7}
```

Let

```math
S_z:=\sum_{zk\in H}\beta_{zk}.
\tag{C68.8}
```

For every diameter edge `zk`,

```math
r_z=0,
\qquad
r_k=D,
```

so its radial-energy contribution is exactly `D^2 beta_zk`. Therefore

```math
E_H(r)
=
D^2S_z
+
\sum_{\substack{ij\in H\\z\notin\{i,j\}}}
\beta_{ij}(r_i-r_j)^2.
\tag{C68.9}
```

Define the contact radial defect

```math
Q_z:=D^2-E_C(r).
\tag{C68.10}
```

By C68.5 and positivity of every contact stress,

```math
Q_z
=
\sum_{ij\in C}\alpha_{ij}
\left[1-(r_i-r_j)^2\right]
\ge0.
\tag{C68.11}
```

Using `E_H(r)<=E_C(r)=D^2-Q_z` in C68.9 gives the main inequality.

### Theorem C68.1 — radial-defect domination

For every diameter vertex `z`,

```math
\boxed{
Q_z+
\sum_{\substack{ij\in H\\z\notin\{i,j\}}}
\beta_{ij}(r_i-r_j)^2
\le
D^2(1-S_z).
}
\tag{C68.12}
```

In particular

```math
\boxed{Q_z\le D^2(1-S_z).}
\tag{C68.13}
```

No response-matrix estimate is used in this step beyond the already promoted full PSD theorem C53.

---

## 3. Exact angular interpretation

Take one unit contact `ij`. Let

```math
r_i=|p_i-z|,
\qquad
r_j=|p_j-z|,
```

and let `theta_ij in [0,pi]` be the angle between the rays `z p_i` and `z p_j` when both radii are nonzero. The cosine law gives

```math
1=r_i^2+r_j^2-2r_ir_j\cos\theta_{ij}.
```

Subtract `(r_i-r_j)^2=r_i^2+r_j^2-2r_ir_j`:

```math
\boxed{
1-(r_i-r_j)^2
=2r_ir_j(1-\cos\theta_{ij})
=4r_ir_j\sin^2\frac{\theta_{ij}}2.
}
\tag{C68.14}
```

The same identity is valid when one endpoint is `z`, because both sides are then zero.

Hence

```math
\boxed{
Q_z
=4\sum_{ij\in C}
\alpha_{ij}r_ir_j
\sin^2\frac{\theta_{ij}}2.
}
\tag{C68.15}
```

Thus `Q_z` measures exactly the contact stress spent on angular motion rather than unit radial progress away from `z`.

### Corollary C68.2 — stress on inefficient radial edges

Fix `eta in (0,1]` and let

```math
C_{z,\eta}:=
\{ij\in C:|r_i-r_j|\le1-\eta\}.
```

Every edge in this set contributes at least

```math
1-(1-\eta)^2=\eta(2-\eta)
```

to the bracket in C68.11. Therefore

```math
\boxed{
\sum_{ij\in C_{z,\eta}}\alpha_{ij}
\le
\frac{Q_z}{\eta(2-\eta)}.
}
\tag{C68.16}
```

So small `Q_z/D^2` means that a correspondingly small fraction of the total contact stress can sit on edges that fail to make near-unit radial progress.

---

## 4. Insert C66 stress-star concentration

C66 supplies constants

```math
\gamma_0>0,
\qquad
\kappa_0=\frac{2\gamma_0}{1+2\gamma_0},
\qquad
C_0=\frac{2\pi}{\kappa_0},
```

and a diameter vertex `z` such that

```math
S_z\ge1-C_0D\varepsilon,
\tag{C68.17}
```

where

```math
\varepsilon=rac12\operatorname{tr}(\Lambda-L_H).
```

Substitute C68.17 into C68.12.

### Theorem C68.3 — near-zero response defect radializes the mechanical stress

For the C66 star center `z`,

```math
\boxed{
Q_z+
\sum_{\substack{ij\in H\\z\notin\{i,j\}}}
\beta_{ij}(r_i-r_j)^2
\le
C_0D^3\varepsilon.
}
\tag{C68.18}
```

In particular

```math
\boxed{Q_z\le C_0D^3\varepsilon.}
\tag{C68.19}
```

If

```math
D\varepsilon\longrightarrow0,
```

then

```math
\boxed{Q_z=o(D^2).}
\tag{C68.20}
```

For every fixed `eta>0`, C68.16 then yields

```math
\sum_{ij\in C_{z,\eta}}\alpha_{ij}=o(D^2).
\tag{C68.21}
```

Thus almost all normalized contact-stress mass is carried by unit contacts satisfying

```math
|r_i-r_j|=1-o(1)
```

in stress measure.

---

## 5. Exact zero-defect classification

C68 also identifies the exact endpoint of this radialization.

Suppose

```math
Q_z=0.
```

Because every `alpha_ij>0` and every summand in C68.11 is nonnegative,

```math
|r_i-r_j|=1
\qquad(ij\in C).
\tag{C68.22}
```

For a unit segment, equality in the reverse triangle inequality holds exactly when `z,p_i,p_j` are collinear and `p_i,p_j` lie on the same ray from `z` (with the edge incident to `z` allowed as the initial segment).

The positive contact graph is connected. Starting at `z`, every contact path therefore remains on the ray determined by its first edge from `z`. Hence the whole force-visible contact core lies in the union of at most

```math
\deg_C(z)\le3
```

rays, using the C-II terminal contact-degree bound.

On each ray only its farthest core vertex can be an extreme point of the force hull. Therefore

```math
|B|\le1+\deg_C(z)\le4.
\tag{C68.23}
```

But C34 gives

```math
2|B|\ge\lceil D\rceil+2,
```

which contradicts C68.23 for all sufficiently large `D`.

### Corollary C68.4 — exact radial equality is impossible

For sufficiently large C-II minimizers,

```math
\boxed{Q_z>0\quad\text{for every diameter vertex }z.}
\tag{C68.24}
```

This is qualitative only. The current theorem does not provide a uniform positive lower bound for `Q_z/D^2`.

---

## 6. Interaction with C67 and the remaining obstruction

C67 gives

```math
\operatorname{area}(F)
\ge
(0.1237019796-o(1))D^2.
```

Therefore the geometry supporting C68.20 remains genuinely two-dimensional even though almost all **stress mass** becomes radial around `z`.

This sharply identifies the remaining regression:

```text
large two-dimensional unit-contact framework
+ all contacts positive
+ almost all alpha-mass on near-radial chains from z
+ geometrically essential off-ray branches carrying arbitrarily small positive stress
+ Omega(D) actual diameter directions, but almost all beta-mass on the z-star.
```

A rectangular/rhombic mesh with one heavily weighted track and many very lightly weighted transverse tracks shows why C67 alone cannot exclude that weighted anisotropy. The next theorem must use either:

1. rhombic/train-track propagation to charge geometrically essential low-stress branches;
2. a quantitative consequence of contact minimality/global diameter optimality forbidding arbitrarily small branch stresses; or
3. a new response inequality that converts the radial angular energy `Q_z` directly into `Omega(D^2)` or at least `Omega(D)` under the C67 two-dimensionality and C34 endpoint count.

## Compact handoff

**C68.1:** for every diameter vertex `z`,

`Q_z + nonstar diameter radial energy <= D^2(1-S_z)`.

**C68.2:**

`Q_z = 4 sum_C alpha_ij r_i r_j sin^2(theta_ij/2)`.

**C68.3:** at the C66 star center,

`Q_z <= C_0 D^3 epsilon`.

Thus `D epsilon ->0` forces `Q_z=o(D^2)` and almost all contact stress onto near-unit radial-progress edges.

**C68.4:** exact `Q_z=0` would put the entire connected core on at most three rays and hence give `|B|<=4`, contradicting C34 for large `D`.

**Next:** prove a quantitative lower bound on `Q_z` from the combination of C67 two-dimensional force hull, C42 near-quadrangulation, and positive-stress train-track propagation.
