> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_kkt_cycle_localization_2026-09-09.md) · source SHA-256 `03861b1e00677bde0ef1d059730b538e36d98e80f05a2a14782214dc70419f57`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-22912651186C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic `d_H=0` KKT variation localizes to the unique diameter cycle

**Date:** 2026-09-09  
**Run type:** exact KKT-polytope / incidence factorization  
**Target:** Target C C-II cyclic primitive endpoint, `d_H=0`  
**Depends on:** DC diameter/contact duality; AS antiperiodic factorization; CY universal positive cycle support  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

The AS report gives one explicit uniform interior KKT stress on the `d_H=0` Reinhardt equality shell. The full normalized KKT polytope has affine dimension two, so its boundary stresses are the remaining object.

This report shows that all stress-polytope variation is supported by the **unique odd cycle of the full diameter graph**. Every diameter branch edge is frozen positive throughout the complete KKT polytope.

Let the actual diameter edges be ordered by the DC half-turn order

$$
h_0,h_1,\ldots,h_{q-1},
$$

and let `c_t` be the contact edge produced by the transition `h_t -> h_{t+1}`. For an arbitrary normalized KKT stress write

$$
a_t:=\alpha_{c_t}>0,
\qquad
b_t:=\beta_{h_t}\ge0.
$$

If `h_t` is not on the unique diameter cycle, then

$$
\boxed{a_{t-1}=a_t,}
\tag{KL.1}
$$

and

$$
\boxed{b_t=\frac{a_t}{D^2}>0.}
\tag{KL.2}
$$

Therefore:

$$
\boxed{
\beta_h>0
\quad\text{for every diameter-tree edge }h
\text{ and every normalized KKT stress.}
}
\tag{KL.3}
$$

So every proper face of the normalized KKT polytope is cut out solely by equations

$$
\beta_h=0
$$

for diameter edges `h` belonging to the unique odd cycle of `H`.

In particular every KKT extreme point retains **all** diameter branches. Since extreme stresses delete at least two diameter coordinates in this `s_Z=2` endpoint, every extreme stress deletes at least two edges of the unique odd cycle and none outside it.

---

## 1. The full diameter graph is connected unicyclic

In `d_H=0`, CY gives

$$
h=q.
\tag{1.1}
$$

DC orders all `q` actual diameter edges cyclically so that consecutive edges share an endpoint:

$$
h_t\cap h_{t+1}\ne\varnothing
\qquad(t\in\mathbb Z/q\mathbb Z).
\tag{1.2}
$$

Because this cyclic list contains every actual diameter edge, the union of the diameter edges is connected as an abstract graph. CY also gives that every one of the `q` loaded terminals belongs to the actual diameter graph. Hence `H` is connected on `q` vertices.

Together with `|E(H)|=q`,

$$
\boxed{H\text{ is connected and unicyclic}.}
\tag{1.3}
$$

Every cycle in a planar diameter graph is odd, so the unique cycle of `H` is odd.

Let

$$
\chi\in\{-1,0,1\}^q
$$

be a signed oriented cycle vector for this unique cycle in the DC diameter-edge ordering. Then

$$
\boxed{\ker A_H^{\mathsf T}=\operatorname{span}\{\chi\},}
\tag{1.4}
$$

where `A_H` is the oriented diameter-incidence matrix used in AS.

---

## 2. Weighted AS factorization for an arbitrary KKT stress

AS proves that, after a signed permutation of the contact rows, the contact incidence matrix factors as

$$
B_C=US A_H,
\tag{2.1}
$$

where

- `U` is a signed permutation matrix;
- `S` is the antiperiodic difference operator
  $$
  (Sz)_t=z_{t+1}-z_t,
  \qquad z_q=-z_0.
  $$

Order the contact weights according to the corresponding transition rows and put

$$
D_a=\operatorname{diag}(a_0,\ldots,a_{q-1}),
\qquad
D_b=\operatorname{diag}(b_0,\ldots,b_{q-1}).
$$

The scalar stress matrix of an arbitrary KKT stress is

$$
\Omega
=B_C^{\mathsf T}D_aB_C
-A_H^{\mathsf T}D_bA_H.
$$

Using (2.1),

$$
\boxed{
\Omega
=A_H^{\mathsf T}MA_H,
\qquad
M:=S^{\mathsf T}D_aS-D_b.
}
\tag{2.2}

Let

