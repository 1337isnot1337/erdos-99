> Generated reading edition · [exact source](../../../docs/reports/target_c_cyclic_surplus_cap_and_capacity_gap_2026-09-11.md) · source SHA-256 `fa6249519f2a3e4404681ba75c194b2cce00d623bcbdc07f1d0dffc2a590f766`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-1FC020EEE920","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — cyclic surplus cap and the remaining capacity gap

**Date:** 2026-09-11  
**Repository state:** `643a06bc28354ec06167a7b8529129640bb689ad`  
**Run type:** exact ledger consequence and obstruction audit  
**Target:** Target C, C-II, cyclic post-ZF branch  
**Status:** STILL OPEN; hold as an unpromoted report

## 1. Endpoint tested

The new cyclic report gives, in the post-ZF circuit case

```math
s_Z=d_H=0,
\qquad P_F/D\to\pi,
\qquad b-P_F=o(D),
```

and the exceptional-face floor

```math
Q/D\ge {4\over5}\sqrt{\pi\over2\sqrt3}-o(1).
```

The attempted closing implication was

```text
linear exceptional-face defect + attachment sparsity
    -> an upper bound below the cyclic surplus floor.
```

The exact identities give an upper bound, but not one below the existing lower
bound.  This report records the calculation so that the missing step is explicit.

## 2. A cyclic surplus upper bound

Let

```math
S_D=e_{BB}+2s_C,
\qquad
\xi_D=Q/D,
\qquad
q=|B_+|.
```

In the cyclic branch, `h=q`.  The exact outer-face identity is

```math
b+Q=2q.
\tag{2.1}
```

Since `b-P_F=o(D)` and `P_F/D\to\pi`, (2.1) gives

```math
{2q\over D}=\pi+\lim {Q\over D}+o(1).
\tag{2.2}
```

The post-ZF incidence identity is

```math
c_I+e_{BB}+s_C=q-2.
\tag{2.3}
```

The outer-walk contact estimate gives `Q\le e_{BB}`.  Therefore

```math
\begin{aligned}
S_D
 &=2q-4-2c_I-e_{BB}\\
 &\le 2q-4-2c_I-Q.
\end{aligned}
\tag{2.4}
```

After division by `D` and use of (2.2), every cyclic post-ZF survivor satisfies

```math
\boxed{\limsup {e_{BB}+2s_C\over D}\le\pi.}
\tag{2.5}
```

This is sharp at the scalar-identity level: the `Q` term cancels.  Thus the
exceptional-face floor cannot by itself provide an upper/lower contradiction.

## 3. Attachment sparsity gives a second, still insufficient cap

Let `\sigma` be the number of connected components of the attachment-incidence
graph, and let

```math
u_A=\sum_r(|A_r|-3).
```

The local attachment inequality in the current report stack gives

```math
s_C\le u_A.
\tag{3.1}
```

Planar incidence gives

```math
u_A\le q-c_I-2\sigma.
\tag{3.2}
```

Using (2.3), (3.1), and (3.2), one obtains

```math
3s_C\le q-c_I,
\tag{3.3}
```

and hence

```math
{S_D\over D}
={q-2-c_I+s_C\over D}
\le {4q\over3D}+o(1).
\tag{3.4}
```

Together with `e_{BB}\ge Q`, this can be written as the piecewise normalized cap

```math
\limsup {S_D\over D}
\le
\begin{cases}
\frac23(\pi+\xi),&0\le\xi\le\pi/2,\\[2mm]
\pi,&\pi/2\le\xi\le\pi,
\end{cases}
\tag{3.5}
```

where `\xi` is any subsequential limit of `Q/D`.  The current universal floor
`\xi\ge0.761850\ldots` lies below `\pi/2`, but (3.5) is still larger than the
cyclic surplus lower floor `0.995540\ldots`.  The scalar ledgers therefore leave a
nonempty high-surplus interval.

## 4. Why this does not close the branch

The cancellation in (2.4) is the exact obstruction.  Increasing `Q` forces more
loaded endpoints through (2.2), while the same `Q` is subtracted through
`e_{BB}\ge Q`.  The identities do not measure the geometric cost of the resulting
loaded-loaded contacts beyond `O(D)` boundary order.

The surviving cyclic model is therefore:

```math
Q=\Theta(D),\quad e_{BB}=\Theta(D),\quad
P_F=\pi D-o(D),\quad A_F={\pi\over4}D^2-o(D^2),
```

with a linear family of exceptional stopped-train faces and a possible quadratic
population of contact-isolated points in the corresponding source regions.  The
full-source Oler/annulus estimate still leaves the fixed margin
`0.0197873937D^2` above the triangular density.  The attachment-perimeter theorem
removes the old `D c_I` error but does not remove this full-source margin.

## 5. Regression audit

- The regular odd shell is not a post-ZF circuit example: it has `s_Z=2`.  It
  remains a valid high-surplus regression for any argument that uses only cyclic
  diameter topology and local KKT response.
- A giant exceptional face is not excluded by (2.5); its perimeter is only linear
  and its area can be quadratic.
- Contact-isolated source points are not counted by the attachment-cell population
  estimate.  Moving them into the nonisolated core would be an additional, unproved
  global operation.
- No upper bound on `s_Z` is inferred.  The calculation applies only after the
  post-ZF reduction.

## 6. Classification

| Statement | Classification |
|---|---|
| cyclic surplus cap (2.5) | proved conditional on the promoted/current post-ZF cyclic identities |
| piecewise cap (3.5) | proved conditional on local attachment sparsity and planar incidence |
| cyclic C-II closure | not proved |
| full Erdős Problem #99 settlement | not proved |

The next decisive result must charge the exceptional-face boundary or the
contact-isolated population by a **quadratic** amount, or produce a source-preserving
finite competitor.  Boundary-order contact bookkeeping cannot close the remaining
interval.
