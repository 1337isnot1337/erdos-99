> Generated reading edition · [exact source](../../../docs/reports/target_c_threshold_fiber_normalization_and_opposite_switch_2026-10-02.md) · source SHA-256 `8b9ed5958a01d567184a948028992eb9304f3d5952494d31cdf94d4f18530ea7`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-E4D0A5DA7249","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- normalize threshold fiber splitting and couple it to the opposite shore

Date: 2026-10-02
Starting commit: 78a65968d51af7871a0ce5a865bf2db1a2c2e0ec
Branch: swarm/audit/threshold-fiber-normalization-20261002
Status: proof-only regression/repair plus a new exact coupling lemma; no promotion claimed. C-II and Level I remain open.

> candidate lemma -> exact canonical quantity -> contradiction / strict competitor / Level I consequence
>
> paired threshold staircase + complete-grid joint switch budget
> -> endpoint-degree / opposite-shore switch currency
> -> either a large extreme gap-star or a linear family of diameter rows constant on the opposite shore
> -> still requires a geometric contradiction or finite source-preserving move.

## 1. Mission

The newest threshold exact-phase report on main proves that the selected physical
diameter forest F has

```math
|E(F)|=2m+1,\qquad
|V(F)|=2m+1+c(F),
```

and, if n_j is the number of physical vertices in collapsed layer j,

```math
\sum_{j=0}^m(n_j-1)=m+c(F).
\tag{1}
```

It interprets (1) as a linear amount of physical layer-fiber splitting which should
next be coupled to the opposite complete O--O shore.

That interpretation needs a normalization correction. The paired-staircase theorem
already chooses two opposite hull-arc orientations over every simple gap-tree edge.
Those two orientations force two different physical vertices at every interior layer
before any genuine side-level fiber splitting occurs.

The first result below separates this mandatory two-sheet duplication from genuine
physical splitting. The second result then performs the requested coupling to the
opposite shore using the already-proved joint switch budget.

## 2. Dependencies and authority

Canonical repository authority remains docs/STATE.md and
docs/state/theorem-state.yaml; C-II is open.

This note uses the following unpromoted proof-only October dependencies from main:

1. docs/reports/target_c_exact_phase_gap_graph_connectivity_2026-10-01.md;
2. docs/reports/target_c_exact_phase_threshold_paired_staircase_2026-10-01.md;
3. docs/reports/target_c_exact_phase_threshold_forest_lift_2026-10-01.md;
4. docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md.

No claim below promotes any of them.

The only facts imported are:

- the simple threshold gap graph T is a tree on 0,...,m;
- every simple edge {a,b}, a<b, has two distinct physical diameter
  representatives
  ```math
  L_aU_b,\qquad L_bU_a;
  
  ```
- all those representatives and the parallel full-support diameter h_0 cross one
  common retained train;
- the resulting physical graph F is a forest;
- for the two shores A,B of the complete O--O rectangle, every actual diameter
  edge h satisfies
  ```math
  t_A(h)+t_B(h)\le2,
  \tag{2}
  
  ```
  where t_A,t_B count internal adjacent selected interfaces at which signed cut
  incidence changes.

No computation is used.

## 3. Mandatory two-sheet occupancy

Let n_j have the meaning used in the current forest-lift report: the number of
distinct physical vertices of F in collapsed complement-dual layer j.

### Lemma 3.1 -- every interior layer already has two physical vertices

For every
```math
1\le j\le m-1,
```
one has
```math
\boxed{n_j\ge2.}
\tag{3}
```

#### Proof

Because T is a spanning tree, layer j is incident with some simple edge {a,b}.

If j=a, the paired-staircase theorem supplies the two physical representatives
```math
L_aU_b,\qquad L_bU_a.
```
Their layer-j endpoints lie respectively on the hull arcs L and U.

If j=b, the same two representatives have their layer-j endpoints on U and L,
respectively.

The open arcs L,U are disjoint away from the two reference-diameter endpoints,
which occupy the extreme layers 0,m. Since j is interior, the two layer-j
endpoints are distinct physical source vertices. This proves (3).

The extreme layers satisfy n_0,n_m>=1 because h_0 itself has one endpoint in
each.

Thus the paired orientation theorem alone forces the baseline occupancy

```math
1,\underbrace{2,\ldots,2}_{m-1\ {\rm layers}},1,
```

containing exactly 2m physical vertices before any excess is counted.

## 4. Exact normalized split identity

Define the normalized collapsed-fiber excess

```math
E_{\rm norm}
:=
(n_0-1)+(n_m-1)
+\sum_{j=1}^{m-1}(n_j-2).
\tag{4}
```

By Lemma 3.1 this is nonnegative.

### Theorem 4.1 -- the genuine excess is component count plus one

