# Target C — audited §166 explicit all-regime atomic Mantel gap

**Date:** 2026-09-12  
**Lifecycle:** new audited-working proof-only route theorem; theorem-state authority unchanged.  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**

Section §164 proves only the existence of an absolute `eta_grid>0`. This section makes
that gap explicit by quantifying the pruning in the robust near-complete-grid theorem.
The constant below is intentionally conservative.

Put

\[
\Delta_2={\pi\over2\sqrt3},
\qquad
s_2:=\sqrt{\Delta_2}.
\]

The main conclusion is

\[
\boxed{
 x\sigma>2s_2+10^{-4}
}
\tag{166.1}
\]

for every audited-working Type-II train-measure subsequential limit in the §142 scope.
Consequently one may take

\[
\boxed{\eta_{\rm grid}=10^{-4}}
\tag{166.2}
\]

in §164.

---

# 166.1 Quantitative robust-grid lemma

Consider two stopped-train families `A_D,B_D` with

\[
{|A_D|\over D}\to a>0,
\qquad
{|B_D|\over D}\to b>0.
\tag{166.3}
\]

Assume their projective direction supports shrink to two axes separated by exactly
`pi/3`, every present cross-family pair crosses in one actual strict unit rhombus, and
at most

\[
(\rho+o(1))D^2
\tag{166.4}
\]

cross-family pairs are missing, for some fixed `rho>=0`.

Suppose also

\[
a>\sqrt\rho\left(\sqrt{a/b}+4\right),
\qquad
b>\sqrt\rho\left(\sqrt{b/a}+4\right).
\tag{166.5}
\]

Then

\[
\boxed{
a+b
\le {2\over\sqrt3}
+\sqrt\rho
\left(
\sqrt{a/b}+\sqrt{b/a}+4
\right).
}
\tag{166.6}
\]

For `rho=0`, this is §163. The point is the explicit `sqrt(rho)` loss.

## Proof

Write `L=pi/3`. Choose real projective lifts so the two shrinking clusters are centered
at directions differing by `+L`. Put

\[
x_u=\alpha_u,
\qquad
y_v=\beta_v-L.
\]

Every actual strict-rhombus crossing on this branch has `y_v>x_u`; hence every
inversion `x_u>=y_v` is a missing pair.

Let `M_D` be the inversion count. Apply the tie-safe Markov separation used in §163.
If `M_D>0`, with

\[
\epsilon_D={M_D\over |A_D||B_D|},
\qquad
\delta_D=\sqrt{\epsilon_D},
\]

one can obtain strict phase separation by deleting at most

\[
\delta_D|A_D|
=\sqrt{M_D{|A_D|\over|B_D|}}
\]

trains from `A_D` and at most

\[
\delta_D|B_D|
=\sqrt{M_D{|B_D|\over|A_D|}}
\]

trains from `B_D`. Therefore the normalized losses are at most

\[
\sqrt\rho\sqrt{a/b}+o(1),
\qquad
\sqrt\rho\sqrt{b/a}+o(1).
\tag{166.7}
\]

After this phase pruning, the remaining missing-pair count is still at most
`(rho+o(1))D^2`.

Now put

\[
\lambda=\sqrt\rho
\]

when `rho>0`. Delete every remaining train missing more than `(lambda+o(1))D`
opposite-family trains. Markov deletes at most

\[
(\sqrt\rho+o(1))D
\]

trains from each shore. Every retained train then misses at most

\[
(\sqrt\rho+o(1))D
\]

retained trains on the opposite shore.

Thus the retained normalized shore sizes are at least

\[
a-\sqrt\rho\left(\sqrt{a/b}+1\right)-o(1),
\tag{166.8}
\]

\[
b-\sqrt\rho\left(\sqrt{b/a}+1\right)-o(1).
\tag{166.9}
\]

Condition (166.5) ensures that, for all sufficiently large `D`, every two and every
three trains on one retained shore have a common neighbor on the other. Therefore the
§163 local-`K_{2,2}` consistency argument gives one global crossing order on each
shore.

Choose the first retained `A` train and its last retained `B` neighbor, exactly as in
§163. The opposite-corner two-leg path has endpoint distance at most `D`. Every
intervening elementary centerline displacement has positive common projection, whether
or not it belongs to a selected cross-family pair. Hence missing pairs do not create a
negative path contribution.

