> Generated reading edition · [exact source](../../../../docs/targets/target-a/20-zero-slack-normalization.md) · source SHA-256 `29050c565c02816f425e09f1a01598e1012b689d0508618465e406cf3918ca40`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — locked-transition or zero-slack response normalization

This audited addendum follows Sections 163--167.  It promotes the fixed-hull
terminalization mechanism that had previously appeared only in a working report and
then applies the Section-165 response alignment to the zero-slack branch.  The main
new consequence is exact: in that branch every actual response vertex, hence every
Schur terminal, can be matched to a distinct point of a triangle-free global optimum
in the same source hull.  There is no `widehat p_H` exceptional set.  A second exact
dichotomy either descends the triangle-free counterexample to the smaller plateau
endpoint or produces pairwise disjoint source gates crossing the smaller-optimum hull.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 168. Locked-transition or zero-slack normalization

Let
```math
A\subset H=\operatorname{conv}A,
\qquad |A|=N,
\qquad \operatorname{diam}A=D=D(N)
\tag{168.1}
```
be a triangle-free global optimum.  Put
```math
M=\alpha_1(H),
\tag{168.2}
```
the maximum cardinality of a unit-separated subset of the fixed source hull.  Since
`A subset H`, one has `M>=N`; since every `M`-point packing in `H` has diameter at
most `D`, monotonicity gives
```math
D(M)=D.
\tag{168.3}
```

## 168.1 Finite cage-or-capacity terminalization

> **Theorem 168.1 (locked-transition or triangle-free zero-slack endpoint).**  At
> least one of the following holds.
>
> 1. **Locked-transition branch.**  There are an integer `q` with
>    

```math
>    N<q\le M
>    \tag{168.4}
>    
```
>    and a `q`-point unit-separated global optimum `P subset H` of diameter `D`
>    containing a unit equilateral triangle `T_*` such that
>    

```math
>    \boxed{
>    a_{ij}(v)=0
>    \qquad(ij\in E(T_*),\ v\in\mathcal C_H(P)).
>    }
>    \tag{168.5}
>    
```
>    Thus all three sides of `T_*` are universally first-order locked in the actual
>    fixed-hull feasible cone.
>
> 2. **Zero-slack triangle-free branch.**  There is a triangle-free global optimum
>    

```math
>    A^{\max}\subset H,
>    \qquad |A^{\max}|=M,
>    \qquad \operatorname{diam}A^{\max}=D,
>    \tag{168.6}
>    
```
>    and therefore
>    

```math
>    \boxed{
>    \alpha_1(H)-|A^{\max}|=0.
>    }
>    \tag{168.7}
>    
```

### Proof

Start from a triangle-free global optimum `B_0 subset H`, initially `B_0=A`.  Given
`B_s`, choose among all triangle-free unit-separated supersets of `B_s` in `H` one of
maximum cardinality and call it `C_s`.  Such a maximum cardinality exists because all
unit-separated subsets of the bounded body `H` have cardinality at most `M`.

Because `B_s subset C_s subset H` and `B_s` already has diameter `D`,
```math
\operatorname{diam}C_s=D.
\tag{168.8}
```
If `q_s=|C_s|`, then monotonicity gives
```math
D(q_s)\ge D(|B_s|)=D,
\tag{168.9}
```
while `C_s` gives `D(q_s)<=D`; hence `C_s` is itself a triangle-free global optimum
of diameter `D`.  If `q_s=M`, alternative 2 holds.

Assume `q_s<M`.  Choose any capacity endpoint `X_s subset H` with `|X_s|=M`.  The
source-capacity plateau exchange theorem of Section 124 applies to the maximal
triangle-free extension `C_s` and `X_s`.  It supplies an adjacent-cardinality flag
```math
P_0=C_s,P_1,\ldots,P_\tau,
\qquad |P_i|=q_s+i,
\tag{168.10}
```
of unit-separated global optima in `H`, all of diameter `D`, ending at cardinality
`M`.

If every `P_i` is triangle-free, then `P_\tau` is a triangle-free `M`-point global
optimum and alternative 2 holds.  Otherwise let `P_j` be the first member containing
a unit triangle.  Corollary 138.2 gives two possibilities.  If its locked alternative
holds, `P=P_j` and its locked triangle give alternative 1.  Otherwise a fixed-hull
perturbation gives a triangle-free global optimum `B_{s+1} subset H` of the same
cardinality `q_s+j`.  In particular
```math
|B_{s+1}|=q_s+j>q_s.
\tag{168.11}
```
Restart the construction from `B_{s+1}`.

Every restart strictly raises the cardinality of the triangle-free global optimum,
and no cardinality exceeds `M`.  Therefore after at most `M-N` successful restarts,
either a locked transition occurs or cardinality `M` is reached.  These are exactly
alternatives 1 and 2.  $`\square`$

The theorem does not preserve the original contact-minimal core, strict-rattler labels,
or activation forest across restarts.  No such preservation is used.  Each restart is
a new triangle-free global optimum in the same fixed hull `H`.

