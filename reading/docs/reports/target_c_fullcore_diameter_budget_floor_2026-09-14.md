> Generated reading edition · [exact source](../../../docs/reports/target_c_fullcore_diameter_budget_floor_2026-09-14.md) · source SHA-256 `1f521274ad9391b7960011649c7e9134ea8ae0d684addedb967388d9bb22dc9b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-F5F4B09FCFA3","canonical":true,"claim_ids":["C-FULLCORE-DIAMETER-BUDGET-FLOOR"],"claim_statuses":{"C-FULLCORE-DIAMETER-BUDGET-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C-II full-core diameter-budget floor — 2026-09-14

Status: `LEVEL I STATUS: STILL OPEN`
Classification: canonical theorem `C-FULLCORE-DIAMETER-BUDGET-FLOOR`, promoted in
state `2026-09-14.audit.49` after the independent audit cited below. The stronger
train-coupled floor is now the live numerical endpoint in the same branch.

## 1. Purpose and exact endpoint

This report isolates a source-level consequence of the canonical full-core branch
that is independent of the numerical carrier coefficient.  It does not solve
Erdős Problem #99.  Its endpoint is the following asymptotic exclusion:

> In the canonical full-core, no-macroscopic-container branch, any sequence of
> triangle-free contact-minimal representatives satisfies
> 

$$

> \liminf_{D\to\infty}
> \frac{e_{BB}+2s_C-3k}{D}\ge 1,
> \qquad k=d_H+s_Z.
> 
$$



Here (D) is the diameter of the representative, (e_{BB}), (s_C), (d_H),
and (s_Z) have exactly the meanings in the canonical Target C-II attachment
currency, component-deatomization, and loaded-hull ledgers.  The source is the
full original configuration when the canonical branch hypotheses invoke it;
the polygons (P_r) below are only the attachment-cell convex hulls and are not
being substituted for the source.

The result eliminates every full-core sequence with a subunit limiting value of
the displayed scalar.  It supplies no upper bound on that scalar, so it does not
eliminate the remaining $\mu\ge1$ full-core regime and does not address the
macroscopic-container/exterior-cap branch.

## 2. Abstract large-cell lemma

Let $D_j\to\infty$.  For each $j$, let $P_{r,j}$ be finitely many convex
polygons (degenerate polygons are allowed), with


$$
 \sum_r \operatorname{area}(P_{r,j})
     \ge \alpha D_j^2-o(D_j^2),
 \qquad
 \sum_r \sqrt{\operatorname{area}(P_{r,j})}
     \le C D_j,
\tag{2.1}
$$

for fixed $\alpha>0$ and $C<\infty$.  Write

$$
 a_{r,j}=\operatorname{area}(P_{r,j}),
 \quad d_{r,j}=\operatorname{diam}(P_{r,j}),
 \quad d_{r,j}\le \delta_{r,j}+b,
\tag{2.2}
$$

with fixed $b<\infty$, and suppose that the exact budget inequality

$$
 \sum_r\delta_{r,j}\le 6+\mu_jD_j
\tag{2.3}
$$

holds.  Then

$$
 \liminf_{j\to\infty}\mu_j
 \ge 2\sqrt{\frac{\alpha}{\pi}}.
\tag{2.4}
$$

### Proof

Fix $0<\eta<\alpha^2/(4C^2)$, and call $r$ large when

$$
 a_{r,j}\ge \eta D_j^2.
$$

The complementary small cells satisfy

$$
 \sum_{r\ {\rm small}}a_{r,j}
 \le \sqrt{\eta}\,D_j
       \sum_r\sqrt{a_{r,j}}
 \le C\sqrt{\eta}\,D_j^2.
\tag{2.5}
$$

Consequently, (2.1) gives

$$
 \sum_{r\ {\rm large}}a_{r,j}
 \ge (\alpha-C\sqrt\eta)D_j^2-o(D_j^2).
\tag{2.6}
$$

For every convex planar set, the isodiametric inequality gives

$$
 a_{r,j}\le \frac\pi4d_{r,j}^2.
$$

Therefore (2.6) implies

$$
 \sum_{r\ {\rm large}}d_{r,j}^2
 \ge \frac4\pi
       \left((\alpha-C\sqrt\eta)D_j^2-o(D_j^2)\right).
\tag{2.7}
$$

Since the (d_{r,j}) are nonnegative,

$$
 \sum_{r\ {\rm large}}d_{r,j}
 \ge \left(\sum_{r\ {\rm large}}d_{r,j}^2\right)^{1/2}.
\tag{2.8}
$$

The number of large cells is uniformly bounded for fixed (eta): indeed,

$$
 |\{r:a_{r,j}\ge\eta D_j^2\}|\sqrt\eta D_j
 \le \sum_r\sqrt{a_{r,j}}\le CD_j,
$$

so it is at most $C/\sqrt{\eta}$.  Combining (2.7)–(2.8), and then using
$d_{r,j}\le\delta_{r,j}+b$, gives

$$
 \begin{aligned}
 \sum_r\delta_{r,j}
 &\ge \sum_{r\ {\rm large}}\delta_{r,j}\\
 &\ge \sum_{r\ {\rm large}}d_{r,j}-b\,\frac C{\sqrt{\eta}}\\
 &\ge 2\sqrt{\frac{\alpha-C\sqrt{\eta}}{\pi}}\,D_j-o(D_j)-b\,\frac C{\sqrt{\eta}}.
 \end{aligned}
\tag{2.9}
$$

Insert (2.9) into the exact budget (2.3), divide by $D_j$, and let
$j\to\infty$.  For each fixed $\eta$,

$$
 \liminf_{j\to\infty}\mu_j
 \ge 2\sqrt{\frac{\alpha-C\sqrt{\eta}}{\pi}}.
$$

Finally let $\eta\downarrow0$.  This proves (2.4).  Notice that the fixed
additive term $bC/\sqrt{\eta}+6$ disappears only after $\eta$ is fixed and
$D_j\to\infty$; no uniform-in-$\eta$ assertion is being smuggled into the
argument.

## 3. Canonical Target C-II application

Take a sequence in the canonical full-core branch, with $D_j\to\infty$.  Let

$$
 P_{r,j}=\operatorname{conv}(A_{r,j}),
$$

where $A_{r,j}$ is the attachment set of the $r$-th unloaded positive-contact
component, with the canonical cell decomposition and occurrence conventions.
The following are canonical inputs, used only with their stated scopes.

1. Full-core near-disk saturation gives

   $$
   \operatorname{area}(F_j)=\frac\pi4D_j^2-o(D_j^2).
   $$

2. Canonical attachment-cell disjoint tiling gives

   $$
   \sum_r\operatorname{area}(P_{r,j})
     =\operatorname{area}(F_j)-o(D_j^2),
   \qquad
   \sum_r\sqrt{\operatorname{area}(P_{r,j})}=O(D_j).
   $$

   The first equality is the canonical full-core rhombic-saturation statement;
   it is not asserted for a Type-I chamber/cap branch.

3. The attachment-cell diameter conversion is

   $$
   d_{r,j}=\operatorname{diam}(P_{r,j})\le\delta_{r,j}+2.
   $$

   The (+2) is retained.  It is not discarded by claiming that boundary walks
   are simple or that bridges occur only once.

4. The exact attachment currency identity and nonnegativity of the residual
   terms give

   $$
   \sum_r\delta_{r,j}+R_{I,j}+s_{B,j}
     =6+e_{BB,j}+2s_{C,j}-3k_j.
   $$

Since $R_{I,j},s_{B,j}\ge0$, this implies

   $$
   \sum_r\delta_{r,j}
      \le6+\mu_jD_j,
   \qquad
   \mu_j:=\frac{e_{BB,j}+2s_{C,j}-3k_j}{D_j}.
   $$

Items 1 and 2 yield (2.1) with $\alpha=\pi/4$; items 3 and 4 yield (2.2)–
(2.3) with $b=2$.  The abstract lemma therefore gives

$$
 \boxed{\displaystyle
 \liminf_{j\to\infty}
 \frac{e_{BB,j}+2s_{C,j}-3k_j}{D_j}\ge1.}
\tag{3.1}
$$

This is a statement about the canonical source-derived ledger.  It does not
delete contact-isolated source points, and it does not extend the affine-kernel
theorem from the nonisolated core to the full source.

## 4. Exact implication for the live route

The chain is:

```text
full-core near-disk area + canonical cell square-root budget
    -> large cells carry almost all quadratic area
    -> isodiametric inequality forces total large-cell diameter >= D-o(D)
    -> d_r <= delta_r+2 and the exact attachment currency force mu >= 1
    -> every full-core sequence with liminf(mu)<1 is excluded.
