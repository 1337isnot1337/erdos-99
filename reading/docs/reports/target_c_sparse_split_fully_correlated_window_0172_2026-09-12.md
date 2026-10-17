> Generated reading edition · [exact source](../../../docs/reports/target_c_sparse_split_fully_correlated_window_0172_2026-09-12.md) · source SHA-256 `1b79d797103d250cf3bb3552ca667479e0468dc1aec747bf6191b816d8e1e8c8`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-06DE90EFB06C","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C — fully correlated sparse-return exclusion through `sigma=0.0172`

**Date:** 2026-09-12  
**Lifecycle:** proof-only strengthening of the sparse/directional signed-return route; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The earlier sparse-return closure maximized the directional product and the sparse
penalty separately. Those two extrema spend the same slack in incompatible places:

- the directional product is maximized near `y=sigma`;
- the largest sparse penalty is obtained by putting the slack into `z`.

Keeping the **entire** four-variable correlation removes this double payment. The
result is a much larger safe full-core exclusion window:

$$
\boxed{0\le\sigma\le s_0:=0.0172.}
\tag{0.1}
$$

The exact one-dimensional scalar envelope of the same fully correlated argument
vanishes only near

$$
\boxed{\sigma_{env}=0.0173116294\ldots .}
\tag{0.2}
$$

The theorem endpoint is deliberately `0.0172`, where the normalized contradiction
margin remains above `0.00232`.

---

## 1. Starting inequality and uniform endpoint relaxation

Use the sparse/directional theorem with

$$
x+y+z+w=\sigma,
\qquad x,y,z,w\ge0,
\tag{1.1}
$$

and

$$
\lambda z\ge\kappa[J]_+,
\qquad
\kappa:=2-\sqrt3,
\tag{1.2}
$$

where

$$
\begin{aligned}
J={}&A_*(x,w)
-\lambda\left(10z+{x\over2}+{25w\over3}\right)\\
&-2\left(U-x-y+2z\right)
\left(Q(y)+y+x+{10w\over3}\right),
\end{aligned}
\tag{1.3}
$$

$$
A_*(x,w)
={\pi\over4}-G(\theta)-2G(\phi_8+r)-G(r),
\qquad
r=x+{10w\over3},
\tag{1.4}
$$

and

$$
G(t)={t-\sin t\over8}.
$$

The tooth inverse `Q(y)` is determined by

$$
\sin Q+\sqrt3(1-\cos Q)-Q={y\over2}.
\tag{1.5}
$$

Define

$$
\widetilde J:=J-{\lambda z\over\kappa}.
\tag{1.6}
$$

If `widetilde J>0`, then (1.2) would imply

$$
\lambda z\ge\kappa J>\lambda z,
$$

which is impossible. Thus it suffices to prove a uniform positive lower bound for
`widetilde J`.

Let `theta_0` be the unique solution of

$$
3\theta_0-2\pi-\sin(\theta_0/2)-2\sin\theta_0=s_0.
$$

At `s_0=0.0172`,

$$
\boxed{
\begin{aligned}
\theta_0&=2.706564629265182\ldots,\\
U_0&=3\theta_0-2\pi=1.836508580615961\ldots,\\
\lambda_0&=\sin(\theta_0/2)=0.976436949372909\ldots,\\
\phi_0&=2\pi-2\theta_0=0.870056048649222\ldots .
\end{aligned}}
\tag{1.7}

For every `sigma<=s_0`, monotonicity gives

