> Generated reading edition · [exact source](../../research/target_c_fan_train_hull_scalar_floor_2026-09-12.md) · source SHA-256 `b98b604952bc02e2cd4e1248d39ad1384bf10d72d0391efa0c36c6699bb9038b`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "67d4026d54f8f737ffd8586b79a41bcf65230abf", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_fan_train_hull_scalar_floor_2026-09-12.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "61162edcd16c8b70a459a6152b6cb5a7e14d51df3511aef0d6de3478c6507da4"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C — fan/train/hull scalar floor (retracted)

**Date:** 2026-09-12  
**Status:** rejected density-floor derivation; finite pair lemma retained.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The bounded-face fan pair budget was claimed to become substantially stronger when it
was combined with the audited two-half-disk atomic train floor and the canonical
Type-II outer ledger. The resulting density floor is withdrawn below.

**Retraction.** This conclusion is withdrawn. The finite fan inequality has a term
`20f=O(D)`, whereas the train-pair budget is `T(T-1)-2R=O(D^2)`. Its division by
`D^2` cannot produce `20(f/D)`; the convex elimination below therefore has no valid
load-bearing inequality. See the normalization correction report.

```math
\boxed{\liminf_{D\to\infty}{q-k\over D}\ge t_* =
2.5147823986\ldots,}
```

where, with

```math
\Delta_2={\pi\over2\sqrt3},
\qquad C=2\sqrt{2\Delta_2}=2.6935473741\ldots,
```

```math
t_*={20\pi+40+\sqrt{1600-400\pi+200\Delta_2}\over50}.
```

The displayed constant is historical provenance only. It does not improve the earlier
ledger, does not exclude the higher-density Type-II branch, and does not address the
Type-I inactive-container branch.

## 1. Candidate implication chain

```text
bounded-face fan pair budget
  + two-half-disk atomic train floor
  + f <= Q <= 2(q-k)/D - pi + o(1)
  -> attempted convex scalar obstruction (invalid after normalization correction).
```

The important direction is the upper bound on `Q`; no equality `b/D=pi` is used.
The proof only needs the canonical Type-II estimate
`Q/D <= 2(q-k)/D - pi + o(1)`.

## 2. Normalized inequalities

Pass to a Type-II survivor subsequence with limits

```math
t={q-k\over D},\qquad \phi={f\over D},\qquad
\kappa={k\over D},\qquad {T\over D}=t+2\phi.
```

The audited fan package gives

```math
20\phi\le (t+2\phi)^2-2\Delta_2+o(1).
\tag{2.1}
```

The two-half-disk atomic train theorem gives

```math
{T\over D}-{q\over2D}\ge C-o(1).
\tag{2.2}
```

Since `q/D=t+\kappa`, (2.2) implies

```math
\phi\ge {C\over2}-{t\over4}+{\kappa\over4}-o(1)
\ge a(t)-o(1),
\qquad a(t):={C\over2}-{t\over4}.
\tag{2.3}
```

The canonical Type-II outer ledger gives

```math
{Q\over D}\le 2t-\pi+o(1).
\tag{2.4}
```

Because every bounded nonquadrilateral face contributes at least one unit to `Q`,
`f<=Q`, so

```math
\phi\le b(t)+o(1),
\qquad b(t):=2t-\pi.
\tag{2.5}
```

## 3. Convex obstruction

Rewrite (2.1) as

```math
H_t(\phi):=(t+2\phi)^2-20\phi-2\Delta_2\ge-o(1).
\tag{3.1}
```

The function `H_t` is convex in `\phi`. If the interval in (2.3)--(2.5) is
nonempty, then `a(t)<=b(t)+o(1)`, and hence

```math
t\ge t_0-o(1),
\qquad t_0:={2C+4\pi\over9}=1.9948294847\ldots.
\tag{3.2}
```

At the lower endpoint,

```math
H_t(a(t))=\left({t\over2}+C\right)^2-10C+5t-2\Delta_2.
\tag{3.3}
```

This is strictly increasing in `t`, and certified bounds give
`H_{t_*}(a(t_*))<-0.56`. Thus it is negative throughout the relevant interval
`[t_0,t_*]`.

At the upper endpoint,

```math
H_t(b(t))=(5t-2\pi)^2-20(2t-\pi)-2\Delta_2=:J(t).
\tag{3.4}
```

The quadratic `J` is convex. Its larger root is exactly `t_*`, while certified
evaluation gives `J(t_0)<-5.15`. Therefore `J(t)<0` for every
`t\in[t_0,t_*)`.

Consequently, for `t<t_*`, both endpoint values of the convex function `H_t` are
strictly negative. Every admissible `\phi` between `a(t)` and `b(t)` then has
`H_t(\phi)<0`, contradicting (3.1). The `o(1)` terms do not affect the argument:
for a fixed strict gap `t_* - t`, the endpoint negativity is uniform along the
subsequence.

Hence

```math
\liminf {q-k\over D}\ge t_* =2.5147823986\ldots.
```

## 4. Scope and remaining obstruction

This retracted candidate used only the audited bounded-face endpoint fan/pair count,
the proof-only two-half-disk groupwise atomic train floor, and the canonical Type-II
outer-hull estimate. It identifies no geometric source, controls no Type-II limits,
and does not touch Type-I.

Contact-isolated source points remain retained in the source and are not inserted
into the train graph.

**Classification:** rejected density-floor derivation; finite fan pair lemma retained.
