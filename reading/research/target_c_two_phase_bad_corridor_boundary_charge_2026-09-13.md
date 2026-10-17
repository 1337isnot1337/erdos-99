> Generated reading edition · [exact source](../../research/target_c_two_phase_bad_corridor_boundary_charge_2026-09-13.md) · source SHA-256 `1412cf6e8053f02d9f6a5f461deb2fbd29c8340abd067e1bae392f15e79eadac`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 1 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "d0673307fb0f5e032be47f89a2144a9ebfeb64d1", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_two_phase_bad_corridor_boundary_charge_2026-09-13.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d8ddb7bbb9cc5ace91deca1e5cb2f3dacb35a5d784d174aa4e7af0d1cdbea4ba"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — near-disk boundary charge for bad exceptional corridors

**Date:** 2026-09-13  
**Classification:** proved candidate awaiting hostile audit; theorem-state authority unchanged.  
**LEVEL I STATUS:** STILL OPEN. C-II REMAINS OPEN.

This note supplies a valid replacement for the missing geometric implication in the
rejected hull-face endpoint-capacity attempt.  It does not replace the false
`Q`-only charge.  The charge is instead made against the actual number of non-hull
side occurrences.

The candidate implication is

```text
near-disk force hull + o(D^2) exceptional-face area
 -> shared loaded-hull boundary <= non-hull boundary + o(D)
 -> bad-face loaded-hull incidence <= 5 unpaid non-phase occurrences + o(D).
```

Here an unpaid occurrence is a non-phase side occurrence of an exceptional face that
is not a loaded-hull side.  The result narrows the surviving long-thin corridor
branch, but does not prove that its unpaid population is sublinear.

## 1. Shared-boundary stability lemma

Let `K_D` be convex polygons with

```math
 d_H(K_D,B(o_D,D/2))=o(D),
\tag{BC.1}
```

and let `C_{D,i}` be convex polygons contained in `K_D` such that

```math
 \max_i \operatorname{area}(C_{D,i})=o(D^2).
\tag{BC.2}
```

For a side occurrence of `C_{D,i}`, call it **shared** if the whole side lies on
`\partial K_D`; call it **free** otherwise.  Write `H_{D,i}` and `I_{D,i}` for the
corresponding side counts.  The side lengths are one in the application, so counts
and lengths agree.  Then

```math
\boxed{
 \sum_i H_{D,i}
 \le
 (1+o(1))\sum_i I_{D,i}.
}
\tag{BC.3}
```

The `o(1)` is uniform over all families satisfying (BC.1)--(BC.2).

### Proof of the candidate lemma

Decompose the shared sides of one `C_{D,i}` into maximal boundary chains.  A chain
`\Gamma` has endpoints `x,y`; the complementary boundary path `\Lambda` between
these endpoints contains no shared side.  Consequently

```math
 |\Lambda|\ge |x-y|.
\tag{BC.4}
```

First, every shared chain has length `o(D)` uniformly.  Otherwise, after scaling by
`D` and passing to a subsequence, (BC.1) and perimeter continuity give a nontrivial
arc of the unit-radius limiting circle as a Hausdorff limit of that chain.  Its convex
hull has positive area.  Since `C_{D,i}` is convex and contains the chain, this
contradicts (BC.2).  A chain that winds through almost the whole limiting circle has
the same contradiction, because its convex hull contains the limiting disk sector of
positive area.

For a convex body between concentric circles of radii `D/2-o(D)` and `D/2+o(D)`, a
boundary arc of length `o(D)` has endpoint chord

```math
 |x-y|=(1-o(1))|\Gamma|.
\tag{BC.5}
```

To see the uniformity, let `r_D=D/2-o(D)` and `R_D=D/2+o(D)`.  Along a boundary
segment the radial angle changes by at most its length divided by `r_D`.  At a
support point, the outward normal and the radial direction differ by at most
`\beta_D=\arccos(r_D/R_D)=o(1)`.  Monotonicity of the normal angle on a convex
boundary therefore bounds the total tangent turn of a chain of length `h=o(D)` by
`h/r_D+2\beta_D=o(1)`.  Projection onto its midpoint tangent direction gives
`|x-y|\ge h\cos(o(1))`.  This proves (BC.5), uniformly over all such chains.

