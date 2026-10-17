> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_reinhardt_uniform_stress_2026-09-09.md) · source SHA-256 `29c13a976dc3e893b7142ae683a84d9fe3e8c2eec57c982bcd8baf3b21e0fede`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-76EF7DDB27BF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact Reinhardt shell has a canonical uniform KKT stress

**Date:** 2026-09-09  
**Repository branch:** PR #118 after RE  
**Run type:** exact KKT construction / spectral reduction  
**Target:** cyclic primitive endpoint, `d_H=0`  
**Depends on:** RE exact Reinhardt collapse, CY/CG selected-stress framework  
**External literature:** not used in the proof  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

RE proves that the cyclic `d_H=0` phase lies exactly on the Reinhardt equality locus:

```math
\delta:=\frac\pi q,
\qquad
D=\frac1{2\sin(\delta/2)},
```

all projective diameter directions are separated by exactly `delta`, and every local normal cone is packed without angular slack.

That equality geometry determines one normalized KKT stress explicitly.

### Theorem US — uniform full-support stress

For every exact `d_H=0` cyclic survivor, the coefficients

```math
\boxed{
\beta_h=\frac1q
\quad(h\in H),
\qquad
\alpha_e=\frac{D^2}{q}
\quad(e\in C_q)}
\tag{US.1}
```

satisfy KKT equilibrium at every loaded vertex. In particular they define a strictly positive normalized full-support stress.

Equivalently, if `L_C` is the unweighted Laplacian of the boundary contact cycle and `L_H` the unweighted Laplacian of the full diameter graph, then the corresponding scalar stress matrix is

```math
\boxed{
\Omega_{\rm unif}
=\frac1q\left(D^2L_C-L_H\right).}
\tag{US.2}
```

By CY/CG this stress is PSD and maximal-rank:

```math
\boxed{
D^2L_C-L_H\succeq0,}
\tag{US.3}
```

```math
\boxed{
\ker(D^2L_C-L_H)
=\operatorname{span}\{\mathbf1,P_x,P_y\},
\qquad
\operatorname{rank}(D^2L_C-L_H)=q-3.}
\tag{US.4}
```

Thus the exact Reinhardt endpoint contains a canonical stress with completely uniform contact and diameter weights. This is a strong warning against trying to exclude the branch from KKT positivity alone.

---

## 1. Exact local packing from RE

Fix a loaded vertex `b` and write

```math
d:=\deg_H(b)\ge1.
```

RE gives the exact exterior angle

```math
\boxed{\theta_b=d\delta.}
\tag{1.1}
```

The pre-RE local diameter theorem gives three nonnegative angular costs inside the normal cone at `b`:

1. clearance at least `delta/2` from the first cone boundary;
2. separation at least `delta` between consecutive incident diameter directions;
3. clearance at least `delta/2` from the second cone boundary.

For `d` incident diameter rays their mandatory total width is therefore

```math
\frac\delta2+(d-1)\delta+\frac\delta2=d\delta.
```

Equation (1.1) says the available cone width is exactly the same number. Hence every local angular inequality is equality.

### Lemma US.1 — exact local fan

The `d` unit diameter directions

```math
n_j:=\frac{b-k_j}{D}
```

are symmetrically placed about the outward normal-cone bisector with offsets

```math
\left(j-\frac{d+1}{2}\right)\delta,
\qquad 1\le j\le d.
\tag{1.2}
```

Equivalently, the extreme rays have boundary clearance exactly `delta/2` and every internal gap is exactly `delta`.

---

## 2. Sum of the diameter fan

Let `n_b` denote the unit vector along the outward bisector of the normal cone at `b`. By the elementary finite geometric-series identity,

```math
\sum_{j=1}^d n_j
=
\frac{\sin(d\delta/2)}{\sin(\delta/2)}\,n_b.
\tag{2.1}
```

Therefore equal diameter coefficients `B>0` contribute the vector

```math
\boxed{
B\sum_{bk\in H}(b-k)
=
BD\,
\frac{\sin(d\delta/2)}{\sin(\delta/2)}\,n_b.}
\tag{2.2}
```

