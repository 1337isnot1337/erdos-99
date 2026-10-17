> Generated reading edition · [exact source](../../../../docs/targets/target-c/162-typeI-container-exchange-unification-audited.md) · source SHA-256 `c3dee7348f73d50963795a9b414e9ebff623666759e79ee1b79da5ac55d3a58d`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — audited §162 unified Type-I inactive-container exchange normal form

**Date:** 2026-09-12
**Lifecycle:** audited-working proof-only route module; theorem-state authority unchanged.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This module normalizes the theorem and hostile audit from PRs #409–#410. It removes the former asymmetry between the two canonical Type-I macroscopic inactive-container alternatives:

1. an internal inactive chamber inside the force hull; and
2. an exterior cap between the force hull and the full source hull.

Both alternatives reduce to the same protected inactive-packing exchange problem. The missing theorem is still a **collective finite density-increasing repacking**; independent pair-closing motions or first-contact activation are not enough.

---

## 162.1 Common container data

Every Type-I macroscopic inactive-container survivor has an actual convex container `C_*`, internal or exterior, with an assigned contact-isolated source set `Z_*` such that

```math
\boxed{
\operatorname{area}(C_*)=\Omega(D^2),
\quad
|Z_*|=\Omega(D^2),
\quad
\operatorname{per}(C_*)=O(D),
\quad
\sigma_*=O(D).
}
\tag{162.1}
```

For an internal chamber this is canonical. For a macroscopic exterior cap, canonical §80 gives constants `alpha,P_0,zeta>0` with

```math
\operatorname{area}(C)\ge\alpha D^2,
\qquad
\operatorname{per}(C)\le P_0D,
\qquad
|Z_C|\ge\zeta D^2.
\tag{162.2}
```

The cap convention uses

```math
\sigma_C^{ext}
={\operatorname{area}(C)\over a_0}
+{\operatorname{per}(C)\over2}-1-|Z_C|,
\qquad a_0={\sqrt3\over2},
```

whereas the isolate-only matching theorem uses

```math
\sigma_C
={\operatorname{area}(C)\over a_0}
+{\operatorname{per}(C)\over2}+1-|Z_C|.
```

Hence

```math
\boxed{\sigma_C=\sigma_C^{ext}+2=O(D).}
\tag{162.3}
```

The difference is only the two closing-chord endpoint convention.

Canonical §80 supplies the exterior-cap geometry, population, slack, and the partition of `K\setminus F` into convex cap interiors up to closing chords. Its promotion audit deliberately does **not** promote the stronger claim that exterior-cap points are contact-isolated. That isolation follows instead from canonical §56. On the lexicographically normalized representative, C63 restoration plus contact minimality gives `C=C_*`, so every actual unit contact belongs to the maximal positive KKT support. Canonical §56 also proves that this positive unit-contact graph has one nontrivial component `G`, with force hull `F=\operatorname{conv}V(G)`. Hence a source point `z\notin F` cannot be incident to a unit contact: otherwise that actual contact lies in `C=C_*`, is positive in a relative-interior normalized stress, and places `z` in `V(G)\subset F`, a contradiction. Therefore every source point assigned to an exterior cap is contact-isolated in the chosen representative. The cap partition then implies that every source point not assigned to the selected cap lies outside `\operatorname{int}(C)`.

---

## 162.2 Linear inradius and fixed-depth cores

Let `r(C)` be the inradius of a bounded convex container. Inner-parallel coarea gives

```math
\operatorname{area}(C)
=\int_0^{r(C)}\operatorname{per}(C_{-t})\,dt
\le r(C)\operatorname{per}(C).
```

Therefore the exterior data (162.2) imply

```math
\boxed{
r(C)\ge {\alpha\over P_0}D.
}
\tag{162.4}
```

The same conclusion is already available for the macroscopic internal chamber. Consequently, for every fixed `w>0`, the inner parallel body `C_{*,-w}` exists for all sufficiently large `D`, and

```math
\operatorname{area}(C_*\setminus C_{*,-w})
\le w\operatorname{per}(C_*)=O_w(D),
```

so

```math
\boxed{
\operatorname{area}(C_{*,-w})=\Omega(D^2).
}
\tag{162.5}
```

Fixed positive depth is therefore available in either Type-I geometry.

---

## 162.3 Strict unit covering and finite exchange saturation

For every sufficiently large survivor,

```math
\boxed{
C_{*,-1}
\subseteq
\bigcup_{z\in Z_*}\overline B(z,1).
}
\tag{162.6}
```

### Proof

Suppose `x in C_{*,-1}` were farther than one from every assigned isolate. Every source point outside `int(C_*)` is also farther than one from `x`: the segment from `x` to that point meets `partial C_*` at distance strictly greater than one.

Delete any nonisolated contact vertex `v` of the positive core and insert `x`. Cardinality is preserved, the new source is strictly unit-separated, and `x` remains in the old full source hull `K`, so its diameter is at most `D`. Global optimality forces the diameter to equal `D(n)`, while the old vertex `v` had at least one unit contact and the inserted point has none. This contradicts contact minimality. $`\square`$

More generally, for every finite `W subset Z_*`, there is no set

```math
Y\subset C_{*,-1},
\qquad |Y|=|W|+1,
\tag{162.7}
```

such that

```math
|y-y'|>1
\quad(y\ne y'\in Y),
\qquad
|y-z|>1
\quad(y\in Y,\ z\in Z_*\setminus W).
\tag{162.8}
```

