> Generated reading edition · [exact source](../../../docs/audits/target_c_october_structural_promotion_audit_2026-10-05.md) · source SHA-256 `34234892e5ae2d41b421cff8050d34a5a7463cc3a88500eee55f53cb0eb931cc`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-6E34E9088A01","canonical":true,"claim_ids":["C-AUGMENTED-TRAIN-RANK","C-CONTACT-FACE-REGULARITY","C-FULLCORE-HULL-DEPLETION-FLOOR","C-FULLCORE-RESIDUAL-FLOOR"],"claim_statuses":{"C-AUGMENTED-TRAIN-RANK":"canonical","C-CONTACT-FACE-REGULARITY":"canonical","C-FULLCORE-HULL-DEPLETION-FLOOR":"canonical","C-FULLCORE-RESIDUAL-FLOOR":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Independent promotion audit — October Target C structural stack

**Date:** 2026-10-05  
**Audit base:** \`fbc8f64cf2bb66a0fe2f43f46a3bb24b763cc220\`  
**State consulted:** \`2026-09-14.audit.51\`  
**Target:** C-II / full-core structural reduction  
**Verdict:** **PASS for canonical promotion of the four exact claims below.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

This audit promotes only four claims:

1. \`C-FULLCORE-HULL-DEPLETION-FLOOR\`;
2. \`C-AUGMENTED-TRAIN-RANK\`;
3. \`C-FULLCORE-RESIDUAL-FLOOR\`;
4. \`C-CONTACT-FACE-REGULARITY\`.

It does **not** promote every October 5 report, any activation theorem, any strict-diameter competitor, the terminal pentagon branches, the wall-refill heuristics, or the macroscopic inactive-container branch.

## 1. Full-core hull-train depletion floor

Audited source:
\`docs/reports/target_c_fullcore_hull_train_depletion_floor_2026-10-04.md\`.

The earlier independent audit
\`docs/audits/target_c_fullcore_hull_train_depletion_floor_independent_audit_2026-10-04.md\`
was reread against the current canonical Sections 61, 63, 68, 69, 75, 76 and the promoted loaded-hull/full-core stack. Its proof survives unchanged.

For every unbounded canonical full-core Type-II sequence, put

```math
\Delta_2=\frac{\pi}{2\sqrt3},\qquad
s=\sqrt{\Delta_2},\qquad
\mu_{\rm hull}=\frac{\pi+s}{2}.
```

The finite good-hull occurrence identity, phase depletion, and Mantel step give

```math
\liminf\left(5t_D+\frac{x_B+m_B}{D}\right)\ge3\pi+2s,
```

```math
\liminf\left(4\mu_D-\frac{k+3m_B}{D}\right)\ge2\pi+2s,
```

hence

```math
\boxed{\liminf\mu_D\ge\mu_{\rm hull}
=2.046952730226875\ldots.}
```

The endpoint $`\mu_D\to\mu_{\rm hull}`$ is impossible. Therefore there are $`\varepsilon_*>0`$ and $`D_*>0`$ such that every sufficiently large canonical full-core Type-II source satisfies

```math
\mu_D\ge\mu_{\rm hull}+\varepsilon_*.
```

No effective value of $`\varepsilon_*`$ is claimed.

### Load-bearing checks

The audit rechecked:

- the distinguished outer-occurrence lemma in the presence of bridges and repeated outer-walk vertices;
- $`B_{\rm bad}=x_B+m_B`$, not merely an upper bound;
- the exact identity
  
  ```math
  4\mu_DD+8c_I+18-2b-M_D-k-3m_B
  =2(Q-f)+2-d_D;
  ```

- the all-hull-side directional count from near-disk radial parametrization;
- the order of limits: fixed phase width first, source limit second, width to zero last;
- heredity of the endpoint pseudosegment/phase argument after restriction to the remaining actual trains.

The exact verifier was rerun independently and passed 383 source packets and 183,212 depletion/slack ledgers, certifying the displayed finite bookkeeping and the numerical floor interval.

**Verdict:** canonical-ready.

## 2. Augmented internal stopped-train columns

Audited source:
\`docs/reports/target_c_augmented_train_phase_rank_small_residual_exclusion_2026-10-05.md\`,
Lemma AR.2.

Augment the positive-contact core by every missing force-hull side. Make one bounded node for every physical nonquadrilateral contact face and every new hull pocket. An internal stopped train joins two bounded augmented nodes. Its angular closure column has blocks $`Jw,-Jw`$.

The claim is:

```math
\boxed{\text{all internal augmented stopped-train columns are linearly independent}.}
```

Consequently, for every nonempty bounded augmented node set $`U`$,

```math
\boxed{e(U)\le2|U|-2.}
```

### Independence proof audit

Assume a nonzero linear dependence. Give every actual contact edge of a train $`\tau`$ displacement $`Jw\,\omega_\tau`$, every added hull side displacement zero, and every outside-ended train rate zero.

- Strict-rhombus face closure is automatic because opposite sides lie on one stopped train with opposite vectors.
- Exceptional physical faces close by the assumed column relation.
- Every hull pocket, including a four-sided pocket with a nonunit added chord, closes because it is retained as an augmented face row.
- Bounded augmented face cycles span the cycle space of the connected augmented graph, so the edge displacements integrate to vertex velocities.
- Every consecutive loaded hull pair has equal velocity: unit hull contacts have zero rate and added hull sides have zero displacement.
- After subtracting this common translation, every loaded vertex is fixed. All active diameter endpoints are loaded, so every active diameter bar is fixed.
- Canonical Section 57 mixed rigidity on the nonisolated positive-contact core forces the velocity field to be Euclidean. Two distinct fixed loaded vertices kill that Euclidean motion.

Therefore every contact-edge angular rate is zero, contradicting the assumed nonzero dependence.

This argument never treats an auxiliary hull side as a source constraint and never extends the affine-kernel theorem to contact isolates.

The two coordinate-sum row dependencies on any restricted node set give the $`(2,2)`$-sparsity inequality above.

The two exact augmented-rank verifiers were rerun independently. They passed 5,436 rational unit-pair checks, 3,114 augmented node-subset checks, 128,685 phase-bank ledgers, and an actual six-point loaded KKT packet with all 31 nonempty node subsets.

**Verdict:** canonical-ready.

## 3. Exact residual conservation and Groemer stability

The residual theorem below uses two intermediate facts that were previously proof-only. They are audited here inside the promoted theorem rather than assigned separate theorem IDs.

### 3.1 Residual conservation

For every augmented inactive chamber $`C`$, put

```math
r_C=\frac{A_C}{a_0}+\frac{P_C}{2}+1-z_C-k_C\ge0,
\qquad a_0=\frac{\sqrt3}{2}.
```

Using the exact Section-67 face, pocket, perimeter and population ledgers gives

```math
\boxed{
\sum_Cr_C
=
R_F
:=
\frac{A_F}{a_0}+\frac{P_F}{2}+1-N_F-\frac{E_4}{a_0}
\ge0.
}
```

The cancellation was rederived term by term. In particular, all assigned contact-isolated source points remain in $`N_F`$ and the chamber populations; no full-source rigidity statement is used.

### 3.2 Fixed-degree direction stability

For every fixed boundary-complexity cutoff $`K`$ and phase tolerance $`\eta>0`$, there is $`\sigma_K(\eta)>0`$ such that an augmented chamber with residual below $`\sigma_K(\eta)`$ has every unit boundary-path direction within $`\eta`$ modulo $`\pi/3`$ of its distinguished hull chord/reference edge.

The compactness proof is valid. At residual zero, the normalized Oler equality case is either a segment or a convex hull triangulated by unit equilateral triangles using the source points. In both cases all boundary directions lie in one reduced triangular-lattice phase. The source statement was rechecked against Böröczky--Ruzsa's transcription of Groemer's equality theorem; their unit-disc normalization rescales to unit-separated centers exactly.

No equality uniqueness beyond that classification is used.

## 4. Full-core residual floor

With the augmented-column theorem, the phase bank satisfies

```math
\boxed{N_j\le10|H|+4E_j}
```

for every shifted reduced-phase bin.

Here $`H`$ is the set of bad augmented chamber nodes, while $`E_j`$ counts actual unit-hull terminals and bounded good-pocket terminal occurrences in the bin. Large face/pocket terminal multiplicity is not silently discarded: bad nodes are paid by rank through $`|H|`$, and good pocket multiplicity is bounded by the fixed cutoff.

The parameter order is valid:

1. choose fixed degree/path cutoffs $`M,L`$;
2. choose fixed equal-circle bin width $`\epsilon`$;
3. choose fixed Groemer tolerance $`\eta`$;
4. take $`D\to\infty`$;
5. finally let the target error tend to zero through the preceding fixed choices.

Under $`R_F=o(D)`$, residual conservation makes the direction-bad bounded-complexity nodes $`o(D)`$. The promoted all-hull-side directional count controls $`E_j`$. Hence $`\max_jN_j=o(D)`$. Canonical Section 69 removes only $`O_\epsilon(D)`$ crossing edges; the simple train crossing graph then has $`o(D^2)`$ rhombi, contradicting the positive Type-II limit.

Thus:

```math
\boxed{\text{no canonical full-core Type-II sequence has }R_F/D\to0.}
```

The quantitative parameter choice in the source report further yields a universal, nonexplicit constant $`\kappa_{\rm fr}>0`$ such that every canonical full-core Type-II sequence satisfies

```math
\boxed{\liminf\frac{R_F}{D}\ge\kappa_{\rm fr}>0.}
```

Equivalently, a surviving full-core sequence carries a linear bank of bounded-degree, bounded-pocket-complexity chambers with a fixed reduced-phase mismatch. This is a structural residual floor, not contact activation and not a source replacement.

**Verdict:** canonical-ready.

## 5. Complete exceptional-face elimination and contact regularity

Audited source:
\`docs/reports/target_c_complete_face_elimination_and_contact_regularity_2026-10-05.md\`.

Let $`f`$ be the number of bounded physical nonquadrilateral contact faces and $`C_{\rm face}`$ the stopped-train angular closure matrix on those physical faces.

The promoted statement is

```math
\boxed{
\operatorname{rank}C_{\rm face}=2f,\qquad
\operatorname{rank}R_C=e,\qquad
\sigma_C=0.
}
```

### 5.1 Strict convexity

Canonical Section 67 already gives convex bounded augmented faces. At a loaded hull vertex, a bounded physical face sector lies in a strict convex-hull tangent cone and has angle $`<\pi`$. At an unloaded vertex, a flat $`\pi`$-sector would put every positive contact ray into one closed half-plane; the positive equilibrium equation then forces every ray onto its boundary line, contradicting contact degree at least three. Thus every bounded physical contact face is strictly convex.

A projective side direction occurs at most twice on such a face.

For a physical unit pentagon, no projectively parallel side pair is possible: opposite parallel unit side vectors would leave three unit side vectors summing to zero, hence spaced by $`2\pi/3`$. Two additional antipodal directions can occupy at most two of the three intervening arcs, so one $`2\pi/3`$ exterior turn is consecutive. The corresponding interior angle is $`\pi/3`$, creating a unit contact chord and contradicting that the pentagon is a face of the complete contact graph.

### 5.2 Two-anchor elimination

For every nonempty set $`U`$ of physical exceptional faces, canonical \`C-AUGMENTED-TRAIN-RANK\` gives

```math
e(U)\le2|U|-2.
```

Hence one face $`F\in U`$ has internal train degree at most three.

- If $`\deg F=5`$, at least two terminal trains leave $`U`$, and the pentagon lemma makes them nonparallel.
- If $`\deg F\ge6`$, at least three terminal trains leave $`U`$; because one projective direction can occur at most twice, two are nonparallel.

Remove $`F`$ and repeat. A terminal outside $`U`$ is either a ground/outside or pocket terminal, or a physical face removed earlier. Selecting the two nonparallel terminal columns at each step produces a block-triangular pivot matrix with invertible $`2\times2`$ diagonal blocks. No pivot train is reused.

Therefore $`\operatorname{rank}C_{\rm face}=2f`$.

The exact train-angle/contact-flex correspondence and Euler identities then give

```math
e-\operatorname{rank}R_C
=
2f-\operatorname{rank}C_{\rm face}=0,
```

so every contact row is independent.

### 5.3 Contact manifold

By the implicit-function theorem, the exact unit-contact realization space of the nonisolated core is a smooth manifold of dimension

```math
2v-e=q-k+2.
```

After fixing translation, the stopped-train angle chart has dimension $`q-k`$; modulo core Euclidean motions it has dimension $`q-k-1`$.

Contact-isolated source points are retained at their original coordinates. Initially strict lower constraints and inactive upper constraints persist in a sufficiently small source-dependent neighborhood. Active diameter feasibility is **not** supplied by this theorem.

The exact stress-energy identity for any labelled realization preserving all original contact lengths is

```math
\sum_{h\in H}\beta_h|p'_i-p'_j|^2
=
D^2-\sum_{c=1}^2\delta_c^T\Omega\delta_c.
```

It controls the weighted active-diameter mean, not the maximum diameter.

The exact verifier was rerun independently and passed 31,549 $`(2,2)`$-sparse endpoint graphs, 94,647 mixed-valence elimination orders, positive pentagon/hexagon packets, the triangle-containing wheel regression, and both weighted-mean failure modes.

**Verdict:** canonical-ready.

## 6. Regression and scope audit

The promoted stack respects all binding Target C corrections.

- No contact-isolated source point is deleted or given a false affine-kernel coordinate.
- No incident-diameter ordering is turned into an Euler path.
- No RSR disk-equality uniqueness is used.
- No phase coarea deletion is interpreted as deleting source constraints.
- No near-unit chord is treated as an active contact.
- No positive residual is treated as positive KKT activation.
- No weighted mean contraction is treated as contraction of every diameter pair.
- No source-uniform contact-chart radius is asserted.
- The macroscopic-container branch is untouched.

The large near-triangular fixed-wall regression remains binding: quadratic population, positive pinned equilibrium and near-triangular geometry do not alone imply a strict same-cardinality fixed-wall refill.

## 7. Canonical frontier after promotion

The full-core Type-II branch now has all of the following canonical facts:

```math
\mu_D\ge
\frac{\pi+\sqrt{\pi/(2\sqrt3)}}2+\varepsilon_*
```

for all sufficiently large canonical full-core sources, for some nonexplicit $`\varepsilon_*>0`$;

```math
\liminf R_F/D\ge\kappa_{\rm fr}>0;
```

and

```math
\sigma_C=0,\qquad \operatorname{rank}R_C=e.
```

Therefore a surviving full-core source cannot escape by becoming asymptotically Groemer-tight, by hiding residual only in unbounded face/pocket tails, or by retaining a stalled pure-contact closure core.

The remaining source-level obstruction is active-diameter feasibility: spend the linear direction-frustrated residual/contact-manifold freedom to produce either an exact unit equilateral triangle or a same-cardinality feasible source of diameter strictly below $`D`$. The canonical aggregate-detour/loaded-hull package remains available as a second global currency.

The separate macroscopic inactive-container branch remains open.

**Promotion recommendation:** advance theorem state to \`2026-10-05.audit.52\` and register the four claims above as canonical.
