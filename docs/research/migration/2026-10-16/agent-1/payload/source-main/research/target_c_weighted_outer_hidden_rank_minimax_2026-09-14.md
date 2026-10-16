# Erdos Problem #99 - weighted outer hidden-rank minimax

**Date:** 2026-09-14
**Target:** C-II, canonical full-core Type-II branch
**Dependencies:** weighted outer-flex gate and private-kernel ledger; flat-pentagon closure/hidden-chord normal form
**Claim class:** proof-only structural refinement; no closure claim
**External literature:** no new import

## LEVEL I STATUS

`STILL OPEN`

The weighted outer-flex theorem controls the total private excess

\[
p=\sum_P(r_P-2)_+,
\]

but does not distinguish the directions on which the hidden leaf chords of a flat
pentagon actually move.  The flat-pentagon four-row calculation does.  Combining the
two gives a sharp minimax statement between

1. exact outer-to-outer train shears, and
2. independent first-order variations of hidden near-contact chords inside the
   face-private outer-to-flat contact-flex space.

The combination is substantially stronger than first splitting into an `OO`-rich or
`OF`-rich branch.

The main normalized lower bound is

\[
\boxed{
\max\left\{
 {L_{OO}\over D},
 {\operatorname{rank}(H_{OF}|W_{OF}^{priv})\over D}
\right\}
\ge
{4\over7}F
+{4\over7}{Q-G\over D}
+{2N_1+N_3+2N_4\over7D}
-o(1),
}
\tag{WH.1}
\]

where `F` is the sharp weighted outer-flex floor from the companion theorem,
`G` is the number of good pentagons receiving an outer-to-flat train, and `N_r` is the
number of receiving good pentagons with exactly `r` such trains.

At the current safe endpoint this yields

\[
\boxed{
\max\left\{
 {L_{OO}\over D},
 {\operatorname{rank}(H_{OF}|W_{OF}^{priv})\over D}
\right\}
\ge 0.606510159671885\ldots-o(1).
}
\tag{WH.2}
\]

There is also a useful Pareto relation.  If

\[
k_{out}:={\dim K_{out}\over D},
\qquad
m:=\max\left\{{L_{OO}\over D},
{\operatorname{rank}(H_{OF}|W_{OF}^{priv})\over D}\right\},
\]

then

\[
\boxed{k_{out}+m\ge2F+2{Q-G\over D}+{N_1\over D}-o(1).}
\tag{WH.3}
\]

Consequently, forcing `m` down to its minimax floor does not also make the localized
contact-flex kernel small.  At equality it forces

\[
\boxed{k_{out}\ge {10\over7}F-o(1)
=1.516275399179714\ldots-o(1),}
\tag{WH.4}
\]

which is

\[
\boxed{{3\over7}F
=0.454882619753914\ldots}
\]

above the universal weighted kernel floor `F`.

This quantitatively separates the minimax equality regime from the previously
classified near-minimal-`K_out` regime.

---

## 1. Weighted outer ledger

Use the notation of the weighted outer-flex theorem.  Thus

- `L_OO` counts complete trains with both terminal occurrences on the actual outer
  face;
- `L_OF` counts complete trains with one outer terminal and one terminal on a
  metrically good flat pentagon;
- `r_P in {1,2,3,4,5}` is the number of such outer-to-flat trains ending on a
  receiving good pentagon `P`;
- `G` is the number of receiving good pentagons;
- `N_r` counts those with `r_P=r`; and
- `p=sum_P (r_P-2)_+`.

Normalize by `D`:

\[
x={L_{OO}\over D},
\qquad
\rho={p\over D},
\qquad
n_r={N_r\over D},
\qquad
\bar q={Q\over D}.
\tag{WH.5}
\]

Put

\[
s_2:={1\over D}\sum_P\min(r_P,2).
\tag{WH.6}
\]

Then exactly

\[
{L_{OF}\over D}=s_2+\rho,
\tag{WH.7}
\]

and, since `G=sum_r N_r`,

\[
\boxed{s_2={2G-N_1\over D}.}
\tag{WH.8}
\]

Define the nonnegative outer-slot slack

