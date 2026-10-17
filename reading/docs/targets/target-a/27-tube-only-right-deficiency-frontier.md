> Generated reading edition · [exact source](../../../../docs/targets/target-a/27-tube-only-right-deficiency-frontier.md) · source SHA-256 `0399e4947619293dfda7818c8961c18a48cf762c2f8c5e0d8e956099ca08db29`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — tube-only right-deficiency frontier

This module independently audits the load-bearing chain through Sections 168--174 and
promotes the strongest correct shield consequence found in the September 4--8 working
reports. It does not close Target A.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 175. Tube-only right-deficiency theorem

Retain the actual plateau-terminalized response optimum `X^*`, its generic triangular
lattice response graph, and the Section-113 fixed `Z`-perfect basis matching

```math
\mu_0:B\longrightarrow Z.
```

Let `Sigma` be a finite connected unit-contact shield in `X^*` satisfying the
Section-174 separation hypotheses. In particular the three-channel locked fan of
Section 172 is admissible. Put

```math
T_\Sigma
=\{y\in Y_{\rm in}:\operatorname{dist}(y,|\Sigma|)<1\},
\qquad
T_Z=T_\Sigma\cap Z,
\qquad
T_O=T_\Sigma\cap O.
\tag{175.1}
```

Let `D_1,...,D_k` be the components of `K^*\setminus|Sigma|`. Use the basis-closed
shield of Section 174 only to define the surviving sector sets. Write

```math
C_i=(C^\partial\setminus\widehat W_\Sigma)\cap D_i
\tag{175.2}
```

and let `O_i` be the surviving exterior sinks having a surviving response neighbor in
`D_i`. Section 174 proves that the `O_i` are pairwise disjoint. Put

```math
O_{\rm iso}
=(O\setminus\widehat W_\Sigma)\setminus\bigcup_i O_i,
\tag{175.3}
```

and

```math
Q_\Sigma=\sum_i\max\{0,|O_i|-|C_i|\}.
\tag{175.4}
```

Finally use the current flexible-source collar demand

```math
j_*=N-|Y_0|-m^*.
\tag{175.5}
```

The exact identity from the plateau-terminalized Schur bookkeeping is

```math
\zeta-s=h(G)-j_*,
\qquad
h(G)=|O|-\operatorname{rank}S,
\qquad
s=\Delta_\Lambda-d_{\rm int}.
\tag{175.6}
```

## 175.1 Nine lattice sites per unit contact edge

> **Lemma 175.1 (nine-site unit tube).** For every unit segment `e` and every unit
> triangular lattice `Lambda`,
> 

```math
> \#\{y\in\Lambda:\operatorname{dist}(y,e)<1\}\le9.
> \tag{175.7}
> 
```
> Consequently
> 

```math
> \boxed{|T_\Sigma|\le9|E(\Sigma)|.}
> \tag{175.8}
> 
```

### Proof

If `y,y'` lie in the open unit tube of the same unit segment, choose `x,x'` on the
segment with `|y-x|<1` and `|y'-x'|<1`. Then

```math
|y-y'|<1+|x-x'|+1\le3.
```

Partition `Lambda` into the nine cosets of `3Lambda`. Distinct points in one coset are
at distance at least three, so the tube contains at most one point from each coset.
This proves (175.7). Since `Sigma` has no isolated vertices, its geometric realization
is the union of its unit edges. A union bound proves (175.8). $`\square`$

For the Section-172 three-channel fan, `Sigma` is connected and unicyclic, so

```math
|E(\Sigma)|=|V(\Sigma)|
\tag{175.9}
```

and the pointwise coarse tube charge is at most `9|V(Sigma)|`.

## 175.2 Every shield-touching Schur path meets a tube row

The basis-closed shield of Section 174 can be written exactly as

```math
\widehat W_\Sigma
=T_\Sigma
\sqcup\mu_0^{-1}(T_Z)
\sqcup(V(\Sigma)\cap C^\circ)
\sqcup(V(\Sigma)\cap C^\partial).
\tag{175.10}
```

Indeed, if `b in B cap V(Sigma)`, then its matched row `mu_0(b)` is a strict response
neighbor of `b` and therefore belongs to `T_Z`; hence every basis vertex of the
geometric shield is already included in `mu_0^{-1}(T_Z)`.

