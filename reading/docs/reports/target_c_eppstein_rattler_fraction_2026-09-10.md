> Generated reading edition · [exact source](../../../docs/reports/target_c_eppstein_rattler_fraction_2026-09-10.md) · source SHA-256 `48465de72a26aa2677e5d66f9f40ce151e656958144c48d42d9606e37aa3f740`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-FCF8AF21ECD0","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — Eppstein isoperimetry forces at least 85% rattlers near the GR frontier

**Date:** 2026-09-10  
**Repository base:** `1adc420e9227476135d6891b61f1a75193aa90ab` plus the GR branch  
**Run type:** literature-assisted force-bulk sharpening / source-population reduction  
**Target:** Target C, all post-ZF survivors  
**Depends on:** C65, C36, ZK/GR, Eppstein 2018 Theorem 4, global-minimizer density asymptotics  
**External input:** none beyond the primary Eppstein paper already stored in `papers/primary/`; checked against `extracted/text/463.txt`  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

The preceding componentwise-Oler report proved

```math
\frac vn\le \mu^2+o(1)
```

for a post-ZF sequence with bounded

```math
\mu_D:=\frac{e_{BB}+2s_C-3(d_H+s_Z)}D.
```

That estimate ignores the fact that each unloaded component is itself a
**triangle-free penny graph**.  Eppstein's stronger isoperimetric edge theorem converts
the exact Eppstein slack already present in ZK into a square-root population charge.
The result is

```math
\boxed{
\limsup\frac vn
\le
\frac4{\pi^2}
\left(\limsup\mu_D\right)^2.
}
\tag{ER.1}
```

Equivalently, for every fixed bounded `u`, any post-ZF sequence with
`mu_D<=u+o(1)` has

```math
\boxed{
\liminf\frac{n-v}{n}
\ge
1-\frac{4u^2}{\pi^2}.
}
\tag{ER.2}
```

C65 identifies `n-v` exactly with fully inactive contact-isolated source rattlers;
none is an actual diameter endpoint.

At the explicit GR scale `u=0.5947`, the formal limiting core fraction is at most

```math
\frac4{\pi^2}(0.5947)^2
=0.1433362779\ldots,
```

so the rattler fraction is at least

```math
\boxed{0.8566637220\ldots .}
\tag{ER.3}
```

GR itself excludes `mu<=0.5947` by a uniform positive amount.  The point of ER is the
near-frontier normal form: any future argument confining `mu` even to `0.60+o(1)`
forces more than 85% of the whole global source outside the positive KKT/contact core.

This is substantially stronger than the preceding Oler-only `1-u^2` rattler fraction
and supersedes that report for force-bulk population estimates.

---

## 1. The exact implication

For one unloaded positive-contact component `I_r`, recall

```math
n_r=|I_r|,
\qquad
\delta_r=\operatorname{diam}_{C[I_r]}I_r,
```

and the exact Eppstein edge slack

```math
r_r:=2n_r-\delta_r-2-e_r\ge0.
```

Therefore

```math
\boxed{
e_r=2n_r-(\delta_r+r_r)-2.}
\tag{1.1}
```

Eppstein 2018 Theorem 4 says that there is an absolute constant `C_E` such that every
`N`-vertex triangle-free penny graph satisfies

```math
\boxed{
e\le2N-c_E\sqrt N+C_E,}
\qquad
c_E:=\frac12\sqrt{2\pi\sqrt3}
=\sqrt{\frac{\pi\sqrt3}{2}}.
\tag{1.2}
```

Apply (1.2) to each `I_r` and compare with (1.1).  With

```math
a_r:=\delta_r+r_r,
```

we obtain

```math
c_E\sqrt{n_r}\le a_r+C_E+2.
\tag{1.3}
```

Thus the same exact component currency `delta_r+r_r` appearing in ZK controls the
square root of the component population.

Summing (1.3) after squaring gives

```math
\sum_r n_r
\le
\frac1{c_E^2}
\left(
\left(\sum_r a_r\right)^2+O\left(\sum_r a_r\right)+O(c_I)
\right).
\tag{1.4}
```

ZK/GR gives

```math
\sum_r a_r+s_B
=\mu_DD+6,
```

so

```math
\sum_r a_r\le\mu_DD+6.
\tag{1.5}
```

Because `q,c_I=O(D)`, the loaded vertices and all linear terms are lower order.  Since

```math
c_E^2=\frac{\pi\sqrt3}{2},
```

we obtain

```math
\boxed{
\limsup\frac v{D^2}
\le
\frac{2}{\pi\sqrt3}
\left(\limsup\mu_D\right)^2.
}
\tag{1.6}
```

Finally

```math
\frac n{D(n)^2}\to\frac\pi{2\sqrt3},
```

so division gives ER.1 because

```math
\frac{2/(\pi\sqrt3)}{\pi/(2\sqrt3)}
=\frac4{\pi^2}.
```

