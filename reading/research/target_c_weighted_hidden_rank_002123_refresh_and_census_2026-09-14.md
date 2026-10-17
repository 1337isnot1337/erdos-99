> Generated reading edition · [exact source](../../research/target_c_weighted_hidden_rank_002123_refresh_and_census_2026-09-14.md) · source SHA-256 `85e78dcad7de6b19ddc61edbdbff2cfe6e5ac912f789a381c1cec86adab28f59`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "73d644145fa4097a4e84df58febe8a69860e8b24", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_weighted_hidden_rank_002123_refresh_and_census_2026-09-14.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "3083f07f05c0894ab152381c27ddebba41624b93b206c23ce791211b64a810c0"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II - weighted hidden-rank minimax: audited 0.002123 refresh and equality census

**Date:** 2026-09-14
**Parent theorem:** `target_c_weighted_outer_hidden_rank_minimax_2026-09-14.md`
**New scalar input:** independently audited `g=0.002123` minimax phase-star theorem
**Status:** algebraic propagation and equality census; C-II remains open

## 1. Why this refresh is needed

The parent hidden-rank theorem was derived from the then-current audited `g=0.0021` endpoint. Its structural statements are parameterized by the weighted outer-flex quantity

```math
F(t,\delta,\kappa)
={9\pi\over2}+{3C_g\over2}-{35t\over4}
+{9\delta\over2}+{3\kappa\over4},
\qquad C_g=2\sqrt{\Delta_2}+g.
```

A newer independent hostile audit now passes

```math
\boxed{g=0.002123}
```

and the propagated safe Type-II scalar threshold

```math
\boxed{
t_0={4\over9}(\pi+\sqrt{\Delta_2})+0.0017327.
}
\tag{RC.1}
```

No structural proof in the hidden-rank theorem changes. Only the endpoint substitution and the derived numerical census change.

## 2. Refreshed endpoint constants

Put

```math
s=\sqrt{\Delta_2},\qquad
\Delta_2={\pi\over2\sqrt3},\qquad
C_{23}=2s+0.002123.
```

At `(t,delta,kappa)=(t_0,0,0)`, direct high-precision substitution gives

```math
q_0=2t_0-\pi
=0.5008998223690961698\ldots,
\tag{RC.2}
```

```math
R_0=7\pi+3C_{23}-{27t_0\over2}
=3.1245702035897932384\ldots,
\tag{RC.3}
```

```math
\boxed{
F_0={R_0-2q_0\over2}
=1.0613852794258004494\ldots .
}
\tag{RC.4}
```

The weighted hidden-rank minimax coefficient becomes

```math
\boxed{
\Theta_0={4F_0\over7}
=0.6065058739576002568\ldots .
}
\tag{RC.5}
```

The associated equality values are

```math
\boxed{{10F_0\over7}=1.5162646848940006420\ldots,}
\tag{RC.6}
```

```math
\boxed{{3F_0\over7}=0.4548794054682001926\ldots,}
\tag{RC.7}
```

```math
\boxed{{6F_0\over7}=0.9097588109364003852\ldots.}
\tag{RC.8}
```

The slight decrease from the older `0.0021` hidden-rank decimal is not a regression in the atomic theorem: the separately propagated safe `t` threshold also increased, and `F` has coefficient `-35/4` in `t`.

## 3. Equality census in the weighted minimax model

Recall the normalized variables

```math
x={L_{OO}\over D},\qquad
z={\operatorname{rank}(H_{OF}|W_{OF}^{priv})\over D},
```

and let `n_r=N_r/D` count receiving good pentagons with private outer degree `r`.

If the weighted minimax bound is asymptotically tight at the formal endpoint, then the parent theorem forces

```math
x=z=\Theta_0+o(1),
\tag{RC.9}
```

```math
{Q-G\over D}=o(1),
\qquad
n_1+n_3+n_4=o(1),
\tag{RC.10}
```

and

```math
n_5={\Theta_0\over2}+o(1)
={2F_0\over7}+o(1).
\tag{RC.11}
```