```math
\boxed{E_{\rm norm}=c(F)+1.}
\tag{5}
```

Equivalently, the current-main identity decomposes exactly as

```math
\boxed{
\sum_{j=0}^m(n_j-1)
=
\underbrace{(m-1)}_{\text{mandatory paired two-sheet baseline}}
+
\underbrace{(c(F)+1)}_{\text{normalized excess}}.
}
\tag{6}
```

#### Proof

The layers partition V(F), so

```math
\sum_{j=0}^m n_j=|V(F)|.
```

The selected graph has 2m+1 edges and is a forest with c(F) nontrivial
components. Hence

```math
|V(F)|=2m+1+c(F).
```

Subtracting the baseline 2m from (4) gives

```math
E_{\rm norm}
=
|V(F)|-2m
=
c(F)+1.
```

Equation (6) is the same identity after adding back the m-1 mandatory interior
duplications.

### Consequence

The statement

```math
\sum_j(n_j-1)\ge m+1
```

does not by itself exhibit Omega(m) genuine side-level splitting. Even with
c(F)=1, the left side is m+1, while the normalized excess is only 2.

The linear term has a precise source: the two opposite hull-arc orientations already
supply one formal L_j and one formal U_j endpoint at every interior layer. What the
forest theorem forces beyond that baseline is much smaller but topologically
localized.

This is a regression in the frontier interpretation, not in the forest identity
itself.

A future argument may still prove c(F)=Omega(m) or force further side-level
multiplicity. The present October chain does not yet do that.

## 4.2 Rejected stronger localization: the formal double-cover shortcut is invalid

A tempting strengthening is to treat the symbols L_j,U_j as unique vertices, identify
L_0=U_0=z and L_m=U_m=a, and conclude that the paired tree lift plus h_0 contains two
formal cycles which must each be broken by a physical split.

That argument is invalid.

In the paired-staircase theorem, L_j and U_j specify a hull arc and an A-layer
category for an endpoint; they do not name one canonical source vertex in that
category. In particular, a selected paired diameter endpoint in A-layer 0 can lie on
the layer-0 portion of L or U without being z, and the analogous statement holds at
layer m without the endpoint being a. The reference diameter h_0 supplies z,a, but it
does not identify all other extreme-layer representatives with them.

Therefore the proposed formal quotient does not faithfully encode physical endpoint
incidence, and its cycle rank cannot be used to localize the c(F)+1 normalized excess.

Disposition: REJECTED. The exact identity E_norm=c(F)+1 remains valid; no localization
of those excess vertices follows from the paired-tree notation alone.

After this branch started, concurrent main commit
fbeae9b3fa18a63e07573676b4e2e512a91ca4d5 proved a different and valid stronger
coupling: every internal A-layer has one selected endpoint on each A-host interval,
those intervals are the two extreme B-layers, and every paired representative of an
internal tree edge has full support on B. That theorem should be used instead of the
rejected double-cover shortcut.

## 5. Exact coupling to the opposite complete shore

Now use the complete O--O rectangle and call the threshold exact-phase shore A.
Let the opposite retained shore be B.

For a simple tree edge
```math
e=\{a,b\},\qquad 0\le a<b\le m,
```
define
```math
k(e):=\mathbf1_{\{a=0\}}+\mathbf1_{\{b=m\}}\in\{0,1,2\}.
\tag{7}
```

The two paired physical representatives over e have the same A-support
interval (a,b].

### Lemma 5.1 -- endpoint gaps pay exactly for lost A-switches

For either physical representative h_e^\pm,

```math
\boxed{
t_A(h_e^\pm)=2-k(e).
}
\tag{8}
```

#### Proof

The signed incidence vector on the ordered A-cuts is zero through position a,
constant nonzero on positions a+1,\ldots,b, and zero after b.

There is an internal start switch exactly when a>0, and an internal stop switch
exactly when b<m. Therefore

```math
t_A=\mathbf1_{\{a>0\}}+\mathbf1_{\{b<m\}}
=2-k(e).
```

Combining (8) with the joint complete-grid bound (2) gives the requested
cross-shore coupling.

### Theorem 5.2 -- opposite-shore switch complementarity

For every paired representative,

```math
\boxed{
t_B(h_e^\pm)\le k(e).
}
\tag{9}
```

In particular:

- if 0<a<b<m, then t_B(h_e^\pm)=0;
- if exactly one of a=0, b=m holds, then t_B(h_e^\pm)\le1;
- if e={0,m}, then t_B(h_e^\pm)\le2.

Because exact laminar support on B is an interval with constant sign, the first
case means that every paired representative over an interior gap-tree edge is
constant on the whole selected B shore: its B-incidence is either empty or full.

