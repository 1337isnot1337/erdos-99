> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_d1_signed_closure_2026-09-09.md) · source SHA-256 `174de996210a390786b3981f32c3b4759f1ed4c7a9f17504a259a01a6c55ea2f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BFBE2E32790D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdos Problem #99 — exact signed closure equations for the cyclic `d_H=1` one-defect shell

**Date:** 2026-09-09  
**Repository branch:** PR #118 after D1/AC/CS  
**Run type:** exact Minkowski sign-code reconstruction  
**Target:** cyclic primitive phase `d_H=1`  
**Depends on:** D1 exact difference-body normal form, AC local endpoint-switch theorem, elementary Minkowski edge merge  
**External literature:** none used in the proof; the resulting sign word is the same object that becomes a Reinhardt dihedral composition in the zero-defect limit  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

D1 reduces the complete `d_H=1` difference body to a one-parameter defect. The remaining reconstruction problem is to decide whether that centrally symmetric difference body can actually be written as

$$
K=F-F
$$

for a closed convex equilateral `q`-gon `F` with the Target C antipodal graph.

Because the S1 difference body has no merged edge directions, this reconstruction has an exact binary sign code. AC fixes the two signs adjacent to the unique short antipodal state to be opposite. The full primal closure therefore reduces to two scalar trigonometric equations, one of which is independent of the nonlinear short-edge angle.

At the P1 endpoint the same equation collapses further to a unit-circle zero of a Littlewood polynomial.

---

## 1. Half-boundary sign code for `K=F-F`

First consider S1, so `F` has no parallel side pair and `K=F-F` has exactly `2q` unit edges.

The oriented edge-direction list of `K=F+(-F)` is the strict cyclic merge of

1. the `q` oriented unit side vectors of `F`, and
2. their negatives, which are the oriented side vectors of `-F`.

Choose any projective half of the boundary of `K`. It contains exactly `q` unit edge vectors

$$
w_0,\ldots,w_{q-1},
\qquad |w_j|=1,
$$

one from each antipodal pair `{t,-t}` coming from a side vector `t` of `F`.

Hence there is a unique sign word

$$
\varepsilon_j\in\{+1,-1\}
$$

such that the `q` primal side vectors of `F` are exactly

$$
\varepsilon_0w_0,\ldots,\varepsilon_{q-1}w_{q-1}.
$$

Since `F` closes,

$$
\boxed{
\sum_{j=0}^{q-1}\varepsilon_jw_j=0.
}
\tag{SC.1}
$$

Conversely, for the fixed strict edge-direction merge, SC.1 is the vector closure condition for the chosen signed unit sides.

---

## 2. Sign changes are the odd-cycle states of the antipodal graph

Let `x_j` be the difference-body vertex between the full-boundary edges `w_{j-1}` and `w_j`. It represents one unordered vertex-vertex antipodal pair of `F`.

Crossing a `+` edge changes the maximizing support vertex of the represented pair; crossing a `-` edge changes the minimizing support vertex. Therefore:

- if the two incident signs at an antipodal state are equal, both neighboring antipodal states share the same endpoint with the current chord, leaving the other endpoint as a leaf in the complete antipodal graph;
- if the two incident signs differ, the two neighboring antipodal states continue through opposite endpoints of the current chord, so both endpoints have antipodal degree at least two.

AC identifies the complete antipodal graph as a maximal convex thrackle, hence as one odd cycle plus direct leaves. Thus an antipodal chord lies on the unique odd cycle exactly when its incident full-boundary signs differ.

On a projective half-word the seam has the central-symmetry sign reversal: the edge immediately before `w_0` on the full boundary is the antipode of `w_{q-1}` and therefore carries sign `-epsilon_{q-1}`. Consequently the odd-cycle length is

$$
\boxed{
\nu
=
\#\{0\le j\le q-2:\varepsilon_j\ne\varepsilon_{j+1}\}
+
\mathbf1_{\{\varepsilon_{q-1}=\varepsilon_0\}}.
}
\tag{SC.2}
$$

The right side is automatically odd. The run lengths of the sign word are therefore exactly the dihedral-composition data of the maximal antipodal cycle, up to the projective seam convention.

In particular AC says the unique short S1 antipodal chord is a cycle edge, so if it is placed at the state between `w_0,w_1`, then

$$
\boxed{
\varepsilon_0=-\varepsilon_1.
}
\tag{SC.3}

---

## 3. Exact S1 edge directions

Use D1 notation

\[
\delta=2\arcsin\frac1{2D},
\qquad
q_R=\frac\pi\delta,
\qquad
s=q_R-q,
$$

and let the unique short difference-body vertex have circular neighbors separated by

$$
G=(s+2)\delta.
\tag{3.1}
$$

Put

$$
\eta:=\arcsin\left(D\sin\frac G2\right),
\qquad
\tau:=\pi-2\eta.
\tag{3.2}
$$

The two unit K-edges adjacent to the short vertex meet at angle `tau`. Rotate the edge-vector coordinate system so their mean direction is zero. Then

$$
\boxed{
\theta_0=-\frac\tau2,
\qquad
\theta_1=\frac\tau2.
}
\tag{SC.4}
$$

Every remaining K-edge joins two radius-`D` circular vertices at unit chord length, so consecutive ordinary edge directions differ by exactly `delta`.

The first ordinary edge after the defect has direction

$$
\frac G2+\frac\delta2
=\left(\frac32+\frac s2\right)\delta.
$$

Therefore, for `2<=j<=q-1`,

$$
\boxed{
\theta_j
=\left(j-\frac12+\frac s2\right)\delta.
}
\tag{SC.5}

The final ordinary direction is the reflection of the first about `pi/2`, since

\[
(q+s)\delta=\pi.
$$

At `s=0`, one has `tau=delta` and SC.4-SC.5 become the regular arithmetic half-direction list

$$
-\frac\delta2,\frac\delta2,\frac{3\delta}2,\ldots,
\pi-\frac{3\delta}2.
$$

---

## 4. The S1 closure splits into a `tau`-free real equation

Write

$$
w_j=e^{i\theta_j}.
$$

After reversing all signs if necessary, take

$$
\varepsilon_0=1,
\qquad
\varepsilon_1=-1.
\tag{4.1}
$$

The two defect-edge contributions are

$$
e^{-i\tau/2}-e^{i\tau/2}
=-2i\sin\frac\tau2,
$$

which is purely imaginary.

Thus SC.1 is equivalent to the exact pair

$$
\boxed{
\sum_{j=2}^{q-1}
\varepsilon_j
\cos\left(\left(j-\frac12+\frac s2\right)\delta\right)=0,
}
\tag{SC.6}
$$

and

$$
\boxed{
\sum_{j=2}^{q-1}
\varepsilon_j
\sin\left(\left(j-\frac12+\frac s2\right)\delta\right)
=2\sin\frac\tau2.
}
\tag{SC.7}
$$

If the global sign normalization in (4.1) is reversed, the right side of SC.7 reverses with it; SC.6 is unchanged up to an overall sign.

The key structural point is SC.6: the nonlinear short-vertex angle `tau` disappears completely. Only the single Reinhardt-ladder defect `s` remains.

---

## 5. Reflection-paired form of the real equation

For

$$
\alpha_j:=\left(j-\frac12+\frac s2\right)\delta,
$$

the involution

$$
j^*:=q+1-j
$$

satisfies

$$
\alpha_{j^*}=\pi-\alpha_j
$$

because `(q+s)delta=pi`. Hence

$$
\cos\alpha_{j^*}=-\cos\alpha_j,
\qquad
\sin\alpha_{j^*}=\sin\alpha_j.
$$

Therefore SC.6 becomes

### even `q`

$$
\boxed{
\sum_{j=2}^{q/2}
(\varepsilon_j-\varepsilon_{q+1-j})
\cos\alpha_j=0.
}
\tag{SC.8e}
$$

### odd `q`

The fixed index `(q+1)/2` has `alpha=pi/2` and contributes zero to SC.6, so

$$
\boxed{
\sum_{j=2}^{(q-1)/2}
(\varepsilon_j-\varepsilon_{q+1-j})
\cos\alpha_j=0.
}
\tag{SC.8o}

Thus the real closure only sees the antisymmetric part of the sign word under reflection across the defect axis.

The corresponding imaginary equation sees the symmetric part:

\[
\sum_{j<j^*}
(\varepsilon_j+\varepsilon_{j^*})\sin\alpha_j
$$

plus the possible odd-`q` central sign, and must equal `2 sin(tau/2)` after the normalization (4.1).

---

## 6. P1 endpoint: exact Littlewood root equation

At P1 the two unit defect edges become collinear and merge into one length-two K-edge. Geometrically

$$
\tau=0,
\qquad
G=\Delta_2,
\qquad
(q-2)\delta+\Delta_2=\pi.
\tag{6.1}
$$

The two corresponding primal sides are oppositely directed parallel unit vectors and therefore cancel in primal closure.

Put

$$
x:=\frac\delta2.
$$

Since `Delta_2/2=pi/2-(q-2)x` and `sin(Delta_2/2)=1/D=2 sin x`, P1 geometry is equivalently

$$
\boxed{
\cos((q-2)x)=2\sin x.
}
\tag{SC.9}
$$

For the remaining `q-2` primal sides, SC.5 becomes

$$
\theta_j
=\frac\pi2+(2j-q-1)x,
\qquad 2\le j\le q-1.
\tag{6.2}
$$

Therefore their exact closure is

$$
\sum_{j=2}^{q-1}
\varepsilon_j e^{i(2j-q-1)x}=0.
$$

Multiplying by the nonzero phase `e^{-i(3-q)x}` and setting

$$
z:=e^{2ix}=e^{i\delta}
$$

gives:

### Corollary SC.1 — P1 Littlewood obstruction

A P1 survivor can exist only if there is a Littlewood polynomial

$$
\boxed{
P(z)=\sum_{k=0}^{q-3}\epsilon_k z^k,
\qquad \epsilon_k\in\{+1,-1\},
}
\tag{SC.10}

such that

\[
\boxed{
P(e^{i\delta})=0,
}
\tag{SC.11}

where `delta` is the unique P1 angle satisfying SC.9.

This is substantially more rigid than arbitrary polygon closure: the root point is fixed by `q` through a one-variable trigonometric equation, while the polynomial has degree exactly `q-3` and every coefficient is nonzero `+/-1`.

---

## 7. Mod-2 normalization of every P1 candidate

Although SC.10 does not by itself imply that the unimodular root is cyclotomic, all candidate polynomials have the same reduction modulo two:

\[
\boxed{
P(z)\equiv1+z+\cdots+z^{q-3}\pmod2.
}
\tag{SC.12}

Equivalently,

\[
(z-1)P(z)\equiv z^{q-2}-1\pmod2.
\tag{SC.13}

This gives an arithmetic handle for a future exclusion. No claim is made here that every unimodular Littlewood zero is a root of unity; that statement is false in general.

---

## 8. Relation to the classical Reinhardt sign code

At zero defect `s=0`, the half-boundary directions are exactly equally spaced by `delta=pi/q`. Then SC.1 is the usual signed-root-of-unity closure problem. The odd number of sign-change states from SC.2 gives the odd dihedral composition; after compressing equal-sign runs, the standard Reinhardt closure polynomial has alternating nonzero coefficients.

S1 is therefore an exact one-parameter deformation of the Reinhardt sign-code problem in which:

1. only one antipodal state is short;
2. that state remains a sign-change/cycle state by AC;
3. the ordinary directions retain exact arithmetic spacing;
4. the real closure equation retains the reflection pairing SC.8;
5. all nonlinearity is concentrated in the single imaginary defect term `2 sin(tau/2)`.

This is the appropriate finite state space for a sign-code exclusion.

---

## 9. Regression audit

### Arbitrary sign words

SC does not claim every binary word corresponds to a convex Target C shell. It gives necessary closure equations; the antipodal odd-cycle/KKT restrictions further reduce the admissible words.

### Unimodular Littlewood roots

They need not be cyclotomic in general. SC.10 is recorded as a necessary arithmetic condition, not a completed contradiction.

### Defect signs

The opposite-sign condition SC.3 uses AC's proved endpoint-switch theorem. Without C65 full diameter visibility, equal defect signs would be possible abstractly.

### P1 merge

At `tau=0`, the two opposite-summand unit K-steps are collinear and merge into one length-two difference-body edge. In the primal polygon their two unit side vectors are opposite and cancel, which is why only `q-2` terms remain in SC.10.

### Projective seam

SC.2 includes the sign reversal at the antipodal half-boundary seam. Treating the half-word as an ordinary cyclic binary word would give the wrong parity.

---

## 10. Next theorem

The next target is now finite and arithmetic.

### P1 exclusion

Combine the fixed-angle equation

\[
\cos((q-2)\delta/2)=2\sin(\delta/2)
$$

with the necessary Littlewood zero

$$
P(e^{i\delta})=0,
\qquad
\deg P=q-3.
$$

Possible approaches are:

1. derive the minimal polynomial of `e^{i delta}` and prove its degree exceeds `q-3`;
2. use the universal mod-2 reduction SC.12 together with the geometric algebraic equation to obtain an incompatible local factorization;
3. exploit the restricted odd-run sign structure from CS rather than arbitrary Littlewood polynomials.

### S1 exclusion

Use SC.8 plus CS: all KKT-face edges are sign-change states on the same odd run composition containing the short defect state. The two endpoint cuts therefore mark two additional sign changes in one word. Insert that run structure into the reflection-paired real equation and the WM/WT endpoint conditions.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

S1, no parallel sides:
Take one projective half of K=F-F, with unit edge vectors w_j and signs epsilon_j
saying whether the corresponding primal F-side is w_j or -w_j. Then primal closure is
  sum epsilon_j w_j=0.
Sign-change antipodal states are exactly the odd-cycle edges of the canonical maximal
antipodal thrackle. AC puts the short state between opposite signs epsilon_0=-epsilon_1.

Let delta=2asin(1/(2D)), s=pi/delta-q, G=(s+2)delta,
eta=asin(D sin(G/2)), tau=pi-2eta. Rotate edge directions so
  theta_0=-tau/2, theta_1=tau/2,
  theta_j=(j-1/2+s/2)delta, 2<=j<=q-1.
Normalize epsilon_0=1, epsilon_1=-1. Closure splits exactly into
  sum_{j=2}^{q-1} epsilon_j cos(theta_j)=0,
  sum_{j=2}^{q-1} epsilon_j sin(theta_j)=2 sin(tau/2).
The real equation is independent of tau. Pairing j* = q+1-j gives
  sum (epsilon_j-epsilon_j*) cos(theta_j)=0.

P1 endpoint: tau=0. Put x=delta/2. Geometry is
  cos((q-2)x)=2 sin x.
The parallel primal pair cancels, and the remaining q-2 directions are
  pi/2+(2j-q-1)x.
Hence P1 requires a Littlewood polynomial of degree q-3,
  P(z)=sum_{k=0}^{q-3} eps_k z^k,
to vanish at the fixed point z=e^{i delta}.
All candidates satisfy mod 2
  P(z) == 1+z+...+z^{q-3}.

Next: exclude P1 arithmetically, then feed the S1 run word into CS+WM+WT.
```
