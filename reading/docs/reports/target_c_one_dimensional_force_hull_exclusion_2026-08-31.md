> Generated reading edition · [exact source](../../../docs/reports/target_c_one_dimensional_force_hull_exclusion_2026-08-31.md) · source SHA-256 `8db8cc4c520b3cc29ea302d944590034108508dfd73b01e9130defb775649a1c`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-E363EEC33715","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Target C addendum: exclusion of the one-dimensional force-hull phase

**Date:** 2026-08-31  
**Repository state:** `research/target-c-force-hull-v2-2026-08-30`  
**Run type:** proof / branch elimination  
**Target:** Level I candidate route C  
**Depends on:** Target C C4, C6, C7 and contact-minimality  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

This note completely eliminates one branch left open by the canonical KKT force-hull normal form.

For a contact-minimal triangle-free global minimizer of diameter `D>1`, the canonical maximal-support force hull cannot be one-dimensional.

The proof has two stages.  In the one-dimensional phase, Target C C4 makes the entire KKT-positive contact network an exact straight unit chain spanning the unique positive diameter pair.  Target C C6--C7 first release every other active diameter constraint while keeping that chain.  Once the unique diameter pair is the only active upper-distance constraint, a tiny transverse bending of the straight chain makes **every** unit edge strictly longer while its endpoints remain distance `D`.  All other pairwise inequalities have strict slack, so the resulting configuration has minimum distance strictly larger than one and diameter exactly `D`.  Rescaling gives diameter below `D`, contradicting global optimality.

Thus every contact-minimal triangle-free counterexample with `D>1` has a genuinely two-dimensional KKT force hull.

---

## 1. One-dimensional maximal support

Let `A` be a triangle-free global minimizer with the minimum possible number of unit contacts among all triangle-free global minimizers of the same cardinality.  Let

```math
C_*,H_*,B_*,F(A)=\operatorname{conv}B_*
```

be the maximal normalized KKT supports and canonical force hull from Target C C4.

Assume for contradiction that `F(A)` is one-dimensional.

Target C Corollary C4.1 then gives, after a rigid motion,

```math
F(A)=[0,D]\times\{0\},
\tag{C19.1}
```

```math
V(C_*)
=
\{p_k=(k,0):k=0,1,\ldots,D\},
\tag{C19.2}
```

so in particular `D` is an integer, and

```math
C_*
=
\{p_{k-1}p_k:1\le k\le D\}.
\tag{C19.3}
```

The positive diameter support consists of the single endpoint pair

```math
\boxed{H_* = \{p_0p_D\}.}
\tag{C19.4}
```

Indeed `B_*=Vert(F)=\{p_0,p_D\}` and a simple graph has only one edge on these two vertices.

### Lemma C19.1

```math
\boxed{C=C_* .}
\tag{C19.5}
```

#### Proof

Target C Corollary C7.1 states that in a contact-minimal triangle-free global minimizer,

```math
|H_*|=1\Longrightarrow C_*=C.
```

Apply (C19.4). `\square`

Thus the **entire** unit-contact graph of the source is exactly the straight chain (C19.3), together with contact-isolated vertices.

---

## 2. Release all weak diameter constraints

There may still be active diameter pairs in

```math
H\setminus H_*.
```

They are universally zero-KKT constraints.  Target C C6 supplies a fixed-`D` critical velocity which makes every weak active constraint strict to first order.  Since `H_*` has only one edge, the common-angular-rate hypothesis of Target C C7 is automatic.  Therefore C7 integrates that direction to a nearby same-`D` family of global minimizers in which every weak active constraint is strict and no inactive constraint becomes active.

Choose a sufficiently small positive time and call the resulting minimizer `A'`.

Because the original source is contact-minimal and C7 never creates a unit contact, no old unit contact can disappear along this move: otherwise `A'` would be a triangle-free global minimizer with fewer unit contacts.  Hence the straight unit chain (C19.2)--(C19.3) survives unchanged up to one common Euclidean motion.  Apply the inverse rigid motion and relabel so that in `A'`

```math
p_k=(k,0),
\qquad 0\le k\le D,
\tag{C19.6}
```

and all chain edges still have length one.

The active constraints of `A'` now have the exact form

```math
\boxed{
C(A')=C_*\text{ is the straight chain},
\qquad
H(A')=H_* = \{p_0p_D\}.
}
\tag{C19.7}
```

Every other pair has strict two-sided slack:

```math
1<|x-y|<D.
\tag{C19.8}
```

The endpoint pair remains at distance exactly `D`, so `A'` is still a global minimizer of diameter exactly `D`.

---

## 3. Bend the chain and destroy every contact

Choose real numbers

```math
a_0=a_D=0
```

such that

```math
a_k\ne a_{k-1}
\qquad(1\le k\le D).
\tag{C19.9}
```

Such a choice exists whenever `D>1`; for example take alternating values on the internal vertices and perturb them slightly if needed so every adjacent difference is nonzero.

For `t\in\mathbb R`, move only the internal chain vertices by

```math
p_k(t)=(k,t a_k),
\qquad 0\le k\le D,
\tag{C19.10}
```