## 168.2 Full response labeling in the zero-slack branch

Assume now alternative 2 and write
```math
A^0:=A^{\max}.
\tag{168.12}
```
Retain the Section-165 very-super-boundary common placement of the actual
plateau-terminalized response optimum
```math
X^*,\qquad |X^*|=m^*,\qquad K^*=\operatorname{conv}X^*,
\tag{168.13}
```
so that
```math
\boxed{K^*+\mathbb B\subset H.}
\tag{168.14}
```
Let the response lattice phase be generic simultaneously for the finite sets `X^*`
and `A^0`, and put
```math
Y_{\rm in}=(\Lambda+v)\cap\operatorname{int}(K^*+\mathbb B).
\tag{168.15}
```

> **Theorem 168.2 (zero-slack full response labels).**  The strict conflict graph
> between `X^*` and `A^0` has a matching saturating every vertex of `X^*`.  Likewise,
> the strict conflict graph between `Y_in` and `A^0` has a matching saturating every
> vertex of `Y_in`.
>
> Consequently every actual Schur terminal
> 

```math
> c\in C^\partial\subset X^*
> \tag{168.16}
> 
```
> has a distinct label `a_c in A^0` satisfying
> 

```math
> |c-a_c|<1,
> \tag{168.17}
> 
```
> and there is a response-lattice vertex `y_c in Y_in` with
> 

```math
> \boxed{
> |c-y_c|<1,
> \qquad |a_c-y_c|<1.
> }
> \tag{168.18}
> 
```
> Thus in the zero-slack branch
> 

```math
> \boxed{C^\partial_{\rm src}=C^\partial;}
> \tag{168.19}
> 
```
> the `widehat p_H` exceptional set of Corollary 165.4 disappears completely.

### Proof

Let `Q subset X^*`.  If its strict neighborhood in `A^0` had cardinality smaller
than `|Q|`, then
```math
(A^0\setminus N_{A^0}(Q))\cup Q
\tag{168.20}
```
would be unit-separated, would lie in `H` by (168.14), and would have more than
`M=alpha_1(H)` points.  This is impossible.  Hall's theorem therefore gives a
matching saturating `X^*`.

The identical replacement argument applies to every `Q subset Y_in`, because
`Y_in` is internally unit-separated and lies in `H`.  Hence `Y_in` also has a
matching into `A^0` saturating its entire shore.

Restrict the first matching to `C^partial`; its source labels remain distinct.  For
each matched pair `(c,a_c)`, the common-neighbor theorem of Section 164 supplies a
lattice site `y_c` satisfying (168.18).  Since `c in K^*`, the inequality
`|c-y_c|<1` puts `y_c` in `Y_in`.  $`\square`$

By Theorem 163.1 the straight segments of either zero-slack matching are pairwise
disjoint.  The lattice vertices `y_c` in (168.18) need not be distinct; Section 166
continues to rule out a local zero-loss SDR theorem.

### 168.2.1 Co-phased deep source cells cover the response lattice up to the boundary

Put
```math
A^0_\partial
=\{a\in A^0:\operatorname{dist}(a,\partial H)\le1\},
\qquad b=|A^0_\partial|.
\tag{168.21}
```
The standard boundary-layer estimate used in Section 154 gives
```math
\boxed{b\le12D+9.}
\tag{168.22}
```
For a response lattice vertex `y in Y_in`, call it **source-boundary-only** when every
strict source conflict lies in `A^0_partial`, and write
```math
Z_\partial
=\{y\in Y_{\rm in}:N_{A^0}(y)\subseteq A^0_\partial\}.
\tag{168.23}
```

> **Corollary 168.2A (boundary-exact co-phased source complex).**  In the zero-slack
> branch,
> 

```math
> \boxed{|Z_\partial|\le b\le12D+9.}
> \tag{168.24}
> 
```
> Hence every response-lattice vertex outside an explicit boundary-order exceptional
> set has a strict conflict with a source point `a in A^0` satisfying
> `dist(a,partial H)>1`.  For every such deep source point its complete strict
> neighborhood in the response triangular lattice has exactly three or four sites,
> whose convex hull is respectively one elementary triangle or one unit lozenge
> containing `a` in its interior.  Distinct deep source-cell interiors are disjoint.

### Proof

The zero-slack replacement argument behind Theorem 168.2 is hereditary: for every
unit-separated `Q subset H`,
```math
|Q|\le|N_{A^0}(Q)|.
\tag{168.25}
```
Apply this to `Q=Z_partial`.  Its source neighborhood is contained in
`A^0_partial`, so
```math
|Z_\partial|
\le|N_{A^0}(Z_\partial)|
\le b,
```
which proves (168.24).

If `a in A^0\setminus A^0_partial`, every triangular-lattice site at distance below
one from `a` lies in `H`; therefore its neighborhood in the prescribed finite lattice
`(Lambda+v) cap H` equals its complete infinite-lattice neighborhood.  The exact
Section-79 three/four-neighbor classification gives the elementary-triangle/lozenge
cell and places `a` in its interior.  The Section-79 disjoint-cell argument uses only
unit separation of the source points, so it applies to `A^0`.  $`\square`$

