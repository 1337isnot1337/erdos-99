> Generated reading edition · [exact source](../../../docs/reports/target_c_component_oler_rattler_fraction_2026-09-10.md) · source SHA-256 `92360b8d978adcd4b7552a4d2da3fa3ea1a9b5f5ca4acce964ff156c7eff4997`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-63584E4CB8C9","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — componentwise Oler bound forces low-surplus sources to be rattler-dominated

**Date:** 2026-09-10  
**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the GR branch  
**Run type:** exact force-bulk sharpening / source-population reduction  
**Target:** Target C, all post-ZF survivors  
**Depends on:** C65 full-source/core split, C36 attachment structure, ZK component ledger, Oler 21.1, the standard asymptotic `n/D(n)^2 -> pi/(2sqrt(3))`  
**External input:** none  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

Let `v` be the number of vertices in the nonisolated positive contact core and let

```math
\mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D.
```

The GR report proves

```math
\mu_DD+6
=
\sum_r\delta_r+R_I+s_B,
\tag{CO.1}
```

where every term on the right is nonnegative.  The previous ZK population estimate
used the crude disk count `n_r<=4(delta_r+1)^2` for an unloaded component.  Applying
Oler directly to the convex hull of each component improves the leading constant by a
factor `8/(pi sqrt(3))` and gives the source-scale statement

```math
\boxed{
\limsup\frac v{D^2}
\le
\frac{\pi}{2\sqrt3}
\left(\limsup\mu_D\right)^2
}
\tag{CO.2}
```

whenever the right-hand limsup is finite.

Since every global minimizer satisfies

```math
\frac n{D(n)^2}\longrightarrow\frac\pi{2\sqrt3},
```

we obtain the particularly simple population ratio

```math
\boxed{
\limsup\frac vn
\le
\left(\limsup\mu_D\right)^2.
}
\tag{CO.3}
```

Thus, for every fixed `u<1`, any post-ZF sequence with `mu_D<=u+o(1)` has

```math
\boxed{
\liminf\frac{n-v}{n}\ge1-u^2.
}
\tag{CO.4}
```

C65 identifies all `n-v` points as fully inactive contact-isolated rattlers which are
not actual diameter endpoints.  In particular a hypothetical sequence lying at the
new explicit GR scale

```math
\mu_D\le0.5947+o(1)
```

would have at least

```math
\boxed{
1-0.5947^2=0.64633191
}
```

of its entire source population outside the positive force core.  GR excludes that
exact endpoint from below, but CO remains useful in any near-frontier window above it:
for example `mu_D<=0.60+o(1)` forces at least `64%` rattlers.

This theorem does not itself exclude a source.  The regular-shell-plus-dense-rattler
regression shows why: a force skeleton can be only `O(D)` while a separate invisible
population carries the `Theta(D^2)` cardinality.  The new result makes that pathology a
quantified obligation rather than an informal possibility.

---

## 1. Exact implication

The new implication is

```text
GR/ZK:
    sum delta_r <= mu_D D + 6

+ graph distance dominates Euclidean distance inside every unit-contact component

+ finite Oler on conv(I_r):
    n_r <= (pi/(2sqrt3)) delta_r^2 + (pi/2) delta_r + 1

+ disjoint component count c_I=O(D), loaded count q=O(D)

=> v/D^2 <= (pi/(2sqrt3)) mu^2 + o(1)

+ global-minimizer density n/D^2 -> pi/(2sqrt3)

=> v/n <= mu^2 + o(1).
```

The leading constant is exact.  No force-hull area estimate is used.

---

## 2. Component diameter is at most graph diameter

Let `I_r` be one unloaded connected component of the positive contact graph.  Write

```math
n_r:=|I_r|,
\qquad
\delta_r:=\operatorname{diam}_{C[I_r]} I_r.
```

Every edge of `C[I_r]` is a unit segment.  For any `x,y in I_r`, choose a shortest
contact path of length at most `delta_r`.  The Euclidean triangle inequality gives

```math
|x-y|\le\delta_r.
```

Therefore

```math
\boxed{\operatorname{diam}(I_r)\le\delta_r.}
\tag{CO.5}
```

For a singleton component `delta_r=0`, as in the canonical convention.

---

## 3. Oler on one unloaded component

Apply canonical Oler 21.1 to

```math
X=I_r,
\qquad
K_r=\operatorname{conv}(I_r).
```

The source is unit-separated, so the Oler hypothesis holds.  By the isodiametric and
Cauchy perimeter inequalities applied with (CO.5),

```math
\operatorname{area}(K_r)
\le\frac\pi4\delta_r^2,
\qquad
\operatorname{per}(K_r)
\le\pi\delta_r.
\tag{CO.6}
```

