> Generated reading edition · [exact source](../../../../docs/targets/target-a/17-plateau-response-lift.md) · source SHA-256 `07a55cd61e593aa17d68a984982809bd7c4cf6f064c513e7a5cd7226d6fe2777`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target A — plateau-endpoint source/response lift

This audited addendum corrects a remaining scope gap in Sections 163–164. The
Section-155 common placement was stated for an independently chosen `m`-point optimum,
whereas the Schur response of Sections 99, 102, and 113 is built after replacing that
optimum by the right endpoint `X^*` of the same `d=D(m)` diameter plateau. The theorem
below shows that the Bonnesen alignment works uniformly for every optimum on that
plateau. Consequently the source-certified conflict lift can be carried out on the
actual response shore `X^*`.

**LEVEL I STATUS: STILL OPEN. TARGET A REMAINS UNRESOLVED.**

---

# 165. Plateau-wide hull alignment and response-certified source lift

Retain the genuine triangle-free source
$$
A\subset H=\operatorname{conv}A,
\qquad |A|=N,
\qquad \operatorname{diam}H=D,
\tag{165.1}
$$
and the Target A smaller diameter
$$
d=D(m),
\qquad
t=\frac{D-d}{2}.
\tag{165.2}
$$
Assume the Section-155 very-super-boundary hypotheses, in particular
$$
D>16\sqrt3,
\qquad
t\ge1+3\eta(D),
\qquad
\eta(u)=3^{1/4}\sqrt u.
\tag{165.3}
$$
The explicit sufficient rattler threshold (155.4) implies (165.3).

Let
$$
p=\widehat p_H=\alpha_1(H)-N,
\qquad 0\le p<\frac{\pi D}{2}.
\tag{165.4}
$$

## 165.1 Uniform alignment for the whole `d`-plateau

> **Theorem 165.1 (plateau-wide hull alignment).** Let `q` be any cardinality with
> 

$$

> D(q)=d,
> \tag{165.5}
> 
$$


> and let `X_q` be any `q`-point global optimum of diameter `d`, with
> `K_q=conv X_q`. After aligning a circumcenter of `K_q` with the circumcenter of `H`
> used in Section 155,
> 

$$

> \boxed{K_q+\mathbb B\subseteq H.}
> \tag{165.6}
> 
$$


> Thus every optimum on the entire `d`-plateau is placeable inside the genuine source
> hull with a full unit collar.

### Proof

First suppose `K_q` is not full-dimensional. Then it is a point or a segment of length
at most `d`; after centering its minimal enclosing disk,
$$
K_q+\mathbb B\subseteq B\left(0,\frac d2+1\right).
\tag{165.7}
$$
Section 155 gives
$$
B\left(0,\frac D2-2\eta(D)\right)\subseteq H.
\tag{165.8}
$$
Since `d/2=D/2-t` and `t>=1+3 eta(D)`,
$$
\frac d2+1
\le\frac D2-3\eta(D)
<\frac D2-2\eta(D),
$$
so (165.6) follows directly.

Now suppose `K_q` is full-dimensional. Let `P_q`, `A_q`, `R_q`, and `r_q` denote its
perimeter, area, circumradius, and inradius. The canonical strict translated-lattice
bound from Section 114.2 gives
$$
q-1>\frac{d^2}{c},
\qquad c=\frac{2\sqrt3}{\pi}.
\tag{165.9}
$$
Oler's finite packing inequality gives
$$
q\le\frac{A_q}{a_0}+\frac{P_q}{2}+1,
\qquad a_0=\frac{\sqrt3}{2}.
\tag{165.10}
$$
Using Cauchy's perimeter bound `P_q<=pi d`,
$$
\begin{aligned}
A_q
&\ge a_0\left(q-1-\frac{P_q}{2}\right)\\
&>\frac{\pi d^2}{4}-\frac{\sqrt3}{4}P_q\\
&\ge\frac{\pi d^2}{4}-\frac{\sqrt3\pi}{4}d.
\end{aligned}
\tag{165.11}
$$
Consequently
$$
\begin{aligned}
P_q^2-4\pi A_q
&<P_q^2-\pi^2d^2+\sqrt3\pi P_q\\
&\le\pi^2\sqrt3\,d.
\end{aligned}
\tag{165.12}
$$
The Bonnesen inequality used in Section 155 therefore yields
$$
R_q-r_q<3^{1/4}\sqrt d=\eta(d).
\tag{165.13}
$$
Since `r_q<=d/2`,
$$
R_q<\frac d2+\eta(d),
$$
and hence, after circumcenter normalization,
$$
K_q\subset B\left(0,\frac d2+\eta(d)\right).
\tag{165.14}
$$
The source inner disk (165.8), together with `d<=D`, `eta(d)<=eta(D)`, and (165.3),
gives
$$
\begin{aligned}
\frac d2+\eta(d)+1
&=\frac D2-t+\eta(d)+1\\
&\le\frac D2-2\eta(D).
\end{aligned}
\tag{165.15}
$$
The containment in (165.14) is strict at the displayed radius, so
$$
K_q+\mathbb B
\subseteq
B\left(0,\frac d2+\eta(d)+1\right)
\subseteq H.
$$
This proves (165.6). $\square$

