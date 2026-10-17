> Generated reading edition · [exact source](../../../../docs/targets/target-a/10-source-backbone-hall-obstruction.md) · source SHA-256 `5f53b96fdf9cd938b15e0d55009cc6c859f4b66eed2df6a73396c148ec28201b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — source-backbone Hall obstruction

This module continues the audited Target A frontier after Section 156. It gives an
exact global-optimality obstruction between the genuine source backbone and the
independently chosen smaller optimum. In the very-super-boundary common placement of
Section 155, the obstruction becomes a concrete Hall witness whose entire insertion
gain must be absorbed by genuine strict rattlers. It does not yet transport that
witness into the plateau Schur response.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 157. Diameter-cover deficiency against the smaller optimum

The symbol ρ below is the selected retained-rattler count from the saturated
source normalization of Section 71. It is not the response defect
ρ†=N₋−m₊ from Sections 114–117. The theorem is applied only when the associated
m=N−ρ lies on a genuinely smaller diameter plateau, so d=D(m)<D.

Let
```math
A=P\sqcup R,
\qquad |A|=N,
\qquad |R|=\rho,
\qquad |P|=m=N-\rho,
\tag{157.1}
```

be the saturated Target A source, where every member of $`R`$ is a strict
rattler. Thus no member of $`R`$ is incident to a diameter pair of $`A`$. Let

```math
D=\operatorname{diam}A,
\qquad
X_m\text{ be an }m\text{-point global optimum},
\qquad
d=\operatorname{diam}X_m=D(m).
\tag{157.2}
```

Write $`\mathcal D_P(A)`$ for the graph on the backbone $`P`$ whose edges are the
pairs at distance $`D`$. (Equivalently, this is the diameter graph of $`A`$ with
the isolated strict rattlers deleted.) Let

```math
\tau_D(A)=\tau(\mathcal D_P(A))
\tag{157.3}
```

be its vertex-cover number. Every diameter edge of $`A`$ lies in
$`\mathcal D_P(A)`$.

For $`\delta>0`$ and any rigid placement of $`X_m`$, define the strict
$`\delta`$-conflict graph

```math
J_\delta=(X_m\sqcup P,E_\delta),
\qquad
xp\in E_\delta\iff |x-p|<\delta.
\tag{157.4}
```

> **Theorem 157.1 (diameter-cover Hall obstruction).** If
> 

```math
> d+2\delta\le D,
> \tag{157.5}
> 
```
> then every matching in $`J_\delta`$ has size at most
> $`m-\tau_D(A)`$. Equivalently,
> 

```math
> \boxed{
> \max_{Q\subseteq X_m}
> \bigl(|Q|-|N_P^\delta(Q)|\bigr)
> =m-\nu(J_\delta)
> \ge\tau_D(A).
> }
> \tag{157.6}
> 
```
> If
> 

```math
> N_-:=\min\{q:D(q)=D\},
> \qquad p_N=N-N_-,
> \tag{157.7}
> 
```
> then
> 

```math
> \boxed{\tau_D(A)\ge p_N+1.}
> \tag{157.8}
> 
```

### Proof

Let $`M`$ be a matching in $`J_\delta`$, and let $`P_M\subseteq P`$ be its
set of matched backbone vertices. Suppose that two vertices $`p,q\in P_M`$
formed a diameter edge of $`A`$. Let $`x,y\in X_m`$ be their distinct matched
partners. Then

```math
|p-q|
\le |p-x|+|x-y|+|y-q|
<\delta+d+\delta
\le D,
\tag{157.9}
```

contrary to $`|p-q|=D`$. Hence $`P_M`$ is an independent set of
$`\mathcal D_P(A)`$. Since that graph has $`m`$ backbone vertices,

```math
|M|=|P_M|
\le\alpha(\mathcal D_P(A))
=m-\tau_D(A).
\tag{157.10}
```

Maximizing over $`M`$, and then using the deficiency form of Hall's theorem for
the equal shores $`|X_m|=|P|=m`$, proves (157.6).

For (157.8), let $`C`$ be a vertex cover of $`\mathcal D_P(A)`$, with
$`|C|=c`$. The unit-separated set $`A\setminus C`$ has no pair at distance
$`D`$, so

```math
\operatorname{diam}(A\setminus C)<D.
\tag{157.11}
```

If $`c\le p_N`$, then $`N-c\ge N_-`$. Monotonicity of $`D(q)`$, together
with $`D(N_-)=D(N)=D`$, gives $`D(N-c)=D`$. But (157.11) would give
$`D(N-c)<D`$, a contradiction. Therefore every diameter cover has at least
$`p_N+1`$ vertices. $`\square`$

## 157.1 Rattler capture in the common source placement

In the super-boundary Target A branch, the compatible-collar theorem gives

```math
t=\frac{D-d}{2}>1
\tag{157.12}
```

for all sufficiently large survivors. Thus Theorem 157.1 applies with
$`\delta=1`$. Under the explicit very-super-boundary hypothesis (155.4), Section
155 places $`X_m\subset H=\operatorname{conv}A`$. The exact fixed-source Hall
bound is then available for every $`Q\subseteq X_m`$.

> **Corollary 157.2 (exact backbone witness and rattler capture).** Under the
> common placement of Section 155, there is a set $`Q\subseteq X_m`$ with
> 

```math
> h:=|Q|-|N_P(Q)|
> =m-\nu(J_1)
> \ge\tau_D(A)
> \ge p_N+1.
> \tag{157.13}
> 
```
> It satisfies
> 

```math
> \boxed{|N_R(Q)|\ge h-\widehat p_H.}
> \tag{157.14}
> 
```
> Moreover
> 

```math
> P_Q=(P\setminus N_P(Q))\cup Q
> \tag{157.15}
> 
```
> is a unit-separated subset of $`H`$ with
> 

```math
> \boxed{|P_Q|=m+h.}
> \tag{157.16}
> 
```

### Proof

Choose $`Q`$ attaining the maximum in (157.6). Equation (157.13) follows from
Theorem 157.1. Since $`A=P\sqcup R`$, its strict neighborhood is the disjoint
union of the two labeled shores:

```math
N_A(Q)=N_P(Q)\sqcup N_R(Q).
\tag{157.17}
```

The fixed-source Hall inequality therefore gives

```math
\widehat p_H
\ge |Q|-|N_A(Q)|
=h-|N_R(Q)|,
\tag{157.18}
```

which is (157.14). Finally, $`Q`$ is internally unit-separated, and every point
of $`P\setminus N_P(Q)`$ is at distance at least one from every point of
$`Q`$. This proves the feasibility and cardinality in (157.15)--(157.16).
$`\square`$

## 157.2 Exact scope and remaining transport

Theorem 157.1 uses the genuine global diameter gap $`D-D(m)>2`$, not local
activation geometry. It therefore survives the Section 152 regression, whose
anchored configuration is intentionally not globally minimum-diameter optimal. It
also uses no KKT multiplier and is unaffected by Section 153.

The result gives a source-specific Hall defect against the **nonrattler backbone**,
not against the fixed-hull source and not against the plateau scaffold. Equation
(157.14) explains exactly how the ordinary fixed-source capacity ceiling absorbs
that defect: enough genuine rattlers must conflict with the backbone insertion
witness. Consequently neither (157.13) nor (157.16) may be promoted to a same-hull
capacity contradiction.

The exact remaining bridge is now sharper in the common-placement subbranch. One
must use the captured set $`N_R(Q)`$, the finite fixed-hull activation flat of
Section 156, and the co-phased scaffold of Sections 154--155 to prove either

```math
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}}
\tag{157.19}
```

or a compatible relocation of the captured rattlers that turns (157.15) into an
$`N`$-point packing of diameter strictly below $`D`$. No such transport is proved
here.

## 157.3 Diameter-cover graft tightening in the aligned subbranch

The common placement gives one additional strict-diameter fact for the witness from
Corollary 157.2. If $`x+\overline B(0,1)\subseteq H`$ and $`a\in H`$, then

```math
|x-a|<D.
\tag{157.20}
```

Indeed, for $`u=(a-x)/|a-x|`$, both $`x-u`$ and $`x+u`$ lie in $`H`$. The width of
$`H`$ in direction $`u`$ is at most $`D`$, while the interval from $`x-u`$ to
$`a=x+|a-x|u`$ has length $`1+|a-x|`$. Hence $`|a-x|+1\le D`$, and $`D>1`$
gives (157.20).

> **Proposition 157.3 (diameter-cover graft obstruction).** Assume the common
> placement $`X_m+\overline B(0,1)\subseteq H`$. Let $`C`$ be any vertex cover of
> $`\mathcal D_P(A)`$. Then every $`Q\subseteq X_m`$ satisfies
>
> 

```math
> \boxed{|Q|-|N_A(Q)\cup C|\le-1.}
> \tag{157.21}
> 
```
> Consequently, for a maximizing backbone witness from Corollary 157.2, with
> $`h=|Q|-|N_P(Q)|`$,
>
> 

```math
> \boxed{|N_R(Q)|
> \ge h-|C\setminus N_A(Q)|+1
> \ge h-|C|+1.}
> \tag{157.22}
> 
```
> In particular, choosing a minimum cover and using $`h\ge\tau_D(A)`$, every
> such witness captures at least one strict rattler.

### Proof

The set

```math
Q\cup\bigl(A\setminus(N_A(Q)\cup C)\bigr)
\tag{157.23}
```

is unit-separated: $`Q`$ is internally unit-separated, and all source points
conflicting with $`Q`$ are removed. Its source part lies in $`A\setminus C`$, so it
has no diameter pair. By (157.20), every cross-distance from $`Q`$ to its source
part is strictly below $`D`$; the $`Q`$-part has diameter at most $`d<D`$. Thus
the set in (157.23) has diameter $`<D`$. If its cardinality were at least $`N`$, an
$`N`$-point subset would contradict $`D(N)=D`$. Therefore its cardinality is at
most $`N-1`$, which is exactly (157.21).

Since $`N_A(Q)=N_P(Q)\sqcup N_R(Q)`$ and
$`|N_A(Q)\cup C|=|N_P(Q)|+|N_R(Q)|+|C\setminus N_A(Q)|`$, (157.21) gives

```math
h-|N_R(Q)|
\le |C\setminus N_A(Q)|-1,
```

which is (157.22). $`\square`$

This is a genuine strengthening only in the common-placement subbranch. It does not
turn the captured rattler into a scaffold response variable: the minimum cover can
still be boundary-order, and no map from $`N_R(Q)`$ to $`\ker S`$ is supplied.

The regular-shell and diameter-star possibilities remain binding: they can keep
$`\tau_D(A)`$ boundary-order or even small. Thus (157.8) must not be upgraded to a
super-boundary lower bound without a new global theorem.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**
