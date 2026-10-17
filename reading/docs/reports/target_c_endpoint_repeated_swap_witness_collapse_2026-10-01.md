> Generated reading edition · [exact source](../../../docs/reports/target_c_endpoint_repeated_swap_witness_collapse_2026-10-01.md) · source SHA-256 `9e669569a3476343a927e2dd9881ace22ad6664dc444e4fc1c3a5e332c541fd4`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-DA73645EFD6D","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- repeated endpoint-swap witnesses collapse to an ultra-near-unit row rail

Date: 2026-10-01
Base main: 5ff8caddec4bd2b56b1934abe8602f071b0c61ba
Status: proof-only; C-II remains open.

## 1. Statement

Work in the open-witness-cell fixed-star branch after the exact finite swap theorem.
Take a family of pairwise nonadjacent ONE-SIGN phase-changing interfaces on one
retained shore, and keep only one sign of the phase step. Thus their exact swap axes

```math
w_i={u_i-u_{i+1}\over |u_i-u_{i+1}|}
```

have one common orientation and satisfy

```math
|w_i-w_j|=O_K(D^{-1})
\tag{1}
```

uniformly. Put

```math
s_i:=|u_i-u_{i+1}|\le {4K\over D}.
\tag{2}
```

Choose one previously strict inactive pair forced by the exact finite swap at each
ONE-SIGN interface.

Then:

1. one unordered source pair can be selected at at most two retained interfaces;
2. if the same pair is selected at two distinct interfaces, then
   ```math
   \boxed{
   |xy|-1=O_K(D^{-2})
   }
   \tag{3}
   
   ```
   in the near-unit case, or
   ```math
   \boxed{
   D-|xy|=O_K(D^{-2})
   }
   \tag{4}
   
   ```
   in the near-diameter case;
3. every twice-selected pair also satisfies
   ```math
   \boxed{
   d_{\mathbb{RP}^1}([xy],[u_*])=O_K(D^{-1}),
   }
   \tag{5}
   
   ```
   where $`[u_*]`$ is the common row-direction window;
4. the family of all twice-selected pairs is already a matching;
5. for fixed $`K`$, only $`O_K(1)`$ source pairs can satisfy simultaneously
   (4) and (5).

Consequently, if a linear number of the chosen ONE-SIGN witnesses are reused at two
interfaces, then all but $`O_K(1)`$ of the repeated witnesses are near-unit and they
form a linear vertex-disjoint matching with

```math
\boxed{
1<|xy|\le1+O_K(D^{-2}),
\qquad
d_{\mathbb{RP}^1}([xy],[u_*])=O_K(D^{-1}).
}
\tag{6}
```

So repeated use of the inactive-slack escape cannot hide in a large family of
almost-diameters. It collapses to an ultra-near-unit row-parallel matching.

No high-$`t`$ routing-hub or host-margin theorem is used.

## 2. A pair can move at at most two retained interfaces

The retained interfaces are pairwise nonadjacent, so their physical middle layers
are pairwise disjoint. The exact swap at interface $`i`$ translates only its middle
layer.

An unordered pair $`xy`$ changes length under that swap exactly when one of $`x,y`$
lies in the translated layer and the other does not. Since the pair has two
endpoints, it can be changed by at most two pairwise-disjoint layer translations.

If it changes under two distinct layers $`R_i,R_j`$, then one endpoint lies in
$`R_i`$ and the other in $`R_j`$. Orient $`r=y-x`$. The two inward incidence
vectors are therefore exact negatives:

```math
\boxed{n_j=-n_i.}
\tag{7}
```

This proves the multiplicity-two statement.

## 3. Common orientation of the swap axes

All retained train directions lie in one Section-90 projective interval of width
$`4K/D`$. For a phase-changing interface, the swap axis is the quarter-turn of the
midpoint of its two train directions, with orientation determined by the sign of the
phase step.

After retaining one of the two phase-step signs, all axes use the same ordinary
lift. Hence for some constant $`C_K`$,

```math
\boxed{|w_i-w_j|\le {C_K\over D}}
\tag{8}
```

for every two retained interfaces. One may take a crude $`C_K=8K`$; no optimization
is used below.

## 4. A repeated near-unit witness has one extra order of slack

Suppose the same previously strict pair is driven to the lower constraint by the two
exact swaps at $`i,j`$. Write

```math
\ell:=|r|>1,
\qquad
A:=\ell^2-1>0.
```

