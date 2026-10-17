> Generated reading edition · [exact source](../../research/target_c_shore_balance_joint_orbit_energy_hostile_audit_2026-09-15.md) · source SHA-256 `f3ae9b1d20bfdef79e2cf166639c12bbace557698f5d0f582846a807eeae93ff`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "da85f0dfcf029743cd5b93129cf39a0e88d0a8f6", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_shore_balance_joint_orbit_energy_hostile_audit_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "7024efc5154bbc479ba030f551b71df2c999c01517e6b4c3e2e6754fceb35f8d"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — shore-balanced atomic gap and sharpened joint orbit-energy floor

**Date:** 2026-09-15  
**Reviewed:**
- `research/target_c_atomic_gap_shore_balance_00059_2026-09-15.md`
- `research/verify_target_c_atomic_gap_shore_balance_00059.py`
- `research/target_c_dominant_orbit_outer_energy_sharpening_2026-09-15.md`
- `research/verify_target_c_dominant_orbit_outer_energy_sharpening.py`

**Disposition:** **PASS at proof-only full-core Type-II scope.**  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The candidate package makes two reusable changes to the current low-`t` stack.

1. It repairs a quantitative inefficiency in the AG42/§168 near-Mantel bookkeeping by
   coupling the two retained Mantel-shore masses.  This raises the safe atomic gap from
   `0.00042` to `0.00059`.
2. It uses the full vector of exact `pi/3` orbit masses to strengthen the dominant-orbit
   lower bound, then inserts both improvements into the already-merged exact joint
   route cost `Phi`.  This raises the safe joint orbit-energy floor from `1.82434` to
   `1.82439`.

The audit below checks the places where the refinement could fail: reuse of the same
minority loss on two shores, whether the chosen atom families remain large enough for
the §163 order theorem, the quadratic root selection, monotonic substitutions through
`A,C,U`, and the two-variable endpoint reduction.

---

## 1. The shore-balance improvement does not invent extra mass

Let `X,Y` be the two Mantel shores in the dominant orbit after the standard
maximum-degree stability step.  With orbit mass `M` and deficit `d_0`, audited §168
gives

$$
|X|+|Y|=(M+o(1))D,
$$

and

$$
\min(|X|,|Y|)/D\ge M/2-\sqrt{d_0}-o(1).
$$

For the three atom windows let `(x_i,y_i)` be their normalized shore populations.
Same-window cross-shore pairs cannot be strict-rhombus crossings, so

$$
\sum_i x_i y_i\le2d_0+o(1).
$$

The total minority population discarded when each window is assigned to its majority
shore is

$$
L=\sum_i\min(x_i,y_i)
\le\sum_i\sqrt{x_i y_i}
\le\sqrt{3\sum_i x_i y_i}
\le\sqrt{6d_0}+o(1).
$$

This is one global discard.  If `P,Q` are the retained shore masses, then

$$
P+Q\ge M-\sqrt{6d_0}-o(1),
$$

while each retained shore loses at most the total discard, so

$$
\min(P,Q)
\ge M/2-\sqrt{d_0}-\sqrt{6d_0}-o(1).
$$

These two inequalities are compatible; they do not count the discarded mass twice.
The first uses the exact total retained mass, and the second uses the worst possible
concentration of the same discard on the smaller shore.

**Verdict:** PASS.

---

## 2. The one-family / two-family selection is exhaustive

After majority assignment, each of the at most three atom windows is assigned wholly
to one Mantel shore.  At `eta=0.00059` the retained individual shore lower bound is
strictly positive, so both shores contain an assigned atom family.

With at most three nonempty atom windows distributed between two nonempty shores, one
shore contains exactly one family and the other contains at most two.  If their total
retained masses are `P,Q`, selecting the unique family on the one-family shore and the
larger family on the other gives at least

$$
\min\{P+Q/2,Q+P/2\}
={P+Q+\min(P,Q)\over2}.
$$

Substituting the two bounds above yields

$$
{3M\over4}-{\sqrt{d_0}\over2}-\sqrt{6d_0}-o(1).
$$

This is the candidate's `G_0` inequality.  It is strictly stronger than replacing both
shore masses independently by the old common lower bound.

A separate randomized optimization in Pyroam sampled 200,000 admissible shore/discard
configurations and found no violation of the deterministic inequality.  The random
check is not part of the proof, but it is useful regression coverage.

**Verdict:** PASS.

---

## 3. The §163 common-neighbor argument still uses the old individual floor