That is the entire argument.

---

## 2. Primary-source audit of Eppstein Theorem 4

The source is David Eppstein,
*Edge Bounds and Degeneracy of Triangle-Free Penny Graphs and Squaregraphs*,
J. Graph Algorithms Appl. 22(3) (2018), 483--499, already stored in the repository
and extracted as `extracted/text/463.txt`.

Theorem 4 states

```math
e\le
2N-\frac12\sqrt{2\pi\sqrt3\,N}+O(1).
\tag{2.1}
```

The preceding Lemma 4 obtains the `sqrt(N)` term from an outer-face isoperimetric
bound; Lemma 5 converts an outer face with `k` incidences into

```math
e\le2N-k/2-2.
```

The `O(1)` in (2.1) is therefore absolute over the class of triangle-free penny graphs,
not a component-dependent parameter.

The paper is written for congruent tangent circles.  Scaling the centers by a constant
does not change the abstract contact graph or the theorem, so the repository's
normalization with center separation/contact length one is identical for this use.

No form of Swanepoel's stronger conjectured `2N-2sqrt(N)` bound is used; Eppstein
explicitly leaves that conjecture open.

---

## 3. Detailed summation with the `O(1)` term

Choose an absolute `K>=0` such that (1.3) holds as

```math
c_E\sqrt{n_r}\le a_r+K
\tag{3.1}
```

for every component.  Then

```math
\begin{aligned}
c_E^2\sum_r n_r
&\le\sum_r(a_r+K)^2\\
&=\sum_r a_r^2+2K\sum_ra_r+K^2c_I\\
&\le\left(\sum_ra_r\right)^2
+2K\sum_ra_r+K^2c_I.
\end{aligned}
\tag{3.2}
```

There is no dangerous `K c_I` term inside one global square.  This is why a linear
number of singleton unloaded components does not alter the leading constant.

C36's noncrossing attachment incidence theorem gives in particular `c_I<=q`, and
loaded vertices are unit-separated around the convex force hull, so

```math
q\le\operatorname{per}F\le\pi D.
```

Thus `c_I=O(D)`.  If `mu_D` is bounded, (1.5) gives `sum a_r=O(D)`, and (3.2) has only
one quadratic term:

```math
\sum_rn_r
\le
\frac{2}{\pi\sqrt3}\mu_D^2D^2+O(D).
\tag{3.3}
```

Adding the `q=O(D)` loaded vertices proves (1.6).

---

## 4. Quantitative near-frontier consequences

For orientation,

```math
\frac4{\pi^2}=0.4052847345\ldots .
```

Hence:

- if `mu_D<=0.5947+o(1)`, then
  
  ```math
  \frac vn\le0.1433362780+o(1),
  \qquad
  \frac{n-v}{n}\ge0.8566637220-o(1);
  ```

- if `mu_D<=0.60+o(1)`, then
  
  ```math
  \frac vn\le0.1459025040+o(1),
  \qquad
  \frac{n-v}{n}\ge0.8540974960-o(1);
  ```

- if `mu_D<=\pi/(2\sqrt2)+o(1)`, at least half of the source is rattlers.

The first bullet is a formal endpoint-window calculation, not an assertion that GR
allows `mu=0.5947`: GR proves a fixed positive gap above that value.

---

## 5. Why this is stronger than componentwise Oler

The Oler-only estimate charges `n_r` by `delta_r^2`.  Eppstein Theorem 4 uses the
**edge count** as well.  Because the exact ZK slack writes

```math
e_r=2n_r-\delta_r-2-r_r,
```

Eppstein's square-root edge deficit is paid by

```math
\delta_r+r_r,
```

not by `delta_r` alone.  This is precisely the component part of the GR currency.

The gain in the leading core-population coefficient is from

```math
\frac\pi{2\sqrt3}=0.906899\ldots
```

to

```math
\frac2{\pi\sqrt3}=0.367552\ldots .
```

No unproved quantitative conductance, rigidity, or geometric-spreading statement is
inserted.

---

## 6. Interaction with the outer-shell frontier

ER turns a low-`mu` source into a much more extreme force-bulk normal form.  At
`mu≈0.6`, fewer than 15% of the source points are in the positive contact/KKT core;
more than 85% are C65 fully inactive rattlers.

C52 absorbs bounded-face rattlers against bounded-face area and leaves the outer
contact face as the sole invisible-population obligation.  Therefore any low-`mu`
survivor must realize an **order-`n` outer-shell rattler population**, not merely a
linear or lower-order exceptional set.

This does not by itself close C52.  A translated near-triangular filling of an outer
region can approach optimal density while keeping all its mutual separations strictly
above one.  Thus leading-density estimates still do not remove the Oler boundary
allowance.  A closing theorem must use either:

- source-specific global optimality to rearrange that huge inactive population and
  obtain a strict sub-`D` competitor; or
- an exact boundary-order packing deficit for the C52 outer contact face.

