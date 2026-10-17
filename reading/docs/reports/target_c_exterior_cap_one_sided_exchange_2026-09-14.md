> Generated reading edition · [exact source](../../../docs/reports/target_c_exterior_cap_one_sided_exchange_2026-09-14.md) · source SHA-256 `636249c32e0f0776a3f22b12d070ced3ef4490ff842ddbfe5dc48fd8fd0215c2`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-1B82189FEB1F","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — one-sided protected exchange for exterior caps

**Date:** 2026-09-14
**Repository commit:** `ef941ab2b44aa393bdc461926769247b45754202`
**State version:** `2026-09-14.audit.47`
**Run type:** closing proof / source-level competitor
**Target:** Target C-II / Level I
**Starting status:** canonical macroscopic-container/full-core dichotomy; exterior-cap hull stability and two-sided protected exchange are unreviewed working artifacts
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md`
**External literature search:** not used for this result
**Computation:** not used; the theorem is finite and analytic

## LEVEL I STATUS

`STILL OPEN`

This report proves a one-sided protected-exchange theorem for an actual exterior cap.
It improves the erosion cost in the earlier protected-lattice exchange from the cap
perimeter to the ambient diameter. It still leaves the low-slack saturated-cap branch
unresolved and therefore does not close C-II or Level I.

## 1. Starting endpoint and exact candidate chain

For a convex inactive container $`C`$, write

```math
 a_0=\frac{\sqrt3}{2},\qquad
 \sigma=\frac{\operatorname{area}C}{a_0}
       +\frac{\operatorname{per}C}{2}+1-z,
```

where $`z`$ is the number of assigned contact-isolated source points. The earlier
two-sided protected exchange loses an inner boundary layer of area at most
$`\lambda\operatorname{per}C`$ when it uses a triangular lattice of spacing
$`\lambda>1`$.

An exterior cap has a stronger separation geometry. It is cut from the source hull
$`K`$ by a closing chord of the force hull. Every source retained after deleting the
cap population lies on the opposite side of that chord. Therefore the protected
replacement lattice needs to avoid only a one-sided chord strip. The exact intended
chain is

```math
\text{cap half-plane separation}
\to\text{one-sided protected lattice}
\to z+1\text{ strict replacement points}
\to\text{delete one nonisolated source}
\to\text{fewer-contact global minimizer}.
```

The first four arrows are proved below. The final low-slack cap branch remains live.

## 2. Exterior-cap hypotheses

Let $`A`$ be a triangle-free contact-minimal global minimizer, with
```math
 |A|=n,\qquad \operatorname{diam}A=D=D(n),\qquad K=\operatorname{conv}A.
```

Assume $`C`$ is an actual exterior cap of the form
```math
 C=K\cap\{x:u\cdot x\ge c\},
\qquad
 K\cap\{x:u\cdot x=c\}=[r,s],
\tag{OC.1}
```
where $`[r,s]`$ is its closing chord in the force hull. Let
```math
 Z=A\cap(C\setminus[r,s]),\qquad z=|Z|.
\tag{OC.2}
```

Assume:

* every point of $`Z`$ is contact-isolated in $`A`$;
* every point of $`A\setminus Z`$ satisfies $`u\cdot a\le c`$;
* $`\operatorname{diam}C\le D`$;
* $`C`$ has nonempty interior, and $`A\setminus Z`$ contains a nonisolated source; and
* $`C`$ has isolate-only Oler slack
  ```math
  \sigma=\frac{\operatorname{area}C}{a_0}
          +\frac{\operatorname{per}C}{2}+1-z.
  \tag{OC.3}
  
  ```

The second item is the precise exterior-cap assignment condition. Sources on the
closing chord are retained outside $`Z`$; sources on the outer cap arc are included
in $`Z`$. No assertion below applies to an arbitrary internal chamber, where
retained sources may occur on both sides of the chamber boundary.

## 3. One-sided protected-exchange theorem

### Theorem OC.1

Let $`\lambda>1`$. Under (OC.1)--(OC.3), if
```math
\boxed{
\sigma>
\frac{\operatorname{area}C}{a_0}\left(1-\frac1{\lambda^2}\right)
+\frac{D}{a_0\lambda}
+\frac{\operatorname{per}C}{2}+2,
}
\tag{OC.4}
```
then such an exterior cap cannot occur in $`A`$.

Equivalently, every surviving contact-minimal source satisfies
```math
\boxed{
\sigma\le
\frac{\operatorname{area}C}{a_0}\left(1-\frac1{\lambda^2}\right)
+\frac{D}{a_0\lambda}
+\frac{\operatorname{per}C}{2}+2.
}
\tag{OC.5}
```

The additional geometric loss is $`D/(a_0\lambda)`$, not
$`\operatorname{per}(C)/(a_0\lambda)`$.

There is also an exact section-profile version. Write
```math
\ell_C(t)=\mathcal H^1\bigl(C\cap\{x:u\cdot x=c+t\}\bigr),
\qquad
b_\lambda(C,u)=\int_0^\lambda \ell_C(t)\,dt,
\tag{OC.4a}
```
where $`\ell_C(t)=0`$ beyond the cap height. Then the same proof gives the
stronger sufficient condition
```math
\boxed{
\sigma>
\frac{\operatorname{area}C}{a_0}\left(1-\frac1{\lambda^2}\right)
\;+\;
\frac{b_\lambda(C,u)}{a_0\lambda^2}
\;+\;
\frac{\operatorname{per}C}{2}+2.
}
\tag{OC.4b}
```
Indeed $`b_\lambda(C,u)=\operatorname{area}(C\setminus U_\lambda)`$, and
$`b_\lambda(C,u)\le\lambda\operatorname{diam}C\le\lambda D`$, so (OC.4)
is the uniform corollary of (OC.4b).

### Proof

Set
```math
 U_\lambda=\operatorname{int}C\cap\{x:u\cdot x>c+\lambda\}.
