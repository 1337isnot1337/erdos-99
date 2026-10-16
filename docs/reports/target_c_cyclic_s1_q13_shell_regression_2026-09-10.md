<!-- theorem-state: {"artifact_id":"ART-7A2B3FF788EF","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
LEVEL I STATUS: STILL OPEN

# Erdős Problem #99 — a strict `q=13` S1 shell survives closure, positive KKT, and maximal-rank PSD stress

**Date:** 2026-09-10  
**Run type:** exact algebraic shell construction plus high-precision mechanical regression check  
**Target:** primitive cyclic `d_H=1,s_Z=1`, S1  
**Depends on:** D1/SC on PR #118; RSQ on this branch  
**Computation:** yes; all numerical claims below are regression/certificate data, not promoted as a source-level theorem

## 1. Status and purpose

RSQ reduces S1 to the exact system

\[
Q(z)=Q^*(z),
\qquad
F_m(z)=(z-1)^2Q(z)^2.
\]

A tempting next conjecture was that this system itself might have no strict-interior S1 solutions. That conjecture is false.

There is already a strict-interior palindromic solution at

\[
\boxed{q=13,\qquad m=11.}
\]

More importantly, reconstructing the equilateral shell from that solution gives exactly the Target-C shell active counts

\[
\boxed{|C|=13,\qquad |H|=12,}
\]

with `H` a spanning tree, and the mixed active framework admits a strictly positive full-support equilibrium stress whose scalar stress matrix is PSD with exactly the affine three-dimensional kernel.

Therefore the following shell-only route is rejected:

```text
S1 signed closure
+ positive full-support KKT stress
+ maximal-rank PSD scalar stress
=> contradiction.
```

It does **not** contradict Target C or Erdős #99. The full source contains a quadratic interior population, and shell local/global active-set conditions are stronger than the first-order/PSD checks recorded here. The result is a durable regression showing that a genuine S1 proof must use additional information.

---

## 2. Exact palindromic sign word

Take

\[
Q(Z)=
-Z^{10}+Z^9-Z^8-Z^7+Z^6+Z^5+Z^4-Z^3-Z^2+Z-1.
\tag{2.1}
\]

Its coefficient word, low degree first, is

```text
(-1,+1,-1,-1,+1,+1,+1,-1,-1,+1,-1).
```

This is palindromic:

\[
Q=Q^*.
\]

Thus the RSQ phase equation is automatic for every point on the unit circle.

For `m=11`, the centered cosine polynomial is

\[
\boxed{
R(T)=-T^5+T^4+4T^3-5T^2-T+5,
}
\tag{2.2}

meaning

\[
z^{-5}Q(z)=R(z+z^{-1}).
\]

The RSQ amplitude equation becomes

\[
G_{11}(T)+(2-T)R(T)^2=0.
\]

After cancellation of the leading term this is

\[
\boxed{
P_{13}(T):=
T^{10}-2T^9-8T^8+18T^7+17T^6-52T^5
+T^4+51T^3-22T^2-13T+11=0.
}
\tag{2.3}

This polynomial is irreducible over `Q` in the symbolic computation used for the regression, though irreducibility is not needed for the shell construction.

It has the real root

\[
\boxed{
t_*=1.94199413054336852922749320256\ldots}
\tag{2.4}

with a rational isolating interval obtained by exact Sturm isolation in the computation. Put

\[
\delta_*:=\arccos(t_*/2).
\]

Numerically,

\[
\boxed{
\delta_*=0.2414300075120225\ldots,
}
\tag{2.5}

and

\[
\boxed{
D_*=rac1{2\sin(\delta_*/2)}
=4.1520639086997635\ldots.
}
\tag{2.6}

---

## 3. The root lies strictly inside the S1 interval

For `q=13`, the zero-defect Reinhardt boundary is

\[
\delta_R=\frac\pi{13}
=0.241660973353061\ldots.
\]

The P1 boundary is the unique solution of

\[
11\delta+2\arcsin\left(2\sin\frac\delta2\right)=\pi,
\]

namely

\[
\delta_P
=0.2413833791241437\ldots.
\]

The constructed root satisfies

\[
\boxed{
\delta_P<\delta_*<\delta_R.
}
\tag{3.1}

The margins are approximately

\[
\delta_* - \delta_P
=4.66284\times10^{-5},
\]

\[
\delta_R-\delta_*
=2.30966\times10^{-4}.
\]

Hence this is neither the P1 collapse nor the Reinhardt equality boundary.

D1 gives the strict short-state angle

\[
G_*=\pi-11\delta_*
=0.4858625709575457\ldots,
\]

and

\[
\boxed{
\tau_*=0.0990340932801166\ldots>0.
}
\tag{3.2}

The RSQ centered closure value is

\[
2\sin(\tau_*/2)
=0.0989936273335191\ldots.
\]

---

## 4. Reconstructed convex equilateral shell

Use the full half-boundary sign word

```text
(+1,-1,-1,+1,-1,-1,+1,+1,+1,-1,-1,+1,-1),
```

where the first two signs are the canonical S1 defect pair and the remaining eleven coefficients are (2.1).

The half-boundary edge directions are the exact SC directions

\[
\theta_0=-\tau_*/2,
\qquad
\theta_1=+\tau_*/2,
\]

\[
\theta_j
=\frac\pi2+(2j-14)\frac{\delta_*}{2},
\qquad2\le j\le12.
\]

Choose the signed primal unit vectors and sort them in cyclic direction order. In the half-boundary index labels this cyclic side order is

```text
3,6,7,8,11,1,2,4,5,9,10,12,0.
```

Their vector sum vanishes to `7.1e-14` in the high-precision reconstruction. The corresponding convex equilateral polygon was then labeled in this cyclic side order as vertices

\[
0,1,\ldots,12.
\]

The active unit contacts are exactly

\[
\boxed{
01,12,23,34,45,56,67,78,89,9\,10,10\,11,11\,12,12\,0.
}
\tag{4.1}

There are no additional unit pairs. The closest inactive pair has distance

\[
1.771341203064894\ldots,
\]

so its unit-separation slack is

\[
\boxed{>0.7713.}
\tag{4.2}

---

## 5. The actual diameter graph has exactly `q-1` edges

At the same reconstruction the actual diameter pairs are exactly

\[
\boxed{
\begin{aligned}
H=\{&06,07,17,18,19,29,39,49,4\,10,4\,11,5\,11,5\,12\}.
\end{aligned}
}
\tag{5.1}

Thus

\[
\boxed{|H|=12=q-1.}
\tag{5.2}

The graph is connected and acyclic, hence a spanning tree.

Its degree sequence in shell order is

```text
2,3,1,1,3,2,1,2,1,4,1,2,1.
```

The closest inactive pair to diameter is the canonical short antipodal pair

\[
05,
\]

with

\[
|05|=4.079643788218755\ldots,
\]

while

\[
D_*=4.1520639086997635\ldots.
\]

Hence the inactive diameter margin is

\[
\boxed{D_*-|05|>0.07242.}
\tag{5.3}

The D1 endpoint lower value is

\[
\sqrt{D_*^2-1}=4.029843012069721\ldots,
\]

so the canonical short edge lies strictly in the expected S1 interval.

Adding `05` to `H` creates the canonical odd cycle of length seven. An abstract second maximal-thrackle completion also exists, which is consistent with AC's warning that arbitrary completion is not unique; `05` is distinguished by the actual antipodal geometry.

---

## 6. Strictly positive full-support equilibrium stress

Construct the signed mixed equilibrium matrix using

- positive contact rows for the 13 shell contacts;
- negative diameter rows for the 12 actual diameter bars.

Normalize

\[
\sum_{h\in H}\beta_h=1.
\]

A linear program maximizing the smallest stress coordinate gives a strictly positive equilibrium stress. One numerical solution has contact coefficients

```text
1.28497804,
1.36393058,
1.24806330,
1.24806330,
1.24806330,
1.28497804,
1.36393058,
1.34831027,
1.37525176,
1.37525176,
1.37525176,
1.37525176,
1.34831027
```

in the contact order (4.1), and diameter coefficients

```text
0.10224509,
0.10515140,
0.05283119,
0.07977267,
0.08760465,
0.07239500,
0.07239500,
0.08760465,
0.07977267,
0.05283119,
0.10515140,
0.10224509
```

in the diameter order (5.1).

The smallest displayed coefficient is

\[
\boxed{0.05283118\ldots>0.}
\tag{6.1}

and the equilibrium residual in the reconstruction is about

\[
3.2\times10^{-15}.
\]

Thus failure of positive KKT support is not a viable explanation for this S1 shell.

---

## 7. Scalar stress is PSD with affine kernel

Form

\[
\Omega=L_C(\alpha)-L_H(\beta).
\]

The computed eigenvalues are

```text
-9.7e-16,
-1.5e-16,
 5.2e-16,
 1.10390115,
 1.10805157,
 2.06473183,
 2.12664090,
 3.40120111,
 3.55459104,
 4.41951551,
 4.47269946,
 5.01046293,
 5.21747392.
```

The first three numerical zero modes are exactly the expected affine modes

\[
\mathbf1,P_x,P_y.
\]

The first nonzero eigenvalue has the robust margin

\[
\boxed{\lambda_4>1.1039.}
\tag{7.1}

Hence the numerical stress is PSD of rank

\[
q-3=10
\]

with no near-zero accidental fourth mode.

---

## 8. Numerical local-diameter optimization regression

As an additional nonproof regression, the reconstructed shell was used as the initial point for a constrained local optimization:

- all 13 consecutive shell distances constrained exactly to one;
- a free diameter variable minimized;
- all pair distances constrained above by that diameter;
- Euclidean rigid motions fixed by pinning one side.

SLSQP returned the same diameter

\[
4.15206390869976\ldots
\]

with improvement below `1e-13`.

This is not a proof of local minimality and is not used as one. It is recorded only because it confirms that the shell is not an obvious first-order numerical saddle missed by the KKT calculation.

---

## 9. Consequence for the proof program

The q=13 shell kills several plausible S1 shortcuts at once.

A genuine S1 contradiction cannot follow from only:

1. exact D1 one-short-state geometry;
2. exact signed primal closure;
3. `q` unit shell contacts and `q-1` actual diameters;
4. connected spanning-tree diameter topology;
5. existence of a full-support positive KKT stress;
6. maximal-rank PSD scalar stress.

All six occur simultaneously in this strict-interior shell regression.

The remaining source-level hypotheses not certified here include:

- existence of the full `n=q+Theta(D^2)` unit-separated interior population required by a global minimum source;
- global minimum diameter at that larger source cardinality;
- the C65 lexicographic active-diameter minimality transferred in SL+;
- any source-specific second-order obstruction involving the dense interior cloud.

Therefore the high-value S1 frontier shifts from generic shell mechanics to either:

- an **interior packing/capacity obstruction** for this one-defect shell family, or
- an **SL+ active-set deformation theorem** stronger than PSD first-order stress.

---

## 10. Scope and audit warnings

- This is not a counterexample to Erdős #99.
- This is not a proof that the q=13 shell is a global or even rigorously local diameter minimum among all equilateral 13-gons.
- The exact algebraic equation (2.3) and the sign word are rigorous symbolic data; active-set and stress claims are high-margin numerical certificates pending interval/exact verification.
- The result deliberately does not promote any canonical theorem.
- No d_H=2 Euler-trail/path inference is used.

---

## 11. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Strict S1 shell regression at q=13, m=11:
  Q=-Z^10+Z^9-Z^8-Z^7+Z^6+Z^5+Z^4-Z^3-Z^2+Z-1,
  Q=Q*.
RSQ amplitude reduces to P13(t)=0 with
  P13=t^10-2t^9-8t^8+18t^7+17t^6-52t^5+t^4+51t^3-22t^2-13t+11.
Physical root:
  t=1.9419941305433685...,
  delta=0.2414300075120225...,
  D=4.1520639086997635...,
strictly between P1 and Reinhardt boundaries.

Reconstruction has exactly:
  13 consecutive unit contacts,
  12 actual diameter edges forming a spanning tree,
  nearest inactive contact slack >0.7713,
  nearest inactive diameter slack >0.07242.

A normalized full-support KKT stress has every coefficient >=0.05283118.
Its scalar stress matrix has exactly three zero affine eigenvalues and
  lambda_4>1.1039.
Numerical constrained local optimization also returns the same D to <1e-13.

Therefore closure + positive KKT + maximal-rank PSD does NOT exclude strict S1.
Any real S1 proof must use stronger active-set/local-minimum information or the quadratic
interior source population.
```
