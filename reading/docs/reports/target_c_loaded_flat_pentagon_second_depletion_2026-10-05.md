> Generated reading edition · [exact source](../../../docs/reports/target_c_loaded_flat_pentagon_second_depletion_2026-10-05.md) · source SHA-256 `4159c6703e3bd9ae63b0126bf4894f67e16ed7bc67cecb684e543b8b31c4269b`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-BD4BC02420D3","canonical":true,"claim_ids":["C-LOADED-FLAT-PENTAGON-DEPLETION"],"claim_statuses":{"C-LOADED-FLAT-PENTAGON-DEPLETION":"canonical"},"index":"docs/state/artifact-index.jsonl","status":"canonical","target":"target-c"} -->
# Target C — loaded flat pentagons give a physical second-depletion bank

**Date:** 2026-10-05. **Starting main:** f539af073a691c13327a0a7fef3c746fb7704e5f.
**Preceding checkpoint:** 1be5e8112624fb1e4bbc3d7cb18cb24cd5557532.
**State:** 2026-09-14.audit.51.
**Classification:** canonical in `2026-10-05.audit.53` as `C-LOADED-FLAT-PENTAGON-DEPLETION` at the exact branch scope `x_B=b-q=o(D)`. **LEVEL I STATUS: STILL OPEN. C-II REMAINS OPEN.**

## 1. Exact expression changed

In any canonical triangle-free full-core Type-II sequence with
`x_B=b-q=o(D)`, write `e_BI` for actual loaded-to-unloaded contacts,
`g_F=Q-f`, and `k=d_H+s_Z`. There is a family of physical pentagonal
contact faces of size

```math
g_D\ge q-e_{BI}-6g_F-o(D)
\tag{1.1}
```

whose incident stopped trains carry only `o(D^2)` rhombi. Their actual
closure equations have rank exactly `2g_D`, witnessed by two distinct
unit hull singleton columns per face. Deleting them together with all
outer-ended trains, and singleton trains outside this family, gives

```math
\boxed{2(f-g_D)\ge2sD+\sigma_C+S_U-o(D),}
\quad s=\sqrt{\pi/(2\sqrt3)}.
\tag{1.2}
```

Consequently every such survivor satisfies

```math
\boxed{
e_{BI}+6(Q-f)
\ge sD+2k+\frac{\sigma_C+S_U}{2}-o(D).
}
\tag{1.3}
```

This excludes the low-outer-walk branch if its actual loaded attachment
and high-degree budgets lie strictly below the right side. It also gives
second depletion without a small total or local Groemer-residual hypothesis.
The general full-core branch is not closed.

The proved implication is

`almost straight loaded degree-two corner on a unit pentagon`
`-> the complete physical face has the hull phase`
`-> all its incident trains deplete`
`-> its two actual hull columns earn rank two`
`-> (1.2) and the loaded attachment/degree penalty (1.3)`.

Prior art already supplies the limiting triangular trapezoid and the
implication from **small residual to flatness**, in the recovered
[flat-center report](target_c_low_t_flat_center_amplification_2026-09-14.md)
and [three-axis regression](target_c_zero_detour_three_axis_pentagon_regression_provenance_2026-10-04.md).
The new use is the converse forced by actual loaded-hull turning angles,
followed by simultaneous angular-rank second depletion. The old empty
low-`t_D` collar hypotheses are not used.

## 2. Elementary flat-pentagon classification

Let `a,x,b,c,d` be cyclic vertices of a convex unit-edge pentagon, pairwise
unit-separated, with a straight angle at `x`. Normalize

```math
x=(0,0),\qquad a=(-1,0),\qquad b=(1,0).
```

The unit equalities `|c-b|=|d-a|=1` give

```math
|c|^2=2c_x,\qquad |d|^2=-2d_x.
```

Separation from `x` implies `c_x>=1/2`, `d_x<=-1/2`. Since `|c-d|=1`,
both bounds are equalities and `c_y=d_y`. Therefore, up to reflection,

```math
c=(1/2,-\sqrt3/2),\qquad d=(-1/2,-\sqrt3/2).
\tag{2.1}
```

The polygon is the triangular trapezoid, all edge phases agree modulo
`pi/3`, and `x-c`, `x-d` are additional unit pairs in this **limit**.
It has only one straight vertex. Three unit equilateral triangles fill
its convex hull. Every point of a unit triangle is within `2/3<1` of
some vertex, by choosing a barycentric coefficient at least `1/3`.
Hence no sixth unit-separated point can be assigned to this wall.

### 2.1 Uniform converse by compactness

For every `eta>0`, there is `theta(eta)>0` such that a convex,
unit-separated unit pentagon with an angle at least `pi-theta(eta)`
has all five reduced edge phases within `eta` of either edge at that
corner. Its assigned isolate population is empty for sufficiently small
`theta`, and its Groemer residual tends uniformly to zero as `theta->0`.

Otherwise normalize the distinguished corner and one neighboring unit
edge. All five coordinates lie in a fixed bounded set. Unit separation
keeps them distinct in every limit. A subsequence has a straight limiting
corner, so (2.1) determines it. Directions of unit edges, area and convex
hull vary continuously. The limiting three-triangle cover has a fixed
margin below one; the same fan triangles in nearby convex pentagons have
maximum side length below `3/2`, so their barycentric bound still covers
the whole polygon strictly by unit disks about its wall vertices. This
rules out assigned isolates. The limiting area is `3sqrt(3)/4`, and the
five-vertex residual `A/a0-3/2` tends to zero.

There is also a fixed threshold below which **two** distinct corners of
one such pentagon cannot both be almost straight. Otherwise a compactness
limit would have two straight vertices, contrary to (2.1).