\tag{OC.6}
```

The part of $`C`$ between the closing chord and the parallel line at distance
$`\lambda`$ has area at most $`\lambda D`$. Indeed, each section
```math
 C\cap\{x:u\cdot x=c+t\},\qquad 0<t<\lambda,
```
is a segment of length at most $`\operatorname{diam}C\le D`$, and integration in
$`t`$ gives
```math
 \operatorname{area}U_\lambda\ge\operatorname{area}C-\lambda D.
\tag{OC.7}
```

More precisely, Cavalieri's formula gives
```math
\operatorname{area}U_\lambda
=\operatorname{area}C-b_\lambda(C,u).
\tag{OC.7a}
```

Take a triangular lattice of nearest-neighbor spacing $`\lambda`$. Its fundamental
cell has area $`a_0\lambda^2`$. Translation averaging over one fundamental cell
gives a translate with at least
```math
 |Y|\ge
\left\lfloor
\frac{\operatorname{area}C-b_\lambda(C,u)}{a_0\lambda^2}
\right\rfloor
\tag{OC.8}
```
points in $`U_\lambda`$. The selected points already lie in
$`\operatorname{int}C\subseteq\operatorname{int}K`$. Under (OC.4), equation
(OC.11) below shows that the real quantity before the floor exceeds $`z+1\ge1`$;
the numerator is therefore automatically positive in the only case in which the
theorem is being applied.

Distinct points of $`Y`$ are at distance at least $`\lambda>1`$. If
$`a\in A\setminus Z`$, then $`u\cdot a\le c`$, while $`u\cdot y>c+\lambda`$.
Consequently
```math
 |y-a|\ge u\cdot(y-a)>\lambda>1.
\tag{OC.9}
```

From (OC.3),
```math
 z=\frac{\operatorname{area}C}{a_0}
   +\frac{\operatorname{per}C}{2}+1-\sigma.
\tag{OC.10}
```
The uniform lower bound for the real quantity before the floor in (OC.8) satisfies
```math
\frac{\operatorname{area}C-\lambda D}{a_0\lambda^2}-z
=\sigma
-\frac{\operatorname{area}C}{a_0}\left(1-\frac1{\lambda^2}\right)
-\frac{D}{a_0\lambda}
-\frac{\operatorname{per}C}{2}-1>1
\tag{OC.11}
```
by (OC.4). The exact unfloored quantity in (OC.8) is no smaller, because
$`b_\lambda(C,u)\le\lambda D`$. Since $`z`$ is an integer, the floor is at least
$`z+1`$. Choose
$`Y'\subseteq Y`$ with $`|Y'|=z+1`$.

Under the stronger condition (OC.4b), use the exact numerator in (OC.8) instead.
Subtracting (OC.10) gives
```math
\frac{\operatorname{area}C-b_\lambda(C,u)}{a_0\lambda^2}-z
=\sigma
-\frac{\operatorname{area}C}{a_0}\left(1-\frac1{\lambda^2}\right)
-\frac{b_\lambda(C,u)}{a_0\lambda^2}
-\frac{\operatorname{per}C}{2}-1>1,
\tag{OC.11a}
```
so the same integer-floor conclusion follows.

By hypothesis, choose a nonisolated source $`v\in A\setminus Z`$, and form
```math
 A'=(A\setminus(Z\cup\{v\}))\cup Y'.
