# Target C-II — twelve additional collapsed support-six chambers are nonplanar

**Status:** proved candidate awaiting independent promotion audit; not canonical.

This note removes twelve more explicit local order chambers from the collapsed
support-six branch.  Together with
`target_c_support6_collapsed_order_chamber_planar_obstruction_2026-09-18.md`,
the exact certificates now exclude thirteen numerically found strict local chambers.
The result is still chamber-local and does not exclude the collapsed branch in
general.

## Certified statement

Let the six collapsed faces be indexed by `0,...,5`, with internal train graph
`K_6` minus the matching `{03,14,25}` and anchor signs
`(+,+,+,-,-,-)`.  Fix the two train angles on edges `(0,1)` and `(0,2)`.
For each of the twelve rational boxes named `ch2`, `ch3`, `ch4`, `ch5`, `ch6`,
`ch7`, `ch8`, `ch9`, `ch10`, `ch11`, `ch12`, and `ch13` in
`verify_target_c_support6_collapsed_additional_chambers_2026_09_18.py`:

1. the ten remaining closure equations have a unique zero in the displayed
   radius-`10^-10` box;
2. all six local pentagons have strict cyclic order, positive gaps, every gap
   less than `2*pi/3`, and every two consecutive gaps summing to less than
   `pi` throughout that box;
3. after removing endpoint-sharing pairs, the interval-certified projective
   gap test leaves respectively 5, 4, 10, 9, 4, 4, 4, 5, 5, 5, 5, and 5 angle-eligible train pairs;
4. no planarization satisfying the endpoint-fan restriction, the triangle-free
   train-crossing restriction, and the certified local rotations exists.

Consequently, no globally embedded collapsed stopped-train complex can have any
of these twelve local cyclic-order chambers, under exactly those local train
hypotheses.

The finite enumeration checks every allowed crossing subset, every order of
multiple crossings along each train, and both alternating rotations at every
proper crossing.  The Python verifier exhausts `ch2/ch3/ch6/ch7/ch8`; the compiled exact
combinatorial verifier
`verify_target_c_support6_collapsed_additional_chambers_planar_obstruction_fast.cpp`
exhausts the larger `ch4/ch5` cases.  It rejects the planar Euler face count
`E-V+2` in every case.  The exact counts are:

| chamber | eligible pairs | triangle-free subsets | rotation systems |
|---|---:|---:|---:|
| `ch2` | 5 | 32 | 507 |
| `ch3` | 4 | 16 | 117 |
| `ch4` | 10 | 1024 | 3,545,841 |
| `ch5` | 9 | 512 | 660,783 |
| `ch6` | 4 | 16 | 117 |
| `ch7` | 4 | 16 | 117 |
| `ch8` | 4 | 16 | 117 |
| `ch9` | 5 | 32 | 1,027 |
| `ch10` | 5 | 32 | 507 |
| `ch11` | 5 | 32 | 1,027 |
| `ch12` | 5 | 32 | 711 |
| `ch13` | 5 | 32 | 507 |

## Proof dependencies and scope

The contraction part uses only rational arithmetic.  Sine and cosine are bounded
by alternating Taylor sums with rational remainder bounds; a rational approximate
inverse Jacobian verifies the interval Newton/Banach inequalities.  The cyclic
orders and turn inequalities are then checked interval-wise, so no floating-point
classification enters the finite obstruction.

The planarization step uses the same local facts audited for the first chamber:
trains with a common bounded endpoint cannot cross, and the positive-contact train
crossing graph is triangle-free.  It does not assume that every eligible pair must
cross.  It also does not assume a global source embedding from the local closure.

The dependency chain is therefore

```text
collapsed support-six local closure equations
  -> certified ch2/ch3/ch4/ch5/ch6/ch7/ch8/ch9/ch10/ch11/ch12/ch13 interval roots and rotations
  -> interval projective-gap and endpoint-fan filtering
  -> exhaustive finite train planarization enumeration
  -> exclusion of these twelve local chambers only.
```

It does not classify all solutions of the two-dimensional collapsed closure family,
and it does not remove the positive-slack global branch.  In particular, the
local realization certificate remains a binding regression against any attempted
exclusion using only six pentagon closures, anchor parallelism, and local
no-extra-contact inequalities.

## Reproducibility

Run:

```text
python3 research/verify_target_c_support6_collapsed_additional_chambers_2026_09_18.py
python3 research/verify_target_c_support6_collapsed_additional_chambers_planar_obstruction_2026_09_18.py
```

The Python scripts pass for the interval roots and `ch2/ch3/ch6/ch7/ch8/ch9/ch10/ch11/ch12/ch13`; compile and run the
fast verifier for the `ch4/ch5` counts:

```text
g++ -O3 -std=c++17 research/verify_target_c_support6_collapsed_additional_chambers_planar_obstruction_fast.cpp -o /tmp/collapsed_planar_fast
/tmp/collapsed_planar_fast
```