Orient $`n:=n_i=-n_j`$. The exact swap equations are

```math
\ell_i'^2
=
\ell^2-2s_i(n\cdot w_i)+s_i^2,
\tag{9}
```

```math
\ell_j'^2
=
\ell^2+2s_j(n\cdot w_j)+s_j^2.
\tag{10}
```

The two lower-bound obstructions give

```math
n\cdot w_i
\ge {A+s_i^2\over2s_i},
\tag{11}
```

```math
n\cdot w_j
\le -{A+s_j^2\over2s_j}.
\tag{12}
```

Subtract. With

```math
H_{ij}:={s_is_j\over s_i+s_j},
```

we obtain

```math
A+s_is_j
\le
2\ell\,|w_i-w_j|\,H_{ij}.
\tag{13}
```

Now

```math
H_{ij}\le\min(s_i,s_j)\le {4K\over D},
```

```math
|w_i-w_j|=O_K(D^{-1}),
```

and every exact-swap near-unit witness already satisfies
$`\ell\le1+4K/D`$. Therefore

```math
A=O_K(D^{-2}),
```

and hence

```math
\ell-1={A\over\ell+1}=O_K(D^{-2}).
```

This proves (3).

The same inequalities give directional collapse. From (11),
$`n\cdot w_i>0`$. From (12),

```math
n\cdot w_i
\le n\cdot(w_i-w_j)
\le \ell |w_i-w_j|.
```

Thus

```math
0<
{n\over\ell}\cdot w_i
\le O_K(D^{-1}).
\tag{14}
```

Since $`w_i`$ is the common transverse direction up to $`O_K(D^{-1})`$, the
projective direction of $`r`$ lies within $`O_K(D^{-1})`$ of the row direction.
This is (5) in the near-unit case.

## 5. A repeated near-diameter witness has the same collapse

Now suppose the same pair is driven to the upper constraint by both exact swaps.
Put

```math
\ell<D,
\qquad
B:=D^2-\ell^2>0.
```

Equations (9)--(10) give

```math
n\cdot w_i
\le {s_i\over2}-{B\over2s_i},
\tag{15}
```

```math
n\cdot w_j
\ge {B\over2s_j}-{s_j\over2}.
\tag{16}
```

Subtracting in the opposite order and multiplying by $`2H_{ij}`$ yields

```math
B
\le
2\ell |w_i-w_j|H_{ij}+s_is_j.
\tag{17}
```

Here

```math
\ell=D-O_K(D^{-1}),
\quad
|w_i-w_j|=O_K(D^{-1}),
\quad
H_{ij}=O_K(D^{-1}).
```

Therefore

```math
B=O_K(D^{-1}).
```

Since $`D+\ell\asymp D`$,

```math
D-\ell={B\over D+\ell}=O_K(D^{-2}),
```

which proves (4).

For direction, (15) gives $`n\cdot w_i\le s_i/2`$, while (16) and (8) give

```math
n\cdot w_i
\ge
-{s_j\over2}-\ell |w_i-w_j|.
```

Divide by $`\ell\asymp D`$:

```math
\left|{n\over\ell}\cdot w_i\right|
=O_K(D^{-1}).
\tag{18}
```

Again this is exactly (5).

A pair cannot switch between the near-unit and near-diameter witness types for large
$`D`$, because the original length windows are disjoint.

## 6. Twice-selected witnesses form a matching

Choose exactly one inactive witness at each retained interface. Let $`e`$ be a pair
selected twice, at layers $`R_i,R_j`$. By Section 2, its two endpoints lie in those
two layers.

Suppose another twice-selected pair $`f\ne e`$ shared one endpoint with $`e`$. That
common endpoint belongs to one definite retained layer, say $`R_i`$. Since $`f`$ is
selected twice, $`R_i`$ must be one of its two selected layer tags as well.

But the witness selection chose only one unordered pair at interface $`i`$. Both
$`e`$ and $`f`$ cannot be selected there. Contradiction.

Hence

```math
\boxed{\text{all distinct twice-selected witnesses are vertex-disjoint}.}
\tag{19}
```

No graph-degree thinning is needed.

## 7. Row-parallel ultra-near-diameters have globally bounded population

Fix constants $`A,L>0`$. Consider any family $`\mathcal E_D`$ of source pairs with

```math
D-{A\over D^2}\le |e|<D
\tag{20}
```

and

```math
d_{\mathbb{RP}^1}([e],[u_*])\le {L\over D}.
\tag{21}
```

