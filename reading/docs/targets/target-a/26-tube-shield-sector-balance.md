> Generated reading edition · [exact source](../../../../docs/targets/target-a/26-tube-shield-sector-balance.md) · source SHA-256 `15e470ca494ddf19b5a7fe80a558b2cff01bab824539a0367a2b628436367798`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — tube-shield sector balance and basis closure

Section 173 uses the smallest natural contact shield: delete contact vertices and all
response-lattice sites conflicting with those vertices.  This gives a good shielding
constant but permits one exterior sink to touch more than one geometric sector.  The
slightly thicker shield below removes every lattice site within unit distance of the
entire contact subgraph.  That makes the whole surviving response graph sector-local.
Closing the shield under the fixed `B<->Z` basis matching then removes a second source
of bookkeeping loss: outside the shield, every sector contains equally many basis
vertices and interior lattice rows.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 174. Unit-tube shields and exact sector population balance

Retain the response notation of Sections 170 and 173.  Let `Sigma` be a finite
unit-contact subgraph of `X^*` with no isolated vertices, and let
$$
D_1,\ldots,D_k
\tag{174.1}
$$
be the connected components of `K^*\setminus|Sigma|`.

Define the right-shore unit tube
$$
T_\Sigma
=
\{y\in Y_{\rm in}:\operatorname{dist}(y,|\Sigma|)<1\}
\tag{174.2}
$$
and the preliminary shield
$$
W_\Sigma^0=V(\Sigma)\sqcup T_\Sigma.
\tag{174.3}
$$

## 174.1 A uniform finite tube bound

> **Lemma 174.1 (eleven lattice sites per contact edge).**  If `e` is any unit
> segment in the plane, then the unit triangular lattice has at most eleven sites at
> distance strictly below one from `e`.  Consequently
> 

$$

> \boxed{|T_\Sigma|\le11|E(\Sigma)|.}
> \tag{174.4}
> 
$$



### Proof

The sites within distance below one from `e` lie in the compact stadium
$$
S_e=e+\overline B(0,1).
\tag{174.5}
$$
The stadium has area `pi+2` and perimeter `2pi+2`.  Apply Oler's finite packing
inequality to the unit-separated lattice sites in `S_e`, with
`a_0=sqrt(3)/2`:
$$
\begin{aligned}
|\Lambda\cap S_e|
&\le
\frac{\pi+2}{a_0}+rac{2\pi+2}{2}+1\\
&=
(\pi+2)\left(1+\frac2{\sqrt3}\right)
<12.
\end{aligned}
\tag{174.6}
$$
The cardinality is an integer, hence at most eleven.  Every point of `|Sigma|` lies on
one of its contact edges because there are no isolated vertices.  A union bound over
those edges proves (174.4).  $\square$

No sharpness of the constant eleven is claimed.

## 174.2 The tube makes the entire response graph sector-local

> **Lemma 174.2 (sector uniqueness for surviving right vertices).**  In
> `G-W_Sigma^0`, every surviving response edge avoids `|Sigma|`.  Moreover every
> surviving right vertex `y in (Z sqcup O)\setminus T_Sigma` has response neighbors
> in at most one component `D_i`.

### Proof

If a response edge `xy` met `|Sigma|` at a point `z`, then `z` lies on the segment
`xy`, so
$$
|y-z|\le|y-x|<1.
\tag{174.7}
$$
This would put `y` in `T_Sigma`.  Thus every surviving response edge avoids the
contact subgraph.

Now suppose a surviving right vertex `y` had neighbors `x_i in D_i` and
`x_j in D_j` with `i!=j`.  The chord `x_ix_j` lies in `K^*` by convexity.  Since it
joins two different components of `K^*\setminus|Sigma|`, it intersects `|Sigma|` at
some point `z`.  Both `x_i` and `x_j` belong to the open unit disk `B(y,1)`, and that
disk is convex.  Hence the whole chord `x_ix_j`, in particular `z`, lies in `B(y,1)`.
Thus `dist(y,|Sigma|)<1`, contradicting survival of `y`.  $\square$

Therefore the sets
$$
O_i
=
\{o\in O\setminus T_\Sigma:
 o\text{ has a surviving neighbor in }D_i\}
\tag{174.8}
$$
are pairwise disjoint.  The same uniqueness holds for surviving `Z` vertices.

## 174.3 Close the shield under the `Z`-basis matching

Let
$$
\mu_0:B\longrightarrow Z
\tag{174.9}
$$
be the fixed perfect basis matching used to orient the Schur gammoid.  Define the
basis-closed shield
$$
\widehat W_\Sigma
=
W_\Sigma^0
\cup
\mu_0(B\cap W_\Sigma^0)
\cup
\mu_0^{-1}(Z\cap W_\Sigma^0).
\tag{174.10}
$$
Here `mu_0(B cap W)` means the matched `Z` partners of shielded basis vertices, and
the inverse term means the matched `B` partners of shielded `Z` vertices.

Since `mu_0` is a bijection,
$$
\boxed{
|\widehat W_\Sigma|
\le2|W_\Sigma^0|
\le2|V(\Sigma)|+22|E(\Sigma)|.
}
\tag{174.11}
$$
Deleting additional vertices cannot reconnect geometric sectors, so Lemma 174.2
continues to hold after basis closure.