Near-unit diagonals remain strict in a finite triangle-free source.
Nothing in this argument creates an exact triangle or force support.

## 3. Select the physical faces from the actual source

Under `x_B=o(D)`, `m_B,u_B=o(D)`, and Type-II disk convergence imply
`q/D->pi`. All but `O(m_B)=o(D)` loaded vertices have both adjacent
actual unit hull contacts. A regular loaded vertex has contact degree
two or three; degree three contributes exactly one loaded-to-unloaded
contact, by the canonical full-core loaded-chord theorem and loaded
contact-degree cap three. Contacts at the irregular vertices are uniformly
bounded, so
the number of regular degree-two loaded vertices is

```math
N_2=q-e_{BI}+o(D).
\tag{3.1}
```

Also discard every remaining regular loaded vertex internal to a new
pocket's contact path. The added-side endpoints were already irregular.
The additional count is at most `sum_P(ell_P-1)=m_B+u_B=o(D)`.
This retains bridge occurrences rather than assuming
every inward sector was originally bounded. For a remaining regular
degree-two vertex, its inward face corner is physical and bounded, since
an old outer corner inside the force hull would become a pocket corner.
This corner equals the loaded hull angle.
Hull turns sum to `2pi`. Discarding vertices whose turn exceeds `D^(-1/2)`
loses at most `2pi sqrt(D)=o(D)` vertices.

A retained degree-two vertex cannot lie on a strict unit-rhombus face:
such a face has all angles below `2pi/3`, whereas its angle here tends to
`pi`. Its bounded face is therefore exceptional. The total occurrence
capacity of degree-at-least-six physical faces is at most

```math
\sum_{m_F\ge6}m_F\le6\sum_{m_F\ge6}(m_F-5)=6(Q-f).
\tag{3.2}
```

At least `q-e_BI-6(Q-f)-o(D)` retained vertices lie on pentagons. For
large `D`, Section 2 makes these pentagons distinct. Mark them, yielding
(1.1). Every isolate remains in the full source; the marked interiors
are actually isolate-free, as just proved, rather than discarded.

## 4. Simultaneous phase and rank depletion

Each marked pentagon has a distinct actual unit hull edge as an anchor.
Its whole contact boundary is within a uniform `eta_D->0` of that anchor's
reduced phase. A fixed phase window has `O(epsilon D)+o(D)` hull anchors,
uniformly in its position. At most five terminal occurrences are charged
per marked face. Coarea and simple crossings therefore show that all
trains incident with marked faces carry `o(D^2)` rhombi.

All outer-ended trains also carry `o(D^2)` rhombi, by the
[terminal short-pocket theorem](target_c_terminal_short_pocket_physical_frustration_2026-10-05.md).
Let `mathcal D` be their union with the marked-face train family. Graph
deletion preserves the full source and removes only `o(D^2)` crossings.

Each marked pentagon has two actual unit hull contacts meeting at its
selected loaded vertex. Each is a singleton train, with an outer and a
pentagonal occurrence. Their angular columns occur only in that
pentagon's closure rows. The two vectors are nonparallel at every finite
strictly convex hull vertex. Thus the submatrix on these columns is block
diagonal of rank `2g_D`; small angles do not reduce this exact rank.

The contact-flex restriction to `mathcal D` is injective modulo
translations, by canonical mixed rigidity and inclusion of every outer
train. Its dimension is `q-k+sigma_C`. The selected closure equations
have rank `2g_D`. The
[marked-face rank argument](target_c_outer_train_rank_groemer_bank_synthesis_2026-10-05.md)
therefore gives

```math
|\mathcal D|\ge q-k+\sigma_C+2g_D.
\tag{4.1}
```

After also deleting the `S_U` singletons outside `mathcal D`, the remaining
train count is at most `2(f-g_D)-sigma_C-S_U`, and its simple triangle-free
crossing graph has `(Delta_2-o(1))D^2` edges. Mantel proves (1.2).
Retaining the independent good-hull count as well gives the stronger
combined bank

```math
2f\ge2sD+\max\{k-m_B,\sigma_C+2g_D\}+S_U-o(D).
\tag{4.1a}
```

Using `f<=Q=q-m_B-u_B-2k` and (1.1) proves (1.3). The equivalent weighted
frontier is

```math
4S+2\sigma_R\ge2(\pi+s)D
+5(\max\{k-m_B,\sigma_C+2g_D\}+S_U)
+2(Q-f)+2(b-P_F)-o(D).
\tag{4.2}
```

Equations (1.2), (1.3) and (4.2) are composed forms of the same source
ledger. Their payments cannot be added again as independent currencies.

## 5. Audit and remaining closure gap

The [exact verifier](../../../research/verify_target_c_loaded_flat_pentagon_second_depletion_2026_10_05.py)
checks strict unit-separated pentagons approaching the flat trapezoid,
all contacts/diagonals, convexity, positive vanishing residual, an exact
interior coverage margin, and the two independent marked unit columns.
It also checks the finite incidence/rank/bank implications on integer
ledgers and the exact formal scalar survivor in the
[live synthesis](../../research/target_c_level1_run_live_synthesis_2026-10-04.md).
The geometry packets have no certified global optimality or
actual loaded support; the ledgers have no asserted plane embedding.

Global optimality is used through canonical mixed rigidity, loaded
contact degree and Type-II reductions, not through an unsupported
activation principle. The marked faces have latent near-unit chords;
these are lower constraints and are not near-diameter pairs.

The surviving low-outer-walk branch must spend at least (1.3) on loaded
attachments or higher-degree face penalties. A collective replacement,
or an additional upper budget contradicting this inequality, is still
required. Other positive-residual full-core regimes and macroscopic
inactive containers remain open. The registered second-depletion claim is canonical in audit.53; it does not settle the Level I quantifiers.