Because `G<=f<=Q`, (RC.10) also implies

```math
\boxed{Q-f=o(D),\qquad f-G=o(D).}
\tag{RC.12}
```

Thus essentially the entire exceptional-face defect is carried by receiving good pentagons, and almost every such pentagon has private outer degree two or five.

Numerically,

```math
\boxed{n_5=0.3032529369788001284\ldots,}
\tag{RC.13}
```

while

```math
\boxed{
n_2=q_0-n_5
=0.1976468853902960414\ldots .
}
\tag{RC.14}
```

The private excess is

```math
\rho=3n_5={6F_0\over7}
=0.9097588109364003852\ldots,
\tag{RC.15}
```

and the outer-to-flat train density is

```math
\begin{aligned}
y={L_{OF}\over D}
&=2n_2+5n_5+o(1)\\
&=2q_0+{6F_0\over7}+o(1)\\
&=1.9115584556745927248\ldots+o(1).
\end{aligned}
\tag{RC.16}
```

The OO density is

```math
\boxed{x={4F_0\over7}=0.6065058739576002568\ldots.}
\tag{RC.17}
```

Therefore the selected system consumes outer terminal occurrences at density

```math
\begin{aligned}
2x+y
&=R_0+o(1)\\
&=3.1245702035897932384\ldots+o(1).
\end{aligned}
\tag{RC.18}
```

## 4. Outer-boundary saturation at the formal endpoint

The exact outer ledger gives

```math
{b\over D}=\pi+\delta+o(1).
```

At the formal endpoint `delta=0`, the outer face therefore has `pi D+o(D)` contact-edge occurrences. Comparing with (RC.18), the density not consumed by the minimax-equality OO/OF system is

```math
\boxed{
\pi-R_0
=0.0170224500000000000\ldots .
}
\tag{RC.19}
```

The expression is exactly transparent after substituting (RC.1):

```math
\boxed{
\pi-R_0
={27\over2}(0.0017327)-3(0.002123)
=0.01702245.
}
\tag{RC.20}
```

So only about

```math
{0.01702245\over\pi}=0.005418\ldots
```

of the outer occurrence density lies outside the selected OO/flat-pentagon train system in this equality model.

The selected outer occurrences split as

```math
\boxed{2L_{OO}/D=1.2130117479152005136\ldots,}
\tag{RC.21}
```

```math
\boxed{5N_5/D=1.5162646848940006420\ldots,}
\tag{RC.22}
```

```math
\boxed{2N_2/D=0.3952937707805920828\ldots.}
\tag{RC.23}
```

Their sum is (RC.18).

This is a stronger geometric fingerprint than the scalar minimax statement alone: roughly half of all outer terminal occurrences belong to degree-five flat-pentagon fans, another `~0.395D` to degree-two flat pentagons, and `~1.213D` to the two ends of exact OO shears.

## 5. Structured flex dimensions at equality

The same refreshed constants give

```math
\boxed{{\dim K_{out}\over D}\ge {10F_0\over7}
=1.5162646848940006420\ldots-o(1),}
\tag{RC.24}
```

and the explicit hidden-null subspace generated by OO shears plus one common-rotation mode per degree-five pentagon has

```math
\boxed{{\dim U_0\over D}\ge {6F_0\over7}
=0.9097588109364003852\ldots-o(1).}
\tag{RC.25}
```

The degree-five rotation modes have the five-step outer-boundary normal form proved in `target_c_degree5_outer_rotation_boundary_normal_form_2026-09-14.md`.

## 6. Scope

This is an endpoint/equality diagnostic, not a claim that an actual survivor attains `(t,delta,kappa)=(t_0,0,0)`. The audited `0.002123` theorem is itself an exclusion/floor mechanism. The purpose of the census is to identify the limiting model that any attempt to saturate the combined weighted inequalities would have to approach.

No near-complete train-crossing product, diameter rank defect, or source-preserving strict descent is inferred from the outer-boundary saturation alone.

**Disposition:** refreshed strongest audited scalar inputs and equality census. C-II remains open.