Combining (BC.4)--(BC.5) for every shared chain and summing over the cyclic boundary
of each face proves (BC.3).  A face with no free path would have its whole simple
boundary on `\partial K_D`, hence would equal `K_D` and violate (BC.2).  Thus the
chain decomposition is always available.  $`\square`$

The same argument can be phrased without a turning-angle estimate: a circular
segment cut off by a shared chain has area proportional to the chain's cubic chord
deficit, while the total exceptional-face area is `o(D^2)`.  This gives the same
uniform (BC.5) after summing the chains.

## 2. Strict face scope in the contact-core application

The count below is by physical unit-edge occurrences, so strictness of the face
polygon matters. Canonical Section 82 supplies it in the present contact-core
setting. A bounded face boundary is a simple cycle. At an unloaded boundary vertex,
an angle equal to `pi` would put all other incident contact vectors in the opposite
closed half-plane; positive equilibrium then forces those vectors onto the boundary
line, while unit separation permits at most two unit neighbors, contradicting the
unloaded degree lower bound three. At a loaded boundary vertex, the bounded face
sector lies in the tangent cone of the strict convex loaded force hull, whose opening
is less than `pi`. Thus no bounded face has a collinear boundary subdivision, and a
strictly convex face has at most two side occurrences in each projective direction.

This strict-face fact is an explicit dependency of the two-phase charge. Without it,
a collinear chain subdivided into many unit edges would invalidate the occurrence
count `S_i<=4`.

## 3. Two-phase bad-face charge

Assume every bounded quadrilateral face uses only two selected projective directions
`[u]` and `[v]`, and every bounded exceptional face is convex.  A convex polygon has
at most two sides in any projective direction, hence at most four selected-direction
sides.  For an exceptional face put

```math
 H_i=\#\{\text{loaded-hull side occurrences}\},
```

```math
 S_i=\#\{\text{non-hull side occurrences in }[u]\cup[v]\},
\qquad
 U_i=\#\{\text{non-hull side occurrences in neither }[u]\text{ nor }[v]\}.
```

Then

```math
 I_i=S_i+U_i,
\qquad S_i\le4.
\tag{BC.6}
```

Call a face **good** if `U_i=0` and **bad** if `U_i\ge1`.

For every bad face, (BC.6) gives

```math
 I_i\le U_i+4\le5U_i.
\tag{BC.7}
```

Applying (BC.3), and writing `U=\sum_iU_i`, yields

```math
\boxed{
 \sum_{i\ {\rm bad}}H_i
 \le 5(1+o(1))U+o(D).
}
\tag{BC.8}
```

For completeness, the `o(D)` term accounts for good faces.  A good face has a
non-hull phase path: if every side were a loaded-hull side, its simple boundary would
be the entire force-hull boundary, contradicting (BC.2).  Its phase path has at most
four unit steps, so its displacement belongs to the finite set

```math
 \mathcal W=\left\{\sum_{j=1}^{r}\epsilon_jw_j:
 1\le r\le4,\quad
 \epsilon_jw_j\in\{u,-u,v,-v\}\right\}.
\tag{BC.9}
```

For a fixed nonzero displacement, the translate-pair lemma for a convex polygon gives
at most two ordered pairs of force-hull vertices.  A fixed ordered phase word then
determines the path.  Hence the number of good faces is `O(1)`.  Their total shared
boundary is `o(D)` by (BC.3), since each has at most four free sides.

This proves (BC.8).  The proof is occurrence-safe: a bridge is not silently treated
as a bounded-face side, and every shared side is counted with the face occurrence on
which it appears.

## 4. Sharpness of the factor-five local charge

