> Generated reading edition · [exact source](../../research/target_c_pentagon_contact_debt_planarity_2026-10-05.md) · source SHA-256 `6649efff9fd5f4243ad09f882ec78b2dbda1ebfd32ee98431410a6d872832cef`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "unreviewed_noncanonical", "source_blob": "f5f96b341b0893c9469dae12bdbe665ffc85fa67", "source_branch_refs": ["refs/heads/automation/target-c-pentagon-contact-debt-planarity-2026-10-05"], "source_commit": "c292562bb6c6117ca6acd12a53c9e61bc3bd1c02", "source_lifecycle": "not indexed", "source_path": "research/target_c_pentagon_contact_debt_planarity_2026-10-05.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "c10b05bcf2b93a5100b1ac7b7eccdfcb6548c141ac2636e4ec6058145e181980"} -->

> **Imported unreviewed branch research.** Source branch status is historical only; no destination claim is promoted.

# Target C: pentagon-wall contact debt forces retained-old contact recreation

**Date:** 2026-10-05  
**Base main:** ad8809fd96c2c0af9a6de4d965e9ab33efe092c6 (2026-10-05.audit.59)  
**Status:** proof-only Target C candidate; theorem-state authority unchanged.  
**LEVEL I STATUS:** OPEN. C-II remains OPEN.

## 1. Purpose

Audit.59 rules out recovering net refill credit merely by deleting contact-active
guards and averaging a strict triangular lattice over newly strict-safe area. It
leaves open non-strict replacement packets carrying exact unit contacts.

This note narrows that surviving route for the canonical pairwise vertex-disjoint
terminal pentagon walls. If every inserted point stays strictly farther than one
from every retained old source point, then exact contacts among the inserted
points cannot repay sparse pentagon-wall deletions. The reason is an exact
four-edge planar contact deficit.

The conclusion does not apply when replacement points deliberately create exact
unit contacts to retained old source vertices.

## 2. Planar contact cap

Let $`Y`$ be any finite unit-separated planar point set whose unit-contact graph
is triangle-free, and put $`r=|Y|`$. Define

```math
\kappa(r)=
\begin{cases}
0,&r\le1,\\
1,&r=2,\\
2r-4,&r\ge3.
\end{cases}
```

Then

```math
\boxed{|C(Y)|\le \kappa(r).}
\tag{2.1}
```

The straight unit-contact drawing has no proper crossing. If unit segments
$`ab`$ and $`cd`$ crossed at an interior point $`z`$, write

```math
|a-z|=t,\quad |b-z|=1-t,\quad
|c-z|=s,\quad |d-z|=1-s.
```

The four broken-line lengths between an endpoint of $`ab`$ and an endpoint of
$`cd`$ are
```math
t+s,\quad t+1-s,\quad 1-t+s,\quad 2-t-s.
```
Their average is one, so one is at most one. For the corresponding endpoint
pair the direct segment is strictly shorter because the two contact segments
meet at a nonzero angle. This contradicts unit separation. Collinear proper
overlap is excluded similarly.

Thus the contact graph is simple planar. Euler's standard triangle-free planar
bound gives $`e\le2r-4`$ for $`r\ge3`$, with the two small cases as displayed.

## 3. Exact internal-contact repayment obstruction

Let $`A`$ be the canonical contact-minimal triangle-free global minimizer used
in Target C, with $`K=\operatorname{conv}A`$. Let

```math
R\subseteq A,\qquad r=|R|>0,
```

consist of contact-active vertices, and let

```math
c_{\rm lost}
=
\#\{e\in C(A):e\cap R\ne\varnothing\}.
```

Suppose there is a same-cardinality replacement $`Y\subseteq K`$, $`|Y|=r`$,
such that

```math
|y-a|>1
\qquad
(y\in Y,\ a\in A\setminus R),
\tag{3.1}
```

and
```math
A'=(A\setminus R)\cup Y
```
is unit-separated and triangle-free.

Condition (3.1) makes every new contact internal to $`Y`$. Hence

```math
c_{\rm new}=|C(Y)|\le\kappa(r).
\tag{3.2}
```

The contact count is exactly

```math
|C(A')|=|C(A)|-c_{\rm lost}+c_{\rm new}.
\tag{3.3}
```

Also $`A'\subseteq K`$, so $`\operatorname{diam}A'\le D`$. Global minimality
forces equality. Contact minimality therefore gives the necessary condition

```math
\boxed{c_{\rm lost}\le\kappa(r).}
\tag{3.4}
```

This is the audited multi-vertex inactive-exchange obstruction specialized to a
replacement whose only possible new contacts are internal, combined with (2.1).

