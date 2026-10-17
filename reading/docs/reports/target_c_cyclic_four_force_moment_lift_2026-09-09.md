> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_four_force_moment_lift_2026-09-09.md) · source SHA-256 `fdfba237136f60dd29506080f34a2296c52e7c29c6d7ce292d56f2d9abfb6d28`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-5F160B3C541B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — four-block tree cuts satisfy an exact force-and-moment wrench relation

**Date:** 2026-09-09  
**Repository branch:** PR #118 after D2 / corrected EU  
**Run type:** exact statics refinement of the cyclic tree-phase endpoint  
**Target:** cyclic primitive phases `d_H=1,2`  
**Depends on:** D2 four-block theorem, corrected EU endpoint corner-cut theorem, central-force KKT equilibrium  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

D2 and corrected EU show that the surviving tree phases contain a four-block cut whose only KKT forces crossing the cut are four positive contact forces on the boundary cycle. The existing reports use only the vanishing of their vector resultant and obtain the reciprocal parallelogram

```math
v_i+v_k=v_j+v_\ell,
\qquad v_r=\alpha_r t_r.
```

Because every KKT bar force is central, summing equilibrium over a component also annihilates total moment. This supplies one additional exact scalar equation.

### Theorem WM — four-force wrench balance

Let the four boundary contact edges crossing a D2 component cut, or a corrected-EU zeroed-edge cut at a `d_H=1` KKT endpoint, have cyclic indices

```math
i<j<k<\ell.
```

Write

```math
t_r:=p_{r+1}-p_r,
\qquad |t_r|=1,
\qquad
m_r:=p_r\times t_r=p_r\times p_{r+1},
\tag{WM.1}
```

and define the homogeneous line/wrench vector

```math
\boxed{
L_r:=(t_{r,x},t_{r,y},m_r)^{\mathsf T}\in\mathbb R^3.}
\tag{WM.2}
```

Choose the signs so that the cut is entered across `i,k` and exited across `j,ell`. Then the endpoint/full stress satisfies

```math
\boxed{
\alpha_iL_i-\alpha_jL_j+\alpha_kL_k-\alpha_\ell L_\ell=0.}
\tag{WM.3}
```

Its first two coordinates are the existing force parallelogram. The third is the new moment identity

```math
\boxed{
\alpha_i m_i-\alpha_jm_j+\alpha_km_k-\alpha_\ell m_\ell=0.}
\tag{WM.4}
```

Consequently, whenever the four line vectors have rank three, the four transition contact coefficients are determined up to a common positive scale solely by the geometry of the four supporting side lines.

More explicitly, define

```math
\Delta_{abc}:=\det(L_a,L_b,L_c).
```

Then

```math
\boxed{
(\alpha_i,-\alpha_j,\alpha_k,-\alpha_\ell)
\propto
(-\Delta_{jk\ell},\ \Delta_{ik\ell},\ -\Delta_{ij\ell},\ \Delta_{ijk}).}
\tag{WM.5}
```

Thus the alternating sign requirement on the positive KKT weights imposes an exact sign pattern on the four triple-line determinants.

This converts the tree-phase cut from a two-equation force condition into a projective line-geometry condition that can be inserted into the weighted-cycle response formulas.

---

## 1. KKT forces are central

For a contact edge `ab`, the scalar KKT coefficient `alpha_ab>0` contributes at vertex `a`

```math
\alpha_{ab}(a-b)
```

and at vertex `b` the opposite force

```math
\alpha_{ab}(b-a).
```

For a selected diameter edge the beta force is likewise parallel to its endpoint difference, with the opposite KKT sign but still equal and opposite along one line.

Therefore every internal edge of a vertex subset contributes zero total force and zero total moment about any origin.

Indeed, for an internal edge with force `f` at `a` and `-f` at `b`, where `f` is parallel to `a-b`,

```math
a\times f+b\times(-f)
=(a-b)\times f=0.
\tag{1.1}
```

This elementary central-force cancellation is the only new mechanism needed below.

---

## 2. D2: sum force and moment over one diameter component

In the full `d_H=2` phase, D2 gives

```math
H=T_A\sqcup T_B
```

and the four cyclic blocks

```math
A_0\mid B_0\mid A_1\mid B_1.
```

