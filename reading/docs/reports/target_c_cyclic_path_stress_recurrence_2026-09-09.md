> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_path_stress_recurrence_2026-09-09.md) · source SHA-256 `d5d48edfdf9964dc4085a9fc17e20375748cb4147ad02c4d4265e79c0bb8b507`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- theorem-state: {"artifact_id":"ART-F40F19F95321","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — the full `d_H=0` KKT family reduces to one stress variable per Reuleaux path

**Date:** 2026-09-09  
**Run type:** exact scalar KKT recurrence / composition reduction  
**Target:** Target C cyclic `d_H=0` Reinhardt endpoint  
**Depends on:** KL signed-stress recurrence in this PR; PR #125 LC Reuleaux leaf composition; exact gap angle `theta=pi/q`  
**External literature:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`

KL parametrizes arbitrary signed equilibrium stresses at the level of the `q` projective diameter directions. The odd-cycle-plus-leaves geometry collapses this to only one contact-stress variable per defining Reuleaux arc.

Let the unique odd diameter-cycle edges occur in projective direction order at positions

```math
t_0<t_1<\cdots<t_{r-1}<t_0+q,
```

with

```math
\ell_i:=t_{i+1}-t_i>0,
\qquad
\sum_i\ell_i=q.
\tag{PS.1}
```

This `ell_i` is exactly the LC leaf-composition part at the cycle vertex shared by the two cycle edges at `t_i,t_{i+1}`.

Put

```math
\theta:=\frac\pi q,
\qquad
\phi_i:=\ell_i\theta.
\tag{PS.2}
```

For an arbitrary normalized KKT stress, define

```math
\boxed{\sigma_i>0}
```

to be the common contact coefficient on the `ell_i` shell contacts of the LC path between those two cycle edges.

Then:

### Theorem PS — exact path-stress reduction

1. Every contact on the `i`th LC path has coefficient exactly `sigma_i`.
2. Every pendant diameter edge lying between `t_i` and `t_{i+1}` has coefficient
   ```math
   \boxed{\beta_h=\frac{\sigma_i}{D^2}.}
   \tag{PS.3}
   
   ```
3. If
   ```math
   d_i:=\sigma_{i-1}-\sigma_i,
   \tag{PS.4}
   
   ```
   then the coefficient `beta_i` of the cycle diameter edge at `t_i` is
   ```math
   \boxed{
   \beta_i
   =(1-\cos\theta)(\sigma_{i-1}+\sigma_i)
   -\frac{\sin\theta}{\sin\phi_i}
   \left(
   \cos\phi_i\,d_i+d_{i+1}
   \right).
   }
   \tag{PS.5}
   
   ```
4. The alternating jump sequence
   ```math
   y_i:=(-1)^i d_i
   
   ```
   satisfies the exact variable-step harmonic recurrence
   ```math
   \boxed{
   y_{i+2}
   =
   \frac{\sin(\phi_i+\phi_{i+1})}{\sin\phi_i}
   y_{i+1}
   -
   \frac{\sin\phi_{i+1}}{\sin\phi_i}
   y_i.
   }
   \tag{PS.6}
   
   ```
5. Under the normalization
   ```math
   \sum_{h\in H}\beta_h=1,
   
   ```
   the path stresses satisfy
   ```math
   \boxed{\sum_i\ell_i\sigma_i=D^2,}
   \tag{PS.7}
   
   ```
   and the total KKT mass on the unique diameter cycle is
   ```math
   \boxed{
   \sum_{i=0}^{r-1}\beta_i
   =\frac1{D^2}\sum_{i=0}^{r-1}\sigma_i.
   }
   \tag{PS.8}
   
   ```

Thus the complete nonnegative KKT polygon is equivalently an `r`-variable positive path-stress family satisfying one variable-step harmonic recurrence and the cycle inequalities `beta_i>=0` from PS.5.

The `q-r` pendant beta coordinates and all `q` contact coordinates are then forced algebraically.

---

## 1. Direction blocks and the LC paths

KL indexes all actual diameter edges

```math
h_0,\ldots,h_{q-1}
```

in projective direction order. Let `chi_t` be the signed unique-cycle vector. Then

```math
\chi_t=0
```

exactly on pendant diameter edges, and the nonzero positions are `t_i`.

The contiguous-star theorem says that between two consecutive cycle positions `t_i,t_{i+1}`, all intermediate diameter edges are the pendant edges incident to their common cycle vertex. There are

```math
\ell_i-1
```

such pendant edges.

The `ell_i` consecutive direction transitions

```math
(t_i,t_i+1),\ldots,(t_{i+1}-1,t_{i+1})
```

are exactly the `ell_i` shell contacts of the corresponding LC path.

This identifies the direction-order gap `t_{i+1}-t_i` with the Reuleaux composition part from PR #125.

---

## 2. Contact stress is constant along each Reuleaux path

KL writes `a_t` for the contact coefficient on the transition between diameter directions `h_t,h_{t+1}`.

Its imaginary equilibrium recurrence is

```math
\sin\theta\,(a_{t-1}-a_t)
=\frac{\chi_t}{D}\,c\cdot J\nu_t,
\tag{2.1}
```

for one global vector parameter `c in R^2` and unit diameter-direction representative `nu_t`.

If `t` is a pendant position, then `chi_t=0`. Therefore

```math
a_{t-1}=a_t.
\tag{2.2}
```

Apply this for

```math
t=t_i+1,\ldots,t_{i+1}-1.
```

It gives

```math
a_{t_i}=a_{t_i+1}=\cdots=a_{t_{i+1}-1}.
```

Define their common value to be

```math
\boxed{\sigma_i.}
\tag{2.3}
```

These are exactly the contact coefficients on the `ell_i` LC shell-path edges. Universal contact positivity gives

```math
\sigma_i>0
```

for every normalized KKT stress.

This proves PS.1.

---

## 3. Pendant beta coefficients are forced by the same path stress

KL's real recurrence is

```math
(1-\cos\theta)(a_{t-1}+a_t)-\beta_t
=\frac{\chi_t}{D}\,c\cdot\nu_t.
\tag{3.1}
```

For a pendant position `t`, `chi_t=0` and `a_{t-1}=a_t=sigma_i`. Hence

```math
\beta_t
=2(1-\cos\theta)\sigma_i.
```

The exact Reinhardt relation gives

```math
2(1-\cos\theta)
=4\sin^2\frac\theta2
=\frac1{D^2}.
```

Therefore

```math
\boxed{\beta_t=\sigma_i/D^2.}
```

This proves PS.3 and strengthens the qualitative leaf-forcing statement: every pendant beta is not merely positive, but exactly proportional to its whole Reuleaux-path contact stress.

---

## 4. Eliminate the global vector parameter from a cycle beta

Choose the cycle signs so

```math
\chi_{t_i}=(-1)^i.
\tag{4.1}
```

Put

```math
\nu_i:=\nu_{t_i},
\qquad
\nu_{i+1}=R_{\phi_i}\nu_i,
\qquad
\phi_i=\ell_i\theta.
\tag{4.2}
```

At cycle position `t_i`, (2.1) becomes

```math
\sin\theta\,d_i
=\frac{(-1)^i}{D}c\cdot J\nu_i,
\tag{4.3}
```

where

```math
d_i=\sigma_{i-1}-\sigma_i.
```

Apply (4.3) also at `i+1`:

```math
c\cdot J\nu_{i+1}
=D\sin\theta\,(-1)^{i+1}d_{i+1}.
\tag{4.4}
```

But

```math
J\nu_{i+1}
=\cos\phi_i J\nu_i-\sin\phi_i\nu_i.
```

Substitute (4.3)-(4.4) and solve for the signed radial projection:

```math
\boxed{
\frac{(-1)^i}{D}c\cdot\nu_i
=
\frac{\sin\theta}{\sin\phi_i}
\left(
\cos\phi_i\,d_i+d_{i+1}
\right).
}
\tag{4.5}
```

Now insert (4.5) into the real cycle equation (3.1), where

```math
a_{t_i-1}=\sigma_{i-1},
\qquad
a_{t_i}=\sigma_i.
```

This gives exactly PS.5. `square`

No global vector parameter remains.

---

## 5. Harmonic recurrence for the stress jumps

Define

```math
y_i:=(-1)^i d_i.
```

Equation (4.3) says, up to the common constant `D sin theta`,

```math
y_i=c\cdot J\nu_i.
\tag{5.1}
```

Thus `y_i` is one fixed sinusoid sampled at the variable angular mesh

```math
\arg\nu_{i+1}-\arg\nu_i=\phi_i.
```

For any function

```math
y(\alpha)=A\cos\alpha+B\sin\alpha,
```

sampled at

```math
\alpha_{i+1}=\alpha_i+\phi_i,
```

the elementary two-point interpolation identity gives

```math
y_{i+2}
=
\frac{\sin(\phi_i+\phi_{i+1})}{\sin\phi_i}y_{i+1}
-
\frac{\sin\phi_{i+1}}{\sin\phi_i}y_i.
```

This proves PS.6.

Equivalently, the jump sequence has only two degrees of freedom despite having `r` entries; the third signed-stress degree of freedom is the common additive level of the `sigma_i`.

---

## 6. Exact normalization identities

The KKT virial identity for unit contacts and diameter-`D` constraints is

```math
\sum_{e\in C_q}\alpha_e
=D^2\sum_{h\in H}\beta_h.
\tag{6.1}
```

Under the standard normalization

```math
\sum_h\beta_h=1,
```

we get

```math
\sum_{e\in C_q}\alpha_e=D^2.
```

The LC paths partition the `q` shell contacts, and path `i` contains exactly `ell_i` contacts of common coefficient `sigma_i`. Hence

```math
\boxed{
\sum_i\ell_i\sigma_i=D^2,
}
```

proving PS.7.

Now count pendant beta mass. Path `i` corresponds to exactly

```math
\ell_i-1
```

pendant diameter edges, each of coefficient `sigma_i/D^2`. Therefore

```math
\sum_{h\text{ pendant}}\beta_h
=\frac1{D^2}
\sum_i(\ell_i-1)\sigma_i.
\tag{6.2}
```

Subtract this from total beta mass one and use PS.7:

```math
\begin{aligned}
\sum_{i=0}^{r-1}\beta_i
&=1-\frac1{D^2}\sum_i(\ell_i-1)\sigma_i\\
&=\frac1{D^2}\sum_i\sigma_i.
\end{aligned}
```

This proves PS.8. `square`

---

## 7. Uniform stress regression

AS's uniform normalized stress has

```math
\alpha_e=\frac{D^2}{q}
```

on every contact and

```math
\beta_h=\frac1q
```

on every diameter edge.

Thus

```math
\sigma_i=\frac{D^2}{q}
```

for all `i`. PS.7 gives

```math
\sum_i\ell_i\frac{D^2}{q}=D^2,
```

and PS.8 gives

```math
\sum_{cycle}\beta
=\frac1{D^2}r\frac{D^2}{q}
=\frac rq,
```

exactly the uniform mass of `r` cycle edges. PS.5 reduces to

```math
\beta_i=2(1-\cos\theta)\frac{D^2}{q}=\frac1q.
```

So the recurrence recovers the known interior point exactly.

---

## 8. Nonnegativity as an `r`-term scalar system

Since every path stress is positive automatically in the KKT cone, all remaining boundary inequalities are exactly

```math
\beta_i\ge0.
```

By PS.5 these are

```math
\boxed{
\frac{\sin\theta}{\sin\phi_i}
\left(
\cos\phi_i(\sigma_{i-1}-\sigma_i)
+(\sigma_i-\sigma_{i+1})
\right)
\le
(1-\cos\theta)(\sigma_{i-1}+\sigma_i).
}
\tag{8.1}
```

Together with

1. `sigma_i>0`;
2. the harmonic jump recurrence PS.6;
3. normalization PS.7;

this is a complete scalar description of the normalized KKT polygon.

At a PP extreme `s_j`, exactly the two inequalities for cycle edges `j` and `j+2` are equalities; every other one is strict.

---

## 9. Interaction with the walking four-bar circuits

WF extreme `s_j` cuts off the short component on the middle cycle edge `e_{j+1}`. Its two shell intervals come from the LC paths adjacent to that edge.

The four shell contacts crossing the short-body cut are endpoints of four consecutive LC paths. Therefore their KKT coefficients are four consecutive path-stress values

```math
\boxed{
\sigma_j,\sigma_{j+1},\sigma_{j+2},\sigma_{j+3},
}
\tag{9.1}
```

up to cyclic relabeling/orientation.

The four-force and four-moment body equilibrium of WF is therefore an exact projective relation among four consecutive terms of the scalar path-stress sequence.

This is the promised bridge from the polar KKT polygon to the Reuleaux composition mesh.

---

## 10. Immediate quantitative consequences

PR #125 gives

```math
\ell_{max}=O(D^{2/3}).
```

PS.7 therefore gives the crude but uniform cycle-mass floor

```math
D^2
=\sum_i\ell_i\sigma_i
\le\ell_{max}\sum_i\sigma_i,
```

so by PS.8

```math
\boxed{
\sum_{cycle}\beta_i
\ge\frac1{\ell_{max}}
=\Omega(D^{-2/3}).
}
\tag{10.1}
```

This is weaker than the uniform stress's cycle mass `r/q=Omega(D^-1/2)`, but it holds for every normalized KKT stress, including extremes, without a coefficient floor assumption.

Similarly, every path with stress `sigma_i` contributes total pendant beta mass

```math
\frac{\ell_i-1}{D^2}\sigma_i.
```

The entire leaf forest is therefore mechanically encoded by the same `r` positive path variables.

---

## 11. What this changes

The complete `d_H=0` normalized KKT family can now be represented without `q` contact variables:

```text
input:
  integer Reuleaux composition ell_i,
  phi_i=ell_i*pi/q;

variables:
  r positive path stresses sigma_i;

constraints:
  alternating jumps (-1)^i(sigma_{i-1}-sigma_i)
      lie on one sampled first harmonic;
  sum ell_i sigma_i=D^2;
  beta_i(sigma)>=0 from PS.5;

forced coefficients:
  every contact on P_i = sigma_i;
  every pendant beta in star i = sigma_i/D^2;
  cycle beta_i = PS.5.
```

The actual affine dimension remains two because the harmonic jump sequence has two parameters and normalization removes the common level.

---

## 12. Next theorem

The high-value target is now explicit:

> At PP extreme `j`, impose `beta_j=beta_{j+2}=0` in PS.5 and solve for the four consecutive path-stress ratios entering the WF body-bar cut. Compare extreme `j` and `j+1` to obtain a transfer map depending only on the adjacent composition angles `phi_i`.

If the product of these transfer maps around the odd core has no positive fixed point except the uniform/regular case, the nonregular Reinhardt stress polygon collapses.

A source-wide closing step would then need to exclude the surviving regular case using the dense interior population/global optimum descent.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Cycle diameter directions occur at positions t_i with ell_i=t_{i+1}-t_i and
phi_i=ell_i*pi/q. These are exactly the LC Reuleaux composition parts.

KL contact variable a_t is constant across every pendant direction position, so all
ell_i shell contacts on one LC path have one common stress sigma_i>0. Every ell_i-1
pendant diameter edge in that star has
  beta=sigma_i/D^2.

Let d_i=sigma_{i-1}-sigma_i. Eliminating KL's global vector c gives cycle beta
  beta_i=(1-cos theta)(sigma_{i-1}+sigma_i)
         -(sin theta/sin phi_i)(cos phi_i d_i+d_{i+1}),
  theta=pi/q.
The alternating jumps y_i=(-1)^i d_i satisfy the exact variable-step harmonic recurrence
  y_{i+2}=sin(phi_i+phi_{i+1})/sin(phi_i) y_{i+1}
          -sin(phi_{i+1})/sin(phi_i) y_i.

Normalized virial identities:
  sum ell_i sigma_i=D^2,
  sum_cycle beta_i=(1/D^2)sum sigma_i.
Thus the full KKT polygon is an r-variable scalar recurrence; q-r pendant betas and all
q contacts are forced.

At WF extreme j, the four inter-body transition contacts carry four consecutive path
stresses sigma_j,...,sigma_{j+3}. Next: solve beta_j=beta_{j+2}=0 for their transfer
ratios and compare consecutive extremes around the odd core.
```
