> Generated reading edition · [exact source](../../research/target_c_adjacent_cut_backbone_542_2026-09-15.md) · source SHA-256 `d670490d22dad869d2cbba40620d0247eb0a396f3adc114fda9f2cef52a61ef3`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "3fac146511d6d53d957a692f4d6ad8544b56557e", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_adjacent_cut_backbone_542_2026-09-15.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "4eda2418ffe1b9890d7aea4f4138f7353085f34e4f7cb24a8a688581839a65b7"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the optimized common-center backbone reduces the adjacent switching set to at most `542` edges

**Date:** 2026-09-15  
**Status:** proof-only source-level quantitative strengthening  
**Scope:** full-core Type-II branch with `t=(q-k)/D<=1.844`  
**Dependencies:** audited smallest-leaf weighted center fan; common-center path construction; global strict-rhombus angular-defect budget; exact laminar interval support; Section-171 / SW1039 live diameter-edge budget; adjacent switching order theorem  
**Certificate:** `research/verify_target_c_adjacent_cut_backbone_542.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

The current `SW1039` theorem reduces the live adjacent switching forest to at most
`1038` edges.  Its switch-count estimate uses the improved full-diameter-edge budget,
but it retains the original common-center path density

```math
p_{old}=0.0035641799\ldots .
```

The common-center path extraction has two free parameters.  Retuning them nearly
doubles the certified path density.  Combining that longer path with the same improved
switch-count budget cuts the finite active interface almost in half again.

## Theorem SW542

Every sufficiently large survivor in the stated proof-only branch contains consecutive
smallest-leaf outer-to-outer cuts

```math
\tau_i,\tau_{i+1}
```

on one common-center complement-dual path such that the number of actual diameter
interval rows switching at their common layer boundary satisfies

```math
\boxed{N_i\le542.}
\tag{SW542.1}
```

The **same** adjacent pair satisfies

```math
\boxed{
B_i=O(D^{-1}),
\qquad
Q_i=q_i+q_{i+1}=O(D^{-1}),
}
\tag{SW542.2}
```

where `B_i` is the switching KKT multiplier mass and `q_j` is the common-center
phase-offset variable.  Consequently

```math
\boxed{
d_{\mathbb{RP}^1}(u_i,u_{i+1})=O(D^{-1}).
}
\tag{SW542.3}
```

More explicitly, one can take

```math
D(B_i+Q_i)<1.8\times10^{11}+o(1).
\tag{SW542.4}
```

By the audited adjacent switching topology, those at most `542` rows are exactly the
diameter edge boundary of the middle source layer.  The switching graph is a forest;
when both switch orientations occur its middle endpoints lie on one outer-boundary arc
in the audited right-prefix / optional-hub / left-suffix order, and its components are
ordered caterpillars.

For the contact-opening strip move, every source-pair distance outside this at-most-542
edge layer cut is invariant **exactly**.  Thus the complete moving diameter obstruction
for that move contains at most `542` edges.

---

## 1. Retune the common-center path before spending the switch budget

Use the audited smallest-leaf inputs

```math
{\sum_\tau w_\tau d_\tau\over\sum_\tau w_\tau}
>0.7404-o(1),
\tag{SW542.5}
```

```math
{1\over D}\sum_\tau w_\tau>0.0848-o(1),
\tag{SW542.6}
```

and

```math
N_C<1.063D+o(D)
\tag{SW542.7}
```

for the total number of center-phase trains.

Choose

```math
\boxed{
\lambda={64033\over100000}=0.64033,
\qquad
r={60237\over100000}=0.60237.
}
\tag{SW542.8}
```

Call a smallest-leaf O--O train **good** when its center degree exceeds
`lambda D`.  Weighted thresholding gives retained good weight, and hence also a lower
bound on the number of distinct good trains,

```math
\begin{aligned}
gD-o(D),
\qquad
g
&={ (0.7404-\lambda)(0.0848)\over1.063-\lambda}\\
&={530371\over26416875}\\
&=0.0200769773109\ldots .
\end{aligned}
\tag{SW542.9}
```

Order the center trains by their real phase representative and let `H` be the top `r`
fraction.  Every good leaf has at least

```math
\begin{aligned}
d_{top}D-o(D),
\qquad
d_{top}
&=\lambda-(1-r)(1.063)\\
&={21764931\over100000000}\\
&=0.21764931
\end{aligned}
\tag{SW542.10}
```

neighbors in `H`.

Averaging good-leaf / `H` incidence gives one center train `gamma in H` crossing more
than

```math
\begin{aligned}
pD-o(D),
\qquad
p
&={d_{top}g\over r(1.063)}\\
&={3847829406467\over563841172411875}\\
&=0.00682431435435\ldots
\end{aligned}
\tag{SW542.11}
```

distinct good leaves.

The good leaves are pairwise noncrossing.  Those crossed by one train form one simple
path in their complement dual.  Hence we obtain

```math
P=(\tau_1,\ldots,\tau_m),
\qquad
m>pD-o(D).
\tag{SW542.12}
```

This is about `1.915` times the path density used in the original triple-small and
`SW1039` certificates.

---

## 2. The aggressive phase split still leaves a positive lower block

The chosen top fraction is close to the largest value compatible with the parent phase
argument.  The remaining lower-phase center-neighbor density is nevertheless a fixed
positive rational:

```math
\begin{aligned}
d_{low}
&=\lambda-r(1.063)\\
&={1069\over100000000}\\
&=1.069\times10^{-5}>0.
\end{aligned}
\tag{SW542.13}
```

Let `alpha_gamma` be the real phase of the selected center train and, for path leaf
`tau_j`, put

```math
q_j=\beta_j-\alpha_\gamma-\pi/3>0.
```

Every good path leaf has at least `d_low D-o(D)` center neighbors whose phase is at
most `alpha_gamma`.  Each such crossing rhombus has angular defect at least `q_j`.
The global strict-rhombus defect budget therefore gives exactly the parent estimate

```math
\boxed{
\sum_{j=1}^m q_j
\le {C_{phase}\over d_{low}}+o(1),
}
\tag{SW542.14}
```

and hence, with

```math
Q_i=q_i+q_{i+1},
```

```math
\boxed{
\sum_{i=1}^{m-1}DQ_i
\le {2C_{phase}\over d_{low}}D+o(D).
}
\tag{SW542.15}
```

The coefficient is large because `d_low` is tiny, but it is a fixed constant.  Thus
the average adjacent projective phase gap remains `O(D^-1)`.

---

## 3. Insert the stronger live switch-count budget

`SW1039` proves on the whole live `t<=1.844` branch that the number `h_H` of actual
diameter edges satisfies

```math
{h_H\over D}<1.851259926+o(1).
\tag{SW542.16}
```

Each actual diameter interval on the selected path starts and stops at most once, so

```math
\boxed{
\sum_{i=1}^{m-1}N_i
<3.702519852D+o(D).
}
\tag{SW542.17}
```

This is the key second gain.  The old universal count budget was `2 pi D`; the new
one is smaller by a factor about `1.697`.

The raw switch-count average on the retuned path is

```math
{3.702519852\over p}
=542.5482560\ldots .
\tag{SW542.18}
```

A count-only averaging argument already yields some boundary with `N_i<=542` for all
sufficiently large members.  To keep the phase and KKT properties on the same boundary,
we need a positive-density version.

---

## 4. A positive-density set of boundaries has `N_i<=542`

Call an internal boundary count-bad when

```math
N_i\ge543.
```

From (SW542.17), count-bad boundaries have asymptotic density at most

```math
{3.702519852\over543}
={308543321\over45250000000}
=0.00681863692817\ldots .
\tag{SW542.19}
```

The path density is `p=0.00682431435435...`, so the count-good boundary density is at
least

```math
\begin{aligned}
rho
&:=p-{3.702519852\over543}\\
&={231764464221212261\over40822100882619750000000}\\
&=5.6774261787\times10^{-6}\\
&>5\times10^{-6}.
\end{aligned}
\tag{SW542.20}
```

Thus for all sufficiently large members there are

```math
rho D-o(D)
```

internal boundaries with

```math
\boxed{N_i\le542.}
```

The integer cutoff is important: `543` is the bad threshold, so every surviving
boundary has at most `542` switching rows.

---

## 5. Retain small switching multiplier and phase gap on the same boundary

The exact KKT interval budget gives

```math
\sum_iB_i\le2,
\tag{SW542.21}
```

where

```math
B_i=\sum_h\beta_h
|\varepsilon_{h,i+1}-\varepsilon_{hi}|.
```

Combine this with (SW542.15):

```math
\sum_iD(B_i+Q_i)
\le
\left(2+{2C_{phase}\over d_{low}}\right)D+o(D).
\tag{SW542.22}
```

Restrict the nonnegative sum to the positive-density count-good set.  Some count-good
boundary obeys

```math
D(B_i+Q_i)
\le
{2+2C_{phase}/d_{low}\over\rho}+o(1).
\tag{SW542.23}
```

Using the same outward rational enclosure already audited in the parent certificates,

```math
C_{phase}
<{3258689123681\over612912000000},
```

the exact companion verifier proves

```math
\boxed{
{2+2C_{phase}^{up}/d_{low}\over\rho}
<1.8\times10^{11}.
}
\tag{SW542.24}
```

This proves (SW542.2) and (SW542.4).  The parent phase identity

```math
d_{\mathbb{RP}^1}(u_i,u_{i+1})\le Q_i
```

gives (SW542.3).

---

## 6. Exact moving-strip consequence

For the selected adjacent pair, let `M` be the unique source layer between their
nested shores.  The audited adjacent strip-opening theorem translates the whole layer
by a vector `v`.  Every source pair with both endpoints in `M` or both endpoints
outside `M` is unchanged exactly.  A source pair moves exactly when one endpoint is in
`M` and the other is outside.

For actual diameter pairs this moving set is exactly the switching graph

```math
H_{sw}=\delta_H(M).
```

Therefore (SW542.1) upgrades the strip theorem to

```math
\boxed{
|E(H_{sw})|\le542.
}
\tag{SW542.25}
```

For an oriented moving diameter vector `r_h` and sign `delta_h in{+-1}`, the exact
upper-distance inequality remains

```math
2\delta_h r_h\cdot v+|v|^2\le0.
\tag{SW542.26}
```

Every old unit contact away from the two boundary train families is invariant under the
strip translation.  The two boundary contact families can be opened by arbitrarily
small nonzero `v`, exactly as in the audited strip-opening theorem.  Old strict
noncontact and nondiameter slacks persist for sufficiently small `v` by finiteness.

Hence the complete local replacement obstruction is now a system of at most `542`
explicit diameter inequalities (SW542.26), together with the two contact-opening
half-plane conditions.

---

## 7. Ordered switching interface inherited from the audited topology

The exact adjacent switching-order theorem applies to this pair without any additional
hypothesis.

- Every switching edge has exactly one endpoint in the middle layer.
- Left-switch edges join the left exterior region to the middle layer; right-switch
  edges join the middle layer to the right exterior region.
- The switching graph is a forest.
- If both switch orientations occur, every participating middle endpoint lies on one
  common outer-boundary arc.
- Along that arc, right-switch middle endpoints form a prefix, left-switch middle
  endpoints form a suffix, and the two sets share at most one transition hub.
- In the mixed-orientation case the components are ordered caterpillars.

Thus the present theorem does not merely shrink an arbitrary finite list to `542`.
It shrinks the audited one-arc interface forest to that size.

---

## 8. Scope and next gate

The improvement uses two facts that were not combined in the previous `1038` theorem:

1. the common-center path can be made substantially longer by retuning `lambda,r`;
2. the live defect ledger bounds the full diameter-edge density far below `pi`.

The very small value of `d_low` is legitimate asymptotically: it is a fixed positive
rational, and every `o(D)` loss is eventually smaller than `d_low D`.  Its only cost is
the large harmless constant in (SW542.4).

No local descent is claimed.  Even two diameter edges can block a two-dimensional
contact-opening cone, so a smaller finite cardinality alone cannot close C-II.  The
remaining source-level problem is geometric:

> classify the oriented diameter normals in the at-most-542 right-prefix / hub /
> left-suffix interface and compare their cone with the two boundary contact-opening
> directions.

A successful sign/cone theorem would immediately feed the audited strip translation,
because every nonswitching source-pair constraint has already been eliminated exactly.

**Disposition:** proved proof-only quantitative strengthening. C-II and Level I remain
open.