No diameter edge crosses the component cut `A|B`. Exactly four cycle contact edges cross it.

Sum all vertex equilibrium equations over `A`.

- every A-internal contact force cancels with its mate;
- every A-internal diameter force cancels;
- no diameter force crosses the cut;
- the only surviving terms are the four boundary contact forces.

The vector sum gives

```math
\alpha_it_i-\alpha_jt_j+\alpha_kt_k-\alpha_\ell t_\ell=0,
\tag{2.1}
```

with signs determined by entry/exit orientation.

Now take total scalar moment about the origin. By (1.1), all internal central forces again cancel. A crossing contact on edge `r=(p_r,p_{r+1})` contributes signed moment

```math
\pm\alpha_r p_r\times t_r
=\pm\alpha_rm_r.
```

The same entry/exit signs give

```math
\alpha_im_i-\alpha_jm_j+\alpha_km_k-\alpha_\ell m_\ell=0.
\tag{2.2}
```

Combining (2.1)-(2.2) is exactly WM.3.

---

## 3. Corrected EU: the same proof works at a `d_H=1` endpoint

Let `H` be the full spanning diameter tree and let `e` be a zeroed nonleaf full-tree edge at a KKT endpoint. Corrected EU gives the full-tree cut

```math
H-e=T_A\sqcup T_B
```

with four alternating color blocks.

The edge `e` is the only **full** diameter edge crossing the cut and has selected coefficient

```math
\beta_e=0.
```

Any additional beta coordinates which vanish at the endpoint lie inside one of the full-tree components. Hence no selected positive diameter force crosses the `A|B` cut.

The same force and moment summation over `A` therefore gives WM.3 exactly. No selected-support equality and no endpoint mixed-rigidity rank are needed.

Thus WM is compatible with the correction made to EU.

---

## 4. Homogeneous line coordinates

The vector

```math
L_r=(t_{r,x},t_{r,y},p_r\times t_r)
```

encodes the oriented supporting line of the unit side `p_rp_{r+1}` up to an invertible linear change of the standard projective line coordinates.

Indeed, with

```math
n_r:=(-t_{r,y},t_{r,x}),
```

the side line has equation

```math
n_r\cdot x=m_r.
```

Thus the standard homogeneous line coordinate is

```math
(-t_{r,y},t_{r,x},-m_r),
```

which is obtained from `L_r` by a fixed nonsingular linear transformation.

Consequently

```math
\det(L_a,L_b,L_c)=0
```

if and only if the three corresponding side lines are concurrent in the projective plane, including the usual point at infinity for parallel lines.

So rank three of the four `L_r` means the transition side lines are not all contained in a projective pencil.

---

## 5. Cofactor formula for the contact-weight ratios

Let

```math
\mathcal L=[L_i\ L_j\ L_k\ L_\ell]
```

be the `3 x 4` line-coordinate matrix. WM.3 says

```math
\mathcal L
\begin{pmatrix}
\alpha_i\\-\alpha_j\\\alpha_k\\-\alpha_\ell
\end{pmatrix}=0.
\tag{5.1}
```

If `rank mathcal L=3`, its nullspace is one-dimensional. The standard alternating-cofactor null vector of a `3 x 4` matrix is

```math
\begin{pmatrix}
-\det(L_j,L_k,L_\ell)\\
\det(L_i,L_k,L_\ell)\\
-\det(L_i,L_j,L_\ell)\\
\det(L_i,L_j,L_k)
\end{pmatrix}.
\tag{5.2}
```

Hence (5.1) gives WM.5.

Because every `alpha_r` is positive in the cyclic source, the four cofactors must have the alternating sign pattern compatible with (5.2). This is an exact projective restriction on the transition side lines.

---

## 6. Resistance ratios at the four transitions

The weighted contact network is the cycle with edge resistances

```math
r_r:=\frac1{\alpha_r}.
```

When `rank mathcal L=3`, WM.5 determines the four transition resistances up to a common reciprocal scale:

```math
\boxed{
(r_i,r_j,r_k,r_\ell)
\propto
\left(
\frac1{|\Delta_{jk\ell}|},
\frac1{|\Delta_{ik\ell}|},
\frac1{|\Delta_{ij\ell}|},
\frac1{|\Delta_{ijk}|}
\right),}
\tag{6.1}
```