Recall the Section-113 alternating orientation: the matched edges are directed
`Z -> B`, and every other response edge is directed from the left shore to the right
shore.

> **Lemma 175.2 (tube-only path interception).** Every directed Schur path from
> `C^partial` to `O` that meets `widehat W_Sigma` also meets a right vertex of
> `T_Sigma`.

### Proof

A path meeting a right vertex of the shield already meets `T_Sigma`. If it meets a
basis vertex `b in mu_0^{-1}(T_Z)`, then `b` has exactly one incoming edge, namely the
matched edge from `mu_0(b) in T_Z`; a Schur path cannot start at a basis vertex, so it
must have just met that tube row.

A nonbasis vertex has no incoming edge in the alternating orientation. Hence a path
cannot visit a shielded `C^circ` vertex internally, and it can meet a shielded
`C^partial` vertex only as its initial terminal. If that terminal lies on `Sigma`, its
next response row is at distance below one from `|Sigma|`, hence belongs to
`T_Sigma`. Thus every possible shield encounter forces a tube-row encounter.
$`\square`$

## 175.3 Tube-only rank and nullity bounds

Take a maximum family of pairwise vertex-disjoint directed Schur paths. By Lemma 175.2,
at most `|T_Sigma|` of them meet the basis-closed shield. Delete those paths. Every
remaining path avoids the shield and is therefore sector-local by Section 174. It
starts at a distinct terminal in one `C_i` and ends at a distinct sink in the
corresponding `O_i`.

> **Theorem 175.3 (tube-only Schur cut).**
> 

```math
> \boxed{
> \operatorname{rank}S
> \le |T_\Sigma|+\sum_i\min\{|C_i|,|O_i|\}.
> }
> \tag{175.11}
> 
```

If

```math
t_\Sigma=|C^\partial\cap V(\Sigma)|,
\qquad
P_\Sigma=\sum_i\max\{0,|C_i|-|O_i|\},
\tag{175.12}
```

then subtracting (175.11) from

```math
|C^\partial|=t_\Sigma+\sum_i|C_i|
```

gives

```math
\boxed{\zeta\ge t_\Sigma+P_\Sigma-|T_\Sigma|.}
\tag{175.13}
```

This strictly improves the Section-174 basis-closed shield charge. In particular it
is sufficient to prove

```math
\boxed{t_\Sigma+P_\Sigma\ge s+|T_\Sigma|.}
\tag{175.14}
```

No basis partner or left contact vertex is charged separately.

## 175.4 Exact right-deficiency form: exterior tube sinks cancel

The right shore decomposes as

```math
O=T_O\sqcup O_{\rm iso}\sqcup\bigsqcup_i O_i.
\tag{175.15}
```

Subtract (175.11) from this identity. Since

```math
|T_\Sigma|=|T_Z|+|T_O|,
```

the exterior tube population cancels exactly.

> **Theorem 175.4 (contact-fan right-deficiency bound).**
> 

```math
> \boxed{
> h(G)=|O|-\operatorname{rank}S
> \ge O_{\rm iso}+Q_\Sigma-|T_Z|.
> }
> \tag{175.16}
> 
```

Combining with (175.6) gives the current locked-branch closing criterion

```math
\boxed{
|O_{\rm iso}|+Q_\Sigma
\ge j_*+|T_Z|.
}
\tag{175.17}
```

Equivalently, any surviving Target A counterexample must satisfy the pointwise integer
inequality

```math
\boxed{
|O_{\rm iso}|+Q_\Sigma
\le j_*+|T_Z|-1.
}
\tag{175.18}
```

This is the strongest exact shield inequality in the audited locked-fan chain. The
hard term is now a genuine exterior-sink surplus. The only shield loss is the number
of **interior** response-lattice sites in the unit tube.

The older sink-surplus formula with the full non-`O` basis-closed shield charge is a
correct reformulation of Section 174, but (175.16)--(175.18) supersede it for the
thick-tube fan.

## 175.5 Translation-averaged interior tube penalty

The geometric fan `Sigma` depends only on the fixed response optimum and its contact
stress, not on the triangular-lattice translation. Average over one lattice
fundamental cell of area