We prove

```math
\boxed{|\mathcal E_D|=O_{A,L}(1).}
\tag{22}
```

Orient every pair consistently with $`+u_*`$. Write its vector as $`r_e`$, midpoint
as $`m_e`$, and endpoints as

```math
x_e=m_e-\frac12r_e,
\qquad
y_e=m_e+\frac12r_e.
```

Take two pairs $`e,f`$. Both cross-endpoint distances are source distances and hence
at most $`D`$:

```math
|x_e-y_f|\le D,
\qquad
|y_e-x_f|\le D.
```

Adding their squares gives the parallelogram identity

```math
2|m_f-m_e|^2
+\frac12|r_e+r_f|^2
\le2D^2.
\tag{23}
```

The angle between $`r_e,r_f`$ is at most $`2L/D`$, so

```math
\frac12|r_e+r_f|
\ge
\left(D-{A\over D^2}\right)\cos{L\over D}.
\tag{24}
```

Equations (23)--(24) imply, for all sufficiently large $`D`$,

```math
|m_f-m_e|^2\le L^2+1.
\tag{25}
```

Also

```math
|r_e-r_f|
\le {A\over D^2}+2D\sin{L\over D}
\le 2L+1
\tag{26}
```

for large $`D`$. Therefore all consistently oriented $`x_e`$ endpoints lie in one
disk of radius depending only on $`A,L`$, and the same holds for all $`y_e`$.

The source is unit separated. Disjoint radius-$`1/2`$ disks around source points give
a constant packing bound in any fixed-radius disk. Hence only $`O_{A,L}(1)`$
possible $`x_e`$ and $`O_{A,L}(1)`$ possible $`y_e`$ occur, proving (22).

Apply this with the uniform constants supplied by (4)--(5). Thus:

```math
\boxed{
\text{only }O_K(1)\text{ twice-selected witnesses can be near-diameter.}
}
\tag{27}
```

## 8. Density consequence

Suppose a pairwise-nonadjacent, common-step-orientation ONE-SIGN family has $`M`$
interfaces. Let

- $`d`$ be the number of distinct witness pairs selected twice;
- $`s`$ be the number selected once.

Then

```math
M=s+2d,
\qquad
N_{\rm distinct}=s+d=M-d.
\tag{28}
```

If

```math
d<{M\over4},
```

then

```math
\boxed{N_{\rm distinct}>{3M\over4}.}
\tag{29}
```

If

```math
d\ge {M\over4},
```

then there are at least $`M/4`$ distinct repeated witnesses. By (27), all but
$`O_K(1)`$ are near-unit. By (19) they are already vertex-disjoint. Therefore

```math
\boxed{
\text{at least }{M\over4}-O_K(1)
\text{ form an ultra-near-unit row-parallel matching.}
}
\tag{30}
```

This is stronger than the generic inactive near-diameter matching reduction: the
repeated upper-slack escape is globally finite.

Starting from any linear ONE-SIGN population on the current shore, one loses at most
a factor two to choose nonadjacent interfaces and at most a factor two to choose one
phase-step orientation. Thus the theorem always applies to a linear subpopulation.

## 9. Frontier effect

The ONE-SIGN inactive-slack branch now has the exact fork

```math
\boxed{
\text{mostly distinct }O(D^{-1})\text{ inactive witnesses}
}
```

or

```math
\boxed{
\text{linear vertex-disjoint }
1+O(D^{-2})
\text{ row-parallel matching}.
}
```

A linear repeated near-diameter family is impossible.

The near-unit matching is not a local diagonal family from the retained complete
grid: the local-immunity theorem already excludes those diagonals as exact-swap
witnesses. It is therefore a genuinely nonlocal source-level object.

The next closing target is to couple this ultra-near-unit matching to the complete
transverse train shore, or to solve the mostly-distinct inactive constraint system
simultaneously. The TWO-SIGN and exact-phase TB2 branches remain open.

No computation, verifier, numerical experiment, CI result, or unexecuted verifier
code is used.

## Salvage provenance and lifecycle

Copied from `proof/target-c-endpoint-repeated-swap-witness-collapse-20261001` at tip
`2cc171084dfe434f3c3242cbcf1f8c841ab39976`. This is a proof-only local result under
the open-witness-cell fixed-star hypotheses and exact finite swap theorem. It does not
close C-II or Level I, and remains unreviewed pending independent audit. No verifier or
computation is included.
