> Generated reading edition · [exact source](../../../docs/reports/target_c_open_guard_packing_saturation_2026-09-12.md) · source SHA-256 `21e8cdf31c406b9f518e6b15a3761e96b0892fbca53ee8bf11576f879b3b987a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-15B5C442D0F1","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C: open-guard packing saturation of the full source

Date: 2026-09-12. Baseline: `7fd69821cb046226f84ecf2c7b9fb24d7077e4e7`;
canonical state `2026-09-12.audit.46`. Target: C-II, both inactive-container types.

**Classification: proved candidates awaiting promotion; artifact unreviewed.**
**C-II and Level I remain open.** No canonical status is changed here.

## 1. Exact implication and dependencies

The closing implication attacked is

```
one spare ordinary packing site in a strictly guarded open region
-> dilate only the inserted finite packing to remove all its unit contacts
-> delete one nonisolated source vertex and replace all selected isolates
-> same-cardinality triangle-free competitor with fewer contacts
-> contradiction to contact-minimal global optimality.
```

The proof uses the contact-minimal normalization among triangle-free global
minimizers. Section 57 is used only for its explicit statement that every actual
diameter endpoint belongs to the nonisolated core. Its affine-kernel theorem is
NOT applied to isolates. No rigidity, stress-transversal, or train theorem is
used. Lattice averaging below is proved directly.

The strict finite-exchange argument on remote commit `86b5227`,
`research/target_c_section122_finite_exchange_saturation.md`, already forbids
strictly separated replacements of one core vertex plus isolates. It is
noncanonical and is not a proof dependency here. The new bridge is from
**ordinary** unit packings, which may contain many unit triangles, to strict
replacements in an **open** region. The full-source lens formulation also
handles isolates outside the interior of the old source hull. This does not
claim a new excluded carrier-ratio window.

## 2. Strictification inside an open region

Let `U` be an open subset of the plane, `D>0`, and let `B subset U` be a finite
unit-separated set with `diam B<D`. There is a finite set `B' subset U` with
the same cardinality, every distinct pair at distance **strictly greater than
one**, and `diam B'<D`. Moreover `B'` can be arbitrarily close to `B`.

**Proof.** Fix any center `c`. Put `B_t={c+(1+t)(b-c): b in B}`. Finiteness
and openness give `B_t subset U` for every sufficiently small `t>=0`.
Distinct pair distances are multiplied by `1+t`; hence for small `t>0`
they are strictly greater than one while the diameter remains less than `D`.
Empty and singleton sets require no change. This proof concerns the inserted
packing only: no motion from the old source population to `B` is asserted.

If `W` is open and `diam W<=D`, every finite `B subset W` has `diam B<D`.
Indeed, a pair attaining distance `D>0` could have one endpoint moved slightly
away from the other while staying in `W`, contradicting `diam W<=D`.
Thus the diameter premise for strictification is automatic in such a `W`.

## 3. Exact full-source open-lens saturation

Let `A` be a triangle-free global minimizer of diameter `D>1`, chosen with
the least number of unit contacts among triangle-free global minimizers of
its cardinality. Let `v` be any contact-nonisolated vertex and `Z` any subset
of the **actual contact-isolated source vertices**. Set

```math
 z=|Z|,\qquad R=A\setminus(Z\cup\{v\}),\qquad
 U_R=\{x:1<|x-r|<D\text{ for every }r\in R\}.
\tag{3.1}
```

Here `R` is nonempty because a contact neighbor of `v` cannot belong to `Z`.
The set `U_R` is open and bounded. Define the integer capacity

```math
 M_D(U_R)=\max\{|B|:B\subset U_R\text{ finite},\quad
 |b-b'|\ge1\ (b\ne b'),\quad\operatorname{diam}B<D\}.
\tag{3.2}
```

The empty set is admissible, with diameter zero. Capacity is finite: the
radius-`1/2` open disks about an admissible set are disjoint and all lie in
a fixed bounded disk. The nonempty set of attainable nonnegative integers
therefore has a maximum. This is not a compactness or attainment claim for
an optimizer in an open configuration space.

### Theorem 3.1

```math
                         M_D(U_R)\le z.                 \tag{3.3}
```

If no actual diameter pair of `A` is incident to an isolate, as in the
canonical C-II normal form, then

```math
                         \boxed{M_D(U_R)=z.}            \tag{3.4}
```

**Proof.** If (3.3) fails, select `z+1` points from an admissible packing and
apply Section 2 in `U_R`. The resulting `B'` has all internal distances
strictly between one and `D`. Its cross distances to `R` satisfy the same
strict inequalities by (3.1). Hence

```math
                          A'=R\cup B'
```

has exactly `|A|` distinct points, is unit-separated, has diameter at most
`D`, and has no new unit contacts. Every triangle in its unit-contact graph
would be an old triangle in the induced graph on `R`; there are none.
At least the positive number `deg_C(v)` of old unit contacts were removed,
and none was added, since the vertices of `Z` were isolates. If `diam A'<D`,
global optimality is contradicted. Otherwise `A'` is a triangle-free global
minimizer with strictly fewer contacts, another contradiction.

