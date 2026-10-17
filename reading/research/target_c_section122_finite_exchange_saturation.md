> Generated reading edition · [exact source](../../research/target_c_section122_finite_exchange_saturation.md) · source SHA-256 `f89c56e1c6981f0e75eef52e7d687cf97162f06a420396c826aa30095c99c456`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — Section 122: contact minimality forces finite exchange saturation in inactive chambers

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only research candidate; theorem state unchanged.  
**Dependencies:** the contact-minimal global representative; canonical Sections 77, 79, and 87 only for the inactive-chamber corollaries below.  

The macroscopic inactive-container branch contains actual contact-isolated source points.  Section 95 shows that moving such points merely until first contact need not change the normalized KKT force polytope.  The correct minimality consequence is stronger and does not use KKT force transfer at all.

Deleting one nonisolated contact vertex provides one unit of cardinality.  Contact minimality then forbids **every finite strict `k -> k+1` repacking** of contact-isolated points inside the old source hull.  On a canonical inactive chamber, any repacking supported more than unit distance from the chamber boundary is automatically compatible with every source point outside that chamber.  Thus a macroscopic inactive chamber is not merely a dense strict packing: its deep isolate population is finitely exchange-saturated in an exact source-level sense.

No source point is discarded in the theorem.  The replacement source has exactly the original cardinality.

---

## 122.1 Global finite exchange obstruction

Let `A` be a triangle-free global minimum-diameter source with

```math
|A|=n,\qquad \min_{x\ne y}|x-y|\ge1,\qquad \operatorname{diam}A=D(n)=D,
```

chosen, among all triangle-free global minimizers of cardinality `n`, to have the minimum possible number of unit contacts.  Put

```math
K=\operatorname{conv}A.
```

Let `v in A` be any nonisolated unit-contact vertex.  Let `Z subset A\setminus\{v\}` be any finite set of contact-isolated source points.

### Theorem 122.1 — one-core-funded finite exchange obstruction

There is no finite set `Y subset K` satisfying all three conditions

```math
|Y|=|Z|+1,
\tag{122.1}
```

```math
|y-y'|>1
\qquad(y\ne y',\ y,y'\in Y),
\tag{122.2}
```

and

```math
|y-a|>1
\qquad
(y\in Y,\ a\in A\setminus(Z\cup\{v\})).
\tag{122.3}
```

#### Proof

Assume such `Y` exists and form

```math
A'=(A\setminus(Z\cup\{v\}))\cup Y.
\tag{122.4}
```

Because `|Y|=|Z|+1`,

```math
|A'|=|A|=n.
\tag{122.5}
```

All retained old pairs remain at distance at least one.  Conditions (122.2)--(122.3) make every pair involving a point of `Y` have distance strictly greater than one.  Hence `A'` is unit-separated.

Every point of `A'` lies in `K`.  Since the diameter of the convex hull of a finite set equals the diameter of that set,

```math
\operatorname{diam}K=\operatorname{diam}A=D,
```

and therefore

```math
\operatorname{diam}A'\le D.
\tag{122.6}
```

But `A'` has cardinality `n` and is unit-separated, so by the definition of `D(n)`,

```math
\operatorname{diam}A'\ge D(n)=D.
```

Thus equality holds in (122.6): `A'` is another global minimizer.

No point of `Y` has a unit contact, by (122.2)--(122.3).  The deleted set `Z` had no unit contacts in `A`, while `v` had at least one.  Hence every old contact incident to `v` disappears, no contact incident to a member of `Z` is lost because there were none, and no new contact is created.  Therefore `A'` has strictly fewer unit contacts than `A`.

It is also triangle-free: all retained old contacts belonged to the triangle-free contact graph of `A`, and the new vertices `Y` have no unit contacts at all.

This contradicts the contact-minimal choice of `A`.  `\square`

### Remarks

1. `Z=emptyset` recovers the one-point deletion-covering obstruction: after deleting a nonisolated contact vertex there is no point of `K` strictly farther than one from every retained source point.
2. The theorem is finite and exact.  It does not use asymptotics, KKT stresses, the Section-57 affine kernel, or any statement about contact-isolated coordinates.
3. The theorem does **not** say that the isolated subpacking is saturated in every standard infinite-packing sense.  The precise property used below is only the source-level finite exchange obstruction (122.1)--(122.3).