A sum lower bound alone would not guarantee that both selected families remain large
enough for pair/triple common neighbors after pruning.  The candidate does not make
that mistake.

It retains the old individual shore quantity

$$
S_0=M_0/2-\sqrt{d_0}-\sqrt{6d_0}
$$

and therefore the same individual family floors used by AG42: one selected family has
mass at least `S_0`, and the larger family on the other shore has mass at least
`S_0/2`.

At `eta=0.00059`, the committed/Pyroam certificate gives

$$
S_0/2-2p_0-3p_0
=0.2674351033\ldots>0,
$$

where `p_0=sqrt(2d_0)`.  Thus the triple-common-neighbor threshold has very large
slack.  The actual §163 `K_{2,2}` consistency and transitivity proof is unchanged.

**Verdict:** PASS.

---

## 4. All six `p_0` losses remain paid

The shore coupling changes only the starting sum of the two selected atom-family
masses.  It does not alter the missing-pair budget.

The inherited proof still pays:

1. one `p_0D` phase-order deletion on the first family;
2. one `p_0D` phase-order deletion on the second family;
3. one `p_0D` minimum-degree deletion on the first family;
4. one `p_0D` minimum-degree deletion on the second family;
5. one `p_0D` missing-neighbor allowance at the first opposite corner;
6. one `p_0D` missing-neighbor allowance at the second opposite corner.

Hence the path coefficient is exactly

$$
E_{bal}
={3M_0\over4}-{\sqrt{d_0}\over2}-\sqrt{6d_0}-6p_0.
$$

No pruning payment has disappeared under a new name.

At `eta=0.00059`, independent Pyroam evaluation gives

$$
{\sqrt3\over2}E_{bal}
=1.0018837957444775\ldots>1.
$$

The revised bookkeeping root lies between `0.00059946` and `0.00059947`, so the round
constant `0.00059` is conservative.

**Verdict:** PASS.

---

## 5. The quadratic dominant-orbit inequality is valid and the large root is forced

Let the exact orbit masses be `M_r`, with total atomic mass `A`, largest mass `M`, and
crossing masses `E_r`.  The audited inequalities are

$$
4\Delta_2\le\sum_rM_r^2,
\qquad
\sum_rM_r=A.
$$

For an orbit attaining `M`, the remaining masses sum to `A-M`, so

$$
\sum_{r\ne r_*}M_r^2\le(A-M)^2.
$$

Therefore

$$
4\Delta_2\le M^2+(A-M)^2.
$$

This quadratic inequality alone permits a small-root and a large-root branch.  The
candidate correctly uses the pre-existing generic estimate

$$
M\ge4\Delta_2/A.
$$

In the low-`t` domain under consideration `A^2<8\Delta_2`, so this generic estimate is
strictly larger than `A/2`.  Therefore `M>A/2` and the small quadratic branch is
excluded.  The valid conclusion is

$$
M\ge{A+\sqrt{8\Delta_2-A^2}\over2}.
$$

A randomized Pyroam regression generated 500,000 orbit-mass vectors; among 37,903
samples satisfying the crossing-capacity and generic-majority hypotheses, none
violated the derived large-root bound.

**Verdict:** PASS.

---

## 6. Replacing `A` by `C` has the correct direction

Define

$$
m(A)={A+\sqrt{8\Delta_2-A^2}\over2}.
$$

For `A>=2sqrt(Delta_2)`,

$$
m'(A)
={1\over2}\left(1-{A\over\sqrt{8\Delta_2-A^2}}\right)\le0.
$$

The audited exposed-hull inequality gives `A<=C`, so

$$
m(A)\ge m(C).
$$

Thus replacing the unknown actual atomic mass by `C` weakens the dominant-orbit lower
bound and is safe.

**Verdict:** PASS.

---

## 7. Replacing `C` by the upper envelope `U` is also safe

After inserting `m(C)`, the dominant-orbit outer-occurrence lower bound is

$$
K\ge
\pi+\delta-t-\kappa-C+
\sqrt{8\Delta_2-C^2}.
$$

The `C`-dependent part

$$
g(C)=-C+\sqrt{8\Delta_2-C^2}
$$

has derivative

$$
g'(C)=-1-{C\over\sqrt{8\Delta_2-C^2}}<0.
$$

Since `C<=U`, one has `g(C)>=g(U)`.  Therefore

$$
K\ge
\pi+\delta-t-\kappa-U+
\sqrt{8\Delta_2-U^2}
$$

