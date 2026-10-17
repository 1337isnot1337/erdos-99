> Generated reading edition · [exact source](../../research/target_c_adaptive_safe_region_saturation_2026-09-15.md) · source SHA-256 `c55083d2bb177dd27aa813a3ecf90d8f851adec9acc06348fac49099db64e90f`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

> Source formatting note: 1 unbalanced display delimiter(s) repaired at paragraph boundaries; consult the exact source.

# Target C - adaptive strict-safe regions are saturated after arbitrary source deletion

**Date:** 2026-09-15  
**Status:** canonical in `2026-10-05.audit.59` as `C-ADAPTIVE-STRICT-SAFE-SATURATION` after independent promotion audit  
**Scope:** any contact-minimal triangle-free global diameter minimizer; Type-I inactive-container applications are the main use  
**Dependencies:** global diameter minimality; canonical contact minimality; convexity of the full source hull  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The Type-I spare-capacity route needs only `O(D)` additional protected unit-packing
slots. A natural attempt is therefore to delete `O(D)` boundary guards, recover part of
the discarded collar, and use triangular-lattice area averaging to pay the diameter
vertex cover.

That strategy cannot work at the level of **strict-safe area**. Contact minimality
re-saturates every enlarged safe region after the deletion set is chosen.

The correct statement is more general than the existing depth-one safe-area theorem.
Let `R` be any finite set of old source points to be deleted, not necessarily isolates.
If `S` is a region in the old hull whose points are strictly farther than one from every
source point outside `R`, then the amount of strict-safe area is bounded by the number
of deleted points. If `R` itself removes even one old unit contact, the bound improves
by one full triangular-lattice cell.

Thus deleting contact-wall guards cannot manufacture net lattice-area credit. Any
successful Type-I boundary exchange must exploit **non-strict exact unit contacts**, not
a larger region of strict clearance.

---

## 1. Setup

Let `A` be a finite noncollinear triangle-free global minimum-diameter source of
cardinality `n`, chosen among such global minimizers to minimize the number of unit
contacts. Put

```math
K=\operatorname{conv}A,
\qquad
D=\operatorname{diam}A=D(n),
\qquad
a_0={\sqrt3\over2}.
\tag{AS.1}
```

Let `R subseteq A` be finite. Define

```math
E_C(R):=\{xy:\ x,y\in A,\ |x-y|=1,\ \{x,y\}\cap R\ne\varnothing\}
\tag{AS.2}
```

as the set of old unit contacts removed when `R` is deleted.

Call a measurable set `S subset int K` **strict-safe relative to `R`** if

```math
\boxed{
|y-a|>1
\qquad
(y\in S,\ a\in A\setminus R).
}
\tag{AS.3}
```

No convexity of `S` is assumed.

---

## 2. General adaptive saturation theorem

### Theorem AS.1 - arbitrary deletion set

Assume `A` has at least one unit contact. Then:

1. if `E_C(R)=emptyset`,
   ```math
   \boxed{\operatorname{area}S\le a_0|R|;}
   \tag{AS.4}
   
   ```
2. if `E_C(R)\ne emptyset`,
   ```math
   \boxed{\operatorname{area}S\le a_0\max\{|R|-1,0\}.}
   \tag{AS.5}
   
   ```

In the second case `R` is necessarily nonempty, so the maximum notation only records
the singleton endpoint cleanly.

### Proof

For `lambda>1`, let

```math
\Lambda_\lambda:=\lambda\Lambda
```

be the triangular lattice of minimum distance `lambda` and covolume

```math
a_0\lambda^2.
```

Translation averaging over one fundamental cell gives

```math
\mathbb E_t |(t+\Lambda_\lambda)\cap S|
={\operatorname{area}S\over a_0\lambda^2}.
\tag{AS.6}
```

#### Case 1: `R` removes no old contact

Then every point of `R` is contact-isolated. Choose one old vertex `v notin R`
incident to a unit contact; such a vertex exists because the source has a unit contact.

If `area(S)>a_0|R|`, choose `lambda>1` sufficiently close to one that

```math
{\operatorname{area}S\over a_0\lambda^2}>|R|.
```

Since the lattice count is integer-valued, some translate contains at least

```math
|R|+1
```

points of `S`. Choose exactly that many and call the set `Y`. Define

```math
A':=(A\setminus(R\cup\{v\}))\cup Y.
\tag{AS.7}
```

Cardinality is unchanged. Distinct points of `Y` are farther than one apart because
`lambda>1`, and (AS.3) gives strict separation from every retained old source point.
Thus `A'` is unit-separated and every unit contact incident to a new point is absent.

All new points lie in `int K`, so every distance involving a new point is strictly below
`D`; retained old-old distances are at most `D`. Hence

```math
\operatorname{diam}A'\le D=D(n).
```

Global minimality forces equality, so `A'` is another global minimizer. It is
triangle-free: no new point has a unit contact, and all retained triangles would have
already existed in `A`.

The deleted vertex `v` was incident to at least one old unit contact, while `R` was
contact-isolated and `Y` creates none. Therefore `A'` has strictly fewer unit contacts
than `A`, contradicting contact minimality. This proves (AS.4).

#### Case 2: `R` removes an old contact

