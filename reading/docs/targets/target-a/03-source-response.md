> Generated reading edition · [exact source](../../../../docs/targets/target-a/03-source-response.md) · source SHA-256 `b56ef3220026dc503d3dfb43ecf04eeb041a05f8b8944234624806712bfc91a4`.
> [Current theorem state](../../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

# Target A: source response and v1.7 frontier

> Canonical v1.7.0 route module. The original section numbering is preserved for
> cross-references; see the [route map](../README.md).

# 111. v1.6.0 post-v1.5.1 audit policy

Sections 111 onward are the authoritative v1.6.0 continuation.  They preserve the
v1.5.1 theorem stack but add the exact post-v1.5.1 results that survived re-audit.
Two proposed strengthenings from intermediate runs are **not** promoted:

1. the genuine triangle-free source minimizer may not simply be replaced by an
   unrelated right endpoint of its diameter plateau; source continuum Hall statements
   therefore carry the exact plateau slack defined below unless a same-source endpoint
   extension is separately proved; and
2. no individual Voronoi cell is known to have area at least
   $`a_0=\sqrt3/2`$.  Oler's hexagonal constant is an aggregate finite-packing
   inequality.  Consequently the proposed $`m_+-O(D)`$ inner-parallel source count is
   not canonical.

The authoritative Target A endpoint remains
```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{111.1}
```
Equivalently,
```math
\boxed{d_{\rm sc}\ge\Delta_\Lambda}
\qquad\Longleftrightarrow\qquad
\boxed{h(G)\ge j}.
\tag{111.2}
```

---

# 112. Strict-rattler product germ and the local-KKT no-go theorem

Let
```math
A=C\sqcup R
```
be a triangle-free global $`N`$-point minimizer of diameter $`D`$, and suppose every
$`r\in R`$ is a genuine strict rattler:
```math
1<|r-q|<D
\qquad(q\ne r).
\tag{112.1}
```
Put
```math
\gamma=
\min_{\substack{r\in R\\q\ne r}}
\min\{|r-q|-1,\ D-|r-q|\}>0.
\tag{112.2}
```

## 112.1 Exact product germ

Choose the product neighborhood sufficiently small that each point moves by less than
$`\gamma/4`$, and shrink the core neighborhood further if necessary.  Every distance
involving a rattler then remains strictly in $`(1,D)`$.  Since every diameter pair of
$`A`$ lies in $`C`$, an original core diameter pair remains longer than every
rattler-involving pair.  Thus the local diameter depends only on the core coordinates.
Moreover no unit edge involving $`R`$ can appear, so triangle-freeness involving a
rattler is automatic in the neighborhood.

> **Theorem 112.1 (strict-rattler product germ).**  There are neighborhoods
> $`U_C,U_R`$ such that the local triangle-free diameter-$`D`$ minimizer germ factors
> as
> ```math
> \boxed{
> \mathcal F_D^\triangle(A)\cap(U_C\times U_R)
> =
> \bigl(\mathcal F_{D,C}^\triangle(C)\cap U_C\bigr)\times U_R,
> }
> \tag{112.3}
> ```
> and throughout this product neighborhood
> ```math
> \boxed{
> \operatorname{diam}(C',R')=\operatorname{diam}(C').
> }
> \tag{112.4}
> ```

In particular $`\{C\}\times U_R`$ is an open $`2|R|`$-dimensional family of
triangle-free global minimizers of diameter exactly $`D`$.

## 112.2 Active-jet consequence

Every active unit edge and active diameter edge lies entirely in $`C`$.  Therefore:

- every active constraint Jacobian has zero $`R`$-columns;
- every finite jet of the active constraint system has zero pure-rattler entries;
- every KKT multiplier on an $`R`$-incident inequality is zero; and
- the KKT Lagrangian Hessian has a zero $`R`$-block.

Hence a velocity supported on $`R`$ has identically zero active first variation,
stress work, and active second variation.  This is stronger than merely saying that
rattlers are first-order invisible.

> **Corollary 112.2 (local-KKT no-go).**  No theorem using only finite-order local
> active KKT/stress data can transfer the $`2|R|`$-dimensional rattler freedom into the
> independent scaffold response.  Any closing argument must use a finite first
> constraint event, global cardinality optimality, or another genuinely nonlocal
> source-to-scaffold invariant.

There is also an algebraic consequence.  Any polynomial relation in the rattler
coordinates that is claimed to hold for **every** nearby global minimizer must vanish
identically on the open product germ.  This does **not** prohibit selecting a special
lower-dimensional representative satisfying an additional alignment equation; it
prohibits deriving such an equation universally from local optimality.

---

# 113. Boundary Schur response as an exact planar strict gammoid

Section 102 gives the Schur response matrix
```math
S=
A[O,C^\partial]
-A[O,B]A[Z,B]^{-1}A[Z,C^\partial],
\tag{113.1}
```
where $`B`$ is matched bijectively to the interior lattice set $`Z`$.
The alternating-linkage interpretation can be sharpened to a full gammoid theorem.

Fix a matching $`\mu_0:B\to Z`$.  Orient the planar bipartite conflict graph by

- every unmatched conflict edge from left to right; and
- every matching edge of $`\mu_0`$ from right to left.

The free right vertices are exactly $`O`$.

> **Theorem 113.1 (contracted-transversal gammoid).**  For every
> $`J\subseteq C^\partial`$,
> ```math
> \boxed{
> J\text{ is independent after contracting }B
> \iff
> J\text{ links by }|J|\text{ pairwise vertex-disjoint directed alternating paths}
> \text{ to distinct vertices of }O.
> }
> \tag{113.2}
> ```

Indeed, a matching of $`B\cup J`$ differs from $`\mu_0`$ by alternating cycles and
vertex-disjoint augmenting paths from $`J`$ to right vertices unmatched by $`\mu_0`$,
which are precisely $`O`$.  Conversely, flipping $`\mu_0`$ along such a path family
matches $`B\cup J`$.

Since $`S`$ represents this contraction,
```math
\boxed{
\operatorname{rank}S=\lambda_S,
}
\tag{113.3}
```
where $`\lambda_S`$ is the maximum number of pairwise vertex-disjoint directed paths
from distinct vertices of $`C^\partial`$ to distinct vertices of $`O`$.
The orientation does not change the trusted planar radial embedding, so this is a
planar strict gammoid.

Directed vertex-Menger therefore gives the exact cut form
```math
\boxed{
\operatorname{rank}S
=
\min\{|W|:
W\text{ meets every directed }C^\partial\!\to O\text{ path}\},
}
\tag{113.4}
```
where terminal vertices may be used in the separator.  The trivial source cut has
size $`|C^\partial|`$.

Writing
```math
\zeta:=\dim\ker S
=|C^\partial|-\operatorname{rank}S,
\tag{113.5}
```
Target A becomes the assertion that the true minimum separator saves at least
$`\Delta_\Lambda-d_{\rm int}`$ vertices relative to that trivial source cut.
Planarity alone still does not imply this saving.

---

# 114. Exact response-corrected collar identities

Use the two-sided plateau normalization
```math
N_-:=\min\{q:D(q)=D\},
\qquad
m_+:=\max\{q:D(q)=d\},
\tag{114.1}
```
```math
\rho^\dagger=N_--m_+,
\qquad
t=\frac{D-d}{2}>1.
\tag{114.2}
```
Let $`K`$ be the hull of the independent $`m_+`$-point optimum.  For a generic
triangular-lattice translate put
```math
Z=(\Lambda+v)\cap\operatorname{int}K,
\tag{114.3}
```
```math
O=(\Lambda+v)\cap
\bigl(\operatorname{int}(K+\mathbb B)\setminus K\bigr),
\tag{114.4}
```
```math
Y_0=(\Lambda+v)\cap
\bigl(\operatorname{int}(K+t\mathbb B)\setminus(K+\mathbb B)\bigr),
\tag{114.5}
```
and
```math
\Gamma_t=O\sqcup Y_0.
\tag{114.6}
```

Because
```math
\nu(G)=|Z|+\operatorname{rank}S,
```
direct subtraction yields

> **Theorem 114.1 (response-corrected collar identity).**
> Define
> ```math
> \Phi(v):=|\Gamma_t(v)|-\operatorname{rank}S(v).
> \tag{114.7}
> ```
> Then
> ```math
> \boxed{
> d_{\rm sc}(v)-\Delta_\Lambda(v)
> =\Phi(v)-\rho^\dagger.
> }
> \tag{114.8}
> ```
> Equivalently,
> ```math
> \boxed{
> \Phi(v)=|Y_0(v)|+h(G_v).
> }
> \tag{114.9}
> ```

Thus Target A is exactly the existence of an admissible generic translate satisfying
```math
\boxed{\Phi(v)\ge\rho^\dagger.}
\tag{114.10}
```
A surviving counterexample has the pointwise integer inequality
```math
\boxed{\Phi(v)\le\rho^\dagger-1}
\tag{114.11}
```
for every admissible generic translate.

## 114.1 Translation average

Let
```math
\overline r_S
=\frac1{a_0}\int_F\operatorname{rank}S(v)\,dv
\tag{114.12}
```
over one lattice fundamental cell $`F`$, normalized so $`\operatorname{area}F=a_0`$.
Translation averaging gives
```math
\boxed{
\overline\Phi
=\frac{Pt+\pi t^2}{a_0}-\overline r_S.
}
\tag{114.13}
```
If
```math
g(v):=\Delta_\Lambda(v)-d_{\rm sc}(v)=\rho^\dagger-\Phi(v),
\tag{114.14}
```
then
```math
\boxed{
\overline g
=\rho^\dagger-\frac{Pt+\pi t^2}{a_0}+\overline r_S.
}
\tag{114.15}
```

Let
```math
J_{\rm av}:=\rho^\dagger-
\frac{\operatorname{area}((K+t\mathbb B)\setminus(K+\mathbb B))}{a_0},
\tag{114.16}
```
```math
B_{\rm av}:=\frac{P+\pi}{a_0}.
\tag{114.17}
```
Then
```math
\boxed{
\overline g=J_{\rm av}-B_{\rm av}+\overline r_S.
}
\tag{114.18}
```
A survivor therefore necessarily satisfies
```math
\boxed{
\overline r_S\ge1-(J_{\rm av}-B_{\rm av}).
}
\tag{114.19}
```
This is necessary, not contradictory.

## 114.2 Scalar plateau defect in its shortest form

Define
```math
q_r:=r-1-\frac{D(r)^2}{c}.
\tag{114.20}
```
The strict translated-lattice theorem and finite Oler give
```math
0<q_r\le\frac{\pi D(r)}2.
\tag{114.21}
```
Exact subtraction gives
```math
\boxed{
\rho^\dagger
=\frac{D^2-d^2}{c}+q_{N_-}-q_{m_+}.
}
\tag{114.22}
```
Writing
```math
\varepsilon^*=\pi d-P,
\tag{114.23}
```
Steiner's formula gives the particularly clean transfer identity
```math
\boxed{
J_{\rm av}-B_{\rm av}
=\frac{\varepsilon^*t}{a_0}+q_{N_-}-q_{m_+}.
}
\tag{114.24}
```
Equivalently, with
```math
E(n)=\frac{D(n)^2}{c}+\frac{\pi D(n)}2-(n-1),
```
this is the restored v1.5.1 identity
```math
J_{\rm av}-B_{\rm av}
=\pi t+\frac{\varepsilon^*t}{a_0}+E(m_+)-E(N_-).
\tag{114.25}
```
The sign remains uncontrolled at boundary order.

## 114.3 Minimal kernel certificate

Put
```math
s:=\Delta_\Lambda-d_{\rm int}.
\tag{114.26}
```
If $`s\le0`$, Target A is already closed.  For $`s>0`$, the desired response
inequality is exactly
```math
\boxed{\dim\ker S\ge s.}
\tag{114.27}
```
Equivalently there must exist a full-rank map
```math
\boxed{
T:\mathbb F^s\longrightarrow\mathbb F^{C^\partial},
\qquad
\operatorname{rank}T=s,
\qquad
ST=0.
}
\tag{114.28}
```
Lifting through the interior basis gives
```math
W=-A[Z,B]^{-1}A[Z,C^\partial]T,
\tag{114.29}
```
with
```math
A[Z,B]W+A[Z,C^\partial]T=0,
\tag{114.30}
```
```math
A[O,B]W+A[O,C^\partial]T=0.
\tag{114.31}
```
Because the representation is generic over the rational-function field, Schur minors
are rational functions.  After multiplying by $`\det A[Z,B]`$, their numerators are
the corresponding block-determinant polynomials.  A response-rank loss must therefore
come from structural absence of alternating linkages, not accidental numerical
cancellation with unrelated source-coordinate equations.

---

# 115. Continuum source Hall theorem with the exact plateau slack

Let $`A`$ be the genuine triangle-free source minimizer used by Target A, with
```math
|A|=N,
\qquad
H=\operatorname{conv}A,
\qquad
\operatorname{diam}H=D.
\tag{115.1}
```
Define the right endpoint of the $`D`$-plateau by
```math
N_+:=\max\{q:D(q)=D\},
\qquad
p:=N_+-N.
\tag{115.2}
```
The plateau theorem gives
```math
0\le p<\frac{\pi D}{2}.
\tag{115.3}
```

For every finite unit-separated set $`Q\subseteq H`$, define its strict source
conflict neighborhood
```math
N_A(Q)
=
\{a\in A:\exists q\in Q,\ |a-q|<1\}.
\tag{115.4}
```

> **Theorem 115.1 (continuum Hall inequality with plateau slack).**
> ```math
> \boxed{
> |Q|-|N_A(Q)|\le p
> \qquad
> \text{for every finite unit-separated }Q\subseteq H.
> }
> \tag{115.5}
> ```

### Proof

The replacement set
```math
A_Q=(A\setminus N_A(Q))\cup Q
\tag{115.6}
```
is unit-separated and lies in $`H`$, hence has diameter at most $`D`$.  By definition
of $`N_+`$, it has at most $`N_+`$ points.  Therefore
```math
N-|N_A(Q)|+|Q|\le N_+=N+p,
```
which is exactly (115.5). $`\square`$

This is a continuum Hall theorem: the candidate replacement set need not be a lattice
translate.

## 115.1 Deletion-cavity capacity

For $`T\subseteq A`$, define
```math
\mathcal U_A(T)
=
\{x\in H:|x-a|\ge1\text{ for every }a\in A\setminus T\}.
\tag{115.7}
```
Let $`\alpha_1(U)`$ be the maximum size of a unit-separated subset of $`U`$.  Since
$`T\subseteq\mathcal U_A(T)`$, while every unit-separated
$`Q\subseteq\mathcal U_A(T)`$ has $`N_A(Q)\subseteq T`$, Theorem 115.1 gives
```math
\boxed{
|T|\le\alpha_1(\mathcal U_A(T))\le|T|+p.
}
\tag{115.8}
```
Translation averaging with the triangular lattice yields the area consequence
```math
\boxed{
\operatorname{area}\mathcal U_A(T)
\le a_0(|T|+p).
}
\tag{115.9}
```

If one separately proves that the **same source representative** is already at the
right endpoint, so $`p=0`$, then (115.8) sharpens to exact hereditary cavity
saturation
```math
\alpha_1(\mathcal U_A(T))=|T|.
\tag{115.10}
```
In that special case singleton deletion cavities have diameter $`<1`$ and distinct
singleton cavities are disjoint.  These zero-slack conclusions must **not** be used for
the genuine Target A source unless $`p=0`$ has actually been established without
changing the source geometry.

## 115.2 Finite-amplitude cross-matching

Let $`T\subseteq A`$ and let $`T'\subset H`$ be another placement of $`|T|`$ points
such that
```math
(A\setminus T)\cup T'
\tag{115.11}
```
is unit-separated.  Form the bipartite graph on $`T\sqcup T'`$ with
```math
t\sim t'\iff |t-t'|<1.
\tag{115.12}
```

> **Theorem 115.2 (cross-matching with plateau slack).**
> ```math
> \boxed{
> \nu(T,T')\ge |T|-p.
> }
> \tag{115.13}
> ```

If $`\nu<|T|-p`$, Kőnig gives an independent set in the bipartite graph of size
```math
2|T|-\nu>|T|+p.
```
Adjoining this independent old/new mixture to $`A\setminus T`$ produces more than
$`N+p=N_+`$ unit-separated points in $`H`$, a contradiction.

For $`p=0`$ this becomes a perfect old/new cross-matching theorem and implies that the
feasible rigid-translation set of every source subset has diameter $`<1`$.  Again,
this stronger caging corollary is conditional on a proved zero-slack source endpoint.

The source theorem therefore supplies a genuine nonlocal invariant, but with an
unavoidable $`O(D)`$ plateau allowance in the current normalization.

---

# 116. Inner-parallel source capacity: exact one-sided form only

Let $`A\subset H`$ be any unit-separated source configuration of diameter $`D`$.  Let
$`m_+`$ be the right endpoint of a smaller diameter plateau with
```math
D(m_+)=d<D,
\qquad
t=\frac{D-d}{2}.
\tag{116.1}
```
When the inner parallel body
```math
H_t:=H\ominus t\mathbb B
\tag{116.2}
```
is nonempty, it satisfies
```math
\boxed{\operatorname{diam}H_t\le d.}
\tag{116.3}
```
Indeed, for $`x,y\in H_t`$ and $`u=(x-y)/|x-y|`$, both $`x+tu`$ and $`y-tu`$ lie in
$`H`$, so
```math
|x-y|+2t\le w_H(u)\le D.
```
Therefore the source points lying in $`H_t`$ form a unit-separated diameter-$`d`$
packing, and hence
```math
\boxed{
|A\cap H_t|\le m_+.
}
\tag{116.4}
```
Equivalently,
```math
\boxed{
|A\setminus H_t|\ge |A|-m_+.
}
\tag{116.5}
```
Thus the entire cardinality drop to the smaller plateau must be physically supported
in a source boundary shell of thickness $`t`$.

A stronger claim from an intermediate run asserted
```math
|A\cap H_t|\ge m_+-O(D).
\tag{116.6}
```
That claim is **not promoted**.  Its proof assigned area at least $`a_0`$ to each
individual full Voronoi cell.  The finite Oler constant $`a_0`$ is an aggregate
Dirichlet-cell inequality after planar cancellation; an individual many-sided Voronoi
cell need not have area $`\ge a_0`$.  No replacement argument currently recovers
(116.6) with an exact boundary-order error.

---

# 117. v1.6.0 source-to-response formulation and exact status

The post-v1.5.1 work makes the last gap more explicit but does not close it.

Write
```math
\zeta:=\dim\ker S
=|C^\partial|-\operatorname{rank}S,
\tag{117.1}
```
```math
s:=\Delta_\Lambda-d_{\rm int}.
\tag{117.2}
```
Then
```math
\boxed{
\Delta_\Lambda-d_{\rm sc}=s-\zeta.
}
\tag{117.3}
```
Using the response-corrected collar,
```math
\boxed{
\Delta_\Lambda-d_{\rm sc}
=\rho^\dagger-\Phi(v).
}
\tag{117.4}
```
Thus a survivor has the positive integer
```math
\boxed{
g:=\Delta_\Lambda-d_{\rm sc}=s-\zeta=\rho^\dagger-\Phi(v)\ge1.}
\tag{117.5}
```

## 117.1 Authoritative Target A theorem

Target A is resolved exactly by proving
```math
\boxed{
\zeta\ge s,
}
\tag{117.6}
```
or equivalently
```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{117.7}
```

In the planar-gammoid presentation, this says that the minimum alternating
$`C^\partial`$-to-$`O`$ vertex cut must save at least $`s`$ vertices relative to the
trivial source cut.

## 117.2 Historical source-exchange target (superseded)

The continuum Hall theorem supplies an exact source-side contradiction target.  Let
```math
p=N_+-N
\tag{117.8}
```
be the source plateau slack.  A sufficient closing theorem is:

> **Source-to-response exchange theorem.**  If the scaffold survivor has
> $`g>0`$, then the genuine source structure produces a finite unit-separated
> $`Q\subseteq H`$ such that
> ```math
> \boxed{
> |Q|-|N_A(Q)|\ge p+1.
> }
> \tag{117.9}
> ```

Equation (117.9) contradicts Theorem 115.1.  Equivalently, one may produce a source
subset and an alternative feasible placement whose old/new cross-matching loses more
than $`p`$ ranks, contradicting Theorem 115.2.

No map from the Schur deficit $`g`$ to such a source replacement is known.  This
paragraph is retained as history only.  It is not a valid open target: Theorem
119.2 later proves the sharper same-source bound
```math
|Q|-|N_A(Q)|\le\widehat p_H=\alpha_1(H)-N\le p
\qquad(Q\subseteq H\text{ unit-separated}),
\tag{117.10}
```
so neither the $`p+1`$ nor the later $`\widehat p_H+1`$ version can occur.  A
source-side closure must instead add boundary/diameter information—for example,
an add-one replacement whose entire configuration lies in $`\operatorname{int}H`$,
or a replacement outside $`H`$ with an explicit diameter-$`<D`$ certificate.

## 117.3 Binding no-go statements

The following are now explicitly ruled out as standalone closures:

1. **Finite-order local KKT/stress transfer.**  The strict-rattler product germ has a
   zero active $`R`$-block to every finite order.
2. **Scaffold-only response algebra.**  The independent smaller optimum exists without
   the source rattlers; global $`N`$-optimality of a survivor itself forces the opposite
   one-integer inequality.
3. **Planarity alone.**  The exact response is a planar gammoid, but planar annular
   networks may have full linkage rank.
4. **Scalar plateau defect alone.**  The exact quantity
   $`\varepsilon^*t/a_0+q_{N_-}-q_{m_+}`$ has uncontrolled sign at boundary order.
5. **Zero-slack source Hall without proof.**  The genuine source carries plateau slack
   $`p`$ unless a same-source right-endpoint extension is separately established.
6. **Per-cell Voronoi $`a_0`$ accounting.**  Oler's $`a_0`$ coefficient is aggregate,
   not an individual-cell lower bound.
7. **Near-triangular or strained-monomer bulk cost.**  Regression 109.2 remains binding.
8. **Long obtuse source runs as automatic Schürmann loose edges.**  Exact Schürmann
   hypotheses are still required.

An exploratory internet literature search conducted during the v1.6 run did not
identify a published theorem that supplies (117.6) or (117.9).  No web-only statement
is incorporated as a trusted theorem here.

## 117.4 Target B

Target B is unchanged and should not be revisited until Target A is closed unless a
Target B theorem directly supplies the missing source-to-response bridge:
```math
\boxed{
\operatorname{rank}\overline{\mathcal B}_\xi+I+r
\le T-q-r_\alpha,
}
\tag{117.10}
```
followed by exact topology-corrected transport.

## 117.5 Version history through v1.6.0

- **v1.5.1:** audited fixed-basis/phase contractions, plateau terminalization,
  phase-pure boundary minors, Schur response, source cage localization, corrected
  branchwise forest confinement, explicit outer-terminal bound, and exact two-sided
  defect transfer.
- **v1.6.0:** strict-rattler product-germ/local-KKT no-go; exact planar strict-gammoid
  completion of the Schur response; response-corrected collar capacity $`\Phi`$;
  minimal kernel-map certificate; continuum source Hall and cross-matching with the
  exact plateau slack; exact inner-parallel capacity; and audit corrections rejecting
  an unjustified zero-slack source terminalization and per-Voronoi-cell $`a_0`$
  accounting.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**


The v1.7.0 theorem-state archive is
docs/archive/erdos_problem_99_1.7.0-full.md; the continuation sections below
remain the active Target A route module.

---

# 118. v1.7.0 post-v1.6 audit policy and status

Sections 118 onward are the authoritative v1.7.0 continuation.  They preserve the
full v1.6.0 theorem stack and add only post-v1.6 results that survive direct audit.

The principal change is conceptual.  The genuine source hull now carries its own
exact finite-capacity Hall theory, and that capacity can be decomposed into an
explicit flag of adjacent-cardinality global optima.  In parallel, every genuine
source has a same-cardinality capacity shadow at pointwise displacement less than
one, with an exact finite-amplitude stress identity.

The following distinctions are binding throughout this continuation.

1. The source-hull capacity slack is not assumed to vanish.
2. A maximal triangle-free source extension need not preserve the old hybrid
   contact-minimal core or bridge-forest decomposition; the scaffold must be rebuilt
   if that extension is substituted for the source.
3. Oler's coefficient a_0 is an aggregate finite-packing coefficient and is never
   assigned as a lower bound to an arbitrary individual Voronoi cell.
4. The source-capacity endpoint and its exchange flag are exact finite-container
   statements.  External results on infinite completely saturated packings are
   research templates only unless an explicit finite-container transfer is proved.
5. The exact Level I target remains the Target A Schur-rank inequality.  No theorem
   below is to be interpreted as a proof of Erdős Problem #99.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

---

# 119. Exact source-hull capacity slack

Let A be the genuine triangle-free source minimizer used by Target A, with

```math
|A|=N,
\qquad
H=\operatorname{conv}A,
\qquad
\operatorname{diam}H=D=D(N).
\tag{119.1}
```

Let

```math
N_+=\max\{q:D(q)=D\},
\qquad
p=N_+-N,
\tag{119.2}
```

and define the exact unit-packing capacity of the actual source hull by

```math
\widehat N_H:=\alpha_1(H)
=\max\{|X|:X\subset H,\ |x-y|\ge1\ (x\ne y)\}.
\tag{119.3}
```

Put

```math
\widehat p_H:=\widehat N_H-N.
\tag{119.4}
```

> **Theorem 119.1 (source-hull capacity bound).**
> ```math
> \boxed{0\le \widehat p_H\le p<\frac{\pi D}{2}.}
> \tag{119.5}
> ```

Indeed, A itself shows $`\widehat N_H\ge N`$.  If $`q=\widehat N_H`$, a
q-point packing in H has diameter at most D.  Monotonicity gives

```math
D=D(N)\le D(q)\le D,
```

so $`D(q)=D`$ and hence $`q\le N_+`$.

For every finite unit-separated $`Q\subset H`$, define

```math
N_A(Q)=\{a\in A:\exists q\in Q,\ |a-q|<1\}.
\tag{119.6}
```

The replacement

```math
(A\setminus N_A(Q))\cup Q
\tag{119.7}
```

is unit-separated and lies in H.  Its cardinality is therefore at most
$`\widehat N_H`$.

> **Theorem 119.2 (exact same-source Hall budget).**
> ```math
> \boxed{|Q|-|N_A(Q)|\le\widehat p_H}
> \qquad(Q\subset H\text{ unit-separated}).
> \tag{119.8}
> ```

Thus v1.6.0 Theorem 115.1 may be sharpened from the global plateau allowance p to
the exact capacity allowance of the genuine source hull.

## 119.1 Deletion cavities and joint source budget

For $`T\subset A`$, put

```math
\mathcal U_A(T)
=
\{x\in H:|x-a|\ge1\text{ for all }a\in A\setminus T\}.
\tag{119.9}
```

Then

```math
\boxed{
|T|\le \alpha_1(\mathcal U_A(T))\le |T|+\widehat p_H.
}
\tag{119.10}
```

More generally, let $`T_i\subset A`$, and let finite sets
$`Q_i\subset\mathcal U_A(T_i)`$ be such that their union
$`Q=\bigcup_iQ_i`$ is unit-separated.  Then

```math
N_A(Q)\subseteq\bigcup_iT_i
```

and therefore

```math
\boxed{
|Q|-\left|\bigcup_iT_i\right|\le\widehat p_H.
}
\tag{119.11}
```

The source has one global hull-capacity budget; overlapping deletion regions do not
create independent copies of that budget.

## 119.2 Cross-matching with exact source-hull slack

Let $`T\subset A`$, and let $`T'\subset H`$ have $`|T'|=|T|`$ such that

```math
(A\setminus T)\cup T'
```

is unit-separated.  Join $`t\in T`$ to $`t'\in T'`$ when $`|t-t'|<1`$.
The same independent-set argument as in Theorem 115.2 gives

```math
\boxed{
\nu(T,T')\ge |T|-\widehat p_H.
}
\tag{119.12}
```

The threshold $`\widehat p_H`$, not p, is the authoritative same-source
finite-amplitude allowance.

---

# 120. Self-container tightness and boundary reserve

Assume H is full-dimensional.  Fix $`c\in\operatorname{int}H`$.  Every finite set
$`X\subset\operatorname{int}H`$ is contained in a strict homothetic contraction

```math
c+\lambda(H-c),
\qquad
\lambda<1.
\tag{120.1}
```

Consequently $`\operatorname{diam}X< D`$ whenever $`|X|\ge N`$ would otherwise
contradict $`D(N)=D`$.

> **Theorem 120.1 (source self-container theorem).**
> ```math
> \boxed{\alpha_1(\operatorname{int}H)\le N-1.}
> \tag{120.2}
> ```

Hence every unit-separated $`X\subset H`$ with

```math
|X|=N+k,
\qquad
k\ge1,
```

satisfies

```math
\boxed{|X\cap\partial H|\ge k+1.}
\tag{120.3}
```

In particular, if the source Hall replacement (119.7) has positive surplus

```math
\sigma=|Q|-|N_A(Q)|\ge1,
```

then

```math
\boxed{
|(A\setminus N_A(Q))\cap\partial H|+|Q\cap\partial H|
\ge \sigma+1.
}
\tag{120.4}
```

This is a boundary-reserve condition on the complete replacement.  It does not
force Q itself to meet $`\partial H`$; retained source boundary vertices may supply
the reserve.

---

# 121. Maximal triangle-free extension inside the genuine source hull

Define

```math
\alpha^\triangle(H;A)
=
\max\{|B|:A\subseteq B\subseteq H,\ B\text{ unit-separated and triangle-free}\}.
\tag{121.1}
```

Put

```math
k=\alpha^\triangle(H;A)-N
```

and choose a maximizing extension B.  Then

```math
A\subseteq B\subseteq H,
\qquad
|B|=q=N+k,
\qquad
0\le k\le\widehat p_H.
\tag{121.2}
```

B contains an original diameter pair of A while lying in H, so
$`\operatorname{diam}B=D`$.  Monotonicity therefore gives

```math
\boxed{D(q)=D,}
\tag{121.3}
```

and B is a triangle-free global minimizer at its new cardinality q.

Let R be any original strict-rattler set of A and define

```math
R_B=
\{r\in R:|r-b|>1\text{ for every }b\in B\setminus\{r\}\}.
\tag{121.4}
```

Every original rattler remains at distance strictly less than D from every new
point of B: for fixed r the convex function $`x\mapsto|r-x|`$ attains its maximum
on H at an extreme point of H, every such extreme point belongs to A, and r was
originally non-diametral.

One newly added point can be at unit distance from at most five original strict
rattlers.  Six unit-distance rattlers around one new point would have six angular
gaps each at least $`\pi/3`$, forcing all six gaps to equal $`\pi/3`$ and hence a
unit equilateral triangle.

> **Theorem 121.1 (rattler retention under maximal triangle-free extension).**
> ```math
> \boxed{|R_B|\ge |R|-5k\ge |R|-5\widehat p_H.}
> \tag{121.5}
> ```

Thus a super-boundary strict-rattler population remains super-boundary.

## 121.1 Append-maximality and unit covering

Put

```math
\mathcal F_B
=
\{x\in H:|x-b|\ge1\text{ for every }b\in B\}.
\tag{121.6}
```

If $`x\in\mathcal F_B`$, the unit-separated set $`B\cup\{x\}`$ cannot remain
triangle-free.  Since B itself is triangle-free, x must complete a unit equilateral
triangle on a unit edge of B.  Hence

```math
\boxed{
\mathcal F_B
\subseteq
\{\text{equilateral apices of unit edges of }B\},
}
\tag{121.7}
```

and in particular $`|\mathcal F_B|\le2e_1(B)`$.

Moreover, if some x had $`|x-b|>1`$ for all b, then adding x would create no unit
edge and therefore no triangle.  Thus

> **Corollary 121.2 (same-hull unit covering).**
> ```math
> \boxed{H\subseteq\bigcup_{b\in B}\overline B(b,1).}
> \tag{121.8}
> ```

This saturation is obtained in the genuine source hull.  It does not assert that
the old contact-minimal core or hybrid bridge forest remains the contact normal form
of B.

Define the residual source-hull capacity

```math
\boxed{
\tau:=\widehat N_H-|B|=\widehat p_H-k.
}
\tag{121.9}
```

Repeating Theorem 119.2 with B gives

```math
\boxed{|Q|-|N_B(Q)|\le\tau}
\tag{121.10}
```

for every unit-separated $`Q\subset H`$, and every feasible old/new replacement
of $`T\subset B`$ satisfies

```math
\boxed{\nu(T,T')\ge |T|-\tau.}
\tag{121.11}
```

The quantity $`\tau`$ is the remaining same-hull capacity after all triangle-free
append-only capacity compatible with retaining A has been exhausted.

---

# 122. Fixed-container capacity endpoint theorem

The following statement is more general than the source normalization and is useful
independently.

Let H be any compact set of finite unit-packing capacity

```math
M=\alpha_1(H).
```

Let $`P\subset H`$ be any unit-separated q-point set and choose a capacity-maximizing
unit-separated set

```math
X_{\max}\subset H,
\qquad
|X_{\max}|=M.
```

Form the strict conflict graph on $`P\sqcup X_{\max}`$, with

```math
p\sim x\iff |p-x|<1.
\tag{122.1}
```

Every independent set in this graph is a unit-separated subset of H, so its size is
at most M.  The whole shore $`X_{\max}`$ is independent of size M.  Hence
$`\alpha(G)=M`$.  Koenig's theorem gives

> **Theorem 122.1 (capacity endpoint matching).**
> ```math
> \boxed{\nu(P,X_{\max})=|P|=q.}
> \tag{122.2}
> ```

Thus every smaller packing in the same container can be injected into a
capacity-maximizing packing by strict-conflict edges of length less than one.

For unit-separated $`Q\subset H`$, the replacement

```math
(P\setminus N_P(Q))\cup Q
```

has at most M points.  Taking $`Q=X_{\max}`$, Theorem 122.1 shows
$`N_P(X_{\max})=P`$.  Therefore:

> **Theorem 122.2 (exact fixed-container Hall slack).**
> ```math
> \boxed{
> \max_{\substack{Q\subseteq H\\ Q\text{ unit-separated}}}
> \bigl(|Q|-|N_P(Q)|\bigr)
> =M-|P|.
> }
> \tag{122.3}
> ```

Applied to A this gives exact maximum Hall slack $`\widehat p_H`$.  Applied to B it
gives exact maximum Hall slack $`\tau`$:

```math
\boxed{
\max_Q\bigl(|Q|-|N_B(Q)|\bigr)=\tau.
}
\tag{122.4}
```

The source capacity allowance is therefore not merely an upper bound; it is attained
by every capacity endpoint through an appropriate matching.

## 122.1 Diameter graph at a source capacity endpoint

For the normalized source B, $`|B|=q`$, $`D(q)=D`$, and
$`X_{\max}\subset H`$ has diameter at most D.  Therefore every q-point subset
$`Y\subset X_{\max}`$ satisfies

```math
\boxed{\operatorname{diam}Y=D.}
\tag{122.5}
```

Let $`\mathcal D(X_{\max})`$ be the graph whose edges join pairs at distance D.
Then

```math
\alpha(\mathcal D(X_{\max}))\le q-1,
```

so its vertex-cover number satisfies

```math
\boxed{
\tau_{\rm VC}(\mathcal D(X_{\max}))\ge M-q+1=\tau+1.
}
\tag{122.6}
```

Because every D-edge realizes the diameter of H, both endpoints lie on
$`\partial H`$.  Consequently

```math
\boxed{|X_{\max}\cap\partial H|\ge\tau+1.}
\tag{122.7}
```

## 122.2 Complete finite-container saturation

A capacity endpoint is completely saturated relative to H in the elementary finite
sense: for no $`r\ge1`$ can r-1 of its points be removed and r new points inserted
inside H while preserving unit separation, since that would produce M+1 points in H.
This observation is exact but should not be conflated with the stronger infinite-space
notions in the saturation literature.

---

# 123. Planarity of strict conflict graphs

Let P and Q be finite, spatially disjoint, internally unit-separated point sets in the
plane.  Join $`p\in P`$ to $`q\in Q`$ when $`|p-q|<1`$, drawing each edge as the
straight segment pq.

> **Theorem 123.1 (straight-line planarity of strict conflicts).**
> The resulting bipartite graph is planar in its straight-line drawing.

If two disjoint edges $`p_1q_1`$ and $`p_2q_2`$ crossed at z, then

```math
2
\le |p_1-p_2|+|q_1-q_2|
\le |p_1q_1|+|p_2q_2|
<2,
```

contradiction.  The same metric obstruction prevents an edge from passing through an
unrelated vertex.  This supplies a genuine planar source-capacity conflict network,
but planarity alone still does not imply a Target A rank deficit.

---

# 124. Source-capacity plateau exchange flag

Return to the maximal triangle-free extension B in H.  Put

```math
|B|=q,
\qquad
M=\alpha_1(H)=q+\tau,
```

and choose a capacity endpoint $`X\subset H`$, $`|X|=M`$.  Regard the strict
conflict graph as a transversal-matroid presentation on the ground set X with right
shore B.  By Theorem 122.1 its rank is q.

Choose a maximum matchable basis

```math
\mathcal B\subset X,
\qquad
|\mathcal B|=q,
```

and write

```math
E_0=X\setminus\mathcal B,
\qquad
|E_0|=\tau.
\tag{124.1}
```

For $`e\in E_0`$, let $`C_e\subset\mathcal B\cup\{e\}`$ be its fundamental circuit.
For $`A_0\subseteq E_0`$, put

```math
U_{A_0}=\bigcup_{e\in A_0}C_e,
\qquad
W_{A_0}=N_B(U_{A_0}).
\tag{124.2}
```

The fixed-basis tight-union theorem of Section 97 is a general transversal-matroid
statement and gives

```math
\boxed{|U_{A_0}|-|W_{A_0}|=|A_0|.}
\tag{124.3}
```

Define the mixed configuration

```math
P_{A_0}=(B\setminus W_{A_0})\cup U_{A_0}.
\tag{124.4}
```

It is unit-separated, lies in H, and has exactly q+|A_0| points.  Since
$`D(q)=D`$ and $`D(\cdot)`$ is nondecreasing,

> **Theorem 124.1 (source-capacity plateau exchange theorem).**
> ```math
> \boxed{
> |P_{A_0}|=q+|A_0|,
> \qquad
> \operatorname{diam}P_{A_0}=D(q+|A_0|)=D.
> }
> \tag{124.5}
> ```
>
> Thus every subset of the nonbasis capacity elements produces an explicit global
> optimum at the corresponding intermediate cardinality.

In particular

```math
\boxed{D(q+r)=D\qquad(0\le r\le\tau).}
\tag{124.6}
```

This is stronger than the scalar statement that q and M lie on the same plateau: the
intermediate global optima are coupled to one fixed source and one fixed capacity
endpoint by nested Hall-tight supports.

## 124.1 Adjacent-cardinality flag

Order

```math
E_0=\{e_1,\ldots,e_\tau\}
```

and put

```math
U_i=\bigcup_{r\le i}C_{e_r},
\qquad
W_i=N_B(U_i),
\qquad
P_i=(B\setminus W_i)\cup U_i.
\tag{124.7}
```

Then

```math
P_0=B,
\qquad
|P_i|=q+i,
\qquad
\operatorname{diam}P_i=D.
\tag{124.8}
```

Let

```math
\Delta X_i=U_i\setminus U_{i-1},
\qquad
\Delta B_i=W_i\setminus W_{i-1}.
\tag{124.9}
```

Subtracting successive deficiencies gives

```math
\boxed{|\Delta X_i|-|\Delta B_i|=1,}
\tag{124.10}
```

and

```math
\boxed{
P_i=(P_{i-1}\setminus\Delta B_i)\cup\Delta X_i.
}
\tag{124.11}
```

Therefore the entire residual capacity decomposes into a flag of exact net-+1
exchanges between adjacent-cardinality global optima.

## 124.2 First-triangle localization

If all $`P_i`$ are triangle-free, then $`P_\tau`$ is a triangle-free global optimum
at full source-hull capacity, so its same-hull capacity slack is zero.

Otherwise let j be the first index for which $`P_j`$ contains a unit equilateral
triangle.  Since $`P_{j-1}`$ was triangle-free and the step only deletes
$`\Delta B_j`$ and inserts $`\Delta X_j`$, every newly appearing triangle contains
at least one point of $`\Delta X_j`$.  Thus the first triangle is localized to one
Hall-tight adjacent plateau transition satisfying

```math
\boxed{|\Delta X_j|=|\Delta B_j|+1.}
\tag{124.12}
```

## 124.3 Rattler-loss concentration along the flag

Let $`R\subset B`$ be a retained strict-rattler population of size $`\rho`$.  Either
the capacity endpoint $`P_\tau`$ retains at least $`\rho/2`$ original rattler
positions, or more than $`\rho/2`$ are removed across the $`\tau`$ increments.
In the latter case, some i satisfies

```math
|R\cap\Delta B_i|
\ge\frac{\rho}{2\tau}.
```

Since $`q`$ and $`M=q+\tau`$ lie on the D-plateau and the plateau theorem gives
$`\tau<\pi D/2`$,

```math
\boxed{
|R\cap\Delta B_i|>\frac{\rho}{\pi D}.
}
\tag{124.13}
```

Hence a super-boundary source has the exact dichotomy: either a capacity endpoint
retains $`\Omega(\rho)`$ original rattler positions, or one single n-to-(n+1)
plateau transition replaces a diverging number of original strict rattlers.

---

# 125. Same-cardinality saturation by replacements

Canonical Theorem 63.1 obtains unit covering by adding boundary-order many points.
For the flexible Target A source one can instead saturate at the same cardinality by
replacements while preserving any specified strict-rattler set pointwise.

Let A be a triangle-free N-point global minimizer of diameter D in the fixed original
hull H, and let $`R\subset A`$ consist of strict rattlers.  If a point
$`y\in H`$ satisfies

```math
|y-a|>1
\qquad(a\in A),
\tag{125.1}
```

then the current minimizer has at least one unit contact: otherwise its finite minimum
separation would exceed one and a uniform contraction would contradict global
minimality.  No endpoint of a unit contact lies in R.  Delete one such endpoint x and
insert y.  The new N-point set is unit-separated, triangle-free, and contained in H,
so its diameter is at most D and hence exactly D(N)=D.

The inserted point creates no unit contact.  Therefore the total number of unit
contacts strictly decreases.  Repeating terminates after finitely many replacements.

Every r in R remains non-diametral against every inserted point because

```math
\max_{z\in H}|r-z|
=
\max_{z\in\operatorname{ext}H}|r-z|
<D,
```

and all extreme points of H belong to the original source A.

> **Theorem 125.1 (same-cardinality rattler-preserving saturation).**
> There is a triangle-free N-point global minimizer $`A^{\rm sat}\subset H`$ such
> that every point of R remains at its original position and remains a genuine strict
> rattler, while
> ```math
> \boxed{
> H\subseteq\bigcup_{a\in A^{\rm sat}}\overline B(a,1).
> }
> \tag{125.2}
> ```

This removes the boundary-order cardinality expenditure of Theorem 63.1 when only
same-cardinality saturation and the strict-rattler population are needed.  It does
not preserve the old contact-minimal core or hybrid forest automatically.

---

# 126. Capacity shadow and bounded-displacement optimum partner

Let A be the genuine N-point source in H and let

```math
M=\alpha_1(H)=N+\widehat p_H.
```

Choose $`X_{\max}\subset H`$ with $`|X_{\max}|=M`$.  Theorem 122.1 gives an
injection

```math
\mu:A\hookrightarrow X_{\max}
```

such that

```math
\boxed{|a-\mu(a)|<1\qquad(a\in A).}
\tag{126.1}
```

Let

```math
Y=\mu(A).
```

Then Y is a unit-separated N-point subset of H.  Hence

```math
\boxed{\operatorname{diam}Y=D(N)=D.}
\tag{126.2}
```

Thus Y is a same-cardinality global optimum contained in one capacity endpoint and
pointwise matched to the source at displacement less than one.

Put

```math
L=\operatorname{conv}Y,
\qquad
\delta=\max_{a\in A}|a-\mu(a)|<1.
\tag{126.3}
```

Since $`L\subseteq H`$, while every convex combination of source points can be
matched coefficientwise to a convex combination of their images,

> **Theorem 126.1 (capacity-shadow hull control).**
> ```math
> \boxed{
> L\subseteq H\subseteq L+\delta\mathbb B,
> \qquad
> d_{\rm H}(H,L)\le\delta<1.
> }
> \tag{126.4}
> ```

Consequently

```math
\boxed{0\le P_H-P_L\le2\pi\delta<2\pi,}
\tag{126.5}
```

and

```math
\boxed{
0\le \operatorname{area}H-\operatorname{area}L
\le \delta P_L+\pi\delta^2.
}
\tag{126.6}
```

This is the first exact pointwise coupling of the genuine source to another global
optimum inside its own capacity endpoint.

---

# 127. Finite-chord stress identity

Label the source and its capacity shadow by

```math
p_i\in A,
\qquad
y_i=\mu(p_i),
\qquad
v_i=y_i-p_i.
\tag{127.1}
```

Fix any normalized proper KKT stress $`(\alpha,\beta)`$ of A from Theorem 4.1.
For an active source contact ij,

```math
2(p_i-p_j)\cdot(v_i-v_j)+|v_i-v_j|^2\ge0,
\tag{127.2}
```

while for an active source diameter edge ij,

```math
2(p_i-p_j)\cdot(v_i-v_j)+|v_i-v_j|^2\le0.
\tag{127.3}
```

The virtual-work identity (11.7) cancels the weighted linear terms.  Therefore:

> **Theorem 127.1 (finite-chord stress inequality).**
> ```math
> \boxed{
> \sum_{ij\in C}\alpha_{ij}|v_i-v_j|^2
> \ge
> \sum_{ij\in H_D}\beta_{ij}|v_i-v_j|^2.
> }
> \tag{127.4}
> ```

More exactly,

```math
\boxed{
\begin{aligned}
&\sum_{ij\in C}\alpha_{ij}\bigl(|y_i-y_j|^2-1\bigr)
+\sum_{ij\in H_D}\beta_{ij}\bigl(D^2-|y_i-y_j|^2\bigr)\\
&\qquad=
\sum_{ij\in C}\alpha_{ij}|v_i-v_j|^2
-\sum_{ij\in H_D}\beta_{ij}|v_i-v_j|^2
\ge0.
\end{aligned}
}
\tag{127.5}
```

Equality holds exactly when every positively stressed source contact remains an exact
unit contact in Y and every positively stressed source diameter edge remains an exact
diameter edge in Y.

This is a finite-amplitude identity along an actual chord between two same-cardinality
global optima.  As required by the product-germ theorem, strict rattlers carry no
direct local stress term; their importance is that their capacity images are coupled
to the stressed backbone in the same finite optimum partner.

---

# 128. Fundamental-circuit sequentialization and exact cycle budget

Let C be a fundamental circuit of any strict conflict transversal matroid, with right
neighborhood W.  Then

```math
|C|=|W|+1,
\tag{128.1}
```

and every proper subset of C is matchable.  In particular every $`w\in W`$ has
degree at least two: if w had unique neighbor x, then $`C\setminus\{x\}`$ would
have at most $`|W|-1`$ neighbors and would be unmatchable.

The induced circuit graph is connected.  Suppose first that it is acyclic.  If
$`w=|W|`$, then the tree has $`2w+1`$ vertices and 2w edges.  Since every right
vertex has degree at least two, every right vertex has degree exactly two.  Contracting
right vertices therefore gives an ordinary tree on the |C| left vertices.

Peel a leaf left vertex x and its unique adjacent blocker w.  In the packing exchange,
x conflicts with no retained source point except w, so w may be swapped for x.  The
residual bipartite graph is again a circuit of the same tree type.  Iteration ends with
one left point and no blocker, which is appended in the final net-+1 step.

> **Theorem 128.1 (tree-circuit sequentialization).**
> A tree fundamental circuit admits an exact sequence of one-for-one feasible swaps,
> followed by one final append.  In the source-capacity plateau each intermediate
> same-cardinality configuration is a global optimum, and the final configuration is
> the adjacent-cardinality global optimum.

No triangle-free conclusion is asserted for the intermediate swaps; exact unit
triangles may first appear during this sequence.

For a general connected planar circuit let e be its number of strict-conflict edges
and $`w=|W|`$.  Define

```math
\kappa=e-2w.
\tag{128.2}
```

Since every right degree is at least two,

```math
\boxed{
\kappa=\sum_{b\in W}(\deg b-2)\ge0.
}
\tag{128.3}
```

Euler's formula for the straight-line planar circuit graph gives simultaneously

```math
\boxed{
\kappa=\#\{\text{bounded faces of the circuit graph}\}.
}
\tag{128.4}
```

Thus the obstruction to pure sequential tree exchange has an exact planar cycle
budget rather than an unspecified Hall-circuit complexity.

---

# 129. Codimension-one triangle walls require straight root paths

Retain the affine one-root forest flat of Section 62.  Theorem 62.2 proves that every
relatively open codimension-one unit-triangle wall has one side identically unit and
that this persistent side lies entirely in the fixed part.

Consider such a triangle wall whose third vertex a is an unpinned forest vertex and
whose fixed persistent side is bc.  Since $`|b-c|=1`$, the conditions

```math
|a(x)-b|=|a(x)-c|=1
```

force $`a(x)`$ to equal one of the two fixed equilateral apices of bc.

The affine displacement map of a is

```math
x\longmapsto
\sum_{e\in P(a)}x_eJu_e,
\tag{129.1}
```

where $`P(a)`$ is the root path to a.  Its rank is

```math
\dim\operatorname{span}\{u_e:e\in P(a)\}.
\tag{129.2}
```

> **Theorem 129.1 (straight-path triangle-wall criterion).**
> If the root path of a contains two nonparallel retained unit-edge directions, then
> every triangle locus involving a has codimension at least two in the affine forest
> coordinates.  Hence a codimension-one triangle wall involving a moving forest
> vertex is possible only when every retained edge on its root path is parallel to one
> common line.

Thus only straight-chain prefixes can genuinely separate the affine forest parameter
space by codimension-one triangle walls.  This refines the general factor-exclusion
theorem; it does not yet bound the number or total length of those straight chains.

---

# 130. Exact Oler-capacity split

For a fixed convex hull H with perimeter P_H and a unit-separated r-point packing P in
H, define

```math
\mathscr O_H(r)
=
\operatorname{area}H+c_0P_H-a_0(r-1).
\tag{130.1}
```

Let $`M=\alpha_1(H)`$.  Since the geometric hull terms are identical,

```math
\boxed{
\mathscr O_H(r)=a_0(M-r)+\mathscr O_H(M).
}
\tag{130.2}
```

Finite Oler gives $`\mathscr O_H(M)\ge0`$.  For the maximal triangle-free source
extension B this becomes

```math
\boxed{
\mathscr O_H(|B|)=a_0\tau+\mathscr O_H(M),
\qquad
\mathscr O_H(|B|)\ge a_0\tau.
}
\tag{130.3}
```

The source Oler surplus therefore contains an exact integer capacity term plus the
nonnegative residual Oler slack of a capacity endpoint.  This identity does not by
itself distinguish forest vertices from core vertices; the cancellation warning of
Section 21 remains binding.

---

# 131. External literature checked during the v1.7 run

Internet literature search is permitted for subsequent Target A work.  The following
results were checked for applicability but are not imported as Target A theorems.

1. **Bondarenko--Hardin--Saff, mesh ratios for best packings**
   (arXiv:1212.6211).  For best-packing
   configurations that arise as limits of Riesz s-energy minimizers as
   $`s\to\infty`$, the covering-radius/separation mesh ratio is at most one.  This
   does not state that every arbitrary best-packing representative has that property.
   The self-contained replacement-saturation Theorem 125.1 is what is trusted here.

2. **Fejes Toth--Kuperberg--Kuperberg, highly saturated packings and reduced coverings**
   (arXiv:math/9511225).  Their notions of
   n-saturation and complete saturation formalize the impossibility of replacing
   n-1 packed bodies by n.  A finite capacity endpoint in H is completely saturated
   relative to H for the trivial cardinality reason recorded in Section 122.2, but
   infinite-plane density conclusions do not automatically transfer to a bounded
   source hull.

3. **G. Kuperberg--K. Kuperberg--W. Kuperberg, lattice packings with gap defects are
   not completely saturated** (arXiv:math/0303366).  They prove that a planar honeycomb circle packing
   with an arbitrarily narrow linear gap defect is not completely saturated.  This is
   directly suggestive for the coherent strained-monomer regression: small distributed
   clearance may be concentratable by a finite rearrangement until one extra point
   fits.  No theorem has yet transferred their infinite linear-gap construction to a
   finite monomer/dimer scaffold in the source hull.

4. **Gensane, generation of optimal packings from optimal packings**
   (Electronic Journal of Combinatorics 16 (2009), R24; DOI 10.37236/113).  The paper
   defines weak and strong generation and conjectures an infinite sequence of strong
   generators for every compact convex container.  The general generation statement
   is conjectural, not available as a black-box bridge.  The exchange flag of Section
   124 is an unconditional discrete generation result specific to the source-capacity
   conflict matroid.

These references sharpen the research direction but do not alter the Level I status.

---

# 132. Regressions and no-go statements added in v1.7

The following remain binding.

1. The exact source Hall slack $`\widehat p_H`$ and residual slack $`\tau`$ need not
   vanish.
2. Capacity alone cannot produce a Hall surplus above its own exact endpoint:
   Theorem 122.2 proves that the maximum source deficiency is exactly the available
   capacity slack.
3. A maximal triangle-free extension can be unit-covering saturated, retain a
   super-boundary rattler population, and still have positive exchange-only capacity.
4. The source-capacity exchange flag consists of global optima, but the intermediate
   configurations need not remain triangle-free.
5. Tree-circuit sequentialization does not prevent the first unit triangle from
   appearing during one of the swaps.
6. Planarity of the source conflict graph and of the target gammoid does not alone
   imply the required rank loss.
7. The capacity shadow gives a bounded-displacement same-cardinality optimum partner,
   not a coordinate identification with the independent smaller optimum used in the
   Schur scaffold.
8. The finite-chord stress identity is nonnegative but does not yet force a positive
   lower bound from the strict rattler population, since strict rattlers carry no
   active source stress.
9. The same-cardinality replacement-saturation theorem may destroy the old hybrid
   core/forest contact normal form.  Use it only where that structure is unnecessary,
   or rebuild the normal form after the replacement.
10. Codimension-one affine triangle walls are confined to straight root paths, but
    arbitrarily long straight rooted chains are not yet excluded.
11. The Kuperberg gap-defect theorem is an external infinite-packing result; applying
    it to finite coherent monomer regions requires a new quantitative transfer
    theorem.
12. No individual Voronoi cell is assigned area a_0.

The strained near-triangular finite-patch regression remains valid: append-maximality,
unit covering, many strict points, and boundary-order unused capacity do not imply
global diameter optimality.  Global extremality remains essential.

---

# 133. Authoritative Target A frontier in v1.7.0

The direct canonical endpoint is unchanged.  For the plateau-terminalized Schur
response write

```math
\zeta=\dim\ker S=|C^\partial|-\operatorname{rank}S,
\qquad
s=\Delta_\Lambda-d_{\rm int}.
\tag{133.1}
```

A survivor has

```math
\boxed{
g=\Delta_\Lambda-d_{\rm sc}=s-\zeta=\rho^\dagger-\Phi(v)\ge1.
}
\tag{133.2}
```

Target A is resolved exactly by

```math
\boxed{\zeta\ge s,}
\tag{133.3}
```

or equivalently

```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{133.4}
```

An earlier draft incorrectly described a fixed-source contradiction threshold.  For
the original genuine source A, Theorem 119.2 instead proves
```math
\boxed{
|Q|-|N_A(Q)|\le\widehat p_H
\qquad(Q\subset H\text{ unit-separated}).
}
\tag{133.5}
```
Thus a same-hull deficiency $`\widehat p_H+1`$ cannot be the missing theorem; it is
ruled out by the exact capacity of H.  The source route must add a boundary/diameter
certificate to a replacement, or transport the Schur deficit directly.  A distinct
valid route is the scaffold-wide Hall target from Section 81: for the independent
smaller optimum $`X_m`$ and its inner lattice shore $`Y_{\rm in}`$, prove

```math
\boxed{h(G)\ge j}
\qquad\text{equivalently}qquad
\boxed{d_{\rm sc}\ge\Delta_\Lambda}.
\tag{133.5a}
```

This does not ask for a forbidden same-hull source deficiency.  The witness uses the
larger shore $`Y\subset L`$, and then the open-body diameter certificate supplies the
contradiction.  The unresolved source task is to transport source information into
$`133.5a`$, or to prove (133.5a) directly from the global scaffold geometry.

If one legally replaces A by the maximal triangle-free extension B and rebuilds the
Target A scaffold for B, the analogous residual-capacity proposal is likewise
impossible:
```math
|Q|-|N_B(Q)|\le\tau
\qquad(Q\subset H\text{ unit-separated}),
\tag{133.6}
```
by Theorem 122.2.  The quantity $`\tau`$ is exactly the maximum Hall deficiency
available from H and B.  Any valid B-based closure must therefore use the global
relationship to the independent smaller-optimum scaffold, boundary/diameter control,
or a direct response-rank argument.

## 133.1 First-transition alternative after the source-Hall audit

Use the source-capacity flag

```math
B=P_0\rightsquigarrow P_1\rightsquigarrow\cdots\rightsquigarrow P_\tau.
```

A high-value closure theorem would prove the following exact alternative for the first
Hall-tight transition that creates a unit triangle:

> **First-transition alternative.**  If $`P_{j-1}`$ is triangle-free and $`P_j`$
> is the first member containing a unit triangle, then either
> 1. the transition admits a triangle-free perturbation or different basis/circuit
>    choice producing a triangle-free global optimum of cardinality q+j; or
> 2. the transition support produces at least the missing Schur nullity
>    $`\Delta_\Lambda-d_{\rm int}`$.

The tree-circuit theorem reduces the acyclic case to a sequence of one-for-one swaps;
the cyclic obstruction is measured exactly by the bounded-face count $`\kappa`$.

This alternative must not be presented as a route to a fixed-source Hall surplus:
$`\widehat p_H+1`$ is forbidden by (119.8), and even a positive Hall surplus is
useful only when the resulting replacement has a boundary/diameter certificate.
The unresolved second alternative is therefore direct source-to-Schur transport,
or an exterior-compatible add-one replacement with
$`\operatorname{diam}<D`$.

## 133.2 Preferred next theorem: finite gap-concentration for monomer bulk

The surviving scaffold has only two locally Hall-neutral phases.  The monomer phase is
a bounded-displacement deformation of the triangular lattice.  The Kuperberg gap
mechanism suggests the following finite theorem:

> **Finite monomer gap-concentration theorem.**  A sufficiently large coherent
> zero-charge monomer domain in a globally optimal source/scaffold, carrying positive
> distributed nearest-neighbor clearance but only boundary-order total clearance,
> admits a finite rearrangement inside the relevant hull/collar that frees one extra
> unit-separated site without increasing the diameter.

Such a theorem would convert the main strained-monomer regression from an obstruction
into a contradiction.  It must be proved in the finite container with explicit
boundary control; the infinite gap-defect theorem cannot simply be quoted.

## 133.3 Preferred next theorem: capacity-shadow transport

The capacity shadow supplies a same-cardinality global optimum Y with

```math
|p_i-y_i|<1,
\qquad
d_{\rm H}(\operatorname{conv}A,\operatorname{conv}Y)<1,
```

and the finite stress identity (127.5).  A second possible closure is to transport this
bounded-displacement chord through deletion of the strict-rattler population to the
smaller plateau endpoint and prove that the induced boundary displacement lies in the
kernel of the Schur response with dimension at least s.

No such transport theorem is currently proved.

## 133.4 Preferred next theorem: straight-chain barrier elimination

The affine forest triangle-wall theorem now shows that only collinear root paths can
form codimension-one triangle barriers.  A fourth closure route is to prove that a
super-boundary number of forest degrees of freedom cannot all be confined behind
straight-chain barriers in a global minimizer.  Any proof must use global finite
capacity or exact source-face geometry; long rooted chains are valid local
regressions.

---

# 134. Version history through v1.7.0

- **v1.5.1:** fixed-basis/phase contractions, plateau terminalization, phase-pure
  boundary minors, Schur response, source cage localization, corrected branchwise
  forest confinement, explicit outer-terminal bound, exact two-sided defect transfer.
- **v1.6.0:** strict-rattler product-germ/local-KKT no-go; exact planar strict-gammoid
  completion of the Schur response; response-corrected collar capacity Phi; minimal
  kernel-map certificate; continuum source Hall and cross-matching with global plateau
  slack; exact inner-parallel capacity; correction of zero-slack and per-cell-Voronoi
  overclaims.
- **v1.7.0:** exact genuine-hull capacity slack $`\widehat p_H`$; self-container and
  boundary-reserve theorems; maximal triangle-free same-hull extension and residual
  exchange-only capacity $`\tau`$; universal fixed-container endpoint matching and
  exact Hall slack; source-capacity plateau exchange flag; same-cardinality
  rattler-preserving saturation; bounded-displacement capacity shadow with
  Hausdorff/perimeter control; finite-chord stress identity; tree-circuit
  sequentialization and exact planar cycle budget; straight-root-path criterion for
  codimension-one affine triangle walls; exact Oler-capacity split; and audited
  external leads from generation and saturation theory.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

`erdos_problem_99_1.7.0.md` supersedes v1.6.0 as the sole canonical theorem-state
file for subsequent runs.


# 135. Exact source-Hall profile of the capacity exchange flag

This continuation records one further exact consequence of Section 124.  It does not
close Target A, but it couples the exchange flag to the genuine fixed source A rather
than only to the extension B.

Retain the notation of Section 124:

```math
A\subseteq B\subseteq H,
\qquad |A|=N,
\qquad |B|=q=N+k,
\qquad M=\alpha_1(H)=q+\tau,
```

and let $`X`$ be a capacity endpoint, $`|X|=M`$.  For a maximum matchable basis
$`\mathcal B\subseteq X`$, let $`E_0=X\setminus\mathcal B`$, and for
$`E\subseteq E_0`$ use

```math
U_E=\bigcup_{e\in E}C_e,
\qquad
W_E=N_B(U_E),
\qquad
P_E=(B\setminus W_E)\cup U_E.
\tag{135.1}
```

Theorem 124.1 gives $`|P_E|=q+|E|`$ and that $`P_E`$ is a unit-separated
global optimum in H.

> **Theorem 135.1 (source-Hall-tight exchange flag).** For every
> $`E\subseteq E_0`$,
> ```math
> \boxed{N_A(P_E)=A,}
> \tag{135.2}
> ```
> and consequently
> ```math
> \boxed{
> |P_E|-|N_A(P_E)|=k+|E|.
> }
> \tag{135.3}
> ```

### Proof

The inclusion $`N_A(P_E)\subseteq A`$ is tautological.  Conversely, fix $`a\in A`$.
Since $`A\subseteq B`$, either $`a\notin W_E`$ or $`a\in W_E`$.

If $`a\notin W_E`$, then $`a\in B\setminus W_E\subseteq P_E`$, so the coincident
pair $`a,a`$ is a strict conflict in the replacement graph and
$`a\in N_A(P_E)`$.  If $`a\in W_E=N_B(U_E)`$, then by definition there is
$`u\in U_E\subseteq P_E`$ with $`|a-u|<1`$, again giving
$`a\in N_A(P_E)`$.  Thus $`N_A(P_E)=A`$.  Now use
$`|P_E|=q+|E|=N+k+|E|`$.  $`\square`$

At the terminal flag member $`E=E_0`$, $`|E_0|=\tau`$ and

```math
|P_{E_0}|=q+\tau=M=N+\widehat p_H,
\qquad
|P_{E_0}|-|N_A(P_{E_0})|=\widehat p_H.
\tag{135.4}
```

Thus the terminal exchange endpoint attains the exact maximum source-Hall deficiency
from Theorem 119.2.  The adjacent flag spends that source capacity one integer at a
time:

```math
\bigl(|P_i|-|N_A(P_i)|\bigr)
 -
\bigl(|P_{i-1}|-|N_A(P_{i-1})|\bigr)=1.
\tag{135.5}
```

There is an exact two-sided slack conservation law.  Applying Theorem 122.2 to the
unit-separated set $`P_E\subset H`$ and the same capacity endpoint X gives

```math
\max_{Q\subset H}\bigl(|Q|-|N_{P_E}(Q)|\bigr)
 =M-|P_E|=\tau-|E|.
\tag{135.6}
```

Combining (135.3) and (135.6),

```math
\boxed{
\bigl(|P_E|-|N_A(P_E)|\bigr)
 +
 \max_Q\bigl(|Q|-|N_{P_E}(Q)|\bigr)
 =k+\tau=\widehat p_H.
}
\tag{135.7}
```

If $`k+|E|\ge1`$, the self-container theorem also supplies the exact reserve

```math
\boxed{|P_E\cap\partial H|\ge k+|E|+1.}
\tag{135.8}
```

This reserve concerns the complete exchanged configuration $`P_E`$; it does not imply
that $`U_E`$, the nonbasis elements, or any first-triangle support meets
$`\partial H`$.

## 135.1 Exact limitation for Target A

Theorem 135.1 rules out a tempting but invalid use of the exchange flag.  The flag
does not itself produce—and, for $`Q\subseteq H`$, cannot produce—the proposed source
contradiction

```math
|Q|-|N_A(Q)|\ge\widehat p_H+1,
```

because its terminal member reaches exactly $`\widehat p_H`$ and Theorem 119.2 forbids
any larger deficiency for a unit-separated $`Q\subset H`$.  Likewise, the intermediate
members spend the fixed source slack while leaving exactly the complementary capacity
slack in (135.7).  A closure must therefore add information from the independent
smaller optimum, the triangle-free condition at a first exchange transition, or an
exact source-to-Schur transport.  In the source-replacement language, the missing
information has to be boundary/diameter control, not a larger same-hull Hall
deficiency.  This lemma supplies none of those inputs.

The following regressions remain active after this result:

1. $`\tau`$ and $`\widehat p_H`$ need not be zero.
2. $`P_E`$ need not contain A and need not be triangle-free.
3. The boundary reserve (135.8) is a reserve for $`P_E`$, not for $`U_E`$.
4. No old Target A scaffold may be transferred from A or B to $`P_E`$ without a
   rebuild.
5. The exact source-Hall profile gives no rank saving for the Schur response.

Accordingly, the authoritative endpoint remains

```math
\boxed{\dim\ker S\ge\Delta_\Lambda-d_{\rm int}},
```

or equivalently

```math
\boxed{\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.}
```

No Level I proof or certified infinite counterexample has been obtained.


# 136. Two exact first-transition and finite-strain reductions

This section adds two finite statements aimed at the remaining Target A routes.  The
first is a sufficient perturbation criterion for the first triangle-producing member
of the source-capacity flag.  The second is an explicit finite model of gap
concentration.  Neither statement supplies the missing Schur nullity.

## 136.1 A simultaneous triangle-breaking cone criterion

Let

```math
T=P_{j-1},
\qquad P=P_j
```

be the first adjacent member of the exchange flag for which a unit equilateral
triangle occurs.  Thus $`T`$ is triangle-free, $`P`$ is a global optimum of diameter
$`D`$, and

```math
P=(T\setminus\Delta B_j)\cup\Delta X_j.
```

Put

```math
U_\triangle
=\{x\in\Delta X_j:x\text{ belongs to a unit equilateral triangle of }P\}.
```

For $`x\in U_\triangle`$, define the finite vector set

```math
\mathcal V_P(x)
:=
\{x-y:y\in P,\ |x-y|=1\}
\cup
\{y-x:y\in P,\ |x-y|=D\}.
\tag{136.1}
```

The first set records directions in which a displacement of $`x`$ increases every
active unit separation.  The second set has the reversed sign, so a positive scalar
product decreases every active diameter separation.

> **Theorem 136.1 (simultaneous first-transition perturbation).**
> Suppose that for every $`x\in U_\triangle`$ there is a vector $`u_x\in\mathbb R^2`$
> such that
> ```math
> v\cdot u_x>0
> \qquad(v\in\mathcal V_P(x)).
> \tag{136.2}
> ```
> Then $`P`$ has a triangle-free global optimum of the same cardinality and diameter
> $`D`$.  More precisely, for all sufficiently small positive $`\epsilon`$, moving
> each $`x\in U_\triangle`$ to $`x+\epsilon u_x`$ and leaving all other points fixed
> gives a unit-separated set of diameter at most $`D`$ with no unit equilateral
> triangle.

### Proof

Every triangle in $`P`$ contains a point of $`\Delta X_j`$, because the points of
$`T`$ that remain in $`P`$ form a subset of the triangle-free set $`T`$.  Hence every
triangle in $`P`$ contains a point of $`U_\triangle`$.

For a unit edge $`xy`$ with $`x\in U_\triangle`$ and $`y\notin U_\triangle`$, (136.2)
gives
```math
(x-y)\cdot u_x>0.
```
If both endpoints lie in $`U_\triangle`$, then
```math
(x-y)\cdot(u_x-u_y)
=(x-y)\cdot u_x+(y-x)\cdot u_y>0.
\tag{136.3}
```
Thus every unit edge incident with a moved point becomes strictly longer under the
displacement.  Unit edges with neither endpoint moved do not become shorter.  Since
every edge of every old unit triangle is incident with a moved point, all old unit
triangles are destroyed.

For a diameter edge $`xy`$ with $`x\in U_\triangle`$ and $`y\notin U_\triangle`$,
(136.2) gives
```math
(x-y)\cdot u_x<0.
```
If both endpoints move, then
```math
(x-y)\cdot(u_x-u_y)
=(x-y)\cdot u_x-(x-y)\cdot u_y<0,
\tag{136.4}
```
because (136.2) at $`y`$ gives $`(x-y)\cdot u_y>0`$.  Therefore every diameter
edge incident with a moved point becomes strictly shorter, and every diameter edge
with neither endpoint moved stays unchanged.

There are finitely many pairs.  Every nonactive pair has distance strictly between
$`1`$ and $`D`$, while every active pair has the strict first-order sign just proved
unless it is unchanged.  Consequently a sufficiently small positive $`\epsilon`$
preserves all lower constraints and does not increase any upper constraint.  The
resulting set is unit-separated and has diameter at most $`D`$.  It has no unit
equilateral triangle: any such triangle would have to be a triangle of $`P`$ for
small enough $`\epsilon`$, but every triangle of $`P`$ had an incident unit edge
strictly increased.

Since $`P=P_j`$ is a global optimum at this cardinality, a unit-separated set of
smaller diameter would contradict the definition of $`D(q+j)=D`$.  Hence the
perturbed set has diameter exactly $`D`$ and is a global optimum.  $`\square`$

The criterion has an exact local alternative.  For a finite nonzero vector set
$`V\subset\mathbb R^2`$, either there is a $`u`$ with $`v\cdot u>0`$ for every
$`v\in V`$, or there are coefficients $`\lambda_v\ge0`$, not all zero, with
```math
\sum_{v\in V}\lambda_vv=0.
\tag{136.5}
```
Indeed, the first case holds precisely when $`0\notin\operatorname{conv}V`$, and
then strict separation of the compact convex hull from $`0`$ supplies $`u`$.  If
$`0\in\operatorname{conv}V`$, its convex-combination coefficients give (136.5).

Therefore, if the independent perturbation in Theorem 136.1 is unavailable, some
$`x\in U_\triangle`$ has a nonnegative equilibrium among its unit-contact vectors
and reversed diameter vectors.  In the special case that $`x`$ has no diameter
partner, the two contact vectors supplied by a triangle make an angle of $`60^\circ`$
and cannot themselves positively balance.  Thus (136.5) then forces at least one
additional unit contact:

```math
\boxed{
x\text{ is triangle-supported and non-diametral, but the cone test fails}
\Longrightarrow \deg_{E_1(P)}(x)\ge3.
}
\tag{136.6}
```

This is only a reduction of the first-transition branch.  The remaining three-contact
and diameter-supported cases are not excluded by the source-capacity flag.

## 136.2 An explicit finite strain-transfer theorem

Let $`e_1,e_2`$ be unit vectors with $`e_1\cdot e_2=1/2`$, and let
```math
\Lambda_0=\mathbb Ze_1+\mathbb Ze_2.
```
For $`L\ge2`$, $`\epsilon>0`$, and $`s=1+\epsilon`$, define
```math
P_{L,\epsilon}
=s\{ie_1+je_2:0\le i,j\le L-1\},
\qquad
K_{L,\epsilon}=\operatorname{conv}P_{L,\epsilon}.
\tag{136.7}
```

> **Theorem 136.2 (finite homothetic gap concentration).**
> The set $`P_{L,\epsilon}`$ is triangle-free, has $`L^2`$ points, and
> ```math
> \operatorname{diam}P_{L,\epsilon}
> =\operatorname{diam}K_{L,\epsilon}
> =s\sqrt3\,(L-1).
> \tag{136.8}
> ```
> If
> ```math
> \epsilon\ge\frac1{L-1},
> \tag{136.9}
> ```
> then $`K_{L,\epsilon}`$ contains a unit-separated set of $`L^2+1`$ points,
> namely
> ```math
> Q_L
> =\{ie_1+je_2:0\le i,j\le L-1\}\cup\{Le_1\},
> \tag{136.10}
> ```
> and $`\operatorname{diam}Q_L\le\operatorname{diam}P_{L,\epsilon}`$.

### Proof

For a nonzero integer pair $`(i,j)`$,
```math
|ie_1+je_2|^2=i^2+ij+j^2\ge1.
```
Thus distinct points of $`P_{L,\epsilon}`$ have distance at least $`s>1`$, so
the set has no unit edges and is triangle-free.  On the coordinate parallelogram
```math
K_{L,\epsilon}
=\{ae_1+be_2:0\le a,b\le s(L-1)\},
```
the squared norm $`a^2+b^2+ab`$ is maximized at opposite vertices.  This gives
(136.8).

The condition (136.9) is equivalent to
```math
L\le s(L-1).
```
Consequently $`Le_1\in K_{L,\epsilon}`$, and the other $`L^2`$ points in (136.10)
also lie in that parallelogram.  All points of $`Q_L`$ belong to the unit triangular
lattice $`\Lambda_0`$, so their mutual distances are at least one.  Since
$`Q_L\subseteq K_{L,\epsilon}`$, its diameter is at most the diameter in (136.8).
$`\square`$

For the strained-patch scale $`\epsilon=\alpha/L`$, condition (136.9) requires
```math
\alpha\ge\frac{L}{L-1}.
\tag{136.11}
```
If $`0<\alpha<1`$, then $`s(L-1)<L`$, and the coordinate parallelogram contains
exactly the original $`L^2`$ lattice sites with integer coordinates
$`0\le i,j\le L-1`$.  Thus the straight homothetic compression followed by a
lattice insertion cannot produce the extra site in this regime, despite the patch
having $`\Theta(L^2)`$ total nearest-neighbor clearance of order $`\Theta(L)`$.
This is a precise finite boundary obstruction, not a claim that no arbitrary
nonlattice rearrangement exists.

## 136.3 Target A audit after the two reductions

Theorem 136.1 removes the first-transition configurations satisfying the explicit
strict cone condition, but it does not control a three-contact equilibrium or a
diameter-supported triangle vertex.  Theorem 136.2 supplies a finite gap-transfer
model only when a full homothetic patch has accumulated one lattice spacing of
longitudinal slack and has no incompatible fixed environment.  The actual source
scaffold supplies neither condition in the surviving general branch.

In particular, the exact unresolved implication remains
```math
\boxed{
\dim\ker S=|C^\partial|-\operatorname{rank}S
\ \ge\ \Delta_\Lambda-d_{\rm int},
}
```
or, on the source side, a boundary-certified add-one replacement (or an equivalent
direct source-to-Schur transport).  A same-hull $`Q`$ with deficiency
$`\widehat p_H+1`$ is ruled out by (119.8).
The strained-monomer, three-contact/diameter-support, overlapping-circuit, and
annular-routing regressions all remain live.  No Level I proof or certified infinite
counterexample has been obtained.



# 136. Finite transfer of a honeycomb gap witness

The Kuperberg--Kuperberg--Kuperberg theorem on a honeycomb packing with a linear gap
defect is a finite-rearrangement theorem after rescaling the circle centers to
minimum separation one.  In particular, for every gap width $`d>0`$ and direction
there are finite sets $`S_d,T_d`$ of centers such that

```math
|T_d|=|S_d|+1,
\qquad
(\mathcal H_d\setminus S_d)\cup T_d
\text{ is unit-separated},
\tag{136.1}
```

where $`\mathcal H_d`$ is the corresponding infinite honeycomb packing with a
linear gap.  The finite witness sets $`S_d,T_d`$ are implicit in their finite block
rearrangement; no uniform bound on their diameter as $`d\downarrow0`$ is asserted.

> **Theorem 136.1 (protected finite-container transfer).** Let $`L`$ be an open
> bounded set with $`\operatorname{diam}L<D`$, and let $`F\subset L`$ be a finite
> unit-separated set.  Suppose that, for some $`d>0`$, there are finite witness sets
> $`S_d,T_d`$ satisfying (136.1), and some set $`F_{\rm far}`$, such that:
>
> 1. $`S_d\subseteq F\subseteq \mathcal H_d\cup F_{\rm far}`$;
> 2. $`F\setminus S_d`$ contains no points outside $`\mathcal H_d`$ that are within
>    unit distance of $`T_d`$;
> 3. $`T_d\subset L`$.
>
> Then
> ```math
> (F\setminus S_d)\cup T_d
> ```
> is unit-separated and has $`|F|+1`$ points in $`L`$.

### Proof

The set $`F\setminus S_d`$ is unit-separated.  Its points lying in
$`\mathcal H_d\setminus S_d`$ are at distance at least one from every point of
$`T_d`$ by (136.1), and hypothesis 2 gives the same conclusion for the remaining
points.  Thus the displayed replacement is unit-separated.  Its cardinality is
```math
|F|-|S_d|+|T_d|=|F|+1.
```
Hypothesis 3 and $`F\subset L`$ put every point in $`L`$.  $`\square`$

Consequently, if $`F`$ has the cardinality $`N`$ of a diameter-minimizing
configuration with $`D(N)=D`$, Theorem 136.1 contradicts the definition of $`D(N)`$:
the replacement has $`N+1`$ points and diameter strictly below $`D`$.

## 136.1 Exact scope and remaining finite gap

This is a genuine finite-container transfer, but it does not yet supply the
finite monomer gap-concentration theorem required by Target A.  The scaffold's
coherent monomer phase is only known to have bounded-displacement triangular-lattice
combinatorics.  The current theorem does not prove that it contains an exact
protected copy of $`\mathcal H_d`$, nor that all non-modeled source points are at
least one from $`T_d`$.

Moreover, the strained-monomer regression can have gap width $`d=d_D\downarrow0`$.
The external theorem and its finite block construction do not provide a quantitative
bound showing that the witness diameter is $`o(D)`$, or even $`O(D)`$, in that regime.
Thus the transfer eliminates the following conditional branch:

```math
\boxed{
\text{a fixed-width, protected honeycomb gap inside the open target hull is
impossible.}
}
\tag{136.2}
```

It leaves the exact branch

```math
\boxed{
\text{vanishing-width or non-protected coherent monomer strain.}
}
\tag{136.3}
```

No Schur nullity saving follows from (136.1)--(136.3), and no source Hall deficiency
above $`\widehat p_H`$ follows.  The Target A endpoint therefore remains

```math
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
```


# 137. Exact one-point test at a first tree-circuit triangle

The tree-circuit sequentialization reduces a tree transition to one-point insertions
and deletions.  The following lemma gives an exact test for the insertion point when
the preceding configuration is triangle-free.  It separates a removable first
triangle from a locally isolated contact cage; it does not use, and does not imply,
global optimality of an arbitrary preceding configuration.

Let $`P`$ be a finite triangle-free unit-separated set, let $`x\notin P`$, and assume
that $`P\cup\{x\}`$ is unit-separated.  Put

```math
C_x=\{p\in P:|p-x|=1\},
\qquad
E_x=\{\{p,q\}\subset C_x:|p-q|=1\}.
\tag{137.1}
```

The edges in $`E_x`$ are exactly the unit triangles created by inserting $`x`$.

> **Theorem 137.1 (semicircle/cage dichotomy).** Suppose that every distance from
> $`x`$ to $`P`$ is strictly less than a prescribed diameter $`D`$.  Then exactly
> the following alternatives apply to a one-point motion of $`x`$:
>
> 1. If the direction set
>    
>    ```math
>    \{p-x:p\in C_x\}\subset\mathbb S^1
>    ```

>    is contained in a closed semicircle, there are a vector $`\xi\ne0`$ and
>    $`\epsilon>0`$ such that, for every $`0<t<\epsilon`$,
>    
>    ```math
>    (P\cup\{x+t\xi\})
>    ```

>    is unit-separated, has diameter at most $`D`$, and is triangle-free.
>
> 2. If the direction set is not contained in a closed semicircle, then $`x`$ is
>    locally isolated in the one-point feasible slice: there is $`\epsilon>0`$ such
>    that the only $`y`$ with $`|y-x|<\epsilon`$ and $`|y-p|\ge1`$ for every
>    $`p\in C_x`$ is $`y=x`$.

### Proof

Write $`a_p=p-x`$, so $`|a_p|=1`$ for $`p\in C_x`$.  If the directions lie in
a closed semicircle, choose a supporting unit normal $`\xi`$ so that

```math
a_p\cdot\xi\le0\qquad(p\in C_x).
\tag{137.2}
```

For a contact $`p`$,

```math
|x+t\xi-p|^2
=1-2t\,a_p\cdot\xi+t^2|\xi|^2\ge1.
\tag{137.3}
```

If $`\{p,q\}\in E_x`$, the two direction vectors cannot both be endpoints of
the containing semicircle: those endpoints are antipodal, whereas $`|p-q|=1`$
would require their angular separation to be $`\pi/3`$.  Consequently at least one
of $`a_p\cdot\xi,a_q\cdot\xi`$ is strictly negative.  Equation (137.3) then makes
at least one of the two sides of every newly created triangle strictly longer than
one for all sufficiently small $`t>0`$.  All other pairs involving $`x`$ have
strict separation slack and remain feasible after shrinking $`\epsilon`$.  The
strict upper slack $`|x-p|<D`$ likewise preserves the diameter bound.  Since $`P`$
was triangle-free, all triangles have been removed.

If the direction set is not contained in a closed semicircle, the planar separation
criterion gives

```math
c:=\min_{|u|=1}\max_{p\in C_x}a_p\cdot u>0.
\tag{137.4}
```

For $`y=x+h`$ with $`|h|>0`$, choose $`p\in C_x`$ with
$`a_p\cdot h\ge c|h|`$.  Feasibility against that contact would require

```math
|a_p-h|^2\ge1
\quad\Longrightarrow\quad
a_p\cdot h\le\frac{|h|^2}{2},
\tag{137.5}
```

which is impossible when $`0<|h|<2c`$.  Thus $`x`$ is locally isolated. $`\square`$

## 137.1 Consequence for a tree first transition

Consider the first triangle in the one-for-one swap sequence supplied by a tree
fundamental circuit.  Before that insertion the current set is triangle-free, so
the new point $`x`$ is the only possible vertex of a newly created triangle.  If
$`x`$ is non-diametral, Theorem 137.1 gives the exact alternative:

```math
\boxed{
\text{closed contact semicircle}\ \Longrightarrow\ \text{triangle-free global optimum
after a small perturbation};
}
\tag{137.6}
```

whereas a first triangle that cannot be removed by a one-point perturbation must
come from a contact direction set that positively surrounds $`x`$, hence from a
locally isolated exact-contact cage.  Unit separation gives at most six such
contacts, and at least three are needed in the surrounding case.  The latter
statement follows directly from the angular gaps: two directions always lie in a
closed semicircle.

This is a reduction of the non-diametral tree branch, not the required Target A
theorem.  It leaves three cases untouched:

1. the locally isolated exact-contact cage;
2. a first-triangle insertion at a diameter endpoint, where upper diameter
   constraints must be included in the displacement cone; and
3. cyclic or multi-point transition supports, where the first triangle can contain
   more than one newly inserted point.

## 137.2 Sharp local cage witness

The cage alternative is nonempty even with a triangle-free preceding set.  Take

```math
x=(0,0),
\quad
p_1=(1,0),
\quad
p_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\quad
p_3=\left(-\frac{\sqrt3}{2},-\frac12\right).
\tag{137.7}
```

The set $`P=\{p_1,p_2,p_3\}`$ is unit-separated and triangle-free: $`|p_1-p_2|=1`$,
while the other two pairwise distances are $`2\sin(5\pi/12)>1`$.  Inserting $`x`$
creates the unit triangle $`xp_1p_2`$.  The three contact directions satisfy

```math
(p_1-x)+(p_2-x)+\sqrt3\,(p_3-x)=0,
\tag{137.8}
```

with all coefficients positive.  Hence they are not contained in a closed
semicircle, and Theorem 137.1 makes $`x`$ locally isolated when the other points
are held fixed.  All distances from $`x`$ are one, while the diameter of $`P`$ is
$`2\sin(5\pi/12)>1`$, so this witness is already in the non-diametral regime.

The witness is only local: it is not a global diameter certificate and supplies no
Schur nullity.  Therefore the exact remaining Target A implication is still

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
```

and the source-side alternative must be boundary/diameter-certified; a Hall excess
of $`\widehat p_H+1`$ inside H is impossible by (119.8).  In particular, Theorem
137.1 does not justify promoting the tree-circuit branch to either conclusion.

## 136.2 Compatible finite witnesses and exact source slack

The same transfer works for several separated finite witnesses and gives the exact
source-Hall threshold rather than only a one-point contradiction.  Let
$`(S_i,T_i)_{i=1}^k`$ be finite Kuperberg witnesses for one honeycomb gap packing,
with the $`S_i`$ and $`T_i`$ pairwise disjoint.  Let $`F`$ be a finite unit-separated
set containing $`\bigcup_iS_i`$, and assume

```math
\bigcup_iT_i\subset L,
\qquad
\left(F\setminus\bigcup_iS_i\right)\cup\bigcup_iT_i
\text{ is unit-separated}.
\tag{136.4}
```

Then, directly,

```math
\left|
\left(F\setminus\bigcup_iS_i\right)\cup\bigcup_iT_i
\right|
=|F|+k.
\tag{136.5}
```

If $`F=A`$ is the genuine source in its hull $`H`$, with
$`T_i\subset H`$, the union $`Q=\bigcup_iT_i`$ also satisfies

```math
N_A(Q)\subseteq\bigcup_iS_i,
\qquad
|Q|-|N_A(Q)|\ge k.
\tag{136.6}
```

Indeed, the displayed replacement in (136.4) is unit-separated by hypothesis, and
pairwise disjointness gives the cardinality identity (136.5).  If
$`a\in A\setminus\bigcup_iS_i`$ and $`t\in Q`$, unit separation of the replacement
gives $`|a-t|\ge1`$, so $`N_A(Q)\subseteq\bigcup_iS_i`$.  Since
$`\sum_i(|T_i|-|S_i|)=k`$, (136.6) follows.  Applying (119.8) proves (136.7).

Therefore the exact fixed-source bound forces

```math
\boxed{k\le\widehat p_H.}
\tag{136.7}
```

This is the finite multi-witness form of the gap-concentration route.  It is useful
only after compatibility with the actual source points has been verified; separate
infinite witnesses need not be mutually compatible after insertion into a finite
configuration.  In particular, positive distributed clearance in the strained
monomer regression still supplies neither the witness sets nor their compatibility.


# 137. Finite concentration of homothetic monomer strain

Section 136 transfers a protected honeycomb gap of fixed positive width.  The
homothetic strained-monomer regression has no such gap at the pointwise scale: its
nearest-neighbor excess can be only $`\alpha/L`$.  For a free rhombic patch, however,
the excess from $`L`$ rows can be concentrated into one fixed-width internal gap
without leaving the original finite hull.

Normalize the triangular lattice as

```math
\Lambda=\mathbb Z e_1+\mathbb Z e_2,
\qquad
e_1=(1,0),
\qquad
e_2=\left(\frac12,\frac{\sqrt3}{2}\right),
\tag{137.1}
```

and put

```math
h=\frac{\sqrt3}{2},
\qquad
n=(0,1).
\tag{137.2}
```

For an integer $`L\ge1`$, let

```math
R_L=\{ie_1+je_2:-L\le i,j\le L\}.
\tag{137.3}
```

> **Theorem 137.1 (finite homothetic-strain concentration).**  Fix
> $`\eta>0`$.  There is $`L_0(\eta)`$ with the following property.  If
> $`L\ge L_0(\eta)`$, $`\varepsilon>0`$, and
> ```math
> L\varepsilon\ge\eta,
> \tag{137.4}
> ```
> then, for
> ```math
> P_L=(1+\varepsilon)R_L,
> \qquad
> H_L=\operatorname{conv}P_L,
> \tag{137.5}
> ```
> there is a unit-separated set $`P_L^+\subset H_L`$ such that
> ```math
> \boxed{|P_L^+|=|P_L|+1.}
> \tag{137.6}
> ```
> Thus a homothetically strained triangular patch whose accumulated strain
> $`L\varepsilon`$ stays bounded away from zero is not completely saturated even
> relative to its own finite convex hull.

### Proof

Put

```math
a=\frac{h\eta}{2}.
\tag{137.7}
```

Inside $`H_L`$, replace the homothetic patch by the same number of points

```math
\begin{aligned}
Q_L^-&=\{ie_1+je_2-an:-L\le i\le L,\ -L\le j\le-1\},\\
Q_L^+&=\{ie_1+je_2+an:-L\le i\le L,\ 0\le j\le L\},\\
Q_L&=Q_L^-\cup Q_L^+.
\end{aligned}
\tag{137.8}
```

Each half is a translate of a triangular-lattice half-patch.  For a point in the
upper half and one in the lower half, the vertical component of their difference is
positive before the translations and is increased by $`2a`$.  The horizontal
component is unchanged.  Hence no cross-half distance decreases, and

```math
Q_L\text{ is unit-separated},
\qquad
|Q_L|=|P_L|=(2L+1)^2.
\tag{137.9}
```

To check the container exactly, use

```math
n=-\frac1{2h}e_1+\frac1h e_2.
\tag{137.10}
```

Thus adding $`an`$ changes the two lattice coefficients by

```math
\left(-\frac{a}{2h},\frac ah\right)
=\left(-\frac\eta4,\frac\eta2\right),
\tag{137.11}
```

and subtracting $`an`$ changes them by the opposite vector.  Since

```math
H_L=(1+\varepsilon)\bigl([-L,L]e_1+[-L,L]e_2\bigr)
\tag{137.12}
```

and its coefficient margin beyond $`[-L,L]^2`$ is
$`L\varepsilon\ge\eta`$, (137.11) proves

```math
Q_L\subset H_L.
\tag{137.13}
```

Let

```math
\mathcal H_a=
\{ie_1+je_2-an:j\le-1\}
\cup
\{ie_1+je_2+an:j\ge0\}.
\tag{137.14}
```

This is, up to one global translation, the honeycomb packing with a linear gap of
width $`2a=h\eta>0`$.  After rescaling their circle-center normalization, the
Kuperberg--Kuperberg--Kuperberg theorem quoted in Section 136 supplies finite sets
$`S\subset\mathcal H_a`$ and $`T\subset\mathbb R^2`$ such that

```math
|T|=|S|+1,
\qquad
(\mathcal H_a\setminus S)\cup T
\text{ is unit-separated}.
\tag{137.15}
```

The witness is finite.  Therefore, for all sufficiently large $`L`$,

```math
S\subset Q_L,
\qquad
T\subset H_L.
\tag{137.16}
```

The second inclusion holds because $`T`$ is fixed while the centered parallelograms
$`H_L`$ have inradius tending to infinity.  Now set

```math
P_L^+=(Q_L\setminus S)\cup T.
\tag{137.17}
```

It is a subset of the unit-separated set in (137.15), lies in $`H_L`$, and has

```math
|P_L^+|=|Q_L|-|S|+|T|=|P_L|+1.
```

This proves the theorem. $`\square`$

The theorem applies in particular to the exact strain scale

```math
\varepsilon_L=\frac\alpha L,
\qquad \alpha>0,
\tag{137.18}
```

that occurs in Regression 105.1.  Although every individual nearest-neighbor excess
tends to zero, the two half-patches in (137.8) expose a gap of the fixed width
$`h\alpha`$ (or any smaller fixed width), after which one finite Kuperberg witness
fits for all sufficiently large $`L`$.

There is also an immediate protected-subcontainer version.  If a finite packing
$`F\subset H`$ contains an isometric copy of $`P_L`$, its rhombic hull is contained
in $`H`$, and

```math
\operatorname{dist}
\bigl(F\setminus P_L,\operatorname{conv}P_L\bigr)\ge1,
\tag{137.19}
```

then the replacement (137.17) adds one point to $`F`$ inside $`H`$.  Condition
(137.19) is much stronger than the monomer-chamber information in the actual
scaffold.

## 137.1 Regression audit and exact limitation

Theorem 137.1 eliminates the **free homothetic rhombus** version of the
strained-monomer regression.  It does not eliminate the canonical Target A monomer
branch for the following exact reasons.

1. A monomer phase records strict-conflict combinatorics, not an exact homothetic
   copy of $`(1+\varepsilon)\Lambda`$.
2. The construction moves the whole rhombic patch, including its boundary rows.
   An embedded coherent domain may be locked to exterior source or scaffold points,
   and (137.19) is not available.
3. If $`L\varepsilon_L\to0`$, the proof creates no fixed positive gap and gives no
   quantitative control on a vanishing-gap Kuperberg witness.
4. One compatible add-one witness does not by itself provide a
   boundary/diameter-certified replacement, nor does it yield $`s`$ independent
   Schur null directions.

Thus the remaining finite gap theorem is now more precise: one must concentrate
strain while preserving the actual exterior boundary constraints of a globally
derived monomer domain, or else extract enough mutually compatible witnesses to
exceed the exact source slack.


# 138. Simultaneous triangle breaking or an infinitesimally locked triangle

The first triangle-producing plateau transition can be sharpened without assuming
that its circuit is a tree.  The relevant alternative is an exact fixed-container
statement.

Let $`H`$ be a convex polygon with nonempty interior and let

```math
P=\{p_1,\ldots,p_r\}\subset H
\tag{138.1}
```

be unit-separated.  Let $`E_1(P)`$ be its unit-contact edges and let
$`\mathcal T(P)`$ be its unit equilateral triangles.  Write the facet inequalities
of $`H`$ as

```math
n_f\cdot z\le c_f.
\tag{138.2}
```

For a velocity $`v=(v_1,\ldots,v_r)`$, put

```math
a_{ij}(v)=(p_i-p_j)\cdot(v_i-v_j).
\tag{138.3}
```

Define the fixed-container expansive cone

```math
\mathcal C_H(P)=\left\{
v:
\begin{array}{ll}
a_{ij}(v)\ge0& (ij\in E_1(P)),\\
n_f\cdot v_i\le0& (n_f\cdot p_i=c_f)
\end{array}
\right\}.
\tag{138.4}
```

For $`T\in\mathcal T(P)`$, define

```math
\ell_T(v)=\sum_{ij\in E(T)}a_{ij}(v).
\tag{138.5}
```

Every term in (138.5) is nonnegative on $`\mathcal C_H(P)`$.

> **Theorem 138.1 (locked-triangle alternative).**  Suppose
> $`\mathcal T(P)\ne\varnothing`$.  Exactly one of the following holds.
>
> 1. There is $`v\in\mathcal C_H(P)`$ such that
>    
>    ```math
>    \ell_T(v)>0
>    \qquad(T\in\mathcal T(P)).
>    \tag{138.6}
>    ```

>    For every sufficiently small $`t>0`$, the linearly perturbed configuration
>    $`P_t=\{p_i+tv_i\}`$ is unit-separated, lies in $`H`$, and is triangle-free.
> 2. There is a triangle $`T_\ast\in\mathcal T(P)`$ such that
>    
>    ```math
>    \boxed{
>    a_{ij}(v)=0
>    \quad
>    (ij\in E(T_\ast),\ v\in\mathcal C_H(P)).
>    }
>    \tag{138.7}
>    ```

>    Thus all three sides of $`T_\ast`$ are fixed to first order by every
>    fixed-container infinitesimally feasible motion.

### Proof

If alternative 2 fails, then for every $`T\in\mathcal T(P)`$ there is
$`v^T\in\mathcal C_H(P)`$ with $`\ell_T(v^T)>0`$.  The set
$`\mathcal C_H(P)`$ is a convex cone, so

```math
v=\sum_{T\in\mathcal T(P)}v^T
\tag{138.8}
```

belongs to it.  Since every $`\ell_{T'}(v^T)\ge0`$,

```math
\ell_{T'}(v)
\ge
\ell_{T'}(v^{T'})>0
\qquad(T'\in\mathcal T(P)),
\tag{138.9}
```

which is alternative 1.

Conversely, if alternative 1 fails, the same summation argument shows that some
$`T_\ast`$ must satisfy

```math
\ell_{T_\ast}(v)=0
\qquad(v\in\mathcal C_H(P)).
\tag{138.10}
```

All three summands are nonnegative on the cone, so each is zero.  This gives
(138.7) and also proves mutual exclusivity.

It remains to justify the finite perturbation in alternative 1.  For a unit edge,

```math
\begin{aligned}
&|p_i+tv_i-p_j-tv_j|^2\\
&\qquad=
1+2t a_{ij}(v)+t^2|v_i-v_j|^2
\ge1.
\end{aligned}
\tag{138.11}
```

Every noncontact pair has a positive finite slack, so it remains separated for all
sufficiently small $`t`$.  The active facet inequalities in (138.4), together with
the positive slack at inactive facets, keep every point in $`H`$.  For each original
unit triangle, (138.6) makes at least one side strictly longer than one.  Finally, a
triple which was not originally a unit triangle had at least one side strictly
longer than one, and the finitely many such strict inequalities persist for small
$`t`$.  Hence no new unit triangle appears. $`\square`$

Apply this theorem to the first triangle-producing member $`P_j`$ of the exact flag
in Section 124.  Since

```math
|P_j|=q+j,
\qquad
D(q+j)=D,
\qquad
P_j\subset H,
\tag{138.12}
```

alternative 1 produces a triangle-free **global optimum at the same new
cardinality**.  In alternative 2, every triangle of $`P_j`$, and hence the locked
triangle $`T_\ast`$, contains a point of $`\Delta X_j`$, because
$`P_{j-1}`$ was triangle-free.

> **Corollary 138.2 (sharpened first-transition alternative).**  At the first bad
> source-capacity transition, either a fixed-container perturbation gives a
> triangle-free global optimum at cardinality $`q+j`$, or the transition creates a
> unit triangle containing a newly inserted point whose three sides are universally
> first-order locked in the cone $`\mathcal C_H(P_j)`$.

This conclusion applies equally to tree and cyclic circuits.  It is stronger than
the statement that every new triangle merely meets $`\Delta X_j`$, but it supplies
one locked triangle, not $`s`$ independent failures of the Schur linkage.


# 139. Interior cage geometry for a bad tree swap

The locked branch of Corollary 138.2 has a sharp one-vertex geometric shadow.  Let
$`P^-\subset H`$ be triangle-free and unit-separated.  Suppose a tree-circuit leaf
swap removes $`b\in P^-`$ and inserts $`x`$, where

```math
|x-b|=r<1,
\qquad
|x-u|\ge1
\quad(u\in P^-\setminus\{b\}).
\tag{139.1}
```

Let

```math
U_x=\{u\in P^-\setminus\{b\}:|x-u|=1\}.
\tag{139.2}
```

If $`x\in\operatorname{int}H`$ and the directions $`u-x`$, $`u\in U_x`$, lie in
an open semicircle, then there is a vector $`v`$ for which

```math
(x-u)\cdot v>0
\qquad(u\in U_x).
\tag{139.3}
```

Moving only $`x`$ a sufficiently small positive distance in direction $`v`$ breaks
all its unit contacts and hence every triangle created by that swap.  Therefore an
interior one-point obstruction requires the contact directions not to lie in an
open semicircle; equivalently their largest circular gap is at most $`\pi`$.

The removed blocker forces a gap in the opposite direction.  If $`w=(b-x)/r`$ and
$`u\in U_x`$, then

```math
1\le|b-u|^2
=r^2+1-2r\,w\cdot(u-x),
\tag{139.4}
```

so

```math
w\cdot(u-x)\le\frac r2.
\tag{139.5}
```

Consequently the contact directions have an empty circular arc centered on $`w`$
of width

```math
\boxed{
2\arccos\frac r2>\frac{2\pi}{3}.
}
\tag{139.6}
```

Thus every interior caged leaf event has a largest angular gap in the exact range

```math
\boxed{
\frac{2\pi}{3}<\gamma\le\pi.
}
\tag{139.7}
```

If the event creates a triangle through $`x`$, two contact directions are separated
by exactly $`\pi/3`$.  These conditions are compatible; they do not yield a local
contradiction.

The boundary alternative is genuinely boundary-order.  If $`x\in\partial H`$, then
(139.1) gives $`\operatorname{dist}(b,\partial H)<1`$.  The boundary-layer estimate
(72.12), applied to any unit-separated source extension in the same diameter-$`D`$
hull, bounds the number of such blocker positions by $`12D+9`$.  This does not show
that the first bad leaf in a chosen elimination order has a deep blocker.

## 139.1 Exact two-leaf cage regression

The interior interval (139.7) is nonempty even for the smallest tree circuit.  The
following family rules out a leaf-ordering or one-point-perturbation proof based only
on tree-circuit geometry.

For

```math
\frac\pi3<\theta<\frac\pi2,
\qquad
c=\cos\theta,
\qquad
a=\frac34+\frac c2,
\tag{139.8}
```

put $`u_\phi=(\cos\phi,\sin\phi)`$,

```math
x_-=(-a,0),
\qquad
x_+=(a,0),
\qquad
b=(0,0),
\tag{139.9}
```

and define the angle sets

```math
\begin{aligned}
L_\theta&=\left\{\theta,\frac{5\pi}{6},\frac{7\pi}{6},2\pi-\theta\right\},\\
R_\theta&=\left\{\frac\pi6,\pi-\theta,\pi+\theta,\frac{11\pi}{6}\right\}.
\end{aligned}
\tag{139.10}
```

Let

```math
B=\{b\}
\cup\{x_-+u_\phi:\phi\in L_\theta\}
\cup\{x_++u_\phi:\phi\in R_\theta\},
\qquad
C=\{x_-,x_+\}.
\tag{139.11}
```

> **Proposition 139.1 (two-leaf caged circuit).**  The sets $`B`$ and $`C`$ are
> internally unit-separated, $`B`$ is triangle-free, and the strict conflict graph
> from $`C`$ to $`B`$ is the three-vertex path
> ```math
> x_- - b - x_+.
> \tag{139.12}
> ```
> Hence $`C`$ is a two-element transversal-matroid circuit whose contracted
> right shore has one degree-two blocker.  Both possible leaf swaps create a unit
> triangle, and the inserted leaf is infinitesimally pinned when the eight cage
> points are held fixed.

### Proof

Within the left cage, the consecutive angular gaps are

```math
\frac{5\pi}{6}-\theta,
\quad
\frac\pi3,
\quad
\frac{5\pi}{6}-\theta,
\quad
2\theta.
\tag{139.13}
```

All are at least $`\pi/3`$, with equality only for the middle pair.  The same holds
for the reflected right cage.  Thus the only unit edges internal to the two cages
are the pairs at angles $`5\pi/6,7\pi/6`$ and $`\pi/6,11\pi/6`$.

Every left-cage point has horizontal coordinate at most $`-a+c`$, while every
right-cage point has horizontal coordinate at least $`a-c`$.  Their cross distance
is therefore at least

```math
2(a-c)=\frac32-c>1.
\tag{139.14}
```

For either of the two left-cage points directed toward $`b`$,

```math
|b-(x_-+u_\phi)|^2=a^2-2ac+1>1,
\tag{139.15}
```

because

```math
a-2c=\frac34-\frac{3c}{2}>0.
\tag{139.16}
```

The two outward points are still farther; the right side is symmetric.  This proves
that $`B`$ is unit-separated and that its unit graph consists of two disjoint edges,
so it is triangle-free.

Now $`|x_--x_+|=2a>1`$, while

```math
|x_\pm-b|=a<1.
\tag{139.17}
```

Each $`x_\pm`$ is exactly unit distance from its own four cage points.  Its distance
to every point of the opposite cage is greater than one: the minimum horizontal
separation is

```math
2a-c=\frac32.
\tag{139.18}
```

Thus (139.12) is the complete strict conflict graph.

After swapping $`b`$ for $`x_-`$, the latter and the left-cage points at angles
$`5\pi/6,7\pi/6`$ form a unit equilateral triangle.  The symmetric statement holds
for $`x_+`$.  Finally, the largest gap among the four contact directions in either
cage is $`2\theta<\pi`$.  Their positive cone is all of $`\mathbb R^2`$, so the
polar cone of one-point noncontracting velocities is $`\{0\}`$.  Each inserted
leaf is infinitesimally pinned. $`\square`$

As $`\theta\downarrow\pi/3`$, the strict blocker length $`a`$ tends to one, the
cross-cage minimum (139.14) tends to one, and the nearest blocker-to-cage distances
in (139.15) tend to one.  Hence no uniform strict-margin charge can be extracted from
this local tree event.

This is an exact local regression, not a global minimizer or a finite-container
capacity endpoint.  It does not defeat Corollary 138.2: allowing the whole
configuration to move is strictly stronger than moving the inserted leaf while its
cage is fixed.


# 140. Post-continuation Target A status

The new results narrow two preferred attacks but do not close Target A.

1. The fixed positive-gap transfer of Section 136 now extends to the vanishing
   pointwise strain $`\varepsilon_L=\alpha/L`$ for a free homothetic rhombus.  What
   remains is the exterior-compatible concentration theorem for a globally derived
   monomer subdomain.
2. Every first triangle-producing exchange now has an exact alternative: a
   triangle-free same-cardinality global perturbation, or a newly supported unit
   triangle universally locked to first order in the fixed hull.
3. In the tree branch, a deep blocker forces the locked inserted vertex into the
   angular cage (139.7).  Proposition 139.1 shows that neither leaf ordering nor a
   one-point perturbation eliminates that cage from local circuit geometry alone.

The exact missing implication is therefore one of the following.

```math
\boxed{
\begin{array}{l}
\text{Transport the locked first-transition triangle(s) to at least }s
\text{ independent failures of the}\ C^\partial\!\to O
\text{ alternating linkage};\\[2mm]
\text{or produce an exterior-compatible add-one replacement with an explicit}\
\text{diameter-}<D\text{ certificate.}
\end{array}}
\tag{140.1}
```

Neither transport is supplied here.  In particular, one locked triangle need not
give one Schur null direction, locked triangles from different circuit orderings
need not be independent, and the free-rhombus rearrangement can violate all of the
actual boundary contacts of an embedded monomer domain.

Accordingly the authoritative endpoint remains

```math
\boxed{
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
}
\tag{140.2}
```

equivalently

```math
\boxed{
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
}
\tag{140.3}
```

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 137. First-transition incidence bound for retained strict rattlers

The source-capacity flag gives one further exact restriction on the first
triangle-producing transition.  It distinguishes a triangle supported by the
retained strict-rattler population from one supported entirely by the exchanged
backbone; the latter remains uncontrolled here.

Use the notation of Sections 124 and 135.  Thus $`B`$ is triangle-free,
$`P_i=(B\setminus W_i)\cup U_i`$, $`X`$ is the capacity endpoint, and $`j`$ is the
first index for which $`P_j`$ contains a unit equilateral triangle.  Let

```math
R\subseteq B
```

be a set of strict rattlers of $`B`$, meaning

```math
|r-b|>1\qquad(r\in R, b\in B\setminus\{r\}).
\tag{137.1}
```

Put

```math
R_j:=R\cap(B\setminus W_j),
\qquad
a_j:=|\Delta X_j|.
\tag{137.2}
```

Let $`\mathcal T_j(R)`$ be the set of unit equilateral triangles in $`P_j`$ that
contain a point of $`R_j`$.  Since $`P_{j-1}`$ is triangle-free, these are all
new triangles at this transition.

> **Theorem 137.1 (retained-rattler incidence bound).** Every triangle in
> $`\mathcal T_j(R)`$ contains exactly one point of $`R_j`$ and two points of
> $`U_j`$.  The two $`X`$-points form a unit edge of the unit-contact graph of
> $`X`$, and that edge has at least one endpoint in $`\Delta X_j`$.  Consequently
> ```math
> \boxed{
> |\mathcal T_j(R)|\le 2e_X(\Delta X_j)\le 12|\Delta X_j|,
> }
> \tag{137.3}
> ```
> where $`e_X(\Delta X_j)`$ is the number of unit edges of $`X`$ incident to
> $`\Delta X_j`$.  In addition, the number of new unit contacts between
> $`R_j`$ and $`\Delta X_j`$ is at most $`6|\Delta X_j|`$.

### Proof

Take $`T\in\mathcal T_j(R)`$, and let $`r\in R_j`$ be a rattler in $`T`$.  The
other vertices of $`T`$ cannot be distinct points of $`B`$: by (137.1) they would
be at distance strictly greater than one from $`r`$.  They therefore both lie in
$`U_j`$.  A point of $`U_j`$ cannot coincide with $`r`$, because then $`r`$ would
belong to $`W_j=N_B(U_j)`$ and would not be in $`R_j`$.  The triangle cannot contain
two points of $`R_j`$, since two distinct points of $`R\subseteq B`$ are strictly
more than one apart.  This proves the first assertion.

Write the two $`X`$-vertices as $`x,y`$.  They are a unit edge of $`X`$.  If both
belonged to $`U_{j-1}`$, the same triangle would already lie in $`P_{j-1}`$, so at
least one belongs to $`\Delta X_j`$.

For a fixed unit edge $`xy`$, the equations

```math
|z-x|=|z-y|=1
```

have at most two solutions in the plane.  Thus at most two rattler triangles can be
assigned to the same (X)-edge.  The unit-contact graph of a unit-separated planar
set has maximum degree six: the angular gaps between unit neighbors of any point are
at least $`60^\circ`$.  Hence

```math
e_X(\Delta X_j)\le
\sum_{x\in\Delta X_j}\deg_X(x)\le6|\Delta X_j|,
```

which proves (137.3).  Finally, a fixed $`x\in\Delta X_j`$ has at most six points
of the unit-separated set (R_j) at distance exactly one, giving the last claim. ∎

For the first flag step, $`U_0=\varnothing`$.  In particular, if
$`|\Delta X_1|=1`$, its first triangle cannot contain a retained strict rattler:
such a triangle would require two $`X`$-vertices.  More generally, Theorem 137.1
shows that a rattler-supported first triangle is a two-capacity-point event; a
one-capacity-point first triangle is necessarily supported by the non-rattler
backbone.

This does not close Target A.  The bound is only an upper bound on rattlers that are
actually used by the first triangle; no theorem forces a positive fraction of the
retained rattlers to participate, and $`|\Delta X_j|`$ is not bounded by the number
of flag increments.  A first triangle can therefore be supported entirely away from
$`R_j`$, including in the strained-monomer or regular-shell regressions.  No Schur
separator or source-Hall surplus follows from (137.3).

The exact remaining implication is still

```math
g>0\Longrightarrow
\text{a boundary/diameter-certified source replacement or direct Schur transport,}
```

equivalently

```math
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
```

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 141. Active-boundary normal form for strict rattlers

The source-capacity route uses a contact-minimal representative, while the forest
rattlerization deliberately produces strict rattlers.  There is a complementary
normalization that separates a property of a chosen representative from a property
forced on every triangle-free minimizer.

For a triangle-free global minimizer $`A`$ of diameter $`D`$, define the active-pair
count

```math
\mathfrak a(A)=|C(A)|+|H_D(A)|,
```

where $`C(A)`$ is the unit-contact set and $`H_D(A)`$ is the set of pairs at distance
$`D`$.  This is an integer bounded above for fixed $`n`$, so a maximally active
triangle-free global minimizer exists whenever any triangle-free global minimizer
exists.

> **Lemma 141.1 (active-boundary elimination).** A maximally active triangle-free
> global minimizer has no strict rattler.  That is, it has no point $`r`$ satisfying
> ```math
> 1<|r-p|<D\qquad(p\in A\setminus\{r\}).
> \tag{141.1}
> ```

### Proof

Suppose that $`r`$ is a strict rattler and hold $`A\setminus\{r\}`$ fixed.  The
strict feasible region for the moving point is

```math
U_r=\bigcap_{p\ne r}\{x:1<|x-p|<D\}.
\tag{141.2}
```

The point $`r`$ lies in $`U_r`$.  Let $`U_0`$ be the connected component containing
$`r`$.  It is bounded, since it lies in the disk
$`\{x:|x-p_0|<D\}`$ for any fixed $`p_0\ne r`$, and its closure is compact.

The boundary of $`U_0`$ is contained in the finite union of circles

```math
\{|x-p|=1\},\qquad \{|x-p|=D\}
\quad(p\in A\setminus\{r\}).
\tag{141.3}
```

Any two distinct circles in (141.3) have only finitely many intersection points.
A nonempty bounded open set has an infinite boundary, so some
$`x\in\partial U_0`$ lies on exactly one circle in (141.3).  Take a path in $`U_0`$
tending to $`x`$, and replace $`r`$ by $`x`$.  All distances remain in $`[1,D]`$.
An original diameter pair does not involve $`r`$, so it remains at distance $`D`$;
the new configuration is therefore another global minimizer.

If the unique active circle has radius $`1`$, the new point has exactly one unit
neighbor and hence cannot lie in a unit equilateral triangle.  If it has radius
$`D`$, the new point has no unit neighbor and is again triangle-free.  The fixed
points were already triangle-free, no old active pair is lost, and exactly one new
active pair is created.  Thus $`\mathfrak a`$ increases by one, a contradiction.
$`\square`$

## 141.1 Consequences and exact limitation

The lemma gives the valid existence normalization

```math
\boxed{
\text{if a triangle-free global minimizer exists, one exists with no strict rattlers.}
}
\tag{141.4}
```

In this representative every point outside the diameter-endpoint set $`Q`$ has at
least one unit contact.  This does not imply first-order jamming: a contact-bearing
vertex may have a feasible motion that breaks its contacts, and the resulting
intermediate point may be a strict rattler.  The lemma only says that such a motion
can be reterminated at a different active boundary; a leaf-to-leaf transfer may keep
the contact count unchanged.

Thus Lemma 141.1 does not prove the source-response rank bound
```math
\operatorname{rank}S\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
```
It does, however, add a useful companion to the rattlerized normal form:

1. strict rattlers can be produced by rattlerization and used to probe
   source-capacity failure; but
2. strict rattlers need not occur in a canonical triangle-free minimizer chosen to
   maximize active constraints.

Any argument combining these representatives must explicitly transport the
contact-minimal/source scaffold through the change of representative.  No such
transport is asserted here.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 142. Monotone activation budget from strict rattlers

Lemma 141.1 can be iterated without choosing a maximally active representative
in advance.  This gives a quantitative normal form and separates the contacts
created at the unit boundary from the exceptional activations that can terminate
on the diameter boundary.

> **Theorem 142.1 (finite monotone activation).** Let $`A_0`$ be any
> triangle-free global minimizer of diameter $`D`$.  There is a finite sequence
> ```math
> A_0,A_1,\ldots,A_s
> \tag{142.1}
> ```
> of triangle-free global minimizers of the same diameter with the following
> properties:
>
> 1. At step $`i`$, one currently strict rattler is moved while all other
>    points are fixed.
> 2. Every active pair of $`A_i`$ remains active in $`A_{i+1}`$.
> 3. Exactly one new active pair is created at each step.  It is either a unit
>    contact or a diameter pair; in the former case the moved point has exactly
>    one unit neighbor and no diameter neighbor, while in the latter it has
>    exactly one diameter neighbor and no unit neighbor.
> 4. The process stops with no strict rattlers, and $`s\le n`$.

### Proof

If $`A_i`$ has a strict rattler $`r`$, repeat the boundary construction in
Lemma 141.1 with $`A_i`$ in place of $`A`$.  The fixed points remain
triangle-free, an old diameter pair avoids $`r`$, and a regular boundary point
creates exactly one active pair without losing any old active pair.  The resulting
configuration is therefore another triangle-free global minimizer.  Since $`r`$
was strict before the move, the new active pair is genuinely new; the unique
active-circle alternative gives the last assertion in item 3.

No active pair is ever lost.  Hence no point that was already non-strict can
become strict, while $`r`$ itself is no longer strict.  The number of strict
rattlers decreases by at least one at every step, so the process terminates in
at most $`n`$ steps. $`\square`$

Let $`T_D`$ be the set of diameter-activation steps.  The diameter pairs created
at those steps have distinct newly moved endpoints and persist to $`A_s`$.  If
$`Q_s`$ is the set of all diameter endpoints of $`A_s`$, then

```math
|T_D|\le |Q_s|\le \pi D.
\tag{142.2}
```

The second inequality is elementary but useful here: Lemma 5.1 puts every
diameter endpoint on the convex-hull boundary; consecutive hull vertices are
unit-separated, so the hull perimeter is at least $`|Q_s|`$, while Cauchy's
perimeter-diameter inequality gives perimeter at most $`\pi D`$.

### Corollary 142.2: most initially strict rattlers activate through unit contacts

Suppose $`R_0`$ is a specified set of $`\rho`$ strict rattlers in $`A_0`$.  Run
Theorem 142.1 to exhaustion.  Every $`r\in R_0`$ eventually becomes incident to
the first new active pair involving $`r`$.  At most $`2\pi D`$ members of $`R_0`$
can have a diameter pair as that first pair, because each diameter-activation
step accounts for at most two endpoints.  Consequently at least

```math
\max\{0,\rho-2\pi D\}
\tag{142.3}
```

members of $`R_0`$ first activate through a unit contact.  Equivalently, the
final minimizer contains at least

```math
\max\left\{0,\frac{\rho-2\pi D}{2}\right\}
\tag{142.4}
```

new unit contacts having an endpoint in $`R_0`$.

This is a genuine source-to-contact transfer, but not yet the Target A Hall
surplus.  A triangle-free contact graph can still absorb linearly many such
unit activations without producing a source-side deficiency, and the theorem
does not preserve the contact-minimal scaffold used by the Schur complement.
The missing step remains a transport or charging lemma from these persistent
unit activations to $`\Delta_\Lambda-d_{\rm int}`$.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 143. Source-capacity-to-activation transfer

The same-hull extension and the monotone activation normal form can be composed.
This does not transport the Schur scaffold, but it gives a single representative
in which a super-boundary strict-rattler population leaves a quantitatively large
unit-contact trace.

Let $`A`$ be a triangle-free $`N`$-point global minimizer in $`H=\operatorname{conv}A`$,
let $`R\subseteq A`$ be a set of $`\rho`$ strict rattlers, and let
$`\widehat p_H=\alpha_1(H)-N`$.  Let $`B`$ be a maximal triangle-free extension of
A inside H, as in Section 121.  Write $`k=|B|-N`$, so $`k\le\widehat p_H`$, and let
```math
R_B=\{r\in R:|r-b|>1\text{ for every }b\in B\setminus\{r\}\}.
\tag{143.1}
```
Theorem 121.1 gives
```math
|R_B|\ge\rho-5k\ge\rho-5\widehat p_H.
\tag{143.2}
```

> **Theorem 143.1 (persistent unit-activation transfer).** There is a
> triangle-free global minimizer $`B^\ast`$ with $`|B^\ast|=|B|`$ and
> $`\operatorname{diam}B^\ast=D`$ for which at least
> ```math
> \boxed{
> \max\{0,\rho-5\widehat p_H-2\pi D\}
> }
> \tag{143.3}
> ```
> members of $`R_B`$ first become active through a unit contact.  In particular,
> $`B^\ast`$ contains at least
> ```math
> \boxed{
> \max\left\{0,\frac{\rho-5\widehat p_H-2\pi D}{2}\right\}
> }
> \tag{143.4}
> ```
> distinct unit contacts created during the activation process, each with an
> endpoint in $`R_B`$.

### Proof

Apply Theorem 142.1 to B, starting with the specified strict-rattler set $`R_B`$.
Every member of $`R_B`$ begins with no active pair and eventually becomes
non-strict, so its first active pair is one of the pairs created by the process.
By (142.2), at most $`\pi D`$ process steps create a diameter pair.  Each such
pair has at most two endpoints in $`R_B`$, so at most $`2\pi D`$ members of $`R_B`$
can have a diameter pair as their first active pair.  Equations (143.2) and (143.3)
follow.

Each unit-activation step creates one distinct unit contact.  A single such contact
can be the first active pair for at most two members of $`R_B`$, which gives
(143.4).  The terminal configuration of the process is $`B^\ast`$. $`\square`$

The conclusion is useful in the super-boundary regime
```math
\rho>5\widehat p_H+2\pi D,
\tag{143.5}
```
where it forces a positive, and asymptotically linear, family of persistent unit
contacts in a triangle-free global optimum at the capacity-extension cardinality.
It also makes the remaining obstruction concrete: the unit-contact trace may still
be absorbed by a triangle-free penny graph, and Theorem 143.1 gives neither
independent Schur-kernel vectors nor a source-Hall deficiency above
$`\widehat p_H`$.  A successful closure must still charge these contacts to the
boundary response or prove that their activation order cannot be realized in a
globally optimal triangle-free representative.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 144. Activation-edge forest

The unit-contact trace in Theorem 143.1 has an additional combinatorial
structure.  Record, for every member $`r`$ of the initial strict-rattler set
whose first active pair is a unit contact, that first pair, keeping one copy if
the same pair is the first pair for both endpoints.

> **Lemma 144.1 (activation-edge forest).** The recorded unit contacts form a
> forest in the final contact graph.  Every recorded edge has an endpoint in the
> initial strict-rattler set.  If $`u`$ initial rattlers first activate through
> unit contacts, then the forest has at least
> ```math
> \left\lceil\frac{u}{2}\right\rceil
> \tag{144.1}
> ```
> edges.

### Proof

Order the recorded edges by the activation step at which they are created.  If
an edge is recorded because $`r`$ has this edge as its first active pair, then
$`r`$ was incident to no earlier active pair and hence to no earlier recorded
edge.  Thus every recorded edge introduces at least one vertex not present in
the preceding recorded-edge graph.  Adding an edge with a new endpoint cannot
create a cycle, so the recorded graph is a forest.  Each edge can be the first
active pair for at most its two endpoints, which gives (144.1). $`\square`$

Combining Lemma 144.1 with Theorem 143.1 gives the explicit lower bound
```math
\boxed{
|F_{\rm act}|
\ge
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H-2\pi D\}}{2}
\right\rceil,
}
\tag{144.2}
```
where $`F_{\rm act}`$ is the activation-edge forest and $`\rho`$ is the size of
the original strict-rattler set in the source A.  The forest is a subgraph of the
final triangle-free unit-contact graph, and every edge has an endpoint in the
retained set $`R_B`$.

This forest statement is stronger than a mere contact count but still does not
close Target A.  The forest may be long and may have components whose two ends are
both rattlers.  The historical possibility that a recorded edge could later become
non-bridging is superseded by Theorem 156.1: the complete activation set is a bridge
forest in the final active graph.  Even with that correction, the forest supplies
neither a boundary/diameter-certified source replacement nor the Schur nullity
```math
\dim\ker S\ge\Delta_\Lambda-d_{\rm int}.
```

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

# 145. Rigidity rank of the activation forest

The forest from Lemma 144.1 has an exact linear-algebraic status that is useful
for interpreting the remaining obstruction.

> **Lemma 145.1 (forest rows are independent).** Let $`F`$ be any forest of
> nonzero unit-contact edges in a planar configuration.  The rows of the
> corresponding unit-distance rigidity matrix are linearly independent.  Hence
> ```math
> \boxed{\operatorname{rank}R_F=|E(F)|.}
> \tag{145.1}
> ```

### Proof

Take a linear dependence among the rows and choose a leaf vertex $`v`$ of a
nonempty component of $`F`$.  Exactly one row $`e=vw`$ has a nonzero block in the
two columns belonging to $`v`$, namely the nonzero vector $`p_v-p_w`$.  Inspecting
those columns forces the coefficient of row $`e`$ to vanish.  Remove $`e`$ and
iterate over the smaller forest.  All coefficients vanish. $`\square`$

Applied to the activation-edge forest $`F_{\rm act}`$, this yields
```math
\operatorname{rank}R_{F_{\rm act}}
\ge
\left\lceil
\frac{\max\{0,\rho-5\widehat p_H-2\pi D\}}{2}
\right\rceil.
\tag{145.2}
```
This is an exact constraint-rank contribution in the terminal triangle-free
representative.  It is not a nullity contribution: the forest rows constrain the
activated positions rather than producing kernel vectors.  Thus the activation
forest sharpens the diagnosis of the Target A gap but does not itself imply
```math
\operatorname{rank}S
\le d_{\rm int}+|C^\partial|-\Delta_\Lambda.
```
A closing theorem would need to show that this independent interior/contact rank
forces a compensating dependence in the boundary response, or else turns the
activation forest into a forbidden source-Hall exchange.

**LEVEL I STATUS: STILL OPEN.  TARGET A REMAINS UNRESOLVED.**

## Post-merge audit cross-reference

The exact capacity and scaffold certificates produced by the mathematical audit
are retained in the authoritative archive
docs/archive/erdos_problem_99_1.7.0-full.md and summarized in
docs/audits/mathematical_audit_2026-08-30.md.  They are intentionally kept
separate from the active continuation sections above because the original section
numbering is append-only and already contains independent activation results.

The retained audit results include the exact homothetic gain
```math
2Lr+r^2,
\qquad
r=\lfloor\varepsilon(L-1)\rfloor,
```
the nonuniform product gain
```math
L(r_1+r_2)+r_1r_2,
```
the boundary-protected core
```math
(K_1-3)_+(K_2-3)_+,
```
the strict closed-cell criterion
```math
\sigma(a,b)=a^2-ab+b^2<3,
```
and the exact free-sink and alternating-core identities
```math
h(G)\ge |Y_{\rm free}|,
\qquad
d_{\rm sc}=\sum_\ell d_\ell.
```
The mixed-interface regression and its sub-half-anchor bound
$`h(G)\le |C|`$ are also retained with executable tests.  Every item remains
conditional where source-side hull isolation or Schur transport is required; none
is promoted to a Level I solution.
