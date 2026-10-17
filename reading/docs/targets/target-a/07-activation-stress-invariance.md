> Generated reading edition · [exact source](../../../../docs/targets/target-a/07-activation-stress-invariance.md) · source SHA-256 `74ad9ea0044a413c07a2130fc70241ae56eca7d0ef7c4ca885971e81fde9e920`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A — KKT-stress invariance under monotone activation

This module continues the audited Target A frontier after Sections 152. It records an
exact consequence of the global-minimizer activation sequence from Sections 142–145:
although the activation forest contributes independent rigidity rows, every constraint
created by that monotone activation is invisible to every normalized first-order KKT
stress of the terminal representative.

The result uses global minimum-diameter optimality through Theorem 4.1 and the fact
that every member of the activation sequence is itself a global minimizer. It therefore
closes a loophole left by the non-global regression in Section 152. It does **not**
produce the missing Schur nullity.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 153. Monotone activation preserves the normalized KKT-stress polytope

Use the monotone activation sequence of Theorem 142.1,

```math
A_0,A_1,\ldots,A_s,
\tag{153.1}
```

where each $`A_i`$ is a triangle-free global minimizer of the same cardinality and
diameter $`D`$. At step $`i`$, one currently strict rattler $`r_i`$ moves while all
other points remain fixed; all old active pairs persist; and exactly one new active
pair $`e_i`$ is created.

Label the points consistently through the sequence. Let $`C_i`$ and $`H_i`$ be the
unit-contact and diameter-pair sets of $`A_i`$. Define $`\mathcal K_i`$ to be the set
of normalized KKT stresses from Theorem 4.1:

```math
\mathcal K_i=
\left\{(\alpha,\beta):
\begin{array}{l}
\alpha_{uv}\ge0\quad(uv\in C_i),\\
\beta_{uv}\ge0\quad(uv\in H_i),\\
\sum_{uv\in H_i}\beta_{uv}=1,\\
\displaystyle
\sum_{v:uv\in C_i}\alpha_{uv}(p_u-p_v)
=
\sum_{v:uv\in H_i}\beta_{uv}(p_u-p_v)
\quad\text{for every }u
\end{array}
\right\}.
\tag{153.2}
```

Theorem 4.1 makes every $`\mathcal K_i`$ nonempty. Its trace identity also gives
$`\sum_{C_i}\alpha_{uv}=D^2`$, so $`\mathcal K_i`$ is a compact convex polytope.

> **Theorem 153.1 (KKT-stress invariance under monotone activation).** For every
> activation step $`A_i\to A_{i+1}`$:
>
> 1. the multiplier of the newly created active pair $`e_i`$ is zero in **every**
>    normalized KKT stress of $`A_{i+1}`$;
> 2. restriction to the old active pairs gives a canonical bijection
>    
>    ```math
>    \boxed{\mathcal K_{i+1}\cong\mathcal K_i,}
>    \tag{153.3}
>    ```

>    whose inverse extends a stress by assigning multiplier zero to $`e_i`$.
>
> Consequently
> ```math
> \boxed{\mathcal K_s\cong\mathcal K_0,}
> \tag{153.4}
> ```
> and every active pair created anywhere in the activation sequence has multiplier
> zero in every normalized KKT stress of the terminal configuration $`A_s`$.

## Proof

Fix one step and write $`r=r_i`$ for the moved point. Since $`r`$ is strict in
$`A_i`$, no active unit or diameter pair of $`A_i`$ is incident to $`r`$. Theorem
142.1 says that exactly one new active pair is created and that every old active pair
persists. Hence at $`A_{i+1}`$, the point $`r`$ is incident to exactly one active
pair, namely $`e_i`$.

Suppose first that $`e_i=rv`$ is a unit contact. Then $`r`$ has exactly one unit
neighbor and no diameter neighbor. The equilibrium equation (4.2) at $`r`$ is

```math
\alpha_{e_i}(p_r-p_v)=0.
\tag{153.5}
```

The edge vector is nonzero, so

```math
\boxed{\alpha_{e_i}=0}
\tag{153.6}
```

for every $`(\alpha,\beta)\in\mathcal K_{i+1}`$.

If instead $`e_i=rv`$ is a diameter pair, then $`r`$ has exactly one diameter
neighbor and no unit neighbor. Equation (4.2) at $`r`$ becomes

```math
0=\beta_{e_i}(p_r-p_v),
\tag{153.7}
```

and therefore

```math
\boxed{\beta_{e_i}=0}
\tag{153.8}
```

for every stress in $`\mathcal K_{i+1}`$. This proves item 1.

