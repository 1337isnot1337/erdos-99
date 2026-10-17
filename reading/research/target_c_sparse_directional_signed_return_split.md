> Generated reading edition · [exact source](../../research/target_c_sparse_directional_signed_return_split.md) · source SHA-256 `5fa93bfd58bd9cf2f086f7427ce4c684736db8fb7f9eb684aa76f36ee4ad96fc`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

# Target C — sparse/directional splitting in whole-area signed return

**Date:** 2026-09-12  
**LEVEL I STATUS:** **STILL OPEN. C-II REMAINS OPEN.**  
**Status:** proof-only structural strengthening of the audited §§117–118 signed-return machinery; theorem authority unchanged.

The whole-area signed-return argument currently sends every bad train through one
`2 T M_bad` estimate.  That is unnecessarily expensive for endpoint classes whose
**total number** is already small.  A sparse family of bad trains should be charged by
the total transverse area of those trains, at most `d` per train, before the
directional concentration estimate is applied to the genuinely diffuse tooth family.

This note proves that separation exactly and records its correlated-slack consequence.
The result is structural rather than a carrier-decimal claim: it removes an avoidable
multiplication of sparse interface/route defects by the full train population and
isolates the remaining obstruction as directional concentration of boundary teeth.

---

## 1. A two-class bad-train area lemma

Let `R` be a finite edge-to-edge complex of strict unit rhombi inside a convex
container of diameter `d`.  Let `T` be its complete physical trains and let `A_4` be
the total rhombus area.  Every rhombus is the crossing of exactly two complete trains.

Partition the bad trains as

$$
\mathcal B=\mathcal B_s\cup\mathcal B_d,
$$

where

- `B_s` is a **sparse** class, controlled by total cardinality
  `N_s=|B_s|`; and
- `B_d` is a **directional** class, controlled by
  $$
  M_d(\epsilon)
  :=\max_I |\{\tau\in\mathcal B_d:\phi_\tau\in I\}|,
  $$
  where `I` ranges over projective direction intervals of width `epsilon`.

Let

$$
\Delta=\sum_R(\varphi_R-\pi/3)
$$

be the total acute-angle excess of the rhombi.  Let `A_gg` be the total area of
rhombi whose two crossing trains are good.

### Lemma 1.1 — sparse/directional bad-area split

For every `0<epsilon<pi/6`,

$$
\boxed{
A_{gg}
\ge
A_4-dN_s-2|\mathcal T|M_d(\epsilon)-{\Delta\over\epsilon}.
}
\tag{1.1}
$$

### Proof

First remove every rhombus incident to a sparse bad train.  For one complete train
`tau`, write its rhombi in transverse order.  If a rhombus has train-edge direction
`u_tau`, its area is exactly the transverse increment of the opposite train-edge
line.  Summing along `tau` telescopes to the transverse separation of its two terminal
parallel lines, hence

$$
\sum_{R\ni\tau}\operatorname{area}(R)\le d.
\tag{1.2}
$$

Therefore the total area of rhombi incident to at least one train in `B_s` is at most

$$
dN_s.
\tag{1.3}
$$

Now work in the remaining rhombi, so every surviving bad incident train belongs to
`B_d`.  Fix the other crossing train.  If a crossing has angle in
`(pi/3,pi/3+epsilon]`, then the bad train direction lies in one of two projective
intervals of width `epsilon`; hence there are at most `2M_d(epsilon)` such crossings
for that fixed other train.  Summing over all complete trains gives at most

$$
2|\mathcal T|M_d(\epsilon)
$$

near-`pi/3` rhombi incident to `B_d`.  This may overcount and is therefore safe.
Every remaining bad rhombus has angular excess greater than `epsilon`, so there are at
most `Delta/epsilon` of them.  Since every unit-rhombus area is at most one, their
total area is bounded by the same count.  Subtracting (1.3) and these two directional
terms from `A_4` proves (1.1). `square`

### Corollary 1.2 — signed return with a sparse class removed first

Under the same injective physical endpoint assignment as hostile-audited §117, let
`E` be the route excess available to trains with two good ends.  The three-host
return theorem and its area transport proof give

$$
\boxed{
dE
\ge(2-\sqrt3)
\left[
A_4-dN_s-2|\mathcal T|M_d(\epsilon)-{\Delta\over\epsilon}
\right]_+.
}
\tag{1.4}
$$

Nothing in the proof changes the route-assignment multiplicity: every good endpoint
is still assigned to one exact physical boundary occurrence, and every sparse bad
train is removed before any good-good return is counted.

---

## 2. Apply the split to the correlated §118 currencies

Use the exact §118 slack simplex

$$
\boxed{x+y+z+w=\sigma,}
$$

with

$$
x=U-|S|,
\quad y=|S|-2\alpha,
\quad z=2\alpha-C,
\quad w=C-M.
$$

Pass to the common subsequence used by the corrected sharp §118 companion and write
`q,c,s_0` for the normalized limits of `Q_D,c_D,s_D`.  Then

