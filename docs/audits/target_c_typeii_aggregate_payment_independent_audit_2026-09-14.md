<!-- theorem-state: {"artifact_id":"ART-34A7F8D6EB0B","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Independent audit — Type-II aggregate payment and inactive exchange

**Date:** 2026-09-14
**Repository commit:** ef941ab2b44aa393bdc461926769247b45754202
**State version:** 2026-09-12.audit.46
**Run type:** audit / closing-proof continuation
**Target:** C-II / Level I
**Audited artifact:** docs/reports/target_c_typeii_aggregate_payment_and_exchange_2026-09-14.md
**Active prompt:** docs/prompts/erdos_problem_99_TARGET_C_CURRENT_CONTINUATION_PROMPT.md
**External literature:** none imported
**Computation:** exact scalar certificates and finite route regressions

## Verdict

The Type-II aggregate-payment theorem is **audited-working at its stated scope**.
The finite inactive-exchange lemmas are also correct at their stated scope. Neither
result is canonical, neither closes C-II, and neither settles Level I.

The audit found no invalid step in the following repaired implication:

~~~
Type-II near-disk geometry
    -> no loaded-loaded interior chords
    -> exact cellwise missing-side payment
    -> aggregate upper bound with explicit negative credits
    -> necessary scalar inequality, but not a contradiction
~~~

The exact unresolved term is

~~~
2 Σᵣ (aᵣ − dᵣ)
~~~

where aᵣ is the attachment count and dᵣ is the attachment-cell diameter. No
proved sign or sufficiently small upper bound for this term is available.

## 1. Audited Type-II theorem

Use the canonical contact-minimal, then diameter-pair-minimal triangle-free global
minimizer, with all source points retained. In the full-core Type-II branch, let

- F = conv(B) be the loaded force hull;
- Iᵣ be an unloaded positive-contact component;
- Aᵣ ⊂ B, aᵣ = |Aᵣ|, and Pᵣ = conv(Aᵣ);
- dᵣ = diam(Pᵣ);
- Lᵣ be the occurrence-counted outer-face walk length of the induced graph on
  Iᵣ ∪ Aᵣ;
- P_exc,ᵣ be the total degree of bounded nonquadrilateral faces;
- Tᵣ, Qᵣ⁺ be the Section-123 triangular and augmented-degree-excess quantities;
- d_tile ≥ 0 be the global polygon-dissection deficit;
- M_miss = Σᵣ Mᵣ be the missing-side route defect; and
- C_∂ = Σᵣ cᵣ^∂ be the number of actual loaded-loaded attachment contacts that
  are sides of the corresponding attachment polygons.

Then, for all sufficiently large Type-II survivors,

~~~
Σᵣ (Lᵣ + P_exc,ᵣ − 2aᵣ)
    ≤ 10(e_BB − k − d_tile) − 4M_miss − 6C_∂,

Σᵣ (Lᵣ + P_exc,ᵣ − 2dᵣ)
    ≤ 10(e_BB − k − d_tile)
       + 2Σᵣ(aᵣ − dᵣ) − 4M_miss − 6C_∂,
~~~

with k = d_H + s_Z.

Combining this with canonical Section 122 gives only the necessary condition

~~~
liminf (1/D) [10(e_BB − k − d_tile)
              + 2Σᵣ(aᵣ − dᵣ)
              − 4M_miss − 6C_∂]
    ≥ (π/2)(2 − √3).
~~~

This is an audited-working theorem, not a canonical theorem-state entry.

## 2. Audit of the no-interior-chord reduction

Canonical C-FULLCORE-NEAR-DISK gives, after translation, a quantity δ(D)=o(D)
such that

~~~
B(0, D/2 − δ) ⊂ F ⊂ B(0, D/2 + δ).
~~~

Put r = D/2 − δ and R_plus = D/2 + δ. Let p,q be distinct loaded hull vertices
with |p−q|=1. Write p = a e and q = b f, where e,f are unit radial directions
and a,b ≥ r.

If γ is the smaller radial angle between e and f, then

~~~
1 = |p−q|²
  = (a−b)² + 2ab(1−cos γ)
  ≥ 4r² sin²(γ/2).
~~~

The antipodal case is impossible for large D, so

~~~
γ ≤ 2 asin(1/(2r)) = o(1).
~~~

For any supporting normal n at a boundary point x,

~~~
n·x ≥ r,       |x| ≤ R_plus,
~~~

so the angle between n and the radial direction of x is at most

~~~
β = acos(r/R_plus) = o(1).
~~~

Along the short convex-boundary arc from p to q, the supporting normals are
monotone and remain within the radial angular interval enlarged by β at each
end. More explicitly, if xy is one of its hull sides and n_xy is an outward
normal to that side, then n_xy·x = n_xy·y = h_F(n_xy) ≥ r. Both radial directions
of x and y are therefore within β of n_xy, so the directed tangent xy is within
β of the corresponding radial tangent direction. Since the radial directions on
the short arc lie in an interval of width γ, every directed hull-side vector on
this arc lies in an angular interval of width

~~~
τ = 2β + 2 asin(1/(2r)) = o(1).
~~~

If p,q were nonconsecutive hull vertices, this arc would contain at least two
hull sides v_i. Source separation gives |v_i| ≥ 1. Let
\(w=(q-p)/|q-p|\). The sum of vectors in a cone of angular width \(\tau<\pi/2\)
remains in that cone, so each \(v_i\) makes angle at most \(\tau\) with \(w\).
Therefore

~~~
1 = |q−p| = w·(q−p)
                  = Σᵢ w·v_i
                 ≥ 2 cos(τ) > 1
~~~

for all sufficiently large D, a contradiction. Thus every loaded-loaded unit
contact is a hull side. In the notation of canonical Section 63,

~~~
c_B = 0,       e_BB = q − m.
~~~

Since Aᵣ ⊂ B, every loaded-loaded contact whose endpoints lie in Aᵣ is also a
side of Pᵣ; there are no loaded interior chords inside any attachment cell.

This audit uses only the finite near-disk inclusion and convexity. It does not use
a source/scaffold identification, an affine-kernel statement on isolated points,
or a global boundary-occurrence simplification.

## 3. Audit of the cellwise ledger

For a fixed component, form Jᵣ⁺ by taking internal and unloaded-to-loaded contacts,
omitting loaded-loaded contacts, and adding every side of Pᵣ. Let
hᵣ = aᵣ − cᵣ^∂ be the number of missing polygon sides.

Partition the augmented degree excess as

~~~
Qᵣ⁺ = Q_M,ᵣ + Q_C,ᵣ + Q_I,ᵣ,
~~~

according to whether a face is assigned to a missing side, an actual contact side,
or the remaining bounded faces. Define

~~~
Mᵣ = hᵣ − Tᵣ + Q_M,ᵣ.
~~~

Every bounded triangular face must use a missing polygon side:

- a triangle with three unit contact edges is forbidden by triangle-freeness;
- a triangle using two polygon sides would require a loaded interior chord, unless
  the attachment polygon is itself a triangle, in which case the three sides are
  the outer face rather than a bounded face; and
- a triangle using an actual contact polygon side and two unit contact edges would
  be a unit equilateral triangle.

Therefore Tᵣ ≤ hᵣ, so Mᵣ ≥ 0.

The outer-face route accounting is occurrence-counted. Each missing-side face of
degree m contributes m−1 old route edges, while each actual contact polygon side
contributes one outer edge. Summing these routes gives

~~~
Lᵣ − 2aᵣ = Mᵣ − cᵣ^∂.                         (A.1)
~~~

The actual bounded nonquadrilateral faces are precisely the non-missing-side faces,
so

~~~
Qᵣ = Q_C,ᵣ + Q_I,ᵣ.
~~~

With P_exc,ᵣ = 4fᵣ + Qᵣ, fᵣ ≤ Qᵣ, and the exact Section-123 defect

~~~
Xᵣ = aᵣ − Tᵣ + Qᵣ⁺,
~~~

we have

~~~
Xᵣ = Mᵣ + cᵣ^∂ + Q_C,ᵣ + Q_I,ᵣ,
~~~

and hence

~~~
Lᵣ + P_exc,ᵣ − 2aᵣ
    ≤ Mᵣ − cᵣ^∂ + 5(Q_C,ᵣ + Q_I,ᵣ)
    = 5Xᵣ − 4Mᵣ − 6cᵣ^∂.                       (A.2)
~~~

This derivation counts every outer-face edge occurrence and makes no assertion that
walks from different components are globally injective.

## 4. Audit of globalization

Canonical Section 123 gives the exact identity

~~~
e_BB − k = (1/2)Σᵣ Xᵣ + d_tile.
~~~

Summing (A.2) gives

~~~
Σᵣ(Lᵣ + P_exc,ᵣ − 2aᵣ)
    ≤ 10(e_BB − k − d_tile)
       − 4M_miss − 6C_∂.
~~~

Adding 2Σᵣ(aᵣ−dᵣ) gives the second displayed inequality in Section 1. There is
no hidden use of dᵣ ≤ D in this algebra; the unresolved term is kept exactly.

The scalar compatibility certificate was rerun after this repair and still passes,
so the new credits do not by themselves yield a contradiction.

## 5. Finite inactive-exchange lemmas

The audited artifact also gives two elementary but useful no-go statements.

### Isolate-plus-one exchange

Let Z be the contact-isolated source points and let v be a nonisolated source
point. If Y ⊂ K = conv(A) has |Y| = |Z|+1, is strictly pairwise separated, and
is strictly farther than one from every source point in A \ (Z ∪ {v}), then
replacing Z ∪ {v} by Y preserves cardinality and diameter, creates no contact,
and removes at least one contact. This contradicts contact-minimality.

The proof is finite and exact: all points remain in K, so the new diameter is at
most the old one; the definition of D(n) forces equality; the old contact graph
with v deleted remains triangle-free; and no new unit edge is created.

### Loaded lexicographic companion

If v is incident to a diameter pair, Y ⊂ int(K), the replacement is unit-separated
and triangle-free, and the number of new contacts incident to Y is at most the
number of contact edges incident to v, then the replacement is impossible in the
contact-minimal, diameter-pair-minimal representative. If the contact count drops,
contact minimality is contradicted; if it is equal, every new interior point has
distance strictly below D(n) from every point of K, so deleting v strictly
decreases the number of diameter pairs.

These lemmas do not produce the required Y. In particular, the protected interior
of a macroscopic inactive chamber has an exact finite exchange obstruction; it does
not provide a source-preserving descent.

## 6. Exact remaining implications

The Type-II branch now has the sharper necessary condition

~~~
liminf (1/D) [10(e_BB − k − d_tile)
              + 2Σᵣ(aᵣ − dᵣ)
              − 4M_miss − 6C_∂]
    ≥ (π/2)(2 − √3).
~~~

To close Type II, one still needs one of:

1. a source-level upper bound for the same expression that beats the Section-122
   constant;
2. a source-preserving finite deformation driven by the residual attachment-cell
   term; or
3. an exact unit equilateral triangle.

To close the full problem, one additionally needs to exclude the macroscopic
internal chamber/exterior-cap branch. The finite exchange lemmas show precisely why
an informal “move one more isolated point inward” argument is insufficient.

## 7. Claim audit table

| Claim | Verdict | Reason |
| --- | --- | --- |
| Near-disk loaded unit chords are hull sides | audited-working | Convex support and short-arc projection argument is finite and uniform for sufficiently large D |
| No loaded interior chords in Type-II attachment cells | audited-working | Follows because Aᵣ⊂B and every loaded unit chord is a global hull side |
| Cellwise identity (A.1) | audited-working | Exact occurrence-counted face-route decomposition |
| Cellwise payment (A.2) | audited-working | Exact degree-excess comparison; no cross-cell boundary injection |
| Global Type-II payment | audited-working | Section-123 exact identity and summation |
| Scalar payment alone closes Type II | rejected | Exact rational scalar witness remains compatible |
| Isolate-plus-one exchange obstruction | audited-working | Direct contact-minimality contradiction |
| Loaded lexicographic exchange obstruction | audited-working | Direct diameter-pair-minimality contradiction |
| Type-II branch is eliminated | not proved | Residual Σᵣ(aᵣ−dᵣ) has no required bound |
| Macroscopic container is eliminated | not proved | No protected exchange or core relocation is constructed |
| Level I | not proved | Original uniform quantifiers remain open |

## 8. Computation and regressions

The following certificates were rerun:

~~~
python3 research/verify_target_c_scalar_ledger_compatibility.py
python3 research/verify_target_c_multigrain_endpoint_capacity_exact.py
python3 research/verify_target_c_protected_contact_creation.py
~~~

They passed at their stated scopes. The scalar certificate is an abstract ledger
witness, not a planar packing. The multi-grain certificate is conditional on
proof-only carrier hypotheses. The protected-contact certificate checks finite
motions and does not prove global optimality.

Binding regressions retained in the audit include contact-isolated source points,
repeated outer-walk occurrences, the no-Euler-path warning, the rejected FB4 and
C53 routes, the withdrawn Section-109 sharpness claim, the Section-121 scaling
correction, and the rejected full-source ZR/ZF extension.

## 9. Promotion recommendation

Classify the repaired Type-II payment and finite exchange lemmas as
**audited-working**, not canonical. Do not increment state_version, edit
docs/STATE.md, or alter the Target C route map until an independent promotion
transaction also adds the complete proof artifact, dependencies, and any required
certificates. The macroscopic-container and high-slack Type-II branches remain open.

## 10. Handoff

1. Strongest audited-working result: the Type-II payment with credits
   −4M_miss−6C_∂ and residual 2Σᵣ(aᵣ−dᵣ).
2. Exact dependencies: C-FULLCORE-NEAR-DISK, C-LOADED-HULL,
   C-HARMONIC-CELL-TILING, and C-AUGMENTED-CELL-DEFECT-BUDGET.
3. Exact remaining lemma: control the embedded attachment-cell term or turn it into
   a source-preserving strict decrease; separately exclude the macroscopic container.
4. Do not promote the scalar witness, the vanishing-shear family, or the safe-window
   multi-grain result to global-minimizer theorems.