For each sector put
$$
B_i=(B\setminus\widehat W_\Sigma)\cap D_i,
\qquad
Z_i=(Z\setminus\widehat W_\Sigma)\cap D_i.
\tag{174.12}
$$

> **Lemma 174.3 (exact sector basis balance).**  For every `i`,
> 

$$

> \boxed{|B_i|=|Z_i|.}
> \tag{174.13}
> 
$$



### Proof

Basis closure guarantees that a matched pair `b,mu_0(b)` has either both endpoints in
`widehat W_Sigma` or neither.  For a surviving pair, the matching edge is a response
edge, so Lemma 174.2 puts both endpoints in the same geometric sector.  Restricting
`mu_0` therefore gives a bijection `B_i->Z_i`.  $\square$

## 174.4 Sector terminal surplus equals local response population surplus

Define
$$
C_i^\circ=(C^\circ\setminus\widehat W_\Sigma)\cap D_i,
\qquad
C_i^\partial=(C^\partial\setminus\widehat W_\Sigma)\cap D_i,
\tag{174.14}
$$
and let `O_i` now mean the exterior sinks surviving the basis-closed shield and
adjacent to sector `D_i`.  The `O_i` remain pairwise disjoint.

Let
$$
X_i=(X^*\setminus\widehat W_\Sigma)\cap D_i.
\tag{174.15}
$$
Then
$$
X_i=B_i\sqcup C_i^\circ\sqcup C_i^\partial.
\tag{174.16}
$$

> **Proposition 174.4 (local population identity).**  For every sector,
> 

$$

> \boxed{
> |C_i^\partial|-|O_i|
> =
> |X_i|-|Z_i|-|O_i|-|C_i^\circ|.
> }
> \tag{174.17}
$$

### Proof

Use (174.16) and cancel `|B_i|=|Z_i|` by Lemma 174.3.  $\square$

Thus the sign relevant to Schur nullity is a genuine local left-versus-right population
surplus after subtracting only the already-accounted interior nonbasis nullity.

## 174.5 Sector-separated Schur bound

Because all surviving right vertices are sector-local, a shield-avoiding directed
Menger path that starts in `C_i^partial` must end at a distinct sink in the disjoint
set `O_i`.

> **Theorem 174.5 (tube-shield sector nullity).**
> 

$$

> \boxed{
> \operatorname{rank}S
> \le
> |\widehat W_\Sigma|
> +
> \sum_{i=1}^k\min\{|C_i^\partial|,|O_i|\}.
> }
> \tag{174.18}
> 
$$


> Consequently
> 

$$

> \boxed{
> \zeta
> \ge
> \sum_{i=1}^k
> \max\{0,|C_i^\partial|-|O_i|\}
> -
> |\widehat W_\Sigma\setminus C^\partial|.
> }
> \tag{174.19}
> 
$$


> By Proposition 174.4 this is equivalently
> 

$$

> \boxed{
> \zeta
> \ge
> \sum_{i=1}^k
> \max\{0,
> |X_i|-|Z_i|-|O_i|-|C_i^\circ|
> \}
> -
> |\widehat W_\Sigma\setminus C^\partial|.
> }
> \tag{174.20}

### Proof

At most `|widehat W_Sigma|` paths in a vertex-disjoint Schur Menger family meet the
shield.  Delete them.  Every remaining path is sector-local by Lemma 174.2, and the
surviving sink sets `O_i` are disjoint.  Hence at most
`min(|C_i^partial|,|O_i|)` remaining paths can start in sector `i`.  This proves
(174.18).

The terminal set decomposes into the shielded terminals and the sector terminals.
Subtract (174.18) from `|C^partial|`; exactly as in Section 170, shielded terminals
cancel from the loss and give (174.19).  Substitute (174.17) for (174.20).  \(\square\)

## 174.6 Locked three-channel specialization and new target

For the locked three-channel fan of Section 172, let `Sigma` be the union of the three
spokes and the locked triangle.  It is a connected unicyclic contact graph, so
\[
|E(\Sigma)|=|V(\Sigma)|.
\tag{174.21}
$$
The basis-closed tube shield therefore satisfies the explicit crude bound
$$
\boxed{
|\widehat W_\Sigma|
\le24|V(\Sigma)|.
}
\tag{174.22}
$$
The useful point is not this constant but the exact decomposition (174.20): after the
shield is removed, the three outer sectors have no shared response rows and no hidden
basis imbalance.

The remaining quantitative statement can now be posed directly in the monomer/dimer
language:

> **Three-sector population theorem.**  For the stress-generated fan, prove
> 

$$

> \sum_i
> \max\{0,
> |X_i|-|Z_i|-|O_i|-|C_i^\circ|
> \}
> \ge
> s+|\widehat W_\Sigma\setminus C^\partial|,
> \tag{174.23}
> 
$$


> or derive a strict-diameter competitor.

Equation (174.23) is sufficient for the exact Target A endpoint by Theorem 174.5.  In
the zero-slack branch, Corollary 168.2A additionally supplies a co-phased deep-source
monomer/lozenge complex covering all but `12D+9` response lattice vertices.  The next
bridge is therefore no longer source/scaffold coordinate identification or Schur
algebra: it is a signed local population inequality in three explicitly separated
geometric sectors.
