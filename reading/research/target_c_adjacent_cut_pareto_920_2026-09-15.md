> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_pareto_920_2026-09-15.md) · source SHA-256 `d50d08eba88312977632f1dcf64084afd2ea6be2f4a4e55cbbd9a5ee25563c44`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "a824eda6e3c3b1beefbe9b7a7a57de843d5cd41f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_pareto_920_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "200b0be10ee49a0c2bb21b8ce32c230a73a385c86e2270e8affe81ecaa1aaa67"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — optimized Pareto selection reduces the adjacent cusp to at most 920 switching rows

**Date:** 2026-09-15
**Status:** proof-only source-level structural strengthening
**Scope:** audited `t=(q-k)/D<=1.844` full-core Type-II adjacent-cut backbone
**Dependencies:** audited weighted smallest-leaf center fan; audited adjacent-cut Pareto theorem; exact laminar interval support; global strict-rhombus angular-defect budget; adjacent switching-caterpillar theorem
**Certificate:** `research/verify_target_c_adjacent_cut_pareto_920.py`
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current Pareto theorem uses the parent choices

$$
\lambda=0.677,
\qquad
r=0.488,
$$

and then takes a very asymmetric union-bound threshold to obtain fewer than
`1800+o(1)` switching diameter rows at one phase-close adjacent pair. Those parent
parameters were convenient, but they are not optimized for the switching-row count.

For blocker classification, the useful quantity is the density of the selected
same-center good-leaf path. We can increase that density almost twofold by moving the
center quantile close to the good-leaf threshold while retaining a fixed positive
lower-phase margin.

## Theorem P920

Use the exact constants

$$
A={1851\over2500}=0.7404,
\qquad
W={53\over625}=0.0848,
\qquad
N={1063\over1000}=1.063
$$

from the audited smallest-leaf weighted center-fan theorem. Choose

$$
\boxed{\lambda={6403\over10000}=0.6403}
$$

and choose the top-center quantile `r` by

$$
rN={64029\over100000}=0.64029,
\qquad
\boxed{r={64029\over106300}}.
$$

Then

$$
\boxed{d_{\rm low}=\lambda-rN={1\over100000}}
\tag{P920.1}
$$

and

$$
\boxed{d_{\rm top}=\lambda-(1-r)N={21759\over100000}=0.21759.}
\tag{P920.2}
$$

The retained weight density of good leaf trains is

$$
\begin{aligned}
g
&={ (A-\lambda)W\over N-\lambda}\\
&={53053\over2641875}\\
&=0.0200815708540\ldots .
\end{aligned}
\tag{P920.3}
$$

Averaging good-leaf incidence over the top `r` fraction of center trains therefore
produces one center train crossing a simple good-leaf dual-tree path of density

$$
\begin{aligned}
p
&={d_{\rm top}g\over rN}\\
&={54970487\over8055076875}\\
&=0.00682432804218\ldots .
\end{aligned}
\tag{P920.4}
$$

Thus the path has

$$
m>pD-o(D).
\tag{P920.5}
$$

For its internal boundaries retain the parent notation

$$
N_i=\#\{h:\varepsilon_{h,i+1}\ne\varepsilon_{hi}\},
$$

$$
B_i=\sum_h\beta_h|\varepsilon_{h,i+1}-\varepsilon_{hi}|,
$$

and

$$
Q_i=q_i+q_{i+1}.
$$

The audited global budgets are

$$
\sum_iN_i\le2\pi D,
\tag{P920.6}
$$

$$
\sum_iDB_i\le2D,
\tag{P920.7}
$$

and, because the present choice has `d_low=10^{-5}`,

$$
\sum_iDQ_i
\le {2C_{\rm phase}\over d_{\rm low}}D+o(D).
\tag{P920.8}
$$

Take the fixed thresholds

$$
\boxed{
n={3683\over4}=920.75,
\qquad
b=10^{12},
\qquad
a=10^{13}.
}
\tag{P920.9}
$$

Using the same outward rational enclosures as the parent certificate,

$$
\pi<{355\over113},
\qquad
C_{\rm phase}
<{3258689123681\over612912000000},
$$

the union-bound density of boundaries violating at least one of

$$
N_i<n,
\qquad
DB_i<b,
\qquad
DQ_i<a
$$

is at most