Thus, after zero-slack terminalization, the actual response lattice and a
triangle-free global optimum carry the same monomer/lozenge cell alphabet in one
coordinate system, with at most `12D+9` response vertices lacking a deep-source cell.
This is a boundary-exact structural statement, not a Hall-surplus conclusion.

## 168.3 Inner-hull descent or transverse source gates

The zero-slack normalization also creates an exact alternative inside the smaller
response hull.  Put
```math
k=|A^0\cap K^*|,
\qquad
r=m^*-k.
\tag{168.26}
```
Because `K^*` has diameter `d=D(m^*)` and `m^*` is the right endpoint of its diameter
plateau,
```math
\boxed{\alpha_1(K^*)=m^*.}
\tag{168.27}
```
Indeed an `(m^*+1)`-point unit-separated subset of `K^*` would have diameter at most
`d`, contradicting `D(m^*+1)>d`.
Thus `0<=r<=m^*`.

> **Theorem 168.3 (descent-or-gates dichotomy).**  Exactly one of the following holds.
>
> 1. **Plateau descent:** `r=0`.  Then
>    

```math
>    A^0\cap K^*
>    \tag{168.28}
>    
```
>    is a triangle-free `m^*`-point global optimum of diameter `d`.  In particular a
>    triangle-free counterexample has descended from the `D`-plateau to the right
>    endpoint of the strictly smaller `d`-plateau.
>
> 2. **Transverse source gates:** `r>0`.  Every matching saturating `X^*` into `A^0`
>    has at least `r` edges
>    

```math
>    x_i a_i
>    \qquad(1\le i\le r)
>    \tag{168.29}
>    
```
>    whose source endpoints satisfy
>    

```math
>    a_i\in (K^*+\mathbb B)\setminus K^*.
>    \tag{168.30}
>    
```
>    Their straight segments are pairwise disjoint and each segment meets
>    `partial K^*`.  For a phase generic for `X^*` and `A^0`, at least
>    

```math
>    \boxed{\frac r5}
>    \tag{168.31}
>    
```
>    of these gates can be selected with pairwise distinct response-lattice vertices
>    `y_i in Y_in` such that
>    

```math
>    |x_i-y_i|<1,
>    \qquad |a_i-y_i|<1.
>    \tag{168.32}
>    
```

### Proof

If `r=0`, then `A^0 cap K^*` contains `m^*` points.  It is triangle-free as a subset
of `A^0`, unit-separated, and has diameter at most `d`.  Since `D(m^*)=d`, its
diameter is exactly `d` and it is a global optimum.  This proves alternative 1.

Assume `r>0`, and take any matching saturating `X^*` into `A^0`.  Its `m^*` source
endpoints are distinct.  At most `k=m^*-r` of them can lie in `K^*`, so at least `r`
lie outside `K^*`.  Each such endpoint is at distance strictly below one from its
matched `x_i in K^*`; hence it belongs to `K^*+B`, and strictness gives (168.30).
The matching segments are pairwise disjoint by Theorem 163.1.  Since one endpoint is
in `K^*` and the other is outside the closed convex body, each segment meets
`partial K^*`.

Apply the Section-164 common-neighbor theorem separately to the `r` gate pairs.  A
fixed response-lattice vertex can be a strict neighbor of at most five points of the
unit-separated set `X^*`, so the same bounded-congestion selection as Theorem 164.2
retains at least `r/5` gates with distinct lattice vertices.  This gives
(168.31)--(168.32).  $`\square`$

The gate count `r` is an exact inner-capacity deficit, not yet the Schur demand
`s=Delta_Lambda-d_int`.  No inequality `r>=s` is claimed.  The importance of the
dichotomy is structural: the zero-slack branch cannot simultaneously avoid both a
strict descent to a smaller triangle-free global optimum and a family of disjoint
source arcs crossing the actual response hull boundary.

## 168.4 Exact remaining obligations

The Level I endpoint remains
```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}
}
\tag{168.33}
```
or an explicit `N`-point unit-separated competitor of diameter `<D`.

Section 168 splits the next work into two exact branches.

1. In the locked-transition branch, combine the boundary-transmitting stress of
   Section 159 with the actual response alignment of Section 165.  The missing theorem
   is still an exact map from the two or more source-hull reaction paths to saved Schur
   terminals or a strict-diameter replacement.
2. In the zero-slack branch, every Schur terminal has a distinct label in a
   triangle-free global optimum, and all but at most `12D+9` response lattice vertices
   belong to the neighborhood of a deep source monomer/lozenge cell.  Either the
   source descends to the smaller plateau endpoint, or `r` disjoint source gates cross
   `partial K^*`.  A closing theorem must show that repeated descent cannot persist
   for an arbitrarily large counterexample, or that the co-phased cell/gate structure
   forces at least `s` omitted response terminals.

The Section-166 SDR regression remains binding: the existence of all terminal labels
in (168.19) does not imply distinct common lattice neighbors.