and keep every contact-isolated point of `A'` fixed.

The endpoint diameter pair is fixed exactly:

```math
|p_D(t)-p_0(t)|=D.
\tag{C19.11}
```

Every old unit chain edge becomes strictly longer for every `t\ne0`:

```math
|p_k(t)-p_{k-1}(t)|^2
=
1+t^2(a_k-a_{k-1})^2
>1.
\tag{C19.12}
```

All other pairs satisfy strict slack (C19.8) at `t=0`.  There are only finitely many such pairs, so for all sufficiently small nonzero `t`, continuity preserves

```math
1<|x(t)-y(t)|<D
\tag{C19.13}
```

for every pair other than the endpoint pair and the old chain contacts.  Equations (C19.11)--(C19.13) therefore show that for sufficiently small `t\ne0`,

```math
\boxed{
\min_{x\ne y}|x(t)-y(t)|>1,
\qquad
\operatorname{diam}A'(t)=D.
}
\tag{C19.14}
```

Let

```math
m(t)=\min_{x\ne y}|x(t)-y(t)|>1.
```

Scale the whole configuration by `1/m(t)`.  The scaled configuration is unit-separated and has diameter

```math
\frac{D}{m(t)}<D=D(n),
```

contradicting the definition of the global minimum diameter.

This proves the main theorem. `\square`

---

## 4. Theorem C19

### Theorem C19 (force hull is genuinely two-dimensional)

Let `A` be a contact-minimal triangle-free global minimizer with

```math
D(n)>1.
```

Then

```math
\boxed{
\dim F(A)=2.
}
\tag{C19.15}
```

Equivalently,

```math
\boxed{|B_*|\ge3.}
\tag{C19.16}
```

In particular, the maximal normalized KKT diameter support contains at least two distinct diameter edges and at least three positive diameter endpoints.

Since `D(n)>1` for every `n\ge4`, the conclusion applies to every cardinality relevant to the large-`n` problem.

---

## 5. What was essential

The proof does **not** assert that an arbitrary one-dimensional positive KKT support is immediately bendable.  Weak active diameter constraints can block the naive straight bending at quadratic or even first order.

The exact order of operations matters:

1. maximal-support duality identifies every other diameter constraint as weak;
2. C6 releases all weak constraints simultaneously to first order;
3. the unique strong diameter edge makes C7's common-angular-rate condition automatic, so the release integrates to finite same-`D` slack;
4. contact minimality forces the strong unit chain to survive that preparation step;
5. only then is the transverse chain bending protected by strict slack in every other inequality.

This avoids the recurring regression in which a formally flexible local object is blocked by coincident diameter constraints.

---

## 6. Regression audit

- `n=2,3`: `D=1`, outside the theorem's stated `D>1` range.
- Unit square: its positive diameter support has two diagonal edges and four endpoints; force hull is two-dimensional.
- Regular pentagon: positive force hull is the pentagon.
- `n=6` pentagon plus center: positive support is two-dimensional; the center may remain KKT-invisible.
- `n=8` heptagon plus center: same.
- Straight-chain toy frameworks: they are correctly excluded as global minimum-diameter sources once all other active diameter constraints have been released.
- Activation/weak-diameter regressions: handled explicitly by the C6--C7 preparation step rather than ignored.

No density, shell, or lattice theorem is used.

---

## 7. Consequence for the current Target C split

The weak-contact branch can no longer hide in a degenerate force skeleton.  Every contact-minimal triangle-free counterexample has

```math
\boxed{
\text{one connected positive unit-contact network of diameter }D
\text{ whose convex force hull has nonempty interior.}
}
\tag{C19.17}
```

By C12 this positive contact network is connected; by C19 its boundary has at least three genuinely loaded diameter vertices; by C17--C18 the supported diameter graph obeys the large-cycle and acute-star restrictions.

The remaining KKT-invisible population therefore surrounds or lies inside a genuinely two-dimensional macroscopic force network, rather than being attached to a single stressed chain.

---

## 8. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Theorem C19:
A contact-minimal triangle-free global minimizer with D>1 cannot have a one-dimensional canonical force hull.

If F were 1D, C4 makes C_* a straight unit chain p_0,...,p_D spanning the unique H_* edge p_0p_D.  Since |H_*|=1, C7.1 gives C=C_*: every other point is contact-isolated.

Use C6+C7 first to make every weak diameter constraint strict at the same diameter D.  Contact minimality forces all chain contacts to remain unit, so after a rigid normalization the only active constraints are:
  - adjacent unit edges of the straight chain;
  - the endpoint diameter pair p_0p_D.

Now move internal chain vertices transversely:
  p_k(t)=(k,t a_k), a_0=a_D=0, a_k!=a_{k-1}.
Every chain edge becomes >1 quadratically, the endpoint pair stays exactly D, and every other pair remains strictly between 1 and D for small t by finite slack.  Hence min distance >1 at diameter D; rescaling gives diameter <D, contradiction.

Therefore dim F=2 and |B_*|>=3 for every large contact-minimal triangle-free source.
```
