> Generated reading edition · [exact source](../../research/audit_target_c_explicit_atomic_gap_166.md) · source SHA-256 `1cf0f30c0f94434dce2efae8aabb677b21426b39a1c3425c1590f9fe1375337a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "225807ec077c24322c41da590836e2cc108f7fa7", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/audit_target_c_explicit_atomic_gap_166.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "06e22a42825b3aadb90858d43fcf44139099e273964d0a82ab257234e12cf9e9"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Hostile audit — Target C §166 explicit atomic Mantel gap

**Disposition:** PASS at audited-working proof-only scope.  
**Level I / C-II:** still open.

This audit independently rechecks the two new ingredients in §166: the explicit
`sqrt(rho)` robust-grid loss and the quantitative extraction of a large opposite atom
pair from one near-Mantel orbit.

## 1. Quantitative robust-grid loss

Let the two pre-pruning family sizes be `aD+o(D)` and `bD+o(D)`, with at most
`rho D^2+o(D^2)` missing cross pairs.

The tie-safe inversion pruning removes at most

$$
\sqrt\rho\sqrt{a/b}\,D+o(D)
$$

from the first shore and

$$
\sqrt\rho\sqrt{b/a}\,D+o(D)
$$

from the second. This is the exact Markov bound

$$
\sqrt{M|A|/|B|},\qquad \sqrt{M|B|/|A|}.
$$

With missing-degree threshold `sqrt(rho)D`, a second Markov pruning removes at most
`sqrt(rho)D+o(D)` vertices from each shore. Every retained train then misses at most
`sqrt(rho)D+o(D)` retained opposite trains.

Thus the two vertex-pruning costs total

$$
\sqrt\rho\left(\sqrt{a/b}+\sqrt{b/a}+2\right)D+o(D),
$$

and the two corner-degree deficits in the projected path cost another
`2sqrt(rho)D+o(D)`. Hence the total coefficient is exactly

$$
\sqrt{a/b}+\sqrt{b/a}+4.
$$

The explicit size condition in §166.5 ensures every pair and every triple on either
retained shore has a common opposite neighbor. Therefore the §163 `K_{2,2}` order
consistency and triple-transitivity proof still applies. No completeness assumption is
reintroduced.

## 2. Maximum-degree near-Mantel estimate

For a finite triangle-free graph with

$$
e=n^2/4-d,
$$

choose a maximum-degree vertex and set `X=N(v)`, `Y=V\X`. Then `X` is independent and

$$
e(X,Y)+2e(Y)\le |X||Y|.
$$

Therefore

$$
e\le |X||Y|,
\qquad
\bigl||X|-n/2\bigr|\le\sqrt d,
$$

and

$$
e(Y)\le |X||Y|-e\le d.
$$

The number of missing `X x Y` pairs is consequently

$$
|X||Y|-e(X,Y)
=|X||Y|-e+e(Y)
\le2d.
$$

These constants are exact.

For three atom windows, every same-window `X x Y` pair is missing because projective
window diameter is below `pi/3`. Thus each window's minority shore population is at
most `sqrt(2 delta)D`. After deleting the three minorities, each shore retains at least

$$
L_*D,
\qquad
L_*={M\over2}-(1+3\sqrt2)\sqrt\delta.
$$

With at most three nonempty assigned windows spread over two nonempty shores, one shore
has a single window of mass at least `L_*`, and the other has a window of mass at least
`L_*/2`. Their cross missing density is at most `2 delta`.

## 3. Atomic deficit decomposition

For total absolute atomic mass `A=x sigma`, orbit masses `M_r`, crossing masses `E_r`,
and orbit deficits `delta_r=M_r^2/4-E_r`,

$$
{A^2\over4}-s_2^2
={A^2-\sum_rM_r^2\over4}+\sum_r\delta_r.
$$

Every term on the right is nonnegative. Hence every orbit deficit is bounded by the
total scalar deficit. Also, if `M=max M_r`,

$$
MA\ge\sum_rM_r^2\ge4s_2^2,
$$

so `M>=4s_2^2/A`. No compactness or atomic-mass semicontinuity enters this step.

## 4. Conservative numerical contradiction

Assume

$$
A\le2s_2+10^{-4}.
$$

Using only `0.95<s_2<0.96`,

$$
G={A^2\over4}-s_2^2<10^{-4},
$$

hence `delta<10^-4`, `sqrt(delta)<0.01`, and

$$
M>2s_2-10^{-4}>1.8999.
$$

Since `1+3sqrt(2)<5.245`,

$$
L_*>0.94995-0.05245=0.8975.
$$

Thus the chosen atom families can be labeled so that

$$
a\ge0.8975,
\qquad b\ge0.44875,
\qquad a,b<1.9201.
$$

Consequently

$$
\sqrt{a/b}<2.07,
\qquad
\sqrt{b/a}<1.464,
\qquad
\sqrt{a/b}+\sqrt{b/a}<4.
$$

With `rho<=2delta<2e-4`, `sqrt(rho)<0.01415`. The common-neighbor hypotheses are not
close:

$$
\sqrt\rho(\sqrt{a/b}+4)<0.086<0.8975\le a,
$$

$$
\sqrt\rho(\sqrt{b/a}+4)<0.078<0.44875\le b.
$$

The quantitative robust-grid bound therefore gives

$$
a+b<1.155+8(0.01415)=1.2682,
$$

whereas the near-Mantel extraction gives

$$
a+b\ge{3\over2}L_*>1.34625.
$$

The contradiction margin exceeds `0.078` even under these coarse bounds.

## 5. Finite-window quantifiers

The theorem is applied inside one fixed Type-II subsequential limit. For its dominant
orbit, choose continuity neighborhoods around the at most three atoms and then shrink
them to zero. Product domination makes their product boundaries crossing-measure null.
For each fixed neighborhood choice, take the source far enough out that train counts,
crossing counts, and Type-II normalized errors approximate their limiting values. Only
then pass the neighborhood radius down.

Thus the quantitative proof does not take a second weak limit of atomic mass and does
not resurrect the rejected semicontinuity argument from the §164 regression.

## 6. Propagation

With `x sigma > 2s_2+10^-4`, the §142 relation

$$
q/T\le2(1-\sigma)
$$

gives the displayed `10^-4` improvement in `(T-q/2)/D`. The exact ledger
`T-q=2f-k` gives the same improvement in the defect floor. Repeating §146 algebra adds
exactly `(2/9)10^-4` to the weighted diameter-edge coefficient, yielding
`1.819535760201666...`.

**Final verdict:** the explicit value `eta_grid=10^-4` is valid with wide numerical
margin. This strengthens Type II quantitatively but does not close C-II or Level I.
