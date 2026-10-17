# Target C — bounded-face fan crossing budget (density-floor claim retracted)

**Date:** 2026-09-12  
**Status:** rejected density-floor derivation; finite pair lemma retained.
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

The bounded-face train fan gives a global pair-count inequality, not only a local
endpoint exclusion. If `d_F` is the number of terminal train occurrences on a bounded
nonquadrilateral face `F`, then

\[
\boxed{
\sum_F {d_F\choose2}\le {T\choose2}-R,
}
\tag{1.1}
\]

where `T` is the complete stopped-train count and `R` is the strict-rhombus count.
The left side counts train pairs forced to be noncrossing by the endpoint fan. The
bounded-face endpoint-simplicity theorem prevents one pair from being counted at two
faces.

**Retraction.** The finite inequality above is valid, but the density consequence
below is not. In the canonical normalization `T=O(D)` and `f=O(D)`, so dividing
`20f<=T(T-1)-2R` by `D^2` makes the left side `o(1)`, not `20(f/D)`. The displayed
claim (1.2) and the normalized equations in Sections 3--5 are withdrawn. See
[`target_c_fan_pair_normalization_retraction_2026-09-12.md`](target_c_fan_pair_normalization_retraction_2026-09-12.md).

The original report claimed that combining (1.1) with the all-regime phase floor
gave the following proof-only Type-II consequence. That consequence is withdrawn:

\[
\boxed{
\liminf_{D\to\infty}{q-k\over D}
\ge
t_{\rm fan}:=
\sqrt{2\Delta_2+10\gamma}-(\gamma)
=1.935992783971307\ldots,
}
\tag{1.2}
\]

where

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
\gamma=2\sqrt{\Delta_2}-{pi\over2}.
\]

The displayed constant is historical provenance only. The finite inequality does not
currently improve any density floor, and the remaining higher-density Type-II branch
and macroscopic-container branch are open.

The candidate implication chain is

```text
bounded-face endpoint fan
  -> bounded-face pairs are missing train crossings
  -> Jensen face-degree bound
  -> finite relation between f, T, and R
  -> possible future near-Mantel argument (not supplied here).
```

## 1. Exact train-pair count

Use the canonical train decomposition of the nonisolated positive-contact core,
including singleton trains. Every strict-rhombus face is one crossing of two complete
trains, and the train pseudosegment geometry makes two distinct trains cross at most
once. Hence the train-crossing graph has `T` vertices and exactly `R` edges.

For a bounded nonquadrilateral face `F`, let `d_F` count terminal train occurrences on
its occurrence-counted boundary. The no-loop theorem ensures one train contributes at
most one occurrence to `F`. The bounded-face endpoint fan says every two trains
incident with `F` are noncrossing. If a pair were incident with two bounded faces, the
two trains would join the same pair of bounded faces, which is excluded by bounded-face
endpoint simplicity. Therefore all pairs counted by the numbers `{d_F\choose2}` are
distinct noncrossing pairs. The total number of noncrossing train pairs is
`{T\choose2}-R`, proving (1.1).

All counts use physical face occurrences. Contact-isolated source points are retained
and do not enter the train graph or the core rigidity matrix.

## 2. Jensen conversion to a scalar inequality

Put

\[
I:=\sum_Fd_F=4f+Q.
\tag{2.1}
\]

Here `f` is the number of bounded nonquadrilateral faces and
`Q=sum_F(deg F-4)`. Since every such face has degree at least five,

\[
Q\ge f,
\qquad I\ge5f.
\tag{2.2}
\]

Jensen's inequality gives

\[
\sum_F{d_F\choose2}
=\frac12\left(\sum_Fd_F^2-I\right)
\ge\frac12\left({I^2\over f}-I\right).
\tag{2.3}
\]

For `I\ge5f`, the expression on the right is increasing in `I`, so

\[
\sum_F{d_F\choose2}\ge10f.
\tag{2.4}
\]

Combining (2.4) with (1.1) yields the exact finite inequality

\[
\boxed{
20f\le T(T-1)-2R.
}
\tag{2.5}
\]