\[
\boxed{
a:=2\bar q-s_2
=2{Q-G\over D}+n_1\ge0.
}
\tag{WH.9}
\]

On the low-`t`, small-residual Type-II subsequence the weighted gate is

\[
2x+{L_{OF}\over D}
\ge R(t,\delta,\kappa)-o(1),
\tag{WH.10}
\]

where

\[
R=7\pi+3C_g-{27t\over2}+7\delta+{3\kappa\over2},
\qquad
C_g=2\sqrt{\pi/(2\sqrt3)}+0.0021.
\tag{WH.11}
\]

The exact outer ledger gives

\[
\bar q=q_0(t,\delta)+o(1),
\qquad
q_0=2t-\pi-\delta.
\tag{WH.12}
\]

As in the companion theorem, define

\[
\boxed{
F(t,\delta,\kappa)
={R-2q_0\over2}
={9\pi\over2}+{3C_g\over2}-{35t\over4}
+{9\delta\over2}+{3\kappa\over4}.
}
\tag{WH.13}
\]

Substituting (WH.7)--(WH.12) into the weighted gate gives the sharper finite ledger

\[
\boxed{2x+\rho\ge2F+a-o(1).}
\tag{WH.14}
\]

The previous theorem used this mainly to lower-bound `x+rho`.  Here we combine it
with hidden-chord rank.

---

## 2. Local private hidden-rank table

Fix a sufficiently small flat-pentagon neighborhood.  At the limiting flat trapezoid,
write the five boundary train angular rates as

\[
\omega=(\omega_1,\ldots,\omega_5).
\]

The two face-closure rows and the two hidden leaf-chord radial derivative rows have
rank four.  Their common kernel is exactly

\[
\boxed{\operatorname{span}\{(1,1,1,1,1)\}.}
\tag{WH.15}
\]

The nonzero `4 x 4` minor persists after shrinking the fixed flatness neighborhood.
Common rotation remains in the kernel for every actual pentagon, so (WH.15) holds
uniformly throughout that neighborhood.

For one receiving good pentagon `P`, let `J_P` be its set of private outer-to-flat train
columns, `r=|J_P|`, and let

\[
W_P:=\{v:\operatorname{supp}v\subseteq J_P,\ C_Pv=0\}.
\tag{WH.16}
\]

Let `H_P` be the two hidden leaf-chord derivative rows.  Then

\[
\boxed{
\operatorname{rank}(H_P|W_P)\ge h(r),
\qquad
(h(1),h(2),h(3),h(4),h(5))=(0,0,1,2,2).
}
\tag{WH.17}
\]

Indeed, for `r<=4`, extend a vector of `W_P` by zero on the omitted train coordinates.
If its two hidden derivatives also vanish, (WH.15) says that the five-coordinate vector
is a common rotation.  Since at least one coordinate is zero, it is the zero vector.
Thus `H_P` is injective on `W_P`.  Since the closure block has only two rows,

\[
\dim W_P\ge r-2,
\]

which gives the `r=3,4` entries.  For `r=5`, `W_P` has dimension three while the
common kernel of closure plus the two hidden rows is one-dimensional, so the hidden
rank is exactly two.

Different receiving faces use disjoint private outer-to-flat train columns.  Therefore
the blocks sum directly.  With

\[
z:={1\over D}\operatorname{rank}(H_{OF}|W_{OF}^{priv}),
\tag{WH.18}
\]

we obtain

\[
z\ge\sum_{r=1}^5 h(r)n_r.
\tag{WH.19}
\]

The exact finite table identity

\[
h(r)={2\over3}(r-2)_++\gamma(r),
\]

with

\[
(\gamma(1),\ldots,\gamma(5))
=\left(0,0,{1\over3},{2\over3},0\right)
\]

gives

\[
\boxed{
z\ge {2\over3}\rho+\beta,
\qquad
\beta:={n_3\over3}+{2n_4\over3}\ge0.
}
\tag{WH.20}
\]

The coefficient `2/3` is sharp for this local information because an `r=5` block has
three contact-flex coordinates but only two independent hidden radial derivatives; the
missing direction is common rotation.

---

## 3. Weighted minimax theorem

Set

