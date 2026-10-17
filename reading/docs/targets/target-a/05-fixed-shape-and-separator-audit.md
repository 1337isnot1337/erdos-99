> Generated reading edition · [exact source](../../../../docs/targets/target-a/05-fixed-shape-and-separator-audit.md) · source SHA-256 `8db1828cdffd639736d3b1a5ad867e782fee431d5b54b73b92e712e0c6fbd9e9`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — fixed-shape strain and cage-to-response audit

This module continues the post-v1.7 audited addenda after Sections 146–147. It records two theorem-level strengthenings and one exact quantitative formulation that arose while rechecking the five provisional Target A claims.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 148. Fixed-shape homothetic same-hull add-one theorem

Section 137 proves the free-rhombus case when the accumulated homothetic strain stays bounded below. The same argument in fact works for every fixed full-dimensional convex triangular-lattice polygon.

Let
```math
\Lambda=\mathbb Z e_1+\mathbb Z e_2,
\qquad
e_1=(1,0),
\qquad
e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
```
and let $`K\subset\mathbb R^2`$ be a fixed convex polygon whose vertices lie in $`\Lambda`$, with $`0\in\operatorname{int}K`$. For integer $`L\ge1`$, put
```math
P_L=\Lambda\cap LK.
```
Since the vertices of $`LK`$ are themselves lattice points,
```math
\operatorname{conv}P_L=LK.
\tag{148.1}
```
For fixed $`\alpha>0`$, define the homothetically strained patch
```math
P^{\rm str}_{L,\alpha}
=\left(1+\frac{\alpha}{L}\right)P_L
\tag{148.2}
```
and its hull
```math
H_{L,\alpha}
=\operatorname{conv}P^{\rm str}_{L,\alpha}
=(L+\alpha)K.
\tag{148.3}
```

> **Theorem 148.1 (fixed-shape same-hull add-one theorem).** For every fixed $`\alpha>0`$ there is $`L_0(K,\alpha)`$ such that for every integer $`L\ge L_0(K,\alpha)`$, the same hull $`H_{L,\alpha}`$ contains a unit-separated set $`P^+_{L,\alpha}`$ with
> 

```math
> \boxed{
> |P^+_{L,\alpha}|=|P^{\rm str}_{L,\alpha}|+1.
> }
> \tag{148.4}
> 
```

### Proof

Let $`n=(0,1)`$, normal to the lattice line $`\mathbb Re_1`$. Because $`0\in\operatorname{int}K`$, choose $`r>0`$ such that
```math
r\mathbb B\subset K.
\tag{148.5}
```
Fix any
```math
0<a<\alpha r.
\tag{148.6}
```
Split the unstrained patch along the row line and move the two halves apart:
```math
Q_L=
\{p+an:p\in P_L,\ n\cdot p\ge0\}
\cup
\{p-an:p\in P_L,\ n\cdot p<0\}.
\tag{148.7}
```
Distances within either half are unchanged. For points in opposite halves, the normal component of their difference strictly increases by $`2a`$ while the tangential component is unchanged. Hence $`Q_L`$ is unit-separated and
```math
|Q_L|=|P_L|.
\tag{148.8}
```

The two translations stay inside the strained hull. Indeed, (148.5)–(148.6) give $`\pm an\in\alpha K`$, and therefore
```math
p\pm an\in LK+\alpha K=(L+\alpha)K=H_{L,\alpha}
\tag{148.9}
```
for every $`p\in LK`$. Thus
```math
Q_L\subset H_{L,\alpha}.
\tag{148.10}
```

Apply the same row split to the entire triangular lattice. After one global translation this is exactly a honeycomb/triangular lattice packing with a positive linear gap defect of width $`2a`$. The Kuperberg–Kuperberg–Kuperberg gap theorem gives a finite positive-gain replacement: there are finite old and new center sets $`S,T`$ with
```math
|T|>|S|
\tag{148.11}
```
such that replacing $`S`$ by $`T`$ preserves unit separation. Retain any one positive-gain connected replacement component and, if necessary, discard additional gain so that it is enough to conclude at least one extra point.

The witness is finite and independent of $`L`$. Because $`0\in\operatorname{int}K`$, the bodies $`LK`$ exhaust the plane. Hence for all sufficiently large $`L`$, every lattice preimage of the finite old witness belongs to $`P_L`$, so $`S\subset Q_L`$. The expanding hulls $`(L+\alpha)K`$ likewise eventually contain the finite replacement set $`T`$. Consequently
```math
(Q_L\setminus S)\cup T\subset H_{L,\alpha}
\tag{148.12}
```
is unit-separated and has more than $`|P_L|`$ points. Selecting any $`|P_L|+1`$ of them proves (148.4). $`\square`$

The fixed-shape and full-dimensional hypotheses are real. The theorem does not by itself apply to a family whose normalized inradius tends to zero, to an arbitrary sparse lattice subset, or to an embedded monomer domain whose exterior source points block the row split or the finite replacement.

---

# 149. A first-transition cage does not locally force a Schur separator

The locked-triangle alternative is exact, and Section 139.1 gives exact local cages. The remaining implication
```math
\text{locked first-transition cage}
\Longrightarrow
\text{Schur rank loss}
\tag{149.1}
```
requires genuinely global source-to-scaffold information. It does not follow from local cage geometry plus planarity/genericity of the response.

