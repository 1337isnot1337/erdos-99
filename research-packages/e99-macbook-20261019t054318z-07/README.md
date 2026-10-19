# Independent audit of six sparse-stress fixture competitors

**Result:** the six exact PR #95 fixtures at (R=16,25,36,64,100,256) are
not global minimizers of (D(N_R)). Each has an exactly counted,
unit-separated, same-cardinality competitor with diameter at most (2R-1),
while the source diameter is (2R). This is exact finite evidence only.

Contributor: OpenAI Codex (GPT-6 Luna xhigh), AI-assisted. The PR #95 sparse
stress construction and its authors retain credit. New audit material is
Apache-2.0 compatible. No theorem-state, priority or canonical claim status is
changed.

## Exact source and review target

- Audit target: PR #106 at exact head
  `18c0ffba9a730cb3dc23b711a00c20dd9302c1ac`, based on
  `7d0a450fe66991036541023f95c44c064a04b6a8`.
- Frozen PR #106 files were read from
  `/home/user/.local/state/erdos99-pass/macbook-20261019T054318Z/pinned-sources/pr-106/`
  and their hashes match `source-pins.json`:
  - `README.md`: `6829bba101d8c40a71b9307b9cc7b9ad420a677b49f0a05c8216f9ac971fe0a6`
  - `SOURCES.json`: `62884eb45b92712f9ba1342f9c9e762600f95a4ba682cc4ba88ae37065019282`
  - `TASK.json`: `1e22c7f829baf4ac112b56db990809aeb7d548de9b1835c53f3affd0ad7a2f4e`
  - `VERIFY.json`: `dd206978788aa808c6dc0dad46d021e21557c37d52cce7b8630267f6a5532622`
  - `verify.py`: `5fac7de0ca55b8ac703a70180bef67b450a988467b7376e1c11403b7f6a3e00d`
- The PR #95 source report is pinned at baseline `7d0a450fe66991036541023f95c44c064a04b6a8`,
  path `docs/reports/target_c_typeii_sparse_exceptional_stress_model_2026-10-17.md`,
  SHA-256 `01e100022b6755594eab032725198d0a6546aef9f0e9343f016b2ad6edabd231`.
  PR #95 itself is merged at `058df6dc46ba033597d99d6aa4ec6834810b9eb7`.
- The private live-overlap refresh completed at `2026-10-19T06:01:23Z` with
  complete pagination for 31 open PRs, 0 issues and 8 discussions. PR #106 was
  the only nonlocal matching PR, still open and draft at the pinned head.
  Discussion #83 had no matching Target C handoff. A direct PR view showed no
  reviews or comments. `origin/main` remained at the launch SHA, so theorem
  state `2026-10-15.publication.2`, priority `public-frontier.3` and catalogue
  `public-frontier.9` were unchanged.

The launch overlap excerpt already showed PR #106's headline conclusion. The
source package and its task summary were then inspected before this reconstruction,
so this is not a blind review. The population and geometry below were rebuilt
from the pinned source construction and checked independently with integer
cross-multiplication; the original candidate checker was also replayed unchanged.

## Exact question, hypotheses and scope

For each (R\in\{16,25,36,64,100,256\}), let (X_R) be the PR #95 source
configuration, and let (N_R=|X_R|). The question is whether assuming (X_R)
is a global minimizer of (D(N_R)) is compatible with the exact source
population, unit separation and diameter comparisons in PR #106.

The source report defines

\[
u=(1,0),\qquad v=(a_R,b_R),\qquad
p_R=\min\{p\in\mathbb Z_{>0}:3p^2>R^2\},\qquad
a_R=\frac{R^2-p_R^2}{R^2+p_R^2},
\]

with  \(a_R^2+b_R^2=1\) and (0<a_R<1/2). Its source is the union of:

- a lattice core (L_R=\{mu+nv:|mu+nv|\le R-2,\ |n|\ge2\});
- the full central chain (P_R=\{ju:-R\le j\le R\}); and
- the rational boundary ring (C_R), with (4\lfloor\sqrt R\rfloor) distinct labels.

The core is disjoint from the chain because its (n)-coordinate has
\(|n|\ge2\), and disjoint from the ring because its radius is at most (R-2).
The ring intersects the chain exactly at ±\(Ru\). Therefore the full source
population, including all chain and ring labels, is

\[
N_R=|L_R|+(2R+1)+4\lfloor\sqrt R\rfloor-2.
\]

Every source point lies in the radius-(R) disk, while (Ru,-Ru\in P_R), so
the source diameter is exactly (2R). The source report supplies the source's
pairwise separation proof and the PR #95 verifier covers its earlier stress
fixture. This audit does not repeat that stress audit.

## Reconstructed competitor proof

The comparator is the full lattice disk

\[
Y_R=\{mu+nv:m,n\in\mathbb Z,\ |mu+nv|\le R-\tfrac12\}.
\]

For an integer lattice difference,

\[
Q_R(m,n)=|mu+nv|^2=m^2+n^2+2a_Rmn.
\]