Indeed every retained source outside the container interior is protected by depth, so replacing `W` together with one nonisolated core vertex by `Y` would produce a same-cardinality global minimizer with fewer contacts.

Thus either Type-I container is finitely exchange-saturated in the same strict sense.

---

## 162.4 Loaded lexicographic exchange also unifies

Let `v` be a source vertex with positive unit-contact degree and positive actual-diameter degree. Let `W subset Z_*` be finite and

```math
Y\subset C_{*,-1},
\qquad |Y|=|W|+1.
```

Assume replacing `W union {v}` by `Y` gives a unit-separated triangle-free source. Let `c_new` be the number of new unit contacts incident to `Y`.

Every point of `C_{*,-1}` is in `int(K)`. Hence for any old `x in K` and new `y in Y`,

```math
|x-y|<D.
```

The inserted points create no actual diameter pairs. If `c_new<d_C(v)`, contact minimality is contradicted. If `c_new=d_C(v)`, the contact count is unchanged while deleting the loaded vertex removes at least one old diameter pair and creates none, contradicting the secondary diameter-pair minimization. Therefore

```math
\boxed{c_{new}>d_C(v).}
\tag{162.9}
```

The same bookkeeping extends to deletion of finitely many loaded core vertices, with the new-contact budget compared to the number of old contacts removed, provided at least one old diameter pair is lost.

Because loaded contact degree is at most three, a protected triangle-free `k -> k+1` repacking creating at most three new contacts is already forbidden whenever funded by a suitable loaded core vertex.

---

## 162.5 Near-unit matchings in either container

Canonical §81 applies to any convex body containing a specified contact-isolated set. If `nu_epsilon` is the maximum matching number among isolate pairs at distance at most `1+epsilon`, then

```math
\nu_\epsilon
\ge {3A\over8a_0}\epsilon-{\sigma\over2}.
\tag{162.10}
```

Use (162.1) with `epsilon=K/D`. Choosing fixed `K` sufficiently large gives

```math
\boxed{
\nu_{K/D}=\Omega(D).
}
\tag{162.11}
```

Thus every macroscopic Type-I container contains linearly many vertex-disjoint actual isolate pairs with

```math
\boxed{1<|x-y|\le1+{K\over D}.}
\tag{162.12}
```

The strict lower bound holds because the assigned points are contact-isolated in the full source.

---

## 162.6 Deep matching and first-blocker localization

Fix `w>0`. Radius-`1/2` disks centered at isolates in the width-`w` boundary strip are disjoint and lie in a fixed-width outer/inner parallel annulus. Since `per(C_*)=O(D)`, only

```math
O_w(D)
```

isolates can lie in that strip.

Increase the matching numerator constant from (162.11), after fixing `w`, until the linear matching lower bound dominates this boundary-strip population. Because the matching is vertex-disjoint, one obtains constants `K_w,c_w>0` with at least

```math
\boxed{c_wD}
```

pairs satisfying

```math
1<|x-y|\le1+{K_w\over D},
\qquad
\operatorname{dist}(\{x,y\},\partial C_*)\ge w.
\tag{162.13}
```

For `w>1`, the straight segment joining such a pair lies in the convex inner core `C_{*,-w}`. Moving one endpoint toward its mate by at most `K_w/D` therefore remains more than one unit from every source point outside `int(C_*)` for all sufficiently large `D`.

Hence if the chosen mate does not reach unit distance first, the first blocker is another contact-isolated source point assigned to the **same container**.

This holds for both the internal-chamber and exterior-cap alternatives.

---

## 162.7 Unified Type-I frontier

Every Type-I macroscopic inactive-container survivor therefore has one actual convex container `C_*` and isolate set `Z_*` satisfying:

1. quadratic area and isolate population;
2. linear perimeter, Oler slack, and inradius scale;
3. strict unit covering of `C_{*,-1}`;
4. strict finite exchange saturation in `C_{*,-1}`;
5. the loaded lexicographic contact-budget obstruction;
6. for every fixed `w>1`, linearly many vertex-disjoint deep isolate pairs at distance `1+O_w(1/D)`; and
7. first blockers for their straight closing motions confined to other isolates in the same container.

The Type-I branch has therefore been reduced to one common local packing obligation:

> prove a protected finite density-increasing repacking of a near-capacity convex isolate packing, possibly allowing the small contact budget paid by deleting one or several loaded core vertices.

This repacking is **not yet proved**. The scaled triangular-lattice regression remains binding: excess gaps may be much smaller than `1/D`, independent first-contact motions need not be simultaneously compatible, and contact creation need not acquire positive reoptimized KKT force.

---

## Scope audit

- The exterior isolate-only slack differs from the cap slack by exactly `2`.
- Exterior isolation is not attributed to the §80 promotion; it is derived from canonical §56's `C=C_*` full-support normalization plus uniqueness of the nontrivial positive-contact component.
- Fixed-depth protection uses the open condition `dist(x,partial C)>1`.
- Cap interiors contain only their assigned exterior source population; unassigned sources lie outside the selected open cap.
- Inserted points remain inside the old full source hull, so diameter cannot increase.
- The loaded-exchange theorem explicitly requires the replacement to remain triangle-free.
- Every exchange preserves cardinality exactly.
- Contact-isolated coordinates are never inserted into the Section-57 core affine kernel.
- No collective exchange is asserted from the near-matching theorem alone.

**Disposition:** §162 is an audited-working proof-only Type-I unification theorem. C-II and Level I remain open.