No global information about the degree sequence is needed: only the exact local fan matters.

---

## 3. Equal cycle-contact coefficients have the same direction

Let `t_-` be the incoming unit boundary-side vector ending at `b` and `t_+` the outgoing unit side vector starting at `b`. Their oriented turning angle is the exterior angle

```math
\theta_b=d\delta.
```

The two contact contributions at `b` with a common coefficient `A>0` are

```math
A(b-p_-)+A(b-p_+)
=A(t_- - t_+).
\tag{3.1}
```

Because `t_-` and `t_+` are unit vectors separated by turning angle `d delta`, their difference lies on the same outward bisector `n_b` and has magnitude

```math
|t_- - t_+|
=2\sin(d\delta/2).
```

Thus

```math
\boxed{
A(t_- - t_+)
=2A\sin(d\delta/2)\,n_b.}
\tag{3.2}
```

The orientation of `n_b` is chosen so both (2.2) and (3.2) point in the same KKT-equilibrium direction.

---

## 4. The degree cancels

KKT equilibrium at `b` asks for equality of (2.2) and (3.2):

```math
2A\sin(d\delta/2)
=BD\frac{\sin(d\delta/2)}{\sin(\delta/2)}.
```

Since `1<=d<q` in a strictly convex finite shell,

```math
\sin(d\delta/2)>0,
```

so it cancels. We obtain

```math
2A
=\frac{BD}{\sin(\delta/2)}.
\tag{4.1}
```

RE gives

```math
D=\frac1{2\sin(\delta/2)},
```

hence

```math
\frac{D}{\sin(\delta/2)}=2D^2.
```

Equation (4.1) is therefore simply

```math
\boxed{A=BD^2.}
\tag{4.2}
```

This relation is independent of `d`. Thus the same pair of constants balances every vertex, no matter how many leaves are attached to a diameter-cycle vertex.

In the `d_H=0` phase,

```math
|H|=q.
```

Normalize by

```math
\sum_{h\in H}\beta_h=1.
```

Choosing

```math
B=1/q
```

and then (4.2) gives

```math
A=D^2/q.
```

This proves US.1. `square`

---

## 5. Exact Laplacian domination

For scalar coordinates, a contact edge of coefficient `alpha` contributes `+alpha L_e` and a diameter edge of coefficient `beta` contributes `-beta L_h` to the signed stress matrix. Substituting US.1 gives

```math
\Omega_{\rm unif}
=\frac{D^2}{q}L_C-\frac1qL_H,
```

which is US.2.

CY/CG prove that every normalized KKT stress in the cyclic endpoint is PSD with exact affine kernel. Applying that theorem to the explicit uniform stress yields US.3-US.4.

Equivalently, on the zero-sum space,

```math
\boxed{
L_H\preceq D^2L_C.}
\tag{5.1}
```

The generalized eigenvalue `D^2` of the pair `(L_H,L_C)` has multiplicity exactly two, represented by the two coordinate functions:

```math
\boxed{
L_HP_x=D^2L_CP_x,
\qquad
L_HP_y=D^2L_CP_y.}
\tag{5.2}
```

All other nonconstant generalized eigenvalues are strictly smaller than `D^2`.

This turns the remaining exact Reinhardt/KKT problem into a spectral graph-embedding problem on the pair

```math
(C_q,H).
```

---

## 6. Leaf consequence

If `b` is a leaf of the full diameter graph, then `d=1`. The unique incident diameter direction is exactly the normal-cone bisector.

For an arbitrary normalized stress `s`, LF keeps the unique leaf diameter coefficient positive. Equilibrium at `b` then forces the two adjacent contact-force coefficients to be equal, because the two unit contact directions are linearly independent and their resultant lies on their angle bisector only when their coefficients agree.

Thus:

### Corollary US.2 — contact stress is constant through diameter leaves

If the boundary cycle edges adjacent to a full-H leaf `b` are `e_-` and `e_+`, then for every normalized KKT stress

```math
\boxed{\alpha_{e_-}(s)=\alpha_{e_+}(s).}
\tag{6.1}
```