\[
W:=A_HP
$$

be the `q x 2` matrix of oriented diameter vectors. CE gives, after one common rotation,

$$
W_t
=D\left(
\cos(\theta_0+t\theta),
\sin(\theta_0+t\theta)
\right),
\qquad
\theta=\frac\pi q.
\tag{2.3}

Equilibrium is

\[
\Omega P=0.
$$

Using (2.2),

$$
A_H^{\mathsf T}MW=0.
\tag{2.4}

By (1.4), each column of `MW` lies in the one-dimensional cycle space. Hence there is a vector

\[
\lambda\in\mathbb R^2
$$

such that

$$
\boxed{MW=\chi\lambda^{\mathsf T}.}
\tag{2.5}

This is the complete place where a nonuniform KKT stress may differ from the uniform AS stress: the middle antiperiodic defect need only vanish modulo the one-dimensional diameter cycle space.

---

## 3. Complex form of the local equilibrium equation

Identify the two coordinate columns of `W` with the complex sequence

\[
z_t:=D e^{i(\theta_0+t\theta)}.
\tag{3.1}
$$

The antiperiodic continuation satisfies

$$
z_{t+q}=-z_t.
$$

Equation (2.5) becomes

$$
\boxed{Mz=c\chi}
\tag{3.2}
$$

for one complex scalar `c`.

The `t`-th coordinate of `S^T D_a S z` is

$$
a_{t-1}(z_t-z_{t-1})
+a_t(z_t-z_{t+1}),
\tag{3.3}
$$

with the antiperiodic indexing convention at the closing edge. Dividing (3.2) by `z_t` gives

$$
a_{t-1}(1-e^{-i\theta})
+a_t(1-e^{i\theta})
-b_t
=
\frac{c\chi_t}{D}e^{-i(\theta_0+t\theta)}.
\tag{3.4}

Taking imaginary and real parts yields

\[
\boxed{
\sin\theta\,(a_{t-1}-a_t)
=
\frac{\chi_t}{D}
\operatorname{Im}
\left(c e^{-i(\theta_0+t\theta)}\right),
}
\tag{3.5}
$$

and

$$
\boxed{
(1-\cos\theta)(a_{t-1}+a_t)-b_t
=
\frac{\chi_t}{D}
\operatorname{Re}
\left(c e^{-i(\theta_0+t\theta)}\right).
}
\tag{3.6}

Equations (3.5)-(3.6) are an explicit three-real-parameter description before normalization: one additive contact level and the two real components of `c`. This matches the known unnormalized KKT stress-space dimension `s_Z+1=3`.

The periodic consistency of (3.5) is automatic. Indeed `chi` is a cycle vector, so

\[
A_H^{\mathsf T}\chi=0.
$$

Multiplying by `P` gives

$$
\chi^{\mathsf T}W=0,
$$

or in complex form

$$
\sum_t\chi_t e^{i(\theta_0+t\theta)}=0.
$$

Its conjugate is exactly the identity needed when summing (3.5) around the cycle.

---

## 4. Tree diameter edges are frozen positive

Now suppose `h_t` is not on the unique diameter cycle. Then

$$
\chi_t=0.
$$

Equation (3.5) immediately gives

$$
a_{t-1}=a_t.
$$

This proves KL.1.

Equation (3.6) then reduces to

$$
b_t
=2(1-\cos\theta)a_t.
\tag{4.1}
$$

CE gives

$$
D=\frac1{2\sin(\theta/2)},
$$

so

$$
2(1-\cos\theta)
=4\sin^2\frac\theta2
=\frac1{D^2}.
\tag{4.2}
$$

Therefore

$$
\boxed{b_t=\frac{a_t}{D^2}.}
$$

CY proves that every cycle contact coefficient is strictly positive for **every** normalized KKT stress. Thus

$$
a_t>0,
$$

and hence

$$
\boxed{b_t>0.}
$$

This proves KL.2-KL.3. `square`

---

## 5. KKT-polytope faces live only on the unique diameter cycle

CG already proves that no contact coefficient can vanish anywhere in the normalized KKT polytope. KL strengthens the remaining diameter statement:

- a diameter-tree coordinate can never vanish;
- only unique-cycle diameter coordinates can define proper faces.

Therefore:

### Theorem KL.1 — cycle-only face lattice

Every proper face of the normalized KKT polytope is induced by a set of equations

$$
\boxed{\beta_h=0\qquad(h\in E(C_H)),}
\tag{5.1}

where `C_H` is the unique odd cycle of the full actual diameter graph.

All branch edges of `H-C_H` remain strictly positive on the entire polytope.

---

## 6. Extreme stresses cut only the odd cycle

The `d_H=0` endpoint has

\[
s_Z=2.
$$

The extreme-stress sparsification theorem says every extreme normalized KKT stress has at least `s_Z=2` zero actual coordinates. CY/CG exclude contact zeros, and KL excludes diameter-tree zeros. Hence:

### Corollary KL.2

Every extreme normalized KKT stress has at least two zero `beta` coordinates, and every such zero lies on the unique odd diameter cycle.

Equivalently the selected diameter support of an extreme stress has the form

\[
\boxed{
H_s=H\setminus Z,
\qquad
Z\subseteq E(C_H),
\qquad
|Z|\ge2.
}
\tag{6.1}

All diameter branches survive every extreme-point reduction.

Since removing at least two edges from the unique cycle destroys the only cycle, every extreme selected diameter graph is a forest.

Thus:

\[
\boxed{
\text{every KKT extreme in the `d_H=0` equality class has a diameter forest support.}
}
\tag{6.2}

CG remains important here: despite the forest support, every extreme stays in the generic C56 transfer phase and its scalar stress matrix still has rank `q-3`.

---

## 7. Edge-cover restriction on the zero set

CY proves every selected diameter support covers all `q` terminals. Therefore the zero set `Z` in (6.1) cannot isolate a cycle terminal after the cycle edges are removed.

In particular, if a vertex `v` of the unique diameter cycle has no incident diameter branch outside the cycle, then the two cycle edges incident to `v` cannot both belong to `Z`.

Hence adjacent zero cycle edges are allowed only at a cycle vertex supported by at least one surviving branch edge.

This is a finite combinatorial restriction on the vertices of the two-dimensional KKT polytope.

---

## 8. Why this matters

Before KL, the `d_H=0` KKT endpoint was

```text
2-dimensional normalized stress polytope;
all q contact coefficients stay positive;
all q terminals stay selected;
extreme stresses delete at least two diameter rows.
```

KL upgrades it to

```text
full H is connected unicyclic;
all diameter-tree edges are positive in every stress;
all KKT-polytope faces come only from the unique odd diameter cycle;
every extreme stress deletes >=2 cycle edges and therefore has forest diameter support;
all branches survive every extreme stress.
```

So the remaining two-dimensional stress-family problem has been localized from `q` diameter variables to the edges of one explicit odd cycle.

---

## 9. Regression audit

- The theorem does not claim cycle-edge `beta` coefficients can all independently vanish; equations (3.5)-(3.6) couple them through only two normalized parameters.
- Extreme stresses may delete more than two cycle edges if several cycle-coordinate facets meet at one stress-polytope vertex. KL does not yet rule out such degeneracy.
- A forest selected diameter support is not the C56 zero-transfer phase. CG already proves every normalized stress, including these forest extremes, remains C56-G.
- The theorem relies on DC connectivity and CE equal direction spacing; it is not asserted for `d_H=1,2`.

---

## 10. Next theorem

The next exact target is now finite-dimensional:

> determine the affine zero lines of the cycle coefficients `beta_h` in the normalized two-parameter stress plane and classify which pairs or larger sets can vanish simultaneously.

A particularly useful outcome would be to prove that every stress-polytope vertex has exactly two zero cycle edges. Then each extreme support would be `H` with exactly two cycle edges deleted, giving a rigid finite list of forest supports that can be tested against CG maximal-rank PSD transfer and the DC curvature/degree structure.

---

## 11. Promotion recommendation

**Hold as a stacked report.**

KL is exact downstream of CE/DC/AS/CY in PR #122. It should remain separate until that shell-classification stack is independently audited.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

In cyclic d_H=0, DC orders all q diameter edges so consecutive edges share an endpoint.
Hence H is connected; h=q, so H is unicyclic with one odd cycle. Let A_H be the
oriented diameter incidence matrix and chi span ker(A_H^T).

AS gives B_C=U S A_H. For arbitrary KKT weights a_t on transition contacts and b_t
on diameter edges,
    Omega=A_H^T M A_H,
    M=S^T diag(a) S-diag(b).
Equilibrium gives MW=chi lambda^T, where W=A_HP is the regular antiperiodic diameter-vector sequence.
In complex form z_t=D exp(i(theta0+t pi/q)):
    sin(theta)(a_{t-1}-a_t)
      =(chi_t/D) Im(c exp(-i theta_t)),
    (1-cos theta)(a_{t-1}+a_t)-b_t
      =(chi_t/D) Re(c exp(-i theta_t)).

If h_t is a tree edge, chi_t=0, so
    a_{t-1}=a_t,
    b_t=2(1-cos theta)a_t=a_t/D^2>0.
Thus every diameter-tree edge is positive in every normalized stress. All KKT faces
are supported only on the unique odd diameter cycle.

Since s_Z=2, every extreme stress has at least two zero coordinates; CY excludes
contact zeros and KL excludes tree-diameter zeros. Therefore every extreme deletes
at least two unique-cycle edges, retains every branch, and has forest diameter support.
```