Let d_0,d_m be the degrees of the extreme vertices 0,m in T, and let

```math
\epsilon_{0m}:=\mathbf1_{\{\{0,m\}\in E(T)\}}.
```

Then the number of simple tree edges incident with neither extreme is exactly

```math
m-d_0-d_m+\epsilon_{0m}.
\tag{10}
```

Hence at least

```math
\boxed{
2\bigl(m-d_0-d_m+\epsilon_{0m}\bigr)
}
\tag{11}
```

of the selected paired actual diameters have t_B=0.

Moreover, summing (9) over both physical representatives of every tree edge gives

```math
\sum_{h\in F\setminus\{h_0\}} t_B(h)
\le
2(d_0+d_m).
\tag{12}
```

The reference full-support diameter has t_A(h_0)=0, so (2) gives
t_B(h_0)\le2. Thus

```math
\boxed{
\sum_{h\in F}t_B(h)
\le
2(d_0+d_m)+2.
}
\tag{13}
```

#### Proof

Equation (9) is (2) minus (8).

For (10), the union of the edge stars at 0 and m has
d_0+d_m-\epsilon_{0m} distinct edges. Subtract from the m edges of the tree.

Each remaining simple edge has two physical representatives and k(e)=0, proving
(11).

Finally
```math
\sum_{e\in E(T)}k(e)=d_0+d_m,
```
so summing the two copies of (9) gives (12); add h_0 to obtain (13).

## 6. A clean extreme-star / opposite-constant dichotomy

For every fixed
```math
0<\theta<\frac12,
```
Theorem 5.2 gives the following exact alternative.

### Corollary 6.1

Either

```math
\boxed{
\max(d_0,d_m)\ge\theta m,
}
\tag{14}
```

or more than

```math
\boxed{
2(1-2\theta)m
}
\tag{15}
```

selected paired actual diameter bars are constant on the entire opposite retained
shore B.

#### Proof

If (14) fails, then d_0+d_m<2\theta m. Equation (11) gives

```math
2(m-d_0-d_m+\epsilon_{0m})
>
2(1-2\theta)m.
```

This is the correct immediate two-shore consequence of the paired staircase.

It replaces the unsupported heuristic

```math
\text{linear collapsed fiber splitting must couple to the opposite shore}
```

by the exact fork

```math
\boxed{
\text{large extreme gap-star}
\quad\text{or}\quad
\text{linear family of paired diameter rows with zero B-switching}.
}
\tag{16}
```

## 7. Hostile audit

The following tempting stronger conclusions are not proved here.

1. t_B=0 does not by itself say whether the B-support is empty or full; both are
   allowed by laminar support.
2. A large quotient degree d_0 or d_m does not imply one physical diameter
   vertex has the same degree. Physical multiplicity inside an extreme layer is still
   possible.
3. Equation (5) does not bound c(F); c(F) could still be linear if later
   geometry forces it.
4. No source-point count contradiction follows from (5) or (13) alone.
5. No finite deformation is constructed in this note.
6. None of the October proof-only dependencies is promoted by this note.

The old September prefix-fiber reports are useful analogies but are not imported as
theorems here; their literal-chain scaffold is different from the present retained
threshold shore.

## 8. Current implication chain to Level I

The threshold exact-phase branch now has the following rigorously separated data,
conditional on the October proof-only stack:

```math
\begin{aligned}
&\text{positive KKT circulation}\\
&\Longrightarrow
\text{paired antitone gap tree }T\\
&\Longrightarrow
\text{two physical diameter orientations per tree edge}\\
&\Longrightarrow
\text{common-cut caterpillar forest }F\\
&\Longrightarrow
E_{\rm norm}=c(F)+1\\
&\Longrightarrow
\text{either an extreme gap-star or many B-constant paired diameter rows.}
\end{aligned}
```

Neither terminal alternative is currently contradictory.

## 9. Exact remaining gap

The next threshold theorem should attack one of the two alternatives in (16).

### Extreme-star branch

A large d_0 or d_m is a large quotient star. One must either:

- bound physical splitting in that extreme layer strongly enough to force a large
  actual diameter star, then use equal-length/unit-separation angular capacity; or
- show that distributing the quotient star among many physical endpoints consumes a
  source/hull/complete-grid currency which is already bounded.

### Opposite-constant branch

A linear family of paired actual diameters has no internal B-switch. The useful
next classification is to split these rows into empty-B and full-B support and use
the convex-thrackle order together with the complete transverse train family. A
closure would need an exact capacity bound, an exact unit triangle, or a
source-preserving strict diameter competitor.

The normalized component currency c(F)+1, not the raw collapsed quantity
m+c(F), should be tracked in any future fiber-splitting argument.

No computation, numerical evidence, verifier execution, or CI result is used.