\tag{OC.12}
```
The cardinality is exactly $`n`$. Equations (OC.8)--(OC.9) and the old
unit-separation inequalities show that $`A'`$ is unit-separated. All its points lie
in $`K`$, hence
```math
 \operatorname{diam}A'\le\operatorname{diam}K=D.
\tag{OC.13}
```
By global minimality of $`D=D(n)`$, equality holds and $`A'`$ is a global minimizer.

The point $`v`$ had at least one unit contact; the points in $`Z`$ had none; and
(OC.9), together with the spacing of $`Y'`$, gives no new unit contact. Thus $`A'`$
has strictly fewer contacts than $`A`$. It is triangle-free because the new vertices
are contact-free and the retained old contact graph was triangle-free. This
contradicts contact minimality. $`\square`$

The proof retains the full source cardinality in the comparison. Global optimality is
used exactly once, to upgrade (OC.13) to equality.

### Corollary OC.2 — one-sided cap covering and finite exchange saturation

Under the same exterior-cap hypotheses, contact minimality also gives
```math
\boxed{
\operatorname{int}C\cap\{x:u\cdot x>c+1\}
\subseteq\bigcup_{z\in Z}\overline B(z,1).
}
\tag{OC.13a}
```
More generally, if $`W\subseteq Z`$ is finite, there is no set
$`Y\subseteq\operatorname{int}C\cap\{u\cdot x>c+1\}`$ with
```math
 |Y|=|W|+1,\qquad |y-y'|>1,\qquad
 |y-z|>1\quad(z\in Z\setminus W).
\tag{OC.13b}
```

Indeed, a point in the displayed one-sided region is strictly farther than one from
every source in $`A\setminus Z`$ by the projection estimate (OC.9). For (OC.13a),
an uncovered point could replace any nonisolated source and reduce the contact count.
For (OC.13b), delete $`W`$ and one nonisolated source and apply the same
source-preserving exchange as in the proof of OC.1. The deleted cap points are
contact-isolated, and the proposed replacement points have no unit contacts.

## 4. Inverse-diameter specialization

Choose
```math
\lambda_D=1+D^{-2}.
\tag{OC.14}
```
For $`D\ge1`$,
```math
1-\lambda_D^{-2}\le2D^{-2},\qquad
\frac{D}{\lambda_D}<D.
\tag{OC.15}
```
The isodiametric inequality gives $`\operatorname{area}C\le\pi D^2/4`$. Therefore
every surviving exterior cap satisfies
```math
\boxed{
\sigma\le
\frac{D}{a_0}+\frac{\operatorname{per}C}{2}
+2+\frac{\pi}{2a_0}.
}
\tag{OC.16}
```

The previous two-sided erosion bound has $` \operatorname{per}C/a_0`$ in place of
$`D/a_0`$. Hence (OC.16) is a strict finite coefficient improvement for caps with
$`\operatorname{per}C>D`$.

The exact section-profile refinement still does not make saturation automatic. In
the strained parallelogram regression $`C_m`$ recorded in the independent cap
audit, take the closing chord parallel to one side. Its parallel sections have
constant length $`m s_m=m+1`$, so
```math
b_{\lambda_D}(C_m,u)=\lambda_D(m+1),
```
whereas
$`\operatorname{area}(C_m)/a_0=(m+1)^2`$,
$`\operatorname{per}(C_m)/2=2(m+1)`$, and
$`\sigma_m=2(m+1)+1`$. Thus the refined threshold (OC.4b) still has a
linear term $`(m+1)/a_0+2(m+1)`$, while $`\sigma_m`$ has only
$`2(m+1)+1`$. This is an exact hostile check that even the one-sided
section-profile loss leaves the saturated-cap model unresolved.

## 5. Scope and adversarial audit

* **Half-plane orientation:** the proof requires every retained source to satisfy
  $`u\cdot a\le c`$. This is true for a cap cut from a convex $`K`$ by its closing
  chord, but is not true for an internal chamber.
* **Outer-arc sources:** these are included in $`Z`$. Omitting them would invalidate
  (OC.9).
* **Chord sources:** points on the closing chord are retained and satisfy the strict
  projection inequality because the replacement region uses $`u\cdot y>c+\lambda`$.
