> Generated reading edition · [exact source](../../../docs/reports/target_c_complete_grid_joint_switch_budget_2026-10-01_r2.md) · source SHA-256 `893bf2f4c2fb80675f47af4ba4d6fb5100c22e2f665124757b8af56f90a710cf`.
> [Current theorem state](../STATE.md) controls lifecycle and scope; historical claims retain their recorded status.

<!-- theorem-state: {"artifact_id":"ART-A127DFA538FD","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Target C-II -- complete-grid joint switch budget

Date: 2026-10-01
Base main: 91be6776e6748b0f449ccfff69bca1e352d1b75d
Status: proof-only; C-II remains open.

## Theorem

Let A={a_1,...,a_m} and B={b_1,...,b_n} be the two retained shores of the
fixed-star complete outer-to-outer rectangle on current main. Members of each shore
are pairwise disjoint proper crosscuts of the outer-face disk, and every a_i crosses
every b_j exactly once.

For an actual diameter edge h, let t_A(h) be the number of adjacent selected
A-interfaces at which its signed cut incidence changes, and define t_B(h)
analogously. Then

```math
\boxed{t_A(h)+t_B(h)\le 2.}
\tag{1}
```

Hence, if N_i^A and N_j^B are the switching-row counts at the two shores' adjacent
interfaces,

```math
\boxed{\sum_i N_i^A+\sum_j N_j^B\le 2h,}
\tag{2}
```

where h is the total number of actual diameter edges.

At the exact rooted endpoint, current main gives h=\pi D+o(D), so

```math
\boxed{\sum_i N_i^A+\sum_j N_j^B\le(2\pi+o(1))D.}
\tag{3}
```

## Proof of the joint per-edge bound

After the standard harmless endpoint resolution for proper train crosscuts, the
boundary endpoints of a complete bipartite crossing grid lie in four disjoint
boundary intervals in cyclic order

```math
\boxed{I_A^+,\ I_B^+,\ I_A^-,\ I_B^-.}
\tag{4}
```

Every A-crosscut joins I_A^+ to I_A^- and every B-crosscut joins I_B^+ to I_B^-.

For completeness, fix one A-crosscut a. Every B-crosscut crosses a, so it has one
endpoint on each of the two boundary arcs cut off by a. Pairwise disjointness of the
B-crosscuts gives opposite endpoint orders on those two arcs. Any other A-crosscut
is disjoint from a, so both of its endpoints lie in one of those two boundary arcs.
To cross every B-crosscut, its endpoints must straddle the whole block of B-endpoints
on that arc. Doing this on both sides of a produces exactly the four alternating host
intervals in (4), up to cyclic relabeling and reversal.

Actual diameter endpoints are extreme source-hull vertices and therefore lie on this
same outer boundary. The endpoint resolution can be chosen away from the finite set
of source vertices.

Order the A-crosscuts by any B-transversal and let
\ell_A(x)\in\{0,1,...,m\} be the A-layer of a boundary point x. Along the A-host
intervals I_A^+ and I_A^- this layer changes when an A endpoint is passed. On the
two B-host intervals it is constant at the two extreme values 0 and m: every
A-crosscut separates I_B^+ from I_B^-.

Exact laminar interval support says that, for h=xy, the nonzero A-incidence columns
form the interval between \ell_A(x) and \ell_A(y). Therefore an endpoint of h can
create an internal A-switch only if that endpoint lies on an A-host interval. Thus

```math
t_A(h)\le \#\{x,y\in I_A^+\cup I_A^-\}.
\tag{5}
```

Symmetrically,

```math
t_B(h)\le \#\{x,y\in I_B^+\cup I_B^-\}.
\tag{6}
```

The four host intervals partition the outer boundary and h has exactly two endpoints.
Adding (5) and (6) proves (1). Summing over h proves (2).

No metric phase estimate, KKT multiplier estimate, or computation is used.

## Shared-switch rows are corner-local

If one diameter row switches internally on both shores, one of its endpoints must lie
on an A-host interval and the other on a B-host interval. Hence every such row has
one of the four corner types

```math
I_A^+-I_B^+,\quad I_A^+-I_B^-,\quad
I_A^--I_B^+,\quad I_A^--I_B^-.
\tag{7}
```

Opposite corner types cannot coexist. For example, an I_A^+-I_B^+ diameter chord
and an I_A^--I_B^- diameter chord join adjacent blocks in the cyclic order (4), so
their four endpoints do not alternate. The chords are vertex-disjoint because the
host intervals are disjoint; therefore they do not cross, contradicting the convex
diameter-thrackle property. The same argument excludes the other opposite pair.

Thus all diameter rows reused by both switching systems occupy at most two adjacent
grid corners. After cyclic relabeling they all have an endpoint on one common host
interval.

## Quantitative consequence on current main

Current main gives

```math
|A|,|B|\ge(c_*-o(1))D,
\qquad
c_*={\kappa^4\over16\pi^3C_KM_K},
```

with C_K=\lfloor4K\rfloor+2 and M_K=2\lfloor4K\rfloor+3. Its rank-switching
theorem gives

```math
s_A,s_B\ge\left({c_*\over2}-o(1)\right)D,
```

so

```math
s_A+s_B\ge(c_*-o(1))D.
\tag{8}
```

Set

```math
H_*=\left\lceil{4\pi\over c_*}\right\rceil.
\tag{9}
```

By (3), the number of active interfaces over both shores with more than H_* switching
rows is at most

```math
{(2\pi+o(1))D\over H_*+1}
<
\left({c_*\over2}+o(1)\right)D.
```

Subtracting from (8), at least

```math
\boxed{\left({c_*\over2}-o(1)\right)D}
\tag{10}
```

interfaces across the two shores satisfy 1\le N\le H_*. Hence one shore contains at
least

```math
\boxed{\left({c_*\over4}-o(1)\right)D}
\tag{11}
```

bounded switching cusps.

Each such cusp inherits the audited adjacent-switching theorem: its switching
diameter graph is a forest, and if both switch orientations occur then all middle
endpoints lie on one common middle boundary arc in the right-prefix / optional-hub /
left-suffix order.

## Remaining target

The fixed-star branch now has a joint two-shore switch ledger rather than two separate
ones:

```math
\boxed{
\text{complete inverse-phase O-O grid}
+
\text{linear bounded ordered cusps on one shore}
+
\text{all cross-shore switch reuse confined to one boundary side}.
}
```

The next target is to couple the one-arc cusp order to the corner-localized reused
diameter rows and the opposite complete train shore. The split-star O-O branch and
the inactive-interface branch remain open.

This is theorem/proof work only. No numerical experiment, verifier, unexecuted
verifier code, or CI result is used.