If $`Y\subset\operatorname{int}K`$ and deleting $`R`$ removes an old diameter
pair, canonical diameter-pair minimality also forbids equality in (3.4):
inserted interior points create no diameter pair. Then necessarily

```math
\boxed{c_{\rm lost}<\kappa(r).}
\tag{3.5}
```

No KKT multiplier floor or area estimate is used.

## 4. Apply to vertex-disjoint terminal pentagon walls

Take physical unit pentagons $`F_1,\ldots,F_p`$ whose source-vertex sets are
pairwise disjoint, as supplied in the applicable branch by canonical
C-PENTAGON-WALL-DISJOINT-BULK.

Let $`R`$ be any nonempty set of vertices chosen from these walls. Put
$`r=|R|`$, and let

```math
t=
\#\{\text{chosen pentagon boundary edges whose two endpoints both lie in }R\}.
```

Every selected wall vertex is incident with exactly two boundary edges of its
chosen pentagon. The chosen pentagon vertex sets are disjoint, so these wall
edges are distinct across the family. Double counting incidences shows that
exactly $`2r-t`$ selected pentagon boundary contacts are lost. Other old
contacts can only increase the debt. Therefore

```math
\boxed{c_{\rm lost}\ge2r-t.}
\tag{4.1}
```

For $`r\ge3`$, equations (3.4) and (4.1) give

```math
2r-t\le2r-4,
```

hence every replacement satisfying Section 3 must obey

```math
\boxed{t\ge4.}
\tag{4.2}
```

For $`r=1`$ or $`2`$, the small planar caps give an immediate contradiction
for every possible choice from the pentagon walls.

If $`Y\subset\operatorname{int}K`$ and the deleted set removes an old diameter
pair, (3.5) instead gives

```math
\boxed{t\ge5.}
\tag{4.3}
```

Thus internal exact contacts cannot make sparse guard deletion free. The
deletion set must already contain at least four original pentagon wall edges,
or at least five when the diameter-pair equality case is invoked.

## 5. Consequences

### 5.1 One guard per wall

Choose one vertex from each of any $`p\ge1`$ pairwise vertex-disjoint terminal
pentagons. Then $`r=p`$ and $`t=0`$. No same-cardinality packet strictly
unit-clear from every retained old source point can repair the deletion, even
if the inserted points may have arbitrary exact unit contacts among themselves.

For $`p\ge3`$, the walls lose at least $`2p`$ contacts while the global
replacement packet has at most $`2p-4`$ internal contacts.

### 5.2 Two nonadjacent vertices per wall

Choose two nonadjacent wall vertices from each selected pentagon. Again
$`t=0`$, now $`r=2p`$ and $`c_{\rm lost}\ge4p`$. A two-point replacement has
at most one internal contact when $`p=1`$; for $`p\ge2`$,

```math
c_{\rm new}\le4p-4<4p\le c_{\rm lost}.
```

So this deletion pattern is impossible under the Section 3 replacement
contract, even allowing contacts between replacement points assigned to
different walls.

## 6. Scope check: adjacency is a genuine escape from this proof

Deleting two adjacent vertices from each of $`p`$ disjoint pentagons gives

```math
r=2p,\qquad t=p,\qquad c_{\rm lost}\ge3p.
```

The global planar cap is $`4p-4`$ for $`p\ge2`$. Contact counting alone rules
this out only for $`p\le3`$. At $`p=4`$ the lower bound equals the planar cap;
if a diameter pair is lost and the replacement is interior, the secondary
normalization still rules out equality. For larger $`p`$, this proof alone
gives no contradiction.

Therefore the live exact-contact mechanism is localized: a collective repair
must concentrate deleted wall vertices along old wall adjacencies, or create
new unit contacts to retained old vertices.

## 7. Target C consequence

Audit.59 leaves exact-contact discrete repair alive after strict-safe area
averaging fails. In the terminal-pentagon branch, this result removes two
natural global repair patterns: one deleted guard per wall, and two
nonadjacent deleted vertices per wall.

A surviving contact-breaking/refill theorem must instead do at least one of:

- delete a pattern containing at least four old pentagon wall adjacencies
  (at least five when the diameter-pair equality case applies);
- make exact unit contacts from inserted points to retained old source points;
- use a finite source motion rather than same-cardinality replacement;
- or obtain the strict sub-$`D`$ contradiction by another Target C route.

This is a proof-only narrowing of the audit.59 repair space. It does not close
C-II, assert existence of a replacement packet, or treat new-old exact
contacts. No computation or verifier output is a proof premise.