> **Proposition 149.1 (local cage-to-Schur no-go).** There are exact source-side first-transition cage data of the type in Proposition 139.1 and, independently, planar strict-conflict boundary-response data whose generic response matrix has full column rank. Hence no theorem using only the local cage constraints, planarity, and generic response algebra can force even one Schur null direction.

### Proof

Use the exact two-leaf source gadget of Proposition 139.1 for the source-side cage.

For the response side, fix $`k\ge1`$ and $`0<\varepsilon<1`$, and take right terminals
```math
o_i=(3i,0),
\qquad 1\le i\le k,
\tag{149.2}
```
and left terminals
```math
c_i=(3i,\varepsilon).
\tag{149.3}
```
Each shore is internally unit-separated. Moreover
```math
|c_i-o_i|=\varepsilon<1,
\qquad
|c_i-o_j|>1\quad(i\ne j).
\tag{149.4}
```
Thus the strict conflict graph consists exactly of the $`k`$ disjoint edges $`c_io_i`$. It is planar. With independent generic edge variables, its boundary response matrix is diagonal with nonzero diagonal entries, so
```math
\boxed{
\operatorname{rank}S=k,
\qquad
\ker S=0.
}
\tag{149.5}
```
If a nonempty interior block is desired, add disjoint matched interior $`B`$-$`Z`$ pairs far from these terminals. The interior basis block is then diagonal and invertible, and the Schur complement on (149.2)–(149.3) remains diagonal and full rank.

Therefore the local cage statement and the local planar-response statement are logically compatible with zero response nullity. What is absent is exactly the global invariant tying the genuine source transition to the plateau-terminalized response. $`\square`$

This proposition is not a counterexample to Target A: the source gadget and response instance are not claimed to arise from one global minimizer. Its role is to certify that Section 140 is a genuine transport gap rather than an omitted local corollary.

---

# 150. Small-gap witness size: what is now proved and what is still missing

Section 146 proves a genuine quantitative asymptotic statement. If $`\kappa_*(d)`$ is the minimum number of deleted old centers in any positive-gain finite rearrangement of any width-$`d`$ triangular gap packing, then
```math
\boxed{
\kappa_*(d)\to\infty
\qquad(d\downarrow0).
}
\tag{150.1}
```
Thus bounded-cardinality Kuperberg witnesses are impossible as the gap closes.

That lower-complexity theorem does not supply an upper bound on the spatial support needed to realize a witness. To isolate the separate finite-container question, define $`W(d)`$ to be the infimum support radius, after a lattice-period translation parallel to the gap, over all finite positive-gain witnesses for the width-$`d`$ triangular gap packing. The Kuperberg theorem gives only
```math
\boxed{W(d)<\infty\qquad(d>0).}
\tag{150.2}
```
No explicit asymptotic upper bound for $`W(d)`$ is part of the active theorem stack.
Unpromoted working reports may analyze the free aligned construction, but they do not
control blockers in the embedded source/scaffold domain.

For a vanishing accumulated homothetic strain $`\alpha_L\to0`$, Theorem 148.1 gives an exact sufficient condition. If $`r\mathbb B\subset K`$ and the row split uses
```math
a_L=\frac r2\alpha_L,
\qquad
d_L=2a_L=r\alpha_L,
\tag{150.3}
```
then
```math
\boxed{
W(r\alpha_L)=o(L)
\Longrightarrow
\alpha_1(H_{L,\alpha_L})\ge|P_L|+1
\text{ for all sufficiently large }L.
}
\tag{150.4}
```
Indeed, an $`o(L)`$-radius witness and its old lattice preimages eventually fit inside the $`\Theta(L)`$ interior of the fixed-shape hull. Equation (150.4) is a conditional embedding criterion, not a claimed rate for $`W`$.

The two quantitative questions are therefore distinct:

1. Section 146 proves the **necessary divergence** $`\kappa_*(d)\to\infty`$ of witness cardinality.
2. A useful vanishing-gap same-hull theorem would need a sufficiently small **upper bound** on support radius $`W(d)`$, for example enough to verify (150.4) at the actual scaffold scale.

The Kuperberg paper itself does not state an asymptotic block-size/support-radius
rate as $`d\downarrow0`$. Any explicit rate requires a separate proof and canonical
audit, and an exterior-compatible support theorem remains a legitimate target.

---

# 151. Exact status after the five-claim check

The selected claims now have the following theorem-level disposition:

1. fixed $`\alpha>0`$ homothetic same-hull add-one: **proved**, now for every fixed full-dimensional triangular-lattice polygon;
2. first-triangle perturbation: **proved in the exact cone-alternative form**, with a locked-triangle branch that cannot be discarded;
3. cage $`\Rightarrow`$ Schur separator: **not a local theorem**; Proposition 149.1 proves an additional global transport invariant is necessary;
4. two-leaf cage gadget: **proved exactly** by the symbolic family in Section 139.1; and
5. Kuperberg witness size as gap closes: **partially quantified** by
$`\kappa_*(d)\to\infty`$, with no promoted exterior-compatible support upper bound.

The direct Target A endpoint is unchanged:
```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\tag{151.1}
```
equivalently
```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{151.2}
```
The remaining useful routes are an exterior-compatible version of Theorem 148.1, a genuinely global locked-cage-to-Schur transport, a quantitative support-radius theorem strong enough for (150.4), or a different invariant coupling the source to the plateau-terminalized response.