The factor five cannot be improved from the per-face direction count alone. Take
unit vectors with arguments

```math
0,\ \theta,\ 120^\circ,\ 180^\circ,\ 180^\circ+\theta,\ 300^\circ,
\qquad \theta=70^\circ.
```

Equivalently, the cyclic edge vectors are `u,v,w,-u,-v,-w`, where `[u]` and `[v]`
are the two selected projective directions and `w` is off-phase. They sum to zero,
and the successive angle gaps are all strictly between zero and `pi`, so they form a
strict convex unit hexagon. Mark one of the two `w` edges as a loaded-hull occurrence
and the other as a non-hull occurrence. Then

```math
H_i=1,\qquad S_i=4,\qquad U_i=1,\qquad I_i=5.
```

Thus `I_i=5U_i` is attained while the face-closure equation is satisfied. This is a
finite incidence regression, not a claim that the marked hexagon is a C-II source
face; any improvement must use global hull incidence, route geometry, or minimality.

## 5. Consequence for the equality corridor

In the Type-II near-disk normalization, `c_B=0`, so every loaded-loaded unit contact
is a force-hull side. If `B_o=o(D)` outer-visible bridges are removed, every other
loaded-hull side is incident to an exceptional bounded face or a strict-rhombus face.
Only exceptional faces enter `H_i`; the two-phase charge therefore controls the
exceptional-face portion of the loaded boundary.

On the scoped equality branch

```math
 k=o(D),\qquad u_B=o(D),\qquad B_o=o(D),
\tag{BC.10}
```

the exact Type-II identity `e_{BB}=Q+2k+u_B` and the bounded-face incidence ledger
give

```math
 \sum_iH_i\ge Q-o(D).
\tag{BC.11}
```

Here is the needed incidence detail.  Every non-bridge loaded-hull side is incident
to a bounded face.  A non-phase such side cannot be incident to a strict-rhombus face,
because every strict-rhombus side is in `[u]\cup[v]`; the convex force hull has at
most four sides in those two projective directions.  Thus all but `O(1)+B_o` of the
`e_{BB}` sides occur on exceptional faces.  With `B_o=o(D)` and
`e_{BB}=Q+o(D)`, this is exactly (BC.11).

Combining (BC.8) and (BC.11) gives the concrete necessary condition

```math
\boxed{
 U\ge {1\over5}Q-o(D).
}
\tag{BC.12}
```

The same shared-boundary estimate also gives a face-count consequence. Since

```math
 H:=\sum_iH_i\ge Q-o(D),
 \qquad H\le(1+o(1))I,
 \qquad H+I=P_{exc}=4f+Q,
```

one obtains

```math
\boxed{Q\le4f+o(D).}
\tag{BC.13}
```

Thus the cheap-boundary equality corridor requires a linear exceptional-face count
whenever `Q` is linear; it cannot hide all of its defect in a sublinear number of
long faces. This remains compatible with a `Theta(D)` family of thin corridors and
does not supply a diameter descent.

Thus a linear `Q` equality corridor cannot be supported by a sublinear unpaid
non-phase population.  The remaining branch is genuinely a linear thin corridor with
unpaid interior side occurrences; (BC.12) does not yet convert those occurrences into
outer detour, a diameter descent, or a unit triangle.

## 6. Scope and disposition

- (BC.3) is a convex near-disk boundary stability candidate; its proof uses only
  compactness, support lines, and the circular small-arc estimate.
- (BC.8) is a finite two-phase incidence consequence once (BC.3) is audited.
- The result is full-core/Type-II and global-two-phase only.
- Contact-isolated source points remain in the full source.
- No `Q`-only exceptional-face capacity is used; the rejected direction reversal is
  explicitly avoided.
- This is not a C-II closure.  The target next step is to charge the linear `U` in
  (BC.12) to the aggregate detour or to a source-preserving strict diameter descent.

**Disposition:** proved candidate awaiting hostile audit; theorem-state unchanged.