The harmless `-T` term is retained in the finite formula and disappears after
division by `D^2`.

## 3. Normalized Type-II relations

Take a Type-II survivor sequence and pass to a subsequence on which the relevant
normalized quantities converge. Write

\[
t={q-k\over D},
\qquad
\kappa={k\over D},
\qquad
\varphi={f\over D},
\qquad
x={T\over D}=t+2\varphi.
\tag{3.1}
\]

The all-regime proof-only phase theorem gives

\[
{T-q\over D}\ge\gamma-o(1).
\tag{3.2}
\]

Since `q/D=t+\kappa` and the exact train ledger is `T-q=2f-k`, (3.2) gives

\[
\boxed{
2\varphi-\kappa\ge\gamma.
}
\tag{3.3}
\]

The Type-II force-hull perimeter limit and the exact loaded-hull identity give

\[
Q/D=2t-b/D\le2t-\pi+o(1).
\tag{3.4}
\]

Since `f\le Q`,

\[
\boxed{
\varphi\le2t-\pi+o(1).
}
\tag{3.5}
\]

Finally, `R/D^2\to\Delta_2`. Dividing (2.5) by `D^2` gives

\[
\boxed{
20\varphi\le(t+2\varphi)^2-2\Delta_2.
}
\tag{3.6}
\]

## 4. Excluding every `t<t_fan`

Define

\[
z:=\gamma+\kappa,
\qquad
\varphi_0:={z\over2}.
\tag{4.1}
\]

Equation (3.3) gives `varphi>=varphi_0`. Equation (3.5) and this lower bound imply

\[
z\le4t-2\pi+o(1).
\tag{4.2}
\]

For fixed `t`, define

\[
F_t(\varphi):=(t+2\varphi)^2-20\varphi-2\Delta_2.
\tag{4.3}
\]

Assume along a subsequence that `t<t_fan`. Since

\[
t_{\rm fan}=\sqrt{2\Delta_2+10\gamma}-\gamma,
\tag{4.4}
\]

we have `5t_fan-2pi<5`. Using (3.5), every admissible `varphi` satisfies

\[
t+2\varphi\le5t-2\pi+o(1)<5
\]

after choosing the strict gap from `t_fan`. Thus `F_t` is strictly decreasing on the
admissible interval, because

\[
F_t'(\varphi)=4(t+2\varphi)-20<0.
\tag{4.5}
\]

Therefore `F_t(varphi)<=F_t(varphi_0)+o(1)`. The inequality `F_t(varphi)>=0`
required by (3.6) implies

\[
t+z\ge\sqrt{2\Delta_2+10z}+o(1),
\qquad	ext{or}qquad
t\ge g(z)+o(1),
\tag{4.6}
\]

where

\[
g(z):=\sqrt{2\Delta_2+10z}-z.
\tag{4.7}
\]

The admissibility bound (4.2), together with `t<t_fan`, gives

\[
\gamma\le z<4t_{\rm fan}-2\pi<1.461.
\tag{4.8}
\]

On this interval,

\[
g'(z)={5\over\sqrt{2\Delta_2+10z}}-1>0,
\tag{4.9}
\]

so `g(z)>=g(gamma)=t_fan`. Equation (4.6) contradicts `t<t_fan`.

The original proof claimed (1.2), but that step used the invalid normalization
described above. The endpoint and monotonicity calculations are retained only as
arithmetic provenance; they do not imply a density floor.

## 5. Frontier effect

The exact pair-count inequality is stronger than a local endpoint check: it uses the
fan for every bounded face and the complete train crossing graph. It could become
useful in a near-Mantel regime with only `O(D)` missing train pairs, but that regime
has not been proved by this note.

It does not close C-II. The remaining Type-II values above this floor can still pay
the current aggregate detour/payment ledger, and the Type-I inactive-container branch
is untouched. A full closure still needs a detour upper bound, an exact triangle, or
a source-preserving strict diameter decrease.

**Classification:** rejected density-floor derivation. The finite fan pair inequality
and its endpoint-fan dependencies remain retained as proof-only structural material.