```math
a_0=\sqrt3/2.
```

Translation averaging gives

```math
\mathbb E_v|T_Z(v)|
={\operatorname{area}(K^*\cap N_1(|\Sigma|))\over a_0}.
\tag{175.19}
```

For any connected finite straight-edge graph of total edge length `L`,

```math
\operatorname{area}N_1(G)\le\pi+2L.
\tag{175.20}
```

To prove this, begin with the unit disk around one graph vertex. Order a spanning-tree
set of edges so each new edge is attached at a vertex already present, then add the
remaining edges. The unit neighborhood of a segment of length `ell` is a stadium of
area `pi+2ell`, while the unit disk around an already present endpoint is already in
the union. Thus each added edge increases area by at most `2ell`.

Every fan edge is a unit contact, so `L=|E(Sigma)|`. Therefore

```math
\boxed{
\mathbb E_v|T_Z(v)|
\le {\pi+2|E(\Sigma)|\over a_0}
={2\pi\over\sqrt3}+{4\over\sqrt3}|E(\Sigma)|.
}
\tag{175.21}
```

For the unicyclic three-channel fan, replace `|E(Sigma)|` by `|V(Sigma)|`.

A survivor consequently obeys the joint averaged necessary inequality

```math
\boxed{
\mathbb E_v\bigl[|O_{\rm iso}(v)|+Q_\Sigma(v)\bigr]
\le
\mathbb E_v j_*(v)
+{\operatorname{area}(K^*\cap N_1(|\Sigma|))\over a_0}-1.
}
\tag{175.22}
```

This average is legitimate because (175.18) holds phase by phase; no phase is selected
by minimizing the tube independently of the collar demand.

## 175.6 Dependency audit through the current endpoint

The following load-bearing interfaces were rechecked independently before promoting
Section 175.

1. Section 122/124 fixed-container matching and the Hall-tight fundamental-circuit
   exchange flag are valid; unions of fixed-basis fundamental circuits have exactly
   the claimed deficiency.
2. Section 138's simultaneous triangle-breaking alternative is valid as a finite
   convex-cone argument, including the finite linear perturbation.
3. Section 159's nonnegative contact/facet stress follows from the polar/Farkas cone,
   and a locked positive-contact component must transmit reaction to at least two
   distinct hull-boundary points.
4. Section 164's common triangular-lattice-neighbor theorem is valid in both the
   elementary-triangle and unit-lozenge cells: the exposed arcs of the union of the
   neighbor unit disks lie in the angular cone opposite the cell interior, so their
   nearest points to `x` are the adjacent nonneighbor lattice vertices, all at distance
   at least one.
5. Section 165's plateau-wide collar uses the Oler area lower bound and Bonnesen
   deficit with the correct constants and applies uniformly to every optimum on the
   smaller-diameter plateau.
6. Section 168's restart process strictly raises the cardinality of a triangle-free
   same-hull global optimum and therefore terminates at a locked transition or a
   zero-slack capacity endpoint.
7. Sections 169--172 correctly move the locked alternative to the actual response
   optimum and produce a proper contact crosscut and then three internally
   vertex-disjoint reaction channels.
8. Sections 173--174 correctly prove contact shielding, thick-tube sector locality,
   and sectorwise basis balance. The notation `Y_in=Z sqcup O` is essential: exterior
   sinks `O` are still part of the thickened response collar and are removed by the
   same tube condition.

No failure was found in those interfaces. Section 175 is a strengthening of the
Schur-cut bookkeeping, not a repair of a broken canonical theorem.

## 175.7 Exact remaining theorem

Target A remains open. In the actual-response locked branch it now suffices to prove,
for one stress-generated three-channel fan,

```math
|O_{\rm iso}|+
\sum_i\max\{0,|O_i|-|C_i|\}
\ge j_*+|T_Z|,
\tag{175.23}
```

or to construct an `N`-point unit-separated configuration of diameter strictly below
`D`.

The zero-slack/descent branch remains separate. Neither (175.16) nor its averaged form
identifies the two independent zero-slack source matchings, and neither converts a
finite descent in cardinality into a contradiction by itself.