---

## 122.2 Protected inactive chambers are internally unit-covered

Now work in the canonical post-ZF C-II representative.  Let `C` be one actual convex inactive chamber from Section 77, and let

```math
Z_C\subset A
```

be the contact-isolated source points assigned to `C`.  By the Section-77 chamber partition, every source point not in `Z_C` lies outside the interior of `C` (boundary points may lie on `partial C`).

For `r>0` write

```math
C_{-r}:=\{x\in C:\operatorname{dist}(x,\partial C)>r\}.
\tag{122.7}
```

### Corollary 122.2 — exact unit covering of the deep chamber

For every inactive chamber `C`,

```math
\boxed{
C_{-1}\subseteq
\bigcup_{z\in Z_C}\overline B(z,1).
}
\tag{122.8}
```

#### Proof

Choose any nonisolated contact vertex `v`; the post-ZF positive-contact core is nonempty.  Suppose `x in C_{-1}` satisfies `|x-z|>1` for every `z in Z_C`.

If `a in A\setminus Z_C`, then `a` is not in the interior of `C`.  Since `C` is convex and `x in int C`, the segment from `x` to `a` meets `partial C`.  Hence

```math
|x-a|\ge\operatorname{dist}(x,\partial C)>1.
```

Thus `x` is strictly farther than one from every point of `A\setminus\{v\}`.  Theorem 122.1 with `Z=emptyset` and `Y={x}` gives a contradiction.  `\square`

This is stronger in scope than the older unreviewed annular-chamber deletion-covering note: it applies to **every canonical inactive chamber** and requires no low-surplus perimeter branch.

---

## 122.3 Every protected finite `k -> k+1` repacking is forbidden

The one-point covering statement still understates the available consequence.

### Corollary 122.3 — finite exchange saturation in the deep chamber

Fix an inactive chamber `C`, a finite subset

```math
W\subseteq Z_C,
```

and a nonisolated contact vertex `v`.  There is no set

```math
Y\subset C_{-1}
```

with

```math
|Y|=|W|+1,
\tag{122.9}
```

such that

```math
|y-y'|>1
\qquad(y\ne y',\ y,y'\in Y)
\tag{122.10}
```

and

```math
|y-z|>1
\qquad(y\in Y,\ z\in Z_C\setminus W).
\tag{122.11}
```

#### Proof

For `y in C_{-1}`, every source point outside `Z_C` is more than one from `y` by the same convex-boundary argument used in Corollary 122.2.  Condition (122.11) handles all retained chamber isolates.  Therefore (122.10)--(122.11) imply

```math
|y-a|>1
\qquad
(y\in Y,\ a\in A\setminus(W\cup\{v\})).
```

Apply Theorem 122.1 with `Z=W`.  `\square`

We will call (122.9)--(122.11) **deep finite exchange saturation**.  This phrase is defined by the displayed conditions and is not an import of a stronger saturation theorem from infinite packing theory.

---

## 122.4 Consequence for the macroscopic-container branch

Canonical Section 79 says that the macroscopic inactive-container branch contains one actual convex inactive chamber `C_*` with

```math
\operatorname{area}(C_*)=\Omega(D^2),
\qquad
|Z_{C_*}|=\Omega(D^2),
\qquad
\operatorname{per}(C_*)=O(D),
\tag{122.12}
```

and Section 87 supplies a linear-size family of deep isolate pairs with separation

```math
1<|z-z'|\le1+{K\over D}
\tag{122.13}
```

for a fixed constant `K` after fixing the depth parameter.

For every fixed `r>0`, the boundary layer of a convex planar body satisfies

```math
\operatorname{area}(C_*\setminus (C_*)_{-r})
\le r\operatorname{per}(C_*),
\tag{122.14}
```

whenever the erosion is nonempty; the inequality also follows directly from the coarea formula and perimeter monotonicity.  Hence for every fixed `r`,

```math
\operatorname{area}((C_*)_{-r})
=\operatorname{area}(C_*)-O(D)
=\Omega(D^2).
\tag{122.15}
```