$$
{2\pi^{up}\over n}
+{2\over b}
+{2C_{\rm phase}^{up}\over d_{\rm low}a}
=0.00682409313079\ldots .
\tag{P920.10}
$$

The exact path density is

$$
p=0.00682432804218\ldots,
$$

and the exact companion verifier proves the strict gap

$$
\boxed{
p-
\left(
{2\pi^{up}\over n}
+{2\over b}
+{2C_{\rm phase}^{up}\over d_{\rm low}a}
\right)
>2\cdot10^{-7}.
}
\tag{P920.11}
$$

Hence some internal boundary satisfies simultaneously

$$
N_i<920.75+o(1),
\tag{P920.12}
$$

$$
B_i<{10^{12}\over D}+o(D^{-1}),
\tag{P920.13}
$$

and

$$
d_{\mathbb{RP}^1}(u_i,u_{i+1})
\le Q_i
<{10^{13}\over D}+o(D^{-1}).
\tag{P920.14}
$$

Since `N_i` is an integer, (P920.12) implies that for all sufficiently large members
of the survivor sequence,

$$
\boxed{N_i\le920.}
\tag{P920.15}
$$

By the adjacent switching-caterpillar theorem, those switching rows are exactly the
edges of one layer cut of the full diameter graph and form a caterpillar forest.
Therefore the live finite-cusp obstruction can be sharpened to

```text
at most 920 switching actual-diameter edges
+ bipartite layer-cut support
+ caterpillar-forest structure
+ switching KKT mass = O(1/D)
+ adjacent leaf-phase mismatch = O(1/D)
+ exact two-cut multishear algebra on the active diameter rows.
```

The constants `10^12` and `10^13` are deliberately large. They are fixed constants,
so the multiplier and phase errors still vanish like `D^{-1}`. Their only purpose is
to spend almost all of the path-density budget on lowering the finite switching-row
count.

## 1. Why the parameter change is valid

Call a leaf train good if its center degree exceeds `lambda D`. The weighted-threshold
argument gives good retained weight density (P920.3).

Let `H` be the top `r` fraction of center trains in phase order. The center trains
outside `H` number at most `(1-r)ND+o(D)`. Hence every good leaf has at least

$$
[\lambda-(1-r)N]D-o(D)=d_{\rm top}D-o(D)
$$

neighbors in `H`. Averaging over at most `rND+o(D)` trains in `H` gives one center
train crossing the path density (P920.4).

For the phase-defect estimate, that chosen center train has at most `rND+o(D)` centers
above it in phase order. Each good leaf on its path therefore has at least

$$
(\lambda-rN)D-o(D)=d_{\rm low}D-o(D)
$$

center neighbors on the lower-phase side. The parent angular-defect argument then gives
(P920.8). No step requires `d_low` to be numerically large; only a fixed positive
constant is needed.

## 2. Union-bound proof

Call a boundary count-bad if `N_i>=n`, multiplier-bad if `DB_i>=b`, and phase-bad if
`DQ_i>=a`. The three parent budgets give at most

$$
{2\pi D\over n},
\qquad
{2D\over b},
\qquad
{2C_{\rm phase}D\over d_{\rm low}a}+o(D)
$$

boundaries of the three kinds. Equation (P920.11) makes their union strictly smaller
than the path length (P920.5), so at least one internal boundary is good in all three
senses.

This is the same logic as the audited `1800`-row Pareto theorem; only the upstream
selection parameters and thresholds have changed.

## 3. Scope and finite-motion warning

This theorem is a first-order/interface statement. It does **not** claim that a shear
of size `xi/D` is uniformly feasible for all inactive source pairs. The current main
correctly repaired that earlier finite-amplitude inference because the minimum inactive
pair slack need not be uniform along an unbounded survivor sequence.

What remains exact is:

- the active-diameter derivative algebra;
- the layer-cut/caterpillar classification of the switching rows;
- the `<=920` eventual edge count;
- `O(D^{-1})` switching multiplier mass; and
- `O(D^{-1})` adjacent phase mismatch.

A closure still needs a source-level argument against this finite caterpillar blocker,
or an enlarged motion/replacement that can break controlled old contacts while
preserving unit separation.

**Disposition:** proved proof-only optimized Pareto strengthening of the adjacent
finite-cusp normal form. C-II and Level I remain open.
