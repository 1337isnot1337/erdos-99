> Generated reading edition · [exact source](../../../docs/reports/toeout_kuperberg_improvement_2026-08-30.md) · source SHA-256 `a09e57ab2f90809794049bd4bc237b1fe287ee37aeeaf0a623bf0e8d67dbdbcd`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "1f07ce132fc995e07443acaae9b27fbcf37d1cbe", "source_canonical": false, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "unreviewed", "source_path": "docs/reports/toeout_kuperberg_improvement_2026-08-30.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "307798c012e15aca45a07700899dbed71dce0d7fdeb223ffc7fff5cab9016e0c"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle was `unreviewed`; it is retained as provenance only. Destination status remains unreviewed/noncanonical.

# Erdős Problem #99 — toe-out Kuperberg five-block improvement

**Date:** 2026-08-30  
**Repository state:** based on `main` after commit `4447bd4828ff7bcbd7b9fb8fbea218627eadb70a`; work branch `research/toeout-kuperberg-2026-08-30`  
**Run type:** closing-proof / exact finite-geometry improvement  
**Target:** A, finite-gap route  
**Active prompt:** `docs/prompts/erdos_problem_99_1.7.5_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used for the theorem  
**Computation:** exact scratch algebra plus `research/kuperberg_five_block_toeout_exact.py`

## LEVEL I STATUS

`STILL OPEN`

The exact Target A Schur endpoint remains unproved.  This run nevertheless produces a
new audited theorem: the Section 157 five-block partition admits a different feasible
rigid translation with an eightfold larger leading quartic gap gain.  The resulting
support theorem has an explicit asymptotic exponent constant and reaches the
borderline accumulated-strain scale `alpha_L \asymp (\log L)^{-1/3}` for a nonempty
range of constants.

## 1. Starting endpoint

The direct Target A closure is

```math
\dim\ker S\ge\Delta_\Lambda-d_{\rm int},
```

or an actual `N`-point unit-separated competitor of diameter strictly below
`D=D(N)`.

The finite-gap subroute starts from Section 157.  In canonical minimum-distance-one
normalization it proved

```math
W(d)\le C_1\exp(C_2d^{-3})
```

using the published five-block movement, whose one-step gain was

```math
\delta_{157,\rm can}(d)=\frac{\sqrt3}{9}d^4+O(d^5).
```

That gave the sufficient fixed-shape condition

```math
\alpha_L^{-3}=o(\log L).
```

The missing Target A implication was, and remains, exterior compatibility with a
monomer domain actually derived from a global minimizer.

The exact implication chain attacked here is

```text
larger exact finite-gap gain
    -> smaller explicit support exponent constant
    -> larger vanishing-strain same-hull add-one regime
    -> stronger finite geometric input for exterior-compatible embedding
```

It is not by itself a Level I closure.

## 2. Strongest genuinely new audited theorem

### Theorem: toe-out five-block widening

Use the paper normalization with center distance two and upper-half gap `d>0`.  Keep
the exact five-block partition of Section 157 and translate

```math
B_1=(-a,-b),\quad B_2=(-c,-e),\quad B_3=(0,v),\quad
B_4=(c,-e),\quad B_5=(a,-b).
```

There are unique real-analytic functions `a,b,c,e,v` near `d=0`, all positive for
small positive `d`, such that the five contact equations

```math
\begin{aligned}
(2-a)^2+b^2&=4,\\
(1-a)^2+(\sqrt3+d-b)^2&=4,\\
(-2+c-a)^2+(e-b)^2&=4,\\
(1-c)^2+(\sqrt3+e)^2&=4,\\
(1+c)^2+(\sqrt3-e-v)^2&=4
\end{aligned}
```

hold and every other pair remains at distance at least two.  The middle lift is

```math
\boxed{
v(d)=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
}
```

Therefore the local aligned gap widens from `d` to `d+v(d)`.  The leading gain is
exactly eight times that of the movement used in Section 157.

### Complete proof

At `d=a=b=c=e=v=0`, the Jacobian of the five displayed equations with respect to
`(a,b,c,e,v)` is

```math
J_0=
\begin{pmatrix}
-4&0&0&0&0\\
-2&-2\sqrt3&0&0&0\\
4&0&-4&0&0\\
0&0&-2&2\sqrt3&0\\
0&0&2&-2\sqrt3&-2\sqrt3
\end{pmatrix}
```

and

```math
\det J_0=384\sqrt3\ne0.
```

The real-analytic implicit-function theorem gives a unique analytic branch.  Expanding
its five equations coefficient by coefficient gives

```math
\begin{aligned}
a&=\frac14d^2-\frac{\sqrt3}{24}d^3+\frac1{24}d^4
   -\frac{\sqrt3}{144}d^5+O(d^6),\\