By the Reinhardt equality classification, the full diameter graph is an odd cycle with degree-one vertices attached to its cycle vertices. Hence `alpha` is constant along every boundary run whose internal vertices are diameter leaves.

This reduces all contact-weight freedom to the boundary positions of the odd diameter-cycle vertices.

---

## 7. Regression audit

### Regular odd shell

Here every diameter degree is two. The theorem gives uniform `alpha` and `beta`, exactly the rotationally symmetric stress. Direct finite-dimensional solves for `q=5,7,9,11` also show that this uniform point lies in the interior of the expected two-dimensional stress polygon; those computations are regression evidence only and are not used in the proof.

### Nonregular Reinhardt polygon

The proof does not assume regularity. High-degree diameter-cycle vertices and leaf vertices are both handled by the same cancellation (4.2).

### KKT-sign exclusion

US explicitly disproves any proposed route claiming that a nonregular exact Reinhardt shell cannot have a strictly positive full-support equilibrium stress merely because its diameter degrees are nonuniform. The equality geometry itself supplies one.

---

## 8. What this changes

RE converted the `d_H=0` source into an exact Reinhardt equality problem. US shows that this equality family is also mechanically self-consistent at the most basic KKT level:

```math
\alpha\equiv D^2/q,
\qquad
\beta\equiv1/q.
```

Therefore the next attack cannot be just

- positivity of KKT coefficients;
- local force balance;
- maximal scalar rank in isolation.

The useful new structure is instead the exact Loewner equality

```math
L_H\preceq D^2L_C
```

with a two-dimensional top generalized eigenspace generated by the Euclidean coordinates, plus the leaf-run constancy (6.1).

A closing theorem must exploit this global spectral/graph structure or return to the quadratic source population outside the `O(D)` force shell.

---

## 9. Next theorem

Two concrete targets remain.

### US-A — generalized spectral rigidity

Classify convex-thrackle unicyclic graphs `H` on the cyclically ordered vertices of `C_q` for which

```math
L_H\preceq D_q^2L_{C_q},
\qquad
D_q=\frac1{2\sin(\pi/(2q))},
```

has top nonconstant generalized eigenspace of dimension exactly two and admits a convex unit-side embedding realizing that eigenspace.

If only the regular odd-star diameter cycle survives, the exact Reinhardt family collapses drastically.

### US-B — leaf-block stress reduction

Use (6.1) to contract the contact-weight variables across every diameter-leaf run. Express the two-dimensional KKT polytope using only the odd-cycle core vertices of the Reinhardt diameter graph and test its C56-G inequalities exactly.

---

## 10. Promotion recommendation

**Hold as report pending independent audit.**

The equilibrium calculation is exact downstream of RE. The PSD/maximal-rank corollary uses report-level CY/CG.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

RE d_H=0 geometry:
  delta=pi/q,
  D=1/(2sin(delta/2)),
  theta_b=deg_H(b) delta,
  every local diameter fan fills the normal cone with boundary gaps delta/2
  and internal gaps delta.

At a vertex of diameter degree d:
  sum of its d unit diameter directions
    = [sin(d delta/2)/sin(delta/2)] n_b.
Equal contact coefficient A gives resultant
    2A sin(d delta/2) n_b.
Equal diameter coefficient B gives resultant
    BD sin(d delta/2)/sin(delta/2) n_b.
Since D=1/(2sin(delta/2)), equilibrium is exactly
    A=B D^2,
independent of d.
Normalize sum beta=1 over h=q edges:
    beta_h=1/q,
    alpha_e=D^2/q.

Hence
    Omega_unif=(D^2 L_C-L_H)/q,
and CY/CG give
    D^2 L_C-L_H >=0,
    ker=span{1,P_x,P_y}, rank=q-3.
So D^2 is the top generalized eigenvalue of (L_H,L_C), multiplicity exactly 2.

At every full-H leaf, arbitrary selected-stress equilibrium also forces the two
adjacent cycle contact coefficients equal. Contact-stress variation therefore only
occurs at the odd diameter-cycle core vertices.

Next: classify the spectral pair (C_q,H), or contract leaf runs and solve the
core KKT polytope exactly.
```
