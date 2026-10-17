> Generated reading edition · [exact source](../../research/target_c_pentagon_rank_threshold_2026-09-19.md) · source SHA-256 `d65a15f22f2a8f2074818a28bbf685e1c810b5656f2377b2063a9c500c97cbcc`.
> [Current theorem state](../docs/STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

> Presentation repairs: 2 exact-source-bound TeX/escape correction(s); [reviewed repair ledger](../../docs/publication/reading-tex-repairs.json). Frozen source bytes are unchanged.

<!-- migration-provenance: {"destination_status": "historical_unreviewed_noncanonical", "source_blob": "77b7f647af26c040149028429a145d2cfc786d9f", "source_canonical": null, "source_commit": "42f0296d1aca068c809f74cee5dcdb4ebdb27c73", "source_lifecycle": "not_indexed_first_party_source_material", "source_path": "research/target_c_pentagon_rank_threshold_2026-09-19.md", "source_repository": "https://github.com/1337isnot1337/e-99", "source_sha256": "d8a0e1a5f7eda7c1d9161462e9f9e68ead288e9d8f745c2d73e4ef17fdc73e88"} -->

> **Imported source research; no destination claim is promoted.** Source lifecycle is recorded in this ledger; destination status remains unreviewed/noncanonical.

# Target C-II — the second-smallest and second-largest physical turns straddle the average

**Date:** 2026-09-19  
**Status:** exact local nonlinear-to-polyhedral consequence; theorem-state authority unchanged  
**Scope:** every strict closed equilateral force pentagon  
**Depends on:** the physical gap-order theorem, the turn-simplex theorem, and the sharp two-gap closure bound with its exact `2/5` secants  
**Certificate:** `research/verify_target_c_pentagon_rank_threshold_2026_09_19.py`  
**LEVEL I STATUS:** `STILL OPEN. C-II REMAINS OPEN.`

Use the representative physical order cone

```math
x_0\le x_2\le x_3\le x_4\le x_1,
\qquad
\sum_{i=0}^4x_i=2.
\tag{1}
```

The average turn is `2/5`. The exact rank-conditioned secant theorem gives

```math
x_{k+2}+x_{k+3}\le \frac23+\frac{x_k}{3}
\qquad(0\le x_k\le 2/5),
\tag{2}
```

and

```math
x_{k+2}+x_{k+3}\le \frac12+\frac{3x_k}{4}
\qquad(2/5\le x_k\le 2/3).
\tag{3}
```

The new point is that the order structure forces the second-smallest gap into the low regime and the second-largest gap into the high regime.

## 1. Second-smallest gap

Because `x_0` is the minimum of five numbers averaging `2/5`,

```math
x_0\le\frac25,
```

so (2) is valid at `k=0`:

```math
C_0:=\frac23+\frac{x_0}{3}-x_2-x_3\ge0.
```

Let

```math
O_{02}:=x_2-x_0\ge0,
\qquad
O_{23}:=x_3-x_2\ge0.
```

Then the exact identity

```math
\boxed{
\frac25-x_2
=
\frac35C_0+\frac15O_{02}+\frac35O_{23}
}
\tag{4}
```

proves

```math
\boxed{x_2\le\frac25.}
\tag{5}
```

Thus the minimum and second-smallest physical turns are always on the low side of the average.

## 2. Second-largest gap

If `x_3\ge2/5`, then (1) already gives `x_4\ge2/5`.

Otherwise `x_3\le2/5`, so (2) is valid at `k=3`:

```math
C_3:=\frac23+\frac{x_3}{3}-x_0-x_1\ge0.
```

Using

```math
O_{23}=x_3-x_2\ge0,
\qquad
O_{34}=x_4-x_3\ge0,
```

and the turn-sum equality

```math
E:=x_0+x_1+x_2+x_3+x_4-2=0,
```

we have the exact identity

```math
\boxed{
 x_4-\frac25
 =
 \frac3{10}C_3
 +\frac3{10}O_{23}
 +\frac7{10}O_{34}
 +\frac3{10}E.
}
\tag{6}
```

Hence in the `x_3\le2/5` branch,

```math
x_4\ge\frac25.
```

Together with the trivial `x_3\ge2/5` branch,

```math
\boxed{x_4\ge\frac25.}
\tag{7}
```

Therefore every physical pentagon in the representative order cone satisfies

```math
\boxed{x_2\le\frac25\le x_4.}
\tag{8}
```

By cyclic relabeling and reflection, this means:

```math
\boxed{
\text{second-smallest turn}\le\frac{2\pi}{5}
\le\text{second-largest turn}.
}
\tag{9}
```

## 3. Equality is rigid

If `x_2=2/5`, every term on the right side of (4) must vanish. Hence

```math
x_0=x_2=x_3=\frac25.
```

The turn sum and order then force

```math
x_4=x_1=\frac25.
```

If `x_4=2/5`, equation (6) forces `x_2=x_3=x_4=2/5`, after which the previous argument again gives all five gaps equal.

Thus

```math
\boxed{
 x_2=\frac25\ \text{or}\ x_4=\frac25
 \Longrightarrow
 x_0=x_1=x_2=x_3=x_4=\frac25.
}
\tag{10}
```

For every non-regular strict physical pentagon,

```math
\boxed{x_2<\frac25<x_4.}
\tag{11}
```

## 4. Only the median turn still needs a `2/5` branch

After the exact physical order is fixed, four of the five secant regimes are now determined:

- rank 1 (minimum): low secant (2);
- rank 2 (second-smallest): low secant (2);
- rank 4 (second-largest): high secant (3);
- rank 5 (maximum): high secant (3).

Only the median `x_3` can lie on either side of `2/5`. Therefore each physical order cone needs only two strong rational closure branches:

```math
x_3\le\frac25
\qquad\text{or}\qquad
x_3\ge\frac25.
\tag{12}
```

This replaces the naive independent low/high splitting of the three middle ranks by one binary branch. Since there are ten physical order cones, the strongest exact `2/5`-secant layer has at most twenty local branches per pentagon rather than eighty.

The regular equality case lies on both closed branches and is not lost.

## 5. Certified branchwise outer intervals

The companion certificate also combines the turn-simplex facets, order facets, thresholds (8), and the appropriate exact low/high secants for all five ranks. It gives the following rational enclosing intervals.

If the median is low, `x_3\le2/5`, then

```math
\boxed{
0\le x_0\le\frac25,
\quad
\frac25\le x_1\le\frac23,
\quad
\frac4{15}\le x_2\le\frac25,
\quad
\frac13\le x_3\le\frac25,
\quad
\frac25\le x_4\le\frac23.
}
\tag{13}
```

If the median is high, `x_3\ge2/5`, then

```math
\boxed{
\frac1{15}\le x_0\le\frac25,
\quad
\frac25\le x_1\le\frac23,
\quad
\frac16\le x_2\le\frac25,
\quad
\frac25\le x_3\le\frac12,
\quad
\frac25\le x_4\le\frac35.
}
\tag{14}
```

Every endpoint in (13)-(14) is checked by an explicit nonnegative rational Farkas identity in the verifier. These are valid outer bounds; no claim of physical attainability of every endpoint is made.

## 6. Consequence for the remaining support-seven systems

This is a stronger and cheaper local polyhedral layer than the previously recorded broad rank intervals. In generic `H6`, generic `H7b`, and convex `H8`, once a face's exact force-gap order is selected, four closure cuts can be inserted without any further branching, and the fifth requires only the median bit (12).

The next exact global step is therefore to rerun the surviving affine cells with the twenty-branch per-face rank-threshold closure layer and extract rational Farkas exclusions. The theorem does not itself exclude a reciprocal cell and does not change theorem-state authority. C-II remains open.