\[
m:=\max\{x,z\}.
\tag{WH.21}
\]

From (WH.20),

\[
\rho\le {3\over2}(m-\beta).
\tag{WH.22}
\]

Together with `x<=m`, the weighted ledger (WH.14) gives

\[
2F+a
\le2x+\rho+o(1)
\le {7\over2}m-{3\over2}\beta+o(1).
\]

Hence

\[
\boxed{
m\ge {4\over7}F+{2\over7}a+{3\over7}\beta-o(1).}
\tag{WH.23}
\]

Using (WH.9) and (WH.20), this is exactly (WH.1):

\[
\boxed{
m\ge {4\over7}F
+{4\over7}{Q-G\over D}
+{2n_1+n_3+2n_4\over7}
-o(1).}
\tag{WH.24}
\]

Thus the worst balanced point of the OO-shear and hidden-rank mechanisms already has a
linear coefficient exceeding `0.6065` at the current endpoint.

---

## 4. Pareto bridge to the total localized kernel

The private-column construction gives

\[
k_{out}:={\dim K_{out}\over D}\ge x+\rho-o(1).
\tag{WH.25}
\]

Since `m>=x`,

\[
\begin{aligned}
k_{out}+m
&\ge x+\rho+m-o(1)\\
&\ge2x+\rho-o(1)\\
&\ge2F+a-o(1).
\end{aligned}
\]

Therefore

\[
\boxed{k_{out}+m\ge2F+a-o(1).}
\tag{WH.26}
\]

This is (WH.3).  In particular, if

\[
m\le {4\over7}F+\varepsilon,
\]

then

\[
\boxed{
k_{out}\ge {10\over7}F-\varepsilon-o(1).}
\tag{WH.27}
\]

So the minimax equality model is separated from the near-minimal-kernel model by a
linear margin `3F/7`.

This matters because the existing exact-two-face network theorem applies when
`k_out=F+o(1)`.  In that regime almost every receiving good pentagon has `r=2` and one
obtains a large simple near-cubic exact-two network.  The minimax equality regime below
has the opposite fingerprint: a linear population of `r=5` pentagons and a much larger
localized kernel.  The two equality mechanisms cannot be conflated.

---

## 5. Equality fingerprint

Assume along a sequence that

\[
m\le {4\over7}F+o(1).
\tag{WH.28}
\]

Then (WH.23) forces

\[
a=o(1),
\qquad
\beta=o(1).
\tag{WH.29}
\]

By their explicit nonnegative decompositions,

\[
{Q-G\over D}=o(1),
\qquad
n_1+n_3+n_4=o(1).
\tag{WH.30}
\]

Thus all but `o(D)` receiving good pentagons have private outer degree

\[
\boxed{r_P\in\{2,5\}.}
\tag{WH.31}
\]

Every inequality used in deriving (WH.23) must also be asymptotically tight.  Hence

\[
x=m+o(1),
\qquad
z=m+o(1),
\qquad
\rho={3\over2}m+o(1).
\tag{WH.32}
\]

Since the only asymptotically surviving positive-excess class is `r=5`,

\[
\rho=3n_5+o(1),
\]

so

\[
\boxed{n_5={m\over2}+o(1).}
\tag{WH.33}
\]

At equality the local hidden rank on those degree-five faces is `2n_5=m`, exactly
matching the OO-shear dimension `x=m`.

The scalar inequalities are therefore sharp under the present inputs.  Improving the
`4/7` coefficient requires new geometry, not tighter algebra on the same ledger.

---

## 6. Structured hidden-null load at minimax equality

Each `r=5` pentagon has a one-dimensional common-rotation mode in its private
three-dimensional contact-flex block.  That mode is annihilated by both hidden
leaf-chord derivative rows.  All OO train shears are also annihilated by the private
hidden rows because their coordinates are disjoint from every bounded-face block.

Therefore the outer-supported hidden-null subspace contains the direct sum of

- all `L_OO` exact OO train shears, and
- one common-rotation vector for every degree-five receiving good pentagon.

If `U_0` denotes this explicit subspace, then

\[
\boxed{{\dim U_0\over D}\ge x+n_5-o(1).}
\tag{WH.34}
\]