Taking `r=1` and applying Corollaries 122.2--122.3 gives the following exact branch normal form.

### Theorem 122.4 — saturated macroscopic inactive chamber

Along every macroscopic internal inactive-chamber survivor sequence there is an actual convex chamber `C_*` such that

1. `(C_*)_{-1}` has area `Omega(D^2)`;
2. `(C_*)_{-1}` is covered by the closed unit disks centered at the actual contact-isolated source points `Z_{C_*}`;
3. `Z_{C_*}` is a strict unit-separated packing;
4. every finite strict `k -> k+1` repacking of chamber isolates supported in `(C_*)_{-1}` is forbidden by global contact minimality in the precise sense of Corollary 122.3; and
5. Section 87 still supplies linearly many pairwise-disjoint deep isolate pairs at distance `1+O(1/D)` whose first blockers are themselves isolates.

All five statements concern actual source points and preserve the full source cardinality in every comparison.

---

## 122.5 Why Section 95 no longer blocks this route

Section 95 correctly shows that moving protected isolates until first contact need not change the normalized KKT stress: the new contacts can form zero-force components while the old diameter-carrying core remains untouched.

Theorem 122.1 uses a different mechanism.  It does not try to make the new contacts force-positive.  Instead it says that if a finite isolate rearrangement creates **one extra strict feasible site**, then deleting one old nonisolated contact vertex and inserting that extra site constructs a same-cardinality global minimizer with fewer contacts.  Contact minimality rules this out before any KKT re-optimization is needed.

Thus the inactive-branch closing problem can be restated without force transfer:

> prove that a macroscopic strict unit-separated packing with the canonical Section-77 `O(D)` Oler slack and the Section-87 inverse-diameter near-pair structure admits one finite strict `k -> k+1` repacking supported in the protected interior.

Such a theorem would eliminate the macroscopic internal inactive-chamber branch immediately by Theorem 122.1.

---

## 122.6 Hostile checks and limitations

### Exact cardinality

The competitor removes `|Z|+1` old source points and inserts `|Z|+1` new points.  No source point is silently discarded.

### Unit separation versus strict separation

The new points are required to be at distance **strictly greater than one** from one another and from all retained source points.  Equality would create new contacts and would not contradict contact minimality by the present argument.

### Diameter

The replacement points lie in the old convex hull `K`, so the competitor has diameter at most `D`.  Global optimality upgrades this to equality.  No unsupported claim of a strict diameter decrease is made.

### Triangle-freeness

The new points have no unit contacts, so they cannot participate in a unit-contact triangle.  The retained old contact graph was already triangle-free.

### Chamber boundary compatibility

The protected depth `>1` is essential.  It is what makes every new chamber point automatically more than one from every source point outside the chamber interior.  No claim is made for a repacking that touches the chamber boundary strip.

### Kuperberg-type finite rearrangements

The existing five-block gap-defect machinery requires an aligned triangular-lattice architecture and quantitative control of the gap width.  Sections 77, 79, and 87 do not currently provide those hypotheses.  Therefore Theorem 122.4 does **not** by itself produce the forbidden `k -> k+1` exchange.

A sequence of strict near-triangular packings can have all excess gaps arbitrarily small, so strictness alone gives no uniform support bound for a constructive exchange.  Any closure theorem here must either be scale-free/topological, derive the required phase and gap control from the canonical Oler-slack structure, or use a different source-preserving collective deformation.

### Exterior-cap branch

The proof above is written for actual internal inactive chambers.  An exterior-cap branch requires its own protected-domain statement; no exterior-cap containment theorem is asserted here.

---

## 122.7 Research disposition

Theorem 122.1 and Corollaries 122.2--122.3 are exact finite consequences of the contact-minimal global representative.  Theorem 122.4 composes them with the canonical inactive-chamber structure.

They do not close C-II.  They remove the Section-95 force-transfer obstruction from the internal inactive-chamber route and replace it with one sharply stated local-packing obligation: construct a finite strict density-increasing exchange inside the protected macroscopic chamber.

**Lifecycle:** proof-only.  No theorem-state manifest or canonical route-map entry is modified pending independent hostile audit.
