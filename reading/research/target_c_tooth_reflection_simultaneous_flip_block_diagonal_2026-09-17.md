> Generated reading edition · [exact source](../../research/target_c_tooth_reflection_simultaneous_flip_block_diagonal_2026-09-17.md) · source SHA-256 `681cf6c8bdaee080a3a2fd5fdf683be189bd25fc4c5af93fa1e8f3da03d044d4`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1b07e4165c6b0167c360e69b1699bd4ebb248c97", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_tooth_reflection_simultaneous_flip_block_diagonal_2026-09-17.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "9506534a6581070d04fe819fcdd0865b889e50e10cfed39e70652589206bcca1"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — slow-scale shallow-tooth reflections have a block-diagonal upper obstruction

**Date:** 2026-09-17  
**Status:** proof-only strengthening of the current `eta=3/26` canonical reflection branch; no canonical promotion claimed  
**Scope:** Type-II full-core shallow-tooth branch after perimeter collapse, flat-cap purification, and slow-scale normal dispersion  
**Dependencies:** shallow-tooth reflection alternative; reflection/perimeter collapse; same-center source-hull disk sandwich; fixed-slack midpoint/star theorem; slow-scale central reflection braid; canonical/thick-star refinements  
**Certificate:** `research/verify_target_c_tooth_reflection_simultaneous_flip_block_diagonal_2026_09_17.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The one-tooth reflection argument can be made simultaneous after the existing slow-scale angular dispersion. For a selected family of shallow teeth, the full sets of source points that violate the diameter after reflection are pairwise disjoint. Moreover the union of all those blocker sets is `o(D)`, and cross-module distances have a growing safety margin. The remaining obstruction is therefore block-diagonal rather than source-wide.

Fix

```math
\eta_*={3\over26},\qquad
h_*={\sqrt{303}\over52},\qquad
C_*:=2h_*={\sqrt{303}\over26}<1.
\tag{SF.1}
```

Let

```math
\kappa_D\to\infty,
\qquad
\kappa_D=o(D^{1/4}),
\qquad
w_D:=\kappa_DD^{-1/4}.
\tag{SF.2}
```

The slow-scale theorem supplies a family `J_D` of flat, upper-blocked, exterior-witness-free teeth with

```math
|J_D|>(\rho_*-o(1)){D^{1/4}\over\kappa_D},
\qquad
\rho_*=0.129220199818177\ldots,
\tag{SF.3}
```

whose inward base normals lie in one quadrant and satisfy

```math
\angle(n_i,n_j)
\ge (2-o(1))\kappa_DD^{-1/4}
\qquad(i\ne j).
\tag{SF.4}
```

For the quantitative union bound below, first choose a controlled subfamily

```math
I_D\subset J_D,
\qquad
|I_D|=(\rho_*-o(1)){D^{1/4}\over\kappa_D}.
\tag{SF.5}
```

This is legitimate because the lower bound in (SF.3) permits choosing exactly any asymptotically slightly smaller number of members. This explicit thinning is needed: a lower bound for `|J_D|` alone cannot be multiplied by a per-module upper bound to obtain an upper bound for the blocker union.

For `i in I_D`, write

```math
a_i=p_i-c_it_i,
\quad
b_i=p_i+c_it_i,
\quad
x_i=p_i+h_in_i,
\quad
q_i:=x_i^-=p_i-h_in_i.
\tag{SF.6}
```

Then

```math
|q_i-x_i|=2h_i\le C_*.
\tag{SF.7}
```

Define the full upper-blocker set

```math
\boxed{
U_i:=\{z\in A:\ |z-q_i|>D\}.
}
\tag{SF.8}
```

The conclusions are:

```math
\boxed{U_i\cap U_j=\varnothing\quad(i\ne j),}
\tag{SF.9}
```

```math
\boxed{
|U_i|
\le
\left(
{208\,3^{1/8}\over\sqrt{373}}+o(1)
\right)D^{3/4}
=
(12.3551799707\ldots+o(1))D^{3/4},
}
\tag{SF.10}
```

and therefore, for the controlled subfamily (SF.5),

```math
\boxed{
\left|\bigcup_{i\in I_D}U_i\right|
\le
(1.59653882461\ldots+o(1)){D\over\kappa_D}
=o(D).
}
\tag{SF.11}
```

If all selected apexes `x_i` are replaced simultaneously by `q_i`, the new configuration remains unit-separated. Every diameter violation has the form `q_i z` with `z in U_i` (apart from selected apexes removed from the configuration). There are no cross-module diameter violations. More strongly, if `i!=j` and `z in U_j`, then

```math
\boxed{
|q_i-z|
\le D-\Omega(\kappa_D^2\sqrt D).
}
\tag{SF.12}
```

Thus different reflection modules have a diverging subdiameter safety margin.

---

## 1. No retained tooth has a reflected lower obstruction

The slow-scale construction is performed after deleting the `o(D)` teeth carrying an exterior reflection witness. By the reflection alternative, a retained tooth therefore has neither a strict lower blocker nor a new exact unit contact away from its two symmetric base endpoints. Hence for every original source point `z`,

```math
|q_i-z|\ge1,
\tag{SF.13}
```

with the intended base equalities

```math
|q_i-a_i|=|q_i-b_i|=1.
\tag{SF.14}
```

The only lower-distance issue not covered by this one-tooth statement is a pair of two newly reflected points. Section 6 handles that pair directly.

---

## 2. Every upper blocker is a fixed-slack neighbor of the original apex

Fix `z in U_i`. Then `|z-q_i|>D`, and (SF.7) gives

```math
|z-x_i|
\ge |z-q_i|-|q_i-x_i|
>D-C_*.
\tag{SF.15}
```

Since `x_i,z` are both original source points,

```math
|z-x_i|\le D.
\tag{SF.16}
```

Thus `U_i` lies inside the fixed-slack near-diameter neighbor set of `x_i` with slack `C_*`.

Here

```math
C_*^2={303\over676},
\qquad
1-C_*^2={373\over676},
\qquad
\sqrt{1-C_*^2}={\sqrt{373}\over26}.
\tag{SF.17}
```

The fixed-slack degree theorem therefore gives

```math
\begin{aligned}
|U_i|
&\le
\left(
{8\,3^{1/8}\over\sqrt{1-C_*^2}}+o(1)
\right)D^{3/4}\\
&=
\left(
{208\,3^{1/8}\over\sqrt{373}}+o(1)
\right)D^{3/4},
\end{aligned}
\tag{SF.18}
```

which is (SF.10).

---

## 3. The whole blocker set lies in the tooth's inverse-quarter directional cone

The quarter-power reflection proof uses only the flat-cap radial estimate and the fixed-slack midpoint estimate, so its direction bound applies uniformly to every upper blocker, not just to one chosen or canonical blocker. If

```math
d_{i,z}:={z-x_i\over|z-x_i|},
\qquad z\in U_i,
```

then

```math
\boxed{
\angle(d_{i,z},n_i)
\le(A+o(1))D^{-1/4},
}
\tag{SF.19}
```

where

```math
A:=2\,3^{5/8}+4\,3^{1/8}
=8.56283745460\ldots .
\tag{SF.20}
```

The same fixed-slack star proof says that two near-diameter pairs sharing one source endpoint have ray-direction gap at most

```math
\boxed{
(B+o(1))D^{-1/4},
\qquad
B:=8\,3^{1/8}
=9.17762152352\ldots .
}
\tag{SF.21}
```

The leading constant is independent of the fixed additive slack; the slack contributes only lower-order terms to the midpoint radius.

---

## 4. Full blocker sets for distinct flips are disjoint

Suppose `z in U_i cap U_j` with `i!=j`. Then both `x_i z` and `x_j z` are fixed-slack pairs of length greater than `D-C_*`. Applying (SF.21) at their common endpoint and (SF.19) at both teeth yields

```math
\angle(n_i,n_j)
\le(2A+B+o(1))D^{-1/4}.
\tag{SF.22}
```

Numerically,

```math
2A+B
=26.3032964327\ldots .
\tag{SF.23}
```

But (SF.4) gives

```math
\angle(n_i,n_j)
\ge(2-o(1))\kappa_DD^{-1/4},
```

and `kappa_D->infinity`. The two inequalities are incompatible for sufficiently large `D`. This proves (SF.9).

Now use the controlled cardinality (SF.5), not merely the lower bound (SF.3). From (SF.9) and (SF.18),

```math
\begin{aligned}
\left|\bigcup_iU_i\right|
&=\sum_i|U_i|\\
&\le
\left(
\rho_*{208\,3^{1/8}\over\sqrt{373}}+o(1)
\right){D\over\kappa_D}.
\end{aligned}
\tag{SF.24}
```

The leading coefficient is

```math
\boxed{
\rho_*{208\,3^{1/8}\over\sqrt{373}}
=1.59653882460\ldots .
}
\tag{SF.25}
```

This proves (SF.11). For example, taking `kappa_D=log D` leaves `(rho_*-o(1))D^(1/4)/log D` simultaneous flips whose entire upper-obstruction union has size at most `(1.59654+o(1))D/log D`.

---

## 5. Two-shore radial localization

Let `o` be the full-source circumcenter. For every flat selected tooth, the existing same-center argument gives

```math
\angle(o-x_i,n_i)=O(D^{-1/4}),
\qquad
|x_i-o|={D\over2}+O(\sqrt D).
\tag{SF.26}
```

Since `|q_i-x_i|=O(1)`,

```math
\boxed{
\angle(q_i-o,-n_i)=O(D^{-1/4}),
\qquad
|q_i-o|={D\over2}+O(\sqrt D).
}
\tag{SF.27}
```

For `z in U_i`, let `m=(x_i+z)/2`. The fixed-slack midpoint theorem gives

```math
|m-o|=O(D^{3/4}).
\tag{SF.28}
```

Because

```math
z-o=2(m-o)-(x_i-o),
```

and `|z-x_i|>D-C_*`, we obtain uniformly over the full blocker set

```math
\boxed{
\angle(z-o,n_i)=O(D^{-1/4}),
\qquad
|z-o|={D\over2}+O(\sqrt D).
}
\tag{SF.29}
```

The radial lower bound in (SF.29) follows from

```math
|z-o|
\ge |z-x_i|-|x_i-o|
>{D\over2}-O(\sqrt D),
```

and the upper bound follows from the source-hull disk sandwich.

The selected normal spacing dominates the `O(D^-1/4)` directional errors by the factor `kappa_D->infinity`. Hence different modules are separated on either shore by

```math
\boxed{
\operatorname{dist}(q_i,q_j),
\operatorname{dist}(U_i,U_j)
=\Omega(\kappa_DD^{3/4})
\qquad(i\ne j).
}
\tag{SF.30}
```

---

## 6. Simultaneous reflection creates no reflected-apex collision

All selected inward normals lie in one quadrant. By (SF.27), the central angle between `q_i-o` and `q_j-o` is at most `pi/2+o(1)`. Their radii are `D/2+O(sqrt D)`, so

```math
|q_i-q_j|
\le\left({1\over\sqrt2}+o(1)\right)D
<D
\tag{SF.31}
```

for large `D`.

At the other end, (SF.4) and (SF.27) give a central-angle lower bound

```math
\angle(q_i-o,q_j-o)
\ge(2-o(1))\kappa_DD^{-1/4}.
\tag{SF.32}
```

The radial lower bound `D/2-O(sqrt D)` then gives

```math
|q_i-q_j|
=\Omega(\kappa_DD^{3/4})>1.
\tag{SF.33}
```

Thus pairs of newly reflected apexes lie strictly inside the admissible interval `(1,D)`.

---

## 7. Cross-module upper pairs have a diverging safety margin

Fix `i!=j` and `z in U_j`. By (SF.27) and (SF.29), the central angle between `q_i-o` and `z-o` equals `pi-delta`, where

```math
\delta\ge(2-o(1))\kappa_DD^{-1/4}.
\tag{SF.34}
```

If the actual `delta` is larger, the estimate below only improves. Both radii are at most `D/2+O(sqrt D)`. Hence

```math
|q_i-z|^2
=(r_i+r_z)^2-2r_ir_z(1-\cos\delta).
\tag{SF.35}
```

The first term is

```math
(r_i+r_z)^2=D^2+O(D^{3/2}),
\tag{SF.36}
```

whereas monotonicity of `1-cos(delta)` and the lower bound (SF.34) give

```math
2r_ir_z(1-\cos\delta)
=\Omega(\kappa_D^2D^{3/2}).
\tag{SF.37}
```

Since `kappa_D->infinity`, the negative term dominates the radial `O(D^(3/2))` uncertainty. Therefore

```math
|q_i-z|^2
\le D^2-\Omega(\kappa_D^2D^{3/2}).
\tag{SF.38}
```

The hypothesis `kappa_D=o(D^(1/4))` makes this deficit `o(D^2)`, so dividing by `D+|q_i-z|=Theta(D)` gives

```math
\boxed{
|q_i-z|
\le D-\Omega(\kappa_D^2\sqrt D),
}
\tag{SF.39}
```

which is (SF.12).

---

## 8. Exact block-diagonal form of the simultaneous flip

Put

```math
X:=\{x_i:i\in I_D\},
\qquad
Q:=\{q_i:i\in I_D\},
\qquad
A':=(A\setminus X)\cup Q.
\tag{SF.40}
```

Pairs of unchanged points retain their original distances in `[1,D]`. For `q_i` and an unchanged original point `z`, Section 1 gives the lower bound `|q_i-z|>=1`; if the upper bound fails, then `z in U_i` by definition. Pairs `q_i,q_j` lie in `(1,D)` by Section 6.

Therefore

```math
\boxed{
|u-v|>D
\Longrightarrow
\{u,v\}=\{q_i,z\}
\text{ for some }i,
\quad z\in U_i\setminus X.
}
\tag{SF.41}
```

The sets `U_i` are pairwise disjoint, their controlled union is `o(D)`, and every nonmatching pair `q_i-U_j` has the diverging margin (SF.39). The simultaneous reflected configuration is thus unit-separated and its entire infeasibility is a collection of independent diagonal upper modules.

---

## 9. Frontier effect

For every slow scale `kappa_D`, the branch contains

```math
(\rho_*-o(1)){D^{1/4}\over\kappa_D}
```

pairwise-separated exact tooth flips that can be performed simultaneously. Their full upper-blocker sets are pairwise disjoint, and after controlled thinning their union contains only

```math
O(D/\kappa_D)=o(D)
```

fixed source vertices. Cross-module lower constraints have `Omega(kappa_D D^(3/4))` separation, and cross-module upper constraints have `Omega(kappa_D^2 sqrt D)` slack below `D`.

This does not close C-II. Every selected tooth is in the upper-blocked branch, so its diagonal set `U_i` is nonempty. The remaining task is local: repair one module `(q_i,U_i)` without creating a unit violation against the rest of the source. Because different modules have growing geometric separation and cross-module diameter margin, any `O(1)` repair can now be analyzed module-by-module.

Two concrete next routes are:

1. take an appropriate contact-connected closure of `U_i` and prove that an inward translation or rotation of that closure repairs every `q_i-U_i` violation without creating a new unit violation at its boundary; or
2. use the canonical exposed blocker head `y_i in U_i` and the thick-star support-depth stratification to construct a compensated finite flip of `(x_i,y_i)`, then show that the remaining members of `U_i` cannot all stay obstructive.

**Disposition:** upgraded the one-tooth reflection obstruction to a simultaneous `D^(1/4-o(1))` exact-flip system with pairwise-disjoint blocker caps and an `o(D)` controlled blocker union. The initial union-coefficient bookkeeping was audited and corrected by explicitly thinning to a family of cardinality `(rho_*-o(1))D^(1/4)/kappa_D` before applying the per-module upper bound. C-II and Level I remain open.