Suppose instead that

```math
\operatorname{area}S>a_0(|R|-1).
```

Choose `lambda>1` sufficiently close to one that

```math
{\operatorname{area}S\over a_0\lambda^2}>|R|-1.
```

Some translate of `Lambda_lambda` therefore contains at least `|R|` points in `S`.
Choose exactly `|R|` and call them `Y`. Set

```math
A':=(A\setminus R)\cup Y.
\tag{AS.8}
```

The same argument gives unit separation, triangle-freeness, cardinality `n`, and
diameter at most `D`, hence exactly `D(n)`. Retained old-old contacts are unchanged;
all contacts in `E_C(R)` disappear; and `Y` creates no new unit contact. Since
`E_C(R)` is nonempty, the total unit-contact count decreases strictly. This again
contradicts contact minimality and proves (AS.5). `square`

---

## 3. Exact deleted-contact covering

The singleton case of (AS.5) is stronger than an area statement.

### Corollary AS.2 - every contact-active vertex is individually indispensable to strict holes

Let `v in A` be incident to a unit contact. Then

```math
\boxed{
\operatorname{int}K
\subseteq
\bigcup_{a\in A\setminus\{v\}}\overline B(a,1).
}
\tag{AS.9}
```

### Proof

If some `y in int K` satisfied

```math
|y-a|>1
\qquad(a\ne v),
```

openness of the finitely many strict inequalities would give a positive-area open
neighborhood `S` of `y` that is strict-safe relative to `R={v}`. But `R` removes at
least one contact, so (AS.5) gives `area(S)<=0`, contradiction. `square`

Equivalently: after deleting any contact-active source vertex, the remaining unit disks
still cover the entire old hull interior. This is an exact finite covering consequence
of the canonical contact-minimal normalization.

---

## 4. Boundary-guard deletion does not create net lattice-area credit

Let `Z` be an assigned contact-isolated population in one Type-I container and let `B`
be any nonempty finite set of old contact-wall guard vertices. Put

```math
R=Z\cup B.
```

Because `Z` is contact-isolated and every member of `B` is incident to an old unit
contact, `E_C(R)` is nonempty. Therefore every strict-safe replacement region
`S subset int K` satisfying

```math
|y-a|>1
\qquad(y\in S,\ a\in A\setminus R)
```

obeys

```math
\boxed{
\operatorname{area}S
\le a_0(z+|B|-1).
}
\tag{AS.10}
```

Thus a triangular lattice of spacing `lambda>1` cannot be forced by area averaging to
contain even `z+|B|` replacement points in such a region, let alone those points plus
a positive-size diameter vertex cover.

This remains true if the safe region is obtained by:

- deleting a consecutive run of contact-wall vertices;
- replacing that run by an artificial chord and taking a mixed-wall subregion;
- deleting several disjoint wall runs; or
- choosing the deleted guards adaptively after inspecting the container.

The geometry of the enlarged region is irrelevant. The obstruction is global
lexicographic minimality.

---

## 5. Consequence for the Type-I diameter-cover program

The audited diameter-cover theorem closes Type I if one can create enough protected
non-strict packing capacity to absorb the assigned isolates plus a vertex cover of the
complete diameter graph.

The old safe-area barrier showed that, with the source fixed, the depth-one body cannot
supply even one **strict** extra lattice point by area averaging. Theorem AS.1 closes a
natural loophole in that regression:

```text
delete O(D) boundary guards
+ recover O(D) collar / wall area
+ use a slightly expanded triangular lattice
+ spend the recovered slots on the diameter cover
```

cannot work. The recovered strict-safe area is itself bounded by the enlarged deletion
set at exactly the same triangular-cell scale.

Therefore any successful boundary exchange must use one of the following genuinely
discrete mechanisms:

1. a non-strict packing with many **exact unit contacts**;
2. a collective finite exchange whose inserted points recreate enough old contacts to
   avoid the contact-minimality contradiction while simultaneously deleting all old
   diameter pairs; or
3. a source-level argument not reducible to translation-averaged safe area.

This sharpens the Type-I frontier: exact-contact saturation is not merely one possible
route after area methods become weak. It is forced even after adaptive deletion of the
wall that created the safe region.

No lower bound on non-strict capacity is claimed here.

---

## 6. Scope audit

- The theorem applies to arbitrary finite deletion sets `R`; `R` need not consist of
  isolates or lie in one container.
- Strict safety is essential. Equality-distance contacts can evade the argument by
  replacing the old contact count and are precisely the remaining Type-I mechanism.
- New points are required to lie in `int K`; this is what keeps all their distances
  strictly below `D`.
- The proof uses the triangle-free comparison class only for contact minimality. The
  constructed strict replacement is automatically triangle-free because it creates no
  unit contacts.
- If the original source has no unit contact, Case 1 has no vertex `v`; Target C's
  canonical post-ZF source is far outside that degenerate situation.
- The theorem does not reverse Oler and does not assert any non-strict packing slot.

**Disposition:** proved exact adaptive safe-area saturation. Boundary-guard deletion
cannot rescue a strict lattice-area Type-I closure; the remaining spare-capacity problem
is necessarily an exact-contact problem. C-II and Level I remain open.