The theorem is stronger than the original Section-155 placement statement: no inclusion,
exchange, or coordinate relation between the chosen plateau optimum and the original
`X_m` is required.

## 165.2 Co-embedding the actual plateau-terminalized response shore

Section 99 defines
$$
m^*=\max\{q\ge m:D(q)=d\}
\tag{165.16}
$$
and chooses an `m^*`-point optimum `X^*`, with `K^*=conv X^*`. Put
$$
\ell=m^*-m.
\tag{165.17}
$$
The plateau theorem gives
$$
0\le\ell<\frac{\pi d}{2}.
\tag{165.18}
$$
By Theorem 165.1,
$$
\boxed{K^*+\mathbb B\subseteq H.}
\tag{165.19}
$$
Thus the exact fixed-source Hall theorem applies directly to `X^*`:
$$
\boxed{\nu(X^*,A)\ge m^*-p.}
\tag{165.20}
$$

Now use the actual generic triangular-lattice phase `Lambda+v` of the
plateau-terminalized scaffold. In the notation of Sections 102 and 113,
$$
Z=(\Lambda+v)\cap\operatorname{int}K^*,
\qquad
O=Y_{\rm in}\setminus Z,
\tag{165.21}
$$
where
$$
Y_{\rm in}=(\Lambda+v)\cap\operatorname{int}(K^*+\mathbb B).
\tag{165.22}
$$
The full response conflict graph has left shore `X^*` and right shore
`Y_in=Z sqcup O` before the Schur contraction.

> **Theorem 165.2 (response-shore source certification).** There is a subset
> 

$$

> X_{\rm src}\subseteq X^*
> \tag{165.23}
> 
$$


> with
> 

$$

> \boxed{|X_{\rm src}|\ge m^*-p}
> \tag{165.24}
> 
$$


> and an injection
> 

$$

> \sigma:X_{\rm src}\longrightarrow A
> \tag{165.25}
> 
$$


> such that, for every `x in X_src`, there is a lattice site
> `y_x in Y_in` satisfying
> 

$$

> \boxed{
> |x-\sigma(x)|<1,
> \qquad
> |x-y_x|<1,
> \qquad
> |\sigma(x)-y_x|<1.
> }
> \tag{165.26}
> 
$$


> In particular every vertex of `X^*` except at most `p` is incident to a genuine
> response-scaffold edge that shares a strict source conflict with a distinct source
> point.

### Proof

Take a matching of size at least `m^*-p` in the strict source conflict graph between
`X^*` and `A`, supplied by (165.20), and let `X_src` be its left image. For
`x in X_src`, put `a=sigma(x)` for its matched source point. The response lattice phase
is generic for the finite set `X^*`, so Theorem 164.1 applied to `x,a` supplies a
lattice site `y_x` with the last two strict inequalities in (165.26). Since
`x in K^*` and `|x-y_x|<1`, one has `y_x in int(K^*+B)=Y_in`. $\square$

The lattice sites `y_x` need not be distinct. Using the response-graph lattice-side
degree bound gives a disjoint subfamily.

> **Corollary 165.3 (vertex-disjoint response certificates).** There are at least
> 

$$

> \boxed{q_{\rm resp}\ge\frac{m^*-p}{5}}
> \tag{165.27}
> 
$$


> pairwise vertex-disjoint triples
> 

$$

> (x_i,a_i,y_i)\in X^*\times A\times Y_{\rm in}
> \tag{165.28}
> 
$$


> satisfying all three strict inequalities in (165.26).

### Proof

Use the same auxiliary selection as Theorem 164.2. Every matched pair `(x,a)` has at
least one common response-lattice neighbor. Any fixed lattice site has fewer than one
unit of distance to at most five points of the unit-separated set `X^*`. Therefore a
chosen right endpoint is used by at most five matched pairs; retain one pair for each
distinct chosen lattice site. $\square$

## 165.3 Certification of the actual Schur terminals

Section 102 chooses a `Z`-row basis `B subset X^*`, puts
$$
C=X^*\setminus B,
\tag{165.29}
$$
and splits the nonbasis columns as
$$
C=C^\circ\sqcup C^\partial,
\qquad |C^\circ|=d_{\rm int}.
\tag{165.30}
$$
The Schur response `S` has precisely the boundary nonbasis columns `C^partial`.

> **Corollary 165.4 (almost every Schur terminal has a source certificate).** There is
> a subset
> 

$$

> C^\partial_{\rm src}\subseteq C^\partial
> \tag{165.31}
> 
$$


> with
> 

$$

> \boxed{
> |C^\partial\setminus C^\partial_{\rm src}|\le p
> }
> \tag{165.32}
> 
$$