Under the minimax equality hypothesis (WH.28), (WH.32)--(WH.33) give

\[
\boxed{{\dim U_0\over D}\ge {3\over2}m-o(1)
={6\over7}F-o(1).}
\tag{WH.35}
\]

At the current endpoint this is

\[
\boxed{{\dim U_0\over D}\ge0.909765239507828\ldots-o(1).}
\tag{WH.36}
\]

The existing mixed-rigidity theorem says that the active-diameter derivative map is
injective on the full contact-flex space modulo Euclidean motions.  Thus any survivor
near minimax equality must in particular block this explicit `0.909765D`-scale
hidden-null family by active diameter rows.  The generators are much more structured
than an arbitrary contact-flex basis: they consist only of OO train shears and one
common face-rotation mode per degree-five flat pentagon.

This is the next natural rank/sign target.

---

## 7. Current numerical endpoint and regression correction

Let

\[
s=\sqrt{\pi/(2\sqrt3)},
\qquad
t_{21}={4\over9}(\pi+s)+0.0017279,
\qquad
C_g=2s+0.0021.
\]

Direct high-precision substitution gives

\[
t_{21}=1.8212414379794447041\ldots,
\]

\[
q_0=2t_{21}-\pi
=0.5008902223690961698\ldots,
\]

\[
R=3.1245660035897932384\ldots,
\]

and

\[
\boxed{F=1.0613927794258004494\ldots .}
\tag{WH.37}
\]

Therefore

\[
\boxed{\Theta:={4F\over7}
=0.6065101596718859711\ldots,}
\tag{WH.38}
\]

\[
\boxed{{10F\over7}
=1.5162753991797149277\ldots,}
\tag{WH.39}
\]

\[
\boxed{{3F\over7}
=0.4548826197539144783\ldots,}
\tag{WH.40}
\]

and

\[
\boxed{{6F\over7}
=0.9097652395078289566\ldots .}
\tag{WH.41}
\]

The symbolic formulas in the companion weighted outer-flex theorem are consistent
with these values.  Its prose Section 6 contains a small last-digit numerical
transcription drift in `R` and `F`; the verifier accompanying this note evaluates the
symbolic formula directly and should be used as the regression authority for these
constants.

---

## 8. What this does and does not solve

The theorem converts the weighted outer-terminal ledger into a much sharper closing
target.

A putative survivor cannot simultaneously have

```text
small OO-shear dimension,
small hidden near-contact rank,
and a near-minimal outer-supported contact-flex kernel.
```

Near the minimax point it instead has a rigid two-species local model:

```text
OO train shears,
degree-2 receiving flat pentagons,
degree-5 receiving flat pentagons,
and one hidden-null common-rotation mode on every degree-5 face.
```

The remaining obstruction is still sign/topology.  Rank alone does not produce a
nonzero contact flex on which all active diameter derivatives are nonpositive.  A
closing theorem must use the straight-line-thrackle structure of the diameter graph,
the train-cut sign formula, or additional near-contact rows to show that active
diameters cannot injectively and sign-compatibly block the structured family in
(WH.34)--(WH.36).

No exact unit triangle, diameter-nonincreasing nonzero flex, or same-cardinality strict
sub-`D` competitor is claimed here.

---

## 9. Scope audit

- The weighted input is exactly the current `2L_OO+L_OF` endpoint gate and
  `Q/D=2t-pi-delta+o(1)` ledger.
- `G` counts only good pentagons receiving at least one outer-to-flat train, so there is
  no spurious `N_0` term.
- The local hidden-rank table is proved in this note from the four-row flat-pentagon
  calculation; it does not require an unmerged research branch.
- Different private face blocks use disjoint outer-to-flat train variables, so their
  hidden ranks sum directly.
- The `4/7` minimax coefficient is sharp for the scalar inputs used here.
- The Pareto relation (WH.26) is independent of hidden-rank sharpness and follows
  directly from the weighted gate plus `m>=x`.
- Numerical constants are recomputed from the symbolic endpoint formulas in the
  companion verifier.
- C-II and Level I remain open.

**Disposition:** proof-only weighted hidden-rank minimax and equality classification.