b&=d-\frac{\sqrt3}{12}d^2+\frac1{24}d^3
   -\frac1{144}d^5+O(d^6),\\
c&=\frac12d^2-\frac{\sqrt3}{6}d^3+\frac5{24}d^4
   -\frac{\sqrt3}{18}d^5+O(d^6),\\
e&=\frac{\sqrt3}{6}d^2-\frac16d^3+\frac{\sqrt3}{72}d^4
   +\frac1{18}d^5+O(d^6),\\
v&=\frac{\sqrt3}{9}d^4-\frac29d^5+O(d^6).
\end{aligned}
```

The signs are positive for sufficiently small `d>0`.

Use the exact lattice-index block model of Section 157.  Rigid translation preserves
all within-block distances.  Enumerating the six nearest-neighbor directions across
moved/moved and moved/fixed interfaces gives fifteen distinct margin polynomials.  Five
are exactly the defining equalities.  For the other ten, substitution of the analytic
branch gives leading margins

```math
2\sqrt3d,\quad d^2,\quad 2\sqrt3d,\quad2d^2,\quad
2\sqrt3d,\quad2\sqrt3d,\quad2\sqrt3d,\quad2\sqrt3d,
\quad2d^2,\quad4d^2,
```

respectively, each plus higher-order terms.  Hence all ten are strictly positive for
small `d>0`.  The full polynomial list is recorded in canonical Section 160 and the
exact truncated-series checker enumerates it directly from the block coordinates.

At `d=0`, every pair that is not a triangular-lattice nearest neighbor has distance at
least `2\sqrt3`.  Every block translation on the analytic branch is `O(d)`, so after
shrinking `d` all originally non-neighboring pairs still have distance greater than
two.  Thus the final translated configuration is unit-separated in the paper
normalization.

The middle block moves only vertically by `v`; the lower half-lattice is fixed.
Therefore its base sees aligned gap width `d+v`.  This proves the gain formula.  Since
Section 157 had paper-normalization leading gain `\sqrt3 d^4/72`, the ratio tends to
eight.

No collision-free continuous path between the initial and final block positions is
required: the finite replacement argument needs the final set to be a packing.  The
construction nevertheless remains a finite rearrangement of exactly the same five
rigid blocks.

### Support theorem

Use a fixed one-ring margin when fitting each child five-block template into the moved
middle block.  The exact containment condition becomes

```math
3m+C\le n
```

for an absolute constant `C`; hence `k` recursive stages still require initial linear
scale `O(3^k)`.  The safety ring ensures that all child nearest-neighbor constraints
are the same local constraints just audited; points outside that ring are non-neighbors
and retain strict clearance.

With

```math
\delta(x)=Kx^4+O(x^5),\qquad K=\frac{\sqrt3}{9},
```

the recurrence `x_{j+1}=x_j+\delta(x_j)` satisfies

```math
x_j^{-3}-x_{j+1}^{-3}=3K+O(x_j).
```

Also `\sum_jx_j=O(d^{-2})` before a fixed width is reached.  One direct proof uses
`\delta(x)\asymp x^4` to compare each `x_j` with a constant multiple of
`\int_{x_j}^{x_{j+1}}t^{-3}\,dt`; summing gives `O(d^{-2})`.  Consequently

```math
k(d)=\frac1{3K}d^{-3}+O(d^{-2})
=\sqrt3d^{-3}+O(d^{-2}).
```

Thus in paper units

```math
\limsup_{d\downarrow0}d^3\log R(d)\le\sqrt3\log3.
```

Canonical gap width is half the paper width, and canonical support radius is half the
paper radius.  Therefore

```math
\boxed{
\limsup_{d\downarrow0}d^3\log W(d)
\le\frac{\sqrt3\log3}{8}.
}
```

The canonical one-step gain itself is

```math
\delta_{\rm can}(d)
=\frac12v(2d)
=\frac{8\sqrt3}{9}d^4-\frac{32}{9}d^5+O(d^6).
```

### Borderline fixed-shape consequence

For the fixed polygon `K` of Sections 148 and 150, choose `r>0` with
`r\mathbb B\subset K`.  The row split has gap `d_L=r\alpha_L`, and Section 150 needs
`W(d_L)=o(L)`.  The explicit support constant yields

```math
\log W(r\alpha_L)
\le
\left(\frac{\sqrt3\log3}{8}+o(1)\right)r^{-3}\alpha_L^{-3}.
```

Hence the same-hull add-one theorem holds whenever

```math
\boxed{
\limsup_{L\to\infty}
\frac{\alpha_L^{-3}}{\log L}
<\frac{8r^3}{\sqrt3\log3}.
}
```

This includes `\alpha_L=A(\log L)^{-1/3}` for every

```math
A>\left(\frac{\sqrt3\log3}{8r^3}\right)^{1/3}.
```

That scale was not covered by the previous little-`o` condition.

### Dependencies

- `docs/targets/target-a/10-quantitative-kuperberg-rate.md`, Section 157: exact block
  partition, factor-three nesting geometry, and the definition of `W(d)`.
- `docs/targets/target-a/05-fixed-shape-and-separator-audit.md`, Section 150: the
  conditional criterion `W(r\alpha_L)=o(L)` for fixed-shape same-hull add-one.
- `research/kuperberg_five_block_toeout_exact.py`: exact arithmetic audit of the
  finite nearest-neighbor series.  It is not used as a global-optimality certificate.

## 3. Exact target implication

The direct Schur endpoint is unchanged.  The quantitative free-gap input is strictly
stronger:

```math
W(d)\le\exp\left[
\left(\frac{\sqrt3\log3}{8}+o(1)\right)d^{-3}
\right].
```

The improvement is not merely cosmetic.  Section 157 only concluded from an unspecified
constant that `\alpha_L^{-3}=o(\log L)` was sufficient.  The new explicit constant
covers a nonempty part of the critical scale `\alpha_L^{-3}\asymp\log L`.

The support exponent remains three.  Therefore this theorem does not reach power-law
strain and does not itself make a Section 157 witness exterior-compatible.

## 4. Exact remaining lemma

> **Exterior-compatible finite-gap lemma after Section 160.** At an aligned gap scale
> actually arising in a global Target A monomer domain, prove that a toe-out nested
> witness of support
> ```math
> \exp\left[
> \left(\frac{\sqrt3\log3}{8}+o(1)\right)d^{-3}
> \right]
> ```
> can be protected from every exterior source/scaffold blocker with support `o(D)`,
> or construct a different finite architecture with gain order below four.

A successful instance still has to feed either the exact Schur nullity inequality or a
strict sub-`D` competitor.

## 5. Audit classification

| Claim | Classification | Reason |
| --- | --- | --- |
| Toe-out analytic branch exists | proved | implicit-function Jacobian has determinant `384\sqrt3` |
| Toe-out final packing is feasible | proved for all sufficiently small `d>0` | complete nearest-neighbor margin list plus non-neighbor slack |
| Leading paper gain is `\sqrt3 d^4/9` | proved | analytic expansion of five active equations |
| Gain is eight times Section 157 to leading order | proved | ratio of exact leading coefficients |
| Toe-out move is optimal among all five-block translations | not claimed | numerical scratch suggested it may be locally extremal, but no proof is needed or promoted |
| Support exponent becomes smaller than `d^{-3}` | false for this theorem | gain order remains four |
| Critical `(\log L)^{-1/3}` strain is partly covered | proved | explicit support exponent constant |
| Embedded Target A monomer domain is solved | open | exterior blockers are untouched |

## 6. Regression tests

| Regression | Passed? | Exact reason |
| --- | --- | --- |
| Section 146 witness-cardinality divergence | yes | support and recursive block size still diverge as `d\downarrow0` |
| Exterior-blocker warning | yes | theorem is explicitly free aligned-gap only |
| Same-hull source Hall ceiling | yes | no source Hall surplus is asserted |
| Activation/monomer zero-nullity regression | yes | no activation-rank implication is used |
| Sections 153/156/158 KKT/orthant/coloop no-gos | yes | theorem is independent finite packing geometry |
| Locked cage and planar full-rank response | yes | no cage-to-Schur implication is used |
| Source/scaffold coordinate-independence warning | yes | no independent source is identified with the gap packing |

## 7. Failed route / useful negative observation

The initial scratch question was whether a different rigid-block direction could lower
the quartic order.  Direct constrained optimization did not find a cubic or quadratic
middle lift.  It instead exposed the toe-out branch above.  The current proof makes no
universal quartic-optimality claim, so this negative observation remains unpromoted.

A future exact contact-cone calculation could ask whether every sufficiently small
rigid translation of this fixed five-block partition has `v=O(d^4)`.  Such a theorem
would close optimization of this architecture and force any exponent improvement to
use a different partition.

## 8. Literature imported

None.  The only external architecture used is already part of the promoted Section 157
Kuperberg reconstruction.  No new web theorem is invoked.

## 9. Computation and reproducibility

Script:

```sh
python3 research/kuperberg_five_block_toeout_exact.py
```

Arithmetic is exact in truncated `\mathbb Q(\sqrt3)[[d]]` through degree five, using
only `fractions.Fraction`.  The script reconstructs the five blocks at sizes
`n=3,4,6,10`, enumerates every crossing nearest-neighbor edge, verifies that the five
active margin families vanish through degree five, and verifies a positive leading
coefficient for every other margin family.  It also checks the two displayed leading
coefficients of `v`.

The script does not prove the implicit-function theorem, non-neighbor clearance,
recursive containment, exterior compatibility, or global minimum-diameter optimality.
Those are handled analytically where claimed, and remain open where stated.

## 10. Canonical promotion recommendation

**Promote now.**  The proof is complete and changes the quantitative free-gap frontier.

Files to update:

- add `docs/targets/target-a/12-toeout-kuperberg-improvement.md` as Section 160;
- update `docs/targets/target-a/README.md`;
- update `docs/README.md` and `docs/KNOWLEDGE_MAP.md`;
- document the verifier in `research/README.md`;
- refresh the active continuation prompt so future runs use the explicit support
  constant and critical logarithmic-strain regime.

## 11. Next run

Highest-value geometric theorem:

> Prove a protected-core/exterior-compatibility criterion whose required clean radius
> is compared directly with the Section 160 support bound at a gap scale forced by the
> source/scaffold geometry.

If the source geometry only supplies polynomially small gap widths, the unchanged
`d^{-3}` exponent will still be too expensive.  In that case the next architecture
search should target a cubic-or-better one-step gain rather than another constant
improvement.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN

Strongest new theorem:
The Section 157 five-block partition has a toe-out rigid translation with paper-unit
one-step gain v(d)=sqrt(3)d^4/9-2d^5/9+O(d^6), eight times the old leading gain.
It yields limsup d^3 log W(d) <= sqrt(3)log(3)/8 in canonical units.

New fixed-shape regime:
limsup alpha_L^{-3}/log L < 8r^3/(sqrt(3)log 3) implies same-hull add-one.
Thus a nonempty part of alpha_L ~ (log L)^(-1/3) is now proved.

Exact endpoint now:
dim ker S >= Delta_Lambda-d_int, or a strict sub-D competitor; unchanged.

Binding missing lemma:
Exterior-compatible embedding/protection of the finite gap witness, or a different
architecture with gain order below four.

Authoritative new files:
docs/targets/target-a/12-toeout-kuperberg-improvement.md
research/kuperberg_five_block_toeout_exact.py
docs/reports/toeout_kuperberg_improvement_2026-08-30.md
```