For (3.4), all distances from an original isolate to any other original
point are strictly greater than one and, by the additional hypothesis,
strictly less than `D`. Consequently `Z subset U_R` and `diam Z<D`.
Thus `Z` itself is admissible in (3.2), including the empty/singleton cases,
and gives the reverse inequality. All original source points are retained
or explicitly replaced in the same-cardinality construction. QED.

No assumption places `Z` inside the old hull interior. In particular (3.4)
applies to contact-isolated extreme points in the exterior-cap branch.
Nor is any isolate silently promoted to a contact-core coordinate.

## 4. Ordinary packing and a sharp area obstruction

Write `N_1(W)` for the ordinary unit-separation packing number in a bounded
set `W`, without requiring strict distances or triangle-freeness.

### Corollary 4.1

For every open `W subset U_R` with `diam W<=D`,

```math
                         N_1(W)\le z.                   \tag{4.1}
```

If `Z subset W`, equality holds under the diameter-endpoint hypothesis of
Theorem 3.1. In particular, one can take any open `W subset int(conv A)`
whose points are at distance greater than one from every retained point.

**Proof.** Section 2 gives the strict diameter needed for (3.2) for each
finite packing in `W`, and Theorem 3.1 applies. For the hull example,
`diam(conv A)=D`; an interior point is strictly less than `D` from any
point of `conv A`, by the same endpoint-motion argument. Thus `W subset U_R`.

### Corollary 4.2

Under the hypotheses of Corollary 4.1, with `a_0=sqrt(3)/2`,

```math
                         |W|\le a_0 z.                  \tag{4.2}
```

**Proof.** Let `Lambda` be the triangular unit lattice, with fundamental
parallelogram `F` of area `a_0`. For a uniformly translated lattice,
Tonelli's theorem and tiling by `F+lambda` give

```math
 \frac1{|F|}\int_F\#((t+\Lambda)\cap W)\,dt=\frac{|W|}{a_0}.
```

Each lattice intersection is a finite unit-separated packing. If
`|W|>a_0 z`, some intersection has at least `z+1` points, contrary to
(4.1). This works for disconnected, nonconvex, or irregular open `W`.
No boundary regularity or perimeter estimate is used.

For a convex inactive container `C subset conv A` holding exactly the
selected isolate population in its interior, with every retained point
outside `int C`, the open inner parallel set

```math
                 C_{-1}=\{x\in\operatorname{int}C:
                                  \operatorname{dist}(x,\partial C)>1\}
```

is an allowable `W`. The same assertion holds if additional removed isolates
were on its boundary. It requires the stated source partition: one must not
ignore retained points lying in the container. This applies to a verified
internal chamber or a verified convex exterior cap, not to a hypothetical
Reuleaux-cap containment.

## 5. Hostile audit and limitations

1. **Diameter lens is not a diameter-D container.** For `R={(0,0)}` and
   `D=3`, both `(2,0)` and `(-2,0)` are in `U_R`, but their mutual distance
   is four. Omitting `diam B<D` from (3.2) is invalid. The test does not
   assert this singleton `R` arises from the normalized source.
2. **Openness is essential.** The closed segment of length one admits two
   unit-separated points but not two strictly separated points. A closed
   unit triangle likewise cannot be strictified inside itself. We do not
   use a closed-container packing theorem without a positive buffer.
3. **Triangle-freeness of the candidate packing is unnecessary.** It may
   be a triangular lattice patch. Dilation removes every internal contact;
   strict cross guards forbid contacts to retained vertices. Triangle-freeness
   of the old retained source is, however, necessary for the lexicographic
   contradiction as stated.
4. **No hidden strict descent.** Retained diameter pairs may survive. The
   contradiction then uses contact minimality among triangle-free global
   minimizers, not an unproved diameter decrease. The exact script includes
   such a retained-diameter example.
5. **No integral gain from asymptotics.** Quadratic area and only `O(D)`
   Oler slack do not imply `|C_{-1}|>a_0 z`. Erosion costs linear area, and
   the remaining one-integer comparison is unresolved. Strict inequality
   in the area criterion is deliberate.
6. **Comparison with stress-transversal reinsertion.** In this normalized
   setting an ordinary packing reserve of **one** site in an open protected
   region suffices. Deleting `s_Z+1` vertices to destroy every stress is
   not required for this contact-count contradiction. This does not replace
   the stress theorem outside this scope or prove its stronger strict-descent
   conclusion from a one-site premise.
7. **Finite certificate scope.** The companion script uses exact rational
   arithmetic in Cartesian and triangular-lattice coordinates. It checks
   internal triangle destruction, full cardinality, every cross pair, a
   surviving diameter, and an extreme original isolate. Its finite sources
   are not claimed globally optimal. The general statements are proved
   above, not inferred from computation.

## 6. Exact surviving closure obligation

Theorem 3.1 is a source-level necessary condition, simultaneously for every
contact vertex `v` and every isolate subset `Z`. It is not a branch elimination.
To close an inactive-container survivor by this route one must prove that at
least one such pair admits `z+1` ordinary packing sites in `U_R` of diameter
strictly below `D`; an open guarded region of packing number greater than `z`
is sufficient. Canonical container estimates have not yet been shown to force
that integer surplus. The full-core branch also remains open.
