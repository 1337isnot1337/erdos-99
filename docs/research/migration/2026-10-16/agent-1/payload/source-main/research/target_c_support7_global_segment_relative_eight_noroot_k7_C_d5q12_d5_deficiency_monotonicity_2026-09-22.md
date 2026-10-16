# Target C: deficiency monotonicity for the remaining `C:(5,12,12)`, `d_6=5` lift branch

Date: 2026-09-22

Status: proved structural strengthening of the remaining finite `d_6=5` branch. It removes the `d_7=4` alternative analytically for every one-cycle lift extending the fixed six-row coefficient line. It does not by itself close the branch; the full-span lift multiplicity audit remains the active finite closure target.

## Setup

Fix one synchronized six-row state in the remaining profile

```text
C: D=-1, p=12, (d_v,q,s)=(5,12,12)
```

with virtual-canonical deficiency

```text
d_6=5.
```

Let `P_6` be its rank-one coefficient space. Restore one deleted no-root cycle and let `P_7` be a compatible rank-one seven-row coefficient space whose projection to the first six coordinates is `P_6`. This is exactly the line-extension condition imposed by the committed one-cycle verifiers.

For a touched root block `b`, let `W_t(b)` denote the row space of its empty-state quotient constraint at `t` external rows. The virtual-canonical convention is

```text
b is canonical-empty  iff W_t(b) subset P_t,
b is canonical-complete otherwise.
```

Write `C_t` for the canonical-complete block set.

## Lemma 1: canonical-complete blocks persist under a compatible lift

For every compatible six-to-seven line lift,

```text
C_6 subset C_7.
```

Proof. Let `pi: Q^7 -> Q^6` delete the restored coordinate. By construction,

```text
pi(P_7)=P_6.
```

The seven-row empty-state constraint is obtained from the six-row one by appending one coordinate to each quotient row, so

```text
pi(W_7(b))=W_6(b).
```

Suppose `b` were canonical-complete at six rows but canonical-empty at seven rows. Then

```text
W_7(b) subset P_7.
```

Applying `pi` gives

```text
W_6(b) subset P_6,
```

which says that `b` was already canonical-empty at six rows, a contradiction. Therefore every block in `C_6` remains in `C_7`. This argument also covers a six-row empty constraint of rank two: two independent projected constraint rows cannot both lie in the rank-one space `P_6`.

## Lemma 2: virtual-canonical deficiency is monotone

Let `H_b` be the fixed complete-block relation row for block `b`, and define

```text
d(C)=|C|-rank{H_b : b in C}.
```

If `A subset B`, then

```text
d(A) <= d(B).
```

Indeed, adjoining one new block increases `|C|` by one and increases the relation-row rank by at most one. Iterating proves the claim.

Combining Lemmas 1 and 2 gives

```text
d_7 >= d_6 = 5.
```

## Consequence for the remaining profile

The established seven-row containment reduction for `C:(5,12,12)` leaves only

```text
d_7=4 with singleton capacity >=10,
```

or

```text
d_7=5 with singleton capacity >=11.
```

The monotonicity result rules out the first alternative before any enumeration. Hence every one-cycle intermediate state that can come from an actual target must satisfy

```text
d_7=5,
singleton capacity >=11.
```

Thus the `seven_d4_lifts` branch in the current full-span verifier is mathematically redundant for this `d_6=5` closure problem. Its presence is harmless as an independent check; an exhaustive run should necessarily report

```text
seven_d4_lifts 0.
```

The small-range validation already recorded for the full-span verifier has exactly this behavior, but the statement above is a proof and does not depend on those samples.

## Remaining obligation

This strengthening does not establish the required two-cycle obstruction. A hypothetical target would still need two distinct deleted cycles whose one-cycle restorations are `d_7=5`, capacity-at-least-11 lifts and retain the full ten-dimensional six-row singleton-functional quotient span.

The active exact target therefore remains the committed full-span multiplicity audit over all 325,955 six-row cover representatives. A complete run proving that every six-row functional witness has at most one distinct full-span lift cycle closes the `d_6=5` side. Together with the already recorded `d_6=3` and `d_6=4` exclusions, that would close `C:(5,12,12)` in the current finite split.

This note is a research artifact only. It does not change the canonical theorem-state declaration that Target C-II and Erdős Problem #99 remain open.