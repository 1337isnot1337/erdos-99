> Generated reading edition · [exact source](../../../docs/reports/target_c_common_hub_transfer_regression_2026-09-11.md) · source SHA-256 `a220ff5c3d21258a3bb2f6ee756c23ff1c078312f7b2fc8d83e6a0cd86902e3a`.
> Formatting and navigation only; the source and theorem ledger control mathematical status.

<!-- theorem-state: {"artifact_id":"ART-A4DE3D500DEE","canonical":false,"claim_ids":[],"claim_statuses":{},"index":"docs/state/artifact-index.jsonl","status":"unreviewed","target":"target-c"} -->
# Erdős Problem #99 — common hub does not inherit bridge-transfer positivity

**Date:** 2026-09-11  
**Repository state:** `053e1e1b85643b738b4cde306838d150ea325783`  
**Run type:** C-II closing attempt / exact response regression  
**Target:** Target C, post-C-I common-block phase  
**Active prompt:** `docs/prompts/erdos_problem_99_TARGET_C_1.0_FINAL_CONTINUATION_PROMPT.md`  
**External web search:** not used  
**Computation:** not used

## LEVEL I STATUS

`STILL OPEN`

## 1. Starting endpoint

The September 10 common-bridge theorem proves that the C24 intersection of all
positive-diameter routes contains no contact bridge. Therefore the route intersection
is one positive contact bridge block. The tempting next implication was:

```text
all diameter routes meet one contact block
    -> every cross-block transfer K_ef is positive
    -> contradiction with C53's min-off-diagonal sign theorem.
```

The first arrow is false for a general multi-edge block. The bridge proof uses the
unique current drop across one edge. A 2-edge-connected block has several current
ports, and the side voltage contributions can cancel.

## 2. Strongest genuinely new audited theorem

### Theorem — a common 2-edge-connected block has no separator-only transfer sign

Let a positive weighted four-cycle have vertices in cyclic order
`0,1,2,3` and edge resistances

```text
r_01=a,  r_12=b,  r_23=c,  r_30=d,
```

where `a,b,c,d>0`. Treat all four vertices as boundary terminals. Let

```text
e=(2,0),  f=(3,1)
```

be oriented from the complementary interval `{0,1}` to `{2,3}`. If `Lambda` is the
Dirichlet response and `K_ef=q_e^T Lambda^+ q_f`, then

```math
\boxed{K_{ef}=\frac{bd-ac}{a+b+c+d}.}
```

Consequently the same common-block topology permits `K_ef<0`, `K_ef=0`, or
`K_ef>0`, by changing only the positive edge weights. For example,
`(a,b,c,d)=(2,1,2,1)` gives `K_ef=-1/2`.

The result remains a common-block regression if arbitrary positive-resistance trees are
attached to the four cycle vertices and the terminals are placed at the tree leaves:
for the disjoint pair `e,f`, the pendant tree edges carry zero current in the unit
transfer problem and the displayed cross-transfer is unchanged.

### Scope

This is an exact response-network statement. The cycle is planar, circular-planar,
strictly positive, and 2-edge-connected. The four terminals can be placed in strict
convex cyclic order, with `{0,1}` and `{2,3}` as complementary boundary intervals.
It does not assert that the weighted cycle is itself a unit-contact KKT realization.
It therefore kills only a separator-only replacement for the bridge theorem.

### Proof

For unit current with source `+1` at vertex `3` and sink `-1` at vertex `1`, current
splits between the two paths from `3` to `1`. The path through `0` has resistance
`a+d`; the path through `2` has resistance `b+c`. Thus the currents on those paths
are

```math
I_0=\frac{b+c}{a+b+c+d},
\qquad
I_2=\frac{a+d}{a+b+c+d}.
```

Set the potential at vertex `1` to zero. Ohm's law gives

```math
V_0=aI_0,
\qquad
V_2=bI_2.
```

The transfer entry for `e=(2,0)` is the voltage difference seen by that incidence
vector:

```math
\begin{aligned}
K_{ef}=V_2-V_0
&=\frac{b(a+d)-a(b+c)}{a+b+c+d}\\
&=\frac{bd-ac}{a+b+c+d}.
\end{aligned}
```

The denominator is positive. The three sign cases follow immediately.

## 3. Exact effect on C-II

The common-bridge exclusion remains valid and stronger than before:

```text
I_* contains no positive contact bridge;
I_* is one bridge block.
```

The new regression shows that this conclusion alone cannot be fed back into CB.1.
In particular, the C53 conclusion

```math
\min_{e\ne f}K_{ef}\le0
```

