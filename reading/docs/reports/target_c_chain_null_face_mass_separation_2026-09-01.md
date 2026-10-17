> Generated reading edition · [exact source](../../../docs/reports/target_c_chain_null_face_mass_separation_2026-09-01.md) · source SHA-256 `b10747895fd63290c7c048bddceff0c00baff785a503971dc5d5f5444d4f4303`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-BA8E17C7CBFF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C C85: chain null-face mass separation

**Date:** 2026-09-01  
**Repository base:** `55f9d1a8` (main after C84 / PR #89)  
**Run type:** exact second-order/KKT-face reduction  
**Target:** Target C C-II, C80--C84 exact chain-face branch  
**Depends on:** C54 universal PSD/null-face selection; C65 full diameter visibility; C80 chain atom; C83 interval normal form; C84 backward-endpoint classification  
**Computation:** not used

## LEVEL I STATUS

**STILL OPEN**.

C84 settles the first-order restriction of active diameter bars to the C80 chain atom:
the interval-prefix multigraph supports a nowhere-zero KKT circulation, and its
connected components give the exact restricted gradient rank. C85 attacks the
complementary second-order question when a nonzero chain-supported neutral mode does
survive.

Let `h_0=za` be the exact C80 chain diameter. C85 proves:

> If a nonzero chain-supported train-angle velocity is first-order neutral for every
> active diameter bar, then every normalized KKT stress having zero stress energy on
> that velocity has
>
> `beta_(h_0) < 1/2`.
>
> If it retains positive weight on `h_0`, then its total beta mass on C83-backward
> diameter intervals is strictly larger than `beta_(h_0)`.

C54 supplies one fixed extreme null-face stress that has zero energy on the entire
fixed-diameter critical-cone span. Therefore, whenever the C84 prefix graph is
not connected enough to kill all chain bending, that fixed extreme stress lies on the
opposite side of the exact hyperplane `beta_(h_0)=1/2` from the exposed C76 chain
stress `beta_(h_0)=1`.

This turns the secondary-stress loophole into a finite KKT-polytope separation rather
than an arbitrarily small perturbation of the chain face.

---

## 1. Chain-supported neutral space

Keep the exact C80 chain

```math
h_0=za,
\qquad
z=x_0,x_1,\ldots,x_D=a,
```

and its ordered parallel train tracks

```math
P=\{\tau_1,\ldots,\tau_D\}.
```

Put

```math
W_P
:=
\left\{
 v:\operatorname{supp}v\subseteq P,
 \quad\sum_{\tau\in P}v_\tau=0
\right\}.
\tag{C85.1}
```

The zero-sum condition removes the common co-rotation of the chain tracks, which is
the C80 kernel direction on `P`.

Let `H` be the full active diameter graph in the C65 normalization and define

```math
\boxed{
N_P:=W_P\cap\bigcap_{h\in H}\ker g_h.
}
\tag{C85.2}
```

Every `v in N_P` is a fixed-diameter critical velocity: exact train-angle variations
preserve all unit contacts to first order, and by definition every active diameter
has zero radial first variation.

C84 gives an equivalent first-order description. If `G_P` is the simple prefix graph
on `0,...,D`, then

```math
\dim N_P=c(G_P)-1.
\tag{C85.3}
```

Thus C85 concerns exactly the disconnected-prefix branch left by C84.

---

## 2. C83 second-order sign law

For every active diameter bar `h`, C83 gives one consecutive interval

```math
I_h\subseteq P
```

and one scalar

```math
c_h=\sigma_h r_h\cdot u,
\qquad
u:=\frac{a-z}{D},
```

with `u=(a-z)/D` the chain direction, such that on `N_P`

```math
\boxed{
H_h[v,v]
=-c_h\|v_{I_h}\|^2.
}
\tag{C85.4}
```

For the chain bar itself,

```math
I_{h_0}=P,
\qquad
c_{h_0}=D,
```

so C80 becomes

```math
\boxed{
H_{h_0}[v,v]=-D\|v\|^2
\qquad(v\in W_P).
}
\tag{C85.5}
```

For `h\ne h_0`, call the interval

- **forward** if `c_h>0`;
- **tangent** if `c_h=0`;
- **backward** if `c_h<0`.

On a chain-supported neutral mode, forward bars have nonpositive quadratic curvature,
tangent bars have zero quadratic curvature, and backward bars are the only positive
quadratic blockers.

C84 further proves that every backward interval belongs to a diameter edge disjoint
from `z,a` and crossing the literal chain segment `za` in its interior.

---

## 3. Every normalized KKT stress has nonpositive weighted train Hessian

Let

```math
s=(\alpha,\beta)
```

be any normalized KKT stress. C54 gives the universal signed-stress inequality

```math
\boxed{
\Omega_s=L_C(\alpha)-L_H(\beta)\succeq0.
}
\tag{C85.6}
```

Along an exact train-angle path every unit-contact length is identically one.
Differentiate the KKT virtual-work identity twice at the base configuration. The
acceleration terms cancel by first-order equilibrium, while the second derivative of
each contact squared length is zero. With `q_s(v)` denoting the C54 stress energy,
this gives

```math
\boxed{
\sum_{h\in H}\beta_h H_h[v,v]
=-q_s(v)\le0.
}
\tag{C85.7}
```

This identity is also the sign relation used in Target B's secondary-cusp theorem,
now with the later universal PSD result fixing the sign for every normalized stress.

C54.2 says that every fixed-diameter critical velocity has some extreme normalized
KKT stress with zero energy. More strongly, C54.3 gives one extreme stress

```math
s^\dagger=(\alpha^\dagger,\beta^\dagger)
```

whose stress matrix annihilates the entire span of the fixed-diameter critical cone.
Consequently

```math
\boxed{
\sum_h\beta_h^\dagger H_h[v,v]=0
\qquad(v\in N_P).
}
\tag{C85.8}
```

The theorem below applies to any normalized stress satisfying equality in C85.7 on
one nonzero `v in N_P`, and therefore in particular to `s^dagger`.

---

## 4. Backward radial coefficients are strictly sub-D

For every diameter bar,

```math
|c_h|\le |r_h|=D.
\tag{C85.9}
```

If `|c_h|=D`, the diameter segment is parallel to the chain direction `u`. A
point set of diameter `D` contains at most one diameter segment in any prescribed
unoriented direction. Indeed, if two distinct parallel diameter segments differ by a
nonzero translation `s`, then their two cross vectors are `r+s` and `r-s`, so

```math
|r+s|^2+|r-s|^2
=2D^2+2|s|^2>2D^2.
```

At least one cross-distance would exceed `D`.

The unique chain bar has `c_{h_0}=D`. Therefore every backward bar satisfies the
strict inequality

```math
\boxed{|c_h|<D.}
\tag{C85.10}
```

No uniform gap below `D` is claimed here.

---

## 5. Exact backward-mass inequality

Fix

```math
0\ne v\in N_P
```

and a normalized KKT stress `s=(alpha,beta)` such that

```math
q_s(v)=0.
\tag{C85.11}
```

Write

```math
\beta_0:=\beta_{h_0}
```

and split the non-chain diameter support into forward, tangent, and backward sets
`F,T,B` according to C83.

Equations C85.4-C85.5 and the equality case of C85.7 give

```math
0
=-\beta_0D\|v\|^2
-\sum_{h\in F}\beta_hc_h\|v_{I_h}\|^2
+\sum_{h\in B}\beta_h|c_h|\|v_{I_h}\|^2.
```

Hence

```math
\boxed{
\sum_{h\in B}\beta_h|c_h|\|v_{I_h}\|^2
=
\beta_0D\|v\|^2
+
\sum_{h\in F}\beta_hc_h\|v_{I_h}\|^2
\ge
\beta_0D\|v\|^2.
}
\tag{C85.12}
```

Let

```math
\beta_B:=\sum_{h\in B}\beta_h.
```

If `beta_0>0`, C85.12 forces at least one backward interval on which `v` is nonzero.
Using C85.10 and `\|v_{I_h}\|\le\|v\|` gives the strict upper bound

```math
\sum_{h\in B}\beta_h|c_h|\|v_{I_h}\|^2
< D\beta_B\|v\|^2.
\tag{C85.13}
```

Comparison with C85.12 yields

```math
\boxed{
\beta_B>\beta_0
\qquad\text{whenever }\beta_0>0.
}
\tag{C85.14}
```

Since the normalized diameter weights sum to one,

```math
\beta_B\le1-\beta_0.
```

Thus `beta_0<1/2` whenever `beta_0>0`; the same strict half bound is trivial if
`beta_0=0`.

### Theorem C85 — chain null-face mass separation

For every nonzero `v in N_P`, every normalized KKT stress with zero stress energy on
`v` satisfies

```math
\boxed{
\beta_{h_0}<\frac12.
}
\tag{C85.15}
```

If that stress retains the chain edge, then

```math
\boxed{
\sum_{h\in B}\beta_h>\beta_{h_0}>0.
}
\tag{C85.16}
```

In particular, if `N_P` is nonzero, the fixed extreme null-face stress `s^dagger`
from C54.3 obeys

```math
\boxed{
\beta_{h_0}^\dagger<\frac12.
}
\tag{C85.17}
```

This is an exact, dimension-free separation from the C76 chain-face stress
`beta_(h_0)=1`.

---

## 6. Coordinatewise backward coverage

For one zero-energy stress define

```math
b_j
:=
\sum_{\substack{h\in B\\\tau_j\in I_h}}
\beta_h\frac{|c_h|}{D}.
\tag{C85.18}
```

Then C85.12 is equivalent to

```math
\boxed{
\sum_{j=1}^D v_{\tau_j}^2b_j
\ge
\beta_0\sum_{j=1}^D v_{\tau_j}^2.
}
\tag{C85.19}
```

If `beta_0>0`, some chain track on which the mode moves must therefore satisfy

```math
\boxed{
b_j\ge\beta_0.}
\tag{C85.20}
```

C83 plus Target B Section 42.3 says every track in every backward interval has both
terminal boundary edges off the convex hull. Thus C85.19 converts null-face equality
into a weighted demand on the doubly non-hull part of the ordered chain atom.

---

## 7. Interaction with C84

C84 says

```math
\dim N_P=c(G_P)-1,
```

where `G_P` is the simple prefix interval graph.

Therefore the exact chain-face branch now has two disjoint structural alternatives.

### A. Connected prefix graph

If `G_P` is connected, then

```math
N_P=0.
```

C84 already forces the non-chain interval multigraph to be bridgeless and to use at
least `D+1` non-chain diameter bars, hence at least `D+2` active diameter bars
including `h_0`. The remaining problem is first-order ordered diameter-thrackle
capacity.

### B. Disconnected prefix graph

If `G_P` has at least two components, then

```math
N_P\ne0.
```

The fixed C54 null-face extreme stress then satisfies

```math
\beta_{h_0}^\dagger<1/2.
```

If it retains `h_0`, backward bars carry more total beta mass than `h_0`; every such
bar is disjoint from the chain endpoints and crosses the chain segment. The remaining
problem is a second-order KKT-polytope/response contradiction.

This is sharper than the previous single statement that a secondary stress may depend
on the chosen chain mode: one fixed extreme stress handles the entire disconnected
prefix branch.

---

## 8. Next target

The most direct continuation is to combine C85 with C66.

Every C85 backward bar is vertex-disjoint from `h_0`, so `{h_0,h}` is a diameter
matching. If the null-face stress retains nonnegligible `beta_(h_0)`, C85 forces even
more total beta mass onto such disjoint matching partners. C66 then transports any
individual heavy partner into a quantitative circular-response defect.

The unresolved issue is mass dispersion: C85 controls total backward beta mass, while
C66 is strongest on a matching of individually nonnegligible edges. A closing theorem
must either prevent the backward mass from spreading over `Theta(D)` crossing chords
or sum C66's matching inequalities efficiently over the C84 interval circulation.

The alternative connected-prefix branch remains the C84 first-order rank problem.
