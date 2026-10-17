> Generated reading edition · [exact source](../../../docs/audits/target_c_adaptive_safe_saturation_promotion_audit_2026-10-05.md) · source SHA-256 `6009cacc34618aa6a90b5fbb2aa2f9fa7648ecbcb05a1099831bad3b973dda1e`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-F26B8515FEB7","canonical":true,"claim_ids":["C-ADAPTIVE-STRICT-SAFE-SATURATION"],"claim_statuses":{"C-ADAPTIVE-STRICT-SAFE-SATURATION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — adaptive strict-safe saturation

**Date:** 2026-10-05  
**Audit base:** \`d99168a39401a00f1716fe1603dfc2fd7468dff3\`  
**Starting theorem state:** \`2026-10-05.audit.58\`  
**Target:** C-II / contact-breaking and protected-refill frontier  
**Verdict:** **PASS. Promote \`C-ADAPTIVE-STRICT-SAFE-SATURATION\`.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Audited sources:

- \`research/target_c_adaptive_safe_region_saturation_2026-09-15.md\`;
- \`research/target_c_adaptive_safe_region_saturation_hostile_audit_2026-09-15.md\`;
- the earlier isolate-only specialization in \`research/target_c_typeI_safe_area_saturation_barrier.md\`.

The promoted theorem is an exact source-level no-go statement for strict-safe area averaging. It is independent of the asymptotic Target C train machinery.

## 1. Setup

Let $`A`$ be a finite noncollinear triangle-free global minimum-diameter source of cardinality $`n`$, chosen among such global minimizers to minimize the number of unit contacts. Put

```math
K=\operatorname{conv}A,
\qquad
D=\operatorname{diam}A=D(n),
\qquad
a_0=\frac{\sqrt3}{2}.
```

Let $`R\subseteq A`$ be any finite deletion set.

Define
```math
E_C(R)
=
\{xy:\ |x-y|=1,\ \{x,y\}\cap R\ne\varnothing\}.
```

A bounded measurable set
```math
S\subset\operatorname{int}K
```
is **strict-safe relative to $`R`$** if
```math
\boxed{
|y-a|>1
\qquad
(y\in S,\ a\in A\setminus R).
}
```

No convexity, chamber structure, wall structure, or KKT property of $`S`$ is assumed.

Assume the source has at least one unit contact, as every canonical post-ZF Target C source does.

## 2. Exact adaptive saturation theorem

The promoted statement is

```math
\boxed{
E_C(R)=\varnothing
\quad\Longrightarrow\quad
\operatorname{area}S\le a_0|R|,
}
```

and

```math
\boxed{
E_C(R)\ne\varnothing
\quad\Longrightarrow\quad
\operatorname{area}S\le a_0(|R|-1).
}
```

The second formula is meaningful because $`E_C(R)\ne\varnothing`$ forces $`R\ne\varnothing`$.

### 2.1 No-contact deletion case

Suppose
```math
E_C(R)=\varnothing.
```

Then every point of $`R`$ is contact-isolated.

Because the source has at least one contact, choose a contact-active vertex
```math
v\in A\setminus R.
```

Assume for contradiction that
```math
\operatorname{area}S>a_0|R|.
```

Choose $`\lambda>1`$ sufficiently close to one that
```math
\frac{\operatorname{area}S}{a_0\lambda^2}>|R|.
```

Let $`\Lambda_\lambda`$ be the triangular lattice of minimum distance $`\lambda`$ and covolume $`a_0\lambda^2`$.

Translation averaging gives
```math
\mathbb E_t
\left|
(t+\Lambda_\lambda)\cap S
\right|
=
\frac{\operatorname{area}S}{a_0\lambda^2}
>
|R|.
```

Because the count is integer-valued, some translate contains at least
```math
|R|+1
```
points of $`S`$. Choose exactly that many and call the set $`Y`$.

Define
```math
A'
=
(A\setminus(R\cup\{v\}))\cup Y.
```

Cardinality is unchanged.

Distinct points of $`Y`$ are at distance at least $`\lambda>1`$, and strict safety gives
```math
|y-a|>1
\qquad
(y\in Y,\ a\in A\setminus(R\cup\{v\})).
```

Thus the inserted points create no unit contact.

Every point of $`Y`$ lies in $`\operatorname{int}K`$. A diameter endpoint of a compact convex set is an extreme boundary point, so every distance involving a point of $`Y`$ is strictly below $`D`$. Retained old-old distances remain at most $`D`$. Hence
```math
\operatorname{diam}A'\le D.
```

If the diameter is strictly below $`D`$, global diameter minimality is contradicted.

If it remains $`D`$, then $`A'`$ is another global minimizer. The points of $`R`$ had no contacts, while $`v`$ had at least one. The inserted set creates no new contacts. Hence $`A'`$ has fewer unit contacts than $`A`$, contradicting contact minimality.

Therefore
```math
\operatorname{area}S\le a_0|R|.
```

## 3. One-cell improvement when the deletion already removes a contact

Now suppose
```math
E_C(R)\ne\varnothing.
```

Assume
```math
\operatorname{area}S>a_0(|R|-1).
```

Choose $`\lambda>1`$ so close to one that
```math
\frac{\operatorname{area}S}{a_0\lambda^2}>|R|-1.
```

Some translate of $`\Lambda_\lambda`$ then contains at least $`|R|`$ points of $`S`$. Choose exactly $`|R|`$ and call the set $`Y`$.

Set
```math
A'=(A\setminus R)\cup Y.
```

Again:

- cardinality is unchanged;
- every new-new distance is $`>1`$;
- every new-old distance is $`>1`$;
- every new-involving upper distance is $`<D`$;
- retained old-old distances are unchanged.

Thus
```math
\operatorname{diam}A'\le D.
```

If the diameter drops, global minimality fails. If it remains $`D`$, contact minimality fails because $`E_C(R)\ne\varnothing`$ and no new unit contact is created.

Hence
```math
\boxed{
\operatorname{area}S\le a_0(|R|-1).
}
```

This is the exact one-cell improvement.

## 4. Pointwise covering consequence

Take
```math
R=\{v\}
```
where $`v`$ is contact-active.

Then $`E_C(R)\ne\varnothing`$, so every strict-safe measurable set relative to $`R`$ has area at most zero.

Suppose there were
```math
y\in\operatorname{int}K
```
with
```math
|y-a|>1
\qquad
\forall a\in A\setminus\{v\}.
```

The finitely many strict inequalities persist in a small open ball around $`y`$, producing a positive-area strict-safe set. Contradiction.

Therefore:

```math
\boxed{
\operatorname{int}K
\subseteq
\bigcup_{a\in A\setminus\{v\}}
\overline B(a,1)
}
```

for every contact-active $`v`$.

Equivalently, deleting one contact-active vertex never opens even one positive-radius strict-safe hole in the old hull.

## 5. Adaptive wall deletion cannot create net strict lattice credit

Let $`Z`$ be any assigned set of $`z`$ contact-isolated source points and let $`B`$ be any nonempty finite set of contact-active wall/guard vertices. Put
```math
R=Z\cup B.
```

Then
```math
E_C(R)\ne\varnothing,
```
and every strict-safe region relative to $`R`$ obeys
```math
\boxed{
\operatorname{area}S
\le
a_0(z+|B|-1).
}
```

This remains true if the region is chosen **after** the deletion set and arises by:

- deleting a consecutive wall run;
- replacing deleted wall vertices by an artificial chord;
- deleting several disjoint wall runs;
- moving selected contacts first and then choosing a protected strict-safe region;
- choosing the deletion set adaptively from the observed source geometry.

The theorem depends only on strict safety relative to the retained source.

Therefore the strategy

```math
\text{delete }O(D)\text{ wall guards}
+
\text{recover }O(D)\text{ strict-safe area}
+
\text{average a }\lambda>1\text{ triangular lattice}
```

cannot produce net refill credit beyond the deletion cost.

Any successful contact-breaking/refill argument must use genuinely discrete structure:

1. non-strict packings with exact unit contacts;
2. an explicit finite packet beating area averaging through boundary/discrete effects;
3. a collective exchange that recreates sufficient contact structure while also deleting the diameter cage;
4. or a non-repacking strict source competitor.

## 6. Compatibility with audit.54--58

The theorem does not invalidate canonical \`C-EMBEDDED-WALL-REFILL\`.

That theorem assumes an **actual certified finite packet** of enough unit-separated sites. Discrete packings can outperform what strict-safe area averaging guarantees, especially through boundary effects and exact unit contacts.

The theorem also does not conflict with audit.58 centered fan reflections. A fan blocker is a discrete near-unit obstruction. Repairing it may still be possible, but not merely because deleting its contact-active source points creates positive strict-safe area.

Audit.57 already proves that preserved walls with at most six unit edges have empty $`W_C`$. The present theorem is stronger in a different direction: even after contact-active wall vertices are deleted, strict-safe **area averaging** cannot create net capacity.

## 7. Scope audit

The promoted theorem does **not** claim:

- that non-strict unit-packing capacity is bounded by $`|R|`$;
- that exact unit-contact refill packets do not exist;
- that a finite explicit strict packet cannot beat a mean-area estimate;
- that deleting a contact-active point leaves no isolated strict-safe point on the boundary of the covered disks;
- that every safe-region construction is useless;
- that the macroscopic-container branch is closed.

Strict safety and positive area are essential.

The theorem is a route-exclusion result: strict-safe **mean area** is never free currency in the contact-minimal representative, even after the deletion set has been chosen adaptively.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.59\` and register \`C-ADAPTIVE-STRICT-SAFE-SATURATION\` as canonical.