is compatible with a common 2-edge-connected hub. There is no contradiction until a
new theorem uses unit-contact geometry, KKT affine equilibrium, circuit sparsity, or the
Woodall forest/cycle structure to control the multiport response.

In the `s_Z=0` branch, the exact circuit bridge ledger still says that a contact bridge
with two nonsingleton sides is crossed by at least three diameter edges. That statement
does not remove the multiport cancellation inside the common block.

## 4. Exact remaining lemma

The shortest honest replacement target is:

> **Unit-contact common-block response lemma.** In the C-II relative-interior KKT
> realization, if every selected positive-diameter route meets one positive contact
> block and no common contact bridge exists, prove either a quantitative signed-transfer
> inequality for `K=Q^T Lambda^+Q` that contradicts C53, or a contact/circuit/diameter
> surplus inequality strong enough to contradict the `s_Z=0` and `s_Z>0` ledgers.

The four-cycle calculation proves that the lemma cannot be replaced by the purely
topological assertion that all routes pass through one block.

## 5. Audit classification of other claims

| Claim | Classification | Reason |
| --- | --- | --- |
| Universal positive transfer across a common contact bridge | proved in the named common-bridge report | A unique bridge forces one voltage drop, and the maximum principle controls both side drops. |
| No common contact bridge in C-II | already canonical through the September 10 report | It combines CB.1 with the promoted C53 sign audit. |
| Positive transfer across an arbitrary common block | rejected | The weighted four-cycle gives either sign. |
| The weighted four-cycle is an actual global minimizer regression | not claimed | Its response calculation omits unit-contact geometry, KKT affine equilibrium, and global diameter optimality. |
| C-II is closed after common-bridge exclusion | rejected | The common block remains, and all contact-isolated source points remain outside the positive support. |

## 6. Regression tests

| Regression | Result | Exact reason |
| --- | --- | --- |
| Single bridge | excluded from this regression | The four-cycle has no contact bridge; the bridge maximum-principle proof still applies when a unique edge exists. |
| Order-reversing diameter matching | retained | The two chords `02` and `13` cross; no star assumption is used. |
| Shared diameter endpoints | not used | The response counterexample uses two disjoint pairs, so it does not rely on a shared-endpoint degeneracy. |
| Contact isolates | irrelevant to the response regression | Pendant trees can be added, but the regression makes no population claim. |
| Regular odd shell | not contradicted | The regression is a network sign example and supplies no global-optimality certificate. |

## 7. Failed routes and no-go result

The failed implication was:

```text
common block separator -> common-bridge voltage lower bound.
```

Its exact failure is the replacement of one forced bridge current by a current split
among multiple block ports. The route is dead under separator topology alone. It may be
revived only with a theorem that uses the actual unit-contact embedding and its affine
KKT equilibrium; the present regression does not rule out such a theorem.

## 8. Literature imported

None.

## 9. Computation and reproducibility

No computation is logically required. The formula is obtained by two-path Ohm-law
calculation and is exact over positive real `a,b,c,d`.

## 10. Canonical promotion recommendation

**Promote regression only.** This report should remain dated working material until a
route-map audit decides whether the multiport sign failure deserves an index entry. No
authoritative theorem module or active prompt was changed.

## 11. Next run

The highest-value next theorem is a multiport common-block inequality that retains the
unit-contact KKT equilibrium and the `s_Z=0` circuit ledger. A useful first restriction
is to classify the block's terminal port order and determine whether its port response
can realize the Woodall caterpillar forest without paying an additional `3d_H` or
loaded-boundary surplus.

## 12. Compact handoff

```text
LEVEL I STATUS: STILL OPEN.

New exact regression:
For a positive weighted 4-cycle with cyclic edge resistances a,b,c,d and cross-pair
incidences e=(2,0), f=(3,1),
    K_ef=(bd-ac)/(a+b+c+d).
The sign can be negative, zero, or positive. Pendant trees preserve the disjoint
cross-transfer. Thus a common 2-edge-connected contact block does not inherit the
single-bridge lower bound K_ef>=1/alpha.

Target effect:
The common-bridge branch is eliminated, but the one-common-block phase survives in both
Woodall topology branches. The missing theorem must use unit-contact KKT geometry or the
exact circuit/forest ledgers; separator topology alone is insufficient.

Authoritative files:
docs/targets/target-c/56-ci-restored-frontier.md
docs/reports/target_c_common_bridge_transfer_exclusion_2026-09-10.md
docs/reports/target_c_woodall_diameter_topology_2026-09-10.md
docs/reports/target_c_sz0_explicit_0597_detour_gap_2026-09-10.md
```