with the correct inequality direction.

The excluded interval satisfies `U<1.927<sqrt(8 Delta_2)`, so no hidden square-root
domain problem occurs.

**Verdict:** PASS.

---

## 8. The merged joint `Phi` theorem applies unchanged

The candidate does not recompute or modify the local joint route relaxation.  It only
feeds a stronger lower bound for dominant-orbit outer occurrence mass into the merged
theorem

$$
\delta\ge\Phi(K),
\qquad
\Phi(z)=z-6\arcsin(\tanh(z/6)).
$$

The merged proof already handles occurrence multiplicity, the simultaneous
`d_i>=n_i g_i` and `d_i>=n_i-s_i` constraints, the perimeter-measure limit, and the
interior dual optimizer.  Since `Phi` is increasing, substituting a lower bound for
`K` is valid.

At the new safe endpoint `K_0=1.3266995103...<3 log 3`, so the exact interior `Phi`
formula remains in scope.

**Verdict:** PASS.

---

## 9. The two-variable minimization remains at `kappa=0`, maximal `delta`

Write

$$
U={9t\over2}-2\pi-2\delta-\kappa/2,
\qquad
S(U)=\sqrt{8\Delta_2-U^2},
$$

and

$$
K_*=
\pi+\delta-t-\kappa-U+S(U).
$$

Because `U>=C_0>2sqrt(Delta_2)`, one has `U>S(U)`.  Direct differentiation gives

$$
{\partial K_*\over\partial\kappa}
={1\over2}\left({U\over S(U)}-1\right)>0.
$$

Thus `Phi(K_*)-delta` is minimized at `kappa=0`.

Also

$$
{\partial K_*\over\partial\delta}
=3+{2U\over S(U)}.
$$

Over the excluded interval the independent Decimal/Pyroam certificate gives the
conservative bounds

$$
{\partial K_*\over\partial\delta}<5.05,
\qquad
K_*<1.33,
\qquad
\Phi'(K_*)<0.025.
$$

Hence

$$
{\partial\over\partial\delta}
[\Phi(K_*)-\delta]
<5.05(0.025)-1<0.
$$

After `kappa=0`, the weakest point is therefore maximal feasible detour

$$
\delta=R(t)/2,
\qquad
U=C_0.
$$

The earlier draft of this branch temporarily used an overly tight `4.03` derivative
envelope for the weaker sequential cost.  Its verifier caught that mistake before PR
publication.  The corrected joint theorem uses the independently checked `5.05`
envelope above.

**Verdict:** PASS.

---

## 10. Scalar endpoint certification

At the weakest point,

$$
K_0(t)
=
\pi+{R(t)\over2}-t-C_0+
\sqrt{8\Delta_2-C_0^2},
$$

and

$$
H_0(t)=\Phi(K_0(t))-R(t)/2.
$$

Since `K_0'(t)=5/4` and `Phi'<1`,

$$
H_0'(t)
={5\over4}\Phi'(K_0(t))-{9\over4}<0.
$$

The committed Decimal certificate and an independent Pyroam execution give

$$
H_0(1.82439)
=0.0000036173637263927671\ldots>0,
$$

and

$$
H_0(1.82439162)>0,
\qquad
H_0(1.82439163)<0.
$$

The same execution reports

$$
{\partial K_*\over\partial\delta}_{max}
=5.0469011333\ldots,
$$

$$
\Phi'(1.33)=0.02407491888\ldots,
$$

whose product is only `0.1215037...`.

**Verdict:** PASS.

---

## 11. Scope and non-implications

The package proves, at proof-only full-core Type-II scope,

$$
\boxed{
\liminf {T-q/2\over D}
\ge2\sqrt{\Delta_2}+0.00059
}
$$

and, after the merged joint route theorem,

$$
\boxed{
\liminf {q-k\over D}\ge1.82439.
}
$$

It does **not** close C-II.  It does not address the macroscopic inactive-container
branch, produce a source-preserving diameter-decreasing competitor, or prove a uniform
contact/KKT weight floor.  It also does not justify replacing the three-direction
bathtub by a stronger cost without new endpoint or train-pairing information.

The next useful gain must therefore use geometry not already optimized by the joint
route relaxation: bounded-face terminal restrictions, correlations between the two
terminals of one stopped train, the forced pentagon population, signed penetration, or
two-sided diameter bracing.

**Final verdict:** PASS at proof-only scope. C-II remains open; theorem-state authority
is unchanged.