Oler gives

```math
\begin{aligned}
n_r
&\le
\frac2{\sqrt3}\operatorname{area}(K_r)
+\frac12\operatorname{per}(K_r)+1\\
&\le
\boxed{
\frac\pi{2\sqrt3}\delta_r^2
+\frac\pi2\delta_r+1.
}
\end{aligned}
\tag{CO.7}
```

For `delta_r=0`, (CO.7) reads `n_r<=1` and is exact.

This is the only new geometric estimate needed.

---

## 4. Sum over the positive core

The nonisolated core decomposes as the loaded terminal set `B` together with the
unloaded components:

```math
v=q+\sum_r n_r.
\tag{CO.8}
```

Summing (CO.7) gives

```math
v
\le
q+c_I
+\frac\pi2\sum_r\delta_r
+\frac\pi{2\sqrt3}\sum_r\delta_r^2.
\tag{CO.9}
```

All `delta_r` are nonnegative, hence

```math
\sum_r\delta_r^2
\le
\left(\sum_r\delta_r\right)^2.
\tag{CO.10}
```

From GR/ZK (CO.1),

```math
\sum_r\delta_r\le\mu_DD+6.
\tag{CO.11}
```

The loaded set lies on the force hull and is unit-separated, so consecutive loaded
vertices have hull distance at least one.  Therefore

```math
q\le\operatorname{per}F\le\pi D.
\tag{CO.12}
```

C36 gives every unloaded component at least three distinct loaded attachments and the
noncrossing incidence bound in particular implies `c_I<=q`; the weaker
`c_I=O(D)` is all that is needed here.

Insert (CO.10)–(CO.12) into (CO.9):

### Theorem CO.1 — finite core-population bound

```math
\boxed{
 v
\le
q+c_I
+\frac\pi2(\mu_DD+6)
+\frac\pi{2\sqrt3}(\mu_DD+6)^2.
}
\tag{CO.13}
```

Whenever `mu_D` remains bounded along an unbounded sequence, the first three terms are
`O(D)`.  Taking limsups proves CO.2.

### Sign check

Equation (CO.11) is safe even when `mu_D` is slightly negative at finite `D`: CO.1
shows `mu_DD+6=sum delta_r+R_I+s_B>=0`.  Along every unbounded sequence
`mu_D>=-6/D`, so the limiting square argument has no sign ambiguity.

---

## 5. Convert to a source fraction

The standard global-minimizer packing asymptotic is

```math
\boxed{
\frac n{D(n)^2}	o\Delta_2:=\frac\pi{2\sqrt3}.
}
\tag{CO.14}
```

It follows from the Oler lower bound for `D(n)` and the strict translated triangular-
lattice upper comparison; no triangle-free assumption is involved.

Let

```math
u:=\limsup\mu_D<\infty.
```

CO.2 and CO.14 give

```math
\limsup\frac vn
=
\limsup
\frac{v/D^2}{n/D^2}
\le
\frac{\Delta_2u^2}{\Delta_2}
=u^2.
```

This proves CO.3.  Since C65 identifies the complement of the positive core with the
fully inactive rattler set `R`, `|R|=n-v`, and CO.4 follows.

---

## 6. Quantitative consequences

The theorem is most informative below `mu=1`.

- `mu<=0.5947+o(1)` implies
  
  ```math
  \liminf |R|/n\ge0.64633191.
  ```

- `mu<=0.60+o(1)` implies
  
  ```math
  \liminf |R|/n\ge0.64.
  ```

- `mu<=2^{-1/2}+o(1)` implies at least half of all source points are rattlers.

The new all-phase GR theorem says `mu>0.5947+epsilon_G` for every sufficiently large
post-ZF survivor.  CO therefore does **not** assert the first bullet is attained.  It
says that any future argument which confines `mu` to a narrow window above the GR
floor automatically enters a quantitatively rattler-dominated source phase.

---

## 7. Relation to C52 and RA

C52 already reduces all KKT-invisible population to the outer contact face after
charging bounded-face rattlers by Oler.  CO supplies a lower bound on the *total*
invisible population whenever `mu` is small.  Consequently a near-GR-floor source
cannot evade the force-bulk problem by keeping only `o(n)` rattlers: it must realize a
positive-density outer-shell population after the C52 bookkeeping is applied.

RA proves that the same source has another same-`n`, same-`D`, triangle-free global
representative in which all isolated rattlers can be moved to first unit contacts while
the original positive core is fixed.  CO therefore also quantifies how extensive that
representative change must be near the GR floor.