with the determinant signs fixed by KKT positivity.

WT expresses every transfer coefficient between crossing selected diameter chords in terms of sums of these cycle resistances over the four intervening boundary arcs. WM therefore supplies exact endpoint data for four distinguished edges of those arc sums.

This does not yet determine the whole arc sums, because the internal cycle resistances remain free. The gain is that the endpoint values are no longer arbitrary KKT variables.

---

## 7. Degenerate line-pencil case

If `rank mathcal L<=2`, all four transition side lines lie in one projective pencil. For a strictly convex polygon this is a rigid geometric degeneracy: either

1. several transition sides are parallel, or
2. their supporting lines pass through one common exterior point.

WM remains valid, but the contact-weight ratios are not uniquely determined by the four lines alone.

No claim is made here that the pencil case is impossible. It should be treated as a separate geometric branch in any WT-based closure.

A useful next sublemma would be to show that RP's near-Reinhardt shell geometry excludes a four-transition pencil except in a symmetric configuration which can be analyzed explicitly.

---

## 8. Regression audit

### Reciprocal parallelogram alone

Recovered as the first two coordinates of WM.3.

### Four concurrent supporting lines

Allowed by this theorem and correctly placed in the rank-deficient branch. No genericity is silently assumed.

### Additional zero beta coordinates at a `d_H=1` endpoint

Allowed. They are internal to the two full-tree components of the chosen zeroed edge and their central forces cancel in the component sum.

### Choice of origin

WM.4 is origin-independent once the force resultant vanishes. Translating the origin by `a` changes the total moment by

```math
a\times\sum F=0.
```

### D2 full stress

All diameter rows are positive, but none crosses the component cut, so WM applies directly.

---

## 9. What this changes

The tree-phase endpoint is now constrained at three levels:

1. **cyclic topology:** four alternating blocks from D2 / corrected EU;
2. **force balance:** transition reciprocal parallelogram;
3. **moment balance:** the four side-line wrenches have one positive alternating projective dependence.

In the generic rank-three branch, the four transition contact weights are a deterministic function of the shell geometry up to one global scale.

This is the first exact reduction tying the KKT contact weights at the four-block interfaces directly to the primal side-line geometry.

---

## 10. Next theorem

The highest-value continuation is now concrete.

### WM-WT

For each tree phase, write the four WT cyclic resistance arc sums `A,B,C,D` associated to selected crossing diameter chords. Use WM.6.1 to substitute the four transition edge resistances into those sums, then combine

```math
K_{ef}=\frac{BD-AC}{A+B+C+D}
```

with C56-G's strict Robinson ordering.

The aim is to show that either

1. the required determinant sign pattern fails for the four transition side lines, or
2. the WT numerator is forced to an equality/sign inconsistent with the single irreducible C56-G block.

The projective-pencil branch should be isolated and checked separately.

---

## 11. Promotion recommendation

**Hold as report pending independent audit.**

WM is elementary downstream of D2/corrected-EU. It introduces no new external theorem.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For a D2 component cut, or a corrected-EU zeroed-edge cut at a d_H=1 endpoint, no
selected diameter force crosses the cut and exactly four cycle contacts do. Internal
KKT forces are central, so summing over one side kills both total force and total moment.

With t_r=p_{r+1}-p_r, m_r=p_r x t_r, L_r=(t_rx,t_ry,m_r):
  alpha_i L_i-alpha_j L_j+alpha_k L_k-alpha_l L_l=0.
First two coordinates recover the reciprocal parallelogram. Third coordinate is new:
  alpha_i m_i-alpha_j m_j+alpha_k m_k-alpha_l m_l=0.

If rank[L_i L_j L_k L_l]=3, then
  (alpha_i,-alpha_j,alpha_k,-alpha_l)
    proportional to
  (-det L_jkl, det L_ikl, -det L_ijl, det L_ijk).
Thus the four transition alpha ratios, hence their resistance ratios, are fixed by the
four supporting side lines. Positivity imposes the corresponding alternating determinant
sign pattern.

Next: insert these four resistance values into WT arc sums and C56-G Robinson ordering.
```