$$
2s_0+c+q\le z,
\qquad q+c\le z.
\tag{2.1}
$$

Also put

$$
C_{tail}\le{x\over2}+{5\over3}w.
\tag{2.2}
$$

### Sparse endpoint classes

Place the following bad trains in `B_s`, choosing one bad physical endpoint occurrence
per train:

1. bounded nonquadrilateral boundary occurrences: at most `5qD+o(D)`;
2. nonprincipal macroscopic routes: at most `(z+C_tail)D+o(D)`;
3. exceptional micro routes: at most `(3z+6c)D+o(D)` in the corrected sharp ledger;
4. the two tiny support spans adjacent to the largest principal gap: at most
   `(20/3)wD+o(D)`.

The first three classes total

$$
(4z+5q+6c+C_{tail})D+o(D).
$$

Since `q+c<=z`,

$$
5q+6c\le6z,
$$

so after adding the tiny spans,

$$
\boxed{
{N_s\over D}
\le
10z+{x\over2}+{25\over3}w+o(1).
}
\tag{2.3}
$$

This is a **total-count** estimate, not a directional supremum.

### Directional tooth class

Leave only the regular two-edge tooth endpoints in `B_d`.  The audited tangent-window
and bathtub argument of §118 gives, after `D->infinity` and then
`epsilon->0`,

$$
\boxed{
\lim_{\epsilon\downarrow0}\limsup_D
{M_d(\epsilon)\over D}
\le
Q_{tooth}(y)+y+2C_{tail}
}
\tag{2.4}
$$

and hence

$$
\boxed{
\lim_{\epsilon\downarrow0}\limsup_D
{M_d(\epsilon)\over D}
\le
Q_{tooth}(y)+y+x+{10\over3}w.
}
\tag{2.5}
$$

Here `Q_tooth(y)` is the unique nonnegative solution of

$$
\sin Q+\sqrt3(1-\cos Q)-Q={y\over2}.
\tag{2.6}
$$

This is the key separation: `z` no longer appears inside the directional
concentration term.

---

## 3. Correlated whole-area inequality after the split

Keep the sharper correlated quantities rather than immediately replacing them by
`sigma`.  Put

$$
r=x+{10\over3}w.
$$

The corrected §118 circular-segment argument gives the normalized carrier-area floor

$$
\boxed{
A_*(x,w)
={\pi\over4}
-G(\theta)-2G(\phi_8+r)-G(r),
}
\tag{3.1}
$$

where `G(t)=(t-sin t)/8`.

The exact retained train ceiling is

$$
\boxed{
C_T(x,y,z)=U-x-y+2z.
}
\tag{3.2}
$$

The three principal-route excess satisfies

$$
{E_D\over D}\le z+o(1),
\tag{3.3}
$$

and the carrier diameter is `d_D/D->lambda=sin(theta/2)`.

Combining Lemma 1.1 with (2.3)--(2.5), canonical `Delta_D=O(D)`, local rhombic
saturation, and hostile-audited signed return gives the following necessary condition
for every survivor in the common §118 stability window:

$$
\boxed{
\begin{aligned}
\lambda z
\ge(2-\sqrt3)\Big[&A_*(x,w)
-\lambda\left(10z+{x\over2}+{25\over3}w\right)\\
&-2\left(U-x-y+2z\right)
\left(Q_{tooth}(y)+y+x+{10\over3}w\right)
\Big]_+.
\end{aligned}
}
\tag{3.4}
$$

Equation (3.4) is strictly stronger than putting all bad classes into one
`2 T M_bad` term.  In particular, the route/face slack `z` now removes rhombic area at
cost `lambda*10z`, rather than at cost approximately `2C_T*10z`.

No numerical carrier coefficient is asserted here; (3.4) is the theorem-level output.

---

## 4. Hostile audit and the remaining obstruction

The strengthening does **not** produce an all-regime closure by itself.

1. A sparse bad train can genuinely traverse macroscopic distance, so the factor `d`
   in (1.2) cannot be replaced by `o(D)` without new geometry.
2. Regular boundary teeth are not sparse: there are `Theta(D)` of them even at the
   sharp endpoint.  They must remain under a directional concentration theorem.
3. Positive base-spacing slack `y` can concentrate a linear family of tooth legs in
   one train-direction window; `Q_tooth(y)` records the exact current cost of doing so.
4. Route/face slack `z` both supplies principal-route excess on the left of (3.4) and
   creates sparse exceptional endpoint capacity on the right.  Large `z` is therefore
   a genuine remaining regime, not something this split can simply discard.
5. Contact-isolated source points are untouched throughout.

The theorem changes the live structural question from

```text
control one aggregate bad-direction count containing every defect class
```

to

```text
control the directional tooth family,
while sparse interface/route defects are paid once by their own train area.
```

A closing continuation should therefore attack `Q_tooth(y)`/tooth order directly or
show that large `z` changes the global diameter-carrying structure.  Further decimal
optimization of (3.4) is secondary.

No theorem authority is changed and C-II remains open.