\[
\theta\le\theta_0,
\qquad
U\le U_0,
\qquad
\lambda\le\lambda_0.
\tag{1.8}
$$

Since `G` is increasing, the actual `widetilde J` is bounded below by the endpoint
relaxation obtained by replacing `theta,U,lambda` by `theta_0,U_0,lambda_0` while
retaining the correlated variables `x,y,z,w`.

We may enlarge the feasible set to

$$
x+y+z+w\le s_0.
\tag{1.9}
$$

For fixed `x,y,z`, the relaxed lower bound is strictly decreasing in `w`: increasing
`w` increases `r`, increases the sparse penalty, and increases the directional factor
`B`, while leaving `C=U_0-x-y+2z` fixed. Therefore the relaxed minimum occurs on

$$
\boxed{x+y+z+w=s_0.}
\tag{1.10}
$$

This reduces all smaller physical slack values to one endpoint simplex without
assigning any fictitious slack to a physical source.

---

## 2. Geometry remains inside the inherited Section-118 regime

The extension to `0.0172` still lies well inside every load-bearing geometric margin.

The hostile Section-117 transfer theorem gives a cost above `0.0326` for the branch
`delta>=0.1`. Since now

$$
w\le\sigma\le0.0172<0.0326,
$$

that branch is impossible, and

$$
\delta\le{10\over3}w.
\tag{2.1}
$$

The exact complement identity gives

$$
x_2+x_3+\tau=\delta+x,
$$

hence

$$
0\le x_2,x_3,\tau
\le x+{10\over3}w
\le{10\over3}s_0
=0.0573333\ldots .
\tag{2.2}

At the endpoint the residual principal gap is

\[
\phi_0=0.8700560\ldots,
$$

so the fourth-gap/adjacent-span branch retains large strict separation.

The oriented tangent-lift extent is bounded by

$$
|S|+\tau
\le U_0+{10\over3}s_0
=1.8938419139\ldots<\pi.
\tag{2.3}

Even the coarser Section-113 principal-corridor mismatch bound remains

\[
{\theta_8\over2}-{\pi\over3}-{73\over6}s_0
=0.0949897969\ldots>0.
\tag{2.4}

Finally,

\[
Q(s_0)=0.100673979368082\ldots<0.101<\pi/3,
\tag{2.5}
$$

so the tooth inverse remains on its unique monotone branch.

Thus the geometry, tangent direction lift, circular-segment area identity, and
signed-return theorem used in (1.3) remain valid throughout the new window.

---

## 3. Substitute `w=s_0-x-y-z`

On the boundary simplex (1.10), put

$$
w=s_0-x-y-z.
$$

Then

$$
r={10s_0\over3}-{7x\over3}-{10y\over3}-{10z\over3},
\tag{3.1}
$$

$$
C=U_0-x-y+2z,
\tag{3.2}
$$

and

$$
B=Q(y)+{10s_0\over3}
-{7x\over3}-{7y\over3}-{10z\over3}.
\tag{3.3}
$$

The relaxed lower bound is

$$
\mathcal F(x,y,z)
=A(r)
-\lambda_0 P(x,y,z)
-2CB,
\tag{3.4}
$$

where

$$
A(r)={\pi\over4}-G(\theta_0)-2G(\phi_8+r)-G(r),
$$

and

$$
P=10z+{x\over2}+{25w\over3}+{z\over\kappa}.
$$

We next show that the global minimum has

$$
\boxed{x=z=0.}
\tag{3.5}

---

## 4. `x=0` at every minimizer

Let

\[
A_r=-2G'(\phi_8+r)-G'(r)<0.
$$

Since

$$
r_x=-{7\over3},
\qquad
C_x=-1,
\qquad
B_x=-{7\over3},
$$

and

$$
P_x={1\over2}-{25\over3}=-{47\over6},
$$

we have

$$
\begin{aligned}
\mathcal F_x
&=-{7\over3}A_r
+{47\over6}\lambda_0
+2B+{14\over3}C.
\end{aligned}
\tag{4.1}

Every term on the right is strictly positive. Therefore

\[
\boxed{\mathcal F_x>0}
$$

throughout the simplex, and every minimizer has `x=0`.

This is exact; no numerical estimate is needed.

---

## 5. `z=0` at every minimizer

Now

$$
r_z=-{10\over3},
\qquad
C_z=2,
\qquad
B_z=-{10\over3},
$$

while

$$
P_z
=10+{1\over\kappa}-{25\over3}
=5.3987174742\ldots .
$$

Hence

$$
\mathcal F_z
=-{10\over3}A_r
-\lambda_0P_z
-4B+{20\over3}C.
\tag{5.1}
$$

The area term is positive. Also throughout the simplex

$$
C\ge U_0-s_0
=1.8193085806\ldots,
\tag{5.2}
$$

and, from the original nonnegative expression for `B`,

$$
B
\le Q(s_0)+{10s_0\over3}
<0.158008.
\tag{5.3}
$$

Therefore

$$
\mathcal F_z
>
-0.976437(5.398718)
-4(0.158008)
+{20\over3}(1.819308)
>6.22.
\tag{5.4}
$$

Thus

$$
\boxed{\mathcal F_z>0}
$$

and every global minimizer has `z=0`.

The formerly expensive `z` endpoint cannot coexist with the product extremizer; this
is the correlation that the earlier separate-max proof discarded.

---

## 6. One-dimensional exact envelope

With `x=z=0`, put

$$
w=s_0-y,
\qquad
r={10\over3}(s_0-y).
$$

The lower-bound function becomes

$$
\boxed{
\begin{aligned}
H(y)={}&{\pi\over4}-G(\theta_0)
-2G\left(\phi_8+{10\over3}(s_0-y)\right)
-G\left({10\over3}(s_0-y)\right)\\
&-{25\lambda_0\over3}(s_0-y)\\
&-2(U_0-y)
\left(Q(y)+{10s_0\over3}-{7y\over3}\right),
\end{aligned}}
\tag{6.1}
$$

for

$$
0\le y\le s_0.
$$

### Strict convexity

Let

$$
F(q)=\sin q+\sqrt3(1-\cos q)-q.
$$

From `F(Q(y))=y/2`,

$$
Q'(y)={1\over2F'(Q)},
$$

and

$$
Q''(y)=-{F''(Q)\over4F'(Q)^3}<0.
\tag{6.2}
$$

On `0<=y<=s_0`, (2.5) gives `Q<0.101`. Hence

$$
F'(Q)\le\sqrt3Q<0.175,
$$

while

$$
F''(Q)=-\sin Q+\sqrt3\cos Q>1.62.
$$

Therefore

$$
-Q''(y)>75.7.
\tag{6.3}
$$

The second derivative of the area term is bounded below by `-25/6`. Using
`U_0-y>1.8193` and `Q'(y)>1/(2(0.175))>2.857`, direct differentiation of (6.1) gives

$$
\boxed{H''(y)>273}
\tag{6.4}
$$

throughout the interval away from `y=0`; the right derivative diverges favorably as
`y downarrow0`. Thus `H` is strictly convex and has a unique minimum.

### Bracket the unique minimizer

Direct endpoint-safe evaluations give

$$
H'(0.00669)<-0.0068,
$$

and

$$
H'(0.00670)>0.0059.
\tag{6.5}
$$

Therefore the unique minimizer lies in

$$
0.00669<y_*<0.00670.
$$

At the midpoint

$$
y_c=0.006695,
$$

$$
H(y_c)
=0.0023269894\ldots .
\tag{6.6}
$$

By convexity, `H'` stays between the two derivative values in the bracket, so moving at
most `5e-6` from `y_c` can lower `H` by less than `3.5e-8`. Consequently

$$
\boxed{
\min_{0\le y\le s_0}H(y)>0.0023269>0.00232.
}
\tag{6.7}

Hence

\[
\widetilde J>0
$$

uniformly on the complete endpoint simplex.

This contradicts the necessary signed-return inequality and proves (0.1).

---

## 7. Scalar envelope of the fully correlated mechanism

For each scalar endpoint `s`, repeat the exact reduction above with the corresponding
`theta(s),U(s),lambda(s)`. The unique one-dimensional minimum decreases with `s` near
the new endpoint. Its first numerical zero is

$$
\boxed{
sigma_{env}=0.0173116294165\ldots .
}
\tag{7.1}

The theorem does not claim that equality root. At `s_0=0.0172` the minimum still has
margin above `0.00232`, while the inherited geometry has large strict room:

\[
{10s_0\over3}=0.05733\ldots<0.1,
\qquad
U_0+{10s_0\over3}<1.894<\pi.
$$

Thus `0.0172` is a safe, non-knife-edge endpoint.

---

## 8. Frontier effect

The earlier `sigma<=0.0105` extension is strictly superseded. The proof-only full-core
survivor must now lie in

$$
\boxed{\sigma>0.0172.}
\tag{8.1}

At the endpoint,

\[
\lambda_0=0.976436949372909\ldots,
$$

so in the Section-101 angular parametrization the selected wrapping carrier must lie
beyond this normalized diameter scale.

The remaining scalar room of the same mechanism is only about `1.12e-4` in `sigma`.
Further work should therefore attack the geometry of the larger-slack / nearly
diameter-spanning carrier, not continue independent-max decimal optimization.

The Type-I inactive-container branch remains open and independent.

---

## 9. Scope

- The theorem keeps all four slack variables correlated until the exact minimization.
- No source point is deleted.
- No contact-isolated coordinate enters a core affine-kernel theorem.
- The Section-117 signed-return and sparse/directional train split remain proof-only
  dependencies.
- The extension is full-core Type II only.
- The theorem does not settle C-II or Level I.

**Disposition:** proof-only full-core exclusion through `sigma=0.0172`.