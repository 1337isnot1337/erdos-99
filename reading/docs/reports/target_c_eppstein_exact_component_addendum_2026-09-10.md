> Generated reading edition · [exact source](../../../docs/reports/target_c_eppstein_exact_component_addendum_2026-09-10.md) · source SHA-256 `d5f1bec0e9a9e6071e47c667e3bc2a93c0d0e9a6a5b59ec3b364c12e425abd7b`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 2 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- theorem-state: {"artifact_id":"ART-485E00180639","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — exact Eppstein component-population addendum

**Date:** 2026-09-10  
**Repository branch:** `research/c2-general-mu05947-20260910`  
**Run type:** adversarial repair / exact strengthening  
**Target:** Target C force-bulk population  
**Depends on:** ZK/GR component definitions; Eppstein 2018 Lemmas 3--5 as stored in `extracted/text/463.txt`  
**Computation:** none

## LEVEL I STATUS

`STILL OPEN`.

This addendum strengthens the preceding Eppstein rattler-fraction report in two ways:

1. it derives the component population bound directly from Eppstein's geometric proof,
   so no opaque `O(1)` theorem term has to be summed over components; and
2. it retains the loaded contact-degree slack `s_B` instead of discarding it.

Let

```math
a_r:=\delta_r+r_r,
\qquad
A:=\sum_r a_r.
```

For every non-singleton unloaded component `I_r`,

```math
\boxed{
 n_r
 \le
 2a_r+
 \frac{2}{\pi\sqrt3}a_r^2.
}
\tag{EA.1}
```

If `c_1` is the number of singleton unloaded components, then

```math
\boxed{
 v
 \le
 q+c_1+2A+
 \frac{2}{\pi\sqrt3}A^2.
}
\tag{EA.2}
```

ZK/GR gives the exact currency split

```math
A+s_B=\mu_DD+6,
\tag{EA.3}
```

and `q,c_1=O(D)`.  Therefore, if

```math
\mu_D\to\mu,
\qquad
\frac{s_B}{D}\to\sigma_B,
```

then

```math
\boxed{
\limsup\frac v{D^2}
\le
\frac{2}{\pi\sqrt3}(\mu-\sigma_B)^2,
}
\tag{EA.4}
```

and global optimality converts this to

```math
\boxed{
\limsup\frac vn
\le
\frac4{\pi^2}(\mu-\sigma_B)^2.
}
\tag{EA.5}
```

Thus loaded degree slack is pure boundary currency: it makes `mu` larger but cannot
support a quadratic positive-core population.  Any force-bulk argument should use
`mu-s_B/D`, not `mu`, as the component-population parameter.

---

## 1. Exact outer-face incidence inequality

Fix a connected non-singleton unloaded component `I_r`, with `n=n_r` vertices and
`e=e_r` unit-contact edges.  Let `k` be the number of vertex-face incidences on its
outer face, counted with multiplicity.

Eppstein Lemma 3 states that every vertex not on the outer face has Voronoi-cell area at
least `2sqrt(3)` in the normalization of unit-radius tangent circles.  If `n>k`, at
least `n-k` vertices are not on the outer face, because the number of distinct outer
vertices is at most the incidence count `k`.  Their disjoint Voronoi cells are enclosed
by the outer-face curve, so that curve encloses area at least

```math
2\sqrt3(n-k).
```

Eppstein's proof of Lemma 4 observes that each outer-face incidence contributes exactly
two units of length to this curve.  Its length is therefore `2k`.  Isoperimetry gives

```math
(2k)^2
\ge
4\pi\,2\sqrt3(n-k),
```

or

```math
\boxed{k^2\ge2\pi\sqrt3(n-k).}
\tag{1.1}
```

If `n<=k`, the inequality needed below is already automatic.  Combining the two cases
we obtain the exact finite estimate

```math
\boxed{
 n\le k+\frac{k^2}{2\pi\sqrt3}.
}
\tag{1.2}
```

No asymptotic notation occurs in (1.2).

---

## 2. Exact face deficit equals the ZK component currency

Because `I_r` is a connected triangle-free plane graph, let `Q_r` be the sum of
`deg(f)-4` over its bounded faces.  Euler and double-counting face incidences give

```math
 e=2n-2-\frac{k+Q_r}{2}.
\tag{2.1}
```

On the other hand the ZK/Eppstein slack definition is

```math
 e=2n-\delta_r-2-r_r
   =2n-a_r-2.
\tag{2.2}
```

Comparing (2.1) and (2.2) yields the useful exact identity

```math
\boxed{
 a_r=\delta_r+r_r=\frac{k+Q_r}{2}.
}
\tag{EA.6}
```

In particular

```math
\boxed{k\le2a_r.}
\tag{2.3}
```

Insert (2.3) into (1.2).  The right side is increasing in `k>=0`, so

```math
 n_r
 \le
 2a_r+
 \frac{(2a_r)^2}{2\pi\sqrt3}
 =
 2a_r+
 \frac{2}{\pi\sqrt3}a_r^2.
```

This proves EA.1.

For a singleton component, `a_r=0` while `n_r=1`; this is the sole reason for the
separate `c_1` term in EA.2.

---

## 3. Sum components without losing the loaded slack

The positive core is

```math
v=q+\sum_rn_r.
```

Apply EA.1 to non-singletons and add the `c_1` singleton vertices:

```math
\begin{aligned}
v
&\le
q+c_1+2\sum_ra_r
+\frac{2}{\pi\sqrt3}\sum_ra_r^2\\
&\le
q+c_1+2A
+\frac{2}{\pi\sqrt3}A^2,
\end{aligned}
```

because all `a_r>=0`.  This is EA.2.

The exact ZK identity is

```math
A+s_B
=
\sum_r(\delta_r+r_r)+s_B
=\mu_DD+6.
```

Therefore

```math
\frac AD
=
\mu_D-\frac{s_B}{D}+O(D^{-1}).
\tag{3.1}
```

Loaded vertices satisfy `q<=per(F)<=pi D`.  The singleton count is at most the total
component count, and C36 gives `c_I=O(D)`.  Divide EA.2 by `D^2` and use (3.1) to prove
EA.4.

Finally global minimizers satisfy

```math
\frac n{D^2}\to\frac\pi{2\sqrt3},
```

so division proves EA.5.

---

## 4. Inverted force-bulk obligation

EA.5 can be inverted.  If

```math
\frac vn\to\eta>0,
```

then every convergent subsequence obeys

```math
\boxed{
\mu-\sigma_B
\ge
\frac\pi2\sqrt\eta.
}
\tag{EA.7}
```

Thus a positive-density force core has a quantitative component-topology cost before
any loaded-degree slack is counted.

Examples:

- `eta=1` requires `mu-sigma_B>=pi/2`;
- `eta=1/2` requires `mu-sigma_B>=pi/(2sqrt2)`;
- `eta=1/4` requires `mu-sigma_B>=pi/4`.

This is not a contradiction because no universal upper bound of these sizes is known.
It is a sharper phase discriminator for any future Woodall/outer-pocket upper theorem.

---

## 5. Audit and regressions

### 5.1 Scale normalization

Eppstein draws unit-radius circles, so contact centers are distance two.  Scaling the
representation by `1/2` changes neither the graph, its outer-face incidence count, nor
any combinatorial inequality.  The coefficient in EA.1 is therefore unchanged.

### 5.2 Bridges and repeated outer-face incidences

The argument uses outer-face incidences **with multiplicity**, exactly Eppstein's
notation.  It does not assume `I_r` is 2-connected.  Bridges are traversed twice and
are automatically counted in `k`.

### 5.3 Singleton components

They are separated explicitly as `c_1`; no false inequality `1<=0` is applied to them.
Since `c_1<=c_I=O(D)`, they do not alter the quadratic source-scale coefficient.

### 5.4 Square-grid / rhombic regression

For a large square-grid-type component, `a_r` is boundary order and EA.1 is of the
correct quadratic form.  The theorem does not create a leading density gap for
near-60-degree rhombic packings.

### 5.5 Folded-path regression

A path has large `a_r`, so EA.1 is weak.  No Euclidean spreading is inferred from
contact-graph diameter.

### 5.6 Global-optimality use

EA.1--EA.4 are structural statements about the post-ZF core.  Global minimality is
used decisively in EA.5 only through the source density asymptotic
`n/D(n)^2->pi/(2sqrt3)`.  Dense isolate regressions without a global-optimality
certificate cannot invoke that conversion.

---

## 6. Effect on the C-II frontier

The low-`mu` force-bulk normal form is now

```math
\boxed{
\frac vn
\le
\frac4{\pi^2}
\left(\mu-\frac{s_B}{D}\right)^2+o(1).
}
```

At the GR scale, taking `s_B=0` already gives the `85.66%` rattler obligation from the
preceding report.  Any positive linear loaded slack makes the positive core even
smaller.

This identifies a sharper source of a future contradiction: a high-density positive
core and a large loaded-degree deficit cannot coexist at low `mu`.  Conversely, if
`mu` stays near the GR floor, the source is forced into an overwhelmingly inactive
outer-shell phase.

---

## 7. Claim classification

| Claim | Classification | Reason |
| --- | --- | --- |
| exact incidence bound (1.2) | proved from Eppstein Lemmas 3--4 | separate `n<=k` case handles no-interior regime |
| exact face identity EA.6 | proved | Euler + ZK definition |
| component population EA.1 | proved | monotone substitution `k<=2a_r` |
| finite core bound EA.2 | proved | component summation |
| retained-slack asymptotic EA.4/EA.5 | proved | exact ZK split + lower-order `q,c_1` |
| inverted obligation EA.7 | proved | algebraic inversion |
| Level I | still open | no matching upper theorem on `mu-sigma_B` / outer-shell population |

---

## 8. Exact remaining implication

For any fixed `u>0.5947`, a C-II closure can now target the two-dimensional phase
variables

```math
\left(\mu,\sigma_B\right),
\qquad
\sigma_B:=s_B/D.
```

If an independent topology theorem forces

```math
\mu-\sigma_B\le w,
```

then EA.5 forces at least

```math
1-4w^2/\pi^2
```

of the whole source into C65 rattlers.  If instead the force core has density at least
`eta`, EA.7 forces

```math
\mu\ge\sigma_B+\frac\pi2\sqrt\eta.
```

The missing step is still an outer-shell packing/rearrangement theorem or a global
upper tradeoff from Woodall/attachment geometry.

---

## 9. Promotion recommendation

**Prefer this exact addendum over the `O(1)` proof in the preceding ER report when
promoting the force-bulk theorem.**  The source-ratio constant is unchanged, but the
finite statement and the retained `s_B` dependence are stronger.