Neither statement transfers the new RA contacts back into positive KKT support, so no
ZF/GR theorem is applied to the RA representative here.

---

## 8. Regression audit

### 8.1 Folded unit-contact paths

A long self-avoiding unit path can have contact-graph diameter much larger than its
Euclidean diameter.  This does not invalidate CO: CO uses
`diam_Euclidean<=delta_r`, never the reverse.  It also explains why CO is an upper
population theorem rather than the missing upper bound on `sum delta_r`.

### 8.2 Square-grid components

A square grid has zero Eppstein slack and graph diameter comparable to its Euclidean
span.  Oler applies normally.  No path-like conclusion is inferred from small `R_I`.

### 8.3 Regular odd shell plus dense isolates

This is the binding force-bulk regression.  Its positive shell has only `O(D)`
vertices while an arbitrarily large invisible population can be inserted without a
global-optimality certificate.  CO permits this: the shell's `mu` is large, and even a
small core is consistent with the one-sided upper bound CO.2.

Dense isolated fillings lack the lexicographically selected **global-minimizer**
certificate needed for CO.14 to become a statement about the actual source
cardinality.  This is exactly where global optimality enters the rattler-fraction
conclusion.

### 8.4 Contact-isolated points

They are not silently discarded.  They are absent from `v` and reappear exactly as
`n-v` through C65.  The source cardinality `n` enters only in Section 5.

---

## 9. Failed closure recorded

It is tempting to combine the large rattler fraction with C52 by packing the rattlers
in the annulus between the force hull and the full source hull.  That does not close.
C52's remaining `Z_out` population includes points both inside and outside `F`, and a
facewise Oler bound on the complementary regions reproduces an internal-boundary
allowance of order `per(F)=Theta(D)`.  At leading order the available areas simply
recombine to the full isodiametric disk area.

Thus CO does not manufacture the missing whole-source inequality

```math
\delta_K+\mathscr O_A\ge c_0P.
```

A closing outer-shell theorem still has to remove the boundary-order allowance or give
a finite rearrangement.

---

## 10. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| component bound CO.7 | proved | graph-path metric + Oler + isodiametric/perimeter bounds |
| finite core bound CO.13 | proved | sum CO.7 + ZK/GR + `q,c_I=O(D)` |
| asymptotic core ratio CO.3 | proved | CO.13 + global-minimizer density asymptotic |
| `64.6%` near-frontier rattler obligation | proved as conditional window statement | direct substitution `u=0.5947` |
| outer-shell capacity contradiction | not proved | Oler boundary term reappears after region splitting |
| Level I | still open | low-`mu` rattler shell and high-`mu` defect phases remain |

---

## 11. Exact remaining implication

CO sharpens the C-II phase split to a source-wide quantitative dichotomy.

For any fixed `u in (0.5947,1)`, every post-ZF survivor satisfies one of:

1. **large renormalized defect:** `mu_D>u` along a subsequence; or
2. **rattler-dominated:** `|R|/n>=1-u^2-o(1)`.

A Level I closure can therefore be obtained by proving, for one such `u`, both:

```math
\mu_D\le u+o(1)
```

from the force/contact topology and an outer-shell theorem excluding
`1-u^2` source-density in fully inactive rattlers; or by directly excluding the
large-`mu` side.

This is stronger than the previous qualitative `force core versus rattlers` split
because the fraction is explicit and tied to the same exact currency that GR charges.

---

## 12. Promotion recommendation

**Promote after independent audit as a shared Target C force-bulk sharpening.**

The proof uses only canonical Oler and the exact ZK/GR component budget.  It does not
change the GR endpoint and is compatible with the C52 correction that leaves the
outer-shell population open.

---

## 13. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

For each unloaded component I_r,
    diam_Euclidean(I_r)<=delta_r.
Oler therefore gives
    n_r <= (pi/(2sqrt3)) delta_r^2 + (pi/2)delta_r + 1.

GR/ZK gives
    sum delta_r <= mu_D D+6,
where
    mu_D=(e_BB+2s_C-3(d_H+s_Z))/D.

Summing components and using q,c_I=O(D):
    v/D^2 <= (pi/(2sqrt3)) mu^2+o(1).
For global minimizers
    n/D^2 -> pi/(2sqrt3),
so
    v/n <= mu^2+o(1),
    rattler fraction >=1-mu^2-o(1).

Thus mu<=0.60 forces at least 64% of all source points to be C65 fully inactive
rattlers.  At 0.5947 the formal fraction is 0.64633191.

This does not close the outer-shell phase: splitting C52 regions and applying Oler
recreates a perimeter-order boundary allowance.  The next theorem must remove that
allowance or control the large-mu phase.
```