ER makes this the dominant low-`mu` obstruction.

---

## 7. Regression audit

### 7.1 Singleton components

For a singleton `I_r`, `a_r=delta_r+r_r=0`.  The uniform constant `K` in (3.1)
absorbs it.  Since `c_I=O(D)`, even `Theta(D)` singleton components contribute only
`O(D)` vertices and do not affect ER.1.

### 7.2 Square-grid / near-rhombic components

These are the correct near-extremal triangle-free contact regressions.  They have edge
deficit of order `sqrt(n)`, so Eppstein's theorem charges exactly the same scale as
`delta+r`.  ER does not falsely force a density gap independent of component diameter.

### 7.3 Folded paths

A path has large `delta` and therefore large `a_r`; ER becomes weak, as it should.
No Euclidean-diameter lower bound is inferred from graph diameter.

### 7.4 Regular odd shell plus dense isolated filling

The shell has only `O(D)` positive vertices and can coexist, absent a global-optimality
certificate, with `Theta(D^2)` isolated points.  ER permits that structure.  What ER
adds is that a genuine global survivor with low `mu` would be quantitatively forced
into an even stronger version of the same invisible-population phase.

### 7.5 Exact use of global optimality

The component bound (1.6) itself needs no global minimality beyond the post-ZF theorem
stack.  **Global optimality enters decisively only when converting it into the source
fraction ER.1**, through

```math
n/D(n)^2\to\pi/(2\sqrt3).
```

Dense shell-plus-isolate constructions without a certificate for `D=D(n)` do not have
this implication available.

---

## 8. Failed closure recorded

Even an `85%` rattler fraction does not by itself contradict global minimality.  The
rattlers can, at the level of leading asymptotics, fill the force-hull gaps and the
region between the force hull and full source hull at near-triangular density.  Splitting
Oler over those regions reintroduces an internal boundary term of order `D`, exactly
the scale at which the global contradiction lives.

Therefore the implication

```text
many rattlers -> insufficient leading-order area -> contradiction
```

is false.  The missing theorem is boundary-order or finite-rearrangement, not another
leading-density estimate.

---

## 9. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Eppstein Theorem 4 import | literature import, audited | primary repository text checked; exact coefficient and absolute `O(1)` |
| component inequality (1.3) | proved | compare Eppstein Theorem 4 with exact ZK definition of `r_r` |
| force-core bound (1.6) | proved | square-and-sum with absolute component constant |
| source-ratio ER.1 | proved | global-minimizer density asymptotic |
| `85.66%` near-0.5947 rattler obligation | proved as a window implication | direct substitution into ER.2 |
| outer-shell contradiction | not proved | boundary-order allowance survives |
| Level I | still open | high-`mu` defect phase and low-`mu` outer-shell phase remain |

---

## 10. Exact remaining implication

For any fixed `u>0.5947`, Target C now has the explicit dichotomy

```math
\boxed{
\mu_D>u
\quad\text{or}\quad
\frac{|R|}{n}
\ge1-\frac{4u^2}{\pi^2}-o(1).
}
\tag{10.1}
```

For `u=0.60`, the second branch means at least `85.4%` fully inactive rattlers.

A complete C-II closure can therefore come from a theorem that simultaneously:

1. excludes `mu_D>u` using Woodall/attachment/face geometry; and
2. excludes an outer-shell rattler fraction
   `1-4u^2/pi^2` by a source-specific packing/rearrangement theorem.

Alternatively, either branch may be eliminated by an independent strict sub-`D`
competitor construction.

---

## 11. Promotion recommendation

**Promote after independent audit.**

ER supersedes the preceding componentwise-Oler report for population estimates but does
not supersede its elementary finite bound.  The Eppstein paper is already a primary
repository dependency; no new source file is needed.

---

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

Eppstein 2018 Theorem 4:
    e <= 2N - c_E sqrt(N) + O(1),
    c_E=sqrt(pi sqrt(3)/2).

For unloaded component I_r, ZK gives exactly
    e_r=2n_r-(delta_r+r_r)-2.
Hence
    c_E sqrt(n_r) <= delta_r+r_r+O(1).

Square and sum componentwise. Because c_I=O(D), the absolute O(1) per component
is lower order. GR gives
    sum_r(delta_r+r_r) <= mu_D D+6.
Therefore
    v/D^2 <= [2/(pi sqrt3)] mu^2+o(1).

Global minimizers have
    n/D^2 -> pi/(2sqrt3),
so
    v/n <= (4/pi^2)mu^2+o(1),
    rattler fraction >=1-(4/pi^2)mu^2-o(1).

At mu=0.5947 this is:
    core <=14.3337% of source,
    rattlers >=85.6663%.
At mu=0.60:
    rattlers >=85.4097%.

This sharpens the low-surplus C-II normal form but does not remove the outer-shell
boundary allowance. The remaining dichotomy is high mu versus an order-n outer-shell
rattler population.
```