> such that each `c in C^partial_src` has a distinct source label `a_c in A` and at
> least one response-lattice neighbor `y_c in Z sqcup O` with
> 

$$

> |c-a_c|<1,
> \qquad |c-y_c|<1,
> \qquad |a_c-y_c|<1.
> \tag{165.33}
> 
$$


> Moreover at least
> 

$$

> \boxed{
> \frac{\max\{0,|C^\partial|-p\}}5
> }
> \tag{165.34}
> 
$$


> Schur terminals admit such certificates with pairwise distinct source labels and
> pairwise distinct lattice neighbors.

### Proof

At most `p` vertices of all of `X^*` are outside `X_src`, so the same is true after
restricting to `C^partial`. This proves (165.32). Apply Theorem 164.1 to each retained
source pair and then the lattice-side degree-five selection for (165.34). $\square$

This is the first promoted theorem in the route that labels the actual Schur terminals
with distinct points of the genuine source configuration, modulo only the exact
fixed-source hull slack `p`. It does not yet turn those labels into a separator saving.

## 165.4 Stronger rattler count at the plateau endpoint

Retain the source decomposition
$$
A=P\sqcup R,
\qquad |P|=m,
\tag{165.35}
$$
and let `tau=tau_D(A)` be the vertex-cover number of the diameter graph on `P` used in
the source-backbone theorem.

> **Lemma 165.5 (diameter-cover obstruction for `X^*`).** Any strict-conflict matching
> from `X^*` into `P` uses at most
> 

$$

> \boxed{m-\tau}
> \tag{165.36}
> 
$$


> source-backbone vertices.

### Proof

Let `U subset P` be the source endpoints used by such a matching. If two points
`p_1,p_2 in U` formed a diameter edge of the source backbone, let `x_1,x_2 in X^*` be
their distinct matched partners. Then
$$
|x_1-x_2|
\ge |p_1-p_2|-|p_1-x_1|-|p_2-x_2|
>D-2.
$$
The Section-155 regime has `t>1`, hence
$$
D-2=d+2t-2>d,
$$
contradicting `diam X^*=d`. Thus `U` is an independent set in the source-backbone
diameter graph. Its size is at most `m-tau`, because `tau` is that graph's minimum
vertex-cover number. $\square$

> **Corollary 165.6 (plateau-amplified rattler certification).** A source matching
> `X^*->A` of size at least `m^*-p` contains at least
> 

$$

> \boxed{
> r_*\ge\max\{0,\tau-p+\ell\}
> }
> \tag{165.37}
> 
$$


> edges ending in genuine strict rattlers, where `ell=m^*-m`. Consequently the actual
> plateau-terminalized response graph contains at least
> 

$$

> \boxed{
> q_R^*\ge\frac{\max\{0,\tau-p+\ell\}}5
> }
> \tag{165.38}
> 
$$


> pairwise vertex-disjoint source-certified scaffold edges whose source mediators are
> strict rattlers.

### Proof

By Lemma 165.5 at most `m-tau` matched source endpoints can lie in `P`, while the full
source matching has at least `m^*-p=m+ell-p` edges. Subtraction gives (165.37). Apply
the common-neighbor lift and degree-five selection only to those rattler-ending edges.
$\square$

The extra plateau population `ell` is a genuine gain over the pre-terminalized
Section-164 bound. It is only boundary-order by (165.18), so it does not create a false
super-boundary conclusion when `tau` is small.

## 165.5 Exact consequence for the Schur problem

The canonical response theorem gives
$$
\operatorname{rank}S
=\lambda_S,
\tag{165.39}
$$
the maximum number of pairwise vertex-disjoint directed alternating paths from
`C^partial` to the free right vertices `O`, and
$$
\zeta=|C^\partial|-\operatorname{rank}S.
\tag{165.40}
$$
Target A still requires
$$
\boxed{\zeta\ge\Delta_\Lambda-d_{\rm int}.}
\tag{165.41}
$$

Corollary 165.4 removes a concrete transport gap: except for at most the exact source
slack `p`, every **actual Schur source terminal** now carries a distinct genuine-source
label together with a common response-lattice conflict. Earlier source/scaffold results
only labeled the pre-terminalized `m`-point optimum or produced source-hull boundary
objects not identified with `C^partial`.

This is still not (165.41). The remaining exact lemma can now be stated more narrowly:

> **Source-labeled Menger lemma.** In the Section-165 common placement, prove that the
> source labels and common-neighbor certificates on `C^partial_src`, together with the
> global minimum-diameter origin of `A`, force every directed `C^partial->O` linkage to
> lose at least
> 

$$

> \Delta_\Lambda-d_{\rm int}
> 
$$


> terminals, or else yield an `N`-point unit-separated set of diameter `<D`.

A proof based only on the cardinality of the certificates is invalid: Sections 152 and
the strained-monomer regression show that abundant local incidence can coexist with
full response rank. The new usable information is the exact identification of almost
all response terminals with distinct genuine-source points in the same geometry.