Each of the two corner trains is missing at most `(sqrt(rho)+o(1))D` opposite retained
trains. Since the direction clusters shrink to axes separated by `pi/3`, the common
projection coefficient tends to `sqrt(3)/2`. The §76 path estimate therefore gives

\[
1
\ge {\sqrt3\over2}
\left[
 a+b
 -\sqrt\rho\left(\sqrt{a/b}+\sqrt{b/a}\right)
 -4\sqrt\rho
\right].
\tag{166.10}
\]

Rearranging proves (166.6). \(\square\)

---

# 166.2 Quantitative near-Mantel extraction inside one atomic orbit

Fix a Type-II train-measure limit and write

\[
A:=x\sigma
\]

for its total atomic train mass in absolute `D` normalization. Group atoms into the
three-point projective orbits of

\[
\phi\mapsto\phi+{\pi\over3}\pmod\pi.
\]

Let `M_r` be the atomic mass of orbit `r`, `E_r` its strict-rhombus crossing mass, and

\[
\delta_r:={M_r^2\over4}-E_r\ge0.
\tag{166.11}
\]

Audited §142 gives

\[
\sum_rE_r=s_2^2,
\qquad
\sum_rM_r=A.
\]

Therefore

\[
\boxed{
G:= {A^2\over4}-s_2^2
= {A^2-\sum_rM_r^2\over4}
 +\sum_r\delta_r.
}
\tag{166.12}
\]

Every term on the right is nonnegative.

Choose an orbit of maximum mass `M`. Since

\[
\sum_rM_r^2\ge4s_2^2
\]

and

\[
\sum_rM_r^2\le M\sum_rM_r=MA,
\]

we have

\[
\boxed{M\ge {4s_2^2\over A}.}
\tag{166.13}
\]

Its Mantel deficit satisfies, directly from (166.12),

\[
\boxed{\delta:={M^2\over4}-E\le G.}
\tag{166.14}
\]

Now freeze arbitrarily small continuity neighborhoods of the at most three atoms in
this orbit and pass far enough along one source sequence realizing the limit. After
normalization, the induced finite triangle-free train graph has vertex mass `M`, edge
mass `M^2/4-delta`, up to arbitrarily small errors.

The following finite estimate is exact. For a triangle-free graph with `n` vertices and

\[
e={n^2\over4}-d,
\]

choose a maximum-degree vertex `v`, put `X=N(v)` and `Y=V\setminus X`. Then `X` is
independent. Since every `y in Y` has degree at most `|X|`,

\[
e(X,Y)+2e(Y)\le |X||Y|.
\]

Hence

\[
e\le |X||Y|
\]

and

\[
\bigl||X|-n/2\bigr|\le\sqrt d.
\tag{166.15}
\]

Also

\[
e(Y)\le |X||Y|-e\le d,
\]

so the number of missing `X x Y` pairs is at most

\[
|X||Y|-e(X,Y)
=|X||Y|-e+e(Y)
\le2d.
\tag{166.16}
\]

Return to the three shrinking atom windows. A single window has projective diameter
below `pi/3`, so two trains in that window cannot cross in a strict triangle-free unit
rhombus. If its normalized populations on `X` and `Y` are `x_r,y_r`, then (166.16)
gives

\[
x_ry_r\le2\delta.
\]

Thus the minority population of each window is at most `sqrt(2delta)`. Assign each
window to its majority shore and discard the minority. By (166.15), each shore retains
at least

\[
\boxed{
L_*:={M\over2}-\sqrt\delta-3\sqrt{2\delta}
={M\over2}-(1+3\sqrt2)\sqrt\delta
}
\tag{166.17}
\]

normalized train mass.

There are at most three window groups and both shores have positive retained mass in
the regime used below. Hence one shore consists of one assigned window, of mass at
least `L_*`, while the other shore contains a window of mass at least `L_*/2`.
Choose those two majority subsets as train families. They have angular widths tending
to zero, axes separated by `pi/3`, and at most

\[
\boxed{2\delta D^2+o(D^2)}
\tag{166.18}
\]

missing cross-family pairs.

---

# 166.3 Excluding `x sigma <= 2s_2+10^-4`

Assume for contradiction

\[
A=x\sigma\le2s_2+10^{-4}.
\tag{166.19}
\]

We use only the elementary safe numerical bounds

\[
0.95<s_2<0.96,
\qquad
\sqrt2<1.415,
\qquad
{2\over\sqrt3}<1.155.
\tag{166.20}
\]