Now remove the zero coordinate belonging to $`e_i`$. Every older active pair has the
same two endpoints at the same positions in $`A_i`$ and $`A_{i+1}`$, because the
only moved point was $`r`$ and $`r`$ was incident to no old active pair. Thus every
old active edge vector is unchanged. The equilibrium equations at every fixed point
therefore become exactly the equilibrium equations for $`A_i`$, while at $`r`$ both
sides are zero. The normalization $`\sum\beta=1`$ is unchanged because the new
multiplier is zero. Restriction hence maps $`\mathcal K_{i+1}`$ into
$`\mathcal K_i`$.

Conversely, take any stress in $`\mathcal K_i`$ and assign multiplier zero to
$`e_i`$. The same unchanged old edge vectors satisfy equilibrium at every fixed point,
the moved point again has equation $`0=0`$, and the diameter normalization is
unchanged. This zero-extension belongs to $`\mathcal K_{i+1}`$. Restriction and
zero-extension are inverse maps, proving (153.3).

Iterating the bijection proves (153.4). At each stage the new coordinate is identically
zero on the entire stress polytope, so every pair created at any earlier stage remains
identically zero after all later bijections. $`\square`$

## 153.1 Initial strict rattlers remain universally stress-unloaded

Let $`R_0`$ be any specified set of strict rattlers in $`A_0`$. No active pair of
$`A_0`$ is incident to a point of $`R_0`$. Therefore every active pair incident to
$`R_0`$ in the terminal configuration $`A_s`$ was created during the activation
sequence. Theorem 153.1 gives immediately:

> **Corollary 153.2 (universal unloading of the initial rattler population).** For
> every normalized KKT stress of $`A_s`$, every point of $`R_0`$ is absent from both
> the positive contact-stress support and the positive diameter-stress support.
> Equivalently, every active pair incident to $`R_0`$ has multiplier zero.

Thus eliminating strict rattlers by the globally optimal activation normalization does
not make them visible to the normalized first-order stress system. Section 112 showed
that the original strict-rattler product germ is invisible to local active KKT data;
Theorem 153.1 shows that the particular finite activation process of Section 142 does
not repair that blindness.

## 153.2 Exact separation between activation rigidity rank and KKT load

Let $`F_{\rm act}`$ be the unit-activation forest from Section 144. Lemma 145.1 gives

```math
\operatorname{rank}R_{F_{\rm act}}=|E(F_{\rm act})|,
\tag{153.9}
```

and the quantitative lower bound is

```math
|E(F_{\rm act})|
\ge
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H-2\pi D\}}{2}
\right\rceil.
\tag{153.10}
```

Every edge of $`F_{\rm act}`$ was created during the monotone activation sequence.
Theorem 153.1 therefore gives, simultaneously for **every** terminal normalized KKT
stress,

```math
\boxed{
\alpha_e=0
\qquad(e\in E(F_{\rm act})).
}
\tag{153.11}
```

Hence the activation forest can contribute a large exact rank to the unweighted
unit-distance rigidity matrix while contributing exactly zero positive KKT load:

```math
\boxed{
\text{large activation rigidity rank}
+\text{global optimality}
\not\Longrightarrow
\text{positive KKT stress on the activation forest}.
}
\tag{153.12}
```

This is stronger, in a different direction, than the non-global compatibility
regression of Section 152. Section 152 shows that large activation rank can coexist
with zero monomer-scaffold nullity when global minimum-diameter optimality is omitted.
Section 153 shows that even for the actual global-minimizer activation sequence, the
ordinary normalized first-order KKT stress cannot supply the hoped-for compensating
load: every new activation multiplier is forced to vanish.

## 153.3 Exact scope of the no-go

The theorem does **not** imply that the activation forest is irrelevant. The terminal
active-constraint Jacobian does contain the independent rows (153.9), and the critical
cone is smaller after the activations. A theorem using unweighted active-constraint
geometry, finite-amplitude global-minimizer paths, higher-order feasibility, or the
actual source/plateau/scaffold coupling could still extract useful information.

The later audited Section 156 sharpens this scope. It constructs an exact affine
global-minimizer orthant that releases every created activation pair independently.
Thus the mere presence of the new rows cannot be used as a terminal critical-cone
**locking** mechanism. A surviving use of unweighted geometry must involve finite
collision walls beyond that local orthant or an additional global source-to-scaffold
or cross-cardinality invariant.

What is now ruled out is the direct first-order stress-compensation route: one cannot
argue that the independent activation rows must acquire positive equilibrium stress and
then charge that stress to the boundary response. Along the canonical monotone
activation normalization the entire normalized KKT-stress polytope is unchanged, and
all new rows have identically zero multipliers.

Accordingly a surviving activation-to-Schur theorem must use information outside the
normalized KKT stress polytope. In particular it must exploit the global relation to
the independently chosen smaller optimum, finite collision geometry beyond the exact
Section 156 release orthant, a relation between global-optimum cardinalities, or
another source-to-response invariant.

The authoritative Target A endpoint remains

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\tag{153.13}
```

equivalently

```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{153.14}
```

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