```

This advances the source-level endpoint by removing the entire subunit-$\mu$
regime.  It does not give the missing implication

$$
 \mu\ge1
 \quad\Longrightarrow\quad
 \text{unit equilateral triangle or a source-preserving strict diameter decrease}.
$$

The Section-122 lower bound and Section-123 excess-payment estimate remain
compatible with $\mu\ge1$.  In particular, their scalar substitution does not
produce a sign contradiction.  The aggregate outer-walk detour and the loaded
diameter geometry are still unresolved.  The Type-I macroscopic inactive chamber
or exterior-cap branch is also untouched.

## 5. Adversarial regression audit

The argument was checked against the relevant regressions as follows.

* The abstract scalar compatibility witness has $\mu>1$ and positive detour.
  It therefore does not contradict (3.1); it demonstrates why the new lower
  bound is not already a closure.

* The square-grid harmonic attachment regression has a large
  $a_r-d_r$, but it lacks the canonical full-core near-disk area saturation and
  disjoint cell square-root budget.  It is not a counterexample to the lemma.

* The vanishing-shear full-core-looking finite family is an exact geometric
  regression, not a canonical global minimizer with the full attachment currency.
  It cannot be used to remove the (+2) term or to reverse (2.9).

* The strict saturated triangular chamber has quadratic population and an
  erosion covering, but it is a Type-I macroscopic container.  It lacks the
  full-core equality (operatorname{area}(F)=\pi D^2/4-o(D^2)) and the
  full-core attachment tiling, so (3.1) does not purport to constrain it.

* Contact-isolated points never enter (P_r), but they also never enter the
  asserted full-source affine-kernel theorem.  The proof uses only the canonical
  component currency, whose hypotheses already distinguish the core from the
  retained isolated source.

* Repeated boundary vertices and bridge occurrences do not affect the proof:
  only the canonical inequality (d_r\le\delta_r+2) and the exact currency
  identity are used.  No Euler-path simplification is made.

The proof uses no floating-point computation and imports no external theorem.
The only geometric input beyond the canonical route modules is the elementary
planar isodiametric inequality.

## 6. Proof-obligation ledger

### Canonical trusted inputs

* Full-core near-disk area asymptotic.
* Canonical attachment-cell disjoint tiling and
  (sum_r\sqrt{\operatorname{area}(P_r)}=O(D)).
* Exact attachment currency and (d_r\le\delta_r+2).

### New proved lemma

* The abstract large-cell/isodiametric budget lemma (Section 2), including the
  order of limits: fix the area threshold first, then send (D\to\infty), then
  send the threshold to zero.

### Exact consequence

* Full-core $\liminf\mu\ge1$, equation (3.1).

### Candidate or conditional claims

* None promoted from this report.  No claim that (mu\ge1) contradicts the
  current carrier/payment inequalities.

### Unresolved obligations

* Eliminate the full-core (mu\ge1) regime by an exact detour upper bound,
  source-preserving strict decrease, or forced unit equilateral triangle.
* Eliminate the Type-I macroscopic chamber/exterior-cap branch at the level of
  global minimizers.
* Cover all sufficiently large cardinalities and every global minimizer.

## 7. Promotion decision

The independent audit
[`target_c_fullcore_diameter_budget_floor_independent_audit_2026-09-14.md`](../audits/target_c_fullcore_diameter_budget_floor_independent_audit_2026-09-14.md)
verified the four hypotheses, the fixed-threshold order of limits, and the relevant
regression scopes. The theorem is promoted as
`C-FULLCORE-DIAMETER-BUDGET-FLOOR`. The promotion changes the machine manifest,
state version, generated views, current Target C frontier, and active Target C prompt;
it does not change the Level I or C-II status.