* **Strictness:** the new points are pairwise at distance $`>\!1`$ and are strictly
  farther than one from every retained source, so contact minimality—not a weaker
  contact-count comparison—is legitimately invoked.
* **Floor and cardinality:** (OC.11) gives a real margin $`>1`$, which is exactly
  enough for the integer floor to supply $`z+1`$ points.
* **Diameter:** the replacement points lie in the old source hull. No strict
  diameter decrease is claimed; global optimality forces equality.
* **Isolated sources:** all cap points are deleted only as a set and replaced by
  $`z+1`$ new points. No source is silently discarded.
* **KKT scope:** no force or affine-kernel assertion is made, and contact-isolated
  coordinates are never included in the positive-contact core.

A hostile fixed-container check remains decisive: a near-triangular lattice can cover
the protected region with no spare strict site while retaining only boundary-order
Oler slack. Thus (OC.4) is a sufficient exchange threshold, not an automatic
contradiction.

## 6. Frontier effect and exact remaining obstruction

The exterior-cap branch is sharpened from
```math
\text{loss proportional to }\lambda\operatorname{per}C
```
to
```math
\text{loss at most }\lambda D,
```
because only the closing chord separates a cap from retained sources. More precisely,
the finite loss is the one-sided section-profile term $`b_\lambda(C,u)`$, with the
uniform $`D`$-bound as a corollary. At
$`\lambda=1+D^{-2}`$, this yields the uniform necessary bound (OC.16).

This eliminates high-slack exterior caps satisfying (OC.4). It does not eliminate a
low-slack macroscopic cap, an internal macroscopic chamber, or the Type-II full-core
branch. The canonical state supplies only $`O(D)`$ cap slack, without the lower bound
needed to violate (OC.16).

The exact next implications are therefore:

1. prove a lower bound on the slack of every macroscopic exterior cap that beats
   (OC.16);
2. reduce the $`D/a_0`$ strip cost using actual boundary-source geometry;
3. prove a collective cap exchange that deletes fewer than all $`z`$ cap points; or
4. construct a cap/core deformation or force an exact unit equilateral triangle.

No canonical theorem-state or route-map file is changed by this report.

## 7. Claim audit table

| Claim | Status | Dependencies | Reason |
| --- | --- | --- | --- |
| Exterior-cap half-plane separation | canonical scope | Section 77 exterior-cap definition | Retained sources lie in the opposite half-plane |
| One-sided strip bound (OC.7) | proved here | $`\operatorname{diam}C\le D`$; Fubini | Parallel sections have length at most $`D`$ |
| Exact section-profile exchange (OC.4b) | proved here | Cavalieri and translation averaging | Replaces the uniform strip cost by $`b_\lambda(C,u)`$ |
| Lattice count (OC.8) | proved here | triangular-lattice covolume | Translation average and exact floor |
| Strict separation (OC.9) | proved here | half-plane separation | Projection gives $`>\lambda>1`$ |
| Exchange theorem (OC.4) | proved here | contact-minimal global source and nonempty core | Same-cardinality fewer-contact competitor |
| Specialization (OC.16) | proved here | theorem plus isodiametric inequality | Uniform inverse-diameter scale |
| Automatic violation of (OC.16) | unproved | none in canonical state | Cap slack is only known as $`O(D)`$ |
| C-II/Level I closure | open | low-slack cap/core bridge | Threshold does not settle Type I |

## 8. Promotion recommendation

**unreviewed**. The theorem is complete under the explicit cap hypotheses but only
removes a high-slack subbranch. Before promotion, audit the exact cap assignment at
shared force-hull sides and the claim that every source outside the cap is in the
opposite half-plane.

## 9. Handoff

1. Strongest new result: (OC.4)--(OC.5), one-sided exterior-cap protected exchange.
2. Canonical chain: Section 77 / \`C-INACTIVE-CHAMBER\` exterior-cap decomposition plus
   contact-minimal global normal form.
3. Exact remaining lemma: a low-slack cap/core exchange, boundary-source improvement,
   or exact triangle/global strict competitor.
4. Binding dead routes: two-sided erosion alone, contact activation without force
   transfer, and density-only strict-lattice comparisons.
5. Files to read next: \`docs/targets/target-c/77-inactive-chamber-saturation-audit.md\`,
   \`docs/reports/target_c_exterior_cap_hull_and_cover_2026-09-14.md\`, and
   \`docs/reports/target_c_protected_lattice_exchange_2026-09-12.md\`.