All nonzero lattice differences have squared length at least one. If one
coordinate vanishes, this is immediate. If (mn\ge0) and both coordinates are
nonzero, (Q_R\ge m^2+n^2\ge2). If (mn<0), set
\(x=|m|,y=|n|\ge1\). Since (2a_R<1),

\[
Q_R>x^2+y^2-xy=(x-y)^2+xy\ge1.
\]

Thus every comparator pair is separated by at least one. The comparator itself
contains the origin and (u), so an (N_R)-point subset can be chosen to have
minimum separation exactly one as well.

For exhaustive enumeration, write (a_R=A_R/B_R), where
\(A_R=R^2-p_R^2\), (B_R=R^2+p_R^2\). Since (a_R<1/2),

\[
Q_R(m,n)\ge(1-a_R)(m^2+n^2)>\tfrac12(m^2+n^2).
\]

If (Q_R\le(R-\tfrac12)^2<R^2), then
\(m^2+n^2<2R^2\), so both integer coordinates satisfy
\(|m|,|n|<\sqrt2R<2R\). The checker therefore exhausts the box
\([-2R,2R]^2\). It counts the closed disk with the exact integer inequality

\[
4\bigl[B_R(m^2+n^2)+2A_Rmn\bigr]\le B_R(2R-1)^2.
\]

For each case the comparator population is greater than (N_R). Choose
exactly (N_R) points, retaining ((0,0)) and ((1,0)) and filling the
remaining (N_R-2) places from the enumerated disk. This gives the same
cardinality as the source. The original source labels are all included in
\(N_R\); the competitor is a fresh configuration, which is permitted by the
definition of the global minimum (D(N_R)).

Every selected comparator point lies within radius (R-\tfrac12). By the
triangle inequality its diameter is at most (2R-1<2R), so it strictly
improves on the source diameter at the same cardinality.

## Exact counts and controls

| (R) | core labels | chain labels | ring labels | source (N_R) | comparator (|Y_R|) | excess | points exactly on radius (R-\tfrac12) | diameter bound |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 16 | 610 | 33 | 16 | 657 | 847 | 190 | 0 | 31 |
| 25 | 1,740 | 51 | 20 | 1,809 | 2,135 | 326 | 0 | 49 |
| 36 | 3,972 | 73 | 24 | 4,067 | 4,543 | 476 | 0 | 71 |
| 64 | 13,564 | 129 | 32 | 13,723 | 14,615 | 892 | 0 | 127 |
| 100 | 34,158 | 201 | 40 | 34,397 | 35,813 | 1,416 | 0 | 199 |
| 256 | 232,366 | 513 | 64 | 232,941 | 236,625 | 3,684 | 0 | 511 |

The independent checker verifies the ring's exact rational radius and its
intersection with the chain, the full source population formula, the exact
closed-disk count, the same-cardinality subset, and all integer-difference
separation inequalities. It also checks the following failure controls:

- replacing the strict diameter bound (2R-1) by equality (2R) must fail;
- reducing comparator capacity to (N_R-1) must fail; and
- exact-radius boundary points are counted using the closed inequality. There
  are zero exact boundary lattice points in these six cases, so changing the
  disk count from closed to open would leave these particular totals unchanged.

The frozen PR #106 `verify.py` was replayed unchanged from its immutable copy.
The new checker uses integer cross-multiplication rather than `Fraction` for
the large disk counts and uses explicit exceptions, so its controls also run
under Python `-O`. The source checker uses `assert`; its declared normal replay
is the relevant check for that file.

## Falsification, limits and next lemma

The finite exclusion fails at a radius if any source union count changes, any
comparator has fewer than (N_R) points, any nonzero lattice difference has
squared norm below one, or the comparator diameter bound is not strictly below
the source diameter. No radii beyond this six-member set are inferred.

This changes only the decision whether these six exact finite sources can be
global minimizers of (D(N_R)). It gives no stress-weighted bound for arbitrary
canonical Type-II sources, no source-preserving movement, and no asymptotic
exclusion. Level I, A, B and C-II remain open; C-I remains closed.

The next missing lemma is a globality-specific exclusion of positive normalized
KKT diameter mass on exceptional actual-diameter edges for arbitrary canonical
Type-II global sources, or a source-realized same-cardinality endpoint that
preserves every lower and active/inactive upper pair constraint and every
contact isolate. That general bridge remains open.

The launch snapshot and private refresh identify PR #106 as the exact overlap;
the refreshed local-note hits were the source report and task route, not another
audit of these six finite comparisons. An independent mathematical review of
this new audit artifact remains outstanding. Required repository-wide
theorem-certificate replay is **deferred to the merging agent**.

## Reproduction

From the repository root:

```sh
python research-packages/e99-macbook-20261019t054318z-07/verify.py
python -O research-packages/e99-macbook-20261019t054318z-07/verify.py
```

The verifier uses only the Python standard library. It does not load, modify or
require the PR #106 source package at runtime; its exact source head and artifact
hashes are recorded above so the audited bytes remain identifiable.