From (166.12), with `epsilon=10^-4`,

\[
G
\le s_2\epsilon+{\epsilon^2\over4}
<9.601\times10^{-5}
<10^{-4}.
\tag{166.21}
\]

Thus by (166.14)

\[
\delta<10^{-4},
\qquad
\sqrt\delta<10^{-2}.
\tag{166.22}
\]

Equation (166.13) gives

\[
M
\ge {4s_2^2\over2s_2+10^{-4}}
>2s_2-10^{-4}
>1.8999.
\tag{166.23}
\]

Therefore (166.17) and `1+3sqrt(2)<5.245` give

\[
L_*
>{1.8999\over2}-5.245(0.01)
=0.8975.
\tag{166.24}
\]

The selected two atom families thus have normalized sizes `a,b` satisfying

\[
a\ge0.8975,
\qquad
b\ge0.44875,
\qquad
a,b\le M\le A<1.9201,
\tag{166.25}
\]

and

\[
\boxed{a+b\ge{3\over2}L_*>1.34625.}
\tag{166.26}
\]

From (166.25),

\[
\sqrt{a/b}
<2.07,
\qquad
\sqrt{b/a}
<1.464,
\]

so

\[
\boxed{
\sqrt{a/b}+\sqrt{b/a}<4.
}
\tag{166.27}
\]

The missing-pair parameter in §166.1 satisfies

\[
\rho\le2\delta<2\times10^{-4},
\qquad
\sqrt\rho<0.01415.
\tag{166.28}
\]

The size hypotheses (166.5) are automatic from (166.25)–(166.28). Applying (166.6)
and (166.27) gives

\[
a+b
<1.155+8(0.01415)
=1.2682.
\tag{166.29}
\]

This contradicts (166.26). Hence (166.19) is impossible and (166.1) follows.

The numerical margin exceeds `0.078`; the proof is not sensitive to the last displayed
decimals.

---

# 166.4 Explicit propagated Type-II floors

Audited §142 gives

\[
{q\over T}\le2(1-\sigma).
\]

Using (166.1),

\[
\boxed{
\liminf {T-q/2\over D}
\ge2s_2+10^{-4}.
}
\tag{166.30}
\]

Since `T-q=2f-k` and `q/D<=pi+o(1)`, also

\[
\boxed{
\liminf {2f-k\over D}
\ge
2s_2-{\pi\over2}+10^{-4}
=0.333929286933018\ldots .
}
\tag{166.31}
\]

Repeating the audited §146 elimination gives

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge
{4\over9}(\pi+s_2)+{2\over9}\,10^{-4}.
}
\tag{166.32}
\]

Numerically,

\[
\boxed{
\liminf {1\over D}
\left(
 h-{d_H\over9}-{10s_Z\over9}
\right)
\ge1.819535760201666\ldots .
}
\tag{166.33}
\]

This is a certified explicit strengthening of §146 and a quantitative version of §164.
It does not by itself close Type II.

---

## Hostile audit / scope

- The proof does **not** use atomic-mass semicontinuity. It works inside one fixed
  Type-II limit and uses finite continuity-window approximations.
- Equation (166.12) is an exact nonnegative decomposition; in particular the dominant
  orbit's Mantel deficit is bounded by the total scalar deficit `G`.
- The finite near-Mantel estimates (166.15)–(166.16) are proved directly from a
  maximum-degree vertex; no unstated stability constant is used.
- Same-window pairs are genuinely noncrossing once the continuity windows have
  projective diameter below `pi/3`.
- The quantitative robust-grid loss includes **both** phase-tail deletion and
  high-missing-degree deletion. The two endpoint degree deficits account for the final
  `+4 sqrt(rho)` term.
- Condition (166.5) explicitly guarantees the pair/triple common neighbors needed to
  globalize crossing order. It is satisfied with wide margin in §166.3.
- Unselected intervening rhombi cannot reduce the projected two-leg path because every
  elementary displacement of a selected train has positive common projection, exactly
  as in §76/§163.
- The conservative bounds in (166.20) imply every displayed numerical comparison with
  substantial slack; no fragile floating-point equality is used.
- Contact-isolated source points remain outside the train/rigidity kernel and are not
  deleted.
- No outer-detour hypothesis is used.

**Disposition:** §166 PASS at audited-working proof-only scope. It makes the §164
all-regime atomic gap explicit with the safe value `eta_grid=10^-4`. C-II and Level I
remain open.
